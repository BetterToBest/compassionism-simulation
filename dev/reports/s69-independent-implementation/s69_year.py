"""S69: one simulated year (runYear), in section 5's order. The programme's own steps are in s69_prog.py."""
import math
from s69_engine import NS, INF
import s69_report as RP
import s69_prog as PG


def run_year(R, agents, yr, p, recSt):
    C = R.CFG
    PR = R.PRICE
    W2U = C['WAGE_TO_USD']
    LWA = C['LIVING_WAGE_ANNUAL']
    POFF = R.PATHWAY_OFF
    AUD = R.AUD
    HO = R.HOUSEHOLDS
    HHON = bool(HO) and bool(R.HHS) and (R.CONVERSION_MODEL == 'framework' or not p['ccoOn'])
    HHPOOL = HHON and HO.get('pool') != 'individual'
    if HHON:
        R.hh_year(agents)
    Y = NS()  # the year's shared values, read by the programme's steps
    Y.yr = yr
    Y.pthApprBonus = p['szhCoh'] * 0.01 if p['szh'] else 0
    szhThetaVal = PG.szh_theta(R, p['szhCoh']) if p['szh'] else 0
    if R.PAS:
        PG.pa_year(R, agents, yr, p)
    if R.THETA_GATE == 'density':
        tdN = 0
        if p['ptf'] and not R.PAS:
            raise NotImplementedError('theta density without open access')
        R.THETA_DENS = (PG.po_t_pop(R) if R.POS else PG.pa_pop_share(R)) if R.PAS else tdN / max(1, len(agents))
        szhThetaVal = PG.szh_theta(R, R.THETA_DENS) if p['szh'] else 0
    Y.ptfConvBonus = 1.30 + (szhThetaVal if (p['szh'] and p['ptf']) else 0)
    Y.szhPartBoost = szhThetaVal * 0.16 if (p['szh'] and p['ccoOn']) else 0
    Y.szhThetaVal = szhThetaVal
    ptfAdoptFrac = 0
    if R.PTFS and R.PFS and p['ptf']:
        PG.ptfs_year(R, agents, yr)
    if p['ptf'] and p['ptfShare'] > 0:
        c0 = 0
        for a in agents:
            if a.inPTF:
                c0 += 1
        ptfAdoptFrac = c0 / max(1, len(agents))
    Y.ptfAdoptFrac = ptfAdoptFrac
    inflRate = p['inflRate'] or 0
    if p['ptf'] and inflRate > 0 and not (PR and PR.noDamp):
        raise NotImplementedError('PTF damping')
    if p['pth'] and inflRate > 0 and not (PR and PR.noDamp):
        raise NotImplementedError('PTH damping')
    gI = math.pow(1 + inflRate, yr)
    dollarCost = C['BASE_DAILY_COST'] * 365 * gI
    if PR:
        dollarCost *= PR.bIdx
    popShock = recSt.incomeMultiplier if recSt.active else 1.0
    E = R.EMPL
    if E and E.get('rec') == 'replace' and recSt.active:
        popShock = 1 - max(0, (1 - popShock) - (C['EMPL_P_REC'] * C['EMPL_W_REC'] - C['EMPL_P'] * C['EMPL_W']) / 52)
    mlNT = 0
    if R.MULT and R.TB and p['tb'] is not None:
        popShock = PG.mult_year(R, agents, yr, recSt, popShock)
    if R.PRS and PR and PR.acc:
        PR.acc.slk = max(0, 1 - popShock) if recSt.active else 0
    if p['ptf'] and p['ptfCap']:
        raise NotImplementedError('ptfCap')
    PG.prod_year(R, agents, yr, p, Y)
    popAIDisp = 0
    if p['automation']:
        if yr >= C['AI_DISPLACEMENT_YEAR_2']:
            popAIDisp = C['AI_DISPLACEMENT_RATE_1'] * (C['AI_DISPLACEMENT_YEAR_2'] - C['AI_DISPLACEMENT_YEAR_1']) + C['AI_DISPLACEMENT_RATE_2'] * (yr - C['AI_DISPLACEMENT_YEAR_2'] + 1)
        elif yr >= C['AI_DISPLACEMENT_YEAR_1']:
            popAIDisp = C['AI_DISPLACEMENT_RATE_1'] * (yr - C['AI_DISPLACEMENT_YEAR_1'] + 1)
        popAIDisp = min(0.10, popAIDisp)
    if p.get('stab'):
        raise NotImplementedError('stabilisers')
    colaF = gI if (p['cola'] and (p['inflRate'] or 0) > (p['colaThresh'] or 0)) else 1
    if PR:
        pmFull = gI * PR.bIdx
        if p['cola'] and pmFull / PR.lastFull - 1 > (p['colaThresh'] or 0):
            PR.colaLevel = pmFull
        PR.lastFull = pmFull
        colaF = PR.colaLevel if p['cola'] else 1
    if R.C22 and R.C22.get('idx') == 'needs':
        colaF = gI * (PG.c22_share(R, PR.comp) / PG.c22_share(R, None) if PR else 1)
    buEff = p['bu'] * 1 * colaF
    if PR:
        PR.buY = buEff
    agP = gI * (PR.bIdx if PR else 1)
    if R.DEBT_READ or R.LF_SCOPE:
        R.DR_PL = agP
    rtP = None
    if R.RETURNS:
        rtP = gI * (PR.bIdx if PR else 1)
        R.rt_init(agents, rtP, yr)
    tbY = R.tb_year(p, colaF) if (R.TB and p['tb'] is not None) else None
    if R.SNET and R.SNS and tbY:
        R.sn_year(agents, yr, HHON, inflRate)
    if R.PTHB and R.PBS and p['pth']:
        PG.pthb_year(R, agents, yr, agP)
    priceIdx = gI
    if PR:
        priceIdx *= PR.bIdx
    Y.priceIdx = priceIdx
    Y.inflRate = inflRate
    Y.buEff = buEff
    Y.agP = agP
    Y.tbY = tbY
    Y.HHON = HHON
    FWON = R.CONVERSION_MODEL == 'framework'
    Y.FWON = FWON
    PG.join_year(R, agents, yr, p, Y)
    PG.fw_year_start(R, agents, yr, p, Y)
    comp = PR.comp if PR else None
    bI = PR.bIdx if PR else 1
    eShareCur = 0.0
    fShareCur = C['BASKET']['food']
    for k in R.bu_ess():
        eShareCur += C['BASKET'][k] * (comp[k] if PR else 1)
    if PR:
        eShareCur /= bI
        fShareCur = C['BASKET']['food'] * comp['food'] / bI
    rsAlt = R.PTH_MODE != 'basket'
    if not rsAlt:
        raise NotImplementedError('PTH_MODE basket')
    tShareCur = C['BASKET']['taxes'] * (comp['taxes'] / bI if PR else 1) if R.DISC_BASE == 'pretax' else 0
    hShareCur = C['BASKET']['housing'] * (comp['housing'] / bI if PR else 1)
    Y.eShareCur = eShareCur
    Y.fShareCur = fShareCur
    Y.hShareCur = hShareCur
    Y.tShareCur = tShareCur
    Y.c22Cur = PG.c22_share(R, comp if PR else None) / (bI if PR else 1) if R.C22S else 0
    PG.surp_year(R, agents, yr, p, Y)
    SPON = Y.SPON
    PJON = Y.PJON
    ESON = Y.ESON
    LB = R.LABOR
    EMS = R.EMS
    LFS = R.LFS
    DR = R.DEBT_READ
    SG = R.SPEND_GRADE
    RET = R.RETURNS
    FLR = C['WEALTH_FLOOR']
    FX = R.FX
    N7 = R.N7_BLEI
    L30 = C['BLEI_PRECARIOUS_MAX']
    mlcBase = LWA * gI * (PR.bIdx if PR else 1)
    for a in agents:
        if a.wealth != a.wealth:
            a.wealth = 0
        if a.wage != a.wage or a.wage <= 0:
            a.wage = 1
        HHA = HHON and a._hh is not None and not a._hh.single
        eSA = a._hhE if HHA else eShareCur
        fSA = a._hhFd if HHA else fShareCur
        hSA = a._hhH if HHA else hShareCur
        buA = buEff * a._hhBU if HHA else buEff
        dcA = dollarCost * a._hhD if HHA else dollarCost
        HHP = HHPOOL and HHA and len(a._hh.a) > 1
        tShA = a._hhT if HHA else tShareCur
        if HHON:
            a._hhPool = HHP
        if RET:
            R.rt_adult(a, rtP)
        a.yrWealthStartUSD = a.wealth
        rng = R.RNG
        agentVar = 0.90 + rng() * 0.20
        incomeShock = popShock * agentVar
        if HHON and HO.get('shock') and a._hh and len(a._hh.a) > 1:
            if HO['shock'] != 'shore':
                raise NotImplementedError('household shock reading')
            hsR = C['HH_SHOCK_CORR'][1 if recSt.active else 0]
            hsA = min(1, abs(hsR))
            hsS = -1 if (hsR < 0 and a._hh.a[1] is a) else 1
            agentVar = 1 + math.sqrt(hsA) * hsS * (a._hh.hv - 1) + math.sqrt(1 - hsA) * (agentVar - 1)
            incomeShock = popShock * agentVar
            a._shkV = agentVar
            a._shkR = bool(recSt.active)
        uSpendFrac = 0.60 + rng() * 0.30
        uCipQuality = rng()
        uAdvance = rng()
        uSzhInduce = rng()
        uSzhPtfShare = rng()
        uPthAppr = rng()
        uPtfAdopt = rng()
        if LFS and LFS.f:
            R.lf_flow(a, agP, yr)
        if R.LF_SCOPE and a._lf:
            a._ssY = a._ssB0 * agP
        A_ = NS(HHA=HHA, eSA=eSA, fSA=fSA, hSA=hSA, buA=buA, dcA=dcA, HHP=HHP, tShA=tShA, incomeShock=incomeShock, uCipQuality=uCipQuality, uAdvance=uAdvance,
                uSzhInduce=uSzhInduce, uSzhPtfShare=uSzhPtfShare, uPthAppr=uPthAppr, uPtfAdopt=uPtfAdopt)
        if R.GATE_CURRENT and FWON and p['ccoOn'] and a.inCCO and p['bu'] > 0 and not POFF['relief']:
            PG.gate_current(R, a, p, Y, A_)
        bleiCheck = R.agent_blei(a, buA, p['ccoOn'], p['pth'], p['szh'], p['szhCoh'], p['ptf'])
        tbNB = R.tb_gate(a, p, buA, tbY) if tbY else 0
        wg = C['WAGE_BASE_GROWTH']
        bleiGate = tbNB if (tbY and R.TB.neutralGate) else bleiCheck
        if AUD and AUD.get('gate'):
            bleiGate /= priceIdx
        bleiProg = 0
        a._bleiR = 0
        a._bleiP = 0
        if bleiGate > L30 and not POFF['bleiWage']:
            drFactor = 1 / (1 + 0.5 * max(0, a.wage / C['WAGE_MEDIAN_SIU'] - 1))
            wg += C['WAGE_BLEI_BONUS'] * max(0.1, drFactor)
            a._bleiR = 1
            if not (R.blei0(a) / (priceIdx if (AUD and AUD.get('gate')) else 1) > L30):
                a._bleiP = 1
                if N7:
                    bleiProg = C['WAGE_BLEI_BONUS'] * max(0.1, drFactor)
        if not POFF['octaveWage']:
            wg += a.octave * C['WAGE_OCTAVE_BONUS']
        if p['cip']:
            wg += p['cipDemo'] * 0.005
        if LB and a._lwNB is None:
            a._lwNB = a.wage
        if PR:
            if a._wNB is None:
                a._wNB = a.wage
            if PR.wIdx:
                wg += PR.wIdx * PR.piG
        if AUD and AUD.get('wOut'):
            raise NotImplementedError('wOut')
        if not (E and E.get('auto') == 'jobs'):
            wg -= popAIDisp * a.automationRisk
        a.wage = max(a.wage * 0.80, a.wage * (1 + wg))
        if a._ret:
            a.wage = a._ssY / 12 / W2U
            if LB:
                a._lwNB = a.wage
            if PR:
                a._wNB = a.wage
        if LB:
            lbProg = (0 if POFF['octaveWage'] else a.octave * C['WAGE_OCTAVE_BONUS']) + (p['cipDemo'] * 0.005 if p['cip'] else 0) + bleiProg
            a._lwNB = max(a._lwNB * 0.80, a._lwNB * (1 + wg - lbProg))
        if PR:
            pmProg = (0 if POFF['octaveWage'] else a.octave * C['WAGE_OCTAVE_BONUS']) + (p['cipDemo'] * 0.005 if p['cip'] else 0) + bleiProg
            a._wNB = max(a._wNB * 0.80, a._wNB * (1 + wg - pmProg))
        # 7. cost factor: PTF and PTH price cuts (the 'housing' / 'pretax' chain)
        cf = 1.0
        rsPtfU = 1
        if p['ptf'] and (a.inPTF or R.PAS):
            rsPtfU = 1 - PG.ptfs_cut(R, a, HHA, p)
            cf = tShA + (cf - tShA) * rsPtfU if R.DISC_BASE == 'pretax' else cf * rsPtfU
        cfPTF = cf
        if p['pth'] and a.inPTH and not POFF['pthCost']:
            cf -= C_PTH(R) * PG.sx_h(R, hSA) * rsPtfU
        cfPreCCO = cf
        if p['ccoOn'] and a.inCCO and p['bu'] > 0:
            if not POFF['relief'] and not FWON:
                raise NotImplementedError('engine-model relief')
        hcX = 0
        mainLoopCostUSD = mlcBase
        if HHA:
            mainLoopCostUSD *= a._hhF
        A_.cf = cf
        A_.cfPTF = cfPTF
        A_.cfPreCCO = cfPreCCO
        A_.rsPtfU = rsPtfU
        A_.mlc = mainLoopCostUSD
        if R.C22S and tbY:
            PG.c22_tally(R, a, p, Y, A_)
        fwB = 0
        fwLeft = 0
        if FWON and p['ccoOn'] and a.inCCO and p['bu'] > 0 and not POFF['relief']:
            PG.bu_purchase(R, a, p, Y, A_)
            cf = A_.cf
            fwB = A_.fwB
            fwLeft = A_.fwLeft
        elif SPON:
            PG.bu_no_purchase_cut(R, a, p, Y, A_)
        emQ = None
        emWk = 0
        if E and EMS:
            er = EMS.r
            emU = [er(), er(), er(), er(), er(), er()]
            emWk = a.wage * 12 * W2U * incomeShock / 52
            if not a._ret:
                emQ = R.empl_year(a, recSt.active, popAIDisp, emU, emWk)
        annualWageUSD = 0 if a._ret else a.wage * 12 * W2U * incomeShock * (1 + mlNT)
        if emQ:
            annualWageUSD *= 1 - emQ.out
        tbG = 0
        tbPT = 0
        if tbY and R.POS and p['ptf']:
            PG.po_free_year(R, a, mainLoopCostUSD, cfPTF, fSA, hSA)
        elif tbY and R.COST:
            raise NotImplementedError('COST without po')
        if tbY:
            tbPT = mainLoopCostUSD * (1 - cfPreCCO)
        if LB:
            lbE0 = annualWageUSD
            lbBU = 0
            lbR = 0
            lbC = a._labC or 0
            lbU = p.get('ubi') or 0
            if p['ccoOn'] and a.inCCO and p['bu'] > 0 and not POFF['relief']:
                if FWON:
                    lbBU = fwB
                    lbR = fwLeft
                else:
                    raise NotImplementedError('engine-model BU')
            lbBiz = 0
            if FWON and R.FWS and R.FWS.prev and R.FWS.prev.wSum > 0:
                lbBiz = max(0, R.FWS.prev.bizNet) / R.FWS.prev.wSum
            if SPON:
                lbBiz = (Y.spProfW if a._spWk else 0) + Y.spRestW
            base = 1 if (LFS and a._lf and not (a._lwNB > 0)) else a.wage / a._lwNB
            lbRaise = math.pow(max(1, base) * (1 + lbBiz) * ((1 + a._esX) if ESON else 1), LB.eps - LB.rho)
            tbQ = R.tb_lab(a, tbY, lbE0, tbPT + tbG + ((a._spCutY or 0) if SPON else 0)) if tbY else None
            if tbQ:
                lbRaise *= tbQ.F
            lbInc = LB.rho * lbU + LB.rhoBU * lbBU + LB.rhoR * lbR + LB.rho * (1 - LB.delta) * lbC + (LB.rho * tbQ.V if tbQ else 0)
            lbDisp = LB.delta * lbC + (tbQ.D if tbQ else 0)
            if SPON and a._spOwn > 0:
                lbInc += LB.rho * a._spOwn
            if emQ:
                lbInc *= 1 - emQ.out
                lbDisp *= 1 - emQ.out
            bgG = 0
            BG = R.BARGAIN
            if BG and lbE0 > 0 and not a._ret:
                bgO = lbU + (LB.rhoBU / LB.rho if LB.rho > 0 else 1) * lbBU + (LB.rhoR / LB.rho if LB.rho > 0 else 0) * lbR + (1 - LB.delta) * lbC + (tbQ.O if tbQ else 0) + (a._spOwn if (SPON and a._spOwn > 0) else 0)
                bgEf = a.wage * 12 * W2U * incomeShock * (1 + mlNT)
                bgG = (min(BG['pi'] * bgO / bgEf, 1 / BG['m'] - 1) if (bgEf > 0 and bgO > 0 and BG['pi'] > 0) else 0)
                a._bgG = bgG
                if R.POS:
                    R.POS.gN += lbE0 * bgG
                    R.POS.gD += lbE0
                bgE1 = max(0, lbE0 * lbRaise - lbInc - lbDisp)
                if bgG > 0:
                    raise NotImplementedError('bargained raise above 0')
                if R.BGS:
                    Rp = max(1, (1 if (LFS and a._lf and not (a._lwNB > 0)) else a.wage / a._lwNB)) * (1 + lbBiz) * ((1 + a._esX) if ESON else 1)
                    RP.bg_acc(R, a, yr, R.BGS.T, lbE0, bgG, bgO, bgEf, Rp, max(0, lbE0 * lbRaise - lbInc - lbDisp) - bgE1, gI * (PR.bIdx if PR else 1))
            elif BG:
                a._bgG = 0
            if LFS and LFS.pm > 0 and lbE0 > 0 and not a._ret:
                Lp = (LB.rho * lbU + LB.rhoBU * lbBU + LB.rhoR * lbR + LB.rho * (1 - LB.delta) * lbC + (LB.rho * tbQ.O if tbQ else 0) + (LB.rho * a._spOwn if (SPON and a._spOwn > 0) else 0)) * ((1 - emQ.out) if emQ else 1)
                annualWageUSD = R.lf_pm(a, lbE0 * lbRaise - lbDisp, lbInc, Lp, emQ, yr, agP)
            else:
                annualWageUSD = max(0, lbE0 * lbRaise - lbInc - lbDisp)
            a._lbE0 = lbE0 * (1 + bgG) if bgG > 0 else lbE0
            if 0 < annualWageUSD < 1e-6 or (annualWageUSD == 0 and lbE0 > 0 and LFS and LFS.pm > 0 and a._lpU is not None and not (a._lpU < LFS.pm)):
                R.tiny += 1  # diagnostic only: an adult-year whose earnings are zero in exact arithmetic, so rounding decides 'worked'
            if LFS and LFS.ac:
                R.lf_acc(a, annualWageUSD, yr)
            LA = LB.acc
            if tbQ and LA is not None:
                LA['cash'] += LB.rho * tbQ.V
            if LA is not None:
                LA['n'] += 1
                if a.inCCO:
                    LA['nP'] += 1
                LA['E0'] += lbE0
                LA['E'] += annualWageUSD
                LA['raise_'] += lbE0 * (lbRaise - 1)
                LA['cash'] += LB.rho * lbU
                LA['bu'] += LB.rhoBU * lbBU
                LA['buR'] += LB.rhoR * lbR
                LA['rent'] += LB.rho * (1 - LB.delta) * lbC
                LA['disp'] += lbDisp
                LA['C'] += lbC
                LA['U'] += lbU + lbBU
                LA['projH'] += lbDisp / lbE0 if lbE0 > 0 else 0
                if annualWageUSD == 0 and lbE0 > 0:
                    LA['zero'] += 1
        A_.annualWageUSD = annualWageUSD
        if PJON:
            PG.project_hours(R, a, p, Y, A_)
        if R.SNET and R.SNET.get('abawd'):
            abW = emQ.out * 52 if emQ else 0
            abUi = min(abW, emQ.ui / (C['EMPL_UI_REPL'] * emWk)) if (emQ and emWk > 0) else 0
            abB = (a._lbE0 or 0) if LB else annualWageUSD
            abR = (annualWageUSD / abB if LB else 1) if abB > 0 else 0
            a._snAbC = 0 if a._ret else 12 * max(0, (52 if abR < 0.5 else abW) - abUi) / 52
            if FX and FX.get('ab') and a._snAbC < 1e-9:
                a._snAbC = 0
        costUSD = mainLoopCostUSD * cf
        a.wealth += annualWageUSD - costUSD
        if SG and not (AUD and AUD.get('sg')):
            raise NotImplementedError('released graded spending')
        a.yrSSUSD = a._ssY if a._ret else 0
        if a._ret:
            a.wealth += a._ssY
        if HHP:
            a._hhWS = annualWageUSD - costUSD
        if p.get('ubi', 0) > 0:
            raise NotImplementedError('ubi')
        if E:
            emUI = emQ.ui if emQ else 0
            a.yrUbiUSD = 0 + emUI
            if emUI > 0:
                a.wealth += emUI
        yrCashSurplus = annualWageUSD - costUSD + 0 + (a._ssY if a._ret else 0)
        if RET and RET.get('ci'):
            rtCk = a._rtCk or 0
            a.yrCapUSD = rtCk
            if rtCk != 0:
                a.wealth += rtCk
                yrCashSurplus += rtCk
        if emQ and emQ.ui > 0:
            yrCashSurplus += emQ.ui
        if tbY:
            net = R.tb_cash_flow(a, tbY, annualWageUSD, yr)
            a.wealth += net
            yrCashSurplus += net
        a.yrWageUSD = annualWageUSD
        a.yrCostUSD = costUSD
        a.yrBasketUSD = mainLoopCostUSD
        a.yrConvUSD = 0
        A_.costUSD = costUSD
        A_.yrCashSurplus = yrCashSurplus
        if FWON:
            PG.fw_payouts(R, a, p, Y, A_)
            yrCashSurplus = A_.yrCashSurplus
        if p['ccoOn'] and a.inCCO and FWON:
            PG.fw_participant(R, a, p, Y, A_)
        if PJON and p['ccoOn'] and a.inCCO:
            PG.project_convert(R, a, p, Y, A_)
            yrCashSurplus = A_.yrCashSurplus
        if p['pth'] and a.inPTH and not POFF['pthEquity'] and not POFF['pthCost']:
            PG.pth_member(R, a, p, Y, A_)
            yrCashSurplus = A_.yrCashSurplus
        elif a.pthTenure:
            PG.pth_left(R, a)
        if p['ptf'] and not a.inPTF and p['ptfShare'] > 0 and yr > 0 and not (HHA and not a._hhHead) and PG.ptf_cap_allows(R, p, Y):
            ap = 0.005 + C['PTF_BASS_Q'] * ptfAdoptFrac
            if bleiCheck / (priceIdx if (AUD and AUD.get('gate')) else 1) < L30:
                ap += 0.015
            if uPtfAdopt < ap:
                a.inPTF = True
                if Y.PDON:
                    Y.pdLive += 1
        elif Y.PDON and R.PROD.get('speed') == 'oneyear' and p['ptf'] and not a.inPTF and p['ptfShare'] > 0 and yr > 0 and not (HHA and not a._hhHead):
            apB = 0.005 + C['PTF_BASS_Q'] * ptfAdoptFrac
            if bleiCheck / (priceIdx if (AUD and AUD.get('gate')) else 1) < L30:
                apB += 0.015
            if uPtfAdopt < apB:
                R.PDS.blk += 1
        if SG and AUD and AUD.get('sg'):
            grS = annualWageUSD + (a._ssY if a._ret else 0) + 0 + (emQ.ui if emQ else 0) + (((a.yrTbCash or 0) - (a.yrTax or 0)) if tbY else 0) + (a.yrConvUSD or 0) + ((a.yrCapUSD or 0) if (RET and RET.get('ci')) else 0)
            a._grCut = 0
            if HHP:
                a._grA = grS
                a._grC = costUSD
            elif costUSD > 0 and grS < costUSD:
                if DR and DR.get('fl') == 'fpl':
                    raise NotImplementedError('dr.fl')
                a._grCut = costUSD - costUSD * math.pow(max(0, grS) / costUSD, SG['eps'])
                if DR:
                    a._grCut += R.dr_extra(grS, costUSD, a._grCut, a.yrWealthStartUSD)
                a.wealth += a._grCut
        if HHP:
            a._hhCS = yrCashSurplus
        if R.SCS > 0 and R.SCB == 'cash' and not HHP:
            a.wealth -= R.SCS * max(0, yrCashSurplus)
        if PR:
            pmW = FLR - a.wealth if (not HHP and a.wealth < FLR) else 0
            pmB = mainLoopCostUSD * cfPreCCO
            pmU = min(1, ((pmW + a._grCut) if (SG and not HHP) else pmW) / pmB) if pmB > 0 else 0
            Ac = PR.acc
            Ac.n += 1
            Ac.essD += 1 - pmU
            Ac.unmet += pmW
            Ac.basketOwn += pmB
            if pmW > 0:
                Ac.unmetN += 1
            Ac.Y += annualWageUSD + a.yrConvUSD + (a.yrSSUSD or 0)
            Ac.Yw += annualWageUSD + (a.yrSSUSD or 0)
            if p['ptf'] and a.inPTF:
                Ac.ptfN += 1
            if HHP:
                a._hhPmB = pmB
            Ac.wageBonus += max(0, a.wage - a._wNB) * 12 * W2U * incomeShock
            Ac.wageBonusNS += max(0, a.wage - a._wNB) * 12 * W2U
        if LB:
            a._labC = a._labCn or 0
            a._labCn = 0
            if LB.acc is not None:
                LB.acc['conv'] += a.yrConvUSD or 0
                if a.inCCO:
                    LB.acc['convP'] += a.yrConvUSD or 0
        if tbY:
            RP.tb_account(R, a, tbY, yr, mainLoopCostUSD, cf, cfPreCCO + hcX, costUSD, annualWageUSD, tbG, tbPT)
        if not HHP and a.wealth < FLR:
            a.wealth = FLR
    if HHON:
        if HHPOOL:
            R.hh_pool(yr, bool(tbY))
        R.hh_sync('ptf')
    PG.fw_year_end(R, agents, yr, p, Y)


def C_PTH(R):
    return R.S['PTH_HOUSING_CUT']
