#!/usr/bin/env python3
"""S82 part 3 (Nov 18, 2026): the tables of the v6 batch, as research-update prereg/2026-11-s82-v6-supply-indexing.md fixes them (Outcomes,
Analysis, Checks, Decision rules; Amendments 1-4). Reads the six result folders s82-v6-<env>-<years>-eb0969c of compassionism-sim-results
(runner/jobs/s82.js at 4881a84; shard-NNNN.json, seeds 1-500 split across 20 shards) and writes Markdown tables and a summary JSON.

  python3 dev/tools/s82_tables.py RESULTS_DIR OUT_DIR [--engine eb0969c] [--reps 10000]

Method (fixed by the preregistration; where it is silent, the cautious reading, said so here and in the tables):
- Effect: the programme run minus its own no-programme run, paired by seed (seeds 1-500, common random numbers). The no-programme partner: base.none
  for the base, A, Achk, C, Slam, Sgrid and Th rows and for the factorial's AC cells; the B rows' own no-programme run (wages are on both runs) for
  B and for the factorial's AB, BC and ABC cells; each E reading's own no-programme run for E.
- "The change a reading makes" = the reading's effect minus the base effect at the same share, paired by seed. The reference is base.a<share>; for the
  Th part's limit rows it is the Th programme row at the same theta and share (Amendment 4: "the change the sourced limit makes against the base row
  at the same theta"); the Sgrid shares have no base row, so only their effects are read.
- Estimate: the mean over seeds; 95% interval: paired bootstrap, 10,000 replicates (seeds resampled), percentile; generator numpy default_rng(20261118),
  one resample shared by every row, key, environment and horizon (the seeds are the same everywhere), so intervals are comparable.
  p: two-sided paired t (499 degrees of freedom), for Holm only.
- Holm: across the primary readings within each question, environment, share and reading, for any statement that a reading "changes the effect". The
  preregistration says "the four primary outcomes"; outcomes 3 and 4 are each read two ways (wealth poverty yearly and at the last year; median real
  wealth weighted and unweighted), so Holm runs over the six readings, the cautious side. Unadjusted intervals are printed.
- Break-even backed shares (question 4's method, dev/tools/s64_tables.py): scanning down from 1, the share at which the effect is no better than no
  programme (favourable-signed effect <= 0), by linear interpolation between the grid points either side, with the bootstrap interval of the crossing;
  "above 1" when the full-backing point is already there; "below 0" when no grid point reaches it (never extrapolated). The same for programme inflation
  reaching 5 points a year. Under a supply reading the share-1 point is the main row: at full backing the unbacked excess is 0 and nothing is cut under
  any reading (check 3 tests it for the strict bound with every rule; for the sourced and restricted readings it follows from the same line,
  r = max(0, eu - ...) with eu = 0).
- Decision rule 2, "holds under a supply limit" (per share, per primary reading, never pooled): under the sourced reading with all three sharing rules
  the effect keeps the sign of the no-limit effect at that share and its 95% interval excludes zero. Rule 3: passes with the design's rule (bu) and
  fails with the market's (pay): "rests on how a shortage is shared". Amendment 3 + 4: the slowest building speed of medical care and food (grid 0,
  0.1, 0.25 = the sourced row, 0.5, 1) from which the test passes at that speed and every faster one; a pattern that passes and then fails at a
  faster speed is printed whole ("not steady in the building speed"). Amendment 4: the same test at half and double theta.
- Question 4: v(S) = per seed, the change made by the readings in S at that share and rule (S a subset of {A, B, C}; v(empty) = 0). Printed: each
  reading alone, the interactions as Harsanyi dividends (AB: v(AB) - v(A) - v(B); ABC: v(ABC) - v(AB) - v(AC) - v(BC) + v(A) + v(B) + v(C)), the joint
  change v(ABC), and the Shapley values (weights 1/3, 1/6, 1/3 on coalitions of size 0, 1, 2); Shapley shares of the joint change only where its
  interval excludes zero. An interaction is claimed only where its interval excludes zero (research rule 4; decision rule 7). At share 1 only B x C.
Standard library and numpy."""
import glob, hashlib, json, math, os, re, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s64_tables import tcdf, holm  # noqa: E402  (the same t distribution and Holm as round 2)

ENVS = ['ref', 'adv', 'str']; ENVL = {'ref': 'Reference', 'adv': 'Adverse', 'str': 'Stress'}
YEARS = [20, 40]
# (key, label, unit, sign of a favourable effect)
PRIM = [('fgt0PY', 'basket poverty', 'points', -1), ('bNAPy', 'below 30 days of basic living', 'points', -1),
        ('ppovA', 'wealth poverty, yearly average', 'points', -1), ('pov', 'wealth poverty, last year', 'points', -1),
        ('wtMedE', 'median real wealth, weighted', '$', 1), ('medWealthReal', 'median real wealth, unweighted', '$', 1)]
PK = [k for k, _, _, _ in PRIM]; LAB = {k: l for k, l, _, _ in PRIM}; FAV = {k: s for k, _, _, s in PRIM}
LAB.update({'endoAnn': 'programme inflation (points a year)', 'fgt2PY': 'poverty severity (FGT2)', 's82Wp50A': 'wealth poverty at half the no-programme median, yearly',
            's82Wp50': 'wealth poverty at half the no-programme median, last year', 's82Wp50Aw': 'the same, weighted, yearly', 's82B30w': 'below 30 days, weighted',
            'slF0p': 'basket poverty on what was paid for'})
FAV.update({'endoAnn': -1, 'fgt2PY': -1, 's82Wp50A': -1, 's82Wp50': -1, 's82Wp50Aw': -1, 's82B30w': -1, 'slF0p': -1})
SCALE = {'endoAnn': 100.0}
DIG = {'wtMedE': 0, 'medWealthReal': 0, 's82BuR20': 0, 's82BuRE': 0, 's82WgG20': 0, 's82WgGE': 0, 's82Mw0': 0}
SHARES = [0, 0.25, 0.5, 0.75, 1]; LOW = [0, 0.25, 0.5, 0.75]; FINE = [0.125, 0.375, 0.625, 0.875]
RD = ['sourced', 'restricted', 'strict']; SH = ['pay', 'even', 'bu']
RDL = {'sourced': 'sourced', 'restricted': 'restricted (today\'s land-use, residency and farm policies; a policy reading)',
       'strict': 'strict bound (no essentials beyond today\'s needs consumption; not the economy and not the design)'}
SHL = {'pay': 'market rule (least able to pay short first)', 'even': 'even rule', 'bu': 'design\'s rule (basics bought with BU first)'}
STRICT = 'the strictest case: no essentials beyond today\'s needs consumption; not the economy and not the design'
LAMS = [0, 0.1, 0.25, 0.5, 1]; WI = [0.5, 0.75]; WC = [0, 1]; LAGS = [0.125, 0.25, 1, 2]
LAGL = {0.125: 'monthly (0.125 years)', 0.25: 'quarterly (0.25)', 1: 'yearly (1)', 2: 'two years (2, a bound)'}
THN = ['half', 'double']; THL = {'half': 'half theta (housing 0.3, medical care 0.25)', 'double': 'double theta (housing 1.2, medical care 1.0)'}
EREAD = ['sc', 'tailLo', 'tailHi', 'p95', 'eb', 'age']
EL = {'sc': 'wage-only spending share 0.862 (theme 9)', 'tailLo': 'tail exponent 1.218 (minus two s.e.; theme 11)', 'tailHi': 'tail exponent 1.762 (plus two s.e.)',
      'p95': 'tail cut at the 95th percentile (theme 11)', 'eb': 'PTH equity base from the basket (theme 15)', 'age': 'ageing, AGE with lf.fl panel (theme 13)'}
