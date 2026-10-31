#!/usr/bin/env python3
"""S6 C2.2 coverage and adequacy: the pilot's tables (dev/reports/c22-coverage-adequacy.md), from one results folder.

Usage: python3 dev/tools/c22_pilot.py <results folder, e.g. compassionism-sim-results/pilot-k-ENGINE> <out dir> [<earlier run folder>]
With an earlier run (preregistration amendment 1): checks that every kept measure but c22PY is identical, seed by seed, and says how c22PY moved.
Writes <out dir>/tables.md and <out dir>/estimates.csv. Pilot figures (labelled pilot), not headline figures.

Method (research-update prereg/2026-11-c22-coverage-adequacy.md, Analysis): per-seed paired differences, averaged over seeds;
95% percentile intervals from a paired bootstrap over seeds, 10,000 replicates, random seed 20261101, one resample of seed
indices shared by every row (so every contrast is paired). Contrasts: (a) row minus none; (b) row minus main; (c) the adults
left out by status in a row minus the same adults in the none row with the same draw (none for 4.1%, none.el56 for 5.6%).
For outcomes that are shares of people below a line, (a) and (b) are written as reductions: positive is better.
"""
import csv, glob, json, os, sys
import numpy as np

SRC, OUT = sys.argv[1], sys.argv[2]
OLD = sys.argv[3] if len(sys.argv) > 3 else None
NB, BSEED = 10000, 20261101
ENVS = [('ref', 'Reference'), ('adv', 'Adverse'), ('st', 'Stress')]
YARDS = [('cps', 'CPS earnings (headline)'), ('rel', 'released wages')]
ROWS = ['main', 'el', 'el56', 'auto', 'act', 'bu1500', 'needs.fixed', 'needs', 'c22', 'c22.act', 'c22.cb50']
RLAB = {'main': 'release row (opt-in, all eligible, $1,200)', 'el': 'status rule 4.1%', 'el56': 'status rule 5.6%',
        'auto': 'automatic, all eligible', 'act': 'the Act as written (automatic, status rule 4.1%)', 'bu1500': 'BU $1,500',
        'needs.fixed': 'BU at needs level, indexed as released', 'needs': 'BU at needs level, needs-indexed',
        'c22': 'C2.2 design (automatic, all, needs level, needs-indexed)', 'c22.act': 'C2.2 design with the status rule 4.1%',
        'c22.cb50': 'C2.2 design, child allowance half'}
# (label, key per horizon, kind): red = reduction in points (positive better), diff = row minus none, infl = points of cumulative inflation
PRI = [('Below 30 days of basic living, design-neutral (% adult-years)', {20: 'bNAPy', 40: 'bNAPy'}, 'red'),
       ('Below the cost of living (% adult-years)', {20: 'fgt0PY', 40: 'fgt0PY'}, 'red'),
       ('Too little wealth at the end (% adults)', {20: 'ppov_19', 40: 'ppov_39'}, 'red'),
       ('Programme cost ($ per adult-year)', {20: 'cost', 40: 'cost'}, 'diff'),
       ('Cumulative inflation (% to the last year)', {20: 'plv_19', 40: 'plv_39'}, 'infl'),
       ('Children below the cost of living (% child-years)', {20: 'hhCostKidPY', 40: 'hhCostKidPY'}, 'red')]
LEVELS = [('Adult-years receiving the BU (%)', 'buPY'), ('Adult-years the BU covers the C2.2 needs (%)', 'c22PY'),
          ('Mean share of the C2.2 needs covered (%)', 'c22R'), ('Adults left out by status (%)', 'elN'),
          ('Participation in the last year (%)', 'jnP19')]
LEFT = [('below the cost of living (% of their years)', 'elF0'), ('too little wealth at the end (% of them)', 'elW'),
        ('real resources ($ a year)', 'elRes')]
NON = [('Non-participants below the cost of living (% of their years)', 'gNonF0'), ('Non-participants with too little wealth (%)', 'gNonW')]


def load(src=None):
    rows, seeds, meta = {}, None, None
    for f in sorted(glob.glob(os.path.join(src or SRC, 'shard-*.json'))):
        if f.endswith('.timing.json'):
            continue
        d = json.load(open(f))
        meta = meta or d['_meta']
        lo, hi = d['_meta']['seeds']
        for r, v in d['rows'].items():
            for k, a in v.items():
                rows.setdefault(r, {}).setdefault(k, {})
                for i, x in enumerate(a):
                    rows[r][k][lo + i] = x
    s = sorted(next(iter(next(iter(rows.values())).values())).keys())
    out = {r: {k: np.array([v[k][q] for q in s], dtype=float) for k in v} for r, v in rows.items()}
    return out, s, meta


R, SEEDS, META = load()
N = len(SEEDS)
assert SEEDS == list(range(SEEDS[0], SEEDS[0] + N)), 'seeds are not one contiguous range'
IDX = np.random.default_rng(BSEED).integers(0, N, size=(NB, N))


def est(x):
    m = x[IDX].mean(axis=1)
    return float(x.mean()), float(np.percentile(m, 2.5)), float(np.percentile(m, 97.5))


def val(row, key, kind):
    v = row[key]
    return (v - 1) * 100 if kind == 'infl' else v


def fmt(e, dp=1, money=False):
    m, lo, hi = e
    if money:
        return '%s (%s to %s)' % tuple(format(round(z), ',') for z in (m, lo, hi))
    return '%.*f (%.*f to %.*f)' % (dp, m, dp, lo, dp, hi)


def sig(e):
    return e[1] > 0 or e[2] < 0


