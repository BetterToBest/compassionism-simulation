"""S69: the programme's own steps (sections 6.4-6.13, 12.2, 12.3, 13.4, 14.1, 14.2), in section 5's order. With no programme every function is inert."""
import math
from s69_engine import NS, INF
from s69_rng import Mulberry32


# ------------------------------------------------------------------ small rules
def szh_theta(R, coh):
    C = R.CFG
    if coh < C['SZH_THETA_THRESHOLD']:
        return 0
    return min(C['SZH_THETA_MAX'], (coh - C['SZH_THETA_THRESHOLD']) / (C['SZH_THETA_MAX_COH'] - C['SZH_THETA_THRESHOLD']) * C['SZH_THETA_MAX'])


def c22_share(R, comp):
    s = 0.0
    for k in R.S['C22_NEEDS']:
        s += R.CFG['BASKET'][k] * (comp[k] if comp else 1)
    return s


def sx_h(R, h):
    return h


def pa_w(R, a):
    return R.PAS.z[0]


def blei_szh_ptf(R, a):
    """agentBLEI's SZH term for PTF customers: under open access every adult, on the zone's PTF share of sales."""
    th = R.THETA_DENS if (R.THETA_GATE == 'density' and R.THETA_DENS is not None) else R.p['szhCoh']
    t = szh_theta(R, th) * 0.20
    return pa_w(R, a) * t if R.PAS else t


def blei_bu_food_engine(R, a, buAlloc):
    return buAlloc * (990 / 1200)


def tb_gate_bu_engine(R, a, buEff):
    return buEff * (990 / 1200)


def ptf_mode_cut(R, p, k='food'):
    if R.S.get('PTF_MODE') == 'shipped':
        return 0.12 + p['szhCoh'] * 0.04 if p['szh'] else 0.12
    return R.S['PTF_FOOD_CUT'][R.S['PTF_MODE']] if k == 'food' else 0


def pj_own_rate(R, a, p, pcb):
    C = R.CFG
    oc = 1 + (a.octave / max(1, p['maxOct'])) * (max(1, p['maxMult']) - 1)
    qf = min(1, a.quality / max(1, p['maxMult']))
    ph = C['PHI_RATIO'] if (p['phi'] and a.quality > p['maxMult'] * C['PHI_QUALITY_THRESH']) else 1.0
    pb = po_bonus(R, a, p, pcb) if R.POS else (pcb if (p['ptf'] and a.inPTF) else 1.0)
    return min((1 + qf * (oc - 1)) * ph * pb, p['maxMult'] * (C['PHI_RATIO'] if p['phi'] else 1.0))


def pj_tax(R, p, r):
    C = R.CFG
    bT = p['tax'] * (1 - p['cipDemo'] * 0.18) if p['cip'] else p['tax']
    return min(C['PROG_TAX_MAX'], bT + max(0, (r - C['PROG_PIVOT']) * C['PROG_RATE']))


# ------------------------------------------------------------------ PTF by sector (12.3), open access (14.1), running costs (14.2)
def ptfs_shares(R, a, HHA):
    if HHA and a._hhS:
        return a._hhS
    C = R.CFG
    PR = R.PRICE

    def c(k):
        return PR.comp[k] / PR.bIdx if PR else 1
    B = C['BASKET']
    return dict(f=B['food'] * c('food'), h=B['housing'] * c('housing'), t=B['transport'] * c('transport'), m=B['medical'] * c('medical'), k=0)


def ptfs_cut(R, a, HHA, p, quiet=False, full=False):
    C = R.CFG
    if R.POS:
        return po_ptfs_cut(R, a, HHA, p, quiet, full)
    s = ptfs_shares(R, a, HHA)
    dens = pa_w(R, a) if R.PAS else R.PFS.dens
    eF = C['PTFS_EPS_FOOD_LOW'] if (R.PFS and dens < C['PTFS_LOW_DENS']) else C['PTFS_EPS_FOOD']
    o = R.PTFS['other']
    c = s['f'] * (1 - 1 / eF) + s['h'] * C['PTFS_UTIL'] * (1 - 1 / C['PTFS_EPS_UTIL']) + (s['t'] + s['m'] + s['k']) * o
    if p['szh']:
        c *= (0.12 + p['szhCoh'] * 0.04) / 0.12
    if R.PAS and not full:
        c = pa_w(R, a) * min(0.95, c)
    if R.PFS and not quiet:
        R.PFS.cut += c
        R.PFS.cn += 1
    return min(0.95, c)


def ptfs_year(R, agents, yr):
    F = R.PFS
    u = [F.r() for _ in agents]
    if yr > 0:
        for i, a in enumerate(agents):
            if not a.inPTF or (a._hh and not a._hh.single and a._hh.a and a._hh.a[0] is not a):
                continue
            if u[i] < R.PTFS['leave']:
                a.inPTF = False
                F.leave += 1
                if a._hh and a._hh.a:
                    for b in a._hh.a:
                        b.inPTF = False
    m = 0
    for a in agents:
        if a.inPTF:
            m += 1
    F.dens = m / max(1, len(agents))
    F.mem += F.dens
    F.yrs += 1


def pa_init(R, agents):
    PA = R.PA
    m = 0
    t = 0
    for a in agents:
        t += 1
        if a.inPTF:
            m += 1
    z = [PA['fix'] if PA['fix'] is not None else m / max(1, t)]
    R.PAS = NS(z=z, s=0.0, sh=0.0, lo=0.0, th=0.0, yrs=0, cb=0.0, ob=0.0, db=0.0, yu=0, cv=0.0, sY={}, cY={})
    pa_pop(R, agents)


def pa_cap_now(R, yr, p):
    if R.PA['cap'] == 'none' or not (R.PROD and R.CONVERSION_MODEL == 'framework' and p['ptf'] and R.PROD.get('cap') == 'ptf' and R.PDS):
        return 1
    K = R.SURP['K'] if R.SURP else INF
    A = R.SPS.capPA if (yr > 0 and R.SURP and R.SPS) else 0
    return 1 if K <= 0 else min(1, R.PDS.c0 + A / K)


def pa_cover(R, s, p):
    C = R.CFG
    g = (0.12 + p['szhCoh'] * 0.04) / 0.12 if p['szh'] else 1
    eF = C['PTFS_EPS_FOOD_LOW'] if s < C['PTFS_LOW_DENS'] else C['PTFS_EPS_FOOD']
    M = R.COST or R.S['COST_DEFAULTS']
    f = C['BASKET']['food']
    u = C['BASKET']['housing'] * C['PTFS_UTIL']
    pf = max(0, 1 - g * (1 - 1 / eF))
    pu = max(0, 1 - g * (1 - 1 / C['PTFS_EPS_UTIL']))
    return (f * pf + u * pu) / (f * (1 - M['food']) + u * (1 - M['util'] / C['PTFS_UTIL']))


def pa_ops_max(R, s, p):
    if R.PA['ops'] == 'hub' or pa_cover(R, 1, p) >= 1:
        return 1
    return max(s, R.CFG['PTFS_LOW_DENS'] * (1 - 1e-12)) if pa_cover(R, 0, p) >= 1 else s


def pa_grow(R, agents, yr, p):
    S = R.PAS
    PA = R.PA
    n = max(1, len(agents))
    w = len(agents) / n
    tot = w * S.z[0]
    o = pa_ops_max(R, S.z[0], p)
    want = max(0, min(PA['dem'], o) - S.z[0])
    al = w * want
    k = min(1, max(0, S.cY[yr] - tot) / al) if al > 0 else 0
    if want > 0 and k < 1:
        S.cb += w
    elif PA['dem'] <= o:
        S.db += w
    else:
        S.ob += w
    S.z[0] += k * want
    S.yu += 1


def pa_pop(R, agents):
    S = R.PAS
    C = R.CFG
    n = max(1, len(agents))
    t = len(agents)
    s = t / n * S.z[0]
    lo = t / n if S.z[0] < C['PTFS_LOW_DENS'] else 0
    th = t / n if S.z[0] > C['SZH_THETA_THRESHOLD'] else 0
    S.s = s
    return lo, th


def pa_year(R, agents, yr, p):
    S = R.PAS
    if yr > 0:
        S.cY[yr] = pa_cap_now(R, yr, p)
        if R.POS:
            po_year(R, agents, yr, p)
        if R.PA['grow'] and R.PA['fix'] is None:
            if R.POS and R.PTF_OPS.get('hire') is not None:
                raise NotImplementedError('po.hire')
            pa_grow(R, agents, yr, p)
    elif R.POS:
        po_year(R, agents, yr, p)
    lo, th = pa_pop(R, agents)
    S.sh += S.s
    S.lo += lo
    S.th += th
    S.yrs += 1
    S.sY[yr] = S.s
    n = max(1, len(agents))
    S.cv += len(agents) / n * pa_cover(R, S.z[0], p)
    if R.POS:
        po_tally(R, agents, p)