REPS = 10000; W = None; NS = 500


def sa(a): return '%g' % a


# ---------------------------------------------------------------- loading and checks
def load(folder):
    files = sorted(glob.glob(os.path.join(folder, 'shard-*.json')))
    files = [f for f in files if not f.endswith('.timing.json')]
    if not files: sys.exit('no shard files in ' + folder)
    D = [json.load(open(f)) for f in files]
    D.sort(key=lambda d: d['_meta']['seeds'][0])
    s = 1
    for d in D:
        if d['_meta']['seeds'][0] != s: sys.exit('seed ranges not consecutive in ' + folder)
        s = d['_meta']['seeds'][1] + 1
    if s != NS + 1: sys.exit('seeds do not cover 1-500 in ' + folder)
    rows = {}
    for full in D[0]['rows']:
        name = full.split('.', 2)[2]
        rows[name] = {k: np.array([np.nan if x is None else x for d in D for x in d['rows'][full][k]], dtype=float) for k in D[0]['rows'][full]}
    meta = [d['_meta'] for d in D]
    return rows, meta


def sha_ok(folder):
    bad, n = [], 0
    for line in open(os.path.join(folder, 'SHA256SUMS')):
        h, f = line.split(None, 1); f = f.strip().lstrip('*'); n += 1
        with open(os.path.join(folder, f), 'rb') as fh:
            if hashlib.sha256(fh.read()).hexdigest() != h: bad.append(f)
    return n, bad


def partner(name):
    m = re.match(r'B\.(w[0-9.]+?)\.(c[01])\.', name)
    if m: return 'B.%s.%s.none' % m.groups()
    if re.match(r'X\.(AB|ABC|BC)\.', name): return 'B.w0.75.c1.none'
    if name.startswith('E.'): return 'E.%s.none' % name.split('.')[1]
    return 'base.none'


# ---------------------------------------------------------------- statistics
def est(d):
    if d is None: return None
    n = len(d); m = float(d.mean()); v = W @ d; sd = float(d.std(ddof=1))
    p = 1.0 if sd == 0 and m == 0 else 0.0 if sd == 0 else 2*(1 - tcdf(abs(m)/(sd/math.sqrt(n)), n - 1))
    lo, hi = np.percentile(v, [2.5, 97.5])
    return {'est': m, 'lo': float(lo), 'hi': float(hi), 'p': p, 'zero': bool(np.all(d == 0))}


def excl(s): return s['lo'] > 0 or s['hi'] < 0
def sgn(x): return 1 if x > 0 else -1 if x < 0 else 0
def fm(x, k=None, d=None):
    if x is None: return '–'
    d = DIG.get(k, 2) if d is None else d
    return ('{:,.%df}' % d).format(x) if abs(x) >= 1000 else ('%.' + str(d) + 'f') % x
def ci(s, k=None):
    if s is None: return '–'
    if s.get('zero'): return '0 (identical in every seed)'
    return '%s (%s to %s)' % (fm(s['est'], k), fm(s['lo'], k), fm(s['hi'], k))


def crossing_vec(a, V):
    """a: grid ascending (G); V: values (G x B), >= 0 means 'no better' (or 'reached'). Per column: scanning from the top down, the interpolated
    share where V reaches 0; np.inf for 'above 1' (the top point is already there), -np.inf for 'below 0' (no grid point reaches it)."""
    a = np.asarray(a, float); G, B = V.shape; out = np.full(B, -np.inf)
    top = V[-1] >= 0; out[top] = np.inf
    nn = V[:-1] >= 0                                       # (G-1, B)
    has = nn.any(axis=0) & ~top
    k = (G - 2) - np.argmax(nn[::-1], axis=0)              # highest index with V >= 0 below the top
    cols = np.where(has)[0]; kk = k[cols]
    v0, v1 = V[kk, cols], V[kk + 1, cols]
    out[cols] = a[kk] + (a[kk + 1] - a[kk])*v0/(v0 - v1)
    return out


def breakeven(a, D, k, off=0.0):
    """D: list of per-seed effect vectors on grid a; k the key (its favourable sign); off: the threshold (inflation 5)"""
    sgn_ = -FAV.get(k, -1) if off == 0 else 1.0
    M = np.array([sgn_*d.mean() - off for d in D])[:, None]
    Bm = np.array([sgn_*(W @ d) - off for d in D])
    c0 = crossing_vec(a, M)[0]; bs = crossing_vec(a, Bm); num = bs[np.isfinite(bs)]
    r = {'est': None if not np.isfinite(c0) else float(c0), 'word': 'above 1' if c0 == np.inf else 'below 0' if c0 == -np.inf else None,
         'lo': float(np.percentile(num, 2.5)) if len(num) else None, 'hi': float(np.percentile(num, 97.5)) if len(num) else None,
         'above1': float(np.mean(bs == np.inf)), 'below0': float(np.mean(bs == -np.inf))}
    return r


def be_str(r):
    s = r['word'] if r['word'] else '%.3f' % r['est']
    if r['lo'] is not None and (r['above1'] < 1 and r['below0'] < 1):
        s += ' (%.3f to %.3f' % (r['lo'], r['hi']) + ('; %.1f%% of replicates above 1' % (100*r['above1']) if r['above1'] > 0 else '') + \
             ('; %.1f%% below 0' % (100*r['below0']) if r['below0'] > 0 else '') + ')'
    elif r['word'] is None:
        s += ' (no interval)'
    return s


# ---------------------------------------------------------------- one folder
class Folder:
    def __init__(self, rows, e, y):
        self.R, self.e, self.y = rows, e, y

    def has(self, n): return n in self.R

    def eff(self, n, k):
        p = partner(n)
        if k not in self.R[n] or k not in self.R[p]: return None
        return (self.R[n][k] - self.R[p][k])*SCALE.get(k, 1.0)

    def lev(self, n, k):
        if k not in self.R[n]: return None
        return self.R[n][k]*SCALE.get(k, 1.0)

    def chg(self, n, ref, k):
        a, b = self.eff(n, k), self.eff(ref, k)
        return None if a is None or b is None else a - b


def holds(F, n, k, ref):
    """decision rule 2's test for one rule's row n against the no-limit row ref (same share): sign kept and interval excludes zero"""
    s = est(F.eff(n, k)); b = F.eff(ref, k).mean()
    return sgn(s['est']) == sgn(b) and sgn(b) != 0 and excl(s)


