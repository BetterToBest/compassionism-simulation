#!/usr/bin/env python3
"""S85 part 3 (Nov 20, 2026): the checks and tables of the output-per-hour and automation batch, as research-update
prereg/2026-11-s85-output-per-hour.md fixes them (Questions, Outcomes, Analysis, Checks, Decision rules; Amendments 1-3). Reads the six folders
s85-<env>-<years>-<engine> of compassionism-sim-results (runner/jobs/s85.js; 20 shards of 25 seeds, seeds 1-500, 179 rows each), the published
main rows with the private price at the sale (s90-sale-<env>-<years>-b8ccd8d, check 1) and, when present, the supplement with the security
measures on (s85sec-<env>-<years>-<engine>, Amendment 3 item 1; check 10). Writes Markdown tables and a summary JSON.

  python3 dev/tools/s85_tables.py RESULTS_DIR OUT_DIR [--engine 503fa48] [--reps 10000] [--nosec]

Method (fixed by the preregistration and Amendment 3; where it is silent, the cautious reading, said so here and in the tables):
- Effect: the programme run minus its own no-programme run (the row's `none` partner in the job's rowSpec), paired by seed.
- Displacement's cost (Amendment 3 items 3-4): harm-signed, positive = worse. Poverty measures: run at D minus run at D 0; median wealth: run at
  D 0 minus run at D. cost_N in the no-programme runs, cost_P in the programme runs; offset = cost_N - cost_P (positive: the programme takes away
  part of the harm); offset share = 1 - mean cost_P / mean cost_N with the bootstrap interval of that ratio, given only where cost_N's interval lies
  wholly on the harmful side. D 0 reference: A.<design>.gain.D0 for blocks A, C and D's even order; G.<design>.zero for B's no-gain row;
  B.<design>.ghigh.D0 for B's high-gain row. B's pass-through rows and D's owner-share rows have no D 0 row at their setting: effects and the change
  against A.<design>.jobs.D0.5 only.
- Primary readings (six): basket poverty fgt0PY; wealth poverty yearly (ppovA, the mean of ppov_1 .. ppov_{T-1}) and at the last year (pov);
  median real wealth weighted (wtMedE) and unweighted (medWealthReal); savings: secM3A (adult-years whose liquid savings cover under three months
  of need) from the supplement for blocks A and F once check 10 passes, otherwise, and for blocks B-E, bNAPy (below 30 days of basic living), the
  batch's nearest stored measure. Each table says which.
- Holm (Amendment 3 item 2): block A, across the six readings x the eight cells (D 0.1-0.7 x lost jobs, shorter hours) = 48 tests within each
  environment, horizon and design; every other comparison, across the six readings within its own cell. p: two-sided paired t (499 degrees of
  freedom). Decision rule 2's categories: offsets fully (offset significant after Holm, positive, cost_P's 95% interval reaching zero or below);
  offsets in part (the same, cost_P's interval above zero); does not offset (offset not significant after Holm); worsens (significant, negative).
- Intervals: paired bootstrap, 10,000 replicates, seeds resampled, percentile; generator numpy default_rng(20261120), one resample for every table.
- Q4 (Amendment 1 item 4, Amendment 3 item 6): programme inflation = the programme run's endoAnn (points a year). Backs enough: interval's upper end
  at most 5; uncertain: straddles 5; does not back enough: lower end above 5. Break-even m: the mean inflation at m 0.25, 0.5, 1 interpolated
  linearly to 5, with the bootstrap interval of the crossing; never extrapolated.
Standard library and numpy."""
import glob, gzip, hashlib, json, math, os, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s64_tables import tcdf, holm  # noqa: E402  (the same t distribution and Holm as the earlier studies)

ENVS = ['ref', 'adv', 'str']; ENVL = {'ref': 'Reference', 'adv': 'Adverse', 'str': 'Stress'}; YEARS = [20, 40]
DES = ['c22', 'rel']; DESL = {'c22': 'full coverage', 'rel': 'opt-in'}
D4 = [0.1, 0.3, 0.5, 0.7]; FORMS = ['jobs', 'hours']; FL = {'jobs': 'lost jobs', 'hours': 'shorter hours'}
CORE = [('fgt0PY', 'basket poverty', -1), ('ppovA', 'wealth poverty, yearly average', -1), ('pov', 'wealth poverty, last year', -1),
        ('wtMedE', 'median real wealth, weighted', 1), ('medWealthReal', 'median real wealth, unweighted', 1)]
LAB = {k: l for k, l, _ in CORE}; FAV = {k: s for k, _, s in CORE}
LAB.update({'secM3A': 'savings under three months of need', 'bNAPy': 'below 30 days of basic living', 'endoAnn': 'programme inflation (points a year)',
            'fgt2PY': 'poverty severity', 'wtT1E': 'top 1% share of wealth (weighted, %)', 'ohLab': 'labour share of income (%)',
            'ohDiv': 'dividend over wages (%)', 'ohPaid': 'share of the dividend paid to the model\'s households (%)', 'ohA': 'produced backed share (%)'})
FAV.update({'secM3A': -1, 'bNAPy': -1, 'endoAnn': -1, 'fgt2PY': -1})
UNIT = {'wtMedE': '$', 'medWealthReal': '$'}
SCALE = {'endoAnn': 100.0}
DIG = {'wtMedE': 0, 'medWealthReal': 0, 'W1': 0, 'W2': 0, 'W3': 0, 'W4': 0, 'W5': 0, 'ohFree': 0, 'ohFreeS': 0, 'ohFreeI': 0, 'ohFreeT': 0,
       'ohFreeST': 0, 'ohFreeIT': 0, 'ohDN': 0, 'ohNN': 0, 'ohN': 0}
KEEP = ['fgt0PY', 'pov', 'wtMedE', 'medWealthReal', 'bNAPy', 'endoAnn', 'fgt2PY', 'wtT1E', 'mfChk'] + \
       ['rt%s%d' % (c, q) for c in 'EVS' for q in range(1, 6)]
SECKEEP = ['secM3A', 'secM3wA', 'secMdA']
REPS = 10000; NS = 500; W = None; SEC = {}  # SEC[(env, years)]: True when the supplement is merged
SECDIR = 's85sec'


def g(x): return '%g' % x


