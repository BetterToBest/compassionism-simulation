#!/usr/bin/env python3
"""No-figure-changed test for wording passes (ledger step s147).

  python3 dev/tools/no_figure_change.py snapshot OUT.json     record the figures and the numbers in every page, data file and report
  python3 dev/tools/no_figure_change.py compare BEFORE.json AFTER.json   exit 1 unless the two agree

A wording pass may change words but no number. The snapshot holds:
  engine   SHA-256 of harness.js, of the engine harness.js reads out of index.html, and of index.html's other script blocks
           (the page-drawing code around the engine may change its words, but the count of every number in it is compared)
  numeric  for each data/*.json file, SHA-256 of every numeric value with its path (not the words)
  tokens   for each page, report, data file and site script, how many times each number appears in the words
           (a file that exists on only one side is listed, not compared: a new report has no 'before')
A comparison fails if the engine hashes or numeric hashes differ (a data file that is new in AFTER is listed, not compared; a removed one fails).
Session 13: a data file may gain new numbers (a new figure, a new block) without any old number moving. The snapshot also holds one hash per chunk of each data file
(the first two parts of a number's path; a list of items that carry an "id" is keyed by it, so adding an item shifts nothing). When a file's whole hash differs, every
chunk of BEFORE must still be there with the same hash; chunks only in AFTER are listed as ADDED and fail unless named in the allow file as 'file<TAB>added<TAB>chunk'. A changed token count is listed; it fails too unless
the line is named in dev/tools/no_figure_change_allow.txt (one 'file<TAB>token<TAB>delta' per line, each with a reason in
the report), so every number that moves in the words is looked at by a person.
"""
import fnmatch, glob, hashlib, json, os, re, subprocess, sys
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
NUM = re.compile(r'\d[\d,]*(?:\.\d+)?')
# HANDOFF.md is left out (session 7): the session log, rewritten every session; it publishes no figure.
TEXT_FILES = (['index.html', 'findings.html', 'study.html', 'suite.html', 'replication.html', 'earlier-engine.html'] + sorted(f for f in glob.glob('*.md') if f != 'HANDOFF.md') +
              sorted(glob.glob('dev/reports/*.md')) + sorted(glob.glob('site/*.js')) + sorted(glob.glob('.github/ISSUE_TEMPLATE/*.yml')))


def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode()).hexdigest()


