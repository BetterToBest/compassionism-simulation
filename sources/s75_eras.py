"""S75 (Nov 16, 2026; research-update prereg/2026-11-s75-deep-history.md, Part A, and Amendment 1): the descriptive panel of US policy eras.
No engine. Every figure is read from files kept in the repository (SHA-256 of each in the output's _meta), downloaded Nov 14 (S74) and Nov 16 (S75):

- sources/s74_history/raw/ (S74): FRED CUSR0000SAF11 (food at home), CUSR0000SAH1 (shelter), CPIMEDSL (medical care), UNRATE, GDPC1, GDPPOT,
  FEDFUNDS, TB3MS, USREC, CSUSHPINSA (Case-Shiller national, NSA), SP500, CPIAUCSL; the Wu-Xia shadow rate (WuXiaShadowRate.xlsx).
- sources/s59_shiller/ie_data.xls (S59): Shiller's real S&P composite price, monthly from 1871.
- sources/s75_eras/raw/ (S75):
  FRED, https://fred.stlouisfed.org/graph/fredgraph.csv?id=<ID>: CPIAUCNS (CPI-U, NSA, from 1913), CPIUFDSL (CPI food, from 1947),
    A939RX0Q048SBEA (real GDP per person, quarterly, from 1947).
  Shiller, Irrational Exuberance Figure 3.1 file (http://www.econ.yale.edu/~shiller/data/Fig3-1.xls): real home price index from 1890.
  Piketty, Saez and Zucman, PSZ2022AppendixTablesII(Distrib).xlsx (https://gabriel-zucman.eu/usdina/): Table B1 (pre-tax national income shares),
    Table E1 (household wealth shares), Table G1 (average tax rates, all taxes, by pre-tax income group; equal-split adults).
  Census, hstpov2.xlsx (official poverty rate, all people, 1959-2025). Columbia Center on Poverty and Social Policy, anchored SPM (2012 thresholds),
    with taxes and transfers, 1967-2024.
  CMS national health expenditure (nhe-summary-1960-2024.zip: NHE24_Summary.csv; nhe-type-service-source-funds-1960-2024.zip: NHE2024.csv).
  Jordà, Schularick and Taylor, Macrohistory database R6 (JSTdatasetR6.xlsx): US unemployment and real GDP per person (1913-1946 reading), and
    real housing and equity capital gains (a cross-check of Shiller by era).
  IRS Statistics of Income, Historical Table 23 (irs_soi_histab23.xls): the top statutory income tax rate, 1913-2018 (context only).
  NBER business cycle dates (nber_business_cycle_dates.json, https://data.nber.org/data/cycles/business_cycle_dates.json).
  Supplied by Duke Johnson, Nov 16 (prereg Amendments 2 and 3): the Historical Statistics of the United States table Bd144-157 (hospitals and
    beds by ownership, 1946-1997; hsus_Bd144-157_paste.txt, as received); Health, United States 2017, Table 82 (hus2017_table82.pdf);
    Pettengill, Social Security Bulletin, Nov 1973 (ssa_bulletin_1973-11_pettengill.pdf); Kuhn, Schularick and Steins, Minneapolis Fed
    Institute Working Paper 9, 2018 (kss_2018_iwp9.pdf). The rows used from the three PDFs are transcribed in transcribed_ownership_and_scf.json,
    and each table is checked against its own totals here before use.

Rules (fixed in the preregistration and Amendment 1, before any figure here was computed):
- Eras: E0 1913-1946 (reading only), E1 1947-1972, E2 1973-1983, E3 1984-2007, E4 2008-2025; W 2005-2025 (S74's window) beside E4.
- Yearly changes are December over December (fourth quarter over fourth quarter for quarterly series), assigned to the later year.
- CPI-U is the NSA index (CPIAUCNS) in every era. Food: CPI food 1948-1952, food at home from 1953. Shelter from 1954. Medical from 1948.
  Unemployment: the year's mean of UNRATE from 1948 (JST before, E0 only). Growth: real GDP per person, Q4 over Q4, from 1948 (JST before, E0 only).
- Homes: Shiller's real index (yearly values before 1953, December values from 1953), continued after January 2023 with Case-Shiller (NSA) over
  CPI-U, linked at December 2022. Shares: Shiller's real price (December for yearly changes; monthly for drawdowns), continued after December 2022
  with FRED's S&P 500 (month's average) over CPIAUCSL, as S74.
- Drawdowns: the largest fall from a peak to a later trough, both inside the era; recovery is the first later date the peak is regained (may be
  after the era).
- Era comparisons (means and standard deviations of yearly values): later era minus earlier era, a moving-block bootstrap of each era on its own
  (block 3 years, 10,000 replicates, numpy default_rng(75), drawn in a fixed order), two-sided p, Holm across the 14 tests of each pair.
- The estimated rule: quarterly OLS of the policy rate on CPI-U's four-quarter change and CBO's output gap, Newey-West (4 lags).

Usage: python3 sources/s75_eras.py           write sources/s75_eras.json and dev/runs/s75-panel/tables.md, print the tables
       python3 sources/s75_eras.py check     rebuild in memory and fail if the committed JSON differs
Needs numpy, pandas, openpyxl, xlrd, statsmodels, scipy.
"""
import csv, hashlib, json, math, os, re, sys
from collections import defaultdict
import warnings
warnings.filterwarnings('ignore')
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, 's75_eras', 'raw')
RAW74 = os.path.join(HERE, 's74_history', 'raw')
OUT = os.path.join(HERE, 's75_eras.json')
TAB = os.path.join(HERE, '..', 'dev', 'runs', 's75-panel', 'tables.md')
ERAS = [('E0', 1913, 1946), ('E1', 1947, 1972), ('E2', 1973, 1983), ('E3', 1984, 2007), ('E4', 2008, 2025), ('W', 2005, 2025)]
ERA_NAME = {'E0': '1913-1946 (reading)', 'E1': '1947-1972', 'E2': '1973-1983', 'E3': '1984-2007', 'E4': '2008-2025', 'W': '2005-2025'}
PAIRS = [('E1', 'E4'), ('E2', 'E4'), ('E3', 'E4'), ('E1', 'W'), ('E2', 'W'), ('E3', 'W'), ('E1', 'E2'), ('E3', 'E2')]
B_REPS, BLOCK, SEED = 10000, 3, 75
SHA = {}


