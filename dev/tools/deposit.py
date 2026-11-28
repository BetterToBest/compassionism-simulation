#!/usr/bin/env python3
"""Deposit tool for study results (the results home; replaces the disabled results repository).

A results folder holds the shard files, `run.txt` (the command, engine commit, machine, date) and
`SHA256SUMS` (the SHA-256 of every other file in it). This tool packs a folder into one archive,
checks it, uploads it to a Zenodo record, and keeps `data/results-manifest.json`, the list of what
was deposited, with each file's hash and the record's DOI.

Subcommands (run `python3 dev/tools/deposit.py <name> -h` for each):
  verify  FOLDER                 check the folder against its SHA256SUMS (and run.txt present)
  pack    FOLDER [--out DIR]     verify, then write FOLDER.tar.gz (reproducible: sorted, fixed times)
  entry   ARCHIVE...             read each archive and print its manifest entry (no network)
  add     ARCHIVE... --record ID --doi DOI [--manifest FILE]
                                 merge the entries into the manifest
  upload  --deposition ID ARCHIVE...
                                 upload archives to an open Zenodo draft (token from ZENODO_TOKEN,
                                 or none where the proxy adds it)
  newversion --record ID         open a new draft of a published record (prints the draft's id)
  readme  --record ID --out FILE  write a record's README from the manifest
  scan    [--manifest FILE]      list folder names the published pages, tables and reports cite
  check   [--manifest FILE]      fail if a cited folder is neither deposited nor listed as not deposited

Nothing here publishes a record: publishing is permanent, so it is a separate, deliberate step
(`publish --deposition ID --yes`).
"""
import argparse, glob, gzip, hashlib, io, json, os, re, shutil, subprocess, sys, tarfile, tempfile, time

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MANIFEST = os.path.join(ROOT, 'data', 'results-manifest.json')
ZENODO = 'https://zenodo.org/api'

# A results folder name: study id, optional env/horizon parts, then the engine commit (7 hex digits).
FOLDER_RE = re.compile(r'\b((?:r2|r2dry|s\d{2,3}[a-z]*|pilot|prog|dry|m|x\d|age|lend)(?:-[a-z0-9.]+)*-[0-9a-f]{7})\b')
# Where published figures and their sources are named (reader-visible text and data).
SCAN_GLOBS = ['data/**/*.json', 'dev/reports/*.md', 'REPRODUCE.md', 'README.md', 'CHANGELOG.md', 'ODD.md',
              'MODEL_SPEC.md', 'TESTBED_SPEC.md', 'ECONOMIST-REVIEW.md', '*.html', 'site/**/*.js', 'site/**/*.html']
SKIP_SCAN = {'data/results-manifest.json'}


def sha256_file(p, buf=1 << 22):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(buf), b''):
            h.update(b)
    return h.hexdigest()


def read_sums(path):
    out = {}
    for line in open(path, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line.strip():
            continue
        h, name = line.split(None, 1)
        name = name.lstrip('*').strip()
        out[name] = h
    return out


def verify_folder(folder):
    """Return (problems, sums). A folder passes with no problems."""
    problems = []
    sp = os.path.join(folder, 'SHA256SUMS')
    if not os.path.isfile(sp):
        return ['no SHA256SUMS'], {}
    sums = read_sums(sp)
    if not os.path.isfile(os.path.join(folder, 'run.txt')):
        problems.append('no run.txt')
    present = set()
    for root, _, files in os.walk(folder):
        for fn in files:
            rel = os.path.relpath(os.path.join(root, fn), folder).replace(os.sep, '/')
            present.add(rel)
    for name, h in sums.items():
        p = os.path.join(folder, name)
        if not os.path.isfile(p):
            problems.append('listed but missing: ' + name)
        elif sha256_file(p) != h:
            problems.append('hash differs: ' + name)
    for rel in sorted(present - set(sums) - {'SHA256SUMS'}):
        problems.append('not listed in SHA256SUMS: ' + rel)
    return problems, sums


def pack(folder, outdir):
    folder = os.path.abspath(folder.rstrip('/'))
    name = os.path.basename(folder)
    problems, _ = verify_folder(folder)
    if problems:
        raise SystemExit('refusing to pack %s:\n  %s' % (name, '\n  '.join(problems[:20])))
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, name + '.tar.gz')
    with open(out, 'wb') as raw, gzip.GzipFile(filename='', mode='wb', fileobj=raw, mtime=0, compresslevel=9) as gz:
        with tarfile.open(fileobj=gz, mode='w', format=tarfile.PAX_FORMAT) as tar:
            def norm(ti):
                ti.uid = ti.gid = 0
                ti.uname = ti.gname = ''
                ti.mtime = 0
                ti.mode = 0o755 if ti.isdir() else 0o644
                return ti
            tar.add(folder, arcname=name, recursive=False, filter=norm)
            for root, dirs, files in os.walk(folder):
                dirs.sort()
                for fn in sorted(files):
                    p = os.path.join(root, fn)
                    tar.add(p, arcname=os.path.join(name, os.path.relpath(p, folder)), filter=norm)
                for d in dirs:
                    tar.add(os.path.join(root, d), arcname=os.path.join(name, os.path.relpath(os.path.join(root, d), folder)),
                            recursive=False, filter=norm)
    return out


