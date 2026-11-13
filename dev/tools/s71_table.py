#!/usr/bin/env python3
"""S71 (Nov 13, 2026; research-update prereg/2026-11-s71-creditor-side.md): tables of the creditor-side pilot, from the files dev/tools/s71_creditors.js writes.
Usage: python3 dev/tools/s71_table.py DIR [OUT.md] [--s59=DIR59]
  DIR holds s71-creditors-ENV.json for ENV = ref, adv, st, or chunks s71-creditors-ENV-1.json, -2.json, ... (merged first: same engine, seeds and rows,
  so merging changes no figure). Default OUT dev/runs/s71-creditors/tables.md; also writes summary.json beside OUT (means and paired effects, no per-seed values).
  --s59: the folder of S59's pilot (compassionism-sim-results s59-tail-62a189b): the rows main and chi1 must equal its per-seed values (cr is off in them).
Analysis only. Intervals: the 2.5th-97.5th percentile of 2,000 paired bootstrap replicates over seeds (fixed generator), unadjusted."""
import glob, json, os, sys
import numpy as np
ARGS = [a for a in sys.argv[1:] if not a.startswith('--')]; D = ARGS[0]
OUT = ARGS[1] if len(ARGS) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'runs', 's71-creditors', 'tables.md')
S59 = ([a[6:] for a in sys.argv[1:] if a.startswith('--s59=')] or [None])[0]
ENVS = [('ref', 'Reference'), ('adv', 'Adverse'), ('st', 'Stress')]; DES = [('rls', 'release'), ('c22', 'C2.2')]
def load(d, stem):
    R = {}
    for e, _ in ENVS:
        f = os.path.join(d, '%s-%s.json' % (stem, e)); ch = sorted(glob.glob(os.path.join(d, '%s-%s-*.json' % (stem, e))), key=lambda p: int(p.rsplit('-', 1)[1][:-5]))
        if ch:
            parts = [json.load(open(p)) for p in ch]; m = dict(parts[0]['_meta']); m['rows'] = [r for q in parts for r in q['_meta']['rows']]; m['chunks'] = [q['_meta']['command'] for q in parts]
            m['seconds'] = sum(q['_meta']['seconds'] for q in parts); m['command'] = 'in chunks: see chunks'
            assert len({json.dumps(q['_meta']['manifest'], sort_keys=True) for q in parts}) == 1, 'chunks from different engines'
            rows = {}
            for q in parts: rows.update(q['rows'])
            R[e] = {'_meta': m, 'rows': rows}
            if stem.startswith('s71'): json.dump(R[e], open(f, 'w'))
        elif os.path.exists(f): R[e] = json.load(open(f))
    return R
R = load(D, 's71-creditors'); L = []; P = L.append
def boot(d):
    d = np.asarray(d, float); g = np.random.default_rng(20261113); b = d[g.integers(0, len(d), (2000, len(d)))].mean(1); return float(d.mean()), float(np.quantile(b, 0.025)), float(np.quantile(b, 0.975))
def eff(e, row, des, k):
    r = R[e]['rows'][row]; return np.asarray(r['seeds'][des][k]) - np.asarray(r['seeds']['none'][k])
def cell(x, dp=2): return ('%+.' + str(dp) + 'f (%+.' + str(dp) + 'f to %+.' + str(dp) + 'f)') % x
CRR = [('cr', 'main: pass'), ('crhold', 'holders of record'), ('crhedge', 'shareholders not charged'), ('crpop', 'model = all households'), ('crall', 'nothing outside'), ('cru', 'unweighted totals')]
FIVE = ['cr', 'crhold', 'crhedge', 'crpop', 'crall']
m0 = R[ENVS[0][0]]['_meta']; man = m0.get('manifest', {})
P('# S71: the creditor side, pilot tables'); P('')
P('Seeds 1-%d, 500 adults, %d years. Engine commit `%s`%s. Programme minus no programme on the same seeds; 95%% intervals from 2,000 paired bootstrap replicates, unadjusted. Weighted measures. A pilot is a mechanism check, not a result.' % (m0['seeds'], m0['years'], str(man.get('commit', '?'))[:7], '' if not man.get('dirty') else ' (dirty worktree)')); P('')
P('Coefficients (sources/s71_creditors.py): `%s`' % json.dumps(m0.get('creditor'))); P('')
summ = {'meta': {'seeds': m0['seeds'], 'years': m0['years'], 'commit': man.get('commit')}, 'ledger': {}, 'effects': {}, 'diff': {}, 'bounds': {}, 'direction': {}, 'checks': {}}

P('## 1. The ledger: where a dollar of debt relief is lost (Year-0 dollars per adult, summed over the run; share of relief in brackets)'); P('')
LK = [('crRel', 'debt inflated away'), ('crBook', 'on the books already'), ('crNom', 'new charge, nominal assets'), ('crEq', 'new charge, shares'), ('crOutG', 'outside: government'), ('crOutF', 'outside: foreigners'),
      ('crOutH', 'outside: households not in the model'), ('crOutS', 'outside: lenders\' shareholders, not charged'), ('crUn', 'unplaced'), ('crGap', 'ledger gap')]
