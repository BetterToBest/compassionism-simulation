#!/usr/bin/env python3
"""S94 part 4 (Nov 21, 2026): the checks and tables of the Creative Collectives' lending study (a fund for community businesses' premises,
equipment and set-up costs) and of charters of public utilities, as research-update prereg/2026-11-s94-collectives-lending.md fixes them
(Questions, Outcomes, Analysis, Checks, Decision rules; Amendments 1 and 2). Reads the six folders s94-<env>-<years>-<engine> of
compassionism-sim-results (runner/jobs/s94.js; 20 shards of 25 seeds, seeds 1-500, 31 rows each) and the published main rows with the private
price at the sale (s90-sale-<env>-<years>-b8ccd8d; the extra check that the study's main row is the published one). Writes Markdown tables and a
summary JSON.

  python3 dev/tools/s94_tables.py RESULTS_DIR OUT_DIR [--engine c5682f9] [--reps 10000] [--main ENGINE7]

Method (fixed by the preregistration; where it is silent, the cautious reading, said so here and in the tables):
- The contrast (blocks A-C): row minus the main row M of the same design, paired by seed. The no-programme run is shared, so this is also the change
  in the programme's effect. Each row's programme effect (row minus the no-programme run) is published beside it.
- Primary readings (six): basket poverty fgt0PY; wealth poverty yearly (ppovA, the job's mean of ppov_1 .. ppov_{T-1}) and at the last year (pov);
  median real wealth weighted (wtMedE) and unweighted (medWealthReal); savings secM3A (adult-years whose liquid savings cover under three months of
  need). All in points, wealth in year-0 dollars.
- p: two-sided paired t (499 degrees of freedom). Holm across the six readings within each row, environment, horizon and design. Intervals: paired
  bootstrap, 10,000 replicates, seeds resampled, percentile, unadjusted; generator numpy default_rng(20261121), one resample for every table.
- Decision rule 2: improves / worsens where the Holm-adjusted p is below 0.05, by the favourable direction of the reading; otherwise no change
  (and no change where the row equals M in every seed).
- Decision rule 3 (the fund's verdict, row A main): helps where basket poverty or yearly wealth poverty improves and none of the six worsens, in
  that environment, design and horizon.
- Decision rule 4 (Amendment 1 item 8): "the same direction" in the pace x 0.5 row and the all-grants row. Cautious reading used: each reading
  that improves in A main also improves (Holm) in both rows, and neither row worsens any of the six. The weaker sign-only reading (the point
  estimate has the same sign) is printed beside it.
- Decision rule 6 is read at the primary horizon (20 years); the 40-year cells are printed beside it.
- Q2: cost per point of basket poverty = (row - M) in programme cost per adult a year (`cost`, year-0 $) over the fall in basket poverty (points),
  ratio of means, with the bootstrap interval of the ratio; only where the basket-poverty change's interval excludes zero (and it falls).
- Q5: interaction = (C - M) - (A main - M) - (B 1/7 - M), per seed, with its interval; claimed only where the interval excludes zero.
Standard library and numpy."""
import glob, gzip, hashlib, json, math, os, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s64_tables import tcdf, holm  # noqa: E402  (the same t distribution and Holm as the earlier studies)

ENVS = ['ref', 'adv', 'str']; ENVL = {'ref': 'Reference', 'adv': 'Adverse', 'str': 'Stress'}; YEARS = [20, 40]
DES = ['c22', 'rel']; DESL = {'c22': 'full coverage', 'rel': 'opt-in'}
PRIM = [('fgt0PY', 'basket poverty', -1), ('ppovA', 'wealth poverty, yearly average', -1), ('pov', 'wealth poverty, last year', -1),
        ('wtMedE', 'median real wealth, weighted', 1), ('medWealthReal', 'median real wealth, unweighted', 1),
        ('secM3A', 'savings under three months of need', -1)]
