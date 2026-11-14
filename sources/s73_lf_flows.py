"""S73 (Nov 14, 2026; research-update prereg/2026-11-s73-participation.md): yearly movement in and out of the labour force, from two linked years of
the Current Population Survey's Annual Social and Economic Supplement (CPS ASEC).

Sources: Census Bureau, CPS ASEC public-use CSV files (https://www2.census.gov/programs-surveys/cps/datasets/YYYY/march/), downloaded Nov 14, 2026:
  asecpub25csv.zip  sha256 318845a2b5e0034eb2973898de1738f4df0025727de38499e7669cb9c0deef0b  (person file pppub25.csv; income and work year 2024)
  asecpub26csv.zip  sha256 fe819d0d2fc4470c282e76c247b8aa8b6054811619730307e9f2fe6186707d93  (person file pppub26.csv; year 2025; the file S61 used)
The CPS interviews a household for 4 months, rests 8, and returns for 4, so about half of one March's sample is interviewed again the next March. The
person identifier PERIDNUM links them. A link is kept when sex is the same and age has risen by 0 to 2 years (97% of identifier matches; the rest are
a different person at the same address).

Status, as S61 (sources/lf_scope.py): "out" = did not work at all in the year (WORKYN 2) for one of four reasons (RSNNOTW 1 ill or disabled, 2 retired,
3 taking care of home or family, 4 going to school); everyone else is "in" (worked some time, or did not work because they could not find work, the
engine's job loss, or for another reason). Household type as S61, in the first year.
Who: adults aged 25-63 in the first survey (so 26-64 in the second), first-year weight MARSUPWT. Movers out of the address are lost to the link (the
CPS samples addresses, not people): a stated limit; the matched sample's out share is printed beside the full first-year sample's.

Estimates (weighted logistic fits, IRLS; no constant is set by hand). Covariates: age band (25-34, 35-49, 50-61, 62-64), sex, household type, and
sex by children (the care reason differs most by sex where there are children); returns on age band and sex only.
  stock[r]  share of adults 25-64 out for reason r in the 2026 cross-section (the S61 sample, now by sex as well): one fit per reason.
  ret[r]    chance that an adult "out" for reason r in year 1 is "in" in year 2 (the linked sample): one fit per reason; an age band with fewer than
            20 records out for that reason is pooled with the band below it.
  exitPanel[r]  chance that an adult "in" in year 1 is "out" for reason r in year 2 (the linked sample): one fit per reason.
  exit[r]   the exit chance that holds each cell's stock where ages do not move (the engine without ageing): exit_r = ret_r x stock_r / (1 - stock),
            stock the cell's total out share; then inflow (1 - stock) exit_r equals outflow stock_r ret_r for every reason.
  pooled    the same for adults with no age or sex (runs without ageing): by household type, each cell weighted by the 2026 survey's adults in it
            (in the labour force for exits, out for reason r for returns), so the type's out share is held as well.
The panel's own exits are higher than the stock-holding ones because they include the life cycle (more people leave than return as they age, and
the ages move); they are the reading for runs with ageing (flows 'panel').
Checks printed: the stationary out share the panel's own flows imply at fixed ages, against the cross-section; the reason mix of those who left work;
the earnings in year 1 of those who left and of those who stayed.

Output (stdout or --json=FILE): exit and ret tables (CFG.LF_FLOWS in the engine), counts, checks.
Usage: python3 sources/s73_lf_flows.py DIR25 DIR26 [--json=FILE]   (needs pandas and numpy)
"""
import json, sys
import numpy as np, pandas as pd
D0, D1 = sys.argv[1], sys.argv[2]; JS = [a[7:] for a in sys.argv[3:] if a.startswith('--json=')]
C = ['PERIDNUM', 'PH_SEQ', 'A_LINENO', 'A_AGE', 'A_SEX', 'MARSUPWT', 'A_MARITL', 'PECOHAB', 'PEPAR1', 'PEPAR2', 'WORKYN', 'RSNNOTW', 'PEARNVAL']
R = {1: 'dis', 2: 'ret', 3: 'care', 4: 'sch'}; RS = list(R.values())
TY = ['single', 'singleParent', 'coupleNoKids', 'coupleKids']; BANDS = [(25, 34), (35, 49), (50, 61), (62, 64)]; BN = ['%d-%d' % b for b in BANDS]

