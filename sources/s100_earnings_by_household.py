"""Earnings by household type, part-time and part-year work, and the EITC's reach, adults 25-64 (research-update prereg/2026-11-s100-part-time-dcc.md).

Source: Census Bureau, Current Population Survey, 2026 Annual Social and Economic Supplement (CPS ASEC), public-use CSV (asecpub26csv.zip:
https://www2.census.gov/programs-surveys/cps/datasets/2026/march/), income year 2025; person file pppub26.csv, weight MARSUPWT.
- Household type as the model's (sources/households.py): an adult is in a couple if a spouse (A_SPOUSE) or a cohabiting partner (PECOHAB) is present;
  with children if any person under 18 in the household names the adult or the partner as a parent (PEPAR1, PEPAR2). Types: single adult (sg),
  single parent (sp), couple without children (cn), couple with children (ck).
- Earnings PEARNVAL (adults with earnings > 0). Part-time: usually under 35 hours a week in the weeks worked (HRSWK); part-year: under 50 weeks
  (WKSWORK); full-time, year-round: both at or above (the Census definition). Under 20 hours: HRSWK < 20 (SNAP's work rule reads 20 hours a week).
- Spread of log earnings from the quartiles, (ln p75 - ln p25) / (2 x 0.6745), as the release's wage reading (sources/baseline_realism_us.py).
- Partners' earnings correlation: couples where both partners are 25-64 and both have earnings; the correlation of the normal scores of their
  earnings ranks (weighted by the first partner's MARSUPWT), the scale the model's Gaussian copula uses.
- EITC: EIT_CRED is the Census tax model's credit, carried on one member of each tax unit (TAX_ID within PH_SEQ); SPM_EITC is the Supplemental
  Poverty Measure unit's total. The tax model simulates the credit for every eligible tax unit (it does not model take-up). "Own tax unit": the
  adult's own tax unit receives it; the S34 figure (15.3%) counts the adult's SPM unit, which also holds other tax units (cohabiting partners
  filing apart, grown children, other relatives). The model's household is one tax unit (couples file jointly), so the own-tax-unit share is the
  figure comparable with the model's at full take-up. ACTC_CRD likewise for the refundable Child Tax Credit.
- Who pays for care: families (a single parent, or a couple, aged 25-64) with a child under 13 of their own (PEPAR1, PEPAR2); "every adult earns": the
  parent, or both partners, have earnings; "pays": SPM_CHILDCAREXPNS > 0 (childcare paid while working, the SPM unit's). Families counted once
  (the partner with the lower line number). Weighted count in millions (MARSUPWT / 100), for the IRS SOI comparison (Table 3.3, tax year 2023:
  5,720,294 returns with the credit for child and dependent care expenses, $3,468,910 thousand).

Weighted percentiles use the midpoint of each record's weight (as sources/scf_households.py).
Usage: python3 sources/s100_earnings_by_household.py DATA_DIR [--json=FILE]   (DATA_DIR holds pppub26.csv; needs pandas and numpy)
"""
import sys, json
import numpy as np, pandas as pd
from statistics import NormalDist

D = sys.argv[1]
OUT = next((a[7:] for a in sys.argv if a.startswith('--json=')), None)
ND = NormalDist()

def wq(x, w, p):
    x = np.asarray(x, float); w = np.asarray(w, float); o = np.argsort(x); x, w = x[o], w[o]
    c = (np.cumsum(w) - w/2)/w.sum(); return float(np.interp(p, c, x))
def share(m, w):
    w = np.asarray(w, float); return float((w*np.asarray(m, bool)).sum()/w.sum()*100)
def lsig(x, w):
    return (np.log(wq(x, w, 0.75)) - np.log(wq(x, w, 0.25)))/(2*0.6744898)
def nscore(x, w):
    x = np.asarray(x, float); w = np.asarray(w, float); o = np.argsort(x, kind='mergesort'); c = (np.cumsum(w[o]) - w[o]/2)/w.sum()
    z = np.empty(len(x)); z[o] = [ND.inv_cdf(min(1 - 1e-9, max(1e-9, v))) for v in c]; return z
def wcorr(a, b, w):
    w = np.asarray(w, float)/np.sum(w); ma, mb = np.sum(w*a), np.sum(w*b)
    return float(np.sum(w*(a - ma)*(b - mb))/np.sqrt(np.sum(w*(a - ma)**2)*np.sum(w*(b - mb)**2)))

cols = ['PH_SEQ', 'A_LINENO', 'A_AGE', 'MARSUPWT', 'PEARNVAL', 'TAX_ID', 'EIT_CRED', 'ACTC_CRD', 'SPM_EITC', 'SPM_ACTC', 'A_SPOUSE', 'PECOHAB',
        'PEPAR1', 'PEPAR2', 'HRSWK', 'WKSWORK', 'DEP_STAT', 'SPM_CHILDCAREXPNS']
