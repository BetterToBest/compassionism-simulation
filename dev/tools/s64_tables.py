#!/usr/bin/env python3
"""S64 (Nov 15, 2026): the tables of round 2, as research-update prereg/2026-11-s63-round2-freeze.md fixes them (Outcomes, Analysis, Decision rules;
Amendments 1-2). Reads the 24 result folders r2-<part>-<env>-<years>-104691f of compassionism-sim-results (runner/jobs/r2.js; shard-NNNN.json.gz,
seeds 1-500 split across shards) and writes Markdown tables, one CSV per specification curve and a summary JSON.

  python3 dev/tools/s64_tables.py RESULTS_DIR OUT_DIR [--engine 104691f] [--bkm DIR] [--reps 2000]

Every effect is the programme run minus its own no-programme run, paired over seeds 1-500 (common random numbers). Estimate: the mean of the paired
differences (the median for the debt keys); 95% interval: paired bootstrap, 2,000 resamples, generator seed 6301 (numpy default_rng), the same resample
for every row, so intervals of different rows are comparable. p: two-sided paired t (499 degrees of freedom). Holm: across the 60 primary tests; within
each table in the secondary family. Interaction contrast of a 2 x 2: both - A alone - B alone + base, paired, with its bootstrap interval.

Decision rules applied mechanically (prereg "Decision rules"): 1 the headline sentence (range across the curve first, then the main row and its seed
interval); 2 robust / mostly robust / fragile; 3 materiality (1 point for the poverty measures, 1 point a year for inflation, 5% of the no-programme median
real wealth); 4 the break-even backed share against the mechanism's own point; 5 financed rows: rate, base, cap, deficit, how it is met, "unsustainable"
when the median year debt passes GDP is within 40 years; 7 no low-share optimum unless both horizons show it with intervals excluding zero.

Rule 7's test, as read here (written before any fixed-share figure was read): an optimum at a low share means the most favourable of the ten fixed shares
is 10%, 20% or 30%, and its paired difference from the 100% share excludes zero in the favourable direction. Rule 3 (materiality) was added to this
test after the first tables were read: without it, differences of a hundredth of a point of inflation and of $1,400-7,200 of median wealth qualified.
Both lists are printed (rule7 and rule7any in the summary).

--bkm DIR: the replay of the backing curve's two mechanism points (S part points 75 and 76, programme rows) with the realised backed share bkA, files
bkm-<env>-<years>.json (r2.js with bkA and bkmO19 added to the stored keys; every other stored key must equal the batch's). Without it the mechanism's
point is marked by its inflation only.
Standard library and numpy."""
import csv, glob, gzip, json, math, os, sys
import numpy as np

ENVS = ['ref', 'adv', 'str']; ENVL = {'ref': 'Reference', 'adv': 'Adverse', 'str': 'Stress'}
YEARS = [20, 40]; DES = ['c22', 'rel']; DESL = {'c22': 'C2.2', 'rel': 'release design'}
PRIM = [('bNAPy', 'basic living (adult-years below 30 days, points)', 'mean', 1.0),
        ('fgt0PY', 'cost of living (basket poverty, points)', 'mean', 1.0),
        ('ppovA', 'wealth poverty, yearly average (points)', 'mean', 1.0),
        ('wtMedE', 'median real wealth (weighted, year-0 $)', 'mean', None),
        ('endoAnn', 'programme inflation (points a year)', 'mean', 1.0)]
SHORT = {'bNAPy': 'basic living', 'fgt0PY': 'basket poverty', 'ppovA': 'wealth poverty', 'wtMedE': 'median real wealth', 'endoAnn': 'programme inflation',
         'gvDebtY': 'programme debt (% of GDP)', 'gvY100': 'year debt passes GDP'}
UNIT = {'bNAPy': 'points', 'fgt0PY': 'points', 'ppovA': 'points', 'wtMedE': '$', 'endoAnn': 'points a year', 'gvDebtY': 'points of GDP', 'gvY100': 'years'}
FAV = {'bNAPy': -1, 'fgt0PY': -1, 'ppovA': -1, 'wtMedE': 1, 'endoAnn': -1, 'gvDebtY': -1, 'gvY100': 1}  # sign of a favourable effect
SCALE = {'endoAnn': 100.0, 'tauMean': 100.0}
DIG = {'wtMedE': 0, 'gvY100': 1, 'h': 4}
REPS = 2000; BS = None


# ---------------------------------------------------------------- loading
def load(folder):
    files = sorted(glob.glob(os.path.join(folder, 'shard-*.json.gz')))
    if not files: sys.exit('no shard files in ' + folder)
    D = [json.load(gzip.open(f)) for f in files]
    D.sort(key=lambda d: d['_meta']['seeds'][0])
    s = 1
    for d in D:
        if d['_meta']['seeds'][0] != s: sys.exit('seed ranges not consecutive in ' + folder)
        s = d['_meta']['seeds'][1] + 1
    if s != 501: sys.exit('seeds do not cover 1-500 in ' + folder)
    rows = {}
    for r in D[0]['rows']:
        rows[r] = {k: np.array([x for d in D for x in d['rows'][r][k]], dtype=float) for k in D[0]['rows'][r]}
    return rows, D[0]['_meta']


def derive(r, T):
    """the yearly averages and fixed-year readings the S and F parts store, computed the same way from the full keys of parts M and B"""
    for p, a in (('ppov', 'ppovA'), ('pmedW', 'pmedWA')):
        if p + '_1' in r: r[a] = sum(r['%s_%d' % (p, t)] for t in range(1, T))/(T - 1)
        if p + '_19' in r: r[p + '20'] = r[p + '_19']
        if T == 40 and p + '_39' in r: r[p + '40'] = r[p + '_39']
    return r


# ---------------------------------------------------------------- statistics
def tcdf(t, df):
    """Student t cumulative distribution (regularised incomplete beta, continued fraction)"""
    x = df/(df + t*t)
    def betacf(a, b, x):
        qab, qap, qam = a + b, a + 1, a - 1; c, d = 1.0, 1 - qab*x/qap; d = 1/(d if abs(d) > 1e-300 else 1e-300); h = d
        for m in range(1, 400):
            m2 = 2*m; aa = m*(b - m)*x/((qam + m2)*(a + m2))
            d = 1 + aa*d; d = 1/(d if abs(d) > 1e-300 else 1e-300); c = 1 + aa/c if abs(c) > 1e-300 else 1e300; h *= d*c
            aa = -(a + m)*(qab + m)*x/((a + m2)*(qap + m2))
            d = 1 + aa*d; d = 1/(d if abs(d) > 1e-300 else 1e-300); c = 1 + aa/c if abs(c) > 1e-300 else 1e300; de = d*c; h *= de
            if abs(de - 1) < 3e-16: break
        return h
    a, b = df/2, 0.5
    if x <= 0: ib = 0.0
    elif x >= 1: ib = 1.0
    else:
        lb = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a*math.log(x) + b*math.log(1 - x)
        ib = math.exp(lb)*betacf(a, b, x)/a if x < (a + 1)/(a + b + 2) else 1 - math.exp(lb)*betacf(b, a, 1 - x)/b
    return 1 - 0.5*ib if t > 0 else 0.5*ib