def sha(path):
    h = hashlib.sha256(open(path, 'rb').read()).hexdigest()
    SHA[os.path.relpath(path, HERE)] = h
    return h


def fred(sid, raw=RAW):
    p = os.path.join(raw, sid + '.csv'); sha(p)
    out = []
    with open(p, newline='') as f:
        r = csv.reader(f); next(r)
        for row in r:
            if len(row) < 2 or row[1] in ('', '.'):
                continue
            out.append((int(row[0][:4]), int(row[0][5:7]), float(row[1])))
    return out


def dec(rows, month=12):
    return {y: v for y, m, v in rows if m == month}


def chg(levels):
    return {y: 100.0 * (levels[y] / levels[y - 1] - 1) for y in levels if y - 1 in levels}


PARTIAL = {}
HSUS_FLAGS = {}


def ymean(rows, name=None, last=2025):
    """The year's mean of a monthly series; the last year is kept with the months the file holds, flagged (prereg: nothing is filled in)."""
    acc = defaultdict(list)
    for y, m, v in rows:
        acc[y].append(v)
    if name and last in acc and len(acc[last]) < 12:
        PARTIAL[name] = '%d of 12 months in %d' % (len(acc[last]), last)
    return {y: sum(v) / len(v) for y, v in acc.items() if len(v) == 12 or (name and y == last)}


def era_vals(d, e):
    _, a, b = [x for x in ERAS if x[0] == e][0]
    return [(y, d[y]) for y in range(a, b + 1) if y in d and d[y] is not None and not (isinstance(d[y], float) and math.isnan(d[y]))]


def r(x, k=2):
    return None if x is None or (isinstance(x, float) and math.isnan(x)) else round(float(x), k)


