#!/usr/bin/env python3
"""S59 (Nov 10, 2026; research-update prereg/2026-11-s59-asset-classes.md): tables of the asset-class pilot, from the files dev/tools/s59_assets.js writes.
Usage: python3 dev/tools/s59_table.py DIR [OUT.md]   (DIR holds s59-assets-ref.json, -adv.json, -st.json; default OUT dev/runs/s59-assets/tables.md;
also writes summary.json beside OUT: every mean and paired effect, without the per-seed values). Analysis only; the intervals are the tool's
(2.5th-97.5th percentile of 2,000 paired bootstrap replicates over seeds, unadjusted)."""
import json, os, sys
D = sys.argv[1]; OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'runs', 's59-assets', 'tables.md')
ENVS = [('ref', 'Reference'), ('adv', 'Adverse'), ('st', 'Stress')]; DES = [('rls', 'release'), ('c22', 'C2.2')]
R = {e: json.load(open(os.path.join(D, 's59-assets-%s.json' % e))) for e, _ in ENVS if os.path.exists(os.path.join(D, 's59-assets-%s.json' % e))}
L = []; P = L.append
def eff(x, d=2, sc=1.0): return '%+.*f (%+.*f to %+.*f)' % (d, x['m']*sc, d, x['lo']*sc, d, x['hi']*sc)
def usd(v): return ('-' if v < 0 else '') + '$' + format(abs(int(round(v/100.0))*100), ',')
def eusd(x): return '%s (%s to %s)' % (('+' if x['m'] >= 0 else '') + usd(x['m']), usd(x['lo']), usd(x['hi']))
m0 = next(iter(R.values()))['_meta']
P('# S59: wealth held by asset class, pilot tables'); P('')
P('Seeds 1-%d, 500 adults, %d years; engine %s. Effects are programme minus no programme on the same seeds, with the 2.5th-97.5th percentile interval of 2,000 paired bootstrap replicates (unadjusted). A pilot is a mechanism check, not a result. Made by `dev/tools/s59_table.py` from the per-seed files in compassionism-sim-results.' % (m0['seeds'], m0['years'], m0['manifest']['commit'][:7])); P('')
P('Check row (every asset nominal, no pass-through) equals "off" on every kept key: ' + ', '.join('%s %s' % (n, 'yes' if R[e]['_meta'].get('checkEqualsOff') else 'NO') for e, n in ENVS if e in R) + '.'); P('')
P('## 1. Primary outcome: the programme\'s effect on wealth poverty (points; adults under $25,000 of real wealth, year 20)'); P('')
P('| Reading | ' + ' | '.join('%s, %s' % (n, dn) for e, n in ENVS if e in R for _, dn in DES) + ' |'); P('|---|' + '---|'*(2*len(R)))
rows = [k for k in next(iter(R.values()))['rows'] if k != 'check']
for k in rows:
    P('| %s | ' % next(iter(R.values()))['rows'][k]['label'] + ' | '.join(eff(R[e]['rows'][k]['effect'][d]['pov']) for e, _ in ENVS if e in R for d, _ in DES) + ' |')
P(''); P('Wealth poverty with no programme (%): ' + '; '.join('%s off %.1f, main %.1f' % (n, R[e]['rows']['off']['mean']['none']['pov'], R[e]['rows']['main']['mean']['none']['pov']) for e, n in ENVS if e in R) + '.'); P('')
SEC = [('dmWp50E', 'median real wealth ($)', 'usd'), ('dmWp10E', 'real wealth at the 10th percentile ($)', 'usd'), ('dmWp90E', 'real wealth at the 90th percentile ($)', 'usd'), ('eGiniWN', 'wealth Gini, debts kept', 3), ('eGiniW', 'wealth Gini, debts as zero', 3),
       ('dmWt1E', 'top 1% share of wealth (%)', 2), ('dmWt10E', 'top 10% share of wealth (%)', 2), ('dmWb50E', 'bottom 50% share of wealth (%)', 2), ('dmFdE', 'families in debt (%)', 2),
       ('fgt0PY', 'basket poverty (% of adult-years)', 2), ('hhCostPY', 'cost of living', 2), ('endoAnn', 'programme inflation (points a year)', 2)]
P('## 2. Secondary outcomes: the programme\'s effect, today\'s reading beside the asset-class readings'); P('')
for e, n in ENVS:
    if e not in R: continue
    for d, dn in DES:
        P('**%s, %s**' % (n, dn)); P(''); P('| Outcome | no programme (off / main) | effect, off | effect, main | effect, fixed debt reprices |'); P('|---|---|---|---|---|')
        for k, lab, f in SEC:
            a = R[e]['rows']
            if k not in a['off']['effect'][d]: continue
            sc = 100.0 if k == 'endoAnn' else 1.0
            lv = '%s / %s' % (usd(a['off']['mean']['none'][k]), usd(a['main']['mean']['none'][k])) if f == 'usd' else '%.*f / %.*f' % (f, a['off']['mean']['none'][k]*sc, f, a['main']['mean']['none'][k]*sc)
            P('| %s | %s | ' % (lab, lv) + ' | '.join(eusd(a[r]['effect'][d][k]) if f == 'usd' else eff(a[r]['effect'][d][k], f, sc) for r in ('off', 'main', 'chi1')) + ' |')
        P('')