# ---------------------------------------------------------------- loading and checks
def shards(folder):
    fs = sorted(f for f in glob.glob(os.path.join(folder, 'shard-*.json*')) if '.timing.' not in f)
    if not fs: sys.exit('no shard files in ' + folder)
    return fs


def jload(f): return json.load(gzip.open(f) if f.endswith('.gz') else open(f))


def sha_ok(folder):
    bad, n = [], 0
    for line in open(os.path.join(folder, 'SHA256SUMS')):
        h, f = line.split(None, 1); f = f.strip().lstrip('*'); n += 1
        with open(os.path.join(folder, f), 'rb') as fh:
            if hashlib.sha256(fh.read()).hexdigest() != h: bad.append(f)
    return n, bad


def keep(k, T):
    return k in KEEP or k.startswith('oh') or (k.startswith('ppov_') and 1 <= int(k[5:]) <= T - 1)


def s90_rows(folder):
    """the published main rows with the private price at the sale: row -> key -> array over seeds 1-500"""
    D = sorted((jload(f) for f in shards(folder)), key=lambda d: d['_meta']['seeds'][0]); out = {}
    for full in D[0]['rows']:
        out[full.split('.', 1)[1]] = {k: [x for d in D for x in d['rows'][full][k]] for k in D[0]['rows'][full]}
    return out


def load(src, e, y, eng, use_sec):
    """one folder: the kept keys per row (arrays over seeds) and every check that reads all keys"""
    fo = os.path.join(src, 's85-%s-%d-%s' % (e, y, eng)); C = []
    n, bad = sha_ok(fo); C.append(('SHA256SUMS: %d files, all match' % n, not bad, bad))
    fsx = shards(fo); D0 = jload(fsx[0]); spec = {r['name']: r for r in D0['_meta']['rowSpec']}
    s90 = s90_rows(os.path.join(src, 's90-sale-%s-%d-b8ccd8d' % (e, y)))
    sfo = os.path.join(src, '%s-%s-%d-%s' % (SECDIR, e, y, eng)); sec = use_sec and os.path.exists(os.path.join(sfo, 'DONE'))
    sfs = shards(sfo) if sec else None
    if sec:
        n2, bad2 = sha_ok(sfo); C.append(('supplement %s: SHA256SUMS, %d files, all match' % (os.path.basename(sfo), n2), not bad2, bad2))
        if len(sfs) != len(fsx): sys.exit('the supplement is cut into a different number of shards')
    nkeys = len(D0['rows'][next(iter(D0['rows']))])
    R = {}; seeds = []; man = []; nonfin = []; chk2 = {}; conv = {}; c1 = {}; c10 = {'rows': 0, 'diff': []}; secS = {}
    for i, f in enumerate(fsx):
        d = D0 if i == 0 else jload(f); D0 = None; m = d['_meta']; seeds.append(tuple(m['seeds'])); man.append((m['manifest'], m['baseline']))
        rows = {full.split('.', 1)[1]: v for full, v in d['rows'].items()}; lo, hi = m['seeds']
        for nm, v in rows.items():
            for k, a in v.items():
                if any(x is None for x in a): nonfin.append((nm, k))
            dst = R.setdefault(nm, {})
            for k, a in v.items():
                if keep(k, y): dst.setdefault(k, []).extend(a)
        for des in DES:  # check 2: the zero rows equal the main row (oh's own keys aside), and their no-programme run the plain one
            for a_, b_ in (('G.%s.zero' % des, 'A.%s.off' % des), (spec['G.%s.zero' % des]['none'], 'none.off')):
                chk2.setdefault((a_, b_), set()).update(k for k in rows[b_] if not k.startswith('oh') and rows[a_][k] != rows[b_][k])
            for mm in [0.5, 1]:
                for D in [0, 0.5]:
                    for c, base in (('conv', ''), ('convgain', 'gain.')):
                        a_ = 'E.%s.%s.m%s.ghigh.D%s' % (des, c, g(mm), g(D)); b_ = ('E.%s.%sm%s.ghigh.D%s' % (des, base, g(mm), g(D))) if base else 'E.%s.m%s.ghigh.D%s' % (des, g(mm), g(D))
                        conv.setdefault((a_, b_), set()).update(k for k in rows[a_] if rows[a_][k] != rows[b_][k])
        for a_, b_ in (('A.c22.off', 'c22.sale'), ('A.rel.off', 'rel.sale'), ('none.off', 'none')):  # check 1
            ks = c1.setdefault(a_, set())
            for k in s90[b_]:
                if k not in rows[a_] or rows[a_][k] != s90[b_][k][lo - 1:hi]: ks.add(k)
        if sec:
            sd = jload(sfs[i]); sm = sd['_meta']
            if tuple(sm['seeds']) != tuple(m['seeds']): sys.exit('supplement shard %d covers other seeds' % i)
            if sm['manifest'].get('commit') != m['manifest'].get('commit') or sm['manifest'].get('dirty'): c10['diff'].append(('manifest', i))
            for full, v in sd['rows'].items():
                nm = full.split('.', 1)[1]; c10['rows'] = len(sd['rows'])
                for k, a in rows[nm].items():
                    if v.get(k) != a: c10['diff'].append((nm, k))
                for k in SECKEEP: secS.setdefault(nm, {}).setdefault(k, []).extend(v[k])
        del d, rows
    for nm in R:
        R[nm] = {k: np.array([np.nan if x is None else x for x in a], dtype=float) for k, a in R[nm].items()}
        R[nm]['ppovA'] = sum(R[nm]['ppov_%d' % t] for t in range(1, y)) / (y - 1)
        for q in range(1, 6): R[nm]['W%d' % q] = R[nm]['rtE%d' % q] + R[nm]['rtV%d' % q] + R[nm]['rtS%d' % q]
    s = 1; cover = True
    for a, b in sorted(seeds):
        if a != s: cover = False
        s = b + 1
    cover = cover and s == NS + 1
    eng40 = {mm['commit'] for mm, _ in man}; clean = all(not mm.get('dirty') for mm, _ in man); base = all(bl.get('checked') for _, bl in man)
    C.append(('%d shards cover seeds 1-500 once; engine %s and a clean checkout in every shard' % (len(seeds), '/'.join(sorted(x[:7] for x in eng40))),
              cover and len(eng40) == 1 and clean, None))
    C.append(('the release start\'s baseline check passed in every shard', base, None))
    C.append(('every stored value is finite (%d rows x %d keys)' % (len(R), nkeys), not nonfin, nonfin[:10]))
    for nm, ks in c1.items():
        C.append(('check 1: %s equals the published main row with the private price at the sale in every key and seed' % nm, not ks, sorted(ks)[:20]))
    for (a_, b_), dk in chk2.items(): C.append(('check 2: %s equals %s in every key and seed (oh\'s own keys aside)' % (a_, b_), not dk, sorted(dk)[:10]))
    ohrows = [nm for nm in R if spec[nm]['oh']]
    bad3 = [(nm, float(np.max(R[nm]['ohChk']))) for nm in ohrows if np.max(R[nm]['ohChk']) > (0 if spec[nm]['oh']['f'] == 'jobs' else 1e-9)]
    C.append(('check 3: displacement as set in every row with oh, every year and seed (lost jobs: displaced count = round(D_t N) exactly; shorter hours: mean cut = D_t within 1e-9); %d rows' % len(ohrows), not bad3, bad3[:10]))
    bad4 = [(nm, float(np.max(R[nm]['ohId']))) for nm in ohrows if np.max(R[nm]['ohId']) > 1e-6]
    mx4 = max(float(np.max(R[nm]['ohId'])) for nm in ohrows)
    C.append(('check 4: wages plus the dividend equal every E0 times G_t within 1e-6 relative, every year, row and seed (largest %.1e)' % mx4, not bad4, bad4[:10]))
    fl = [nm for nm in R if nm.startswith('E.') and '.floor.' in nm]
    C.append(('check 6: the floor rows (%s) produce nothing (produced share 0 in every seed)' % ', '.join(fl), all(np.all(R[nm]['ohA'] == 0) for nm in fl), None))
    mf = {}
    for nm in R:
        b = 'main' if nm in ('A.c22.off', 'A.rel.off') else 'bk' if spec[nm]['oh'] and spec[nm]['oh'].get('bk') else 'oh' if spec[nm]['oh'] else 'none'
        if b == 'none': continue
        v = float(np.nanmean(np.abs(R[nm]['mfChk']))); mf.setdefault(b, []).append(v)
    C.append(('(inspection, not a pass/fail check; check 7 rests on the build\'s unit test for the money accounts): `mfChk`, the Source-financing identity |U - (payout - matched)|, is 0 only on a '
              'Source-financed row; the main row is financed by the flat contribution, so it is not 0 there. Mean over seeds, per adult-year: the main rows %s; rows with the option %s to %s; '
              'with the produced backing %s to %s' % ('/'.join('%.0f' % v for v in mf['main']), '%.0f' % min(mf['oh']), '%.0f' % max(mf['oh']), '%.0f' % min(mf['bk']), '%.0f' % max(mf['bk'])), None, None))
    for (a_, b_), dk in conv.items(): C.append(('conv row %s equals %s in every key and seed (Amendment 2 item 9)' % (a_, b_), not dk, sorted(dk)[:10]))
    if sec:
        ok10 = not c10['diff'] and c10['rows'] == 48
        C.append(('check 10: the supplement\'s %d rows equal the batch in every key the batch holds, every seed' % c10['rows'], ok10, c10['diff'][:10]))
        if ok10:
            for nm, v in secS.items():
                for k, a in v.items(): R[nm][k] = np.array(a, dtype=float)
    SEC[(e, y)] = bool(sec and not c10['diff'])
    return R, spec, C


