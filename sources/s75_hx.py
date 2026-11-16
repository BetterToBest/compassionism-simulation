#!/usr/bin/env python3
"""S75 part 2 (Nov 16, 2026; research-update prereg/2026-11-s75-deep-history.md, Part B, and Amendment 4): the engine's era paths.
For each era E1-E4, the yearly paths of S74's history environment (HX), plus the era's settings for the arms R (its estimated rule), T (its tax
schedule) and H (its health cost growth). Every figure is read from files already in the repository (S74's and S75's raw files, SHA-256 in _meta)
plus one file added by this step: Census Table F-7 (median family income, all families, 2025 dollars, 1947-2025; f07ar.xlsx, downloaded Nov 16,
2026 from www2.census.gov/programs-surveys/cps/tables/time-series/historical-income-families/).

Rules (Amendment 4, fixed before any engine run):
- An era of L years runs L + 1 engine years: year 0 is the December before the era (the start: price level 1, no revaluation, no recession), and
  year t is the era's t-th year, whose revaluation covers December of the year before to December of the year. E1 1946-1972 (27 engine years),
  E2 1972-1983 (12), E3 1983-2007 (25), E4 2007-2025 (19). Year 0's values are read only as "last year" (the rule's first reading of inflation and
  the gap, the actual stance, the income peak).
- cpi: CPI-U NSA (CPIAUCNS), December over December, as the panel (Amendment 1, item 3). hR, eR: the panel's real home and share price changes
  (Shiller, linked to Case-Shiller and FRED's S&P 500 as in Amendment 1, item 5). food, shel, med: the panel's (food at home from 1953, CPI food
  1948-1952, shelter from 1954, medical from 1948); a year before a series starts takes CPI-U all items (they are read only by the reporting key
  stIo, own inflation).
- ff: the year's mean effective federal funds rate (FEDFUNDS) from 1955 (its first full year); the 3-month bill (TB3MS) before. sh (the actual
  stance): as S74, Wu-Xia's shadow rate in months the effective rate sat below 0.25%, otherwise the effective rate; the bill before 1955.
- m30: the year's mean 30-year mortgage rate (MORTGAGE30US) from 1972 (its first full year); before, JST's long-term government bond rate plus the
  mean spread of the mortgage rate over it in 1972-1981 (the first ten full years both hold).
- ug: the year's mean unemployment rate (UNRATE from 1948; JST before) minus CBO's noncyclical rate (NROU; 1949's value held back before 1949).
  yg: CBO's output gap, 100 x (GDPC1 / GDPPOT - 1), the year's mean of quarters, from 1949; before 1949, -2 x ug (Okun's rule of thumb, the
  engine's own ok = 2). rm: NBER recession months in the year (USREC).
- fa: the Fed's balance sheet as a share of GDP enters only as the actual purchases' effect on the 10-year yield, against year 0; there were no
  large-scale purchases before 2008, so E1-E3 carry 0 (no effect). E4: S74's series (2007-2025).
- mhi: real median family income (Census Table F-7, all families, 2025 dollars) in every era, so the four eras use one series (S74's History keeps
  real median household income); 1946 takes 1947's value. Where a year is listed twice (a method change), the first listed (the newer method).
- T: for each group (bottom 50%, middle 40%, next 9%, top 1% of pre-tax income), the era's mean PSZ average tax rate (all taxes, Table G1) over the
  era's years the file holds (it ends in 2019) minus 2019's, in points. The next 9% is the top 10% less the top 1%, weighted by their pre-tax income
  shares (Table B1); the middle 40% is the file's own from 1962, and before 1962 the bottom 90% less the bottom 50%, with the bottom half's share of
  the bottom 90%'s income held at its 1962 value (Table B1's bottom 50% starts in 1962).
- H: the era's mean real change of medical prices, 100 x ((1 + medical/100)/(1 + CPI-U/100) - 1), over the era's years with medical data.
- R: the era's fitted rule (s75_eras.json, B5): a = phi - 1, b = beta, r = the intercept at a 2% target (rstar_at_2pct), pt 2%.
Usage: python3 sources/s75_hx.py          write sources/s75_hx.json and print a summary
       python3 sources/s75_hx.py check    rebuild in memory and fail if the committed file differs
"""
import json, os, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s75_eras as E  # noqa: E402
OUT = os.path.join(HERE, 's75_hx.json')
RAW74 = os.path.join(HERE, 's74_history', 'raw')
ERAS = [('e1', 'E1', 1946, 1972), ('e2', 'E2', 1972, 1983), ('e3', 'E3', 1983, 2007), ('e4', 'E4', 2007, 2025)]
PSZ_LAST = 2019