maxgap = 0.0; maxun = 0.0
for e, en in ENVS:
    if e not in R: continue
    for des, dn in [('none', 'no programme')] + DES:
        P('**%s, %s**' % (en, dn)); P(''); P('| | ' + ' | '.join(n for _, n in CRR) + ' |'); P('|---|' + '---|'*len(CRR))
        for k, kn in LK:
            cells = []
            for row, _ in CRR:
                mn = R[e]['rows'][row]['mean'][des]; rel = mn['crRel']
                if k == 'crGap':
                    g = max(abs(a)/max(1.0, abs(b)) for a, b in zip(R[e]['rows'][row]['seeds'][des]['crGap'], R[e]['rows'][row]['seeds'][des]['crRel'])); maxgap = max(maxgap, g); cells.append('%.1e of relief at most' % g)
                else:
                    if k == 'crUn': maxun = max(maxun, abs(mn[k])/max(1.0, abs(rel)))
                    cells.append('%s (%.1f%%)' % ('{:,.0f}'.format(mn[k]), 100*mn[k]/rel if rel else 0) if k != 'crRel' else '{:,.0f}'.format(mn[k]))
                summ['ledger'].setdefault(e, {}).setdefault(des, {}).setdefault(row, {})[k] = mn[k]
            P('| %s | ' % kn + ' | '.join(cells) + ' |')
        P('')
summ['checks']['max_gap_over_relief'] = maxgap; summ['checks']['max_unplaced_over_relief'] = maxun

P('## 2. Who bears the new charges, and who gets the relief (Year-0 dollars per adult in each fifth of starting wealth, summed over the run; main creditor reading)'); P('')
for e, en in ENVS:
    if e not in R: continue
    P('**%s**' % en); P(''); P('| | Poorest fifth | 2nd | 3rd | 4th | Richest fifth | Top 1%\'s share of new charges |'); P('|---|---|---|---|---|---|---|')
    for des, dn in [('none', 'no programme')] + DES:
        mn = R[e]['rows']['cr']['mean'][des]
        P('| %s: relief | ' % dn + ' | '.join('{:,.0f}'.format(mn['crR%d' % q]) for q in range(1, 6)) + ' | |')
        P('| %s: new charges | ' % dn + ' | '.join('{:,.0f}'.format(mn['crN%d' % q]) for q in range(1, 6)) + ' | %.1f%% |' % mn['crT1'])
    P('')
P('Top 1%\'s share of new charges (by starting wealth), each reading, release design: ' + '; '.join('%s %s' % (en, ', '.join('%s %.1f%%' % (row, R[e]['rows'][row]['mean']['rls']['crT1']) for row, _ in CRR)) for e, en in ENVS if e in R)); P('')

OUTC = [('wtPovE', 'Wealth poverty, year 20 (points)', 2), ('wtT01E', 'Top 0.1% share of wealth (points)', 2), ('wtT1E', 'Top 1% share of wealth (points)', 2), ('wtT10E', 'Top 10% share (points)', 2), ('wtB50E', 'Bottom 50% share (points)', 2),
        ('wtGnE', 'Wealth Gini', 3), ('wtMedE', 'Median real wealth (Year-0 dollars)', 0), ('wtMeanE', 'Mean real wealth (Year-0 dollars)', 0), ('rtE', 'Real wealth: opening nominal position', 0), ('rtV', 'Real wealth: opening real assets', 0), ('rtS', 'Real wealth: saving since', 0),
        ('wtF0E', 'Income below the basket, year 20 (points)', 2), ('fgt0PY', 'Below the cost of living, adult-years (points; unweighted)', 2), ('endoAnn', 'Yearly inflation (points; unweighted)', 3)]
ROWS = [('main', 'S59 main (bound 1)'), ('chi1', 'no debt relief (bound 2)')] + [(r, 'creditor side, ' + n) for r, n in CRR] + [('r2', 'no tail, no creditor side'), ('r2cr', 'no tail, creditor side')]
P('## 3. The programme\'s effect under each reading'); P('')
for k, kn, dp in OUTC:
    P('**%s**' % kn); P(''); P('| Reading | ' + ' | '.join('%s, %s' % (en, dn) for e, en in ENVS if e in R for _, dn in DES) + ' |'); P('|---|' + '---|'*(2*len([1 for e, _ in ENVS if e in R])))
    for row, rn in ROWS:
        cells = []
        for e, en in ENVS:
            if e not in R: continue
            for des, _ in DES:
                if k not in R[e]['rows'][row]['seeds'][des]: cells.append(''); continue
                x = boot(eff(e, row, des, k)); cells.append(cell(x, dp)); summ['effects'].setdefault(k, {}).setdefault(row, {})['%s.%s' % (e, des)] = x
        P('| %s | ' % rn + ' | '.join(cells) + ' |')
    P('')

