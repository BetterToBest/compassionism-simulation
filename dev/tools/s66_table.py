#!/usr/bin/env python3
"""S66 (Nov 10, 2026; research-update prereg/2026-11-s66-low-share-trace.md): the tables of the low-share trace from dev/tools/s66_trace.js's files.

Usage: python3 dev/tools/s66_table.py RAW_DIR [--out=dev/runs/s66-trace]
Writes tables.md and summary.json. Every difference is paired by seed; intervals are the 2.5th-97.5th percentiles of 2,000 paired bootstrap
replicates over seeds (numpy default_rng(20261110)); unadjusted (a trace, not a study).
Signs: in Part A a wealth-poverty "effect" is no programme minus programme (positive = fewer adults under $25,000, S55's sign); in Parts B and C,
programme minus no programme (positive = more adults under $25,000, S61's sign). Each table says which.
"""
import glob, gzip, json, os, sys
import numpy as np

RAW = sys.argv[1]
OUT = next((a.split('=', 1)[1] for a in sys.argv if a.startswith('--out=')), 'dev/runs/s66-trace')
B = 2000
ENVS = [('ref', 'Reference'), ('adv', 'Adverse'), ('st', 'Stress')]
LINE = 25000.0


def load(part, env):
    rows, meta = {}, []
    for f in sorted(glob.glob(os.path.join(RAW, 's66-%s-%s-*.json.gz' % (part, env)))):
        d = json.loads(gzip.open(f).read())
        meta.append(d['_meta'])
        for nm, r in d['rows'].items():
            o = rows.setdefault(nm, {'seeds': [], 'keys': {}})
            o['seeds'] += r['seeds']
            for k, v in r['keys'].items():
                o['keys'].setdefault(k, []).extend(v)
    return rows, meta


def boot(d):
    d = np.asarray(d, float)
    r = np.random.default_rng(20261110)
    idx = r.integers(0, len(d), size=(B, len(d)))
    m = d[idx].mean(axis=1)
    return float(d.mean()), float(np.percentile(m, 2.5)), float(np.percentile(m, 97.5))


def fm(t, nd=2):
    m, lo, hi = t
    excl = (lo > 0 or hi < 0)
    return ('%+.' + str(nd) + 'f [%+.' + str(nd) + 'f, %+.' + str(nd) + 'f]%s') % (m, lo, hi, ' *' if excl else '')


def series(row, k, yr):
    return np.array([s[k][yr] for s in row['seeds']], float)


def key(row, k):
    return np.array(row['keys'][k], float)


md, summ = [], {}
w = md.append
w('# S66 trace tables (seeds 1-100, 500 adults)\n')
w('Made by `dev/tools/s66_table.py` from `dev/tools/s66_trace.js` output (research-update `prereg/2026-11-s66-low-share-trace.md`). '
  'Paired by seed; intervals 2.5th-97.5th percentile of 2,000 paired bootstrap replicates; `*` = interval excludes zero. Unadjusted.\n')

