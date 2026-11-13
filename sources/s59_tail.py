"""S59, part 2 (Nov 12, 2026; research-update prereg/2026-11-s59-tail-returns.md): the top tail of net worth, for switch WEALTH_TAIL.

Sources (all opened and downloaded by this script unless paths are given):
  - Board of Governors of the Federal Reserve System, 2022 Survey of Consumer Finances, summary extract public data (rscfp2022.dta in
    https://www.federalreserve.gov/econres/files/scfp2022s.zip), all five implicates pooled with the weight WGT (the file of sources/scf_households.py);
  - Forbes, "The Forbes 400" 2022 (https://www.forbes.com/forbesapi/person/forbes-400/2022/position/true.json?limit=500): 400 net worths, September 2022.
    Only rank, net worth and whether the entry's name says "& family" are kept (sources/s59_tail/forbes400_2022.json);
  - Board of Governors, Distributional Financial Accounts (dfa-networth-shares.csv in https://www.federalreserve.gov/releases/z1/dataviz/download/zips/dfa.zip).

What it does.
  1. Shares of net worth held by the top 1%, 10%, 0.1% and the bottom half, and the Gini, for all SCF families and for the engine's starting population
     (head aged 25 to 66 with wage income, the four household types), by family and, for the engine's population, by adult (a couple's net worth split
     equally between its two adults, as the engine does).
  2. For a grid of cutoffs (percentiles of each population's net worth): the weighted Hill estimate of the Pareto exponent, its approximate standard error
     (exponent over the square root of the effective number of families above the cutoff: Kish's formula on the weights, divided by 5 for the implicates),
     the weighted Kolmogorov-Smirnov distance of the Pareto fit, the generalised Pareto fit by weighted maximum likelihood (survival
     (1 + xi (x - u)/sigma)^(-1/xi); the Pareto is the case sigma = xi u), its distance, and twice the gain in log likelihood per effective family.
  3. THE CUTOFF RULE (fixed in the preregistration before any engine run): the lowest cutoff on the grid, up to the 99.5th percentile, from which the
     Hill estimate at every higher cutoff up to the 99.5th percentile stays within one standard error (the cutoff's own) of the cutoff's estimate, and at
     which the Pareto is not rejected against the generalised Pareto (the scaled statistic below 3.84).
  4. Per household type: the share of the type's families above the cutoff, the number of families of the type (the tail is cut off at one family), and the
     type's own Hill estimate (a check on using one exponent for all four types).
  5. Checks, never targets: the Forbes 400 (how many families the fitted tail puts above the list's lowest net worth, and what they hold, against the list);
     the SCF with the Forbes 400 added (Bricker, Hansen and Volz, Economics Letters 2019, report about +1.5 points on the top 1% share); the Fed's
     Distributional Financial Accounts.
Dollars: 2022 dollars (the extract's amounts divided by FILE, below; the Forbes list is September 2022); the engine's cutoff is taken to 2025 with CPI-U
annual averages 292.655 and 321.943 (BLS), as the engine's wealth tables were (sources/scf_households.py).

Prints the tables and writes sources/s59_tail.json. Usage: python3 sources/s59_tail.py [rscfp2022.dta forbes.json dfa-networth-shares.csv]
(needs pandas and numpy; without paths it downloads the three files).
"""
import csv, hashlib, io, json, os, sys, tempfile, urllib.request, zipfile
import numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)); CPI22, CPI25 = 292.655, 321.943
# The Fed re-issued the summary extract on Oct 5, 2026 with every dollar amount in 2025 dollars (CPI-U-RS): a home's value in the extract is 1.09438 times the
# value given at the 2022 interview in the full public data set (HOUSES over X716, every family; checked in sources/s59_capital.py). FILE takes the extract
# back to 2022 dollars; before that date the extract was in 2022 dollars (FILE = 1), which is what the engine's tables of Oct 7 were computed from.
FILE = 1.09438
U_SCF = 'https://www.federalreserve.gov/econres/files/scfp2022s.zip'; U_F = 'https://www.forbes.com/forbesapi/person/forbes-400/2022/position/true.json?limit=500'
U_DFA = 'https://www.federalreserve.gov/releases/z1/dataviz/download/zips/dfa.zip'
GRID = [90, 92.5, 95, 96, 97, 97.5, 98, 98.5, 99, 99.25, 99.5, 99.75, 99.9]
def fetch(url): return urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (research script)'}), timeout=300).read()
def wq(x, w, q):
    o = np.argsort(x); xs = x[o]; ws = w[o]; c = (np.cumsum(ws) - ws/2)/ws.sum(); return np.interp(q, c, xs)
