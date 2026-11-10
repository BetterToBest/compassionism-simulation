"""S59 (Nov 10, 2026; research-update prereg/2026-11-s59-asset-classes.md): long-run real price gains of US homes and shares, for switch RETURNS.

Source: Robert J. Shiller's online data (Irrational Exuberance, Princeton University Press, as updated by the author), downloaded Nov 10, 2026 from
http://www.econ.yale.edu/~shiller/data/ie_data.xls (S&P Composite, monthly from 1871; column "Real Price", the index over the CPI) and
http://www.econ.yale.edu/~shiller/data/Fig3-1.xls (the real home price index: annual 1890-1952, monthly from 1953). Copies in sources/s59_shiller/.

What is measured: the yearly rate of real price gain (geometric), price only: no dividends and no rents. Dividends and rents are income, which the engine's
households do not receive in this round (a limit, stated in the report); a home's rent is the housing the owner consumes. Windows: the main one is 1953-2022
(the home series is monthly from 1953; 2022 is the last full year in both files and the SCF's year); beside it 1890-2022 and 1983-2022. Year averages for
shares; for homes the year's average where monthly, the annual value before 1953.
Private business has no price series here: the engine gives it the shares' rate, labelled a modelling assumption (swept with the others).

Prints the rates and writes sources/s59_real_gains.json. Usage: python3 sources/s59_real_gains.py   (needs pandas and xlrd)
"""
import hashlib, json, os
import pandas as pd
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's59_shiller')
def sha(f): return hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
s = pd.read_excel(os.path.join(D, 'ie_data.xls'), sheet_name='Data', header=None, skiprows=8).iloc[:, [0, 7]].dropna(); s.columns = ['d', 'rp']
s = s[pd.to_numeric(s.d, errors='coerce').notna()].astype(float); s['y'] = s.d.astype(int); eq = s.groupby('y').rp.mean(); n = s.groupby('y').rp.count(); eq = eq[n == 12]
h = pd.read_excel(os.path.join(D, 'Fig3-1.xls'), sheet_name='Data', header=None, skiprows=7).iloc[:, [0, 1]].dropna(); h.columns = ['d', 'rp']; h = h.astype(float)
h['y'] = h.d.astype(int); hp = h.groupby('y').rp.mean(); hn = h.groupby('y').rp.count(); hp = hp[(hn == 12) | (hp.index < 1953)]
def rate(x, a, b): return (x[b]/x[a])**(1.0/(b - a)) - 1
out = {'source': 'Shiller online data (ie_data.xls, Fig3-1.xls), downloaded Nov 10, 2026; sources/s59_real_gains.py', 'sha256': {f: sha(f) for f in ('ie_data.xls', 'Fig3-1.xls')}, 'windows': {}}
for a, b in ((1953, 2022), (1890, 2022), (1983, 2022)):
    out['windows']['%d-%d' % (a, b)] = {'home': round(rate(hp, a, b), 4), 'eq': round(rate(eq, a, b), 4)}
    print('%d-%d: real price gain a year, homes %.4f, shares %.4f' % (a, b, rate(hp, a, b), rate(eq, a, b)))
out['main'] = out['windows']['1953-2022']
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 's59_real_gains.json'), 'w'), indent=1)
for f in out['sha256']: print(f, out['sha256'][f])
