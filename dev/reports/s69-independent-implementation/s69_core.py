"""S69: a whole run (tbRunCore, tbRun), the supply path (tbBaseS, 13.2 fx.sp) and the per-seed pair (tbStudy's loop for one seed)."""
import math
from s69_engine import NS, INF
from s69_rng import median_of, gini_of
from s69_run import Run
from s69_year import run_year
import s69_report as RP
import s69_prog as PG


def run_core(state, tables, p, seed, o, S, tau0, yMax, spd=None):
    R = Run(state, tables, p, seed, o, S, tau0, yMax, spd)
    R.setup()
    C = R.CFG
    agents = R.agents
    T = p['years']
    CALM0 = NS(active=False, incomeMultiplier=1.0, yearsLeft=0)
    PGl = 1.0
    path = []
    wbPrev = 0.0
    L = dict(pjg=0.0, cost=0.0, cash=0.0, endow=0.0, bu=0.0, conv=0.0, cutPT=0.0, cutG=0.0, cap=0.0, pth=0.0, tax=0.0, need=0.0, treas=0.0, f0=0, f1=0.0, f2=0.0, n=0,
             endowTot=0.0, need0=0.0, base0=0.0, pd=0.0, tgt=0.0, emp=0, hrs=0.0, Er=0.0, bR=0, bP=0, bz=0.0, es=0.0, n1=0, nP1=0, nN1=0, pyP=0.0, pyN=0.0, nWP1=0, esWP=0.0,
             convM=0.0, buIss=0.0, ctax=0.0, cutFree=0.0, bkP=0.0, bkU=0.0, bkY=0.0, ntR=0.0)
    epD0 = housing_distress_y0(R, agents)
    epSum = 0.0
    BG = RP.blei_acc()
    dbt20 = 0
    R52 = RP.rep_acc() if o['rep52'] else None
    comp = R.PRICE.comp
    for yr in range(yMax):
        R.PRICE.acc = NS(n=0, essD=0.0, unmet=0.0, basketOwn=0.0, unmetN=0, Y=0.0, Yw=0.0, ptfN=0, conv=0.0, pthLiq=0.0, wageBonus=0.0, wageBonusNS=0.0, slk=0)
        recSt = R.recPath[yr] if R.recPath else CALM0
        run_year(R, agents, yr, p, recSt)
        RP.blei_year(R, BG, agents, p, o, yr == T - 1, yr == 19)
        epY = None
        if not o.get('noEP'):
            epY = extreme_poverty(R, housing_distress(agents), epD0, p)
            epSum += epY / 100 if epY is not None else 0
        if R52:
            RP.rep_year(R, R52, agents, p, o, yr, T, epY if (not o.get('noEP') and epY is not None) else None)
        if R.DMS:
            RP.dm_year(R, R.DMS, agents, p, o, yr, T)
        if R.RTR is not None:
            RP.rt_rep(R, R.RTR, agents, o, yr, T)
        if R.WTS is not None:
            RP.wt_rep(R, R.WTS, agents, o, yr, T)
        if R.BGS:
            RP.bg_year(R, agents, yr, R.BGS.yIdx if R.BGS.yIdx is not None else 1)
        if R.RHH:
            RP.hh_rep_year(R, R.RHH, agents, p, o, yr, T)
        if yr == 19:
            dbt20 = debt_share(R, agents)
        A = R.PRICE.acc
        Cc = R.TB.cur
        d = A.essD / A.n if A.n else 1
        tauUsed = R.TB.tau
        if R.SPD is not None and yMax >= T:
            R.SPD.append(d)
        wbInc = A.wageBonusNS - wbPrev
        wbPrev = A.wageBonusNS
        extra = (0) + (1 - o['aw']) * wbInc
        if o.get('floorUnmatched') or o.get('awLevel'):
            raise NotImplementedError('floorUnmatched/awLevel')
        if yr == 0:
            L['endowTot'] = Cc.endow
        L['pjg'] += Cc.pjg
        gRun = bool(R.PROJ and R.PROJ.get('giftFin') == 'run')
        if gRun:
            raise NotImplementedError('giftFin run')
        need = Cc.cash + L['endowTot'] / T + (0 if o['fin'] == 'source' else Cc.bu) + (0 if o['fin'] in ('hybrid', 'source') else Cc.conv) + Cc.cap + (1 - o['eP']) * (Cc.cutPT - Cc.cutFree + Cc.cutG) + Cc.pthLiq
        bkP = bkU = 0
        if o['fin'] == 'money':
            raise NotImplementedError('fin money')
        elif o['fin'] == 'tax':
            U = extra + (0 if not o.get('taxBase') else None)
        elif o['fin'] == 'source':
            cvS = Cc.conv
            bkP = (Cc.bu if not o.get('faceM') else 0) + cvS - Cc.convM
            bkU = (1 - o['a']) * bkP
            if o.get('aK') or o.get('bkm'):
                raise NotImplementedError('aK/bkm')
            U = bkU + extra
            L['bkP'] += bkP / Cc.idx
            L['bkU'] += bkU / Cc.idx
            L['bkY'] += A.Yw / Cc.idx
        else:
            raise NotImplementedError('fin ' + str(o['fin']))
        if R.FX and R.FX.get('fin'):
            L['yr'] = yr
            U = RP.fin_step(R, L, o, Cc, A, need, U, extra, gRun, bkP if o['fin'] == 'source' else 0, bkU if o['fin'] == 'source' else 0, T, tauUsed)
        if R.GVS:
            RP.gv_step(R, R.GVS, o, Cc, need, agents, yr, T, R.recPath[yr].incomeMultiplier if R.recPath else 1, tauUsed)
        if R.MFS:
            RP.mf_year(R.MFS, Cc, U, A.Y)
        if yr == 0:
            L['need0'] = need
            L['base0'] = Cc.base
        if R.MULT and R.MLS:
            R.MLS.push = max(0, Cc.bu + Cc.conv - Cc.ctax) if o['fin'] == 'source' else None
            if o['fin'] != 'source':
                raise NotImplementedError('MULT push')
        idx = Cc.idx
        L['cost'] += (Cc.cash + Cc.endow + Cc.bu + Cc.conv + Cc.cap + Cc.cutPT - Cc.cutFree + Cc.cutG + Cc.pthLiq) / idx
        L['cutFree'] += Cc.cutFree / idx
        L['cash'] += Cc.cash / idx
        L['endow'] += Cc.endow / idx
        L['bu'] += Cc.bu / idx
        L['conv'] += Cc.conv / idx
        L['cutPT'] += Cc.cutPT / idx
        L['cutG'] += Cc.cutG / idx
        L['cap'] += Cc.cap / idx
        L['pth'] += Cc.pthLiq / idx
        L['pd'] += Cc.pd / idx
        L['tgt'] += Cc.tgt / idx
        L['tax'] += Cc.tax / idx
        L['need'] += need / idx
        L['treas'] += (Cc.tax - need) / idx
        L['f0'] += Cc.f0
        L['f1'] += Cc.f1
        L['f2'] += Cc.f2
        L['n'] += Cc.n
        L['emp'] += Cc.emp
        L['hrs'] += Cc.hrs
        L['Er'] += Cc.E / idx
        L['bR'] += Cc.bR
        L['bP'] += Cc.bP
        L['convM'] += Cc.convM / idx
        L['buIss'] += Cc.buIss / idx
        L['ctax'] += Cc.ctax / idx
        L['bz'] += Cc.bz / idx
        L['es'] += Cc.es / idx
        L['pyP'] += Cc.pyP / idx
        L['pyN'] += Cc.pyN / idx
        L['esWP'] += Cc.esWP / idx
        L['n1'] += Cc.n1
        L['nP1'] += Cc.nP1
        L['nN1'] += Cc.nN1
        L['nWP1'] += Cc.nWP1
        if o['fin'] in ('tax', 'hybrid', 'source'):
            if o.get('taxBase') == 'prog':
                raise NotImplementedError('prog')
            if Cc.base > 0:
                R.TB.tau = min(R.TB.capE, RP.gv_target(R, need) / Cc.base) if R.GOV else min(o['tauMax'], need / Cc.base)
            else:
                R.TB.tau = 0
        PGn = PGl * (1 + o['lamG'] * U / A.Y) if A.Y > 0 else PGl
        capShare = o['ptfCap'] * (A.ptfN / A.n if A.n else 0)
        PE = {}
        for k in C['ESSENTIALS']:
            cut = 0
            if p['ptf']:
                cut = PG.ptf_mode_cut(R, p, k)
            if not S or o['essMatched']:
                PE[k] = 1
                continue
            if o['supply'] == 'baseline':
                raise NotImplementedError('supply baseline')
            sRef = S[0] * math.pow(1 + o['gS'], yr)
            dEff = sRef + max(0, d - sRef) - max(0, S[yr] - sRef)
            s_ = sRef * (1 + capShare * cut)
            PE[k] = max(0, 1 + o['theta'][k] * (dEff - s_) / s_) if s_ > 0 else 1
        wyN = len(R.PRS.y) if R.PRS else 0
        if R.PRS:
            PGn = RP.pr_step(R, R.PRS, U, A.Y, o['lamG'], R.PRICE.wIdx, R.PRICE.piG, R.PRICE.bIdx, A.slk or 0, yr, PGn)
        if R.WYS:
            RP.wy_year(R.WYS, math.exp(R.PRS.y[-1].get('avg') or 0) if (R.PRS and len(R.PRS.y) > wyN) else 1)
        path.append(NS(bIdx=R.PRICE.bIdx, PG=PGl, U=U, Y=A.Y, tau=tauUsed, colaLevel=R.PRICE.colaLevel, full=Cc.idx))
        R.PRICE.piG = PGn / PGl - 1
        PGl = PGn
        for k in C['BASKET_KEYS']:
            comp[k] = PE[k] * (PGl if o['pgOnE'] else 1) if k in C['ESSENTIALS'] else PGl
        b = 1.0
        for k in C['BASKET_KEYS']:
            b += C['BASKET'][k] * (comp[k] - 1)
        R.PRICE.bIdx = b
    if yMax < T:
        if R.GOV:
            return dict(tau0=min(R.gvCap, R.GOV['sh'] * L['need0'] / L['base0']) if L['base0'] > 0 else 0)
        return dict(tau0=min(o['tauMax'], L['need0'] / L['base0']) if L['base0'] > 0 else 0)
    return results(R, agents, p, o, T, L, path, BG, R52, epSum, dbt20)


