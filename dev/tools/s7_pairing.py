#!/usr/bin/env python3
"""S7 part 2, item 9 (Nov 15, 2026): the observed variance reduction from paired seeds, measured on study D (500 adults, 500 seeds, release row, 20 years, CPS yardstick).
For each environment, programme level (take-up 30% and 90%, no raise) and outcome, the programme run and the no-programme run of each seed share a seed (same adults, same
shocks). With per-seed values a (programme) and b (none): paired variance = var(a - b); unpaired variance = var(a) + var(b), what two independent samples of the same size
would give for the difference of means. Reduction = 1 - paired/unpaired; interval widths scale with the square root, so 'interval narrower by' = 1 - sqrt(paired/unpaired).
95% percentile bootstrap over seeds (2,000 resamples, seed 20261101). Programme inflation and programme cost are left out: the no-programme run has none (constant), so pairing cannot reduce their variance by construction.
Reads the batch's results folder; writes dev/runs/s7-pairing/pairing.csv.
  python3 dev/tools/s7_pairing.py [RESULTS_DIR]"""
import os, sys, csv
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
import batch_load as bl
RES = sys.argv[1] if len(sys.argv) > 1 else '/home/user/bettertobest/compassionism-sim-results'
rows, meta = bl.load(os.path.join(RES, 'prog-d-ce8d030'))
assert not meta['_problems'] and meta['seedList'] == list(range(1, 501))
OUT = [('fgt0PY', 'below the cost of living, % of adult-years'), ('pov', 'too little wealth at year 20, %'), ('medWealthReal', 'median real wealth')]
rng = np.random.default_rng(20261101); idx = rng.integers(0, 500, size=(2000, 500))
def vr(a, b):
    d = a - b; return 1 - d.var(ddof=1) / (a.var(ddof=1) + b.var(ddof=1))
res = []
for env, en in (('ref', 'Reference'), ('adv', 'Adverse'), ('st', 'Stress')):
    none = rows['%s.n500.y20.rls.cps.none' % env]
    for q in (30, 90):
        prog = rows['%s.n500.y20.rls.cps.main.p%d' % (env, q)]
        for k, lab in OUT:
            a, b = np.asarray(prog[k], float), np.asarray(none[k], float)
            m = vr(a, b); bs = np.array([vr(a[i], b[i]) for i in idx])
            res.append([en, q, lab, '%.1f' % (100*m), '%.1f' % (100*np.percentile(bs, 2.5)), '%.1f' % (100*np.percentile(bs, 97.5)), '%.1f' % (100*(1 - (1 - m) ** 0.5)), '%.3f' % np.corrcoef(a, b)[0, 1]])
with open(os.path.join(os.path.dirname(__file__), '..', 'runs', 's7-pairing', 'pairing.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['environment', 'take_up_pct', 'outcome', 'variance_reduction_pct', 'lo95', 'hi95', 'interval_narrower_pct', 'correlation_programme_vs_none']); w.writerows(res)
for r in res: print(r)
