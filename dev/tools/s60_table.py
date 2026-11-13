#!/usr/bin/env python3
"""S60 (Nov 13, 2026; research-update prereg/2026-11-s60-bargaining-power.md): tables of the bargaining pilot, from the files dev/tools/s60_bargain.js writes.
Usage: python3 dev/tools/s60_table.py DIR [OUT.md]
  DIR holds s60-bargain-ENV.json (or chunks s60-bargain-ENV-1.json, -2.json, ...; merged first: same engine, seeds and rows, so merging changes no figure)
  for ENV = ref, adv, st, and s60-validate-ref.json. Default OUT dev/runs/s60-bargain/tables.md; also writes summary.json beside OUT (means and paired
  effects, no per-seed values).
Analysis only. Intervals: the 2.5th-97.5th percentile of 2,000 paired bootstrap replicates over seeds (fixed generator), unadjusted."""
import glob, json, os, sys
import numpy as np
ARGS = [a for a in sys.argv[1:] if not a.startswith('--')]; D = ARGS[0]
OUT = ARGS[1] if len(ARGS) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'runs', 's60-bargain', 'tables.md')
ENVS = [('ref', 'Reference'), ('adv', 'Adverse'), ('st', 'Stress')]; DES = [('rls', 'release'), ('c22', 'C2.2')]
READ = ['off', 'bg0', 'bg03', 'bg10', 'nash24', 'nash48', 'nash48y', 'nash48n']
PI = {'off': None, 'bg0': (0, 1/1.21), 'bg03': (0.03, 1/1.21), 'bg10': (0.10, 1/1.21), 'nash24': (0.24, 1/1.21), 'nash48': (0.48, 1/1.21), 'nash48y': (0.48, 1/1.53), 'nash48n': (0.48, 1.0)}
def load(stem, e):
    f = os.path.join(D, '%s-%s.json' % (stem, e)); ch = sorted(glob.glob(os.path.join(D, '%s-%s-*.json' % (stem, e))), key=lambda p: int(p.rsplit('-', 1)[1][:-5]))
    if ch:
        parts = [json.load(open(p)) for p in ch]; m = dict(parts[0]['_meta']); m['rows'] = [r for q in parts for r in q['_meta']['rows']]; m['chunks'] = [q['_meta']['command'] for q in parts]
        m['seconds'] = sum(q['_meta']['seconds'] for q in parts); m['command'] = 'in chunks: see chunks'
        assert len({json.dumps(q['_meta']['manifest'], sort_keys=True) for q in parts}) == 1, 'chunks from different engines'
        rows = {}
        for q in parts: rows.update(q['rows'])
        return {'_meta': m, 'rows': rows}
    return json.load(open(f)) if os.path.exists(f) else None
R = {e: load('s60-bargain', e) for e, _ in ENVS}; V = load('s60-validate', 'ref'); L = []; P = L.append
def boot(d):
    d = np.asarray(d, float); g = np.random.default_rng(20261113); b = d[g.integers(0, len(d), (2000, len(d)))].mean(1); return float(d.mean()), float(np.quantile(b, 0.025)), float(np.quantile(b, 0.975))
def eff(e, r, d, k):
    x = R[e]['rows'][r]['effect'][d].get(k); return (x['m'], x['lo'], x['hi']) if x else (float('nan'),) * 3
def dd(e, r, d, k):  # the reading's effect less off's, paired by seed
    A = R[e]['rows'][r]['seeds']; B = R[e]['rows']['off']['seeds']; a = np.asarray(A[d][k]) - np.asarray(A['none'][k]); b = np.asarray(B[d][k]) - np.asarray(B['none'][k]); return boot(a - b)
f1 = lambda t: '%.1f [%.1f, %.1f]' % t; f2 = lambda t: '%.2f [%.2f, %.2f]' % t; f0 = lambda t: '%.0f [%.0f, %.0f]' % t
S = {'meta': {}, 'checks': {}, 'mech': {}, 'effects': {}, 'diff': {}, 'validate': {}}
P('# S60 pilot tables: bargaining power (a worker\'s outside option and an employer markdown)\n')
P('Seeds 1-100, 500 adults, 20 years; the release row and the C2.2 design, each against its own no-programme run on the same seeds; S71\'s rows with adults outside the labour force. A pilot is a mechanism check, not a result. Intervals: 2.5th-97.5th percentile of 2,000 paired bootstrap replicates over seeds, unadjusted. Dollars are Year-0 dollars.\n')
for e, en in ENVS:
    if R[e]: S['meta'][e] = {k: R[e]['_meta'][k] for k in ('seeds', 'years', 'seconds', 'command')}; S['meta'][e]['commit'] = R[e]['_meta']['manifest'].get('commit')