PK = [k for k, _, _ in PRIM]
LAB = {k: l for k, l, _ in PRIM}; FAV = {k: s for k, _, s in PRIM}
SECD = ['cost', 'tax', 'tauMean', 'payPart', 'clOut', 'clGrant', 'clInt', 'clOff', 'clNet', 'clFail', 'clBind', 'chSub', 'poSub', 'paCap', 'endoAnn', 'pLev20', 'bNAPy', 'fgt2PY']
for t in (5, 10, 19, 39): SECD += ['clCap%d' % t, 'paS%d' % t, 'paC%d' % t]
LAB.update({'cost': 'programme cost per adult a year ($)', 'tax': 'the contribution that finances the programme, per adult a year ($)',
            'tauMean': 'its rate, mean over the years (points of pay)', 'payPart': 'the payout per participant a year ($)', 'clOut': "the fund's outlay per adult a year ($)", 'clGrant': 'of which grants ($)',
            'clInt': 'interest received ($)', 'clOff': 'loans written off ($, information)', 'clNet': "the fund's net outlay (outlay less interest, $)",
            'clFail': 'funded capacity lost to failures, cumulative (points)', 'clBind': 'adult-years where the pace limit bound (%)',
            'chSub': 'added subsidy from charters ($)', 'poSub': "community businesses' running-cost subsidy ($)",
            'paCap': 'adult-years where capital limited the community-business share (%)', 'endoAnn': 'programme inflation (points a year)',
            'pLev20': 'price level at the last year', 'bNAPy': 'below 30 days of basic living', 'fgt2PY': 'poverty severity',
            'ppov20': 'wealth poverty at year 20 (40-year runs)', 'W1': 'mean real wealth, poorest fifth at the start ($)',
            'W2': 'mean real wealth, second fifth ($)', 'W3': 'mean real wealth, middle fifth ($)', 'W4': 'mean real wealth, fourth fifth ($)',
            'W5': 'mean real wealth, richest fifth ($)'})
for t in (5, 10, 19, 39):
    LAB['clCap%d' % t] = 'funded capacity share, year %d (%%)' % (t + 1 if t in (19, 39) else t)
    LAB['paS%d' % t] = 'community-business share of essential sales, year %d (%%)' % (t + 1 if t in (19, 39) else t)
    LAB['paC%d' % t] = 'community-business capacity, year %d (%%)' % (t + 1 if t in (19, 39) else t)
FAV.update({'bNAPy': -1, 'fgt2PY': -1, 'endoAnn': -1, 'ppov20': -1, 'W1': 1, 'W2': 1, 'W3': 1, 'W4': 1, 'W5': 1})
SCALE = {'endoAnn': 100.0, 'tauMean': 100.0}
DIG = {'tax': 0, 'payPart': 0, 'wtMedE': 0, 'medWealthReal': 0, 'W1': 0, 'W2': 0, 'W3': 0, 'W4': 0, 'W5': 0, 'cost': 0, 'pLev20': 4}
ROWL = {'A.main': "the fund, main reading", 'A.pace0.5': 'the fund, pace x 0.5', 'A.pace2': 'the fund, pace x 2', 'A.nolimit': 'the fund, no pace limit',
        'A.lent': "the fund, pace limits the fund's additions only", 'A.mature': 'the fund, mature-firm failures', 'A.haznone': 'the fund, no failures',
        'A.grant0': 'the fund, all loans', 'A.grant1': 'the fund, all grants', 'B.ch1of7': 'charters 1/7, no fund', 'B.ch1of3': 'charters 1/3, no fund',
        'B.ch2of3': 'charters 2/3, no fund', 'C.main.ch1of7': 'the fund and charters 1/7', 'D.zero': 'check row (switch on at zero)'}
CONTRAST = [r for r in ROWL if not r.startswith('D.')]
REPS = 10000; NS = 500; W = None


def shards(folder):
    fs = sorted(f for f in glob.glob(os.path.join(folder, 'shard-*.json*')) if '.timing.' not in f)
    if not fs: sys.exit('no shard files in ' + folder)
    return fs


def jload(f): return json.load(gzip.open(f) if f.endswith('.gz') else open(f))


