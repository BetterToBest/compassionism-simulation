"""S67 (Nov 13, 2026; research-update prereg/2026-11-s67-price-rule-derivation.md, A2): the capacity price rule's response speed estimated on the
rule's own variable, the gap between the money-implied price level and prices (the price-gap or P-star form), beside S58's output-gap regression.

Sources: FRED (Federal Reserve Bank of St. Louis), fredgraph.csv?id=<series>, downloaded Nov 13, 2026; each file's sha256 is printed.
- M2SL  M2 (Federal Reserve H.6), monthly, from 1959;  GDP  nominal GDP (BEA), quarterly;  GDPC1  real GDP;  GDPPOT  real potential GDP (CBO);
  GDPDEF  GDP deflator;  CPIAUCSL  CPI-U (BLS), monthly. Annual (quarterly) values are means over complete years (quarters); 2025 lacks October's
  CPI (not collected), so annual samples end in 2024, as S58.
The form (stated in Tatom 1992, St. Louis Fed WP 1992-001A, for Hallman, Porter and Small 1991, whose article could not be opened):
  P* = M V*/Q*, so the price gap g = p* - p = (v* - v) + (output gap), v = ln(GDP/M2), v* = trend velocity. Three readings of v*:
  const  the estimation sample's mean (the 1991 form);  trail  the mean of v over the ten years (40 quarters) before (one-sided: no future data; MAIN);
  hp     a two-sided Hodrick-Prescott trend (lambda 100 annual, 1600 quarterly).
Forms (OLS; Newey-West errors, Bartlett kernel, lag floor(4 (T/100)^(2/9)); plain OLS errors beside them):
  F0  S58's regression: pi(t) on 1, pi(t-1), max(0, output gap(t-1)), min(0, output gap(t-1))
  F1  the rule's form:  pi(t) on 1, pi(t-1), max(0, g(t-1)), min(0, g(t-1))
  F2  two-sided:        pi(t) on 1, pi(t-1), g(t-1)
  F3  error correction: pi(t) - pi(t-1) on 1, g(t-1)
  F4  the two parts apart: pi(t) on 1, pi(t-1), (v* - v)(t-1), output gap(t-1); t-statistic of the difference of the two slopes (the form's restriction)
pi: the log change of CPI-U (main: only the gap variable differs from S58) and of the GDP deflator.
Derived readings (rules fixed in the preregistration): pg = F1, CPI-U, trail, full sample: k = slope above, k2 = slope below (each floored at 0),
r = max(0, persistence - a); wy = F0 at quarterly frequency, full sample, the same rule (per quarter).
Usage: python3 sources/s67_pstar.py sources/s67_fred [--fetch] > sources/s67_pstar.json     (standard library only)
"""
import csv, hashlib, json, math, os, statistics as st, sys, urllib.request

SERIES = ['M2SL', 'GDP', 'GDPC1', 'GDPPOT', 'GDPDEF', 'CPIAUCSL']
A_LABOUR = 62784.912/123630.857  # index.html MULT_LS
D = sys.argv[1]
if '--fetch' in sys.argv:
    os.makedirs(D, exist_ok=True)
    for s in SERIES: urllib.request.urlretrieve('https://fred.stlouisfed.org/graph/fredgraph.csv?id=' + s, os.path.join(D, s + '.csv'))
def rd(s):
    out = {}
    with open(os.path.join(D, s + '.csv')) as f:
        for r in csv.DictReader(f):
            k = list(r.keys()); v = r[k[1]]
            if v not in ('', '.'): out[r[k[0]]] = float(v)
    return out
def sha(s): return hashlib.sha256(open(os.path.join(D, s + '.csv'), 'rb').read()).hexdigest()
def per(x, n, quarterly):
    """Means over complete periods: key = year (annual) or 4*year + quarter index (quarterly); n observations expected per period."""
    a = {}
    for d, v in x.items():
        y, m = int(d[:4]), int(d[5:7]); a.setdefault(4*y + (m - 1)//3 if quarterly else y, []).append(v)
    return {k: st.mean(v) for k, v in a.items() if len(v) == n}

# ---- small linear algebra (lists) ----
def solve(A, B):
    n = len(A); M = [list(A[i]) + list(B[i]) for i in range(n)]; m = len(M[0])
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c])); M[c], M[p] = M[p], M[c]
        d = M[c][c]; M[c] = [v/d for v in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]; M[r] = [a - f*b for a, b in zip(M[r], M[c])]
    return [row[n:] for row in M]
