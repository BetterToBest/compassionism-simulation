#!/usr/bin/env python3
"""S76: the central-bank study's page data (data/studies/s74-cb.json) from its per-seed results.

Reads the 100-seed rerun of S74 (research-update prereg/2026-11-s74-central-bank.md, Amendment 4: run with the release's global settings, so its
"no central bank" arm is release 2's main row on seeds 1-100) and writes one columnar file in the format of the round-2 study files: for each design,
environment and central-bank arm, each outcome's mean in the no-programme run and the programme run, and the programme's effect with a 95% interval
(paired seeds: mean of the per-seed differences +/- 1.96 standard errors). A second table gives the central bank's own effect (the rule against no
central bank, same seeds) in each run. Nothing is typed: every number comes from the results folder.

Usage: python3 dev/tools/s76_cb_data.py RESULTS_DIR [--check-r2=R2_DIR]
  RESULTS_DIR  the folder with s74-pilot-ref.json, -adv, -st, -hx (compassionism-sim-results s74-final-<commit>)
  --check-r2   a folder holding r2-m-<env>-20-104691f/shard-0000.json.gz: the "no central bank" arm must equal release 2's main row per seed
               (Amendment 4's condition); the script stops if it does not.
  --r2-engine=E7  the part M folders' engine for --check-r2 (default 104691f); S93 part 3 (Nov 23, 2026), the check against the release rerun
  --check-only    stop after the check (writes nothing)
"""
import gzip, json, math, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ENVS = [('ref', 'Reference'), ('adv', 'Adverse'), ('st', 'Stress'), ('hx', 'History 2005-2025')]
DESIGNS = [('c22', 'C2.2'), ('rel', 'release design')]
ARMS = {'none': 'no central bank', 'cb': 'the policy-rate rule', 'actual': 'the actual rate path'}
OUT = [  # key, label, scale
    ('bNAPy', 'basic living (adult-years below 30 days, points)', 1),
    ('fgt0PY', 'cost of living (basket poverty, adult-years, points)', 1),
    ('hhCostKidPY', 'children below the cost of living (child-years, points)', 1),
    ('ppovA', 'wealth poverty, yearly average (points)', 1),
    ('wtMedE', 'median real wealth (year-0 $)', 1),
    ('endoAnn', 'programme inflation (points a year)', 100),
    ('stP5', 'pushed below the basket line in a recession year (%)', 1),
    ('stP3', 'largest fall in real wealth (year-0 $, median adult)', 1),
    ('stP1', 'spread of the basket price level\'s yearly change (points)', 1),
    ('wtT1E', 'top 1% share of net worth at the end (%)', 1),
    ('wtB50E', 'bottom half\'s share of net worth at the end (%)', 1),
    ('fsN', 'adult-years with a forced sale (%)', 1),
]


def ppovA(r, n):
    ks = [r['ppov_%d' % t] for t in range(n) if ('ppov_%d' % t) in r]
    return [sum(v[j] for v in ks) / len(ks) for j in range(len(ks[0]))]


def series(r, k, n, scale):
    if k == 'ppovA': return ppovA(r, n)
    if k not in r: return None
    return [x * scale for x in r[k]]


def stats(a, b=None):
    d = a if b is None else [y - x for x, y in zip(a, b)]
    n = len(d); m = sum(d) / n; sd = math.sqrt(sum((x - m) ** 2 for x in d) / (n - 1)) if n > 1 else 0
    se = sd / math.sqrt(n); return m, m - 1.96 * se, m + 1.96 * se


