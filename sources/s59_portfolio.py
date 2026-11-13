"""S59 (Nov 10, 2026; research-update prereg/2026-11-s59-asset-classes.md): what a family's net worth is made of, by wealth group, for switch RETURNS.

Source: Board of Governors of the Federal Reserve System, 2022 Survey of Consumer Finances.
  - summary extract public data (rscfp2022.dta in https://www.federalreserve.gov/econres/files/scfp2022s.zip), the file of sources/scf_households.py;
  - full public data set (p22i6.dta in https://www.federalreserve.gov/econres/files/scf2022s.zip) for one question only: is each of the first three
    mortgages on the home adjustable-rate (X820, X920, X1020: 1 yes, 5 no) and how much is owed on it (X805, X905, X1005); codebook
    https://www.federalreserve.gov/econres/files/codebk2022.txt.
All five implicates pooled with the weight WGT. The families are the engine's starting population (sources/scf_households.py): head aged 25 to 66 with
wage income, in the four household types, pooled. Dollars are taken from 2022 to 2025 with CPI-U annual averages 292.655 and 321.943 (BLS), as there.

Wealth groups: families with net worth below zero; then families at or above zero by the pooled population's net-worth percentiles 25, 50, 75, 90, 99.
Zero is a group edge so that every group's debts are below its assets (or above, in the first group) and a family's balance sheet can be scaled from its
net worth alone: gross assets G = W/(1 - lev), debts lev*G, where lev is the group's debts over its assets.

Classes (summary extract variables):
  real assets      home: HOUSES; ore: ORESRE + NNRESRE (other residential, and net equity in non-residential, real estate); eq: EQUITY (stocks held directly
                   and through funds, retirement accounts and trusts); bus: BUS (private businesses); oth: VEHIC + OTHNFIN (vehicles, other non-financial)
  nominal assets   nom: FIN - EQUITY (deposits, certificates, bonds, the non-stock part of funds and retirement accounts, life insurance, other financial)
  debts            floating: HELOC + OTHLOC + CCBAL + ODEBT + the adjustable-rate share of (NH_MORT + RESDBT)
                   fixed: INSTALL (education, vehicle, other instalment loans) + the fixed-rate share of (NH_MORT + RESDBT)
The adjustable-rate share is the share of dollars owed on the first three home mortgages that is adjustable-rate, in the same population (one number, pooled:
the groups' own shares are printed beside it). Debt for other residential property (RESDBT) has no rate question in the summary extract and takes the same share.

Prints the table and writes sources/s59_portfolio.json. Usage: python3 sources/s59_portfolio.py [rscfp2022.dta p22i6.dta]
(without paths it downloads both, about 12 MB zipped; needs pandas and numpy).
"""
import io, json, os, sys, tempfile, urllib.request, zipfile
import numpy as np, pandas as pd
CPI22, CPI25 = 292.655, 321.943
# The Fed re-issued the summary extract on Oct 5, 2026 with every dollar amount in 2025 dollars (CPI-U-RS): a home's value in the extract is 1.09438 times the
# value given at the 2022 interview in the full public data set (HOUSES over X716, every family; checked in sources/s59_capital.py). FILE takes the extract
# back to 2022 dollars; before that date the extract was in 2022 dollars (FILE = 1), which is what the engine's tables of Oct 7 were computed from.
FILE = 1.09438  # correction of Nov 12, 2026 (S59 part 2): the edges printed on Nov 10 were 1.09438 times too high
U1 = 'https://www.federalreserve.gov/econres/files/scfp2022s.zip'; U2 = 'https://www.federalreserve.gov/econres/files/scf2022s.zip'
COLS = ['y1', 'wgt', 'age', 'married', 'kids', 'wageinc', 'networth', 'asset', 'fin', 'nfin', 'debt', 'equity', 'houses', 'oresre', 'nnresre', 'bus', 'vehic', 'othnfin',
        'mrthel', 'heloc', 'nh_mort', 'resdbt', 'othloc', 'ccbal', 'install', 'odebt']
MC = ['y1', 'x820', 'x920', 'x1020', 'x805', 'x905', 'x1005']
def get(url, name, d):
    zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (research script)'}), timeout=300).read())).extractall(d)
    return os.path.join(d, name)
def stata(path, cols):
    r = pd.io.stata.StataReader(path); names = {c.lower(): c for c in r.variable_labels().keys()}
    df = pd.read_stata(path, columns=[names[c] for c in cols], convert_categoricals=False); df.columns = [c.lower() for c in df.columns]; return df
with tempfile.TemporaryDirectory() as d:
    p1 = sys.argv[1] if len(sys.argv) > 2 else get(U1, 'rscfp2022.dta', d); p2 = sys.argv[2] if len(sys.argv) > 2 else get(U2, 'p22i6.dta', d)
    df = stata(p1, COLS); mf = stata(p2, MC)