def ols(X, Y):
    """Coefficients, OLS errors, Newey-West errors and covariance, R2."""
    n, k = len(X), len(X[0])
    XtX = [[sum(X[t][i]*X[t][j] for t in range(n)) for j in range(k)] for i in range(k)]
    inv = solve(XtX, [[1.0 if i == j else 0.0 for j in range(k)] for i in range(k)])
    Xty = [sum(X[t][i]*Y[t] for t in range(n)) for i in range(k)]
    b = [sum(inv[i][j]*Xty[j] for j in range(k)) for i in range(k)]
    e = [Y[t] - sum(b[i]*X[t][i] for i in range(k)) for t in range(n)]
    s2 = sum(v*v for v in e)/(n - k); se = [math.sqrt(s2*inv[i][i]) for i in range(k)]
    L = int(math.floor(4*(n/100.0)**(2.0/9.0)))
    S = [[0.0]*k for _ in range(k)]
    for l in range(0, L + 1):
        w = 1.0 if l == 0 else 1.0 - l/(L + 1.0)
        for t in range(l, n):
            for i in range(k):
                for j in range(k):
                    g = X[t][i]*e[t]*e[t - l]*X[t - l][j]
                    S[i][j] += w*g
                    if l > 0: S[j][i] += w*g
    S = [[v*n/(n - k) for v in row] for row in S]
    V = [[sum(inv[i][a]*S[a][c]*inv[c][j] for a in range(k) for c in range(k)) for j in range(k)] for i in range(k)]
    ym = sum(Y)/n; r2 = 1 - sum(v*v for v in e)/sum((y - ym)**2 for y in Y)
    return b, se, [math.sqrt(max(0.0, V[i][i])) for i in range(k)], V, r2, L
def hp(y, lam):
    n = len(y); A = [[0.0]*n for _ in range(n)]
    for i in range(n): A[i][i] = 1.0
    for i in range(n - 2):
        d = [1.0, -2.0, 1.0]
        for a in range(3):
            for c in range(3): A[i + a][i + c] += lam*d[a]*d[c]
    return [r[0] for r in solve(A, [[v] for v in y])]

def build(quarterly):
    q = quarterly; n1, n3 = (1, 3) if q else (4, 12)
    m2, gdp, y, ypot, pdef, cpi = per(rd('M2SL'), n3, q), per(rd('GDP'), n1, q), per(rd('GDPC1'), n1, q), per(rd('GDPPOT'), n1, q), per(rd('GDPDEF'), n1, q), per(rd('CPIAUCSL'), n3, q)
    if not q:  # S58: the annual output gap is the mean of the quarterly log gaps
        yq, pq = rd('GDPC1'), rd('GDPPOT'); og = per({d: math.log(yq[d]/pq[d]) for d in yq if d in pq}, 4, False)
    else: og = {k: math.log(y[k]/ypot[k]) for k in y if k in ypot}
    v = {k: math.log(gdp[k]/m2[k]) for k in gdp if k in m2}
    return {'og': og, 'v': v, 'pi_cpi': {k: math.log(cpi[k]/cpi[k - 1]) for k in cpi if k - 1 in cpi}, 'pi_def': {k: math.log(pdef[k]/pdef[k - 1]) for k in pdef if k - 1 in pdef}}

def vstar(Dt, kind, quarterly, lo, hi):
    v = Dt['v']; ks = sorted(v); W = 40 if quarterly else 10
    if kind == 'const':
        m = st.mean(v[k - 1] for k in range(lo, hi + 1)); return {k: m for k in ks}
    if kind == 'trail': return {k: st.mean(v[j] for j in range(k - W, k)) for k in ks if all(j in v for j in range(k - W, k))}
    t = hp([v[k] for k in ks], 1600.0 if quarterly else 100.0); return dict(zip(ks, t))