def housing_distress(agents):
    if not agents or agents[0].yrWealthStartUSD is None:
        return None
    n = 0
    for a in agents:
        inc = _f(a.yrWageUSD) + _f(a.yrConvUSD) + _f(a.yrSSUSD)
        w = _f(a.yrWealthStartUSD)
        if inc + max(0, w) < _f(a.yrCostUSD):
            n += 1
    return n / len(agents)


def _f(x):
    return 0 if (x is None or x != x) else x


def housing_distress_y0(R, agents):
    n = 0
    for a in agents:
        inc = max(a.wage, 0) * 12 * R.CFG['WAGE_TO_USD']
        w = a.wealth
        if inc + max(0, w) < R.CFG['LIVING_WAGE_ANNUAL']:
            n += 1
    return n / len(agents)


def extreme_poverty(R, d, d0, p):
    """Appendix C, item 29; returns the total (%)."""
    if d is None or d != d or not (d0 > 0):
        return None
    C = R.CFG
    Rr = C['EP_Y0_RATE']
    s = C['EP_SMI_SHARE']
    v = C['EP_VOL_SHARE']
    wz = C['EP_WZ_EFFECT'] * max(0, min(1, p['szhCoh'] or 0)) if (p['pth'] and p['szh']) else 0
    econ = Rr * (1 - s - v) * d / d0
    smi = Rr * s * (1 - wz)
    vol = Rr * v
    return (econ + smi + vol) * 100