def topshare(x, w, f):
    o = np.argsort(-x); xs = x[o]; ws = w[o]; cw = np.cumsum(ws); take = np.clip(f*ws.sum() - (cw - ws), 0, ws); return (take*xs).sum()/(ws*xs).sum()
def gini(x, w):
    o = np.argsort(x); xs = x[o]; ws = w[o]; cx = np.cumsum(ws*xs); L = cx/cx[-1]; Lp = np.concatenate([[0], L[:-1]]); return 1 - (ws*(L + Lp)).sum()/ws.sum()
def hill(x, w, u):
    m = x > u; return w[m].sum()/(w[m]*np.log(x[m]/u)).sum()
def neff(w): return w.sum()**2/(w**2).sum()/5
def ks(x, w, u, sf):
    m = x > u; xs = x[m]; ws = w[m]; o = np.argsort(xs); xs = xs[o]; ws = ws[o]; cw = np.cumsum(ws)/ws.sum(); F = 1 - sf(xs)
    return float(max(np.abs(cw - F).max(), np.abs(cw - ws/ws.sum() - F).max()))
def nelder(f, x0, it=400):
    n = len(x0); P = [np.array(x0, float)] + [np.array(x0, float) + (0.2*abs(x0[i]) + 0.05)*np.eye(n)[i] for i in range(n)]; V = [f(p) for p in P]
    for _ in range(it):
        o = np.argsort(V); P = [P[i] for i in o]; V = [V[i] for i in o]; c = sum(P[:-1])/n; r = c + (c - P[-1]); fr = f(r)
        if fr < V[0]:
            e = c + 2*(c - P[-1]); fe = f(e); P[-1], V[-1] = (e, fe) if fe < fr else (r, fr)
        elif fr < V[-2]: P[-1], V[-1] = r, fr
        else:
            k = c + 0.5*(P[-1] - c); fk = f(k)
            if fk < V[-1]: P[-1], V[-1] = k, fk
            else: P = [P[0]] + [P[0] + 0.5*(p - P[0]) for p in P[1:]]; V = [V[0]] + [f(p) for p in P[1:]]
    return P[int(np.argmin(V))], min(V)
def gpd(x, w, u):
    m = x > u; y = x[m] - u; ws = w[m]
    def nll(t):
        xi, ls = t; sig = np.exp(ls)
        return 1e30 if xi <= 1e-6 or xi > 3 else float((ws*(np.log(sig) + (1/xi + 1)*np.log1p(xi*y/sig))).sum())
    a = hill(x, w, u); t, v = nelder(nll, [1/a, np.log(u/a)]); return float(t[0]), float(np.exp(t[1])), -v
def par_ll(x, w, u, a):
    m = x > u; return float((w[m]*(np.log(a/u) - (a + 1)*np.log(x[m]/u))).sum())
def table(name, x, w):
    print('\n' + name + '\n  pct   cutoff $M   rows  families M  exponent   se    KS Pareto | GPD xi  sigma/u  KS GPD  scaled 2dLL')
    rows = []
    for pc in GRID:
        u = float(wq(x, w, pc/100)); m = x > u; a = float(hill(x, w, u)); ne = float(neff(w[m])); xi, sig, ll = gpd(x, w, u)
        r = {'pct': pc, 'u': round(u), 'rows': int(m.sum()), 'fam': round(float(w[m].sum())), 'alpha': round(a, 4), 'se': round(a/np.sqrt(ne), 4), 'neff': round(ne, 1),
             'ksPareto': round(ks(x, w, u, lambda z: (z/u)**(-a)), 4), 'xi': round(xi, 4), 'sigU': round(sig/u, 4), 'ksGpd': round(ks(x, w, u, lambda z: (1 + xi*(z - u)/sig)**(-1/xi)), 4),
             'lr': round(2*(ll - par_ll(x, w, u, a))*ne/float(w[m].sum()), 3)}
        rows.append(r); print('  %5.2f %9.2f %6d %10.3f   %6.3f  %5.3f   %6.4f  | %5.3f  %6.3f  %6.4f  %7.2f' % (pc, u/1e6, r['rows'], r['fam']/1e6, a, r['se'], r['ksPareto'], xi, r['sigU'], r['ksGpd'], r['lr']))
    return rows
def rule(rows):
    use = [r for r in rows if r['pct'] <= 99.5]
    for i, r in enumerate(use[:-1]):
        if r['lr'] < 3.84 and all(abs(h['alpha'] - r['alpha']) <= r['se'] for h in use[i + 1:]): return r
    return use[-1]
