#!/usr/bin/env python3
"""S57 (Nov 9, 2026): the analysis of the distribution-measures pilot, exactly as preregistered (research-update
prereg/2026-11-s57-distribution-measures.md, Analysis). Reads the per-seed files written by dev/tools/s57_dm.js (s57-dm-ref.json, -adv, -st in one
folder) and writes tables.md, estimates.csv and the findings page's data file.

  python3 dev/tools/s57_table.py DIR [--data FILE] [--reps 2000]

Estimates: the programme run minus the no-programme run on the same seed, as the mean of the paired differences (design rel = the release row, c22 = the
C2.2 design). Intervals: paired bootstrap over seeds, 2,000 replicates, resampler seed 57, the same resample for every cell; 95% percentile interval.
Ratios are computed per seed first; a ratio that is not reported in either run of a seed (bottom 40% without positive wealth or income) leaves that seed out of
the cell, and the cell says how many seeds it uses. Each cell's two-sided bootstrap p-value is twice the smaller tail share (floor 1/(reps+1)); Holm is
applied within the family (all cells in estimates.csv). Intervals shown are not adjusted. Standard library only."""
import json, os, sys, random, math, csv

REPS = 2000
ENVS = [('ref', 'Reference'), ('adv', 'Adverse'), ('st', 'Stress')]
DES = [('rel', 'release row'), ('c22', 'C2.2 design')]
# key, plain label, unit, ok-flag key (the ratio is used only where both runs report it)
SC = [('eGiniW', 'Gini of wealth, debts counted as zero (eGiniW)', 'Gini', None),
      ('eGiniWN', 'Gini of wealth, debts kept (eGiniWN)', 'Gini', None),
      ('dmWt1E', 'top 1% share of wealth', '%', None), ('dmWt10E', 'top 10% share of wealth', '%', None), ('dmWb50E', 'bottom 50% share of wealth', '%', None),
      ('dmWrE', 'wealth ratio, top 10% over bottom 40% (only where the bottom 40% hold positive wealth)', 'ratio', 'dmWrOkE'),
      ('dmYt1E', 'top 1% share of disposable income', '%', None), ('dmYt10E', 'top 10% share of disposable income', '%', None), ('dmYb50E', 'bottom 50% share of disposable income', '%', None),
      ('dmYpE', 'income Palma ratio, top 10% over bottom 40%', 'ratio', 'dmYpOkE'),
      ('dmFdE', 'families in debt', '%', None), ('dmDmE', 'median debt of families in debt (Year-0 $)', '$', None), ('dmDiE', 'debt over income of families in debt', 'ratio', None),
      ('dmLsE', "labour's share of money income, wages, last year", '%', None), ('dmLcE', "labour's share, wages plus conversion proceeds, last year", '%', None),
      ('dmLsPY', "labour's share, wages, all years", '%', None), ('dmLcPY', "labour's share, wages plus conversion proceeds, all years", '%', None)]
GRID = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 99]
CHECK = [('dmWt1S', 'top 1% share of wealth', 'DFA Q2 2026: 32.5%'), ('dmWt10S', 'top 10% share of wealth', 'CBO 2022: 69% without Social Security wealth (60% with)'),
         ('dmWb50S', 'bottom 50% share of wealth', 'CBO 2022: 6%'), ('eGiniWN', 'Gini of wealth, debts kept (last year; Year-0 values are in the data file)', '')]

def mean(v): return sum(v)/len(v) if v else float('nan')
def pct(b, q): return b[min(len(b) - 1, max(0, int(round(q*(len(b) - 1)))))]

def load(d):
    R = {}
    for e, _ in ENVS:
        p = os.path.join(d, 's57-dm-%s.json' % e)
        if os.path.exists(p): R[e] = json.load(open(p))
    return R

def mobsum(r, i):  # per-seed mobility summaries from one run's matrix
    M = [[r['dmMob%d%d' % (a, b)][i] for b in range(5)] for a in range(5)]
    return {'stay': mean([M[a][a] for a in range(5)]), 'up': mean([sum(M[a][a + 1:]) for a in range(5)]), 'down': mean([sum(M[a][:a]) for a in range(5)]),
            'b2t': M[0][3] + M[0][4]}