def entry_from_archive(archive):
    """Build the manifest entry for one archive by reading its SHA256SUMS and run.txt."""
    base = os.path.basename(archive)
    if not base.endswith('.tar.gz'):
        raise SystemExit('not a .tar.gz: ' + archive)
    name = base[:-7]
    with tarfile.open(archive, 'r:gz') as tar:
        members = {m.name: m for m in tar.getmembers() if m.isfile()}
        def get(rel):
            m = members.get(name + '/' + rel)
            return tar.extractfile(m).read() if m else None
        sums_raw, run_raw = get('SHA256SUMS'), get('run.txt')
    e = {'folder': name, 'archive': base, 'archive_sha256': sha256_file(archive), 'archive_bytes': os.path.getsize(archive)}
    if sums_raw is None:
        e['note'] = 'no SHA256SUMS inside (a code archive, not a results folder)'
        return e
    sums = {}
    for line in sums_raw.decode('utf-8').splitlines():
        if line.strip():
            h, n = line.split(None, 1)
            sums[n.lstrip('*').strip()] = h
    e['files'] = sums
    e['sums_sha256'] = hashlib.sha256(sums_raw).hexdigest()   # the folder's fingerprint (as REPRODUCE.md gives)
    run = (run_raw or b'').decode('utf-8', 'replace')
    e['run_txt_sha256'] = hashlib.sha256(run_raw).hexdigest() if run_raw is not None else None
    m = re.search(r'\bengine[: ]+(?:BetterToBest/compassionism-simulation )?([0-9a-f]{40})\b', run)
    e['engine_commit'] = m.group(1) if m else None
    sfx = re.search(r'-([0-9a-f]{7})$', name)
    e['engine_short'] = sfx.group(1) if sfx else None   # the folder name's own commit, where run.txt gives no full hash
    jobs = sorted(set(re.findall(r'\b(?:runner/jobs|dev/tools)/([A-Za-z0-9_-]+\.js)\b', run)))
    e['job'] = jobs[0] if len(jobs) == 1 else (jobs or None)
    seeds = sorted(set(re.findall(r'--seeds=([0-9A-Za-z,-]+)', run)) | set(re.findall(r'seeds (\d+-\d+)', run)))
    e['seeds'] = [x for x in seeds if x not in ('A-B',)] or None
    d = re.search(r'(20\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ|20\d\d-\d\d-\d\d \d\d:\d\d)', run)
    e['run_date'] = d.group(1) if d else None
    return e


def load_manifest(path):
    if os.path.exists(path):
        return json.load(open(path, encoding='utf-8'))
    return {'about': 'Results deposited outside git. One entry per results folder: archive, hashes, engine commit, job, seeds, '
                     'and the record (DOI) that holds it. Written by dev/tools/deposit.py.',
            'records': {}, 'folders': {}, 'cited_not_deposited': {}}


def save_manifest(m, path):
    m['folders'] = dict(sorted(m['folders'].items()))
    m['cited_not_deposited'] = dict(sorted(m['cited_not_deposited'].items()))
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(m, f, indent=1, ensure_ascii=False)
        f.write('\n')


def cmd_add(a):
    m = load_manifest(a.manifest)
    m['records'][a.record] = {'doi': a.doi, 'url': 'https://doi.org/' + a.doi, 'host': 'zenodo', 'status': a.status}
    for ar in a.archives:
        e = entry_from_archive(ar)
        e['record'] = a.record
        if 'files' not in e:
            m.setdefault('code', {})[e['folder']] = e
        else:
            m['folders'][e['folder']] = e
            m['cited_not_deposited'].pop(e['folder'], None)
    save_manifest(m, a.manifest)
    print('manifest now holds %d folders' % len(m['folders']))


def scan():
    cited = {}
    for g in SCAN_GLOBS:
        for p in glob.glob(os.path.join(ROOT, g), recursive=True):
            rel = os.path.relpath(p, ROOT).replace(os.sep, '/')
            if rel in SKIP_SCAN or '/node_modules/' in rel or not os.path.isfile(p):
                continue
            try:
                text = open(p, encoding='utf-8', errors='replace').read()
            except OSError:
                continue
            for f in set(FOLDER_RE.findall(text)):
                cited.setdefault(f, set()).add(rel)
    return cited


