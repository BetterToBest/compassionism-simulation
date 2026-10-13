#!/usr/bin/env python3
"""No-figure-changed test for wording passes (ledger step s147).

  python3 dev/tools/no_figure_change.py snapshot OUT.json     record the figures and the numbers in every page, data file and report
  python3 dev/tools/no_figure_change.py compare BEFORE.json AFTER.json   exit 1 unless the two agree

A wording pass may change words but no number. The snapshot holds:
  engine   SHA-256 of harness.js and of every <script> block in index.html (the engine is read out of index.html)
  numeric  for each data/*.json file, SHA-256 of every numeric value with its path (not the words)
  tokens   for each page, report, data file and site script, how many times each number appears in the words
           (a file that exists on only one side is listed, not compared: a new report has no 'before')
A comparison fails if the engine hashes or numeric hashes differ. A changed token count is listed; it fails too unless
the line is named in dev/tools/no_figure_change_allow.txt (one 'file<TAB>token<TAB>delta' per line, each with a reason in
the report), so every number that moves in the words is looked at by a person.
"""
import glob, hashlib, json, os, re, sys
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
NUM = re.compile(r'\d[\d,]*(?:\.\d+)?')
TEXT_FILES = (['index.html', 'findings.html', 'study.html', 'replication.html', 'earlier-engine.html'] + sorted(glob.glob('*.md')) +
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


def words_of(path, text):
    if path.endswith('.html'):
        text = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', text, flags=re.S)
        text = re.sub(r'<[^>]+>', ' ', text)
    return text


def tokens(text):
    return Counter(t.rstrip(',') for t in NUM.findall(text))


def snapshot():
    S = {'engine': {}, 'numeric': {}, 'tokens': {}}
    S['engine']['harness.js'] = sha(open(os.path.join(ROOT, 'harness.js'), 'rb').read())
    idx = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
    S['engine']['index.html scripts'] = sha('\n'.join(re.findall(r'<script[^>]*>(.*?)</script>', idx, flags=re.S)))
    for f in sorted(glob.glob(os.path.join(ROOT, 'data', '**', '*.json'), recursive=True)):
        rel = os.path.relpath(f, ROOT)
        j = json.load(open(f, encoding='utf-8'))
        nums = [(p, v) for p, v in leaves(j) if isinstance(v, (int, float)) and not isinstance(v, bool)]
        S['numeric'][rel] = sha(json.dumps(nums))
        strs = ' '.join(v for p, v in leaves(j) if isinstance(v, str))
        S['tokens'][rel] = dict(tokens(strs))
    for rel in TEXT_FILES:
        f = os.path.join(ROOT, rel)
        if os.path.exists(f):
            S['tokens'][rel] = dict(tokens(words_of(rel, open(f, encoding='utf-8', errors='replace').read())))
    return S


def compare(a, b):
    bad = []
    for sec in ('engine', 'numeric'):
        for k in sorted(set(a[sec]) | set(b[sec])):
            if a[sec].get(k) != b[sec].get(k):
                bad.append('%s differs: %s' % (sec, k))
    allow = set()
    ap = os.path.join(ROOT, 'dev', 'tools', 'no_figure_change_allow.txt')
    if os.path.exists(ap):
        allow = {l.rstrip('\n') for l in open(ap) if l.strip() and not l.startswith('#')}
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
