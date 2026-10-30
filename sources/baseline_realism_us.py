"""S34 (Oct 30, 2026; preregistration research-update prereg/s34-baseline-realism.md): the outside figures the no-programme run is compared with.

Sources (all public; dollars are 2025 dollars unless stated):
- Census Bureau, Current Population Survey, 2026 Annual Social and Economic Supplement (CPS ASEC), public-use CSV (asecpub26csv.zip:
  https://www2.census.gov/programs-surveys/cps/datasets/2026/march/), income year 2025. Person file pppub26.csv, weight MARSUPWT (the ASEC weight;
  two implied decimals, which cancel in shares). PEARNVAL: earnings; PERLIS 1: below the official poverty level (POV_UNIV 1: in the poverty universe);
  SPM_RESOURCES < SPM_POVTHRESHOLD: below the Supplemental Poverty Measure (SPM_WEIGHT); SPM_SNAPSUB, SPM_EITC, SPM_ACTC: the unit's SNAP, EITC, refundable CTC; WORKYN 1: worked at some time in 2025; PEMLR 1-2 employed,
  3-4 unemployed, 5-7 not in the labour force (March 2026). Household file hhpub26.csv: HTOTVAL (household money income), weight HSUP_WGT, for
  households whose reference person (PERRP 40 or 41) is aged 25 to 64.
- Federal Reserve, 2025 and 2022 Survey of Consumer Finances, summary extract public data (scfp2025s.zip, scfp2022s.zip:
  https://www.federalreserve.gov/econres/files/), five implicates pooled with WGT. Families whose head is aged 25 to 64 (the model's adults), with wage
  income (WAGEINC > 0) and, beside them, all families of that age. Types as sources/scf_households.py: MARRIED 1 (married or living with a partner) or 2,
  KIDS > 0 or 0. 2022 dollars moved to 2025 with CPI-U annual averages 292.655 and 321.943 (BLS); 2025 figures as published (2025 dollars).
- Bureau of Labor Statistics, CPS (via FRED, fredgraph.csv): LNS12300060 employment-population ratio 25-54, LNS11300060 labour force participation
  rate 25-54, LNS14000060 unemployment rate 25-54; the mean of the 2025 monthly values published (October 2025 was not collected).

Weighted percentiles use the midpoint of each record's weight (as sources/scf_households.py). The Gini is the weighted Gini of non-negative values.

Usage: python3 sources/baseline_realism_us.py DATA_DIR [--json=FILE]   (DATA_DIR holds pppub26.csv, hhpub26.csv, rscfp2025.dta, rscfp2022.dta, unzipped
       from the files above; the FRED series are downloaded; needs pandas and numpy)
"""
import csv, io, json, sys, urllib.request
import numpy as np, pandas as pd
D = sys.argv[1]
JS = [a[7:] for a in sys.argv[2:] if a.startswith('--json=')]
CPI22, CPI25 = 292.655, 321.943

def wq(x, w, q):
    o = np.argsort(x); xs = np.asarray(x, float)[o]; ws = np.asarray(w, float)[o]; c = (np.cumsum(ws) - ws/2)/ws.sum(); return np.interp(q, c, xs)
def wgini(x, w):
    x = np.maximum(0, np.asarray(x, float)); w = np.asarray(w, float); o = np.argsort(x); x, w = x[o], w[o]
    cw = np.cumsum(w); cxw = np.cumsum(x*w); W, T = cw[-1], cxw[-1]
    return 1 - np.sum(w*(2*cxw - x*w))/(W*T)  # 1 - 2 x area under the Lorenz curve (trapezoids)
def share(mask, w):
    w = np.asarray(w, float); return float((w*mask).sum()/w.sum()*100)

out = {'_meta': {'script': 'sources/baseline_realism_us.py', 'sources': __doc__.split('Weighted percentiles')[0].strip()}}

# CPS ASEC 2026 (income year 2025)
P = pd.read_csv(D + '/pppub26.csv', usecols=['PH_SEQ', 'PERRP', 'A_AGE', 'MARSUPWT', 'PEARNVAL', 'PERLIS', 'POV_UNIV', 'SPM_RESOURCES', 'SPM_POVTHRESHOLD',
                                              'SPM_WEIGHT', 'WORKYN', 'PEMLR', 'WKSWORK', 'HRSWK', 'SPM_SNAPSUB', 'SPM_EITC', 'SPM_ACTC'])