def pa_res(R, out):
    S = R.PAS
    out['paSh'] = S.sh / S.yrs * 100 if S.yrs else 0
    out['paLo'] = S.lo / S.yrs * 100 if S.yrs else 0
    out['paTh'] = S.th / S.yrs * 100 if S.yrs else 0
    out['paCap'] = S.cb / S.yu * 100 if S.yu else 0
    out['paOps'] = S.ob / S.yu * 100 if S.yu else 0
    out['paDem'] = S.db / S.yu * 100 if S.yu else 0
    out['paCv'] = S.cv / S.yrs * 100 if S.yrs else 0
    for y in (5, 10, 19, 39):
        out['paS' + str(y)] = S.sY[y] * 100 if y in S.sY else 0
        out['paC' + str(y)] = S.cY[y] * 100 if y in S.cY else 0


def po_forg(R, k):
    P = R.PTF_OPS
    C = R.CFG
    M = R.COST or R.S['COST_DEFAULTS']
    g = R.POS.g if R.POS else 0
    if k == 'f':
        return 1 - C['PO_SECTOR']['f'] - C['PO_PAY']['f'] * g if P['cost'] == 'sector' else M['food'] - P['res'] - C['PO_PAY']['f'] * g
    return C['PTFS_UTIL'] * (1 - C['PO_SECTOR']['u'] - C['PO_PAY']['u'] * g) if P['cost'] == 'sector' else M['util'] - C['PTFS_UTIL'] * (P['res'] + C['PO_PAY']['u'] * g)


def po_cost(R, k):
    return 1 - po_forg(R, 'f') if k == 'f' else 1 - po_forg(R, 'u') / R.CFG['PTFS_UTIL']


def po_eps(R, sh):
    P = R.PTF_OPS
    C = R.CFG
    lo = C['PTFS_EPS_FOOD_LOW']
    hi = C['PTFS_EPS_FOOD']
    t = C['PTFS_LOW_DENS']
    if P['curve'] == 'step' or not (P['w'] > 0):
        return lo if sh < t else hi
    x = min(1, max(0, (sh - (t - P['w'])) / (2 * P['w'])))
    return 1 / ((1 - x) / lo + x / hi)


def po_price(R):
    return R.PTF_OPS['pay'] == 'price' and R.PTF_OPS['cost'] != 'hub'


def po_tz(R, z):
    P = R.PTF_OPS
    return R.POS.mz[z] if P['test'] == 'members' else (R.POS.cs if P['test'] == 'capacity' else R.PAS.z[z])


def po_t_pop(R):
    if R.PTF_OPS['test'] == 'sales':
        return R.PAS.s
    return R.POS.wz[0] * po_tz(R, 0)


def pa_pop_share(R):
    return R.PAS.s


def po_cut_parts(R, sh, ts, p):
    if po_price(R):
        return [max(0, 1 - po_cost(R, 'f')), max(0, 1 - po_cost(R, 'u'))]
    g = (0.12 + p['szhCoh'] * 0.04) / 0.12 if p['szh'] else 1
    return [g * (1 - 1 / po_eps(R, ts)), g * (1 - 1 / R.CFG['PTFS_EPS_UTIL'])]


def po_cover(R, i, p):
    C = R.CFG
    if R.PTF_OPS['cost'] == 'hub':
        return 1
    c = po_cut_parts(R, R.PAS.z[i], po_tz(R, i), p)
    f = C['BASKET']['food']
    u = C['BASKET']['housing'] * C['PTFS_UTIL']
    return (f * max(0, 1 - c[0]) + u * max(0, 1 - c[1])) / (f * po_cost(R, 'f') + u * po_cost(R, 'u'))


def po_worker(R, a):
    return (not a._ret) and not (R.LFS and a._lf) and a.wage > 0


def po_bonus(R, a, p, pcb):
    if R.PTF_OPS['bonus'] == 'members':
        return pcb if (p['ptf'] and a.inPTF) else 1.0
    if not p['ptf'] or not po_worker(R, a):
        return 1.0
    return 1 + min(1, R.CFG['PO_JOBS'] * pa_w(R, a)) * (pcb - 1)


def po_free(R, a, M, cfP, fS, hS):
    cut = M * (1 - cfP)
    if R.PTF_OPS['cost'] == 'hub' or po_price(R):
        return cut
    return max(0, min(cut, M * (fS * po_forg(R, 'f') + hS * po_forg(R, 'u')) * pa_w(R, a)))


def po_ptfs_cut(R, a, HHA, p, quiet, full):
    C = R.CFG
    s = ptfs_shares(R, a, HHA)
    pr = po_price(R)
    if pr:
        eF = 1 / min(1, max(1e-9, po_cost(R, 'f')))
        eU = 1 / min(1, max(1e-9, po_cost(R, 'u')))
        o = 0
    else:
        eF = po_eps(R, po_tz(R, 0))
        eU = C['PTFS_EPS_UTIL']
        o = R.PTFS['other']
    c = s['f'] * (1 - 1 / eF) + s['h'] * C['PTFS_UTIL'] * (1 - 1 / eU) + (s['t'] + s['m'] + s['k']) * o
    if p['szh'] and not pr:
        c *= (0.12 + p['szhCoh'] * 0.04) / 0.12
    if not full:
        c = pa_w(R, a) * min(0.95, c)
    if R.PFS and not quiet:
        R.PFS.cut += c
        R.PFS.cn += 1
        R.POS.eN += pa_w(R, a) * eF
        R.POS.eD += pa_w(R, a)
    return min(0.95, c)


def po_init(R, agents):
    n = max(1, len(agents))
    wz = [0.0]
    for a in agents:
        wz[0] += 1 / n
    R.POS = NS(wz=wz, mz=[0.0], cs=0.0, g=0.0, gN=0.0, gD=0.0, gY=0.0, gy=0, sub=0.0, fr=0.0, eN=0.0, eD=0.0, cv=0.0, cy=0, wk=0.0, wh=0.0, wn=0, ay=0, bn=0.0, bc=0, hb=0.0, yu=0)


def po_year(R, agents, yr, p):
    S = R.POS
    n = max(1, len(agents))
    t = 0
    m = 0
    for a in agents:
        t += 1
        if a.inPTF:
            m += 1
    S.wz[0] = t / n
    S.mz[0] = m / max(1, t)
    S.g = S.gN / S.gD if S.gD > 0 else 0
    S.gN = 0.0
    S.gD = 0.0
    if yr > 0:
        S.gY += S.g
        S.gy += 1
    cap = R.PAS.cY[yr] if (yr > 0 and yr in R.PAS.cY) else pa_cap_now(R, 0, p)
    S.cs = min(1, cap / R.PA['dem'])


def po_tally(R, agents, p):
    S = R.POS
    n = max(1, len(agents))
    wk = 0
    wh = 0.0
    PJ = R.CFG['PO_JOBS']
    for a in agents:
        if not po_worker(R, a):
            continue
        wk += 1
        wh += min(1, PJ * pa_w(R, a))
    S.cv += S.wz[0] * po_cover(R, 0, p)
    S.cy += 1
    S.wk += wh / n * 100
    S.wh += wh / wk * 100 if wk > 0 else 0
    S.wn += 1


def po_res(R, out, NY, cost):
    S = R.POS
    out['poSub'] = S.sub / max(1, NY)
    out['poFree'] = S.fr / max(1, NY)
    out['poSubSh'] = out['poSub'] / cost * 100 if cost > 0 else 0
    out['poEpsF'] = S.eN / S.eD if S.eD > 0 else 0
    out['poCov'] = S.cv / S.cy * 100 if S.cy else 0
    out['poWk'] = S.wk / S.wn if S.wn else 0
    out['poWkH'] = S.wh / S.wn if S.wn else 0
    out['poBon'] = S.bn / S.bc * 100 if S.bc else 0
    out['poHire'] = S.hb / S.yu * 100 if S.yu else 0
    out['poG'] = S.gY / S.gy * 100 if S.gy else 0


def po_free_year(R, a, M, cfPTF, fSA, hSA):
    a._csFree = po_free(R, a, M, cfPTF, fSA, hSA)
    a._csFreeY = a._csFree
    a._poS = max(0, M * (1 - cfPTF) - a._csFree)
    a._poF = a._csFree


# ------------------------------------------------------------------ PTH's books (12.2, 13.2 fx.pthb and fx.hb)
def pthb_init(R, agents, latent, seed):
    R.PBS = NS(r=Mulberry32(seed + 600043), q=[], P=1, pi=0, n=0, exits=0, cash=0.0, cover=0, aP=0.0, aR=0.0, aC=0.0, fill=0, slots=[])
    for i, a in enumerate(agents):
        a._pbU = latent[i].uPTH if i < len(latent) else 1
        if a.inPTH:
            a._pbS = NS(V=0.0, D=0.0, CE=0.0)
            R.PBS.slots.append(a._pbS)
        else:
            R.PBS.q.append(a)
    R.PBS.q.sort(key=lambda x: x._pbU)
    R.agentIndex = {id(a): i for i, a in enumerate(agents)}


