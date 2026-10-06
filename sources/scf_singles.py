"""v5.2 round, step 5 (Oct 3, 2026): the Survey of Consumer Finances figures behind the US-data check and the "fix" readings (harness.js LATENT).

Source: Board of Governors of the Federal Reserve System, 2022 Survey of Consumer Finances, summary extract public data (rscfp2022.dta, in
https://www.federalreserve.gov/econres/files/scfp2022s.zip), all five implicates pooled with the weight WGT. The group closest to the model's adults:
families whose head is single (MARRIED = 2: neither married nor living with a partner), with no children (KIDS = 0), aged 25 to 66, with wage income
(WAGEINC > 0). Dollars are taken from 2022 to 2025 with CPI-U annual averages 292.655 and 321.943 (BLS).

Prints: net worth percentiles, the share in debt and below the model's wealth line, the wealth Gini both ways, the spread of log wage income and the
lognormal spread that gives the same wage-income Gini (CFG.SCF_WAGE_SIGMA), the normal-score (Gaussian-copula) correlation of wage income with net worth, and the 100 net-worth quantiles at 0.5%, 1.5%, ..., 99.5% in 2025 dollars that
harness.js holds as CFG.SCF_NETWORTH_PCTL.

Usage: python3 sources/scf_singles.py   (downloads the extract, about 3 MB; needs pandas and numpy)
"""
import io, urllib.request, zipfile, tempfile, os
from statistics import NormalDist
import numpy as np, pandas as pd
URL = 'https://www.federalreserve.gov/econres/files/scfp2022s.zip'
CPI22, CPI25 = 292.655, 321.943
with tempfile.TemporaryDirectory() as d:
    zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0 (research script)'}), timeout=120).read())).extractall(d)
    df = pd.read_stata(os.path.join(d, 'rscfp2022.dta'), columns=['wgt', 'age', 'married', 'kids', 'wageinc', 'networth'])
g = df[(df.married == 2) & (df.kids == 0) & (df.age >= 25) & (df.age <= 66) & (df.wageinc > 0)]
w = g.wgt.values.astype(float); nw = g.networth.values*CPI25/CPI22; wi = g.wageinc.values*CPI25/CPI22
def wq(x, q):
    o = np.argsort(x); xs = x[o]; ws = w[o]; c = (np.cumsum(ws) - ws/2)/ws.sum(); return np.interp(q, c, xs)
def gini(x):
    o = np.argsort(x); xs = x[o]; ws = w[o]; cw = np.cumsum(ws); W = cw[-1]; mu = (ws*xs).sum()/W; F = (cw - ws/2)/W; return 2*np.sum(ws*(xs - mu)*(F - 0.5))/W/mu
def nscore(x):
    o = np.argsort(x); r = np.empty(len(x)); cw = np.cumsum(w[o]); r[o] = (cw - w[o]/2)/cw[-1]; nd = NormalDist(); return np.array([nd.inv_cdf(min(max(p, 1e-9), 1 - 1e-9)) for p in r])
def wcorr(a, b):
    ma = (w*a).sum()/w.sum(); mb = (w*b).sum()/w.sum(); return (w*(a - ma)*(b - mb)).sum()/np.sqrt((w*(a - ma)**2).sum()*(w*(b - mb)**2).sum())
lw = np.log(wi); m = (w*lw).sum()/w.sum()
print('families: %d records (%.1f million families)' % (len(g), w.sum()/1e6))
print('net worth, 2025 $: p10 %.0f  p25 %.0f  median %.0f  p75 %.0f  p90 %.0f' % tuple(wq(nw, q) for q in (0.1, 0.25, 0.5, 0.75, 0.9)))
print('share with negative net worth %.4f; share below $25,000 (2025 $) %.4f' % ((w*(nw < 0)).sum()/w.sum(), (w*(nw < 25000)).sum()/w.sum()))
print('wealth Gini: debts kept %.4f; debts counted as zero %.4f' % (gini(nw), gini(np.maximum(0, nw))))
print('wage income, 2025 $: median %.0f; sd of log %.4f; Gini %.4f' % (wq(wi, 0.5), np.sqrt((w*(lw - m)**2).sum()/w.sum()), gini(wi)))
print('normal-score correlation of wage income and net worth: %.4f' % wcorr(nscore(wi), nscore(nw)))
gw = gini(wi); print('lognormal spread with the same wage-income Gini (2 Phi(s / sqrt 2) - 1 = %.4f): s = %.4f' % (gw, NormalDist().inv_cdf((gw + 1)/2)*2**0.5))
print('CFG.SCF_NETWORTH_PCTL = [' + ','.join('%d' % round(v) for v in wq(nw, np.arange(0.005, 1.0, 0.01))) + '];')
