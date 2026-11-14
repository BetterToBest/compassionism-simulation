"""S69: the start of a run (MODEL_SPEC.md section 4, 6.13, 12.1, 12.4, 14.4, 14.6, 14.8, 14.15)."""
import math
from s69_rng import Mulberry32, norm_cdf, norm_inv, js_round
from s69_engine import Ag, HH, NS


def make_latent(R, n):
    """Section 4, item 1, and 4.1: the construction draws, in makeLatentAgent's order."""
    C = R.CFG
    sm = R.sm
    pop = []
    for _ in range(n):
        r = sm.rng
        l = NS()
        l.uCCO = r()
        l.uPTF = r()
        l.uPTH = r()
        l.wealth = sm.lognormal(C['WEALTH_INIT_MU'], C['WEALTH_INIT_SIGMA'])
        l.wage = sm.lognormal(3.5, 0.5)
        l.octaveShape = sm.beta(2, 5)
        l.qualityZ = sm.normal()
        c = r()
        v = r()
        l.automationRisk = math.pow(v, 1 / C['AUTO_HIGH_A']) if c < C['AUTO_HIGH_SHARE'] else 1 - math.pow(1 - v, 1 / C['AUTO_LOW_B'])
        l.lam = C['FBS_LAMBDA_LO'] + r() * (C['FBS_LAMBDA_HI'] - C['FBS_LAMBDA_LO'])
        pop.append(l)
    return pop


def latent_adjust(R, l):
    """The US-data readings (LATENT; not in the description: GAPS.md). Only the wage spread and median are on in this row."""
    L = R.LATENT
    C = R.CFG
    zw = (math.log(l.wage) - 3.5) / 0.5
    if L.get('risk'):
        raise NotImplementedError('LATENT.risk')
    if L.get('wealth'):
        raise NotImplementedError('LATENT.wealth')
    if L.get('wsd') or L.get('wmed'):
        l.wage = math.exp((math.log(L['wmed'] / (12 * C['WAGE_TO_USD'])) if L.get('wmed') else 3.5) + (L.get('wsd') or 0.5) * zw)


def instantiate(l, p):
    a = Ag()
    qN = (1 - p['cipDemo'] * 0.5) if p['cip'] else 1.0
    maxOct = p['maxOct']
    maxMult = p['maxMult']
    inPTH = bool(p['pth'] and l.uPTH < p['pthUptake'])
    a.wealth = l.wealth
    a.wage = l.wage
    a.initialWage = l.wage
    a.octave = math.floor(l.octaveShape * maxOct)
    a.quality = min(maxMult, max(0, math.exp(math.log(maxMult * 0.5) + 0.4 * l.qualityZ) * qN))
    a.automationRisk = l.automationRisk
    a.lam = l.lam
    a.uCCO = l.uCCO
    a.inCCO = bool(p['ccoOn'] and l.uCCO < p['partRate'])
    a.inPTF = bool(p['ptf'] and l.uPTF < p['ptfShare'])
    a.inPTH = inPTH
    a.buBalance = 0
    a.acreEquity = 5000 if inPTH else 0
    a.pthTenure = 0
    return a


def empl_occ(R, agents, seed):
    """12.1, occupations (Appendix C, items 9 and 16)."""
    O = R.CFG['EMPL_OCC']
    r = Mulberry32(seed + 600041)
    n = len(agents)
    lw = [math.log(max(1e-9, a.wage)) for a in agents]
    m = 0.0
    for x in lw:
        m += x
    m /= n
    v = 0.0
    for x in lw:
        v += (x - m) * (x - m)
    v /= n
    rho = math.sqrt(min(1, O['vb'] / v)) if v > 0 else 0
    ordr = sorted(range(n), key=lambda i: (agents[i].wage, i))
    rk = [0] * n
    for k, i in enumerate(ordr):
        rk[i] = k
    cum = O['cum']
    pr = O['p']
    for i, a in enumerate(agents):
        e = norm_inv(min(1 - 1e-12, max(1e-12, r())))
        z = rho * norm_inv((rk[i] + 0.5) / n) + math.sqrt(1 - rho * rho) * e
        q = norm_cdf(z)
        lo, hi = 0, len(cum) - 1
        while lo < hi:
            mid = (lo + hi) >> 1
            if cum[mid] >= q:
                hi = mid
            else:
                lo = mid + 1
        a._emOcc = lo
        a.automationRisk = pr[lo]
    return rho