def pthb_year(R, agents, yr, P):
    B = R.PBS
    B.pi = P / B.P - 1 if (yr > 0 and B.P > 0) else 0
    B.P = P
    if yr == 0:
        return
    PT = R.PTHB
    x = PT['x']
    rate = R.CFG['PTHB_EXIT_OWN'] if PT['exit'] == 'owners' else PT['exit']
    u = [B.r() for _ in agents]
    idx = R.agentIndex
    go = []
    for i, a in enumerate(agents):
        if not a.inPTH or not a._pbS:
            continue
        h = a._hh.a[0] if (a._hh and not a._hh.single and a._hh.a) else a
        j = idx.get(id(h), -1)
        if (u[j] if j >= 0 else u[i]) < rate:
            go.append(a)
    for a in go:
        S = a._pbS
        E = max(0, a.acreEquity or 0)
        c = x * E
        a.wealth += c
        S.D += c
        S.CE += E - c
        a.acreEquity = 0
        a.inPTH = False
        a.pthTenure = 0
        a._pbS = None
        B.exits += 1
        B.cash += c / P
        while B.q and (B.q[0].inPTH or id(B.q[0]) not in idx):
            B.q.pop(0)
        if B.q:
            b = B.q.pop(0)
            b.inPTH = True
            b.acreEquity = 0
            b.pthTenure = 0
            b._pbS = S
            B.fill += 1


def pthb_res(R, out):
    A = R.PBS
    n = len(A.slots) if (A and A.slots) else 0
    P = A.P if A else 1

    def sm(k):
        t = 0.0
        for S in A.slots:
            t += getattr(S, k)
        return t
    out['pbV'] = sm('V') / n / P if n else 0
    out['pbD'] = sm('D') / n / P if n else 0
    out['pbCE'] = sm('CE') / n / P if n else 0
    out['pbME'] = out['pbV'] - out['pbD'] - out['pbCE'] if n else 0
    out['pbCover'] = A.cover / A.n * 100 if (A and A.n) else 0
    out['pbExit'] = A.exits / A.n * 100 if (A and A.n) else 0
    out['pbCash'] = A.cash / A.exits if (A and A.exits) else 0
    out['pbAprP'] = A.aP / A.n if (A and A.n) else 0
    out['pbAprR'] = A.aR / A.n if (A and A.n) else 0
    out['pbAprC'] = A.aC / A.n if (A and A.n) else 0
    out['pbFill'] = A.fill / A.exits * 100 if (A and A.exits) else 0


def pth_member(R, a, p, Y, A_):
    C = R.CFG
    a.pthTenure = (a.pthTenure or 0) + 1
    dcA = A_.dcA
    pthSaving = max(0, dcA * (A_.cfPTF - A_.cfPreCCO) * 1)
    equityContrib = pthSaving * C['PTH_EQUITY_CONTRIB_SHARE']
    a.acreEquity += equityContrib
    a.wealth -= equityContrib
    A_.yrCashSurplus -= equityContrib
    ar = 0.030 + A_.uPthAppr * 0.020 + Y.pthApprBonus
    PB = R.PBS
    pbS = a._pbS if (R.PTHB and PB) else None
    pbV0 = pbVn = 0.0
    if pbS:
        if not pbS.V:
            pbS.V = C['PTHB_PR'] * A_.hSA * (A_.mlc if (R.FX and R.FX.get('hb')) else dcA)
            pbS.D = pbS.V - (a.acreEquity - equityContrib)
        pbV0 = pbS.V
        pbVn = pbV0 * (1 + PB.pi) * (1 + C['PTHB_G'])
        if R.PTHB['cap'] == 'hub':
            ar = min(pbVn / pbV0 - 1, PB.pi + 0.02)
    appr = a.acreEquity * ar
    T = a.pthTenure
    tt = max(1, min(C['PTH_LIQUID_SHARE_MATURE_YR'], T))
    span = C['PTH_LIQUID_SHARE_MATURE_YR'] - 1
    lqs = C['PTH_LIQUID_SHARE_YEAR1'] + (tt - 1) / span * (C['PTH_LIQUID_SHARE_YEAR5PLUS'] - C['PTH_LIQUID_SHARE_YEAR1']) if span > 0 else C['PTH_LIQUID_SHARE_YEAR5PLUS']
    if pbS:
        lqs *= max(0, appr - PB.pi * a.acreEquity) / appr if appr > 0 else 0
    if R.PTH_APPR_CONSERVE:
        a.acreEquity += appr * (1 - lqs)
    else:
        a.acreEquity += appr
    a.wealth += appr * lqs
    A_.yrCashSurplus += appr * lqs
    if Y.tbY:
        a._tbPthNow = appr * lqs
    if pbS:
        pbR = A_.hSA * (A_.mlc if (R.FX and R.FX.get('hb')) else dcA)
        pbI = ((1 + C['PTHB_RREAL']) * (1 + PB.pi) - 1) * pbS.D
        pbU = C['PTHB_UPK'] * (1 - C['PTHB_LAND']) * pbV0
        pbT = C['PTHB_TAX'] * pbV0
        pbL = appr * lqs
        pbS.D -= pbR + equityContrib - pbI - pbU - pbT - pbL
        pbS.CE += (pbVn - pbV0) + pbR - pbI - pbU - pbT - appr
        pbS.V = pbVn
        PB.n += 1
        if pbR + equityContrib >= pbI - PB.pi * (pbS.D + pbR + equityContrib - pbI - pbU - pbT - pbL) + pbU + pbT + pbL:
            PB.cover += 1
        PB.aP += pbV0 * PB.pi / PB.P
        PB.aR += pbV0 * (1 + PB.pi) * C['PTHB_G'] / PB.P
        PB.aC += (pbVn - pbV0 - appr) / PB.P
    if R.PRICE:
        R.PRICE.acc.pthLiq += appr * lqs


def pth_left(R, a):
    a.pthTenure = 0


# ------------------------------------------------------------------ the C2.2 design (13.4)
def c22_init(R, agents, seed):
    R.C22S = NS(n=0, k=0, r=0.0, b=0)
    if (R.C22.get('u') or 0) > 0:
        raise NotImplementedError('c22.u')
    if R.C22.get('auto'):
        for a in agents:
            if not a._inel:
                a.inCCO = True


def c22_tally(R, a, p, Y, A_):
    S = R.C22S
    c2N = A_.mlc * (a._hhC22 if A_.HHA else Y.c22Cur)
    c2B = 12 * A_.buA if (p['ccoOn'] and a.inCCO and p['bu'] > 0 and not R.PATHWAY_OFF['relief']) else 0
    S.n += 1
    if c2B > 0:
        S.b += 1
    if c2B >= c2N * (1 - 1e-9):
        S.k += 1
    S.r += min(1, c2B / c2N) if c2N > 0 else 1


def c22_res(R, out, g, n):
    S = R.C22S
    out['c22PY'] = S.k / S.n * 100 if (S and S.n) else 0
    out['c22R'] = S.r / S.n * 100 if (S and S.n) else 0
    out['buPY'] = S.b / S.n * 100 if (S and S.n) else 0
    out['elN'] = g['k'] / max(1, n) * 100
    out['elF0'] = g['f0']
    out['elW'] = g['wp']
    out['elRes'] = g['res']


# ------------------------------------------------------------------ year set-up: the spending layer, the production side, joining
def mult_year(R, agents, yr, recSt, popShock):
    if yr == 0 or not R.MLS:
        R.MLS = NS(push=0, y={})
    mlFill = mlLoss = mlRest = 0
    W2U = R.CFG['WAGE_TO_USD']
    if recSt.active and popShock < 1 and R.MLS.push > 0:
        mlW = 0.0
        for a in agents:
            if a.wage == a.wage and a.wage > 0:
                mlW += a.wage * 12 * W2U
        mlLoss = (1 - popShock) * mlW
        if mlLoss > 0:
            mlRest = min(mlLoss, R.S['MULT_LS'] * R.MULT['m'] * R.MLS.push)
            mlFill = mlRest / mlLoss
            popShock += (1 - popShock) * mlFill
    elif R.MULT.get('nt'):
        raise NotImplementedError('ml.nt')
    R.MLS.y[yr] = dict(fill=mlFill, loss=mlLoss, rest=mlRest, push=R.MLS.push)
    return popShock