def analyse(F):
    e, y = F.e, F.y; S = {'env': e, 'years': y}
    # ---- the base curve
    S['base'] = {sa(a): {k: est(F.eff('base.a' + sa(a), k)) for k in PK + ['endoAnn', 'fgt2PY', 's82Wp50A', 's82Wp50', 's82Wp50Aw']} for a in SHARES}
    S['none'] = {k: est(F.lev('base.none', k)) for k in PK + ['fgt2PY', 's82U', 's82B30w', 's82Mw0']}
    for q in range(1, 6): S['none']['s82Uq%d' % q] = est(F.lev('base.none', 's82Uq%d' % q))

    def readrow(n, ref, keys=PK + ['endoAnn', 'fgt2PY']):
        keys = list(dict.fromkeys(PK + keys))  # the primary readings always (Holm runs over them)
        r = {'eff': {k: est(F.eff(n, k)) for k in keys}}
        if ref:
            ch = {k: est(F.chg(n, ref, k)) for k in keys}
            ad = holm([ch[k]['p'] for k in PK]); r['chg'] = ch; r['holm'] = {k: ad[i] for i, k in enumerate(PK)}
        return r

    # ---- Q1: the supply limit (A), with the limit's own keys
    SLK = ['slE', 'slEu', 'slRfood', 'slRhousing', 'slRmedical', 'slREfood', 'slREhousing', 'slREmedical', 'slCfood', 'slChousing', 'slCmedical', 'slX', 'slCutSh', 'slF0p']
    S['A'] = {}
    for rd in RD:
        for sh in SH:
            for a in LOW:
                n = 'A.%s.%s.a%s' % (rd, sh, sa(a)); r = readrow(n, 'base.a' + sa(a), PK + ['endoAnn', 'fgt2PY', 'slF0p'])
                r['sl'] = {k: est(F.lev(n, k)) for k in SLK}
                S['A'][n] = r
    # decision rules 2-3 at the sourced reading; Amendment 3's building speed; Amendment 4's theta
    def lamrow(l, sh, a): return 'A.sourced.%s.a%s' % (sh, sa(a)) if l == 0.25 else 'Slam.lam%s.%s.a%s' % (sa(l), sh, sa(a))
    S['DR'] = {}
    for a in LOW:
        for k in PK:
            ref = 'base.a' + sa(a); per = {sh: holds(F, 'A.sourced.%s.a%s' % (sh, sa(a)), k, ref) for sh in SH}
            lam = {sa(l): all(holds(F, lamrow(l, sh, a), k, ref) for sh in SH) for l in LAMS}
            seq = [lam[sa(l)] for l in LAMS]
            if not seq[-1]: slow = 'does not hold at any building speed on the grid'
            else:
                j = len(seq) - 1
                while j > 0 and seq[j - 1]: j -= 1
                steady = not any(seq[:j])  # passes at some slower speed below a failing one: not steady
                slow = ('holds at the strict bound for medical care and food (speed 0)' if j == 0 else 'from speed %s' % sa(LAMS[j])) + ('' if steady else '; not steady in the building speed: ' + ', '.join('%s %s' % (sa(l), 'pass' if lam[sa(l)] else 'fail') for l in LAMS))
            th = {}
            for tn in THN:
                tref = 'Th.%s.base.a%s' % (tn, sa(a))
                th[tn] = all(holds(F, 'Th.%s.sourced.%s.a%s' % (tn, sh, sa(a)), k, tref) for sh in SH)
            strict = {sh: holds(F, 'A.strict.%s.a%s' % (sh, sa(a)), k, ref) for sh in SH}
            restr = {sh: holds(F, 'A.restricted.%s.a%s' % (sh, sa(a)), k, ref) for sh in SH}
            base_ok = excl(est(F.eff(ref, k)))
            S['DR'][sa(a) + '.' + k] = {'a': a, 'k': k, 'baseExcl0': base_ok, 'rules': per, 'holds': all(per.values()),
                                        'restsOnRule': per['bu'] and not per['pay'], 'lam': lam, 'slowest': slow, 'theta': th, 'strict': strict, 'restricted': restr}
    # ---- Amendment 3: the building speed sweep (effects and changes from the sourced row)
    S['Slam'] = {}
    for l in [0, 0.1, 0.5, 1]:
        for sh in SH:
            for a in LOW:
                n = lamrow(l, sh, a); r = readrow(n, 'base.a' + sa(a), ['fgt0PY', 'endoAnn', 'fgt2PY'])
                r['vsSourced'] = est(F.eff(n, 'fgt0PY') - F.eff(lamrow(0.25, sh, a), 'fgt0PY'))
                r['sl'] = {k: est(F.lev(n, k)) for k in ['slX', 'slCutSh', 'slCmedical', 'slCfood', 'slChousing', 'slRmedical']}
                S['Slam'][n] = r
    # ---- Amendment 4: theta
    S['Th'] = {}
    for tn in THN:
        for a in SHARES:
            n = 'Th.%s.base.a%s' % (tn, sa(a)); S['Th'][n] = readrow(n, 'base.a' + sa(a), PK + ['endoAnn'])
        for sh in SH:
            for a in LOW:
                n = 'Th.%s.sourced.%s.a%s' % (tn, sh, sa(a)); S['Th'][n] = readrow(n, 'Th.%s.base.a%s' % (tn, sa(a)), PK + ['endoAnn'])
    # ---- break-even shares
    BE = {}
    def be_all(tag, names, grid):
        D = {k: [F.eff(n, k) for n in names] for k in PK + ['endoAnn']}
        BE[tag] = {k: breakeven(grid, D[k], k) for k in PK}
        BE[tag]['inflation5'] = breakeven(grid, D['endoAnn'], 'endoAnn', 5.0)
    be_all('base', ['base.a' + sa(a) for a in SHARES], SHARES)
    for rd in RD:
        for sh in SH:
            be_all('A.%s.%s' % (rd, sh), ['A.%s.%s.a%s' % (rd, sh, sa(a)) for a in LOW] + ['base.a1'], SHARES)
    G9 = sorted(LOW + FINE + [1])
    for sh in SH:
        be_all('strict9.%s' % sh, [('A.strict.%s.a%s' % (sh, sa(a)) if a in LOW else 'Sgrid.strict.%s.a%s' % (sh, sa(a)) if a in FINE else 'base.a1') for a in G9], G9)
    for l in [0, 0.1, 0.5, 1]:
        for sh in SH:
            be_all('lam%s.%s' % (sa(l), sh), [lamrow(l, sh, a) for a in LOW] + ['base.a1'], SHARES)
    for w in WI:
        for c in WC:
            be_all('B.w%s.c%d' % (sa(w), c), ['B.w%s.c%d.a%s' % (sa(w), c, sa(a)) for a in SHARES], SHARES)
    for L in LAGS:
        be_all('C.L%s' % sa(L), ['C.L%s.a%s' % (sa(L), sa(a)) for a in SHARES], SHARES)
    for tn in THN:
        be_all('Th.%s.base' % tn, ['Th.%s.base.a%s' % (tn, sa(a)) for a in SHARES], SHARES)
        for sh in SH:
            be_all('Th.%s.sourced.%s' % (tn, sh), ['Th.%s.sourced.%s.a%s' % (tn, sh, sa(a)) for a in LOW] + ['Th.%s.base.a1' % tn], SHARES)
    S['breakeven'] = BE
    # Sgrid effects (no base row at these shares)
    S['Sgrid'] = {('Sgrid.strict.%s.a%s' % (sh, sa(a))): readrow('Sgrid.strict.%s.a%s' % (sh, sa(a)), None, ['fgt0PY', 'endoAnn']) for sh in SH for a in FINE}
    # ---- Q2: wages
    S['B'] = {}
    for w in WI:
        for c in WC:
            for a in SHARES:
                n = 'B.w%s.c%d.a%s' % (sa(w), c, sa(a)); r = readrow(n, 'base.a' + sa(a))
                r['lev'] = {k: est(F.lev(n, k)) for k in ['s82WgG20', 's82BuR20']}
                S['B'][n] = r
    # ---- Q3: the BU's delay
    S['C'] = {}
    for L in LAGS:
        for a in SHARES:
            n = 'C.L%s.a%s' % (sa(L), sa(a)); r = readrow(n, 'base.a' + sa(a))
            r['lev'] = {k: est(F.lev(n, k)) for k in ['s82BuR20', 's82BuRE', 's82WgG20']}
            S['C'][n] = r
    S['baseLev'] = {sa(a): {k: est(F.lev('base.a' + sa(a), k)) for k in ['s82BuR20', 's82BuRE', 's82WgG20', 's82WF', 's82WFPY', 's82LS', 's82LSPY', 's82B30', 's82B30w']} for a in SHARES}
    S['noneLev'] = {k: est(F.lev('base.none', k)) for k in ['s82WgG20', 's82WF', 's82WFPY', 's82LS', 's82LSPY', 's82B30', 's82B30w']}
    # ---- Q4: the factorial
    S['X'] = {}
    keys4 = PK + ['endoAnn']
    for sh in ['pay', 'bu']:
        for a in LOW:
            cell = {'A': 'A.sourced.%s.a%s' % (sh, sa(a)), 'B': 'B.w0.75.c1.a%s' % sa(a), 'C': 'C.L1.a%s' % sa(a),
                    'AB': 'X.AB.%s.a%s' % (sh, sa(a)), 'AC': 'X.AC.%s.a%s' % (sh, sa(a)), 'BC': 'X.BC.a%s' % sa(a), 'ABC': 'X.ABC.%s.a%s' % (sh, sa(a))}
            S['X']['%s.a%s' % (sh, sa(a))] = factorial(F, cell, 'base.a' + sa(a), keys4)
    S['X']['BC.a1'] = factorial(F, {'B': 'B.w0.75.c1.a1', 'C': 'C.L1.a1', 'BC': 'X.BC.a1'}, 'base.a1', keys4)
    # ---- Q5: who goes short
    S['Q5'] = {}
    for rd in RD:
        for sh in SH:
            for a in LOW:
                n = 'A.%s.%s.a%s' % (rd, sh, sa(a))
                S['Q5'][n] = {k: est(F.lev(n, k)) for k in ['s82Xq1', 's82Xq2', 's82Xq3', 's82Xq4', 's82Xq5', 'slXP', 'slXN', 'slX', 's82Uq1', 's82Uq5', 's82U']}
    for l in [0]:
        for sh in SH:
            for a in LOW:
                n = lamrow(l, sh, a); S['Q5'][n] = {k: est(F.lev(n, k)) for k in ['s82Xq1', 's82Xq2', 's82Xq3', 's82Xq4', 's82Xq5', 'slXP', 'slXN', 'slX']}
    for a in SHARES:
        n = 'base.a' + sa(a); S['Q5'][n] = {k: est(F.lev(n, k)) for k in ['s82Uq1', 's82Uq2', 's82Uq3', 's82Uq4', 's82Uq5', 's82UP', 's82UN', 's82U']}
    # ---- Q6: the smaller readings
    S['E'] = {}
    for x in EREAD:
        for a in [0, 1]:
            n = 'E.%s.a%s' % (x, sa(a)); S['E'][n] = readrow(n, 'base.a' + sa(a), PK + ['endoAnn', 's82Wp50A'])
    S['D'] = {sa(a): {k: est(F.eff('base.a' + sa(a), k)) for k in ['s82Wp50A', 's82Wp50', 's82Wp50Aw', 's82Wp50w', 's82B30w']} for a in SHARES}
    S['ppov20'] = {sa(a): est(F.eff('base.a' + sa(a), 'ppov20')) for a in SHARES} if 'ppov20' in F.R['base.a1'] else None
    S['prices'] = {sa(a): {k: est(F.eff('base.a' + sa(a), k)) for k in ['prSh', 'prWsh', 'prPovSh']} for a in SHARES}
    return S, BE


