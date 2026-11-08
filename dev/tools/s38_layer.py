#!/usr/bin/env python3
"""S38 community-layer report: every table of dev/reports/s38-community-layer.md, from the full study batch.

Usage: python3 dev/tools/s38_layer.py <compassionism-sim-results checkout> <out dir>
Reads prog-{g,g10,h,i,j}-ce8d030 (the layer's rows) and prog-{a,b,b10}-ce8d030 (the same rows without the layer, and the
no-programme rows), through batch_load.py. Writes <out dir>/tables.md (every table) and <out dir>/estimates.csv.

Method (research-update prereg/2026-11-community-layer.md, with its Amendment 1; the study programme's Analysis, unchanged):
- Q7 layer effect: per seed, the release row with the layer minus the release row without it (paired), and the release row's
  effect against none with and without the layer. 500 adults: G against B (CPS and released-wage yardsticks, raise off and on);
  2,000 adults: J against A; 10,000 adults: G10 against B10 (20 years, headline) and J against A (40 years).
- Q8 synergy with the layer: the study programme's Shapley values and 11 contrasts on the factorial whose 16 cells with PTF
  come from G (or G10) and whose 15 cells without PTF and none row come from B (or B10); and each estimate minus its value
  with the layer off (B or B10), paired.
- Q9 design parameters: each row of study H minus the main-value row (G's release row with the layer; for the four `zc` cells,
  G's same cell with the layer), paired; and whether any decision under the addendum's rule 1 or the programme's rule 1 differs.
- Q10 PTF starting size: the layer's effect at a starting share of 10%, 30% and 50% (study I) beside the environment's own (G
  against B), and the differences between shares.
- Scale (addendum rule 5, the programme's rule 3): J and G10 against G, independent runs.
- 95% intervals: paired bootstrap over seeds, 10,000 replicates, percentile, bootstrap seed 20261101. One resample of seed
  indices per population size (500, then 2,000, then 10,000 adults, from one generator), shared by every study at that size,
  so every comparison between studies at one size is paired on the same resample (the addendum's Analysis). Between sizes the
  runs are independent and the difference's interval comes from the two bootstraps.
"""
import csv, math, os, sys
from itertools import combinations
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import batch_load  # noqa: E402

SRC, OUT = sys.argv[1], sys.argv[2]
ENG = 'ce8d030'
PARTS = 'CFHZI'
PNAME = {'C': 'CCO', 'F': 'PTF', 'H': 'PTH', 'Z': 'SZH', 'I': 'CIP'}
ENVS = [('ref', 'Reference'), ('adv', 'Adverse'), ('st', 'Stress')]
DESIGNS = [('c22', 'C2.2 design'), ('rls', 'release design')]
NB, BSEED, NS = 10000, 20261101, 500

O20 = [('BLEI<30 neutral', 'bNAPy', 'red', 0), ('BLEI<30 own (not claimed)', 'bOAPy', 'red', 0),
       ('below cost of living', 'fgt0PY', 'red', 0), ('wealth<25k y20', 'ppov_19', 'red', 0), ('cost $', 'cost', 'diff', 0),
       ('inflation to y20, cumulative %', 'plv_19', 'infl', 0), ('inflation to y20, yearly rate', 'plv_19', 'iyr', 20)]
O40 = [('BLEI<30 neutral', 'bNAPy', 'red', 0), ('BLEI<30 own (not claimed)', 'bOAPy', 'red', 0),
       ('below cost of living', 'fgt0PY', 'red', 0), ('wealth<25k y40', 'ppov_39', 'red', 0), ('cost $', 'cost', 'diff', 0),
       ('inflation to y40, cumulative %', 'plv_39', 'infl', 0), ('inflation to y40, yearly rate', 'plv_39', 'iyr', 40)]
OUTS = {20: O20, 40: O40}
# secondary outcomes (programme Outcomes): (label, key, kind, scale)
SEC = [('Gini disposable income x100', 'giniD', 100), ('Gini wealth x100', 'eGiniW', 100), ('children below cost of living', 'hhCostKidPY', 1),
       ('hours vs full time, %', 'hrs', 100), ('below official poverty line', 'hhFplPY', 1), ('FGT2 x100', 'fgt2PY', 100)]
DIAG = ['clN', 'clZ', 'clSd', 'clHi', 'clTh', 'pfMem', 'pfCut']


def oid(o):
    return o[1] + ('.yr' if o[2] == 'iyr' else '')


def claimable(o):
    return o[1] != 'bOAPy' and o[2] != 'infl'


# ---------------------------------------------------------------- load
def load(study):
    rows, meta = batch_load.load(os.path.join(SRC, 'prog-%s-%s' % (study, ENG)))
    assert not meta['_problems'], (study, meta['_problems'])
    assert meta['seedList'] == list(range(1, NS + 1)), study
    return rows


D = {s: load(s) for s in ('g', 'g10', 'h', 'i', 'j', 'a', 'b', 'b10')}
CHECKS = []


def chk(ok, text):
    CHECKS.append(('PASS' if ok else 'FAIL') + '  ' + text)
    if not ok:
        print('FAIL', text, file=sys.stderr)


def R(study, e, n, y, d, yard, row):
    return D[study]['%s.n%d.y%d.%s.%s.%s' % (e, n, y, d, yard, row)]


def same(a, b, skip=()):
    return all(np.array_equal(x, b[k], equal_nan=True) for k, x in a.items() if k not in skip and k in b) and set(a) == set(b)