def prod_year(R, agents, yr, p, Y):
    PDON = bool(R.PROD) and R.CONVERSION_MODEL == 'framework' and bool(p['ptf']) and R.PROD.get('cap') == 'ptf'
    Y.PDON = PDON
    Y.pdCap = 1
    Y.pdLive = 0
    if not PDON:
        return
    n = max(1, len(agents))
    if yr == 0 or not R.PDS:
        c = 0
        for a in agents:
            if a.inPTF:
                c += 1
        R.PDS = NS(c0=c / n, y={}, blk=0, borPA=0, debt=0)
    D = R.PDS
    pdK = R.SURP['K'] if R.SURP else INF
    pdA = R.SPS.capPA if (yr > 0 and R.SURP and R.SPS) else 0
    pdCap = 1 if pdK <= 0 else min(1, D.c0 + pdA / pdK)
    pdLive = 0
    for a in agents:
        if a.inPTF:
            pdLive += 1
    pdOwn = pdCap
    pdBor = 0
    if R.PROD.get('speed') == 'oneyear':
        if yr > 0 and pdK < INF and pdK > 0:
            pdCap = min(1, max(pdOwn, (pdLive + (D.blk or 0)) / n))
            pdBor = max(0, pdCap - pdOwn) * pdK
        D.blk = 0
        D.borPA = pdBor
    D.y[yr] = dict(cap=pdCap, mem=pdLive / n, own=pdOwn, bor=pdBor)
    Y.pdCap = pdCap
    Y.pdLive = pdLive


def ptf_cap_allows(R, p, Y):
    return (not p['ptfCap']) and (not Y.PDON or Y.pdLive < len(R.agents) * Y.pdCap)


def join_year(R, agents, yr, p, Y):
    if not (R.JOIN and R.CONVERSION_MODEL == 'framework' and p['ccoOn']):
        return
    C = R.CFG
    PR = R.PRICE
    if yr == 0 or not R.JNS:
        R.JNS = NS(y={}, join=0, leave=0)
        for a in agents:
            a._jnY = 0
    jnN = jnJ = jnL = 0
    if yr > 0:
        jnIdx = math.pow(1 + Y.inflRate, yr) * (PR.bIdx if PR else 1)
        jnM = C['LIVING_WAGE_ANNUAL'] * jnIdx
        jnE = 0.0
        for k in R.bu_ess():
            jnE += C['BASKET'][k] * (PR.comp[k] if PR else 1)
        if PR:
            jnE /= PR.bIdx
        jnF = C['BASKET']['food'] * (PR.comp['food'] / PR.bIdx if PR else 1)
        jnH = C['BASKET']['housing'] * (PR.comp['housing'] / PR.bIdx if PR else 1)
        jnRs = R.PTH_MODE != 'basket' or R.DISC_BASE != 'basket'
        J = R.JOIN
        for a in agents:
            jHH = Y.HHON and a._hh is not None and not a._hh.single
            ef = a._hhE if jHH else jnE
            u = 1
            jH = a._hhH if jHH else jnH
            jM = jnM * a._hhF if jHH else jnM
            jB = Y.buEff * a._hhBU if jHH else Y.buEff
            if a._inel:
                a.inCCO = False
                continue
            if p['ptf'] and (a.inPTF or R.PAS):
                if R.PTFS:
                    jnC = 1 - ptfs_cut(R, a, jHH, p, True)
                    ef = ef * jnC
                    if jnRs:
                        u = jnC
                else:
                    raise NotImplementedError('PTF_MODE')
            if p['pth'] and a.inPTH and not R.PATHWAY_OFF['pthCost']:
                if R.PTH_MODE == 'housing':
                    ef -= R.S['PTH_HOUSING_CUT'] * sx_h(R, jH) * u
                else:
                    ef *= 0.65
            use = min(12 * jB, jM * ef)
            if J['cost'] == 'none' or (R.C22 and R.C22.get('auto')):
                cost = 0
            else:
                cost = 12 * p['bu'] * (a.uCCO if isinstance(a.uCCO, (int, float)) else 1) / max(1e-9, p['partRate']) * (1 if J['cost'] == 'nominal' else jnIdx)
            want = p['bu'] > 0 and use >= cost
            if a.inCCO and not want and yr - a._jnY >= J['stay']:
                a.inCCO = False
                a._jnY = yr
                jnL += 1
            elif not a.inCCO and want:
                a.inCCO = True
                a._jnY = yr
                jnJ += 1
        if Y.HHON:
            R.hh_sync('cco')
    for a in agents:
        if a.inCCO:
            jnN += 1
    R.JNS.join += jnJ
    R.JNS.leave += jnL
    R.JNS.y[yr] = dict(part=jnN / max(1, len(agents)), join=jnJ, leave=jnL)


# ------------------------------------------------------------------ the framework model: project hiring and ESP payroll at the year's start
def pj_new_acc():
    return dict(pool=0.0, gift=0.0, exp=0.0, alloc=0.0, carry=0.0, conv=0.0, giftConv=0.0, gross=0.0, net=0.0, giftNet=0.0, hrs=0.0, disp=0.0, work=0, partY=0, rc=0.0, rcN=0, overCap=0, unwilling=0)


def es_new_acc():
    return dict(accBU=0.0, ownBU=0.0, poolPaid=0.0, alloc=0.0, conv=0.0, ret=0.0, retNon=0.0, retPar=0.0, retCap=0.0, retWage=0.0, retNet=0.0, gross=0.0, tax=0.0, prem=0.0, rateXbu=0.0,
                wkY=0, wkY1=0, wage=0.0, partWkY=0, tk=0, capBind=0, maxShare=0.0, sv=0.0)


def sp_new_acc():
    return dict(pool=0.0, own=0.0, ptf=0.0, rest=0.0, pricePool=0.0, cut=0.0, cutN=0.0, cutP=0.0, freed=0.0, cash=0.0, carry=0.0, profit=0.0, profitN=0.0, reinv=0.0, wkY=0, wkY1=0,
                d1=0.0, n1=0, d2=0.0, n2=0, non=0.0, yrs=0)