def factorial(F, cell, base, keys):
    """per seed v(S) = the change made by the readings in S; dividends, Shapley values"""
    out = {}
    pl = sorted(set(''.join(cell.keys())))
    for k in keys:
        b = F.eff(base, k); v = {S_: F.eff(n, k) - b for S_, n in cell.items()}; v[''] = np.zeros_like(b)
        r = {'alone': {p: est(v[p]) for p in pl}, 'joint': est(v[''.join(pl)])}
        div = {}
        if len(pl) == 3:
            for i, j in (('A', 'B'), ('A', 'C'), ('B', 'C')): div[i + j] = v[i + j] - v[i] - v[j]
            div['ABC'] = v['ABC'] - v['AB'] - v['AC'] - v['BC'] + v['A'] + v['B'] + v['C']
            def V(s): return v[''.join(sorted(s))]
            sh = {}
            for p in pl:
                o = [q for q in pl if q != p]
                sh[p] = (V([p]) - v[''])/3 + (V([p, o[0]]) - V([o[0]]))/6 + (V([p, o[1]]) - V([o[1]]))/6 + (V(pl) - V(o))/3
        else:
            div['BC'] = v['BC'] - v['B'] - v['C']
            sh = {p: (v[p] + (v['BC'] - v[[q for q in pl if q != p][0]]))/2 for p in pl}
        r['inter'] = {d: est(x) for d, x in div.items()}
        r['shapley'] = {p: est(x) for p, x in sh.items()}
        r['claimed'] = [d for d, s in r['inter'].items() if not s['zero'] and excl(s)]
        if excl(r['joint']) and not r['joint']['zero']:
            r['share'] = {p: 100*r['shapley'][p]['est']/r['joint']['est'] for p in pl}
        out[k] = r
    return out