def est(d, how='mean'):
    """estimate, 2.5% and 97.5% bootstrap percentiles, two-sided paired t p (mean only)"""
    n = len(d)
    if how == 'median':
        m = float(np.median(d)); v = np.median(d[BS], axis=1); p = None
    else:
        m = float(d.mean()); v = d[BS].mean(axis=1); sd = float(d.std(ddof=1))
        p = 1.0 if sd == 0 and m == 0 else 0.0 if sd == 0 else 2*(1 - tcdf(abs(m)/(sd/math.sqrt(n)), n - 1))
    lo, hi = np.percentile(v, [2.5, 97.5])
    return {'est': m, 'lo': float(lo), 'hi': float(hi), 'p': p}


def holm(ps):
    """Holm-adjusted p-values (same order)"""
    k = len(ps); order = sorted(range(k), key=lambda i: ps[i]); adj = [0.0]*k; run = 0.0
    for j, i in enumerate(order): run = max(run, min(1.0, (k - j)*ps[i])); adj[i] = run
    return adj


def excl(s): return s['lo'] > 0 or s['hi'] < 0
def sgn(x): return 1 if x > 0 else -1 if x < 0 else 0
def f(x, k, d=None):
    if x is None: return '–'
    d = DIG.get(k, 2) if d is None else d
    return ('{:,.%df}' % d).format(x) if abs(x) >= 1000 else ('%.' + str(d) + 'f') % x
def ci(s, k): return '%s (%s to %s)' % (f(s['est'], k), f(s['lo'], k), f(s['hi'], k))
def pf(p): return '–' if p is None else '<1e-15' if p < 1e-15 else '%.2g' % p


# ---------------------------------------------------------------- effects
def diff(rows, a, b, k):
    if k not in rows[a] or k not in rows[b]: return None
    return (rows[a][k] - rows[b][k])*SCALE.get(k, 1.0)


def material(k, e, thrW):
    thr = thrW if k == 'wtMedE' else 10.0 if k == 'gvDebtY' else 2.0 if k == 'gvY100' else 1.0
    return abs(e) >= thr, thr


# ---------------------------------------------------------------- the specification curve
def classify(points, mainS, k, thr):
    """rule 2 on a list of point stats; mainS the main row's"""
    s0 = sgn(mainS['est']); n = len(points)
    same = [p for p in points if excl(p['s']) and sgn(p['s']['est']) == s0]
    opp = [p for p in points if excl(p['s']) and sgn(p['s']['est']) == -s0]
    share = len(same)/n if n else 0
    cls = 'robust' if len(same) == n else 'mostly robust' if share >= 0.9 and not opp else 'fragile'
    lo = min(p['s']['est'] for p in points); hi = max(p['s']['est'] for p in points)
    weak = [p['label'] for p in points if p not in same]
    return {'n': n, 'same': len(same), 'opp': len(opp), 'share': share, 'class': cls, 'min': lo, 'max': hi, 'notSame': weak,
            'reverse': [p['label'] for p in opp], 'material': abs(mainS['est']) >= thr}


def sentence(design, k, cl, mainS, thr):
    """rule 1"""
    u = UNIT[k]; nm = SHORT[k]
    if u == '$':  # dollars before the figure, not after
        g = lambda x: '$' + f(x, k)
        lead = ('no material change in %s at the main row ($%s; materiality $%s)' % (nm, f(mainS['est'], k), f(thr, k))) if not cl['material'] else None
        return 'Across the %d preregistered readings, the %s design changes %s by %s to %s; %s (seed interval %s to %s).' % (
            cl['n'], DESL[design], nm, g(cl['min']), g(cl['max']), lead or 'at the main row, ' + g(mainS['est']), g(mainS['lo']), g(mainS['hi']))
    if not cl['material']:
        lead = 'no material change in %s at the main row (%s %s; materiality %s)' % (nm, f(mainS['est'], k), u, f(thr, k))
        return 'Across the %d preregistered readings, the %s design changes %s by %s to %s %s; %s, seed interval %s to %s.' % (
            cl['n'], DESL[design], nm, f(cl['min'], k), f(cl['max'], k), u, lead, f(mainS['lo'], k), f(mainS['hi'], k))
    return 'Across the %d preregistered readings, the %s design changes %s by %s to %s %s; at the main row, %s %s (seed interval %s to %s).' % (
        cl['n'], DESL[design], nm, f(cl['min'], k), f(cl['max'], k), u, f(mainS['est'], k), u, f(mainS['lo'], k), f(mainS['hi'], k))


def pidx(design_meta):
    """id or alias -> point index"""
    m = {}
    for p in design_meta:
        m[p['id']] = p['p']
        for a in p['alias']: m[a] = p['p']
    return m


def rk(env, p, r): return '%s.p%04d.%s' % (env, p, r)


def label(pt):
    if pt['kind'] == 'main': return 'main row'
    x = ', '.join('%s=%s' % (a, ('%.4g' % v) if isinstance(v, float) else v) for a, v in sorted(pt['x'].items()))
    return (pt['id'] + (' [' + x + ']' if pt['kind'] == 'bound' else '') + (' (' + pt['mod'] + ')' if pt['mod'] and pt['kind'] not in ('backing', 'fixed') else ''))


def curve_points(D, design, k):
    """the curve: the main row, every single reading, every pair's joint point, the least-favourable bound for (design, k)"""
    ix = pidx(D); pts = [p for p in D if p['kind'] in ('main', 'single', 'pair')]
    b = ix.get('bound.%s.%s' % (design, k))  # a bound equal to a single reading (C2.2's inflation bound is wIdx 0.75) is drawn once
    if b is not None and D[b] not in pts: pts.append(D[b])
    return [p for p in pts if design in p['rows']]