def fw_year_start(R, agents, yr, p, Y):
    C = R.CFG
    PR = R.PRICE
    FW = R.FW
    W2U = C['WAGE_TO_USD']
    FWON = Y.FWON
    if FWON:
        if yr == 0 or not R.FWS:
            R.FWS = NS(prev=None)
        R.FWS.next = NS(bizBU=0.0, projBU=0.0, expiredBU=0.0, destroyedBU=0.0, wSum=0.0, pwSum=0.0, projAlloc=0.0, projGross=0.0, projTax=0.0, projNet=0.0, projLost=0.0, bizPaid=0.0, bizBUptf=None)
    PJON = bool(R.PROJ)
    Y.PJON = PJON
    Y.pjPay = 0
    Y.pjIdx = 1
    Y.pjCipB = 1
    Y.pjFg = 0
    if PJON:
        P = R.PROJ
        if yr == 0 or not R.PJS:
            R.PJS = NS(prev=None, acc=pj_new_acc())
        R.PJS.next = NS(pool=0.0, gpool=0.0)
        Y.pjIdx = math.pow(1 + Y.inflRate, yr) * (PR.bIdx if PR else 1)
        Y.pjPay = P['pay'] * Y.pjIdx
        Y.pjCipB = (1 + p['cipDemo'] * 0.12) if p['cip'] else 1.0
        pjP = []
        pjWt = 0.0
        pjWR = 0.0
        prev = R.PJS.prev
        pjIn = prev.pool + prev.gpool if prev else 0
        pjCarry = 0
        Y.pjFg = prev.gpool / pjIn if pjIn > 0 else 0
        if p['ccoOn']:
            for a in agents:
                if not a.inCCO:
                    continue
                if a._ret and (R.LF_SCOPE and a._lf and R.LF_SCOPE.get('conv') == 'none'):
                    a._pjBU = 0
                    if a._pjR is None:
                        a._pjR = 0
                    if a._pjRu is None:
                        a._pjRu = 0
                    continue
                r = pj_own_rate(R, a, p, Y.ptfConvBonus)
                cap = 12 * FW['octaveCapBase'] * math.pow(2, a.octave)
                w = cap * max(0, a.quality)
                if R.POS:
                    R.POS.bn += po_bonus(R, a, p, Y.ptfConvBonus) - 1
                    R.POS.bc += 1
                a._pjR = r
                a._pjCap = cap
                a._pjW = w
                a._pjBU = 0
                pjWt += w
                pjWR += w * r
                pjP.append(a)
        pjRc = pjWR / pjWt if pjWt > 0 else 1
        pjSet = []
        acc = R.PJS.acc
        acc['rc'] += pjRc
        acc['rcN'] += 1
        for a in pjP:
            if P['rate'] != 'max':
                raise NotImplementedError('PROJ.rate')
            ru = max(a._pjR, pjRc)
            v = Y.pjPay * ru * (1 - pj_tax(R, p, ru)) * Y.pjCipB
            h = a.wage * 12 * W2U / P['hrsYr']
            a._pjRu = ru
            a._pjWill = v > (0 if a._ret else h)
            if P['alloc'] == 'capqAll' or a._pjWill:
                pjSet.append(a)
        if pjIn > 0 and pjSet:
            if P['alloc'] in ('low', 'equal'):
                raise NotImplementedError('PROJ.alloc')
            pjS = 0.0
            for a in pjSet:
                pjS += a._pjW
            if pjS > 0:
                for a in pjSet:
                    a._pjBU = pjIn * a._pjW / pjS
            else:
                pjCarry = pjIn
        else:
            pjCarry = pjIn
        for a in pjP:
            if a._pjBU > 0:
                acc['alloc'] += a._pjBU / Y.pjIdx
                acc['work'] += 1
                if not a._pjWill:
                    acc['unwilling'] += 1
        acc['carry'] = pjCarry / Y.pjIdx
        R.PJS.next.pool += pjCarry * (1 - Y.pjFg)
        R.PJS.next.gpool += pjCarry * Y.pjFg
        acc['partY'] += len(pjP)
        if yr == 0 and P['giftMode'] == 'forward' and P['gift'] > 0:
            R.PJS.next.gpool += P['gift'] * len(pjP)
            acc['gift'] += P['gift'] * len(pjP)
            acc['pool'] += P['gift'] * len(pjP)
        if yr == 1 and P['giftMode'] == 'holder':
            raise NotImplementedError('gift holder')
    ESON = FWON and bool(R.ESP)
    Y.ESON = ESON
    Y.esIdx = 1
    Y.esCipB = 1
    if ESON:
        E = R.ESP
        if yr == 0 or not R.ESS:
            R.ESS = NS(prev=None, acc=es_new_acc(), y={}, wW=0.0, next=None)
        Y.esIdx = math.pow(1 + Y.inflRate, yr) * (PR.bIdx if PR else 1)
        Y.esCipB = (1 + p['cipDemo'] * 0.12) if p['cip'] else 1.0
        esA = R.ESS.acc
        esPool = R.ESS.prev.pool if R.ESS.prev else 0
        esW = 0.0
        esRet = 0.0
        esSv = 0.0
        esY = dict(pool=esPool, conv=0.0, ret=0.0, sv=0.0)
        R.ESS.y[yr] = esY
        GOLD = R.S['ESP_GOLD']
        for i, a in enumerate(agents):
            if a._esU is None:
                a._esU = math.fmod((i + 1) * GOLD, 1)
            if E['work'] == 'all':
                wk = True
            elif E['work'] == 'ptf':
                wk = bool(p['ptf'] and a.inPTF)
            else:
                wk = a._esU < E['work']
            a._esWk = wk and not a._ret
            a._esBU = 0
            a._esC = 0
            a._esX = 0
            a._esR = 0
            if a._esWk:
                esW += max(0, a._fwW or 0)
        R.ESS.wW = esW
        esA['poolPaid'] += esPool / Y.esIdx
        PJ = R.PROJ
        for a in agents:
            if not a._esWk and not ((a._esSv or 0) > 0):
                continue
            w = max(0, a._fwW or 0)
            sh = 0
            bu = 0
            if a._esWk:
                esA['wkY'] += 1
                if yr > 0:
                    esA['wkY1'] += 1
                    esA['wage'] += w / Y.esIdx
                if esPool > 0 and esW > 0:
                    sh = esPool * w / esW
                    bu = min(sh, w)
                    if sh > bu:
                        esRet += sh - bu
                        esA['retWage'] += (sh - bu) / Y.esIdx
                    if w > 0:
                        esA['maxShare'] = max(esA['maxShare'], bu / w)
                a._esBU = bu
                esA['alloc'] += bu / Y.esIdx
            if not (p['ccoOn'] and a.inCCO):
                esRet += bu
                esA['retNon'] += bu / Y.esIdx
                continue
            if a._esWk:
                esA['partWkY'] += 1
            r = pj_own_rate(R, a, p, Y.ptfConvBonus)
            tx = pj_tax(R, p, r)
            ok = r > FW['bizRate'] if E['take'] == 'biz' else r * (1 - tx) * Y.esCipB > 1
            if not ok:
                esRet += bu
                esA['retPar'] += bu / Y.esIdx
                continue
            if E['cap'] == 'save':
                raise NotImplementedError('ESP.cap save')
            have = bu
            cap = INF if E['cap'] == 'none' else max(0, 12 * FW['octaveCapBase'] * math.pow(2, a.octave) - (((a._pjBU or 0) + (a._pjSaved or 0)) if PJ else 0))
            c = min(have, cap)
            a._esK = cap
            if have > c + 1e-9:
                esA['capBind'] += 1
                esRet += have - c
                esA['retCap'] += (have - c) / Y.esIdx
            if c > 0:
                a._esC = c
                a._esR = r
                a._esX = c * (r * (1 - tx) * Y.esCipB - 1) / w if w > 0 else 0
                esA['tk'] += 1
        esY['ret'] = esRet
        esY['sv'] = esSv
        esA['ret'] += esRet / Y.esIdx
        esA['sv'] = esSv / Y.esIdx
        for a in agents:
            esY['conv'] += a._esC
        if esRet > 0 and R.FWS.prev:
            esBT = p['tax'] * (1 - p['cipDemo'] * 0.18) if p['cip'] else p['tax']
            esTR = min(C['PROG_TAX_MAX'], esBT + max(0, (FW['bizRate'] - C['PROG_PIVOT']) * C['PROG_RATE']))
            esTP = min(C['PROG_TAX_MAX'], esBT)
            esRG = esRet * (FW['bizCap'] * FW['bizRate'] + (1 - FW['bizCap']))
            esRT = esRet * (FW['bizCap'] * FW['bizRate'] * esTR + (1 - FW['bizCap']) * esTP)
            esRN = 0 if R.PATHWAY_OFF['conversion'] else esRG - esRT - esRet
            R.FWS.prev.bizNet += esRN
            esA['retNet'] += esRN / Y.esIdx
            if Y.tbY:
                R.TB.cur.ctax += esRT