P = pd.read_csv(D + '/pppub26.csv', usecols=cols); P = P[P.MARSUPWT > 0].copy()
tu = P.groupby(['PH_SEQ', 'TAX_ID']).agg(tuE=('EIT_CRED', 'max'), tuA=('ACTC_CRD', 'max')).reset_index()
P = P.merge(tu, on=['PH_SEQ', 'TAX_ID'], how='left')
P['partner'] = np.where(P.A_SPOUSE > 0, P.A_SPOUSE, np.where(P.PECOHAB > 0, P.PECOHAB, -1))
k = P[P.A_AGE < 18][['PH_SEQ', 'PEPAR1', 'PEPAR2']]
par = pd.concat([k[['PH_SEQ', 'PEPAR1']].rename(columns={'PEPAR1': 'L'}), k[['PH_SEQ', 'PEPAR2']].rename(columns={'PEPAR2': 'L'})]); par = par[par.L > 0]
nk = par.groupby(['PH_SEQ', 'L']).size().rename('nk').reset_index()
P = P.merge(nk, left_on=['PH_SEQ', 'A_LINENO'], right_on=['PH_SEQ', 'L'], how='left').drop(columns='L')
P = P.merge(nk.rename(columns={'nk': 'nkp'}), left_on=['PH_SEQ', 'partner'], right_on=['PH_SEQ', 'L'], how='left').drop(columns='L')
P['kids'] = np.maximum(P.nk.fillna(0), P.nkp.fillna(0))
a = P[(P.A_AGE >= 25) & (P.A_AGE <= 64)].copy()
a['type'] = np.where(a.partner > 0, np.where(a.kids > 0, 'ck', 'cn'), np.where(a.kids > 0, 'sp', 'sg'))
e = a[a.PEARNVAL > 0].copy()
e['pt'] = e.HRSWK < 35; e['py'] = (e.HRSWK >= 35) & (e.WKSWORK < 50); e['ftyr'] = (e.HRSWK >= 35) & (e.WKSWORK >= 50); e['u20'] = e.HRSWK < 20

out = {'_meta': {'script': 'sources/s100_earnings_by_household.py', 'sources': __doc__.split('Weighted percentiles')[0].strip(), 'adults25to64': int(len(a)), 'earners': int(len(e))}}
def earnBlock(x):
    w = x.MARSUPWT
    return {'n': int(len(x)), 'median': wq(x.PEARNVAL, w, 0.5), 'p10': wq(x.PEARNVAL, w, 0.1), 'p25': wq(x.PEARNVAL, w, 0.25), 'p75': wq(x.PEARNVAL, w, 0.75),
            'p90': wq(x.PEARNVAL, w, 0.9), 'sigmaLogIQR': float(lsig(x.PEARNVAL, w)), 'partTime': share(x.pt, w), 'partYearFullTime': share(x.py, w),
            'fullTimeYearRound': share(x.ftyr, w), 'under20Hours': share(x.u20, w)}
out['earners'] = {'all': earnBlock(e)}
for t in ['sg', 'sp', 'cn', 'ck']:
    x = a[a.type == t]
    out['earners'][t] = dict(earnBlock(e[e.type == t]), shareOfAdults=share(a.type == t, a.MARSUPWT), withEarnings=share(x.PEARNVAL > 0, x.MARSUPWT))
# part-time and part-year work by age band and by earnings quintile (earners)
out['byAge'] = {}
for lo, hi in [(25, 34), (35, 44), (45, 54), (55, 64)]:
    x = e[(e.A_AGE >= lo) & (e.A_AGE <= hi)]; out['byAge'][f'{lo}-{hi}'] = {'partTime': share(x.pt, x.MARSUPWT), 'partYearFullTime': share(x.py, x.MARSUPWT), 'under20Hours': share(x.u20, x.MARSUPWT)}
cuts = [wq(e.PEARNVAL, e.MARSUPWT, p) for p in (0.2, 0.4, 0.6, 0.8)]
e['q'] = np.searchsorted(cuts, e.PEARNVAL.values, side='right')
out['byEarningsQuintile'] = {'cuts': cuts}
for q in range(5):
    x = e[e.q == q]; out['byEarningsQuintile'][str(q + 1)] = {'partTime': share(x.pt, x.MARSUPWT), 'partYearFullTime': share(x.py, x.MARSUPWT), 'median': wq(x.PEARNVAL, x.MARSUPWT, 0.5)}
