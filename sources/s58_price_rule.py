"""S58 (Nov 9, 2026; research-update prereg/2026-11-s58-price-rule.md): the capacity price rule's sourced and derived parameters
(index.html PR_DEFAULTS: k, r, h, um; the cost share a is CFG's MULT_LS, sourced earlier).

Sources: FRED (Federal Reserve Bank of St. Louis), fredgraph.csv?id=<series>, downloaded Nov 9, 2026; each file's sha256 is printed.
- GDPC1  real GDP (BEA), quarterly;  GDPPOT  real potential GDP (CBO), quarterly. Output gap = ln(GDPC1/GDPPOT); annual = mean of the quarters.
- TCU  capacity utilisation, total industry (Federal Reserve G.17);  CAPUTLG311S  the same, food manufacturing (NAICS 311); monthly, %.
- RRVRUSQ156N  rental vacancy rate (Census, Housing Vacancy Survey); quarterly, %.
- CPIAUCSL  CPI-U, all items, seasonally adjusted (BLS); monthly. Annual inflation = ln change of the annual average (complete years only; 2025 lacks
  October, not collected, so the regression ends in 2024).
Derived:
- k, k2, r: OLS of inflation(t) on 1, inflation(t-1), max(0, gap(t-1)) and min(0, gap(t-1)) (the rule's form: separate slopes above and below
  potential), 1960-2024. k = the slope above, k2 = the slope below; persistence = the lag coefficient; r = persistence - a x wIdx (a = MULT_LS 0.5079,
  wIdx 1), since the rule's wage channel already carries that much of last year's inflation. Printed beside it: the one-sided form (the
  preregistration's first form, before Amendment 1), the two-sided form, and the subperiods 1960-1983 and 1984-2024 (the sweep's ends).
- h (normal-years slack, log, floored at 0): CBO gap 2025; food manufacturing 2025 against its 1972-2025 mean; rental occupancy (100 - vacancy) 2025
  against its 1956-2025 mean. The reading: total industry 2025 against its 1972-2025 mean.
- um (reporting only): the largest positive quarterly CBO gap since 1949.
Usage: python3 sources/s58_price_rule.py sources/s58_fred [--fetch] > sources/s58_price_rule.json   (the directory holds <series>.csv as downloaded; --fetch downloads them again; standard library only)
"""
import csv, hashlib, json, math, os, statistics as st, sys, urllib.request

SERIES = ['GDPC1', 'GDPPOT', 'TCU', 'CAPUTLG311S', 'RRVRUSQ156N', 'CPIAUCSL']
A_LABOUR = 62784.912/123630.857  # index.html MULT_LS: compensation of employees over gross domestic income, 2025
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
def by_year(x, n):
    a = {}
    for d, v in x.items(): a.setdefault(d[:4], []).append(v)
    return {y: st.mean(v) for y, v in a.items() if len(v) == n}
def ols(X, Y):
    k = len(X[0]); n = len(Y)
    M = [[sum(X[i][a]*X[i][b] for i in range(n)) for b in range(k)] + [1.0 if a == j else 0.0 for j in range(k)] for a in range(k)]
    for i in range(k):
        pv = M[i][i]; M[i] = [v/pv for v in M[i]]
        for r in range(k):
            if r != i: f = M[r][i]; M[r] = [M[r][j] - f*M[i][j] for j in range(2*k)]
    inv = [row[k:] for row in M]; xy = [sum(X[i][a]*Y[i] for i in range(n)) for a in range(k)]
    b = [sum(inv[a][c]*xy[c] for c in range(k)) for a in range(k)]
    res = [Y[i] - sum(X[i][j]*b[j] for j in range(k)) for i in range(n)]; s2 = sum(e*e for e in res)/(n - k)
    return b, [math.sqrt(s2*inv[i][i]) for i in range(k)], n
g, p = rd('GDPC1'), rd('GDPPOT')
gapQ = {d: math.log(g[d]/p[d]) for d in g if d in p}
gapA = by_year(gapQ, 4)
cpi = by_year(rd('CPIAUCSL'), 12)
inf = {y: math.log(cpi[y]/cpi[str(int(y) - 1)]) for y in cpi if str(int(y) - 1) in cpi}
def phillips(a, b, form):
    X, Y = [], []
    for t in range(a, b + 1):
        T, P = str(t), str(t - 1)
        if T in inf and P in inf and P in gapA:
            gp = gapA[P]; X.append([1, inf[P]] + ([max(0, gp), min(0, gp)] if form == 'asymmetric' else [max(0, gp)] if form == 'one-sided' else [gp])); Y.append(inf[T])
    c, se, n = ols(X, Y)
    r = {'years': [a, b], 'n': n, 'form': form, 'const': round(c[0], 4), 'persistence': round(c[1], 3), 'persistenceSE': round(se[1], 3), 'slope': round(c[2], 3), 'slopeSE': round(se[2], 3)}
    if form == 'asymmetric': r.update({'slopeBelow': round(c[3], 3), 'slopeBelowSE': round(se[3], 3)})
    return r
reg = [phillips(a, b, f) for (a, b) in [(1960, 2024), (1960, 1983), (1984, 2024)] for f in ('asymmetric', 'one-sided', 'two-sided')]
main = reg[0]
tcu, food, vac = rd('TCU'), rd('CAPUTLG311S'), rd('RRVRUSQ156N')
def mean_years(x, a, b): return st.mean([v for d, v in x.items() if a <= int(d[:4]) <= b])
gap25 = gapA['2025']
tcu25, tcuLR = mean_years(tcu, 2025, 2025), mean_years(tcu, 1972, 2025)
food25, foodLR = mean_years(food, 2025, 2025), mean_years(food, 1972, 2025)
vac25, vacLR = mean_years(vac, 2025, 2025), mean_years(vac, 1956, 2025)
mx = max(gapQ.items(), key=lambda z: z[1])
out = {'files': {s: sha(s) for s in SERIES},
       'phillips': reg,
       'k': main['slope'], 'k2': main['slopeBelow'], 'k2High': reg[3]['slopeBelow'], 'persistence': main['persistence'], 'a': round(A_LABOUR, 4),
       'r': round(main['persistence'] - A_LABOUR, 3), 'rAnchored': round(max(0.0, reg[6]['persistence'] - A_LABOUR), 3), 'rMax': round(1 - A_LABOUR, 3),
       'slack': {'cboGap2025': round(math.exp(gap25) - 1, 4), 'hGeneral': round(max(0.0, -gap25), 4),
                 'food2025': round(food25, 2), 'foodMean1972_2025': round(foodLR, 2), 'hFood': round(max(0.0, math.log(foodLR/food25)), 4),
                 'vacancy2025': round(vac25, 2), 'vacancyMean1956_2025': round(vacLR, 2), 'hHousing': round(max(0.0, math.log((100 - vacLR)/(100 - vac25))), 4),
                 'tcu2025': round(tcu25, 2), 'tcuMean1972_2025': round(tcuLR, 2), 'hGeneralIndustryReading': round(max(0.0, math.log(tcuLR/tcu25)), 4)},
       'um': {'maxGapQuarter': mx[0], 'maxGap': round(math.exp(mx[1]) - 1, 4), 'um': round(mx[1], 4)}}
print(json.dumps(out, indent=1))
