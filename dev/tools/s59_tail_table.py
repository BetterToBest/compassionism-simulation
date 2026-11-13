#!/usr/bin/env python3
"""S59, part 2 (Nov 12, 2026; research-update prereg/2026-11-s59-tail-returns.md): tables of the tail, owners and capital-income pilot, from the files
dev/tools/s59_tail.js writes.
Usage: python3 dev/tools/s59_tail_table.py DIR [OUT.md] [--part1=DIR1]
  DIR holds s59-tail-ENV.json for ENV = ref, adv, st, or the pilot's chunks s59-tail-ENV-1.json, -2.json, ... (one invocation of the tool per chunk of
  readings; the chunks are merged into s59-tail-ENV.json first: same engine, seeds and rows, so merging changes no figure). Default OUT
  dev/runs/s59-tail/tables.md; also writes summary.json beside OUT (every mean and paired effect, without the per-seed values).
  --part1: the folder of part 1's pilot (compassionism-sim-results s59-assets-1d2cf29), for the table that sets the corrected rows beside it.
Analysis only. Intervals: the 2.5th-97.5th percentile of 2,000 paired bootstrap replicates over seeds (fixed generator), unadjusted; the tool's for the
programme's effects, this script's (same method) for the start's levels and for differences between two readings."""
import glob, json, os, sys
import numpy as np
ARGS = [a for a in sys.argv[1:] if not a.startswith('--')]; D = ARGS[0]
OUT = ARGS[1] if len(ARGS) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'runs', 's59-tail', 'tables.md')
P1 = ([a[8:] for a in sys.argv[1:] if a.startswith('--part1=')] or [None])[0]
HERE = os.path.dirname(os.path.abspath(__file__)); SRC = json.load(open(os.path.join(HERE, '..', '..', 'sources', 's59_tail.json')))
ENVS = [('ref', 'Reference'), ('adv', 'Adverse'), ('st', 'Stress')]; DES = [('rls', 'release'), ('c22', 'C2.2')]
R = {}
for e, _ in ENVS:
    f = os.path.join(D, 's59-tail-%s.json' % e); ch = sorted(glob.glob(os.path.join(D, 's59-tail-%s-*.json' % e)), key=lambda p: int(p.rsplit('-', 1)[1][:-5]))
    if ch:
        parts = [json.load(open(p)) for p in ch]; m = dict(parts[0]['_meta']); m['rows'] = [r for q in parts for r in q['_meta']['rows']]; m['chunks'] = [q['_meta']['command'] for q in parts]
        m['seconds'] = sum(q['_meta']['seconds'] for q in parts); m['command'] = 'in chunks: see chunks'; m['checkEqualsOff'] = any(q['_meta'].get('checkEqualsOff') for q in parts) and not any(q['_meta'].get('checkEqualsOff') is False for q in parts)
        assert len({q['_meta']['manifest']['commit'] if isinstance(q['_meta']['manifest'], dict) and 'commit' in q['_meta']['manifest'] else json.dumps(q['_meta']['manifest'], sort_keys=True)[:400] for q in parts}) == 1, 'chunks from different engines'
        rows = {}
        for q in parts: rows.update(q['rows'])
        json.dump({'_meta': m, 'rows': rows}, open(f, 'w'))
    if os.path.exists(f): R[e] = json.load(open(f))
L = []; P = L.append
RNG = np.random.default_rng(20261112)
def boot(d):
    d = np.asarray(d, float); n = len(d); b = d[RNG.integers(0, n, (2000, n))].mean(axis=1); return {'m': float(d.mean()), 'lo': float(np.quantile(b, 0.025)), 'hi': float(np.quantile(b, 0.975))}
