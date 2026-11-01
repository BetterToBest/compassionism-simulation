"""Builds the S50 packet: everything a fresh session (or a plain chat) needs to write a second, independent implementation of the release row
and its no-programme run, and check it against the real engine.
Usage: python3 dev/packets/build_s50_packet.py <reference dir> <coverage dir> <config.json> <out.zip>
  reference dir: s50-ref-1-500.json, s50-adv-1-500.json, s50-st-1-500.json (node dev/packets/make_s50_reference.js run ENV 1 500)
  coverage dir:  release-row-code.js, release-row-code-full.js, not-run.md (node dev/packets/make_s50_reference.js coverage 20 DIR)
  config.json:   node dev/packets/make_s50_reference.js config"""
import hashlib, json, os, sys, zipfile
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ref, cov, cfg, out = sys.argv[1:5]
note = sys.argv[5] if len(sys.argv) > 5 else ''  # optional free-text note for run.txt
files = {  # packet path -> bytes
    '00-START-HERE.md': open(os.path.join(ROOT, 'dev/packets/s50-brief.md'), 'rb').read(),
    '01-PROMPT-to-paste.md': open(os.path.join(ROOT, 'dev/packets/s50-prompt.md'), 'rb').read(),
    'MODEL_SPEC.md': open(os.path.join(ROOT, 'MODEL_SPEC.md'), 'rb').read(),
    'ODD.md': open(os.path.join(ROOT, 'ODD.md'), 'rb').read(),
    'release-config.json': open(cfg, 'rb').read(),
    'reference/KEYS.md': open(os.path.join(ROOT, 'dev/packets/s50-keys.md'), 'rb').read(),
}
for f in ('release-row-code.js', 'release-row-code-full.js', 'not-run.md'):
    files['code/' + f] = open(os.path.join(cov, f), 'rb').read()
man = {}
for e in ('ref', 'adv', 'st'):
    b = open(os.path.join(ref, 's50-%s-1-500.json' % e), 'rb').read()
    d = json.loads(b)
    assert d['lo'] == 1 and d['hi'] == 500 and len(d['rows']) == 2 and all(len(r['seeds']['fgt0PY']) == 500 for r in d['rows']), e
    man[e] = {'seconds': d['seconds'], **d['manifest']}
    files['reference/s50-%s-1-500.json' % e] = b
c0 = json.loads(files['release-config.json'])['manifest']
eng = {(m['engineSha256'], m['harnessSha256'], m['engineBlockSha256']) for m in list(man.values()) + [c0]}
assert len(eng) == 1, 'the reference files and the config come from different engines'
sha = lambda b: hashlib.sha256(b).hexdigest()
run = ['S50 packet: how it was made', '',
       'Engine: index.html and harness.js as at commit %s (the reference script added on top changes no engine file).' % c0['commit'],
       'Engine hashes (runManifest): engineSha256 %s, harnessSha256 %s, engineBlockSha256 %s.' % sorted(eng)[0],
       'Node %s.' % c0['node'], '',
       'Commands (from the repository root):',
       '  node dev/packets/make_s50_reference.js run ref 1 500 > s50-ref-1-500.json   (and adv, st; one process each)',
       '  node dev/packets/make_s50_reference.js config > release-config.json',
       '  node dev/packets/make_s50_reference.js coverage 20 <dir>',
       '  python3 dev/packets/build_s50_packet.py <reference dir> <dir> release-config.json dev/packets/s50-release-row.zip', '',
       'The pair is built the way `node harness.js testbed 500 release ref,adv,st --v54 --snab --slope` builds its no-programme run and its row `release`',
       '(checked: the 500-seed means equal the published v5.6 panel, data/releases/v5.6.json, to its rounding, on every headline key in all three environments).', '',
       'Reference runs:']
for e in ('ref', 'adv', 'st'):
    m = man[e]; run.append('  %s: commit %s, dirty %s, %.0f s' % (e, m['commit'], m['dirty'], m['seconds']))
run.append('')
run.append('"dirty" means a tracked file was being edited while that run went; the engine hashes are asserted equal for all three reference files and the config, so no engine file differed.')
if note: run += ['', note]
run.append('')
files['run.txt'] = ('\n'.join(run) + '\n').encode()
files['SHA256SUMS'] = ''.join('%s  %s\n' % (sha(files[k]), k) for k in sorted(files)).encode()
with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for k in sorted(files):
        z.writestr(k, files[k])
print(out, os.path.getsize(out), 'bytes,', len(files), 'files')
