"""S67 (Nov 13, 2026; research-update prereg/2026-11-s67-price-rule-derivation.md, A3): how inflation behaves in episodes of sustained high inflation.

Source: World Bank, World Development Indicators, through its API (api.worldbank.org/v2/country/all/indicator/<code>?format=json&per_page=20000&date=1960:2025;
database last updated 2026-11-11; downloaded Nov 13, 2026): FP.CPI.TOTL.ZG consumer prices (annual %), FM.LBL.BMNY.ZG broad money growth (annual %),
NY.GDP.MKTP.KD.ZG real GDP growth (annual %), and the country list (aggregates dropped). --fetch downloads them again and rewrites
sources/s67_wdi/panel.csv (iso3, year, the three series; the country-years with at least one value) and sources/s67_wdi/raw_sha256.json (the hash of each
response as downloaded; the raw responses, 11 MB, are not kept).
Logs throughout: pi = ln(1 + inflation), mu = ln(1 + broad money growth), y = ln(1 + real growth).
An episode: at least three consecutive years in one country with inflation of 20% or more and all three series present.
  P1 persistence: pi(t) on pi(t-1) inside episodes, pooled and with episode fixed effects; pooled by band of last year's inflation.
  P2 the rule's own form: pi(t) = a + phi pi(t-1) + kappa x(t-1), x = the cumulative sum of mu - y - pi since the episode began (minus the cumulative change
     in log velocity); pooled and with episode fixed effects.
  P3 inflation against money: per episode the mean of pi - (mu - y) (velocity growth); the share of episodes where it is positive; the median; the
     cross-section slope of episode-mean pi on episode-mean mu - y.
  P4 the velocity response: the change in log velocity (pi + y - mu) on the change in pi inside episodes, pooled (beta, in years), and in levels with
     episode fixed effects.
Standard errors clustered by country. Every estimate with and without the years above 1,000% a year.
Usage: python3 sources/s67_panel.py sources/s67_wdi [--fetch] > sources/s67_panel.json     (standard library only)
"""
import csv, hashlib, json, math, os, statistics as st, sys, urllib.request

CODES = ['FP.CPI.TOTL.ZG', 'FM.LBL.BMNY.ZG', 'NY.GDP.MKTP.KD.ZG']
D = sys.argv[1]; CSV = os.path.join(D, 'panel.csv')
if '--fetch' in sys.argv:
    os.makedirs(D, exist_ok=True); raw = {}; hs = {}
    def get(u):
        f = os.path.join(D, u[0]);
        if not os.path.exists(f): urllib.request.urlretrieve(u[1], f)
        b = open(f, 'rb').read(); hs[u[0]] = hashlib.sha256(b).hexdigest(); return json.loads(b)
    cs = get(('countries.json', 'https://api.worldbank.org/v2/country?format=json&per_page=400'))
    ok = {c['id'] for c in cs[1] if c['region']['value'] != 'Aggregates'}
    for c in CODES:
        d = get((c + '.json', 'https://api.worldbank.org/v2/country/all/indicator/' + c + '?format=json&per_page=20000&date=1960:2025'))
        hs[c + ' lastupdated'] = d[0]['lastupdated']
        for r in d[1]:
            if r['countryiso3code'] in ok and r['value'] is not None: raw.setdefault((r['countryiso3code'], int(r['date'])), {})[c] = r['value']
    with open(CSV, 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['iso3', 'year', 'cpi_pct', 'broad_money_pct', 'real_gdp_pct'])
        for k in sorted(raw): w.writerow([k[0], k[1]] + [repr(raw[k][c]) if c in raw[k] else '' for c in CODES])
    json.dump(hs, open(os.path.join(D, 'raw_sha256.json'), 'w'), indent=1)

rows = {}
for r in csv.DictReader(open(CSV)):
    if r['cpi_pct'] and r['broad_money_pct'] and r['real_gdp_pct']:
        c, m, g = float(r['cpi_pct']), float(r['broad_money_pct']), float(r['real_gdp_pct'])
        if c > -100 and m > -100 and g > -100: rows[(r['iso3'], int(r['year']))] = (c, math.log(1 + c/100), math.log(1 + m/100), math.log(1 + g/100))
# episodes
eps = []
for iso in sorted({k[0] for k in rows}):
    ys = sorted(y for (i, y) in rows if i == iso and rows[(i, y)][0] >= 20.0); run = []
    for y in ys + [None]:
        if run and (y is None or y != run[-1] + 1):
            if len(run) >= 3: eps.append((iso, run))
            run = []
        if y is not None: run.append(y)
HYPER = math.log(11.0)

def solve(A, B):
    n = len(A); M = [list(A[i]) + list(B[i]) for i in range(n)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c])); M[c], M[p] = M[p], M[c]
        d = M[c][c]; M[c] = [v/d for v in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]; M[r] = [a - f*b for a, b in zip(M[r], M[c])]
    return [row[n:] for row in M]