# ---------------------------------------------------------------- checks on the batch's own rows
def checks(F):
    R = F.R; out = []
    def differ(a, b, skip=None):
        ks = set(R[a]) | set(R[b]); bad = []
        for k in ks:
            if skip and k.startswith(skip): continue
            if k not in R[a] or k not in R[b] or not np.array_equal(R[a][k], R[b][k], equal_nan=True): bad.append(k)
        return bad
    d2 = differ('Achk.full.a0', 'base.a0', 'sl'); out.append(('check 2: sl full at share 0 equals base share 0 in every key but the limit\'s own', not d2, d2))
    for sh in SH:
        d3 = differ('Achk.strict.%s.a1' % sh, 'base.a1', 'sl'); out.append(('check 3: sl strict, %s rule, at share 1 equals the main row in every key but the limit\'s own' % sh, not d3, d3))
    for w in WI:
        for c in WC:
            d4 = differ('B.w%s.c%d.none' % (sa(w), c), 'base.none'); out.append(('check 4: the no-programme run with wIdx %s, wc %d equals base.none in every key' % (sa(w), c), not d4, d4))
    ok = all(np.all(R[n]['s82Ok'] == 1) for n in R if 's82Ok' in R[n]); out.append(('every run read the same seed\'s no-programme median (s82Ok 1 in every row and seed)', ok, []))
    ok = np.array_equal(R['base.none']['s82Mw0'], R['base.none']['medWealthReal']); out.append(('the no-programme run\'s s82Mw0 equals its own median real wealth', ok, []))
    nf = [n + ':' + k for n in R for k in R[n] if not np.all(np.isfinite(R[n][k]))]; out.append(('every stored value is finite', not nf, nf[:10]))
    # A moves the wealth outcomes and basic living only through prices; the cut does not change prices (essD is demand before the cut)
    same = [n for n in R if n.startswith('A.') and all(np.array_equal(R[n][k], R['base.a' + n.split('.a')[-1]][k]) for k in ['ppovA', 'pov', 'wtMedE', 'medWealthReal', 'bNAPy', 'endoAnn'])]
    out.append(('reported, not a pass/fail check: A rows whose wealth, basic-living and inflation keys equal the base row at the same share in every seed: %d of 36' % len(same), None, []))
    return out


# ---------------------------------------------------------------- writing
def main():
    global W, REPS
    src, out = sys.argv[1], sys.argv[2]
    eng = sys.argv[sys.argv.index('--engine') + 1] if '--engine' in sys.argv else 'eb0969c'
    if '--reps' in sys.argv: REPS = int(sys.argv[sys.argv.index('--reps') + 1])
    os.makedirs(out, exist_ok=True)
    rng = np.random.default_rng(20261118); idx = rng.integers(0, NS, size=(REPS, NS))
    W = np.zeros((REPS, NS))
    for b in range(REPS): W[b] = np.bincount(idx[b], minlength=NS)/NS
    ALL, CHK, META = {}, {}, {}
    for e in ENVS:
        for y in YEARS:
            fo = os.path.join(src, 's82-v6-%s-%d-%s' % (e, y, eng))
            n, bad = sha_ok(fo)
            rows, meta = load(fo)
            F = Folder(rows, e, y)
            CHK['%s-%d' % (e, y)] = [('SHA256SUMS: %d files, all match' % n, not bad, bad)] + \
                [('20 shards cover seeds 1-500 once; engine %s and a clean checkout in every shard' % meta[0]['manifest'].get('commit', '?')[:7],
                  all(m['manifest'].get('commit', '').startswith(eng) and not m['manifest'].get('dirty', False) for m in meta), [])] + \
                [('the release start\'s baseline check passed in every shard', all(m['baseline'] and m['baseline'].get('checked') for m in meta), [])] + checks(F)
            S, _ = analyse(F)
            ALL['%s-%d' % (e, y)] = S
            META['%s-%d' % (e, y)] = {'command': meta[0]['command'], 'manifest': meta[0]['manifest']}
            print('analysed', e, y, flush=True)
    json.dump({'engine': eng, 'reps': REPS, 'bootstrapSeed': 20261118, 'meta': META, 'checks': {k: [(a, None if b is None else bool(b), c) for a, b, c in v] for k, v in CHK.items()}, 'results': ALL},
              open(os.path.join(out, 's82-summary.json'), 'w'), indent=0, default=lambda o: float(o) if isinstance(o, np.floating) else bool(o) if isinstance(o, np.bool_) else str(o))
    write(out, ALL, CHK, eng)