# ---------------- Part A ----------------
SH = [5, 10, 15, 20, 25, 30, 35, 40, 50]
w('## Part A. The low end of the fixed-share curve (C2.2 design, open access, share held)\n')
for env, EN in ENVS:
    R, meta = load('A', env)
    if not R:
        continue
    T = len(R['none']['seeds'][0]['pov']) - 1
    none = R['none']
    S = summ.setdefault('A', {}).setdefault(env, {})
    w('### %s, 20 years\n' % EN)
    w('Against no programme. Wealth = adults under $25,000 at year-0 prices, no programme minus programme (points; positive = better). '
      'Inflation = the programme row\'s yearly rate minus no programme\'s (points a year). Real wealth at year 20, year-0 dollars, programme minus no programme.\n')
    w('| Row | Wealth | Inflation | Median real wealth | Mean real wealth | Price level, year 20 (x start) |')
    w('|---|---|---|---|---|---|')
    for nm in ['members'] + ['fix%d' % q for q in SH]:
        r = R[nm]
        wp = boot(series(none, 'pov', T) - series(r, 'pov', T))
        inf = boot((key(r, 'endoAnn') - key(none, 'endoAnn')) * 100)
        md_ = boot(series(r, 'rMed', T) - series(none, 'rMed', T))
        mn = boot(series(r, 'rMean', T) - series(none, 'rMean', T))
        lf = series(r, 'lf', T).mean()
        S[nm] = {'wealth': wp, 'infl': inf, 'rMed': md_, 'rMean': mn, 'lf': lf}
        w('| %s | %s | %s | %s | %s | %.1f |' % (nm, fm(wp), fm(inf), fm(md_, 0), fm(mn, 0), lf))
    w('')
    w('The dip: one share minus another, on the same seeds (wealth as above; inflation in points a year; real wealth in dollars).\n')
    w('| Comparison | Wealth | Inflation | Median real wealth | Mean real wealth | Price level ratio, year 20 |')
    w('|---|---|---|---|---|---|')
    for a, b in [('fix10', 'fix20'), ('fix30', 'fix20'), ('fix5', 'fix10'), ('fix10', 'members'), ('fix40', 'fix30')]:
        ra, rb = R[a], R[b]
        dw = boot(series(rb, 'pov', T) - series(ra, 'pov', T))
        di = boot((key(ra, 'endoAnn') - key(rb, 'endoAnn')) * 100)
        dm = boot(series(ra, 'rMed', T) - series(rb, 'rMed', T))
        dn = boot(series(ra, 'rMean', T) - series(rb, 'rMean', T))
        pr = boot(series(ra, 'lf', T) / series(rb, 'lf', T) - 1)
        S[a + '-' + b] = {'wealth': dw, 'infl': di, 'rMed': dm, 'rMean': dn, 'lfRatio': pr}
        w('| %s − %s | %s | %s | %s | %s | %s |' % (a, b, fm(dw), fm(di), fm(dm, 0), fm(dn, 0), fm((pr[0] * 100, pr[1] * 100, pr[2] * 100)) + ' %'))
    w('')
    # year paths
    K = [('lf', 'price level (x start)', 3), ('UY', 'new money U, % of cash income', 2), ('U', 'U per adult (year-0 $)', 0), ('pay', 'Source payout per adult', 0),
         ('bu', '  of which BU at face value', 0), ('conv', '  of which conversion, net', 0), ('ctax', 'conversion tax withheld', 0), ('convM', 'output matched', 0),
         ('sp_pool', 'business premium pool', 0), ('sp_ptf', '  PTFs\' part', 0), ('sp_reinv', '  PTF reinvestment', 0), ('sp_privP', '  private ESPs\' price pass-through', 0),
         ('cutPtfPA', 'PTF price cut per adult (real $)', 0), ('cutN', 'adults with a PTF cut (%)', 1), ('cutPer', 'cut per adult receiving one (real $)', 0),
         ('wage', 'real wage income', 0), ('convI', 'real conversion income', 0), ('disp', 'real disposable income', 0), ('cost', 'real own cash cost of essentials', 0),
         ('spend', 'real cash spending', 0), ('nMed', 'median nominal wealth', 0), ('rMed', 'median real wealth', 0), ('rMean', 'mean real wealth', 0),
         ('debt', 'in debt (%)', 2), ('pov', 'under $25,000 (%)', 2), ('near', 'within $5,000 of $25,000 (%)', 2)]
    YR = [0, 1, 2, 3, 4, 6, 9, 14, 19]
    w('Year by year, means over seeds: the 10% row, and 10% minus 20% (same seeds). Dollar figures per adult; "real" = at year-0 prices.\n')
    w('| Measure | ' + ' | '.join('y%d' % (y + 1) for y in YR) + ' |')
    w('|---|' + '---|' * len(YR))
    pth = S.setdefault('paths', {})
    for k, lab, nd in K:
        if k not in R['fix10']['seeds'][0]:
            continue
        a = [series(R['fix10'], k, y).mean() for y in YR]
        d = [boot(series(R['fix10'], k, y) - series(R['fix20'], k, y)) for y in YR]
        pth[k] = {'fix10': a, 'd10_20': d, 'fix30': [series(R['fix30'], k, y).mean() for y in YR], 'fix20': [series(R['fix20'], k, y).mean() for y in YR]}
        f = '%.' + str(nd) + 'f'
        w('| %s, 10%% | %s |' % (lab, ' | '.join(f % x for x in a)))
        w('| &nbsp;&nbsp;10%% − 20%% | %s |' % ' | '.join((('%+.' + str(nd) + 'f') % x[0]) + ('*' if (x[1] > 0 or x[2] < 0) else '') for x in d))
    w('')
    # density at year 20
    w('Real wealth at year 20 in $2,500 bands, % of adults (means over seeds), $0-$50,000.\n')
    hdr = ['%dk' % (i * 2.5) for i in range(20)] + ['50k+']
    w('| Row | ' + ' | '.join(hdr) + ' |')
    w('|---|' + '---|' * len(hdr))
    for nm in ['none', 'fix10', 'fix20', 'fix30']:
        bb = np.array([s['band'][T] for s in R[nm]['seeds']]).mean(axis=0)
        w('| %s | %s |' % (nm, ' | '.join('%.1f' % x for x in bb)))
    w('')
    # switch-offs
    w('Switch-offs (each alone). Wealth effect against no programme (positive = better) at each share, and 10% minus 20% on the same seeds.\n')
    w('| Reading | 10% | 20% | 30% | 40% | 10% − 20% | inflation 10% − 20% |')
    w('|---|---|---|---|---|---|---|')
    ko = S.setdefault('K', {})
    for k, lab in [('', 'main'), ('K1', 'K1 40% rule off'), ('K2', 'K2 PTF damping off'), ('K3', 'K3 conversion income off'), ('K4', 'K4 surplus split held at 10%'), ('K5', 'K5 price cut held at 10%')]:
        p = (k + '.') if k else ''
        if p + 'fix10' not in R:
            continue
        e = [boot(series(none, 'pov', T) - series(R[p + 'fix%d' % q], 'pov', T)) for q in [10, 20, 30, 40]]
        d = boot(series(R[p + 'fix20'], 'pov', T) - series(R[p + 'fix10'], 'pov', T))
        di = boot((key(R[p + 'fix10'], 'endoAnn') - key(R[p + 'fix20'], 'endoAnn')) * 100)
        ko[k or 'main'] = {'e': e, 'd': d, 'di': di}
        w('| %s | %s | %s |' % (lab, ' | '.join(fm(x) for x in e), fm(d) + ' | ' + fm(di)))
    w('')