def fit(Dt, form, pi, kind, quarterly, lo, hi):
    P = Dt[pi]; og = Dt['og']; vs = vstar(Dt, kind, quarterly, lo, hi) if form != 'F0' else None
    X, Y = [], []
    for t in range(lo, hi + 1):
        l = t - 1
        if form == 'F0': terms = [P[l], max(0.0, og[l]), min(0.0, og[l])]
        else:
            vg = vs[l] - Dt['v'][l]; g = vg + og[l]
            terms = {'F1': [P[l], max(0.0, g), min(0.0, g)], 'F2': [P[l], g], 'F3': [g], 'F4': [P[l], vg, og[l]]}[form]
        X.append([1.0] + terms); Y.append(P[t] - (P[l] if form == 'F3' else 0.0))
    b, se, nw, V, r2, L = ols(X, Y)
    names = {'F0': ['const', 'persistence', 'slopeAbove', 'slopeBelow'], 'F1': ['const', 'persistence', 'slopeAbove', 'slopeBelow'], 'F2': ['const', 'persistence', 'slope'],
             'F3': ['const', 'slope'], 'F4': ['const', 'persistence', 'slopeVelocityGap', 'slopeOutputGap']}[form]
    lab = (lambda k: '%dQ%d' % (k//4, k % 4 + 1)) if quarterly else str
    r = {'freq': 'quarterly' if quarterly else 'annual', 'form': form, 'inflation': pi[3:], 'vstar': kind if form != 'F0' else None, 'sample': [lab(lo), lab(hi)], 'n': len(Y), 'nwLag': L, 'r2': round(r2, 3)}
    for i, nm in enumerate(names): r[nm] = round(b[i], 4); r[nm + 'SE'] = round(nw[i], 4); r[nm + 'OLSSE'] = round(se[i], 4)
    if form == 'F4':
        d = b[2] - b[3]; sd = math.sqrt(max(1e-18, V[2][2] + V[3][3] - 2*V[2][3])); r['equalSlopesT'] = round(d/sd, 2)
    if form in ('F0', 'F1'):
        d = b[2] - b[3]; sd = math.sqrt(max(1e-18, V[2][2] + V[3][3] - 2*V[2][3])); r['asymmetryT'] = round(d/sd, 2)
    return r

def reading(r):
    return {'k': round(max(0.0, r['slopeAbove']), 4), 'k2': round(max(0.0, r['slopeBelow']), 4), 'r': round(max(0.0, r['persistence'] - A_LABOUR), 4), 'a': round(A_LABOUR, 4),
            'kRaw': r['slopeAbove'], 'k2Raw': r['slopeBelow'], 'persistence': r['persistence'], 'from': {k: r[k] for k in ('freq', 'form', 'inflation', 'vstar', 'sample')}}

out = {'files': {s: sha(s) for s in SERIES}, 'regressions': []}
for quarterly in (False, True):
    Dt = build(quarterly); key = (lambda y, qn=0: 4*y + qn) if quarterly else (lambda y, qn=0: y)
    S = {'full': (key(1960), key(2024, 3)), 'early': (key(1960), key(1983, 3)), 'late': (key(1984), key(2024, 3))}
    T = {'full': (key(1970), key(2024, 3)), 'early': (key(1970), key(1983, 3)), 'late': (key(1984), key(2024, 3))}
    for pi in ('pi_cpi', 'pi_def'):
        for nm in ('full', 'early', 'late'):
            out['regressions'].append(fit(Dt, 'F0', pi, None, quarterly, *S[nm]))
            if nm != 'late': out['regressions'].append(fit(Dt, 'F0', pi, None, quarterly, *T[nm]))  # the same years as the trailing-trend sample
            for kind in ('const', 'trail', 'hp'):
                lo, hi = (T if kind == 'trail' else S)[nm]
                for form in ('F1', 'F2', 'F3', 'F4'): out['regressions'].append(fit(Dt, form, pi, kind, quarterly, lo, hi))
    if not quarterly:
        v = Dt['v']; out['velocityM2'] = {str(k): round(math.exp(v[k]), 3) for k in sorted(v) if k % 5 == 0 or k == 2024}
        out['pg'] = reading(fit(Dt, 'F1', 'pi_cpi', 'trail', False, *T['full']))
        e, l = fit(Dt, 'F1', 'pi_cpi', 'trail', False, *T['early']), fit(Dt, 'F1', 'pi_cpi', 'trail', False, *T['late'])
        f = fit(Dt, 'F1', 'pi_cpi', 'trail', False, *T['full'])
        out['decisionRule2a'] = {'fullSlopeAbove': f['slopeAbove'], 'se': f['slopeAboveSE'], 'ci95': [round(f['slopeAbove'] - 1.96*f['slopeAboveSE'], 4), round(f['slopeAbove'] + 1.96*f['slopeAboveSE'], 4)],
                                 'early': e['slopeAbove'], 'late': l['slopeAbove'],
                                 'identified': bool(abs(f['slopeAbove']) > 1.96*f['slopeAboveSE'] and e['slopeAbove']*f['slopeAbove'] > 0 and l['slopeAbove']*f['slopeAbove'] > 0)}
    else:
        out['wy'] = reading(fit(Dt, 'F0', 'pi_cpi', None, True, *S['full']))
json.dump(out, sys.stdout, indent=1)
