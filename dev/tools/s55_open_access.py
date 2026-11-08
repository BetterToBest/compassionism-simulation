#!/usr/bin/env python3
"""S55 part 4: the open-PTF-access report's tables (dev/reports/s55-open-access.md), from the nine 500-seed studies.

Usage: python3 dev/tools/s55_open_access.py <compassionism-sim-results checkout> <out dir>
Reads prog-{t,u,u10,v,v10,vj,w,w10,y}-0c93593 (rows under open access, engine 0c93593) and the frozen batch's rows they pair with,
prog-{a,b,b10,g,g10,h,i,j}-ce8d030 (members only; with PTF_ACCESS off the engine 0c93593 is the frozen engine ce8d030 figure for
figure: guard test and engine lineage, S55 parts 1 and 2), plus the pilots pilot55-{t,u,v,w,y}-0c93593 (seeds 1-50) as a check.
Writes <out dir>/tables.md (every table) and <out dir>/estimates.csv (every estimate with its interval and flags).

Method: research-update prereg/2026-11-ptf-access-addendum.md (Q24-Q28, Analysis, decision rules 1-6), which keeps the study
programme's Analysis and the community-layer addendum's unchanged.
- Q24 open access: per seed, the release row under open access (T) minus the same row with members only (A), and each row's
  effect against no programme (A's none row); 500 and 10,000 adults, 20 and 40 years, both designs, three environments.
- Q25 synergy under open access: the programme's Shapley values and 11 contrasts on the factorial whose 16 cells with PTF come
  from U (or U10) and whose 15 cells without PTF and none row come from B (or B10); and each minus its members-only value (B, B10).
- Q26 the layer under open access: the layer addendum's Q7 (layer effect: V, V10, VJ against T), Q8 (the layer factorial, PTF
  cells from V or V10), Q9 (study H's rows, from V) and Q10 (study I's rows, from V), each minus the members-only answer (G, G10,
  H, I, J against A and B).
- Q27 response curve: the release row with every zone's share held at 10%, ..., 100% (W, W10) against no programme and against
  the members-only row (A), and the two threshold steps.
- Q28 growth: the access diagnostics of T's rows (which limit binds; the share and capacity by year), and the open-access effect
  under each swept setting of the growth rule (Y), with whether any rule-1 decision differs from the main-value row (T).
- 95% intervals: paired bootstrap over seeds, 10,000 replicates, percentile, bootstrap seed 20261101; one resample of seed indices
  per population size (500, then 2,000, then 10,000 adults, from one generator, as S38 drew them), shared by every study at that
  size, so every comparison at one size is paired on the same resample. Between sizes the runs are independent.
"""
import csv, math, os, sys
from itertools import combinations
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import batch_load  # noqa: E402

SRC, OUT = sys.argv[1], sys.argv[2]
ENG, ENGF = '0c93593', 'ce8d030'
ENG40 = '0c93593e1ea502555387e42215b79f290a60f127'
PARTS = 'CFHZI'
PNAME = {'C': 'CCO', 'F': 'PTF', 'H': 'PTH', 'Z': 'SZH', 'I': 'CIP'}
ENVS = [('ref', 'Reference'), ('adv', 'Adverse'), ('st', 'Stress')]
DESIGNS = [('c22', 'C2.2 design'), ('rls', 'release design')]
NB, BSEED, NS = 10000, 20261101, 500
DEM = 49.0   # the demand ceiling's main value, in % (design parameter)

O20 = [('Basic living (BLEI<30, neutral)', 'bNAPy', 'red', 0), ('BLEI<30 own (not claimed)', 'bOAPy', 'red', 0),
       ('Cost of living', 'fgt0PY', 'red', 0), ('Wealth<25k y20', 'ppov_19', 'red', 0), ('Cost $', 'cost', 'diff', 0),
       ('Inflation to y20, cumulative %', 'plv_19', 'infl', 0), ('Inflation, yearly rate', 'plv_19', 'iyr', 20)]
O40 = [('Basic living (BLEI<30, neutral)', 'bNAPy', 'red', 0), ('BLEI<30 own (not claimed)', 'bOAPy', 'red', 0),
       ('Cost of living', 'fgt0PY', 'red', 0), ('Wealth<25k y40', 'ppov_39', 'red', 0), ('Cost $', 'cost', 'diff', 0),
       ('Inflation to y40, cumulative %', 'plv_39', 'infl', 0), ('Inflation, yearly rate', 'plv_39', 'iyr', 40)]
OUTS = {20: O20, 40: O40}
SEC = [('Gini disposable income x100', 'giniD', 100), ('Gini wealth x100', 'eGiniW', 100), ('children below cost of living', 'hhCostKidPY', 1),
       ('hours vs full time, %', 'hrs', 100), ('below official poverty line', 'hhFplPY', 1), ('FGT2 x100', 'fgt2PY', 100)]
PAK = ['paSh', 'paLo', 'paTh', 'paCap', 'paOps', 'paDem', 'paCv', 'paS5', 'paS10', 'paS19', 'paS39', 'paC5', 'paC10', 'paC19', 'paC39', 'pfMem', 'pfCut']
C22_ONLY = ('c22PY', 'c22R', 'buPY', 'elN', 'elF0', 'elW', 'elRes')


def oid(o):
    return o[1] + ('.yr' if o[2] == 'iyr' else '')


def claimable(o):
    return o[1] != 'bOAPy' and o[2] != 'infl'


# ---------------------------------------------------------------- load
def load(folder, seeds):
    rows, meta = batch_load.load(os.path.join(SRC, folder))
    assert not meta['_problems'], (folder, meta['_problems'])
    assert meta['seedList'] == list(seeds), folder
    return rows, meta


NEW = ('t', 'u', 'u10', 'v', 'v10', 'vj', 'w', 'w10', 'y')
FRZ = ('a', 'b', 'b10', 'g', 'g10', 'h', 'i', 'j')
D, META = {}, {}
for s in NEW:
    D[s], META[s] = load('prog-%s-%s' % (s, ENG), range(1, NS + 1))
for s in FRZ:
    D[s], META[s] = load('prog-%s-%s' % (s, ENGF), range(1, NS + 1))
PIL = {s: load('pilot55-%s-%s' % (s, ENG), range(1, 51))[0] for s in ('t', 'u', 'v', 'w', 'y')}
CHECKS = []


def chk(ok, text):
    CHECKS.append(('PASS' if ok else 'FAIL') + '  ' + text)
    if not ok:
        print('FAIL', text, file=sys.stderr)


def R(study, e, n, y, d, row):
    return D[study]['%s.n%d.y%d.%s.cps.%s' % (e, n, y, d, row)]


def same(a, b, skip=()):
    return all(np.array_equal(x, b[k], equal_nan=True) for k, x in a.items() if k not in skip and k in b) and set(a) == set(b)


