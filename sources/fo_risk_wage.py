"""v5.2 round, step 5 (Oct 5, 2026): how automation risk is linked to wages in the "automation risk linked to wages" reading (harness.js CFG.FO_RISK_WAGE_RHO).

Source: Frey and Osborne (2013; Technological Forecasting and Social Change 114, 2017), probability of computerisation for 702 occupations, with May 2016
BLS Occupational Employment Statistics employment and median annual wages, as carried by the plotly/datasets file job-automation-probability.csv
(every row checked against the paper's appendix in v4.20; CONTRIBUTING.md, "AUTO_HIGH_SHARE"). Retrieved Oct 5, 2026 from
https://raw.githubusercontent.com/plotly/datasets/master/job-automation-probability.csv

Result (700 occupations with a wage and employment, 130.3 million jobs, weighted by employment): the correlation of log median wage with the probability
is -0.650 (the figure quoted since v4.20); the normal-score correlation (each variable replaced by the normal quantile of its weighted mid-rank) is -0.531.
The model links the two with a Gaussian copula, whose parameter is the normal-score correlation, so it uses -0.531: the -0.650 figure mixes the link with the
shapes of the two distributions (occupations' median wages are not lognormal and the probabilities pile up near 0 and 1). Both are correlations across
occupations' median wages; within an occupation wages vary and the risk does not, so the link between one person's wage and their risk is weaker than
either figure (a stated limit: the reading is an upper bound on the link).

Usage: python3 sources/fo_risk_wage.py   (downloads the file, about 120 kB; needs pandas and numpy)
"""
import io, urllib.request
from statistics import NormalDist
import numpy as np, pandas as pd
URL = 'https://raw.githubusercontent.com/plotly/datasets/master/job-automation-probability.csv'
d = pd.read_csv(io.BytesIO(urllib.request.urlopen(URL, timeout=60).read()))
for c in ('median_ann_wage', 'employed_may2016', 'prob'):
    d[c] = pd.to_numeric(d[c].astype(str).str.replace(',', ''), errors='coerce')
d = d.dropna(subset=['median_ann_wage', 'employed_may2016', 'prob']); d = d[(d.median_ann_wage > 0) & (d.employed_may2016 > 0)]
w = d.employed_may2016.values.astype(float); p = d.prob.values; lw = np.log(d.median_ann_wage.values); nd = NormalDist()
def wcorr(a, b):
    ma = (w*a).sum()/w.sum(); mb = (w*b).sum()/w.sum(); return (w*(a - ma)*(b - mb)).sum()/np.sqrt((w*(a - ma)**2).sum()*(w*(b - mb)**2).sum())
def nscore(x):
    out = np.empty(len(x)); W = w.sum()
    for v in np.unique(x):
        m = x == v; out[m] = nd.inv_cdf((w[x < v].sum() + w[m].sum()/2)/W)
    return out
print('%d occupations, %.1f million jobs' % (len(d), w.sum()/1e6))
print('correlation of log median wage with the probability: %.4f' % wcorr(lw, p))
print('normal-score correlation (the Gaussian copula parameter, CFG.FO_RISK_WAGE_RHO): %.4f' % wcorr(nscore(lw), nscore(p)))
