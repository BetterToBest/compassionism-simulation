#!/usr/bin/env python3
"""S5 (Nov 8, 2026): the participation figure, from the batch's studies D (500 adults) and D10 (10,000 adults).

  python3 dev/tools/s5_participation.py [RESULTS_DIR] [--out DIR]

Reads prog-d-<engine> and prog-d10-<engine> from the results repository, applies prereg/2026-11-study-program.md decision rule 5:
the figure is the lowest level in the grid at which the release row's effect on all three of outcomes 1-3 (design-neutral basic living,
bNAPy; below the cost of living, fgt0PY; too little wealth at the last year, ppov_19 / ppov_39) has a 95% interval that excludes zero in
the favourable direction. Reference, CPS yardstick, raise off is the headline cell; every other cell is reported beside it.
Estimates: per-seed paired differences from the none row, averaged; paired bootstrap over seeds, 10,000 replicates, percentile intervals,
one resample shared by every row of a study, bootstrap seed 20261101. Straight-line departure at level q: effect(q) - q/90 * effect(90).
Writes estimates.csv and tables.md; prints the checks (exit 1 on failure). No random draw other than the bootstrap.
"""
import os, sys, csv, re
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
import batch_load as bl

ENGINE = 'ce8d030'
NB, BSEED = 10000, 20261101
LEVELS = [2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90]
ENVN = {'ref': 'Reference', 'adv': 'Adverse', 'st': 'Stress'}
YARDN = {'cps': 'CPS earnings', 'rel': 'as released'}
# (key at 20 years, key at 40 years, label, kind); a reduction is a positive number for outcomes 1-3
OUT = [('bNAPy', 'bNAPy', 'below 30 days of basic living (design-neutral)', 'red'),
       ('fgt0PY', 'fgt0PY', 'below the cost of living', 'red'),
       ('ppov_19', 'ppov_39', 'too little wealth at the last year', 'red'),
       ('cost', 'cost', 'cost per adult-year ($)', 'diff'),
       ('endoAnn', 'endoAnn', 'inflation, % a year (programme minus none)', 'diff'),
       ('jnP19', 'jnP39', 'realised participation at the last year (%)', 'level')]
args = [a for a in sys.argv[1:] if not a.startswith('--')]
RES = args[0] if args else '/home/user/compassionism-sim-results'
OUTD = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else os.path.join(os.path.dirname(__file__), '..', 'runs', 's5-participation')
os.makedirs(OUTD, exist_ok=True)
fails = []


def chk(ok, text):
    print(('ok   ' if ok else 'FAIL ') + text)
    if not ok: fails.append(text)


def pct(b): return float(np.percentile(b, 2.5)), float(np.percentile(b, 97.5))


def resample(ns):
    rng = np.random.default_rng(BSEED)
    idx = rng.integers(0, ns, size=(NB, ns))
    W = np.zeros((NB, ns))
    np.add.at(W, (np.repeat(np.arange(NB), ns), idx.ravel()), 1.0 / ns)
    return W


def key(k, y):  # last-year key for a 40-year row
    return k


def eff(rows, pre, lvl, raise_, k, kind, none):
    r = rows[pre + ('main.raise.p%d' if raise_ else 'main.p%d') % lvl]
    v = r[k]
    return v if kind == 'level' else (none[k] - v if kind == 'red' else v - none[k])


est = []   # dict rows
for study, folder, ns_expected in (('D', 'prog-d-%s' % ENGINE, 500), ('D10', 'prog-d10-%s' % ENGINE, 500)):
    rows, meta = bl.load(os.path.join(RES, folder))
    chk(not meta['_problems'] and len(meta['seedList']) == ns_expected and meta['seedList'] == list(range(1, ns_expected + 1)),
        '%s: seeds 1-%d contiguous, one engine commit, rows complete' % (study, ns_expected))
    chk(all(str(meta.get('engine') or meta.get('manifest', {}).get('commit', '')).startswith(ENGINE) or ENGINE in str(meta) for _ in [0]),
        '%s: engine commit %s recorded' % (study, ENGINE))
    W = resample(len(meta['seedList']))
    for r in rows:
        pass
    cells = sorted({m.group(1) for r in rows for m in [re.match(r'^(.+?)\.none$', r)] if m})
    for c in cells:  # c = ENV.nN.yY.rls.YARD
        env, n, y = c.split('.')[:3]
        T = int(y[1:]); N = int(n[1:]); yard = c.split('.')[4]
        none = rows[c + '.none']
        for raise_ in ([False, True] if study == 'D' else [False]):
            E = {}
            for (k20, k40, lab, kind) in OUT:
                k = k20 if T == 20 else k40
                if k not in none: continue
                E[k20] = {}
                for q in LEVELS:
                    nm = c + ('.main.raise.p%d' if raise_ else '.main.p%d') % q
                    if nm not in rows: continue
                    row = rows[nm]
                    d = row[k] if kind == 'level' else (none[k] - row[k] if kind == 'red' else row[k] - none[k])
                    if kind == 'diff' and k == 'endoAnn': d = row[k] - none[k]
                    E[k20][q] = d
                for q in E[k20]:
                    d = E[k20][q]
                    b = W @ d
                    lo, hi = pct(b)
                    dep = None
                    if q != 90 and 90 in E[k20]:
                        dd = d - q / 90.0 * E[k20][90]
                        dep = (float(dd.mean()), *pct(W @ dd))
                    est.append(dict(study=study, env=env, adults=N, years=T, yard=yard, raise_='on' if raise_ else 'off', outcome=k20, label=lab,
                                    level=q, mean=float(d.mean()), lo=lo, hi=hi,
                                    dep=dep[0] if dep else '', dep_lo=dep[1] if dep else '', dep_hi=dep[2] if dep else ''))