def sha_ok(folder):
    bad, n = [], 0
    for line in open(os.path.join(folder, 'SHA256SUMS')):
        h, f = line.split(None, 1); f = f.strip().lstrip('*'); n += 1
        if f == 'SHA256SUMS': bad.append('lists itself'); continue
        with open(os.path.join(folder, f), 'rb') as fh:
            if hashlib.sha256(fh.read()).hexdigest() != h: bad.append(f)
    return n, bad


def keep(k, T):
    return k in PK or k in SECD or k in ('ppov20', 'clChk') or (k[:3] in ('rtE', 'rtV', 'rtS') and k[3:].isdigit())


def s90_rows(folder):
    """the published main rows with the private price at the sale: row -> key -> list over seeds 1-500"""
    D = sorted((jload(f) for f in shards(folder)), key=lambda d: d['_meta']['seeds'][0]); out = {}
    for full in D[0]['rows']:
        out[full.split('.', 1)[1]] = {k: [x for d in D for x in d['rows'][full][k]] for k in D[0]['rows'][full]}
    return out


MAIN = None  # S93 part 3 (Nov 23, 2026): --main ENGINE7 compares the main rows with the rerun part M r2-m-<env>-<years>-ENGINE7 (the release main row)


def main_rows(src, e, y):
    """the main rows the study's own must equal: the at-sale folder (default) or, with --main, the rerun part M (rows renamed as the at-sale ones)"""
    if not MAIN: return s90_rows(os.path.join(src, 's90-sale-%s-%d-b8ccd8d' % (e, y)))
    r = s90_rows(os.path.join(src, 'r2-m-%s-%d-%s' % (e, y, MAIN)))
    return {'none': r['none'], 'c22.sale': r['c22'], 'rel.sale': r['rel']}


def main_label(e, y):
    return 'the published main row with the private price at the sale (s90-sale-%s-%d-b8ccd8d)' % (e, y) if not MAIN else 'the release main row (r2-m-%s-%d-%s)' % (e, y, MAIN)


