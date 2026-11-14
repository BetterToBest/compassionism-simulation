"""S69: the measures (section 9 and every part's own keys). Reporting only: nothing here moves an adult or draws a number."""
import math
from s69_engine import NS, INF
from s69_rng import median_of, quantile_of, gini_of, gini_neg, js_round


def tb_new_acc():
    return NS(pjg=0.0, n=0, cash=0.0, endow=0.0, bu=0.0, conv=0.0, convM=0.0, buIss=0.0, ctax=0.0, cutFree=0.0, cutPT=0.0, cutG=0.0, cap=0.0, pthLiq=0.0, tax=0.0, base=0.0, E=0.0,
              f0=0, f1=0.0, f2=0.0, idx=1, pd=0.0, tgt=0.0, emp=0, hrs=0.0, bR=0, bP=0, bz=0.0, es=0.0, n1=0, nP1=0, nN1=0, pyP=0.0, pyN=0.0, nWP1=0, esWP=0.0, endowV=0.0)


def tb_cash_income(R, a):
    c = _p(a.yrWageUSD) + _p(a.yrConvUSD) + _p(a.yrUbiUSD) + _p(a.yrSSUSD) + _p(a.yrTbCash)
    if R.RETURNS and R.RETURNS.get('ci'):
        c += _p(a.yrCapUSD)
    return c - a._snB if (R.SNET and R.SNS and a._snB) else c


def _p(x):
    if x is None:
        return 0
    return x if x == x else 0


def tb_account(R, a, y, yr, mlc, cf, cfPreCCO, costUSD, E, tbG, tbPT):
    C = R.TB.cur
    LWA = R.CFG['LIVING_WAGE_ANNUAL']
    idx = mlc / LWA / (a._hhF or 1)
    conv = _p(a.yrConvUSD)
    R.TB.xIdx = idx
    gw = float(a._w) if (R.GOV and R.GOV.get('wb') and a._w is not None) else 1
    C.n += 1
    C.idx = idx
    C.E += E
    C.cash += a.yrTbCash
    if R.SNET and R.SNS and a._snB:
        C.cash -= a._snB
    C.tax += gw * a.yrTax
    C.base += gw * max(0, E - y.X)
    spCut = a._spCutY or 0
    buR = max(0, mlc * (cfPreCCO - cf) - tbG - spCut)
    if a._csFree:
        C.cutFree += a._csFree
        a._csFree = 0
    if R.POS and a._poS is not None:
        R.POS.sub += a._poS / idx
        R.POS.fr += a._poF / idx
        a._poS = None
    C.bu += buR
    C.conv += conv + spCut
    if a._pdM:
        C.convM += a._pdM
        a._pdM = 0
    C.pjg += a.yrPjGift or 0
    a.yrPjGift = 0
    C.cutPT += tbPT
    C.cutG += tbG
    C.pthLiq += a._tbPthNow or 0
    pd = a.yrTbCash + 0 + buR + conv + spCut + tbPT + tbG + (a._tbPthNow or 0)
    if R.SNET and R.SNS and a._snB:
        pd -= a._snB
    C.pd += pd
    C.tgt += min(pd, max(0, mlc - E - (a.yrSSUSD or 0)))
    inc = E + conv + (a.yrUbiUSD or 0) + (a.yrSSUSD or 0) + a.yrTbCash - a.yrTax + 0
    disp = E + conv + (a.yrUbiUSD or 0) + (a.yrSSUSD or 0) + a.yrTbCash - a.yrTax
    if R.RETURNS and R.RETURNS.get('ci'):
        inc += _p(a.yrCapUSD)
        disp += _p(a.yrCapUSD)
    if a._hh:
        a._hhInc = inc
        a._hhDisp = disp
        a._hhMlc = mlc
        a._hhCost = costUSD
        a._hhIdx = idx
    if not a._hhPool:
        tb_pov(R, a, C, idx, inc, mlc, costUSD, disp)
    C.emp += 1 if E > 0 else 0
    C.hrs += ((E + a._pjHW) if a._pjHW else E) / a._lbE0 if (a._lbE0 is not None and a._lbE0 > 0) else 1
    C.bR += a._bleiR or 0
    C.bP += a._bleiP or 0
    if yr > 0:
        bzY = a._fwPayY or 0
        esY = a._esPrY or 0
        C.n1 += 1
        C.bz += bzY
        C.es += esY
        if a.inCCO:
            C.nP1 += 1
            C.pyP += bzY + esY
            if a._esWk:
                C.nWP1 += 1
                C.esWP += esY
        else:
            C.nN1 += 1
            C.pyN += bzY
    a._tbPthPrev = a._tbPthNow or 0
    a._tbPthNow = 0


def tb_pov(R, a, C, idx, inc, mlc, costUSD, disp):
    g = max(0, costUSD - inc) / mlc
    C.f0 += 1 if g > 0 else 0
    C.f1 += g
    C.f2 += g * g
    if R.WYS:
        R.WYS.cur.extend((costUSD, inc, mlc))
    a._tbGap = g
    a._tbF0 = (a._tbF0 or 0) + (1 if g > 0 else 0)
    a._tbF2 = (a._tbF2 or 0) + g * g
    a._tbRes = (a._tbRes or 0) + (inc + mlc - costUSD) / idx
    a._tbYrs = (a._tbYrs or 0) + 1
    if g > 0:
        if not a._tbInSp:
            a._tbSp = (a._tbSp or 0) + 1
        a._tbInSp = True
    else:
        a._tbInSp = False
    a._tbDisp = disp
    a._tbExt = a._tbDisp + max(0, mlc - costUSD)


# ------------------------------------------------------------------ BLEI by group (tbBleiAcc, tbBleiYear, tbBleiRes)
def blei_acc():
    return NS(py=[0] * 9, pov=[0] * 9, cri=[0] * 9, pov20=[0] * 9, n20=[0] * 9, v20=[[] for _ in range(9)], y20=[0, 0, 0])


def lf_line(R, agents, o):
    return 1 if o['lines'] == 'nominal' else agents[0].yrBasketUSD / R.CFG['LIVING_WAGE_ANNUAL'] / (agents[0]._hhF or 1)


def blei_year(R, BG, agents, p, o, last, y20):
    C = R.CFG
    lf = lf_line(R, agents, o)
    L30 = C['BLEI_PRECARIOUS_MAX']
    L7 = C['BLEI_CRISIS_MAX']
    W2U = C['WAGE_TO_USD']
    BDC = C['BASE_DAILY_COST']
    for a in agents:
        m = (a._tbM or 0) / BDC
        g2 = 1 if a._tbPart else 2
        v0 = (R.blei0(a) + m) / lf
        v1 = R.agent_blei(a, p['bu'], p['ccoOn'], p['pth'], p['szh'], p['szhCoh'], p['ptf']) / lf
        wnet = max(0, _p(a.yrWageUSD) - _p(a.yrTax)) / 12 / W2U
        v2 = (R.agent_blei(a, 0, False, False, False, 0, False, wealth=a.wealth, wage=wnet, hhD=a._hhD) + m) / lf
        v = (v0, v1, v2)
        for d in range(3):
            x = v[d]
            j0 = d * 3
            j1 = j0 + g2
            BG.py[j0] += 1
            BG.py[j1] += 1
            if x < L30:
                BG.pov[j0] += 1
                BG.pov[j1] += 1
            if x < L7:
                BG.cri[j0] += 1
                BG.cri[j1] += 1
            if last:
                BG.n20[j0] += 1
                BG.n20[j1] += 1
                if x < L30:
                    BG.pov20[j0] += 1
                    BG.pov20[j1] += 1
                BG.v20[j0].append(x)
                BG.v20[j1].append(x)
        if y20:
            BG.y20[2] += 1
            if v0 < L30:
                BG.y20[0] += 1
            if v1 < L30:
                BG.y20[1] += 1