def eff(x, d=2, sc=1.0): return '%+.*f (%+.*f to %+.*f)' % (d, x['m']*sc, d, x['lo']*sc, d, x['hi']*sc)
def lev(x, d=2, sc=1.0): return '%.*f (%.*f to %.*f)' % (d, x['m']*sc, d, x['lo']*sc, d, x['hi']*sc)
def usd(v): return ('-' if v < 0 else '') + '$' + format(abs(int(round(v/100.0))*100), ',')
def eusd(x): return '%s (%s to %s)' % (('+' if x['m'] >= 0 else '') + usd(x['m']), usd(x['lo']), usd(x['hi']))
def lusd(x): return '%s (%s to %s)' % (usd(x['m']), usd(x['lo']), usd(x['hi']))
def seeds(e, r, d, k): return np.asarray(R[e]['rows'][r]['seeds'][d][k], float)
def diff2(e, r1, r0, d, k):  # the programme's effect under reading r1 less the effect under r0, paired by seed
    return boot((seeds(e, r1, d, k) - seeds(e, r1, 'none', k)) - (seeds(e, r0, d, k) - seeds(e, r0, 'none', k)))
A = next(iter(R.values())); m0 = A['_meta']; ROWS = [k for k in A['rows']]; LAB = {k: A['rows'][k]['label'] for k in ROWS}
have = lambda k: all(k in R[e]['rows'] for e in R)
SUM = {'meta': {'engine': m0['manifest'], 'seeds': m0['seeds'], 'years': m0['years']}, 'start': {}, 'effects': {}, 'means': {}}
for e in R:
    SUM['effects'][e] = {r: R[e]['rows'][r]['effect'] for r in R[e]['rows']}; SUM['means'][e] = {r: R[e]['rows'][r]['mean'] for r in R[e]['rows']}
eng = m0['manifest'].get('commit', '') if isinstance(m0['manifest'], dict) else ''
P('# S59, part 2: the weighted top tail, business owners and the income wealth pays, pilot tables'); P('')
P('Seeds 1-%d, 500 adults, %d years; engine %s. Effects are programme minus no programme on the same seeds, with the 2.5th-97.5th percentile interval of 2,000 paired bootstrap replicates (unadjusted). Shares, percentiles and rates are weighted by each adult\'s population weight (1 for every adult where the tail is off). A pilot is a mechanism check, not a result. Made by `dev/tools/s59_tail_table.py` from the per-seed files in compassionism-sim-results.' % (m0['seeds'], m0['years'], ('`%s`' % eng[:7]) if eng else 'in each file\'s manifest')); P('')
P('Check row (the tail with every weight 1 and no change of wealth) equals part 1\'s reading on every kept key: ' + ', '.join('%s %s' % (n, 'yes' if R[e]['_meta'].get('checkEqualsOff') else 'NO') for e, n in ENVS if e in R) + '.'); P('')
P('Readings: ' + '; '.join('**%s** %s' % (k, LAB[k]) for k in ROWS) + '.'); P('')
# 1. the start
sc = SRC['shares']; k25 = SRC['cpi'][1]/SRC['cpi'][0]; dfa = SRC['dfa']; dq = sorted(dfa.keys())
P('## 1. The start (end of Year 0, no programme, Reference) beside the survey'); P('')
P('The SCF rows are the 2022 Survey of Consumer Finances for the engine\'s families (head aged 25-66 with wage income), counted by adult as the engine does (a couple\'s net worth split equally), in 2025 dollars. The tail is fitted to that survey, so agreement with it checks the build; the Fed\'s Distributional Financial Accounts (all households, a wider wealth concept) are the outside comparison.'); P('')
P('| | top 0.1% share | top 1% share | top 10% share | bottom 50% share | Gini (debts kept) | mean | median | 99.9th percentile |'); P('|---|---|---|---|---|---|---|---|---|')
ST = [('wtT01S', 2, 0), ('wtT1S', 2, 0), ('wtT10S', 2, 0), ('wtB50S', 2, 0), ('wtGnS', 3, 0), ('wtMeanS', 0, 1), ('wtMedS', 0, 1), ('wtP999S', 0, 1)]
if 'ref' in R:
    for r in ROWS:
        if r in ('flat', 'p1chi', 'chi1', 'ix05', 'ownW', 'ownE', 'ng0', 'ngall', 'rg', 'ci0'): continue
        b = {k: boot(seeds('ref', r, 'none', k)) for k, _, _ in ST}; SUM['start'][r] = b
        P('| %s | ' % LAB[r] + ' | '.join(lusd(b[k]) if u else lev(b[k], d) for k, d, u in ST) + ' |')
    a = sc['modelPerAdult']; f = sc['model']; al = sc['allFamilies']
    P('| **SCF 2022, the engine\'s families, by adult** | %.2f | %.2f | %.2f | %.2f | %.3f | %s | %s | |' % (a['top01'], a['top1'], a['top10'], a['bottom50'], a['gini'], usd(a['mean']*k25), usd(a['median']*k25)))
    P('| SCF 2022, the engine\'s families, by family | %.2f | %.2f | %.2f | %.2f | %.3f | %s | %s | |' % (f['top01'], f['top1'], f['top10'], f['bottom50'], f['gini'], usd(f['mean']*k25), usd(f['median']*k25)))
    P('| SCF 2022, all families | %.2f | %.2f | %.2f | %.2f | %.3f | %s | %s | |' % (al['top01'], al['top1'], al['top10'], al['bottom50'], al['gini'], usd(al['mean']*k25), usd(al['median']*k25)))
    P('| SCF 2022 with the Forbes 400 added, all families | | %.2f | | | | | | |' % SRC['forbesAdded']['top1ScfForbes'])
    for q in (dq[0], dq[-1]): P('| Distributional Financial Accounts, %s | %.1f | %.1f | %.1f | %.1f | | | | |' % (q, dfa[q]['top01'], dfa[q]['top1'], dfa[q]['top10'], dfa[q]['bottom50']))
    P('')
    if have('main'):
        b = SUM['start']['main']; g = b['wtT1S']['m'] - a['top1']
        P('Primary outcome (i): the start\'s weighted top 1%% share under the main reading is %s, against the SCF\'s %.2f%% for the same families by adult (gap %+.2f points) and the Fed accounts\' %.1f%% (%s) and %.1f%% (%s). Tail adults per run: %.0f of 500, standing for %.2f%% of adults.' % (lev(b['wtT1S']), a['top1'], g, dfa[dq[0]]['top1'], dq[0], dfa[dq[-1]]['top1'], dq[-1], R['ref']['rows']['main']['mean']['none']['wtN'], R['ref']['rows']['main']['mean']['none']['wtTailW'])); P('')