def load(f):
    P = pd.read_csv(f, usecols=C, dtype={'PERIDNUM': str}); P = P[P.MARSUPWT > 0]
    K = P[P.A_AGE < 18]
    par = pd.concat([K[['PH_SEQ', 'PEPAR1']].rename(columns={'PEPAR1': 'L'}), K[['PH_SEQ', 'PEPAR2']].rename(columns={'PEPAR2': 'L'})])
    par = par[par.L > 0].groupby(['PH_SEQ', 'L']).size().rename('nk').reset_index()
    P = P.merge(par, how='left', left_on=['PH_SEQ', 'A_LINENO'], right_on=['PH_SEQ', 'L']); P['nk'] = P.nk.fillna(0)
    hk = K.groupby('PH_SEQ').size()
    P['partner'] = P.A_MARITL.isin([1, 2]) | (P.PECOHAB > 0)
    P['kids'] = np.where(P.partner, P.PH_SEQ.map(hk).fillna(0).values > 0, P.nk > 0)
    P['type'] = np.where(P.partner, np.where(P.kids, 'coupleKids', 'coupleNoKids'), np.where(P.kids, 'singleParent', 'single'))
    P['r'] = np.where(P.WORKYN == 2, P.RSNNOTW.map(R).fillna('in'), 'in')
    return P

A = load(D0 + '/pppub25.csv'); B = load(D1 + '/pppub26.csv')
M = A.merge(B[['PERIDNUM', 'A_AGE', 'A_SEX', 'r']], on='PERIDNUM', suffixes=('', '1'))
idm = len(M); M = M[(M.A_SEX == M.A_SEX1) & (M.A_AGE1 - M.A_AGE).between(0, 2)]
M = M[(M.A_AGE >= 25) & (M.A_AGE <= 63)].copy()
M['band'] = pd.cut(M.A_AGE, [24, 34, 49, 61, 64], labels=BN).astype(str); M['fem'] = (M.A_SEX == 2).astype(float)

def logit(X, y, w, it=50):
    b = np.zeros(X.shape[1])
    for _ in range(it):
        p = 1/(1 + np.exp(-X @ b)); W = w*p*(1 - p) + 1e-12
        g = X.T @ (w*(y - p)); H = X.T @ (X*W[:, None]) + 1e-8*np.eye(X.shape[1])
        d = np.linalg.solve(H, g); b += d
        if np.max(np.abs(d)) < 1e-10: break
    return b
def design(df, full):
    cols = [np.ones(len(df))] + [(df.band == x).astype(float).values for x in BN[1:]] + [df.fem.values]
    if full: cols += [(df.type == t).astype(float).values for t in TY[1:]] + [df.fem.values*df.kids.astype(float).values]
    return np.column_stack(cols)
def grid(full):
    g = [{'band': b, 'fem': f, 'type': t, 'kids': t in ('singleParent', 'coupleKids')} for b in BN for f in (0.0, 1.0) for t in (TY if full else ['single'])]
    return pd.DataFrame(g)