def blei_res(R, BG, out):
    for di, d in enumerate(R.S['TB_BLEI_DEFS']):
        for gi, g in enumerate(R.S['TB_BLEI_GRPS']):
            j = di * 3 + gi
            k = 'b' + d + g
            out[k + 'Py'] = BG.pov[j] / BG.py[j] * 100 if BG.py[j] else 0
            out[k + 'Cr'] = BG.cri[j] / BG.py[j] * 100 if BG.py[j] else 0
            out[k + '20'] = BG.pov20[j] / BG.n20[j] * 100 if BG.n20[j] else 0
            out[k + 'Md'] = median_of(BG.v20[j])
    out['bNAy20'] = BG.y20[0] / BG.y20[2] * 100 if BG.y20[2] else 0
    out['bOAy20'] = BG.y20[1] / BG.y20[2] * 100 if BG.y20[2] else 0
    return out


# ------------------------------------------------------------------ the v5.2 reporting (tbRepAcc, tbRepYear, tbRepRes) and the risk measures
REP_SNAP = ['fpl', 'fplX', 'fplNom', 'f0', 'bO', 'bN', 'bONom', 'bNNom', 'pov', 'povNom', 'ep', 'giniD', 'giniX', 'giniW', 'giniWN']
PATH_M = ['f0', 'pov', 'bO', 'medW', 'buR', 'wageR']


def rep_acc():
    return NS(n=0, fpl=0, fplX=0, fplNom=0, bONom=0, bNNom=0, y7=None, end=None, y0=None, hist=[], path={m: {} for m in PATH_M})


def rep_year(R, Rr, agents, p, o, yr, T, ep):
    C = R.CFG
    n = len(agents)
    lf = lf_line(R, agents, o)
    thr = C['POVERTY_THRESHOLD_ONE']
    L30 = C['BLEI_PRECARIOUS_MAX']
    BDC = C['BASE_DAILY_COST']
    PL = C['POVERTY_LINE']
    s = dict(fpl=0, fplX=0, fplNom=0, f0=0, bO=0, bN=0, bONom=0, bNNom=0, pov=0, povNom=0)
    for a in agents:
        c = tb_cash_income(R, a)
        bo = R.agent_blei(a, p['bu'], p['ccoOn'], p['pth'], p['szh'], p['szhCoh'], p['ptf'])
        bn = R.blei0(a) + (a._tbM or 0) / BDC
        th = thr
        pf = c < th * lf
        h = a._h52
        if not h:
            h = a._h52 = NS(f=[], c=[])
            Rr.hist.append(h)
        h.f.append(1 if pf else 0)
        h.c.append(1 if (a._tbGap or 0) > 0 else 0)
        if R.RISK_MEASURE:
            if h.w is None:
                h.w = []
                h.b = []
                h.y = []
            h.w.append(a.wealth / lf)
            h.b.append(bo / lf)
            h.y.append(c / lf)
        if pf:
            s['fpl'] += 1
        if c < th:
            s['fplNom'] += 1
        if (a._tbExt if a._tbExt is not None else 0) < th * lf:
            s['fplX'] += 1
        if (a._tbGap or 0) > 0:
            s['f0'] += 1
        if bo / lf < L30:
            s['bO'] += 1
        if bn / lf < L30:
            s['bN'] += 1
        if bo < L30:
            s['bONom'] += 1
        if bn < L30:
            s['bNNom'] += 1
        if a.wealth < PL * lf:
            s['pov'] += 1
        if a.wealth < PL:
            s['povNom'] += 1
    Rr.n += n
    for k in ('fpl', 'fplX', 'fplNom', 'bONom', 'bNNom'):
        setattr(Rr, k, getattr(Rr, k) + s[k])
    wk = [a.yrWageUSD / 12 / lf for a in agents if (not a._ret) and a.yrWageUSD > 0]
    P = Rr.path
    P['f0'][yr] = s['f0'] / n * 100
    P['pov'][yr] = s['pov'] / n * 100
    P['bO'][yr] = s['bO'] / n * 100
    P['medW'][yr] = quantile_of([a.wealth / lf for a in agents], 0.5)
    P['buR'][yr] = R.PRICE.buY / lf if (p['ccoOn'] and p['bu'] > 0 and R.PRICE and R.PRICE.buY) else 0
    P['wageR'][yr] = quantile_of(wk, 0.5) if wk else 0
    if yr == 0 or yr == 6 or yr == T - 1:
        gc = n / (n - 1) if (o['giniNN1'] and n > 1) else 1
        q = {'ep': ep}
        for k in s:
            q[k] = s[k] / n * 100
        q['giniD'] = gini_of([a._tbDisp for a in agents]) * gc
        q['giniX'] = gini_of([a._tbExt for a in agents]) * gc
        q['giniW'] = gini_of([a.wealth for a in agents]) * gc
        q['giniWN'] = gini_neg([a.wealth for a in agents]) * gc
        if yr == 0:
            Rr.y0 = q
        if yr == 6:
            Rr.y7 = q
        if yr == T - 1:
            Rr.end = q


def rep_spells(hist, m, out, key):
    N = [0] * 6
    X = [0] * 6
    RN = 0
    RR = 0
    for h in hist:
        x = getattr(h, m)
        L = len(x)
        t = 0
        while t < L:
            if not x[t] or (t > 0 and x[t - 1]):
                t += 1
                continue
            e = t
            while e < L and x[e]:
                e += 1
            ln = e - t
            if t > 0:
                for d in range(1, ln + 1):
                    if t + d >= L:
                        break
                    k = min(d, 5)
                    N[k] += 1
                    if d == ln:
                        X[k] += 1
            if e < L and e + 1 < L:
                RN += 1
                if x[e + 1]:
                    RR += 1
            t = e
            t += 1
    for d in range(1, 6):
        out[key + 'N' + str(d)] = N[d]
        out[key + 'X' + str(d)] = X[d]
    out[key + 'RN'] = RN
    out[key + 'R'] = RR


def rk_draw(x):
    pk = x[0]
    d = 0
    for t in range(1, len(x)):
        if x[t] > pk:
            pk = x[t]
        elif pk - x[t] > d:
            d = pk - x[t]
    return d


def rk_reentry(hist, m, K):
    N = [0] * len(K)
    X = [0] * len(K)
    for h in hist:
        x = getattr(h, m)
        L = len(x)
        for e in range(1, L):
            if x[e] or not x[e - 1]:
                continue
            for i, k in enumerate(K):
                if e + k >= L:
                    continue
                N[i] += 1
                for j in range(1, k + 1):
                    if x[e + j]:
                        X[i] += 1
                        break
    return [X[i] / N[i] * 100 if N[i] else 0 for i in range(len(K))]