# ---------------------------------------------------------------- checks before any table
cnt = {s: len(D[s]) // 3 for s in NEW}
want = {'t': 8, 'u': 64, 'u10': 32, 'v': 124, 'v10': 32, 'vj': 8, 'w': 40, 'w10': 20, 'y': 24}
chk(cnt == want, 'rows per environment as the addendum\'s Studies table (both designs; x2 horizons for T, U, V, VJ, W, Y; x2 sizes for T, VJ): '
    + ', '.join('%s %d' % (s.upper(), cnt[s]) for s in NEW))
bad = [s for s in NEW if META[s]['manifest']['commit'] != ENG40 or META[s]['manifest']['dirty']]
chk(not bad, 'every shard of the nine studies records engine %s, clean checkout: %s' % (ENG40, 'all' if not bad else 'not ' + ', '.join(bad)))
# the pilots (seeds 1-50, same engine) are the first 50 seeds of the full runs, every key
bad = n = 0
for s, P in PIL.items():
    for r, v in P.items():
        if s == 't' and r.endswith('cps.main'):
            full = D['a'][r]       # T's pilot ran the members-only rows too: they are study A's rows
        else:
            full = D[s][r]
        n += 1
        bad += not all(np.array_equal(x, full[k][:50], equal_nan=True) for k, x in v.items() if k in full)
chk(n > 0 and bad == 0, 'the pilot rows (seeds 1-50: T with its members-only rows, U, V, W, Y; %d rows) equal seeds 1-50 of the full runs and of study A, every key: %d differ' % (n, bad))
# the same row in two studies is identical
pairs = [(('u', e, 500, y, d, 'main.open'), ('t', e, 500, y, d, 'main.open')) for e, _ in ENVS for d, _ in DESIGNS for y in (20, 40)]
pairs += [(('u10', e, 10000, 20, d, 'main.open'), ('t', e, 10000, 20, d, 'main.open')) for e, _ in ENVS for d, _ in DESIGNS]
pairs += [(('v10', e, 10000, 20, d, 'main.lay.open'), ('vj', e, 10000, 20, d, 'main.lay.open')) for e, _ in ENVS for d, _ in DESIGNS]
bad = sum(not same(R(*a), R(*b)) for a, b in pairs)
chk(bad == 0, 'the same row in two studies is identical, every key and seed (U and T at 500 adults; U10 and T, V10 and VJ at 10,000 adults; %d rows): %d differ' % (len(pairs), bad))
bad = sum(not same(R('b', e, 500, y, d, r), R('a', e, 500, y, d, r)) for e, _ in ENVS for d, _ in DESIGNS for y in (20, 40) for r in ('main', 'none'))
bad += sum(not same(R('b10', e, 10000, 20, d, r), R('a', e, 10000, 20, d, r)) for e, _ in ENVS for d, _ in DESIGNS for r in ('main', 'none'))
chk(bad == 0, 'the frozen rows the comparisons use agree: B\'s and B10\'s release and none rows equal study A\'s (36 rows): %d differ' % bad)
# 40-year rows' year-20 measures equal the 20-year rows'
bad = n = 0
for s in ('t', 'u', 'v', 'vj', 'w', 'y'):
    for r in D[s]:
        if '.y40.' not in r:
            continue
        for k in ('ppov_19', 'plv_19', 'pbO_19', 'pf0_19', 'paS5', 'paS10', 'paS19', 'paC5', 'paC10', 'paC19'):
            n += 1
            bad += not np.array_equal(D[s][r][k], D[s][r.replace('.y40.', '.y20.')][k])
chk(bad == 0, 'in every 40-year row the year-20 measures (and the share and capacity at years 5, 10, 19) equal the 20-year row, seed by seed: %d of %d differ' % (bad, n))
# cells without the CCO are the same rows under the two designs
bad = n = 0
for s in ('u', 'u10', 'v', 'v10'):
    for r in D[s]:
        p = r.split('.')
        if p[3] != 'c22' or p[5][0] != 'c':
            continue
        n += 1
        bad += not same(D[s][r], D[s]['.'.join(p[:3] + ['rls'] + p[4:])], C22_ONLY)
chk(n > 0 and bad == 0, 'U, U10, V, V10: the %d rows without the CCO are identical under the two designs (but the C2.2 reporting keys): %d differ' % (n, bad))
# the access diagnostics behave as the rule says
grow = [(s, r) for s in ('t', 'u', 'u10', 'v', 'v10', 'vj', 'y') for r in D[s] if not r.endswith('.held')]
bad = sum(not np.allclose(D[s][r]['paCap'] + D[s][r]['paOps'] + D[s][r]['paDem'], 100, atol=1e-9) for s, r in grow)
chk(bad == 0, 'every growing row: the shares of adult-years where capacity, operations or demand stopped growth add up to 100%%, every seed (%d rows): %d differ' % (len(grow), bad))
bad = sum(np.any(D[s][r]['paOps'] != 0) for s, r in grow if not r.endswith('.outside'))
chk(bad == 0, 'the operations limit never binds in the main reading (the Hub prices at cost): paOps is 0 on every seed of every row but Y\'s outside-cost rows (%d rows): %d differ' % (sum(1 for s, r in grow if not r.endswith('.outside')), bad))
bad = 0
for s in NEW:
    for r, v in D[s].items():
        y = int(r.split('.')[2][1:])
        path = [v['paS5'], v['paS10'], v['paS19']] + ([v['paS39']] if y == 40 else [])
        bad += any(np.any(path[i + 1] < path[i] - 1e-9) for i in range(len(path) - 1))
chk(bad == 0, 'the share never falls: paS5 <= paS10 <= paS19 (<= paS39), every seed of every row: %d rows differ' % bad)
bad = n = 0
for s in ('w', 'w10'):
    for r, v in D[s].items():
        q = int(r.split('.fix')[1]); n += 1
        bad += not (np.allclose(v['paSh'], q) and np.all(v['paLo'] == (100 if q < 40 else 0)) and np.all(v['paTh'] == (100 if q > 55 else 0))
                    and np.all(v['paCap'] + v['paOps'] + v['paDem'] == 0) and np.allclose(v['paS19'], q))
chk(n > 0 and bad == 0, 'every fixed-share row holds its share on every seed and year, below the 40%% test only under 40%%, above the 55%% test only from 60%%, no growth tallied (%d rows): %d differ' % (n, bad))
bad = n = 0
for r, v in D['y'].items():
    if r.endswith('.held'):
        n += 1
        bad += not (np.all(v['paCap'] + v['paOps'] + v['paDem'] == 0) and np.array_equal(v['paS5'], v['paS19']))
chk(n > 0 and bad == 0, 'the growth-off rows (Y, held) never grow (%d rows): %d differ' % (n, bad))

# ---------------------------------------------------------------- bootstrap: one resample per size
rng = np.random.default_rng(BSEED)


def resample():
    idx = rng.integers(0, NS, size=(NB, NS))
    W = np.zeros((NB, NS))
    np.add.at(W, (np.repeat(np.arange(NB), NS), idx.ravel()), 1.0 / NS)
    return W


W = {500: resample(), 2000: resample(), 10000: resample()}


def pct(b):
    return float(np.percentile(b, 2.5)), float(np.percentile(b, 97.5))


def bootp(b):
    return min(1.0, 2 * min((b <= 0).mean(), (b >= 0).mean()))


def holm(ps):
    order = sorted(range(len(ps)), key=lambda i: ps[i]); ok = [False] * len(ps); m = len(ps)
    for r, i in enumerate(order):
        if ps[i] <= 0.05 / (m - r):
            ok[i] = True
        else:
            break
    return ok


class E:
    """an estimate: per-seed vector x at size n (paired) or a difference of two sizes (independent)."""
    def __init__(self, x, n, x2=None, n2=None):
        self.x = x
        if x2 is None:
            self.b = x @ W[n].T
            self.m = float(x.mean())
        else:     # x2 at n2 minus x at n
            self.b = x2 @ W[n2].T - x @ W[n].T
            self.m = float(x2.mean() - x.mean())
        self.lo, self.hi = pct(self.b)
        self.p = bootp(self.b)

    @property
    def ex0(self):
        return self.lo > 0 or self.hi < 0

    @property
    def hw(self):
        return (self.hi - self.lo) / 2


def eff(row, base, o):
    """row against base, in the outcome's convention (reduction positive for shares)."""
    key, kind, T = o[1], o[2], o[3]
    if kind == 'red':
        return base[key] - row[key]
    if kind == 'infl':
        return (row[key] - base[key]) * 100
    if kind == 'iyr':
        return (row[key] ** (1.0 / T) - base[key] ** (1.0 / T)) * 100
    return row[key] - base[key]


def thr(o, cost_ref):
    if o[2] == 'diff':
        return 0.05 * abs(cost_ref)
    if o[2] == 'infl':
        return None
    return 1.0


# the bootstrap is S38's: its published members-only effect in the headline cell is reproduced
_t = E(eff(R('a', 'ref', 10000, 20, 'c22', 'main'), R('a', 'ref', 10000, 20, 'c22', 'none'), O20[0]), 10000)
chk('%.2f [%.2f, %.2f]' % (_t.m, _t.lo, _t.hi) == '17.62 [17.60, 17.65]',
    'the resample is S38\'s: the members-only release row\'s effect on basic living, C2.2, Reference, 10,000 adults, 20 years, is %.2f [%.2f, %.2f] (S38 published 17.62 [17.60, 17.65])' % (_t.m, _t.lo, _t.hi))

# ---------------------------------------------------------------- formatting
L = []
CSV = []


def out(*a):
    L.append(' '.join(str(x) for x in a))


def f(x, dg=2):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return 'n/a'
    if abs(x) >= 1000:
        return '{:,.0f}'.format(x)
    return ('{:.%df}' % dg).format(x)


def dgt(o):
    return 0 if o[2] == 'diff' else 2


def fe(t, dg=2):
    return '%s [%s, %s]' % (f(t.m, dg), f(t.lo, dg), f(t.hi, dg))


def csvrow(section, setting, outcome, name, t, *flags):
    CSV.append([section, setting, outcome, name, '%.6g' % t.m, '%.6g' % t.lo, '%.6g' % t.hi] + [('' if x is None else int(x)) for x in flags]
               + [''] * (3 - len(flags)))


def sign(t):
    return '+' if t.lo > 0 else '-' if t.hi < 0 else '0'


def dec1(t, th):
    """addendum rule 1 (the programme's rule 1 when th is None): material +/-, stated +/-, or not stated."""
    if not t.ex0:
        return 'not stated'
    if th is not None and abs(t.m) >= th:
        return 'material ' + sign(t)
    return 'stated ' + sign(t)


def status(t, th):
    if t.ex0 and th is not None and abs(t.m) >= th:
        return 'material ' + sign(t)
    return 'detected, below materiality' if t.ex0 else 'not detected'


def flg(t, mat, h):
    return ('†' if t.ex0 else '') + ('M' if mat else '') + ('H' if h else '')


def sname(n, y, d, e):
    return '%s, %s, %s adults, %d years' % (dict(DESIGNS)[d], dict(ENVS)[e], '{:,}'.format(n), y)


def skey(n, y, d, e):
    return 'n%d.y%d.%s.%s' % (n, y, d, e)


# ---------------------------------------------------------------- Q24: open access against members only (T against A)
Q24 = []
for d, _ in DESIGNS:
    for e, _ in ENVS:
        for n in (500, 10000):
            for y in (20, 40):
                Q24.append(dict(n=n, y=y, d=d, e=e, op=R('t', e, n, y, d, 'main.open'), mem=R('a', e, n, y, d, 'main'), none=R('a', e, n, y, d, 'none')))
for s in Q24:
    s['res'] = {}
    cost_ref = float((s['mem']['cost'] - s['none']['cost']).mean())
    claim = [o for o in OUTS[s['y']] if claimable(o)]
    for o in OUTS[s['y']]:
        acc = E(eff(s['op'], s['mem'], o), s['n'])
        won = E(eff(s['op'], s['none'], o), s['n'])
        wmem = E(eff(s['mem'], s['none'], o), s['n'])
        th = thr(o, cost_ref)
        s['res'][oid(o)] = dict(o=o, acc=acc, on=won, mem=wmem, th=th, d1=dec1(acc, th), pon=dec1(won, None), pmem=dec1(wmem, None))
    for o, h in zip(claim, holm([s['res'][oid(o)]['acc'].p for o in claim])):
        s['res'][oid(o)]['h'] = h
    k = skey(s['n'], s['y'], s['d'], s['e'])
    for o in OUTS[s['y']]:
        r = s['res'][oid(o)]
        csvrow('Q24 open access', k, oid(o), 'open - members', r['acc'], r['acc'].ex0, r['d1'].startswith('material'), r.get('h'))
        csvrow('Q24 open access', k, oid(o), 'open vs none', r['on'], r['on'].ex0)
        csvrow('Q24 open access', k, oid(o), 'members vs none', r['mem'], r['mem'].ex0)
    for lab, key, sc in SEC:
        t = E((s['op'][key] - s['mem'][key]) * sc, s['n'])
        s['res']['sec.' + key] = t
        csvrow('Q24 open access, secondary', k, key, 'open - members (level)', t, t.ex0)
    for key in PAK:
        if key.endswith('39') and s['y'] == 20:
            continue
        t = E(s['op'][key], s['n'])
        s['res']['pa.' + key] = t
        csvrow('Q24 open access, diagnostics', k, key, 'open row (level)', t)


def q24(n, y, d, e):
    return next(s for s in Q24 if (s['n'], s['y'], s['d'], s['e']) == (n, y, d, e))


def fl24(r):
    return flg(r['acc'], r['d1'].startswith('material'), r.get('h'))


# scale (addendum rule 1's last sentence; the programme's rule 3): 10,000 against 500 adults
SC24 = []
for d, _ in DESIGNS:
    for e, _ in ENVS:
        for y in (20, 40):
            a, b = q24(500, y, d, e), q24(10000, y, d, e)
            for o in OUTS[y]:
                if not claimable(o):
                    continue
                ra, rb = a['res'][oid(o)], b['res'][oid(o)]
                dl = E(ra['acc'].x, 500, rb['acc'].x, 10000)
                th = 0.05 * abs(ra['acc'].m) if o[2] == 'diff' else 1.0
                ok = abs(dl.m) > dl.hw and abs(dl.m) >= th
                SC24.append(dict(d=d, e=e, y=y, o=o, dl=dl, ok=ok, da=ra['d1'], db=rb['d1'], pa=(ra['pmem'], ra['pon']), pb=(rb['pmem'], rb['pon'])))
                csvrow('Q24 scale', 'y%d.%s.%s' % (y, d, e), oid(o), 'open - members: 10,000 minus 500 adults', dl, ok)

# ---------------------------------------------------------------- the factorial machinery (as S36, S38)
z = lambda: np.zeros(32)
NAMES, ROWS_ = [], []


def add(name, coef):
    NAMES.append(name); ROWS_.append(coef)


c = z(); c[31] = 1; add('v(all five)', c)
for i in range(5):
    c = z()
    for m in range(32):
        if m & (1 << i):
            continue
        kk = bin(m).count('1')
        w = math.factorial(kk) * math.factorial(4 - kk) / math.factorial(5)
        c[m | (1 << i)] += w; c[m] -= w
    add('shapley ' + PNAME[PARTS[i]], c)
c = z(); c[31] = 1
for i in range(5):
    c[1 << i] -= 1
add('contrast whole design', c)
PAIRS = list(combinations(range(5), 2))
PAIRN = ['%s x %s' % (PNAME[PARTS[i]], PNAME[PARTS[j]]) for i, j in PAIRS]
for (i, j), pn in zip(PAIRS, PAIRN):
    bi, bj = 1 << i, 1 << j
    c = z(); c[31] += 1; c[31 ^ bi] -= 1; c[31 ^ bj] -= 1; c[31 ^ bi ^ bj] += 1
    add('contrast ' + pn, c)
MAP = np.array(ROWS_)
IX = {nm: k for k, nm in enumerate(NAMES)}
CONTR = ['contrast whole design'] + ['contrast ' + p for p in PAIRN]
SHAP = ['shapley ' + PNAME[ch] for ch in PARTS]
chk(np.allclose(MAP[1:6, 1:].sum(0), MAP[0, 1:]), 'Shapley values add up to v(all five), as linear maps')


def cellname(m):
    if m == 0:
        return 'none'
    if m == 31:
        return 'main'
    return ''.join(ch if m & (1 << i) else ch.lower() for i, ch in enumerate(PARTS))


def vmat(e, n, y, d, o, ptf_study, suffix, off_study):
    """effects of the 31 cells against none: cells with PTF from ptf_study (row name + suffix), the others from off_study."""
    N = R(off_study, e, n, y, d, 'none')
    V = np.zeros((32, NS))
    for m in range(1, 32):
        row = R(ptf_study, e, n, y, d, cellname(m) + suffix) if (m & 2 and ptf_study) else R(off_study, e, n, y, d, cellname(m))
        V[m] = eff(row, N, o)
    return V


def factorial(sett, name, on_spec, ref_spec, section, extra_ref=None):
    """on_spec / ref_spec: (ptf_study or None, suffix) per size; the off study is B (500) or B10 (10,000)."""
    for s in sett:
        s['res'] = {}
        off = 'b' if s['n'] == 500 else 'b10'
        k = skey(s['n'], s['y'], s['d'], s['e'])
        for o in OUTS[s['y']]:
            Yon = MAP @ vmat(s['e'], s['n'], s['y'], s['d'], o, on_spec[s['n']][0], on_spec[s['n']][1], off)
            Yref = MAP @ vmat(s['e'], s['n'], s['y'], s['d'], o, ref_spec[s['n']][0], ref_spec[s['n']][1], off)
            on = {nm: E(Yon[kk], s['n']) for nm, kk in IX.items()}
            ref = {nm: E(Yref[kk], s['n']) for nm, kk in IX.items()}
            dl = {nm: E(Yon[kk] - Yref[kk], s['n']) for nm, kk in IX.items()}
            res = dict(o=o, Yon=Yon, on=on, ref=ref, dl=dl)
            if extra_ref:
                Yx = MAP @ vmat(s['e'], s['n'], s['y'], s['d'], o, extra_ref[s['n']][0], extra_ref[s['n']][1], off)
                res['dx'] = {nm: E(Yon[kk] - Yx[kk], s['n']) for nm, kk in IX.items()}
            th_on = thr(o, on['v(all five)'].m); th_ref = thr(o, ref['v(all five)'].m)
            res['hon'] = dict(zip(CONTR, holm([on[nm].p for nm in CONTR])))
            res['href'] = dict(zip(CONTR, holm([ref[nm].p for nm in CONTR])))
            res['st_on'] = {nm: status(on[nm], th_on) for nm in CONTR}
            res['st_ref'] = {nm: status(ref[nm], th_ref) for nm in CONTR}
            s['res'][oid(o)] = res
            for nm in NAMES:
                csvrow(section, k, oid(o), nm + ' (' + name + ')', on[nm], on[nm].ex0 if nm in CONTR else None,
                       res['st_on'][nm].startswith('material') if nm in CONTR else None, res['hon'].get(nm))
                csvrow(section, k, oid(o), nm + ' (members only)', ref[nm])
                csvrow(section, k, oid(o), nm + ' (' + name + ' - members only)', dl[nm], dl[nm].ex0)
                if extra_ref:
                    csvrow(section, k, oid(o), nm + ' (' + name + ' - open without the layer)', res['dx'][nm], res['dx'][nm].ex0)
    mx = max(float(np.abs(r['Yon'][1:6].sum(0) - r['Yon'][0]).max() / max(1.0, np.abs(r['Yon'][0]).max())) for s in sett for r in s['res'].values())
    chk(mx < 1e-9, 'per seed, in every setting and outcome, the Shapley values (%s) add up to v(all five) (largest relative gap %.1e)' % (name, mx))


def settings_f():
    S = []
    for d, _ in DESIGNS:
        for e, _ in ENVS:
            for y in (20, 40):
                S.append(dict(n=500, y=y, d=d, e=e))
            S.append(dict(n=10000, y=20, d=d, e=e))
    return S


# ---------------------------------------------------------------- Q25: synergy under open access (U, U10 with B, B10)
Q25 = settings_f()
factorial(Q25, 'open', {500: ('u', '.open'), 10000: ('u10', '.open')}, {500: (None, ''), 10000: (None, '')}, 'Q25 synergy under open access')
bad = sum(not np.array_equal(s['res']['fgt0PY']['on']['v(all five)'].x, q24(s['n'], s['y'], s['d'], s['e'])['res']['fgt0PY']['on'].x) for s in Q25)
chk(bad == 0, 'the open factorial\'s full cell is Q24\'s open release row, seed by seed (18 settings): %d differ' % bad)


def chg_count(sett):
    """decision changes between the open and members-only factorials (claimable outcomes, 11 contrasts)."""
    n = ch = mat = 0
    lst = []
    for s in sett:
        for o in OUTS[s['y']]:
            if not claimable(o):
                continue
            r = s['res'][oid(o)]
            for nm in CONTR:
                n += 1
                a, b = r['st_ref'][nm], r['st_on'][nm]
                if a != b:
                    ch += 1
                    if a.startswith('material') or b.startswith('material'):
                        mat += 1
                        lst.append((s, o, nm, a, b, r['ref'][nm], r['on'][nm], r['dl'][nm]))
    return n, ch, mat, lst


def shap_moves(sett):
    """Shapley values and contrasts whose change from members only has an interval excluding zero (rule 5), and the largest."""
    n = nx = 0
    big = {}
    for s in sett:
        for o in OUTS[s['y']]:
            if not claimable(o):
                continue
            r = s['res'][oid(o)]
            for nm in SHAP + CONTR:
                n += 1
                t = r['dl'][nm]
                nx += t.ex0
                kk = (OUTS[s['y']].index(o), nm)
                if kk not in big or abs(t.m) > abs(big[kk][0].m):
                    big[kk] = (t, s)
    return n, nx, big


# ---------------------------------------------------------------- Q26: the layer under open access
# Q7 under open access: V (500), V10 (10,000, 20 years), VJ (10,000, 40 years; 2,000) against T (no layer, open)
Q26a = []
for d, _ in DESIGNS:
    for e, _ in ENVS:
        for y in (20, 40):
            Q26a.append(dict(n=500, y=y, d=d, e=e, on=R('v', e, 500, y, d, 'main.lay.open'), off=R('t', e, 500, y, d, 'main.open'),
                             mon=R('g', e, 500, y, d, 'main.lay'), moff=R('b', e, 500, y, d, 'main'), none=R('a', e, 500, y, d, 'none')))
        Q26a.append(dict(n=10000, y=20, d=d, e=e, on=R('v10', e, 10000, 20, d, 'main.lay.open'), off=R('t', e, 10000, 20, d, 'main.open'),
                         mon=R('g10', e, 10000, 20, d, 'main.lay'), moff=R('b10', e, 10000, 20, d, 'main'), none=R('a', e, 10000, 20, d, 'none')))
        Q26a.append(dict(n=10000, y=40, d=d, e=e, on=R('vj', e, 10000, 40, d, 'main.lay.open'), off=R('t', e, 10000, 40, d, 'main.open'),
                         mon=R('j', e, 10000, 40, d, 'main.lay'), moff=R('a', e, 10000, 40, d, 'main'), none=R('a', e, 10000, 40, d, 'none')))
        for y in (20, 40):   # 2,000 adults: no open row without the layer was run, so the layer's effect under open access cannot be formed
            Q26a.append(dict(n=2000, y=y, d=d, e=e, on=R('vj', e, 2000, y, d, 'main.lay.open'), off=None,
                             mon=R('j', e, 2000, y, d, 'main.lay'), moff=R('a', e, 2000, y, d, 'main'), none=R('a', e, 2000, y, d, 'none')))
for s in Q26a:
    s['res'] = {}
    k = skey(s['n'], s['y'], s['d'], s['e'])
    cost_ref = float((s['moff']['cost'] - s['none']['cost']).mean())
    claim = [o for o in OUTS[s['y']] if claimable(o)]
    for o in OUTS[s['y']]:
        th = thr(o, cost_ref)
        mlay = E(eff(s['mon'], s['moff'], o), s['n'])
        oacc = E(eff(s['on'], s['mon'], o), s['n'])   # open minus members, both with the layer
        won = E(eff(s['on'], s['none'], o), s['n'])
        r = dict(o=o, th=th, mlay=mlay, oacc=oacc, won=won, dm=dec1(mlay, th), dacc=dec1(oacc, th), pon=dec1(won, None))
        if s['off'] is not None:
            r['lay'] = E(eff(s['on'], s['off'], o), s['n'])
            r['dl'] = E(eff(s['on'], s['off'], o) - eff(s['mon'], s['moff'], o), s['n'])
            r['d1'] = dec1(r['lay'], th)
        s['res'][oid(o)] = r
    if s['off'] is not None:
        for o, h in zip(claim, holm([s['res'][oid(o)]['lay'].p for o in claim])):
            s['res'][oid(o)]['h'] = h
    for o in OUTS[s['y']]:
        r = s['res'][oid(o)]
        if 'lay' in r:
            csvrow('Q26 layer (Q7) under open access', k, oid(o), 'layer effect, open (lay.open - open)', r['lay'], r['lay'].ex0, r['d1'].startswith('material'), r.get('h'))
            csvrow('Q26 layer (Q7) under open access', k, oid(o), 'layer effect, open minus members only', r['dl'], r['dl'].ex0)
        csvrow('Q26 layer (Q7) under open access', k, oid(o), 'layer effect, members only', r['mlay'], r['mlay'].ex0)
        csvrow('Q26 layer (Q7) under open access', k, oid(o), 'open - members, both with the layer', r['oacc'], r['oacc'].ex0, r['dacc'].startswith('material'))
        csvrow('Q26 layer (Q7) under open access', k, oid(o), 'open with the layer vs none', r['won'], r['won'].ex0)
    for key in PAK + ['clZ', 'clTh', 'clHi']:
        if key in s['on'] and not (key.endswith('39') and s['y'] == 20):
            t = E(s['on'][key], s['n'])
            s['res']['pa.' + key] = t
            csvrow('Q26 layer, diagnostics', k, key, 'open row with the layer (level)', t)

# Q8 under open access: the layer factorial, PTF cells from V (V10); against the members-only layer factorial (G, G10) and the open one without the layer (U, U10)
Q26b = settings_f()
factorial(Q26b, 'open, layer', {500: ('v', '.lay.open'), 10000: ('v10', '.lay.open')}, {500: ('g', '.lay'), 10000: ('g10', '.lay')},
          'Q26 layer factorial (Q8) under open access', extra_ref={500: ('u', '.open'), 10000: ('u10', '.open')})

# Q9 under open access: study H's rows (from V) against the main-value row with the layer
HROWS = [('main.f67', 'f 2/3', 'main.lay', 'main'), ('main.f100', 'f 1', 'main.lay', 'main'), ('main.k50', 'k 50', 'main.lay', 'main'),
         ('main.k250', 'k 250', 'main.lay', 'main'), ('main.pop', 'imitation population-wide', 'main.lay', 'main')]
HROWS += [(cl + '.zc', cl + ' zones need CIP', cl + '.lay', cl) for cl in ('CFHZi', 'CFhZi', 'cFHZi', 'cFhZi')]
Q26c = []
for d, _ in DESIGNS:
    for e, _ in ENVS:
        for y in (20, 40):
            s = dict(d=d, e=e, y=y, res={})
            none = R('a', e, 500, y, d, 'none')
            cost_ref = float((R('a', e, 500, y, d, 'main')['cost'] - none['cost']).mean())
            for o in OUTS[y]:
                if o[2] == 'infl':
                    continue
                th = thr(o, cost_ref)
                rr = []
                for hr, lab, ref, offr in HROWS:
                    ho = R('v', e, 500, y, d, hr + '.open'); go = R('v', e, 500, y, d, ref + '.open')
                    bo = R('t', e, 500, y, d, 'main.open') if offr == 'main' else R('u', e, 500, y, d, offr + '.open')
                    hm = R('h', e, 500, y, d, hr); gm = R('g', e, 500, y, d, ref); bm = R('b', e, 500, y, d, offr)
                    vs = E(eff(ho, go, o), 500)
                    vs_m = E(eff(hm, gm, o), 500)
                    dd = E(eff(ho, go, o) - eff(hm, gm, o), 500)
                    lay_h, lay_g = E(eff(ho, bo, o), 500), E(eff(go, bo, o), 500)
                    pe_h, pe_g = E(eff(ho, none, o), 500), E(eff(go, none, o), 500)
                    rr.append(dict(row=hr, lab=lab, vs=vs, vs_m=vs_m, dd=dd, d1h=dec1(lay_h, th), d1g=dec1(lay_g, th), p1h=dec1(pe_h, None),
                                   p1g=dec1(pe_g, None), lay_h=lay_h))
                for x, hh in zip(rr, holm([x['vs'].p for x in rr])):
                    x['h'] = hh
                    kk = 'n500.y%d.%s.%s' % (y, d, e)
                    csvrow('Q26 design parameters (Q9) under open access', kk, oid(o), x['lab'] + ': row - main-value row (open)', x['vs'], x['vs'].ex0, None, hh)
                    csvrow('Q26 design parameters (Q9) under open access', kk, oid(o), x['lab'] + ': row - main-value row (members only)', x['vs_m'], x['vs_m'].ex0)
                    csvrow('Q26 design parameters (Q9) under open access', kk, oid(o), x['lab'] + ': open minus members only', x['dd'], x['dd'].ex0)
                    csvrow('Q26 design parameters (Q9) under open access', kk, oid(o), x['lab'] + ': layer effect (open)', x['lay_h'], x['lay_h'].ex0)
                s['res'][oid(o)] = dict(o=o, rows=rr, th=th)
            Q26c.append(s)

# Q10 under open access: the layer's effect at PTF starting shares 10%, 30%, 50% (from V) and at the environment's own (V against T)
Q26d = []
for d, _ in DESIGNS:
    for e, _ in ENVS:
        for y in (20, 40):
            s = dict(d=d, e=e, y=y, res={})
            cost_ref = float((R('a', e, 500, y, d, 'main')['cost'] - R('a', e, 500, y, d, 'none')['cost']).mean())
            for o in OUTS[y]:
                if o[2] == 'infl':
                    continue
                X, XM = {}, {}
                for sh in ('s10', 's30', 's50'):
                    X[sh] = eff(R('v', e, 500, y, d, 'main.%s.lay.open' % sh), R('v', e, 500, y, d, 'main.%s.off.open' % sh), o)
                    XM[sh] = eff(R('i', e, 500, y, d, 'main.%s.lay' % sh), R('i', e, 500, y, d, 'main.%s.off' % sh), o)
                X['own'] = eff(R('v', e, 500, y, d, 'main.lay.open'), R('t', e, 500, y, d, 'main.open'), o)
                XM['own'] = eff(R('g', e, 500, y, d, 'main.lay'), R('b', e, 500, y, d, 'main'), o)
                ests = {kk: E(v, 500) for kk, v in X.items()}
                dm = {kk: E(X[kk] - XM[kk], 500) for kk in X}
                hp = dict(zip(('s10', 's30', 's50'), holm([ests[kk].p for kk in ('s10', 's30', 's50')])))
                th = thr(o, cost_ref)
                diffs = {}
                for a_, b_ in (('s10', 's30'), ('s10', 's50'), ('s30', 's50')):
                    t = E(X[a_] - X[b_], 500)
                    diffs[a_ + '-' + b_] = (t, t.ex0 and abs(t.m) >= th)
                    csvrow('Q26 PTF starting size (Q10) under open access', 'n500.y%d.%s.%s' % (y, d, e), oid(o), 'layer effect %s minus %s (open)' % (a_, b_), t, t.ex0, diffs[a_ + '-' + b_][1])
                for kk, t in ests.items():
                    csvrow('Q26 PTF starting size (Q10) under open access', 'n500.y%d.%s.%s' % (y, d, e), oid(o), 'layer effect at %s (open)' % kk, t, t.ex0, None, hp.get(kk))
                    csvrow('Q26 PTF starting size (Q10) under open access', 'n500.y%d.%s.%s' % (y, d, e), oid(o), 'layer effect at %s: open minus members only' % kk, dm[kk], dm[kk].ex0)
                s['res'][oid(o)] = dict(o=o, ests=ests, dm=dm, hp=hp, diffs=diffs)
            Q26d.append(s)

# ---------------------------------------------------------------- Q27: response curve (W, W10 against A)
LEV = list(range(10, 101, 10))
Q27 = []
for d, _ in DESIGNS:
    for e, _ in ENVS:
        for n, y, st in ((500, 20, 'w'), (500, 40, 'w'), (10000, 20, 'w10')):
            Q27.append(dict(n=n, y=y, d=d, e=e, st=st))
for s in Q27:
    s['res'] = {}
    n, y, d, e = s['n'], s['y'], s['d'], s['e']
    none, mem = R('a', e, n, y, d, 'none'), R('a', e, n, y, d, 'main')
    cost_ref = float((mem['cost'] - none['cost']).mean())
    k = skey(n, y, d, e)
    for o in OUTS[y]:
        th = thr(o, cost_ref)
        F = {q: eff(R(s['st'], e, n, y, d, 'main.fix%d' % q), none, o) for q in LEV}
        G = {q: eff(R(s['st'], e, n, y, d, 'main.fix%d' % q), mem, o) for q in LEV}
        fv = {q: E(F[q], n) for q in LEV}
        gv = {q: E(G[q], n) for q in LEV}
        st40 = E((F[40] - F[30]) - ((F[30] - F[20]) + (F[50] - F[40])) / 2, n)
        st55 = E((F[60] - F[50]) - ((F[50] - F[40]) + (F[70] - F[60])) / 2, n)
        r = dict(o=o, th=th, fv=fv, gv=gv, st40=st40, st55=st55)
        if claimable(o):
            r['hf'] = dict(zip(LEV, holm([fv[q].p for q in LEV])))
            r['hg'] = dict(zip(LEV, holm([gv[q].p for q in LEV])))
            r['hs'] = holm([st40.p, st55.p])
        s['res'][oid(o)] = r
        for q in LEV:
            csvrow('Q27 response curve', k, oid(o), 'share %d%%: vs none' % q, fv[q], fv[q].ex0, None, r.get('hf', {}).get(q))
            csvrow('Q27 response curve', k, oid(o), 'share %d%%: vs members only' % q, gv[q], gv[q].ex0,
                   gv[q].ex0 and th is not None and abs(gv[q].m) >= th, r.get('hg', {}).get(q))
        for nm, t, hh in (('step at the 40% test', st40, r.get('hs', [None, None])[0]), ('step at the 55% test', st55, r.get('hs', [None, None])[1])):
            csvrow('Q27 response curve', k, oid(o), nm, t, t.ex0, t.ex0 and th is not None and abs(t.m) >= th, hh)
# scale for the curve: W10 against W at 20 years, level by level (the programme's rule 3)
SC27 = []
for d, _ in DESIGNS:
    for e, _ in ENVS:
        a = next(s for s in Q27 if (s['n'], s['y'], s['d'], s['e']) == (500, 20, d, e))
        b = next(s for s in Q27 if (s['n'], s['y'], s['d'], s['e']) == (10000, 20, d, e))
        for o in O20:
            if not claimable(o):
                continue
            for q in LEV:
                dl = E(a['res'][oid(o)]['fv'][q].x, 500, b['res'][oid(o)]['fv'][q].x, 10000)
                th = 0.05 * abs(a['res'][oid(o)]['fv'][q].m) if o[2] == 'diff' else 1.0
                ok = abs(dl.m) > dl.hw and abs(dl.m) >= th
                SC27.append(ok)
                csvrow('Q27 scale', 'y20.%s.%s' % (d, e), oid(o), 'share %d%% vs none: 10,000 minus 500 adults' % q, dl, ok)

# ---------------------------------------------------------------- Q28: growth (T's diagnostics; Y's swept settings)
YSET = [('d25', 'demand ceiling 25%'), ('d75', 'demand ceiling 75%'), ('d100', 'demand ceiling 100%'), ('capnone', 'no capacity limit'),
        ('outside', 'outside running costs'), ('held', 'growth off (share held at its start)')]
BIND = []   # by year: share of seeds where demand (else capacity) stopped growth that year
for s in Q24:
    v = s['op']
    s['bind'] = {}
    for yr in (5, 10, 19, 39):
        if yr == 39 and s['y'] != 40:
            continue
        dem = (v['paS%d' % yr] >= DEM - 1e-6).astype(float) * 100
        s['bind'][yr] = E(dem, s['n'])
        csvrow('Q28 which limit binds', skey(s['n'], s['y'], s['d'], s['e']), 'year %d' % yr, '% of seeds at the demand ceiling (else capacity binds)', s['bind'][yr])
Q28 = []
for d, _ in DESIGNS:
    for e, _ in ENVS:
        for y in (20, 40):
            s = dict(d=d, e=e, y=y, res={}, diag={})
            mem, none, main = R('a', e, 500, y, d, 'main'), R('a', e, 500, y, d, 'none'), R('t', e, 500, y, d, 'main.open')
            cost_ref = float((mem['cost'] - none['cost']).mean())
            base = q24(500, y, d, e)
            for o in OUTS[y]:
                if not claimable(o):
                    continue
                th = thr(o, cost_ref)
                rr = []
                for ys, lab in YSET:
                    row = R('y', e, 500, y, d, 'main.open.' + ys)
                    acc = E(eff(row, mem, o), 500)
                    vsm = E(eff(row, main, o), 500)
                    rr.append(dict(ys=ys, lab=lab, acc=acc, vsm=vsm, d1=dec1(acc, th), d0=base['res'][oid(o)]['d1'],
                                   p1=dec1(E(eff(row, none, o), 500), None), p0=base['res'][oid(o)]['pon']))
                for x, hh in zip(rr, holm([x['acc'].p for x in rr])):
                    x['h'] = hh
                    kk = 'n500.y%d.%s.%s' % (y, d, e)
                    csvrow('Q28 growth settings', kk, oid(o), x['lab'] + ': open - members', x['acc'], x['acc'].ex0, x['d1'].startswith('material'), hh)
                    csvrow('Q28 growth settings', kk, oid(o), x['lab'] + ': row - main-value open row', x['vsm'], x['vsm'].ex0)
                s['res'][oid(o)] = dict(o=o, rows=rr, th=th)
            for ys, lab in YSET:
                row = R('y', e, 500, y, d, 'main.open.' + ys)
                s['diag'][ys] = {kk: E(row[kk], 500) for kk in PAK if not (kk.endswith('39') and y == 20)}
                for kk in s['diag'][ys]:
                    csvrow('Q28 growth settings, diagnostics', 'n500.y%d.%s.%s' % (y, d, e), kk, lab + ' (level)', s['diag'][ys][kk])
            Q28.append(s)

# ================================================================ tables.md
OUTL = lambda y: [o for o in OUTS[y] if o[2] != 'infl']
out('# Open PTF access (S55): tables')
out('')
out('Full 500-seed runs of studies T, U, U10, V, V10, VJ, W, W10 and Y (engine `%s`, rows under open PTF access), each compared with the'
    ' frozen batch\'s rows on the same seeds (studies A, B, B10, G, G10, H, I and J, engine `%s`: members only; with the switch off the'
    ' two engines give the same figures). Generated by `python3 dev/tools/s55_open_access.py <compassionism-sim-results checkout>'
    ' dev/runs/s55-open-access` from BetterToBest/compassionism-sim-results `prog-{t,u,u10,v,v10,vj,w,w10,y}-%s` and'
    ' `prog-{a,b,b10,g,g10,h,i,j}-%s`. Every interval is a 95%% paired-bootstrap interval over seeds (10,000 replicates); comparisons'
    ' between population sizes are independent runs. For the three shares a reduction is a positive number of points, so a positive'
    ' "open − members" figure means open access helps; for cost and inflation positive means more cost or more inflation. Flags: †'
    ' interval excludes zero; M also material (1 point; 5%% of the members-only row\'s cost, or of the full design\'s cost for'
    ' contrasts; 1 point of the yearly inflation rate); H survives Holm in its preregistered family. Every estimate is also in'
    ' `estimates.csv`.' % (ENG, ENGF, ENG, ENGF))
out('')
out('## 0. Checks')
out('')
CHK_AT = len(L)
out('')

# 1. headline
out('## 1. The headline cell (Q24): C2.2 design, Reference, 10,000 adults, 20 years, CPS yardstick, raise off')
out('')
for d, dn in DESIGNS:
    s = q24(10000, 20, d, 'ref')
    out('**%s.** The release row with members only and with open access, against no programme, and open access\'s effect (paired).' % dn)
    out('')
    out('| Outcome | Effect, members only | Effect, open access | Open − members | Flags | Programme rule 1 (members / open) |')
    out('|---|---|---|---|---|---|')
    for o in OUTS[20]:
        r = s['res'][oid(o)]
        pr = r['pmem'] + ' / ' + r['pon']
        out('| %s | %s | %s | %s | %s | %s |' % (o[0], fe(r['mem'], dgt(o)), fe(r['on'], dgt(o)), fe(r['acc'], dgt(o)), fl24(r),
                                              pr if r['pmem'] == r['pon'] else '**' + pr + '**'))
    out('')
    out('Secondary outcomes, open − members (level difference): ' + '; '.join('%s %s%s' % (lab, fe(s['res']['sec.' + key]), ' †' if s['res']['sec.' + key].ex0 else '')
                                                                             for lab, key, sc in SEC) + '.')
    out('')
    out('Access diagnostics of the open row (mean over seeds): ' + '; '.join('%s %s' % (kk, fe(s['res']['pa.' + kk])) for kk in PAK if not kk.endswith('39')) + '.')
    out('')

# 2. Q24 every setting
out('## 2. Open access against members only, every setting (Q24)')
out('')
out('Open − members (paired), the row\'s effect with members only and with open access (against no programme), and the decisions under'
    ' the addendum\'s rule 1 (open − members) and the programme\'s rule 1 (each row against no programme; bold where they differ).')
out('')
for d, dn in DESIGNS:
    out('### %s' % dn)
    out('')
    out('| Setting | Outcome | Open − members | Flags | Rule 1 | Effect, members only | Effect, open | Programme rule 1 (members / open) |')
    out('|---|---|---|---|---|---|---|---|')
    for e, en in ENVS:
        for n in (500, 10000):
            for y in (20, 40):
                s = q24(n, y, d, e)
                for o in OUTS[y]:
                    if o[2] == 'infl':
                        continue
                    r = s['res'][oid(o)]
                    pr = r['pmem'] + ' / ' + r['pon']
                    out('| %s, %s, %d y | %s | %s | %s | %s | %s | %s | %s |' % (en, '{:,}'.format(n), y, o[0], fe(r['acc'], dgt(o)), fl24(r), r['d1'],
                                                                         fe(r['mem'], dgt(o)), fe(r['on'], dgt(o)), pr if r['pmem'] == r['pon'] else '**' + pr + '**'))
    out('')
out('### Secondary outcomes (open − members, level difference)')
out('')
out('| Setting | ' + ' | '.join(lab for lab, _, _ in SEC) + ' |')
out('|---|' + '---|' * len(SEC))
for s in Q24:
    out('| %s | %s |' % (sname(s['n'], s['y'], s['d'], s['e']), ' | '.join(fe(s['res']['sec.' + key]) + (' †' if s['res']['sec.' + key].ex0 else '') for _, key, _ in SEC)))
out('')
nmat24 = sum(1 for s in Q24 for o in OUTS[s['y']] if claimable(o) and s['res'][oid(o)]['d1'].startswith('material'))
nst24 = sum(1 for s in Q24 for o in OUTS[s['y']] if claimable(o) and s['res'][oid(o)]['d1'] != 'not stated')
nall24 = sum(1 for s in Q24 for o in OUTS[s['y']] if claimable(o))
pch24 = [(s, o) for s in Q24 for o in OUTS[s['y']] if claimable(o) and s['res'][oid(o)]['pmem'] != s['res'][oid(o)]['pon']]
out('Over all %d settings: %d of %d open-access effects on the claimable outcomes are stated (interval excludes zero), %d material. The'
    ' programme\'s rule-1 decision (the row against no programme) differs between members only and open access in %d outcome-settings%s.'
    % (len(Q24), nst24, nall24, nmat24, len(pch24), (': ' + '; '.join('%s, %s (%s → %s)' % (sname(s['n'], s['y'], s['d'], s['e']), o[0], s['res'][oid(o)]['pmem'], s['res'][oid(o)]['pon']) for s, o in pch24)) if pch24 else ''))
out('')
out('### 500 against 10,000 adults (rule 1, last sentence; the programme\'s rule 3)')
out('')
dif = [x for x in SC24 if x['da'] != x['db']]
pdif = [x for x in SC24 if x['pa'] != x['pb']]
out('%d of %d open-access decisions differ between 500 and 10,000 adults%s. %d of %d differences pass the scale rule (|Δ| above its Monte Carlo error'
    ' and the materiality threshold). The programme\'s rule-1 decision differs between sizes in %d of %d outcome-settings.'
    % (len(dif), len(SC24), (': ' + '; '.join('%s, %s, %d years, %s: %s at 500, %s at 10,000' % (dict(DESIGNS)[x['d']], dict(ENVS)[x['e']], x['y'], x['o'][0], x['da'], x['db']) for x in dif)) if dif else '',
       sum(x['ok'] for x in SC24), len(SC24), len(pdif), len(SC24)))
out('')

# 3. Q28 growth
out('## 3. Growth: which limit binds, by environment and year (Q28)')
out('')
out('The open release row (main values: capacity from the PTFs\' own capital, the Hub\'s cost structure, demand ceiling 49%). paCap, paOps,'
    ' paDem: share of adult-years from year 1 in zones where that limit stopped growth (%). Share s and capacity c at the year\'s index (%).'
    ' "At the ceiling": share of seeds whose s has reached the 49% demand ceiling that year; on every other seed capacity binds that year'
    ' (operations never binds in the main reading, section 0).')
out('')
out('| Setting | paCap | paOps | paDem | s, year 5 | s, year 10 | s, year 19 | s, year 39 | c, year 5 | c, year 10 | c, year 19 | c, year 39 | At the ceiling, years 5 / 10 / 19 / 39 |')
out('|---|---|---|---|---|---|---|---|---|---|---|---|---|')
for s in Q24:
    p = lambda kk: f(s['res']['pa.' + kk].m, 1)
    bd = ' / '.join('%.0f%%' % s['bind'][yr].m for yr in (5, 10, 19, 39) if yr in s['bind'])
    out('| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (sname(s['n'], s['y'], s['d'], s['e']), p('paCap'), p('paOps'), p('paDem'),
        p('paS5'), p('paS10'), p('paS19'), p('paS39') if s['y'] == 40 else '–', p('paC5'), p('paC10'), p('paC19'), p('paC39') if s['y'] == 40 else '–', bd))