# ---------------------------------------------------------------- statistics
def est(d, extra=None):
    n = len(d); m = float(d.mean()); v = W @ d; sd = float(d.std(ddof=1))
    p = 1.0 if sd == 0 and m == 0 else 0.0 if sd == 0 else 2 * (1 - tcdf(abs(m) / (sd / math.sqrt(n)), n - 1))
    lo, hi = np.percentile(v, [2.5, 97.5])
    r = {'est': m, 'lo': float(lo), 'hi': float(hi), 'p': p, 'zero': bool(np.all(d == 0))}
    if extra: r.update(extra)
    return r


def lev(d):
    v = W @ d; lo, hi = np.percentile(v, [2.5, 97.5]); return {'est': float(d.mean()), 'lo': float(lo), 'hi': float(hi)}


def fm(x, k=None, d=None):
    if x is None: return '–'
    x = x * SCALE.get(k, 1.0); d = DIG.get(k, 2) if d is None else d
    return ('{:,.%df}' % d).format(x) if abs(x) >= 1000 else ('%.' + str(d) + 'f') % x


def ci(s, k=None):
    if s is None: return '–'
    if s.get('zero'): return '0 (identical in every seed)'
    return '%s (%s to %s)' % (fm(s['est'], k), fm(s['lo'], k), fm(s['hi'], k))


def pf(p): return '<0.001' if p < 0.001 else '%.3f' % p


def excl(s): return s['lo'] > 0 or s['hi'] < 0


class Folder:
    def __init__(self, R, spec, e, y): self.R, self.spec, self.e, self.y = R, spec, e, y
    def N(self, p): return self.spec[p]['none']
    def x(self, n, k): return self.R[n][k]
    def eff(self, p, k): return self.x(p, k) - self.x(self.N(p), k)
    def has(self, n): return n in self.R

    def pk(self, block):
        sav = 'secM3A' if block in ('A', 'F') and SEC.get((self.e, self.y)) else 'bNAPy'
        return [k for k, _, _ in CORE] + [sav]

    def cost(self, p, p0, k):
        """harm-signed costs of displacement and the offset, per seed"""
        s = -FAV[k]; n, n0 = self.N(p), self.N(p0)
        cN = s * (self.x(n, k) - self.x(n0, k)); cP = s * (self.x(p, k) - self.x(p0, k)); return cN, cP, cN - cP

    def offset(self, p, p0, keys):
        out = {}
        for k in keys:
            cN, cP, off = self.cost(p, p0, k); r = {'levN': lev(self.x(self.N(p), k)), 'levP': lev(self.x(p, k)), 'cN': est(cN), 'cP': est(cP), 'off': est(off)}
            if r['cN']['lo'] > 0:
                mN, mP = W @ cN, W @ cP; sh = 1 - mP / mN; lo, hi = np.percentile(sh, [2.5, 97.5])
                r['share'] = {'est': float(1 - cP.mean() / cN.mean()), 'lo': float(lo), 'hi': float(hi)}
            else: r['share'] = None; r['noShare'] = 'displacement improves this with no programme' if r['cN']['hi'] < 0 else 'no significant cost with no programme'
            out[k] = r
        return out

    def change(self, p, ref, keys):
        """the change a reading makes to the programme's effect, paired by seed, Holm across the primary readings"""
        out = {k: est(self.eff(p, k) - self.eff(ref, k)) for k in keys}
        prim = [k for k in keys if k in FAV and k not in ('endoAnn', 'fgt2PY')]
        ad = holm([out[k]['p'] for k in prim])
        for i, k in enumerate(prim): out[k]['holm'] = ad[i]
        return out

    def effects(self, p, keys): return {k: est(self.eff(p, k)) for k in keys}