# ---------------------------------------------------------------- sources
def load():
    import pandas as pd, openpyxl
    S = {}
    cpins = fred('CPIAUCNS'); S['cpi_m'] = cpins
    S['cpi'] = chg(dec(cpins))
    S['cpi_sa_W'] = chg(dec(fred('CPIAUCSL', RAW74)))
    food_all = chg(dec(fred('CPIUFDSL'))); food_home = chg(dec(fred('CUSR0000SAF11', RAW74)))
    S['food'] = {y: (food_home[y] if y >= 1953 else food_all[y]) for y in set(food_all) | set(food_home) if (y >= 1953 and y in food_home) or (y < 1953 and y in food_all)}
    S['shelter'] = chg(dec(fred('CUSR0000SAH1', RAW74)))
    S['medical'] = chg(dec(fred('CPIMEDSL', RAW74)))
    S['unemp'] = ymean(fred('UNRATE', RAW74), 'unemployment')
    gq = fred('A939RX0Q048SBEA'); S['growth'] = chg(dec(gq, 10))
    S['usrec'] = fred('USREC', RAW74)
    nb = os.path.join(RAW, 'nber_business_cycle_dates.json'); sha(nb)
    S['peaks'] = [p['peak'] for p in json.load(open(nb)) if p.get('peak')]
    # JST (E0 reading; cross-check)
    jp = os.path.join(RAW, 'JSTdatasetR6.xlsx'); sha(jp)
    j = pd.read_excel(jp); u = j[j.iso == 'USA'].set_index('year')
    S['jst_unemp'] = {int(y): float(v) for y, v in u.unemp.dropna().items()}
    g = u.rgdpbarro.dropna(); S['jst_growth'] = {int(y): 100 * (g[y] / g[y - 1] - 1) for y in g.index if y - 1 in g.index}
    cpi_j = u.cpi
    S['jst_home_real'] = {int(y): 100 * ((1 + u.housing_capgain[y]) / (cpi_j[y] / cpi_j[y - 1]) - 1) for y in u.index if y - 1 in u.index and not math.isnan(u.housing_capgain[y])}
    S['jst_eq_real'] = {int(y): 100 * ((1 + u.eq_capgain[y]) / (cpi_j[y] / cpi_j[y - 1]) - 1) for y in u.index if y - 1 in u.index and not math.isnan(u.eq_capgain[y])}
    # Shiller real share price, monthly; spliced after Dec 2022 as S74
    ie = os.path.join(HERE, 's59_shiller', 'ie_data.xls'); sha(ie)
    s = pd.read_excel(ie, sheet_name='Data', header=None, skiprows=8).iloc[:, [0, 7]].dropna()
    s.columns = ['d', 'rp']; s = s[pd.to_numeric(s.d, errors='coerce').notna()].astype(float)
    eqm = {}
    for d_, rp in zip(s.d, s.rp):
        y = int(d_); m = int(round((d_ - y) * 100)); eqm[(y, m)] = rp
    sp = fred('SP500', RAW74); spm = defaultdict(list)
    for y, m, v in sp:
        spm[(y, m)].append(v)
    cpim = {(y, m): v for y, m, v in fred('CPIAUCSL', RAW74)}
    spr = {k: (sum(v) / len(v)) / cpim[k] for k, v in spm.items() if k in cpim}
    link = (2022, 12)
    for k, v in sorted(spr.items()):
        if k > link:
            eqm[k] = eqm[link] * v / spr[link]
    S['eq_m'] = sorted((y, m, v) for (y, m), v in eqm.items())
    S['eq'] = chg({y: v for (y, m), v in eqm.items() if m == 12})
    # Shiller real home price; yearly before 1953, December from 1953; Case-Shiller over CPI-U after Jan 2023, linked at Dec 2022
    hp = os.path.join(RAW, 'Fig3-1.xls'); sha(hp)
    h = pd.read_excel(hp, header=None, skiprows=7).iloc[:, [0, 1]].dropna()
    h = h[pd.to_numeric(h[0], errors='coerce').notna()].astype(float)
    hy = defaultdict(dict)
    for d_, v in zip(h[0], h[1]):
        y = int(round(d_ * 12)) // 12; m = int(round(d_ * 12)) % 12 + 1; hy[y][m] = v
    home = {}
    for y, mm in hy.items():
        if y < 1953:
            home[y] = mm[min(mm)]
        elif 12 in mm:
            home[y] = mm[12]
    cs = dec(fred('CSUSHPINSA', RAW74)); cpid = dec(cpins)
    for y in cs:
        if y > 2022 and y in cpid:
            home[y] = home[2022] * (cs[y] / cpid[y]) / (cs[2022] / cpid[2022])
    S['home_lvl'] = home; S['home'] = chg(home)
    S['home_link_check'] = {str(y): [r(100 * (home[y] / home[y - 1] - 1)), r(100 * ((cs[y] / cpid[y]) / (cs[y - 1] / cpid[y - 1]) - 1))] for y in range(2015, 2023) if y in cs and y - 1 in cs}
    # PSZ
    pz = os.path.join(RAW, 'PSZ2022AppendixTablesII(Distrib).xlsx'); sha(pz)
    wb = openpyxl.load_workbook(pz, read_only=True, data_only=True)

    def psz(sheet):
        rows = list(wb[sheet].iter_rows(values_only=True)); hdr = None; out = defaultdict(dict)
        for row in rows:
            if row and row[0] is None and row[1] in ('Bottom 90%', 'All'):
                hdr = row
            elif hdr and isinstance(row[0], (int, float)) and 1900 < row[0] < 2100:
                for k, name in enumerate(hdr):
                    if name and isinstance(row[k], (int, float)):
                        out[name.strip()][int(row[0])] = 100.0 * row[k]
        return out
    S['psz_inc'] = psz('TB1'); S['psz_wealth'] = psz('TE1'); S['psz_tax'] = psz('TG1')
    # poverty
    hpv = os.path.join(RAW, 'hstpov2.xlsx'); sha(hpv)
    d = pd.read_excel(hpv, header=None); pov = {}
    for i in range(8, len(d)):
        c0 = d.iloc[i, 0]
        if isinstance(c0, str) and not re.match(r'^\d{4}', c0.strip()):
            break  # end of the All Races block
        y = int(str(c0).strip()[:4])
        if y not in pov:  # the first listed of a year shown twice (2013, 2017: the redesigned estimate)
            pov[y] = float(d.iloc[i, 3])
    S['pov_off'] = pov
    cp = os.path.join(RAW, 'Columbia-SPM-1967-2024.xlsx'); sha(cp)
    c = pd.read_excel(cp, sheet_name='Poverty Rates', header=None)
    S['pov_spm'] = {int(c.iloc[i, 0]): 100 * float(c.iloc[i, 2]) for i in range(2, len(c)) if pd.notna(c.iloc[i, 0]) and str(c.iloc[i, 0]).strip().isdigit() and pd.notna(c.iloc[i, 2])}
    # NHE
    import zipfile, io
    zs = os.path.join(RAW, 'nhe-summary-1960-2024.zip'); sha(zs)
    with zipfile.ZipFile(zs) as z:
        txt = z.read([n for n in z.namelist() if n.endswith('.csv')][0]).decode('latin-1')
    rows = list(csv.reader(io.StringIO(txt)))
    yrs = [int(x) for x in next(row for row in rows if row and row[0].strip() == 'Expenditure Amount')[1:] if x.strip().isdigit()]

    def nrow(prefix):
        for row in rows:
            if row and row[0].strip().startswith(prefix):
                return {y: float(v.replace(',', '')) for y, v in zip(yrs, row[1:]) if v.strip()}
    S['nhe_gdp'] = nrow('National Health Expenditures as a Percent of Gross Domestic Product')
    S['nhe_pc'] = nrow('National Health Expenditures (Per Capita Amount)')
    zt = os.path.join(RAW, 'nhe-type-service-source-funds-1960-2024.zip'); sha(zt)
    with zipfile.ZipFile(zt) as z:
        txt = z.read([n for n in z.namelist() if n.endswith('.csv')][0]).decode('latin-1')
    rows2 = list(csv.reader(io.StringIO(txt)))
    hdr = [x for x in rows2 if x and x[0].strip() == 'Expenditure Amount' or (x and x[0].strip().startswith('Expenditure'))]
    yrs2 = [int(x) for x in (hdr[0] if hdr else rows2[1])[1:] if x.strip().isdigit()]
    tot = oop = None
    for i, row in enumerate(rows2):
        if row and row[0].strip() == 'Total National Health Expenditures' and tot is None:
            tot = {y: float(v.replace(',', '')) for y, v in zip(yrs2, row[1:]) if v.strip()}
            nxt = rows2[i + 1]; oop = {y: float(v.replace(',', '')) for y, v in zip(yrs2, nxt[1:]) if v.strip()}
            assert nxt[0].strip() == 'Out of pocket'
    S['nhe_oop'] = {y: 100 * oop[y] / tot[y] for y in tot if y in oop}
    cpa = ymean(cpins)
    S['nhe_real_pc'] = chg({y: S['nhe_pc'][y] / cpa[y] for y in S['nhe_pc'] if y in cpa})
    # IRS top statutory rate (context)
    ir = os.path.join(RAW, 'irs_soi_histab23.xls'); sha(ir)
    t = pd.read_excel(ir, header=None); top = {}
    for i in range(8, len(t)):
        y = str(t.iloc[i, 0]).strip()[:4]
        if y.isdigit() and int(y) not in top:
            v = re.sub(r'\[\d+\]', '', str(t.iloc[i, 6])).strip()
            try:
                top[int(y)] = float(v)
            except ValueError:
                pass
    S['top_stat'] = top
    # quarterly series for the rule
    S['ff_m'] = fred('FEDFUNDS', RAW74); S['tb3_m'] = fred('TB3MS', RAW74)
    S['gdpc1'] = fred('GDPC1', RAW74); S['gdppot'] = fred('GDPPOT', RAW74)
    wx = os.path.join(RAW74, 'WuXiaShadowRate.xlsx'); sha(wx)
    ws = openpyxl.load_workbook(wx, read_only=True, data_only=True).worksheets[0]
    S['wx'] = {(row[0].year, row[0].month): (float(row[2]), float(row[1])) for row in ws.iter_rows(min_row=2, values_only=True) if row[0] is not None and row[2] is not None}
    # hospital ownership (Amendment 2) and SCF+ (Amendment 3)
    for f in ('hus2017_table82.pdf', 'ssa_bulletin_1973-11_pettengill.pdf', 'kss_2018_iwp9.pdf'):
        sha(os.path.join(RAW, f))
    hp_ = os.path.join(RAW, 'hsus_Bd144-157_paste.txt'); sha(hp_)
    own = {}
    for line in open(hp_):
        if line.startswith('#'):
            continue
        c = [x.strip() for x in line.rstrip('\n').split('\t') if x.strip() != '']
        if len(c) >= 16 and re.match(r'^\d{4}$', c[1]):
            v = [None if x == '----' else int(x.replace(',', '')) for x in c[2:16]]
            if v[12] is None:
                continue  # 1994 on: only total and federal
            z = lambda k: v[k] or 0
            for off, tag in ((0, 'hosp'), (1, 'beds')):
                gov = z(2 + off) + z(4 + off) + z(6 + off); np_ = z(8 + off) + z(10 + off); pr = z(12 + off)
                if gov + np_ + pr != v[off]:  # shares are over the groups' sum; a row whose stated total differs is flagged (1957 beds: 30,000)
                    HSUS_FLAGS['%s %s' % (c[1], tag)] = {'groups': gov + np_ + pr, 'stated total': v[off]}
                tot = gov + np_ + pr
                own.setdefault(tag, {}).setdefault('government', {})[int(c[1])] = 100.0 * gov / tot
                own[tag].setdefault('non-profit', {})[int(c[1])] = 100.0 * np_ / tot
                own[tag].setdefault('proprietary', {})[int(c[1])] = 100.0 * pr / tot
    S['own'] = own
    tj = os.path.join(RAW, 'transcribed_ownership_and_scf.json'); sha(tj); T = json.load(open(tj))
    t82 = T['hus2017_table82']; adm = {}
    for k, y in enumerate(t82['years']):
        a, b, c_, tot = t82['nonprofit'][k], t82['forprofit'][k], t82['state_local'][k], t82['community'][k]
        assert abs(a + b + c_ - tot) <= 2, ('Table 82 does not add up', y)
        adm[y] = {'non-profit': r(100.0 * a / tot, 1), 'for-profit': r(100.0 * b / tot, 1), 'state-local government': r(100.0 * c_ / tot, 1)}
    S['adm82'] = adm
    pt = T['pettengill1973_table2']; pet = {}
    for k, y in enumerate(pt['years']):
        n_, f_, tot = pt['revenue_nonprofit'][k], pt['revenue_forprofit'][k], pt['revenue_total'][k]
        assert abs(n_ + f_ - tot) <= 1, ('Pettengill Table 2 does not add up', y)
        pet[y] = {'for-profit % of revenue': r(100.0 * f_ / tot), 'net income % of revenue, non-profit': r(100.0 * pt['net_income_nonprofit'][k] / n_),
                  'net income % of revenue, for-profit': r(100.0 * pt['net_income_forprofit'][k] / f_)}
    for y in set(pt['estimated_by_source']['revenue_nonprofit']) | set(pt['estimated_by_source']['revenue_forprofit']):
        pet[y]['note'] = "the source's estimate: 1969's split assumed, so the for-profit share is not an observation"
    S['pet'] = pet; S['pet_estimated'] = pt['estimated_by_source']
    kf = T['kss2018_tableF']; scf = {'top10': {}, 'bottom50': {}, 'gini': {}}
    for k, y in enumerate(kf['years']):
        assert abs(kf['wealth_bottom50'][k] + kf['wealth_50to90'][k] + kf['wealth_top10'][k] - 100) <= 0.2, ('SCF+ Table F does not add up', y)
        scf['top10'][y] = kf['wealth_top10'][k]; scf['bottom50'][y] = kf['wealth_bottom50'][k]; scf['gini'][y] = float(kf['wealth_gini'][k])
    S['scf'] = scf
    return S