out('')
out('The share over the run and the two tests (open release row): paSh mean share of essential sales; paLo adult-years below the 40% test;'
    ' paTh adult-years above the 55% test; paCv sales at PTF prices over running costs at outside margins; pfMem members (% of adults); pfCut'
    ' the mean PTF price cut over every adult.')
out('')
out('| Setting | paSh | paLo | paTh | paCv | pfMem | pfCut |')
out('|---|---|---|---|---|---|---|')
for s in Q24:
    out('| %s | %s |' % (sname(s['n'], s['y'], s['d'], s['e']), ' | '.join(fe(s['res']['pa.' + kk]) for kk in ('paSh', 'paLo', 'paTh', 'paCv', 'pfMem', 'pfCut'))))
out('')
out('### The growth rule\'s settings (study Y, 500 adults; rule 2)')
out('')
out('Diagnostics of each swept row (mean over seeds): the share over the run, at years 10 and 19, and which limit stopped growth.')
out('')
out('| Setting | Swept row | paSh | s, year 10 | s, year 19 | s, year 39 | paCap | paOps | paDem | paLo | paTh |')
out('|---|---|---|---|---|---|---|---|---|---|---|')
for s in Q28:
    base = q24(500, s['y'], s['d'], s['e'])
    out('| %s | main values | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (sname(500, s['y'], s['d'], s['e']), *[f(base['res']['pa.' + kk].m, 1) if not (kk == 'paS39' and s['y'] == 20) else '–'
                                                                       for kk in ('paSh', 'paS10', 'paS19', 'paS39', 'paCap', 'paOps', 'paDem', 'paLo', 'paTh')]))
    for ys, lab in YSET:
        g = s['diag'][ys]
        out('| | %s | %s |' % (lab, ' | '.join(f(g[kk].m, 1) if not (kk == 'paS39' and s['y'] == 20) else '–' for kk in ('paSh', 'paS10', 'paS19', 'paS39', 'paCap', 'paOps', 'paDem', 'paLo', 'paTh'))))