P('## 4. What the creditor side changes: each creditor reading less S59\'s main reading (difference of paired effects)'); P('')
for k, kn, dp in OUTC[:8]:
    P('**%s**' % kn); P(''); P('| Reading | ' + ' | '.join('%s, %s' % (en, dn) for e, en in ENVS if e in R for _, dn in DES) + ' |'); P('|---|' + '---|'*(2*len([1 for e, _ in ENVS if e in R])))
    for row, rn in CRR + [('chi1', 'no debt relief (for scale)')]:
        cells = []
        for e, en in ENVS:
            if e not in R: continue
            for des, _ in DES:
                x = boot(eff(e, row, des, k) - eff(e, 'main', des, k)); cells.append(cell(x, dp)); summ['diff'].setdefault(k, {}).setdefault(row, {})['%s.%s' % (e, des)] = x
        P('| %s | ' % rn + ' | '.join(cells) + ' |')
    x = [boot(eff(e, 'r2cr', des, k) - eff(e, 'r2', des, k)) for e, _ in ENVS if e in R for des, _ in DES]
    P('| without the tail (r2cr less r2) | ' + ' | '.join(cell(v, dp) for v in x) + ' |'); P('')

P('## 5. Preregistered rules'); P('')
P('**Rule 1 (checks).** Largest ledger gap in any seed of any row: %.1e of the relief (limit 1e-6): %s. Largest unplaced share of relief (row means): %.4f%% (limit 5%%): %s.' % (maxgap, 'pass' if maxgap < 1e-6 else 'FAIL', 100*maxun, 'pass' if maxun < 0.05 else 'FAIL')); P('')
if S59:
    R59 = load(S59, 's59-tail'); bad = []; n = 0
    for e, _ in ENVS:
        if e not in R or e not in R59: bad.append(e + ' missing'); continue
        for row in ('main', 'chi1', 'r2'):
            for des in ('none', 'rls', 'c22'):
                a = R[e]['rows'][row]['seeds'][des]; b = R59[e]['rows'][row]['seeds'][des]
                for k in b:
                    n += 1
                    if k not in a or any(x != y for x, y in zip(a[k], b[k])): bad.append('%s.%s.%s.%s' % (e, row, des, k))
    summ['checks']['equals_s59'] = not bad; summ['checks']['equals_s59_compared'] = n
    P('**Check: the rows without the creditor side equal S59\'s per-seed files** (main, chi1, r2; every key S59 kept; %d series): %s.' % (n, 'identical' if not bad else 'DIFFERENT: ' + ', '.join(bad[:10]))); P('')
P('**Rule 2 (direction of the effect on the top 1% share).** Established for a design only if the effect has one sign with a 95% interval excluding zero in all five creditor readings in all three environments.'); P('')
for des, dn in DES:
    signs = {}
    for row in FIVE:
        for e, en in ENVS:
            if e not in R: continue
            m, lo, hi = boot(eff(e, row, des, 'wtT1E')); signs['%s.%s' % (row, e)] = -1 if hi < 0 else (1 if lo > 0 else 0)
    v = set(signs.values()); est = len(v) == 1 and 0 not in v
    summ['direction'][des] = {'established': est, 'signs': signs}
    word = {1: 'raises', -1: 'lowers', 0: 'interval includes zero'}
    P('- %s: %s.' % (dn, ('established: the programme %s the top 1%% share in every creditor reading and environment' % ('lowers' if v == {-1} else 'raises')) if est else 'not established: ' + '; '.join('%s in %s' % (word[t], ', '.join(k for k, q in signs.items() if q == t)) for t in sorted(v))))
P('')
P('**Rule 3 (bounds).** Does each creditor reading\'s effect lie between S59\'s two readings (means)? Cells list the readings outside.'); P('')
P('| Outcome | ' + ' | '.join('%s, %s' % (en, dn) for e, en in ENVS if e in R for _, dn in DES) + ' |'); P('|---|' + '---|'*(2*len([1 for e, _ in ENVS if e in R])))
for k, kn, dp in OUTC[:8]:
    cells = []
    for e, en in ENVS:
        if e not in R: continue
        for des, _ in DES:
            a = float(eff(e, 'main', des, k).mean()); b = float(eff(e, 'chi1', des, k).mean()); lo, hi = min(a, b), max(a, b); outs = []
            for row in FIVE:
                x = float(eff(e, row, des, k).mean())
                if x < lo or x > hi: outs.append('%s (%s main)' % (row, 'beyond' if abs(x - a) < abs(x - b) else 'beyond no-relief'))
            summ['bounds'].setdefault(k, {})['%s.%s' % (e, des)] = outs; cells.append('all inside' if not outs else ', '.join(outs))
    P('| %s | ' % kn + ' | '.join(cells) + ' |')
P('')
open(OUT, 'w').write('\n'.join(L) + '\n'); json.dump(summ, open(os.path.join(os.path.dirname(OUT), 'summary.json'), 'w'), indent=1)
print('wrote %s (%d lines)' % (OUT, len(L)))
