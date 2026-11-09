"""S61 (Nov 9, 2026; research-update prereg/2026-11-s61-baseline-scope.md): adults 25-64 outside the labour force for the whole year, and their own income.

Source: Census Bureau, Current Population Survey, 2026 Annual Social and Economic Supplement (CPS ASEC), public-use CSV (asecpub26csv.zip,
https://www2.census.gov/programs-surveys/cps/datasets/2026/march/, downloaded Nov 9, 2026, sha256 fe819d0d2fc4470c282e76c247b8aa8b6054811619730307e9f2fe6186707d93),
person file pppub26.csv, income year 2025, weight MARSUPWT (two implied decimals, which cancel in shares and percentiles).

Who: adults aged 25-64 (A_AGE) who did not work at all in 2025 (WORKYN 2), by the reason they give (RSNNOTW): 1 ill or disabled, 2 retired, 3 taking care
of home or family, 4 going to school. Reasons 5 (could not find work: in the labour force, the engine's job loss covers it) and 6 (other), and those
not asked (0), are left in the labour force: a stated simplification (2.1% of adults 25-64).
Household type, as sources/households.py: partnered = married with the spouse present (A_MARITL 1-2) or cohabiting (PECOHAB > 0); with children = a
child under 18 in the household who names this adult as a parent (PEPAR1, PEPAR2; for a partnered adult: any child under 18 in the household, so the
partner's children count, as the model's couple-with-children class does).
Own income (2025 dollars): the adult's cash income that does not come from work or from wealth: Social Security (SS_VAL, including disability
insurance), Supplemental Security Income (SSI_VAL), other disability income (DSAB_VAL), pensions (PNSN_VAL), survivor income (SRVS_VAL), veterans'
payments (VET_VAL), public assistance (PAW_VAL), unemployment and workers' compensation (UC_VAL, WC_VAL), educational assistance (ED_VAL), child support
(CSP_VAL), financial help from outside the household (FIN_VAL) and other income (OI_VAL). Interest, dividends, rent, annuities and retirement-account
withdrawals are left out: in the model they are paid out of the adult's wealth, and SNAP and tax credits are the engine's own safety net.

Output (stdout or --json=FILE): shares of adults 25-64 by household type and reason; the same by age band (25-34, 35-49, 50-61, 62-64) for runs with
ageing; own-income percentiles 0, 0.5, ..., 100 by reason, and their means beside the survey's (ownIncomeMean); official poverty (PERLIS 1, POV_UNIV 1) by reason; checks (share with no earnings, share who did not work, unweighted counts).
Usage: python3 sources/lf_scope.py DATA_DIR [--json=FILE]   (needs pandas and numpy)
"""
import json, sys
import numpy as np, pandas as pd
D = sys.argv[1]; JS = [a[7:] for a in sys.argv[2:] if a.startswith('--json=')]
INC = ['SS_VAL', 'SSI_VAL', 'DSAB_VAL', 'PNSN_VAL', 'SRVS_VAL', 'VET_VAL', 'PAW_VAL', 'UC_VAL', 'WC_VAL', 'ED_VAL', 'CSP_VAL', 'FIN_VAL', 'OI_VAL']
P = pd.read_csv(D + '/pppub26.csv', usecols=['PH_SEQ', 'A_LINENO', 'A_AGE', 'MARSUPWT', 'A_MARITL', 'PECOHAB', 'PEPAR1', 'PEPAR2', 'WORKYN', 'RSNNOTW', 'PEARNVAL', 'PERLIS', 'POV_UNIV'] + INC)
P = P[P.MARSUPWT > 0]
K = P[P.A_AGE < 18]
par = pd.concat([K[['PH_SEQ', 'PEPAR1']].rename(columns={'PEPAR1': 'L'}), K[['PH_SEQ', 'PEPAR2']].rename(columns={'PEPAR2': 'L'})])
par = par[par.L > 0].groupby(['PH_SEQ', 'L']).size().rename('nk').reset_index()
P = P.merge(par, how='left', left_on=['PH_SEQ', 'A_LINENO'], right_on=['PH_SEQ', 'L']); P['nk'] = P.nk.fillna(0)
hk = K.groupby('PH_SEQ').size()
a = P[(P.A_AGE >= 25) & (P.A_AGE <= 64)].copy()
a['partner'] = a.A_MARITL.isin([1, 2]) | (a.PECOHAB > 0)
a['kids'] = np.where(a.partner, a.PH_SEQ.map(hk).fillna(0).values > 0, a.nk > 0)
a['type'] = np.where(a.partner, np.where(a.kids, 'coupleKids', 'coupleNoKids'), np.where(a.kids, 'singleParent', 'single'))
R = {1: 'dis', 2: 'ret', 3: 'care', 4: 'sch'}
a['r'] = np.where(a.WORKYN == 2, a.RSNNOTW.map(R).fillna('lf'), 'lf')
a['own'] = a[INC].clip(lower=0).sum(axis=1)
TY = ['single', 'singleParent', 'coupleNoKids', 'coupleKids']; BANDS = [(25, 34), (35, 49), (50, 61), (62, 64)]
def sh(m, w): return float((w*m).sum()/w.sum())
def wq(x, w, q):
    o = np.argsort(x.values, kind='stable'); xs = x.values[o].astype(float); ws = w.values[o].astype(float); c = (np.cumsum(ws) - ws/2)/ws.sum(); return np.interp(q, c, xs)