def cmd_scan(a):
    cited = scan()
    for f in sorted(cited):
        print(f, len(cited[f]))
    print(len(cited), 'folder names cited', file=sys.stderr)


def cmd_check(a):
    m = load_manifest(a.manifest)
    known = set(m['folders']) | set(m['cited_not_deposited']) | set(m.get('not_folders', {}))
    cited = scan()
    bad = sorted(f for f in cited if f not in known)
    if a.record_missing:
        for f in bad:
            m['cited_not_deposited'][f] = {'cited_in': sorted(cited[f])[:5], 'note': 'named in published text or data; the folder is not in a deposit'}
        save_manifest(m, a.manifest); print('recorded %d cited folders as not deposited' % len(bad)); return 0
    for f in bad:
        print('cited but not in the manifest: %s (in %s)' % (f, ', '.join(sorted(cited[f])[:3])))
    # every deposited entry must carry a record with a DOI and a SHA-256 for each file
    for name, e in m['folders'].items():
        if e.get('record') not in m['records']:
            print('entry without a record:', name); bad.append(name)
        elif not e.get('files') or not e.get('archive_sha256'):
            print('entry without hashes:', name); bad.append(name)
    print('%d folders deposited, %d cited and not deposited, %d names cited on pages and reports'
          % (len(m['folders']), len(m['cited_not_deposited']), len(cited)))
    return 1 if bad else 0