P('## 1. Checks: readings that must equal off\n')
P('| environment | reading | series compared | series that differ |'); P('|---|---|---|---|')
for e, en in ENVS:
    if not R[e]: continue
    off = R[e]['rows']['off']['seeds']
    for r in ('bg0', 'nash48n'):
        if r not in R[e]['rows']: continue
        X = R[e]['rows'][r]['seeds']; n = 0; bad = []
        for d in off:
            for k in off[d]:
                if k.startswith('bg'): continue
                n += 1
                if off[d][k] != X[d].get(k): bad.append(d + ':' + k)
        S['checks']['%s_%s' % (e, r)] = {'n': n, 'differ': len(bad), 'first': bad[:5]}; P('| %s | %s | %d | %d%s |' % (en, r, n, len(bad), (' (' + ', '.join(bad[:3]) + ')') if bad else ''))
P('\n## 2. The mechanism, programme runs (means over seeds; workers are adults with earnings in the year, years 1-19)\n')
MK = [('bgN', 'worker-years, % of adult-years', '%.1f'), ('bgO', 'outside-option rise per worker-year ($)', '%.0f'), ('bgR', 'bargained raise per worker-year, wage part ($)', '%.0f'),
      ('bgE', 'earnings it adds after the hours response ($)', '%.0f'), ('bgSh', 'bargained share of the programme\'s raises to the wage rate (%)', '%.1f'), ('bgCap', 'worker-years at the markdown cap (%)', '%.1f'),
      ('bgMd', 'mean wage over what the worker adds (%)', '%.1f'), ('bgOP10', 'outside-option rise, % of full-year earnings, P10 (year 20)', '%.1f'), ('bgOP50', 'same, median', '%.1f'),
      ('bgOP90', 'same, P90', '%.1f'), ('bgK', 'bargained raise over the capital income adults receive (%)', '%.1f')]
for d, dn in DES:
    P('### %s design\n' % dn); P('| measure | environment | ' + ' | '.join(READ[1:]) + ' |'); P('|---|---|' + '---|' * (len(READ) - 1))
    for k, kn, fm in MK:
        for e, en in ENVS:
            if not R[e]: continue
            vals = [R[e]['rows'][r]['mean'][d].get(k, float('nan')) if r in R[e]['rows'] else float('nan') for r in READ[1:]]
            for r, v in zip(READ[1:], vals): S['mech'].setdefault(d, {}).setdefault(e, {}).setdefault(r, {})[k] = v
            P('| %s | %s | ' % (kn, en) + ' | '.join(fm % v for v in vals) + ' |')
    P('')
P('### Reservation wages under the Nash relation (wage = (1 - pi) x what the worker adds + pi x reservation wage)\n')
P('Before the programme the relation puts the reservation wage at (1 - (1 - pi)/m)/pi of the wage; the programme adds the outside-option rise (P10, median, P90 of the year-20 workers, as a share of their full-year earnings). A negative starting value means the Nash relation cannot give that pass-through with that markdown (the puzzle Jager et al. report).\n')
P('| reading | pi | wage over what the worker adds | reservation wage before (% of wage) | after, release: P10 / median / P90 | after, C2.2: P10 / median / P90 |'); P('|---|---|---|---|---|---|')
for r in READ[2:]:
    pi, m = PI[r]; rw = (1 - (1 - pi)/m)/pi*100 if pi > 0 else float('nan'); row = []
    for d, _ in DES:
        x = R['ref']['rows'][r]['mean'][d] if R['ref'] and r in R['ref']['rows'] else {}
        row.append(' / '.join('%.0f' % (rw + x.get(k, float('nan'))) for k in ('bgOP10', 'bgOP50', 'bgOP90')))
    S['mech'].setdefault('nash_rw0', {})[r] = rw; P('| %s | %.2f | %.3f | %.0f | %s | %s |' % (r, pi, m, rw, row[0], row[1]))