sx = {0.0: 'm', 1.0: 'f'}
I = M[M.r == 'in']; O = M[M.r != 'in']
out = {'_meta': {'script': 'sources/s73_lf_flows.py', 'source': __doc__.split('Output')[0].strip()}}
X = B[(B.A_AGE >= 25) & (B.A_AGE <= 64)].copy()
X['band'] = pd.cut(X.A_AGE, [24, 34, 49, 61, 64], labels=BN).astype(str); X['fem'] = (X.A_SEX == 2).astype(float)
ex, rt, sk, cnt = {}, {}, {}, {'exit': {}, 'ret': {}, 'stock': {}, 'retPooled': {}}
for r in RS:
    w = X.MARSUPWT.values/X.MARSUPWT.mean(); b = logit(design(X, True), (X.r == r).astype(float).values, w)
    G = grid(True); p = 1/(1 + np.exp(-design(G, True) @ b))
    for (i, g) in G.iterrows(): sk.setdefault(g.band, {}).setdefault(sx[g.fem], {}).setdefault(g.type, {})[r] = round(float(p[i]), 5)
    cnt['stock'][r] = int((X.r == r).sum())
    w = I.MARSUPWT.values/I.MARSUPWT.mean(); b = logit(design(I, True), (I.r1 == r).astype(float).values, w)
    G = grid(True); p = 1/(1 + np.exp(-design(G, True) @ b))
    for (i, g) in G.iterrows(): ex.setdefault(g.band, {}).setdefault(sx[g.fem], {}).setdefault(g.type, {})[r] = round(float(p[i]), 5)
    cnt['exit'][r] = int((I.r1 == r).sum())
    Q = O[O.r == r].copy(); mp = {}
    for k, bn in enumerate(BN):  # pool a thin band with the band below it
        mp[bn] = bn if k == 0 or (Q.band == bn).sum() >= 20 else mp[BN[k - 1]]
    Q['band'] = Q.band.map(mp); cnt['retPooled'][r] = {k: v for k, v in mp.items() if k != v}
    w = Q.MARSUPWT.values/Q.MARSUPWT.mean(); b = logit(design(Q, False), (Q.r1 == 'in').astype(float).values, w)
    G = grid(False); G['band'] = G.band.map(mp); p = 1/(1 + np.exp(-design(G, False) @ b))
    for (i, g) in grid(False).iterrows(): rt.setdefault(r, {}).setdefault(g.band, {})[sx[g.fem]] = round(float(p[i]), 5)
    cnt['ret'][r] = {'out': int(len(Q)), 'returned': int((Q.r1 == 'in').sum()), 'byBand': {bn: int((Q.band == bn).sum()) for bn in BN}}
eh = {}
for b in BN:
    for f in ('m', 'f'):
        for t in TY:
            S = sum(sk[b][f][t].values()); eh.setdefault(b, {}).setdefault(f, {})[t] = {r: round(rt[r][b][f]*sk[b][f][t][r]/(1 - S), 5) for r in RS}
cw = X.groupby(['band', 'fem', 'type']).MARSUPWT.sum()
pl = {'stock': {}, 'exit': {}, 'exitPanel': {}, 'ret': {}}
for t in TY:
    cells = [(b, f) for b in BN for f in (0.0, 1.0) if (b, f, t) in cw.index]; W = {c: cw[(c[0], c[1], t)] for c in cells}
    win = {c: W[c]*(1 - sum(sk[c[0]][sx[c[1]]][t].values())) for c in cells}
    pl['stock'][t] = {r: round(sum(W[c]*sk[c[0]][sx[c[1]]][t][r] for c in cells)/sum(W.values()), 5) for r in RS}
    pl['exit'][t] = {r: round(sum(win[c]*eh[c[0]][sx[c[1]]][t][r] for c in cells)/sum(win.values()), 5) for r in RS}
    pl['exitPanel'][t] = {r: round(sum(win[c]*ex[c[0]][sx[c[1]]][t][r] for c in cells)/sum(win.values()), 5) for r in RS}
    pl['ret'][t] = {r: round(sum(W[c]*sk[c[0]][sx[c[1]]][t][r]*rt[r][c[0]][sx[c[1]]] for c in cells)/sum(W[c]*sk[c[0]][sx[c[1]]][t][r] for c in cells), 5) for r in RS}