def hh_need(R, H):
    """Appendix C, item 12."""
    C = R.CFG
    nA = len(H.a)
    nK = len(H.kids)
    Rt = C['HH_RATIO'][str(nA) + 'a' + str(min(3, nK)) + 'k']
    need = {}
    tot = 0.0
    for k in C['BASKET_KEYS']:
        need[k] = C['LIVING_WAGE_ANNUAL'] * C['BASKET'][k] * Rt[k]
        tot += need[k]
    cc = 0.0
    nc = 0
    for age in sorted(H.kids):
        if age < C['HH_CARE_AGE']:
            cc += C['HH_CHILDCARE'][min(nc, len(C['HH_CHILDCARE']) - 1)]
            nc += 1
    need['childcare'] = cc
    tot += cc
    bl = 0.0
    bl1 = 0.0
    for k in C['HH_BLEI_KEYS']:
        bl += C['BASKET'][k] * Rt[k]
        bl1 += C['BASKET'][k]
    H.single = nA == 1 and nK == 0
    H.need = need
    H.need0 = tot
    H.buM = 1 + (R.HOUSEHOLDS.get('childBU') or 0) * nK / nA
    H.dM = bl / bl1 / nA


def hh_type(H):
    return ('coupleKids' if H.kids else 'coupleNoKids') if len(H.a) > 1 else ('singleParent' if H.kids else 'single')


def hh_init(R, agents, seed):
    """6.13 and Appendix C, item 11."""
    C = R.CFG
    r = Mulberry32(seed + 500009)
    n = len(agents)
    Cm = C['HH_COMP']
    ordr = list(range(n))
    for i in range(n - 1, 0, -1):
        j = math.floor(r() * (i + 1))
        ordr[i], ordr[j] = ordr[j], ordr[i]
    nC = js_round(n * (Cm['coupleKids'] + Cm['coupleNoKids']) / 2)
    nCK = js_round(nC * Cm['coupleKids'] / (Cm['coupleKids'] + Cm['coupleNoKids']))
    nSP = js_round(n * Cm['singleParent'])

    def kids(arr):
        u = r()
        K = C['HH_KIDS'][arr]
        k = 0
        c = K[0]
        A = C['HH_KID_AGES'][arr]
        out = []
        while k < len(K) - 1 and u >= c:
            k += 1
            c += K[k]
        for _ in range(k + 1):
            v = r()
            b = 0 if v < A[0] else (1 if v < A[0] + A[1] else 2)
            out.append(b * 6 + math.floor(r() * 6))
        return out

    lst = []
    q = 0
    for i in range(nC):
        a1 = agents[ordr[q]]
        a2 = agents[ordr[q + 1]]
        q += 2
        H = HH()
        H.a = [a1, a2]
        H.kids = kids('couple') if i < nCK else []
        lst.append(H)
    i = 0
    while i < nSP and q < n:
        H = HH()
        H.a = [agents[ordr[q]]]
        q += 1
        H.kids = kids('single')
        lst.append(H)
        i += 1
    while q < n:
        H = HH()
        H.a = [agents[ordr[q]]]
        q += 1
        H.kids = []
        lst.append(H)
    for h, H in enumerate(lst):
        H.id = h
        H.grown = []
        hd = H.a[0]
        hh_need(R, H)
        for j, a in enumerate(H.a):
            a._hh = H
            a._hhHead = j == 0
            if not H.single:
                a._hhD = H.dM
            if j > 0:
                a.inCCO = hd.inCCO
                a.inPTF = hd.inPTF
                a.inPTH = hd.inPTH
                a.uCCO = hd.uCCO
    if R.HOUSEHOLDS.get('wealth') == 'scf':
        hh_scf_wealth(R, lst, seed)
    R.HHS = NS(list=lst, grown=[], elig=[], nextId=len(lst), rng=None, st=None, srng=Mulberry32(seed + 500041))


def hh_scf_q(Q, p):
    h = p * 100 - 0.5
    k = math.floor(h)
    if k < 0:
        return Q[0]
    if k >= len(Q) - 1:
        return Q[-1]
    return Q[k] + (Q[k + 1] - Q[k]) * (h - k)


def hh_scf_wealth(R, lst, seed):
    """Appendix C, item 14, with the weighted top tail (14.8)."""
    C = R.CFG
    G = {'coupleKids': [], 'coupleNoKids': [], 'singleParent': [], 'single': []}
    wr = Mulberry32(seed + 600073) if R.WEALTH_TAIL else None
    for H in lst:
        G[hh_type(H)].append(H)
    for t in ('coupleKids', 'coupleNoKids', 'singleParent', 'single'):
        L = G[t]
        n = len(L)
        Q = C['SCF_NETWORTH_PCTL'] if t == 'single' else C['HH_SCF_PCTL'][t]
        rho = C['HH_SCF_RHO'][t]
        wu = None
        if wr:
            wu = [wr() for _ in range(R.WEALTH_TAIL['m'])]
        if not n:
            continue

        def scores(f):
            o = sorted(((f(H), i) for i, H in enumerate(L)), key=lambda x: x[0])
            z = [0.0] * n
            for rr, qq in enumerate(o):
                z[qq[1]] = norm_inv((rr + 0.5) / n)
            return z

        def sw(H):
            m = 0.0
            for a in H.a:
                m += a.wage
            return m

        def sq(H):
            m = 0.0
            for a in H.a:
                m += a.wealth
            return m
        zw = scores(sw)
        zq = scores(sq)
        if wr:
            wt_assign(R, L, t, Q, [norm_cdf(rho * zw[i] + math.sqrt(1 - rho * rho) * zq[i]) for i in range(n)], wu)
            continue
        for i, H in enumerate(L):
            W = hh_scf_q(Q, norm_cdf(rho * zw[i] + math.sqrt(1 - rho * rho) * zq[i]))
            for a in H.a:
                a.wealth = W / len(H.a)
    if wr:
        wt_rank(lst)


