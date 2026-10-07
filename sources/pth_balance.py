"""v5.4 item 3 (Oct 7, 2026; dev/reports/v5-21-v54-design.md, 1.2): the housing constants of the PTH balance sheet (harness.js CFG.PTHB_*).

Sources (via FRED, fred.stlouisfed.org/graph/fredgraph.csv?id=..., retrieved Oct 7, 2026; and the Census Bureau's CPS ASEC 2023 geographic mobility table):
  HOOREVLMHMV        Federal Reserve Z.1: households' owner-occupied real estate at market value (millions, quarterly)
  DOWNRC1A027NBEA    BEA: imputed rental of owner-occupied nonfarm housing (billions, annual): the gross rent of the same homes
  BOGZ1LM155012665Q  Federal Reserve Z.1: households' residential structures at current cost (millions): value minus this is land
  B2607C1Q027SBEA    BEA: consumption of fixed capital, owner-occupied housing (billions, annual rate): the yearly wear of the structures
  A2016C1A027NBEA    BEA: owner-occupied housing, taxes on production and imports (billions, annual; mostly property tax)
  HPIPONM226S        FHFA purchase-only house price index (monthly, from 1991); CPIAUCSL  CPI-U
  MORTGAGE30US       Freddie Mac 30-year fixed mortgage rate (weekly)
  CPS ASEC 2023 Table 1 (www2.census.gov/programs-surveys/demo/tables/geographic-mobility/2023/cps-2023/mig_01_2023_1yr.xlsx), people in renter-occupied
  units: 101,024 thousand, of whom 6,295 thousand moved to a different county in the past year (6.2%); owner-occupied: 4,184 of 226,143 (1.9%); everyone:
  10,480 of 327,167 (3.2%).

Constants (2015-2025 means unless said):
  PR     value / gross rent (HOOREVLMHMV / DOWNRC1A027NBEA)                         a home costs PR years of its market rent
  LAND   1 - structures / value                                                    the land's share of a home's value
  UPK    consumption of fixed capital / structures' value                          upkeep that keeps the structure's value
  TAX    taxes on production and imports / value (2015-2022, the series' years)
  G      FHFA purchase-only index growth over CPI-U growth, 1991-2025              real house-price growth a year
  RREAL  30-year mortgage rate minus the CPI-U's 12-month change, monthly           the trust's real borrowing rate

Usage: python3 sources/pth_balance.py   (downloads eight small CSV files; standard library only)
"""
import csv, io, urllib.request
def get(s, start='1991-01-01'):
    u = 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=%s&cosd=%s&coed=2025-12-31' % (s, start)
    r = csv.reader(io.StringIO(urllib.request.urlopen(u, timeout=60).read().decode())); next(r)
    out = []
    for d, v in r:
        try: out.append((d, float(v)))
        except ValueError: pass
    return out
def yearly(rows):
    y = {}
    for d, v in rows: y.setdefault(int(d[:4]), []).append(v)
    return {k: sum(v)/len(v) for k, v in y.items()}
YR = range(2015, 2026)
V, R, S = yearly(get('HOOREVLMHMV')), yearly(get('DOWNRC1A027NBEA')), yearly(get('BOGZ1LM155012665Q'))
CFC, TX = yearly(get('B2607C1Q027SBEA')), yearly(get('A2016C1A027NBEA'))
def mean(f, ys): v = [f(y) for y in ys]; return sum(v)/len(v)
both = [y for y in YR if y in V and y in R]; ss = [y for y in YR if y in V and y in S]
PR = mean(lambda y: V[y]/1000/R[y], both)
LAND = mean(lambda y: 1 - S[y]/V[y], ss)
UPK = mean(lambda y: CFC[y]*1000/S[y], [y for y in ss if y in CFC])
TAX = mean(lambda y: TX[y]*1000/V[y], [y for y in YR if y in TX and y in V])
H, C = get('HPIPONM226S'), dict(get('CPIAUCSL'))
n = (int(H[-1][0][:4]) - int(H[0][0][:4])) + (int(H[-1][0][5:7]) - int(H[0][0][5:7]))/12
G = ((H[-1][1]/H[0][1])/(C[H[-1][0]]/C[H[0][0]]))**(1/n) - 1
M = {}
for d, v in get('MORTGAGE30US', '2014-01-01'): M.setdefault(d[:7], []).append(v)
rr = []
for k, v in M.items():
    y = int(k[:4]); a, b = k + '-01', '%d-%s-01' % (y - 1, k[5:7])
    if y in YR and a in C and b in C: rr.append(sum(v)/len(v)/100 - (C[a]/C[b] - 1))
RREAL = sum(rr)/len(rr)
print('PR %.2f  LAND %.3f  UPK %.4f (of structures)  TAX %.4f  G %.4f (%.1f years)  RREAL %.4f' % (PR, LAND, UPK, TAX, G, n, RREAL))
print('moves to another county a year: renters %.3f, owners %.3f, everyone %.3f' % (6295/101024, 4184/226143, 10480/327167))
