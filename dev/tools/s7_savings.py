#!/usr/bin/env python3
"""S7 part 2, item 3 (Nov 15, 2026): wealth poverty (share of adults with too little wealth at year 20) with ordinary savings, with savings that only keep
their value (zero real return) and with savings that earn the TIPS real rate (+0.97% a year), each beside its own no-programme control, from the frozen release panel
dev/runs/release-panel-frozen.json (engine ce8d030, 500 paired seeds, 500 adults, 20 years, three environments). Rows: release (ordinary: savings earn nothing nominal),
sav0 (interest = inflation in both runs), sav (interest = inflation + 0.97% in both runs). The control of release is the panel's `base`; of sav0 and sav, `bases.sv0` and `bases.sv`.
The panel's paired change and 95% interval over seeds (dPov = [mean, lo, hi]) are copied as stored; nothing is recomputed.  python3 dev/tools/s7_savings.py
Writes dev/runs/s7-savings/savings.csv, which dev/tools/study_files.py copies into data/studies/s7-savings.json."""
import os, json, csv
D = os.path.join(os.path.dirname(__file__), '..', 'runs')
P = json.load(open(os.path.join(D, 'release-panel-frozen.json')))
READ = [('release', None, 'ordinary savings (no interest)'), ('sav0', 'sv0', 'zero real return (interest = inflation)'), ('sav', 'sv', 'real return +0.97% a year (interest = inflation + 0.97%)')]
ENV = [('ref', 'Reference'), ('adv', 'Adverse'), ('st', 'Stress')]
out = []
for e, en in ENV:
    E = P['envs'][e]
    for row, bk, lab in READ:
        r = E['rows'][row]; b = E['base'] if bk is None else E['bases'][bk]
        none, prog = b['pov'], r['pov']; dm, lo, hi = r['dPov']
        assert abs((prog - none) - dm) < 0.2, (e, row, prog, none, dm)
        out.append([en, lab, '%.1f' % none, '%.1f' % prog, '%.2f' % dm, '%.2f' % lo, '%.2f' % hi, '%.1f' % r['infl'], r['medWealth']])
with open(os.path.join(D, 's7-savings', 'savings.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['environment', 'savings', 'no_programme_pct', 'programme_pct', 'change_pp', 'lo95', 'hi95', 'programme_inflation_pct_a_year', 'median_wealth_programme_usd']); w.writerows(out)
for r in out: print(r)