# ---------------- Part A, 40 years ----------------
w('## Part A at 40 years\n')
w('Wealth effect against no programme (positive = better) at years 20 and 40, and median real wealth at year 40 (programme minus no programme).\n')
w('| Environment | Row | Wealth, year 20 | Wealth, year 40 | Median real wealth, year 40 | Inflation |')
w('|---|---|---|---|---|---|')
for env, EN in ENVS[:2]:
    R, _ = load('A40', env)
    if not R:
        continue
    n = R['none']
    for nm in ['members', 'fix10', 'fix20', 'fix30', 'fix40']:
        r = R[nm]
        a = boot(series(n, 'pov', 19) - series(r, 'pov', 19)); b = boot(series(n, 'pov', 39) - series(r, 'pov', 39))
        c = boot(series(r, 'rMed', 39) - series(n, 'rMed', 39)); i = boot((key(r, 'endoAnn') - key(n, 'endoAnn')) * 100)
        summ.setdefault('A40', {}).setdefault(env, {})[nm] = {'w20': a, 'w40': b, 'rMed40': c, 'infl': i}
        w('| %s | %s | %s | %s | %s | %s |' % (EN, nm, fm(a), fm(b), fm(c, 0), fm(i)))
    for a_, b_ in [('fix10', 'fix20'), ('fix30', 'fix20')]:
        d = boot(series(R[b_], 'pov', 39) - series(R[a_], 'pov', 39)); summ['A40'][env][a_ + '-' + b_] = d
        w('| %s | %s − %s | | %s | | |' % (EN, a_, b_, fm(d)))