def wt_tail_q(s, Cc, O):
    if O['form'] == 'gpd':
        xi = O.get('xi') or Cc['xi']
        sg = O.get('sg') or Cc['sg']
        return Cc['u'] * (1 + sg / xi * (math.pow(s, -xi) - 1))
    return Cc['u'] * math.pow(s, -1 / (O.get('a') or Cc['a']))


def wt_table(Q, P, pc, u):
    q = Q[-1]
    if P <= 0.995 or pc <= 0.995 or not (q > 0) or u <= q:
        return hh_scf_q(Q, P)
    return q * math.pow(u / q, min(1, (P - 0.995) / (pc - 0.995)))


def wt_assign(R, L, t, Q, p, u):
    O = R.WEALTH_TAIL
    Cc = R.S['WT_CUTS'][O['cut']]
    n = len(L)
    pi = Cc['pi'][t]
    m = min(O['m'], n - 1)
    if O.get('flat') or m < 1:
        for i, H in enumerate(L):
            W = hh_scf_q(Q, p[i])
            H._wtJ = 0
            for a in H.a:
                a.wealth = W / len(H.a)
                a._w = 1
                a._wtJ = 0
        return
    B = 1 / (Cc['N'][t] * pi)
    ordr = sorted(range(n), key=lambda i: (p[i], i))
    c = (1 - pi) / (1 - m / n)
    wN = n * (1 - pi) / (n - m)
    for k, i in enumerate(ordr):
        H = L[i]
        j = k - (n - m) + 1
        if j < 1:
            W = min(wt_table(Q, min(p[i] * c, 1 - pi), 1 - pi, Cc['u']), Cc['u'])
            w = wN
            j = 0
        else:
            b0 = math.pow(B, (j - 1) / m)
            b1 = math.pow(B, j / m)
            W = wt_tail_q(b1 + u[j - 1] * (b0 - b1), Cc, O)
            w = n * pi * (b0 - b1) / (1 - B)
        H._wtJ = j
        for a in H.a:
            a.wealth = W / len(H.a)
            a._w = w
            a._wtJ = j


def wt_rank(lst):
    A = [a for H in lst for a in H.a]
    idx = sorted(range(len(A)), key=lambda i: (A[i].wealth, i))
    W = 0.0
    for a in A:
        W += a._w
    c = 0.0
    for i in idx:
        A[i]._wtP = (c + A[i]._w / 2) / W if W > 0 else 0
        c += A[i]._w


def lf_type(a):
    H = a._hh
    if not H:
        return 'single'
    return hh_type(H)


def lf_income(Q, u):
    h = u * (len(Q) - 1)
    k = min(len(Q) - 2, math.floor(h))
    return Q[k] + (Q[k + 1] - Q[k]) * (h - k)


def lf_init(R, agents, seed):
    """14.4 and 14.15."""
    L = R.LF_SCOPE or {}
    R.LFS = NS(r=Mulberry32(seed + 600071), n=0, k={'dis': 0, 'ret': 0, 'care': 0, 'sch': 0}, inc=0.0, z=0)
    S = R.LFS
    if L.get('fl') or (L.get('pm') or 0) > 0:
        S.fl = L.get('fl') or None
        S.pm = float(L.get('pm') or 0)
        S.f = Mulberry32(seed + 730073) if L.get('fl') else None
        S.u = Mulberry32(seed + 730079) if S.pm > 0 else None
        S.ac = NS(iy=0.0, oy=0.0, ex=0.0, rt=0.0, ev=0, k={'dis': 0.0, 'ret': 0.0, 'care': 0.0, 'sch': 0.0}, ay=0.0, pt=0.0, out=0.0, lp=0.0, lpE=0.0, ayY=[], outY=[])
    R.DR_PL = 1
    C = R.CFG
    for a in agents:
        if S.u:
            a._lpU = S.u()
        r = S.r
        u1 = r()
        u2 = r()
        t = lf_type(a)
        Sh = C['LF_SHARES'][t]
        c = 0.0
        why = None
        for rs in R.S['LF_REASONS']:
            c += Sh[rs]
            if u1 < c:
                why = rs
                break
        S.n += 1
        if not why or a._ret:
            continue
        y = lf_income(C['LF_INCOME'][why], u2)
        a._lf = why
        a._lfW = a.wage
        a._ret = True
        a._ssB0 = y
        a._ssY = y * R.DR_PL
        a.wage = a._ssY / 12 / C['WAGE_TO_USD']
        S.k[why] += 1
        S.inc += y
        if not (y > 0):
            S.z += 1