def debt_share(R, agents):
    n = k = 0
    if R.HHS and R.HHS.list:
        for H in R.HHS.list:
            if not H.a:
                continue
            w = 0.0
            for a in H.a:
                w += a.wealth
            n += 1
            if w < 0:
                k += 1
    else:
        for a in agents:
            n += 1
            if a.wealth < 0:
                k += 1
    return k / n * 100 if n else 0


def results(R, agents, p, o, T, L, path, BG, R52, epSum, dbt20):
    C = R.CFG
    n = len(agents)
    NY = n * T
    full = agents[0].yrBasketUSD / C['LIVING_WAGE_ANNUAL'] / (agents[0]._hhF or 1)
    lineF = 1 if o['lines'] == 'nominal' else full
    PL = C['POVERTY_LINE']
    L30 = C['BLEI_PRECARIOUS_MAX']
    pov = bpov = nbpov = g0 = 0
    g1 = g2 = 0.0
    for a in agents:
        if a.wealth < PL * lineF:
            pov += 1
        if R.agent_blei(a, p['bu'], p['ccoOn'], p['pth'], p['szh'], p['szhCoh'], p['ptf']) / lineF < L30:
            bpov += 1
        if (R.blei0(a) + (a._tbM or 0) / C['BASE_DAILY_COST']) / lineF < L30:
            nbpov += 1
        g = a._tbGap or 0
        if g > 0:
            g0 += 1
        g1 += g
        g2 += g * g

    def grp(f):
        m = k = f0 = f2 = wp = 0
        m = 0.0
        f0 = 0.0
        f2 = 0.0
        for a in agents:
            if f(a):
                k += 1
                m += a._tbRes / a._tbYrs
                f0 += a._tbF0 / a._tbYrs
                f2 += (a._tbF2 or 0) / a._tbYrs
                if a.wealth < PL * lineF:
                    wp += 1
        return dict(res=m / k, f0=f0 / k * 100, f2=f2 / k * 100, wp=wp / k * 100, k=k) if k else dict(res=0, f0=0, f2=0, wp=0, k=0)
    gP = grp(lambda a: a._tbPart)
    gN = grp(lambda a: not a._tbPart)
    gH = grp(lambda a: a._tbPTH)
    gL = grp(lambda a: a._tbLow)
    gT = grp(lambda a: a._tbTop)
    sp = spY = ever = chron = 0
    for a in agents:
        sp += a._tbSp or 0
        spY += a._tbF0 or 0
        if (a._tbF0 or 0) > 0:
            ever += 1
        if (a._tbF0 or 0) >= T / 2:
            chron += 1
    gcF = n / (n - 1) if (o['giniNN1'] and n > 1) else 1
    giniD = gini_of([a._tbDisp for a in agents]) * gcF
    giniX = gini_of([a._tbExt for a in agents]) * gcF
    pT = path[T - 1]
    p10 = path[min(T - 1, 9)]
    realT = (pT.colaLevel if p['cola'] else 1) / pT.full
    bI = path[T - 1].bIdx
    mx = 0
    for t in range(1, T):
        mx = max(mx, path[t].bIdx / path[t - 1].bIdx - 1)
    tauS = 0.0
    for q in path:
        tauS += q.tau
    lab = R.labAcc
    r = {}
    r['endoAnn'] = math.pow(bI, 1 / (T - 1)) - 1
    r['endoMax'] = mx
    r['pov'] = pov / n * 100
    r['bleiPov'] = bpov / n * 100
    r['nbleiPov'] = nbpov / n * 100
    r['tgt'] = L['tgt'] / L['pd'] if L['pd'] > 0 else 0
    r['medWealthReal'] = median_of([a.wealth for a in agents]) / full
    r['fgt0'] = g0 / n * 100
    r['fgt1'] = g1 / n * 100
    r['fgt2'] = g2 / n * 100
    r['fgt0PY'] = L['f0'] / L['n'] * 100
    r['fgt1PY'] = L['f1'] / L['n'] * 100
    r['fgt2PY'] = L['f2'] / L['n'] * 100
    r['cost'] = L['cost'] / NY
    r['cCash'] = L['cash'] / NY
    r['cEndow'] = L['endow'] / NY
    r['cBU'] = L['bu'] / NY
    r['cConv'] = L['conv'] / NY
    r['cCut'] = (L['cutPT'] + L['cutG']) / NY
    r['cCap'] = L['cap'] / NY
    r['cPth'] = L['pth'] / NY
    r['tax'] = L['tax'] / NY
    r['need'] = L['need'] / NY
    r['treas'] = L['treas'] / NY
    r['tauMean'] = tauS / T
    r['tauLast'] = path[T - 1].tau
    r['dE'] = (lab['E'] - lab['E0']) / lab['E0'] if (lab and lab['E0'] > 0) else 0
    r['E'] = lab['E'] / max(1, lab['n']) if lab else 0
    r['E0'] = lab['E0'] / max(1, lab['n']) if lab else 0
    r['zero'] = lab['zero'] / max(1, lab['n']) if lab else 0
    for nm, g in (('Part', gP), ('Non', gN), ('Pth', gH), ('Low', gL), ('Top', gT)):
        r['g' + nm + 'Res'] = g['res']
        r['g' + nm + 'F0'] = g['f0']
        r['g' + nm + 'W'] = g['wp']
    r['pyPoor'] = spY / n
    r['everPoor'] = ever / n * 100
    r['spellMean'] = spY / sp if sp > 0 else 0
    r['chronic'] = chron / n * 100
    r['emp'] = L['emp'] / L['n'] * 100
    r['hrs'] = L['hrs'] / L['n'] - 1
    r['Er'] = L['Er'] / NY
    r['giniD'] = giniD
    r['giniX'] = giniX
    r['pLev10'] = p10.full
    r['pLev20'] = pT.full
    r['realT'] = realT
    r['bleiR'] = L['bR'] / L['n'] * 100
    r['bleiP'] = L['bP'] / L['n'] * 100
    PG.prog_results(R, r, L, T, n, NY)
    r['bzPay'] = L['bz'] / L['n1'] if L['n1'] else 0
    r['esPrem'] = L['es'] / L['n1'] if L['n1'] else 0
    r['payPart'] = L['pyP'] / L['nP1'] if L['nP1'] else 0
    r['payNon'] = L['pyN'] / L['nN1'] if L['nN1'] else 0
    r['esPremW'] = L['esWP'] / L['nWP1'] if L['nWP1'] else 0
    r['gPartF2'] = gP['f2']
    r['gNonF2'] = gN['f2']
    r['gPartK'] = gP['k']
    r['gNonK'] = gN['k']
    r['srcIss'] = L['buIss'] / NY
    r['srcPay'] = (L['bu'] + L['conv']) / NY
    r['srcTax'] = L['ctax'] / NY
    r['srcM'] = L['convM'] / NY
    r['srcCover'] = L['ctax'] / L['buIss'] * 100 if L['buIss'] > 0 else 0
    r['pdMatch'] = L['convM'] / L['conv'] * 100 if L['conv'] > 0 else 0
    r['csFree'] = L['cutFree'] / NY
    r['epPY'] = epSum / T * 100
    for k in ('agRet', 'agAge0', 'agAge', 'agDeaths', 'agBorn', 'svInt', 'svIntR', 'hcM', 'rvX', 'rvC'):
        r[k] = 0
    r['bkA'] = (1 - L['bkU'] / L['bkP']) * 100 if L['bkP'] > 0 else 0
    r['bkPY'] = L['bkP'] / L['bkY'] * 100 if L['bkY'] > 0 else 0
    r['mlNT'] = L['ntR'] / NY
    r['taxAvg'] = L['tax'] / L['Er'] * 100 if L['Er'] > 0 else 0
    r['hhDebt20'] = dbt20
    r['hhDebt40'] = 0
    np_ = [a for a in agents if a.inCCO]
    s_ = 0
    for a in agents:
        s_ += a.octave if a.inCCO else 0
    r['octMean'] = s_ / max(1, len(np_))
    RP.blei_res(R, BG, r)
    RP.rep_res(R, R52, r)
    RP.hh_res(R, R.RHH, r)
    lf_res(R, r)
    em = {}
    if R.EMPL and R.EMS:
        empl_res(R, em)
    PG.prog_res_parts(R, em, NY, L, grp(lambda a: bool(a._inel)))
    if R.FX and R.FX.get('fin'):
        RP.fin_res(em, L.get('fi'), NY)
    if R.GVS:
        RP.gv_res(R, em, R.GVS, NY, T)
    if R.WYS:
        RP.wy_res(em, R.WYS)
    if R.SNET and R.SNS:
        sn_res(R, em)
    if R.DMS:
        RP.dm_res(em, R.DMS)
    if R.RTR is not None:
        em.update(R.RTR)
    if R.WTS is not None:
        em.update(R.WTS)
    if R.PRS:
        RP.pr_res(R, em, R.PRS, agents, lineF)
    if R.MFS:
        RP.mf_res(em, R.MFS, NY)
    r.update(em)
    r['_tinyEarn'] = R.tiny
    for t in range(40):
        r['plv_' + str(t)] = path[t].full if t < len(path) else 0
    return r