w('')


# ---------------- Parts B and C: erosion of opening balances ----------------
def erosion(none, prog, grp=None):
    """Per seed: mean gap in last-year real wealth, mean erosion term, published and adjusted wealth-poverty effects (prog - none, points), by fifth."""
    out = {'gap': [], 'ero': [], 'pov': [], 'povAdj': [], 'n': [], 'fifth': [[[], []] for _ in range(5)]}
    for sn, sp in zip(none['seeds'], prog['seeds']):
        An = {a[0]: a for a in sn['adults']}; Pn = sn['lfEnd']; Pp = sp['lfEnd']
        g, e, pv, pa, w0s = [], [], [0, 0], 0, []
        for a in sp['adults']:
            b = An.get(a[0])
            if b is None:
                continue
            if grp is not None and ((a[3] is not None) != grp):
                continue
            W0 = b[1]
            rp, rn = a[2] / Pp, b[2] / Pn
            ero = W0 * (1 / Pp - 1 / Pn)
            g.append(rp - rn); e.append(ero); w0s.append(W0)
            pv[0] += rp < LINE; pv[1] += rn < LINE; pa += (rp - ero) < LINE
        n = len(g)
        if not n:
            continue
        g, e, w0s = np.array(g), np.array(e), np.array(w0s)
        out['gap'].append(g.mean()); out['ero'].append(e.mean()); out['n'].append(n)
        out['pov'].append((pv[0] - pv[1]) / n * 100); out['povAdj'].append((pa - pv[1]) / n * 100)
        q = np.argsort(np.argsort(w0s, kind='stable'), kind='stable') * 5 // n
        for f in range(5):
            m = q == f
            out['fifth'][f][0].append(g[m].mean()); out['fifth'][f][1].append(e[m].mean())
    return out


def ero_rows(lab, o):
    gap, ero = boot(o['gap']), boot(o['ero'])
    sh = 100 * np.mean(o['ero']) / np.mean(o['gap']) if np.mean(o['gap']) != 0 else float('nan')
    pv, pa = boot(o['pov']), boot(o['povAdj'])
    part = boot(np.array(o['pov']) - np.array(o['povAdj']))
    return gap, ero, sh, pv, pa, part


w('## Part B. The erosion of opening balances (members-only main rows)\n')
w('For each adult in both runs of a seed: the gap in year-20 real wealth (programme minus no programme, year-0 dollars), and the erosion term: the adult\'s '
  'opening balance times the difference of the two runs\' deflators, W0 x (1/P_prog − 1/P_none). Wealth poverty here is programme minus no programme '
  '(points; positive = more adults under $25,000). "Without erosion" deflates each opening balance at the no-programme price level instead.\n')
w('| Environment | Design | Real-wealth gap | Erosion term | Erosion share of gap | Wealth poverty, published | Without erosion | Part that is erosion |')
w('|---|---|---|---|---|---|---|---|')
for env, EN in ENVS:
    R, _ = load('B', env)
    if not R:
        continue
    for d, lab in [('rls', 'release'), ('c22', 'C2.2')]:
        o = erosion(R['none'], R[d]); gap, ero, sh, pv, pa, part = ero_rows(lab, o)
        summ.setdefault('B', {}).setdefault(env, {})[d] = {'gap': gap, 'ero': ero, 'share': sh, 'pov': pv, 'povAdj': pa, 'part': part,
                                                           'fifth': [[float(np.mean(x[0])), float(np.mean(x[1]))] for x in o['fifth']]}
        w('| %s | %s | %s | %s | %.0f%% | %s | %s | %s |' % (EN, lab, fm(gap, 0), fm(ero, 0), sh, fm(pv), fm(pa), fm(part)))