def risk_res(R, hist, out):
    mo = R.CFG['LIVING_WAGE_ANNUAL'] / 12
    dW = []
    dB = []
    ev = 0
    ay = 0
    Rk = [[0, 0], [0, 0], [0, 0]]
    B3 = [0, 0]
    rs = 0
    rn = 0
    for h in hist:
        if not h.w:
            continue
        y = h.y
        b = h.b
        L = len(y)
        ay += L
        dW.append(rk_draw(h.w) / mo)
        dB.append(rk_draw(b))
        for t in range(1, L):
            if not (y[t - 1] > 0) or y[t] >= 0.8 * y[t - 1]:
                continue
            ev += 1
            u = t + 1
            while u < L and y[u] < y[t - 1]:
                u += 1
            got = u - t if u < L else INF
            if got < INF:
                rs += got
                rn += 1
            for i, k in enumerate((1, 3, 5)):
                if t + k < L:
                    Rk[i][0] += 1
                    if got <= k:
                        Rk[i][1] += 1
            if t + 3 < L:
                B3[0] += 1
                for v in range(t + 1, t + 4):
                    if b[v] >= b[t - 1]:
                        B3[1] += 1
                        break

    def pc(x):
        return x[1] / x[0] * 100 if x[0] else 0
    rc = rk_reentry(hist, 'c', [1, 3, 5])
    rf = rk_reentry(hist, 'f', [5])
    out['rkDdW'] = median_of(dW) if dW else 0
    out['rkDdW6'] = len([v for v in dW if v > 6]) / len(dW) * 100 if dW else 0
    out['rkDdB'] = median_of(dB) if dB else 0
    out['rkDdB30'] = len([v for v in dB if v > 30]) / len(dB) * 100 if dB else 0
    out['rkEv'] = ev / ay * 100 if ay else 0
    out['rkRec1'] = pc(Rk[0])
    out['rkRec3'] = pc(Rk[1])
    out['rkRec5'] = pc(Rk[2])
    out['rkRecM'] = rs / rn if rn else 0
    out['rkRecB3'] = pc(B3)
    out['rkReC1'] = rc[0]
    out['rkReC3'] = rc[1]
    out['rkReC5'] = rc[2]
    out['rkReF5'] = rf[0]
    return out


def rep_res(R, Rr, out):
    def pc(k):
        return getattr(Rr, k) / Rr.n * 100 if (Rr and Rr.n) else 0
    out['fplPY'] = pc('fpl')
    out['fplXPY'] = pc('fplX')
    out['fplNomPY'] = pc('fplNom')
    out['bOAPyNom'] = pc('bONom')
    out['bNAPyNom'] = pc('bNNom')
    for k in REP_SNAP:
        K = k[0].upper() + k[1:]
        out['y7' + K] = Rr.y7[k] if (Rr and Rr.y7) else 0
        out['e' + K] = Rr.end[k] if (Rr and Rr.end) else 0
        out['y0' + K] = Rr.y0[k] if (Rr and Rr.y0) else 0
    for m in PATH_M:
        for t in range(40):
            v = Rr.path[m].get(t) if Rr else None
            out['p' + m + '_' + str(t)] = v if isinstance(v, (int, float)) else 0
    if Rr and R.RISK_MEASURE:
        risk_res(R, Rr.hist, out)
    if Rr:
        rep_spells(Rr.hist, 'f', out, 'sf')
        rep_spells(Rr.hist, 'c', out, 'sc')
        out['everFpl'] = len([h for h in Rr.hist if any(h.f)]) / len(Rr.hist) * 100 if Rr.hist else 0
    return out


# ------------------------------------------------------------------ the household reading
HH_TYPES = ['sg', 'sp', 'cn', 'ck']


def hh_type_of(H):
    return ('sp' if H.kids else 'sg') if len(H.a) == 1 else ('ck' if H.kids else 'cn')


def hh_rep_acc():
    R = NS(py=0, kpy=0, c={}, y7=None, end=None, per=0, kid=0, gini=None, med=None)
    for k in ('cost', 'fpl', 'wlth', 'blei'):
        R.c[k] = 0
        R.c[k + 'K'] = 0
    R.t = {t: dict(py=0, cost=0, wlth=0) for t in HH_TYPES}
    R.ab = {k: dict(py=0, c=0) for k in ('a25', 'a35', 'a50', 'a67')}
    R.sp = []
    return R


def hh_rep_year(R, Rr, agents, p, o, yr, T):
    C = R.CFG
    lf = lf_line(R, agents, o)
    s = dict(per=0, kid=0, cost=0, costK=0, fpl=0, fplK=0, wlth=0, wlthK=0, blei=0, bleiK=0)
    eq = []
    for H in R.HHS.list:
        nA = len(H.a)
        nK = len(H.kids)
        n = nA + nK
        inc = cost = need = money = disp = w = b = 0.0
        for a in H.a:
            inc += a._hhInc
            cost += a._hhCost
            need += a._hhMlc
            disp += a._hhDisp
            money += tb_cash_income(R, a)
            w += a.wealth
            b += R.agent_blei(a, p['bu'], p['ccoOn'], p['pth'], p['szh'], p['szhCoh'], p['ptf']) / lf
        fC = inc < cost
        fF = money < C['HH_FPL'][str(nA) + 'a' + str(min(4, nK)) + 'k'] * lf
        fW = w < need * C['HH_WEALTH_MONTHS'] / 12
        fB = b / nA < C['BLEI_PRECARIOUS_MAX']
        t = Rr.t[hh_type_of(H)]
        s['per'] += n
        s['kid'] += nK
        if fC:
            s['cost'] += n
            s['costK'] += nK
        if fF:
            s['fpl'] += n
            s['fplK'] += nK
        if fW:
            s['wlth'] += n
            s['wlthK'] += nK
        if fB:
            s['blei'] += n
            s['bleiK'] += nK
        t['py'] += n
        if fC:
            t['cost'] += n
        if yr == T - 1:
            t['n'] = t.get('n', 0) + n
            if fW:
                t['w'] = t.get('w', 0) + n
        if not H._sp:
            H._sp = NS(c=[], t=hh_type_of(H))
            Rr.sp.append(H._sp)
        H._sp.c.append(fC)
        if yr == T - 1:
            e = disp / math.sqrt(n) / lf
            for _ in range(n):
                eq.append(e)
    Rr.py += s['per']
    Rr.kpy += s['kid']
    Rr.per = s['per']
    Rr.kid = s['kid']
    for k in ('cost', 'fpl', 'wlth', 'blei'):
        Rr.c[k] += s[k]
        Rr.c[k + 'K'] += s[k + 'K']

    def snap():
        return dict(cost=s['cost'] / s['per'] * 100, costK=s['costK'] / s['kid'] * 100 if s['kid'] else 0, fpl=s['fpl'] / s['per'] * 100,
                    fplK=s['fplK'] / s['kid'] * 100 if s['kid'] else 0, wlth=s['wlth'] / s['per'] * 100, wlthK=s['wlthK'] / s['kid'] * 100 if s['kid'] else 0,
                    blei=s['blei'] / s['per'] * 100, bleiK=s['bleiK'] / s['kid'] * 100 if s['kid'] else 0)
    if yr == 6:
        Rr.y7 = snap()
    if yr == T - 1:
        Rr.end = snap()
        Rr.gini = gini_of(eq)
        Rr.med = quantile_of(eq, 0.5)