def shares(x, w): return {'top1': round(topshare(x, w, .01)*100, 2), 'top10': round(topshare(x, w, .1)*100, 2), 'top01': round(topshare(x, w, .001)*100, 2), 'bottom50': round((1 - topshare(x, w, .5))*100, 2),
                          'gini': round(float(gini(x, w)), 4), 'mean': round(float((w*x).sum()/w.sum())), 'median': round(float(wq(x, w, .5))), 'p99': round(float(wq(x, w, .99))), 'families': round(float(w.sum()))}
with tempfile.TemporaryDirectory() as d:
    if len(sys.argv) > 3: p1, fb, dfa = sys.argv[1], open(sys.argv[2], 'rb').read(), open(sys.argv[3], 'rb').read()
    else:
        zipfile.ZipFile(io.BytesIO(fetch(U_SCF))).extractall(d); p1 = os.path.join(d, 'rscfp2022.dta'); fb = fetch(U_F); dfa = zipfile.ZipFile(io.BytesIO(fetch(U_DFA))).read('dfa-networth-shares.csv')
    r = pd.io.stata.StataReader(p1); nm = {c.lower(): c for c in r.variable_labels().keys()}
    df = pd.read_stata(p1, columns=[nm[c] for c in ['wgt', 'age', 'married', 'kids', 'wageinc', 'networth']], convert_categoricals=False); df.columns = [c.lower() for c in df.columns]
out = {'fileDollars': FILE, 'source': {'scf': U_SCF, 'forbes': U_F, 'forbesSha256': hashlib.sha256(fb).hexdigest(), 'dfa': U_DFA, 'dfaSha256': hashlib.sha256(dfa).hexdigest()}, 'grid': GRID, 'cpi': [CPI22, CPI25]}
F = json.loads(fb)['personList']['personsLists']; F.sort(key=lambda p: p['position'])
fl = [{'position': p['position'], 'worthM': p['finalWorth'], 'family': 'family' in (p.get('personName') or '').lower()} for p in F]
os.makedirs(os.path.join(HERE, 's59_tail'), exist_ok=True); json.dump({'source': U_F, 'sha256': out['source']['forbesSha256'], 'list': fl}, open(os.path.join(HERE, 's59_tail', 'forbes400_2022.json'), 'w'))
fw = np.array([p['worthM'] for p in fl])*1e6; ffam = np.array([p['family'] for p in fl])
df['networth'] = df.networth/FILE
x = df.networth.values.astype(float); w = df.wgt.values.astype(float)
mp = df[(df.age >= 25) & (df.age <= 66) & (df.wageinc > 0) & (df.married > 0)]; xm = mp.networth.values.astype(float); wm = mp.wgt.values.astype(float)
ad = np.where(mp.married.values == 1, 2.0, 1.0)
out['shares'] = {'allFamilies': shares(x, w), 'model': shares(xm, wm), 'modelPerAdult': shares(xm/ad, wm*ad)}
print('Shares of net worth, SCF 2022 (2022 dollars)'); [print('  %-14s %s' % (k, json.dumps(v))) for k, v in out['shares'].items()]
ta = table('All families: tail fits by cutoff', x, w); tm = table('The engine\'s population: tail fits by cutoff', xm, wm)
tf = table('All families with the Forbes 400 added (each entry one family, weight 1): tail fits by cutoff', np.concatenate([x, fw]), np.concatenate([w, np.ones(len(fw))]))
ra, rm = rule(ta), rule(tm); out['fits'] = {'allFamilies': ta, 'model': tm, 'allFamiliesForbes': tf}; out['rule'] = {'allFamilies': ra, 'model': rm}
print('\nThe cutoff rule picks: all families the %.2fth percentile ($%.2fM, exponent %.3f, se %.3f); the engine\'s population the %.2fth percentile ($%.2fM, exponent %.3f, se %.3f)'
      % (ra['pct'], ra['u']/1e6, ra['alpha'], ra['se'], rm['pct'], rm['u']/1e6, rm['alpha'], rm['se']))
TY = [('coupleKids', (mp.married == 1) & (mp.kids > 0)), ('coupleNoKids', (mp.married == 1) & (mp.kids == 0)), ('singleParent', (mp.married == 2) & (mp.kids > 0)), ('single', (mp.married == 2) & (mp.kids == 0))]
def cut(pc):  # what the engine needs for one cutoff of the engine's population
    r = [q for q in tm if q['pct'] == pc][0]; u = r['u']; c = {'pct': pc, 'u2022': u, 'u2025': round(u*CPI25/CPI22), 'alpha': r['alpha'], 'se': r['se'], 'xi': r['xi'], 'sigU': r['sigU'], 'types': {}}
    for t, sel in TY:
        g = mp[sel.values]; gx = g.networth.values.astype(float); gw = g.wgt.values.astype(float); m = gx > u
        c['types'][t] = {'pi': round(float(gw[m].sum()/gw.sum()), 6), 'families': round(float(gw.sum())), 'rows': int(m.sum()), 'alpha': round(float(hill(gx, gw, u)), 3) if m.sum() > 5 else None,
                         'se': round(float(hill(gx, gw, u)/np.sqrt(neff(gw[m]))), 3) if m.sum() > 5 else None}
    return c