def ols(obs, fe):
    """obs: list of (cluster, group, y, [x...]). fe: demean by group (no constant) or add a constant. Cluster-robust errors by cluster."""
    if len(obs) < 8: return None
    if fe:
        gm = {}
        for o in obs: gm.setdefault(o[1], []).append(o)
        obs2 = []
        for g, L in gm.items():
            if len(L) < 2: continue
            my = st.mean(o[2] for o in L); mx = [st.mean(o[3][j] for o in L) for j in range(len(L[0][3]))]
            obs2 += [(o[0], g, o[2] - my, [o[3][j] - mx[j] for j in range(len(mx))]) for o in L]
        obs = obs2; X = [o[3] for o in obs]; dfx = len({o[1] for o in obs})
    else: X = [[1.0] + list(o[3]) for o in obs]; dfx = 0
    Y = [o[2] for o in obs]; n, k = len(X), len(X[0])
    XtX = [[sum(X[t][i]*X[t][j] for t in range(n)) for j in range(k)] for i in range(k)]
    inv = solve(XtX, [[1.0 if i == j else 0.0 for j in range(k)] for i in range(k)])
    b = [sum(inv[i][j]*sum(X[t][j]*Y[t] for t in range(n)) for j in range(k)) for i in range(k)]
    e = [Y[t] - sum(b[i]*X[t][i] for i in range(k)) for t in range(n)]
    sc = {}
    for t in range(n):
        s = sc.setdefault(obs[t][0], [0.0]*k)
        for i in range(k): s[i] += X[t][i]*e[t]
    G = len(sc); S = [[sum(s[i]*s[j] for s in sc.values()) for j in range(k)] for i in range(k)]
    adj = G/(G - 1.0)*(n - 1.0)/(n - k - dfx)
    V = [[adj*sum(inv[i][a]*S[a][c]*inv[c][j] for a in range(k) for c in range(k)) for j in range(k)] for i in range(k)]
    off = 0 if fe else 1
    return {'n': n, 'clusters': G, 'coef': [round(v, 4) for v in b[off:]], 'se': [round(math.sqrt(max(0.0, V[i][i])), 4) for i in range(off, k)], 'const': None if fe else round(b[0], 4)}

def analyse(drop_hyper):
    P1, P2, P4, P4L, P3 = [], [], [], [], []
    for n, (iso, run) in enumerate(eps):
        R = [rows[(iso, y)] for y in run]; x = 0.0; v = 0.0; X = []; Vv = []
        for r in R: x += r[2] - r[3] - r[1]; X.append(x)
        keep = [not (drop_hyper and r[1] > HYPER) for r in R]
        for t in range(1, len(R)):
            v += R[t][1] + R[t][3] - R[t][2]
            if keep[t] and keep[t - 1]:
                P1.append((iso, n, R[t][1], [R[t - 1][1]])); P2.append((iso, n, R[t][1], [R[t - 1][1], X[t - 1]]))
                P4.append((iso, n, R[t][1] + R[t][3] - R[t][2], [R[t][1] - R[t - 1][1]]))
            if keep[t]: P4L.append((iso, n, v, [R[t][1]]))
        K = [r for r, k in zip(R, keep) if k]
        if len(K) >= 3: P3.append((iso, n, st.mean(r[1] for r in K), [st.mean(r[2] - r[3] for r in K)], len(K)))
    band = lambda lo, hi: [o for o in P1 if lo <= math.exp(o[3][0]) - 1 < hi]
    vg = [o[2] - o[3][0] for o in P3]
    out = {'episodes': len(P3), 'countries': len({o[0] for o in P3}), 'countryYears': sum(o[4] for o in P3), 'medianLength': st.median(o[4] for o in P3),
           'medianInflationPct': round(100*(math.exp(st.median(o[2] for o in P3)) - 1), 1),
           'P1': {'pooled': ols(P1, False), 'episodeFE': ols(P1, True), 'band20to50': ols(band(0.2, 0.5), False), 'band50to100': ols(band(0.5, 1.0), False), 'bandOver100': ols(band(1.0, 1e9), False)},
           'P2': {'pooled': ols(P2, False), 'episodeFE': ols(P2, True)},
           'P3': {'meanVelocityGrowth': round(st.mean(vg), 4), 'medianVelocityGrowth': round(st.median(vg), 4), 'sharePositive': round(sum(1 for v in vg if v > 0)/len(vg), 3),
                  'meanInflation': round(st.mean(o[2] for o in P3), 4), 'meanMoneyPerOutput': round(st.mean(o[3][0] for o in P3), 4), 'crossSection': ols([o[:4] for o in P3], False)},
           'P4': {'pooledChanges': ols(P4, False), 'levelsEpisodeFE': ols(P4L, True)}}
    return out

res = {'source': json.load(open(os.path.join(D, 'raw_sha256.json'))), 'panelCsvSha256': hashlib.sha256(open(CSV, 'rb').read()).hexdigest(),
       'countryYearsWithAllThree': len(rows), 'all': analyse(False), 'withoutYearsAbove1000pct': analyse(True),
       'episodeList': [{'iso3': iso, 'from': run[0], 'to': run[-1], 'peakPct': round(max(rows[(iso, y)][0] for y in run), 1)} for iso, run in eps]}
res['bv'] = {'vel': res['all']['P4']['pooledChanges']['coef'][0], 'velh': round(res['all']['P4']['pooledChanges']['coef'][0]/2, 4)}
json.dump(res, sys.stdout, indent=1)
