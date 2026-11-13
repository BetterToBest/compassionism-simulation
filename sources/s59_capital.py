"""S59, part 2 (Nov 12, 2026; research-update prereg/2026-11-s59-tail-returns.md): who owns a private business, what owners and non-owners hold, and the
money income that wealth pays, by wealth group, for switch RETURNS (options bo and ci).

Source: Board of Governors of the Federal Reserve System, 2022 Survey of Consumer Finances: the summary extract (rscfp2022.dta) and, from the full public
data set (p22i6.dta), the income questions one by one and the mortgage-rate question of sources/s59_portfolio.py (codebook
https://www.federalreserve.gov/econres/files/codebk2022.txt): X5704 income from a sole proprietorship or farm; X5714 income from other businesses or
investments, net rent, trusts or royalties; X5706 + X5708 taxable and non-taxable interest; X5710 dividends (all for calendar 2021).
Population, pooling, classes, wealth groups and dollars: exactly sources/s59_portfolio.py (the engine's starting families; seven groups by net worth).

For each wealth group, split by whether the family owns a private business (HBUS = 1):
  - the owners' share of the group's families;
  - debts over assets, the asset shares (home, other real estate, shares, private business, other goods; the rest nominal) and the fixed-rate share of debts,
    as RT_GROUPS, for owners and for the others (the pooled adjustable-rate share of mortgages is used for both, as in part 1);
and for each group (owners and others together), money income over the holdings it comes from:
  - interest over nominal assets; dividends over shares; X5714 (rents, royalties, trusts, businesses not run as a sole proprietorship) over other real
    estate plus private business. X5704 (sole proprietorships and farms) is NOT a yield here: it is self-employment income, already inside the earnings the
    engine draws from the CPS; it is printed as a share of owners' wage-plus-business income so the report can keep it apart from wages.
Checks against the SCF Bulletin (all families): the share owning a business (about 20%), in the bottom half of income (about 14%) and the top tenth (nearly half).

Prints the tables and writes sources/s59_capital.json. Usage: python3 sources/s59_capital.py [rscfp2022.dta p22i6.dta]  (needs pandas and numpy).
"""
import io, json, os, sys, tempfile, urllib.request, zipfile
import numpy as np, pandas as pd
CPI22, CPI25 = 292.655, 321.943
# The Fed re-issued the summary extract on Oct 5, 2026 with every dollar amount in 2025 dollars (CPI-U-RS): a home's value in the extract is 1.09438 times the
# value given at the 2022 interview in the full public data set (HOUSES over X716, every family; checked in sources/s59_capital.py). FILE takes the extract
# back to 2022 dollars; before that date the extract was in 2022 dollars (FILE = 1), which is what the engine's tables of Oct 7 were computed from.
FILE = 1.09438
U1 = 'https://www.federalreserve.gov/econres/files/scfp2022s.zip'; U2 = 'https://www.federalreserve.gov/econres/files/scf2022s.zip'
COLS = ['y1', 'wgt', 'age', 'married', 'kids', 'wageinc', 'income', 'networth', 'asset', 'fin', 'nfin', 'debt', 'equity', 'houses', 'oresre', 'nnresre', 'bus', 'vehic', 'othnfin',
        'mrthel', 'heloc', 'nh_mort', 'resdbt', 'othloc', 'ccbal', 'install', 'odebt', 'hbus', 'bussefarminc', 'intdivinc']
MC = ['y1', 'x716', 'x820', 'x920', 'x1020', 'x805', 'x905', 'x1005', 'x5704', 'x5714', 'x5706', 'x5708', 'x5710']
def get(url, name, d):
    zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (research script)'}), timeout=300).read())).extractall(d)
    return os.path.join(d, name)
def stata(path, cols):
    r = pd.io.stata.StataReader(path); names = {c.lower(): c for c in r.variable_labels().keys()}
    df = pd.read_stata(path, columns=[names[c] for c in cols], convert_categoricals=False); df.columns = [c.lower() for c in df.columns]; return df
with tempfile.TemporaryDirectory() as d:
    p1 = sys.argv[1] if len(sys.argv) > 2 else get(U1, 'rscfp2022.dta', d); p2 = sys.argv[2] if len(sys.argv) > 2 else get(U2, 'p22i6.dta', d)
    al = stata(p1, COLS); mf = stata(p2, MC)
al = al.merge(mf, on='y1', how='left', validate='one_to_one')
_h = al[al.x716 > 0]; _f = float((_h.wgt*_h.houses).sum()/(_h.wgt*_h.x716).sum()); print('the extract\'s dollars over 2022 dollars (HOUSES over X716): %.5f' % _f)
assert abs(_f/FILE - 1) < 1e-3, 'the extract is not in the dollars FILE assumes: set FILE to the printed ratio'
for c in COLS:
    if c not in ('y1', 'wgt', 'age', 'married', 'kids', 'hbus'): al[c] = al[c]/FILE  # 2022 dollars (income amounts are then 2021 income in 2022 prices, as the Bulletin)
for c in ('x5704', 'x5714', 'x5706', 'x5708', 'x5710'): al[c] = al[c].where(al[c] > -9e8, 0.0).astype(float)  # no negative codes other than losses are expected; guard anyway
def wq(x, w, q):
    o = np.argsort(x); xs = x[o]; ws = w[o]; c = (np.cumsum(ws) - ws/2)/ws.sum(); return np.interp(q, c, xs)