# ---------------------------------------------------------------- measures
def describe(d, e):
    v = era_vals(d, e)
    if len(v) < 2:
        return None
    x = np.array([b for a, b in v])
    hi = max(v, key=lambda t: t[1]); lo = min(v, key=lambda t: t[1])
    return {'years': '%d-%d' % (v[0][0], v[-1][0]), 'n': len(v), 'mean': r(x.mean()), 'sd': r(x.std(ddof=1)), 'max': [hi[0], r(hi[1])], 'min': [lo[0], r(lo[1])]}


def drawdown(series, a, b):
    """series: sorted list of (t, v) with t a sortable key; peak and trough inside [a, b] (keys)."""
    inside = [(t, v) for t, v in series if a <= t <= b]
    best = (0.0, None, None); pk = inside[0]
    for t, v in inside:
        if v > pk[1]:
            pk = (t, v)
        f = 1 - v / pk[1]
        if f > best[0]:
            best = (f, pk, (t, v))
    if best[1] is None:
        return None
    f, (tp, vp), (tt, vt) = best
    rec = next((t for t, v in series if t > tt and v >= vp), None)
    return {'fall_pct': r(100 * f, 1), 'peak': tp, 'trough': tt, 'recovered': rec}


def months_between(a, b):
    return (b[0] - a[0]) * 12 + (b[1] - a[1])