def table(title, key, d=2, sc=1.0, rows=None, note=None, usdf=False):
    P(title); P('')
    if note: P(note); P('')
    P('| Reading | ' + ' | '.join('%s, %s' % (n, dn) for e, n in ENVS if e in R for _, dn in DES) + ' |'); P('|---|' + '---|'*(2*len(R)))
    for k in (ROWS if rows is None else rows):
        if k == 'flat' or not have(k) or key not in A['rows'][k]['effect']['rls']: continue
        P('| %s | ' % LAB[k] + ' | '.join((eusd(R[e]['rows'][k]['effect'][d2][key]) if usdf else eff(R[e]['rows'][k]['effect'][d2][key], d, sc)) for e, _ in ENVS if e in R for d2, _ in DES) + ' |')
    P('')
def levels(key, d=2, rows=('p1', 'main')):
    return '; '.join('%s %s' % (n, ', '.join('%s %.*f' % (r, d, R[e]['rows'][r]['mean']['none'][key]) for r in rows if r in R[e]['rows'])) for e, n in ENVS if e in R)
table('## 2. Primary outcome (ii): the programme\'s effect on the top 1% share of wealth at year 20 (points)', 'wtT1E', note='Top 1% share with no programme at year 20 (%): ' + levels('wtT1E') + '.')
table('## 3. The programme\'s effect on the top 0.1% share of wealth at year 20 (points)', 'wtT01E', note='With no programme (%): ' + levels('wtT01E') + '.')
table('## 4. The programme\'s effect on the top 10% share of wealth at year 20 (points)', 'wtT10E', note='With no programme (%): ' + levels('wtT10E') + '.')
table('## 5. The programme\'s effect on the bottom 50% share of wealth at year 20 (points)', 'wtB50E', note='With no programme (%): ' + levels('wtB50E') + '.')
table('## 6. The programme\'s effect on the wealth Gini, debts kept, at year 20', 'wtGnE', 3, note='With no programme: ' + levels('wtGnE', 3) + '. With debts counted as zero the effects are in summary.json (`wtGzE`).')
table('## 7. The programme\'s effect on the top 1% of adults\' share of private-business equity at year 20 (points)', 'rtBt1E', rows=[k for k in ROWS if k != 'off'], note='With no programme (%): ' + levels('rtBt1E') + '; at the start: ' + levels('rtBt1S') + '.')
table('## 8. The programme\'s effect on wealth poverty at year 20 (points; adults under $25,000 of real wealth, weighted)', 'wtPovE', note='With no programme (%): ' + levels('wtPovE', 1, ('off', 'p1', 'main')) + '.')
table('## 9. The programme\'s effect on median real wealth at year 20 (Year-0 dollars, weighted)', 'wtMedE', usdf=True)
table('## 10. The programme\'s effect on basket poverty (points of adult-years; unweighted, the engine\'s own measure)', 'fgt0PY', note='Weighted, at year 20 (`wtF0E`), in summary.json. With no programme (% of adult-years): ' + levels('fgt0PY', 1, ('off', 'p1', 'r2', 'main')) + '.')
table('## 11. Programme inflation (points a year)', 'endoAnn', 2, 100.0)
# 12. check 2
P('## 12. Check 2: does the tail move the economy? The programme\'s effect with the tail less the effect without it, same seeds'); P('')
P('"Tail only" against part 1\'s reading, and the main reading against the same reading without the tail (r2). The preregistered rule: programme inflation, the cost of living and unweighted basket poverty must differ by less than their intervals. Each difference is followed in square brackets by the half-width of the interval of the effect itself under the reading without the tail. The unweighted poverty measures count the tail\'s adults as ordinary adults (about 18 of 500 where the population has 2.6%), so they also move through who is counted; the weighted year-20 measures are given beside them.'); P('')
P('| Comparison | Outcome | ' + ' | '.join('%s, %s' % (n, dn) for e, n in ENVS if e in R for _, dn in DES) + ' |'); P('|---|---|' + '---|'*(2*len(R)))
SUM['check2'] = {}
for r1, r0 in (('tailonly', 'p1'), ('main', 'r2')):
    if not (have(r1) and have(r0)): continue
    for k, lab, d, s in (('endoAnn', 'programme inflation (points a year)', 3, 100.0), ('hhCostPY', 'adults below the cost of living (points of adult-years, unweighted)', 2, 1.0), ('fgt0PY', 'basket poverty (points of adult-years, unweighted)', 2, 1.0), ('wtF0E', 'basket poverty at year 20, weighted (points)', 2, 1.0), ('wtPovE', 'wealth poverty at year 20, weighted (points)', 2, 1.0), ('pLev20', 'price level at year 20 (ratio to Year 0)', 2, 1.0)):
        if k not in R[next(iter(R))]['rows'][r1]['seeds']['rls']: continue
        c = {e: {d2: diff2(e, r1, r0, d2, k) for d2, _ in DES} for e in R}; SUM['check2']['%s-%s.%s' % (r1, r0, k)] = c
        P('| %s less %s | %s | ' % (r1, r0, lab) + ' | '.join('%s [%.*f]' % (eff(c[e][d2], d, s), d, (R[e]['rows'][r0]['effect'][d2][k]['hi'] - R[e]['rows'][r0]['effect'][d2][k]['lo'])/2*s) for e, _ in ENVS if e in R for d2, _ in DES) + ' |')