# ---------------------------------------------------------------- main
def main():
    global BS, REPS
    a = sys.argv[1:]
    if len(a) < 2: sys.exit(__doc__)
    RES, OUT = a[0], a[1]
    eng = a[a.index('--engine') + 1] if '--engine' in a else '104691f'
    BKM = a[a.index('--bkm') + 1] if '--bkm' in a else None
    if '--reps' in a: REPS = int(a[a.index('--reps') + 1])
    BS = np.random.default_rng(6301).integers(0, 500, size=(REPS, 500))
    os.makedirs(os.path.join(OUT, 'curves'), exist_ok=True)
    SUM = {'engine': eng, 'reps': REPS, 'checks': [], 'q1': [], 'curves': {}, 'pairs': {}, 'backing': {}, 'financed': {}, 'dist': [], 'work': [],
           'named': [], 'fixed': {}, 'big': [], 'a0price': []}
    chk = SUM['checks']
    M = {}  # (env, years) -> part M rows (derived)
    for e in ENVS:
        for y in YEARS:
            r, _ = load(os.path.join(RES, 'r2-m-%s-%d-%s' % (e, y, eng)))
            M[(e, y)] = {n.split('.', 1)[1]: derive(v, y) for n, v in r.items()}
    # check: the 20-year run equals the first 20 years of the 40-year run
    for e in ENVS:
        bad = 0
        for row in M[(e, 20)]:
            for k, v in M[(e, 20)][row].items():
                if '_' in k and k.rsplit('_', 1)[1].isdigit() and int(k.rsplit('_', 1)[1]) < 20 and k in M[(e, 40)][row]:
                    if not np.array_equal(v, M[(e, 40)][row][k]): bad += 1
        chk.append('%s: yearly series of the 20-year run equal the first 20 years of the 40-year run in every row of part M: %s' % (ENVL[e], 'yes' if not bad else 'NO (%d series differ)' % bad))

    thrW = {(e, y): 0.05*float(M[(e, y)]['none']['wtMedE'].mean()) for e in ENVS for y in YEARS}
    thrWF = {(e, y): 0.05*float(M[(e, y)]['Fnone']['wtMedE'].mean()) for e in ENVS for y in YEARS}

    # ---------------- Q1: the primary family on the main row
    L = []; p = L.append
    q1 = SUM['q1']
    for d in DES:
        for e in ENVS:
            for y in YEARS:
                R = M[(e, y)]
                for k, nm, how, thr in PRIM:
                    s = est(diff(R, d, 'none', k)); mat, th = material(k, s['est'], thrW[(e, y)])
                    q1.append({'design': d, 'env': e, 'years': y, 'key': k, 'none': float(R['none'][k].mean()*SCALE.get(k, 1)), 'prog': float(R[d][k].mean()*SCALE.get(k, 1)),
                               's': s, 'material': mat, 'thr': th})
    for x, hp in zip(q1, holm([x['s']['p'] for x in q1])): x['holm'] = hp
    nEx = sum(1 for x in q1 if excl(x['s'])); nH = sum(1 for x in q1 if x['holm'] < 0.05); nM = sum(1 for x in q1 if x['material'] and excl(x['s']))
    p('# Round 2, question 1: the main effects (primary family)'); p('')
    p('Generated by `python3 dev/tools/s64_tables.py` from compassionism-sim-results `r2-m-<env>-<years>-%s` (part M, full precision), seeds 1-500. Main row: harness.js `r2FreezePair` (full backing, a design parameter; today\'s price rule; S69\'s two reporting corrections). Effect: programme run minus its own no-programme run, mean over seeds; 95%% paired-bootstrap interval (%d resamples, generator seed 6301); p: two-sided paired t; Holm across the 60 tests. "Material": at or above rule 3\'s threshold (1 point; 1 point a year; 5%% of the no-programme median real wealth). Wealth figures rest on today\'s price rule (rule 6).' % (eng, REPS)); p('')
    p('**%d of 60 intervals exclude zero; %d tests survive Holm at 5%%; %d effects are material with an interval excluding zero.**' % (nEx, nH, nM)); p('')
    for d in DES:
        p('## %s' % DESL[d]); p('')
        p('| Environment | Years | Outcome | No programme | Programme | Effect (95% interval) | p | Holm p | Material |'); p('|---|---|---|---|---|---|---|---|---|')
        for x in q1:
            if x['design'] != d: continue
            k = x['key']
            p('| %s | %d | %s | %s | %s | %s | %s | %s | %s |' % (ENVL[x['env']], x['years'], SHORT[k], f(x['none'], k), f(x['prog'], k), ci(x['s'], k), pf(x['s']['p']), pf(x['holm']),
              'yes' if x['material'] else 'no (threshold %s)' % f(x['thr'], k)))
        p('')
    p('## Beside the headline: wealth at fixed years and as yearly averages, the within-year cost of living, programme cost'); p('')
    p('Same pairing and interval; not in the 60 tests. Wealth poverty and median wealth at year 20 and year 40 (`ppov_19`, `ppov_39`, `pmedW_*`), the yearly average of median wealth (`pmedWA`), basket poverty on the within-year count (`wyF0PY`, beside every basket-poverty figure), programme cost a year.'); p('')
    BES = [('ppov20', 'wealth poverty, year 20', 'points'), ('ppov40', 'wealth poverty, year 40', 'points'), ('pmedWA', 'median real wealth, yearly average', '$'),
           ('pmedW20', 'median real wealth, year 20', '$'), ('pmedW40', 'median real wealth, year 40', '$'), ('wyF0PY', 'basket poverty, within-year count', 'points'), ('cost', 'programme cost per adult a year (year-0 $)', '$')]
    p('| Design | Environment | Years | ' + ' | '.join(b[1] for b in BES) + ' |'); p('|---|---|---|' + '---|'*len(BES))
    SUM['q1beside'] = []
    for d in DES:
        for e in ENVS:
            for y in YEARS:
                R = M[(e, y)]; cells = []
                for k, nm, u in BES:
                    dd = diff(R, d, 'none', k)
                    if dd is None: cells.append('–'); continue
                    s = est(dd); kk = 'wtMedE' if u == '$' else k; cells.append(ci(s, kk)); SUM['q1beside'].append({'design': d, 'env': e, 'years': y, 'key': k, 's': s})
                p('| %s | %s | %d | %s |' % (DESL[d], ENVL[e], y, ' | '.join(cells)))
    p('')
    open(os.path.join(OUT, 's64-q1-main.md'), 'w').write('\n'.join(L) + '\n')

    # ---------------- parts S and F: curves, pairs, backing, named, fixed
    curveL = []; pairL = []; backL = []; namedL = []; fixL = []; finL = []
    bkm = {}
    for blk, part in (('S', 's'), ('F', 'f')):
        for e in ENVS:
            for y in YEARS:
                rows, meta = load(os.path.join(RES, 'r2-%s-%s-%d-%s' % (part, e, y, eng)))
                D = meta['design']; ix = pidx(D)
                # check: the block's main point equals part M's main rows (7 significant digits)
                mm = {'none': 'none', 'c22': 'c22', 'rel': 'rel'} if blk == 'S' else {'none': 'Fnone', 'c22': 'Fc22', 'rel': 'Frel'}
                worst = 0.0
                for r0, rM in mm.items():
                    for k, v in rows[rk(e, 0, r0)].items():
                        if k in M[(e, y)][rM]:
                            ref = M[(e, y)][rM][k]; den = np.maximum(np.abs(ref), 1e-12)
                            worst = max(worst, float(np.max(np.abs(v - ref)/den)))
                chk.append('part %s %s %d years: main point against part M, largest relative difference %.1e (7 significant digits stored)' % (blk, ENVL[e], y, worst))
                keys = [x[0] for x in PRIM] + (['gvDebtY', 'gvY100'] if blk == 'F' else [])
                tW = thrW[(e, y)] if blk == 'S' else thrWF[(e, y)]
                for d in DES:
                    for k in keys:
                        how = 'median' if k in ('gvDebtY', 'gvY100') else 'mean'
                        pts = []
                        for pt in curve_points(D, d, k):
                            # the year debt passes GDP is read as the programme run's own year (median; horizon + 1 = not within the run):
                            # the no-programme run's debt never passes, so a difference would carry no information rule 2 could read
                            dd = rows[rk(e, pt['p'], d)][k].copy() if k == 'gvY100' else diff(rows, rk(e, pt['p'], d), rk(e, pt['p'], 'none'), k)
                            s = est(dd, how)
                            m0 = rows[rk(e, 0, d)][k] if k == 'gvY100' else diff(rows, rk(e, 0, d), rk(e, 0, 'none'), k)
                            sh = est(dd - m0, how) if pt['p'] else None
                            pts.append({'p': pt['p'], 'label': label(pt),
                                        'kind': pt['kind'], 's': s, 'shift': sh})
                        mainS = pts[0]['s']; mat, thr = material(k, mainS['est'], tW)
                        if k == 'gvY100':
                            pas = [q['label'] for q in pts if q['s']['est'] <= y]
                            cl = {'n': len(pts), 'same': len(pts) - len(pas), 'opp': len(pas), 'share': 1 - len(pas)/len(pts), 'min': min(q['s']['est'] for q in pts), 'max': max(q['s']['est'] for q in pts),
                                  'class': 'debt passes GDP within the run (median) at %d points' % len(pas) if pas else 'debt stays below GDP at every point', 'notSame': pas, 'reverse': pas, 'material': bool(pas)}
                            cl['sentence'] = ''
                        else:
                            cl = classify(pts, mainS, k, thr); cl['sentence'] = sentence(d, k, cl, mainS, thr)
                        cl['main'] = mainS; cl['thr'] = thr
                        cid = '%s-%s-%s-%s-%d' % (blk, d, k, e, y)
                        SUM['curves'][cid] = cl
                        with open(os.path.join(OUT, 'curves', cid + '.csv'), 'w', newline='') as fh:
                            w = csv.writer(fh); w.writerow(['rank', 'point', 'reading', 'kind', 'estimate', 'lo95', 'hi95', 'excludes_zero', 'shift_from_main', 'shift_lo95', 'shift_hi95'])
                            for i, q in enumerate(sorted(pts, key=lambda q: q['s']['est'])):
                                sh = q['shift'] or {'est': 0, 'lo': 0, 'hi': 0}
                                w.writerow([i + 1, q['p'], q['label'], q['kind'], '%.6g' % q['s']['est'], '%.6g' % q['s']['lo'], '%.6g' % q['s']['hi'], int(excl(q['s'])), '%.6g' % sh['est'], '%.6g' % sh['lo'], '%.6g' % sh['hi']])
                        if blk == 'S' and k in ('bNAPy', 'fgt0PY', 'ppovA', 'wtMedE', 'endoAnn'):
                            prs = [q for q in pts if q['kind'] == 'single' and q['label'].split('.', 1)[1].split('=')[0] in ('prK', 'prR', 'prA', 'prH', 'prBd')]
                            cl['priceWithinNoise'] = all(not excl(q['shift']) or abs(q['shift']['est']) < thr for q in prs)
                            cl['priceShifts'] = [(q['label'], q['shift']) for q in prs]
                    # pairs (rule 5): interaction contrasts
                    for q in sorted({a2[len('pair.'):] for p2 in D for a2 in [p2['id']] + p2['alias'] if a2.startswith('pair.')}):
                        P4 = [ix['pairbase.' + q], ix['pairA.' + q], ix['pairB.' + q], ix['pair.' + q]]
                        for k in keys:
                            how = 'median' if k in ('gvDebtY', 'gvY100') else 'mean'
                            E4 = [diff(rows, rk(e, i, d), rk(e, i, 'none'), k) for i in P4]
                            s = est(E4[3] - E4[1] - E4[2] + E4[0], how)
                            mat, thr = material(k, s['est'], tW)
                            ag = np.median if how == 'median' else np.mean
                            SUM['pairs'].setdefault(blk, []).append({'pair': q, 'design': d, 'key': k, 'env': e, 'years': y, 's': s, 'material': mat, 'thr': thr,
                                                                     'alone': [float(ag(E4[1] - E4[0])), float(ag(E4[2] - E4[0]))]})
                if blk == 'S':
                    # backing curve (Q4): a 0, 0.25, 0.5, 0.75 and 1 (the main row); mechanism points; the price readings at a 0
                    grid = [(0.0, ix['back.a=0']), (0.25, ix['back.a=0.25']), (0.5, ix['back.a=0.5']), (0.75, ix['back.a=0.75']), (1.0, 0)]
                    nb = rk(e, 0, 'none')
                    for d in DES:
                        B = {'grid': [], 'mech': {}}
                        for aa, i in grid:
                            B['grid'].append({'a': aa, 'p': i, 'eff': {k: est(diff(rows, rk(e, i, d), nb, k)) for k, _, _, _ in PRIM}})
                        def crossing(fun, idx):
                            """scanning from a = 1 down: the backed share where fun(a) reaches 0 (interpolated); 'above 1' / 'below 0'"""
                            vals = [fun(g['p'], idx) for g in B['grid']]  # a ascending
                            if vals[-1] >= 0: return 'above 1'
                            for j in range(len(vals) - 1, 0, -1):
                                if vals[j - 1] >= 0:
                                    a0, a1, v0, v1 = grid[j - 1][0], grid[j][0], vals[j - 1], vals[j]
                                    return a0 + (a1 - a0)*v0/(v0 - v1)
                            return 'below 0'
                        def mk(k, off):
                            def fun(i, idx):
                                dd = diff(rows, rk(e, i, d), nb, k); return (dd.mean() if idx is None else dd[idx].mean()) - off
                            return fun
                        for name, k, off in (('inflation5', 'endoAnn', 5.0), ('wealthPoverty0', 'ppovA', 0.0)):
                            fun = mk(k, off); c0 = crossing(fun, None); bs = [crossing(fun, BS[j]) for j in range(REPS)]
                            num = [x for x in bs if not isinstance(x, str)]
                            B[name] = {'est': c0, 'lo': float(np.percentile(num, 2.5)) if num else None, 'hi': float(np.percentile(num, 97.5)) if num else None,
                                       'above1': sum(1 for x in bs if x == 'above 1')/REPS, 'below0': sum(1 for x in bs if x == 'below 0')/REPS}
                        for nm2 in ('back.bkm', 'back.bkmNc'):
                            i = ix[nm2]; m2 = {'p': i, 'eff': {k: est(diff(rows, rk(e, i, d), nb, k)) for k, _, _, _ in PRIM}}
                            if BKM:
                                fp = os.path.join(BKM, 'bkm-%s-%d.json' % (e, y))
                                if os.path.exists(fp):
                                    J = json.load(open(fp)); rr = J['rows'][rk(e, i, d)]
                                    same = all(np.array_equal(np.array(rr[k2], dtype=float), rows[rk(e, i, d)][k2]) for k2 in rows[rk(e, i, d)])
                                    m2['bkA'] = est(np.array(rr['bkA'], dtype=float)); m2['bkmO19'] = float(np.mean(rr['bkmO19'])); m2['replayEqual'] = same
                            B['mech'][nm2] = m2
                        B['a0price'] = []
                        for pid in [x['id'] for x in D if x['kind'] == 'a0price']:
                            i = ix[pid]; B['a0price'].append({'id': pid, 'eff': {k: est(diff(rows, rk(e, i, d), rk(e, i, 'none'), k)) for k, _, _, _ in PRIM}})
                        SUM['backing']['%s-%s-%d' % (d, e, y)] = B
                        # named readings (exploratory) and the fixed-share rows
                        for pt in [x for x in D if x['kind'] == 'named' or any(al.startswith('named.') for al in x['alias'])]:
                            nm3 = pt['id'] if pt['kind'] == 'named' else [al for al in pt['alias'] if al.startswith('named.')][0]
                            SUM['named'].append({'id': nm3, 'design': d, 'env': e, 'years': y,
                                                 'eff': {k: est(diff(rows, rk(e, pt['p'], d), rk(e, pt['p'], 'none'), k)) for k, _, _, _ in PRIM},
                                                 'shift': {k: est(diff(rows, rk(e, pt['p'], d), rk(e, pt['p'], 'none'), k) - diff(rows, rk(e, 0, d), nb, k)) for k, _, _, _ in PRIM}})
                        fx = [(int(x['id'].split('.')[1]), x['p']) for x in D if x['kind'] == 'fixed']
                        FX = {sh: {k: est(diff(rows, rk(e, i, d), nb, k)) for k, _, _, _ in PRIM} for sh, i in fx}
                        FXd = {}
                        for k, _, _, _ in PRIM:
                            best = max(FX, key=lambda sh: FAV[k]*FX[sh][k]['est'])
                            dv = est(diff(rows, rk(e, dict(fx)[best], d), nb, k) - diff(rows, rk(e, dict(fx)[100], d), nb, k)) if best != 100 else None
                            lowAny = best <= 30 and dv is not None and excl(dv) and sgn(dv['est']) == FAV[k]
                            FXd[k] = {'best': best, 'vs100': dv, 'lowAny': lowAny, 'low': lowAny and material(k, dv['est'], tW)[0]}  # rule 3 applies to rule 7's difference too
                        SUM['fixed']['%s-%s-%d' % (d, e, y)] = {'eff': FX, 'opt': FXd}
                if blk == 'F':
                    R = M[(e, y)]
                    for d in DES:
                        pr = 'F' + d; X = R[pr]
                        out = {'tauMean': est(X['tauMean']*100), 'defShare': est(X['gvDef']/np.maximum(X['gvPay'], 1e-12)*100), 'finGapSh': est(X['finGapSh']),
                               'debt': est(X['gvDebtY'], 'median'), 'debtEff': est(X['gvDebtY'] - R['Fnone']['gvDebtY'], 'median'),
                               'y100': est(X['gvY100'], 'median'), 'passShare': float(np.mean(X['gvY100'] <= y)), 'noneDebt': float(np.median(R['Fnone']['gvDebtY'])),
                               'eff': {k: est(diff(R, pr, 'Fnone', k)) for k, _, _, _ in PRIM}}
                        out['unsustainable'] = out['y100']['est'] <= y  # the median year debt passes GDP falls within the run (20 or 40 years)
                        SUM['financed']['%s-%s-%d' % (d, e, y)] = out
                del rows

    # ---------------- Q6 and Q7 (part M) and the 10,000-adult pair (part B)
    DIST = [('dmWt1E', 'top 1% share of wealth (%)'), ('dmWt10E', 'top 10% share of wealth (%)'), ('dmYt1E', 'top 1% share of income (%)'), ('dmYt10E', 'top 10% share of income (%)'),
            ('dmYpE', 'Palma ratio of income (top 10% / bottom 40%)'), ('dmWb50E', 'bottom 50% share of wealth (%)'), ('dmYb50E', 'bottom 50% share of income (%)'),
            ('dmWp10E', 'wealth P10 ($)'), ('dmWp25E', 'wealth P25 ($)'), ('dmWp50E', 'wealth P50 ($)'), ('dmWp75E', 'wealth P75 ($)'), ('dmWp90E', 'wealth P90 ($)'), ('dmWp99E', 'wealth P99 ($)'), ('wtP999E', 'wealth P99.9 ($, weighted tail)'),
            ('dmYp10E', 'income P10 ($)'), ('dmYp50E', 'income P50 ($)'), ('dmYp90E', 'income P90 ($)'), ('dmYp99E', 'income P99 ($)'),
            ('dmMob00', 'stayed in the lowest wealth fifth (%)'), ('dmMob44', 'stayed in the top wealth fifth (%)'), ('dmMob04', 'lowest fifth to top fifth (%)'),
            ('dmLsPY', "labour's share of money income (%)"), ('dmFdE', 'families in debt (%)')]
    WORK = [('emp', 'employment (% of adult-years)'), ('hrs', 'hours (relative to the no-change level)'), ('lfPart', 'participation (% of adult-years)'), ('lfOut', 'outside the labour force (% of adult-years)'),
            ('lpOut', 'programme leavers (% of adult-years)'), ('lpE', 'earnings forgone by leavers ($ per adult-year)')]
    for tab, spec, store in (('dist', DIST, SUM['dist']), ('work', WORK, SUM['work'])):
        for d in DES:
            for e in ENVS:
                for y in YEARS:
                    R = M[(e, y)]; cells = []
                    for k, nm in spec:
                        dd = diff(R, d, 'none', k)
                        if dd is None: continue
                        cells.append({'key': k, 'name': nm, 'none': float(R['none'][k].mean()), 'prog': float(R[d][k].mean()), 's': est(dd)})
                    for c, hp in zip(cells, holm([c['s']['p'] for c in cells])): c['holm'] = hp
                    store.append({'design': d, 'env': e, 'years': y, 'cells': cells})
    for e in ENVS:
        for y in YEARS:
            r, _ = load(os.path.join(RES, 'r2-b-%s-%d-%s' % (e, y, eng)))
            R = {n.split('.', 1)[1]: derive(v, y) for n, v in r.items()}
            for d in DES:
                SUM['big'].append({'design': d, 'env': e, 'years': y, 'eff': {k: est(diff(R, d, 'none', k)) for k in [x[0] for x in PRIM] + ['hrs', 'emp', 'lfPart', 'wtT1E', 'wtT10E', 'dmWt1E']},
                                   'small': {k: est(diff(M[(e, y)], d, 'none', k)) for k in ['hrs', 'emp', 'lfPart', 'wtT1E', 'wtT10E', 'dmWt1E']}})
            del r

    # ---------------- write the remaining tables
    # Q2
    L = []; p = L.append
    p('# Round 2, question 2: robustness across the specification curve'); p('')
    p('Generated by `python3 dev/tools/s64_tables.py`. On the financed rows the year debt passes GDP is the programme run\'s own year (median over seeds; horizon + 1 = not within the run), and its columns count the points where debt stays below GDP and where it passes. One curve per outcome, design, environment and horizon: the main row, the 32 single readings S70\'s rules carry (Source rows; 49 on the financed rows), the 28 flagged pairs at their joint point (66 financed), and the least-favourable bound for that outcome and design: 62 points on the Source rows, 117 on the financed rows. Every point is a pair run on seeds 1-500 (part S, 7 significant digits). Rule 2: robust = every point\'s interval excludes zero with the main row\'s sign; mostly robust = at least 90% do and none excludes zero with the opposite sign; fragile otherwise. Rule 3: an effect below materiality at the main row is "no material change". Each curve\'s points are in `curves/<block>-<design>-<outcome>-<env>-<years>.csv`. Wealth figures rest on today\'s price rule (rule 6). The financed rows run without the weighted tail.'); p('')
    for blk, title in (('S', 'Source rows (C2.2 and the release design paid for by the Source)'), ('F', 'Financed rows (a contribution, the rest borrowed; never led with, D23)')):
        p('## ' + title); p('')
        p('| Design | Outcome | Environment | Years | Main row (95% interval) | Range across the curve | Points with the main sign excluding zero | Opposite sign excluding zero | Rule 2 | Material at main |')
        p('|---|---|---|---|---|---|---|---|---|---|')
        for d in DES:
            for k in [x[0] for x in PRIM] + (['gvDebtY', 'gvY100'] if blk == 'F' else []):
                for e in ENVS:
                    for y in YEARS:
                        c = SUM['curves']['%s-%s-%s-%s-%d' % (blk, d, k, e, y)]
                        p('| %s | %s | %s | %d | %s | %s to %s | %d of %d | %d | %s | %s |' % (DESL[d], SHORT[k], ENVL[e], y, ci(c['main'], k), f(c['min'], k), f(c['max'], k), c['same'], c['n'], c['opp'], c['class'], 'yes' if c['material'] else 'no'))
        p('')
    p('## Headline sentences (rule 1), Source rows'); p('')
    for d in DES:
        for k in [x[0] for x in PRIM]:
            for e in ENVS:
                for y in YEARS:
                    c = SUM['curves']['S-%s-%s-%s-%d' % (d, k, e, y)]
                    tail = '' if c['class'] != 'fragile' else ' Fragile: the readings without an interval excluding zero with the main sign: %s.' % (', '.join(c['notSame'][:12]) + (' and %d more' % (len(c['notSame']) - 12) if len(c['notSame']) > 12 else ''))
                    p('- **%s, %d years.** %s (%s.)%s' % (ENVL[e], y, c['sentence'], c['class'], tail))
            p('')
    p('## The price rule\'s readings at full backing (expected within seed noise of the main row; S70 rule 6)'); p('')
    p('Shift from the main row (paired; 95% interval) of each price-rule single reading, Source rows. "Within noise": the shift\'s interval includes zero or the shift is below materiality.'); p('')
    p('| Design | Outcome | Environment | Years | Within noise | Largest shift (reading) |'); p('|---|---|---|---|---|---|')
    for d in DES:
        for k in [x[0] for x in PRIM]:
            for e in ENVS:
                for y in YEARS:
                    c = SUM['curves']['S-%s-%s-%s-%d' % (d, k, e, y)]
                    big = max(c['priceShifts'], key=lambda q: abs(q[1]['est']))
                    p('| %s | %s | %s | %d | %s | %s (%s) |' % (DESL[d], SHORT[k], ENVL[e], y, 'yes' if c['priceWithinNoise'] else 'no', ci(big[1], k), big[0]))
    p('')
    open(os.path.join(OUT, 's64-q2-curves.md'), 'w').write('\n'.join(L) + '\n')

    # Q3
    L = []; p = L.append
    p('# Round 2, question 3: interactions in the flagged pairs'); p('')
    p('Generated by `python3 dev/tools/s64_tables.py`. For each pair S70 flagged (28 on the Source rows, 66 on the financed rows): the interaction contrast (both together - A alone - B alone + base), paired over seeds 1-500, with its 95% bootstrap interval, for every outcome, design, environment and horizon. A synergy or antagonism is claimed only where the interval excludes zero (research rule 4); "material" uses rule 3\'s thresholds on the contrast. Exploratory family: displayed, not tested.'); p('')
    for blk in ('S', 'F'):
        PS = SUM['pairs'][blk]; ex = [x for x in PS if excl(x['s'])]; exm = [x for x in ex if x['material']]
        p('## %s rows: %d contrasts, %d with an interval excluding zero, %d of them material' % ('Source' if blk == 'S' else 'Financed', len(PS), len(ex), len(exm))); p('')
        p('| Pair | Contrasts | Excluding zero | Material and excluding zero | Largest material contrast (cell) |'); p('|---|---|---|---|---|')
        for q in sorted({x['pair'] for x in PS}):
            Q = [x for x in PS if x['pair'] == q]; Qe = [x for x in Q if excl(x['s'])]; Qm = [x for x in Qe if x['material']]
            big = max(Qm, key=lambda x: abs(x['s']['est'])/x['thr']) if Qm else None  # largest relative to its materiality threshold
            p('| %s | %d | %d | %d | %s |' % (q, len(Q), len(Qe), len(Qm), '–' if not big else '%s %s (%s, %s, %d y)' % (SHORT[big['key']], ci(big['s'], big['key']), DESL[big['design']], ENVL[big['env']], big['years'])))
        p('')
        p('### Every material contrast with an interval excluding zero'); p('')
        p('| Pair | Design | Outcome | Environment | Years | Contrast (95% interval) | A alone | B alone |'); p('|---|---|---|---|---|---|---|---|')
        for x in sorted(exm, key=lambda x: (x['pair'], x['design'], x['key'], x['env'], x['years'])):
            p('| %s | %s | %s | %s | %d | %s | %s | %s |' % (x['pair'], DESL[x['design']], SHORT[x['key']], ENVL[x['env']], x['years'], ci(x['s'], x['key']), f(x['alone'][0], x['key']), f(x['alone'][1], x['key'])))
        p('')
    open(os.path.join(OUT, 's64-q3-pairs.md'), 'w').write('\n'.join(L) + '\n')

    # Q4
    L = []; p = L.append
    p('# Round 2, question 4: the backing curve'); p('')
    p('Generated by `python3 dev/tools/s64_tables.py`. The backed share `a` (the share of the payout matched by new output) at 0, 0.25, 0.5, 0.75 and 1. **1 is the main row: "full backing, as the design states"** (a design parameter, ledger D25), not an estimate. Programme runs against the main row\'s no-programme run. Break-even shares: scanning down from 1, where programme inflation reaches 5 points a year, and where wealth poverty (yearly average) is no better than with no programme, by linear interpolation between the grid points either side; 95% interval from the bootstrap crossings; "above 1" when the main row is already past the threshold, "below 0" when no grid point reaches it (never extrapolated). The mechanism\'s points: S51\'s main reading (only added output absorbs new money, ceiling 8% of earned income, lag 2 years, wear 5%, at the most productive setting S51 shows) and the same without the ceiling, with the backed share they reach (`bkA`, from the replay of those two points).'); p('')
    for d in DES:
        p('## %s' % DESL[d]); p('')
        p('| Environment | Years | Backed share | ' + ' | '.join(SHORT[k] for k, _, _, _ in PRIM) + ' |'); p('|---|---|---|' + '---|'*len(PRIM))
        for e in ENVS:
            for y in YEARS:
                B = SUM['backing']['%s-%s-%d' % (d, e, y)]
                for g in B['grid']:
                    p('| %s | %d | %s | %s |' % (ENVL[e], y, ('%.2f' % g['a']) + (' (main row, full backing as the design states)' if g['a'] == 1 else ''), ' | '.join(ci(g['eff'][k], k) for k, _, _, _ in PRIM)))
                for nm2, lab in (('back.bkm', "mechanism, S51's main reading"), ('back.bkmNc', 'mechanism, no ceiling')):
                    m2 = B['mech'][nm2]; ba = ' (reaches %s%% backed)' % ci(m2['bkA'], 'x') if 'bkA' in m2 else ''
                    p('| %s | %d | %s%s | %s |' % (ENVL[e], y, lab, ba, ' | '.join(ci(m2['eff'][k], k) for k, _, _, _ in PRIM)))
        p('')
        p('### Break-even backed shares'); p('')
        p('| Environment | Years | Inflation reaches 5 points a year at a = | Wealth poverty no better than no programme at a = | Mechanism reaches (main reading / no ceiling) | Rule 4 |'); p('|---|---|---|---|---|---|')
        for e in ENVS:
            for y in YEARS:
                B = SUM['backing']['%s-%s-%d' % (d, e, y)]
                def be(x):
                    s = x['est'] if isinstance(x['est'], str) else '%.3f' % x['est']
                    iv = (' (%.3f to %.3f)' % (x['lo'], x['hi'])) if x['lo'] is not None else ''
                    tl = []
                    if x['above1']: tl.append('above 1 in %.0f%% of resamples' % (100*x['above1']))
                    if x['below0']: tl.append('below 0 in %.0f%%' % (100*x['below0']))
                    return s + iv + ('; ' + ', '.join(tl) if tl else '')
                mk2 = [B['mech'][n2].get('bkA') for n2 in ('back.bkm', 'back.bkmNc')]
                mech = ' / '.join('%.3f' % (m['est']/100) if m else '–' for m in mk2)
                i5 = B['inflation5']['est']; r4 = '–'
                if mk2[0] is not None:
                    above = i5 == 'above 1' or (not isinstance(i5, str) and i5 > mk2[0]['est']/100)
                    r4 = 'break-even above the mechanism\'s point: say so beside any inflation headline' if above else 'mechanism at or above break-even'
                B['rule4'] = r4
                p('| %s | %d | %s | %s | %s | %s |' % (ENVL[e], y, be(B['inflation5']), be(B['wealthPoverty0']), mech, r4))
        p('')
        p('### The price rule\'s readings at no assumed backing (a = 0; each with its own no-programme run)'); p('')
        p('| Environment | Years | Reading | ' + ' | '.join(SHORT[k] for k, _, _, _ in PRIM) + ' |'); p('|---|---|---|' + '---|'*len(PRIM))
        for e in ENVS:
            for y in YEARS:
                B = SUM['backing']['%s-%s-%d' % (d, e, y)]
                p('| %s | %d | today\'s rule (a = 0 point) | %s |' % (ENVL[e], y, ' | '.join(ci(B['grid'][0]['eff'][k], k) for k, _, _, _ in PRIM)))
                for x in B['a0price']:
                    p('| %s | %d | %s | %s |' % (ENVL[e], y, x['id'], ' | '.join(ci(x['eff'][k], k) for k, _, _, _ in PRIM)))
        p('')
    open(os.path.join(OUT, 's64-q4-backing.md'), 'w').write('\n'.join(L) + '\n')

    # Q5
    L = []; p = L.append
    p('# Round 2, question 5: the financed rows (never led with; D23)'); p('')
    p('Generated by `python3 dev/tools/s64_tables.py` from part M\'s financed main rows (full precision). C2.2: a contribution on all money income, share 1, cap 0.9 (the highest rate), the rest borrowed. The release design: a flat contribution on wages, the rest borrowed. Both at backed share 0 (who pays is the question here), the government account on, **without the weighted tail** (S72 Amendment 2). Rate: the contribution\'s mean rate. Deficit: the year\'s deficit as a share of the payout (`gvDef`/`gvPay`); not raised: the share of the payout the contribution does not raise (`finGapSh`). Debt: % of GDP at the end of the run, median over seeds (interval: bootstrap of the median). Year debt passes GDP: median (horizon + 1 = not within the run). Rule 5: unsustainable when the median year is within 40 years.'); p('')
    p('| Design | Environment | Years | Rate (%) | Deficit (% of payout) | Not raised (% of payout) | Debt, % of GDP (no programme) | Year debt passes GDP (share of seeds within the run) | Label |'); p('|---|---|---|---|---|---|---|---|---|')
    for d in DES:
        for e in ENVS:
            for y in YEARS:
                o2 = SUM['financed']['%s-%s-%d' % (d, e, y)]
                p('| %s | %s | %d | %s | %s | %s | %s (%s) | %s (%.0f%%) | %s |' % (DESL[d], ENVL[e], y, ci(o2['tauMean'], 'x'), ci(o2['defShare'], 'x'), ci(o2['finGapSh'], 'x'), ci(o2['debt'], 'x'), f(o2['noneDebt'], 'x'), ci(o2['y100'], 'gvY100'), 100*o2['passShare'],
                  'unsustainable (rule 5)' if o2['unsustainable'] else '–'))
    p('')
    p('## The five headline outcomes on the financed main rows'); p('')
    p('| Design | Environment | Years | ' + ' | '.join(SHORT[k] for k, _, _, _ in PRIM) + ' |'); p('|---|---|---|' + '---|'*len(PRIM))
    for d in DES:
        for e in ENVS:
            for y in YEARS:
                o2 = SUM['financed']['%s-%s-%d' % (d, e, y)]
                p('| %s | %s | %d | %s |' % (DESL[d], ENVL[e], y, ' | '.join(ci(o2['eff'][k], k) for k, _, _, _ in PRIM)))
    p('')
    p('The financed rows\' specification curves are in `s64-q2-curves.md` (financed section) and `curves/F-*.csv`.'); p('')
    open(os.path.join(OUT, 's64-q5-financed.md'), 'w').write('\n'.join(L) + '\n')

    # Q6, Q7
    for tab, title, intro in (('dist', 'Round 2, question 6: distribution (secondary family)', 'S57\'s measures at the end of the run, weighted (`dm*E`; wealth and income in real, year-0 dollars of the living-wage basket). Mobility: the share of adults in a year-0 wealth fifth found in a given fifth at the end. Labour\'s share: wages over money income, all years. **Not computed here:** the erosion share of each wealth figure (S66 trace, part B), which needs the per-adult trace on the frozen row (S64 part 3), and basket poverty by labour-force reason (S61\'s key, not among the batch\'s outputs).'),
                              ('work', 'Round 2, question 7: work (secondary family)', 'Participation and hours on the main row (S73, S68). Every participation figure is printed with programme leavers (share of adult-years) and their earnings forgone, and with what the model does not count: the value of care, community work and new ventures (S73 section 6). Hours at 500 adults are printed with the 10,000-adult figure (part B) below.')):
        L = []; p = L.append
        p('# ' + title); p(''); p('Generated by `python3 dev/tools/s64_tables.py` from part M. Effect: programme minus no programme, paired over seeds 1-500, 95% bootstrap interval; Holm within each table (one table per design, environment and horizon). ' + intro); p('')
        for t in SUM[tab]:
            cells = t['cells']; nH = sum(1 for c in cells if c['holm'] < 0.05); nE = sum(1 for c in cells if excl(c['s']))
            p('## %s, %s, %d years (%d of %d intervals exclude zero; %d survive Holm)' % (DESL[t['design']], ENVL[t['env']], t['years'], nE, len(cells), nH)); p('')
            p('| Measure | No programme | Programme | Effect (95% interval) | Holm p |'); p('|---|---|---|---|---|')
            for c in cells:
                dg = 0 if '$' in c['name'] else 2 if c['key'] != 'hrs' else 4
                p('| %s | %s | %s | %s | %s |' % (c['name'], f(c['none'], 'x', dg), f(c['prog'], 'x', dg), '%s (%s to %s)' % (f(c['s']['est'], 'x', dg), f(c['s']['lo'], 'x', dg), f(c['s']['hi'], 'x', dg)), pf(c['holm'])))
            p('')
        if tab == 'work':
            p('## The 10,000-adult main pair beside 500 adults (S68: no hours figure from 500 adults alone; S59: the tail at scale)'); p('')
            p('| Design | Environment | Years | Hours: 500 / 10,000 adults | Employment: 500 / 10,000 | Participation: 500 / 10,000 | Top 1% wealth share (tail): 500 / 10,000 |'); p('|---|---|---|---|---|---|---|')
            for b in SUM['big']:
                p('| %s | %s | %d | %s / %s | %s / %s | %s / %s | %s / %s |' % (DESL[b['design']], ENVL[b['env']], b['years'], *[ci(b[w][k], 'h') if k == 'hrs' else ci(b[w][k], 'x') for k in ('hrs', 'emp', 'lfPart', 'wtT1E') for w in ('small', 'eff')]))
            p('')
            p('### The 10,000-adult pair\'s headline outcomes'); p('')
            p('| Design | Environment | Years | ' + ' | '.join(SHORT[k] for k, _, _, _ in PRIM) + ' |'); p('|---|---|---|' + '---|'*len(PRIM))
            for b in SUM['big']:
                p('| %s | %s | %d | %s |' % (DESL[b['design']], ENVL[b['env']], b['years'], ' | '.join(ci(b['eff'][k], k) for k, _, _, _ in PRIM)))
            p('')
        open(os.path.join(OUT, 's64-q%s-%s.md' % ('6' if tab == 'dist' else '7', 'distribution' if tab == 'dist' else 'work')), 'w').write('\n'.join(L) + '\n')

    # named readings and fixed-share rows
    L = []; p = L.append
    p('# Round 2: the named readings and the fixed PTF share rows (exploratory; displayed)'); p('')
    p('Generated by `python3 dev/tools/s64_tables.py` from part S. Named readings: each with its own no-programme run; "shift" is the change from the main row\'s effect (paired). Fixed-share rows (S66, D16): the PTF share held at 10% to 100% with growth off, programme runs against the main row\'s no-programme run. Rule 7: no low-share optimum is claimed unless the 20- and 40-year rows both show one (the best share at 10-30%, and its difference from the 100% share excluding zero in the favourable direction); rule 3 (materiality) applies to that difference, as to every effect.'); p('')
    p('## Named readings'); p('')
    p('| Reading | Design | Environment | Years | ' + ' | '.join(SHORT[k] + ' (shift from main)' for k, _, _, _ in PRIM) + ' |'); p('|---|---|---|---|' + '---|'*len(PRIM))
    for x in sorted(SUM['named'], key=lambda x: (x['id'], x['design'], ENVS.index(x['env']), x['years'])):
        p('| %s | %s | %s | %d | %s |' % (x['id'], DESL[x['design']], ENVL[x['env']], x['years'], ' | '.join('%s (%s)' % (ci(x['eff'][k], k), f(x['shift'][k]['est'], k)) for k, _, _, _ in PRIM)))
    p('')
    p('## Fixed PTF share rows'); p('')
    for d in DES:
        for e in ENVS:
            for y in YEARS:
                F2 = SUM['fixed']['%s-%s-%d' % (d, e, y)]
                p('### %s, %s, %d years' % (DESL[d], ENVL[e], y)); p('')
                p('| PTF share | ' + ' | '.join(SHORT[k] for k, _, _, _ in PRIM) + ' |'); p('|---|' + '---|'*len(PRIM))
                for sh in sorted(F2['eff']): p('| %d%% | %s |' % (sh, ' | '.join(ci(F2['eff'][sh][k], k) for k, _, _, _ in PRIM)))
                p(''); p('Most favourable share: ' + '; '.join('%s %d%%%s' % (SHORT[k], F2['opt'][k]['best'], ' (low-share optimum at this horizon)' if F2['opt'][k]['low'] else '') for k, _, _, _ in PRIM) + '.'); p('')
    lows = []; anys = []
    for d in DES:
        for e in ENVS:
            for k, _, _, _ in PRIM:
                o20, o40 = SUM['fixed']['%s-%s-20' % (d, e)]['opt'][k], SUM['fixed']['%s-%s-40' % (d, e)]['opt'][k]
                if o20['low'] and o40['low']: lows.append('%s, %s, %s' % (DESL[d], ENVL[e], SHORT[k]))
                if o20['lowAny'] and o40['lowAny']: anys.append('%s, %s, %s (%s and %s at 20 and 40 years, against 100%%)' % (DESL[d], ENVL[e], SHORT[k], f(o20['vs100']['est'], k), f(o40['vs100']['est'], k)))
    SUM['rule7'] = lows; SUM['rule7any'] = anys
    p('**Rule 7 (with rule 3):** ' + ('a material low-share optimum at both horizons in: ' + '; '.join(lows) + '.' if lows else 'no outcome shows a material low-share optimum at both horizons; none is claimed.'))
    p(''); p('Before materiality is applied, a best share at 10-30% whose difference from the 100% share excludes zero at both horizons appears in: ' + ('; '.join(anys) if anys else 'none') + '. Each is below rule 3\'s threshold (no material change).'); p('')
    open(os.path.join(OUT, 's64-named-fixed.md'), 'w').write('\n'.join(L) + '\n')

    open(os.path.join(OUT, 's64-checks.md'), 'w').write('# Round 2: checks run by the tables tool\n\n' + '\n'.join('- ' + c for c in chk) + '\n')
    json.dump(SUM, open(os.path.join(OUT, 's64-summary.json'), 'w'), indent=0, default=lambda o: float(o) if isinstance(o, (np.floating,)) else bool(o) if isinstance(o, np.bool_) else str(o))
    print('wrote', OUT); print('\n'.join(chk))


if __name__ == '__main__':
    main()