def leaves(o, p=''):
    if isinstance(o, dict):
        for k in sorted(o):
            yield from leaves(o[k], p + '.' + k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from leaves(v, p + '[%d]' % i)
    else:
        yield p, o


def chunk_of(path_parts):
    return '.'.join(path_parts[:2])


def leaves_keyed(o, parts=()):
    """like leaves(), but a list item that is a dict with an 'id' is keyed by it, and the path is a tuple of parts"""
    if isinstance(o, dict):
        for k in sorted(o):
            yield from leaves_keyed(o[k], parts + (k,))
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from leaves_keyed(v, parts + ((str(v['id']) if isinstance(v, dict) and 'id' in v else '[%d]' % i),))
    else:
        yield parts, o


def words_of(path, text):
    if path.endswith('.html'):
        text = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', text, flags=re.S)
        text = re.sub(r'<[^>]+>', ' ', text)
    return text


def tokens(text):
    return Counter(t.rstrip(',') for t in NUM.findall(text))


def snapshot():
    S = {'engine': {}, 'numeric': {}, 'chunks': {}, 'tokens': {}}
    S['engine']['harness.js'] = sha(open(os.path.join(ROOT, 'harness.js'), 'rb').read())
    idx = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
    # Session 7 (Oct 14): the engine is what harness.js runs, cut out of index.html by its own csEngineSource; it must not change by one byte.
    # The rest of the page's main script draws the page: its words may change (wording passes), but no number in it may (counted under tokens).
    # Every other script block (the embedded release panels, the structured data) is hashed whole.
    eng = subprocess.run(['node', '-e', "const fs=require('fs'),H=require('./harness.js');process.stdout.write(H.csEngineSource(fs.readFileSync('index.html','utf8')))"],
                         cwd=ROOT, capture_output=True, check=True).stdout
    S['engine']['index.html engine (what harness.js runs)'] = sha(eng)
    blocks = re.findall(r'<script[^>]*>(.*?)</script>', idx, flags=re.S)
    main = max(blocks, key=len)
    S['engine']['index.html other script blocks'] = sha('\n'.join(b for b in blocks if b is not main))
    S['tokens']['index.html page code (numbers in the main script)'] = dict(tokens(main))
    for f in sorted(glob.glob(os.path.join(ROOT, 'data', '**', '*.json'), recursive=True)):
        rel = os.path.relpath(f, ROOT)
        j = json.load(open(f, encoding='utf-8'))
        nums = [(p, v) for p, v in leaves(j) if isinstance(v, (int, float)) and not isinstance(v, bool)]
        S['numeric'][rel] = sha(json.dumps(nums))
        ch = {}
        for ps, v in leaves_keyed(j):
            if isinstance(v, (int, float)) and not isinstance(v, bool):
                ch.setdefault(chunk_of(ps), []).append(('.'.join(ps), v))
        S['chunks'][rel] = {c: sha(json.dumps(x)) for c, x in ch.items()}
        strs = ' '.join(v for p, v in leaves(j) if isinstance(v, str))
        S['tokens'][rel] = dict(tokens(strs))
    for rel in TEXT_FILES:
        f = os.path.join(ROOT, rel)
        if os.path.exists(f):
            S['tokens'][rel] = dict(tokens(words_of(rel, open(f, encoding='utf-8', errors='replace').read())))
    return S


def compare(a, b):
    bad = []
    allow = set()
    ap = os.path.join(ROOT, 'dev', 'tools', 'no_figure_change_allow.txt')
    if os.path.exists(ap):
        allow = {l.rstrip('\n') for l in open(ap) if l.strip() and not l.startswith('#')}
    for sec in ('engine', 'numeric'):
        for k in sorted(set(a[sec]) | set(b[sec])):
            if sec == 'numeric' and k not in a[sec]:  # session 11: a new data file has no 'before'; it is listed, and its numbers are checked where it is made
                print('new file  %s (numbers not compared: no counterpart)' % k)
                continue
            if a[sec].get(k) != b[sec].get(k):
                if sec == 'numeric' and k in a.get('chunks', {}) and k in b.get('chunks', {}):  # session 13: no old number may move; new ones are listed
                    ca_, cb_ = a['chunks'][k], b['chunks'][k]
                    changed = [c for c in ca_ if cb_.get(c) != ca_[c]]
                    added = [c for c in cb_ if c not in ca_]
                    for c in changed:
                        bad.append('numeric differs: %s (%s)' % (k, c))
                    for c in added:
                        line = '%s\tadded\t%s' % (k, c)
                        ok = any(fnmatch.fnmatchcase(line, p) for p in allow if '\tadded\t' in p)  # an allow line may end in a wildcard pattern
                        print(('allowed  ' if ok else 'ADDED    ') + line)
                        if not ok:
                            bad.append('numbers added: %s %s' % (k, c))
                    if not changed and not added:
                        bad.append('%s differs: %s' % (sec, k))
                else:
                    bad.append('%s differs: %s' % (sec, k))
    moved = []
    for k in sorted(set(a['tokens']) | set(b['tokens'])):
        if k not in a['tokens'] or k not in b['tokens']:
            print('%s  %s (not compared: no counterpart)' % ('new file' if k in b['tokens'] else 'removed ', k))
            continue
        ca, cb = Counter(a['tokens'].get(k, {})), Counter(b['tokens'].get(k, {}))
        for t in sorted(set(ca) | set(cb)):
            if ca[t] != cb[t]:
                line = '%s\t%s\t%+d' % (k, t, cb[t] - ca[t])
                moved.append((line, line in allow))
    for line, ok in moved:
        print(('allowed  ' if ok else 'MOVED    ') + line)
        if not ok:
            bad.append('number count moved: ' + line.replace('\t', ' '))
    for m in bad:
        print('FAIL', m)
    n_files = len(a['tokens'])
    print('%s: %d engine hashes, %d data files, %d files with number counts compared; %d moved numbers (%d allowed)' % (
        'FAIL' if bad else 'PASS', len(a['engine']), len(a['numeric']), n_files, len(moved), sum(1 for _, ok in moved if ok)))
    return 1 if bad else 0


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == 'snapshot':
        json.dump(snapshot(), open(sys.argv[2], 'w'), sort_keys=True)
        print('wrote', sys.argv[2])
    elif len(sys.argv) == 4 and sys.argv[1] == 'compare':
        sys.exit(compare(json.load(open(sys.argv[2])), json.load(open(sys.argv[3]))))
    else:
        print(__doc__)
        sys.exit(2)