df = df.merge(mf, on='y1', how='left', validate='one_to_one')
df = df[(df.age >= 25) & (df.age <= 66) & (df.wageinc > 0) & (df.married > 0)].copy()
w = df.wgt.values.astype(float); k = CPI25/CPI22/FILE
assert np.allclose(df.asset, df.fin + df.nfin) and np.allclose(df.networth, df.asset - df.debt)
assert np.allclose(df.debt, df.mrthel + df.resdbt + df.othloc + df.ccbal + df.install + df.odebt, atol=1) and np.allclose(df.mrthel, df.nh_mort + df.heloc, atol=1)
assert np.allclose(df.nfin, df.houses + df.oresre + df.nnresre + df.bus + df.vehic + df.othnfin, atol=1)
df['adj'] = sum(df[b].where(df[a] == 1, 0.0) for a, b in (('x820', 'x805'), ('x920', 'x905'), ('x1020', 'x1005')))
df['mor'] = sum(df[b].where(df[a].isin([1, 5]), 0.0) for a, b in (('x820', 'x805'), ('x920', 'x905'), ('x1020', 'x1005')))
def wq(x, q):
    o = np.argsort(x); xs = x[o]; ws = w[o]; c = (np.cumsum(ws) - ws/2)/ws.sum(); return np.interp(q, c, xs)
nw = df.networth.values*k
edges = [0.0] + [float(round(v)) for v in wq(nw, [0.25, 0.50, 0.75, 0.90, 0.99])]
assert all(edges[i] < edges[i + 1] for i in range(len(edges) - 1)), edges
grp = np.searchsorted(edges, nw, side='right')  # 0: below zero; 1: zero to P25; ... 6: P99 and above
names = ['below zero', 'zero to P25', 'P25 to P50', 'P50 to P75', 'P75 to P90', 'P90 to P99', 'P99 and above']
def S(col, m): return float((w[m]*df[col].values[m]).sum())
arm_all = S('adj', np.ones(len(df), bool))/S('mor', np.ones(len(df), bool))
out = {'source': 'SCF 2022 (summary extract and full public data set), families with a head aged 25-66 with wage income; sources/s59_portfolio.py',
       'dollars': '2025 (CPI-U 321.943/292.655)', 'edges': edges, 'arm': round(arm_all, 4), 'groups': []}
print('adjustable-rate share of dollars owed on home mortgages, all groups: %.4f' % arm_all)
print('group            families%  lev      home    ore     eq      bus     oth     nom   | fixed  floating | ARM(own)  mean net worth')
tot = {}
for g, nm in enumerate(names):
    m = grp == g; A = S('asset', m); D = S('debt', m)
    a = {'home': S('houses', m), 'ore': S('oresre', m) + S('nnresre', m), 'eq': S('equity', m), 'bus': S('bus', m), 'oth': S('vehic', m) + S('othnfin', m), 'nom': S('fin', m) - S('equity', m)}
    mort = S('nh_mort', m) + S('resdbt', m); flt = S('heloc', m) + S('othloc', m) + S('ccbal', m) + S('odebt', m) + arm_all*mort; fix = S('install', m) + (1 - arm_all)*mort
    assert abs(sum(a.values()) - A) < 1e-6*A and abs(fix + flt - D) < 1e-6*max(D, 1)
    arm_g = S('adj', m)/S('mor', m) if S('mor', m) > 0 else float('nan')
    row = {'name': nm, 'share': round(w[m].sum()/w.sum(), 4), 'lev': round(D/A, 4), 'fix': round(fix/D, 4)}
    for c in a: row[c] = round(a[c]/A, 4)
    row['nom'] = round(1 - sum(row[c] for c in ('home', 'ore', 'eq', 'bus', 'oth')), 4)  # the six shares sum to 1 exactly
    out['groups'].append(row)
    for c in a: tot[c] = tot.get(c, 0) + a[c]
    tot['fix'] = tot.get('fix', 0) + fix; tot['flt'] = tot.get('flt', 0) + flt
    print('%-16s %6.1f   %6.4f  %6.4f %6.4f %6.4f %6.4f %6.4f %6.4f | %6.4f %6.4f | %6.4f   %12.0f'
          % (nm, row['share']*100, row['lev'], row['home'], row['ore'], row['eq'], row['bus'], row['oth'], row['nom'], row['fix'], 1 - row['fix'], arm_g, (A - D)*k/w[m].sum()))
NW = sum(tot[c] for c in ('home', 'ore', 'eq', 'bus', 'oth', 'nom')) - tot['fix'] - tot['flt']
print('all families, as shares of net worth: ' + ', '.join('%s %.3f' % (c, tot[c]/NW) for c in ('home', 'ore', 'eq', 'bus', 'oth', 'nom', 'fix', 'flt')))
print('  net nominal position (nominal assets less every debt) over net worth: %.3f; with floating debt set aside (it reprices): %.3f' % ((tot['nom'] - tot['fix'] - tot['flt'])/NW, (tot['nom'] - tot['fix'])/NW))
out['all'] = {c: round(tot[c]/NW, 4) for c in ('home', 'ore', 'eq', 'bus', 'oth', 'nom', 'fix', 'flt')}
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 's59_portfolio.json'), 'w'), indent=1)
print('edges (2025 dollars): ' + json.dumps(edges))
