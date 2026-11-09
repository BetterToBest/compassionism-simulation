#!/usr/bin/env python3
"""S39: the outside engine cross-check's tables (research-update prereg/2026-11-s39-outside-crosscheck.md). Analysis only.

python3 dev/tools/s39_crosscheck.py --engine RESULTS/s39-path-ce8d030 [--full RESULTS/s39-full-ce8d030] [--k1 RESULTS/s39-k1-ce8d030] [--out DIR]

Engine side: for each environment and design (study A's rows, 500 adults, 20 years, CPS yardstick, raise off), the mean over seeds of U/Y by year,
the matched share of the Source's payout, and the general (PG) and full price levels at years 3 and 20 (log and level).
Outside side (preregistration, Analysis): each scenario paired seed by seed with the no-payout run of its closure (base-ea or base-dom);
d = ln(CPI_s / CPI_base) at quarters 12 and 80; lambda = mean d / sum over the years so far of ln(1 + s_y) (s from the run's own shares);
intervals: t over seeds at full scale, paired percentile bootstrap (10,000 replicates, generator seed 20261108) at 1:1000.
The same for the GDP deflator and the food, housing and medical indices; real GDP, unemployment, debt over a year's output, rate, tax rate as levels.
Written before any BeforeIT result was read (written Nov 8, 2026, S39 part 1).

Added Nov 9, 2026 (S39 part 2), after the results were read, and marked as such: (1) the identity check, which tests in every run
that the CPI grows each quarter by exactly BeforeIT's expected inflation (pi_e) and that every sector index equals the CPI (the reading
of BeforeIT's price rule in the report, section 3); (2) the intervals for preregistration rule 5's secondary contrasts (Q4 gross vs net,
Q5 tax vs new money, Q6 domestic vs euro-area closure, Q8 full scale vs 1:1000), for the CPI and real GDP, with the same interval
methods as above (Q8 compares independent seeds: Welch interval). Nothing above this note changed."""
import argparse, glob, gzip, json, os, sys
import numpy as np
# two-sided 95% t quantiles (no SciPy dependency): df 1-10, then the normal value beyond 30
T975 = {1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365, 8: 2.306, 9: 2.262, 10: 2.228}
tq975 = lambda df: T975.get(df, 2.086 if df <= 20 else 2.042 if df <= 30 else 1.96)

ap = argparse.ArgumentParser()
ap.add_argument('--engine', required=True); ap.add_argument('--full'); ap.add_argument('--k1'); ap.add_argument('--out'); ap.add_argument('--quarters', default='12,80', help='the readings (preregistered: 12,80; other values only to test the tool)')
A = ap.parse_args()
QS = [int(x) for x in A.quarters.split(',')]
lines = []
say = lines.append


def load(f):
    op = gzip.open if f.endswith('.gz') else open
    with op(f, 'rt') as h:
        return json.load(h)


# ---------- engine side ----------
say('## Engine side: study A rows rerun year by year (seeds 1-500, 500 adults, 20 years, CPS yardstick, raise off)\n')
say('| Environment | Design | Unmatched money, share of cash income (mean of years) | year 1 | year 20 | Payout matched by output | General price level after 3 years | after 19 years | Full price level after 3 years | after 19 years | Yearly rate (full level) |')
say('|---|---|---|---|---|---|---|---|---|---|---|')
EN = {'ref': 'Reference', 'adv': 'Adverse', 'st': 'Stress'}
DN = {'c22': 'C2.2', 'rls': 'release'}
eng = {}
for env in ('ref', 'adv', 'st'):
    R = load(os.path.join(A.engine, env + '-y20.json'))
    for d in ('c22', 'rls'):
        r = R['rows']['%s.n500.y20.%s.cps.main' % (env, d)]
        U, Y, PG, F = (np.array(r[k], float) for k in ('U', 'Y', 'PG', 'full'))
        s = (U / Y).mean(0); m = np.mean(r['srcM']) / np.mean(r['srcPay'])
        pg3, pg20, f3, f20 = PG[:, 3].mean(), PG[:, 19].mean(), F[:, 3].mean(), F[:, 19].mean()
        rate = np.exp(np.log(F[:, 19]).mean() / 19) - 1
        eng[(env, d)] = dict(s=s, lnPG3=np.log(PG[:, 3]).mean(), lnPG20=np.log(PG[:, 19]).mean(), lnF3=np.log(F[:, 3]).mean(), lnF20=np.log(F[:, 19]).mean())
        say('| %s | %s | %.1f%% | %.1f%% | %.1f%% | %.1f%% | %.2f | %.0f | %.2f | %.0f | %.1f%% |' % (EN[env], DN[d], 100 * s.mean(), 100 * s[0], 100 * s[19], 100 * m, pg3, pg20, f3, f20, 100 * rate))