def main():
    A = [a for a in sys.argv[1:] if not a.startswith('--')]; D = A[0]
    opt = lambda k: (sys.argv[sys.argv.index('--' + k) + 1] if '--' + k in sys.argv else None)
    reps = int(opt('reps') or REPS); R = load(D)
    if not R: sys.exit('no s57-dm-*.json in ' + D)
    n = len(next(iter(R.values()))['rows']['np']['dmWt1E']); rnd = random.Random(57)
    idx = [[rnd.randrange(n) for _ in range(n)] for _ in range(reps)]
    cells = []; out = []; data = {'about': 'S57 distribution measures, pilot (prereg/2026-11-s57-distribution-measures.md)', 'seeds': n, 'reps': reps, 'envs': {}}
    def est(v, ok=None):  # v: per-seed list (None where unused)
        use = [i for i in range(n) if v[i] is not None]; m = len(use)
        if m < 5: return None
        x = [v[i] for i in use]; pos = {s: j for j, s in enumerate(use)}
        b = []
        for ix in idx:
            s = [pos[i] for i in ix if i in pos]
            b.append(mean([x[j] for j in s]) if s else float('nan'))
        b = sorted(t for t in b if t == t)
        lo, hi = pct(b, 0.025), pct(b, 0.975); le = sum(1 for t in b if t <= 0)/len(b); ge = sum(1 for t in b if t >= 0)/len(b)
        p = max(1/(len(b) + 1), min(1.0, 2*min(le, ge)))
        return {'m': mean(x), 'lo': lo, 'hi': hi, 'p': p, 'n': m}
    def diff(env, d, k, flag=None):
        P, N = R[env]['rows'][d], R[env]['rows']['np']
        return [(P[k][i] - N[k][i]) if (flag is None or (P[flag][i] == 1 and N[flag][i] == 1)) else None for i in range(n)]
    out.append('# S57 distribution measures: pilot tables\n')
    out.append('Seeds 1-%d, 500 adults, 20 years, frozen yardstick, engine %s. Programme minus no programme on the same seed; mean of the paired differences with the 95%% paired-bootstrap interval (%d replicates, resampler seed 57). Family: preregistered secondary. Intervals are not adjusted for multiple comparisons; the Holm count is at the end.\n' % (n, next(iter(R.values()))['_meta']['manifest'].get('commit', '?')[:7], reps))
    out.append('## 1. The no-programme start against outside figures (checks, never targets)\n')
    out.append('| Measure | Environment | No programme, Year 0 (mean, 95% interval over seeds) | Outside figure |\n|---|---|---|---|')
    for k, lab, ext in CHECK[:3]:
        for e, en in ENVS:
            if e not in R: continue
            r = est(R[e]['rows']['np'][k] and [R[e]['rows']['np'][k][i] for i in range(n)])
            out.append('| %s | %s | %.1f%% (%.1f to %.1f) | %s |' % (lab, en, r['m'], r['lo'], r['hi'], ext))
    out.append('')
    for e, en in ENVS:
        if e not in R: continue
        data['envs'][e] = {'name': en, 'np': {}, 'effects': {}, 'gic': {}, 'mobility': {}}
        out.append('## 2. %s: end of year %d\n' % (en, R[e]['_meta']['years']))
        out.append('| Measure | No programme | Release row minus none | C2.2 design minus none | Seeds used |\n|---|---|---|---|---|')
        for k, lab, unit, flag in SC:
            N = R[e]['rows']['np'][k]; row = []; used = []
            for d, dl in DES:
                r = est(diff(e, d, k, flag))
                if r is None: row.append('not enough seeds'); continue
                cells.append((e, d, k, 'scalar', r)); used.append(r['n'])
                row.append('%+.3g (%.3g to %.3g)' % (r['m'], r['lo'], r['hi']))
                data['envs'][e]['effects'].setdefault(k, {})[d] = r
            npm = mean([N[i] for i in range(n) if flag is None or R[e]['rows']['np'][flag][i] == 1])
            data['envs'][e]['np'][k] = npm
            out.append('| %s (%s) | %.3g | %s | %s | %s |' % (lab, unit, npm, row[0], row[1], '-'.join(str(u) for u in sorted(set(used)))))
        out.append('')
        for pre, what in (('W', 'wealth'), ('Y', 'disposable income')):
            out.append('### Growth-incidence curve, %s (year-0 dollars; same rank in the two distributions, not the same person)\n' % what)
            out.append('| Percentile | No programme | Release row minus none | C2.2 design minus none |\n|---|---|---|---|')
            for q in GRID:
                k = 'dm%sp%dE' % (pre, q); N = R[e]['rows']['np'][k]; row = []
                for d, dl in DES:
                    r = est(diff(e, d, k))
                    cells.append((e, d, k, 'gic', r)); data['envs'][e]['gic'].setdefault(k, {})[d] = r; row.append('%+.0f (%.0f to %.0f)' % (r['m'], r['lo'], r['hi']))
                out.append('| P%d | %.0f | %s | %s |' % (q, mean(N), row[0], row[1]))
            out.append('')
        out.append('### Mobility between wealth fifths (adults present at Year 0; %% of each starting fifth)\n')
        out.append('| Summary | No programme | Release row minus none | C2.2 design minus none |\n|---|---|---|---|')
        for key, lab in (('stay', 'stay in the same fifth'), ('up', 'move up'), ('down', 'move down'), ('b2t', 'poorest fifth reaching the top two fifths')):
            ms = {d: [mobsum(R[e]['rows'][d], i)[key] for i in range(n)] for d in ('np', 'rel', 'c22')}; row = []
            for d, dl in DES:
                r = est([ms[d][i] - ms['np'][i] for i in range(n)]); cells.append((e, d, 'mob_' + key, 'mobility', r)); row.append('%+.2f (%.2f to %.2f)' % (r['m'], r['lo'], r['hi']))
                data['envs'][e]['mobility'].setdefault(key, {})[d] = r
            data['envs'][e]['mobility'].setdefault(key, {})['np'] = mean(ms['np'])
            out.append('| %s | %.2f | %s | %s |' % (lab, mean(ms['np']), row[0], row[1]))
        out.append('')
    # Holm within the family
    ps = sorted(range(len(cells)), key=lambda j: cells[j][4]['p']); m = len(cells); surv = set(); prev = False
    for rank, j in enumerate(ps):
        if cells[j][4]['p'] <= 0.05/(m - rank) and not prev: surv.add(j)
        else: prev = True
    excl = sum(1 for c in cells if c[4]['lo'] > 0 or c[4]['hi'] < 0)
    out.append('## 3. Counts for the family\n')
    out.append('%d estimates (environments x designs x measures, percentile cells and mobility summaries included). Intervals excluding zero: %d. Surviving Holm within the family at 5%%: %d. The intervals above are not adjusted. "Excludes zero" is not "material".\n' % (m, excl, len(surv)))
    open(os.path.join(D, 'tables.md'), 'w').write('\n'.join(out))
    with open(os.path.join(D, 'estimates.csv'), 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['env', 'design', 'measure', 'kind', 'mean_diff', 'lo95', 'hi95', 'p_boot', 'seeds', 'holm_survives'])
        for j, (e, d, k, kind, r) in enumerate(cells): w.writerow([e, d, k, kind, '%.6g' % r['m'], '%.6g' % r['lo'], '%.6g' % r['hi'], '%.4g' % r['p'], r['n'], int(j in surv)])
    data['counts'] = {'estimates': m, 'excludeZero': excl, 'holmSurvive': len(surv)}
    if opt('data'):
        json.dump(data, open(opt('data'), 'w'), indent=1)
    print('wrote tables.md and estimates.csv in', D, '; estimates', m, 'exclude zero', excl, 'Holm', len(surv))
main()