out('')
out('Open − members under each swept setting (paired; rule 1 decision), and the swept row minus the main-value open row. Bold where the rule-1'
    ' decision differs from the main-value row\'s.')
out('')
DIFF28 = []
for s in Q28:
    out('#### %s' % sname(500, s['y'], s['d'], s['e']))
    out('')
    out('| Outcome | Main values: open − members | ' + ' | '.join(lab for _, lab in YSET) + ' |')
    out('|---|---|' + '---|' * len(YSET))
    for o in OUTS[s['y']]:
        if not claimable(o):
            continue
        r = s['res'][oid(o)]
        b = q24(500, s['y'], s['d'], s['e'])['res'][oid(o)]
        cells = []
        for x in r['rows']:
            c_ = '%s %s; vs main %s' % (fe(x['acc'], dgt(o)), flg(x['acc'], x['d1'].startswith('material'), x['h']), fe(x['vsm'], dgt(o)))
            if x['d1'] != x['d0']:
                c_ = '**' + c_ + ' (' + x['d1'] + ')**'
                DIFF28.append((s, o, x))
            cells.append(c_)
        out('| %s | %s %s (%s) | %s |' % (o[0], fe(b['acc'], dgt(o)), fl24(b), b['d1'], ' | '.join(cells)))
    out('')
