"""S58 (Nov 9, 2026): tables for the capacity price rule pilot (research-update prereg/2026-11-s58-price-rule.md, Outcomes and Amendment 1).
Reads the per-seed files written by dev/tools/s58_price.js (s58-price-ref.json, -adv, -st in one directory) and writes tables.md and estimates.csv there.
Estimates: (a) the programme's effect, the row minus the no-programme run (np) on the same seed; (b) the rule's difference, a capacity row minus the same design
under today's rule (rel or c22) on the same seed. Mean of the paired differences; 95% percentile interval of a paired bootstrap over seeds (2,000 replicates,
resampler seed 58, the same resample for every cell). Family: exploratory (pilot); intervals not adjusted; Holm at 5% within the family (the p-value from the
normal tail of the mean over its bootstrap standard error, as S57 Amendment 1), counted at the end. Price levels are read in logs (ln pLev20). Standard library only.
Usage: python3 dev/tools/s58_table.py DIR [--reps N]"""
import json, os, sys, random, math, csv

ENVS = [('ref', 'Reference'), ('adv', 'Adverse'), ('st', 'Stress')]
PROG = ['rel', 'rel-cap', 'rel-k25', 'c22', 'c22-cap', 'c22-k25', 'c22-k1', 'c22-r0', 'c22-r45', 'c22-a0', 'c22-h', 'c22-k2z', 'c22-k2h', 'c22-nest']
LABEL = {'np': 'no programme', 'rel': 'release, today\'s rule', 'rel-cap': 'release, capacity rule', 'rel-k25': 'release, capacity, k 0.25', 'c22': 'C2.2, today\'s rule',
         'c22-cap': 'C2.2, capacity rule', 'c22-k25': 'C2.2, k 0.25', 'c22-k1': 'C2.2, k 1', 'c22-r0': 'C2.2, r 0', 'c22-r45': 'C2.2, r 0.45', 'c22-a0': 'C2.2, a 0',
         'c22-h': 'C2.2, slack 0.0446', 'c22-k2z': 'C2.2, k2 0', 'c22-k2h': 'C2.2, k2 0.657', 'c22-nest': 'C2.2, nesting point'}
BASEQ = lambda r: 'rel' if r.startswith('rel') else 'c22'
MF = [('mfIss', 'BU issued'), ('mfBU', 'BU spent at face value'), ('mfCvG', 'conversion, gross'), ('mfTax', 'conversion tax withheld'), ('mfCvN', 'conversion paid, net'),
      ('mfPay', 'the Source\'s payout (BU at face + net conversion)'), ('mfM', 'output matched to it'), ('mfU', 'new money U'), ('mfCut', 'price cuts paid (outside U)'),
      ('mfPth', 'PTH appreciation credited'), ('mfReSp', 'tax re-spent'), ('mfY', 'cash income Y'), ('mfUY', 'U/Y, mean of years (%)'), ('mfTaxSh', 'tax / gross conversion (%)'),
      ('mfChk', 'identity gap |U - (payout - matched)|')]
REPS = 2000

def mean(v): return sum(v)/len(v) if v else float('nan')
def pct(b, q): return b[min(len(b) - 1, max(0, int(round(q*(len(b) - 1)))))]