out['stock'] = sk; out['ret'] = rt; out['exit'] = eh; out['exitPanel'] = ex; out['pooled'] = pl; out['counts'] = cnt
def ws(m, w): return float((w*m).sum()/w.sum())
out['checks'] = {
  'idMatches': idm, 'linked25to63': int(len(M)), 'linkedIn': int(len(I)), 'linkedOut': int(len(O)),
  'outShareLinked': {r: round(ws(M.r == r, M.MARSUPWT), 5) for r in RS},
  'outShareFull2025': {r: round(ws(A[(A.A_AGE >= 25) & (A.A_AGE <= 63)].r == r, A[(A.A_AGE >= 25) & (A.A_AGE <= 63)].MARSUPWT), 5) for r in RS},
  'exitRate': round(ws(I.r1 != 'in', I.MARSUPWT), 5), 'exitMix': {r: round(ws(I[I.r1 != 'in'].r1 == r, I[I.r1 != 'in'].MARSUPWT), 4) for r in RS},
  'exitMixBySex': {s: {r: round(ws(x.r1 == r, x.MARSUPWT), 4) for r in RS} for s, x in [('m', I[(I.r1 != 'in') & (I.fem == 0)]), ('f', I[(I.r1 != 'in') & (I.fem == 1)])]},
  'returnRate': {r: round(ws(O[O.r == r].r1 == 'in', O[O.r == r].MARSUPWT), 4) for r in RS},
  'leaversEarnYear1Mean': round(float((I[I.r1 != 'in'].PEARNVAL.clip(lower=0)*I[I.r1 != 'in'].MARSUPWT).sum()/I[I.r1 != 'in'].MARSUPWT.sum())),
  'stayersEarnYear1Mean': round(float((I[I.r1 == 'in'].PEARNVAL.clip(lower=0)*I[I.r1 == 'in'].MARSUPWT).sum()/I[I.r1 == 'in'].MARSUPWT.sum()))}
# stationary shares the fitted flows imply, by cell (out share for each reason = exit_r / (exit_r + ret_r), treating reasons separately), against the linked cross-section
st = {}
for b in BN:
    for f in ('m', 'f'):
        for t in TY:
            e = ex[b][f][t]; st.setdefault(b, {}).setdefault(f, {})[t] = round(sum(e[r]/(e[r] + rt[r][b][f]) for r in RS), 4)
out['checks']['stationaryOutShare'] = st
x = M.copy(); x['cell'] = list(zip(x.band, x.fem.map(sx), x.type))
x['stat'] = [st[c[0]][c[1]][c[2]] for c in x.cell]
xs = X.copy(); xs['S'] = [sum(sk[b][sx[f]][t].values()) for b, f, t in zip(xs.band, xs.fem, xs.type)]
xs['E'] = [sum(eh[b][sx[f]][t].values()) for b, f, t in zip(xs.band, xs.fem, xs.type)]; xs['EP'] = [sum(ex[b][sx[f]][t].values()) for b, f, t in zip(xs.band, xs.fem, xs.type)]
out['checks']['stockFit'] = {'fitted': round(float((xs.S*xs.MARSUPWT).sum()/xs.MARSUPWT.sum()), 4), 'survey': round(ws(xs.r != 'in', xs.MARSUPWT), 4)}
out['checks']['exitMean'] = {'stockHolding': round(float((xs.E*(1 - xs.S)*xs.MARSUPWT).sum()/((1 - xs.S)*xs.MARSUPWT).sum()), 5), 'panel': round(float((xs.EP*(1 - xs.S)*xs.MARSUPWT).sum()/((1 - xs.S)*xs.MARSUPWT).sum()), 5)}
out['checks']['stationaryVsLinked'] = {'stationary': round(float((x.stat*x.MARSUPWT).sum()/x.MARSUPWT.sum()), 4), 'linkedYear1': round(ws(x.r != 'in', x.MARSUPWT), 4), 'linkedYear2': round(ws(x.r1 != 'in', x.MARSUPWT), 4)}
s = json.dumps(out, indent=1)
if JS: open(JS[0], 'w').write(s + '\n')
else: print(s)