DIFF28m = [z_ for z_ in DIFF28 if z_[2]['d1'].startswith('material') != z_[2]['d0'].startswith('material')]
out('Rule-1 decisions that differ from the main-value row: %d of %d (of which %d cross the materiality line). By setting: %s.'
    % (len(DIFF28), sum(len(s['res']) * len(YSET) for s in Q28), len(DIFF28m),
       ', '.join('%s %d (%d material)' % (lab, sum(1 for z_ in DIFF28 if z_[2]['ys'] == ys), sum(1 for z_ in DIFF28m if z_[2]['ys'] == ys)) for ys, lab in YSET)))
out('')
PDIFF28 = [(s, o, x) for s in Q28 for o in OUTS[s['y']] if claimable(o) for x in s['res'][oid(o)]['rows'] if x['p1'] != x['p0']]
out('The programme\'s rule-1 decision (the swept row against no programme) differs from the main-value open row\'s in %d outcome-settings%s.'
    % (len(PDIFF28), (': ' + '; '.join('%s, %s, %s (%s → %s)' % (sname(500, s['y'], s['d'], s['e']), o[0], x['lab'], x['p0'], x['p1']) for s, o, x in PDIFF28)) if PDIFF28 else ''))
out('')

# 4. Q27 response curve
out('## 4. The fixed-share response curve (Q27)')
out('')
out('The release row with every zone\'s PTF share of essential sales held at 10%, ..., 100% (growth off). For each level, the row\'s effect'
    ' against no programme and against the members-only release row. Steps: the change across a test minus the mean of the two neighbouring'
    ' changes (rule 4: a step is claimed where its interval excludes zero and it is at least 1 point, or 5% of the members-only row\'s cost).')
