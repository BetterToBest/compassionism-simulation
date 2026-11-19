#!/usr/bin/env python3
"""S92 (Nov 19, 2026): the tables of the preregistered rerun with the private businesses' BU price at the sale
(research-update prereg/2026-11-s90-private-price-at-sale.md). Written before any result of the six folders was read.

  python3 dev/tools/s90_tables.py RESULTS_DIR OUT_DIR [--engine b8ccd8d] [--pub 104691f] [--swing FILE] [--acct FILE] [--reps 2000]

Reads the six folders s90-sale-<env>-<years>-<engine> of compassionism-sim-results (runner/jobs/s90.js; rows none, c22, rel, c22.sale, rel.sale; every key
at full precision; seeds 1-500 across shards) and the published part-M folders r2-m-<env>-<years>-<pub>.

Checks first (prereg "Checks"); the script stops before any outcome if one fails (decision rule 1):
  1. the no-programme row and the lagged rows (none, c22, rel) equal the published r2-m rows per seed on every key the published rows hold;
  2. every folder has DONE, run.txt and SHA256SUMS (each sum verified), shards covering seeds 1-500 once, the engine commit and a clean engine in every
     shard, and 500 values per key in every row;
  3. (run separately: dev/tools/s90_acct.js; pass its output with --acct to print it here.)
Then, per design (c22 full coverage, rel opt-in), environment and horizon, for each outcome: the effect against no programme under each rule (lagged, at
the sale) and the paired change (at the sale minus lagged); estimate the mean over seeds 1-500; 95% interval: paired bootstrap, 2,000 resamples, generator
seed 9001 (numpy default_rng), the same resample for every row; p: two-sided paired t; Holm across the five primary outcomes within each cell, for "the
change is not zero". Question 1's swing measure is printed from dev/tools/s90_swing.js's output (--swing).

Outcomes (prereg "Outcomes"; keys as REPRODUCE.md's headline table uses them):
  primary   bNAPy below 30 days of basic living (unweighted, points); fgt0PY basket poverty (unweighted, points); ppovA too little wealth, yearly average
            (unweighted, points; the mean of ppov_1 .. ppov_(T-1)); wtMedE median real wealth (weighted, year-0 $); endoAnn programme inflation (x 100,
            points a year).
  secondary fgt2PY FGT2 (poverty severity); Er real wage earnings per adult-year (year-0 $); dmYp50E median real disposable income at the last year
            (weighted, year-0 $); mfBU BU spent at face value per adult-year (year-0 $, mean over the run); mfIss - mfBU BU issued and not spent per
            adult-year (the BU that expire); cost programme cost per adult-year (year-0 $); wtF0E and wtPovE basket poverty and too little wealth at the
            last year (weighted, %).
  Reading of the secondary list (a reporting assumption, written before the results): the engine stores no mean real income key, so real wage earnings
  (Er) and the median of disposable income (dmYp50E) stand for it; BU spent and expired are stored per adult-year over all adults, not per programme
  adult; for the full-coverage design these are the same adults.
Question 3 (findings-page statements) is read against the page; the script marks each primary effect whose sign changes, or whose value at REPRODUCE.md's
rounding (2 decimals; whole dollars) changes, as input to that reading.
Standard library and numpy."""
import gzip, hashlib, json, math, os, sys, glob
import numpy as np

