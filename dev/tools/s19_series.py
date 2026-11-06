#!/usr/bin/env python3
"""S53 (Nov 2, 2026), for S19: the loader of the per-year poverty series (keys s19<m>_<t>, index.html S19_KEYS; study option sec) that the
public-costs step turns into costs after the full batch, with no new run. Reads a run-study folder or one shard file of any job that records
them (runner/jobs/security.js, and the S47 batch jobs), and returns, for each row, a dict measure -> list over years -> list over seeds.
It checks what S19 relies on: every year present, the same seeds in every row, and, weighted by adults, the yearly basket poverty and FGT1
equal the row's person-year figures (fgt0PY, fgt1PY) where the job records them.

  python3 dev/tools/s19_series.py RESULTS_FOLDER_OR_SHARD [--years N]      (prints the check and, per row, the programme-wide means)

Without --years each row is read to its own horizon (S47: study R holds 20- and 40-year rows in one file).

Measures (per year, all adults unless named): f0 basket poverty %; f1 FGT1 %; gD poverty-gap dollars per adult (year-0 $); gDc the same, each gap
capped at $10,000; dp deep poverty %; hd housing distress %; ep the engine's extreme-poverty (unhoused) estimate %; n adults; f0X basket poverty
of the adults who chose not to take part %. Standard library only."""
import json, os, re, sys, glob, math

M = ['f0', 'f1', 'gD', 'gDc', 'dp', 'hd', 'ep', 'n', 'f0X']


def row_years(r, v):
    """A row's horizon: the `.yNN.` segment of a batch row name (study R runs 20- and 40-year rows in one file, S47), else every year recorded."""
    m = re.search(r'\.y(\d+)\.', r)
    if m: return int(m.group(1))
    t = 0
    while 's19f0_%d' % t in v: t += 1
    return t


def load(path, years=None):
    """years=None: each row to its own horizon (row_years); a number: that many years for every row."""
    files = [path] if path.endswith('.json') else sorted(f for f in glob.glob(os.path.join(path, 'shard-*.json')) if not f.endswith('.timing.json'))
    if not files: sys.exit('no shard files in ' + path)
    D = sorted((json.load(open(f)) for f in files), key=lambda d: d['_meta']['seeds'][0])
    out, extra = {}, {}
    for d in D:
        for r, v in d['rows'].items():
            if 's19f0_0' not in v: continue
            Y = years or row_years(r, v)
            S = out.setdefault(r, {m: [[] for _ in range(Y)] for m in M}); X = extra.setdefault(r, {})
            for m in M:
                for t in range(Y): S[m][t].extend(v.get('s19%s_%d' % (m, t), [None]*len(v['s19f0_0'])))
            for k in ('fgt0PY', 'fgt1PY'):
                if k in v: X.setdefault(k, []).extend(v[k])
    return out, extra


def check(S, X):
    worst, bad = 0.0, []
    seeds = {len(S[r]['f0'][0]) for r in S}
    for r in S:
        Y = len(S[r]['f0'])
        if any(len(S[r][m][t]) != len(S[r]['f0'][0]) or None in S[r][m][t] for m in M for t in range(Y)): bad.append(r); continue
        for k, m in (('fgt0PY', 'f0'), ('fgt1PY', 'f1')):
            if k not in X[r]: continue
            for i, v in enumerate(X[r][k]):
                n = sum(S[r]['n'][t][i] for t in range(Y)); w = sum(S[r][m][t][i]*S[r]['n'][t][i] for t in range(Y))/n
                worst = max(worst, abs(w - v))
    yrs = sorted({len(S[r]['f0']) for r in S})
    ok = bool(S) and not bad and len(seeds) == 1 and worst < 1e-6
    print(('PASS' if ok else 'FAIL') + '  s19_series.py: %d rows, %s years, %s seeds; adult-weighted yearly f0 and f1 against fgt0PY and fgt1PY: largest difference %.2e%s'
          % (len(S), '/'.join(map(str, yrs)), '/'.join(map(str, sorted(seeds))), worst, ('; incomplete rows: ' + ', '.join(bad[:5])) if bad else ''))
    return ok


def main():
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    years = int(a[a.index('--years') + 1]) if '--years' in a else None
    S, X = load(a[0], years)
    ok = check(S, X)
    for r in sorted(S):
        Y = len(S[r]['f0'])
        mean = lambda m: sum(sum(S[r][m][t]) for t in range(Y))/(Y*len(S[r][m][0]))
        print('  %-24s ' % r + '  '.join('%s %.2f' % (m, mean(m)) for m in M if m != 'n'))
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
