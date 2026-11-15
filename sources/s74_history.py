"""S74 (Nov 14, 2026; research-update prereg/2026-11-s74-central-bank.md): the 2005-2025 history environment's yearly paths, from opened sources.

Everything here is read from files downloaded on Nov 14, 2026 and kept in sources/s74_history/raw/ (SHA-256 of each in the output's _meta):
- FRED (Federal Reserve Bank of St. Louis), https://fred.stlouisfed.org/graph/fredgraph.csv?id=<ID>:
  FEDFUNDS (effective federal funds rate, monthly average), DGS10 (10-year Treasury, daily), MORTGAGE30US and MORTGAGE15US (Freddie Mac PMMS, weekly),
  TB3MS (3-month bill), SP500 (S&P 500 price index, daily, last ten years; used after Shiller's file ends), WALCL (Fed total assets, weekly, $ million), WSHOMCB (Fed holdings of agency MBS, weekly), TREAST (Fed holdings of Treasuries,
  weekly), GDP (nominal GDP, quarterly, $ billion, SAAR), GDPC1 and GDPPOT (real GDP and CBO's real potential GDP), CPIAUCSL (CPI-U all items, SA),
  CPILFESL (core CPI), CUSR0000SAF11 (food at home), CUSR0000SAH1 (shelter), CPIMEDSL (medical care, SA), PCEPI, UNRATE (unemployment rate),
  NROU (CBO's noncyclical rate of unemployment), USREC (NBER recession months), CSUSHPINSA (S&P CoreLogic Case-Shiller national home prices, NSA),
  USSTHPI (FHFA all-transactions house price index, quarterly).
- The Wu-Xia shadow federal funds rate (Federal Reserve Bank of Atlanta, WuXiaShadowRate.xlsx; Wu and Xia 2016, JMCB). The file's series ends
  February 2022; the stance (`shadow`) is the shadow rate in months the effective rate sat at the floor (below 0.25%), otherwise FRED's monthly
  effective rate (so March 2022 on, off the floor, needs no shadow rate).
- Shiller's online data (sources/s59_shiller/ie_data.xls, already in the repository since S59; the file ends Sep 2023): S&P Composite real
  price, monthly; continued from Dec 2022 with FRED's SP500 over CPI-U (the splice and the overlap's agreement are in _meta.eqSplice).
- The Federal Reserve's Distributional Financial Accounts (https://www.federalreserve.gov/releases/z1/dataviz/download/zips/dfa.zip, release files
  dated Sep 15, 2026): net worth by wealth group (top 0.1%, next 0.9%, next 9%, next 40%, bottom 50%), fourth quarter of each year. Used only to
  check the no-programme run, never to set a constant.

Rules (fixed before any engine run; research rule 3: nothing here is tuned):
- Years 2005-2025. Rates are the year's average of the published frequency. Prices are year-end over year-end (December over December; the fourth
  quarter for quarterly series), because the engine revalues balance sheets once a year and the DFA and SCF are year-end stocks. Year averages are
  kept beside them (`_avg`) as a reading.
- Real gains: a nominal index's year-end change deflated by CPI-U's December-over-December change.
- The Fed's balance sheet: the last weekly value of the year, as a share of that year's nominal GDP (average of the four quarters).
- The unemployment gap: the year's average unemployment rate minus CBO's noncyclical rate (NROU), in points.
- 2025: series whose 2025 values are incomplete are flagged in `_meta.partial` (each figure is what the file holds; nothing is filled in).

Usage: python3 sources/s74_history.py           write sources/s74_history.json and print the table
       python3 sources/s74_history.py check     rebuild in memory and fail if the committed file differs
Needs pandas, openpyxl and xlrd.
"""
import csv, hashlib, json, os, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, 's74_history', 'raw')
OUT = os.path.join(HERE, 's74_history.json')
Y0, Y1 = 2005, 2025
YEARS = list(range(Y0, Y1 + 1))