def cmd_readme(a):
    """Write the README for a Zenodo record from the manifest (nothing typed by hand)."""
    m = load_manifest(a.manifest)
    rec = m['records'][a.record]
    rows = sorted(m['folders'].values(), key=lambda e: e['folder'])
    mb = sum(e['archive_bytes'] for e in rows) / 1e6
    L = []
    L.append('# Compassionism Simulation: study results (recovered folders)\n')
    L.append('Results of the Compassionism Simulation studies: one archive per results folder, each with the shard files, '
             '`run.txt` (the exact command, the engine commit, the machine and the date) and `SHA256SUMS` (the SHA-256 of every other file in the folder). '
             'The simulation is at https://github.com/BetterToBest/compassionism-simulation (engine `index.html`, studies `harness.js`); '
             'the findings are at https://bettertobest.github.io/research-hub/.\n')
    L.append('## Where these files come from\n')
    L.append('The results were first published in the GitHub repository BetterToBest/compassionism-sim-results. GitHub disabled that repository on '
             'Nov 26, 2026 (a terms-of-service matter; no reason was given). The files here were recovered from working copies kept by two earlier '
             'working sessions and then checked: every results archive matches the SHA-256 listed in `SHA256SUMS` and `SHA256SUMS-*.txt` in this record (the hash of `runner.tar.gz` is in `results-manifest.json`), and every '
             'folder inside matches its own `SHA256SUMS`. Nothing was edited. The studies are deterministic, so a folder not recovered can be rebuilt '
             'from its engine commit and the command in its `run.txt`.\n')
    L.append('## What is here\n')
    L.append('%d results folders (%.0f MB compressed), listed in `results-manifest.json` with each file\'s SHA-256, the engine commit, the job and the seeds. '
             'Release-engine folders (suffix `-50bc51d`, version 5.9.23) are the data behind the current findings page; folders with other suffixes are earlier '
             'runs kept for comparison. `runner.tar.gz` holds the job scripts (`runner/jobs/*.js`) and the shard checks that produced them.\n' % (len(rows), mb))
    L.append('| Folder | Engine commit | Job | Seeds | Files | MB |')
    L.append('|---|---|---|---|---|---|')
    for e in rows:
        job = e['job'] if isinstance(e['job'], str) else ', '.join(e['job'] or [])
        seeds = ', '.join(e['seeds'] or [])
        L.append('| `%s` | `%s` | %s | %s | %d | %.1f |' % (e['folder'], (e.get('engine_commit') or e.get('engine_short') or '')[:7], job, seeds, len(e['files']), e['archive_bytes'] / 1e6))
    L.append('\n## What is not here\n')
    L.append('%d further folder names are cited in the simulation\'s published pages and reports and are not in this record (`cited_not_deposited` in `results-manifest.json`): '
             'older studies and the small table folders made from the large ones. They are listed so that a missing folder is visible. If one is recovered it will be added as a new version of this record.\n' % len(m['cited_not_deposited']))
    L.append('## Checking a file\n')
    L.append('```\nsha256sum -c SHA256SUMS            # the archives listed there\ntar -xzf <folder>.tar.gz && (cd <folder> && sha256sum -c SHA256SUMS)\n```\n')
    L.append('## Licence and citation\n')
    L.append('Data: CC BY 4.0. Code in the linked repository has its own licence files. Cite this record by its DOI: https://doi.org/%s\n' % rec['doi'])
    open(a.out, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print('wrote', a.out)


def curl_json(method, url, token=None, data=None, extra=()):
    cmd = ['curl', '-sS', '-L', '--retry', '3', '-X', method, url]
    if token:
        cmd += ['-H', 'Authorization: Bearer ' + token]
    if data is not None:
        cmd += ['-H', 'Content-Type: application/json', '--data', json.dumps(data)]
    cmd += list(extra)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit('curl failed: ' + r.stderr[:300])
    try:
        return json.loads(r.stdout) if r.stdout.strip() else {}
    except ValueError:
        raise SystemExit('not JSON from %s: %s' % (url, r.stdout[:300]))


def cmd_upload(a):
    tok = os.environ.get('ZENODO_TOKEN')
    d = curl_json('GET', '%s/deposit/depositions/%s' % (ZENODO, a.deposition), tok)
    if d.get('submitted'):
        raise SystemExit('deposition %s is published; use newversion first' % a.deposition)
    bucket = d['links']['bucket']
    have = {f['filename']: f.get('checksum') for f in d.get('files', [])}
    for ar in a.archives:
        fn = os.path.basename(ar)
        md5 = hashlib.md5(open(ar, 'rb').read()).hexdigest() if os.path.getsize(ar) < (1 << 30) else None
        if fn in have and (md5 is None or have[fn] == md5):
            print('already there:', fn); continue
        print('uploading', fn, os.path.getsize(ar), 'bytes')
        r = curl_json('PUT', '%s/%s' % (bucket, fn), tok, extra=['--upload-file', ar])
        if r.get('checksum', '').replace('md5:', '') and md5 and r['checksum'].replace('md5:', '') != md5:
            raise SystemExit('checksum differs after upload: ' + fn)


def cmd_newversion(a):
    tok = os.environ.get('ZENODO_TOKEN')
    r = curl_json('POST', '%s/deposit/depositions/%s/actions/newversion' % (ZENODO, a.record), tok)
    print(r.get('links', {}).get('latest_draft') or json.dumps(r)[:300])


def cmd_publish(a):
    if not a.yes:
        raise SystemExit('publishing is permanent; pass --yes')
    tok = os.environ.get('ZENODO_TOKEN')
    r = curl_json('POST', '%s/deposit/depositions/%s/actions/publish' % (ZENODO, a.deposition), tok)
    print(r.get('doi') or json.dumps(r)[:300])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest='cmd', required=True)
    s = sp.add_parser('verify'); s.add_argument('folder')
    s = sp.add_parser('pack'); s.add_argument('folder'); s.add_argument('--out', default='.')
    s = sp.add_parser('entry'); s.add_argument('archives', nargs='+')
    s = sp.add_parser('add'); s.add_argument('archives', nargs='+'); s.add_argument('--record', required=True)
    s.add_argument('--doi', required=True); s.add_argument('--status', default='draft'); s.add_argument('--manifest', default=MANIFEST)
    s = sp.add_parser('upload'); s.add_argument('--deposition', required=True); s.add_argument('archives', nargs='+')
    s = sp.add_parser('newversion'); s.add_argument('--record', required=True)
    s = sp.add_parser('publish'); s.add_argument('--deposition', required=True); s.add_argument('--yes', action='store_true')
    s = sp.add_parser('readme'); s.add_argument('--record', required=True); s.add_argument('--out', required=True); s.add_argument('--manifest', default=MANIFEST)
    s = sp.add_parser('scan'); s.add_argument('--manifest', default=MANIFEST)
    s = sp.add_parser('check'); s.add_argument('--manifest', default=MANIFEST)
    s.add_argument('--record-missing', action='store_true', help='write every cited folder not deposited into the manifest (a deliberate act)')
    a = ap.parse_args()
    if a.cmd == 'verify':
        p, s_ = verify_folder(a.folder)
        print('\n'.join(p) if p else 'ok: %d files match SHA256SUMS' % len(s_)); return 1 if p else 0
    if a.cmd == 'pack':
        print(pack(a.folder, a.out)); return 0
    if a.cmd == 'entry':
        for ar in a.archives:
            e = entry_from_archive(ar); e.pop('files', None); print(json.dumps(e, indent=1))
        return 0
    return {'add': cmd_add, 'upload': cmd_upload, 'newversion': cmd_newversion, 'publish': cmd_publish,
            'scan': cmd_scan, 'readme': cmd_readme, 'check': cmd_check}[a.cmd](a) or 0


if __name__ == '__main__':
    sys.exit(main())