def empl_res(R, out):
    A = R.EMS
    out['emUrate'] = A.weeks / 52 / A.n * 100 if A.n else 0
    out['emSpells'] = A.spells / A.n * 100 if A.n else 0
    out['emWeeks'] = A.weeks / A.out if A.out else 0
    out['emAuto'] = A.auto / A.n * 100 if A.n else 0
    out['emUI'] = A.ui / A.lost * 100 if A.lost > 0 else 0
    out['emCut'] = A.cut / A.cutN * 100 if A.cutN else 0
    out['emLong'] = A.long / A.spells * 100 if A.spells else 0
    out['emRho'] = A.rho
    return out


def sn_res(R, out):
    A = R.SNS.acc
    ay = A['ay'] or 1

    def pc(x):
        return x / ay * 100
    out['snSnap'] = pc(A['snapN'])
    out['snEitc'] = pc(A['eitcN'])
    out['snCtc'] = pc(A['ctcN'])
    out['snSnapM'] = A['snap'] / ay
    out['snEitcM'] = A['eitc'] / ay
    out['snCtcM'] = A['ctc'] / ay
    out['snAll'] = out['snSnapM'] + out['snEitcM'] + out['snCtcM']
    out['snMtr'] = A['m'] / A['mN'] * 100 if A['mN'] else 0
    out['snKids'] = A['kN'] / A['ky'] * 100 if A['ky'] else 0
    if R.SNET.get('abawd'):
        out['snAbN'] = pc(A['abN'])
        out['snAbM'] = A['abM'] / ay
        out['snAbLost'] = A['abL'] / ay
    return out