def hh_res(R, Rr, out):
    if not Rr:
        return out

    def pc(k, kid=False):
        d = Rr.kpy if kid else Rr.py
        return Rr.c[k] / d * 100 if d else 0
    out['hhPer'] = Rr.per
    out['hhKid'] = Rr.kid
    out['hhCostPY'] = pc('cost')
    out['hhCostKidPY'] = pc('costK', 1)
    out['hhFplPY'] = pc('fpl')
    out['hhFplKidPY'] = pc('fplK', 1)
    out['hhWlthPY'] = pc('wlth')
    out['hhWlthKidPY'] = pc('wlthK', 1)
    out['hhBleiPY'] = pc('blei')
    out['hhBleiKidPY'] = pc('bleiK', 1)
    y7 = Rr.y7 or {}
    e = Rr.end or {}
    out['hhFpl7'] = y7.get('fpl', 0)
    out['hhFplKid7'] = y7.get('fplK', 0)
    out['hhCost7'] = y7.get('cost', 0)
    out['hhCostKid7'] = y7.get('costK', 0)
    for k, kk in (('Fpl', 'fpl'), ('FplKid', 'fplK'), ('Cost', 'cost'), ('CostKid', 'costK'), ('Wlth', 'wlth'), ('WlthKid', 'wlthK'), ('Blei', 'blei'), ('BleiKid', 'bleiK')):
        out['hh' + k + 'End'] = e.get(kk, 0)
    out['hhGiniEq'] = Rr.gini or 0
    out['hhMedEq'] = Rr.med or 0
    for t in HH_TYPES:
        q = Rr.t[t]
        out['hhCost_' + t] = q['cost'] / q['py'] * 100 if q['py'] else 0
        out['hhWlth_' + t] = q.get('w', 0) / q['n'] * 100 if q.get('n') else 0
        out['hhShare_' + t] = q['py'] / Rr.py * 100 if Rr.py else 0
    for k in ('a25', 'a35', 'a50', 'a67'):
        q = Rr.ab[k]
        out['hhCostA' + k[1:]] = q['c'] / q['py'] * 100 if q['py'] else 0

    def sp(L):
        o2 = {}
        rep_spells(L, 'c', o2, 'q')
        return (o2['qX1'] / o2['qN1'] if o2['qN1'] else 0), o2['qN1']
    ex, nn = sp(Rr.sp)
    out['hhSpEx1'] = ex
    out['hhSpN'] = nn
    for t in HH_TYPES:
        ex, nn = sp([x for x in Rr.sp if x.t == t])
        out['hhSpEx1_' + t] = ex
        out['hhSpN_' + t] = nn
    return out


# ------------------------------------------------------------------ distribution measures (dm), the tail (wt), asset classes (rt)
DM_GRID = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 99]


def dm_keys():
    k = []
    for s in ('S', 'E'):
        for m in ('Wt1', 'Wt10', 'Wb50', 'Yt1', 'Yt10', 'Yb50', 'Yp', 'YpOk', 'Wr', 'WrOk', 'Ls', 'Lc', 'Fd', 'Dm', 'Di', 'N'):
            k.append('dm' + m + s)
        for q in DM_GRID:
            k.append('dmWp' + str(q) + s)
            k.append('dmYp' + str(q) + s)
    k += ['dmLsPY', 'dmLcPY', 'dmMobN']
    for i in range(5):
        for j in range(5):
            k.append('dmMob' + str(i) + str(j))
    return k


def dm_new(o):
    return NS(o={} if o is True else o, snap={}, pyW=0.0, pyC=0.0, pyY=0.0, mob=None)


RK = False  # S63 fx.rk (GAPS item 24), set by Run from the row's FX: the weighted measures rank on the value rounded to the cent, ties by index


def dm_sort(v):
    if RK:
        k = [js_round(x * 100) for x in v]
        return sorted(range(len(v)), key=lambda i: (k[i], i))
    return sorted(range(len(v)), key=lambda i: (v[i], i))


def dm_quantiles(v, w, qs):
    n = len(v)
    if not n:
        return [0 for _ in qs]
    idx = dm_sort(v)
    W = 0.0
    for i in idx:
        W += w[i]
    den = W - W / n
    p = []
    c = 0.0
    for i in idx:
        p.append(c / den if den > 0 else 0)
        c += w[i]
    out = []
    for q in qs:
        if n == 1 or den <= 0:
            out.append(v[idx[0]])
            continue
        k = 0
        while k < n - 2 and p[k + 1] <= q + 1e-12:
            k += 1
        a = p[k]
        b = p[k + 1]
        t = min(1, max(0, (q - a) / (b - a))) if b > a else 0
        out.append(v[idx[k]] + (v[idx[k + 1]] - v[idx[k]]) * t)
    return out


def dm_tail(v, w, f, top):
    idx = dm_sort(v)
    if top:
        idx.reverse()
    W = 0.0
    for i in idx:
        W += w[i]
    rem = f * W
    s = 0.0
    t = 0
    while t < len(idx) and rem > 0:
        i = idx[t]
        u = min(w[i], rem)
        s += u * v[i]
        rem -= u
        t += 1
    return s


def dm_tot(v, w):
    s = 0.0
    for i in range(len(v)):
        s += w[i] * v[i]
    return s


def dm_measure(v, w, out, pre, s):
    T = dm_tot(v, w)

    def sh(f, top):
        return dm_tail(v, w, f, top) / T * 100 if T > 0 else 0
    out['dm' + pre + 't1' + s] = sh(0.01, True)
    out['dm' + pre + 't10' + s] = sh(0.10, True)
    out['dm' + pre + 'b50' + s] = sh(0.50, False)
    b40 = dm_tail(v, w, 0.40, False)
    t10 = dm_tail(v, w, 0.10, True)
    ok = 1 if b40 > 0 else 0
    out['dm' + ('Wr' if pre == 'W' else 'Yp') + s] = t10 / b40 if ok else 0
    out['dm' + ('WrOk' if pre == 'W' else 'YpOk') + s] = ok
    qs = dm_quantiles(v, w, [q / 100 for q in DM_GRID])
    for j, q in enumerate(DM_GRID):
        out['dm' + pre + 'p' + str(q) + s] = qs[j]


def dm_fifths(v, w):
    idx = dm_sort(v)
    W = 0.0
    for i in idx:
        W += w[i]
    c = 0.0
    q = [0] * len(v)
    for i in idx:
        q[i] = min(4, math.floor(5 * (c + w[i] / 2) / W)) if W > 0 else 0
        c += w[i]
    return q


def wt_of(a):
    return 1 if a._w is None else float(a._w)