out('')
for s in Q27:
    out('### %s' % sname(s['n'], s['y'], s['d'], s['e']))
    out('')
    out('Against no programme:')
    out('')
    out('| Outcome | ' + ' | '.join('%d%%' % q for q in LEV) + ' | Step at 40% | Step at 55% |')
    out('|---|' + '---|' * (len(LEV) + 2))
    for o in OUTL(s['y']):
        r = s['res'][oid(o)]
        hs = r.get('hs', [None, None])
        out('| %s | %s | %s | %s |' % (o[0], ' | '.join(fe(r['fv'][q], dgt(o)) for q in LEV),
                                       fe(r['st40'], dgt(o)) + ' ' + flg(r['st40'], r['st40'].ex0 and r['th'] is not None and abs(r['st40'].m) >= r['th'], hs[0]),
                                       fe(r['st55'], dgt(o)) + ' ' + flg(r['st55'], r['st55'].ex0 and r['th'] is not None and abs(r['st55'].m) >= r['th'], hs[1])))
    out('')
    out('Against the members-only release row (flags as rule 1):')
    out('')
    out('| Outcome | ' + ' | '.join('%d%%' % q for q in LEV) + ' |')
    out('|---|' + '---|' * len(LEV))
    for o in OUTL(s['y']):
        r = s['res'][oid(o)]
        out('| %s | %s |' % (o[0], ' | '.join(fe(r['gv'][q], dgt(o)) + ' ' + flg(r['gv'][q], r['gv'][q].ex0 and r['th'] is not None and abs(r['gv'][q].m) >= r['th'], r.get('hg', {}).get(q)) for q in LEV)))
    out('')