def rnd(x, k=6):
    return None if x is None else float('%.*g' % (k + 3, x))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args: print(__doc__); sys.exit(1)
    rdir = args[0]; chk = [a.split('=', 1)[1] for a in sys.argv[1:] if a.startswith('--check-r2=')]
    r2e = ([a.split('=', 1)[1] for a in sys.argv[1:] if a.startswith('--r2-engine=')] or ['104691f'])[0]
    files = {e: json.load(open(os.path.join(rdir, 's74-pilot-%s.json' % e))) for e, _ in ENVS}
    man = files['ref']['_meta']['manifest']
    for e, f in files.items():
        if f['_meta']['manifest']['commit'] != man['commit'] or f['_meta']['manifest'].get('dirty'): sys.exit('%s: commit differs or tree dirty' % e)
    if chk:  # Amendment 4: the no-central-bank arm is release 2's main row on seeds 1-100
        bad = []
        for e, re_ in [('ref', 'ref'), ('adv', 'adv'), ('st', 'str')]:
            R = json.load(gzip.open(os.path.join(chk[0], 'r2-m-%s-20-%s' % (re_, r2e), 'shard-0000.json.gz')))['rows']
            for d, _ in DESIGNS:
                for i, row in ((0, 'none'), (1, d)):
                    for k in ('fgt0PY', 'pov', 'wtMedE', 'bNAPy'):
                        a = files[e][d]['off'][i][k]; b = R['%s.%s' % (re_, row)][k][:len(a)]
                        if any(abs(x - y) > 1e-9 * max(1, abs(y)) for x, y in zip(a, b)): bad.append('%s %s %s %s' % (e, d, row, k))
        if bad: sys.exit('the no-central-bank arm does not equal release 2: ' + '; '.join(bad[:6]))
        print('check: the no-central-bank arm equals the main row of r2-m-*-20-%s per seed (Reference, Adverse, Stress; both designs; both runs; 4 keys)' % r2e)
    if '--check-only' in sys.argv: return
    cols = ['design', 'environment', 'central bank', 'outcome', 'no programme', 'programme', 'effect', 'lo95', 'hi95']
    cbc = ['design', 'environment', 'run', 'outcome', 'without the rule', 'with the rule', 'change', 'lo95', 'hi95']
    rows, cbr = [], []
    for e, en in ENVS:
        f = files[e]; n = 21 if e == 'hx' else 20
        for d, dn in DESIGNS:
            arms = {'none': f[d]['infl' if e == 'hx' else 'off'], 'cb': f[d]['cb']}
            if e == 'hx': arms['actual'] = f[d]['actual']
            for a, A in arms.items():
                for k, lab, sc in OUT:
                    x, y = series(A[0], k, n, sc), series(A[1], k, n, sc)
                    if x is None or y is None: continue
                    m, lo, hi = stats(x, y)
                    rows.append([dn, en, ARMS[a], lab, rnd(sum(x) / len(x)), rnd(sum(y) / len(y)), rnd(m), rnd(lo), rnd(hi)])
            for i, run in ((0, 'no programme'), (1, 'programme')):
                for k, lab, sc in OUT:
                    x, y = series(arms['none'][i], k, n, sc), series(arms['cb'][i], k, n, sc)
                    if x is None or y is None: continue
                    m, lo, hi = stats(x, y)
                    cbr.append([dn, en, run, lab, rnd(sum(x) / len(x)), rnd(sum(y) / len(y)), rnd(m), rnd(lo), rnd(hi)])
    folder = os.path.basename(os.path.normpath(rdir))
    out = {'meta': {'id': 's74-cb', 'title': 'The central bank in both runs (S74): the main row with and without a policy-rate rule, both designs, four environments',
                    'prereg': 'prereg/2026-11-s74-central-bank.md (research-update; Amendments 1-4)', 'report': 'dev/reports/s74-central-bank.md',
                    'engine': man['commit'][:7], 'seeds': len(files['ref']['c22']['off'][0]['fgt0PY']),
                    'rows': 'release 2\'s main row (r2FreezePair, full backing) with the release\'s global settings; arms: no central bank, the policy-rate rule (cb, forced sales on); History also the actual rate path',
                    'resultsFolder': folder, 'resultsRepo': 'BetterToBest/compassionism-sim-results',
                    'command': 'python3 dev/tools/s76_cb_data.py ' + folder + ' --check-r2=<folder with r2-m-*-20-104691f>',
                    'intervals': '95% intervals over paired seeds (mean of the per-seed differences, +/- 1.96 standard errors); the model\'s randomness only',
                    'n': len(rows)},
           'columns': cols, 'data': [list(c) for c in zip(*rows)],
           'cb': {'columns': cbc, 'data': [list(c) for c in zip(*cbr)]}}
    p = os.path.join(ROOT, 'data', 'studies', 's74-cb.json')
    with open(p, 'w') as fh: json.dump(out, fh, ensure_ascii=False, separators=(',', ':'))
    print('wrote %s: %d effect rows, %d central-bank rows (engine %s, %d seeds)' % (os.path.relpath(p, ROOT), len(rows), len(cbr), out['meta']['engine'], out['meta']['seeds']))


if __name__ == '__main__':
    main()