def main():
    A = [a for a in sys.argv[1:] if not a.startswith('--')]; D = A[0]
    reps = int(sys.argv[sys.argv.index('--reps') + 1]) if '--reps' in sys.argv else REPS
    R = {e: json.load(open(os.path.join(D, 's58-price-%s.json' % e))) for e, _ in ENVS if os.path.exists(os.path.join(D, 's58-price-%s.json' % e))}
    if not R: sys.exit('no s58-price-*.json in ' + D)
    n = len(next(iter(R.values()))['rows']['np']['pov']); rnd = random.Random(58)
    idx = [[rnd.randrange(n) for _ in range(n)] for _ in range(reps)]
    def est(x):
        b = sorted(mean([x[i] for i in ix]) for ix in idx); mb = mean(b); se = math.sqrt(sum((t - mb)**2 for t in b)/(len(b) - 1)); mm = mean(x)
        return {'m': mm, 'lo': pct(b, 0.025), 'hi': pct(b, 0.975), 'p': math.erfc(abs(mm)/(se*math.sqrt(2))) if se > 0 else (0.0 if mm != 0 else 1.0)}
    def val(env, row, k):
        v = R[env]['rows'][row].get(k)
        if v is None: return None
        return [math.log(z) for z in v] if k == 'pLev20' else [z*100 for z in v] if k == 'endoAnn' else v
    def dif(env, a, b, k):
        x, y = val(env, a, k), val(env, b, k)
        return None if x is None or y is None else est([p - q for p, q in zip(x, y)])
    cells, out, csvrows = [], [], []
    def cell(env, row, kind, k, e):
        if e is None: return 'n/a'
        cells.append(e); csvrows.append([env, row, kind, k, e['m'], e['lo'], e['hi'], e['p']]); return '%s [%s, %s]' % (f(e['m']), f(e['lo']), f(e['hi']))
    def f(v): return ('%.0f' % v) if abs(v) >= 1000 else ('%.2f' % v) if abs(v) >= 1 else ('%.3f' % v)
    meta = next(iter(R.values()))['_meta']
    out.append('# S58 pilot tables: the capacity price rule\n')
    out.append('Seeds 1-%d, 500 adults, %d years, frozen yardstick, engine %s; rule defaults %s. Every interval is the 95%% paired-bootstrap interval over seeds (%d replicates, resampler seed 58). Family: exploratory (pilot); intervals not adjusted; the Holm count is at the end.\n'
               % (n, meta['years'], meta['manifest'].get('commit', '?')[:7], json.dumps({k: (round(v, 4) if isinstance(v, float) else v) for k, v in meta['defaults'].items()}), reps))
    # checks
    out.append('## 1. Checks (decision rule 1)\n')
    for env, nm in ENVS:
        if env not in R: continue
        rr = R[env]['rows']; same = [k for k in rr['np'] if not k.startswith(('pr', 'mf')) and k in rr['np-cap'] and rr['np'][k] != rr['np-cap'][k]]
        nest = max(abs(a/b - 1) for a, b in zip(rr['c22-nest']['pLev20'], rr['c22']['pLev20']))
        chk = max(max(rr[r]['mfChk']) for r in ['rel', 'rel-cap', 'c22', 'c22-cap'])
        out.append('- %s: the no-programme run under the capacity rule differs from today\'s on %d keys (of %d); the nesting point\'s year-20 price level differs from today\'s rule by at most %.1e (relative); the money-flow identity gap is at most %.1e dollars per adult-year.'
                   % (nm, len(same), len([k for k in rr['np'] if not k.startswith(('pr', 'mf'))]), nest, chk))
    out.append('')
    # table 2: prices
    out.append('## 2. Prices (primary)\n')
    out.append('Programme inflation in points a year (the row\'s yearly rate of its own price index, `endoAnn`, beside the environment\'s outside inflation, which is the same in every row), the year-20 price level (geometric mean over seeds), and general pass-through (ln P_G over the log of the money-implied level, after 3 and 19 years). "Rule difference": the capacity row minus the same design under today\'s rule, paired; for the log price level, ln(capacity/today).\n')
    out.append('| Row | Environment | Inflation, points a year | Year-20 price level | Pass-through, year 3 | Pass-through, year 19 | Rule difference: inflation | Rule difference: ln price level |\n|---|---|---|---|---|---|---|---|')
    for r in ['np'] + PROG:
        for env, nm in ENVS:
            if env not in R: continue
            rr = R[env]['rows'][r]; gl = math.exp(mean([math.log(z) for z in rr['pLev20']]))
            cap = r not in ('np', 'rel', 'c22')
            d1 = cell(env, r, 'rule', 'endoAnn', dif(env, r, BASEQ(r), 'endoAnn')) if cap else ''
            d2 = cell(env, r, 'rule', 'lnP20', dif(env, r, BASEQ(r), 'pLev20')) if cap else ''
            out.append('| %s | %s | %.1f | %s | %.3f | %.3f | %s | %s |' % (LABEL[r], nm, mean(val(env, r, 'endoAnn')), f(gl), mean(rr['prPT3']), mean(rr['prPT19']), d1, d2))
    out.append('')
    # table 3: effects
    out.append('## 3. The programme\'s effects (secondary)\n')
    out.append('Programme minus no programme on the same seed: basket poverty (`fgt0PY`, points), wealth poverty (`pov`, points), the cost-of-living measure (`hhCostPY`, points), median real wealth (`medWealthReal`, year-0 dollars); at shadow prices, median real wealth and wealth poverty of the programme row against the no-programme run (whose shadow ratio is 1). Below each capacity row, the rule difference (the capacity row minus the same design under today\'s rule).\n')
    K3 = [('fgt0PY', 'Basket poverty'), ('pov', 'Wealth poverty'), ('hhCostPY', 'Cost of living'), ('medWealthReal', 'Median real wealth')]
    out.append('| Row | Environment | ' + ' | '.join(l for _, l in K3) + ' | Median real wealth at shadow prices | Wealth poverty at shadow prices |\n|---|---|' + '---|'*(len(K3) + 2))
    for r in PROG:
        for env, nm in ENVS:
            if env not in R: continue
            rr, np_ = R[env]['rows'][r], R[env]['rows']['np']
            cs = [cell(env, r, 'effect', k, dif(env, r, 'np', k)) for k, _ in K3]
            cs.append(cell(env, r, 'effect', 'wealthShadow', est([a - b for a, b in zip(rr['prWsh'], np_['medWealthReal'])])))
            cs.append(cell(env, r, 'effect', 'povShadow', est([a - b for a, b in zip(rr['prPovSh'], np_['pov'])])))
            out.append('| %s | %s | %s |' % (LABEL[r], nm, ' | '.join(cs)))
            if r not in ('rel', 'c22'):
                q = BASEQ(r); qq = R[env]['rows'][q]
                cs = [cell(env, r, 'rule', k, dif(env, r, q, k)) for k, _ in K3]
                cs.append(cell(env, r, 'rule', 'wealthShadow', est([a - b for a, b in zip(rr['prWsh'], qq['prWsh'])])))
                cs.append(cell(env, r, 'rule', 'povShadow', est([a - b for a, b in zip(rr['prPovSh'], qq['prPovSh'])])))
                out.append('| (rule difference) | %s | %s |' % (nm, ' | '.join(cs)))
    out.append('')
    # table 4: demand and output
    out.append('## 4. Demand, output and shortage (reporting only)\n')
    out.append('Means over the run of: excess demand at the year\'s prices (% of no-pressure output), the part output meets (up to the slack plus the 6.1% stretch), the rationed share (demand no output can meet), the output loss after an overshoot; the last year\'s rationed share and shadow ratio (how far the measured price level sits below one that would clear demand). Means over seeds.\n')
    out.append('| Row | Environment | Excess demand | Output response | Rationed | Output loss | Rationed, last year | Shadow ratio, last year | Recession idle share |\n|---|---|---|---|---|---|---|---|---|')
    for r in PROG:
        for env, nm in ENVS:
            if env not in R: continue
            rr = R[env]['rows'][r]
            out.append('| %s | %s | %.1f | %.2f | %.1f | %.2f | %.1f | %.3f | %.2f |' % (LABEL[r], nm, mean(rr['prX']), mean(rr['prOut']), mean(rr['prRat']), mean(rr['prLoss']), mean(rr['prRatE']), mean(rr['prSh']), mean(rr['prSlk'])))
    out.append('')
    # table 5: money flows
    out.append('## 5. The money-flow table (section 3 of the preregistration)\n')
    out.append('Year-0 dollars per adult-year, means over the run and over seeds (shares in %). The conversion tax is withheld from each payout: gross conversion = net conversion + tax, and U = payout - matched output, so the tax is never in U.\n')
    cols = [(env, r) for env, _ in ENVS if env in R for r in ('rel', 'rel-cap', 'c22', 'c22-cap')]
    out.append('| Line | ' + ' | '.join('%s, %s' % (dict(ENVS)[e], LABEL[r]) for e, r in cols) + ' |\n|---|' + '---|'*len(cols))
    for k, l in MF:
        out.append('| %s | %s |' % (l, ' | '.join(f(mean(R[e]['rows'][r][k])) if k != 'mfChk' else '%.1e' % max(R[e]['rows'][r][k]) for e, r in cols)))
    out.append('')
    # Holm
    ps = sorted(range(len(cells)), key=lambda j: cells[j]['p']); m = len(cells); surv = set(); stop = False
    for rank, j in enumerate(ps):
        if not stop and cells[j]['p'] <= 0.05/(m - rank): surv.add(j)
        else: stop = True
    excl = sum(1 for c in cells if c['lo'] > 0 or c['hi'] < 0)
    out.append('## 6. Counts for the family\n')
    out.append('%d estimates (tables 2 and 3: effects and rule differences). Intervals excluding zero: %d. Surviving Holm within the family at 5%%: %d. Intervals are not adjusted; "excludes zero" is not "material".\n' % (m, excl, len(surv)))
    open(os.path.join(D, 'tables.md'), 'w').write('\n'.join(out) + '\n')
    with open(os.path.join(D, 'estimates.csv'), 'w', newline='') as fh:
        w = csv.writer(fh); w.writerow(['env', 'row', 'kind', 'measure', 'mean_diff', 'lo95', 'hi95', 'p_normal_from_boot_se', 'holm_survives'])
        for j, c in enumerate(csvrows): w.writerow(c + [j in surv])
    print('wrote tables.md and estimates.csv in', D, '; estimates', m, 'exclude zero', excl, 'Holm', len(surv))

main()