def dm_year(R, S, agents, p, o, yr, T):
    n = len(agents)
    if not n or yr >= T:
        return
    lf = lf_line(R, agents, o)
    wt = [wt_of(a) for a in agents]
    wg = wc = mi = 0.0
    for i, a in enumerate(agents):
        wgi = _p(a.yrWageUSD)
        cv = _p(a.yrConvUSD)
        wg += wt[i] * wgi
        wc += wt[i] * (wgi + cv)
        mi += wt[i] * tb_cash_income(R, a)
    S.pyW += wg / lf
    S.pyC += wc / lf
    S.pyY += mi / lf
    if yr != 0 and yr != T - 1:
        return
    s = 'S' if yr == 0 else 'E'
    o2 = {}
    W = [a.wealth / lf for a in agents]
    Yv = [_p(a._tbDisp) / lf for a in agents]
    dm_measure(W, wt, o2, 'W', s)
    dm_measure(Yv, wt, o2, 'Y', s)
    o2['dmLs' + s] = wg / mi * 100 if mi > 0 else 0
    o2['dmLc' + s] = wc / mi * 100 if mi > 0 else 0
    o2['dmN' + s] = n
    fam = [H.a for H in R.HHS.list if H.a] if (R.HHS and R.HHS.list) else [[a] for a in agents]
    fd = fw = dy = dd = 0.0
    dv = []
    dw = []
    for m in fam:
        wl = y = ww = 0.0
        for a in m:
            wl += a.wealth
            y += _p(a._tbDisp)
            ww += wt_of(a)
        ww /= len(m)
        fw += ww
        if wl < 0:
            fd += ww
            dv.append(-wl / lf)
            dw.append(ww)
            dd += ww * (-wl / lf)
            dy += ww * y / lf
    o2['dmFd' + s] = fd / fw * 100 if fw > 0 else 0
    o2['dmDm' + s] = dm_quantiles(dv, dw, [0.5])[0] if dv else 0
    o2['dmDi' + s] = dd / dy if dy > 0 else 0
    S.snap[s] = o2
    q = dm_fifths(W, wt)
    if yr == 0:
        for i, a in enumerate(agents):
            a._dmQ = q[i]
    else:
        M = [[0.0] * 5 for _ in range(5)]
        N = 0
        for i, a in enumerate(agents):
            if a._dmQ is not None:
                M[a._dmQ][q[i]] += wt[i]
                N += 1
        S.mob = NS(M=M, N=N)


def dm_res(r, S):
    for k in dm_keys():
        r[k] = 0
    for s in ('S', 'E'):
        o2 = S.snap.get(s)
        if o2:
            r.update(o2)
    r['dmLsPY'] = S.pyW / S.pyY * 100 if S.pyY > 0 else 0
    r['dmLcPY'] = S.pyC / S.pyY * 100 if S.pyY > 0 else 0
    if S.mob:
        r['dmMobN'] = S.mob.N
        for i, row in enumerate(S.mob.M):
            t = 0.0
            for x in row:
                t += x
            for j, c in enumerate(row):
                r['dmMob' + str(i) + str(j)] = c / t * 100 if t > 0 else 0
    return r


def wt_gini(v, w):
    idx = dm_sort(v)
    W = T = c = g = 0.0
    for i in idx:
        W += w[i]
        T += w[i] * v[i]
    if not (T > 0) or not (W > 0):
        return 0
    for i in idx:
        c1 = c + w[i] * v[i]
        g += w[i] * (c + c1)
        c = c1
    return 1 - g / (W * T)


WT_KEYS = ['wt' + m + s for s in ('S', 'E') for m in ('Pov', 'F0', 'Gn', 'Gz', 'T01', 'T1', 'T10', 'B50', 'P999', 'Mean', 'Med')] + ['wtN', 'wtW', 'wtTailW']


def wt_rep(R, S, agents, o, yr, T):
    n = len(agents)
    if not n or (yr != 0 and yr != T - 1):
        return
    lf = lf_line(R, agents, o)
    s = 'S' if yr == 0 else 'E'
    w = [wt_of(a) for a in agents]
    v = [a.wealth / lf for a in agents]
    z = [max(0, x) for x in v]
    W = pv = f0 = tw = 0.0
    tn = 0
    tot = dm_tot(v, w)
    PL = R.CFG['POVERTY_LINE']
    for i, a in enumerate(agents):
        W += w[i]
        if a.wealth < PL * lf:
            pv += w[i]
        if (a._tbGap or 0) > 0:
            f0 += w[i]
        if (a._wtJ or 0) > 0:
            tn += 1
            tw += w[i]

    def sh(f, top):
        return dm_tail(v, w, f, top) / tot * 100 if tot > 0 else 0
    q = dm_quantiles(v, w, [0.5, 0.999])
    S['wtPov' + s] = pv / W * 100
    S['wtF0' + s] = f0 / W * 100
    S['wtGn' + s] = wt_gini(v, w)
    S['wtGz' + s] = wt_gini(z, w)
    S['wtT01' + s] = sh(0.001, True)
    S['wtT1' + s] = sh(0.01, True)
    S['wtT10' + s] = sh(0.10, True)
    S['wtB50' + s] = sh(0.50, False)
    S['wtP999' + s] = q[1]
    S['wtMean' + s] = tot / W
    S['wtMed' + s] = q[0]
    S['wtN'] = tn
    S['wtW'] = W
    S['wtTailW'] = tw / W * 100
    if yr == 0:
        for k in WT_KEYS:
            S.setdefault(k, 0)