def yavg(rows, full=12):
    acc = defaultdict(list)
    for y, m, v in rows:
        acc[y].append(v)
    return {y: sum(v) / len(v) for y, v in acc.items() if len(v) >= full or y == 2025}


def f7():
    import pandas as pd
    p = os.path.join(E.RAW, 'f07ar.xlsx'); E.sha(p)
    d = pd.read_excel(p, header=None); out = {}
    for i in range(9, len(d)):
        c0 = str(d.iloc[i, 0]).strip()
        if not c0[:4].isdigit():
            break  # end of the All Families block
        y = int(c0[:4])
        if y not in out:
            out[y] = float(d.iloc[i, 3])
    return out


def build():
    import pandas as pd
    S = E.load()
    ff_m = E.fred('FEDFUNDS', RAW74); tb3 = yavg(E.fred('TB3MS', RAW74)); ff = yavg(ff_m)
    wx = S['wx']; sh_m = defaultdict(list)
    for y, m, v in ff_m:
        w = wx.get((y, m)); sh_m[y].append(w[0] if (w is not None and w[1] < 0.25) else v)
    sh = {y: sum(v) / len(v) for y, v in sh_m.items() if len(v) == 12 or y == 2025}
    m30 = yavg(E.fred('MORTGAGE30US', RAW74), 50)
    jp = os.path.join(E.RAW, 'JSTdatasetR6.xlsx'); j = pd.read_excel(jp); u = j[j.iso == 'USA'].set_index('year')
    lt = {int(y): float(v) for y, v in u.ltrate.dropna().items()}
    spread = sum(m30[y] - lt[y] for y in range(1972, 1982)) / 10.0
    nrou = yavg(E.fred('NROU', RAW74), 4); gq = yavg(E.fred('GDPC1', RAW74), 4); gp = yavg(E.fred('GDPPOT', RAW74), 4)
    usrec = defaultdict(int)
    for y, m, v in S['usrec']:
        usrec[y] += int(v)
    h74 = json.load(open(os.path.join(HERE, 's74_history.json'))); fa74 = dict(zip(h74['years'], h74['series']['fedAssetsGDP']))
    mfi = f7()
    tx, inc = S['psz_tax'], S['psz_inc']
    r62 = inc['Bottom 50%'][1962] / inc['Bottom 90%'][1962]

    def grp_rates(y):
        s10, s1 = inc['Top 10%'][y], inc['Top 1%'][y]
        n9 = (tx['Top 10%'][y] * s10 - tx['Top 1%'][y] * s1) / (s10 - s1)
        if y >= 1962:
            m40 = tx['Middle 40%'][y]
        else:
            m40 = (tx['Bottom 90%'][y] - tx['Bottom 50%'][y] * r62) / (1 - r62)
        return [tx['Bottom 50%'][y], m40, n9, tx['Top 1%'][y]]
    last = grp_rates(PSZ_LAST)
    B5 = json.load(open(os.path.join(HERE, 's75_eras.json')))['B5 estimated rule']
    rule = None
    out = {'_meta': {'built_by': 'sources/s75_hx.py', 'rules': __doc__.split('Rules')[1].split('Usage')[0].strip(), 'mortgage_spread_1972_1981': round(spread, 4),
                     'psz_last_year': PSZ_LAST, 'psz_group_rates_last': [round(x, 4) for x in last], 'bottom50_share_of_bottom90_1962': round(r62, 4),
                     'substitutes': {}, 'downloaded': {'s75_eras/raw/f07ar.xlsx': '2026-11-16'}}}
    for key, code, y0, y1 in ERAS:
        yrs = list(range(y0, y1 + 1)); sub = []
        c = {k: [] for k in ('cpi', 'hR', 'eR', 'ff', 'sh', 'm30', 'ug', 'yg', 'rm', 'un', 'fa', 'mhi', 'food', 'shel', 'med')}
        for y in yrs:
            c['cpi'].append(S['cpi'][y]); c['hR'].append(S['home'][y]); c['eR'].append(S['eq'][y])
            if y >= 1955:
                c['ff'].append(ff[y]); c['sh'].append(sh[y])
            else:
                c['ff'].append(tb3[y]); c['sh'].append(tb3[y]); sub.append('%d ff, sh: 3-month bill' % y)
            if y >= 1972:
                c['m30'].append(m30[y])
            else:
                c['m30'].append(lt[y] + spread); sub.append('%d m30: JST long-term rate + spread' % y)
            if y >= 1948:
                un = S['unemp'][y]
            else:
                un = S['jst_unemp'][y]; sub.append('%d unemployment: JST' % y)
            nr = nrou[y] if y >= 1949 else nrou[1949]
            if y < 1949:
                sub.append('%d NROU: 1949 held back' % y)
            c['un'].append(un); c['ug'].append(un - nr)
            if y >= 1949:
                c['yg'].append(100.0 * (gq[y] / gp[y] - 1.0))
            else:
                c['yg'].append(-2.0 * (un - nr)); sub.append('%d output gap: -2 x unemployment gap' % y)
            c['rm'].append(usrec[y])
            c['fa'].append(fa74[y] if key == 'e4' else 0)
            if y in mfi:
                c['mhi'].append(mfi[y])
            else:
                c['mhi'].append(mfi[y + 1]); sub.append('%d family income: %d held back' % (y, y + 1))
            for k, src in (('food', 'food'), ('shel', 'shelter'), ('med', 'medical')):
                if y in S[src]:
                    c[k].append(S[src][y])
                else:
                    c[k].append(S['cpi'][y]); sub.append('%d %s: CPI-U all items (reporting only)' % (y, k))
        ey = [y for y in range(y0 + 1, y1 + 1) if y <= PSZ_LAST]
        mean_g = [sum(grp_rates(y)[g] for y in ey) / len(ey) for g in range(4)]
        hm_y = [100.0 * ((1 + S['medical'][y] / 100.0) / (1 + S['cpi'][y] / 100.0) - 1) for y in range(y0 + 1, y1 + 1) if y in S['medical']]
        b5 = B5[code]
        out[key] = {'era': E.ERA_NAME[code], 'y0': y0, 'n': len(yrs), 'series': {k: [round(float(v), 4) for v in vs] for k, vs in c.items()},
                    'T': {'years': '%d-%d' % (ey[0], ey[-1]), 'groups': ['bottom 50%', 'middle 40%', 'next 9%', 'top 1%'],
                          'era_rates': [round(x, 4) for x in mean_g], 'd': [round(mean_g[g] - last[g], 4) for g in range(4)]},
                    'H': {'years': '%d' % len(hm_y), 'hm': round(sum(hm_y) / len(hm_y), 4)},
                    'R': {'quarters': b5['quarters'], 'a': b5['a'], 'b': b5['b'], 'r': round(b5['rstar_at_2pct'] / 100.0, 6), 'pt': 0.02}}
        out['_meta']['substitutes'][key] = sub
    out['_meta']['sha256'] = dict(sorted(E.SHA.items()))
    return out