def category(o, padj):
    if o['off']['zero'] or padj >= 0.05: return 'does not offset'
    if o['off']['est'] < 0: return 'worsens'
    return 'offsets fully' if o['cP']['lo'] <= 0 else 'offsets in part'


def crossing(m, f, lim=5.0):
    """f: inflation at the grid m (rising m, falling inflation expected); the m where f reaches lim, linear, never extrapolated"""
    if f[-1] > lim: return math.inf
    if f[0] <= lim: return -math.inf
    for i in range(len(m) - 1, 0, -1):
        if f[i - 1] > lim >= f[i]: return m[i - 1] + (m[i] - m[i - 1]) * (f[i - 1] - lim) / (f[i - 1] - f[i])
    return math.nan


def bes(b): return '%s (%s to %s)' % (be_str(b['est']), be_str(b['lo']), be_str(b['hi']))


def be_str(x):
    return 'above 1' if x == math.inf else 'at or below 0.25' if x == -math.inf else 'not monotone' if x != x else '%.2f' % x


# ---------------------------------------------------------------- analysis
def analyse(F):
    S = {'sec': SEC.get((F.e, F.y), False)}
    pkA = F.pk('A'); prim6 = F.pk('A')
    # Q1: block A
    A = {}
    for des in DES:
        p0 = 'A.%s.gain.D0' % des; cells = {}
        for D in D4:
            for f in FORMS: cells[(D, f)] = F.offset('A.%s.%s.D%s' % (des, f, g(D)), p0, pkA)
        ps = [cells[c][k]['off']['p'] for c in cells for k in pkA]; ad = holm(ps); i = 0
        for c in cells:
            for k in pkA: cells[c][k]['holm'] = ad[i]; cells[c][k]['cat'] = category(cells[c][k], ad[i]); i += 1
        eff = {nm: F.effects(nm, pkA + ['endoAnn', 'fgt2PY', 'bNAPy']) for nm in ['A.%s.off' % des, p0] + ['A.%s.%s.D%s' % (des, f, g(D)) for D in D4 for f in FORMS]}
        A[des] = {'cells': cells, 'eff': eff, 'gainOnly': F.change(p0, 'A.%s.off' % des, pkA + ['endoAnn'])}
    S['A'] = A
    pkB = F.pk('B')
    # Q2: form and order
    Q2 = {}
    for des in DES:
        Q2[des] = {'hoursVsJobs': {D: F.change('A.%s.hours.D%s' % (des, g(D)), 'A.%s.jobs.D%s' % (des, g(D)), pkB + ['endoAnn']) for D in D4},
                   'even': {f: {'chg': F.change('D.%s.even.%s.D0.5' % (des, f), 'A.%s.%s.D0.5' % (des, f), pkB + ['endoAnn']),
                                'off': F.offset('D.%s.even.%s.D0.5' % (des, f), 'A.%s.gain.D0' % des, pkB)} for f in FORMS}}
    S['Q2'] = Q2
    # Q3: the gain, its pass-through, the owners' share; who gains
    Q3 = {}
    for des in DES:
        ref = 'A.%s.jobs.D0.5' % des; q = {}
        for rd, p, p0 in (('no gain', 'B.%s.gnone.D0.5' % des, 'G.%s.zero' % des), ('high gain', 'B.%s.ghigh.D0.5' % des, 'B.%s.ghigh.D0' % des),
                          ('pass-through 0', 'B.%s.pw0.D0.5' % des, None), ('pass-through 1', 'B.%s.pw1.D0.5' % des, None),
                          ('owners\' share 0.5', 'D.%s.own0.5.D0.5' % des, None), ('owners\' share 1', 'D.%s.own1.D0.5' % des, None)):
            q[rd] = {'row': p, 'eff': F.effects(p, pkB + ['endoAnn']), 'chg': F.change(p, ref, pkB + ['endoAnn']), 'off': F.offset(p, p0, pkB) if p0 else None}
        q['high gain, no displacement'] = {'row': 'B.%s.ghigh.D0' % des, 'eff': F.effects('B.%s.ghigh.D0' % des, pkB + ['endoAnn']),
                                           'chg': F.change('B.%s.ghigh.D0' % des, 'A.%s.gain.D0' % des, pkB + ['endoAnn'])}
        who = {}
        for nm in ['A.%s.gain.D0' % des, 'A.%s.jobs.D0.5' % des, 'A.%s.hours.D0.5' % des, 'B.%s.ghigh.D0.5' % des, 'D.%s.own1.D0.5' % des]:
            who[nm] = {'lev': {k: {'N': lev(F.x(F.N(nm), k)), 'P': lev(F.x(nm, k))} for k in ['W1', 'W2', 'W3', 'W4', 'W5', 'wtT1E', 'ohLab', 'ohDiv', 'ohPaid']},
                       'eff': {k: est(F.eff(nm, k)) for k in ['W1', 'W2', 'W3', 'W4', 'W5', 'wtT1E', 'ohLab']}}
        q['who'] = who; Q3[des] = q
    S['Q3'] = Q3
    # Q4: the backing produced
    Q4 = {}
    for des in DES:
        rows = {}
        for nm in F.R:
            if not nm.startswith('E.%s.' % des): continue
            infl = F.x(nm, 'endoAnn') * 100; s = lev(infl)
            catg = 'backs enough' if s['hi'] <= 5 else 'does not back enough' if s['lo'] > 5 else 'uncertain'
            rows[nm] = {'infl': s, 'cat': catg, 'A': lev(F.x(nm, 'ohA')), 'A5': lev(F.x(nm, 'ohA5')), 'A10': lev(F.x(nm, 'ohA10')),
                        'A19': lev(F.x(nm, 'ohA19')), 'A39': lev(F.x(nm, 'ohA39')) if F.y == 40 else None, 'Mk': lev(F.x(nm, 'ohMk')),
                        'eff': F.effects(nm, pkB)}
        be = {}
        for D in [0, 0.3, 0.5, 0.7]:
            for gg in ['low', 'high']:
                ms = [0.25, 0.5, 1]; V = [F.x('E.%s.m%s.g%s.D%s' % (des, g(mm), gg, g(D)), 'endoAnn') * 100 for mm in ms]
                pt = crossing(ms, [float(v.mean()) for v in V]); BV = np.stack([W @ v for v in V], 1)
                bs = np.array([crossing(ms, list(b)) for b in BV]); fin = np.clip(bs[~np.isnan(bs)], -1.0, 9.0)  # -1: at or below 0.25; 9: above 1
                lo, hi = (np.percentile(fin, [2.5, 97.5], method='inverted_cdf') if len(fin) else (math.nan, math.nan))
                mp = lambda v: -math.inf if v == -1 else math.inf if v == 9 else float(v); lo, hi = mp(lo), mp(hi)
                be['D%s.%s' % (g(D), gg)] = {'est': pt, 'lo': float(lo), 'hi': float(hi), 'nonmono': int(np.isnan(bs).sum())}
        Q4[des] = {'rows': rows, 'be': be}
    S['Q4'] = Q4
    # Q5: displaced adults, both runs
    Q5 = {}
    for des in DES:
        q = {}
        for D in D4:
            for f in FORMS:
                nm = 'A.%s.%s.D%s' % (des, f, g(D))
                q[nm] = {k: {'N': lev(F.x(F.N(nm), k)), 'P': lev(F.x(nm, k)), 'eff': est(F.eff(nm, k))} for k in ['ohDN', 'ohDB', 'ohDW', 'ohDM', 'ohNB', 'ohNW', 'ohNM']}
        Q5[des] = q
    S['Q5'] = Q5
    # Q6: paid hours and free time
    Q6 = {}
    for des in DES:
        q = {}
        for nm in ['A.%s.%s.D%s' % (des, f, g(D)) for D in D4 for f in FORMS] + ['D.%s.kp.hours.D0.3' % des, 'D.%s.kp.hours.D0.5' % des]:
            q[nm] = {k: {'N': lev(F.x(F.N(nm), k)), 'P': lev(F.x(nm, k)), 'eff': est(F.eff(nm, k))} for k in ['ohH', 'ohHT', 'ohFree', 'ohFreeS', 'ohFreeI', 'ohFreeT', 'ohFreeST', 'ohFreeIT']}
        Q6[des] = q
    S['Q6'] = Q6
    # Q7: the design's maintained take-home
    S['Q7'] = {des: {D: {'chg': F.change('D.%s.kp.hours.D%s' % (des, g(D)), 'A.%s.hours.D%s' % (des, g(D)), pkB + ['endoAnn']),
                         'off': F.offset('D.%s.kp.hours.D%s' % (des, g(D)), 'A.%s.gain.D0' % des, pkB),
                         'offPlain': F.offset('A.%s.hours.D%s' % (des, g(D)), 'A.%s.gain.D0' % des, pkB)} for D in [0.3, 0.5]} for des in DES}
    # Q8: together, and its offsets (headline block)
    pkF = F.pk('F'); Q8 = {}
    for des in DES:
        q = {}
        for mm in [0.5, 1]:
            for gg in ['low', 'high']:
                for D in [0, 0.5]:
                    nm = 'F.%s.m%s.g%s.D%s' % (des, g(mm), gg, g(D)); e_ = 'E.%s.m%s.g%s.D%s' % (des, g(mm), gg, g(D))
                    infl = lev(F.x(nm, 'endoAnn') * 100)
                    q[nm] = {'eff': F.effects(nm, pkF + ['endoAnn']), 'chg': F.change(nm, e_, pkB + ['endoAnn']), 'infl': infl, 'A': lev(F.x(nm, 'ohA')),
                             'cat': 'backs enough' if infl['hi'] <= 5 else 'does not back enough' if infl['lo'] > 5 else 'uncertain'}
                p, p0 = 'F.%s.m%s.g%s.D0.5' % (des, g(mm), gg), 'F.%s.m%s.g%s.D0' % (des, g(mm), gg)
                o = F.offset(p, p0, pkF); ad = holm([o[k]['off']['p'] for k in pkF])
                for i, k in enumerate(pkF): o[k]['holm'] = ad[i]; o[k]['cat'] = category(o[k], ad[i])
                q['offset.m%s.g%s' % (g(mm), gg)] = o
        Q8[des] = q
    S['Q8'] = Q8
    # the slower path (block C) and the implied output per remaining hour
    QC = {}
    for des in DES:
        QC[des] = {D: {'eff': F.effects('C.%s.T40.D%s' % (des, g(D)), pkB + ['endoAnn']), 'off': F.offset('C.%s.T40.D%s' % (des, g(D)), 'A.%s.gain.D0' % des, pkB),
                       'chg': F.change('C.%s.T40.D%s' % (des, g(D)), 'A.%s.jobs.D%s' % (des, g(D)), pkB + ['endoAnn'])} for D in [0.3, 0.5, 0.7]}
    S['C'] = QC
    S['oph'] = {nm: {'OPH': float(F.x(nm, 'ohOPH').mean()), 'DT': float(F.x(nm, 'ohDT').mean()), 'GT': float(F.x(nm, 'ohGT').mean())}
                for nm in F.R if F.spec[nm]['oh'] and not nm.startswith('none.') and nm.split('.')[1] == 'c22'}
    return S