def load(src, e, y, eng):
    fo = os.path.join(src, 's94-%s-%d-%s' % (e, y, eng)); C = []
    C.append(('DONE and run.txt present', os.path.exists(os.path.join(fo, 'DONE')) and os.path.exists(os.path.join(fo, 'run.txt')), None))
    n, bad = sha_ok(fo); C.append(('check 9: SHA256SUMS, %d files, all match (the file does not list itself)' % n, not bad, bad))
    s90 = main_rows(src, e, y)
    fsx = shards(fo); R = {}; seeds = []; man = []; nullk = set(); nullkept = []; d2 = {}; c1 = {}; spec = None; nkeys = 0
    for f in fsx:
        d = jload(f); m = d['_meta']; seeds.append(tuple(m['seeds'])); man.append((m['manifest'], m['baseline'])); lo, hi = m['seeds']
        spec = spec or {r['name']: r for r in m['rowSpec']}
        rows = {full.split('.', 1)[1]: v for full, v in d['rows'].items()}; nkeys = max(len(v) for v in rows.values())
        for nm, v in rows.items():
            dst = R.setdefault(nm, {})
            for k, a in v.items():
                if a is None or any(x is None for x in a):
                    nullk.add(k)
                    if keep(k, y): nullkept.append((nm, k))
                if keep(k, y): dst.setdefault(k, []).extend(a)
        for des in DES:  # check 2: row D equals M in every key the two share; D carries the switch's own keys at zero
            a_, b_ = 'D.%s.zero' % des, 'M.%s.main' % des; dk = d2.setdefault(des, {'diff': set(), 'only': set(), 'shared': 0})
            dk['shared'] = len(set(rows[a_]) & set(rows[b_])); dk['only'] |= set(rows[a_]) ^ set(rows[b_])
            dk['diff'] |= {k for k in set(rows[a_]) & set(rows[b_]) if rows[a_][k] != rows[b_][k]}
        for a_, b_ in (('M.c22.main', 'c22.sale'), ('M.rel.main', 'rel.sale'), ('none', 'none')):  # the main row is the published one
            ks = c1.setdefault(a_, {'diff': set(), 'n': 0}); ks['n'] = len(s90[b_])
            for k in s90[b_]:
                if k not in rows[a_] or rows[a_][k] != s90[b_][k][lo - 1:hi]: ks['diff'].add(k)
        del d, rows
    s = 1; cover = True
    for a, b in sorted(seeds):
        if a != s: cover = False
        s = b + 1
    cover = cover and s == NS + 1
    engs = {mm['commit'] for mm, _ in man}; clean = all(not mm.get('dirty') for mm, _ in man); base = all(bl.get('checked') for _, bl in man)
    C.append(('check 9: %d shards cover seeds 1-500 once; engine %s and a clean checkout in every shard' % (len(seeds), '/'.join(sorted(x[:7] for x in engs))),
              cover and len(engs) == 1 and clean and next(iter(engs)).startswith(eng), None))
    C.append(("check 9: the release start's baseline check passed in every shard", base, None))
    C.append(('every value this analysis reads is finite (%d rows; %d keys per row stored)' % (len(R), nkeys), not nullkept, nullkept[:10]))
    C.append(('(inspection) keys with a missing value somewhere among the %d stored: %s' % (nkeys, ', '.join(sorted(nullk))[:300] or 'none'), None, None))
    for des, dk in d2.items():
        C.append(('check 2: row D equals M in all %d shared keys, every seed (%s); keys only in D: the switch\'s own reporting keys (%d)'
                  % (dk['shared'], DESL[des], len(dk['only'])), not dk['diff'], sorted(dk['diff'])[:10]))
    for a_, ks in c1.items():
        C.append(('%s equals %s in all %d of its keys, every seed'
                  % ('the no-programme run' if a_ == 'none' else 'M (%s)' % DESL[a_.split('.')[1]], main_label(e, y), ks['n']), not ks['diff'], sorted(ks['diff'])[:10]))
    for nm in R:
        R[nm] = {k: np.array([np.nan if x is None else x for x in a], dtype=float) for k, a in R[nm].items()}
        if 'rtE1' in R[nm]:
            for q in range(1, 6): R[nm]['W%d' % q] = R[nm]['rtE%d' % q] + R[nm]['rtV%d' % q] + R[nm]['rtS%d' % q]
    fund = [nm for nm in R if nm.startswith(('A.', 'C.'))]
    mx = max(float(np.nanmax(R[nm]['clChk'])) for nm in fund)
    C.append(("check 4: the fund's accounts close (outlays = (outstanding + lost funded capacity) x K) within 1e-9 relative in every fund row and seed "
              "(largest miss %.1e)" % mx, mx <= 1e-9, None))
    nz = [nm for nm in R if nm.startswith('B.') and (np.any(R[nm]['clOut'] != 0) or np.any(R[nm]['clCap5'] != 0))]
    C.append(('charter rows without the fund lend nothing (outlay and funded capacity 0 in every seed)', not nz, nz))
    zc = [nm for nm in R if nm.startswith('A.') and np.any(R[nm]['chSub'] != 0)]
    C.append(('fund rows without charters pay no charter subsidy', not zc, zc))
    if e == 'str':
        a = R['A.rel.main']; ok = a['clOut'][0] > 0 and a['clBind'][0] > 0
        C.append(('check 3b (non-vacuity): Stress, opt-in, seed 1: the fund lends (outlay %.1f) and the pace limit binds in %.1f%% of adult-years'
                  % (a['clOut'][0], a['clBind'][0]), ok, None))
    return R, spec, C


# ---------------------------------------------------------------- statistics
def est(d):
    n = len(d); m = float(d.mean()); v = W @ d; sd = float(d.std(ddof=1))
    p = 1.0 if sd == 0 and m == 0 else 0.0 if sd == 0 else 2 * (1 - tcdf(abs(m) / (sd / math.sqrt(n)), n - 1))
    lo, hi = np.percentile(v, [2.5, 97.5])
    return {'est': m, 'lo': float(lo), 'hi': float(hi), 'p': p, 'zero': bool(np.all(d == 0))}


def lev(d):
    v = W @ d; lo, hi = np.percentile(v, [2.5, 97.5]); return {'est': float(d.mean()), 'lo': float(lo), 'hi': float(hi)}


