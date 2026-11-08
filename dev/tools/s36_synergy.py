#!/usr/bin/env python3
"""S36 synergy report: every table of dev/reports/s36-synergy.md, from the full study batch (studies B and B10).

Usage: python3 dev/tools/s36_synergy.py <compassionism-sim-results checkout> <out dir>
Reads prog-b-ce8d030 and prog-b10-ce8d030 (through batch_load.py) and writes <out dir>/tables.md (every table) and
<out dir>/estimates.csv (every estimate with its interval, every setting).

Method (research-update prereg/2026-11-study-program.md, Analysis and decision rules 2, 3, 6 and 7, with Amendments 4, 9
and 10; prereg/run-manifest.md section 3, B and B10):
- The players are the five parts CCO, PTF, PTH, SZH, CIP. v(S) is the per-seed effect of the cell with exactly the parts in
  S on, against the none row of the same environment, size, horizon, yardstick, design and seed; v(empty) = 0.
- Shapley values phi_i = sum over S not containing i of |S|! (4 - |S|)! / 5! [v(S + i) - v(S)]; shares phi_i / v(all five),
  only where v(all five)'s interval excludes zero.
- Contrasts: (a) whole design v(all) - sum_i v({i}); (b) the 10 pairs within the design, v(all) - v(all - i) - v(all - j) +
  v(all - i - j); (c, secondary) the 26 Harsanyi dividends and the 10 two-way contrasts averaged over the other three parts.
- 95% intervals: paired bootstrap over seeds, 10,000 replicates, percentile, bootstrap seed 20261101; one resample of seed
  indices per study (B first, then B10, from one generator), shared by every row of that study. B10 against B (Q1) compares
  independent runs: the difference's interval comes from the two bootstraps.
- Decision rule 2: a synergy is claimed only where the interval excludes zero (dagger); material (M) if also at least 1 point
  (shares), 5% of the full design's cost, or 1 point of the yearly inflation rate implied by the price level (Amendment 9,
  item 5: cumulative inflation is reported as preregistered, the threshold is read on (pLev)^(1/T) - 1); H = survives Holm
  over the 11 contrasts (a) and (b) of that outcome and setting. BLEI synergies are claimed on the design-neutral reading
  only; the design's own reading is shown, not claimed.
- Every setting: 3 environments x 20 and 40 years x 2 yardsticks x raise off and on x 2 designs (B, 500 adults); 3 environments
  x 2 designs (B10, 10,000 adults, 20 years, CPS, raise off). The raise is a setting of the CCO: cells without CCO have it off.
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
YARDS = [('cps', 'CPS yardstick'), ('rel', 'released-wage yardstick')]
NB, BSEED = 10000, 20261101
NS = 500

# outcomes: (short label, key, kind, horizon for the yearly rate). kind: red = reduction in points (positive is better),
# diff = row minus none ($), infl = points of cumulative inflation, iyr = points of the yearly rate implied by the price level
O20 = [('BLEI<30 neutral', 'bNAPy', 'red', 0), ('BLEI<30 own (not claimed)', 'bOAPy', 'red', 0),
       ('below cost of living', 'fgt0PY', 'red', 0), ('wealth<25k y20', 'ppov_19', 'red', 0), ('cost $', 'cost', 'diff', 0),
       ('inflation to y20, cumulative %', 'plv_19', 'infl', 0), ('inflation to y20, yearly rate', 'plv_19', 'iyr', 20)]
# a 40-year run's first 20 years equal the 20-year run (checked below), so its year-20 points are left to the 20-year tables
O40 = [('BLEI<30 neutral', 'bNAPy', 'red', 0), ('BLEI<30 own (not claimed)', 'bOAPy', 'red', 0),
       ('below cost of living', 'fgt0PY', 'red', 0), ('wealth<25k y40', 'ppov_39', 'red', 0), ('cost $', 'cost', 'diff', 0),
       ('inflation to y40, cumulative %', 'plv_39', 'infl', 0), ('inflation to y40, yearly rate', 'plv_39', 'iyr', 40)]
OUTS = {20: O20, 40: O40}
SHARE_KEYS = ('bNAPy', 'fgt0PY', 'ppov_19', 'ppov_39')


def oid(o):
    return o[1] + ('.yr' if o[2] == 'iyr' else '')


def claimable(o):
    """outcomes a synergy may be claimed on: design-neutral BLEI, cost of living, wealth, cost, the yearly inflation rate."""
    return o[1] != 'bOAPy' and o[2] != 'infl'


# ---------------------------------------------------------------- load and check
def load(study):
    rows, meta = batch_load.load(os.path.join(SRC, 'prog-%s-%s' % (study, ENG)))
    assert not meta['_problems'], meta['_problems']
    assert meta['seedList'] == list(range(1, NS + 1)), study
    return rows, meta


B_ALL, BMETA = load('b')
B10_ALL, B10META = load('b10')
CHECKS = []


def chk(ok, text):
    CHECKS.append(('PASS' if ok else 'FAIL') + '  ' + text)
    if not ok:
        print('FAIL', text, file=sys.stderr)


def cell(mask):
    return ''.join(ch if mask & (1 << i) else ch.lower() for i, ch in enumerate(PARTS))


def rowname(mask, raise_):
    if mask == 0:
        return 'none'
    return ('main' if mask == 31 else cell(mask)) + ('.raise' if raise_ and mask & 1 else '')


C22_ONLY = ('c22PY', 'c22R', 'buPY', 'elN', 'elF0', 'elW', 'elRes')
# check: cells without CCO (and none) are the same rows under the two designs (manifest section 3, B and B10)
for nm, R in (('B', B_ALL), ('B10', B10_ALL)):
    bad = n = 0
    for r in R:
        p = r.split('.')
        if p[3] != 'c22':
            continue
        last = p[5]
        if last != 'none' and (last[0] == 'C' or last.startswith('main')):
            continue
        o = '.'.join(p[:3] + ['rls'] + p[4:])
        n += 1
        for k, x in R[r].items():
            if k in C22_ONLY:
                continue
            if not np.array_equal(x, R[o][k], equal_nan=True):
                bad += 1
                break
    chk(bad == 0, '%s: the none row and the %d rows without CCO are identical under the two designs (every key but the C2.2 design\'s'
        ' own reporting keys, null on the release design; every seed): %d differ' % (nm, n, bad))

# check: the 40-year rows' year-20 measures equal the 20-year rows' (study programme Amendment 9, item 4)
bad = n = 0
for r in B_ALL:
    if '.y40.' not in r:
        continue
    r20 = r.replace('.y40.', '.y20.')
    for k in ('ppov_19', 'plv_19', 'pbO_19', 'pf0_19'):
        n += 1
        if not np.array_equal(B_ALL[r][k], B_ALL[r20][k]):
            bad += 1
chk(bad == 0, 'B: in all %d 40-year rows, the year-20 measures (wealth, price level, BLEI and cost-of-living shares at year 20) '
    'equal the 20-year rows seed by seed: %d of %d differ' % (sum('.y40.' in r for r in B_ALL), bad, n))

# check (when prog-a is in the checkout): B's full-design and no-programme rows are study A's rows at 500 adults, seed by seed
AF = os.path.join(SRC, 'prog-a-%s' % ENG)
if os.path.isdir(AF):
    A_ALL, _ = batch_load.load(AF)
    bad = n = 0
    for r in A_ALL:
        if '.n500.' not in r or r not in B_ALL:
            continue
        n += 1
        for k, x in A_ALL[r].items():
            if not np.array_equal(x, B_ALL[r][k], equal_nan=True):
                bad += 1
                break
    chk(n == 72 and bad == 0, 'B against study A: the %d rows at 500 adults that both hold (none, full design, raise on; both designs,'
        ' yardsticks, horizons, environments) are identical, every key and seed: %d differ' % (n, bad))
    del A_ALL
else:
    CHECKS.append('SKIP  B against study A (prog-a-%s not in the checkout)' % ENG)

B = {d: batch_load.by_design(B_ALL, d) for d, _ in DESIGNS}
B10 = {d: batch_load.by_design(B10_ALL, d) for d, _ in DESIGNS}
chk(all(len(B[d]) == 576 for d in B) and all(len(B10[d]) == 96 for d in B10),
    'rows per design: B %s (576 = 96 per environment and horizon x 3 x 2), B10 %s (96 = 32 x 3)'
    % ('/'.join(str(len(B[d])) for d in B), '/'.join(str(len(B10[d])) for d in B10)))

# ---------------------------------------------------------------- bootstrap
rng = np.random.default_rng(BSEED)


def resample():
    idx = rng.integers(0, NS, size=(NB, NS))
    W = np.zeros((NB, NS))
    np.add.at(W, (np.repeat(np.arange(NB), NS), idx.ravel()), 1.0 / NS)
    return W


W = {'B': resample(), 'B10': resample()}

# ---------------------------------------------------------------- linear maps from v(S) (32 x seeds) to every estimate
NAMES, ROWS_ = [], []


def add(name, coef):
    NAMES.append(name)
    ROWS_.append(coef)


z = lambda: np.zeros(32)
c = z(); c[31] = 1; add('v(all five)', c)
for i in range(5):
    c = z()
    for m in range(32):
        if m & (1 << i):
            continue
        s = bin(m).count('1')
        w = math.factorial(s) * math.factorial(4 - s) / math.factorial(5)
        c[m | (1 << i)] += w
        c[m] -= w
    add('shapley ' + PNAME[PARTS[i]], c)
for i in range(5):
    c = z(); c[1 << i] = 1; add('alone ' + PNAME[PARTS[i]], c)
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
DIVS = [t for t in range(32) if bin(t).count('1') >= 2]
DIVN = ['+'.join(PNAME[PARTS[i]] for i in range(5) if t & (1 << i)) for t in DIVS]
for t, dn in zip(DIVS, DIVN):
    c = z()
    for s in range(32):
        if s & ~t:
            continue
        c[s] += (-1) ** (bin(t).count('1') - bin(s).count('1'))
    add('dividend ' + dn, c)
for (i, j), pn in zip(PAIRS, PAIRN):
    bi, bj = 1 << i, 1 << j
    c = z()
    others = [m for m in range(32) if not m & (bi | bj)]
    for m in others:
        c[m | bi | bj] += 1 / 8; c[m | bi] -= 1 / 8; c[m | bj] -= 1 / 8; c[m] += 1 / 8
    add('two-way avg ' + pn, c)
MAP = np.array(ROWS_)
IX = {n: k for k, n in enumerate(NAMES)}
CONTR = ['contrast whole design'] + ['contrast ' + p for p in PAIRN]   # the Holm family (a) + (b)

# checks of the maps on the identities they must satisfy
chk(np.allclose(MAP[1:6, 1:].sum(0), MAP[0, 1:]), 'Shapley values add up to v(all five) (efficiency), as linear maps')
chk(np.allclose(MAP[[IX['dividend ' + d] for d in DIVN], 1:].sum(0) + MAP[6:11, 1:].sum(0), MAP[0, 1:]),
    'the 26 dividends plus the five single-part effects add up to v(all five)')
chk(np.allclose(MAP[IX['contrast whole design'], 1:], MAP[[IX['dividend ' + d] for d in DIVN], 1:].sum(0)),
    'the whole-design contrast equals the sum of the 26 dividends')
# (column 0 is v(empty), which is 0 on every seed, so its coefficients do not count)


def eff(row, none, key, kind, T):
    if kind == 'red':
        return none[key] - row[key]
    if kind == 'infl':
        return (row[key] - none[key]) * 100
    if kind == 'iyr':
        return (row[key] ** (1.0 / T) - none[key] ** (1.0 / T)) * 100
    return row[key] - none[key]


def vmat(rows, p, o, raise_):
    N = rows[p + 'none']
    V = np.zeros((32, NS))
    for m in range(1, 32):
        V[m] = eff(rows[p + rowname(m, raise_)], N, o[1], o[2], o[3])
    return V


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


def thr(o, vfull):
    if o[2] == 'diff':
        return 0.05 * abs(vfull)
    if o[2] == 'infl':
        return None          # Amendment 9: materiality is read on the yearly rate (the iyr row)
    return 1.0


# ---------------------------------------------------------------- compute every setting
CSV = []
RES = {}     # setting -> outcome id -> dict(Y=per-seed estimates (n x seeds), est={name: (mean, lo, hi)}, flags, share)
SETTINGS = []
for d, _ in DESIGNS:
    for e, _ in ENVS:
        for y in (20, 40):
            for yd, _ in YARDS:
                for rz in (False, True):
                    SETTINGS.append(('B', d, e, y, yd, rz))
for d, _ in DESIGNS:
    for e, _ in ENVS:
        SETTINGS.append(('B10', d, e, 20, 'cps', False))


def prefix(st):
    s, d, e, y, yd, rz = st
    return '%s.n%d.y%d.%s.' % (e, 500 if s == 'B' else 10000, y, yd)


def sname(st):
    s, d, e, y, yd, rz = st
    return '%s.%s.%s.y%d.%s.%s' % (s, d, e, y, yd, 'raise' if rz else 'off')


for st in SETTINGS:
    s, d, e, y, yd, rz = st
    rows = (B if s == 'B' else B10)[d]
    Wm = W[s]
    RES[st] = {}
    for o in OUTS[y]:
        V = vmat(rows, prefix(st), o, rz)
        Y = MAP @ V                       # estimates x seeds
        Bt = Y @ Wm.T                     # estimates x replicates
        mean = Y.mean(1)
        lo = np.percentile(Bt, 2.5, axis=1); hi = np.percentile(Bt, 97.5, axis=1)
        est = {n: (float(mean[k]), float(lo[k]), float(hi[k])) for n, k in IX.items()}
        vt = est['v(all five)']
        ex0 = lambda t: t[1] > 0 or t[2] < 0
        share = {}
        if ex0(vt):
            vb = Bt[0]
            for i in range(5):
                n = 'shapley ' + PNAME[PARTS[i]]
                sb = Bt[IX[n]] / vb * 100
                share[n] = (est[n][0] / vt[0] * 100,) + pct(sb)
        hp = holm([bootp(Bt[IX[n]]) for n in CONTR])
        th = thr(o, vt[0])
        flags = {}
        for n in NAMES:
            if n.startswith(('contrast', 'dividend', 'two-way')):
                t = est[n]
                x = ex0(t)
                mat = x and th is not None and abs(t[0]) >= th
                h = hp[CONTR.index(n)] if n in CONTR else None
                flags[n] = (x, mat, h)
        med = float(np.median(Y[0])) if o[2] == 'iyr' else None
        RES[st][oid(o)] = dict(o=o, Y=Y, est=est, share=share, flags=flags, med=med)
        for n in NAMES:
            t = est[n]
            fl = flags.get(n)
            CSV.append([s, d, e, y, yd, 'raise on' if rz else 'raise off', oid(o), n, '%.6g' % t[0], '%.6g' % t[1], '%.6g' % t[2],
                        '' if fl is None else int(fl[0]), '' if fl is None else int(fl[1]), '' if fl is None or fl[2] is None else int(fl[2])])
        for n, t in share.items():
            CSV.append([s, d, e, y, yd, 'raise on' if rz else 'raise off', oid(o), n.replace('shapley', 'shapley share %'),
                        '%.6g' % t[0], '%.6g' % t[1], '%.6g' % t[2], '', '', ''])

# check: per seed, Shapley values add up to v(all five) and the full design's row is the 'main' row
mx = max(float(np.abs(r['Y'][1:6].sum(0) - r['Y'][0]).max() / max(1.0, np.abs(r['Y'][0]).max())) for st in RES for r in RES[st].values())
chk(mx < 1e-9, 'per seed, in every setting and outcome, the five Shapley values add up to v(all five) (largest relative gap %.1e)' % mx)

# ---------------------------------------------------------------- formatting
L = []


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


def fi(t, dg=2):
    return '%s [%s, %s]' % (f(t[0], dg), f(t[1], dg), f(t[2], dg))


def flagstr(fl):
    x, m, h = fl
    return ('†' if x else '') + ('M' if m else '') + ('H' if h else '')


def title(st):
    s, d, e, y, yd, rz = st
    return '%s, %s, %s adults, %d years, %s, raise %s' % (
        dict(DESIGNS)[d], dict(ENVS)[e], '500' if s == 'B' else '10,000', y, dict(YARDS)[yd], 'on' if rz else 'off')


def shapley_table(st):
    out('| Outcome | v(all five) | ' + ' | '.join(PNAME[ch] for ch in PARTS) + ' |')
    out('|---|---|' + '---|' * 5)
    for o in OUTS[st[3]]:
        r = RES[st][oid(o)]
        cells = []
        for ch in PARTS:
            n = 'shapley ' + PNAME[ch]
            sh = r['share'].get(n)
            cells.append(fi(r['est'][n], dgt(o)) + ('; %s%%' % f(sh[0], 0) if sh else ''))
        v = fi(r['est']['v(all five)'], dgt(o)) + (' (median %s)' % f(r['med']) if r['med'] is not None else '')
        out('| %s | %s | %s |' % (o[0], v, ' | '.join(cells)))
    out('')


def contrast_table(st):
    out('| Outcome | ' + ' | '.join(n.replace('contrast ', '') for n in CONTR) + ' |')
    out('|---|' + '---|' * len(CONTR))
    for o in OUTS[st[3]]:
        r = RES[st][oid(o)]
        cells = []
        for n in CONTR:
            fs = flagstr(r['flags'][n])
            cells.append(fi(r['est'][n], dgt(o)) + (' ' + fs if fs else ''))
        out('| %s | %s |' % (o[0], ' | '.join(cells)))
    out('')


def setting_block(st, level='###'):
    out('%s %s' % (level, title(st)))
    out('')
    out('Shapley values, and shares of the full effect in % where v(all five) excludes zero:')
    out('')
    shapley_table(st)
    out('Interaction contrasts (a) and (b):')
    out('')
    contrast_table(st)


def secondary_block(st):
    out('#### Secondary: the 26 Harsanyi dividends and the two-way contrasts averaged over the other three parts')
    out('')
    os_ = [o for o in OUTS[st[3]] if claimable(o)]
    out('| Term | ' + ' | '.join(o[0] for o in os_) + ' |')
    out('|---|' + '---|' * len(os_))
    for n in ['dividend ' + dn for dn in DIVN] + ['two-way avg ' + p for p in PAIRN]:
        cells = []
        for o in os_:
            r = RES[st][oid(o)]
            fs = flagstr(r['flags'][n])
            cells.append(fi(r['est'][n], dgt(o)) + (' ' + fs if fs else ''))
        out('| %s | %s |' % (n.replace('dividend ', 'd(').replace('two-way avg ', 'avg ') + (')' if n.startswith('dividend') else ''), ' | '.join(cells)))
    out('')


# ---------------------------------------------------------------- tables.md
out('# Synergy report (S36): tables')
out('')
out('Full study batch: studies B (500 adults) and B10 (10,000 adults), seeds 1-500, engine `%s`, the frozen engine on every row.'
    ' Generated by `python3 dev/tools/s36_synergy.py <compassionism-sim-results checkout> dev/runs/s36-synergy` from'
    ' BetterToBest/compassionism-sim-results `prog-b-%s` and `prog-b10-%s`. Every interval is a 95%% paired-bootstrap interval'
    ' over seeds (10,000 replicates). v(S) is the effect of the cell with the parts in S on, against no programme; for the share'
    ' outcomes a reduction is a positive number of percentage points, so a positive contrast is synergy (the parts together'
    ' cut the share by more than their separate effects add up to). For cost, a positive contrast means the parts together'
    ' cost more than separately. For inflation, positive means more inflation together. Flags: † interval excludes zero;'
    ' M also material (1 point; 5%% of the full design\'s cost; 1 point of the yearly inflation rate); H survives Holm over'
    ' the 11 contrasts of its row. Cumulative inflation compounds, so its contrasts are not judged material (Amendment 9);'
    ' the yearly-rate row is. The design\'s own BLEI is shown, never claimed. Every estimate is also in `estimates.csv`.'
    % (ENG, ENG, ENG))
out('')
out('## 0. Checks')
out('')
CHK_AT = len(L)
out('')

HEAD = [('B', d, 'ref', 20, 'cps', False) for d, _ in DESIGNS]
out('## 1. The headline cell, in full')
out('')
out('Reference, 500 adults, 20 years, CPS yardstick, raise off (the cell that heads the preregistered report), on the'
    ' C2.2 design (headline, Amendment 4) and the release design beside it.')
out('')
for st in HEAD:
    setting_block(st)
    out('Each part alone (v of the one-part cell):')
    out('')
    out('| Outcome | ' + ' | '.join(PNAME[ch] for ch in PARTS) + ' |')
    out('|---|' + '---|' * 5)
    for o in OUTS[20]:
        r = RES[st][oid(o)]
        out('| %s | %s |' % (o[0], ' | '.join(fi(r['est']['alone ' + PNAME[ch]], dgt(o)) for ch in PARTS)))
    out('')
    secondary_block(st)

out('## 2. Every setting of study B (500 adults)')
out('')
for st in SETTINGS:
    if st[0] == 'B' and st not in HEAD:
        setting_block(st)

out('## 3. Study B10 (10,000 adults, 20 years, CPS yardstick, raise off)')
out('')
for st in SETTINGS:
    if st[0] == 'B10':
        setting_block(st)


# ---------------------------------------------------------------- comparisons
def status(st, n, k):
    r = RES[st][k]
    x, m, _ = r['flags'][n]
    t = r['est'][n][0]
    if m:
        return 'material +' if t > 0 else 'material -'
    if x:
        return 'detected, below materiality'
    return 'not detected'


def compare(pairs, label):
    """pairs: list of (setting a, setting b, paired). Counts every contrast whose decision under rule 2 differs (claimed or not;
    material or not, by sign) and lists those where a material synergy is gained, lost or changes sign; Delta = b - a."""
    out('| Setting (a) | Outcome | Contrast | (a) | (b) | Delta (b - a) | Decision (a) / (b) |')
    out('|---|---|---|---|---|---|---|')
    nd = nm = nall = 0
    for a, b_, paired in pairs:
        for o in OUTS[a[3]]:
            if not claimable(o):
                continue
            k = oid(o)
            ra, rb = RES[a][k], RES[b_][k]
            for n in CONTR:
                nall += 1
                sa, sb = status(a, n, k), status(b_, n, k)
                if sa == sb:
                    continue
                nd += 1
                i = IX[n]
                if paired:
                    bd = (rb['Y'][i] - ra['Y'][i]) @ W[a[0]].T
                else:
                    bd = rb['Y'][i] @ W[b_[0]].T - ra['Y'][i] @ W[a[0]].T
                dl = (rb['est'][n][0] - ra['est'][n][0],) + pct(bd)
                CSV.append([label, a[1], a[2], a[3], a[4], 'raise on' if a[5] else 'raise off', k, n + ' delta', '%.6g' % dl[0],
                            '%.6g' % dl[1], '%.6g' % dl[2], '', '', ''])
                if sa.startswith('material') or sb.startswith('material'):
                    nm += 1
                    out('| %s | %s | %s | %s | %s | %s | %s / %s |' % (sname(a), o[0], n.replace('contrast ', ''), fi(ra['est'][n], dgt(o)),
                                                                   fi(rb['est'][n], dgt(o)), fi(dl, dgt(o)), sa, sb))
    out('')
    out('%d of %d claimable contrasts change decision under rule 2; %d of them gain, lose or change the sign of a material synergy'
        ' (listed). The other %d move between "not detected" and "detected, below materiality"; their differences are in estimates.csv.'
        % (nd, nall, nm, nd - nm))
    out('')
    return nm, nd, nall


SUM = {}
out('## 4. Octave raise on against off (Q5, decision rule 6)')
out('')
out('Paired (same seeds). (a) is raise off, (b) raise on.')
out('')
SUM['raise'] = compare([(st, st[:5] + (True,), True) for st in SETTINGS if st[0] == 'B' and not st[5]], 'raise')

out('## 5. Yardstick: released wages against CPS earnings (Q6, decision rule 7)')
out('')
out('Paired. (a) is the CPS yardstick (headline), (b) the released-wage yardstick.')
out('')
SUM['yard'] = compare([(st, st[:4] + ('rel', st[5]), True) for st in SETTINGS if st[0] == 'B' and st[4] == 'cps'], 'yardstick')

out('## 6. Design: the release design against the C2.2 design')
out('')
out('Paired (the same seeds and none row). (a) is the C2.2 design (headline), (b) the release design.')
out('')
SUM['design'] = compare([(st, (st[0], 'rls') + st[2:], True) for st in SETTINGS if st[1] == 'c22'], 'design')

out('## 7. Scale: 10,000 adults against 500 (Q1, decision rule 3, contrast by contrast)')
out('')
out('Independent runs. A difference passes the scale rule where |Delta| exceeds both its Monte Carlo error (the half-width of its'
    ' interval) and the materiality threshold (1 point; 5% of the 500-adult full cost; 1 point of the yearly inflation rate).'
    ' Shapley values are compared by the same rule. Listed: every Delta that passes, and the whole-design contrast of every outcome.')
out('')
out('| Design | Environment | Outcome | Estimate | 500 adults | 10,000 adults | Delta | Passes |')
out('|---|---|---|---|---|---|---|---|')
nsc = nscall = 0
for d, _ in DESIGNS:
    for e, en in ENVS:
        a = ('B', d, e, 20, 'cps', False); b_ = ('B10', d, e, 20, 'cps', False)
        for o in O20:
            if not claimable(o):
                continue
            k = oid(o)
            ra, rb = RES[a][k], RES[b_][k]
            th = thr(o, ra['est']['v(all five)'][0])
            for n in CONTR + ['shapley ' + PNAME[ch] for ch in PARTS] + ['v(all five)']:
                i = IX[n]
                bd = rb['Y'][i] @ W['B10'].T - ra['Y'][i] @ W['B'].T
                lo, hi = pct(bd)
                dl = rb['est'][n][0] - ra['est'][n][0]
                ok = abs(dl) > (hi - lo) / 2 and abs(dl) > th
                nscall += 1; nsc += ok
                CSV.append(['B10-B', d, e, 20, 'cps', 'raise off', k, n + ' delta', '%.6g' % dl, '%.6g' % lo, '%.6g' % hi, int(ok), '', ''])
                if ok or n == 'contrast whole design':
                    out('| %s | %s | %s | %s | %s | %s | %s | %s |' % (dict(DESIGNS)[d], en, o[0], n.replace('contrast ', ''),
                        fi(ra['est'][n], dgt(o)), fi(rb['est'][n], dgt(o)), fi((dl, lo, hi), dgt(o)), 'yes' if ok else 'no'))
out('')
out('%d of %d comparisons (contrasts, Shapley values and the full effect, claimable outcomes) pass the scale rule.' % (nsc, nscall))
out('')
SUM['scale'] = (nsc, nscall)

out('## 8. Horizon: year 40 against year 20 in the 40-year runs (Q3, decision rule 4)')
out('')
out('Paired, within the same 40-year rows (their first 20 years equal the 20-year rows, check 0). For wealth below $25,000 and the'
    ' yearly inflation rate: the year-40 contrast minus the year-20 contrast. A change is stated only where its interval excludes'
    ' zero and it is at least 1 point. Without ageing only (study B has no ageing; rule 4 asks for study C too, which has no'
    ' factorial, so any 40-year synergy statement holds without ageing only). Listed: changes that pass, and the whole-design contrast.')
out('')
out('| Setting | Outcome | Contrast | Year 20 | Year 40 | Change | Passes |')
out('|---|---|---|---|---|---|---|')
nh = nhall = 0
for st in SETTINGS:
    if st[0] != 'B' or st[3] != 40:
        continue
    s20 = st[:3] + (20,) + st[4:]
    for k20, k40, lab in (('ppov_19', 'ppov_39', 'wealth<25k'), ('plv_19.yr', 'plv_39.yr', 'yearly inflation')):
        r20, r40 = RES[s20][k20], RES[st][k40]
        for n in CONTR:
            i = IX[n]
            dY = r40['Y'][i] - r20['Y'][i]
            lo, hi = pct(dY @ W['B'].T)
            dl = float(dY.mean())
            ok = (lo > 0 or hi < 0) and abs(dl) >= 1.0
            nhall += 1; nh += ok
            CSV.append(['horizon', st[1], st[2], 40, st[4], 'raise on' if st[5] else 'raise off', k40, n + ' y40-y20', '%.6g' % dl,
                        '%.6g' % lo, '%.6g' % hi, int(ok), '', ''])
            if ok or n == 'contrast whole design':
                out('| %s | %s | %s | %s | %s | %s | %s |' % (sname(st), lab, n.replace('contrast ', ''), fi(r20['est'][n]), fi(r40['est'][n]),
                                                         fi((dl, lo, hi)), 'yes' if ok else 'no'))
out('')
out('%d of %d horizon changes pass.' % (nh, nhall))
out('')
SUM['horizon'] = (nh, nhall)

out('## 9. Summary: how many contrasts pass, by outcome and sign')
out('')
out('Contrasts (a) and (b), every setting of the study, claimable outcomes. "Material" counts those with an interval excluding'
    ' zero and above the materiality threshold; "Holm" those of them that also survive Holm.')
out('')
out('| Study | Design | Outcome | Contrasts | Interval excludes zero | Material + | Material - | Material and Holm | Median half-width |')
out('|---|---|---|---|---|---|---|---|---|')
for s in ('B', 'B10'):
    for d, dn in DESIGNS:
        sts = [st for st in SETTINGS if st[0] == s and st[1] == d]
        groups = {}
        for st in sts:
            for k, r in RES[st].items():
                if not claimable(r['o']):
                    continue
                g = {'ppov_19': 'wealth (y20, y40)', 'ppov_39': 'wealth (y20, y40)', 'plv_19.yr': 'yearly inflation',
                     'plv_39.yr': 'yearly inflation'}.get(k, r['o'][0])
                for n in CONTR:
                    x, m, h = r['flags'][n]
                    t = r['est'][n]
                    G = groups.setdefault(g, [0, 0, 0, 0, 0, []])
                    G[0] += 1; G[1] += x; G[2] += m and t[0] > 0; G[3] += m and t[0] < 0; G[4] += m and h
                    G[5].append((t[2] - t[1]) / 2)
        for g, G in groups.items():
            out('| %s | %s | %s | %d | %d | %d | %d | %d | %s |' % (s, dn, g, G[0], G[1], G[2], G[3], G[4], f(float(np.median(G[5])), 0 if g == 'cost $' else 3)))
out('')
out('Material synergies gained, lost or changing sign (of all decision changes, of all contrasts): raise on against off %d (%d of %d);'
    ' released wages against CPS %d (%d of %d); release design against C2.2 %d (%d of %d). Passing the scale rule, 10,000 adults'
    ' against 500: %d of %d. Passing rule 4, year 40 against year 20: %d of %d.'
    % (SUM['raise'] + SUM['yard'] + SUM['design'] + SUM['scale'] + SUM['horizon']))
out('')

out('### Which interactions are material, and how often')
out('')
out('For each contrast: in how many of the 24 settings of study B (3 environments x 2 horizons x 2 yardsticks x raise off and on)'
    ' it is a material synergy (+) or a material overlap (-), by design. Wealth counts year 20 in 20-year runs and year 40 in'
    ' 40-year runs. Contrasts never material on any claimable outcome are left out. Signs as in the contrast tables: for the shares, +'
    ' is synergy (together they cut the share by more than the sum of their separate effects); for cost and inflation, + means'
    ' they cost or inflate more together, so - is the favourable direction.')
out('')
GRP = [('bNAPy', 'BLEI<30 neutral'), ('fgt0PY', 'below cost'), ('ppov', 'wealth<25k'), ('cost', 'cost $'), ('plv', 'yearly inflation')]
out('| Design | Contrast | ' + ' | '.join(g for _, g in GRP) + ' |')
out('|---|---|' + '---|' * len(GRP))
for d, dn in DESIGNS:
    for n in CONTR:
        cnt = []
        for gk, _ in GRP:
            pl = mi = 0
            for st in SETTINGS:
                if st[0] != 'B' or st[1] != d:
                    continue
                for k, r in RES[st].items():
                    if not claimable(r['o']) or not k.startswith(gk):
                        continue
                    x, m, h = r['flags'][n]
                    if m:
                        pl += r['est'][n][0] > 0; mi += r['est'][n][0] < 0
            cnt.append((pl, mi))
        if any(a or b for a, b in cnt):
            out('| %s | %s | %s |' % (dn, n.replace('contrast ', ''), ' | '.join('%d+ / %d-' % c for c in cnt)))
out('')

out('## 10. Every material synergy on a share outcome, design-neutral BLEI included')
out('')
out('Contrasts (a) and (b), every setting, material under rule 2. Sorted by setting.')
out('')
out('| Setting | Outcome | Contrast | Estimate | Holm |')
out('|---|---|---|---|---|')
for st in SETTINGS:
    for k in ('bNAPy', 'fgt0PY', 'ppov_19', 'ppov_39'):
        if k not in RES[st]:
            continue
        r = RES[st][k]
        for n in CONTR:
            x, m, h = r['flags'][n]
            if m:
                out('| %s | %s | %s | %s | %s |' % (sname(st), r['o'][0], n.replace('contrast ', ''), fi(r['est'][n]), 'yes' if h else 'no'))
out('')

out('## 11. Secondary terms for every environment (20 years, CPS yardstick, raise off, both designs)')
out('')
for d, _ in DESIGNS:
    for e, _ in ENVS:
        for s in ('B', 'B10'):
            st = (s, d, e, 20, 'cps', False)
            if st in HEAD:
                continue
            out('### %s' % title(st))
            out('')
            secondary_block(st)
out('The secondary terms of every other setting are in `estimates.csv`.')
out('')

L[CHK_AT:CHK_AT] = ['- ' + x for x in CHECKS]
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, 'tables.md'), 'w') as fh:
    fh.write('\n'.join(L) + '\n')
with open(os.path.join(OUT, 'estimates.csv'), 'w', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['study', 'design', 'env', 'years', 'yardstick', 'raise', 'outcome', 'estimate', 'mean', 'lo95', 'hi95',
                'excludes_zero', 'material', 'holm'])
    w.writerows(CSV)
print('\n'.join(CHECKS))
print('wrote %s/tables.md (%d lines) and estimates.csv (%d estimates)' % (OUT, len(L), len(CSV)))
sys.exit(1 if any(x.startswith('FAIL') for x in CHECKS) else 0)