# ------------------------------------------------------------------ the ESP surplus split (6.7)
def surp_year(R, agents, yr, p, Y):
    C = R.CFG
    PR = R.PRICE
    SPON = Y.FWON and bool(R.SURP)
    Y.SPON = SPON
    Y.spDelta = 0
    Y.spProfW = 0
    Y.spRestW = 0
    Y.spOwnW = 0
    if not SPON:
        return
    SU = R.SURP
    if yr == 0 or not R.SPS:
        R.SPS = NS(capPA=0.0, cap=0.0, carry=0.0, carryP=0.0, sw=-1, acc=sp_new_acc(), y={}, carryV=None)
    S = R.SPS
    spIdx = math.pow(1 + Y.inflRate, yr) * (PR.bIdx if PR else 1)
    Y.spIdx = spIdx
    spA = S.acc
    spN = len(agents)
    FP = R.FWS.prev
    spPool = FP.bizNet if FP else 0
    if SU['priv'] in ('owners', 'prices'):
        spS = ((FP.bizBUptf or 0) / FP.bizBU) if (FP and FP.bizBU > 0) else 0
    else:
        spS = 1
    PDON = Y.PDON
    if yr == 0:
        spPh = 1
    elif SU.get('swYear') is not None:
        spPh = 2 if yr >= SU['swYear'] else 1
    else:
        spPh = 2 if ((SU['K'] <= 0 or R.PDS.c0 + S.capPA / SU['K'] >= 1) if PDON else S.capPA >= SU['K']) else 1
    if spPh == 2 and S.sw < 0:
        S.sw = yr
    spSh = SU['p1'] if spPh == 1 else SU['p2']
    spPtf = spPool * spS
    spOwn = spPool - spPtf
    spChD = spChI = 0.0
    spChDue = None
    if PDON and R.PROD.get('speed') == 'oneyear':
        D = R.PDS
        PCD = R.S['PROD_CAP_DEP']
        PCI = R.S['PROD_CAP_INT']
        spChDue = (D.borPA or 0) * (PCD + PCI) * spN * spIdx + (D.debt or 0) * spIdx
        spChPd = min(spPtf, spChDue)
        D.debt = (spChDue - spChPd) / spIdx
        spPtf -= spChPd
        spChD = spChPd * PCD / (PCD + PCI)
        spChI = spChPd - spChD
        if Y.tbY:
            R.TB.cur.conv += spChPd
            R.TB.cur.convM += spChD
        if PR and PR.acc:
            PR.acc.conv += spChPd
        spA['chD'] = spA.get('chD', 0) + spChD / spIdx
        spA['chI'] = spA.get('chI', 0) + spChI / spIdx
    spRest = spPtf * max(0, 1 - spSh[0] - spSh[1] - spSh[2])
    spCarryIn = S.carry
    spPP = spPtf * spSh[0] + (spPtf * spSh[1] if SU['rv'] == 'price' else 0) + S.carry
    spRv = 0 if SU['rv'] == 'price' else spPtf * spSh[1]
    spPr = spPtf * spSh[2] + S.carryP
    S.carryP = 0
    spCust = ('ptf' if SU['priv'] in ('owners', 'prices') else 'all') if SU['cust'] == 'auto' else SU['cust']
    spVOn = SU['priv'] == 'prices'
    spVW = spVP = spVSum = spVUsed = 0.0
    if spVOn:
        if S.carryV is None:
            S.carryV = 0
        spVW = 0 if SU['privWk'] == 'none' else spOwn * spSh[2]
        spVP = spOwn - spVW + S.carryV
        spPr += spVW
        spOwn = 0
    spMlc = C['LIVING_WAGE_ANNUAL'] * math.pow(1 + Y.inflRate, yr)
    if PR:
        spMlc *= PR.bIdx
    spSum = spWW = spWO = 0.0
    if not Y.ESON:
        raise NotImplementedError('SURP without ESP')
    PTH_CUT = R.S['PTH_HOUSING_CUT']
    POFF = R.PATHWAY_OFF
    HHON = Y.HHON
    for a in agents:
        bp = p['ccoOn'] and a.inCCO and p['bu'] > 0 and not POFF['relief']
        spPw = bool(R.PAS) and (spCust == 'ptf' or (spCust == 'pp' and not (p['ccoOn'] and a.inCCO)))
        isC = spCust == 'all' or (spCust == 'pp' and ((p['ccoOn'] and a.inCCO) or (p['ptf'] and (a.inPTF or R.PAS)))) or (spCust == 'ptf' and p['ptf'] and (a.inPTF or R.PAS)) or (spCust == 'part' and p['ccoOn'] and a.inCCO)
        e = 0
        sHH = HHON and a._hh is not None and not a._hh.single
        sE = a._hhE if sHH else Y.eShareCur
        sH = a._hhH if sHH else Y.hShareCur
        sM = spMlc * a._hhF if sHH else spMlc
        if isC:
            ef = sE
            u = 1
            if p['ptf'] and (a.inPTF or R.PAS):
                if R.PTFS:
                    spC = 1 - ptfs_cut(R, a, sHH, p, True, spPw)
                    ef = ef * spC
                    u = spC
                else:
                    raise NotImplementedError('PTF_MODE')
            if p['pth'] and a.inPTH and not POFF['pthCost']:
                if R.PTH_MODE == 'housing':
                    ef -= PTH_CUT * sx_h(R, sH) * u
                else:
                    ef *= 0.65
            e = sM * ef
            if SU['bu'] == 'cash':
                raise NotImplementedError('SURP.bu cash')
            if spPw:
                e *= pa_w(R, a)
        if spVOn:
            if R.PAS:
                vBu = max(0, a._spBU or 0) * (1 - pa_w(R, a)) if bp else 0
            else:
                vBu = max(0, a._spBU or 0) if (bp and not (p['ptf'] and a.inPTF)) else 0
            vE = 0
            if vBu > 0:
                vE = sE
                if p['pth'] and a.inPTH and not POFF['pthCost']:
                    if R.PTH_MODE == 'housing':
                        vE -= PTH_CUT * sH
                    else:
                        vE *= 0.65
                vE *= sM
                if R.PAS:
                    vE *= 1 - pa_w(R, a)
            a._spVw = vBu
            a._spVE = vE
            spVSum += vBu
        a._spE = e
        a._spPw = spPw
        a._spCutY = 0
        a._spPay = 0
        a._spOwn = 0
        a._spBU = 0
        a._spWk = bool(a._esWk) and (SU['wk'] != 'espPart' or bool(p['ccoOn'] and a.inCCO))
        spSum += e
        if a._spWk:
            spWW += max(0, a._fwW or 0)
        spWO += sp_base(R, a)
    spDelta = min(1, spPP / spSum) if spSum > 0 else 0
    spUsed = spDelta * spSum
    S.carry = spPP - spUsed
    if spVOn:
        for a in agents:
            a._spV = min(spVP * a._spVw / spVSum, a._spVE) if (spVSum > 0 and a._spVw > 0) else 0
            spVUsed += a._spV
        S.carryV = spVP - spVUsed
    spProfW = 0
    if spWW > 0:
        spProfW = spPr / spWW
    else:
        S.carryP = spPr
        spPr = 0
    spRestOn = spRest > 0 and FP and FP.wSum > 0
    spRestW = max(0, spRest) / FP.wSum if spRestOn else 0
    spOwnW = 0
    if spWO > 0:
        spOwnW = spOwn / spWO
    else:
        S.carry += spOwn
        spOwn = 0
    for a in agents:
        w = a._fwW or 0
        a._spOwn = spOwnW * sp_base(R, a)
        a._spRest = spRest * w / FP.wSum if spRestOn else 0
        a._spPay = (spPr * max(0, w) / spWW if (a._spWk and spWW > 0) else 0) + a._spRest + a._spOwn
    S.cap += spRv
    S.capPA += spRv / spIdx / spN
    if Y.tbY:
        R.TB.cur.conv += spRv
        if R.PROD:
            R.TB.cur.convM += spRv
    if PR and PR.acc:
        PR.acc.conv += spRv
    spA['pool'] += spPool / spIdx
    spA['own'] += spOwn / spIdx
    if spVOn:
        spA['privW'] = spA.get('privW', 0) + spVW / spIdx
        spA['privP'] = spA.get('privP', 0) + (spVP - S.carryV) / spIdx
    spA['ptf'] += spPtf / spIdx
    spA['rest'] += spRest / spIdx
    spA['pricePool'] += (spPP - spCarryIn) / spIdx
    spA['reinv'] += spRv / spIdx
    spA['carry'] = S.carry / spIdx
    if yr > 0:
        if spPh == 1:
            spA['d1'] += spDelta
            spA['n1'] += 1
        else:
            spA['d2'] += spDelta
            spA['n2'] += 1
        spA['yrs'] += 1
    S.y[yr] = dict(pool=spPool, s=spS, own=spOwn, ptf=spPtf, rest=spRest, carryIn=spCarryIn, pp=spPP, sum=spSum, delta=spDelta, used=spUsed, carryOut=S.carry, profit=spPr, reinv=spRv,
                   cap=S.cap, capPA=S.capPA, phase=spPh, cut=0.0, freed=0.0, paid=0.0, pjFreed=0.0, privW=spVW, privPool=spVP, privUsed=spVUsed, cutV=0.0, ch=spChD + spChI, chDue=spChDue if spChDue is not None else 0)
    Y.spDelta = spDelta
    Y.spProfW = spProfW
    Y.spRestW = spRestW
    Y.spOwnW = spOwnW


def sp_base(R, a):
    if R.SURP.get('own') == 'eq' and a._rt:
        return max(0, a._rt.r[2] + a._rt.r[3])
    return max(0, a.wealth)


# ------------------------------------------------------------------ per adult: the gate, BU purchases, project hours, payouts, conversion, octaves
def gate_current(R, a, p, Y, A_):
    C = R.CFG
    gEss = A_.eSA
    HHA = A_.HHA
    if p['ptf'] and (a.inPTF or R.PAS):
        if not R.PTFS:
            raise NotImplementedError('PTF_MODE')
        gEss = gEss * (1 - ptfs_cut(R, a, HHA, p, True))
    if p['pth'] and a.inPTH and not R.PATHWAY_OFF['pthCost']:
        if R.PTH_MODE == 'housing':
            m = (1 - ptfs_cut(R, a, HHA, p, True)) if (p['ptf'] and (a.inPTF or R.PAS) and R.PTFS) else 1
            gEss -= R.S['PTH_HOUSING_CUT'] * sx_h(R, A_.hSA) * m
        else:
            gEss *= 0.65
    gCost = C['LIVING_WAGE_ANNUAL'] * math.pow(1 + Y.inflRate, Y.yr)
    if R.PRICE:
        gCost *= R.PRICE.bIdx
    if HHA:
        gCost *= a._hhF
    a._fwBUm = min(12 * A_.buA, gCost * gEss) / 12