def excl(s): return s['lo'] > 0 or s['hi'] < 0


def cat(s, k):
    if s['zero'] or s['holm'] >= 0.05: return 'no change'
    return 'improves' if s['est'] * FAV[k] > 0 else 'worsens'


def analyse(R, y):
    out = {}
    sec = [k for k in SECD + ['ppov20', 'W1', 'W2', 'W3', 'W4', 'W5'] if k in R['M.c22.main'] or k in R['A.c22.main']]
    for des in DES:
        M = R['M.%s.main' % des]; N = R['none']; o = {'levels': {}, 'contrast': {}, 'effect': {}, 'q2': {}, 'q5': {}, 'rules': {}}
        for r in ['M.main'] + CONTRAST:
            b, rd = r.split('.', 1); X = R['%s.%s.%s' % (b, des, rd)]
            o['levels'][r] = {k: lev(X[k]) for k in PK + sec if k in X}
            o['effect'][r] = {k: est(X[k] - N[k]) for k in PK}
            if r == 'M.main': continue
            c = {k: est(X[k] - M[k]) for k in PK + sec if k in X and k in M}
            ad = holm([c[k]['p'] for k in PK])
            for i, k in enumerate(PK): c[k]['holm'] = ad[i]; c[k]['cat'] = cat(c[k], k)
            for k in c:
                if k in FAV and k not in PK: c[k]['dir'] = None if not excl(c[k]) else ('better' if c[k]['est'] * FAV[k] > 0 else 'worse')
            o['contrast'][r] = c
            dp = X['fgt0PY'] - M['fgt0PY']; s0 = c['fgt0PY']
            if excl(s0) and s0['est'] < 0:
                dc = X['cost'] - M['cost']; num, den = W @ dc, W @ (-dp); lo, hi = np.percentile(num / den, [2.5, 97.5])
                o['q2'][r] = {'est': float(dc.mean() / (-dp.mean())), 'lo': float(lo), 'hi': float(hi)}
        A, B, Cc = (R['%s.%s.%s' % (b, des, rd)] for b, rd in (('A', 'main'), ('B', 'ch1of7'), ('C', 'main.ch1of7')))
        o['q5'] = {k: est((Cc[k] - M[k]) - (A[k] - M[k]) - (B[k] - M[k])) for k in PK + ['cost']}
        # decision rules 3 and 4
        cm = o['contrast']['A.main']; imp = [k for k in PK if cm[k]['cat'] == 'improves']; wor = [k for k in PK if cm[k]['cat'] == 'worsens']
        helps = bool(set(imp) & {'fgt0PY', 'ppovA'}) and not wor
        rob = {}
        for rr in ('A.pace0.5', 'A.grant1'):
            cr = o['contrast'][rr]
            rob[rr] = {'strict': all(cr[k]['cat'] == 'improves' for k in imp) and not any(cr[k]['cat'] == 'worsens' for k in PK),
                       'sign': all(cr[k]['est'] * cm[k]['est'] > 0 for k in imp)}
        o['rules'] = {'improves': imp, 'worsens': wor, 'helps': helps, 'robust': rob,
                      'rule4': helps and all(v['strict'] for v in rob.values()), 'rule4sign': helps and all(v['sign'] for v in rob.values())}
        out[des] = o
    return out


# ---------------------------------------------------------------- writing
def fm(x, k=None, d=None):
    if x is None: return '–'
    x = x * SCALE.get(k, 1.0); d = DIG.get(k, 2) if d is None else d
    return ('{:,.%df}' % d).format(x) if abs(x) >= 1000 else ('%.' + str(d) + 'f') % x


def ci(s, k=None):
    if s is None: return '–'
    if s.get('zero'): return '0 (identical in every seed)'
    return '%s (%s to %s)' % (fm(s['est'], k), fm(s['lo'], k), fm(s['hi'], k))


def pf(p): return '<0.001' if p < 0.001 else '%.3f' % p


