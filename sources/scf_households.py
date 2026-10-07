"""v5.3 B7 (Oct 7, 2026; plan item B7, "wealth initialisation to the SCF household distribution"): household net worth at the start, by household type.

Source: Board of Governors of the Federal Reserve System, 2022 Survey of Consumer Finances, summary extract public data (rscfp2022.dta, in
https://www.federalreserve.gov/econres/files/scfp2022s.zip; the same file as sources/scf_singles.py), all five implicates pooled with the weight WGT.
Families whose head is aged 25 to 66 with wage income (WAGEINC > 0), in the model's four household types: MARRIED = 1 (married or living with a partner)
or 2 (neither), KIDS > 0 or KIDS = 0. Dollars are taken from 2022 to 2025 with CPI-U annual averages 292.655 and 321.943 (BLS). The single adults without
children are exactly the group of sources/scf_singles.py, so their 100 quantiles equal CFG.SCF_NETWORTH_PCTL.

Prints, for each type and for all four together: the share of families, net worth percentiles, the share in debt, the normal-score (Gaussian-copula) correlation of the family's
wage income with its net worth, and the 100 net-worth quantiles at 0.5%, 1.5%, ..., 99.5% in 2025 dollars that index.html holds as CFG.HH_SCF_PCTL.

Usage: python3 sources/scf_households.py [rscfp2022.dta]   (without a path it downloads the extract, about 3 MB; needs pandas and numpy)
"""
import io, os, sys, tempfile, urllib.request, zipfile
from statistics import NormalDist
import numpy as np, pandas as pd
URL = 'https://www.federalreserve.gov/econres/files/scfp2022s.zip'
CPI22, CPI25 = 292.655, 321.943
COLS = ['wgt', 'age', 'married', 'kids', 'wageinc', 'networth']
if len(sys.argv) > 1:
    df = pd.read_stata(sys.argv[1], columns=COLS)
else:
    with tempfile.TemporaryDirectory() as d:
        zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0 (research script)'}), timeout=120).read())).extractall(d)
        df = pd.read_stata(os.path.join(d, 'rscfp2022.dta'), columns=COLS)
base = df[(df.age >= 25) & (df.age <= 66) & (df.wageinc > 0)]
TYPES = [('coupleKids', (base.married == 1) & (base.kids > 0)), ('coupleNoKids', (base.married == 1) & (base.kids == 0)),
         ('singleParent', (base.married == 2) & (base.kids > 0)), ('single', (base.married == 2) & (base.kids == 0))]
TYPES = TYPES + [('all', base.married > 0)]  # every family of the four types together (the yardstick's all-household line)
for name, sel in TYPES:
    g = base[sel]; w = g.wgt.values.astype(float); nw = g.networth.values*CPI25/CPI22; wi = g.wageinc.values*CPI25/CPI22
    def wq(x, q):
        o = np.argsort(x); xs = x[o]; ws = w[o]; c = (np.cumsum(ws) - ws/2)/ws.sum(); return np.interp(q, c, xs)
    def nscore(x):
        o = np.argsort(x); r = np.empty(len(x)); cw = np.cumsum(w[o]); r[o] = (cw - w[o]/2)/cw[-1]; nd = NormalDist()
        return np.array([nd.inv_cdf(min(max(p, 1e-9), 1 - 1e-9)) for p in r])
    def wcorr(a, b):
        ma, mb = (w*a).sum()/w.sum(), (w*b).sum()/w.sum(); return (w*(a - ma)*(b - mb)).sum()/np.sqrt((w*(a - ma)**2).sum()*(w*(b - mb)**2).sum())
    print('%s: %d records, %.1f%% of families; net worth p10 %.0f p25 %.0f median %.0f p75 %.0f p90 %.0f; in debt %.1f%%; normal-score correlation of wage income and net worth %.4f'
          % (name, len(g), w.sum()/base.wgt.sum()*100, *wq(nw, [0.1, 0.25, 0.5, 0.75, 0.9]), (w*(nw < 0)).sum()/w.sum()*100, wcorr(nscore(wi), nscore(nw))))
    print('  ' + name + ': [' + ','.join('%d' % round(v) for v in wq(nw, np.arange(0.005, 1.0, 0.01))) + '],')