with open(os.path.join(OUTD, 'estimates.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['study', 'env', 'adults', 'years', 'yardstick', 'raise', 'outcome', 'level_pct', 'estimate', 'lo95', 'hi95', 'departure_from_line', 'dep_lo95', 'dep_hi95'])
    for e in est:
        w.writerow([e['study'], e['env'], e['adults'], e['years'], e['yard'], e['raise_'], e['outcome'], e['level'],
                    '%.4f' % e['mean'], '%.4f' % e['lo'], '%.4f' % e['hi'],
                    '' if e['dep'] == '' else '%.4f' % e['dep'], '' if e['dep'] == '' else '%.4f' % e['dep_lo'], '' if e['dep'] == '' else '%.4f' % e['dep_hi']])

# ---- the figure: lowest level where all of outcomes 1-3 have intervals excluding zero (favourable = positive)
def get(study, env, N, T, yard, rz, o, q):
    for e in est:
        if (e['study'], e['env'], e['adults'], e['years'], e['yard'], e['raise_'], e['outcome'], e['level']) == (study, env, N, T, yard, rz, o, q): return e
fig = {}
cellsall = sorted({(e['study'], e['env'], e['adults'], e['years'], e['yard'], e['raise_']) for e in est})
for c in cellsall:
    ok = {}
    for q in LEVELS:
        es = [get(*c, o, q) for o in ('bNAPy', 'fgt0PY', 'ppov_19')]
        ok[q] = all(e is not None and e['lo'] > 0 for e in es)
    first = next((q for q in LEVELS if ok[q]), None)
    # also: does it stay detected at every higher level?
    stays = first is not None and all(ok[q] for q in LEVELS if q >= first)
    last = None
    if first is not None:
        i = LEVELS.index(first)
        while i < len(LEVELS) and ok[LEVELS[i]]: last = LEVELS[i]; i += 1
    fig[c] = (first, stays, ok, last)

# ---- checks
head = ('D', 'ref', 500, 20, 'cps', 'off')
chk(head in fig, 'the headline cell (Reference, 500 adults, 20 years, CPS, raise off) is present')
chk(len(cellsall) == 24 + 3, 'cells: 3 environments x 2 horizons x 2 yardsticks x raise off/on (24) plus D10 in 3 environments')
chk(len(est) == sum(1 for _ in est) and all(np.isfinite(e['mean']) and np.isfinite(e['lo']) for e in est), 'every estimate and interval is finite')
for e in est:
    if e['outcome'] in ('bNAPy', 'fgt0PY', 'ppov_19') and e['study'] == 'D' and e['level'] == 90 and not (e['lo'] <= e['mean'] <= e['hi']):
        chk(False, 'mean inside interval %s' % e); break
else:
    chk(True, 'every mean lies inside its own interval (headline outcomes at 90%)')

# ---- tables
L = []
def p(s=''): L.append(s)
def fm(e, dg=2): return '%.*f [%.*f, %.*f]' % (dg, e['mean'], dg, e['lo'], dg, e['hi'])
p('# S5 participation: tables (generated by dev/tools/s5_participation.py)'); p()
p('Effects are the release row minus the no-programme run, paired by seed (500 seeds, paired bootstrap, 10,000 replicates). Reductions are positive points. Intervals are 95%.'); p()
p('## The figure, every cell'); p()
p('| Study | Environment | Adults | Years | Yardstick | Raise | Lowest level with all of outcomes 1-3 detected | Highest level before any of the three stops being favourable | Detected at every higher level |')
p('|---|---|---|---|---|---|---|---|---|')
for c in cellsall:
    f1, st, _, la = fig[c]
    p('| %s | %s | %s | %d | %s | %s | %s | %s | %s |' % (c[0], ENVN[c[1]], format(c[2], ','), c[3], YARDN[c[4]], c[5], '%d%%' % f1 if f1 else 'none in the grid', '%d%%' % la if la else '-', 'yes' if st else ('no' if f1 else '-')))
p()
for c in [head, ('D10', 'ref', 10000, 20, 'cps', 'off')]:
    p('## Curve: %s, %s adults, %d years, %s yardstick, raise %s' % (ENVN[c[1]], format(c[2], ','), c[3], YARDN[c[4]], c[5])); p()
    p('| Level | Basic living (design-neutral) | Cost of living | Wealth | Cost per adult-year ($) | Inflation (points a year) | Realised participation (%) | Wealth: departure from straight line |')
    p('|---|---|---|---|---|---|---|---|')
    for q in LEVELS:
        g = [get(*c, o, q) for o in ('bNAPy', 'fgt0PY', 'ppov_19', 'cost', 'endoAnn', 'jnP19')]
        if g[0] is None: continue
        w = g[2]
        p('| %d%% | %s | %s | %s | %s | %s | %.1f | %s |' % (q, fm(g[0]), fm(g[1]), fm(g[2]), fm(g[3], 0), fm(g[4], 3), g[5]['mean'],
          ('%.2f [%.2f, %.2f]' % (w['dep'], w['dep_lo'], w['dep_hi'])) if w['dep'] != '' else '(reference level)'))
    p()
open(os.path.join(OUTD, 'tables.md'), 'w').write('\n'.join(L) + '\n')
print('\nFIGURE (headline cell): %s' % (fig[head][0],))
for c in cellsall: print(c, fig[c][0], fig[c][1])
sys.exit(1 if fails else 0)
