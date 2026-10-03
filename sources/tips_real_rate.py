"""v5.2 round, step 3 (Oct 3, 2026): the real rate for "savings that keep up with prices" (harness.js SAVE_DEFAULTS.r).

Source: Board of Governors of the Federal Reserve System, Market Yield on U.S. Treasury Securities at 10-Year Constant Maturity, Quoted on an
Investment Basis, Inflation-Indexed (FRED series DFII10, daily, percent). Retrieved Oct 3, 2026 from
https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFII5,DFII10 (the same file carries DFII5, the 5-year yield, for comparison).

Result (2003-2025, every full year of the series): DFII10 mean 0.972% over 5,753 daily observations (mean of the 23 annual means 0.973%);
2025 alone 1.963%; DFII5 mean 0.551%, 2025 1.507%. The model uses 0.0097 (the long-run 10-year mean: a 20- to 40-year run is better matched by a
long-run average than by one year, and a 10-year bond is closer to a saver's horizon than a 5-year one); 0 and the 2025 average are readings.

Usage: python3 sources/tips_real_rate.py   (downloads the file and prints the figures above; needs network access)
"""
import csv, io, urllib.request
URL = 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFII5,DFII10'
rows = list(csv.DictReader(io.StringIO(urllib.request.urlopen(URL, timeout=60).read().decode())))
for k in ('DFII10', 'DFII5'):
    v = [(r['observation_date'][:4], float(r[k])) for r in rows if r[k] not in ('', '.') and '2003' <= r['observation_date'][:4] <= '2025']
    years = sorted(set(y for y, _ in v)); ann = [sum(x for y2, x in v if y2 == y) / sum(1 for y2, _ in v if y2 == y) for y in years]
    print('%s 2003-2025: daily mean %.3f%% (%d observations); mean of annual means %.3f%%; 2025 %.3f%%' % (k, sum(x for _, x in v) / len(v), len(v), sum(ann) / len(ann), ann[-1]))