# row counts (addendum Amendment 1: G 36, G10 32, H 18, I 12, J 4 per environment, both designs; per horizon for G, H, I)
cnt = {s: len(D[s]) // 3 for s in ('g', 'g10', 'h', 'i', 'j')}
chk(cnt == {'g': 72, 'g10': 32, 'h': 36, 'i': 24, 'j': 8},
    'rows per environment: G %(g)d (36 x 2 horizons), G10 %(g10)d, H %(h)d (18 x 2), I %(i)d (12 x 2), J %(j)d (4 x 2 sizes)' % cnt)

# G10's release row and J's release row at 10,000 adults, 20 years, are the same row on the same seeds
bad = sum(not same(R('g10', e, 10000, 20, d, 'cps', 'main.lay'), R('j', e, 10000, 20, d, 'cps', 'main.lay')) for e, _ in ENVS for d, _ in DESIGNS)
chk(bad == 0, 'G10 and J: the release row with the layer at 10,000 adults, 20 years, is identical in both studies, every key and seed (6 rows): %d differ' % bad)
# B10's release and none rows equal study A's at 10,000 adults (the layer-off rows the headline compares with)
bad = sum(not same(R('b10', e, 10000, 20, d, 'cps', r), R('a', e, 10000, 20, d, 'cps', r)) for e, _ in ENVS for d, _ in DESIGNS for r in ('main', 'none'))
chk(bad == 0, 'B10 against A: the release and none rows at 10,000 adults, 20 years, CPS, are identical, every key and seed (12 rows): %d differ' % bad)
# 40-year rows' year-20 measures equal the 20-year rows'
bad = n = 0
for s in ('g', 'h', 'i', 'j'):
    for r in D[s]:
        if '.y40.' not in r:
            continue
        for k in ('ppov_19', 'plv_19', 'pbO_19', 'pf0_19'):
            n += 1
            bad += not np.array_equal(D[s][r][k], D[s][r.replace('.y40.', '.y20.')][k])
chk(bad == 0, 'G, H, I, J: in every 40-year row the year-20 measures equal the 20-year row, seed by seed: %d of %d differ' % (bad, n))
# cells without the CCO are the same rows under the two designs (G, G10, H)
C22_ONLY = ('c22PY', 'c22R', 'buPY', 'elN', 'elF0', 'elW', 'elRes')
bad = n = 0
for s in ('g', 'g10', 'h'):
    for r in D[s]:
        p = r.split('.')
        if p[3] != 'c22' or p[5][0] != 'c':
            continue
        n += 1
        bad += not same(D[s][r], D[s]['.'.join(p[:3] + ['rls'] + p[4:])], C22_ONLY)
chk(n > 0 and bad == 0, 'G, G10, H: the %d rows without the CCO are identical under the two designs (but the C2.2 reporting keys): %d differ' % (n, bad))
# the layer's own count of communities is adults / 100 (k = 100), / 50 or / 250 in H's k rows
bad = 0
for s in ('g', 'g10', 'i', 'j'):
    for r, v in D[s].items():
        if r.endswith('.lay'):
            bad += not np.all(v['clN'] == int(r.split('.')[1][1:]) / 100)
for r, v in D['h'].items():
    k = 50 if r.endswith('.k50') else 250 if r.endswith('.k250') else 100
    bad += not np.all(v['clN'] == int(r.split('.')[1][1:]) // k)
chk(bad == 0, 'every row with the layer has adults / k communities on every seed (5 at 500 adults, 20 at 2,000, 100 at 10,000; k 50 and 250 in H): %d rows differ' % bad)

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
    """addendum rule 1 (and the programme's rule 1 when th is None): material +/-, stated +/-, or not stated."""
    if not t.ex0:
        return 'not stated'
    if th is not None and abs(t.m) >= th:
        return 'material ' + sign(t)
    return 'stated ' + sign(t)


# ---------------------------------------------------------------- Q7: layer effect on the release row
# settings: (label, n, y, design, env, yard, raise, layer-on row getter, layer-off row getter, none getter)
Q7 = []
for d, _ in DESIGNS:
    for e, _ in ENVS:
        for y in (20, 40):
            for yard, rz in (('cps', False), ('cps', True), ('rel', False)):
                rn = 'main.raise' if rz else 'main'
                Q7.append(dict(n=500, y=y, d=d, e=e, yard=yard, rz=rz, on=R('g', e, 500, y, d, yard, rn + '.lay'),
                               off=R('b', e, 500, y, d, yard, rn), none=R('b', e, 500, y, d, yard, 'none'), src='G vs B'))
        for y in (20, 40):
            Q7.append(dict(n=2000, y=y, d=d, e=e, yard='cps', rz=False, on=R('j', e, 2000, y, d, 'cps', 'main.lay'),
                           off=R('a', e, 2000, y, d, 'cps', 'main'), none=R('a', e, 2000, y, d, 'cps', 'none'), src='J vs A'))
        Q7.append(dict(n=10000, y=20, d=d, e=e, yard='cps', rz=False, on=R('g10', e, 10000, 20, d, 'cps', 'main.lay'),
                       off=R('b10', e, 10000, 20, d, 'cps', 'main'), none=R('b10', e, 10000, 20, d, 'cps', 'none'), src='G10 vs B10'))
        Q7.append(dict(n=10000, y=40, d=d, e=e, yard='cps', rz=False, on=R('j', e, 10000, 40, d, 'cps', 'main.lay'),
                       off=R('a', e, 10000, 40, d, 'cps', 'main'), none=R('a', e, 10000, 40, d, 'cps', 'none'), src='J vs A'))


def q7name(s):
    return '%s, %s, %s adults, %d years, %s%s' % (dict(DESIGNS)[s['d']], dict(ENVS)[s['e']], '{:,}'.format(s['n']), s['y'],
                                                 'CPS' if s['yard'] == 'cps' else 'released wages', ', raise on' if s['rz'] else '')


def q7key(s):
    return 'n%d.y%d.%s.%s.%s.%s' % (s['n'], s['y'], s['d'], s['e'], s['yard'], 'raise' if s['rz'] else 'off')


for s in Q7:
    s['res'] = {}
    cost_ref = float((s['off']['cost'] - s['none']['cost']).mean())
    claim = [o for o in OUTS[s['y']] if claimable(o)]
    for o in OUTS[s['y']]:
        lay = E(eff(s['on'], s['off'], o), s['n'])
        won = E(eff(s['on'], s['none'], o), s['n'])
        woff = E(eff(s['off'], s['none'], o), s['n'])
        th = thr(o, cost_ref)
        s['res'][oid(o)] = dict(o=o, lay=lay, on=won, off=woff, th=th, d1=dec1(lay, th), pon=dec1(won, None), poff=dec1(woff, None))
    hp = holm([s['res'][oid(o)]['lay'].p for o in claim])
    for o, h in zip(claim, hp):
        s['res'][oid(o)]['h'] = h
    for o in OUTS[s['y']]:
        r = s['res'][oid(o)]
        mat = r['d1'].startswith('material')
        csvrow('Q7 layer effect', q7key(s), oid(o), 'layer effect (on - off)', r['lay'], r['lay'].ex0, mat, r.get('h'))
        csvrow('Q7 layer effect', q7key(s), oid(o), 'effect with layer (vs none)', r['on'])
        csvrow('Q7 layer effect', q7key(s), oid(o), 'effect without layer (vs none)', r['off'])
    for lab, key, sc in SEC:
        t = E((s['on'][key] - s['off'][key]) * sc, s['n'])
        s['res']['sec.' + key] = t
        csvrow('Q7 layer effect, secondary', q7key(s), key, 'layer effect (on - off)', t, t.ex0)


def fl7(r):
    return ('†' if r['lay'].ex0 else '') + ('M' if r['d1'].startswith('material') else '') + ('H' if r.get('h') else '')


def q7table(sel, outs_filter=None):
    out('| Setting | Outcome | Layer effect (with − without) | Flags | Effect without layer | Effect with layer | Programme rule 1 (without / with) |')
    out('|---|---|---|---|---|---|---|')
    for s in sel:
        for o in OUTS[s['y']]:
            if o[2] == 'infl':
                continue
            r = s['res'][oid(o)]
            pr = r['poff'] + ' / ' + r['pon']
            out('| %s | %s | %s | %s | %s | %s | %s |' % (q7name(s), o[0], fe(r['lay'], dgt(o)), fl7(r), fe(r['off'], dgt(o)),
                                                       fe(r['on'], dgt(o)), pr if r['poff'] == r['pon'] else '**' + pr + '**'))
    out('')


# ---------------------------------------------------------------- Q8: factorial with the layer
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
        k = bin(m).count('1')
        w = math.factorial(k) * math.factorial(4 - k) / math.factorial(5)
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
IX = {n: k for k, n in enumerate(NAMES)}
CONTR = ['contrast whole design'] + ['contrast ' + p for p in PAIRN]
SHAP = ['shapley ' + PNAME[ch] for ch in PARTS]
chk(np.allclose(MAP[1:6, 1:].sum(0), MAP[0, 1:]), 'Shapley values add up to v(all five), as linear maps')


def cellname(m):
    if m == 0:
        return 'none'
    if m == 31:
        return 'main'
    return ''.join(ch if m & (1 << i) else ch.lower() for i, ch in enumerate(PARTS))


Q8 = []
for d, _ in DESIGNS:
    for e, _ in ENVS:
        for y in (20, 40):
            Q8.append(dict(n=500, y=y, d=d, e=e, on='g', off='b'))
        Q8.append(dict(n=10000, y=20, d=d, e=e, on='g10', off='b10'))


def q8name(s):
    return '%s, %s, %s adults, %d years' % (dict(DESIGNS)[s['d']], dict(ENVS)[s['e']], '{:,}'.format(s['n']), s['y'])


def vmat(s, o, layer):
    N = R(s['off'], s['e'], s['n'], s['y'], s['d'], 'cps', 'none')
    V = np.zeros((32, NS))
    for m in range(1, 32):
        if layer and m & 2:
            row = R(s['on'], s['e'], s['n'], s['y'], s['d'], 'cps', cellname(m) + '.lay')
        else:
            row = R(s['off'], s['e'], s['n'], s['y'], s['d'], 'cps', cellname(m))
        V[m] = eff(row, N, o)
    return V


def status(t, th):
    if t.ex0 and th is not None and abs(t.m) >= th:
        return 'material ' + sign(t)
    return 'detected, below materiality' if t.ex0 else 'not detected'


for s in Q8:
    s['res'] = {}
    key = 'n%d.y%d.%s.%s' % (s['n'], s['y'], s['d'], s['e'])
    for o in OUTS[s['y']]:
        Yon = MAP @ vmat(s, o, True)
        Yoff = MAP @ vmat(s, o, False)
        on = {nm: E(Yon[k], s['n']) for nm, k in IX.items()}
        off = {nm: E(Yoff[k], s['n']) for nm, k in IX.items()}
        dl = {nm: E(Yon[k] - Yoff[k], s['n']) for nm, k in IX.items()}
        th_on = thr(o, on['v(all five)'].m); th_off = thr(o, off['v(all five)'].m)
        hp_on = holm([on[nm].p for nm in CONTR]); hp_off = holm([off[nm].p for nm in CONTR])
        hon = dict(zip(CONTR, hp_on)); hoff = dict(zip(CONTR, hp_off))
        st_on = {nm: status(on[nm], th_on) for nm in CONTR}
        st_off = {nm: status(off[nm], th_off) for nm in CONTR}
        s['res'][oid(o)] = dict(o=o, Yon=Yon, on=on, off=off, dl=dl, th=th_on, hon=hon, hoff=hoff, st_on=st_on, st_off=st_off)
        for nm in NAMES:
            csvrow('Q8 synergy with layer', key, oid(o), nm + ' (layer on)', on[nm], on[nm].ex0 if nm in CONTR else None,
                   st_on[nm].startswith('material') if nm in CONTR else None, hon.get(nm))
            csvrow('Q8 synergy with layer', key, oid(o), nm + ' (layer off)', off[nm])
            csvrow('Q8 synergy with layer', key, oid(o), nm + ' (on - off)', dl[nm], dl[nm].ex0)
mx = max(float(np.abs(r['Yon'][1:6].sum(0) - r['Yon'][0]).max() / max(1.0, np.abs(r['Yon'][0]).max())) for s in Q8 for r in s['res'].values())
chk(mx < 1e-9, 'per seed, in every setting and outcome, the Shapley values with the layer add up to v(all five) (largest relative gap %.1e)' % mx)
# the layer factorial's full cell is Q7's release row with the layer
bad = sum(not np.array_equal(s8['res']['fgt0PY']['on']['v(all five)'].x,
                             next(s7 for s7 in Q7 if (s7['n'], s7['y'], s7['d'], s7['e'], s7['yard'], s7['rz']) == (s8['n'], s8['y'], s8['d'], s8['e'], 'cps', False))['res']['fgt0PY']['on'].x)
          for s8 in Q8)
chk(bad == 0, 'the factorial\'s full cell with the layer is the release row with the layer of Q7, seed by seed (18 settings): %d differ' % bad)


def flag8(r, nm, on=True):
    t = r['on' if on else 'off'][nm]
    st = (r['st_on'] if on else r['st_off'])[nm]
    h = (r['hon'] if on else r['hoff'])[nm]
    return ('†' if t.ex0 else '') + ('M' if st.startswith('material') else '') + ('H' if h else '')


def q8block(s):
    out('#### %s' % q8name(s))
    out('')
    out('Shapley values with the layer, and their change from the layer off (Δ, paired):')
    out('')
    out('| Outcome | v(all five) | ' + ' | '.join(PNAME[ch] for ch in PARTS) + ' |')
    out('|---|---|' + '---|' * 5)
    for o in OUTS[s['y']]:
        if o[2] == 'infl':
            continue
        r = s['res'][oid(o)]
        cells = ['%s; Δ %s' % (fe(r['on'][nm], dgt(o)), fe(r['dl'][nm], dgt(o))) for nm in ['v(all five)'] + SHAP]
        out('| %s | %s |' % (o[0], ' | '.join(cells)))
    out('')
    out('Interaction contrasts with the layer (flags), and Δ from the layer off:')
    out('')
    out('| Outcome | ' + ' | '.join(n.replace('contrast ', '') for n in CONTR) + ' |')
    out('|---|' + '---|' * len(CONTR))
    for o in OUTS[s['y']]:
        if o[2] == 'infl':
            continue
        r = s['res'][oid(o)]
        cells = []
        for nm in CONTR:
            fl = flag8(r, nm)
            cells.append('%s%s; Δ %s' % (fe(r['on'][nm], dgt(o)), ' ' + fl if fl else '', fe(r['dl'][nm], dgt(o))))
        out('| %s | %s |' % (o[0], ' | '.join(cells)))
    out('')


# ---------------------------------------------------------------- Q9: design parameters (study H)
HROWS = [('main.f67', 'f 2/3', 'main.lay', 'main'), ('main.f100', 'f 1', 'main.lay', 'main'), ('main.k50', 'k 50', 'main.lay', 'main'),
         ('main.k250', 'k 250', 'main.lay', 'main'), ('main.pop', 'imitation population-wide', 'main.lay', 'main')]
HROWS += [(cl + '.zc', cl + ' zones need CIP', cl + '.lay', cl) for cl in ('CFHZi', 'CFhZi', 'cFHZi', 'cFhZi')]
Q9 = []
for d, _ in DESIGNS:
    for e, _ in ENVS:
        for y in (20, 40):
            s = dict(d=d, e=e, y=y, res={})
            none = R('b', e, 500, y, d, 'cps', 'none')
            cost_ref = float((R('b', e, 500, y, d, 'cps', 'main')['cost'] - none['cost']).mean())
            for o in OUTS[y]:
                if o[2] == 'infl':
                    continue
                th = thr(o, cost_ref)
                rr = []
                for hr, lab, ref, offr in HROWS:
                    h = R('h', e, 500, y, d, 'cps', hr); g = R('g', e, 500, y, d, 'cps', ref); b = R('b', e, 500, y, d, 'cps', offr)
                    vs = E(eff(h, g, o), 500)
                    lay_h, lay_g = E(eff(h, b, o), 500), E(eff(g, b, o), 500)
                    pe_h, pe_g = E(eff(h, none, o), 500), E(eff(g, none, o), 500)
                    rr.append(dict(row=hr, lab=lab, vs=vs, d1h=dec1(lay_h, th), d1g=dec1(lay_g, th), p1h=dec1(pe_h, None), p1g=dec1(pe_g, None),
                                   lay_h=lay_h, pe_h=pe_h))
                hp = holm([x['vs'].p for x in rr])
                for x, hh in zip(rr, hp):
                    x['h'] = hh
                    csvrow('Q9 design parameters', 'n500.y%d.%s.%s' % (y, d, e), oid(o), x['lab'] + ': row - main-value row', x['vs'], x['vs'].ex0, None, hh)
                    csvrow('Q9 design parameters', 'n500.y%d.%s.%s' % (y, d, e), oid(o), x['lab'] + ': layer effect', x['lay_h'], x['lay_h'].ex0)
                s['res'][oid(o)] = dict(o=o, rows=rr)
            Q9.append(s)

# ---------------------------------------------------------------- Q10: PTF starting size (study I)
Q10 = []
for d, _ in DESIGNS:
    for e, _ in ENVS:
        for y in (20, 40):
            s = dict(d=d, e=e, y=y, res={})
            for o in OUTS[y]:
                if o[2] == 'infl':
                    continue
                X = {}
                for sh in ('s10', 's30', 's50'):
                    X[sh] = eff(R('i', e, 500, y, d, 'cps', 'main.%s.lay' % sh), R('i', e, 500, y, d, 'cps', 'main.%s.off' % sh), o)
                X['own'] = eff(R('g', e, 500, y, d, 'cps', 'main.lay'), R('b', e, 500, y, d, 'cps', 'main'), o)
                ests = {k: E(v, 500) for k, v in X.items()}
                hp = dict(zip(('s10', 's30', 's50'), holm([ests[k].p for k in ('s10', 's30', 's50')])))
                diffs = {}
                for a_, b_ in (('s10', 's30'), ('s10', 's50'), ('s30', 's50')):
                    t = E(X[a_] - X[b_], 500)
                    th = 1.0 if o[2] != 'diff' else 0.05 * abs(float((R('b', e, 500, y, d, 'cps', 'main')['cost'] - R('b', e, 500, y, d, 'cps', 'none')['cost']).mean()))
                    diffs[a_ + '-' + b_] = (t, t.ex0 and abs(t.m) >= th)
                    csvrow('Q10 PTF starting size', 'n500.y%d.%s.%s' % (y, d, e), oid(o), 'layer effect %s minus %s' % (a_, b_), t, t.ex0, diffs[a_ + '-' + b_][1])
                for k, t in ests.items():
                    csvrow('Q10 PTF starting size', 'n500.y%d.%s.%s' % (y, d, e), oid(o), 'layer effect at ' + k, t, t.ex0, None, hp.get(k))
                s['res'][oid(o)] = dict(o=o, ests=ests, hp=hp, diffs=diffs)
            Q10.append(s)

# ---------------------------------------------------------------- tables.md
out('# Community-layer report (S38): tables')
out('')
out('Full study batch: studies G, G10, H, I and J (the community layer), compared with studies A, B and B10 (the same rows without the'
    ' layer, and the no-programme rows), seeds 1-500, engine `%s`, the frozen engine on every row. Generated by'
    ' `python3 dev/tools/s38_layer.py <compassionism-sim-results checkout> dev/runs/s38-layer` from BetterToBest/compassionism-sim-results'
    ' `prog-{g,g10,h,i,j,a,b,b10}-%s`. Every interval is a 95%% paired-bootstrap interval over seeds (10,000 replicates); comparisons'
    ' between population sizes are independent runs. For the three shares a reduction is a positive number of points, so a positive'
    ' layer effect means the layer helps; for cost and inflation positive means more cost or more inflation. Flags: † interval excludes'
    ' zero; M also material (1 point; 5%% of the release row\'s cost, or the full design\'s cost for contrasts; 1 point of the yearly'
    ' inflation rate); H survives Holm in its preregistered family. Every estimate is also in `estimates.csv`.' % (ENG, ENG))
out('')
out('## 0. Checks')
out('')
CHK_AT = len(L)
out('')

HEAD = [s for s in Q7 if (s['n'], s['y'], s['e'], s['yard'], s['rz']) == (10000, 20, 'ref', 'cps', False)]
out('## 1. The headline cell (Q7): Reference, 10,000 adults, 20 years, CPS yardstick, raise off')
out('')
out('The release row with the layer against the release row without it (paired, same seeds), C2.2 design (headline) and release design.'
    ' Holm over the five claimable primary outcomes. Bold: the programme\'s rule 1 decision differs with the layer.')
out('')
q7table(HEAD)
out('Secondary outcomes, the layer\'s effect (with − without), headline cell:')
out('')
out('| Design | ' + ' | '.join(l for l, _, _ in SEC) + ' |')
out('|---|' + '---|' * len(SEC))
for s in HEAD:
    out('| %s | %s |' % (dict(DESIGNS)[s['d']], ' | '.join(fe(s['res']['sec.' + k]) for _, k, _ in SEC)))
out('')

out('## 2. The layer\'s effect in every setting (Q7)')
out('')
nst = nmat = 0
for d, dn in DESIGNS:
    out('### %s' % dn)
    out('')
    q7table([s for s in Q7 if s['d'] == d and s not in HEAD])
out('Summary of the addendum\'s rule 1 over every setting (claimable outcomes):')
out('')
out('| Design | Size | Settings | Outcome-settings | Interval excludes zero | Material | Programme rule 1 decision differs |')
out('|---|---|---|---|---|---|---|')
for d, dn in DESIGNS:
    for n in (500, 2000, 10000):
        sel = [s for s in Q7 if s['d'] == d and s['n'] == n]
        rs = [s['res'][oid(o)] for s in sel for o in OUTS[s['y']] if claimable(o)]
        out('| %s | %s | %d | %d | %d | %d | %d |' % (dn, '{:,}'.format(n), len(sel), len(rs), sum(r['lay'].ex0 for r in rs),
                                                    sum(r['d1'].startswith('material') for r in rs), sum(r['poff'] != r['pon'] for r in rs)))
out('')
out('Every material layer effect (claimable outcomes):')
out('')
out('| Setting | Outcome | Layer effect | Flags | Without | With |')
out('|---|---|---|---|---|---|')
for s in Q7:
    for o in OUTS[s['y']]:
        r = s['res'][oid(o)]
        if claimable(o) and r['d1'].startswith('material'):
            out('| %s | %s | %s | %s | %s | %s |' % (q7name(s), o[0], fe(r['lay'], dgt(o)), fl7(r), fe(r['off'], dgt(o)), fe(r['on'], dgt(o))))
out('')

out('## 3. Synergy with the layer (Q8)')
out('')
out('The study programme\'s Shapley values and interaction contrasts on the factorial with the layer on: the 16 cells with PTF from'
    ' G (500 adults) or G10 (10,000 adults), the 15 cells without PTF and the none row from B or B10 (identical with the layer on,'
    ' addendum check 2). CPS yardstick, raise off. Δ is the estimate with the layer minus the estimate with the layer off (B or B10),'
    ' paired. The pairs the layer is built to test are PTF × SZH and CIP × SZH. Headline: G10 at 10,000 adults (20 years).')
out('')
out('### 3a. Every decision under rule 2 that differs with the layer')
out('')
out('| Setting | Outcome | Contrast | Layer off | Layer on | Δ | Decision off / on |')
out('|---|---|---|---|---|---|---|')
nd = nall = 0
for s in Q8:
    for o in OUTS[s['y']]:
        if not claimable(o):
            continue
        r = s['res'][oid(o)]
        for nm in CONTR:
            nall += 1
            if r['st_on'][nm] != r['st_off'][nm]:
                nd += 1
                out('| %s | %s | %s | %s | %s | %s | %s / %s |' % (q8name(s), o[0], nm.replace('contrast ', ''), fe(r['off'][nm], dgt(o)),
                                                               fe(r['on'][nm], dgt(o)), fe(r['dl'][nm], dgt(o)), r['st_off'][nm], r['st_on'][nm]))
out('')
out('%d of %d claimable contrasts change decision under rule 2 when the layer is switched on.' % (nd, nall))
out('')
Q8SUM = (nd, nall)
out('### 3b. The tested pairs (PTF × SZH, CIP × SZH) and every Δ whose interval excludes zero')
out('')
out('| Setting | Outcome | Estimate | Layer off | Layer on | Δ (on − off) |')
out('|---|---|---|---|---|---|')
ndl = ndlall = 0
for s in Q8:
    for o in OUTS[s['y']]:
        if not claimable(o):
            continue
        r = s['res'][oid(o)]
        for nm in CONTR + SHAP + ['v(all five)']:
            ndlall += 1
            t = r['dl'][nm]
            ndl += t.ex0
            if t.ex0 or nm in ('contrast PTF x SZH', 'contrast SZH x CIP'):
                out('| %s | %s | %s | %s | %s | %s%s |' % (q8name(s), o[0], nm.replace('contrast ', ''), fe(r['off'][nm], dgt(o)),
                                                        fe(r['on'][nm], dgt(o)), fe(t, dgt(o)), ' †' if t.ex0 else ''))
out('')
out('%d of %d changes (contrasts, Shapley values and the full effect, claimable outcomes) have an interval excluding zero.' % (ndl, ndlall))
out('')
Q8DL = (ndl, ndlall)
out('### 3c. Every setting in full')
out('')
for s in sorted(Q8, key=lambda s: (s['n'] != 10000, s['d'] != 'c22')):
    q8block(s)

out('## 4. Design parameters (Q9, study H)')
out('')
out('Each swept row minus the main-value row (k 100, f 0.5, local imitation, zones without CIP), paired, 500 adults, CPS, raise off.'
    ' For the four `zc` rows the main-value row is the same cell with the layer at its main values (G). Holm over the nine rows of'
    ' each outcome. "Decision differs" lists any outcome whose decision under the addendum\'s rule 1 (the layer\'s effect: row against'
    ' the same row without the layer) or the programme\'s rule 1 (row against none) differs from the main-value row.')
out('')
DIFF9 = []
for s in Q9:
    out('#### %s, %s, %d years' % (dict(DESIGNS)[s['d']], dict(ENVS)[s['e']], s['y']))
    out('')
    out('| Row | ' + ' | '.join(r['o'][0] for r in s['res'].values()) + ' | Decision differs |')
    out('|---|' + '---|' * (len(s['res']) + 1))
    for k, (hr, lab, _, _) in enumerate(HROWS):
        cells, dd = [], []
        for r in s['res'].values():
            x = r['rows'][k]; o = r['o']
            fl = ('†' if x['vs'].ex0 else '') + ('H' if x['h'] else '')
            cells.append(fe(x['vs'], dgt(o)) + (' ' + fl if fl else ''))
            if claimable(o):
                if x['d1h'] != x['d1g']:
                    dd.append('%s layer: %s → %s' % (o[0], x['d1g'], x['d1h']))
                    DIFF9.append((s, lab, o[0], 'layer rule 1', x['d1g'], x['d1h']))
                if x['p1h'] != x['p1g']:
                    dd.append('%s programme: %s → %s' % (o[0], x['p1g'], x['p1h']))
                    DIFF9.append((s, lab, o[0], 'programme rule 1', x['p1g'], x['p1h']))
        out('| %s | %s | %s |' % (lab, ' | '.join(cells), '; '.join(dd) if dd else 'none'))
    out('')

out('Summary by swept row (addendum rule 3): how many outcome-settings (claimable outcomes; 3 environments x 2 horizons x 2 designs)'
    ' have a decision that differs from the main-value row, and whether any of them involves a material layer effect.')
out('')
out('| Row | Layer rule 1 differs | Programme rule 1 differs | Any involving "material" |')
out('|---|---|---|---|')
for hr, lab, _, _ in HROWS:
    xs = [x for x in DIFF9 if x[1] == lab]
    out('| %s | %d | %d | %s |' % (lab, sum(x[3] == 'layer rule 1' for x in xs), sum(x[3] == 'programme rule 1' for x in xs),
                                   'yes' if any('material' in x[4] + x[5] for x in xs) else 'no'))
out('')
nmat9 = sum(x['lay_h'].ex0 and dec1(x['lay_h'], thr(r['o'], float((R('b', s['e'], 500, s['y'], s['d'], 'cps', 'main')['cost'] - R('b', s['e'], 500, s['y'], s['d'], 'cps', 'none')['cost']).mean()))).startswith('material')
            for s in Q9 for r in s['res'].values() if claimable(r['o']) for x in r['rows'])
out('Material layer effects among all study H rows (claimable outcomes): %d.' % nmat9)
out('')

out('## 5. PTF starting size (Q10, study I)')
out('')
out('The layer\'s effect (with − without, paired) at a PTF starting share of 10%, 30% and 50%, beside the environment\'s own share'
    ' (18% in Reference and Adverse, 8% in Stress; G against B). Holm over the three shares. Rule 4: the layer\'s effect depends on the'
    ' starting share only where a difference between two shares has an interval excluding zero and is at least 1 point (5% of the'
    ' release row\'s cost for cost).')
out('')
out('| Setting | Outcome | Own share | 10% | 30% | 50% | 10% − 30% | 10% − 50% | 30% − 50% |')
out('|---|---|---|---|---|---|---|---|---|')
DEP10 = []
for s in Q10:
    for r in s['res'].values():
        o = r['o']
        es, hp = r['ests'], r['hp']
        cells = [fe(es['own'], dgt(o))] + [fe(es[k], dgt(o)) + (' †' if es[k].ex0 else '') + ('H' if hp[k] else '') for k in ('s10', 's30', 's50')]
        dc = []
        for k, (t, ok) in r['diffs'].items():
            dc.append(fe(t, dgt(o)) + (' †' if t.ex0 else '') + (' **depends**' if ok and claimable(o) else ''))
            if ok and claimable(o):
                DEP10.append((s, o[0], k, t))
        out('| %s, %s, %d y | %s | %s | %s |' % (dict(DESIGNS)[s['d']], dict(ENVS)[s['e']], s['y'], o[0], ' | '.join(cells), ' | '.join(dc)))
out('')
out('%d outcome-settings meet rule 4 (claimable outcomes).' % len(DEP10))
out('')

out('## 6. Scale (addendum rule 5; the programme\'s rule 3)')
out('')
out('Independent runs. A difference passes where |Δ| exceeds both the half-width of its interval and the materiality threshold'
    ' (1 point; 5% of the 500-adult value for cost). Rows: the release row with the layer, its effect against none and the layer\'s'
    ' effect, at 2,000 and 10,000 adults against 500 (J and G10 against G); and the synergy table with the layer, G10 against G'
    ' (20 years), contrast by contrast. Listed: every Δ that passes, and the layer\'s effect on every claimable outcome.')
out('')
out('| Setting (larger size) | Outcome | Estimate | 500 adults | Larger | Δ | Passes |')
out('|---|---|---|---|---|---|---|')
nsc = nscall = 0
for s in Q7:
    if s['n'] == 500:
        continue
    a = next(x for x in Q7 if (x['n'], x['y'], x['d'], x['e'], x['yard'], x['rz']) == (500, s['y'], s['d'], s['e'], 'cps', False))
    for o in OUTS[s['y']]:
        if not claimable(o):
            continue
        ra, rb = a['res'][oid(o)], s['res'][oid(o)]
        th = 1.0 if o[2] != 'diff' else 0.05 * abs(ra['on'].m)
        for nm, lab in (('lay', 'layer effect'), ('on', 'effect with layer')):
            t = E(ra[nm].x, 500, rb[nm].x, s['n'])
            thx = th if not (o[2] == 'diff' and nm == 'lay') else 0.05 * abs(ra['off'].m)
            ok = abs(t.m) > (t.hi - t.lo) / 2 and abs(t.m) > thx
            nscall += 1; nsc += ok
            csvrow('scale', q7key(s), oid(o), lab + ' delta vs 500', t, ok)
            if ok or nm == 'lay':
                out('| %s | %s | %s | %s | %s | %s | %s |' % (q7name(s), o[0], lab, fe(ra[nm], dgt(o)), fe(rb[nm], dgt(o)), fe(t, dgt(o)), 'yes' if ok else 'no'))
for s in Q8:
    if s['n'] != 10000:
        continue
    a = next(x for x in Q8 if (x['n'], x['y'], x['d'], x['e']) == (500, 20, s['d'], s['e']))
    for o in OUTS[20]:
        if not claimable(o):
            continue
        ra, rb = a['res'][oid(o)], s['res'][oid(o)]
        th = 1.0 if o[2] != 'diff' else 0.05 * abs(ra['on']['v(all five)'].m)
        for nm in CONTR + SHAP:
            t = E(ra['on'][nm].x, 500, rb['on'][nm].x, 10000)
            ok = abs(t.m) > (t.hi - t.lo) / 2 and abs(t.m) > th
            nscall += 1; nsc += ok
            csvrow('scale', 'synergy n10000.y20.%s.%s' % (s['d'], s['e']), oid(o), nm + ' (layer on) delta vs 500', t, ok)
            if ok:
                out('| %s | %s | %s | %s | %s | %s | yes |' % (q8name(s), o[0], nm, fe(ra['on'][nm], dgt(o)), fe(rb['on'][nm], dgt(o)), fe(t, dgt(o))))
out('')
out('%d of %d comparisons pass the scale rule.' % (nsc, nscall))
out('')
SCALE = (nsc, nscall)

out('## 7. The layer\'s diagnostics')
out('')
out('Means over seeds (2.5th-97.5th percentile over seeds in brackets). clN communities; clZ zones at the start; clSd how much the PTF'
    ' member share varies between communities (points); clHi % of members living where the share is at least 40%; clTh the same where'
    ' θ is above zero; pfMem PTF members, % of adults, mean over years; pfCut members\' average price cut (%). For comparison, pfMem and'
    ' pfCut are written only on rows with the layer (the job reports them there; the layer-off rows carry the PTF without its per-community reading).')
out('')


def pq(x):
    if x is None or not np.any(np.isfinite(x)):
        return 'not reported'
    return '%s (%s-%s)' % (f(float(np.nanmean(x)), 1), f(float(np.nanpercentile(x, 2.5)), 1), f(float(np.nanpercentile(x, 97.5)), 1))


out('| Row | ' + ' | '.join(DIAG) + ' |')
out('|---|' + '---|' * len(DIAG))
for d, dn in DESIGNS:
    for e, en in ENVS:
        for st, n, y, row, offst, offrow in (('g', 500, 20, 'main.lay', 'b', 'main'), ('g', 500, 40, 'main.lay', 'b', 'main'),
                                             ('j', 2000, 20, 'main.lay', 'a', 'main'), ('g10', 10000, 20, 'main.lay', 'b10', 'main'),
                                             ('j', 10000, 40, 'main.lay', 'a', 'main')):
            v = R(st, e, n, y, d, 'cps', row)
            out('| %s, %s, %s adults, %d y, release row | %s |' % (dn, en, '{:,}'.format(n), y, ' | '.join(pq(v.get(k)) for k in DIAG)))
out('')
out('Study H and I rows (20 years; Reference, C2.2 design shown; every environment and design in estimates.csv):')
out('')
out('| Row | ' + ' | '.join(DIAG) + ' |')
out('|---|' + '---|' * len(DIAG))
for hr, lab, _, _ in HROWS:
    v = R('h', 'ref', 500, 20, 'c22', 'cps', hr)
    out('| H: %s | %s |' % (lab, ' | '.join(pq(v.get(k)) for k in DIAG)))
for sh in ('s10', 's30', 's50'):
    for lo in ('lay', 'off'):
        v = R('i', 'ref', 500, 20, 'c22', 'cps', 'main.%s.%s' % (sh, lo))
        out('| I: PTF start %s%%, layer %s | %s |' % (sh[1:], 'on' if lo == 'lay' else 'off', ' | '.join(pq(v.get(k)) for k in DIAG)))
out('')
for st in ('g', 'g10', 'h', 'i', 'j'):
    for r, v in D[st].items():
        for k in DIAG:
            if k in v and np.any(np.isfinite(v[k])):
                CSV.append(['diagnostics', st + ':' + r, k, 'mean over seeds', '%.6g' % float(np.nanmean(v[k])), '%.6g' % float(np.nanpercentile(v[k], 2.5)),
                            '%.6g' % float(np.nanpercentile(v[k], 97.5)), '', '', ''])

# ---------------------------------------------------------------- write
L[CHK_AT:CHK_AT] = ['- ' + x for x in CHECKS]
SUMMARY = dict(q8=Q8SUM, q8dl=Q8DL, scale=SCALE, q9diff=len(DIFF9), q9mat=nmat9, q10dep=len(DEP10))
L.append('## 8. Counts')
L.append('')
L.append('```')
L.append(repr(SUMMARY))
L.append('```')
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, 'tables.md'), 'w') as fh:
    fh.write('\n'.join(L) + '\n')
with open(os.path.join(OUT, 'estimates.csv'), 'w', newline='') as fh:
    wr = csv.writer(fh)
    wr.writerow(['section', 'setting', 'outcome', 'estimate', 'mean', 'lo95', 'hi95', 'excludes_zero', 'material', 'holm'])
    wr.writerows(CSV)
print('\n'.join(CHECKS))
print(SUMMARY, len(CSV), 'estimates')