def sha(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


def fred(sid):
    """FRED csv -> list of (year, month, value); '.' (missing) rows are skipped."""
    out = []
    with open(os.path.join(RAW, sid + '.csv'), newline='') as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            if len(row) < 2 or row[1] in ('', '.'):
                continue
            y, m = int(row[0][:4]), int(row[0][5:7])
            out.append((y, m, float(row[1])))
    return out


def year_avg(rows):
    acc = defaultdict(list)
    for y, m, v in rows:
        acc[y].append(v)
    return {y: sum(v) / len(v) for y, v in acc.items()}


def year_end(rows):
    """last observation of each year (rows are in date order)."""
    out = {}
    for y, m, v in rows:
        out[y] = v
    return out


def months_seen(rows):
    acc = defaultdict(set)
    for y, m, v in rows:
        acc[y].add(m)
    return {y: len(s) for y, s in acc.items()}


def pct(a, b):
    return 100.0 * (b / a - 1.0)


def build():
    meta = {'built_by': 'sources/s74_history.py', 'downloaded': '2026-11-14', 'sha256': {}, 'partial': {}, 'rules': __doc__.split('Rules')[1].split('Usage')[0].strip()}
    S = {}
    ids = ['FEDFUNDS', 'DGS10', 'MORTGAGE30US', 'MORTGAGE15US', 'TB3MS', 'WALCL', 'WSHOMCB', 'TREAST', 'GDP', 'GDPC1', 'GDPPOT', 'CPIAUCSL',
           'CPILFESL', 'CUSR0000SAF11', 'CUSR0000SAH1', 'CPIMEDSL', 'PCEPI', 'UNRATE', 'NROU', 'USREC', 'CSUSHPINSA', 'USSTHPI']
    for sid in ids:
        S[sid] = fred(sid)
        meta['sha256'][sid + '.csv'] = sha(os.path.join(RAW, sid + '.csv'))
        seen = months_seen(S[sid])
        q = sid in ('GDP', 'GDPC1', 'GDPPOT', 'NROU', 'USSTHPI')
        if Y1 in seen and seen[Y1] < (4 if q else 12):
            meta['partial'][sid] = '%d of %d %s in %d' % (seen[Y1], 4 if q else 12, 'quarters' if q else 'months', Y1)
        if Y1 not in seen:
            meta['partial'][sid] = 'no %d observation' % Y1
    # Wu-Xia shadow rate (monthly, last business day)
    import openpyxl
    wx = os.path.join(RAW, 'WuXiaShadowRate.xlsx')
    meta['sha256']['WuXiaShadowRate.xlsx'] = sha(wx)
    ws = openpyxl.load_workbook(wx, read_only=True, data_only=True).worksheets[0]
    shadow = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        if row[0] is None or row[2] is None:
            continue
        shadow.append((row[0].year, row[0].month, float(row[2]), float(row[1])))
    wxm = {(y, m): (v, e) for y, m, v, e in shadow}
    # the policy stance each month: Wu-Xia's shadow rate where its effective rate is at the floor (below 0.25%), else FRED's monthly effective rate
    stance = []
    for y, m, v in fred('FEDFUNDS'):
        w = wxm.get((y, m))
        stance.append((y, m, w[0] if (w is not None and w[1] < 0.25) else v))
    if any(v < 0.25 for y, m, v in fred('FEDFUNDS') if (y, m) not in wxm and Y0 <= y <= Y1):
        meta['partial']['shadow'] = 'months at the floor after the Wu-Xia file ends use the effective rate'
    # Shiller real share price (monthly)
    import pandas as pd
    ie = os.path.join(HERE, 's59_shiller', 'ie_data.xls')
    meta['sha256']['s59_shiller/ie_data.xls'] = sha(ie)
    s = pd.read_excel(ie, sheet_name='Data', header=None, skiprows=8).iloc[:, [0, 7]].dropna()
    s.columns = ['d', 'rp']
    s = s[pd.to_numeric(s.d, errors='coerce').notna()].astype(float)
    eq = []
    for d, rp in zip(s.d, s.rp):
        y = int(d); m = int(round((d - y) * 100))
        eq.append((y, m, rp))
    # After Shiller's file ends (Sep 2023): FRED SP500 (S&P 500 price index, daily; FRED holds the last ten years), the month's average,
    # deflated by CPI-U (CPIAUCSL). Shiller's real price is the S&P Composite's monthly average over the CPI, so the two are spliced at the
    # last December both hold; the overlap's agreement is written to _meta.eqSplice.
    sp = fred('SP500'); meta['sha256']['SP500.csv'] = sha(os.path.join(RAW, 'SP500.csv'))
    spm = defaultdict(list)
    for y, m, v in sp:
        spm[(y, m)].append(v)
    cpim = {(y, m): v for y, m, v in fred('CPIAUCSL')}
    spr = {k: (sum(v) / len(v)) / cpim[k] for k, v in spm.items() if k in cpim}
    eqm = {(y, m): v for y, m, v in eq}
    last = max(eqm); lastDec = (last[0] if last[1] == 12 else last[0] - 1, 12)
    ov = [y for y in range(Y0, lastDec[0] + 1) if (y, 12) in spr and (y - 1, 12) in spr and (y - 1, 12) in eqm]
    meta['eqSplice'] = {'shillerLast': '%d-%02d' % last, 'spliceAt': '%d-12' % lastDec[0],
                        'overlap_dec_dec_real_change': {str(y): [round(pct(eqm[(y - 1, 12)], eqm[(y, 12)]), 2), round(pct(spr[(y - 1, 12)], spr[(y, 12)]), 2)] for y in ov}}
    for (y, m), v in sorted(spr.items()):
        if (y, m) > lastDec and (y, m) not in eqm or (y, m) > last:
            eqm[(y, m)] = eqm[lastDec] * v / spr[lastDec]
    eq = [(y, m, eqm[(y, m)]) for (y, m) in sorted(eqm)]
    # DFA net worth by group, Q4
    dfa = os.path.join(RAW, 'dfa', 'dfa-networth-levels.csv')
    meta['sha256']['dfa/dfa-networth-levels.csv'] = sha(dfa)
    nw = defaultdict(dict)
    with open(dfa, newline='') as f:
        for r in csv.DictReader(f):
            if r['Date'].endswith(':Q4'):
                nw[int(r['Date'][:4])][r['Category']] = float(r['Net worth'])

    ff = year_avg(S['FEDFUNDS']); ffe = year_end(S['FEDFUNDS'])
    cpi_e = year_end(S['CPIAUCSL']); cpi_a = year_avg(S['CPIAUCSL'])
    gdp = year_avg(S['GDP'])
    out = {'_meta': meta, 'years': YEARS, 'series': {}}
    col = defaultdict(dict)
    sh_by = defaultdict(list)
    for y, m, v in stance:
        sh_by[y].append(v)
    for y in YEARS:
        c = col
        c['ff'][y] = ff.get(y); c['ffDec'][y] = ffe.get(y)
        c['shadow'][y] = (sum(sh_by[y]) / len(sh_by[y])) if len(sh_by[y]) == 12 else None
        c['y10'][y] = year_avg(S['DGS10']).get(y); c['m30'][y] = year_avg(S['MORTGAGE30US']).get(y); c['m15'][y] = year_avg(S['MORTGAGE15US']).get(y)
        c['tb3'][y] = year_avg(S['TB3MS']).get(y)
        for k, sid in (('fedAssets', 'WALCL'), ('fedMBS', 'WSHOMCB'), ('fedTsy', 'TREAST')):
            v = year_end(S[sid]).get(y)
            c[k][y] = v / 1000.0 if v is not None else None            # $ billion
            c[k + 'GDP'][y] = 100.0 * (v / 1000.0) / gdp[y] if v is not None and y in gdp else None
        for k, sid in (('cpi', 'CPIAUCSL'), ('core', 'CPILFESL'), ('food', 'CUSR0000SAF11'), ('shelter', 'CUSR0000SAH1'), ('medical', 'CPIMEDSL'), ('pce', 'PCEPI')):
            e = year_end(S[sid]); a = year_avg(S[sid])
            c[k][y] = pct(e[y - 1], e[y]) if y in e and y - 1 in e else None
            c[k + '_avg'][y] = pct(a[y - 1], a[y]) if y in a and y - 1 in a and months_seen(S[sid]).get(y) == 12 else None
        u = year_avg(S['UNRATE']).get(y); un = year_avg(S['NROU']).get(y)
        c['unemp'][y] = u; c['nrou'][y] = un; c['ugap'][y] = (u - un) if u is not None and un is not None else None
        rec = [v for yy, m, v in S['USREC'] if yy == y]
        c['recMonths'][y] = int(sum(rec)) if rec else None
        g = year_avg(S['GDPC1']); gp = year_avg(S['GDPPOT'])
        c['ygap'][y] = 100.0 * (g[y] / gp[y] - 1.0) if y in g and y in gp else None
        infl = c['cpi'][y]
        for k, sid in (('homeCS', 'CSUSHPINSA'), ('homeFHFA', 'USSTHPI')):
            e = year_end(S[sid])
            n = pct(e[y - 1], e[y]) if y in e and y - 1 in e else None
            c[k][y] = n
            c[k + 'Real'][y] = 100.0 * ((1 + n / 100.0) / (1 + infl / 100.0) - 1.0) if n is not None and infl is not None else None
        eqe = year_end(eq)
        c['eqReal'][y] = pct(eqe[y - 1], eqe[y]) if y in eqe and y - 1 in eqe and max(m for yy, m, v in eq if yy == y) == 12 else None
        if y in nw:
            tot = sum(nw[y].values())
            c['dfaTop1'][y] = 100.0 * (nw[y]['TopPt1'] + nw[y]['RemainingTop1']) / tot
            c['dfaNext9'][y] = 100.0 * nw[y]['Next9'] / tot
            c['dfaNext40'][y] = 100.0 * nw[y]['Next40'] / tot
            c['dfaBottom50'][y] = 100.0 * nw[y]['Bottom50'] / tot
        else:
            for k in ('dfaTop1', 'dfaNext9', 'dfaNext40', 'dfaBottom50'):
                c[k][y] = None
    if not any(y in nw for y in [Y1]):
        meta['partial']['dfa'] = 'no %d Q4 observation' % Y1
    meta['shadowEnds'] = '%d-%02d' % (shadow[-1][0], shadow[-1][1])
    for k, d in col.items():
        out['series'][k] = [None if d[y] is None else round(d[y], 4) for y in YEARS]
    out['_meta']['units'] = {
        'ff, ffDec, shadow, y10, m30, m15, tb3, unemp, nrou': 'percent a year (ffDec: December average)',
        'ugap': 'points (unemployment minus CBO noncyclical rate)', 'ygap': 'percent of potential output',
        'fedAssets, fedMBS, fedTsy': '$ billion, last week of the year', 'fedAssetsGDP, fedMBSGDP, fedTsyGDP': 'percent of the year\'s nominal GDP',
        'cpi, core, food, shelter, medical, pce': 'percent, December over December (_avg: year average over year average)',
        'homeCS, homeFHFA': 'percent nominal, year-end over year-end (Real: deflated by CPI-U Dec/Dec)', 'eqReal': 'percent, S&P Composite real price, December over December',
        'recMonths': 'NBER recession months in the year', 'dfaTop1, dfaNext9, dfaNext40, dfaBottom50': 'percent of household net worth, Q4'}
    return out


def table(o):
    keys = ['ff', 'shadow', 'm30', 'fedAssetsGDP', 'cpi', 'food', 'shelter', 'medical', 'unemp', 'ugap', 'recMonths', 'homeCSReal', 'eqReal', 'dfaTop1', 'dfaBottom50']
    print('year ' + ' '.join('%8s' % k[:8] for k in keys))
    for i, y in enumerate(o['years']):
        print('%d ' % y + ' '.join('%8s' % ('-' if o['series'][k][i] is None else '%.2f' % o['series'][k][i]) for k in keys))
    print('partial:', json.dumps(o['_meta']['partial']))


if __name__ == '__main__':
    o = build()
    txt = json.dumps(o, indent=1, sort_keys=True)
    if len(sys.argv) > 1 and sys.argv[1] == 'check':
        if open(OUT).read() != txt:
            sys.exit('s74_history.json differs from a rebuild')
        print('ok: s74_history.json matches a rebuild')
    else:
        open(OUT, 'w').write(txt)
        table(o)