STEPS = [(s, o, nm, r[nm]) for s in Q27 for o in OUTS[s['y']] if claimable(o) for r in [s['res'][oid(o)]] for nm in ('st40', 'st55')]
STEPc = [x for x in STEPS if x[3].ex0 and abs(x[3].m) >= x[0]['res'][oid(x[1])]['th']]
out('Steps claimed under rule 4: %d of %d%s. Steps with an interval excluding zero but below the threshold: %d.'
    % (len(STEPc), len(STEPS), (' (' + '; '.join('%s, %s, %s %s' % (sname(s['n'], s['y'], s['d'], s['e']), o[0], {'st40': 'at 40%', 'st55': 'at 55%'}[nm], fe(t, dgt(o))) for s, o, nm, t in STEPc) + ')') if STEPc else '',
       sum(1 for x in STEPS if x[3].ex0) - len(STEPc)))
out('')
out('Scale (W10 against W, 20 years, every level, claimable outcomes): %d of %d differences pass the programme\'s scale rule.' % (sum(SC27), len(SC27)))
out('')

# 5. Q25 synergy
def fblock(s, name, refname, extra=None):
    out('#### %s' % sname(s['n'], s['y'], s['d'], s['e']))
    out('')
    out('Shapley values (%s), and their change from %s (Δ, paired):' % (name, refname))
    out('')
    out('| Outcome | v(all five) | ' + ' | '.join(PNAME[ch] for ch in PARTS) + ' |')
    out('|---|---|' + '---|' * 5)
    for o in OUTL(s['y']):
        r = s['res'][oid(o)]
        out('| %s | %s |' % (o[0], ' | '.join('%s; Δ %s' % (fe(r['on'][nm], dgt(o)), fe(r['dl'][nm], dgt(o))) for nm in ['v(all five)'] + SHAP)))
    out('')
    out('Interaction contrasts (%s; flags), and Δ from %s:' % (name, refname))
    out('')
    out('| Outcome | ' + ' | '.join(nm.replace('contrast ', '') for nm in CONTR) + ' |')
    out('|---|' + '---|' * len(CONTR))
    for o in OUTL(s['y']):
        r = s['res'][oid(o)]
        cells = []
        for nm in CONTR:
            fl = flg(r['on'][nm], r['st_on'][nm].startswith('material'), r['hon'][nm])
            cells.append('%s%s; Δ %s' % (fe(r['on'][nm], dgt(o)), ' ' + fl if fl else '', fe(r['dl'][nm], dgt(o))))
        out('| %s | %s |' % (o[0], ' | '.join(cells)))
    out('')


out('## 5. Synergy under open access (Q25)')
out('')
n25, c25, m25, l25 = chg_count(Q25)
sn25, sx25, big25 = shap_moves(Q25)
out('The study programme\'s factorial with its 16 cells that include PTF run under open access (studies U, U10) and the other 15 cells and'
    ' the none row from B (B10). %d of %d contrast decisions (claimable outcomes, 11 contrasts, 18 settings) change between members only and'
    ' open access; %d of them cross the materiality line%s. Of the %d Shapley values and contrasts on the claimable outcomes, %d change from members only'
    ' with an interval excluding zero (rule 5).'
    % (c25, n25, m25, (': ' + '; '.join('%s, %s, %s: %s → %s (%s → %s; Δ %s)' % (sname(s['n'], s['y'], s['d'], s['e']), o[0], nm.replace('contrast ', ''), a, b, fe(ra, dgt(o)), fe(rb, dgt(o)), fe(dd, dgt(o)))
                                     for s, o, nm, a, b, ra, rb, dd in l25)) if l25 else '', sn25, sx25))
out('')
out('Largest change from members only, per outcome, over the 18 settings:')
out('')
out('| Estimate | ' + ' | '.join(o[0] for o in O20 if claimable(o)) + ' |')
out('|---|' + '---|' * 5)
for nm in SHAP + CONTR:
    cells = []
    for o in O20:
        if not claimable(o):
            continue
        t, s = big25[(O20.index(o), nm)]
        cells.append('%s (%s)' % (fe(t, dgt(o)), '%s %s %d/%dy' % (s['d'], s['e'], s['n'], s['y'])))
    out('| %s | %s |' % (nm, ' | '.join(cells)))