P('## 3. The programme\'s effect on mean real wealth in three parts (Year-0 dollars per adult)'); P('')
P('E: the opening nominal position held untouched (nominal assets and floating debt with their interest, less fixed-rate debt). V: the opening real assets held untouched. S: saving since the start and what it earned. The share is E\'s part of the whole effect.'); P('')
for e, n in ENVS:
    if e not in R: continue
    P('**%s**' % n); P(''); P('| Reading | Design | Group | E: opening nominal position | V: opening real assets | S: saving | Whole | E share |'); P('|---|---|---|---|---|---|---|---|')
    for r in [k for k in rows if k != 'off']:
        for d, dn in DES:
            x = R[e]['rows'][r]['effect'][d]
            for q, qn in [('', 'all adults')] + ([(str(i), 'fifth %d of starting wealth' % i) for i in range(1, 6)] if r in ('main', 'chi1') else []):
                E, V, S = x['rtE' + q]['m'], x['rtV' + q]['m'], x['rtS' + q]['m']; W = E + V + S
                P('| %s | %s | %s | %s | %s | %s | %s | %s |' % (R[e]['rows'][r]['label'] if not q else '', dn if not q else '', qn, eusd(x['rtE' + q]), eusd(x['rtV' + q]), eusd(x['rtS' + q]), ('+' if W >= 0 else '') + usd(W), ('%.0f%%' % (E/W*100)) if abs(W) > 1 else 'n/a'))
    P('')
P('## 4. Levels of the three parts under the main reading (Year-0 dollars per adult, year 20), and the start'); P('')
for e, n in ENVS:
    if e not in R: continue
    a = R[e]['rows']['main']['mean']
    P('**%s**' % n); P(''); P('| Group | start: nominal position / real assets | no programme: E / V / S | release: E / V / S | C2.2: E / V / S |'); P('|---|---|---|---|---|')
    for q, qn in [('', 'all adults')] + [(str(i), 'fifth %d' % i) for i in range(1, 6)]:
        P('| %s | %s / %s | ' % (qn, usd(a['none']['rtE0' + q]), usd(a['none']['rtV0' + q])) + ' | '.join(' / '.join(usd(a[d][k + q]) for k in ('rtE', 'rtV', 'rtS')) for d in ('none', 'rls', 'c22')) + ' |')
    P('')
P('## 5. The no-programme run: the start and year 20, today\'s reading and the main reading'); P('')
P('| Environment | Measure | start | year 20, off | year 20, main | year 20, no real price gain |'); P('|---|---|---|---|---|---|')
for e, n in ENVS:
    if e not in R: continue
    a = R[e]['rows']
    for kS, kE, lab, f in [('dmWp50S', 'dmWp50E', 'median real wealth', 'usd'), ('dmWt1S', 'dmWt1E', 'top 1% share (%)', 1), ('dmWt10S', 'dmWt10E', 'top 10% share (%)', 1), ('dmWb50S', 'dmWb50E', 'bottom 50% share (%)', 1), ('dmFdS', 'dmFdE', 'families in debt (%)', 1)]:
        g = lambda r, k: usd(a[r]['mean']['none'][k]) if f == 'usd' else '%.*f' % (f, a[r]['mean']['none'][k])
        P('| %s | %s | %s | %s | %s | %s |' % (n, lab, g('off', kS), g('off', kE), g('main', kE), g('rho0', kE)))
P(''); P('## 6. The top 1% of adults\' share of private business equity (%, main reading)'); P('')
P('| Environment | start | year 20, no programme | year 20, release | year 20, C2.2 |'); P('|---|---|---|---|---|')
for e, n in ENVS:
    if e not in R: continue
    a = R[e]['rows']['main']['mean']; P('| %s | %.1f | %.1f | %.1f | %.1f |' % (n, a['none']['rtBt1S'], a['none']['rtBt1E'], a['rls']['rtBt1E'], a['c22']['rtBt1E']))
P(''); P('Year-20 holdings under the main reading (Year-0 dollars per adult: real assets / nominal assets / floating debt / fixed-rate debt): ' + '; '.join('%s: ' % n + ', '.join('%s %s' % (dn, ' / '.join(usd(R[e]['rows']['main']['mean'][d][k]) for k in ('rtRE', 'rtNE', 'rtDvE', 'rtDfE'))) for d, dn in [('none', 'no programme')] + DES) for e, n in ENVS if e in R) + '.')
os.makedirs(os.path.dirname(os.path.abspath(OUT)), exist_ok=True); open(OUT, 'w').write('\n'.join(L) + '\n')
summ = {e: {'_meta': R[e]['_meta'], 'rows': {k: {'label': v['label'], 'rt': v['rt'], 'mean': v['mean'], 'effect': v['effect']} for k, v in R[e]['rows'].items()}} for e in R}
json.dump(summ, open(os.path.join(os.path.dirname(os.path.abspath(OUT)), 'summary.json'), 'w'), separators=(',', ':'))
print('wrote', OUT)