OUTK = [('wtPovE', 'wealth poverty, year 20, weighted (points)', f1), ('fgt0PY', 'basket poverty, person-years (points)', f1), ('Er', 'real wage earnings per adult-year ($)', f0),
        ('hrs', 'hours (share of hours with no response)', lambda t: '%.4f [%.4f, %.4f]' % t), ('emp', 'adults with earnings (points)', f2), ('endoAnn', 'inflation a year (points)', lambda t: '%.2f [%.2f, %.2f]' % tuple(100*x for x in t)),
        ('hhCostPY', 'basket poverty, households (person-years, points)', f2), ('wtT1E', 'top 1% share of wealth, year 20, weighted (points)', f2), ('wtMedE', 'median wealth, year 20, weighted ($)', f0)]
P('\n## 3. Effects of the programme (programme minus no programme), by reading\n')
for d, dn in DES:
    P('### %s design\n' % dn)
    for e, en in ENVS:
        if not R[e]: continue
        P('**%s**\n' % en); P('| outcome | ' + ' | '.join(r for r in READ if r in R[e]['rows']) + ' |'); P('|---|' + '---|' * len([r for r in READ if r in R[e]['rows']]))
        for k, kn, fm in OUTK:
            cells = []
            for r in READ:
                if r not in R[e]['rows']: continue
                t = eff(e, r, d, k); S['effects'].setdefault(d, {}).setdefault(e, {}).setdefault(r, {})[k] = t; cells.append(fm(t))
            P('| %s | ' % kn + ' | '.join(cells) + ' |')
        P('')
P('## 4. What bargaining changes: the effect under each reading less the effect without it (paired by seed)\n')
for d, dn in DES:
    P('### %s design\n' % dn); P('| outcome | environment | ' + ' | '.join(READ[2:]) + ' |'); P('|---|---|' + '---|' * (len(READ) - 2))
    for k, kn, fm in OUTK:
        for e, en in ENVS:
            if not R[e]: continue
            cells = []
            for r in READ[2:]:
                if r not in R[e]['rows']: cells.append('-'); continue
                t = dd(e, r, d, k); S['diff'].setdefault(d, {}).setdefault(e, {}).setdefault(r, {})[k] = t; cells.append(fm(t))
            P('| %s | %s | ' % (kn, en) + ' | '.join(cells) + ' |')
    P('')
if V:
    P('## 5. Validation against Vivalt et al. (no programme; $12,000 a year to every adult, unfinanced, 3 years, Reference, %d seeds)\n' % V['_meta']['seeds'])
    P('Study: individual income excluding the transfer -$1,900 a year (16 cents per dollar); participation -4.2 points; hours -1 to -2 a week; hourly pay -$0.14, interval -$0.87 to +$0.59. The engine\'s earnings are per adult (adults outside the labour force earn nothing and do not respond); the bargained hourly change is the raise per worker-year over 2,080 hours.\n')
    P('| reading | earnings per adult-year ($) | per transfer dollar | adults with earnings (points) | hours | bargained raise per worker-year ($) | per hour ($) | inside the study\'s pay interval |'); P('|---|---|---|---|---|---|---|---|')
    for r in ('ubi', 'ubi03', 'ubi10', 'ubi24', 'ubi48'):
        if r not in V['rows']: continue
        o = V['rows'][r]; E = o['effect']['E']; br = o['mean'].get('bgR', 0.0); ph = br/2080
        S['validate'][r] = {'E': E, 'perDollar': E['m']/12000, 'emp': o['effect']['emp'], 'hrs': o['effect']['hrs'], 'bgR': br, 'perHour': ph, 'inside': -0.87 <= ph <= 0.59}
        P('| %s | %.0f [%.0f, %.0f] | %.3f | %.2f [%.2f, %.2f] | %.4f | %.0f | %.2f | %s |' % (r, E['m'], E['lo'], E['hi'], E['m']/12000, o['effect']['emp']['m'], o['effect']['emp']['lo'], o['effect']['emp']['hi'], o['effect']['hrs']['m'], br, ph, 'yes' if -0.87 <= ph <= 0.59 else 'no'))
    P('')
open(OUT, 'w').write('\n'.join(L) + '\n'); json.dump(S, open(os.path.join(os.path.dirname(os.path.abspath(OUT)), 'summary.json'), 'w'), indent=1)
print('wrote ' + OUT)