def rt_rep(R, S, agents, o, yr, T):
    n = len(agents)
    if not n or (yr != 0 and yr != T - 1):
        return
    RT = R.RETURNS
    lf = lf_line(R, agents, o)
    sfx = 'S' if yr == 0 else 'E'
    L = [a for a in agents if a._rt]
    wt = [wt_of(a) for a in L]
    tw = tb = cw = top = 0.0
    ordr = sorted(range(len(L)), key=lambda i: (-L[i].wealth, i))
    for i, w in enumerate(wt):
        tw += w
        tb += w * L[i]._rt.r[3]
    for i in ordr:
        take = max(0, min(wt[i], 0.01 * tw - cw))
        cw += wt[i]
        top += take * L[i]._rt.r[3]
    S['rtBt1' + sfx] = top / tb * 100 if tb > 0 else 0
    for k in R.S['RT2_KEYS']:
        S.setdefault(k, 0)
    if RT.get('ci'):
        yk = mi = yb = ow = 0.0
        SOLE = R.S['RT_SOLE']
        for i, a in enumerate(L):
            b = a._rt
            yk += wt[i] * _p(a.yrCapUSD)
            mi += wt[i] * tb_cash_income(R, a)
            if b.own:
                ow += wt[i]
                if b.g >= 0:
                    yb += wt[i] * SOLE[b.g] * _p(a.yrWageUSD)
        S['rtYk' + sfx] = yk / tw / lf if tw > 0 else 0
        if yr == 0:
            S['rtOwnS'] = ow / tw * 100 if tw > 0 else 0
            oi = sorted(range(len(L)), key=lambda i: (tb_cash_income(R, L[i]), i))
            ci0 = 0.0
            lo = [0.0, 0.0]
            hi = [0.0, 0.0]
            for i in oi:
                m = (ci0 + wt[i] / 2) / tw
                ci0 += wt[i]
                if m < 0.5:
                    lo[0] += wt[i]
                    if L[i]._rt.own:
                        lo[1] += wt[i]
                if m >= 0.9:
                    hi[0] += wt[i]
                    if L[i]._rt.own:
                        hi[1] += wt[i]
            S['rtOwnLoS'] = lo[1] / lo[0] * 100 if lo[0] > 0 else 0
            S['rtOwnHiS'] = hi[1] / hi[0] * 100 if hi[0] > 0 else 0
        if yr == T - 1:
            S['rtYkShE'] = yk / mi * 100 if mi > 0 else 0
            S['rtYbE'] = yb / tw / lf if tw > 0 else 0
    if yr == T - 1:
        gs = 0.0
        og = sorted(range(len(L)), key=lambda i: (-((_p(L[i]._tbDisp)) + L[i]._rt.gy), i))
        cg = g1 = g10 = 0.0
        for i, a in enumerate(L):
            gs += wt[i] * a._rt.gy
        for i in og:
            t1 = max(0, min(wt[i], 0.01 * tw - cg))
            t10 = max(0, min(wt[i], 0.10 * tw - cg))
            cg += wt[i]
            g1 += t1 * L[i]._rt.gy
            g10 += t10 * L[i]._rt.gy
        S['rtGt1E'] = g1 / gs * 100 if gs > 0 else 0
        S['rtGt10E'] = g10 / gs * 100 if gs > 0 else 0
    if yr == 0:
        o0 = sorted(range(len(L)), key=lambda i: (L[i]._rt.w0, i))
        c0 = 0.0
        for i in o0:
            L[i]._rt.q = min(5, math.floor((c0 + wt[i] / 2) / tw * 5) + 1)
            c0 += wt[i]
        if RT.get('cr'):
            c1 = 0.0
            for i in reversed(o0):
                L[i]._rt.t1 = max(0, min(wt[i], 0.01 * tw - c1)) / wt[i] if wt[i] > 0 else 0
                c1 += wt[i]
    if yr != T - 1:
        return
    A = {k: [0.0] * 6 for k in ('rtE', 'rtV', 'rtS', 'rtE0', 'rtV0', 'rtRE', 'rtNE', 'rtDvE', 'rtDfE')}
    Wq = [0.0] * 6
    for i, a in enumerate(L):
        b = a._rt
        q = b.q or 0
        w = wt[i]
        Ee = (b.en - b.ed - b.df) / lf
        V = (b.v[0] + b.v[1] + b.v[2] + b.v[3] + b.v[4]) / lf
        k = NS(r=list(b.r), n=b.n, dv=b.dv, al=b.al)
        R.rt_place(k, a.wealth - b.w, RT)
        Rr = (k.r[0] + k.r[1] + k.r[2] + k.r[3] + k.r[4]) / lf
        for t, j in enumerate((0, q)):
            if t and not q:
                continue
            Wq[j] += w
            A['rtE'][j] += w * Ee
            A['rtV'][j] += w * V
            A['rtS'][j] += w * (a.wealth / lf - Ee - V)
            A['rtE0'][j] += w * b.e0 / b.p0
            A['rtV0'][j] += w * b.v0 / b.p0
            A['rtRE'][j] += w * Rr
            A['rtNE'][j] += w * k.n / lf
            A['rtDvE'][j] += w * k.dv / lf
            A['rtDfE'][j] += w * b.df / lf
    for kk in ('rtE', 'rtV', 'rtS', 'rtE0', 'rtV0'):
        for j in range(6):
            S[kk + (str(j) if j else '')] = A[kk][j] / Wq[j] if Wq[j] > 0 else 0
    for kk in ('rtRE', 'rtNE', 'rtDvE', 'rtDfE'):
        S[kk] = A[kk][0] / Wq[0] if Wq[0] > 0 else 0
    if RT.get('cr') and R.CRS:
        CA = R.CRS.A
        cn = [0.0] * 6
        cr_ = [0.0] * 6
        cwq = [0.0] * 6
        ct = cs = 0.0
        for i, a in enumerate(L):
            b = a._rt
            q = b.q or 0
            w = wt[i]
            x = b.crn or 0
            cwq[q] += w
            cn[q] += w * x
            cr_[q] += w * (b.crr or 0)
            cs += w * x
            ct += w * (b.t1 or 0) * x
        for k, kk in (('crRel', 'rel'), ('crBook', 'book'), ('crNom', 'nom'), ('crEq', 'eq'), ('crOutG', 'outG'), ('crOutF', 'outF'), ('crOutH', 'outH'), ('crOutS', 'outS'), ('crUn', 'un')):
            S[k] = CA[kk]
        S['crGap'] = CA['rel'] - CA['book'] - CA['nom'] - CA['eq'] - CA['outG'] - CA['outF'] - CA['outH'] - CA['outS'] - CA['un']
        for cq in range(1, 6):
            S['crN' + str(cq)] = cn[cq] / cwq[cq] if cwq[cq] > 0 else 0
            S['crR' + str(cq)] = cr_[cq] / cwq[cq] if cwq[cq] > 0 else 0
        S['crT1'] = ct / cs * 100 if cs != 0 else 0


# ------------------------------------------------------------------ the price rule's record (o.mf), the money flows, the within-year costs
def pr_new(o, on, S):
    O = dict(S['PR_DEFAULTS'])
    if o and o is not True:
        O.update(o)
    return NS(on=bool(on), o=O, n=0.0, m=0.0, p={'gen': 0.0, 'food': 0.0, 'housing': 0.0, 'medical': 0.0}, bPrev=1, y=[], pt={}, dg=0.0, dl=0.0, dq=[])


def pr_sec(v, s, d):
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        return v
    if isinstance(v, dict) and isinstance(v.get(s), (int, float)):
        return v[s]
    return d


def pr_step(R, S, U, Y, lam, wIdx, piG, bIdx, slk, yr, PGq):
    o = S.o
    dn = math.log(max(1e-12, 1 + lam * U / Y)) if Y > 0 else 0
    w = math.log(max(1e-12, 1 + (wIdx or 0) * (piG or 0)))
    piE = math.log(bIdx / S.bPrev)
    hR = -math.log(1 - min(0.999, slk)) if (o.get('rs') is not False and slk > 0) else 0
    ks = (o['ks'][yr] if yr < len(o['ks']) else 0) or 0 if isinstance(o.get('ks'), list) else o.get('ks')
    xG = hG = 0.0
    p0 = S.p['gen']
    S.m += dn
    if o.get('bd'):
        dn *= 1 + o['bd']
    if o.get('q', 1) > 1 and S.on:
        raise NotImplementedError('prStepQ')
    S.n += dn
    S.bPrev = bIdx
    nE = S.n + o['bv'] * S.dg if o.get('bv') else S.n
    ML = R.S['MULT_LS']
    for s in R.S['PR_SECT']:
        h = pr_sec(o.get('h'), s, 0) + hR - pr_sec(ks, s, 0)
        x = nE - S.p[s]
        if s == 'gen':
            xG = x
            hG = h
        if S.on:
            S.p[s] += pr_sec(o.get('a'), s, ML) * w + o['r'] * piE + o['k'] * max(0, x - h) + o['k2'] * min(0, x)
    if not S.on:
        S.p['gen'] = math.log(PGq)
    cap = hG + o['um']
    rec = dict(x=xG, h=hG, slk=min(0.999, slk) if hR > 0 else 0, out=min(max(0, xG), max(0, cap)), rat=max(0, xG - cap), loss=min(0, xG))
    S.y.append(rec)
    if S.n > 0:
        S.pt[yr + 1] = S.p['gen'] / (S.m if o.get('bd') else S.n)
    S.dg = S.p['gen'] - p0
    return math.exp(S.p['gen']) if S.on else PGq