# partners' earnings correlation (normal scores), both 25-64 with earnings
cp = a[(a.partner > 0) & (a.A_LINENO < a.partner)][['PH_SEQ', 'A_LINENO', 'partner', 'PEARNVAL', 'MARSUPWT', 'type']]
cp = cp.merge(a[['PH_SEQ', 'A_LINENO', 'PEARNVAL']].rename(columns={'A_LINENO': 'partner', 'PEARNVAL': 'E2'}), on=['PH_SEQ', 'partner'])
out['partners'] = {}
for t in ['cn', 'ck', 'all']:
    x = cp if t == 'all' else cp[cp.type == t]
    both = x[(x.PEARNVAL > 0) & (x.E2 > 0)]
    z1, z2 = nscore(both.PEARNVAL.values, both.MARSUPWT.values), nscore(both.E2.values, both.MARSUPWT.values)
    out['partners'][t] = {'couples': int(len(x)), 'bothEarn': int(len(both)), 'shareBothEarn': share((x.PEARNVAL > 0) & (x.E2 > 0), x.MARSUPWT),
                          'rhoNormalScores': wcorr(z1, z2, both.MARSUPWT.values), 'rhoLog': wcorr(np.log(both.PEARNVAL.values), np.log(both.E2.values), both.MARSUPWT.values)}
# the EITC's and the refundable CTC's reach (% of adults 25-64)
w = a.MARSUPWT
out['eitc'] = {'spmUnit': share(a.SPM_EITC > 0, w), 'ownTaxUnit': share(a.tuE > 0, w), 'otherTaxUnitOnly': share((a.SPM_EITC > 0) & ~(a.tuE > 0), w),
               'dependents': share(a.DEP_STAT > 0, w), 'ownTaxUnitNoOwnEarnings': share((a.tuE > 0) & (a.PEARNVAL <= 0), w),
               'byType': {t: {'ownTaxUnit': share(a[a.type == t].tuE > 0, a[a.type == t].MARSUPWT), 'spmUnit': share(a[a.type == t].SPM_EITC > 0, a[a.type == t].MARSUPWT)} for t in ['sg', 'sp', 'cn', 'ck']}}
r = e[e.tuE > 0]
out['eitc']['recipientsWithEarnings'] = {'partTime': share(r.pt, r.MARSUPWT), 'partYearFullTime': share(r.py, r.MARSUPWT), 'fullTimeYearRound': share(r.ftyr, r.MARSUPWT)}
out['actc'] = {'spmUnit': share(a.SPM_ACTC > 0, w), 'ownTaxUnit': share(a.tuA > 0, w),
               'byType': {t: share(a[a.type == t].tuA > 0, a[a.type == t].MARSUPWT) for t in ['sg', 'sp', 'cn', 'ck']}}
# who pays for care: families with a child under 13
k13 = P[P.A_AGE < 13][['PH_SEQ', 'PEPAR1', 'PEPAR2']]
p13 = pd.concat([k13[['PH_SEQ', 'PEPAR1']].rename(columns={'PEPAR1': 'L'}), k13[['PH_SEQ', 'PEPAR2']].rename(columns={'PEPAR2': 'L'})]); p13 = p13[p13.L > 0]
n13 = p13.groupby(['PH_SEQ', 'L']).size().rename('n13').reset_index()
f = a.merge(n13, left_on=['PH_SEQ', 'A_LINENO'], right_on=['PH_SEQ', 'L'], how='left').drop(columns='L'); f['n13'] = f.n13.fillna(0)
f = f.merge(P[['PH_SEQ', 'A_LINENO', 'PEARNVAL', 'A_AGE']].rename(columns={'A_LINENO': 'partner', 'PEARNVAL': 'E2', 'A_AGE': 'age2'}), on=['PH_SEQ', 'partner'], how='left')
f = f[(f.n13 > 0) & ((f.partner < 0) | (f.A_LINENO < f.partner) | f.age2.isna())].copy()
f['couple'] = f.partner > 0; f['allEarn'] = np.where(f.couple, (f.PEARNVAL > 0) & (f.E2.fillna(0) > 0), f.PEARNVAL > 0); f['pays'] = f.SPM_CHILDCAREXPNS > 0
out['care'] = {'familiesUnder13Millions': float(f.MARSUPWT.sum()/100/1e6), 'familiesUnder13AllEarnMillions': float(f[f.allEarn].MARSUPWT.sum()/100/1e6)}
for nm, m in [('sp', ~f.couple), ('ck', f.couple)]:
    x = f[m]; y = x[x.allEarn]
    out['care'][nm] = {'families': int(len(x)), 'allEarn': share(x.allEarn, x.MARSUPWT), 'paysAll': share(x.pays, x.MARSUPWT), 'paysAllEarn': share(y.pays, y.MARSUPWT),
                       'medianPaidPayersAllEarn': wq(y[y.pays].SPM_CHILDCAREXPNS, y[y.pays].MARSUPWT, 0.5)}
out['care']['soiTY2023'] = {'returns': 5720294, 'amountThousands': 3468910, 'meanPerReturn': 3468910e3/5720294,
                            'returnsPerFamilyUnder13': 5720294/(f.MARSUPWT.sum()/100)*100}
s = json.dumps(out, indent=1)
if OUT: open(OUT, 'w').write(s + '\n')
print(s)
