"""S61 (Nov 9, 2026; research-update prereg/2026-11-s61-baseline-scope.md): the borrowing limit for ordinary spending and the liquid share, for the debt
reading (index.html DEBT_READ: lim, liq).

Source: Federal Reserve, 2025 Survey of Consumer Finances, summary extract public data (scfp2025s.zip, https://www.federalreserve.gov/econres/files/,
downloaded Nov 9, 2026, sha256 32dcf86be48b20fb5fd9e659f79fa22a4d9cccf456e44b6ca9b1329e9869bbeb), file rscfp2025.dta; five implicates pooled with WGT;
2025 dollars. Families whose head is aged 25-64 (the model's adults).
- Unsecured consumer debt: CCBAL (credit-card balances after the last payment) + OTH_INST (instalment loans other than vehicle and education) + ODEBT
  (other debt). Percentiles among families who hold any, all and in the bottom 40% of income (INCOME).
- Liquid share: LIQ (transaction accounts) over NETWORTH, median among families with positive net worth.
- Checks: families in debt (NETWORTH < 0); TURNDOWN (turned down for credit in the past year), FEARDENIAL (did not apply, fearing denial).
Usage: python3 sources/s61_borrowing.py DATA_DIR   (DATA_DIR holds rscfp2025.dta; needs pandas and numpy)
"""
import json, sys
import numpy as np, pandas as pd
S = pd.read_stata(sys.argv[1] + '/rscfp2025.dta'); S.columns = [c.upper() for c in S.columns]
a = S[(S.AGE >= 25) & (S.AGE <= 64)].copy()
def wq(x, w, q):
    o = np.argsort(x.values, kind='stable'); xs = x.values[o].astype(float); ws = w.values[o].astype(float); c = (np.cumsum(ws) - ws/2)/ws.sum(); return np.interp(q, c, xs)
def sh(m, w): return round(float((w*m).sum()/w.sum()*100), 1)
a['uns'] = a.CCBAL + a.OTH_INST + a.ODEBT
h = a[a.uns > 0]; lo = a[a.INCOME <= wq(a.INCOME, a.WGT, 0.4)]; hl = lo[lo.uns > 0]; p = a[a.NETWORTH > 0]
out = {'holdAny': sh(a.uns > 0, a.WGT), 'holdAnyBottom40': sh(lo.uns > 0, lo.WGT),
       'unsecuredHolders': [round(float(v)) for v in wq(h.uns, h.WGT, [0.25, 0.5, 0.75])],
       'unsecuredHoldersBottom40': [round(float(v)) for v in wq(hl.uns, hl.WGT, [0.25, 0.5, 0.75])],
       'liquidShareMedian': round(float(wq(p.LIQ/p.NETWORTH, p.WGT, 0.5)), 3), 'inDebt': sh(a.NETWORTH < 0, a.WGT),
       'turnedDown': sh(a.TURNDOWN > 0, a.WGT), 'fearedDenial': sh(a.FEARDENIAL > 0, a.WGT)}
print(json.dumps(out, indent=1))