P('')
# 13. capital income and owners
P('## 13. Business owners and the income wealth pays (no programme unless said; Year-0 dollars per adult)'); P('')
P('| Environment | Reading | owners among adults, start (%) | in the bottom half of money income (%) | in the top tenth (%) | capital income per adult, start | year 20 | share of money income, year 20 (%) | sole-proprietorship income inside owners\' earnings, per adult |'); P('|---|---|---|---|---|---|---|---|---|')
for e, n in ENVS:
    if e not in R: continue
    for r in ('r2', 'main', 'bo0', 'ci0'):
        if r not in R[e]['rows']: continue
        a = R[e]['rows'][r]['mean']['none']; P('| %s | %s | %.1f | %.1f | %.1f | %s | %s | %.1f | %s |' % (n, r, a['rtOwnS'], a['rtOwnLoS'], a['rtOwnHiS'], usd(a['rtYkS']), usd(a['rtYkE']), a['rtYkShE'], usd(a['rtYbE'])))
P(''); P('SCF 2022: 14.7% of the engine\'s families hold private-business equity; of all families 14.6%, 8.3% in the bottom half of income and 41.0% in the top tenth (the Bulletin\'s 20%, 14% and "nearly half" also count the self-employed without business equity). The engine\'s own unweighted income Gini (`giniD`) and wealth Ginis (`eGiniW`, `eGiniWN`) are not valid where the tail is on; the weighted keys are.'); P('')
table('**The programme\'s effect on capital income per adult at year 20 (Year-0 dollars)**', 'rtYkE', rows=[k for k in ('r2', 'main', 'chi1', 'ix05') if k in ROWS], usdf=True)
P('**Shares of the last year\'s real gains on real assets received by the top 1% and top 10% of adults ranked by disposable income plus those gains (%)** (Campbell, Robbins and Wylde 2025 report 45.3% and 75.7% of capital gains for 2002-2021 on a comparable ranking; a comparison, not a target)'); P('')
P('| Reading | ' + ' | '.join('%s: none / release / C2.2' % n for e, n in ENVS if e in R) + ' |'); P('|---|' + '---|'*len(R))
for r in ('p1', 'r2', 'main', 'rg', 'a135', 'a163'):
    if not have(r): continue
    P('| %s | ' % LAB[r] + ' | '.join(' / '.join('%.1f and %.1f' % (R[e]['rows'][r]['mean'][d2]['rtGt1E'], R[e]['rows'][r]['mean'][d2]['rtGt10E']) for d2 in ('none', 'rls', 'c22')) for e, _ in ENVS if e in R) + ' |')