def boot_stat(x, stat, rng):
    n = len(x); k = int(math.ceil(n / BLOCK)); out = np.empty(B_REPS)
    starts = rng.integers(0, n - BLOCK + 1, size=(B_REPS, k))
    idx = (starts[:, :, None] + np.arange(BLOCK)[None, None, :]).reshape(B_REPS, -1)[:, :n]
    xs = x[idx]
    return xs.mean(axis=1) if stat == 'mean' else xs.std(axis=1, ddof=1)


# measure key, series key, statistic, the direction that is "less stable" for the later era (+1: higher is less stable)
TESTS = [('A1 inflation mean', 'cpi', 'mean', 1), ('A1 inflation sd', 'cpi', 'sd', 1),
         ('A2 food mean', 'food', 'mean', 1), ('A2 food sd', 'food', 'sd', 1),
         ('A2 shelter mean', 'shelter', 'mean', 1), ('A2 shelter sd', 'shelter', 'sd', 1),
         ('A2 medical mean', 'medical', 'mean', 1), ('A2 medical sd', 'medical', 'sd', 1),
         ('A3 unemployment mean', 'unemp', 'mean', 1), ('A3 unemployment sd', 'unemp', 'sd', 1),
         ('A4 growth mean', 'growth', 'mean', -1), ('A4 growth sd', 'growth', 'sd', 1),
         ('A5 shares real change sd', 'eq', 'sd', 1), ('A5 homes real change sd', 'home', 'sd', 1)]


def holm(ps):
    m = len(ps); order = sorted(range(m), key=lambda i: ps[i]); adj = [0.0] * m; run = 0.0
    for k, i in enumerate(order):
        run = max(run, min(1.0, (m - k) * ps[i])); adj[i] = run
    return adj


def compare(S):
    rng = np.random.default_rng(SEED); res = {}
    for a, b in PAIRS:
        rows = []
        for name, key, stat, sgn in TESTS:
            xa = np.array([v for _, v in era_vals(S[key], a)]); xb = np.array([v for _, v in era_vals(S[key], b)])
            fa = xa.mean() if stat == 'mean' else xa.std(ddof=1); fb = xb.mean() if stat == 'mean' else xb.std(ddof=1)
            ba = boot_stat(xa, stat, rng); bb = boot_stat(xb, stat, rng); dd = bb - ba
            p = min(1.0, 2 * min((dd <= 0).mean(), (dd >= 0).mean()))
            rows.append({'measure': name, 'earlier': r(fa), 'later': r(fb), 'diff': r(fb - fa), 'ci95': [r(np.percentile(dd, 2.5)), r(np.percentile(dd, 97.5))], 'p': r(p, 4), 'sgn': sgn})
        for row, pa in zip(rows, holm([x['p'] for x in rows])):
            row['p_holm'] = r(pa, 4)
            if pa < 0.05:
                row['verdict'] = 'less stable' if row['diff'] * row['sgn'] > 0 else 'more stable'
            else:
                row['verdict'] = 'no clear difference'
            del row['sgn']
        res['%s vs %s' % (b, a)] = rows
    # Duke's view: W against E1, E2 and E3 together
    tally = []
    for i, (name, _, _, _) in enumerate(TESTS):
        v = [next(x for x in res['W vs %s' % e] if x['measure'] == name)['verdict'] for e in ('E1', 'E2', 'E3')]
        if all(x == 'less stable' for x in v):
            t = 'supported'
        elif 'more stable' in v and 'less stable' not in v:
            t = 'against it'
        else:
            t = 'mixed'
        tally.append({'measure': name, 'vs 1947-1972': v[0], 'vs 1973-1983': v[1], 'vs 1984-2007': v[2], 'reading': t})
    return res, tally