def bu_purchase(R, a, p, Y, A_):
    HHA = A_.HHA
    essF = A_.eSA
    if p['ptf'] and (a.inPTF or R.PAS):
        if not R.PTFS:
            raise NotImplementedError('PTF_MODE')
        essF = essF * (1 - ptfs_cut(R, a, HHA, p, True))
    if p['pth'] and a.inPTH and not R.PATHWAY_OFF['pthCost']:
        if R.PTH_MODE == 'housing':
            essF -= R.S['PTH_HOUSING_CUT'] * sx_h(R, A_.hSA) * A_.rsPtfU
        else:
            essF *= 0.65
    mlc = A_.mlc
    fwBudget = 12 * A_.buA
    fwB = min(fwBudget, mlc * essF)
    spC = 0
    fwB0 = fwB
    if Y.tbY:
        R.TB.cur.buIss += fwBudget
    SPON = Y.SPON
    S = R.SPS
    yr = Y.yr
    if SPON and a._spE > 0 and Y.spDelta > 0:
        spE = mlc * essF
        if R.SURP['bu'] == 'cash':
            raise NotImplementedError('SURP.bu cash')
        spC = Y.spDelta * a._spE if a._spPw else Y.spDelta * spE
        fwB = min(fwBudget, spE - spC)
        a._spCutY = spC
        spY = S.y[yr]
        spY['cut'] += spC
        spY['freed'] += fwB0 - fwB
        ac = S.acc
        ac['cut'] += spC / Y.spIdx
        ac['cutP'] += spC / Y.spIdx
        ac['freed'] += (fwB0 - fwB) / Y.spIdx
        ac['cash'] += (spC - (fwB0 - fwB)) / Y.spIdx
    if SPON and (a._spV or 0) > 0:
        vSpE = mlc * essF
        vC = min(a._spV, max(0, vSpE - spC))
        vB = fwB
        if vC > 0:
            spC += vC
            fwB = min(fwBudget, vSpE - spC)
            a._spCutY = spC
            vY = S.y[yr]
            vY['cut'] += vC
            vY['cutV'] += vC
            vY['freed'] += vB - fwB
            ac = S.acc
            ac['cut'] += vC / Y.spIdx
            ac['cutP'] += vC / Y.spIdx
            ac['cutV'] = ac.get('cutV', 0) + vC / Y.spIdx
            ac['freed'] += (vB - fwB) / Y.spIdx
            ac['cash'] += (vC - (vB - fwB)) / Y.spIdx
    fwLeft = fwBudget - fwB
    cf = A_.cfPreCCO + 0 - fwB / mlc
    if spC:
        cf -= spC / mlc
    a._fwBUm = fwB0 / 12
    FN = R.FWS.next
    if SPON:
        a._spBU = fwB
        if R.PAS:
            FN.bizBUptf = (FN.bizBUptf or 0) + fwB * pa_w(R, a)
        elif p['ptf'] and a.inPTF:
            FN.bizBUptf = (FN.bizBUptf or 0) + fwB
    if SPON and Y.PJON:
        S.y[yr]['pjFreed'] += (fwB0 - fwB) * R.PROJ['share']
    FW = R.FW
    FN.bizBU += fwB
    FN.expiredBU += fwLeft
    FN.projBU += fwLeft * FW['directedShare']
    FN.destroyedBU += fwLeft * (1 - FW['directedShare'])
    if Y.PJON:
        R.PJS.next.pool += fwLeft * R.PROJ['share']
        R.PJS.acc['exp'] += fwLeft / Y.pjIdx
        R.PJS.acc['pool'] += fwLeft * R.PROJ['share'] / Y.pjIdx
    A_.cf = cf
    A_.fwB = fwB
    A_.fwLeft = fwLeft


def bu_no_purchase_cut(R, a, p, Y, A_):
    """A customer without BU saves the split's cut in cash (never reached under the C2.2 design: everyone holds BU)."""
    if Y.SPON and (a._spE or 0) > 0 and Y.spDelta > 0:
        raise NotImplementedError('split cut without BU')


def project_hours(R, a, p, Y, A_):
    a._pjHW = 0
    if (a._pjBU or 0) > 0:
        P = R.PROJ
        pjH = a._pjBU / Y.pjPay
        pjHw = a.wage * 12 * R.CFG['WAGE_TO_USD'] * A_.incomeShock / P['hrsYr'] * 1
        pjD = pjH * pjHw
        if P['hours'] == 'displace':
            raise NotImplementedError('PROJ.hours displace')
        a._pjHW = pjD
        R.PJS.acc['hrs'] += pjH
        R.PJS.acc['disp'] += 0 / Y.pjIdx


def fw_payouts(R, a, p, Y, A_):
    a._fwPayY = 0
    FP = R.FWS.prev
    ann = A_.annualWageUSD
    if FP and FP.wSum > 0:
        fwPay = FP.bizNet * (a._fwW or 0) / FP.wSum
        if Y.ESON and R.ESP.get('rest') == 'esp':
            raise NotImplementedError('ESP.rest esp')
        if Y.SPON:
            S = R.SPS
            fwPay = a._spPay
            S.y[Y.yr]['paid'] += fwPay
            S.acc['profit'] += (fwPay - a._spOwn - a._spRest) / Y.spIdx
            if not a.inCCO:
                S.acc['non'] += fwPay / Y.spIdx
            if a._spWk and Y.yr > 0:
                S.acc['wkY1'] += 1
                S.acc['profitN'] += (fwPay - a._spOwn - a._spRest) / Y.spIdx
        a.wealth += fwPay
        a.yrConvUSD += fwPay
        A_.yrCashSurplus += fwPay
        R.FWS.next.bizPaid += fwPay
        a._fwPayY = fwPay
        if R.PRICE:
            R.PRICE.acc.conv += fwPay
    if Y.ESON:
        a._esPrY = 0
        if a._esC > 0:
            esTx = pj_tax(R, p, a._esR)
            esG = 0 if R.PATHWAY_OFF['conversion'] else a._esC * a._esR * Y.esCipB * A_.incomeShock
            esPr = 0 if R.PATHWAY_OFF['conversion'] else esG * (1 - esTx) - a._esC
            a.wealth += esPr
            a.yrConvUSD += esPr
            A_.yrCashSurplus += esPr
            a._esPrY = esPr
            a._esShk = A_.incomeShock
            if Y.tbY:
                R.TB.cur.ctax += esG * esTx
            ea = R.ESS.acc
            ea['conv'] += a._esC / Y.esIdx
            ea['gross'] += esG / Y.esIdx
            ea['tax'] += esG * esTx / Y.esIdx
            ea['prem'] += esPr / Y.esIdx
            ea['rateXbu'] += a._esR * a._esC / Y.esIdx
            if R.PRICE:
                R.PRICE.acc.conv += esPr
    a._fwW = ann
    R.FWS.next.wSum += ann


def fw_participant(R, a, p, Y, A_):
    C = R.CFG
    if p['cip'] and A_.uCipQuality < p['cipDemo'] * 0.15:
        a.quality = min(p['maxMult'], a.quality + 0.1)
    capBU = 12 * R.FW['octaveCapBase'] * math.pow(2, a.octave)
    if R.POS:
        ptfBF = po_bonus(R, a, p, Y.ptfConvBonus)
        if not R.PROJ:
            R.POS.bn += ptfBF - 1
            R.POS.bc += 1
    if R.FWS.prev and R.FWS.prev.pwSum > 0 and not Y.PJON:
        raise NotImplementedError('N2 allocation')
    a._fwPW = capBU * max(0, a.quality)
    R.FWS.next.pwSum += a._fwPW
    if a.octave < p['maxOct']:
        YusdF = a.wage * C['WAGE_TO_USD']
        cBasicF = (A_.dcA * A_.cfPreCCO) / 12
        edcF = C['FBS_EDC_RESIDUAL_PTH'] if (p['pth'] and a.inPTH) else C['FBS_EDC_RESIDUAL_BASE']
        fbsF = max(0, YusdF + A_.buA - cBasicF - edcF * YusdF) / (Y.priceIdx if (R.AUD and R.AUD.get('fbs')) else 1)
        lamF = a.lam
        if p['cip']:
            lamF *= (1 + p['cipDemo'] * C['FBS_CIP_LAMBDA_BOOST'])
        if A_.uAdvance < 1 - math.exp(-lamF * fbsF) and not R.PATHWAY_OFF['octave'] and not R.OCT:
            a.octave += 1
    HHA = A_.HHA
    if A_.uSzhInduce < Y.szhPartBoost and not a.inPTF and p['ptf'] and not (HHA and not a._hhHead) and ptf_cap_allows(R, p, Y):
        a.inPTF = A_.uSzhPtfShare < p['ptfShare']
        if a.inPTF and Y.PDON:
            Y.pdLive += 1
    elif Y.PDON and R.PROD.get('speed') == 'oneyear' and A_.uSzhInduce < Y.szhPartBoost and not a.inPTF and p['ptf'] and not (HHA and not a._hhHead) and A_.uSzhPtfShare < p['ptfShare'] and not p['ptfCap']:
        R.PDS.blk += 1


def project_convert(R, a, p, Y, A_):
    P = R.PROJ
    pjA = R.PJS.acc
    if P['cap']:
        raise NotImplementedError('PROJ.cap')
    pjCapR = INF
    pjE = (a._pjSaved or 0) + (a._pjBU or 0)
    pjC1 = min(pjE, pjCapR)
    a._pjSaved = pjE - pjC1
    pjCapR -= pjC1
    pjGh = a._pjGiftH or 0
    pjC2 = min(pjGh, pjCapR)
    a._pjGiftH = pjGh - pjC2
    rvR = a._pjRu
    pjTx = pj_tax(R, p, rvR)
    sh = A_.incomeShock
    pjG1 = 0 if R.PATHWAY_OFF['conversion'] else pjC1 * rvR * Y.pjCipB * sh
    pjN1 = pjG1 * (1 - pjTx)
    pjTg = pj_tax(R, p, a._pjR)
    pjG2 = 0 if R.PATHWAY_OFF['conversion'] else pjC2 * a._pjR * Y.pjCipB * sh
    pjN2 = pjG2 * (1 - pjTg)
    if R.PROD and Y.FWON:
        pdH = pjC1 / Y.pjPay
        pdV = pdH * (Y.pjPay if R.PROD['match'] == 'face' else a.wage * 12 * R.CFG['WAGE_TO_USD'] * sh / P['hrsYr']) * (1 + (R.PROD.get('mat') or 0))
        a._pdM = max(0, pjN1) if R.PROD['match'] == 'market' else min(max(0, pjN1), pdV)
        a._pdMy = a._pdM
        a._pdNy = pjN1
        a._pdVy = pdV
    if Y.tbY:
        R.TB.cur.ctax += pjG1 * pjTx + pjG2 * pjTg
    a.wealth += pjN1 + pjN2
    a.yrConvUSD += pjN1 + pjN2
    A_.yrCashSurplus += pjN1 + pjN2
    if R.LABOR and pjN2:
        a._labCn = (a._labCn or 0) + pjN2
    a.yrPjGift = pjN1 * Y.pjFg + pjN2
    if R.PRICE:
        R.PRICE.acc.conv += pjN1 + pjN2
    pjA['conv'] += pjC1 / Y.pjIdx
    pjA['giftConv'] += pjC2 / Y.pjIdx
    pjA['gross'] += (pjG1 + pjG2) / Y.pjIdx
    pjA['net'] += pjN1 / Y.pjIdx
    pjA['giftNet'] += pjN2 / Y.pjIdx
    if a.wealth != a.wealth:
        a.wealth = 0