def pr_res(R, r, S, agents, lineF):
    Yl = S.y
    T = len(Yl)

    def m(f):
        if not T:
            return 0
        t = 0.0
        for y in Yl:
            t += f(y)
        return t / T * 100
    Lr = Yl[-1] if T else dict(x=0, h=0, rat=0)

    def pct(v):
        return math.exp(v) - 1
    sh = math.exp(Lr.get('rat') or 0)
    ws = [a.wealth for a in agents]
    pv = 0
    PL = R.CFG['POVERTY_LINE']
    for w in ws:
        if w < PL * lineF * sh:
            pv += 1
    r['prOn'] = 1 if S.on else 0
    for t in (3, 10, 19, 39):
        r['prPT' + str(t)] = S.pt.get(t, 0) or 0
    r['prX'] = m(lambda y: pct(y['x']))
    r['prH'] = m(lambda y: pct(y['h']))
    r['prSlk'] = m(lambda y: y['slk'])
    r['prOut'] = m(lambda y: pct(y['out']))
    r['prRat'] = m(lambda y: 1 - math.exp(-y['rat']))
    r['prLoss'] = m(lambda y: 1 - math.exp(y['loss']))
    r['prXE'] = pct(Lr['x']) * 100
    r['prRatE'] = (1 - math.exp(-(Lr.get('rat') or 0))) * 100
    r['prSh'] = sh
    if T:
        t = 0.0
        for y in Yl:
            t += math.exp(y.get('avg') or 0)
        r['prAvg'] = t / T
    else:
        r['prAvg'] = 1
    r['prWsh'] = median_of(ws) / (agents[0].yrBasketUSD / R.CFG['LIVING_WAGE_ANNUAL'] / (agents[0]._hhF or 1)) / sh
    r['prPovSh'] = pv / len(agents) * 100 if agents else 0
    return r


def mf_new():
    return NS(iss=0.0, bu=0.0, tax=0.0, cv=0.0, M=0.0, cut=0.0, pth=0.0, U=0.0, Y=0.0, uy=0.0, chk=0.0, T=0)


def mf_year(F, C, U, Y):
    i = C.idx or 1
    F.iss += C.buIss / i
    F.bu += C.bu / i
    F.tax += C.ctax / i
    F.cv += C.conv / i
    F.M += C.convM / i
    F.cut += (C.cutPT - C.cutFree + C.cutG) / i
    F.pth += C.pthLiq / i
    F.U += U / i
    F.Y += Y / i
    F.uy += U / Y if Y > 0 else 0
    F.chk += abs(U - (C.bu + C.conv - C.convM)) / i
    F.T += 1


def mf_res(r, F, NY):
    r['mfIss'] = F.iss / NY
    r['mfBU'] = F.bu / NY
    r['mfCvG'] = (F.cv + F.tax) / NY
    r['mfTax'] = F.tax / NY
    r['mfCvN'] = F.cv / NY
    r['mfPay'] = (F.bu + F.cv) / NY
    r['mfM'] = F.M / NY
    r['mfCut'] = F.cut / NY
    r['mfPth'] = F.pth / NY
    r['mfReSp'] = 0
    r['mfU'] = F.U / NY
    r['mfY'] = F.Y / NY
    r['mfUY'] = F.uy / F.T * 100 if F.T else 0
    r['mfTaxSh'] = F.tax / (F.cv + F.tax) * 100 if F.cv + F.tax > 0 else 0
    r['mfChk'] = F.chk / NY
    return r


def wy_year(W, f):
    c = W.cur
    for j in range(0, len(c), 3):
        g = max(0, c[j] * f - c[j + 1]) / (c[j + 2] * f)
        W.f0 += 1 if g > 0 else 0
        W.f1 += g
        W.f2 += g * g
        W.n += 1
    W.cur = []
    W.fs += f
    W.ny += 1


def wy_res(r, W):
    n = max(1, W.n)
    r['wyF0PY'] = W.f0 / n * 100
    r['wyF1PY'] = W.f1 / n * 100
    r['wyF2PY'] = W.f2 / n * 100
    r['wyAvg'] = W.fs / W.ny if W.ny else 1
    return r


# ------------------------------------------------------------------ who pays (fx.fin) and the government account (gv)
def fin_step(R, L, o, C, A, need, U, extra, gRun, bkP, bkU, T, tauUsed):
    F = R.FX and R.FX.get('fin')
    cuts = (1 - o['eP']) * (C.cutPT - C.cutFree + C.cutG)
    taxed = o['fin'] in ('tax', 'hybrid', 'source')
    gp = sr = gm = 0.0
    if F not in (None, False, 'report', 'money', 'debt', 'cap'):
        raise ValueError('fx.fin')
    if F in ('debt', 'cap'):
        raise NotImplementedError('fx.fin debt/cap')
    if taxed:
        gp = max(0, need - C.tax)
        sr = max(0, C.tax - need)
    if F in ('money', 'cap') and (o['fin'] in ('hybrid', 'source') or (o['fin'] == 'tax' and not o.get('taxBase'))):
        gm = gp
        U += gp
    if o['fin'] == 'tax' and o.get('taxBase'):
        gm = gp
    M = U - extra
    if o['fin'] == 'tax':
        P = need
        B = 0
        G = gp - gm
    elif o['fin'] == 'hybrid':
        P = need + C.conv
        B = o['a'] * (C.conv - C.convM) + C.convM
        G = gp - gm
    elif o['fin'] == 'source':
        cvS = C.conv - C.pjg + L['pjg'] / (T - 1) if gRun else C.conv
        P = need + C.bu + cvS
        B = bkP - bkU + C.convM + (C.bu if o.get('faceM') else 0)
        G = gp - gm
    else:
        raise NotImplementedError('fin money/none')
    Tx = C.tax if taxed else 0
    if F:
        Q = L.get('fi')
        if Q is None:
            Q = L['fi'] = dict(P=0.0, T=0.0, M=0.0, B=0.0, G=0.0, S=0.0, GM=0.0, cap=0)
        i = C.idx or 1
        Q['P'] += P / i
        Q['T'] += Tx / i
        Q['M'] += M / i
        Q['B'] += B / i
        Q['G'] += (gp if taxed else G) / i
        Q['S'] += sr / i
        Q['GM'] += gm / i
        capE = R.TB.capE if R.TB.capE is not None else o['tauMax']
        if o['fin'] == 'tax' and not o.get('taxBase') and tauUsed >= capE - 1e-12:
            Q['cap'] += 1
    return U


def fin_res(r, Q, NY):
    Q = Q or dict(P=0, T=0, M=0, B=0, G=0, S=0, GM=0, cap=0)
    r['finPay'] = Q['P'] / NY
    r['finTax'] = Q['T'] / NY
    r['finMoney'] = Q['M'] / NY
    r['finMatch'] = Q['B'] / NY
    r['finGap'] = Q['G'] / NY
    r['finSur'] = Q['S'] / NY
    r['finGapM'] = Q['GM'] / NY
    r['finGapSh'] = (Q['G'] - Q['GM'] - Q.get('GB', 0)) / Q['P'] * 100 if Q['P'] > 0 else 0
    r['finCapYrs'] = Q['cap']
    return r