def line(o):
    """The engine's copy: var HXE = {e1:{...}, ...} (index.html; dev/tools/s75_hx_copy.py writes and checks it)."""
    parts = []
    for key, code, y0, y1 in ERAS:
        e = o[key]; s = e['series']
        f = lambda v: repr(float(v)) if not float(v).is_integer() else str(int(v))
        seg = ['era:%s' % json.dumps(key), 'y0:%d' % e['y0'], 'n:%d' % e['n']] + ['%s:[%s]' % (k, ','.join(f(v) for v in s[k])) for k in s]
        seg += ['T:[%s]' % ','.join(f(v / 100.0) for v in e['T']['d']), 'hm:%s' % f(e['H']['hm'] / 100.0),
                'R:{a:%s, b:%s, r:%s, pt:0.02}' % (f(e['R']['a']), f(e['R']['b']), f(e['R']['r']))]
        parts.append('%s:{%s}' % (key, ', '.join(seg)))
    return 'var HXE = {' + ', '.join(parts) + '};  /* S75: generated by dev/tools/s75_hx_copy.py from sources/s75_hx.json (do not edit by hand) */'


if __name__ == '__main__':
    o = build(); txt = json.dumps(o, indent=1, sort_keys=False)
    if len(sys.argv) > 1 and sys.argv[1] == 'check':
        if open(OUT).read() != txt + '\n':
            print('sources/s75_hx.json differs from a rebuild'); sys.exit(1)
        print('s75_hx.json rebuilds identically'); sys.exit(0)
    open(OUT, 'w').write(txt + '\n')
    for key, code, y0, y1 in ERAS:
        e = o[key]
        print(key, e['era'], 'n', e['n'], 'T d (pts)', e['T']['d'], 'era rates', e['T']['era_rates'], 'H hm %', e['H']['hm'], 'R', e['R'])
    print('last PSZ group rates', o['_meta']['psz_group_rates_last'], 'mortgage spread', o['_meta']['mortgage_spread_1972_1981'])