P = P[P.MARSUPWT > 0]
pov = P[P.POV_UNIV == 1]
a = P[(P.A_AGE >= 25) & (P.A_AGE <= 64)]; ap = pov[(pov.A_AGE >= 25) & (pov.A_AGE <= 64)]; kp = pov[pov.A_AGE < 18]
e = a[a.PEARNVAL > 0]
c = {'persons': len(P),
     'official': {'all': share(pov.PERLIS == 1, pov.MARSUPWT), 'age25to64': share(ap.PERLIS == 1, ap.MARSUPWT), 'under18': share(kp.PERLIS == 1, kp.MARSUPWT),
                  'age18to64': share(pov[(pov.A_AGE >= 18) & (pov.A_AGE <= 64)].PERLIS == 1, pov[(pov.A_AGE >= 18) & (pov.A_AGE <= 64)].MARSUPWT),
                  'age25to64Earners': share(ap[ap.PEARNVAL > 0].PERLIS == 1, ap[ap.PEARNVAL > 0].MARSUPWT)},
     'spm': {'all': share(P.SPM_RESOURCES < P.SPM_POVTHRESHOLD, P.SPM_WEIGHT), 'age25to64': share(a.SPM_RESOURCES < a.SPM_POVTHRESHOLD, a.SPM_WEIGHT),
             'under18': share(P[P.A_AGE < 18].SPM_RESOURCES < P[P.A_AGE < 18].SPM_POVTHRESHOLD, P[P.A_AGE < 18].SPM_WEIGHT)},
     'earnings25to64': {'shareWithEarnings': share(a.PEARNVAL > 0, a.MARSUPWT), 'workedLastYear': share(a.WORKYN == 1, a.MARSUPWT),
                        'p10': float(wq(e.PEARNVAL, e.MARSUPWT, 0.1)), 'p25': float(wq(e.PEARNVAL, e.MARSUPWT, 0.25)), 'median': float(wq(e.PEARNVAL, e.MARSUPWT, 0.5)),
                        'p75': float(wq(e.PEARNVAL, e.MARSUPWT, 0.75)), 'p90': float(wq(e.PEARNVAL, e.MARSUPWT, 0.9)),
                        'mean': float((e.PEARNVAL*e.MARSUPWT).sum()/e.MARSUPWT.sum()), 'gini': float(wgini(e.PEARNVAL, e.MARSUPWT))},
     'march2026_25to64': {'employed': share(a.PEMLR.isin([1, 2]), a.MARSUPWT), 'unemployedOfLabourForce': share(a[a.PEMLR.isin([1, 2, 3, 4])].PEMLR.isin([3, 4]), a[a.PEMLR.isin([1, 2, 3, 4])].MARSUPWT),
                          'inLabourForce': share(a.PEMLR.isin([1, 2, 3, 4]), a.MARSUPWT)}}
ft = e[(e.WKSWORK >= 50) & (e.HRSWK >= 35)]  # full-time, year-round (the Census definition: 50 or more weeks, usually 35 or more hours a week)
lq = lambda x, w, p: float(np.log(wq(x, w, p)))
c['earnings25to64FTYR'] = {'shareOfEarners': share((e.WKSWORK >= 50) & (e.HRSWK >= 35), e.MARSUPWT), 'p10': float(wq(ft.PEARNVAL, ft.MARSUPWT, 0.1)),
                           'p25': float(wq(ft.PEARNVAL, ft.MARSUPWT, 0.25)), 'median': float(wq(ft.PEARNVAL, ft.MARSUPWT, 0.5)), 'p75': float(wq(ft.PEARNVAL, ft.MARSUPWT, 0.75)),
                           'p90': float(wq(ft.PEARNVAL, ft.MARSUPWT, 0.9)), 'gini': float(wgini(ft.PEARNVAL, ft.MARSUPWT)),
                           # the spread of log earnings read from the quartiles (robust to top-coding and to very small earnings): (ln p75 - ln p25) / (2 x 0.6745)
                           'sigmaLogIQR': (lq(ft.PEARNVAL, ft.MARSUPWT, 0.75) - lq(ft.PEARNVAL, ft.MARSUPWT, 0.25))/(2*0.6744898),
                           'sigmaLog1090': (lq(ft.PEARNVAL, ft.MARSUPWT, 0.9) - lq(ft.PEARNVAL, ft.MARSUPWT, 0.1))/(2*1.2815516)}