def gv_new(R):
    U = R.S['GV_US']
    return NS(D=0.0, int=0.0, piP=0.0, gapP=0.0, ixP=None, ratio=0.0, r15=0.0, y100=0, gd=0, fix=U['D0'] * U['fc'], fixM=U['D0'] * U['fc'], cap=0,
              A=dict(pay=0.0, tax=0.0, int=0.0, def_=0.0, mon=0.0, bor=0.0, unp=0.0, sur=0.0, er=0.0, erM=0.0, rate=0.0, rr=0.0, ny=0))


def gv_step(R, S, o, C, need, agents, yr, T, mult, tauUsed):
    G = R.GOV
    F = R.FX and R.FX.get('fin')
    taxed = o['fin'] in ('tax', 'hybrid', 'source')
    a0 = agents[0] if agents else None
    ix = a0.yrBasketUSD / R.CFG['LIVING_WAGE_ANNUAL'] / (a0._hhF or 1) if (a0 and a0.yrBasketUSD and a0.yrBasketUSD > 0) else 1
    n = max(1, len(agents))
    if not taxed and need > 0:
        raise ValueError('gv needs a contribution')
    pi = 0 if S.ixP is None else ix / S.ixP - 1
    prem = G['dk'] * S.ratio
    Dp = S.D
    tx = C.tax if taxed else 0
    if F != 'debt':
        i = 0
    elif G['r'] == 'fixed':
        i = (1 + G['rr'] + prem) * (1 + pi) - 1
    else:
        i = max(0, G['rs'] + S.piP + G['a'] * (S.piP - G['pt']) + G['b'] * S.gapP) + prem
    if i > 1:
        i = 1
        S.gd += 1
    it = i * Dp
    df = need + it - tx
    gp = max(0, need - tx)
    sr = max(0, tx - need)
    mon = bor = unp = sur = 0.0
    if F == 'debt':
        bor = max(df, -Dp)
        sur = max(0, -df - Dp)
    else:
        mon = gp if (F in ('money', 'cap') or (o['fin'] == 'tax' and o.get('taxBase'))) else 0
        unp = gp - mon
        sur = sr
    S.D = Dp + bor
    S.int = it
    S.piP = pi
    S.gapP = math.log(mult if mult > 0 else 1)
    S.ixP = ix
    S.ratio = max(0, S.D / ix / n / R.S['GV_US']['Y0'])
    if yr == T - 6:
        S.r15 = S.ratio
    if not S.y100 and S.ratio > 1:
        S.y100 = yr + 1
    A = S.A
    A['pay'] += need / ix
    A['tax'] += tx / ix
    A['int'] += it / ix
    A['def_'] += df / ix
    A['mon'] += mon / ix
    A['bor'] += bor / ix
    A['unp'] += unp / ix
    A['sur'] += sur / ix
    if F == 'debt':
        A['rate'] += i
        A['rr'] += (1 + i) / (1 + pi) - 1
        A['ny'] += 1
    er = S.fix * pi / (1 + pi)
    erM = S.fixM * pi / (1 + pi)
    S.fix /= 1 + pi
    S.fixM *= (1 - 1 / G['m']) / (1 + pi)
    A['er'] += er
    A['erM'] += erM
    capE = R.TB.capE if R.TB.capE is not None else o['tauMax']
    if o['fin'] == 'tax' and not o.get('taxBase') and need > 0 and tauUsed >= capE - 1e-12:
        S.cap += 1


def gv_target(R, need):
    G = R.GOV
    return G['sh'] * need + (R.GVS.int if (G['ip'] == 'tax' and R.FX and R.FX.get('fin') == 'debt' and R.GVS) else 0)


def gv_res(R, r, S, NY, T):
    A = S.A
    Y0 = R.S['GV_US']['Y0']
    r['gvPay'] = A['pay'] / NY
    r['gvTax'] = A['tax'] / NY
    r['gvInt'] = A['int'] / NY
    r['gvDef'] = A['def_'] / NY
    r['gvMon'] = A['mon'] / NY
    r['gvBor'] = A['bor'] / NY
    r['gvUnp'] = A['unp'] / NY
    r['gvSur'] = A['sur'] / NY
    r['gvDebt'] = S.ratio * Y0
    r['gvDebtY'] = S.ratio * 100
    r['gvDebtY15'] = S.r15 * 100
    r['gvIntSh'] = A['int'] / A['pay'] * 100 if A['pay'] > 0 else 0
    r['gvShR'] = A['tax'] / A['pay'] * 100 if A['pay'] > 0 else 0
    r['gvRate'] = A['rate'] / A['ny'] * 100 if A['ny'] else 0
    r['gvRReal'] = A['rr'] / A['ny'] * 100 if A['ny'] else 0
    r['gvEr'] = A['er'] / T
    r['gvErM'] = A['erM'] / T
    r['gvCapYrs'] = S.cap
    r['gvY100'] = S.y100 or T + 1
    r['gvGuard'] = S.gd
    return r


# ------------------------------------------------------------------ bargaining's tallies
def bg_new():
    return NS(wy=0.0, ay=0.0, O=0.0, R=0.0, E=0.0, cap=0.0, md=0.0, mdW=0.0, lg=0.0, lgB=0.0, Kc=0.0, L=[], yIdx=None, T=None)


def bg_acc(R, a, yr, T, E0, g, O, Ef, Rp, Eg, idx):
    S = R.BGS
    w = float(a._w) if a._w is not None else 1
    S.yIdx = idx
    if yr == T - 1:
        S.L.append([O / Ef * 100 if Ef > 0 else 0, w])
    if yr < 1:
        return
    B = R.BARGAIN
    S.wy += w
    S.O += w * O / idx
    S.R += w * E0 * g / idx
    S.E += w * Eg / idx
    if g > 0 and g >= 1 / B['m'] - 1 - 1e-12:
        S.cap += w
    S.md += w * E0 * B['m'] * (1 + g)
    S.mdW += w * E0
    lr = math.log(max(1e-12, Rp)) + math.log(1 + g)
    if lr > 0:
        S.lg += w * E0 * lr
        S.lgB += w * E0 * math.log(1 + g)


def bg_year(R, agents, yr, idx):
    S = R.BGS
    if not S or yr < 1:
        return
    for a in agents:
        w = float(a._w) if a._w is not None else 1
        S.ay += w
        S.Kc += w * _p(a.yrCapUSD) / idx


def bg_q(L, p):
    if not L:
        return 0
    v = sorted(L, key=lambda x: x[0])
    W = 0.0
    for x in v:
        W += x[1]
    c = 0.0
    for x in v:
        c += x[1]
        if c >= p * W - 1e-12:
            return x[0]
    return v[-1][0]


def bg_res(R, out):
    S = R.BGS
    n = S.wy if S.wy > 0 else 1
    B = R.BARGAIN
    out['bgN'] = S.wy / S.ay * 100 if S.ay > 0 else 0
    out['bgO'] = S.O / n
    out['bgR'] = S.R / n
    out['bgE'] = S.E / n
    out['bgSh'] = S.lgB / S.lg * 100 if S.lg > 0 else 0
    out['bgCap'] = S.cap / n * 100
    out['bgMd'] = S.md / S.mdW * 100 if S.mdW > 0 else B['m'] * 100
    out['bgOP10'] = bg_q(S.L, 0.1)
    out['bgOP50'] = bg_q(S.L, 0.5)
    out['bgOP90'] = bg_q(S.L, 0.9)
    out['bgK'] = S.R / S.Kc * 100 if S.Kc > 0 else 0
    return out