def lf_res(R, out):
    if R.BGS:
        RP.bg_res(R, out)
    if R.DR_ACC:
        D = R.DR_ACC
        out['drHit'] = D.h / D.n * 100 if D.n else 0
        out['drCut'] = D.c / D.h if D.h else 0
    S = R.LFS
    if not S:
        return out
    k = S.k
    m = k['dis'] + k['ret'] + k['care'] + k['sch']
    n = max(1, S.n)
    out['lfShare'] = m / n * 100
    out['lfDis'] = k['dis'] / n * 100
    out['lfRet'] = k['ret'] / n * 100
    out['lfCare'] = k['care'] / n * 100
    out['lfSch'] = k['sch'] / n * 100
    out['lfInc0'] = S.inc / m if m else 0
    out['lfZero'] = S.z / m * 100 if m else 0
    if S.ac:
        A = S.ac
        x = A.ex or 1
        Tn = len(A.ayY) - 1
        out['lfOut0'] = (A.outY[0] or 0) / A.ayY[0] * 100 if (A.ayY and A.ayY[0]) else 0
        out['lfOut'] = A.out / A.ay * 100 if A.ay else 0
        out['lfOutL'] = (A.outY[Tn] or 0) / A.ayY[Tn] * 100 if (Tn >= 1 and A.ayY[Tn]) else 0
        out['lfEx'] = A.ex / A.iy * 100 if A.iy else 0
        out['lfRt'] = A.rt / A.oy * 100 if A.oy else 0
        out['lfEver'] = (k['dis'] + k['ret'] + k['care'] + k['sch'] + A.ev) / max(1, S.n) * 100
        out['lfExDis'] = A.k['dis'] / x * 100
        out['lfExRet'] = A.k['ret'] / x * 100
        out['lfExCare'] = A.k['care'] / x * 100
        out['lfExSch'] = A.k['sch'] / x * 100
        out['lfPart'] = A.pt / A.ay * 100 if A.ay else 0
        out['lpOut'] = A.lp / A.ay * 100 if A.ay else 0
        out['lpE'] = A.lpE / A.ay if A.ay else 0
    return out


def tb_run(state, tables, p, seed, o, S, spd=None):
    """tbRun: the year-0 contribution from a complete one-year pre-pass (12.5; Appendix C, item 17), then the run."""
    tau0 = run_core(state, tables, p, seed, o, S, 0, 1)['tau0'] if (o['fin'] in ('tax', 'hybrid', 'source') and p.get('tb') is not None) else 0
    return run_core(state, tables, p, seed, o, S, tau0, p['years'], spd)