out = {'_meta': {'script': 'sources/lf_scope.py', 'source': __doc__.split('Output')[0].strip()}}
out['shares'] = {t: {r: round(sh(a[a.type == t].r == r, a[a.type == t].MARSUPWT), 5) for r in R.values()} for t in TY}
out['sharesByAge'] = {'%d-%d' % b: {t: {r: round(sh(x.r == r, x.MARSUPWT), 5) for r in R.values()} for t in TY for x in [a[(a.type == t) & (a.A_AGE >= b[0]) & (a.A_AGE <= b[1])]]} for b in BANDS}
out['nByAge'] = {'%d-%d' % b: {t: int(((a.type == t) & (a.A_AGE >= b[0]) & (a.A_AGE <= b[1])).sum()) for t in TY} for b in BANDS}
Q = np.linspace(0, 1, 201)  # S61 Amendment 2: 0.5-point steps (5-point steps overstated the mean by 9-280% through the top bin)
out['ownIncome'] = {r: [round(float(v)) for v in wq(a[a.r == r].own, a[a.r == r].MARSUPWT, Q)] for r in R.values()}
out['ownIncomeMean'] = {r: round(float((a[a.r == r].own*a[a.r == r].MARSUPWT).sum()/a[a.r == r].MARSUPWT.sum())) for r in R.values()}
out['ownIncomeZero'] = {r: round(sh(a[a.r == r].own <= 0, a[a.r == r].MARSUPWT), 4) for r in R.values()}
pv = a[a.POV_UNIV == 1]
out['officialPoverty'] = dict({r: round(sh(pv[pv.r == r].PERLIS == 1, pv[pv.r == r].MARSUPWT), 4) for r in R.values()}, inLF=round(sh(pv[pv.r == 'lf'].PERLIS == 1, pv[pv.r == 'lf'].MARSUPWT), 4), all=round(sh(pv.PERLIS == 1, pv.MARSUPWT), 4))
out['checks'] = {'adults': int(len(a)), 'didNotWork': round(sh(a.WORKYN == 2, a.MARSUPWT), 4), 'noEarnings': round(sh(a.PEARNVAL <= 0, a.MARSUPWT), 4),
                 'outsideLF': {r: round(sh(a.r == r, a.MARSUPWT), 5) for r in R.values()}, 'leftInLF': round(sh((a.WORKYN == 2) & (a.r == 'lf'), a.MARSUPWT), 4),
                 'typeShares': {t: round(sh(a.type == t, a.MARSUPWT), 4) for t in TY}, 'n': {r: int((a.r == r).sum()) for r in R.values()}}
s = json.dumps(out, indent=1)
if JS: open(JS[0], 'w').write(s + '\n')
else: print(s)