def write(out, ALL, CHK, eng):
    L = ['# Checks of the lending study (%s)' % eng, '', 'Every check must pass before any table is read (preregistration, Checks). '
         'Checks 1 and 5-8 rest on the engine\'s unit tests and the build\'s proofs (compassionism-simulation `clUnitSuite`, 8 of 8 on `%s`; '
         'the off-equals-identical proofs of the build); check 2b (the no-programme run unchanged with the switch set on it) was proved in the dry run.' % eng, '']
    allok = True
    for fk, C in CHK.items():
        L += ['## %s, %s years' % (ENVL[fk.split('-')[0]], fk.split('-')[1]), '']
        for t, ok, det in C:
            if ok is False: allok = False
            L.append('- %s %s%s' % ('PASS' if ok else ('FAIL' if ok is False else '·'), t, '' if ok or not det else ' — ' + str(det)))
        L.append('')
    L.insert(2, '**%s**' % ('All checks pass.' if allok else 'A CHECK FAILED: decision rule 1 applies; no table may be read.')); L.insert(3, '')
    open(os.path.join(out, 's94-checks.md'), 'w').write('\n'.join(L) + '\n')
    js = {}
    for y in YEARS:
        L = ['# The lending study: tables at %d years%s (%s)' % (y, ' (primary horizon)' if y == 20 else '', eng), '',
             'Each cell: the mean over seeds 1-500 of the row minus the main row of the same design, paired by seed, with its 95% paired-bootstrap '
             'interval (10,000 replicates; unadjusted). For the six primary readings the Holm-adjusted p (across the six, within the row, environment, '
             'horizon and design) and decision rule 2\'s category follow. Points for shares, year-0 dollars for wealth and costs. '
             'Lower is better for poverty, savings shortfall, severity and inflation; higher is better for wealth.', '']
        for e in ENVS:
            S = ALL['%s-%d' % (e, y)]
            for des in DES:
                o = S[des]; js['%s-%d-%s' % (e, y, des)] = o
                L += ['## %s, %s, %d years' % (ENVL[e], DESL[des], y), '', '### Levels of the main row and its programme effect', '',
                      '| reading | no-programme run | main row | main row\'s programme effect |', '|---|---|---|---|']
                for k in PK:
                    L.append('| %s | %s | %s | %s |' % (LAB[k], fm(S['_lev_none'][k]['est'], k), ci(o['levels']['M.main'][k], k), ci(o['effect']['M.main'][k], k)))
                L += ['', '### Primary readings: row minus the main row', '']
                for r in CONTRAST:
                    c = o['contrast'][r]
                    L += ['**%s**' % ROWL[r], '', '| reading | change | Holm p | category | the row\'s programme effect |', '|---|---|---|---|---|']
                    for k in PK: L.append('| %s | %s | %s | %s | %s |' % (LAB[k], ci(c[k], k), pf(c[k]['holm']), c[k]['cat'], ci(o['effect'][r][k], k)))
                    L.append('')
                L += ['### Secondary readings: row minus the main row (level in the row in brackets)', '']
                ks = [k for k in SECD + ['ppov20', 'W1', 'W2', 'W3', 'W4', 'W5'] if k in o['contrast']['A.main']]
                L += ['| reading | ' + ' | '.join(ROWL[r] for r in CONTRAST) + ' |', '|---' * (len(CONTRAST) + 1) + '|']
                for k in ks:
                    L.append('| %s | ' % LAB[k] + ' | '.join('%s [%s]' % (ci(o['contrast'][r].get(k), k), fm(o['levels'][r][k]['est'], k)) if k in o['contrast'][r] else '–'
                                                         for r in CONTRAST) + ' |')
                L += ['', '### Cost per point of basket poverty (question 2)', '']
                if o['q2']:
                    for r, q in o['q2'].items(): L.append('- %s: $%s per adult a year for each point of basket poverty (%s to %s)' % (ROWL[r], fm(q['est'], 'cost'), fm(q['lo'], 'cost'), fm(q['hi'], 'cost')))
                else: L.append('- No row lowers basket poverty with an interval that excludes zero, so no cost per point is reported.')
                L += ['', '### The fund and charters together: the interaction (question 5)', '',
                      '(together - main) - (fund - main) - (charters 1/7 - main), per seed:', '', '| reading | interaction | interval excludes zero |', '|---|---|---|']
                for k, s in o['q5'].items(): L.append('| %s | %s | %s |' % (LAB[k], ci(s, k), 'yes' if not s['zero'] and excl(s) else 'no'))
                ru = o['rules']
                L += ['', '### Decision rules 3 and 4 (the fund\'s main reading)', '',
                      '- improves: %s; worsens: %s.' % (', '.join(LAB[k] for k in ru['improves']) or 'none', ', '.join(LAB[k] for k in ru['worsens']) or 'none'),
                      '- Rule 3, "the fund helps": **%s**.' % ('yes' if ru['helps'] else 'no')]
                for rr, v in ru['robust'].items():
                    L.append('- Rule 4, %s: the same readings improve and none worsens: %s; same sign only: %s.' % (ROWL[rr], 'yes' if v['strict'] else 'no', 'yes' if v['sign'] else 'no'))
                L += ['- Rule 4 holds (the cautious reading): **%s**.' % ('yes' if ru['rule4'] else 'no'), '']
        open(os.path.join(out, 's94-tables-%d.md' % y), 'w').write('\n'.join(L) + '\n')
    # decision rule 6
    L = ['# Decision rule 6: the fund and the main row (%s)' % eng, '', 'Read at the primary horizon (20 years); 40 years beside it.', '',
         '| environment | design | 20 years: helps | 20 years: rule 4 | 40 years: helps | 40 years: rule 4 |', '|---|---|---|---|---|---|']
    hold = False
    for e in ENVS:
        for des in DES:
            r20, r40 = ALL['%s-20' % e][des]['rules'], ALL['%s-40' % e][des]['rules']; hold = hold or r20['rule4']
            L.append('| %s | %s | %s | %s | %s | %s |' % (ENVL[e], DESL[des], 'yes' if r20['helps'] else 'no', 'yes' if r20['rule4'] else 'no',
                                                     'yes' if r40['helps'] else 'no', 'yes' if r40['rule4'] else 'no'))
    L += ['', '**Rule 6: %s**' % ('rules 3 and 4 hold in at least one environment and design at 20 years: the fund at its main reading is proposed for the '
                                  "release's main row (Duke's decision)." if hold else 'rule 3 with rule 4 holds nowhere at 20 years: the fund is reported as a reading '
                                  'beside the main row, and the main row is unchanged.'), '']
    open(os.path.join(out, 's94-rule6.md'), 'w').write('\n'.join(L) + '\n')
    json.dump({'checks': {k: [[t, None if ok is None else bool(ok)] for t, ok, _ in c] for k, c in CHK.items()}, 'rule6': hold, 'results': js}, open(os.path.join(out, 's94-summary.json'), 'w'))
    return allok, hold