out('')
for s in Q25:
    fblock(s, 'open access', 'members only')

# 6. Q26 the layer under open access
out('## 6. The community layer under open access (Q26)')
out('')
out('### Q7: the layer\'s effect on the release row, open access')
out('')
out('The open release row with the layer minus the open release row without it (paired); the same with members only (S38); and the difference.'
    ' At 2,000 adults no open row without the layer was run, so only the open row with the layer against members only (both with the layer)'
    ' is shown.')
out('')
out('| Setting | Outcome | Layer effect, open | Flags | Layer effect, members only | Open minus members only | Open − members, both with the layer |')
out('|---|---|---|---|---|---|---|')
for s in Q26a:
    for o in OUTS[s['y']]:
        if o[2] == 'infl':
            continue
        r = s['res'][oid(o)]
        if 'lay' in r:
            out('| %s | %s | %s | %s | %s | %s | %s |' % (sname(s['n'], s['y'], s['d'], s['e']), o[0], fe(r['lay'], dgt(o)),
                                                     flg(r['lay'], r['d1'].startswith('material'), r.get('h')), fe(r['mlay'], dgt(o)), fe(r['dl'], dgt(o)), fe(r['oacc'], dgt(o))))
        else:
            out('| %s | %s | – | | %s | – | %s |' % (sname(s['n'], s['y'], s['d'], s['e']), o[0], fe(r['mlay'], dgt(o)), fe(r['oacc'], dgt(o))))
out('')
q7m = sum(1 for s in Q26a for o in OUTS[s['y']] if claimable(o) and 'd1' in s['res'][oid(o)] and s['res'][oid(o)]['d1'].startswith('material'))
q7n = sum(1 for s in Q26a for o in OUTS[s['y']] if claimable(o) and 'd1' in s['res'][oid(o)])
q7mm = sum(1 for s in Q26a for o in OUTS[s['y']] if claimable(o) and s['res'][oid(o)]['dm'].startswith('material'))
q7am = sum(1 for s in Q26a for o in OUTS[s['y']] if claimable(o) and s['res'][oid(o)]['dacc'].startswith('material'))
out('Material layer effects under open access: %d of %d (members only, the same settings and the 2,000-adult ones: %d). Open access with the layer'
    ' against members only with the layer: %d of %d material.' % (q7m, q7n, q7mm, q7am, sum(1 for s in Q26a for o in OUTS[s['y']] if claimable(o))))
out('')
out('Diagnostics of the open rows with the layer (mean over seeds): the share over the run, the tests, zones.')
out('')
out('| Setting | paSh | paLo | paTh | paCap | paDem | s, year 19 | clZ | pfMem | pfCut |')
out('|---|---|---|---|---|---|---|---|---|---|')
for s in Q26a:
    out('| %s | %s |' % (sname(s['n'], s['y'], s['d'], s['e']), ' | '.join(f(s['res']['pa.' + kk].m, 1) if 'pa.' + kk in s['res'] else 'n/a'
                                                                         for kk in ('paSh', 'paLo', 'paTh', 'paCap', 'paDem', 'paS19', 'clZ', 'pfMem', 'pfCut'))))
out('')
out('### Q8: the layer\'s synergy table under open access')
out('')
n26, c26, m26, l26 = chg_count(Q26b)
sn26, sx26, big26 = shap_moves(Q26b)
out('The layer factorial with its 16 PTF cells run under open access (V, V10), against the same factorial with members only (G, G10; S38).'
    ' %d of %d contrast decisions change; %d cross the materiality line%s. %d of %d Shapley values and contrasts change from members only with an'
    ' interval excluding zero.'
    % (c26, n26, m26, (': ' + '; '.join('%s, %s, %s: %s → %s (%s → %s; Δ %s)' % (sname(s['n'], s['y'], s['d'], s['e']), o[0], nm.replace('contrast ', ''), a, b, fe(ra, dgt(o)), fe(rb, dgt(o)), fe(dd, dgt(o)))
                                     for s, o, nm, a, b, ra, rb, dd in l26)) if l26 else '', sx26, sn26))
out('')
out('Largest change from members only, per outcome, over the 18 settings:')
out('')
out('| Estimate | ' + ' | '.join(o[0] for o in O20 if claimable(o)) + ' |')
out('|---|' + '---|' * 5)
for nm in SHAP + CONTR:
    cells = []
    for o in O20:
        if not claimable(o):
            continue
        t, s = big26[(O20.index(o), nm)]
        cells.append('%s (%s)' % (fe(t, dgt(o)), '%s %s %d/%dy' % (s['d'], s['e'], s['n'], s['y'])))
    out('| %s | %s |' % (nm, ' | '.join(cells)))
out('')
for s in Q26b:
    if (s['e'], s['n'], s['y']) in (('ref', 10000, 20), ('ref', 500, 20)):
        fblock(s, 'open access, layer on', 'members only, layer on')
out('Every other setting of this table is in `estimates.csv` (section "Q26 layer factorial (Q8) under open access"), with the change from'
    ' the open factorial without the layer.')
out('')
out('### Q9: the layer\'s design parameters under open access (study H\'s rows)')
out('')
out('Each row minus the main-value row with the layer (open; members only; and the difference). Decisions under the layer addendum\'s rule 1'
    ' (layer effect) and the programme\'s rule 1 (row against no programme) that differ from the main-value row\'s are counted.')
out('')
out('| Setting | Outcome | ' + ' | '.join(lab for _, lab, _, _ in HROWS) + ' |')
out('|---|---|' + '---|' * len(HROWS))
DIFF9 = []
for s in Q26c:
    for o in OUTL(s['y']):
        r = s['res'][oid(o)]
        cells = []
        for x in r['rows']:
            if x['d1h'] != x['d1g'] or x['p1h'] != x['p1g']:
                DIFF9.append((s, o, x))
            cells.append('%s; Δ %s' % (fe(x['vs'], dgt(o)), fe(x['dd'], dgt(o))))
        out('| %s | %s | %s |' % (sname(500, s['y'], s['d'], s['e']), o[0], ' | '.join(cells)))
out('')
nmat9 = sum(1 for s in Q26c for o in OUTL(s['y']) if claimable(o) for x in s['res'][oid(o)]['rows'] if x['d1h'].startswith('material'))
pd9 = [z_ for z_ in DIFF9 if claimable(z_[1]) and z_[2]['p1h'] != z_[2]['p1g']]
out('Rows with a material layer effect under open access: %d. Outcome-settings where a decision differs from the main-value row: %d (layer rule 1'
    ' or the programme\'s rule 1, every outcome shown); of which the programme\'s rule 1 on a claimable outcome: %d%s.'
    % (nmat9, len(DIFF9), len(pd9), (' (' + '; '.join('%s, %s, %s: %s → %s' % (sname(500, s['y'], s['d'], s['e']), o[0], x['lab'], x['p1g'], x['p1h']) for s, o, x in pd9) + ')') if pd9 else ''))
out('')
out('### Q10: the PTF\'s starting size under open access (study I\'s rows)')
out('')
out('The layer\'s effect at starting shares of 10%, 30% and 50% and at the environment\'s own, open access; Δ from members only.')
out('')
out('| Setting | Outcome | 10% | 30% | 50% | own | 10% − 30% | 10% − 50% | 30% − 50% |')
out('|---|---|---|---|---|---|---|---|---|')
DEP10 = []
for s in Q26d:
    for o in OUTL(s['y']):
        r = s['res'][oid(o)]
        for kk, (t, ok) in r['diffs'].items():
            if ok and claimable(o):
                DEP10.append((s, o, kk, t))
        out('| %s | %s | %s | %s |' % (sname(500, s['y'], s['d'], s['e']), o[0],
                                       ' | '.join('%s; Δ %s' % (fe(r['ests'][kk], dgt(o)), fe(r['dm'][kk], dgt(o))) for kk in ('s10', 's30', 's50', 'own')),
                                       ' | '.join(fe(r['diffs'][kk][0], dgt(o)) + (' M' if r['diffs'][kk][1] else '') for kk in ('s10-s30', 's10-s50', 's30-s50'))))
out('')
out('Differences between starting shares that are material (rule 4 of the layer addendum) on a claimable outcome: %d%s.'
    % (len(DEP10), (' (' + '; '.join('%s, %s, %s %s' % (sname(500, s['y'], s['d'], s['e']), o[0], kk, fe(t, dgt(o))) for s, o, kk, t in DEP10) + ')') if DEP10 else ''))
out('')

# checks at the top
L[CHK_AT:CHK_AT] = ['- ' + c_ for c_ in CHECKS]

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, 'tables.md'), 'w') as fh:
    fh.write('\n'.join(L) + '\n')
with open(os.path.join(OUT, 'estimates.csv'), 'w', newline='') as fh:
    wr = csv.writer(fh)
    wr.writerow(['section', 'setting', 'outcome', 'estimate', 'mean', 'lo95', 'hi95', 'excludes_zero', 'material', 'holm'])
    wr.writerows(CSV)
print('checks: %d, failed: %d; estimates: %d' % (len(CHECKS), sum(c_.startswith('FAIL') for c_ in CHECKS), len(CSV)))
sys.exit(1 if any(c_.startswith('FAIL') for c_ in CHECKS) else 0)