P('')
table('## 14. The programme\'s effect on the top 1% share of disposable income at year 20 (points)', 'dmYt1E', rows=[k for k in ('off', 'p1', 'r2', 'main', 'ci0', 'chi1', 'ix05', 'ownW', 'ownE') if k in ROWS], note='With no programme (%): ' + levels('dmYt1E', 2, ('p1', 'r2', 'main')) + '. Top 10% share with no programme (%): ' + levels('dmYt10E', 2, ('p1', 'r2', 'main')) + '.')
table('**Top 10% share of disposable income (points)**', 'dmYt10E', rows=[k for k in ('off', 'p1', 'r2', 'main', 'ci0', 'ownW', 'ownE') if k in ROWS])
# 15. three parts
P('## 15. The programme\'s effect on mean real wealth in three parts (Year-0 dollars per adult, weighted)'); P('')
P('E: the opening nominal position held untouched. V: the opening real assets held untouched. S: saving since the start and what it earned (capital income that is saved is here).'); P('')
for e, n in ENVS:
    if e not in R: continue
    P('**%s**' % n); P(''); P('| Reading | Design | Group | E | V | S | Whole |'); P('|---|---|---|---|---|---|---|')
    for r in ('p1', 'p1chi', 'r2', 'main', 'chi1', 'ix05'):
        if r not in R[e]['rows']: continue
        for d2, dn in DES:
            x = R[e]['rows'][r]['effect'][d2]
            for q, qn in [('', 'all adults')] + ([(str(i), 'fifth %d of starting wealth' % i) for i in range(1, 6)] if r == 'main' else []):
                W = x['rtE' + q]['m'] + x['rtV' + q]['m'] + x['rtS' + q]['m']
                P('| %s | %s | %s | %s | %s | %s | %s |' % (r if not q else '', dn if not q else '', qn, eusd(x['rtE' + q]), eusd(x['rtV' + q]), eusd(x['rtS' + q]), ('+' if W >= 0 else '') + usd(W)))
    P('')