# checks on all families
wa = al.wgt.values.astype(float); inc = al.income.values.astype(float); hb = (al.hbus.values == 1)
i50, i90 = wq(inc, wa, [0.5, 0.9]); out = {'checks': {'ownersAll': round(float((wa*hb).sum()/wa.sum()*100), 1), 'ownersBottomHalfIncome': round(float((wa*hb*(inc < i50)).sum()/(wa*(inc < i50)).sum()*100), 1),
                                                    'ownersTopTenthIncome': round(float((wa*hb*(inc >= i90)).sum()/(wa*(inc >= i90)).sum()*100), 1)}}
print('All families owning a private business: %.1f%% (Bulletin: about 20%%); bottom half of income %.1f%% (about 14%%); top tenth %.1f%% (nearly half)' % tuple(out['checks'].values()))
df = al[(al.age >= 25) & (al.age <= 66) & (al.wageinc > 0) & (al.married > 0)].copy(); w = df.wgt.values.astype(float); k = CPI25/CPI22
# the income questions are calendar-2021 dollars; the extract's sums are the same amounts in 2022 prices (about 1.08 times)
print('check, engine population, weighted totals $bn: X5704+X5714 %.1f against BUSSEFARMINC %.1f; X5706+X5708+X5710 %.1f against INTDIVINC %.1f'
      % ((w*(df.x5704 + df.x5714)).sum()/1e9, (w*df.bussefarminc).sum()/1e9, (w*(df.x5706 + df.x5708 + df.x5710)).sum()/1e9, (w*df.intdivinc).sum()/1e9))
df['adj'] = sum(df[b].where(df[a] == 1, 0.0) for a, b in (('x820', 'x805'), ('x920', 'x905'), ('x1020', 'x1005')))
df['mor'] = sum(df[b].where(df[a].isin([1, 5]), 0.0) for a, b in (('x820', 'x805'), ('x920', 'x905'), ('x1020', 'x1005')))
arm = float((w*df.adj).sum()/(w*df.mor).sum())
nw = df.networth.values*k; pos = nw >= 0
edges = [0.0] + [float(round(v)) for v in wq(nw, w, [0.25, 0.5, 0.75, 0.9, 0.99])]
p1e = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 's59_portfolio.json'))).get('edges')
grp = np.zeros(len(df), int)
for e in edges: grp += (nw >= e)
own = (df.hbus.values == 1)
def sheet(m):
    g = df[m]; ww = w[m]; S = lambda c: float((ww*g[c].values).sum())
    a = {'home': S('houses'), 'ore': S('oresre') + S('nnresre'), 'eq': S('equity'), 'bus': S('bus'), 'oth': S('vehic') + S('othnfin')}; A = S('asset'); D = S('debt')
    mort = S('nh_mort') + S('resdbt'); flt = S('heloc') + S('othloc') + S('ccbal') + S('odebt') + arm*mort; fix = S('install') + (1 - arm)*mort
    row = [round(D/A, 4)] + [round(a[c]/A, 4) for c in ('home', 'ore', 'eq', 'bus', 'oth')] + [round(fix/D, 4) if D > 0 else 0.0]; return row, A, D
out['arm'] = round(arm, 4); out['edges'] = edges; out['groups'] = []
print('\ngroup   owners %   | owners: lev  home   ore    eq     bus    oth    fixed | others: lev  home   ore    eq     bus    oth    fixed | yields %: interest dividends rents-and-other | sole-prop share of owners\' wage+business income')
for gi in range(7):
    m = grp == gi; mo = m & own; mn = m & ~own; ro, _, _ = sheet(mo); rn, _, _ = sheet(mn); g = df[m]; ww = w[m]; S = lambda c: float((ww*g[c].values).sum())
    nomA = S('fin') - S('equity'); yi = (S('x5706') + S('x5708'))/nomA; yd = S('x5710')/S('equity'); yr = S('x5714')/(S('oresre') + S('nnresre') + S('bus'))
    go = df[mo]; wo = w[mo]; sp = float((wo*go.x5704).sum()/((wo*go.x5704).sum() + (wo*go.wageinc).sum()))
    out['groups'].append({'owners': round(float(w[mo].sum()/w[m].sum()), 4), 'own': ro, 'other': rn, 'yInt': round(yi, 5), 'yDiv': round(yd, 5), 'yRent': round(yr, 5), 'soleShare': round(sp, 4), 'rowsOwn': int(mo.sum()), 'rows': int(m.sum())})
    print('%d   %6.1f   | %s | %s | %6.2f %6.2f %6.2f | %.3f  (rows %d, owners %d)' % (gi, w[mo].sum()/w[m].sum()*100, ' '.join('%6.4f' % v for v in ro), ' '.join('%6.4f' % v for v in rn), yi*100, yd*100, yr*100, sp, m.sum(), mo.sum()))
print('edges (2025 dollars): %s; part 1\'s: %s' % (json.dumps(edges), json.dumps(p1e)))
T = lambda c: float((w*df[c].values).sum())
out['all'] = {'owners': round(float(w[own].sum()/w.sum()), 4), 'interestBn': round((T('x5706') + T('x5708'))/1e9, 1), 'dividendsBn': round(T('x5710')/1e9, 1), 'rentsOtherBn': round(T('x5714')/1e9, 1), 'soleBn': round(T('x5704')/1e9, 1), 'wagesBn': round(T('wageinc')/1e9, 1)}
print('engine population: owners %.1f%% of families; $bn a year: wages %.0f, sole proprietorships and farms %.0f, rents and other business %.0f, interest %.0f, dividends %.0f'
      % (out['all']['owners']*100, out['all']['wagesBn'], out['all']['soleBn'], out['all']['rentsOtherBn'], out['all']['interestBn'], out['all']['dividendsBn']))
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 's59_capital.json'), 'w'), indent=1)