c['earnings25to64']['sigmaLogIQR'] = (lq(e.PEARNVAL, e.MARSUPWT, 0.75) - lq(e.PEARNVAL, e.MARSUPWT, 0.25))/(2*0.6744898)
# the safety net, as the survey reports it (SNAP receipt is under-reported in the CPS; the EITC and the refundable CTC are the Census tax model's):
# % of adults 25-64 in a Supplemental Poverty Measure unit receiving each
c['safetyNet25to64'] = {'snap': share(a.SPM_SNAPSUB > 0, a.MARSUPWT), 'eitc': share(a.SPM_EITC > 0, a.MARSUPWT), 'actc': share(a.SPM_ACTC > 0, a.MARSUPWT)}
mu = pov[((pov.A_AGE >= 25) & (pov.A_AGE <= 64)) | (pov.A_AGE < 18)]  # the model's people: adults 25-64 and children
c['official']['age25to64AndUnder18'] = share(mu.PERLIS == 1, mu.MARSUPWT)
Hh = pd.read_csv(D + '/hhpub26.csv', usecols=['H_SEQ', 'HTOTVAL', 'HSUP_WGT'])
ref = P[P.PERRP.isin([40, 41])][['PH_SEQ', 'A_AGE']].drop_duplicates('PH_SEQ')
Hh = Hh.merge(ref, left_on='H_SEQ', right_on='PH_SEQ'); Hh = Hh[(Hh.A_AGE >= 25) & (Hh.A_AGE <= 64) & (Hh.HSUP_WGT > 0)]
c['householdIncome25to64'] = {'households': len(Hh), 'median': float(wq(Hh.HTOTVAL, Hh.HSUP_WGT, 0.5)), 'gini': float(wgini(Hh.HTOTVAL, Hh.HSUP_WGT))}
Hall = pd.read_csv(D + '/hhpub26.csv', usecols=['HTOTVAL', 'HSUP_WGT']); Hall = Hall[Hall.HSUP_WGT > 0]
c['householdIncomeAll'] = {'median': float(wq(Hall.HTOTVAL, Hall.HSUP_WGT, 0.5)), 'gini': float(wgini(Hall.HTOTVAL, Hall.HSUP_WGT))}
out['cps'] = c

# SCF 2025 and 2022
def scf(f, k):
    df = pd.read_stata(D + '/' + f, columns=['wgt', 'age', 'married', 'kids', 'wageinc', 'networth'])
    df = df[(df.age >= 25) & (df.age <= 64)]
    o = {}
    for base, sel0 in (('withWages', df.wageinc > 0), ('all', df.age > 0)):
        b = df[sel0]; r = {}
        for name, sel in (('all', b.married > 0), ('ck', (b.married == 1) & (b.kids > 0)), ('cn', (b.married == 1) & (b.kids == 0)),
                          ('sp', (b.married == 2) & (b.kids > 0)), ('sg', (b.married == 2) & (b.kids == 0))):
            g = b[sel]; nw = g.networth.values*k; w = g.wgt.values
            r[name] = {'records': int(len(g)), 'familyShare': float(w.sum()/b.wgt.sum()*100), 'median': float(wq(nw, w, 0.5)), 'p25': float(wq(nw, w, 0.25)),
                       'p75': float(wq(nw, w, 0.75)), 'neg': share(nw < 0, w), 'below25k': share(nw < 25000, w)}
        o[base] = r
    return o
out['scf2025'] = scf('rscfp2025.dta', 1.0)
out['scf2022'] = scf('rscfp2022.dta', CPI25/CPI22)

# BLS via FRED, 2025
def fred(s):
    u = 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=%s&cosd=2025-01-01&coed=2025-12-31' % s
    r = csv.reader(io.StringIO(urllib.request.urlopen(u, timeout=60).read().decode())); next(r)
    v = [float(x[1]) for x in r if len(x) > 1 and x[1] not in ('', '.')]
    return {'mean2025': sum(v)/len(v), 'months': len(v)}
out['bls'] = {'epop25to54': fred('LNS12300060'), 'lfpr25to54': fred('LNS11300060'), 'urate25to54': fred('LNS14000060')}

js = json.dumps(out, indent=1)
print(js)
if JS: open(JS[0], 'w').write(js)
