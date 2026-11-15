#!/usr/bin/env python3
"""S7 part 2, item 2 (Nov 15, 2026): reads dev/runs/s7-spend-groups/groups.json (dev/tools/s7_spend_groups.js, 100 seeds, frozen no-programme row, Reference,
500 adults, 20 years) and writes dev/runs/s7-spend-groups/groups.csv: for each income fifth (adults ranked by their own disposable income over the 20 years,
within each seed), the saving rate (income less consumption, over income), consumption as a share of the full cost of living, and income per adult-year,
each as the mean over seeds with a 95% percentile bootstrap interval over seeds (10,000 resamples, seed 20261101).  python3 dev/tools/s7_spend_groups.py"""
import os, json, csv
import numpy as np
D = os.path.join(os.path.dirname(__file__), '..', 'runs', 's7-spend-groups')
d = json.load(open(os.path.join(D, 'groups.json')))
S = d['seeds']; ns = len(S)
rng = np.random.default_rng(20261101); idx = rng.integers(0, ns, size=(10000, ns))
NAMES = ['lowest fifth', 'second fifth', 'middle fifth', 'fourth fifth', 'highest fifth', 'all adults']
def arr(q, k): return np.array([s['groups'][q][k] for s in S]) if q < 5 else np.array([sum(g[k] for g in s['groups']) for s in S])
def ci(v): b = v[idx].mean(axis=1); return float(v.mean()), float(np.percentile(b, 2.5)), float(np.percentile(b, 97.5))
rows = []
for q in range(6):
    I, C, K = arr(q, 'I'), arr(q, 'C'), arr(q, 'K'); n = (100 if q < 5 else 500) * 20
    for name, v, u in (('saving rate: income less consumption, over income, %', 100*(1 - C/I), '%'), ('spending as a share of the cost-of-living basket, %', 100*C/K, '%'),
                       ('income per adult-year, year-0 dollars', I/n, '$')):
        m, lo, hi = ci(v); rows.append([NAMES[q], name, '%.4f' % m, '%.4f' % lo, '%.4f' % hi, ns])
with open(os.path.join(D, 'groups.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['group', 'measure', 'mean', 'lo95', 'hi95', 'seeds']); w.writerows(rows)
for r in rows: print(r)