# ---------------------------------------------------------------- writing
SHORT = {'offsets fully': 'full', 'offsets in part': 'part', 'does not offset': 'none', 'worsens': 'WORSE'}


def sav_note(S): return ('savings: adult-years whose liquid savings cover under three months of need (`secM3A`, the supplement)' if S['sec'] else
                         'savings: below 30 days of basic living (`bNAPy`), the batch\'s nearest stored measure, until the supplement is read')


def unit(k): return '$' if UNIT.get(k) == '$' else 'points'


def w_q1(L, S, e):
    for des in DES:
        A = S['A'][des]; ks = list(A['cells'][(0.1, 'jobs')].keys())
        L += ['', '## %s, %s design' % (ENVL[e], DESL[des]), '', 'Categories after Holm across the 48 tests (six readings x eight cells). full: offsets fully; part: offsets in part; none: does not offset; WORSE: worsens.', '',
              '| D | form | ' + ' | '.join(LAB[k] for k in ks) + ' |', '|---|---|' + '---|' * len(ks)]
        for D in D4:
            for f in FORMS: L.append('| %s | %s | ' % (g(D), FL[f]) + ' | '.join(SHORT[A['cells'][(D, f)][k]['cat']] for k in ks) + ' |')
        for k in ks:
            L += ['', '### %s (%s; %s is better)' % (LAB[k], unit(k), 'lower' if FAV[k] < 0 else 'higher'), '',
                  '| D | form | no programme at D | programme at D | cost, no programme | cost, programme | offset | Holm p | offset share | category |', '|---|---|---|---|---|---|---|---|---|---|']
            for D in D4:
                for f in FORMS:
                    c = A['cells'][(D, f)][k]; sh = ('%.2f (%.2f to %.2f)' % (c['share']['est'], c['share']['lo'], c['share']['hi'])) if c['share'] else c['noShare']
                    L.append('| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (g(D), FL[f], fm(c['levN']['est'], k), fm(c['levP']['est'], k), ci(c['cN'], k), ci(c['cP'], k), ci(c['off'], k), pf(c['holm']), sh, c['cat']))
        L += ['', '### The programme\'s effect at each displacement (programme minus no programme; full backing)', '',
              '| row | ' + ' | '.join(LAB[k] for k in ks + ['endoAnn', 'fgt2PY']) + ' |', '|---|' + '---|' * (len(ks) + 2)]
        for nm, ef in A['eff'].items(): L.append('| `%s` | ' % nm + ' | '.join(ci(ef[k], k) for k in ks + ['endoAnn', 'fgt2PY']) + ' |')
        L += ['', 'The low gain alone (D 0) against the main row with the option off, change in the effect: ' + '; '.join('%s %s' % (LAB[k], ci(v, k)) for k, v in A['gainOnly'].items())]


def chg_line(c, ks):
    return ' | '.join(ci(c[k], k) + (' H' if 'holm' in c[k] and c[k]['holm'] < 0.05 and not c[k]['zero'] else '') for k in ks)


def w_off_table(L, title, rows, ks):
    L += ['', title, '', '| reading | ' + ' | '.join('%s: cost N / cost P / offset' % LAB[k] for k in ks) + ' |', '|---|' + '---|' * len(ks)]
    for nm, o in rows:
        if o: L.append('| %s | ' % nm + ' | '.join('%s / %s / %s' % (ci(o[k]['cN'], k), ci(o[k]['cP'], k), ci(o[k]['off'], k)) for k in ks) + ' |')


def write(out, ALL, CHK, eng):
    hdr = ('Generated by `python3 dev/tools/s85_tables.py` from compassionism-sim-results `s85-<env>-<years>-%s` (runner/jobs/s85.js, seeds 1-500, 500 adults). '
           'Effect: programme run minus its own no-programme run, mean over seeds; 95%% paired-bootstrap interval (10,000 replicates, generator seed 20261120). '
           'Preregistration: research-update `prereg/2026-11-s85-output-per-hour.md`, Amendments 1-3. H: survives Holm across the six primary readings of its cell. '
           'Blocks A-D run at full backing (a design parameter); decision rule 5 applies to any statement from them (see the backing produced).' % eng)
    L = ['# Output per hour and automation: the checks (before any table is read)', '', hdr, '']
    allok = all(ok is not False for c in CHK.values() for _, ok, _ in c)
    L += ['**All checks: %s.**' % ('PASS' if allok else 'NOT ALL PASS'), '', 'Check 5 (pairing): `node runner/jobs/s85.js --check` at the job\'s commit passes (every programme row\'s no-programme partner has the same both-run settings). Check 8 (draws): the build\'s unit test; nothing in the batch measures draws.']
    for fk, c in CHK.items():
        e, y = fk.split('-'); L += ['', '## %s, %s years' % (ENVL[e], y), '']
        for t, ok, det in c: L.append('- %s %s%s' % ('NOTE' if ok is None else 'PASS' if ok else 'FAIL', t, '' if ok is not False or not det else ': ' + str(det)))
    open(os.path.join(out, 's85-checks.md'), 'w').write('\n'.join(L) + '\n')
    for y in YEARS:
        sfx = '' if y == 20 else '-40y'; yl = '%d years' % y
        envs = [e for e in ENVS if '%s-%d' % (e, y) in ALL]
        if not envs: continue
        Ss = {e: ALL['%s-%d' % (e, y)] for e in envs}
        # Q1
        L = ['# Displacement and the programme: costs, offsets and categories (%s)' % yl, '', hdr, '', 'Savings reading: ' + '; '.join('%s: %s' % (ENVL[e], sav_note(Ss[e])) for e in envs) + '.',
             'Costs are harm-signed (positive = worse): poverty at D minus at D 0; median wealth at D 0 minus at D. Offset = cost with no programme minus cost with the programme. D 0.5 and 0.7 by year 20 are stress readings, beyond the forecasts (output per remaining hour would have to grow 3.5% and 6.2% a year above trend).']
        for e in envs: w_q1(L, Ss[e], e)
        open(os.path.join(out, 's85-q1-displacement%s.md' % sfx), 'w').write('\n'.join(L) + '\n')
        # Q2, Q3, Q7, C
        ks = Ss[envs[0]]['Q2']['c22']['hoursVsJobs'][0.5].keys(); ks = [k for k in ks]
        L = ['# Form, order, the gain, the owners\' share, the slower path and the design\'s take-home (%s)' % yl, '', hdr,
             'Savings reading in these blocks: below 30 days of basic living (`bNAPy`; not rerun with the security measures).']
        for e in envs:
            for des in DES:
                Q2, Q3, Q7, QC = Ss[e]['Q2'][des], Ss[e]['Q3'][des], Ss[e]['Q7'][des], Ss[e]['C'][des]
                L += ['', '## %s, %s design' % (ENVL[e], DESL[des]), '', '### Change in the programme\'s effect (paired; H: Holm across the six readings)', '',
                      '| reading | against | ' + ' | '.join(LAB[k] for k in ks) + ' |', '|---|---|' + '---|' * len(ks)]
                for D in D4: L.append('| shorter hours, D %s | lost jobs, D %s | ' % (g(D), g(D)) + chg_line(Q2['hoursVsJobs'][D], ks) + ' |')
                for f in FORMS: L.append('| even order, %s, D 0.5 | most exposed first | ' % FL[f] + chg_line(Q2['even'][f]['chg'], ks) + ' |')
                for rd, q in Q3.items():
                    if rd == 'who': continue
                    L.append('| %s, %s | %s | ' % (rd, 'D 0' if rd.endswith('no displacement') else 'lost jobs, D 0.5', 'low gain, D 0' if rd.endswith('no displacement') else 'main reading, D 0.5') + chg_line(q['chg'], ks) + ' |')
                for D in [0.3, 0.5]: L.append('| design\'s take-home, D %s | shorter hours, D %s | ' % (g(D), g(D)) + chg_line(Q7[D]['chg'], ks) + ' |')
                for D in [0.3, 0.5, 0.7]: L.append('| displacement reached at 40 years, D %s | at 20 years, D %s | ' % (g(D), g(D)) + chg_line(QC[D]['chg'], ks) + ' |')
                rows = [('even order, %s, D 0.5' % FL[f], Q2['even'][f]['off']) for f in FORMS] + [('%s, D 0.5' % rd, Q3[rd]['off']) for rd in ('no gain', 'high gain')] + \
                       [('design\'s take-home, D %s' % g(D), Q7[D]['off']) for D in [0.3, 0.5]] + [('shorter hours (plain), D %s' % g(D), Q7[D]['offPlain']) for D in [0.3, 0.5]] + \
                       [('reached at 40 years, D %s' % g(D), QC[D]['off']) for D in [0.3, 0.5, 0.7]]
                w_off_table(L, '### Displacement\'s cost and the offset in these readings (unadjusted 95% intervals; not headline cells)', rows, [k for k in ks if k != 'endoAnn'])
                L += ['', '### Who gains: mean real wealth at the last year by fifth of starting wealth, the top 1% share, the labour share (no programme / programme / effect)', '',
                      '| row | fifth 1 | fifth 2 | fifth 3 | fifth 4 | fifth 5 | top 1% share | labour share | dividend over wages | share paid in the model |', '|---|---|---|---|---|---|---|---|---|---|']
                for nm, w in Q3['who'].items():
                    L.append('| `%s` | ' % nm + ' | '.join('%s / %s / %s' % (fm(w['lev'][k]['N']['est'], k), fm(w['lev'][k]['P']['est'], k), ci(w['eff'][k], k)) for k in ['W1', 'W2', 'W3', 'W4', 'W5', 'wtT1E', 'ohLab'])
                             + ' | %s / %s | %s / %s |' % (fm(w['lev']['ohDiv']['N']['est']), fm(w['lev']['ohDiv']['P']['est']), fm(w['lev']['ohPaid']['N']['est']), fm(w['lev']['ohPaid']['P']['est'])))
        open(os.path.join(out, 's85-q2-q3-q7-readings%s.md' % sfx), 'w').write('\n'.join(L) + '\n')
        # Q4
        L = ['# The backing produced by the programme\'s own work (%s)' % yl, '', hdr,
             'Every row runs with nothing assumed backed; the produced output M_t replaces the project payout\'s valuation. m: the share of programme work whose output people or businesses would otherwise buy (goods and services alike; Amendment 1 item 8). Category by the 95% interval of programme inflation against 5 points a year. Produced share: over the run (and at years 5, 10, 19, 39). Savings reading: `bNAPy`.']
        for e in envs:
            for des in DES:
                Q = Ss[e]['Q4'][des]; L += ['', '## %s, %s design' % (ENVL[e], DESL[des]), '', '### Break-even m (programme inflation reaches 5 points a year; linear between m 0.25, 0.5, 1)', '',
                                             '| D | low gain | high gain |', '|---|---|---|']
                for D in [0, 0.3, 0.5, 0.7]:
                    L.append('| %s | ' % g(D) + ' | '.join(bes(Q['be']['D%s.%s' % (g(D), gg)]) for gg in ['low', 'high']) + ' |')
                kq = ['fgt0PY', 'ppovA', 'wtMedE', 'bNAPy']
                L += ['', '| row | programme inflation | category | produced share, run | year 5 | year 10 | year 19 | %scapital\'s part of M | ' % ('year 39 | ' if y == 40 else '') + ' | '.join(LAB[k] for k in kq) + ' |',
                      '|---|---|---|---|---|---|---|---|' + ('---|' if y == 40 else '') + '---|' * len(kq)]
                for nm in sorted(Q['rows']):
                    r = Q['rows'][nm]
                    L.append('| `%s` | %s | %s | %s | %s | %s | %s | %s%s | ' % (nm, ci(r['infl']), r['cat'], ci(r['A']), fm(r['A5']['est']), fm(r['A10']['est']), fm(r['A19']['est']),
                                                                       (fm(r['A39']['est']) + ' | ') if y == 40 else '', fm(r['Mk']['est'])) + ' | '.join(ci(r['eff'][k], k) for k in kq) + ' |')
        open(os.path.join(out, 's85-q4-backing%s.md' % sfx), 'w').write('\n'.join(L) + '\n')
        # Q5 and Q6
        L = ['# Where the programme falls short, and free time (%s)' % yl, '', hdr, '']
        for e in envs:
            for des in DES:
                L += ['', '## %s, %s design' % (ENVL[e], DESL[des]), '', '### Every block-A cell that does not offset or worsens (after Holm across 48)', '']
                bad = [(D, f, k, c[k]) for (D, f), c in Ss[e]['A'][des]['cells'].items() for k in c if c[k]['cat'] in ('does not offset', 'worsens')]
                L += ['- %s, D %s, %s: %s (offset %s; cost with no programme %s; with the programme %s)' % (FL[f], g(D), LAB[k], c['cat'], ci(c['off'], k), ci(c['cN'], k), ci(c['cP'], k)) for D, f, k, c in bad] or ['- none']
                L += ['', '### Displaced adults and the rest at the last year (no programme / programme / effect)', '',
                      '| row | displaced (count) | displaced: basket poverty % | displaced: wealth poverty % | displaced: median months of cover | rest: basket poverty % | rest: wealth poverty % | rest: median months of cover |', '|---|---|---|---|---|---|---|---|']
                for nm, q in Ss[e]['Q5'][des].items():
                    L.append('| `%s` | %s | ' % (nm, fm(q['ohDN']['P']['est'], 'ohDN')) + ' | '.join('%s / %s / %s' % (fm(q[k]['N']['est']), fm(q[k]['P']['est']), ci(q[k]['eff'])) for k in ['ohDB', 'ohDW', 'ohDM', 'ohNB', 'ohNW', 'ohNM']) + ' |')
                L += ['', '### Paid hours and free time per adult in paid work at the start (hours a year at 2,080 a full year; secure: household above its cost-of-living line that year)', '',
                      '| row | paid hours, mean over the run (% of the start) | free time, mean | of which secure | of which insecure | free time, last year | secure | insecure |', '|---|---|---|---|---|---|---|---|']
                for nm, q in Ss[e]['Q6'][des].items():
                    L.append('| `%s` | %s | ' % (nm, fm(q['ohH']['P']['est'])) + ' | '.join('%s / %s' % (fm(q[k]['N']['est'], k), fm(q[k]['P']['est'], k)) for k in ['ohFree', 'ohFreeS', 'ohFreeI', 'ohFreeT', 'ohFreeST', 'ohFreeIT']) + ' |')
        open(os.path.join(out, 's85-q5-q6-shortfall-free-time%s.md' % sfx), 'w').write('\n'.join(L) + '\n')
        # Q8
        L = ['# Together: the produced backing with the supply limit, wages made up a year later and the BU a month behind (%s)' % yl, '', hdr]
        for e in envs:
            L.append('Savings reading, %s: %s.' % (ENVL[e], sav_note(Ss[e])))
        for e in envs:
            for des in DES:
                Q = Ss[e]['Q8'][des]; kf = list(Q['offset.m1.glow'].keys())
                L += ['', '## %s, %s design' % (ENVL[e], DESL[des]), '', '| row | programme inflation | category | produced share | ' + ' | '.join(LAB[k] for k in kf) + ' |', '|---|---|---|---|' + '---|' * len(kf)]
                for nm in sorted(k for k in Q if not k.startswith('offset')):
                    L.append('| `%s` | %s | %s | %s | ' % (nm, ci(Q[nm]['infl']), Q[nm]['cat'], ci(Q[nm]['A'])) + ' | '.join(ci(Q[nm]['eff'][k], k) for k in kf) + ' |')
                kb = list(Q['F.%s.m1.glow.D0' % des]['chg'].keys())
                L += ['', '| change against the produced backing alone (same m, gain, D) | ' + ' | '.join(LAB[k] for k in kb) + ' |', '|---|' + '---|' * len(kb)]
                for nm in sorted(k for k in Q if not k.startswith('offset')): L.append('| `%s` | ' % nm + chg_line(Q[nm]['chg'], kb) + ' |')
                for ok_ in sorted(k for k in Q if k.startswith('offset')):
                    o = Q[ok_]; L += ['', '### Displacement at D 0.5 (lost jobs), %s: cost, offset and category (Holm across the six readings)' % ok_.replace('offset.', ''), '',
                                      '| reading | cost, no programme | cost, programme | offset | Holm p | category |', '|---|---|---|---|---|---|']
                    for k in kf: L.append('| %s | %s | %s | %s | %s | %s |' % (LAB[k], ci(o[k]['cN'], k), ci(o[k]['cP'], k), ci(o[k]['off'], k), pf(o[k]['holm']), o[k]['cat']))
        open(os.path.join(out, 's85-q8-together%s.md' % sfx), 'w').write('\n'.join(L) + '\n')
    js = san(keystr(ALL))
    json.dump({'checks': {k: [[t, ok] for t, ok, _ in c] for k, c in CHK.items()}, 'results': js}, open(os.path.join(out, 's85-summary.json'), 'w'))


def san(d):
    if isinstance(d, dict): return {k: san(v) for k, v in d.items()}
    if isinstance(d, (list, tuple)): return [san(v) for v in d]
    if isinstance(d, float): return None if d != d else 'inf' if d == math.inf else '-inf' if d == -math.inf else d
    return d


def keystr(d):
    if isinstance(d, dict): return {(str(k) if not isinstance(k, tuple) else '.'.join(g(x) if isinstance(x, float) else str(x) for x in k)): keystr(v) for k, v in d.items()}
    return d


def main():
    global W, REPS
    src, out = sys.argv[1], sys.argv[2]
    eng = sys.argv[sys.argv.index('--engine') + 1] if '--engine' in sys.argv else '503fa48'
    if '--reps' in sys.argv: REPS = int(sys.argv[sys.argv.index('--reps') + 1])
    use_sec = '--nosec' not in sys.argv
    os.makedirs(out, exist_ok=True)
    rng = np.random.default_rng(20261120); idx = rng.integers(0, NS, size=(REPS, NS))
    W = np.zeros((REPS, NS))
    for b in range(REPS): W[b] = np.bincount(idx[b], minlength=NS) / NS
    ALL, CHK = {}, {}
    only = sys.argv[sys.argv.index('--only') + 1].split(',') if '--only' in sys.argv else None  # testing: e.g. ref-20 (the tables need all six)
    for e in ENVS:
        for y in YEARS:
            if only and '%s-%d' % (e, y) not in only: continue
            R, spec, C = load(src, e, y, eng, use_sec)
            CHK['%s-%d' % (e, y)] = C
            ALL['%s-%d' % (e, y)] = analyse(Folder(R, spec, e, y))
            print('done %s %d (supplement %s)' % (e, y, SEC.get((e, y))), file=sys.stderr)
            del R
    write(out, ALL, CHK, eng)


if __name__ == '__main__':
    main()
