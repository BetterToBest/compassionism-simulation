"""S69: one run (tbRunCore): set-up, the year loop of section 5, the price step and every reported measure."""
import math
from s69_rng import Mulberry32, Sampler, hl_u, norm_cdf, norm_inv, js_round, median_of, quantile_of, gini_of, gini_neg
from s69_engine import Engine, Ag, HH, NS, nz, fnum, INF
import s69_setup as SU
import s69_report as RP
import s69_prog as PG


class Run(Engine):

    def __init__(self, state, tables, p, seed, o, S, tau0, yMax, spd=None):
        Engine.__init__(self, state, tables)
        RP.RK = bool(self.FX and self.FX.get('rk'))  # S63 fx.rk
        self.p = p
        self.seed = seed
        self.o = o
        self.Spath = S
        self.tau0 = tau0
        self.yMax = yMax
        self.SPD = spd
        self.sm = Sampler()
        self.RNG = None
        self.HHS = None
        self.EMS = None
        self.SNS = None
        self.LFS = None
        self.PFS = None
        self.PBS = None
        self.PAS = None
        self.POS = None
        self.C22S = None
        self.RTO = None
        self.CRS = None
        self.CRY = None
        self.CRP = None
        self.DR_PL = 1
        self.DR_ACC = None
        self.BGS = None
        self.FWS = self.PJS = self.ESS = self.SPS = self.PDS = self.JNS = self.MLS = None
        self.THETA_DENS = state.get('THETA_DENS')
        self.tiny = 0

    # ---------------------------------------------------------------- set-up (section 4; tbRunCore's head)
    def setup(self):
        p, seed, o = self.p, self.seed, self.o
        C = self.CFG
        self.sm.rng = Mulberry32(seed + 700003)
        latent = SU.make_latent(self, p['nAgents'])
        if self.LATENT:
            for l in latent:
                SU.latent_adjust(self, l)
        agents = [SU.instantiate(l, p) for l in latent]
        self.recPath = self.build_recession(p['years'], seed) if p['shock'] else None
        gR = Mulberry32(seed + 900001)
        grp = o['grp']
        wq = sorted(l.wage for l in latent)
        w1 = wq[len(wq) // 3]
        w2 = wq[(2 * len(wq)) // 3]
        for i, a in enumerate(agents):
            l = latent[i]
            a._tbU = gR()
            a._tbEl = False
            a._tbPart = l.uCCO < grp['part']
            a._tbPTH = l.uPTH < grp['pth']
            a._tbLow = l.wage < w1
            a._tbTop = l.wage >= w2
        if self.EMPL:
            self.EMS = NS(r=Mulberry32(seed + 600031), n=0, out=0, spells=0, weeks=0.0, auto=0, ui=0.0, lost=0.0, cut=0.0, cutN=0, long=0,
                          rho=SU.empl_occ(self, agents, seed) if self.EMPL.get('occ') else 0)
        if self.SNET:
            self.SNS = NS(seed=(seed | 0) + 700001, idxPrev=1, acc=dict(ay=0, ky=0, kN=0, snapN=0, eitcN=0, ctcN=0, snap=0.0, eitc=0.0, ctc=0.0, mN=0, m=0.0, abN=0, abM=0.0, abL=0.0))
            for j, a in enumerate(agents):
                a._snId = j
                a._snB = 0
                a._snM = 0
        if self.PTHB and p['pth'] and not (self.FX and self.FX.get('pthb')):
            raise NotImplementedError('PTH books before households')
        if self.PTFS and p['ptf']:
            self.PFS = NS(r=Mulberry32(seed + 600047), cut=0.0, cn=0, leave=0, mem=0, yrs=0, dens=1)
        if self.WEALTH_TAIL and not (self.HOUSEHOLDS and self.HOUSEHOLDS.get('wealth') == 'scf'):
            raise NotImplementedError('tail without SCF wealth')
        self.RTO = Mulberry32(seed + 600091) if (self.RETURNS and self.RETURNS.get('bo')) else None
        if self.HOUSEHOLDS:
            SU.hh_init(self, agents, seed)
        if self.PTHB and p['pth'] and self.FX and self.FX.get('pthb'):
            PG.pthb_init(self, agents, latent, seed)
        if self.PTF_ACCESS == 'open' and p['ptf']:
            PG.pa_init(self, agents)
        else:
            self.PAS = None
        if self.PTF_OPS:
            if self.PAS:
                PG.po_init(self, agents)
            else:
                self.POS = None
        if self.C22:
            PG.c22_init(self, agents, seed)
        else:
            self.C22S = None
        self.RHH = RP.hh_rep_acc() if (self.HOUSEHOLDS and self.HHS) else None
        if self.LF_SCOPE:
            SU.lf_init(self, agents, seed)
        if self.BARGAIN and not o.get('labor'):
            raise ValueError('bg needs the labour response')
        self.BGS = RP.bg_new() if self.BARGAIN else None
        if self.BGS:
            self.BGS.T = p['years']
        self.DR_ACC = NS(n=0, h=0, c=0.0) if self.DEBT_READ else None
        self.DR_PL = 1
        self.sm.rng = Mulberry32(seed)
        self.RNG = self.sm.rng
        comp = {k: 1 for k in C['BASKET_KEYS']}
        self.PRICE = NS(bIdx=1, comp=comp, piG=0, colaLevel=1, lastFull=1, wIdx=o['wIdx'], noDamp=o['noDamp'], acc=None)
        self.WYS = NS(cur=[], f0=0, f1=0.0, f2=0.0, n=0, fs=0.0, ny=0) if o.get('wy') else None
        self.DMS = RP.dm_new(o['dm']) if o.get('dm') else None
        self.RTR = {} if self.RETURNS else None
        self.WTS = {} if (self.WEALTH_TAIL or o.get('wtm')) else None
        self.PRS = RP.pr_new(self.PR_OPTS, self.PRICE_RULE == 'capacity', self.S) if (self.PRICE_RULE == 'capacity' or o.get('mf')) else None
        if self.PRICE_RULE == 'capacity':
            raise NotImplementedError('capacity price rule')
        self.MFS = RP.mf_new() if o.get('mf') else None
        if o.get('lv') or o.get('sec') or p.get('sx'):
            raise NotImplementedError('lv/sec/sx')
        self.TB = NS(fin=o['fin'], tau=self.tau0, X=o['X'], inkindRho=o['inkindRho'], neutralGate=o['neutralGate'], cur=None, tb=o.get('taxBase'), tauMax=o['tauMax'])
        self.GVS = RP.gv_new(self) if self.GOV else None
        if self.GOV:
            self.gvCap = o['tauMax'] if not (self.FX and self.FX.get('fin') == 'cap') else self.GOV['capHi']
            self.TB.capE = self.gvCap
        self.agents = agents
        self.latent = latent
        self.THETA_DENS = None
        self.FWS = self.PJS = self.ESS = self.SPS = self.PDS = self.JNS = self.HCS = None
        self.LABOR = None
        self.labAcc = None
        if o.get('labor'):
            self.labAcc = dict(n=0, nP=0, E0=0.0, E=0.0, raise_=0.0, cash=0.0, bu=0.0, buR=0.0, rent=0.0, disp=0.0, C=0.0, U=0.0, projH=0.0, zero=0, conv=0.0, convP=0.0)
            L = dict(o['labor'])
            self.LABOR = NS(rho=L['rho'], rhoBU=L['rhoBU'], rhoR=L['rhoR'], eps=L['eps'], delta=L['delta'], acc=self.labAcc)

    def build_recession(self, years, seed):
        """Section 4, item 3."""
        sm = Sampler()
        sm.rng = Mulberry32(seed + 700000)
        r = sm.rng
        path = []
        st = NS(active=False, incomeMultiplier=1.0, yearsLeft=0)
        for y in range(years):
            if y > 0:
                if st.active:
                    st.yearsLeft -= 1
                    if st.yearsLeft <= 0:
                        st.active = False
                        st.incomeMultiplier = 1.0
                elif r() < 0.10:
                    st.active = True
                    st.yearsLeft = 1 + math.floor(r() * 3)
                    st.incomeMultiplier = 0.70 + sm.beta(5, 2) * 0.25
            path.append(NS(active=st.active, incomeMultiplier=st.incomeMultiplier))
        return path

    # ---------------------------------------------------------------- small rules
    def agent_blei(self, a, buAlloc, ccoOn, pthOn, szhOn, szhCoh, ptfOn, wealth=None, wage=None, hhD=None):
        """6.2 (agentBLEI)."""
        C = self.CFG
        w = a.wealth if wealth is None else wealth
        liquid = max(0, w * 0.20)
        gammaV = 0.20 if (ccoOn and a.inCCO) else 0.12
        wg = a.wage if wage is None else wage
        mInc = max(wg, 0.1) * C['WAGE_TO_USD']
        buFood = 0
        if ccoOn and a.inCCO and buAlloc > 0:
            buFood = a._fwBUm if (self.CONVERSION_MODEL == 'framework' and a._fwBUm is not None) else PG.blei_bu_food_engine(self, a, buAlloc)
        szhD = szhCoh * C['SZH_ALL_RESIDENTS'] if szhOn else 0
        if szhOn and ptfOn and (a.inPTF or self.PAS):
            szhD += PG.blei_szh_ptf(self, a)
        baseCost = C['CCO_PTH_DAILY_COST'] if (ccoOn and a.inCCO and pthOn and a.inPTH) else C['BASE_DAILY_COST']
        d = a._hhD if hhD is None else hhD
        dc = max(baseCost * (1 - szhD), 0.1) * (d or 1)
        r = (liquid + gammaV * mInc + buFood) / dc
        if r != r or r in (INF, -INF):
            return 0
        return max(0, r)

    def blei0(self, a):
        return self.agent_blei(a, 0, False, False, False, 0, False)

    def bu_ess(self):
        return self.CFG['ESSENTIALS_HUB'] if self.BU_SCOPE == 'hub' else self.CFG['ESSENTIALS']

    # ---------------------------------------------------------------- households each year (hhYear, hhPool, hhSync)
    def hh_year(self, agents):
        C = self.CFG
        PR = self.PRICE
        bI = PR.bIdx if PR else 1
        comp = PR.comp if PR else None
        HO = self.HOUSEHOLDS
        for H in self.HHS.list:
            if H.single:
                continue
            if HO.get('shock') and len(H.a) > 1:
                H.hv = 0.90 + self.HHS.srng() * 0.20
            N = H.need

            def c(k):
                return comp['other' if k == 'childcare' else k] if comp else 1
            P = 0.0
            for k in N:
                P += N[k] * c(k)
            e = 0.0
            for k in self.bu_ess():
                e += N[k] * c(k)
            if self.BU_SCOPE == 'hub':
                e += N['childcare'] * c('childcare')
            f = N['food'] * c('food') / P
            hs = N['housing'] * c('housing') / P
            t = N['taxes'] * c('taxes') / P if self.DISC_BASE == 'pretax' else 0
            pS = dict(f=f, h=hs, t=N['transport'] * c('transport') / P, m=N['medical'] * c('medical') / P, k=(N.get('childcare') or 0) * c('childcare') / P) if self.PTFS else None
            q22 = 0.0
            if self.C22:
                for k in self.S['C22_NEEDS']:
                    q22 += N[k] * c(k)
            for a in H.a:
                if self.C22:
                    a._hhC22 = q22 / P
                a._hhF = P / (len(H.a) * C['LIVING_WAGE_ANNUAL'] * bI)
                a._hhE = e / P
                a._hhFd = f
                a._hhH = hs
                a._hhT = t
                a._hhBU = H.buM
                if pS:
                    a._hhS = pS

    def hh_sync(self, what):
        for H in self.HHS.list:
            if len(H.a) < 2:
                continue
            hd = H.a[0]
            for a in H.a[1:]:
                if what == 'cco':
                    a.inCCO = hd.inCCO
                    a._jnY = hd._jnY
                else:
                    a.inPTF = hd.inPTF

    def hh_pool(self, yr, tbOn):
        C = self.CFG
        FL = C['WEALTH_FLOOR']
        for H in self.HHS.list:
            if len(H.a) < 2:
                continue
            n = len(H.a)
            if self.SCS > 0:
                cs = 0.0
                for a in H.a:
                    cs += a._hhCS if self.SCB == 'cash' else a._hhWS
                sc = self.SCS * max(0, cs) / n
                for a in H.a:
                    a.wealth -= sc
            if self.SPEND_GRADE:
                gA = 0.0
                gC = 0.0
                for a in H.a:
                    gA += a._grA
                    gC += a._grC
                if gC > 0 and gA < gC:
                    if self.DEBT_READ and self.DEBT_READ.get('fl') == 'fpl':
                        raise NotImplementedError('dr.fl')
                    gc = gC - gC * math.pow(max(0, gA) / gC, self.SPEND_GRADE['eps'])
                else:
                    gc = 0
                if self.DEBT_READ and gc > 0:
                    gW = 0.0
                    for a in H.a:
                        gW += a.yrWealthStartUSD
                    gc += self.dr_extra(gA, gC, gc, gW)
                for a in H.a:
                    a._grCut = gc / n
                    a.wealth += gc / n
            w = 0.0
            for a in H.a:
                w += a.wealth
            w /= n
            for a in H.a:
                a.wealth = w
            if self.PRICE and self.PRICE.acc:
                A = self.PRICE.acc
                for a in H.a:
                    pmW = FL - a.wealth if a.wealth < FL else 0
                    pmU = min(1, ((pmW + a._grCut) if self.SPEND_GRADE else pmW) / a._hhPmB) if a._hhPmB > 0 else 0
                    A.essD -= pmU
                    A.unmet += pmW
                    if pmW > 0:
                        A.unmetN += 1
            if tbOn:
                inc = mlc = cost = disp = 0.0
                for a in H.a:
                    inc += a._hhInc
                    mlc += a._hhMlc
                    cost += a._hhCost
                    disp += a._hhDisp
                for a in H.a:
                    RP.tb_pov(self, a, self.TB.cur, a._hhIdx, inc / n, mlc / n, cost / n, disp / n)
            for a in H.a:
                if a.wealth < FL:
                    a.wealth = FL

    def dr_extra(self, inc, cost, cut, w0):
        D = self.DEBT_READ
        ex = cost - cut - max(0, inc)
        liq = D.get('liq')
        ok = max(0, (w0 * liq if (liq is not None and liq != 1 and w0 > 0) else w0) + (D['lim'] * self.DR_PL if D.get('lim') else 0))
        x = ex - ok if ex > ok else 0
        if self.DR_ACC:
            self.DR_ACC.n += 1
            if x > 0:
                self.DR_ACC.h += 1
                self.DR_ACC.c += x / self.DR_PL
        return x

    # ---------------------------------------------------------------- job loss (12.1)
    def empl_weeks(self, u, rec):
        s = self.CFG['EMPL_S']['r' if rec else 'n']
        S1, S2 = s[0], s[1]
        if u >= 1:
            return 2.5
        if u >= S1:
            return 2.5 + 7 * math.log(u) / math.log(S1)
        if u >= S2:
            return 9.5 + 11 * (math.log(u) - math.log(S1)) / (math.log(S2) - math.log(S1))
        return 20.5 + s[2] * math.log(S2 / u)

    def empl_year(self, a, rec, aiH, u, wkPay):
        C = self.CFG
        E = self.EMPL
        A = self.EMS
        ui = 0.0
        carry = min(52, a._emW or 0)
        a._emW = (a._emW or 0) - carry
        w = carry
        if carry > 0 and a._emUi:
            uw = min(carry, max(0, C['EMPL_UI_WEEKS'] - a._emUiW))
            a._emUiW += uw
            ui += uw * C['EMPL_UI_REPL'] * wkPay
        if carry == 0:
            if E['auto'] != 'jobs':
                raise NotImplementedError('EMPL.auto')
            hA = max(0, aiH * a.automationRisk)
            h = C['EMPL_P_REC'] if rec else C['EMPL_P']
            pE = 1 - (1 - h) * (1 - hA)
            if u[0] < pE:
                auto = u[0] < hA
                D = self.empl_weeks(u[2], rec)
                st = u[3] * 52
                now = min(D, 52 - st)
                A.spells += 1
                if auto:
                    A.auto += 1
                if D > 26:
                    A.long += 1
                w = now
                a._emW = D - now
                a._emUi = bool(E.get('ui')) and u[4] < (C['EMPL_UI_RECIP_REC'] if rec else C['EMPL_UI_RECIP'])
                a._emUiW = 0
                if a._emUi:
                    uw2 = min(now, C['EMPL_UI_WEEKS'])
                    a._emUiW = uw2
                    ui += uw2 * C['EMPL_UI_REPL'] * wkPay
                a._emCut = 2 * E['cut'] * u[5] if (auto or u[1] < (C['EMPL_PERM_REC'] if rec else C['EMPL_PERM'])) else 0
                a._emAuto = auto
        if a._emW <= 0 and (a._emCut or a._emAuto):
            f = 1 - (a._emCut or 0)
            a.wage *= f
            if a._lwNB is not None:
                a._lwNB *= f
            if a._wNB is not None:
                a._wNB *= f
            A.cut += a._emCut or 0
            A.cutN += 1
            if a._emAuto:
                a.automationRisk = 1 / (1 + C['AUTO_LOW_B'])
            a._emCut = 0
            a._emAuto = False
        A.n += 1
        A.weeks += w
        A.ui += ui
        A.lost += w * wkPay
        if w > 0:
            A.out += 1
        return NS(out=min(1, w / 52), ui=ui)

    # ---------------------------------------------------------------- today's safety net (12.4; Appendix C, item 22)
    def sn_inc_tax(self, f, agi):
        T = self.CFG['SN_TAX']
        x = max(0, agi - T['std'][f])
        lo = 0
        t = 0.0
        for b in T['br'][f]:
            t += max(0, min(x, b[0]) - lo) * b[1]
            lo = b[0]
            if x <= b[0]:
                break
        return t

    def sn_ben(self, h, earn, keep=False):
        C = self.CFG
        E = self.SNET
        Y = max(0, earn + h['other'])
        n = max(1, h['nA'] + h['nK'])
        line = C['HL_FPL']['one'] + C['HL_FPL']['add'] * (n - 1)
        ratio = Y / line
        f = 'j' if h['nA'] >= 2 else ('h' if h['nK'] > 0 else 's')
        snap = eitc = ctc = 0
        if E.get('snap') and h['takeS'] and (keep or ratio <= E['gross']):
            S = C['SN_SNAP']
            ni = max(0, Y - S['earnDed'] * earn - 12 * S['std'][min(n, len(S['std'])) - 1] - h['care'])
            sh = max(0, h['house'] - 0.5 * ni)
            if not h['old']:
                sh = min(sh, 12 * S['shCap'])
            ni = max(0, ni - sh)
            mx = 12 * (S['max'][n - 1] if n <= len(S['max']) else S['max'][-1] + S['add'] * (n - len(S['max'])))
            snap = max(0, mx - S['rate'] * ni)
            if n <= 2:
                snap = max(snap, 12 * S['min'])
        if E.get('eitc') and h['takeT'] and (h['nK'] > 0 or h['okAge']):
            P = C['SN_EITC'][min(3, h['nK'])]
            st = P['pj'] if f == 'j' else P['ps']
            en = P['ej'] if f == 'j' else P['es']
            eitc = max(0, min(P['max'], P['max'] / P['inc'] * max(0, earn)) - P['max'] / (en - st) * max(0, max(earn, Y) - st))
        if E.get('ctc') and h['takeT'] and h['k17'] > 0:
            Cc = C['SN_CTC']
            cr = max(0, Cc['per'] * h['k17'] - Cc['poR'] * max(0, Y - Cc['po'][f]))
            ctc = max(0, min(Cc['ref'] * h['k17'], Cc['rate'] * max(0, earn - Cc['thr']), cr - self.sn_inc_tax(f, Y)))
        return [snap, eitc, ctc]

    def sn_ab_clock(self, a, subject, gets):
        pr = a._snAb or [0, 0]
        c = a._snAbC or 0
        cr = min(c, max(0, 3 - pr[0] - pr[1])) if (subject and gets) else 0
        a._snAb = [cr, pr[0]]
        return c - cr if (subject and gets) else 0

    def sn_ab_cut(self, h, earn, snap, lost):
        if not lost or snap <= 0:
            return 0
        h1 = dict(h)
        h1['nA'] = h['nA'] - 1
        w = self.sn_ben(h1, earn)[0] if h1['nA'] + h1['nK'] > 0 else 0
        f = 0.0
        for l in lost:
            f += l / 12
        return min(snap, f * (1 - self.SNET['abawdEx']) * max(0, snap - w))

    def sn_year(self, agents, yr, HHON, inflRate):
        C = self.CFG
        S = self.SNS
        ac = S.acc
        gIdx = math.pow(1 + inflRate, yr) * (self.PRICE.bIdx if self.PRICE else 1)
        if not HHON:
            raise NotImplementedError('safety net without households')
        W2U = C['WAGE_TO_USD']
        for H in self.HHS.list:
            if not H.a:
                continue
            ua = H.a
            nA = len(ua)
            nK = len(H.kids)
            earn = 0.0
            other = 0.0
            old = False
            okAge = False
            k17 = 0
            hd = ua[0]._snId
            for a in ua:
                if yr == 0 or a.yrWageUSD is None:
                    earn += 0 if a._ret else a.wage * 12 * W2U
                else:
                    earn += (a.yrWageUSD or 0) / S.idxPrev
                    other += ((a.yrSSUSD or 0) + (a.yrUbiUSD or 0) + (a.yrConvUSD or 0)) / S.idxPrev
                if yr == 0 and a._ret:
                    other += (a._ssY or 0)
                okAge = True
            for age in H.kids:
                if age < C['SN_CTC']['age']:
                    k17 += 1
            h = dict(nA=nA, nK=nK, k17=k17, other=other, house=H.need['housing'], care=(H.need.get('childcare') or 0), old=old, okAge=okAge,
                     takeS=hl_u(S.seed, hd, 0, 31) < self.SNET['snapTake'], takeT=hl_u(S.seed, hd, 0, 32) < self.SNET['taxTake'])
            b0 = self.sn_ben(h, earn)
            b1 = self.sn_ben(h, earn + 1000, bool(self.SNET.get('slope')) and b0[0] > 0)
            if self.SNET.get('abawd'):
                abK = any(age < 14 for age in H.kids)
                abL = []
                for a in ua:
                    l = self.sn_ab_clock(a, (not abK) and (not a._ret), b0[0] > 0)
                    if l > 0:
                        abL.append(l)
                        ac['abN'] += 1
                        ac['abL'] += l
                abCut = self.sn_ab_cut(h, earn, b0[0], abL)
                b0[0] -= abCut
                b1[0] -= self.sn_ab_cut(h, earn + 1000, b1[0], abL)
                ac['abM'] += abCut
            B = b0[0] + b0[1] + b0[2]
            m = max(-0.5, min(0.9, (B - (b1[0] + b1[1] + b1[2])) / 1000))
            for a in ua:
                a._snB = B * gIdx / nA
                a._snM = m if (B > 0 or m != 0) else 0
            ac['ay'] += nA
            ac['ky'] += nK
            if B > 0:
                ac['kN'] += nK
            if b0[0] > 0:
                ac['snapN'] += nA
            if b0[1] > 0:
                ac['eitcN'] += nA
            if b0[2] > 0:
                ac['ctcN'] += nA
            ac['snap'] += b0[0]
            ac['eitc'] += b0[1]
            ac['ctc'] += b0[2]
            if B > 0:
                ac['mN'] += nA
                ac['m'] += m * nA
        S.idxPrev = gIdx

    # ---------------------------------------------------------------- labour-force flows (14.15)
    def lf_flow(self, a, P, yr):
        S = self.LFS
        F = S.f
        u1 = F()
        u2 = F()
        if not (yr >= 1) or (a._ret and not a._lf):
            return
        t = SU.lf_type(a)
        A = S.ac
        w = a._w if a._w is not None else 1
        FL = self.CFG['LF_FLOWS']
        if a._lf:
            A.oy += w
            if u1 < FL['pooled']['ret'][t][a._lf]:
                k = P / (a._lfP or 1)
                a.wage = a._lfW * k
                if a._lwNB is not None:
                    a._lwNB = a._lfNB * k if a._lfNB is not None else a.wage
                if a._wNB is not None:
                    a._wNB = a._lfWN * k if a._lfWN is not None else a.wage
                a._ret = False
                a._lf = None
                a._ssY = 0
                A.rt += w
            return
        A.iy += w
        if S.fl == 'panel':
            raise NotImplementedError('lf.fl panel')
        Sh = FL['pooled']['exit'][t]
        c = 0.0
        why = None
        for r in self.S['LF_REASONS']:
            c += Sh[r]
            if u1 < c:
                why = r
                break
        if not why:
            return
        y = SU.lf_income(self.CFG['LF_INCOME'][why], u2)
        a._lf = why
        a._lfW = a.wage
        a._lfNB = a._lwNB
        a._lfWN = a._wNB
        a._lfP = P
        a._ret = True
        a._ssB0 = y
        a._ssY = y * P
        a.wage = a._ssY / 12 / self.CFG['WAGE_TO_USD']
        A.ex += w
        A.k[why] += w
        if not a._lfEv:
            a._lfEv = 1
            A.ev += 1

    def lf_pm(self, a, Ep, I, L, emQ, yr, P):
        S = self.LFS
        L = min(I, L)
        E = Ep - (I - L)
        if not (E > 0):
            return 0
        m = min(L, E)
        q = S.pm * m / E
        if a._lpU < q:
            if emQ:
                emQ.ui = 0
            if yr >= 1 and S.ac:
                w = a._w if a._w is not None else 1
                S.ac.lp += w
                S.ac.lpE += w * E / P
            return 0
        return max(0, E - (1 - S.pm) * m / (1 - q))

    def lf_acc(self, a, E, yr):
        if not (yr >= 0) or (a._ret and not a._lf):
            return
        A = self.LFS.ac
        w = a._w if a._w is not None else 1
        while len(A.ayY) <= yr:
            A.ayY.append(None)
            A.outY.append(None)
        A.ayY[yr] = (A.ayY[yr] or 0) + w
        if a._lf:
            A.outY[yr] = (A.outY[yr] or 0) + w
        if yr < 1:
            return
        A.ay += w
        if E > 0:
            A.pt += w
        if a._lf:
            A.out += w

    # ---------------------------------------------------------------- wealth by asset class (14.6, 14.7)
    def rt_group(self, W):
        E = self.S['RT_EDGES']
        g = 0
        while g < len(E) and W >= E[g]:
            g += 1
        return g

    def rt_open(self, w, Wh, R, P, own):
        b = NS(r=[0.0] * 5, v=[0.0] * 5, n=0.0, dv=0.0, df=0.0, en=0.0, ed=0.0, al=None, g=-1, w0=w, w=w, p=P, p0=P)
        if R.get('all'):
            q = None
        else:
            q = (self.S['RT_GROUPS_O'] if own else self.S['RT_GROUPS_N']) if R.get('bo') else self.S['RT_GROUPS']
            q = q[self.rt_group(Wh)]
        G = w / (1 - q[0]) if q else 0
        b.own = bool(own)
        b.gy = 0
        if q and G >= 0:
            s = 0.0
            b.g = self.rt_group(Wh)
            for c in range(5):
                b.r[c] = G * q[1 + c]
                s += q[1 + c]
            b.n = G * (1 - s)
            b.df = G * q[0] * q[6]
            b.dv = G * q[0] * (1 - q[6])
            b.al = q[1:6] + [1 - s]
        else:
            if w >= 0:
                if R.get('all') == 'real':
                    b.r[4] = w
                else:
                    b.n = w
            else:
                b.dv = -w
            b.al = [0, 0, 0, 0, 1, 0] if R.get('all') == 'real' else [0, 0, 0, 0, 0, 1]
        for c in range(5):
            b.v[c] = b.r[c]
        b.en = b.n
        b.ed = b.dv
        b.e0 = b.n - b.dv - b.df
        b.v0 = b.r[0] + b.r[1] + b.r[2] + b.r[3] + b.r[4]
        return b

    def rt_place(self, b, flow, R):
        if flow >= 0:
            pay = min(b.dv, flow)
            b.dv -= pay
            flow -= pay
            if R.get('ns') == 'port':
                raise NotImplementedError('rt.ns port')
            b.n += flow
        else:
            d = min(b.n, -flow)
            b.n -= d
            b.dv += -flow - d

    def rt_step(self, b, flow, pi, R, cr):
        I = 0.0
        self.rt_place(b, flow, R)
        gy = 0.0
        CL = self.S['RT_CLASSES']
        ix = R['ix']
        for c in range(5):
            rh = R['rho'][CL[c]]
            if R.get('rg'):
                raise NotImplementedError('rt.rg')
            gy += b.r[c] * rh * (1 + ix * pi)
            f = (1 + ix * pi) * (1 + rh) - 1
            if cr and c == 2:
                b.ce = b.r[2] * cr.re
                f -= cr.re
            I += b.r[c] * f
            b.r[c] += b.r[c] * f
            b.v[c] += b.v[c] * f
        b.gy = gy
        x = R['phi'] * pi
        if R.get('ng') == 'all':
            raise NotImplementedError('rt.ng all')
        if cr:
            f = self.cr_t(b)
            f = f * cr.rb + (1 - f) * cr.rd
            b.cn = b.n * f
            x -= f
        I += b.n * x
        b.n += b.n * x
        b.en += b.en * x
        x = R['psi'] * pi
        I -= b.dv * x
        b.dv += b.dv * x
        b.ed += b.ed * x
        x = R['chi'] * pi
        I -= b.df * x
        b.df += b.df * x
        return I

    def cr_t(self, b):
        T = self.S['RT_CR']
        return T['t'][b.g] if b.g >= 0 else T['tAll']

    def rt_cap(self, b):
        if b.g < 0:
            return 0
        y = self.S['RT_YLD'][b.g]
        return y[0] * (b.ng or 1) * b.n + y[1] * b.r[2] + y[2] * (b.r[1] + b.r[3])

    def rt_init(self, agents, P, yr):
        R = self.RETURNS
        for a in agents:
            if a._rt:
                continue
            Wh = a.wealth
            if a._hh and a._hh.a and len(a._hh.a) > 1:
                Wh = 0.0
                for m in a._hh.a:
                    Wh += m.wealth
            own = False
            if R.get('bo'):
                H = a._hh
                if H and H._rtOwn is not None:
                    own = H._rtOwn
                else:
                    own = self.RTO() < self.S['RT_OWN'][self.rt_group(Wh / P)]
                    if H:
                        H._rtOwn = own
            a._rt = self.rt_open(a.wealth, Wh / P, R, P, own)
            a._rtNew = True
            if R.get('ng') and a._wtP is not None:
                NG = self.S['RT_NG']
                a._rt.ng = NG[1] if a._wtP >= 0.9999 else (NG[0] if a._wtP >= 0.999 else 1)
        self.CRY = None
        self.CRP = NS(agents=agents, yr=yr) if R.get('cr') else None

    def cr_rates(self, D, NB, ND, EQ, pi, R):
        Cc = R['cr']
        L = Cc['led']
        O = Cc['own']
        W = Cc['wf']
        a = 1 - R['chi']
        k = R['phi'] - R['chi']
        h = 1 - R['phi']
        dAll = L['dHH'] + L['dGOV'] + L['dROW']
        hold = Cc['inc'] == 'hold'
        dl = k if hold else h
        Kb = L['bHH'] * W['wB'] * D
        Kd = L['dHH'] * W['wD'] * D
        kb = min(Kb, max(0, NB))
        kd = min(Kd, max(0, ND))
        pool = a * L['BUS'] * D if hold else (a * L['BUS'] + k * dAll) * D
        ch = Cc['inc'] != 'hedge'
        eq = pool * O['eH'] * W['wE'] if ch else 0
        pl = max(-EQ, min(EQ, eq)) if EQ > 0 else 0
        return NS(pi=pi, rb=k * pi * kb / NB if NB > 0 else 0, rd=(k * pi * kd / ND if ND > 0 else 0) if hold else 0, re=pi * pl / EQ if EQ > 0 else 0,
                  rel=a * pi * D, book=h * pi * (kb + kd), un=pi * (a * (Kb - kb) + dl * (Kd - kd) + (eq - pl)),
                  outG=pi * (a * L['GOV'] * D + dl * L['dGOV'] * D + (pool * O['eG'] if ch else 0)),
                  outF=pi * (a * L['ROW'] * D + dl * L['dROW'] * D + (pool * O['eR'] if ch else 0)),
                  outH=pi * (a * L['bHH'] * (1 - W['wB']) * D + dl * L['dHH'] * (1 - W['wD']) * D + (pool * O['eH'] * (1 - W['wE']) if ch else 0)),
                  outS=0 if ch else pi * pool * O['eH'] * W['wE'])

    def cr_year(self, agents, P, yr):
        if yr == 0 or not self.CRS:
            self.CRS = NS(p0=P, A=dict(rel=0.0, book=0.0, nom=0.0, eq=0.0, outG=0.0, outF=0.0, outH=0.0, outS=0.0, un=0.0))
        R = self.RETURNS
        D = NB = ND = EQ = Wt = 0.0
        pi = None
        for a in agents:
            b = a._rt
            if not b or a._rtNew:
                continue
            w = a._w if (R['cr'].get('w') and a._w is not None) else 1
            k = NS(r=list(b.r), n=b.n, dv=b.dv, al=b.al)
            t = self.cr_t(b)
            self.rt_place(k, a.wealth - b.w, R)
            if pi is None:
                pi = P / b.p - 1
            D += w * b.df
            NB += w * t * k.n
            ND += w * (1 - t) * k.n
            EQ += w * k.r[2]
            Wt += w
        if pi is None or not (Wt > 0):
            return None
        y = self.cr_rates(D, NB, ND, EQ, pi, R)
        f = self.CRS.p0 / P / Wt
        y.f = self.CRS.p0 / P
        y.Wt = Wt
        A = self.CRS.A
        for k in ('rel', 'book', 'outG', 'outF', 'outH', 'outS', 'un'):
            A[k] += getattr(y, k) * f
        return y

    def rt_adult(self, a, P):
        R = self.RETURNS
        b = a._rt
        if self.CRP:
            self.CRY = self.cr_year(self.CRP.agents, P, self.CRP.yr)
            self.CRP = None
        if a._rtNew:
            a._rtNew = False
            if R.get('ci'):
                a._rtCk = self.rt_cap(b)
            return 0
        I = self.rt_step(b, a.wealth - b.w, P / b.p - 1, R, self.CRY)
        CY = self.CRY
        if CY:
            cw = a._w if (R['cr'].get('w') and a._w is not None) else 1
            cf = CY.f
            cx = (1 - R['chi']) * CY.pi * b.df
            self.CRS.A['nom'] += cw * b.cn * cf / CY.Wt
            self.CRS.A['eq'] += cw * b.ce * cf / CY.Wt
            b.crn = (b.crn or 0) + (b.cn + b.ce) * cf
            b.crr = (b.crr or 0) + cx * cf
        a.wealth += I
        b.w = a.wealth
        b.p = P
        if R.get('ci'):
            a._rtCk = self.rt_cap(b)
        return I

    # ---------------------------------------------------------------- the testbed's per-adult accounts
    def tb_year(self, p, colaF):
        s = p['tb']
        self.TB.cur = RP.tb_new_acc()
        if s.get('xc') or s.get('nit') or s.get('endow') or s.get('groc'):
            raise NotImplementedError('testbed transfers')
        nw = bool(self.GOV and self.GOV.get('base') != 'w')
        if nw:
            raise NotImplementedError('gv.base')
        return NS(ubi=(s.get('ubi') or 0) * colaF, xc=0, xd=0, G=0, t=0, tau=self.TB.tau or 0, X=(self.TB.X or 0) * (self.TB.xIdx or 1), tb=self.TB.tb,
                  xi=(self.TB.xIdx or 1), cap=self.TB.tauMax, W=0, T=p['years'], gcap=0, gcov=0, Gp=False, nw=nw)

    def tb_gate(self, a, p, buEff, y):
        Ep = a.yrWageUSD if a.yrWageUSD is not None else a.wage * 12 * self.CFG['WAGE_TO_USD']
        m = (y.ubi + y.xc + 0) / 12
        if p['ccoOn'] and a.inCCO and buEff > 0:
            m += a._fwBUm if (self.CONVERSION_MODEL == 'framework' and a._fwBUm is not None) else PG.tb_gate_bu_engine(self, a, buEff)
        a._tbM = m
        return self.blei0(a) + m / self.CFG['BASE_DAILY_COST']

    def tb_lab(self, a, y, E0, cutUSD):
        LB = self.LABOR
        ex = LB.eps - LB.rho
        F = 1.0
        tx = y.tau > 0 and E0 > y.X
        V = y.ubi + y.xc * (1 - y.xd)
        D = y.xc * y.xd
        O = V
        if y.tb == 'prog' or y.tb == 'land':
            raise NotImplementedError('taxBase')
        elif tx:
            F *= math.pow(1 - y.tau, ex)
            V += y.tau * y.X
        if self.SNET and self.SNS and a._snB is not None:
            F *= math.pow(1 - a._snM, ex)
            V += a._snB + a._snM * E0
        if self.TB.inkindRho:
            V += cutUSD + (a._tbPthPrev or 0)
            O += cutUSD + (a._tbPthPrev or 0)
        return NS(F=F, V=V, D=D, O=O)

    def tb_cash_flow(self, a, y, E, yr):
        cash = y.ubi + y.xc + 0
        tax = y.tau * max(0, E - y.X) if y.tau > 0 else 0
        if self.SNET and self.SNS and a._snB:
            cash += a._snB
        a.yrTbCash = cash
        a.yrTax = tax
        a._tbNit = 0
        return cash - tax