def rule_fit(S):
    import statsmodels.api as sm
    from scipy.optimize import least_squares

    def qavg(rows):
        acc = defaultdict(list)
        for y, m, v in rows:
            acc[(y, (m - 1) // 3 + 1)].append(v)
        return {k: sum(v) / len(v) for k, v in acc.items() if len(v) == 3}
    ff = {(y, m): v for y, m, v in S['ff_m']}; tb = {(y, m): v for y, m, v in S['tb3_m']}
    eff, shadow = [], []
    for y in range(1947, 2026):
        for m in range(1, 13):
            if (y, m) in ff:
                v = ff[(y, m)]
            elif (y, m) in tb and (y, m) < (1954, 7):
                v = tb[(y, m)]
            else:
                continue
            eff.append((y, m, v)); w = S['wx'].get((y, m))
            shadow.append((y, m, w[0] if (w is not None and v < 0.25 and y >= 2008) else v))
    iq_e, iq_s = qavg(eff), qavg(shadow)
    cq = qavg(S['cpi_m']); piq = {k: 100 * (cq[k] / cq[(k[0] - 1, k[1])] - 1) for k in cq if (k[0] - 1, k[1]) in cq}
    g = {(y, (m - 1) // 3 + 1): v for y, m, v in S['gdpc1']}; p = {(y, (m - 1) // 3 + 1): v for y, m, v in S['gdppot']}
    gap = {k: 100 * (g[k] / p[k] - 1) for k in g if k in p}
    fits = {}
    spec = [('E1', (1949, 1), (1972, 4), iq_e), ('E1 from 1951Q2', (1951, 2), (1972, 4), iq_e), ('E2', (1973, 1), (1983, 4), iq_e),
            ('E3', (1984, 1), (2007, 4), iq_e), ('E4', (2008, 1), (2025, 4), iq_s), ('E4 effective rate (reading)', (2008, 1), (2025, 4), iq_e),
            ('W', (2005, 1), (2025, 4), iq_s)]
    for name, q0, q1, iq in spec:
        ks = [k for k in sorted(iq) if q0 <= k <= q1 and k in piq and k in gap]
        y = np.array([iq[k] for k in ks]); X = np.column_stack([np.ones(len(ks)), [piq[k] for k in ks], [gap[k] for k in ks]])
        m = sm.OLS(y, X).fit(cov_type='HAC', cov_kwds={'maxlags': 4})
        c, phi, beta = m.params; se = m.bse
        # smoothed reading (point estimates only)
        ks2 = [k for k in ks if (k[0] if k[1] > 1 else k[0] - 1, k[1] - 1 if k[1] > 1 else 4) in iq]
        lag = np.array([iq[(k[0] if k[1] > 1 else k[0] - 1, k[1] - 1 if k[1] > 1 else 4)] for k in ks2])
        y2 = np.array([iq[k] for k in ks2]); pi2 = np.array([piq[k] for k in ks2]); g2 = np.array([gap[k] for k in ks2])
        sol = least_squares(lambda b: y2 - (b[0] * lag + (1 - b[0]) * (b[1] + b[2] * pi2 + b[3] * g2)), x0=[0.7, c, phi, beta], bounds=([0, -50, -10, -10], [0.99, 50, 10, 10]))
        fits[name] = {'quarters': '%dQ%d-%dQ%d' % (ks[0] + ks[-1]), 'n': len(ks), 'c': r(c), 'phi': r(phi), 'beta': r(beta),
                      'se': [r(se[0]), r(se[1]), r(se[2])], 'r2': r(m.rsquared), 'a': r(phi - 1), 'b': r(beta), 'rstar_at_2pct': r(c + (phi - 1) * 2),
                      'smoothed': {'rho': r(sol.x[0]), 'c': r(sol.x[1]), 'phi': r(sol.x[2]), 'beta': r(sol.x[3])}}
    return fits


def level_summary(d, e):
    v = era_vals(d, e)
    if not v:
        return None
    x = [b for a, b in v]; hi = max(v, key=lambda t: t[1])
    return {'years': '%d-%d' % (v[0][0], v[-1][0]), 'start': r(v[0][1]), 'end': r(v[-1][1]), 'change': r(v[-1][1] - v[0][1]), 'mean': r(sum(x) / len(x)), 'max': [hi[0], r(hi[1])]}


def build():
    S = load(); out = {'eras': ERA_NAME, 'A': {}, 'B': {}, 'checks': {}}
    for e, a, b in ERAS:
        A = {}
        A['A1 inflation'] = describe(S['cpi'], e)
        iv = era_vals(S['cpi'], e)
        A['A1 inflation']['years_above_5'] = [y for y, v in iv if v > 5]; A['A1 inflation']['years_falling'] = [y for y, v in iv if v < 0]
        for k in ('food', 'shelter', 'medical'):
            dsc = describe(S[k], e)
            if dsc:
                rel = [S[k][y] - S['cpi'][y] for y, _ in era_vals(S[k], e)]
                dsc['mean_minus_cpi'] = r(sum(rel) / len(rel))
            A['A2 ' + k] = dsc
        A['A3 unemployment'] = describe(S['unemp'] if e != 'E0' else S['jst_unemp'], e)
        rec = [v for y, m, v in S['usrec'] if a <= y <= b]
        A['A3 months in recession %'] = r(100 * sum(rec) / len(rec), 1)
        A['A3 recessions starting'] = [p_[:7] for p_ in S['peaks'] if a <= int(p_[:4]) <= b]
        A['A4 growth per person'] = describe(S['growth'] if e != 'E0' else S['jst_growth'], e)
        A['A5 shares real change'] = describe(S['eq'], e); A['A5 homes real change'] = describe(S['home'], e)
        dd = drawdown([((y, m), v) for y, m, v in S['eq_m']], (a, 1), (b, 12))
        if dd:
            dd['months_to_recover'] = months_between(dd['trough'], dd['recovered']) if dd['recovered'] else None
            dd['peak'] = '%d-%02d' % dd['peak']; dd['trough'] = '%d-%02d' % dd['trough']; dd['recovered'] = '%d-%02d' % dd['recovered'] if dd['recovered'] else 'not by the end of the data'
        A['A5 shares drawdown (monthly)'] = dd
        hd = drawdown(sorted(S['home_lvl'].items()), a, b)
        if hd:
            hd['years_to_recover'] = (hd['recovered'] - hd['trough']) if hd['recovered'] else None
            if not hd['recovered']:
                hd['recovered'] = 'not by the end of the data'
        A['A5 homes drawdown (yearly)'] = hd
        A['JST cross-check: mean real change, homes / shares (Shiller | JST)'] = [r(np.mean([v for _, v in era_vals(S['home'], e)])), r(np.mean([v for _, v in era_vals(S['jst_home_real'], e)]) if era_vals(S['jst_home_real'], e) else None),
                                                                                r(np.mean([v for _, v in era_vals(S['eq'], e)])), r(np.mean([v for _, v in era_vals(S['jst_eq_real'], e)]) if era_vals(S['jst_eq_real'], e) else None)]
        out['A'][e] = A
        B = {}
        for nm, src in (('B1 top 10% income share', S['psz_inc']['Top 10%']), ('B1 top 1% income share', S['psz_inc']['Top 1%']),
                        ('B1 top 10% wealth share', S['psz_wealth']['Top 10%']), ('B1 top 1% wealth share', S['psz_wealth']['Top 1%']),
                        ('B1 bottom 50% wealth share', S['psz_wealth']['Bottom 50%']),
                        ('B2 official poverty %', S['pov_off']), ('B2 anchored SPM poverty %', S['pov_spm']),
                        ('B3 health spending % of GDP', S['nhe_gdp']), ('B3 out-of-pocket % of health spending', S['nhe_oop'])):
            B[nm] = level_summary(src, e)
        B['B3 real health spending per person, yearly growth'] = describe(S['nhe_real_pc'], e)
        for tag, lab in (('hosp', 'hospitals'), ('beds', 'beds')):
            for g in ('government', 'non-profit', 'proprietary'):
                B['B3 all hospitals (HSUS): %s %% of %s' % (g, lab)] = level_summary(S['own'][tag][g], e)
        B['B1 SCF+ top 10% wealth share (survey years)'] = level_summary(S['scf']['top10'], e)
        B['B1 SCF+ bottom 50% wealth share (survey years)'] = level_summary(S['scf']['bottom50'], e)
        B['B1 SCF+ wealth Gini x100 (survey years)'] = level_summary(S['scf']['gini'], e)
        for g in ('All', 'Bottom 50%', 'Middle 40%', 'Top 10%', 'Top 1%', 'Top 0.1%'):
            B['B4 average tax rate, ' + g] = level_summary(S['psz_tax'][g], e)
        B['B4 top statutory rate (context; IRS SOI)'] = level_summary(S['top_stat'], e)
        out['B'][e] = B
    out['B3 community hospital admissions by ownership, % (Health, United States 2017, Table 82)'] = S['adm82']
    out['B3 private community hospitals, 1961-1971 (Pettengill 1973, Table 2)'] = dict(S['pet'], estimated_by_source=S['pet_estimated'])
    out['B5 estimated rule'] = rule_fit(S)
    out['comparisons'], out['dukes_view'] = compare(S)
    tx = S['psz_tax']
    out['checks']['planning figures (PSZ average tax rate, all taxes)'] = {
        'top 1% 1950-1959 mean': [r(np.mean([tx['Top 1%'][y] for y in range(1950, 1960)]), 1), 42.0],
        'top 0.1% 1950-1959 mean': [r(np.mean([tx['Top 0.1%'][y] for y in range(1950, 1960)]), 1), 50.6],
        'top 1% 2014': [r(tx['Top 1%'][2014], 1), 36.4], 'top 0.1% 2014': [r(tx['Top 0.1%'][2014], 1), 39.8],
        'note': '[file, planning]'}
    out['checks']['HSUS rows whose stated total differs from the sum of its ownership groups (shares use the sum)'] = HSUS_FLAGS
    out['checks']['PSZ last year'] = {'income': max(S['psz_inc']['Top 1%']), 'wealth': max(S['psz_wealth']['Top 1%']), 'tax': max(S['psz_tax']['Top 1%'])}
    out['checks']['CPI-U 2005-2025 NSA vs SA (S74): mean, sd'] = [[r(np.mean([v for _, v in era_vals(S['cpi'], 'W')])), r(np.std([v for _, v in era_vals(S['cpi'], 'W')], ddof=1))],
                                                                    [r(np.mean([v for _, v in era_vals(S['cpi_sa_W'], 'W')])), r(np.std([v for _, v in era_vals(S['cpi_sa_W'], 'W')], ddof=1))]]
    out['checks']['home link: Shiller vs Case-Shiller real change 2015-2022'] = S['home_link_check']
    out['_meta'] = {'built_by': 'sources/s75_eras.py', 'downloaded': {'s74_history/raw': '2026-11-14', 's75_eras/raw': '2026-11-16'}, 'sha256': dict(sorted(SHA.items())),
                    'partial': dict(PARTIAL, rule='the last quarter fitted is the last with three CPI months (October 2025 is missing from the CPI file)'), 'bootstrap': {'replicates': B_REPS, 'block': BLOCK, 'seed': SEED}}
    return out


def fmt(v):
    if v is None:
        return 'n/a'
    if isinstance(v, dict):
        return ', '.join('%s %s' % (k, fmt(x)) for k, x in v.items())
    if isinstance(v, list):
        return '[' + ', '.join(fmt(x) for x in v) + ']'
    return str(v)


def table(o):
    L = ['# S75 descriptive panel: US policy eras (no engine)', '',
         'Built by `sources/s75_eras.py` from the files in its docstring; preregistration research-update `prereg/2026-11-s75-deep-history.md` (Part A, Amendment 1). Yearly changes in %, December over December; levels in %.', '']
    eras = [e for e, _, _ in ERAS]
    L += ['## A. Stability measures by era', '', '| measure | ' + ' | '.join(ERA_NAME[e] for e in eras) + ' |', '|---|' + '---|' * len(eras)]
    for k in o['A']['E1']:
        L.append('| %s | %s |' % (k, ' | '.join(fmt(o['A'][e].get(k)) for e in eras)))
    L += ['', '## B. Policy and distribution by era', '', '| measure | ' + ' | '.join(ERA_NAME[e] for e in eras) + ' |', '|---|' + '---|' * len(eras)]
    for k in o['B']['E1']:
        L.append('| %s | %s |' % (k, ' | '.join(fmt(o['B'][e].get(k)) for e in eras)))
    for k in ('B3 community hospital admissions by ownership, % (Health, United States 2017, Table 82)', 'B3 private community hospitals, 1961-1971 (Pettengill 1973, Table 2)'):
        L += ['', '### ' + k, '']
        for y, v in o[k].items():
            L.append('- %s: %s' % (y, fmt(v)))
    L += ['', '## B5. The central bank\'s rule as estimated in each era', '', 'i = c + phi x inflation + beta x gap (quarterly OLS, Newey-West 4 lags); S74 terms a = phi - 1, b = beta; r* at a 2% target = c + 2a.', '',
          '| fit | quarters | n | c | phi | beta | se (c, phi, beta) | R2 | a | b | r* | smoothed (rho, c, phi, beta) |', '|---|---|---|---|---|---|---|---|---|---|---|---|']
    for k, f in o['B5 estimated rule'].items():
        s = f['smoothed']
        L.append('| %s | %s | %d | %s | %s | %s | %s | %s | %s | %s | %s | %s, %s, %s, %s |' % (k, f['quarters'], f['n'], f['c'], f['phi'], f['beta'], fmt(f['se']), f['r2'], f['a'], f['b'], f['rstar_at_2pct'], s['rho'], s['c'], s['phi'], s['beta']))
    L += ['', '## Era comparisons (later era minus earlier; block bootstrap; Holm across the 14 tests of each pair)', '']
    for pair, rows in o['comparisons'].items():
        b, a = pair.split(' vs ')
        L += ['### %s minus %s' % (ERA_NAME[b], ERA_NAME[a]), '', '| measure | %s | %s | difference | 95%% interval | p | Holm p | reading for %s |' % (ERA_NAME[a], ERA_NAME[b], ERA_NAME[b]), '|---|---|---|---|---|---|---|---|']
        for x in rows:
            L.append('| %s | %s | %s | %s | %s to %s | %s | %s | %s |' % (x['measure'], x['earlier'], x['later'], x['diff'], x['ci95'][0], x['ci95'][1], x['p'], x['p_holm'], x['verdict']))
        L.append('')
    L += ['## Duke\'s view: was 2005-2025 less stable than the decades before it? (per measure; prereg decision rule)', '', '| measure | vs 1947-1972 | vs 1973-1983 | vs 1984-2007 | reading |', '|---|---|---|---|---|']
    for x in o['dukes_view']:
        L.append('| %s | %s | %s | %s | %s |' % (x['measure'], x['vs 1947-1972'], x['vs 1973-1983'], x['vs 1984-2007'], x['reading']))
    L += ['', '## Checks', '']
    for k, v in o['checks'].items():
        L.append('- %s: %s' % (k, fmt(v)))
    return '\n'.join(L) + '\n'


if __name__ == '__main__':
    o = build(); js = json.dumps(o, indent=1, sort_keys=False, default=str)
    if len(sys.argv) > 1 and sys.argv[1] == 'check':
        same = open(OUT).read() == js
        print('identical' if same else 'DIFFERS'); sys.exit(0 if same else 1)
    open(OUT, 'w').write(js)
    os.makedirs(os.path.dirname(TAB), exist_ok=True); t = table(o); open(TAB, 'w').write(t); print(t)
