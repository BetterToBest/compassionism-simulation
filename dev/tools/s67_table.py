"""S67 (Nov 13, 2026): tables for the pilot of the price rule's new readings (research-update prereg/2026-11-s67-price-rule-derivation.md, Part C, Outcomes,
Amendment 1). Reads the per-seed files written by dev/tools/s67_price.js (s67-price-ref.json, -adv, -st in one directory) and writes tables.md and estimates.csv
there. Estimates are means of paired differences over seeds (the programme's effect: the row minus the no-programme run; a reading's difference: the row minus
the same design under its base rule) with the 95% percentile interval of a paired bootstrap (2,000 replicates, resampler seed 67, the same resample for every
cell). Family: exploratory (pilot); intervals not adjusted; Holm at 5% within the family (p from the normal tail of the mean over its bootstrap standard error),
counted at the end. The wave: the largest less the smallest yearly inflation over years 5-19, in points. Standard library only.
Usage: python3 dev/tools/s67_table.py DIR [S58_RESULTS_DIR] [--reps N]"""
import json, os, sys, random, math, csv

ENVS = [('ref', 'Reference'), ('adv', 'Adverse'), ('st', 'Stress')]
LABEL = {'np': 'no programme', 'rel': "release, today's rule", 'rel-cap': 'release, capacity rule', 'c22': "C2.2, today's rule", 'c22-cap': 'C2.2, capacity rule',
         'c22-wy': 'C2.2, within-year (quarterly-fitted)', 'c22-wyroot': 'C2.2, within-year (same roots)', 'c22-qt4': "C2.2, today's rule in four sub-steps",
         'c22-vel': 'C2.2, capacity + velocity response 0.0043', 'c22-velh': 'C2.2, capacity + velocity response 0.0022', 'c22-qtvel': "C2.2, today's rule + velocity response 0.0043",
         'c22-drift': 'C2.2, capacity + velocity drift 0.132', 'c22-qtdrift': "C2.2, today's rule + velocity drift 0.132", 'rel-wy': 'release, within-year (quarterly-fitted)',
         'rel-vel': 'release, capacity + velocity response 0.0043', 'rel-drift': 'release, capacity + velocity drift 0.132'}
PROG = [r for r in LABEL if r != 'np']
BASE = {'rel-cap': 'rel', 'c22-cap': 'c22', 'c22-wy': 'c22-cap', 'c22-wyroot': 'c22-cap', 'c22-qt4': 'c22', 'c22-vel': 'c22-cap', 'c22-velh': 'c22-cap', 'c22-qtvel': 'c22',
        'c22-drift': 'c22-cap', 'c22-qtdrift': 'c22', 'rel-wy': 'rel-cap', 'rel-vel': 'rel-cap', 'rel-drift': 'rel-cap'}
S58ROWS = ['np', 'np-cap', 'rel', 'rel-cap', 'c22', 'c22-cap']
REPS = 2000
def mean(v): return sum(v)/len(v) if v else float('nan')
def pct(b, q): return b[min(len(b) - 1, max(0, int(round(q*(len(b) - 1)))))]
def f(v): return ('%.0f' % v) if abs(v) >= 1000 else ('%.2f' % v) if abs(v) >= 1 else ('%.3f' % v)