say('\nPrice levels: means over seeds (1 before any payout). The engine sets a year\'s price level from the new money of the years before it, so its level in year index k (the year path\'s entry k) is the level after k years of payout; the run\'s last entry is after 19 years. The yearly rate is the geometric mean over those 19 years, from the mean log.')
say('The engine pass-through is 1 for the general level by construction (PG grows by exactly U/Y each year); the full level adds the essentials rule.\n')
for (env, d), e in sorted(eng.items()):
    cum3, cum20 = np.log1p(e['s'][:3]).sum(), np.log1p(e['s'][:19]).sum()
    say('- %s, %s: pass-through, ln(price level) / sum of ln(1 + U/Y) over the years paid: full level after 3 years %.2f, after 19 years %.2f; general level %.2f, %.2f.' % (EN[env], DN[d], e['lnF3'] / cum3, e['lnF20'] / cum20, e['lnPG3'] / cum3, e['lnPG20'] / cum20))


# ---------- outside side ----------
def outside(folder, label, boot):
    files = sorted(f for f in glob.glob(os.path.join(folder, 'shard-*.json*')) if '.timing.' not in f)
    runs = []
    for f in files:
        d = load(f); m = d['_meta']; R = d['rows']['runs']
        for i in range(len(R['index'])):
            runs.append({'scen': R['scenario'][i], 'seed': R['seed'][i], **{k: np.array(R[k][i], float) for k in R if k not in ('index', 'scenario', 'seed')}})
    shares = m['shares']['shares']
    sh = {'c22-ref': shares['c22.ref'], 'c22-adv': shares['c22.adv'], 'c22-st': shares['c22.st'], 'rls-ref': shares['rls.ref'], 'c22-ref-gross': shares['c22.ref.gross']}
    def share_of(sc):
        for k in sorted(sh, key=len, reverse=True):
            if sc.startswith(k + '-'): return sh[k]
        if sc.startswith('dose'): return [int(sc[4:6]) / 100.0]
        return None
    by = {}
    for r in runs: by.setdefault(r['scen'], {})[r['seed']] = r
    say('\n## BeforeIT, %s (%d runs)\n' % (label, len(runs)))
    say('| Scenario | Quarter | Price level vs no payout (CPI, %) | 95% interval | Pass-through λ | 95% interval | Deflator (%) | Food (%) | Housing (%) | Medical (%) | Real GDP (%) | Unemployment | Debt / year\'s output |')
    say('|---|---|---|---|---|---|---|---|---|---|---|---|---|')
    rng = np.random.default_rng(20261108); est = []
    for sc in by:
        if sc.startswith('base'): continue
        base = by['base-dom' if sc.endswith('-dom') else 'base-ea']; seeds = sorted(set(by[sc]) & set(base))
        s = share_of(sc)
        for q in QS:
            if q > len(base[seeds[0]]['cpi']): continue
            y = (q - 1) // 4 + 1
            ss = [s[min(t, len(s) - 1)] for t in range(y)]
            cum = np.log1p(np.array(ss)).sum()
            def diff(k): return np.array([np.log(by[sc][x][k][q - 1] / base[x][k][q - 1]) for x in seeds])
            dc = diff('cpi'); lam = dc / cum
            if boot:
                bi = rng.integers(0, len(seeds), (10000, len(seeds))); bm = dc[bi].mean(1)
                lo, hi = np.percentile(bm, [2.5, 97.5])
            else:
                se = dc.std(ddof=1) / np.sqrt(len(seeds)); tq = tq975(len(seeds) - 1); lo, hi = dc.mean() - tq * se, dc.mean() + tq * se
            pct = lambda v: 100 * (np.exp(v) - 1)
            row = dict(scenario=sc, quarter=q, cpi=pct(dc.mean()), lo=pct(lo), hi=pct(hi), lam=dc.mean() / cum, lamLo=lo / cum, lamHi=hi / cum,
                       deflator=pct(diff('deflator').mean()), food=pct(diff('food').mean()), housing=pct(diff('housing').mean()), medical=pct(diff('medical').mean()),
                       gdp=pct(diff('real_gdp').mean()), unemp=np.mean([by[sc][x]['unemp'][q - 1] for x in seeds]),
                       debt=np.mean([by[sc][x]['gov_debt_gdp'][q - 1] / 4 for x in seeds]), seeds=len(seeds), scale=label)
            est.append(row)
            say('| %s | %d | %+.2f | %+.2f to %+.2f | %.3f | %.3f to %.3f | %+.2f | %+.2f | %+.2f | %+.2f | %+.2f | %.3f | %.2f |' % (
                sc, q, row['cpi'], row['lo'], row['hi'], row['lam'], row['lamLo'], row['lamHi'], row['deflator'], row['food'], row['housing'], row['medical'], row['gdp'], row['unemp'], row['debt']))
    for b in ('base-ea', 'base-dom'):
        if b in by:
            for q in QS:
                if q > len(next(iter(by[b].values()))['cpi']): continue
                say('- No payout (%s), quarter %d: CPI %.3f, unemployment %.3f, debt / year\'s output %.2f (means over seeds).' % (
                    b, q, np.mean([r['cpi'][q - 1] for r in by[b].values()]), np.mean([r['unemp'][q - 1] for r in by[b].values()]), np.mean([r['gov_debt_gdp'][q - 1] / 4 for r in by[b].values()])))
    BY[label] = by
    return est