# 16. owners readings
if have('ownW') and have('r2'):
    P('## 16. The owners readings (no tail): owners keep the private premium, against the release reading (lower prices for customers)'); P('')
    P('Each cell: the programme\'s effect under the reading, and in brackets the reading less r2 on the same seeds.'); P('')
    SUM['owners'] = {}
    for k, lab, d in (('wtT1E', 'top 1% share of wealth (points)', 2), ('wtT10E', 'top 10% share of wealth (points)', 2), ('wtGnE', 'wealth Gini, debts kept', 3), ('rtBt1E', 'top 1% share of business equity (points)', 2), ('wtPovE', 'wealth poverty (points)', 2), ('dmYt1E', 'top 1% share of disposable income (points)', 2), ('fgt0PY', 'basket poverty (points of adult-years)', 2)):
        P('**%s**' % lab); P(''); P('| Reading | ' + ' | '.join('%s, %s' % (n, dn) for e, n in ENVS if e in R for _, dn in DES) + ' |'); P('|---|' + '---|'*(2*len(R)))
        P('| r2: lower prices (release reading) | ' + ' | '.join(eff(R[e]['rows']['r2']['effect'][d2][k], d) for e, _ in ENVS if e in R for d2, _ in DES) + ' |')
        for r in ('ownW', 'ownE'):
            c = {e: {d2: diff2(e, r, 'r2', d2, k) for d2, _ in DES} for e in R}; SUM['owners']['%s.%s' % (r, k)] = c
            P('| %s | ' % LAB[r] + ' | '.join('%s [%s]' % (eff(R[e]['rows'][r]['effect'][d2][k], d), eff(c[e][d2], d)) for e, _ in ENVS if e in R for d2, _ in DES) + ' |')
        P('')
# 17. part 1 beside its correction
if P1 and have('p1'):
    P('## 17. Part 1\'s rows again with the corrected wealth-group edges, beside the Nov 10 pilot (the programme\'s effect on wealth poverty, points)'); P('')
    P('| Row | ' + ' | '.join('%s, %s' % (n, dn) for e, n in ENVS if e in R for _, dn in DES) + ' |'); P('|---|' + '---|'*(2*len(R)))
    O = {e: json.load(open(os.path.join(P1, 's59-assets-%s.json' % e))) for e in R}
    for lab, src, r, key in (('all wealth is cash, Nov 10', O, 'off', 'pov'), ('all wealth is cash, this pilot', R, 'off', 'pov'), ('main reading, Nov 10 (edges 9.4% too high)', O, 'main', 'pov'), ('main reading, corrected edges', R, 'p1', 'pov'),
                              ('fixed-rate debt reprices, Nov 10', O, 'chi1', 'pov'), ('fixed-rate debt reprices, corrected edges', R, 'p1chi', 'pov')):
        if not all(r in src[e]['rows'] for e in R): continue
        P('| %s | ' % lab + ' | '.join(eff(src[e]['rows'][r]['effect'][d2][key]) for e, _ in ENVS if e in R for d2, _ in DES) + ' |')
    P('')
    SUM['part1'] = {e: {r: {d2: O[e]['rows'][r]['effect'][d2]['pov'] for d2, _ in DES} for r in ('off', 'main', 'chi1') if r in O[e]['rows']} for e in R}
os.makedirs(os.path.dirname(os.path.abspath(OUT)), exist_ok=True)
open(OUT, 'w').write('\n'.join(L) + '\n'); json.dump(SUM, open(os.path.join(os.path.dirname(os.path.abspath(OUT)), 'summary.json'), 'w'))
print('wrote %s (%d lines) and summary.json; environments: %s' % (OUT, len(L), ', '.join(R.keys())))
