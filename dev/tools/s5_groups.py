#!/usr/bin/env python3
"""S7 part 2, item 6 (Nov 15, 2026): participants and non-participants, from the batch's studies D (500 adults) and D10 (10,000 adults).

  python3 dev/tools/s5_groups.py [RESULTS_DIR] [--out DIR]

For each environment, income yardstick, raise setting and participation level of the release row (design `rls`, 20 years), reads the two groups' figures
(gPartF0 / gNonF0: share of their adult-years below the cost of living, %; gPartW / gNonW: share with too little wealth at the last year, %) and writes
the group's level with no programme, its level with the programme, and the paired change with a 95% interval. A group is a take-up flag drawn for each
adult, so the same people form it in the no-programme row and in the programme row of a seed: each group is paired against its own no-programme figure.
Intervals as in s5_participation.py: per-seed paired differences, paired bootstrap over seeds, 10,000 replicates, percentile, one resample shared by all rows,
bootstrap seed 20261101. Writes dev/runs/s5-participation/groups.csv, which dev/tools/study_files.py copies into data/studies/s5-groups.json.
Modelling assumption: the flag belongs to the adult, not to the programme level; whether it is drawn identically across rows is read from the no-programme
figures of both groups being close (the engine's grouping, harness.js, is not edited here).
"""
import os, sys, csv, re
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
import batch_load as bl

ENGINE = 'ce8d030'
NB, BSEED = 10000, 20261101
LEVELS = [2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90]
args = [a for a in sys.argv[1:] if not a.startswith('--')]
RES = args[0] if args else '/home/user/bettertobest/compassionism-sim-results'
OUTD = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else os.path.join(os.path.dirname(__file__), '..', 'runs', 's5-participation')
MEAS = [('F0', 'below the cost of living, % of adult-years'), ('W', 'too little wealth at year 20, %')]
GROUPS = [('Part', 'participants'), ('Non', 'non-participants')]


def pct(b): return float(np.percentile(b, 2.5)), float(np.percentile(b, 97.5))


def resample(ns):
    rng = np.random.default_rng(BSEED)
    idx = rng.integers(0, ns, size=(NB, ns))
    W = np.zeros((NB, ns))
    np.add.at(W, (np.repeat(np.arange(NB), ns), idx.ravel()), 1.0 / ns)
    return W


out = []
for study, folder in (('D', 'prog-d-%s' % ENGINE), ('D10', 'prog-d10-%s' % ENGINE)):
    rows, meta = bl.load(os.path.join(RES, folder))
    assert not meta['_problems'] and meta['seedList'] == list(range(1, 501)), meta['_problems']
    W = resample(500)
    for c in sorted({m.group(1) for r in rows for m in [re.match(r'^(.+?)\.none$', r)] if m}):
        env, n, y, _, yard = c.split('.')[:5]
        none = rows[c + '.none']
        for raise_ in ('off', 'on'):
            for q in LEVELS:
                nm = c + ('.main.raise.p%d' if raise_ == 'on' else '.main.p%d') % q
                if nm not in rows: continue
                row = rows[nm]
                for g, gl in GROUPS:
                    for m, ml in MEAS:
                        k = 'g%s%s' % (g, m)
                        d = row[k] - none[k]
                        lo, hi = pct(W @ d)
                        out.append([study, env, int(n[1:]), int(y[1:]), yard, raise_, q, gl, ml, float(np.mean(none[k])), float(np.mean(row[k])),
                                    float(d.mean()), lo, hi, float(np.mean(row['jnP19']))])
os.makedirs(OUTD, exist_ok=True)
with open(os.path.join(OUTD, 'groups.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['study', 'env', 'adults', 'years', 'yardstick', 'raise', 'level_pct', 'group', 'measure', 'none', 'programme', 'change', 'lo95', 'hi95', 'realised_participation_pct'])
    for r in out: w.writerow(r[:9] + ['%.4f' % x for x in r[9:]])
print('wrote %d rows' % len(out))