out['cuts'] = {'main': cut(rm['pct']), 'p99': cut(99), 'p90': cut(90)}
print('\nPer household type at the main cutoff (share of the type above it, families of the type, rows, the type\'s own exponent and se):')
for t, v in out['cuts']['main']['types'].items(): print('  %-13s %.4f%%  %10d  %5d  %s  %s' % (t, v['pi']*100, v['families'], v['rows'], v['alpha'], v['se']))
# checks
fmin = fw.min(); N = w.sum(); tail = N*(1 - ra['pct']/100); chk = {}
for lab, a in (('exponent', ra['alpha']), ('minus one se', ra['alpha'] - ra['se']), ('plus one se', ra['alpha'] + ra['se'])):
    n = tail*(fmin/ra['u'])**(-a); top = N**(1/a)*0 + ra['u']*(tail)**(1/a)  # the net worth at which one family is left
    tot = n*fmin*a/(a - 1) - 1*top*a/(a - 1) if a > 1 else float('nan')  # the tail's wealth above the list's lowest, less what lies above the one-family cap
    chk[lab] = {'alpha': round(a, 3), 'familiesAboveForbesMin': round(float(n)), 'theirWealthTn': round(float(tot)/1e12, 2), 'capBn': round(float(top)/1e9, 1)}
out['forbes'] = {'entries': len(fw), 'totalTn': round(fw.sum()/1e12, 3), 'minBn': fmin/1e9, 'maxBn': fw.max()/1e9, 'familyEntries': int(ffam.sum()), 'familyEntriesTn': round(fw[ffam].sum()/1e12, 3), 'fittedTail': chk,
                 'exponentOfTheListAlone': round(float(len(fw)/np.log(fw/fmin).sum()), 3)}
print('\nForbes 400, 2022: %d entries, $%.3f trillion, from $%.1f to $%.0f billion; %d entries say "& family" ($%.3f trillion). Hill exponent of the list alone above its lowest: %.3f'
      % (len(fw), fw.sum()/1e12, fmin/1e9, fw.max()/1e9, ffam.sum(), fw[ffam].sum()/1e12, out['forbes']['exponentOfTheListAlone']))
for lab, v in chk.items(): print('  fitted SCF tail (all families), %-13s %.3f: %5d families above $%.1f billion holding $%.2f trillion (cap at one family: $%.1f billion)' % (lab, v['alpha'], v['familiesAboveForbesMin'], fmin/1e9, v['theirWealthTn'], v['capBn']))
s0 = topshare(x, w, .01)*100; x2 = np.concatenate([x, fw]); w2 = np.concatenate([w, np.ones(len(fw))]); s1 = topshare(x2, w2, .01)*100
out['forbesAdded'] = {'top1Scf': round(s0, 2), 'top1ScfForbes': round(s1, 2), 'change': round(s1 - s0, 2)}
print('SCF top 1%% share %.2f%%; with the Forbes 400 added %.2f%% (+%.2f points; Bricker, Hansen and Volz 2019 report about +1.5)' % (s0, s1, s1 - s0))
rows = list(csv.DictReader(io.StringIO(dfa.decode('utf-8-sig')))); dq = {}
for r0 in rows: dq.setdefault(r0['Date'], {})[r0['Category']] = float(r0['Net worth'])
last = sorted(dq.keys(), key=lambda s: (int(s[:4]), int(s[-1])))[-1]; out['dfa'] = {}
for q in ['2022:Q1', '2022:Q2', '2022:Q3', '2022:Q4', last]:
    v = dq[q]; out['dfa'][q] = {'top1': round(v['TopPt1'] + v['RemainingTop1'], 1), 'top01': v['TopPt1'], 'top10': round(v['TopPt1'] + v['RemainingTop1'] + v['Next9'], 1), 'bottom50': v['Bottom50']}
    print('Distributional Financial Accounts %s: top 1%% %.1f%%, top 0.1%% %.1f%%, top 10%% %.1f%%, bottom half %.1f%%' % (q, out['dfa'][q]['top1'], v['TopPt1'], out['dfa'][q]['top10'], v['Bottom50']))
json.dump(out, open(os.path.join(HERE, 's59_tail.json'), 'w'), indent=1)