ENVS = ['ref', 'adv', 'str']; ENVL = {'ref': 'Reference', 'adv': 'Adverse', 'str': 'Stress'}; YEARS = [20, 40]
DES = ['c22', 'rel']; DESL = {'c22': 'full coverage', 'rel': 'opt-in'}
PRIM = ['bNAPy', 'fgt0PY', 'ppovA', 'wtMedE', 'endoAnn']
SEC = ['fgt2PY', 'Er', 'dmYp50E', 'mfBU', 'buLeft', 'cost', 'wtF0E', 'wtPovE']
LAB = {'bNAPy': 'below 30 days of basic living (points)', 'fgt0PY': 'basket poverty (points)', 'ppovA': 'too little wealth, yearly average (points)',
       'wtMedE': 'median real wealth, weighted (year-0 $)', 'endoAnn': 'programme inflation (points a year)', 'fgt2PY': 'FGT2, poverty severity',
       'Er': 'real wage earnings per adult-year ($)', 'dmYp50E': 'median real disposable income, last year, weighted ($)',
       'mfBU': 'BU spent per adult-year ($)', 'buLeft': 'BU issued and not spent per adult-year ($)', 'cost': 'programme cost per adult-year ($)',
       'wtF0E': 'basket poverty, last year, weighted (%)', 'wtPovE': 'too little wealth, last year, weighted (%)'}
SCALE = {'endoAnn': 100.0}
DOLLAR = {'wtMedE', 'Er', 'dmYp50E', 'mfBU', 'buLeft', 'cost'}
REPS = 2000; SEED = 9001


def opt(k, d):
    a = sys.argv
    return a[a.index('--' + k) + 1] if '--' + k in a else d


def shards(folder):
    files = sorted(glob.glob(os.path.join(folder, 'shard-*.json.gz')) or [f for f in glob.glob(os.path.join(folder, 'shard-*.json')) if not f.endswith('.timing.json')])
    if not files: return None
    D = [json.load(gzip.open(f) if f.endswith('.gz') else open(f)) for f in files]
    D.sort(key=lambda d: d['_meta']['seeds'][0])
    return D


def join(D):
    rows = {}
    for r in D[0]['rows']:
        rows[r] = {k: np.array([np.nan if x is None else x for d in D for x in d['rows'][r][k]], dtype=float) for k in D[0]['rows'][r]}
    return rows


def derive(r, T):
    if 'ppov_1' in r: r['ppovA'] = sum(r['ppov_%d' % t] for t in range(1, T))/(T - 1)
    if 'mfIss' in r and 'mfBU' in r: r['buLeft'] = r['mfIss'] - r['mfBU']
    return r


def check2(folder, engine):
    bad = []
    for f in ('DONE', 'run.txt', 'SHA256SUMS'):
        if not os.path.exists(os.path.join(folder, f)): bad.append(f + ' missing')
    if os.path.exists(os.path.join(folder, 'SHA256SUMS')):
        for line in open(os.path.join(folder, 'SHA256SUMS')):
            h, n = line.split()
            p = os.path.join(folder, n.lstrip('*'))
            if not os.path.exists(p) or hashlib.sha256(open(p, 'rb').read()).hexdigest() != h: bad.append('sum fails: ' + n)
    D = shards(folder)
    if not D: return bad + ['no shard files'], None
    s = 1
    for d in D:
        m = d['_meta']
        if m['seeds'][0] != s: bad.append('seed ranges not consecutive at ' + str(m['seeds']))
        s = m['seeds'][1] + 1
        man = m.get('manifest') or {}
        if not str(man.get('commit', '')).startswith(engine): bad.append('shard %s: engine %s' % (m['seeds'], man.get('commit')))
        if man.get('dirty') is not False: bad.append('shard %s: engine not recorded clean' % (m['seeds'],))
    if s != 501: bad.append('seeds do not cover 1-500 (end %d)' % (s - 1))
    rows = join(D)
    for r, kv in rows.items():
        for k, v in kv.items():
            if len(v) != 500: bad.append('%s %s: %d values' % (r, k, len(v))); break
    return bad, rows


def check1(new, pub, env):
    bad, n = [], 0
    for r in ('none', 'c22', 'rel'):
        a, b = new.get(env + '.' + r), pub.get(env + '.' + r)
        if a is None or b is None: bad.append('row %s missing' % r); continue
        for k, y in b.items():
            if k not in a: bad.append('%s: key %s missing' % (r, k)); continue
            x = a[k]; n += len(y)
            same = (x == y) | (np.isnan(x) & np.isnan(y))
            if not same.all(): bad.append('%s %s: %d seeds differ (first seed %d: %r against %r)' % (r, k, int((~same).sum()), int(np.argmax(~same)) + 1, x[~same][0], y[~same][0]))
    return bad, n