# ---------- added in part 2 (Nov 9, 2026), after the results: identity check and rule 5's contrasts ----------
BY = {}


def identity(label):
    by = BY[label]; g = e = 0.0; n = 0
    for sc in by.values():
        for r in sc.values():
            c = r['cpi']; pe = r['pi_e']
            g = max(g, abs(c[0] - 1 - pe[0]), np.abs(c[1:] / c[:-1] - 1 - pe[1:]).max())
            for k in ('deflator', 'food', 'housing', 'medical'): e = max(e, np.abs(r[k] / c - 1).max())
            n += 1
    say('- Identity check, %s (%d runs): largest gap between a quarter\'s CPI growth and expected inflation %.1e; largest gap between any of the deflator, food, housing and medical indices and the CPI %.1e (relative).' % (label, n, g, e))


def paired(label, num, den, k, q, sub=None):
    by = BY[label]; seeds = sorted(set(by[num]) & set(by[den]) & (set(by[sub[0]]) & set(by[sub[1]]) if sub else set(by[num])))
    x = np.array([np.log(by[num][s][k][q - 1] / by[den][s][k][q - 1]) - (np.log(by[sub[0]][s][k][q - 1] / by[sub[1]][s][k][q - 1]) if sub else 0) for s in seeds])
    return x