def write(out, ALL, CHK, eng):
    gen = ('Generated by `python3 dev/tools/s82_tables.py` from compassionism-sim-results `s82-v6-<env>-<years>-%s` (runner/jobs/s82.js, seeds 1-500, 500 adults). '
           'Effect: programme run minus its own no-programme run, mean over seeds; 95%% paired-bootstrap interval (%d replicates, generator seed 20261118). '
           'Shares are the backed share (the part of the payout matched by new output); share 1 is the main row (full backing, a design parameter). '
           'Preregistration: research-update `prereg/2026-11-s82-v6-supply-indexing.md` with Amendments 1-4.' % (eng, REPS))
    # ---- checks
    L = ['# S82, the checks (before any table is read)', '', gen, '']
    allok = True
    for key, cs in CHK.items():
        e, y = key.split('-'); L += ['## %s, %s years' % (ENVL[e], y), '']
        for name, ok, bad in cs:
            allok &= ok is not False; L.append('- %s %s%s' % ('NOTE' if ok is None else 'PASS' if ok else 'FAIL', name, (': ' + ', '.join(bad[:8])) if bad and not ok else ''))
        L.append('')
    L.insert(4, '**All checks: %s.**' % ('PASS' if allok else 'FAIL')); L.insert(5, '')
    open(os.path.join(out, 's82-checks.md'), 'w').write('\n'.join(L) + '\n')

    for y in YEARS:
        tag = '' if y == 20 else '-40y'
        hz = '%d years%s' % (y, ' (primary)' if y == 20 else ' (secondary: the 40-year figures)')
        # ---- Q1
        L = ['# S82, question 1: the supply limit (%s)' % hz, '', gen, '',
             'Under the supply limit (part A) only housing, medical care and food can be short. In the main reading the money a cut leaves unspent goes to other goods, '
             'so the wealth outcomes, basic living and inflation move only through prices; the cut does not change prices (the engine\'s essentials demand is read before the cut). '
             'A\'s real cost shows in basket poverty (read on what households received) and in the shortfall; the wage and BU readings (questions 2-3) are the ones that bear on wealth. '
             'The strict bound is ' + STRICT + '. The restricted reading halves every sourced value: a policy reading. Effects in points; wealth in Year-0 dollars.', '']
        for e in ENVS:
            S = ALL['%s-%d' % (e, y)]
            L += ['## %s' % ENVL[e], '']
            L += ['### Basket poverty: the programme\'s effect at each backed share', '', '| Reading | Rule | ' + ' | '.join('share %s' % sa(a) for a in SHARES) + ' |', '|---|---|' + '---|'*len(SHARES)]
            L.append('| no limit (base) | – | ' + ' | '.join(ci(S['base'][sa(a)]['fgt0PY']) for a in SHARES) + ' |')
            for rd in RD:
                for sh in SH:
                    L.append('| %s | %s | ' % (rd if rd != 'strict' else 'strict bound', sh) + ' | '.join(ci(S['A']['A.%s.%s.a%s' % (rd, sh, sa(a))]['eff']['fgt0PY']) for a in LOW) + ' | = main row |')
            L += ['', '### The change the limit makes to basket poverty (reading minus no limit, same share; H: survives Holm across the six primary readings)', '',
                  '| Reading | Rule | ' + ' | '.join('share %s' % sa(a) for a in LOW) + ' |', '|---|---|' + '---|'*len(LOW)]
            for rd in RD:
                for sh in SH:
                    cells = []
                    for a in LOW:
                        r = S['A']['A.%s.%s.a%s' % (rd, sh, sa(a))]; c = r['chg']['fgt0PY']
                        cells.append(ci(c) + (' H' if r['holm']['fgt0PY'] < 0.05 and not c['zero'] else ''))
                    L.append('| %s | %s | ' % (rd if rd != 'strict' else 'strict bound', sh) + ' | '.join(cells) + ' |')
            unmoved = [k for k in PK if k != 'fgt0PY' and all(S['A'][n]['chg'][k]['zero'] for n in S['A'])]
            L += ['', 'Under every A row, %s: the change is 0 in every seed (the limit acts on these only through prices, and it moves no price). '
                  'Their effects are the base row\'s, below.' % (', '.join(LAB[k] for k in unmoved) if unmoved else 'no other primary reading is unchanged'), '']
            L += ['### The base curve: every primary reading (no limit)', '', '| Outcome | ' + ' | '.join('share %s' % sa(a) for a in SHARES) + ' |', '|---|' + '---|'*len(SHARES)]
            for k in PK + ['endoAnn', 'fgt2PY']:
                L.append('| %s | ' % LAB[k] + ' | '.join(ci(S['base'][sa(a)][k], k) for a in SHARES) + ' |')
            L += ['', 'No-programme levels: ' + '; '.join('%s %s' % (LAB.get(k, k), ci(S['none'][k], k)) for k in PK) + '.', '']
            # the limit's own keys
            L += ['### The limit\'s own readings (means over the run, %; c: capacity built by the last year, share of needs consumption)', '',
                  '| Reading | Rule | Share | excess e | unbacked | target cut housing / medical / food | realised cut (all three) | capacity built housing / medical / food | shortfall (% of basket) | basket poverty on what was paid for (level) |',
                  '|---|---|---|---|---|---|---|---|---|---|']
            for rd in RD:
                for sh in ['pay']:
                    for a in LOW:
                        q = S['A']['A.%s.%s.a%s' % (rd, sh, sa(a))]['sl']
                        L.append('| %s | %s | %s | %s | %s | %s / %s / %s | %s | %s / %s / %s | %s | %s |' % (rd, sh, sa(a), fm(q['slE']['est']), fm(q['slEu']['est']),
                                 fm(q['slRhousing']['est']), fm(q['slRmedical']['est']), fm(q['slRfood']['est']), fm(q['slCutSh']['est']),
                                 fm(q['slChousing']['est']), fm(q['slCmedical']['est']), fm(q['slCfood']['est']), ci(q['slX']), fm(q['slF0p']['est'])))
            L += ['', 'The excess and the target cut do not depend on the sharing rule; the realised cut and the shortfall do slightly (a household\'s cut stops at its own spending; Amendment 1, item 3). Other rules: the summary JSON.', '']
            # decision rules
            L += ['### Decision rules 2-4 and Amendments 3-4, per share and primary reading', '',
                  'Holds: under the sourced reading with all three rules, the effect keeps the no-limit sign and its interval excludes zero. Rules: which of pay / even / bu pass. '
                  'Slowest building speed (medical care and food; housing sourced): from which speed on the grid (0, 0.1, 0.25 sourced, 0.5, 1) the test passes at every faster speed. '
                  'Theta: the same test at half and double the essentials price response. Strict and restricted: which rules pass at those readings (reported beside; no headline from the strict bound alone).', '',
                  '| Share | Outcome | Holds (sourced) | pay / even / bu | Rests on the rule | Slowest building speed | half theta | double theta | restricted pay / even / bu | strict bound pay / even / bu |',
                  '|---|---|---|---|---|---|---|---|---|---|']
            yn = lambda b: 'yes' if b else 'no'
            for a in LOW:
                for k in PK:
                    d = S['DR'][sa(a) + '.' + k]
                    L.append('| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (sa(a), LAB[k], yn(d['holds']) + ('' if d['baseExcl0'] else ' (no-limit effect\'s interval includes zero)'),
                             ' / '.join(yn(d['rules'][s]) for s in SH), yn(d['restsOnRule']), d['slowest'], yn(d['theta']['half']), yn(d['theta']['double']),
                             ' / '.join(yn(d['restricted'][s]) for s in SH), ' / '.join(yn(d['strict'][s]) for s in SH)))
            L.append('')
            # break-even
            BE = S['breakeven']
            L += ['### Break-even backed shares', '', 'Scanning down from full backing: where the effect is no better than no programme (poverty, wealth), and where programme inflation reaches 5 points a year. '
                  '"below 0": no grid point reaches it; "above 1": the main row is already there. 95% interval of the crossing from the bootstrap; replicates past the grid\'s ends are counted, not interpolated.', '',
                  '| Reading | Rule | ' + ' | '.join(LAB[k] for k in PK) + ' | inflation reaches 5 points |', '|---|---|' + '---|'*(len(PK) + 1)]
            L.append('| no limit | – | ' + ' | '.join(be_str(BE['base'][k]) for k in PK) + ' | ' + be_str(BE['base']['inflation5']) + ' |')
            for rd in RD:
                for sh in SH:
                    b = BE['A.%s.%s' % (rd, sh)]; L.append('| %s | %s | ' % (rd if rd != 'strict' else 'strict bound', sh) + ' | '.join(be_str(b[k]) for k in PK) + ' | ' + be_str(b['inflation5']) + ' |')
            for sh in SH:
                b = BE['strict9.%s' % sh]; L.append('| strict bound, 9-point grid | %s | ' % sh + ' | '.join(be_str(b[k]) for k in PK) + ' | ' + be_str(b['inflation5']) + ' |')
            for l in [0, 0.1, 0.5, 1]:
                for sh in SH:
                    b = BE['lam%s.%s' % (sa(l), sh)]; L.append('| building speed %s (medical, food) | %s | ' % (sa(l), sh) + ' | '.join(be_str(b[k]) for k in PK) + ' | ' + be_str(b['inflation5']) + ' |')
            for tn in THN:
                b = BE['Th.%s.base' % tn]; L.append('| %s, no limit | – | ' % THL[tn] + ' | '.join(be_str(b[k]) for k in PK) + ' | ' + be_str(b['inflation5']) + ' |')
                for sh in SH:
                    b = BE['Th.%s.sourced.%s' % (tn, sh)]; L.append('| %s, sourced | %s | ' % (THL[tn], sh) + ' | '.join(be_str(b[k]) for k in PK) + ' | ' + be_str(b['inflation5']) + ' |')
            L.append('')
            # the building speed sweep on basket poverty
            L += ['### Amendment 3: basket poverty at each building speed of medical care and food (effect; speed 0 puts those two sectors at the strict bound)', '',
                  '| Speed | Rule | ' + ' | '.join('share %s' % sa(a) for a in LOW) + ' |', '|---|---|' + '---|'*len(LOW)]
            for l in LAMS:
                for sh in SH:
                    n = lambda a: ('A.sourced.%s.a%s' % (sh, sa(a))) if l == 0.25 else ('Slam.lam%s.%s.a%s' % (sa(l), sh, sa(a)))
                    src = S['A'] if l == 0.25 else S['Slam']
                    L.append('| %s%s | %s | ' % (sa(l), ' (sourced)' if l == 0.25 else '', sh) + ' | '.join(ci(src[n(a)]['eff']['fgt0PY']) for a in LOW) + ' |')
            L.append('')
            L += ['### Amendment 3: the strict bound on the finer grid, basket poverty (effect)', '', '| Rule | ' + ' | '.join('share %s' % sa(a) for a in sorted(LOW + FINE)) + ' |', '|---|' + '---|'*8]
            for sh in SH:
                L.append('| %s | ' % sh + ' | '.join(ci(S['A']['A.strict.%s.a%s' % (sh, sa(a))]['eff']['fgt0PY']) if a in LOW else ci(S['Sgrid']['Sgrid.strict.%s.a%s' % (sh, sa(a))]['eff']['fgt0PY']) for a in sorted(LOW + FINE)) + ' |')
            L.append('')
            # theta
            L += ['### Amendment 4: the essentials price response theta (a design parameter, swept at half and double)', '',
                  '| Theta | Row | Outcome | ' + ' | '.join('share %s' % sa(a) for a in SHARES) + ' |', '|---|---|---|' + '---|'*len(SHARES)]
            for tn in THN:
                for k in PK + ['endoAnn']:
                    L.append('| %s | no limit: effect | %s | ' % (tn, LAB[k]) + ' | '.join(ci(S['Th']['Th.%s.base.a%s' % (tn, sa(a))]['eff'][k], k) for a in SHARES) + ' |')
                    L.append('| %s | no limit: change from the engine\'s theta | %s | ' % (tn, LAB[k]) + ' | '.join(ci(S['Th']['Th.%s.base.a%s' % (tn, sa(a))]['chg'][k], k) for a in SHARES) + ' |')
                for sh in SH:
                    L.append('| %s | sourced, %s: change the limit makes | basket poverty | ' % (tn, sh) + ' | '.join(ci(S['Th']['Th.%s.sourced.%s.a%s' % (tn, sh, sa(a))]['chg']['fgt0PY']) for a in LOW) + ' | = main row |')
            L.append('')
        open(os.path.join(out, 's82-q1-supply%s.md' % tag), 'w').write('\n'.join(L) + '\n')

        # ---- Q2 and Q3
        for part, title, rowsf in (('B', 'question 2: wages that follow programme inflation in part', lambda: [('wIdx %s, made up a year later: %s' % (sa(w), 'yes' if c else 'no'), 'B.w%s.c%d' % (sa(w), c)) for w in WI for c in WC]),
                                   ('C', 'question 3: the BU follows the price of the needs with a delay (the design\'s monthly and quarterly first)', lambda: [(LAGL[L_], 'C.L%s' % sa(L_)) for L_ in LAGS])):
            L = ['# S82, %s (%s)' % (title, hz), '', gen, '',
                 ('Wages: `wg += wIdx x inflation(t) + wc x (1 - wIdx) x inflation(t - 1)`, on both runs (the no-programme run has no programme inflation, so it is unchanged: check 4). wIdx 1 is today\'s engine.' if part == 'B' else
                  'The BU and the child allowance are set from the needs\' price read L years back (today: no delay). Today\'s safety net keeps the engine\'s indexing in both runs, so the delay falls only on the programme run (the cautious side).'), '']
            for e in ENVS:
                S = ALL['%s-%d' % (e, y)]; BE = S['breakeven']
                L += ['## %s' % ENVL[e], '']
                for k in PK + ['endoAnn']:
                    L += ['### %s' % LAB[k], '', '| Reading | Row | ' + ' | '.join('share %s' % sa(a) for a in SHARES) + ' |', '|---|---|' + '---|'*len(SHARES)]
                    L.append('| none (base) | effect | ' + ' | '.join(ci(S['base'][sa(a)][k], k) for a in SHARES) + ' |')
                    for lab, pre in rowsf():
                        L.append('| %s | effect | ' % lab + ' | '.join(ci(S[part]['%s.a%s' % (pre, sa(a))]['eff'][k], k) for a in SHARES) + ' |')
                        L.append('| %s | change | ' % lab + ' | '.join(ci(S[part]['%s.a%s' % (pre, sa(a))]['chg'][k], k) + (' H' if k in PK and S[part]['%s.a%s' % (pre, sa(a))]['holm'][k] < 0.05 and not S[part]['%s.a%s' % (pre, sa(a))]['chg'][k]['zero'] else '') for a in SHARES) + ' |')
                    L.append('')
                L += ['### Break-even backed shares', '', '| Reading | ' + ' | '.join(LAB[k] for k in PK) + ' | inflation reaches 5 points |', '|---|' + '---|'*(len(PK) + 1)]
                L.append('| none (base) | ' + ' | '.join(be_str(BE['base'][k]) for k in PK) + ' | ' + be_str(BE['base']['inflation5']) + ' |')
                for lab, pre in rowsf():
                    L.append('| %s | ' % lab + ' | '.join(be_str(BE[pre][k]) for k in PK) + ' | ' + be_str(BE[pre]['inflation5']) + ' |')
                L.append('')
                L += ['### The real BU (a month of the BU over the needs\' price, Year-0 $) and the real wage (mean wage over the general price level, Year-0 $), year %d' % min(20, y), '',
                      '| Reading | Level | ' + ' | '.join('share %s' % sa(a) for a in SHARES) + ' |', '|---|---|' + '---|'*len(SHARES)]
                for kk, nm in (('s82BuR20', 'real BU'), ('s82WgG20', 'real wage')):
                    L.append('| none (base) | %s | ' % nm + ' | '.join(ci(S['baseLev'][sa(a)][kk], kk) for a in SHARES) + ' |')
                    for lab, pre in rowsf():
                        L.append('| %s | %s | ' % (lab, nm) + ' | '.join(ci(S[part]['%s.a%s' % (pre, sa(a))]['lev'][kk], kk) for a in SHARES) + ' |')
                L += ['', 'No-programme real wage: %s.' % ci(S['noneLev']['s82WgG20'], 's82WgG20'), '']
            open(os.path.join(out, 's82-q%s-%s%s.md' % ('2' if part == 'B' else '3', 'wages' if part == 'B' else 'bu-delay', tag)), 'w').write('\n'.join(L) + '\n')

        # ---- Q4
        L = ['# S82, question 4: the three readings together (%s)' % hz, '', gen, '',
             'The 2 x 2 x 2 design at the central readings: A, the sourced supply limit (market rule, or the design\'s rule); B, wages indexed 0.75 and made up a year later; C, the BU a year behind. '
             'v(S): the change the readings in S make to the programme\'s effect at that share, paired by seed. Alone: v(A), v(B), v(C). Interactions (Harsanyi dividends): AB = v(AB) - v(A) - v(B), and so on; '
             'ABC = v(ABC) - v(AB) - v(AC) - v(BC) + v(A) + v(B) + v(C). Joint: v(ABC). Shapley values split the joint change (they add up to it). '
             '* an interaction whose 95% interval excludes zero (claimed, research rule 4): then the readings\' separate changes are not summed anywhere and the joint row is the one reported (decision rule 7). '
             'At full backing the limit is inactive, so only B x C is read there.', '']
        for e in ENVS:
            S = ALL['%s-%d' % (e, y)]; L += ['## %s' % ENVL[e], '']
            for k in PK + ['endoAnn']:
                L += ['### %s' % LAB[k], '', '| Rule, share | A alone | B alone | C alone | AB | AC | BC | ABC | joint | Shapley A / B / C | claimed |', '|---|---|---|---|---|---|---|---|---|---|---|']
                for key in ['%s.a%s' % (sh, sa(a)) for sh in ['pay', 'bu'] for a in LOW] + ['BC.a1']:
                    r = S['X'][key][k]; al = r['alone']; it = r['inter']
                    g = lambda d, s: (ci(d[s], k) + ('*' if s in r['claimed'] else '')) if s in d else '–'
                    L.append('| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (key.replace('.a', ', share ').replace('BC, share 1', 'share 1 (B x C only)'), g(al, 'A'), g(al, 'B'), g(al, 'C'), g(it, 'AB'), g(it, 'AC'), g(it, 'BC'), g(it, 'ABC'), ci(r['joint'], k),
                             ' / '.join(fm(r['shapley'][p]['est'], k) for p in sorted(r['shapley'])) + ((' (%s %%)' % ' / '.join('%.0f' % r['share'][p] for p in sorted(r['share']))) if 'share' in r else ''),
                             ', '.join(r['claimed']) or 'none'))
                L.append('')
        open(os.path.join(out, 's82-q4-factorial%s.md' % tag), 'w').write('\n'.join(L) + '\n')

        # ---- Q5
        L = ['# S82, question 5: who goes short (%s)' % hz, '', gen, '',
             'The supply cut by fifth of cash income over the cost of living (1: the least able to pay; the year\'s own adults ranked, unweighted), % of the needs basket, mean over adult-years; '
             'beside it the need nobody paid for in the no-programme run on the same scale and ranking (the market\'s rationing by ability to pay today). Participants and others: the cut among CCO members and the rest. '
             'Levels, not differences; intervals over seeds.', '']
        for e in ENVS:
            S = ALL['%s-%d' % (e, y)]; Q = S['Q5']; L += ['## %s' % ENVL[e], '']
            L += ['| Row | Share | fifth 1 | fifth 2 | fifth 3 | fifth 4 | fifth 5 | all | participants | others |', '|---|---|---|---|---|---|---|---|---|---|']
            L.append('| no programme: unpaid need | – | ' + ' | '.join(ci(S['none']['s82Uq%d' % q]) for q in range(1, 6)) + ' | ' + ci(S['none']['s82U']) + ' | – | – |')
            for a in SHARES:
                q = Q['base.a' + sa(a)]
                L.append('| programme, no limit: unpaid need | %s | ' % sa(a) + ' | '.join(ci(q['s82Uq%d' % i]) for i in range(1, 6)) + ' | ' + ci(q['s82U']) + ' | ' + ci(q['s82UP']) + ' | ' + ci(q['s82UN']) + ' |')
            for rd in RD:
                for sh in SH:
                    for a in LOW:
                        q = Q['A.%s.%s.a%s' % (rd, sh, sa(a))]
                        L.append('| %s, %s: supply cut | %s | ' % (rd if rd != 'strict' else 'strict bound', sh, sa(a)) + ' | '.join(ci(q['s82Xq%d' % i]) for i in range(1, 6)) + ' | ' + ci(q['slX']) + ' | ' + ci(q['slXP']) + ' | ' + ci(q['slXN']) + ' |')
            for sh in SH:
                for a in LOW:
                    q = Q['Slam.lam0.%s.a%s' % (sh, sa(a))]
                    L.append('| building speed 0, %s: supply cut | %s | ' % (sh, sa(a)) + ' | '.join(ci(q['s82Xq%d' % i]) for i in range(1, 6)) + ' | ' + ci(q['slX']) + ' | ' + ci(q['slXP']) + ' | ' + ci(q['slXN']) + ' |')
            L.append('')
        open(os.path.join(out, 's82-q5-shortfall%s.md' % tag), 'w').write('\n'.join(L) + '\n')

        # ---- Q6
        L = ['# S82, question 6: the triage\'s smaller readings (%s)' % hz, '', gen, '',
             'Each reading is its own pair (programme and no-programme run with the reading) at no backing and at the main row. Change: the reading\'s effect minus the base effect at the same share. H: survives Holm across the six primary readings.' +
             (' Ageing at 40 years: labelled, as the triage asks (theme 13); partnerships stay fixed.' if y == 40 else ''), '']
        for e in ENVS:
            S = ALL['%s-%d' % (e, y)]; L += ['## %s' % ENVL[e], '']
            L += ['| Reading | Share | ' + ' | '.join(LAB[k] for k in PK + ['endoAnn']) + ' |', '|---|---|' + '---|'*(len(PK) + 1)]
            for a in [0, 1]:
                L.append('| base effect | %s | ' % sa(a) + ' | '.join(ci(S['base'][sa(a)][k], k) for k in PK + ['endoAnn']) + ' |')
            for x in EREAD:
                for a in [0, 1]:
                    r = S['E']['E.%s.a%s' % (x, sa(a))]
                    L.append('| %s: change | %s | ' % (EL[x], sa(a)) + ' | '.join(ci(r['chg'][k], k) + (' H' if k in PK and r['holm'][k] < 0.05 and not r['chg'][k]['zero'] else '') for k in PK + ['endoAnn']) + ' |')
            L += ['', '### Section D\'s keys (themes 10, 22, 24)', '', '| Key | ' + ' | '.join('share %s' % sa(a) for a in SHARES) + ' | no programme (level) |', '|---|' + '---|'*(len(SHARES) + 1)]
            for k, nm in (('s82Wp50A', 'wealth poverty at half the same seed\'s no-programme median, yearly average: effect (theme 24)'), ('s82Wp50', 'the same at the last year: effect'),
                          ('s82Wp50Aw', 'the same, weighted, yearly: effect'), ('s82B30w', 'below 30 days of basic living, weighted: effect (theme 10)')):
                L.append('| %s | ' % nm + ' | '.join(ci(S['D'][sa(a)][k]) for a in SHARES) + ' | %s |' % (ci(S['none'][k]) if k in S['none'] else '–'))
            for k, nm in (('s82B30', 'below 30 days, unweighted (= bNAPy): level'), ('s82B30w', 'below 30 days, weighted: level'), ('s82WFPY', 'wages over factor income, all years: level % (theme 22)'),
                          ('s82LSPY', 'labour\'s share of money income, all years: level %')):
                L.append('| %s | ' % nm + ' | '.join(ci(S['baseLev'][sa(a)][k]) for a in SHARES) + ' | %s |' % ci(S['noneLev'][k]))
            L.append('| the shadow-price readings (prSh / prWsh / prPovSh): effect | ' + ' | '.join(' / '.join(fm(S['prices'][sa(a)][k]['est']) for k in ['prSh', 'prWsh', 'prPovSh']) for a in SHARES) + ' | – |')
            if S['ppov20']: L.append('| wealth poverty at year 20 of the 40-year run: effect | ' + ' | '.join(ci(S['ppov20'][sa(a)]) for a in SHARES) + ' | – |')
            L.append('')
        open(os.path.join(out, 's82-q6-smaller%s.md' % tag), 'w').write('\n'.join(L) + '\n')


if __name__ == '__main__':
    main()