# ------------------------------------------------------------------ year close: businesses convert the BU they accepted
def fw_year_end(R, agents, yr, p, Y):
    if Y.FWON:
        C = R.CFG
        FW = R.FW
        nx = R.FWS.next
        bTaxB = p['tax'] * (1 - p['cipDemo'] * 0.18) if p['cip'] else p['tax']
        taxR = min(C['PROG_TAX_MAX'], bTaxB + max(0, (FW['bizRate'] - C['PROG_PIVOT']) * C['PROG_RATE']))
        taxP = min(C['PROG_TAX_MAX'], bTaxB)
        bzB = nx.bizBU * (1 - R.ESP['lam']) if Y.ESON else nx.bizBU
        nx.bizGross = bzB * (FW['bizCap'] * FW['bizRate'] + (1 - FW['bizCap']))
        nx.bizTax = bzB * (FW['bizCap'] * FW['bizRate'] * taxR + (1 - FW['bizCap']) * taxP)
        nx.bizNet = 0 if R.PATHWAY_OFF['conversion'] else nx.bizGross - nx.bizTax - bzB
        if Y.tbY:
            R.TB.cur.ctax += nx.bizTax
        if Y.ESON:
            R.ESS.next = NS(pool=nx.bizBU * R.ESP['lam'])
            ea = R.ESS.acc
            ea['accBU'] += nx.bizBU / Y.esIdx
            ea['ownBU'] += bzB / Y.esIdx
            ey = R.ESS.y[yr]
            ey['acc'] = nx.bizBU
            ey['own'] = bzB
            ey['poolNext'] = R.ESS.next.pool
        R.FWS.prev = nx
    if Y.ESON:
        R.ESS.prev = R.ESS.next
    if Y.PJON:
        R.PJS.prev = R.PJS.next


# ------------------------------------------------------------------ the programme parts' keys
PJ_KEYS = ['pjNet', 'pjGift', 'pjBU', 'pjExp', 'pjHrs', 'pjDisp', 'pjWork', 'pjRc', 'pjSaved']
ES_KEYS = ['esBUW', 'esShare', 'esRate', 'esCapB', 'esConv', 'esRet']
SP_KEYS = ['spPool', 'spOwn', 'spPtfS', 'spCut', 'spCutN', 'spFreed', 'spCash', 'spProfit', 'spProfW', 'spReinv', 'spRest', 'spCap', 'spSw', 'spD1', 'spD2', 'spNon', 'spCarry']
PD_KEYS = ['pdC5', 'pdC10', 'pdC19', 'pdMem19']
JN_KEYS = ['jnP5', 'jnP10', 'jnP19', 'jnJoin', 'jnLeave']


def prog_results(R, r, L, T, n, NY):
    PJ = R.PJS if (R.PROJ and R.PJS) else None
    A = PJ.acc if PJ else None

    def pjQ(k):
        return A[k] / A['partY'] if (A and A['partY'] > 0) else 0
    pjSv = 0.0
    if A and A['partY'] > 0:
        for a in R.agents:
            pjSv += (a._pjSaved or 0) + (a._pjGiftH or 0)
        pjSv /= max(1, A['partY'] / T)
    r['pjNet'] = pjQ('net')
    r['pjGift'] = pjQ('giftNet')
    r['pjBU'] = pjQ('alloc')
    r['pjExp'] = pjQ('exp')
    r['pjHrs'] = pjQ('hrs')
    r['pjDisp'] = pjQ('disp')
    r['pjWork'] = pjQ('work') * 100
    r['pjRc'] = A['rc'] / A['rcN'] if (A and A['rcN']) else 0
    r['pjSaved'] = pjSv
    esOn = bool(R.ESP and R.ESS and R.CONVERSION_MODEL == 'framework')
    eA = R.ESS.acc if esOn else None
    r['esBUW'] = eA['alloc'] / eA['wkY1'] if (eA and eA['wkY1']) else 0
    r['esShare'] = eA['alloc'] / eA['wage'] * 100 if (eA and eA['wage'] > 0) else 0
    r['esRate'] = eA['rateXbu'] / eA['conv'] if (eA and eA['conv'] > 0) else 0
    r['esCapB'] = eA['capBind'] / eA['partWkY'] * 100 if (eA and eA['partWkY']) else 0
    r['esConv'] = eA['conv'] / L['n1'] if (eA and L['n1']) else 0
    r['esRet'] = eA['ret'] / L['n1'] if (eA and L['n1']) else 0
    spOn = bool(R.SURP and R.SPS and R.CONVERSION_MODEL == 'framework')
    sA = R.SPS.acc if spOn else None

    def spQ(k):
        return sA[k] / L['n1'] if (spOn and L['n1']) else 0
    for k in ('pool', 'own'):
        r['sp' + k[0].upper() + k[1:]] = spQ(k)
    r['spPtfS'] = sA['ptf'] / sA['pool'] * 100 if (spOn and sA['pool'] > 0) else 0
    r['spCut'] = spQ('cut')
    r['spCutN'] = spQ('cutN')
    r['spFreed'] = spQ('freed')
    r['spCash'] = spQ('cash')
    r['spProfit'] = spQ('profit')
    r['spProfW'] = sA['profitN'] / sA['wkY1'] if (spOn and sA['wkY1']) else 0
    r['spReinv'] = spQ('reinv')
    r['spRest'] = spQ('rest')
    r['spCap'] = R.SPS.capPA if spOn else 0
    r['spSw'] = (99 if R.SPS.sw < 0 else R.SPS.sw) if spOn else 0
    r['spD1'] = sA['d1'] / sA['n1'] * 100 if (spOn and sA['n1']) else 0
    r['spD2'] = sA['d2'] / sA['n2'] * 100 if (spOn and sA['n2']) else 0
    r['spNon'] = (sA['non'] + sA['cutN']) / sA['pool'] * 100 if (spOn and sA['pool'] > 0) else 0
    r['spCarry'] = sA['carry'] / n if spOn else 0

    def pdQ(y, k):
        return R.PDS.y[y][k] * 100 if (R.PROD and R.PDS and y in R.PDS.y and R.CONVERSION_MODEL == 'framework') else 0
    r['pdC5'] = pdQ(5, 'cap')
    r['pdC10'] = pdQ(10, 'cap')
    r['pdC19'] = pdQ(T - 1, 'cap')
    r['pdMem19'] = pdQ(T - 1, 'mem')
    jnOn = bool(R.JOIN and R.JNS and R.CONVERSION_MODEL == 'framework' and R.p['ccoOn'])

    def jnQ(y):
        return R.JNS.y[y]['part'] * 100 if (jnOn and y in R.JNS.y) else 0
    r['jnP5'] = jnQ(5)
    r['jnP10'] = jnQ(10)
    r['jnP19'] = jnQ(T - 1)
    r['jnJoin'] = R.JNS.join / n * 100 if jnOn else 0
    r['jnLeave'] = R.JNS.leave / n * 100 if jnOn else 0


def prog_res_parts(R, out, NY, L, grp_inel=None):
    """pthbRes, ptfsRes, paRes, poRes, c22Res (in tbRunCore's order)."""
    if R.PTHB:
        if R.PBS:
            pthb_res(R, out)
        else:
            for k in ('pbV', 'pbD', 'pbCE', 'pbME', 'pbCover', 'pbExit', 'pbCash', 'pbAprP', 'pbAprR', 'pbAprC', 'pbFill'):
                out[k] = 0
    if R.PTFS:
        A = R.PFS
        out['pfCut'] = A.cut / A.cn * 100 if (A and A.cn) else 0
        out['pfLeave'] = A.leave / A.yrs if (A and A.yrs) else 0
        out['pfMem'] = A.mem / A.yrs * 100 if (A and A.yrs) else 0
    if R.PAS:
        pa_res(R, out)
    if R.POS:
        po_res(R, out, NY, L['cost'] / NY)
    if R.C22:
        c22_res(R, out, grp_inel, len(R.agents))