def interval(x, boot, rng):
    if boot:
        bm = x[rng.integers(0, len(x), (10000, len(x)))].mean(1); lo, hi = np.percentile(bm, [2.5, 97.5])
    else:
        se = x.std(ddof=1) / np.sqrt(len(x)); t = tq975(len(x) - 1); lo, hi = x.mean() - t * se, x.mean() + t * se
    return x.mean(), lo, hi


def contrasts():
    pct = lambda v: 100 * (np.exp(v) - 1)
    say('\n## Rule 5: secondary contrasts (added in part 2), seed-paired differences in log points shown as %\n')
    say('| Contrast | Scale | Quarter | CPI difference (%) | 95% interval | Real GDP difference (%) | 95% interval |')
    say('|---|---|---|---|---|---|---|')
    C = [('Q4 gross minus net (c22-ref-gross-ea vs c22-ref-ea)', 'c22-ref-gross-ea', 'c22-ref-ea', None),
         ('Q5 tax-financed minus new money (c22-ref-tax-ea vs c22-ref-ea)', 'c22-ref-tax-ea', 'c22-ref-ea', None),
         ('Q6 domestic minus euro-area closure (each against its own no-payout run)', 'c22-ref-dom', 'base-dom', ('c22-ref-ea', 'base-ea')),
         ('Primary row against no payout (c22-ref-ea vs base-ea)', 'c22-ref-ea', 'base-ea', None)]
    for name, a, b, sub in C:
        for label, boot in (('full scale (1:1)', False), ('1:1000', True)):
            if label not in BY: continue
            rng = np.random.default_rng(20261109)
            for q in QS:
                c = interval(paired(label, a, b, 'cpi', q, sub), boot, rng); y = interval(paired(label, a, b, 'real_gdp', q, sub), boot, rng)
                say('| %s | %s | %d | %+.2f | %+.2f to %+.2f | %+.2f | %+.2f to %+.2f |' % (name, label, q, *map(pct, c), *map(pct, y)))
    if len(BY) == 2:
        say('\nQ8, full scale minus 1:1000 (independent seeds; Welch interval; log points shown as %):\n')
        say('| Scenario | Quarter | CPI effect, full minus 1:1000 (%) | 95% interval | Real GDP effect, full minus 1:1000 (%) | 95% interval |')
        say('|---|---|---|---|---|---|')
        F, K = BY['full scale (1:1)'], BY['1:1000']
        for sc in [s for s in F if not s.startswith('base')]:
            b = 'base-dom' if sc.endswith('-dom') else 'base-ea'
            for q in QS:
                out = []
                for k in ('cpi', 'real_gdp'):
                    xf, xk = paired('full scale (1:1)', sc, b, k, q), paired('1:1000', sc, b, k, q)
                    vf, vk = xf.var(ddof=1) / len(xf), xk.var(ddof=1) / len(xk); se = np.sqrt(vf + vk)
                    df = (vf + vk) ** 2 / (vf ** 2 / (len(xf) - 1) + vk ** 2 / (len(xk) - 1)); t = tq975(max(1, int(np.floor(df))))
                    d = xf.mean() - xk.mean(); out += [d, d - t * se, d + t * se]
                say('| %s | %d | %+.2f | %+.2f to %+.2f | %+.2f | %+.2f to %+.2f |' % (sc, q, *map(pct, out)))


est = []
if A.full: est += outside(A.full, 'full scale (1:1)', boot=False)
if A.k1: est += outside(A.k1, '1:1000', boot=True)
if BY:
    say('\n## Identity check (added in part 2)\n')
    for label in BY: identity(label)
    contrasts()
text = '\n'.join(lines) + '\n'
if A.out:
    os.makedirs(A.out, exist_ok=True)
    open(os.path.join(A.out, 'tables.md'), 'w').write(text)
    if est:
        import csv
        with open(os.path.join(A.out, 'estimates.csv'), 'w', newline='') as h:
            w = csv.DictWriter(h, fieldnames=list(est[0])); w.writeheader(); w.writerows(est)
print(text)