w('')
w('By fifth of opening wealth (lowest first): mean real-wealth gap / mean erosion term (year-0 dollars).\n')
w('| Environment | Design | Fifth 1 | Fifth 2 | Fifth 3 | Fifth 4 | Fifth 5 |')
w('|---|---|---|---|---|---|---|')
for env, EN in ENVS:
    for d, lab in [('rls', 'release'), ('c22', 'C2.2')]:
        f = summ.get('B', {}).get(env, {}).get(d)
        if f:
            w('| %s | %s | %s |' % (EN, lab, ' | '.join('%+.0f / %+.0f' % (a, b) for a, b in f['fifth'])))
w('')

w('## Part C. The wealth harm with adults outside the labour force (C2.2 design)\n')
w('As Part B, on S61\'s row L (`lf: {}`) and the same rows without `lf`; split by adults outside the labour force and in it (rows with `lf`).\n')
w('| Environment | Rows | Adults | Real-wealth gap | Erosion term | Erosion share | Wealth poverty, published | Without erosion | Part that is erosion |')
w('|---|---|---|---|---|---|---|---|---|')
for env, EN in ENVS:
    R, _ = load('C', env)
    if not R:
        continue
    for t, lab in [('', 'without lf'), ('lf.', 'with lf')]:
        for g, gl in ([(None, 'all')] if not t else [(None, 'all'), (True, 'outside the labour force'), (False, 'in the labour force')]):
            o = erosion(R[t + 'none'], R[t + 'c22'], g); gap, ero, sh, pv, pa, part = ero_rows(gl, o)
            summ.setdefault('C', {}).setdefault(env, {})[t + gl] = {'gap': gap, 'ero': ero, 'share': sh, 'pov': pv, 'povAdj': pa, 'part': part, 'n': float(np.mean(o['n']))}
            w('| %s | %s | %s (%.0f) | %s | %s | %.0f%% | %s | %s | %s |' % (EN, lab, gl, np.mean(o['n']), fm(gap, 0), fm(ero, 0), sh, fm(pv), fm(pa), fm(part)))
w('')
w('Year 20, means over seeds, rows with `lf`: real yearly income and cost per adult by group (no programme → programme).\n')
w('| Environment | Adults | Wage | Conversion | Disposable income | Own cash cost | Opening balance (mean) |')
w('|---|---|---|---|---|---|---|')
for env, EN in ENVS:
    R, _ = load('C', env)
    if not R:
        continue
    for g, gl in [(True, 'outside the labour force'), (False, 'in the labour force')]:
        acc = {k: [[], []] for k in ['wage', 'conv', 'disp', 'cost', 'w0']}
        for j, nm in enumerate(['lf.none', 'lf.c22']):
            for s in R[nm]['seeds']:
                A = [a for a in s['adults'] if (a[3] is not None) == g]
                for k, i in [('wage', 4), ('conv', 5), ('disp', 6), ('cost', 7), ('w0', 1)]:
                    acc[k][j].append(np.mean([a[i] for a in A]) if A else 0)
        w('| %s | %s | %s |' % (EN, gl, ' | '.join('%.0f → %.0f' % (np.mean(acc[k][0]), np.mean(acc[k][1])) for k in ['wage', 'conv', 'disp', 'cost']) + ' | %.0f' % np.mean(acc['w0'][0])))
w('')

os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, 'tables.md'), 'w').write('\n'.join(md) + '\n')
json.dump(summ, open(os.path.join(OUT, 'summary.json'), 'w'), indent=1, default=float)
print('wrote', os.path.join(OUT, 'tables.md'))