def tcdf(t, df):
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


def est(d, BS):
    n = len(d); m = float(d.mean()); v = d[BS].mean(axis=1); sd = float(d.std(ddof=1))
    p = 1.0 if sd == 0 and m == 0 else 0.0 if sd == 0 else 2*(1 - tcdf(abs(m)/(sd/math.sqrt(n)), n - 1))
    lo, hi = np.percentile(v, [2.5, 97.5])
    return {'est': m, 'lo': float(lo), 'hi': float(hi), 'p': p}


def holm(ps):
    k = len(ps); order = sorted(range(k), key=lambda i: ps[i]); adj = [0.0]*k; run = 0.0
    for j, i in enumerate(order): run = max(run, min(1.0, (k - j)*ps[i])); adj[i] = run
    return adj


def fmt(x, k):
    if k in DOLLAR: return '{:,.0f}'.format(x)
    return '%.3f' % x if abs(x) < 0.1 else '%.2f' % x


def ci(s, k): return '%s (%s to %s)' % (fmt(s['est'], k), fmt(s['lo'], k), fmt(s['hi'], k))
def rnd(x, k): return round(x) if k in DOLLAR else round(x, 2)


def main():
    if len(sys.argv) < 3: sys.exit(__doc__)
    R, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
    eng, pubE = opt('engine', 'b8ccd8d'), opt('pub', '104691f'); reps = int(opt('reps', REPS))
    BS = np.random.default_rng(SEED).integers(0, 500, size=(reps, 500))
    md, S = [], {'engine': eng, 'published': pubE, 'reps': reps, 'seed': SEED, 'checks': {}, 'cells': []}
    # ---- checks
    data, fail = {}, False
    md.append('# The main rows with the private BU price at the sale: tables\n')
    md.append('Engine `%s`; published rows `r2-m-*-%s`; paired over seeds 1-500; 95%% intervals by paired bootstrap (%d resamples, generator seed %d).\n' % (eng, pubE, reps, SEED))
    md.append('## Checks\n')
    for e in ENVS:
        for y in YEARS:
            f = os.path.join(R, 's90-sale-%s-%d-%s' % (e, y, eng))
            b2, rows = check2(f, eng)
            pd = shards(os.path.join(R, 'r2-m-%s-%d-%s' % (e, y, pubE)))
            b1, n1 = check1(rows, join(pd), e) if rows and pd else (['cannot compare (folder missing)'], 0)
            S['checks']['%s-%d' % (e, y)] = {'check1': b1, 'check1Values': n1, 'check2': b2}
            md.append('- %s, %d years: check 1 %s (%s values); check 2 %s' % (ENVL[e], y, 'passes' if not b1 else 'FAILS: ' + '; '.join(b1[:4]), '{:,}'.format(n1), 'passes' if not b2 else 'FAILS: ' + '; '.join(b2[:4])))
            if b1 or b2: fail = True
            if rows: data[(e, y)] = {r.split('.', 1)[1]: derive(v, y) for r, v in rows.items()}
    acct = opt('acct', '')
    if acct:
        A = json.load(open(acct)); S['checks']['check3'] = A.get('pass')
        md.append('- Check 3 (accounting identities on the at-sale rows, seeds %d-%d, %d years): %s' % (A['seeds'][0], A['seeds'][1], A['years'], 'passes' if A.get('pass') else 'FAILS'))
        if not A.get('pass'): fail = True
    md.append('')
    if fail:
        open(os.path.join(OUT, 's90-tables.md'), 'w').write('\n'.join(md) + '\nA check failed: no outcome is read (decision rule 1).\n')
        json.dump(S, open(os.path.join(OUT, 's90-summary.json'), 'w'), indent=1)
        print('\n'.join(md)); sys.exit('a check failed: stopped before any outcome (decision rule 1)')
    # ---- question 1
    sw = opt('swing', '')
    if sw:
        W = json.load(open(sw)); S['q1'] = {k: {'lagged': v['lagged']['swing'], 'sale': v['sale']['swing'], 'ratio': v['ratio'], 'lagPooled': v['lagged']['swingPooled'], 'salePooled': v['sale']['swingPooled']} for k, v in W['cells'].items()}
        S['q1']['rule2'] = W['rule2']
        md.append('## Question 1: the swing (mean year-to-year change in BU spent, years %d-%d, seeds %d-%d, full-coverage row, 20 years)\n' % (W['years'][0], W['years'][1], W['seeds'][0], W['seeds'][1]))
        md.append('| Environment | Lagged | At the sale | Ratio | Pooled series: lagged | at the sale |'); md.append('|---|---|---|---|---|---|')
        for k, lab in (('ref', 'Reference'), ('adv', 'Adverse'), ('st', 'Stress')):
            c = W['cells'][k]; md.append('| %s | %.2f%% | %.2f%% | %.3f | %.2f%% | %.2f%% |' % (lab, 100*c['lagged']['swing'], 100*c['sale']['swing'], c['ratio'], 100*c['lagged']['swingPooled'], 100*c['sale']['swingPooled']))
        md.append('\nDecision rule 2 (at the sale below half of lagged in every environment): **%s**.\n' % ('holds' if W['rule2'] else 'does not hold'))
    # ---- question 2
    md.append('## Question 2: effects against no programme, and the change at the sale\n')
    for d in DES:
        for e in ENVS:
            for y in YEARS:
                rows = data[(e, y)]; base = rows['none']
                md.append('### %s, %s, %d years\n' % (DESL[d], ENVL[e], y))
                md.append('| Outcome | Effect, lagged | Effect, at the sale | Change (at the sale − lagged) | p (Holm) | Sign or rounding changes |'); md.append('|---|---|---|---|---|---|')
                cell, ps = [], []
                for k in PRIM + SEC:
                    if k not in base or k not in rows[d] or k not in rows[d + '.sale']: md.append('| %s | not stored | | | | |' % LAB[k]); continue
                    sc = SCALE.get(k, 1.0)
                    eL, eS, ch = est((rows[d][k] - base[k])*sc, BS), est((rows[d + '.sale'][k] - base[k])*sc, BS), est((rows[d + '.sale'][k] - rows[d][k])*sc, BS)
                    q3 = None
                    if k in PRIM:
                        ps.append(ch['p'])
                        q3 = 'sign' if (eL['est'] > 0) != (eS['est'] > 0) else 'rounding' if rnd(eL['est'], k) != rnd(eS['est'], k) else 'no'
                    cell.append({'key': k, 'primary': k in PRIM, 'lagged': eL, 'sale': eS, 'change': ch, 'q3': q3})
                H = holm(ps); j = 0
                for c in cell:
                    if c['primary']: c['change']['pHolm'] = H[j]; j += 1
                    ph = '%.2g' % c['change']['pHolm'] if c['primary'] else '%.2g (unadjusted)' % c['change']['p']
                    md.append('| %s%s | %s | %s | %s | %s | %s |' % (LAB[c['key']], '' if c['primary'] else ' (secondary)', ci(c['lagged'], c['key']), ci(c['sale'], c['key']), ci(c['change'], c['key']), ph, c['q3'] or '–'))
                md.append('')
                S['cells'].append({'design': d, 'env': e, 'years': y, 'outcomes': cell})
    open(os.path.join(OUT, 's90-tables.md'), 'w').write('\n'.join(md) + '\n')
    json.dump(S, open(os.path.join(OUT, 's90-summary.json'), 'w'), indent=1)
    print('wrote %s/s90-tables.md and s90-summary.json' % OUT)


if __name__ == '__main__':
    main()