def main():
    A = [a for a in sys.argv[1:] if not a.startswith('--') and not a.isdigit()]; D = A[0]; D58 = A[1] if len(A) > 1 else None
    reps = int(sys.argv[sys.argv.index('--reps') + 1]) if '--reps' in sys.argv else REPS
    R = {e: json.load(open(os.path.join(D, 's67-price-%s.json' % e))) for e, _ in ENVS if os.path.exists(os.path.join(D, 's67-price-%s.json' % e))}
    if not R: sys.exit('no s67-price-*.json in ' + D)
    meta = next(iter(R.values()))['_meta']; T = meta['years']; n = len(next(iter(R.values()))['rows']['np']['pov']); rnd = random.Random(67)
    idx = [[rnd.randrange(n) for _ in range(n)] for _ in range(reps)]
    cells, out, csvrows = [], [], []
    def est(x):
        b = sorted(mean([x[i] for i in ix]) for ix in idx); mb = mean(b); se = math.sqrt(sum((t - mb)**2 for t in b)/(len(b) - 1)); mm = mean(x)
        return {'m': mm, 'lo': pct(b, 0.025), 'hi': pct(b, 0.975), 'p': math.erfc(abs(mm)/(se*math.sqrt(2))) if se > 0 else (0.0 if mm != 0 else 1.0)}
    def infl(env, row, s): rr = R[env]['rows'][row]; return [100*(rr['plv_%d' % t][s]/rr['plv_%d' % (t - 1)][s] - 1) for t in range(1, T)]
    def val(env, row, k):
        rr = R[env]['rows'][row]
        if k == 'lnP20': return [math.log(z) for z in rr['pLev20']]
        if k == 'endoAnn': return [100*z for z in rr['endoAnn']]
        if k == 'wave': return [max(infl(env, row, s)[4:]) - min(infl(env, row, s)[4:]) for s in range(n)]
        if k in ('povAvg', 'medWAvg', 'f0Avg'): key = {'povAvg': 'ppov_', 'medWAvg': 'pmedW_', 'f0Avg': 'pf0_'}[k]; return [mean([rr[key + str(t)][s] for t in range(T)]) for s in range(n)]
        return rr.get(k)
    def dif(env, a, b, k):
        x, y = val(env, a, k), val(env, b, k)
        return None if x is None or y is None else est([p - q for p, q in zip(x, y)])
    def cell(env, row, kind, k, e):
        if e is None: return 'n/a'
        cells.append(e); csvrows.append([env, row, kind, k, e['m'], e['lo'], e['hi'], e['p']]); return '%s [%s, %s]' % (f(e['m']), f(e['lo']), f(e['hi']))
    def gpath(env, row): rr = R[env]['rows'][row]; L = [mean([math.log(z) for z in rr['plv_%d' % t]]) for t in range(T)]; return [100*(math.exp(L[t] - L[t - 1]) - 1) for t in range(1, T)]
    def gwave(env, row): p = gpath(env, row)[4:]; return max(p) - min(p)
    out.append("# S67 pilot tables: the price rule's new readings\n")
    out.append('Seeds 1-%d, 500 adults, %d years, S58\'s yardstick, engine %s. Every interval is the 95%% paired-bootstrap interval over seeds (%d replicates, resampler seed 67). Family: exploratory (pilot); intervals not adjusted; the Holm count is at the end. Row options: %s.\n'
               % (n, T, meta['manifest'].get('commit', '?')[:7], reps, '; '.join('%s `%s`' % (r['name'], json.dumps(r['pr']).replace('"', '')) for r in meta['rows'] if r['pr'] not in ('qt', True))))
    out.append('## 1. Checks\n')
    for env, nm in ENVS:
        if env not in R: continue
        rr = R[env]['rows']; keys = [k for k in rr['np'] if not k.startswith(('pr', 'mf'))]; same = [k for k in keys if rr['np'][k] != rr['np-cap'][k]]
        chk = max(max(rr[r]['mfChk']) for r in PROG); q4 = max(abs(a/b - 1) for a, b in zip(rr['c22-qt4']['pLev20'], rr['c22']['pLev20']))
        line = "- %s: the no-programme run under the capacity rule differs from today's on %d keys (of %d); today's rule in four sub-steps gives today's year-20 price level within %.1e (relative); the money-flow identity gap is at most %.1e dollars" % (nm, len(same), len(keys), q4, chk)
        if D58 and os.path.exists(os.path.join(D58, 's58-price-%s.json' % env)):
            J = json.load(open(os.path.join(D58, 's58-price-%s.json' % env)))['rows']; bad = tot = 0
            for r in S58ROWS:
                for k, v in J[r].items():
                    if k in rr[r]: tot += len(v); bad += sum(1 for a, b in zip(v, rr[r][k]) if a != b)
            line += "; the six rows S58 also ran reproduce S58's published per-seed values on %d of %d values (%d differ)" % (tot - bad, tot, bad)
        out.append(line + '.')
    out.append('\n## 2. Prices (primary)\n')
    out.append("Programme inflation in points a year (`endoAnn`), the year-20 price level (geometric mean), level pass-through on the money at years 3 and 19, the wave on the geometric-mean path and as the mean of each seed's own wave, the rationed share (mean of years, % of no-pressure output), the last year's shadow ratio, and the within-year average price level over the year's opening level. Difference columns: the row minus its base rule on the same seed (base: today's rule for the capacity rule and the readings on today's rule; the capacity rule for the others).\n")
    out.append('| Row | Environment | Inflation | Year-20 level | Pass-through 3 | Pass-through 19 | Wave, mean path | Wave, per seed | Rationed % | Shadow ratio | Within-year level | Difference: inflation | Difference: pass-through 19 | Difference: wave |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')
    for r in PROG:
        for env, nm in ENVS:
            if env not in R: continue
            rr = R[env]['rows'][r]; b = BASE.get(r)
            out.append('| %s | %s | %.1f | %s | %.3f | %.3f | %.1f | %.1f | %.1f | %.3f | %.3f | %s | %s | %s |' % (LABEL[r], nm, mean(val(env, r, 'endoAnn')), f(math.exp(mean(val(env, r, 'lnP20')))), mean(rr['prPT3']), mean(rr['prPT19']),
                gwave(env, r), mean(val(env, r, 'wave')), mean(rr['prRat']), mean(rr['prSh']), mean(rr['prAvg']),
                cell(env, r, 'reading', 'endoAnn', dif(env, r, b, 'endoAnn')) if b else '', cell(env, r, 'reading', 'prPT19', dif(env, r, b, 'prPT19')) if b else '', cell(env, r, 'reading', 'wave', dif(env, r, b, 'wave')) if b else ''))
    if 'ref' in R:
        w1, w0 = gwave('ref', 'c22-wy'), gwave('ref', 'c22-cap'); x, y = val('ref', 'c22-wy', 'wave'), val('ref', 'c22-cap', 'wave'); e = est([p - 0.5*q for p, q in zip(x, y)])
        out.append("\n**Decision rule 2(b):** the wave of the C2.2 design in Reference is %.1f points under the quarterly-fitted within-year reading against %.1f under the yearly capacity rule on the mean path (ratio %.2f); per seed %.1f against %.1f (ratio of means %.2f; the within-year wave less half the yearly wave: %s). The waves %s a shorter lag by the preregistered test (at least half)." % (
            w1, w0, w1/w0, mean(x), mean(y), mean(x)/mean(y), cell('ref', 'c22-wy', 'rule2b', 'wave - 0.5 wave(cap)', e), 'survive' if w1 >= 0.5*w0 else 'do not survive'))
        e1, e2, e3, e4 = dif('ref', 'c22-vel', 'c22-cap', 'prPT19'), dif('ref', 'c22-qtvel', 'c22', 'prPT19'), dif('ref', 'c22-drift', 'c22-cap', 'prPT19'), dif('ref', 'c22-qtdrift', 'c22', 'prPT19')
        out.append("\n**Decision rule 3:** level pass-through at year 19, C2.2, Reference: the velocity response moves it by %.4f on the capacity rule and %.4f on today's rule (threshold 0.05: %s); the velocity drift (Amendment 1) by %.3f and %.3f (%s)." % (
            e1['m'], e2['m'], 'joins the readings' if max(abs(e1['m']), abs(e2['m'])) > 0.05 else 'reported and dropped', e3['m'], e4['m'], 'joins the readings' if max(abs(e3['m']), abs(e4['m'])) > 0.05 else 'reported and dropped'))
    out.append('\n## 3. The yearly inflation path (%, geometric mean over seeds; year t is the change from year t − 1)\n')
    for env, nm in ENVS:
        if env not in R: continue
        out.append('**%s**\n\n| Row | ' % nm + ' | '.join(str(t) for t in range(1, T)) + ' |\n|---|' + '---|'*(T - 1))
        for r in PROG: out.append('| %s | ' % LABEL[r] + ' | '.join('%.0f' % v for v in gpath(env, r)) + ' |')
        out.append('')
    out.append("## 4. The programme's effects (secondary)\n")
    out.append("Programme minus no programme on the same seed. Basket poverty (`fgt0PY`) and the cost of living (`hhCostPY`) are already averages over the run's adult-years. Wealth poverty and median real wealth are given at year 20 (`pov`, `medWealthReal`) and as the average of the 20 yearly readings (`ppov_*`, `pmedW_*`); then both at shadow prices (year 20).\n")
    K = [('fgt0PY', 'Basket poverty'), ('hhCostPY', 'Cost of living'), ('pov', 'Wealth poverty, year 20'), ('povAvg', 'Wealth poverty, yearly average'), ('medWealthReal', 'Median real wealth, year 20'), ('medWAvg', 'Median real wealth, yearly average'),
         ('prPovSh', 'Wealth poverty at shadow prices'), ('prWsh', 'Median real wealth at shadow prices')]
    out.append('| Row | Environment | ' + ' | '.join(l for _, l in K) + ' |\n|---|---|' + '---|'*len(K))
    for r in PROG:
        for env, nm in ENVS:
            if env in R: out.append('| %s | %s | ' % (LABEL[r], nm) + ' | '.join(cell(env, r, 'effect', k, dif(env, r, 'np', k)) for k, _ in K) + ' |')
    out.append("\n## 5. What each reading changes in the programme's effects\n")
    out.append('The row minus its base rule on the same seed (the no-programme run is the same under every rule, so this is the change in the programme\'s effect).\n')
    K5 = K[:6]
    out.append('| Row | Base | Environment | ' + ' | '.join(l for _, l in K5) + ' |\n|---|---|---|' + '---|'*len(K5))
    for r in PROG:
        if r not in BASE: continue
        for env, nm in ENVS:
            if env in R: out.append('| %s | %s | %s | ' % (LABEL[r], LABEL[BASE[r]], nm) + ' | '.join(cell(env, r, 'reading', k, dif(env, r, BASE[r], k)) for k, _ in K5) + ' |')
    ps = sorted(c['p'] for c in cells); m = len(ps); holm = 0
    for i, p in enumerate(ps):
        if p <= 0.05/(m - i): holm += 1
        else: break
    out.append('\n## 6. Counts\n\n%d estimates; %d have a 95%% interval that excludes zero; %d survive Holm at 5%% (with %d paired seeds almost any difference does; "excludes zero" is not "material").' % (m, sum(1 for c in cells if c['lo'] > 0 or c['hi'] < 0), holm, n))
    open(os.path.join(D, 'tables.md'), 'w').write('\n'.join(out) + '\n')
    with open(os.path.join(D, 'estimates.csv'), 'w', newline='') as fh:
        w = csv.writer(fh); w.writerow(['env', 'row', 'kind', 'key', 'mean', 'lo95', 'hi95', 'p']); w.writerows(csvrows)
    print('wrote tables.md and estimates.csv in', D, '(%d estimates)' % m)
main()