def main():
    global W, REPS, MAIN
    src, out = sys.argv[1], sys.argv[2]
    eng = sys.argv[sys.argv.index('--engine') + 1] if '--engine' in sys.argv else 'c5682f9'
    if '--reps' in sys.argv: REPS = int(sys.argv[sys.argv.index('--reps') + 1])
    if '--main' in sys.argv: MAIN = sys.argv[sys.argv.index('--main') + 1]
    os.makedirs(out, exist_ok=True)
    rng = np.random.default_rng(20261121); idx = rng.integers(0, NS, size=(REPS, NS))
    W = np.zeros((REPS, NS))
    for b in range(REPS): W[b] = np.bincount(idx[b], minlength=NS) / NS
    ALL, CHK = {}, {}
    for e in ENVS:
        for y in YEARS:
            R, spec, C = load(src, e, y, eng); CHK['%s-%d' % (e, y)] = C
            S = analyse(R, y); S['_lev_none'] = {k: lev(R['none'][k]) for k in PK}; ALL['%s-%d' % (e, y)] = S
            print('done %s %d' % (e, y), file=sys.stderr); del R
    ok, hold = write(out, ALL, CHK, eng)
    print('checks %s; rule 6 %s' % ('pass' if ok else 'FAIL', 'holds' if hold else 'does not hold'), file=sys.stderr)


if __name__ == '__main__':
    main()