CSV, MD = [], []
MD.append('# C2.2 coverage and adequacy: pilot tables (S6)\n')
MD.append('PILOT: seeds %d-%d (%d seeds), 500 adults. Engine %s; command `%s`. Written by `dev/tools/c22_pilot.py`. '
          'Effects on shares below a line are reductions (positive = fewer people below it); 95%% paired bootstrap intervals in brackets.\n'
          % (SEEDS[0], SEEDS[-1], N, META['manifest']['commit'][:7], META['command']))
for yr in (20, 40):
    for y, ylab in YARDS:
        for e, elab in ENVS:
            pre = '%s.n500.y%d.%s.' % (e, yr, y)
            none, main = R[pre + 'none'], R[pre + 'main']
            MD.append('\n## %s, %d years, %s\n' % (elab, yr, ylab))
            # levels
            MD.append('\n### Coverage and adequacy (levels)\n\n| Row | ' + ' | '.join(l for l, _ in LEVELS) + ' |\n|' + '---|' * (len(LEVELS) + 1))
            for r in ROWS:
                x = R[pre + r]
                cells = []
                for l, k in LEVELS:
                    q = est(x[k]); cells.append(fmt(q)); CSV.append([e, yr, y, r, 'level', k, *q])
                MD.append('| %s | %s |' % (RLAB[r], ' | '.join(cells)))
            # effects against none
            MD.append('\n### Effects against no programme (a)\n\n| Row | ' + ' | '.join(l for l, _, _ in PRI) + ' |\n|' + '---|' * (len(PRI) + 1))
            for r in ROWS:
                x = R[pre + r]; cells = []
                for l, kk, kind in PRI:
                    k = kk[yr]; d = val(x, k, kind) - val(none, k, kind)
                    if kind == 'red':
                        d = -d
                    q = est(d); cells.append(fmt(q, 0 if kind == 'diff' else 1, kind == 'diff') + ('' if sig(q) else ' ns'))
                    CSV.append([e, yr, y, r, 'vs none', k, *q])
                MD.append('| %s | %s |' % (RLAB[r], ' | '.join(cells)))
            # effects against main
            MD.append('\n### Each option against the release row (b)\n\n| Row | ' + ' | '.join(l for l, _, _ in PRI) + ' | label (rule 4) |\n|' + '---|' * (len(PRI) + 2))
            for r in ROWS[1:]:
                x = R[pre + r]; cells = []; q2 = {}
                for l, kk, kind in PRI:
                    k = kk[yr]; d = val(x, k, kind) - val(main, k, kind)
                    if kind == 'red':
                        d = -d
                    q = est(d); q2[k] = q; cells.append(fmt(q, 0 if kind == 'diff' else 1, kind == 'diff') + ('' if sig(q) else ' ns'))
                    CSV.append([e, yr, y, r, 'vs main', k, *q])
                f0, w = q2['fgt0PY'], q2[PRI[2][1][yr]]
                lab = 'better' if f0[1] > 0 and w[1] > 0 else 'worse' if f0[2] < 0 or w[2] < 0 else 'mixed'
                MD.append('| %s | %s | %s |' % (RLAB[r], ' | '.join(cells), lab))
            # left out by status, against the same adults with no programme
            MD.append('\n### Adults left out by status, against the same adults with no programme (c; positive = worse off with the programme)\n\n| Row | '
                      + ' | '.join(l for l, _ in LEFT) + ' |\n|' + '---|' * (len(LEFT) + 1))
            for r in ('el', 'el56', 'act', 'c22.act'):
                x, b = R[pre + r], R[pre + ('none.el56' if r == 'el56' else 'none')]
                cells = []
                for l, k in LEFT:
                    q = est(x[k] - b[k]); cells.append(fmt(q, 0 if k == 'elRes' else 1, k == 'elRes') + ('' if sig(q) else ' ns'))
                    CSV.append([e, yr, y, r, 'left out vs none', k, *q])
                MD.append('| %s | %s |' % (RLAB[r], ' | '.join(cells)))
            MD.append('\n### Non-participants (levels; the release row and the opt-in rows)\n\n| Row | ' + ' | '.join(l for l, _ in NON) + ' |\n|' + '---|' * (len(NON) + 1))
            for r in ('main', 'el', 'bu1500', 'needs'):
                x = R[pre + r]; cells = []
                for l, k in NON:
                    q = est(x[k]); cells.append(fmt(q)); CSV.append([e, yr, y, r, 'level', k, *q])
                MD.append('| %s | %s |' % (RLAB[r], ' | '.join(cells)))
if OLD:
    R0, S0, M0 = load(OLD)
    assert S0 == SEEDS and set(R0) == set(R), 'the two runs differ in seeds or rows'
    diff = sorted({k for r in R for k in R[r] if k != 'c22PY' and not np.array_equal(R[r][k], R0[r][k])})
    moved = sorted({r.split('.', 4)[-1] for r in R if not np.array_equal(R[r]['c22PY'], R0[r]['c22PY'])})
    MD.insert(2, '\nAmendment 1 check against %s (engine %s): every kept measure but c22PY identical seed by seed: %s. c22PY moved in rows: %s.\n'
              % (os.path.basename(OLD.rstrip('/')), M0['manifest']['commit'][:7], 'yes' if not diff else 'NO, differs on ' + ', '.join(diff), ', '.join(moved) or 'none'))
    print('amendment 1 check: identical but c22PY' if not diff else 'amendment 1 check FAILED: ' + ', '.join(diff), '| c22PY moved in', moved)
os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, 'tables.md'), 'w').write('\n'.join(MD) + '\n')
with open(os.path.join(OUT, 'estimates.csv'), 'w', newline='') as fh:
    w = csv.writer(fh); w.writerow(['env', 'years', 'yardstick', 'row', 'contrast', 'key', 'mean', 'lo95', 'hi95']); w.writerows(CSV)
print('wrote %s (%d estimates, %d seeds)' % (OUT, len(CSV), N))
