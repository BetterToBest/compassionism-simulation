#!/usr/bin/env python3
"""S50: a second, independent implementation of the Compassionism Simulation's release row
and its paired no-programme run (Reference, Adverse, Stress), written in Python from the
S50 packet (dev/packets/s50-release-row.zip): MODEL_SPEC.md and ODD.md first, the packet's
code excerpt only where the description leaves a question open (each such question is listed
in GAPS.md beside this file).

Every setting is read from the packet's release-config.json (the constants CFG, the presets,
the study options and the switches in effect while each run goes); nothing is retuned here.

Usage (python3 -I keeps the interpreter from loading modules from the working directory):
  python3 -I s50_release.py --env ref --row release --seed 1          one run, its keys as JSON
  python3 -I s50_release.py --env ref --batch 1 500 --jobs 4          both runs, seeds 1-500, written to results/
  python3 -I s50_release.py --compare results/s50-py-ref-1-500.json   the comparison with the packet's reference
"""
import argparse
import json
import math
import os
import sys
import time
import zipfile
import gzip

INF = float('inf')
M32 = 0xFFFFFFFF
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
DEFAULT_PACKET = os.path.join(ROOT, 'dev', 'packets', 's50-release-row.zip')
RUN_STATE = ('S3_CACHE', 'HL_GOVREF', 'HHS', 'TB_BLEI_NET')  # entries of release-config.json that are run state, not settings (00-START-HERE.md)


# ---------------------------------------------------------------------------------------------
# The packet
# ---------------------------------------------------------------------------------------------
def _fix_inf(x):
    if isinstance(x, dict):
        return {k: _fix_inf(v) for k, v in x.items()}
    if isinstance(x, list):
        return [_fix_inf(v) for v in x]
    if x == 'Infinity':
        return INF
    return x


def packet_read(name, packet=DEFAULT_PACKET):
    """Read one file of the packet (the zip, or an unzipped folder)."""
    if os.path.isdir(packet):
        with open(os.path.join(packet, name)) as f:
            return f.read()
    with zipfile.ZipFile(packet) as z:
        cand = [n for n in z.namelist() if n == name or n.endswith('/' + name)]
        if not cand:
            raise FileNotFoundError(name)
        return z.read(cand[0]).decode('utf-8')


class Packet:
    def __init__(self, packet=DEFAULT_PACKET):
        self.path = packet
        c = json.loads(packet_read('release-config.json', packet))
        self.manifest = c.get('manifest')
        self.atLoad = _fix_inf(c['atLoad'])
        self.CFG = self.atLoad['CFG']
        self.envs = {}
        for env, e in c['envs'].items():
            rows = {}
            for r in e['rows']:
                sw = dict(self.atLoad)
                for k, v in r['switchesDifferentFromLoad'].items():
                    if k in RUN_STATE:
                        continue
                    sw[k] = _fix_inf(v)
                rows[r['row']] = {'p': _fix_inf(r['rowConfig']['p']), 'o': _fix_inf(r['options']), 'sw': sw, 'label': r['label']}
            self.envs[env] = {'env': e['env'], 'rows': rows}


# ---------------------------------------------------------------------------------------------
# Random numbers and samplers (MODEL_SPEC 4.1)
# ---------------------------------------------------------------------------------------------
def imul(a, b):
    return ((a & M32) * (b & M32)) & M32


def mulberry32(seed):
    s = [int(seed) & M32]

    def rng():
        x = (s[0] + 0x6D2B79F5) & M32
        s[0] = x
        t = imul(x ^ (x >> 15), 1 | x)
        t = ((t + imul(t ^ (t >> 7), 61 | t)) & M32) ^ t
        return ((t ^ (t >> 14)) & M32) / 4294967296
    return rng


def jlog(x):
    return math.log(x) if x > 0 else (-INF if x == 0 else float('nan'))


def gamma_s(a, R):
    if a == 1:
        return -math.log(max(1e-14, R()))
    if a < 1:
        return gamma_s(1 + a, R) * math.pow(max(1e-14, R()), 1 / a)
    for _ in range(5000):
        u = R()
        v = R()
        y = math.tan(math.pi * u)
        x = math.sqrt(2 * a - 1) * y + a - 1
        if x > 0 and v <= (1 + y * y) * math.exp((a - 1) * math.log(x / (a - 1)) - math.sqrt(2 * a - 1) * y):
            return x
    return a


def beta_s(a, b, R):
    x = gamma_s(a, R)
    return x / (x + gamma_s(b, R))


def lognormal(mu, sigma, R):
    u = max(1e-14, 1 - R())
    v = R()
    return math.exp(mu + sigma * math.sqrt(-2 * math.log(u)) * math.cos(2 * math.pi * v))


def std_normal(R):
    u = max(1e-14, 1 - R())
    v = R()
    return math.sqrt(-2 * math.log(u)) * math.cos(2 * math.pi * v)


def norm_cdf(z):  # GAPS: the approximation the code uses (an erfc series), not stated in the description
    x = abs(z) / math.sqrt(2)
    t = 1 / (1 + 0.5 * x)
    r = t * math.exp(-x * x - 1.26551223 + t * (1.00002368 + t * (0.37409196 + t * (0.09678418 + t * (-0.18628806 + t * (0.27886807 + t * (-1.13520398 + t * (1.48851587 + t * (-0.82215223 + t * 0.17087277)))))))))
    return 1 - r / 2 if z >= 0 else r / 2


_NA = [-39.69683028665376, 220.9460984245205, -275.9285104469687, 138.3577518672690, -30.66479806614716, 2.506628277459239]
_NB = [-54.47609879822406, 161.5858368580409, -155.6989798598866, 66.80131188771972, -13.28068155288572]
_NC = [-0.007784894002430293, -0.3223964580411365, -2.400758277161838, -2.549732539343734, 4.374664141464968, 2.938163982698783]
_ND = [0.007784695709041462, 0.3224671290700398, 2.445134137142996, 3.754408661907416]


def norm_inv(p):  # GAPS: Acklam's rational approximation, clamped to [1e-12, 1 - 1e-12]
    a, b, c, d = _NA, _NB, _NC, _ND
    p = min(1 - 1e-12, max(1e-12, p))
    if p < 0.02425:
        q = math.sqrt(-2 * math.log(p))
        return (((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1)
    if p > 1 - 0.02425:
        q = math.sqrt(-2 * math.log(1 - p))
        return -(((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1)
    q = p - 0.5
    r = q * q
    return (((((a[0] * r + a[1]) * r + a[2]) * r + a[3]) * r + a[4]) * r + a[5]) * q / (((((b[0] * r + b[1]) * r + b[2]) * r + b[3]) * r + b[4]) * r + 1)


def hash_u(s, id_, yr, j):  # the safety net's take-up: a fixed hash, no stream (12.4)
    h = imul(s ^ 0x5bd1e995, 0x85ebca6b) ^ imul((int(id_) + 0x632be5ab), 0xc2b2ae35) ^ imul((int(yr) + 0x7f4a7c15), 0x27d4eb2f) ^ imul((int(j) + 0x165667b1), 0x9e3779b1)
    h &= M32
    h ^= h >> 16
    h = imul(h, 0x85ebca6b)
    h ^= h >> 13
    h = imul(h, 0xc2b2ae35)
    h ^= h >> 16
    return ((h & M32) + 0.5) / 4294967296


def median_of(arr):
    s = sorted(arr)
    n = len(s)
    if not n:
        return 0
    return (s[n // 2 - 1] + s[n // 2]) / 2 if n % 2 == 0 else s[n // 2]


def quantile_of(arr, q):
    v = sorted(arr)
    h = (len(v) - 1) * q
    lo = math.floor(h)
    hi = math.ceil(h)
    return v[lo] + (v[hi] - v[lo]) * (h - lo)


def gini_of(x):  # section 9: values floored at 0, sorted
    v = sorted(max(0.0, z) for z in x)
    n = len(v)
    t = 0.0
    w = 0.0
    for i in range(n):
        t += v[i]
        w += (i + 1) * v[i]
    return 2 * w / (n * t) - (n + 1) / n if (n > 0 and t > 0) else 0


def gini_neg(x):  # the same with negative values kept (debts counted)
    v = sorted(x)
    n = len(v)
    t = 0.0
    w = 0.0
    for i in range(n):
        t += v[i]
        w += (i + 1) * v[i]
    return 2 * w / (n * t) - (n + 1) / n if (n > 0 and t > 0) else 0


class O(dict):
    """A dict with attribute access, for the engine's small records."""
    __getattr__ = dict.get

    def __setattr__(self, k, v):
        self[k] = v


class Ag:
    """One adult. Class attributes are the values a field has before the engine first sets it."""
    _hh = None; _hhHead = False; _hhD = None; _hhF = None; _hhE = 0; _hhFd = 0; _hhH = 0; _hhT = 0; _hhBU = 1; _hhS = None; _hhPool = False
    yrWageUSD = None; yrConvUSD = 0; yrSSUSD = 0; yrUbiUSD = 0; yrTbCash = 0; yrTax = 0; yrCostUSD = 0; yrBasketUSD = 0; yrWealthStartUSD = 0; yrPjGift = 0
    _esU = None; _esWk = False; _esBU = 0; _esC = 0; _esX = 0; _esR = 0; _esSv = 0; _esPrY = 0
    _fwW = 0; _fwPW = 0; _fwBUm = None; _fwPayY = 0
    _pjR = 0; _pjCap = 0; _pjW = 0; _pjBU = 0; _pjRu = 0; _pjWill = False; _pjSaved = 0; _pjGiftH = 0; _pjHW = 0
    _spE = 0; _spCutY = 0; _spPay = 0; _spOwn = 0; _spBU = 0; _spWk = False; _spVw = 0; _spVE = 0; _spV = 0; _spRest = 0
    _jnY = 0; _wNB = None; _lwNB = None; _lbE0 = 0; _labC = 0; _labCn = 0; _bleiR = 0; _bleiP = 0
    _tbU = 0; _tbEl = False; _tbPart = False; _tbPTH = False; _tbLow = False; _tbTop = False; _tbM = 0; _tbGap = 0; _tbF0 = 0; _tbF2 = 0
    _tbRes = 0; _tbYrs = 0; _tbSp = 0; _tbInSp = False; _tbDisp = 0; _tbExt = 0; _tbPthNow = 0; _tbPthPrev = 0
    _csFree = 0; _pdM = 0; _emW = 0; _emUi = False; _emUiW = 0; _emCut = 0; _emAuto = False; _emOcc = 0
    _snId = None; _snB = 0; _snM = 0; _snAb = None; _snAbC = 0; _pbU = 1; _pbS = None
    _grCut = 0; _grA = 0; _grC = 0; _hhWS = 0; _hhCS = 0; _hhPmB = 0; _hhInc = 0; _hhDisp = 0; _hhMlc = 0; _hhCost = 0; _hhIdx = 1
    _edcR = 0; _edcInt = 0; _edcIntP = 0; _edcBU = 0; _edcY = 0; _h52 = None; _ret = False; age = None


class Latent:
    __slots__ = ('uCCO', 'uPTF', 'uPTH', 'wealth', 'wage', 'octaveShape', 'qualityZ', 'automationRisk', 'lam')


class HH:
    def __init__(self, a, kids):
        self.a = a
        self.kids = kids
        self.hv = 1.0
        self.single = False
        self._sp = None


# ---------------------------------------------------------------------------------------------
# The engine
# ---------------------------------------------------------------------------------------------
class Engine:
    def __init__(self, pk, sw):
        self.pk = pk
        self.CFG = pk.CFG
        C = self.CFG
        self.W2U = C['WAGE_TO_USD']
        self.LWA = C['LIVING_WAGE_ANNUAL']
        self.BASKET = C['BASKET']
        self.BKEYS = C['BASKET_KEYS']
        self.sw = sw
        g = sw.get
        # switches this implementation does not have must be off in these runs
        for k in ('AGE', 'ACCT', 'LEDGER', 'HEALTH', 'DIS', 'C22', 'COMM', 'HCAP', 'REVIEW', 'SAVE', 'OCT', 'AUD', 'DEBT_READ', 'LATENT', 'LW', 'REC_SCRIPT', 'REP_HOOK'):
            if g(k):
                raise SystemExit('switch %s is on; this implementation does not model it' % k)
        if g('AUTOMATION_SAMPLER_LEGACY') or g('CCO_RELIEF_FLAT') or g('RELIEF_PRICE_LEGACY') or g('FBS_BU_ONCE'):
            raise SystemExit('a legacy switch is on')
        self.PTH_APPR_CONSERVE = g('PTH_APPR_CONSERVE')
        self.SURP_CUT_MARKUP = g('SURP_CUT_MARKUP')
        self.PATHWAY_OFF = g('PATHWAY_OFF')
        self.SCS = g('SURPLUS_CONSUMPTION_SHARE')
        self.SCB = g('SURPLUS_CONSUMPTION_BASE')
        self.N7_BLEI = g('N7_BLEI')
        self.BU_SCOPE = g('BU_SCOPE')
        self.PTF_MODE = g('PTF_MODE')
        self.CONVERSION_MODEL = g('CONVERSION_MODEL')
        self.FW = g('FW')
        self.PROJ = g('PROJ')
        self.ESP = g('ESP')
        self.ESP_GOLD = g('ESP_GOLD')
        self.SURP = g('SURP')
        self.PROD = g('PROD')
        self.MULT = g('MULT')
        self.MULT_LS = g('MULT_LS')
        self.PROD_CAP_DEP = g('PROD_CAP_DEP')
        self.PROD_CAP_INT = g('PROD_CAP_INT')
        self.COST = g('COST')
        self.JOIN = g('JOIN')
        self.SPEND_GRADE = g('SPEND_GRADE')
        self.FBS50 = g('FBS50')
        self.HOUSEHOLDS = g('HOUSEHOLDS')
        self.EDC_MEASURE = g('EDC_MEASURE')
        self.THETA_GATE = g('THETA_GATE')
        self.PTH_MODE = g('PTH_MODE')
        self.DISC_BASE = g('DISC_BASE')
        self.PTH_HOUSING_CUT = g('PTH_HOUSING_CUT')
        self.GATE_CURRENT = g('GATE_CURRENT')
        self.RISK_MEASURE = g('RISK_MEASURE')
        self.EMPL = g('EMPL')
        self.PTHB = g('PTHB')
        self.PTFS = g('PTFS')
        self.SNET = g('SNET')
        self.BU_ALLOC = g('BU_ALLOCATIONS_PER_YEAR')
        if self.PTF_MODE != 'shipped' and not self.PTFS:
            raise SystemExit('PTF_MODE other than shipped without PTFS is not modelled')
        if self.FBS50 and (self.FBS50.get('dist') != 'lambda' or (self.FBS50.get('scale') or 1) != 1):
            raise SystemExit('FBS50 readings other than the default are not modelled')
        # run state (the engine's globals that a run sets)
        self.RNG = None
        self.PRICE = None
        self.TB = None
        self.LABOR = None
        self.THETA_DENS = None
        self.HHS = None
        self.EMS = None
        self.SNS = None
        self.PBS = None
        self.PFS = None
        self.FWS = None
        self.PJS = None
        self.ESS = None
        self.SPS = None
        self.PDS = None
        self.JNS = None
        self.MLS = None
        self.EDCS = None
        self.FBSS = None

    # --- small pieces -----------------------------------------------------------------------
    def bu_ess(self):
        return self.CFG['ESSENTIALS_HUB'] if self.BU_SCOPE == 'hub' else self.CFG['ESSENTIALS']

    def szh_theta(self, coh):
        C = self.CFG
        if coh < C['SZH_THETA_THRESHOLD']:
            return 0
        return min(C['SZH_THETA_MAX'], (coh - C['SZH_THETA_THRESHOLD']) / (C['SZH_THETA_MAX_COH'] - C['SZH_THETA_THRESHOLD']) * C['SZH_THETA_MAX'])

    def pth_liquid_share(self, tenure):
        C = self.CFG
        t = max(1, min(C['PTH_LIQUID_SHARE_MATURE_YR'], tenure))
        span = C['PTH_LIQUID_SHARE_MATURE_YR'] - 1
        return C['PTH_LIQUID_SHARE_YEAR1'] + (t - 1) / span * (C['PTH_LIQUID_SHARE_YEAR5PLUS'] - C['PTH_LIQUID_SHARE_YEAR1']) if span > 0 else C['PTH_LIQUID_SHARE_YEAR1']

    def blei(self, a, buAlloc, ccoOn, pthOn, szhOn, szhCoh, ptfOn):  # 6.2
        C = self.CFG
        liquid = max(0, a.wealth * 0.20)
        gammaV = 0.20 if (ccoOn and a.inCCO) else 0.12
        mInc = max(a.wage, 0.1) * self.W2U
        if ccoOn and a.inCCO and buAlloc > 0:
            buFood = a._fwBUm if (self.CONVERSION_MODEL == 'framework' and a._fwBUm is not None) else buAlloc * (990 / 1200)
        else:
            buFood = 0
        szhD = szhCoh * C['SZH_ALL_RESIDENTS'] if szhOn else 0
        if szhOn and ptfOn and a.inPTF:
            szhD += self.szh_theta(self.THETA_DENS if (self.THETA_GATE == 'density' and self.THETA_DENS is not None) else szhCoh) * 0.20
        baseCost = C['CCO_PTH_DAILY_COST'] if (ccoOn and a.inCCO and pthOn and a.inPTH) else C['BASE_DAILY_COST']
        dc = max(baseCost * (1 - szhD), 0.1) * (a._hhD or 1)
        r = (liquid + gammaV * mInc + buFood) / dc
        if math.isnan(r) or math.isinf(r):
            return 0
        return max(0, r)

    def blei0(self, a):  # the no-programme reading
        return self.blei(a, 0, False, False, False, 0, False)

    def agent_edc(self, a, ccoOn, pthOn):
        C = self.CFG
        mInc = max(a.wage, 1)
        w = C['WAGE_MEDIAN_SIU']
        if ccoOn and a.inCCO and pthOn and a.inPTH:
            return min(C['EDC_PTH_CAP'], (C['EDC_PTH_CAP'] * w) / mInc)
        if not ccoOn or not a.inCCO:
            return min(0.75, min(0.50, (0.50 * w) / mInc) + 0.08)
        return min(0.42, min(0.35, (0.35 * w) / mInc) + 0.03)

    def pj_own_rate(self, a, p, pcb):  # 6.6
        C = self.CFG
        oc = 1 + (a.octave / max(1, p['maxOct'])) * (max(1, p['maxMult']) - 1)
        qf = min(1, a.quality / max(1, p['maxMult']))
        ph = C['PHI_RATIO'] if (p['phi'] and a.quality > p['maxMult'] * C['PHI_QUALITY_THRESH']) else 1.0
        pb = pcb if (p['ptf'] and a.inPTF) else 1.0
        return min((1 + qf * (oc - 1)) * ph * pb, p['maxMult'] * (C['PHI_RATIO'] if p['phi'] else 1.0))

    def pj_tax(self, p, r):
        C = self.CFG
        bT = p['tax'] * (1 - p['cipDemo'] * 0.18) if p['cip'] else p['tax']
        return min(C['PROG_TAX_MAX'], bT + max(0, (r - C['PROG_PIVOT']) * C['PROG_RATE']))

    # --- the starting population (4) ---------------------------------------------------------
    def make_latent(self, n):
        C = self.CFG
        R = self.RNG
        pop = []
        for _ in range(n):
            L = Latent()
            L.uCCO = R()
            L.uPTF = R()
            L.uPTH = R()
            L.wealth = lognormal(C['WEALTH_INIT_MU'], C['WEALTH_INIT_SIGMA'], R)
            L.wage = lognormal(3.5, 0.5, R)
            L.octaveShape = beta_s(2, 5, R)
            L.qualityZ = std_normal(R)
            c = R()
            v = R()
            L.automationRisk = math.pow(v, 1 / C['AUTO_HIGH_A']) if c < C['AUTO_HIGH_SHARE'] else 1 - math.pow(1 - v, 1 / C['AUTO_LOW_B'])
            L.lam = C['FBS_LAMBDA_LO'] + R() * (C['FBS_LAMBDA_HI'] - C['FBS_LAMBDA_LO'])
            pop.append(L)
        return pop

    def instantiate(self, L, p):
        a = Ag()
        qN = (1 - p['cipDemo'] * 0.5) if p['cip'] else 1.0
        maxOct = p['maxOct'] or 1
        maxMult = p['maxMult'] or 1
        inPTH = bool(p['pth'] and L.uPTH < p['pthUptake'])
        a.wealth = L.wealth
        a.wage = L.wage
        a.initialWage = L.wage
        a.octave = math.floor(L.octaveShape * maxOct)
        a.quality = min(maxMult, max(0, math.exp(math.log(maxMult * 0.5) + 0.4 * L.qualityZ) * qN))
        a.automationRisk = L.automationRisk
        a.lam = L.lam
        a.uCCO = L.uCCO
        a.inCCO = bool(p['ccoOn'] and L.uCCO < p['partRate'])
        a.inPTF = bool(p['ptf'] and L.uPTF < p['ptfShare'])
        a.inPTH = inPTH
        a.buBalance = 0
        a.acreEquity = 5000 if inPTH else 0
        a.pthTenure = 0
        return a

    def recession_path(self, years, seed):  # 4, item 3
        R = mulberry32(seed + 700000)
        st = O(active=False, incomeMultiplier=1.0, yearsLeft=0)
        path = []
        for y in range(years):
            if y > 0:
                if st.active:
                    st.yearsLeft -= 1
                    if st.yearsLeft <= 0:
                        st.active = False
                        st.incomeMultiplier = 1.0
                elif R() < 0.10:
                    st.active = True
                    st.yearsLeft = 1 + math.floor(R() * 3)
                    st.incomeMultiplier = 0.70 + beta_s(5, 2, R) * 0.25
            path.append(O(active=st.active, incomeMultiplier=st.incomeMultiplier))
        return path

    # --- households (6.13) --------------------------------------------------------------------
    def hh_need(self, H):
        C = self.CFG
        nA = len(H.a)
        nK = len(H.kids)
        R = C['HH_RATIO']['%da%dk' % (nA, min(3, nK))]
        need = {}
        tot = 0
        cc = 0
        nc = 0
        bl = 0
        bl1 = 0
        for k in self.BKEYS:
            need[k] = self.LWA * self.BASKET[k] * R[k]
            tot += need[k]
        for age in sorted(H.kids):
            if age < C['HH_CARE_AGE']:
                cc += C['HH_CHILDCARE'][min(nc, len(C['HH_CHILDCARE']) - 1)]
                nc += 1
        need['childcare'] = cc
        tot += cc
        for k in C['HH_BLEI_KEYS']:
            bl += self.BASKET[k] * R[k]
            bl1 += self.BASKET[k]
        H.single = nA == 1 and nK == 0
        H.need = need
        H.need0 = tot
        H.buM = 1 + (self.HOUSEHOLDS.get('childBU') or 0) * nK / nA
        H.dM = bl / bl1 / nA

    def hh_init(self, agents, seed):
        C = self.CFG
        r = mulberry32(seed + 500009)
        n = len(agents)
        Cm = C['HH_COMP']
        ord_ = list(range(n))
        for i in range(n - 1, 0, -1):
            j = math.floor(r() * (i + 1))
            ord_[i], ord_[j] = ord_[j], ord_[i]
        jround = lambda x: math.floor(x + 0.5)
        nC = jround(n * (Cm['coupleKids'] + Cm['coupleNoKids']) / 2)
        nCK = jround(nC * Cm['coupleKids'] / (Cm['coupleKids'] + Cm['coupleNoKids']))
        nSP = jround(n * Cm['singleParent'])

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
            a1 = agents[ord_[q]]
            a2 = agents[ord_[q + 1]]
            q += 2
            lst.append(HH([a1, a2], kids('couple') if i < nCK else []))
        i = 0
        while i < nSP and q < n:
            lst.append(HH([agents[ord_[q]]], kids('single')))
            q += 1
            i += 1
        while q < n:
            lst.append(HH([agents[ord_[q]]], []))
            q += 1
        for h, H in enumerate(lst):
            H.id = h
            hd = H.a[0]
            self.hh_need(H)
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
        if self.HOUSEHOLDS.get('wealth') == 'scf':
            self.hh_scf_wealth(lst)
        self.HHS = O(list=lst, srng=mulberry32(seed + 500041))

    @staticmethod
    def scf_q(Q, p):
        h = p * 100 - 0.5
        k = math.floor(h)
        if k < 0:
            return Q[0]
        if k >= len(Q) - 1:
            return Q[-1]
        return Q[k] + (Q[k + 1] - Q[k]) * (h - k)

    def hh_scf_wealth(self, lst):
        C = self.CFG
        G = {'coupleKids': [], 'coupleNoKids': [], 'singleParent': [], 'single': []}
        for H in lst:
            G[('coupleKids' if H.kids else 'coupleNoKids') if len(H.a) > 1 else ('singleParent' if H.kids else 'single')].append(H)
        for t in G:
            L = G[t]
            n = len(L)
            Q = C['SCF_NETWORTH_PCTL'] if t == 'single' else C['HH_SCF_PCTL'][t]
            rho = C['HH_SCF_RHO'][t]
            if not n:
                continue

            def scores(f):
                o = sorted([(f(H), i) for i, H in enumerate(L)], key=lambda q: q[0])
                z = [0.0] * n
                for rk, qq in enumerate(o):
                    z[qq[1]] = norm_inv((rk + 0.5) / n)
                return z

            def wsum(H):
                m = 0
                for a in H.a:
                    m = m + a.wage
                return m

            def qsum(H):
                m = 0
                for a in H.a:
                    m = m + a.wealth
                return m
            zw = scores(wsum)
            zq = scores(qsum)
            for i, H in enumerate(L):
                W = self.scf_q(Q, norm_cdf(rho * zw[i] + math.sqrt(1 - rho * rho) * zq[i]))
                for a in H.a:
                    a.wealth = W / len(H.a)

    def hh_year(self, agents):
        bI = self.PRICE.bIdx if self.PRICE else 1
        comp = self.PRICE.comp if self.PRICE else None
        shock = self.HOUSEHOLDS.get('shock')
        ess = self.bu_ess()
        for H in self.HHS.list:
            if H.single:
                continue
            if shock and len(H.a) > 1:
                H.hv = 0.90 + self.HHS.srng() * 0.20
            N = H.need
            c = (lambda k: comp['other' if k == 'childcare' else k]) if comp else (lambda k: 1)
            P = 0
            e = 0
            for k in N:
                P += N[k] * c(k)
            for k in ess:
                e += N[k] * c(k)
            if self.BU_SCOPE == 'hub':
                e += N['childcare'] * c('childcare')
            f = N['food'] * c('food') / P
            hs = N['housing'] * c('housing') / P
            t = N['taxes'] * c('taxes') / P if self.DISC_BASE == 'pretax' else 0
            pS = {'f': f, 'h': hs, 't': N['transport'] * c('transport') / P, 'm': N['medical'] * c('medical') / P, 'k': (N.get('childcare') or 0) * c('childcare') / P} if self.PTFS else None
            for a in H.a:
                a._hhF = P / (len(H.a) * self.LWA * bI)
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
        FLOOR = C['WEALTH_FLOOR']
        for H in self.HHS.list:
            if len(H.a) < 2:
                continue
            n = len(H.a)
            cs = 0
            w = 0
            if self.SCS > 0:
                for a in H.a:
                    cs += a._hhCS if self.SCB == 'cash' else a._hhWS
                sc = self.SCS * max(0, cs) / n
                for a in H.a:
                    a.wealth -= sc
            if self.SPEND_GRADE:
                gA = 0
                gC = 0
                for a in H.a:
                    gA += a._grA
                    gC += a._grC
                gc = gC - gC * math.pow(max(0, gA) / gC, self.SPEND_GRADE['eps']) if (gC > 0 and gA < gC) else 0
                for a in H.a:
                    a._grCut = gc / n
                    a.wealth += gc / n
            for a in H.a:
                w += a.wealth
            w /= n
            for a in H.a:
                a.wealth = w
            if self.PRICE and self.PRICE.acc is not None:
                A = self.PRICE.acc
                for a in H.a:
                    pmW = FLOOR - a.wealth if a.wealth < FLOOR else 0
                    pmU = min(1, ((pmW + a._grCut) if self.SPEND_GRADE else pmW) / a._hhPmB) if a._hhPmB > 0 else 0
                    A.essD -= pmU
                    A.unmet += pmW
                    if pmW > 0:
                        A.unmetN += 1
            if tbOn:
                inc = 0
                mlc = 0
                cost = 0
                disp = 0
                for a in H.a:
                    inc += a._hhInc
                    mlc += a._hhMlc
                    cost += a._hhCost
                    disp += a._hhDisp
                for a in H.a:
                    self.tb_pov(a, self.TB.cur, a._hhIdx, inc / n, mlc / n, cost / n, disp / n)
            for a in H.a:
                if a.wealth < FLOOR:
                    a.wealth = FLOOR

    # --- job loss and re-employment (12.1) ----------------------------------------------------
    def empl_occ(self, agents, seed):
        O_ = self.CFG['EMPL_OCC']
        r = mulberry32(seed + 600041)
        n = len(agents)
        if not n:
            return 0
        lw = [math.log(max(1e-9, a.wage)) for a in agents]
        m = 0
        for x in lw:
            m = m + x
        m = m / n
        v = 0
        for x in lw:
            v = v + (x - m) * (x - m)
        v = v / n
        rho = math.sqrt(min(1, O_['vb'] / v)) if v > 0 else 0
        order = sorted(range(n), key=lambda i: (agents[i].wage, i))
        rk = [0] * n
        for k, i in enumerate(order):
            rk[i] = k
        cum = O_['cum']
        for i, a in enumerate(agents):
            e = norm_inv(min(1 - 1e-12, max(1e-12, r())))
            z = rho * norm_inv((rk[i] + 0.5) / n) + math.sqrt(1 - rho * rho) * e
            q = norm_cdf(z)
            lo = 0
            hi = len(cum) - 1
            while lo < hi:
                mid = (lo + hi) >> 1
                if cum[mid] >= q:
                    hi = mid
                else:
                    lo = mid + 1
            a._emOcc = lo
            a.automationRisk = O_['p'][lo]
        return rho

    def empl_init(self, agents, seed):
        self.EMS = O(r=mulberry32(seed + 600031), n=0, out=0, spells=0, weeks=0, auto=0, ui=0, lost=0, cut=0, cutN=0, long=0, rho=0)
        self.EMS.rho = self.empl_occ(agents, seed) if self.EMPL.get('occ') else 0

    def empl_weeks(self, u, rec):
        s = self.CFG['EMPL_S']['r' if rec else 'n']
        S1 = s[0]
        S2 = s[1]
        if u >= 1:
            return 2.5
        if u >= S1:
            return 2.5 + 7 * jlog(u) / math.log(S1)
        if u >= S2:
            return 9.5 + 11 * (jlog(u) - math.log(S1)) / (math.log(S2) - math.log(S1))
        return 20.5 + s[2] * jlog(S2 / u) if u > 0 else INF

    def empl_year(self, a, rec, aiH, u, wkPay):
        C = self.CFG
        A = self.EMS
        EM = self.EMPL
        w = 0
        ui = 0
        carry = min(52, a._emW or 0)
        a._emW = (a._emW or 0) - carry
        w = carry
        if carry > 0 and a._emUi:
            uw = min(carry, max(0, C['EMPL_UI_WEEKS'] - a._emUiW))
            a._emUiW += uw
            ui += uw * C['EMPL_UI_REPL'] * wkPay
        if carry == 0:
            hA = max(0, aiH * a.automationRisk) if EM['auto'] == 'jobs' else 0
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
                a._emUi = bool(EM.get('ui')) and u[4] < (C['EMPL_UI_RECIP_REC'] if rec else C['EMPL_UI_RECIP'])
                a._emUiW = 0
                if a._emUi:
                    uw2 = min(now, C['EMPL_UI_WEEKS'])
                    a._emUiW = uw2
                    ui += uw2 * C['EMPL_UI_REPL'] * wkPay
                a._emCut = 2 * EM['cut'] * u[5] if (auto or u[1] < (C['EMPL_PERM_REC'] if rec else C['EMPL_PERM'])) else 0
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
        return (min(1, w / 52), ui)

    def empl_res(self, out):
        A = self.EMS
        out['emUrate'] = A.weeks / 52 / A.n * 100 if (A and A.n) else 0
        out['emSpells'] = A.spells / A.n * 100 if (A and A.n) else 0
        out['emWeeks'] = A.weeks / A.out if (A and A.out) else 0
        out['emAuto'] = A.auto / A.n * 100 if (A and A.n) else 0
        out['emUI'] = A.ui / A.lost * 100 if (A and A.lost > 0) else 0
        out['emCut'] = A.cut / A.cutN * 100 if (A and A.cutN) else 0
        out['emLong'] = A.long / A.spells * 100 if (A and A.spells) else 0
        out['emRho'] = A.rho if A else 0
        return out

    # --- PTH's books (12.2) and PTF by sector (12.3) ------------------------------------------
    def pthb_init(self, agents, latent, seed):
        self.PBS = O(r=mulberry32(seed + 600043), q=[], P=1, pi=0, n=0, exits=0, cash=0, cover=0, aP=0, aR=0, aC=0, fill=0, slots=[])
        for i, a in enumerate(agents):
            a._pbU = latent[i].uPTH if i < len(latent) else 1
            if a.inPTH:
                a._pbS = O(V=0, D=0, CE=0)
                self.PBS.slots.append(a._pbS)
            else:
                self.PBS.q.append(a)
        self.PBS.q.sort(key=lambda x: x._pbU)

    def pthb_year(self, agents, yr, P):
        B = self.PBS
        B.pi = P / B.P - 1 if (yr > 0 and B.P > 0) else 0
        B.P = P
        if yr == 0:
            return
        x = self.PTHB['x']
        rate = self.CFG['PTHB_EXIT_OWN'] if self.PTHB['exit'] == 'owners' else self.PTHB['exit']
        u = [B.r() for _ in agents]
        idx = {id(a): i for i, a in enumerate(agents)}
        go = []
        for i, a in enumerate(agents):
            if not a.inPTH or not a._pbS:
                continue
            h = a._hh.a[0] if (a._hh is not None and not a._hh.single) else a
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

    def pthb_res(self, out):
        A = self.PBS
        n = len(A.slots) if (A and A.slots) else 0
        P = A.P if A else 1

        def sm(k):
            s = 0
            for S in A.slots:
                s = s + S[k]
            return s
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
        return out

    def ptfs_shares(self, a, HHA):
        if HHA and a._hhS:
            return a._hhS
        P = self.PRICE
        c = (lambda k: P.comp[k] / P.bIdx) if P else (lambda k: 1)
        B = self.BASKET
        return {'f': B['food'] * c('food'), 'h': B['housing'] * c('housing'), 't': B['transport'] * c('transport'), 'm': B['medical'] * c('medical'), 'k': 0}

    def ptfs_cut(self, a, HHA, p, quiet=False):
        C = self.CFG
        s = self.ptfs_shares(a, HHA)
        eF = C['PTFS_EPS_FOOD_LOW'] if (self.PFS and self.PFS.dens < C['PTFS_LOW_DENS']) else C['PTFS_EPS_FOOD']
        o = self.PTFS['other']
        c = s['f'] * (1 - 1 / eF) + s['h'] * C['PTFS_UTIL'] * (1 - 1 / C['PTFS_EPS_UTIL']) + (s['t'] + s['m'] + s['k']) * o
        if p['szh']:
            c *= (0.12 + p['szhCoh'] * 0.04) / 0.12
        if self.PFS and not quiet:
            self.PFS.cut += c
            self.PFS.cn += 1
        return min(0.95, c)

    def ptfs_year(self, agents, yr):
        F = self.PFS
        u = [F.r() for _ in agents]
        m = 0
        if yr > 0:
            for i, a in enumerate(agents):
                if not a.inPTF or (a._hh is not None and not a._hh.single and a._hh.a[0] is not a):
                    continue
                if u[i] < self.PTFS['leave']:
                    a.inPTF = False
                    F.leave += 1
                    if a._hh is not None:
                        for b in a._hh.a:
                            b.inPTF = False
        for a in agents:
            if a.inPTF:
                m += 1
        F.dens = m / max(1, len(agents))
        F.mem += F.dens
        F.yrs += 1

    def ptfs_res(self, out):
        A = self.PFS
        out['pfCut'] = A.cut / A.cn * 100 if (A and A.cn) else 0
        out['pfLeave'] = A.leave / A.yrs if (A and A.yrs) else 0
        out['pfMem'] = A.mem / A.yrs * 100 if (A and A.yrs) else 0
        return out

    # --- today's safety net (12.4) ------------------------------------------------------------
    def sn_inc_tax(self, f, agi):
        T = self.CFG['SN_TAX']
        x = max(0, agi - T['std'][f])
        lo = 0
        t = 0
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
        snap = 0
        eitc = 0
        ctc = 0
        if E['snap'] and h['takeS'] and (keep or ratio <= E['gross']):
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
        if E['eitc'] and h['takeT'] and (h['nK'] > 0 or h['okAge']):
            P = C['SN_EITC'][min(3, h['nK'])]
            st = P['pj'] if f == 'j' else P['ps']
            en = P['ej'] if f == 'j' else P['es']
            eitc = max(0, min(P['max'], P['max'] / P['inc'] * max(0, earn)) - P['max'] / (en - st) * max(0, max(earn, Y) - st))
        if E['ctc'] and h['takeT'] and h['k17'] > 0:
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
        f = 0
        for l in lost:
            f += l / 12
        return min(snap, f * (1 - self.SNET['abawdEx']) * max(0, snap - w))

    def sn_init(self, agents, seed):
        self.SNS = O(seed=(int(seed) + 700001), idxPrev=1, acc=O(ay=0, ky=0, kN=0, snapN=0, eitcN=0, ctcN=0, snap=0, eitc=0, ctc=0, mN=0, m=0, abN=0, abM=0, abL=0))
        for j, a in enumerate(agents):
            a._snId = j
            a._snB = 0
            a._snM = 0

    def sn_year(self, agents, yr, HHON, inflRate):
        C = self.CFG
        S = self.SNS
        ac = S.acc
        gIdx = math.pow(1 + inflRate, yr) * (self.PRICE.bIdx if self.PRICE else 1)
        units = [(H.a, H.kids, H) for H in self.HHS.list if len(H.a) > 0] if HHON else [([a], [], None) for a in agents]
        SN = self.SNET
        for (ua, ukids, uH) in units:
            nA = len(ua)
            nK = len(ukids)
            earn = 0
            other = 0
            old = False
            okAge = False
            k17 = 0
            hd = ua[0]._snId
            for a in ua:
                if yr == 0 or a.yrWageUSD is None:
                    earn += 0 if a._ret else a.wage * 12 * self.W2U
                else:
                    earn += (a.yrWageUSD or 0) / S.idxPrev
                    other += ((a.yrSSUSD or 0) + (a.yrUbiUSD or 0) + (a.yrConvUSD or 0)) / S.idxPrev
                okAge = True  # no ages in these runs: every adult counts as 25-64
            for age in ukids:
                if age < C['SN_CTC']['age']:
                    k17 += 1
            h = {'nA': nA, 'nK': nK, 'k17': k17, 'other': other,
                 'house': uH.need['housing'] if uH is not None else self.LWA * self.BASKET['housing'],
                 'care': (uH.need.get('childcare') or 0) if uH is not None else 0, 'old': old, 'okAge': okAge,
                 'takeS': hash_u(S.seed, hd, 0, 31) < SN['snapTake'], 'takeT': hash_u(S.seed, hd, 0, 32) < SN['taxTake']}
            b0 = self.sn_ben(h, earn)
            b1 = self.sn_ben(h, earn + 1000, bool(SN.get('slope')) and b0[0] > 0)
            if SN.get('abawd'):
                abK = any(age < 14 for age in ukids)
                abL = []
                for a in ua:
                    l = self.sn_ab_clock(a, (not abK) and (not a._ret), b0[0] > 0)
                    if l > 0:
                        abL.append(l)
                        ac.abN += 1
                        ac.abL += l
                abCut = self.sn_ab_cut(h, earn, b0[0], abL)
                b0[0] -= abCut
                b1[0] -= self.sn_ab_cut(h, earn + 1000, b1[0], abL)
                ac.abM += abCut
            B = b0[0] + b0[1] + b0[2]
            m = max(-0.5, min(0.9, (B - (b1[0] + b1[1] + b1[2])) / 1000))
            for a in ua:
                a._snB = B * gIdx / nA
                a._snM = m if (B > 0 or m != 0) else 0
            ac.ay += nA
            ac.ky += nK
            if B > 0:
                ac.kN += nK
            if b0[0] > 0:
                ac.snapN += nA
            if b0[1] > 0:
                ac.eitcN += nA
            if b0[2] > 0:
                ac.ctcN += nA
            ac.snap += b0[0]
            ac.eitc += b0[1]
            ac.ctc += b0[2]
            if B > 0:
                ac.mN += nA
                ac.m += m * nA
        S.idxPrev = gIdx

    def sn_res(self, out):
        A = self.SNS.acc if self.SNS else None
        ay = A.ay if (A and A.ay) else 1
        pc = lambda x: x / ay * 100 if A else 0
        out['snSnap'] = pc(A.snapN if A else 0)
        out['snEitc'] = pc(A.eitcN if A else 0)
        out['snCtc'] = pc(A.ctcN if A else 0)
        out['snSnapM'] = A.snap / ay if A else 0
        out['snEitcM'] = A.eitc / ay if A else 0
        out['snCtcM'] = A.ctc / ay if A else 0
        out['snAll'] = out['snSnapM'] + out['snEitcM'] + out['snCtcM']
        out['snMtr'] = A.m / A.mN * 100 if (A and A.mN) else 0
        out['snKids'] = A.kN / A.ky * 100 if (A and A.ky) else 0
        if self.SNET and self.SNET.get('abawd'):
            out['snAbN'] = pc(A.abN if A else 0)
            out['snAbM'] = A.abM / ay if A else 0
            out['snAbLost'] = A.abL / ay if A else 0
        return out

    # --- the testbed's yearly pieces: the gate, the labour response, cash flows, accounts ----
    @staticmethod
    def tb_new_acc():
        return O(pjg=0, n=0, cash=0, endow=0, bu=0, conv=0, convM=0, buIss=0, ctax=0, cutFree=0, cutPT=0, cutG=0, cap=0, pthLiq=0, tax=0, base=0, E=0, f0=0, f1=0, f2=0, idx=1, pd=0, tgt=0, emp=0, hrs=0, bR=0, bP=0,
                 bz=0, es=0, n1=0, nP1=0, nN1=0, pyP=0, pyN=0, nWP1=0, esWP=0)

    def tb_year(self, p, colaF):
        s = p['tb']
        TB = self.TB
        TB.cur = self.tb_new_acc()
        if s:
            raise SystemExit('testbed comparators are not modelled')
        return O(ubi=0, xc=0, xd=0, G=0, t=0, tau=TB.tau or 0, X=(TB.X or 0) * (TB.xIdx or 1), tb=TB.tb, cap=TB.tauMax or 0.9, W=0, T=p['years'], gcap=0, gcov=0, Gp=False)

    def tb_gate(self, a, p, buEff, y):
        m = (y.ubi + y.xc + 0) / 12
        if p['ccoOn'] and a.inCCO and buEff > 0:
            m += a._fwBUm if (self.CONVERSION_MODEL == 'framework' and a._fwBUm is not None) else buEff * (990 / 1200)
        a._tbM = m
        return self.blei0(a) + m / self.CFG['BASE_DAILY_COST']

    def tb_lab(self, a, y, E0, cutUSD):
        L = self.LABOR
        ex = L['eps'] - L['rho']
        F = 1
        tx = y.tau > 0 and E0 > y.X
        V = y.ubi + y.xc * (1 - y.xd) + 0
        D = y.xc * y.xd
        if y.tb == 'prog' or y.tb == 'land':
            raise SystemExit('tax bases other than the flat contribution are not modelled')
        elif tx:
            F *= math.pow(1 - y.tau, ex)
            V += y.tau * y.X
        if self.SNET and self.SNS:
            F *= math.pow(1 - a._snM, ex)
            V += a._snB + a._snM * E0
        if self.TB.inkindRho:
            V += cutUSD + (a._tbPthPrev or 0)
        return (F, V, D)

    def tb_cash_flow(self, a, y, E, yr):
        B = 0
        cash = y.ubi + y.xc + B
        tax = y.tau * max(0, E - y.X) if y.tau > 0 else 0
        if self.SNET and self.SNS and a._snB:
            cash += a._snB
        a.yrTbCash = cash
        a.yrTax = tax
        a._tbNit = B
        return (cash - tax, 0)

    def tb_account(self, a, y, yr, mlc, cf, cfPreCCO, costUSD, E, tbG, tbPT):
        TB = self.TB
        C = TB.cur
        idx = mlc / self.LWA / (a._hhF or 1)
        conv = a.yrConvUSD or 0
        TB.xIdx = idx
        C.n += 1
        C.idx = idx
        C.E += E
        C.cash += a.yrTbCash
        if self.SNET and self.SNS and a._snB:
            C.cash -= a._snB
        C.tax += a.yrTax
        C.base += max(0, E - y.X)
        spCut = a._spCutY or 0
        buR = max(0, mlc * (cfPreCCO - cf) - tbG - spCut)
        if a._csFree:
            C.cutFree += a._csFree
            a._csFree = 0
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
        if self.SNET and self.SNS and a._snB:
            pd -= a._snB
        C.pd += pd
        C.tgt += min(pd, max(0, mlc - E - (a.yrSSUSD or 0)))
        inc = E + conv + (a.yrUbiUSD or 0) + (a.yrSSUSD or 0) + a.yrTbCash - a.yrTax + 0
        disp = E + conv + (a.yrUbiUSD or 0) + (a.yrSSUSD or 0) + a.yrTbCash - a.yrTax
        if self.EDCS is not None:
            a._edcY = E + conv + (a.yrUbiUSD or 0) + (a.yrSSUSD or 0) + a.yrTbCash + (a._edcBU or 0)
        if a._hh is not None:
            a._hhInc = inc
            a._hhDisp = disp
            a._hhMlc = mlc
            a._hhCost = costUSD
            a._hhIdx = idx
        if not a._hhPool:
            self.tb_pov(a, C, idx, inc, mlc, costUSD, disp)
        C.emp += 1 if E > 0 else 0
        C.hrs += ((E + a._pjHW) if a._pjHW else E) / a._lbE0 if a._lbE0 > 0 else 1
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

    @staticmethod
    def tb_pov(a, C, idx, inc, mlc, costUSD, disp):
        g = max(0, costUSD - inc) / mlc
        C.f0 += 1 if g > 0 else 0
        C.f1 += g
        C.f2 += g * g
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

    # --- one simulated year (section 5) -----------------------------------------------------
    def run_year(self, agents, yr, p, recSt):
        C = self.CFG
        W2U = self.W2U
        LWA = self.LWA
        PO = self.PATHWAY_OFF
        PRICE = self.PRICE
        TB = self.TB
        LABOR = self.LABOR
        EMPL = self.EMPL
        SNET = self.SNET
        PTFS = self.PTFS
        FLOOR = C['WEALTH_FLOOR']
        n = len(agents)
        totalBU = 0
        totalConversion = 0
        HHON = bool(self.HOUSEHOLDS) and bool(self.HHS) and (self.CONVERSION_MODEL == 'framework' or not p['ccoOn'])
        HHPOOL = HHON and self.HOUSEHOLDS['pool'] != 'individual'
        if HHON:
            self.hh_year(agents)
        pthApprBonus = p['szhCoh'] * 0.01 if p['szh'] else 0
        szhThetaVal = self.szh_theta(p['szhCoh']) if p['szh'] else 0
        if self.THETA_GATE == 'density':
            tdN = 0
            if p['ptf']:
                for a in agents:
                    if a.inPTF:
                        tdN += 1
            self.THETA_DENS = tdN / max(1, n)
            szhThetaVal = self.szh_theta(self.THETA_DENS) if p['szh'] else 0
        ptfConvBonus = 1.30 + (szhThetaVal if (p['szh'] and p['ptf']) else 0)
        szhPartBoost = szhThetaVal * 0.16 if (p['szh'] and p['ccoOn']) else 0
        ptfAdoptFrac = 0
        if PTFS and self.PFS and p['ptf']:
            self.ptfs_year(agents, yr)
        if p['ptf'] and p['ptfShare'] > 0:
            c0 = 0
            for a in agents:
                if a.inPTF:
                    c0 += 1
            ptfAdoptFrac = c0 / max(1, n)
        pthMemberFrac = 0
        if p['pth']:
            c0 = 0
            for a in agents:
                if a.inPTH:
                    c0 += 1
            pthMemberFrac = c0 / max(1, n)
        inflRate = p['inflRate'] or 0
        if p['ptf'] and inflRate > 0 and not (PRICE and PRICE.noDamp):
            inflRate *= (1 - ptfAdoptFrac * 0.5)
        if p['pth'] and inflRate > 0 and not (PRICE and PRICE.noDamp):
            inflRate *= (1 - pthMemberFrac * 0.10)
        powI = math.pow(1 + inflRate, yr)
        dollarCost = C['BASE_DAILY_COST'] * 365 * powI
        if PRICE:
            dollarCost *= PRICE.bIdx
        popShock = recSt.incomeMultiplier if recSt.active else 1.0
        if EMPL and EMPL['rec'] == 'replace' and recSt.active:
            popShock = 1 - max(0, (1 - popShock) - (C['EMPL_P_REC'] * C['EMPL_W_REC'] - C['EMPL_P'] * C['EMPL_W']) / 52)
        mlNT = 0
        tbOn = p.get('tb') is not None
        if self.MULT and TB and tbOn:  # the spending layer (5, A4)
            if yr == 0 or not self.MLS:
                self.MLS = O(push=0, y={})
            mlFill = mlLoss = mlRest = 0
            if recSt.active and popShock < 1 and self.MLS.push > 0:
                mlW = 0
                for a in agents:
                    if a.wage > 0:
                        mlW += a.wage * 12 * W2U
                mlLoss = (1 - popShock) * mlW
                if mlLoss > 0:
                    mlRest = min(mlLoss, self.MULT_LS * self.MULT['m'] * self.MLS.push)
                    mlFill = mlRest / mlLoss
                    popShock += (1 - popShock) * mlFill
            elif self.MULT.get('nt'):
                raise SystemExit('MULT.nt is not modelled')
            self.MLS.y[yr] = O(fill=mlFill, loss=mlLoss, rest=mlRest, push=self.MLS.push)
        FWON = self.CONVERSION_MODEL == 'framework'
        PROD = self.PROD
        SURP = self.SURP
        PDON = bool(PROD) and FWON and bool(p['ptf']) and PROD['cap'] == 'ptf'
        pdCap = 1
        pdLive = 0
        PDS = None
        if PDON:  # PTF capacity (5, A5)
            if yr == 0 or not self.PDS:
                pdN0 = 0
                for a in agents:
                    if a.inPTF:
                        pdN0 += 1
                self.PDS = O(c0=pdN0 / max(1, n), y={}, blk=0, borPA=0, debt=0)
            PDS = self.PDS
            pdK = SURP['K'] if SURP else INF
            pdA = self.SPS.capPA if (yr > 0 and SURP and self.SPS) else 0
            pdCap = 1 if pdK <= 0 else min(1, PDS.c0 + pdA / pdK)
            for a in agents:
                if a.inPTF:
                    pdLive += 1
            pdOwn = pdCap
            pdBor = 0
            if PROD['speed'] == 'oneyear':
                if yr > 0 and pdK < INF and pdK > 0:
                    pdCap = min(1, max(pdOwn, (pdLive + (PDS.blk or 0)) / max(1, n)))
                    pdBor = max(0, pdCap - pdOwn) * pdK
                PDS.blk = 0
                PDS.borPA = pdBor
            PDS.y[yr] = O(cap=pdCap, mem=pdLive / max(1, n), own=pdOwn, bor=pdBor)
        ptfLiveTotal = n
        if p['ptfCap']:
            raise SystemExit('p.ptfCap is not modelled')
        popAIDisp = 0
        if p['automation']:
            if yr >= C['AI_DISPLACEMENT_YEAR_2']:
                popAIDisp = C['AI_DISPLACEMENT_RATE_1'] * (C['AI_DISPLACEMENT_YEAR_2'] - C['AI_DISPLACEMENT_YEAR_1']) + C['AI_DISPLACEMENT_RATE_2'] * (yr - C['AI_DISPLACEMENT_YEAR_2'] + 1)
            elif yr >= C['AI_DISPLACEMENT_YEAR_1']:
                popAIDisp = C['AI_DISPLACEMENT_RATE_1'] * (yr - C['AI_DISPLACEMENT_YEAR_1'] + 1)
            popAIDisp = min(0.10, popAIDisp)
        if p.get('stab'):
            raise SystemExit('the stabiliser is not modelled')
        stabM = 1
        colaF = powI if (p.get('cola') and (p['inflRate'] or 0) > (p.get('colaThresh') or 0)) else 1
        if PRICE:
            pmFull = powI * PRICE.bIdx
            if p.get('cola') and pmFull / PRICE.lastFull - 1 > (p.get('colaThresh') or 0):
                PRICE.colaLevel = pmFull
            PRICE.lastFull = pmFull
            colaF = PRICE.colaLevel if p.get('cola') else 1
        buEff = p['bu'] * stabM * colaF
        if PRICE:
            PRICE.buY = buEff
        agP = powI * (PRICE.bIdx if PRICE else 1)
        tbY = self.tb_year(p, colaF) if (TB and tbOn) else None
        if SNET and self.SNS and tbY:
            self.sn_year(agents, yr, HHON, inflRate)
        if self.PTHB and self.PBS and p['pth']:
            self.pthb_year(agents, yr, agP)
        rsAlt = self.PTH_MODE != 'basket' or self.DISC_BASE != 'basket'
        if not rsAlt:
            raise SystemExit('PTH_MODE basket with DISC_BASE basket is not modelled')
        JOIN = self.JOIN
        if JOIN and FWON and p['ccoOn']:  # joining and leaving (6.9)
            if yr == 0 or not self.JNS:
                self.JNS = O(y={}, join=0, leave=0)
                for a in agents:
                    a._jnY = 0
            JNS = self.JNS
            jnN = jnJ = jnL = 0
            if yr > 0:
                jnIdx = powI * (PRICE.bIdx if PRICE else 1)
                jnM = LWA * jnIdx
                jnE = 0
                for k in self.bu_ess():
                    jnE += self.BASKET[k] * (PRICE.comp[k] if PRICE else 1)
                if PRICE:
                    jnE /= PRICE.bIdx
                jnF = self.BASKET['food'] * (PRICE.comp['food'] / PRICE.bIdx if PRICE else 1)
                jnH = self.BASKET['housing'] * (PRICE.comp['housing'] / PRICE.bIdx if PRICE else 1)
                jnRs = self.PTH_MODE != 'basket' or self.DISC_BASE != 'basket'
                for a in agents:
                    jHH = HHON and a._hh is not None and not a._hh.single
                    ef = a._hhE if jHH else jnE
                    u = 1
                    jH = a._hhH if jHH else jnH
                    jM = jnM * a._hhF if jHH else jnM
                    jB = buEff * a._hhBU if jHH else buEff
                    if p['ptf'] and a.inPTF:
                        jnC = 1 - self.ptfs_cut(a, jHH, p, True)
                        ef = ef * jnC
                        if jnRs:
                            u = jnC
                    if p['pth'] and a.inPTH and not PO['pthCost']:
                        if self.PTH_MODE == 'housing':
                            ef -= self.PTH_HOUSING_CUT * jH * u
                        else:
                            ef *= 0.65
                    use = min(12 * jB, jM * ef)
                    if JOIN['cost'] == 'none':
                        cost = 0
                    else:
                        cost = 12 * p['bu'] * a.uCCO / max(1e-9, p['partRate']) * (1 if JOIN['cost'] == 'nominal' else jnIdx)
                    want = p['bu'] > 0 and use >= cost
                    if a.inCCO and not want and yr - a._jnY >= JOIN['stay']:
                        a.inCCO = False
                        a._jnY = yr
                        jnL += 1
                    elif not a.inCCO and want:
                        a.inCCO = True
                        a._jnY = yr
                        jnJ += 1
                if HHON:
                    self.hh_sync('cco')
            for a in agents:
                if a.inCCO:
                    jnN += 1
            JNS.join += jnJ
            JNS.leave += jnL
            JNS.y[yr] = O(part=jnN / max(1, n), join=jnJ, leave=jnL)
        if FWON:
            if yr == 0 or not self.FWS:
                self.FWS = O(prev=None)
            self.FWS.next = O(bizBU=0, projBU=0, expiredBU=0, destroyedBU=0, wSum=0, pwSum=0, projAlloc=0, projGross=0, projTax=0, projNet=0, projLost=0, bizPaid=0)
        FWS = self.FWS
        FW = self.FW
        PROJ = self.PROJ
        PJON = bool(PROJ)
        pjPay = 0
        pjIdx = 1
        pjCipB = 1
        pjFg = 0
        PJS = None
        if PJON:  # project hiring (6.5)
            if yr == 0 or not self.PJS:
                self.PJS = O(prev=None, acc=O(pool=0, gift=0, exp=0, alloc=0, carry=0, conv=0, giftConv=0, gross=0, net=0, giftNet=0, hrs=0, disp=0, work=0, partY=0, rc=0, rcN=0, overCap=0, unwilling=0))
            PJS = self.PJS
            PJS.next = O(pool=0, gpool=0)
            pjIdx = powI * (PRICE.bIdx if PRICE else 1)
            pjPay = PROJ['pay'] * pjIdx
            pjCipB = (1 + p['cipDemo'] * 0.12) if p['cip'] else 1.0
            pjP = []
            pjWt = 0
            pjWR = 0
            pjIn = PJS.prev.pool + PJS.prev.gpool if PJS.prev else 0
            pjCarry = 0
            pjFg = PJS.prev.gpool / pjIn if pjIn > 0 else 0
            if p['ccoOn']:
                for a in agents:
                    if not a.inCCO:
                        continue
                    r = self.pj_own_rate(a, p, ptfConvBonus)
                    cap = 12 * FW['octaveCapBase'] * math.pow(2, a.octave)
                    w = cap * max(0, a.quality)
                    a._pjR = r
                    a._pjCap = cap
                    a._pjW = w
                    a._pjBU = 0
                    pjWt += w
                    pjWR += w * r
                    pjP.append(a)
            pjRc = pjWR / pjWt if pjWt > 0 else 1
            pjSet = []
            PJS.acc.rc += pjRc
            PJS.acc.rcN += 1
            for a in pjP:
                ru = max(a._pjR, pjRc) if PROJ['rate'] == 'max' else a._pjR
                v = pjPay * ru * (1 - self.pj_tax(p, ru)) * pjCipB
                h = a.wage * 12 * W2U / PROJ['hrsYr']
                a._pjRu = ru
                a._pjWill = v > (0 if a._ret else h)
                if PROJ['alloc'] == 'capqAll' or a._pjWill:
                    pjSet.append(a)
            if pjIn > 0 and pjSet:
                if PROJ['alloc'] in ('low', 'equal'):
                    raise SystemExit('PROJ.alloc %s is not modelled' % PROJ['alloc'])
                pjS = 0
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
                    PJS.acc.alloc += a._pjBU / pjIdx
                    PJS.acc.work += 1
                    if not a._pjWill:
                        PJS.acc.unwilling += 1
            PJS.acc.carry = pjCarry / pjIdx
            PJS.next.pool += pjCarry * (1 - pjFg)
            PJS.next.gpool += pjCarry * pjFg
            PJS.acc.partY += len(pjP)
            if yr == 0 and PROJ['giftMode'] == 'forward' and PROJ['gift'] > 0:
                PJS.next.gpool += PROJ['gift'] * len(pjP)
                PJS.acc.gift += PROJ['gift'] * len(pjP)
                PJS.acc.pool += PROJ['gift'] * len(pjP)
            if PROJ['giftMode'] == 'holder':
                raise SystemExit('PROJ.giftMode holder is not modelled')
        ESP = self.ESP
        ESON = FWON and bool(ESP)
        esIdx = 1
        esCipB = 1
        ESS = None
        if ESON:  # ESP payroll (6.7)
            if yr == 0 or not self.ESS:
                self.ESS = O(prev=None, acc=O(accBU=0, ownBU=0, poolPaid=0, alloc=0, conv=0, ret=0, retNon=0, retPar=0, retCap=0, retWage=0, retNet=0, gross=0, tax=0, prem=0, rateXbu=0,
                                             wkY=0, wkY1=0, wage=0, partWkY=0, tk=0, capBind=0, maxShare=0, sv=0), y={})
            ESS = self.ESS
            esIdx = powI * (PRICE.bIdx if PRICE else 1)
            esCipB = (1 + p['cipDemo'] * 0.12) if p['cip'] else 1.0
            esA = ESS.acc
            esPool = ESS.prev.pool if ESS.prev else 0
            esW = 0
            esRet = 0
            esSv = 0
            esY = ESS.y[yr] = O(pool=esPool, conv=0, ret=0, sv=0)
            if ESP['cap'] == 'save' or ESP['take'] == 'biz':
                raise SystemExit('ESP readings other than the default are not modelled')
            for i, a in enumerate(agents):
                if a._esU is None:
                    a._esU = ((i + 1) * self.ESP_GOLD) % 1
                if ESP['work'] == 'all':
                    wk = True
                elif ESP['work'] == 'ptf':
                    wk = bool(p['ptf'] and a.inPTF)
                else:
                    wk = a._esU < ESP['work']
                a._esWk = wk and not a._ret
                a._esBU = 0
                a._esC = 0
                a._esX = 0
                a._esR = 0
                if a._esWk:
                    esW += max(0, a._fwW or 0)
            ESS.wW = esW
            esA.poolPaid += esPool / esIdx
            for a in agents:
                if not a._esWk and not (a._esSv > 0):
                    continue
                w = max(0, a._fwW or 0)
                sh = 0
                bu = 0
                if a._esWk:
                    esA.wkY += 1
                    if yr > 0:
                        esA.wkY1 += 1
                        esA.wage += w / esIdx
                    if esPool > 0 and esW > 0:
                        sh = esPool * w / esW
                        bu = min(sh, w)
                        if sh > bu:
                            esRet += sh - bu
                            esA.retWage += (sh - bu) / esIdx
                        if w > 0:
                            esA.maxShare = max(esA.maxShare, bu / w)
                    a._esBU = bu
                    esA.alloc += bu / esIdx
                if not (p['ccoOn'] and a.inCCO):
                    esRet += bu
                    esA.retNon += bu / esIdx
                    continue
                if a._esWk:
                    esA.partWkY += 1
                r = self.pj_own_rate(a, p, ptfConvBonus)
                tx = self.pj_tax(p, r)
                ok = r * (1 - tx) * esCipB > 1
                if not ok:
                    esRet += bu
                    esA.retPar += bu / esIdx
                    continue
                have = bu
                cap = INF if ESP['cap'] == 'none' else max(0, 12 * FW['octaveCapBase'] * math.pow(2, a.octave) - (((a._pjBU or 0) + (a._pjSaved or 0)) if PJON else 0))
                c = min(have, cap)
                a._esK = cap
                if have > c + 1e-9:
                    esA.capBind += 1
                    esRet += have - c
                    esA.retCap += (have - c) / esIdx
                if c > 0:
                    a._esC = c
                    a._esR = r
                    a._esX = c * (r * (1 - tx) * esCipB - 1) / w if w > 0 else 0
                    esA.tk += 1
            esY.ret = esRet
            esY.sv = esSv
            esA.ret += esRet / esIdx
            esA.sv = esSv / esIdx
            for a in agents:
                esY.conv += a._esC
            if esRet > 0 and FWS.prev:
                esBT = p['tax'] * (1 - p['cipDemo'] * 0.18) if p['cip'] else p['tax']
                esTR = min(C['PROG_TAX_MAX'], esBT + max(0, (FW['bizRate'] - C['PROG_PIVOT']) * C['PROG_RATE']))
                esTP = min(C['PROG_TAX_MAX'], esBT)
                esRG = esRet * (FW['bizCap'] * FW['bizRate'] + (1 - FW['bizCap']))
                esRT = esRet * (FW['bizCap'] * FW['bizRate'] * esTR + (1 - FW['bizCap']) * esTP)
                esRN = 0 if PO['conversion'] else esRG - esRT - esRet
                FWS.prev.bizNet += esRN
                esA.retNet += esRN / esIdx
                if tbY:
                    TB.cur.ctax += esRT
        bIdxP = PRICE.bIdx if PRICE else 1
        eShareCur = 0
        fShareCur = self.BASKET['food']
        for k in self.bu_ess():
            eShareCur += self.BASKET[k] * (PRICE.comp[k] if PRICE else 1)
        if PRICE:
            eShareCur /= PRICE.bIdx
            fShareCur = self.BASKET['food'] * PRICE.comp['food'] / PRICE.bIdx
        tShareCur = (self.BASKET['taxes'] * (PRICE.comp['taxes'] / PRICE.bIdx if PRICE else 1)) if self.DISC_BASE == 'pretax' else 0
        hShareCur = self.BASKET['housing'] * (PRICE.comp['housing'] / PRICE.bIdx if PRICE else 1)
        pretax = self.DISC_BASE == 'pretax'
        SPON = FWON and bool(SURP)
        spDelta = 0
        spProfW = 0
        spRestW = 0
        spOwnW = 0
        SPS = None
        spIdx = 1
        if SPON:  # the ESP surplus split (6.7)
            if yr == 0 or not self.SPS:
                self.SPS = O(capPA=0, cap=0, carry=0, carryP=0, sw=-1, acc=O(pool=0, own=0, ptf=0, rest=0, pricePool=0, cut=0, cutN=0, cutP=0, freed=0, cash=0, carry=0, profit=0, profitN=0, reinv=0, wkY=0, wkY1=0,
                                                                          d1=0, n1=0, d2=0, n2=0, non=0, yrs=0), y={}, carryV=None)
            SPS = self.SPS
            spIdx = powI * (PRICE.bIdx if PRICE else 1)
            spA = SPS.acc
            spN = n
            spPool = FWS.prev.bizNet if FWS.prev else 0
            if SURP['priv'] in ('owners', 'prices'):
                spS = ((FWS.prev.get('bizBUptf') or 0) / FWS.prev.bizBU) if (FWS.prev and FWS.prev.bizBU > 0) else 0
            else:
                spS = 1
            if yr == 0:
                spPh = 1
            elif SURP['swYear'] is not None:
                spPh = 2 if yr >= SURP['swYear'] else 1
            else:
                spPh = 2 if ((SURP['K'] <= 0 or PDS.c0 + SPS.capPA / SURP['K'] >= 1) if PDON else SPS.capPA >= SURP['K']) else 1
            if spPh == 2 and SPS.sw < 0:
                SPS.sw = yr
            spSh = SURP['p1'] if spPh == 1 else SURP['p2']
            spPtf = spPool * spS
            spOwn = spPool - spPtf
            spChD = 0
            spChI = 0
            spChDue = 0
            if PDON and PROD['speed'] == 'oneyear':
                spChDue = (PDS.borPA or 0) * (self.PROD_CAP_DEP + self.PROD_CAP_INT) * spN * spIdx + (PDS.debt or 0) * spIdx
                spChPd = min(spPtf, spChDue)
                PDS.debt = (spChDue - spChPd) / spIdx
                spPtf -= spChPd
                spChD = spChPd * self.PROD_CAP_DEP / (self.PROD_CAP_DEP + self.PROD_CAP_INT)
                spChI = spChPd - spChD
                if tbY:
                    TB.cur.conv += spChPd
                    TB.cur.convM += spChD
                if PRICE and PRICE.acc is not None:
                    PRICE.acc.conv += spChPd
                SPS.acc.chD = (SPS.acc.chD or 0) + spChD / spIdx
                SPS.acc.chI = (SPS.acc.chI or 0) + spChI / spIdx
            spRest = spPtf * max(0, 1 - spSh[0] - spSh[1] - spSh[2])
            spCarryIn = SPS.carry
            spPP = spPtf * spSh[0] + (spPtf * spSh[1] if SURP['rv'] == 'price' else 0) + SPS.carry
            spRv = 0 if SURP['rv'] == 'price' else spPtf * spSh[1]
            spPr = spPtf * spSh[2] + SPS.carryP
            SPS.carryP = 0
            if SURP['cust'] == 'auto':
                spCust = 'ptf' if SURP['priv'] in ('owners', 'prices') else 'all'
            else:
                spCust = SURP['cust']
            spVOn = SURP['priv'] == 'prices'
            spVW = 0
            spVP = 0
            spVSum = 0
            spVUsed = 0
            if spVOn:
                if SPS.carryV is None:
                    SPS.carryV = 0
                spVW = 0 if SURP['privWk'] == 'none' else spOwn * spSh[2]
                spVP = spOwn - spVW + SPS.carryV
                spPr += spVW
                spOwn = 0
            spMlc = LWA * powI
            if PRICE:
                spMlc *= PRICE.bIdx
            spSum = 0
            spWW = 0
            spWO = 0
            if SURP['bu'] == 'cash' or SURP['wk'] not in ('espPart', 'esp', 'all') and False:
                raise SystemExit('SURP.bu cash is not modelled')
            for a in agents:
                bp = p['ccoOn'] and a.inCCO and p['bu'] > 0 and not PO['relief']
                isC = spCust == 'all' or (spCust == 'pp' and ((p['ccoOn'] and a.inCCO) or (p['ptf'] and a.inPTF))) or (spCust == 'ptf' and p['ptf'] and a.inPTF) or (spCust == 'part' and p['ccoOn'] and a.inCCO)
                e = 0
                sHH = HHON and a._hh is not None and not a._hh.single
                sE = a._hhE if sHH else eShareCur
                sH = a._hhH if sHH else hShareCur
                sM = spMlc * a._hhF if sHH else spMlc
                if isC:
                    ef = sE
                    u = 1
                    if p['ptf'] and a.inPTF:
                        spC = 1 - self.ptfs_cut(a, sHH, p, True)
                        ef = ef * spC
                        if rsAlt:
                            u = spC
                    if p['pth'] and a.inPTH and not PO['pthCost']:
                        if self.PTH_MODE == 'housing':
                            ef -= self.PTH_HOUSING_CUT * sH * u
                        else:
                            ef *= 0.65
                    e = sM * ef
                if spVOn:
                    vBu = max(0, a._spBU or 0) if (bp and not (p['ptf'] and a.inPTF)) else 0
                    vE = 0
                    if vBu > 0:
                        vE = sE
                        if p['pth'] and a.inPTH and not PO['pthCost']:
                            if self.PTH_MODE == 'housing':
                                vE -= self.PTH_HOUSING_CUT * sH
                            else:
                                vE *= 0.65
                        vE *= sM
                    a._spVw = vBu
                    a._spVE = vE
                    spVSum += vBu
                a._spE = e
                a._spCutY = 0
                a._spPay = 0
                a._spOwn = 0
                a._spBU = 0
                a._spWk = bool(a._esWk) and (SURP['wk'] != 'espPart' or bool(p['ccoOn'] and a.inCCO))
                spSum += e
                if a._spWk:
                    spWW += max(0, a._fwW or 0)
                spWO += max(0, a.wealth)
            spDelta = min(1, spPP / spSum) if spSum > 0 else 0
            spUsed = spDelta * spSum
            SPS.carry = spPP - spUsed
            if spVOn:
                for a in agents:
                    a._spV = min(spVP * a._spVw / spVSum, a._spVE) if (spVSum > 0 and a._spVw > 0) else 0
                    spVUsed += a._spV
                SPS.carryV = spVP - spVUsed
            if spWW > 0:
                spProfW = spPr / spWW
            else:
                SPS.carryP = spPr
                spPr = 0
            spRestOn = spRest > 0 and FWS.prev and FWS.prev.wSum > 0
            spRestW = max(0, spRest) / FWS.prev.wSum if spRestOn else 0
            if spWO > 0:
                spOwnW = spOwn / spWO
            else:
                SPS.carry += spOwn
                spOwn = 0
            for a in agents:
                w = a._fwW or 0
                a._spOwn = spOwnW * max(0, a.wealth)
                a._spRest = spRest * w / FWS.prev.wSum if spRestOn else 0
                a._spPay = (spPr * max(0, w) / spWW if (a._spWk and spWW > 0) else 0) + a._spRest + a._spOwn
            SPS.cap += spRv
            SPS.capPA += spRv / spIdx / spN
            if tbY:
                TB.cur.conv += spRv
                if PROD:
                    TB.cur.convM += spRv
            if PRICE and PRICE.acc is not None:
                PRICE.acc.conv += spRv
            spA.pool += spPool / spIdx
            spA.own += spOwn / spIdx
            if spVOn:
                spA.privW = (spA.privW or 0) + spVW / spIdx
                spA.privP = (spA.privP or 0) + (spVP - SPS.carryV) / spIdx
            spA.ptf += spPtf / spIdx
            spA.rest += spRest / spIdx
            spA.pricePool += (spPP - spCarryIn) / spIdx
            spA.reinv += spRv / spIdx
            spA.carry = SPS.carry / spIdx
            if yr > 0:
                if spPh == 1:
                    spA.d1 += spDelta
                    spA.n1 += 1
                else:
                    spA.d2 += spDelta
                    spA.n2 += 1
                spA.yrs += 1
            SPS.y[yr] = O(cut=0, freed=0, paid=0, pjFreed=0, cutV=0)

        # --- B. each adult in array order -----------------------------------------------------
        R = self.RNG
        EMS = self.EMS
        PJacc = PJS.acc if PJS else None
        LA = LABOR.get('acc') if LABOR else None
        SG = self.SPEND_GRADE
        SCS = self.SCS
        cashBase = self.SCB == 'cash'
        HSH = self.HOUSEHOLDS.get('shock') if self.HOUSEHOLDS else None
        EDCS = self.EDCS
        PTHB = self.PTHB
        PBS = self.PBS
        mlcBase = LWA * powI
        for a in agents:
            if math.isnan(a.wealth):
                a.wealth = 0
            if math.isnan(a.wage) or a.wage <= 0:
                a.wage = 1
            HHA = HHON and a._hh is not None and not a._hh.single
            if HHA:
                eSA = a._hhE
                fSA = a._hhFd
                hSA = a._hhH
                buA = buEff * a._hhBU
                dcA = dollarCost * a._hhD
                tShA = a._hhT
            else:
                eSA = eShareCur
                fSA = fShareCur
                hSA = hShareCur
                buA = buEff
                dcA = dollarCost
                tShA = tShareCur
            HHP = HHPOOL and HHA and len(a._hh.a) > 1
            if HHON:
                a._hhPool = HHP
            a.yrWealthStartUSD = a.wealth
            agentVar = 0.90 + R() * 0.20
            incomeShock = popShock * agentVar
            if HHON and HSH and a._hh is not None and len(a._hh.a) > 1:
                hsR = C['HH_SHOCK_CORR'][1 if recSt.active else 0] if HSH == 'shore' else float(HSH)
                hsA = min(1, abs(hsR))
                hsS = -1 if (hsR < 0 and a._hh.a[1] is a) else 1
                agentVar = 1 + math.sqrt(hsA) * hsS * (a._hh.hv - 1) + math.sqrt(1 - hsA) * (agentVar - 1)
                incomeShock = popShock * agentVar
                a._shkV = agentVar
                a._shkR = bool(recSt.active)
            if EDCS is not None:
                a._edcInt = 0
                a._edcBU = 0
            uSpendFrac = 0.60 + R() * 0.30
            uCipQuality = R()
            uAdvance = R()
            uSzhInduce = R()
            uSzhPtfShare = R()
            uPthAppr = R()
            uPtfAdopt = R()
            inCCO = p['ccoOn'] and a.inCCO
            ptfMem = p['ptf'] and a.inPTF
            pthMem = p['pth'] and a.inPTH and not PO['pthCost']
            if self.GATE_CURRENT and FWON and inCCO and p['bu'] > 0 and not PO['relief']:
                gEss = eSA
                if ptfMem:
                    gEss = gEss * (1 - self.ptfs_cut(a, HHA, p, True))
                if pthMem:
                    if self.PTH_MODE == 'housing':
                        gEss -= self.PTH_HOUSING_CUT * hSA * ((1 - self.ptfs_cut(a, HHA, p, True)) if (rsAlt and ptfMem and PTFS) else 1)
                    else:
                        gEss *= 0.65
                gCost = mlcBase
                if PRICE:
                    gCost *= PRICE.bIdx
                if HHA:
                    gCost *= a._hhF
                a._fwBUm = min(12 * buA, gCost * gEss) / 12
            bleiCheck = self.blei(a, buA, p['ccoOn'], p['pth'], p['szh'], p['szhCoh'], p['ptf'])
            tbNB = self.tb_gate(a, p, buA, tbY) if tbY else 0
            wg = C['WAGE_BASE_GROWTH']
            bleiGate = tbNB if (tbY and TB.neutralGate) else bleiCheck
            bleiProg = 0
            a._bleiR = 0
            a._bleiP = 0
            if bleiGate > C['BLEI_PRECARIOUS_MAX'] and not PO['bleiWage']:  # 6.1
                drFactor = 1 / (1 + 0.5 * max(0, a.wage / C['WAGE_MEDIAN_SIU'] - 1))
                wg += C['WAGE_BLEI_BONUS'] * max(0.1, drFactor)
                a._bleiR = 1
                if not (self.blei0(a) > C['BLEI_PRECARIOUS_MAX']):
                    a._bleiP = 1
                    if self.N7_BLEI:
                        bleiProg = C['WAGE_BLEI_BONUS'] * max(0.1, drFactor)
            if not PO['octaveWage']:
                wg += a.octave * C['WAGE_OCTAVE_BONUS']
            if p['cip']:
                wg += p['cipDemo'] * 0.005
            if LABOR and a._lwNB is None:
                a._lwNB = a.wage
            if PRICE:
                if a._wNB is None:
                    a._wNB = a.wage
                if PRICE.wIdx:
                    wg += PRICE.wIdx * PRICE.piG
            if not (EMPL and EMPL['auto'] == 'jobs'):
                wg -= popAIDisp * a.automationRisk
            a.wage = max(a.wage * 0.80, a.wage * (1 + wg))
            prog = (0 if PO['octaveWage'] else a.octave * C['WAGE_OCTAVE_BONUS']) + (p['cipDemo'] * 0.005 if p['cip'] else 0) + bleiProg
            if LABOR:
                a._lwNB = max(a._lwNB * 0.80, a._lwNB * (1 + wg - prog))
            if PRICE:
                a._wNB = max(a._wNB * 0.80, a._wNB * (1 + wg - prog))
            # 6.3: the cost factor (PTF cut on the pre-tax basket, PTH on housing)
            cf = 1.0
            rsPtfU = 1
            rsRel = 1
            if ptfMem:
                rsPtfU = 1 - self.ptfs_cut(a, HHA, p)
                cf = tShA + (cf - tShA) * rsPtfU if pretax else cf * rsPtfU
            cfPTF = cf
            if pthMem:
                if self.PTH_MODE == 'housing':
                    cf -= self.PTH_HOUSING_CUT * hSA * rsPtfU
                else:
                    cf = tShA + (cf - tShA) * 0.65 if pretax else cf * 0.65
            cfPreCCO = cf
            if inCCO and p['bu'] > 0 and not PO['relief'] and not FWON:
                raise SystemExit('the engine conversion model is not modelled')
            hcX = 0
            mlc = mlcBase
            if PRICE:
                mlc *= PRICE.bIdx
            if HHA:
                mlc *= a._hhF
            if EDCS is not None:
                a._edcR = 0 if (p['pth'] and a.inPTH) else mlc * (hSA + hcX)
                a._edcInt = a._edcIntP or 0
                a._edcIntP = 0
            fwB = 0
            fwLeft = 0
            if FWON and inCCO and p['bu'] > 0 and not PO['relief']:  # 6.4: BU purchases and expiry
                essF = eSA
                if ptfMem:
                    essF = essF * (1 - self.ptfs_cut(a, HHA, p, True))
                if pthMem:
                    if self.PTH_MODE == 'housing':
                        essF -= self.PTH_HOUSING_CUT * hSA * rsPtfU
                    else:
                        essF *= 0.65
                fwBudget = 12 * buA
                fwB = min(fwBudget, mlc * essF)
                spC = 0
                fwB0 = fwB
                if tbY:
                    TB.cur.buIss += fwBudget
                if EDCS is not None:
                    a._edcBU = fwBudget
                if SPON and a._spE > 0 and spDelta > 0:
                    spE = mlc * essF
                    spC = spDelta * spE
                    fwB = min(fwBudget, spE - spC)
                    a._spCutY = spC
                    spY = SPS.y[yr]
                    spY.cut += spC
                    spY.freed += fwB0 - fwB
                    SPS.acc.cut += spC / spIdx
                    SPS.acc.cutP += spC / spIdx
                    SPS.acc.freed += (fwB0 - fwB) / spIdx
                    SPS.acc.cash += (spC - (fwB0 - fwB)) / spIdx
                if SPON and a._spV > 0:
                    vSpE = mlc * essF
                    vC = min(a._spV, max(0, vSpE - spC))
                    vB = fwB
                    if vC > 0:
                        spC += vC
                        fwB = min(fwBudget, vSpE - spC)
                        a._spCutY = spC
                        vY = SPS.y[yr]
                        vY.cut += vC
                        vY.cutV += vC
                        vY.freed += vB - fwB
                        SPS.acc.cut += vC / spIdx
                        SPS.acc.cutP += vC / spIdx
                        SPS.acc.cutV = (SPS.acc.cutV or 0) + vC / spIdx
                        SPS.acc.freed += (vB - fwB) / spIdx
                        SPS.acc.cash += (vC - (vB - fwB)) / spIdx
                fwLeft = fwBudget - fwB
                cf = cfPreCCO + hcX - fwB / mlc
                if spC:
                    cf -= spC / mlc
                a._fwBUm = fwB0 / 12
                if SPON:
                    a._spBU = fwB
                    if ptfMem:
                        FWS.next.bizBUptf = (FWS.next.get('bizBUptf') or 0) + fwB
                if SPON and PJON:
                    SPS.y[yr].pjFreed += (fwB0 - fwB) * PROJ['share']
                FWS.next.bizBU += fwB
                FWS.next.expiredBU += fwLeft
                FWS.next.projBU += fwLeft * FW['directedShare']
                FWS.next.destroyedBU += fwLeft * (1 - FW['directedShare'])
                if PJON:
                    PJS.next.pool += fwLeft * PROJ['share']
                    PJacc.exp += fwLeft / pjIdx
                    PJacc.pool += fwLeft * PROJ['share'] / pjIdx
            elif SPON and a._spE > 0 and spDelta > 0:
                spC2 = spDelta * a._spE
                cf -= spC2 / mlc
                a._spCutY = spC2
                SPS.y[yr].cut += spC2
                SPS.acc.cut += spC2 / spIdx
                SPS.acc.cash += spC2 / spIdx
                if not a.inCCO:
                    SPS.acc.cutN += spC2 / spIdx
                else:
                    SPS.acc.cutP += spC2 / spIdx
            # 12.1: job loss (six draws on its own stream, every adult-year)
            emQ = None
            emWk = 0
            if EMPL and EMS:
                rr = EMS.r
                emU = [rr(), rr(), rr(), rr(), rr(), rr()]
                emWk = a.wage * 12 * W2U * incomeShock / 52
                if not a._ret:
                    emQ = self.empl_year(a, recSt.active, popAIDisp, emU, emWk)
            annualWageUSD = 0 if a._ret else a.wage * 12 * W2U * incomeShock * (1 + mlNT)
            if emQ:
                annualWageUSD *= 1 - emQ[0]
            tbG = 0
            tbPT = 0
            if tbY and self.COST and ptfMem:
                a._csFree = min(mlc * (1 - cfPTF), mlc * (fSA * self.COST['food'] + hSA * self.COST['util']))
            if tbY:
                tbPT = mlc * (1 - cfPreCCO)
            if LABOR:  # 6.11
                lbE0 = annualWageUSD
                lbBU = 0
                lbR = 0
                lbC = a._labC or 0
                lbU = p.get('ubi') or 0
                if inCCO and p['bu'] > 0 and not PO['relief']:
                    lbBU = fwB
                    lbR = fwLeft
                lbBiz = max(0, FWS.prev.bizNet) / FWS.prev.wSum if (FWON and FWS.prev and FWS.prev.wSum > 0) else 0
                if ESON and ESP['rest'] == 'esp':
                    lbBiz = max(0, FWS.prev.bizNet) / ESS.wW if (a._esWk and ESS.wW > 0 and FWS.prev) else 0
                if SPON:
                    lbBiz = (spProfW if a._spWk else 0) + spRestW
                lbRaise = math.pow(max(1, a.wage / a._lwNB) * (1 + lbBiz) * ((1 + a._esX) if ESON else 1), LABOR['eps'] - LABOR['rho'])
                tbQ = self.tb_lab(a, tbY, lbE0, tbPT + tbG + (a._spCutY if SPON else 0)) if tbY else None
                if tbQ:
                    lbRaise *= tbQ[0]
                lbInc = LABOR['rho'] * lbU + LABOR['rhoBU'] * lbBU + LABOR['rhoR'] * lbR + LABOR['rho'] * (1 - LABOR['delta']) * lbC + (LABOR['rho'] * tbQ[1] if tbQ else 0)
                lbDisp = LABOR['delta'] * lbC + (tbQ[2] if tbQ else 0)
                if SPON and a._spOwn > 0:
                    lbInc += LABOR['rho'] * a._spOwn
                    if LA is not None:
                        LA.cash += LABOR['rho'] * a._spOwn
                if emQ:
                    lbInc *= 1 - emQ[0]
                    lbDisp *= 1 - emQ[0]
                annualWageUSD = max(0, lbE0 * lbRaise - lbInc - lbDisp)
                a._lbE0 = lbE0
                if tbQ and LA is not None:
                    LA.cash += LABOR['rho'] * tbQ[1]
                if LA is not None:
                    LA.n += 1
                    if a.inCCO:
                        LA.nP += 1
                    LA.E0 += lbE0
                    LA.E += annualWageUSD
                    LA.raise_ += lbE0 * (lbRaise - 1)
                    LA.cash += LABOR['rho'] * lbU
                    LA.bu += LABOR['rhoBU'] * lbBU
                    LA.buR += LABOR['rhoR'] * lbR
                    LA.rent += LABOR['rho'] * (1 - LABOR['delta']) * lbC
                    LA.disp += lbDisp
                    LA.C += lbC
                    LA.U += lbU + lbBU
                    LA.projH += lbDisp / lbE0 if lbE0 > 0 else 0
                    if annualWageUSD == 0 and lbE0 > 0:
                        LA.zero += 1
            if PJON:
                a._pjHW = 0
                if a._pjBU > 0:
                    pjH = a._pjBU / pjPay
                    pjHw = a.wage * 12 * W2U * incomeShock / PROJ['hrsYr']
                    pjD = pjH * pjHw
                    if PROJ['hours'] == 'displace':
                        raise SystemExit('PROJ.hours displace is not modelled')
                    a._pjHW = pjD
                    PJacc.hrs += pjH
                    PJacc.disp += 0 / pjIdx
            if SNET and SNET.get('abawd'):
                abW = emQ[0] * 52 if emQ else 0
                abUi = min(abW, emQ[1] / (C['EMPL_UI_REPL'] * emWk)) if (emQ and emWk > 0) else 0
                abB = (a._lbE0 or 0) if LABOR else annualWageUSD
                abR = (annualWageUSD / abB if LABOR else 1) if abB > 0 else 0
                a._snAbC = 0 if a._ret else 12 * max(0, (52 if abR < 0.5 else abW) - abUi) / 52
            costUSD = mlc * cf
            a.wealth += annualWageUSD - costUSD
            emUIv = emQ[1] if emQ else 0
            if SG:  # 6.4: income-graded spending
                grA = annualWageUSD + 0 + 0 + emUIv
                if SNET and self.SNS and a._snB:
                    grA += a._snB
                a._grCut = 0
                if HHP:
                    a._grA = grA
                    a._grC = costUSD
                elif costUSD > 0 and grA < costUSD:
                    a._grCut = costUSD - costUSD * math.pow(max(0, grA) / costUSD, SG['eps'])
                    a.wealth += a._grCut
            a.yrSSUSD = 0
            if SCS > 0 and self.SCB == 'wage' and not HHP:
                a.wealth -= SCS * max(0, annualWageUSD - costUSD)
            if HHP:
                a._hhWS = annualWageUSD - costUSD
            if p.get('ubi'):
                raise SystemExit('p.ubi is not modelled')
            if EMPL:
                a.yrUbiUSD = 0 + emUIv
                if emUIv > 0:
                    a.wealth += emUIv
            yrCashSurplus = annualWageUSD - costUSD + 0 + 0
            if emQ and emQ[1] > 0:
                yrCashSurplus += emQ[1]
            if tbY:
                tbNet, tbEnd = self.tb_cash_flow(a, tbY, annualWageUSD, yr)
                a.wealth += tbNet + tbEnd
                yrCashSurplus += tbNet
            a.yrWageUSD = annualWageUSD
            a.yrCostUSD = costUSD
            a.yrBasketUSD = mlc
            a.yrConvUSD = 0
            if FWON:  # business payout and ESP payroll conversion
                a._fwPayY = 0
                if FWS.prev and FWS.prev.wSum > 0:
                    fwPay = FWS.prev.bizNet * (a._fwW or 0) / FWS.prev.wSum
                    if ESON and ESP['rest'] == 'esp':
                        fwPay = FWS.prev.bizNet * (a._fwW or 0) / ESS.wW if (a._esWk and ESS.wW > 0) else 0
                    if SPON:
                        fwPay = a._spPay
                        SPS.y[yr].paid += fwPay
                        SPS.acc.profit += (fwPay - a._spOwn - a._spRest) / spIdx
                        if not a.inCCO:
                            SPS.acc.non += fwPay / spIdx
                        if a._spWk and yr > 0:
                            SPS.acc.wkY1 += 1
                            SPS.acc.profitN += (fwPay - a._spOwn - a._spRest) / spIdx
                    a.wealth += fwPay
                    a.yrConvUSD += fwPay
                    yrCashSurplus += fwPay
                    FWS.next.bizPaid += fwPay
                    a._fwPayY = fwPay
                    if PRICE:
                        PRICE.acc.conv += fwPay
                if ESON:
                    a._esPrY = 0
                    if a._esC > 0:
                        esTx = self.pj_tax(p, a._esR)
                        esG = 0 if PO['conversion'] else a._esC * a._esR * esCipB * incomeShock
                        esPr = 0 if PO['conversion'] else esG * (1 - esTx) - a._esC
                        a.wealth += esPr
                        a.yrConvUSD += esPr
                        yrCashSurplus += esPr
                        a._esPrY = esPr
                        if tbY:
                            TB.cur.ctax += esG * esTx
                        esAc = ESS.acc
                        esAc.conv += a._esC / esIdx
                        esAc.gross += esG / esIdx
                        esAc.tax += esG * esTx / esIdx
                        esAc.prem += esPr / esIdx
                        esAc.rateXbu += a._esR * a._esC / esIdx
                        if PRICE:
                            PRICE.acc.conv += esPr
                a._fwW = annualWageUSD
                FWS.next.wSum += annualWageUSD
            if math.isnan(a.wealth):
                a.wealth = 0
            if p['ccoOn'] and a.inCCO and FWON:  # 6.8: octaves; quality; SZH induction
                if p['cip'] and uCipQuality < p['cipDemo'] * 0.15:
                    a.quality = min(p['maxMult'], a.quality + 0.1)
                capBU = 12 * FW['octaveCapBase'] * math.pow(2, a.octave)
                if FWS.prev and FWS.prev.pwSum > 0 and not PJON:
                    raise SystemExit('the framework allocation without project hiring is not modelled')
                a._fwPW = capBU * max(0, a.quality)
                FWS.next.pwSum += a._fwPW
                if a.octave < p['maxOct']:
                    YusdF = a.wage * W2U
                    cBasicF = (dcA * cfPreCCO) / 12
                    edcF = C['FBS_EDC_RESIDUAL_PTH'] if (p['pth'] and a.inPTH) else C['FBS_EDC_RESIDUAL_BASE']
                    fbsF = max(0, YusdF + buA - cBasicF - edcF * YusdF) / 1
                    lamF = a.lam
                    if p['cip']:
                        lamF *= (1 + p['cipDemo'] * C['FBS_CIP_LAMBDA_BOOST'])
                    if self.FBS50 and self.FBSS is not None and tbY:
                        F = self.FBSS
                        fbK = bool(a._hh is not None and a._hh.kids)
                        F.n += 1
                        if lamF * fbsF >= math.log(2):
                            F.a += 1
                        if fbK:
                            F.nK += 1
                            if lamF * fbsF >= math.log(2):
                                F.aK += 1
                        if yr == 0:
                            F.f.append(math.log(2) / lamF)
                    if uAdvance < 1 - math.exp(-lamF * fbsF) and not PO['octave']:
                        a.octave += 1
                if uSzhInduce < szhPartBoost and not a.inPTF and p['ptf'] and not (HHA and not a._hhHead) and ((not PDON) or pdLive < ptfLiveTotal * pdCap):
                    a.inPTF = uSzhPtfShare < p['ptfShare']
                    if a.inPTF and PDON:
                        pdLive += 1
                elif PDON and PROD['speed'] == 'oneyear' and uSzhInduce < szhPartBoost and not a.inPTF and p['ptf'] and not (HHA and not a._hhHead) and uSzhPtfShare < p['ptfShare']:
                    PDS.blk += 1
            elif p['ccoOn'] and a.inCCO:
                raise SystemExit('the engine conversion model is not modelled')
            if PJON and p['ccoOn'] and a.inCCO:  # 6.5: project conversion
                if PROJ['cap']:
                    raise SystemExit('PROJ.cap is not modelled')
                pjE = (a._pjSaved or 0) + (a._pjBU or 0)
                pjC1 = min(pjE, INF)
                a._pjSaved = pjE - pjC1
                pjGh = a._pjGiftH or 0
                pjC2 = min(pjGh, INF - pjC1)
                a._pjGiftH = pjGh - pjC2
                rvR = a._pjRu
                pjTx = self.pj_tax(p, rvR)
                pjG1 = 0 if PO['conversion'] else pjC1 * rvR * pjCipB * incomeShock
                pjN1 = pjG1 * (1 - pjTx)
                pjTg = self.pj_tax(p, a._pjR)
                pjG2 = 0 if PO['conversion'] else pjC2 * a._pjR * pjCipB * incomeShock
                pjN2 = pjG2 * (1 - pjTg)
                if PROD and FWON:
                    pdH = pjC1 / pjPay
                    pdV = pdH * (pjPay if PROD['match'] == 'face' else a.wage * 12 * W2U * incomeShock / PROJ['hrsYr']) * (1 + (PROD.get('mat') or 0))
                    a._pdM = max(0, pjN1) if PROD['match'] == 'market' else min(max(0, pjN1), pdV)
                if tbY:
                    TB.cur.ctax += pjG1 * pjTx + pjG2 * pjTg
                a.wealth += pjN1 + pjN2
                a.yrConvUSD += pjN1 + pjN2
                yrCashSurplus += pjN1 + pjN2
                totalConversion += pjN1 + pjN2
                totalBU += pjC1 + pjC2
                if LABOR and pjN2:
                    a._labCn = (a._labCn or 0) + pjN2
                a.yrPjGift = pjN1 * pjFg + pjN2
                if PRICE:
                    PRICE.acc.conv += pjN1 + pjN2
                PJacc.conv += pjC1 / pjIdx
                PJacc.giftConv += pjC2 / pjIdx
                PJacc.gross += (pjG1 + pjG2) / pjIdx
                PJacc.net += pjN1 / pjIdx
                PJacc.giftNet += pjN2 / pjIdx
                if math.isnan(a.wealth):
                    a.wealth = 0
            if p['pth'] and a.inPTH and not PO['pthEquity'] and not PO['pthCost']:  # 6.10 and 12.2: PTH
                a.pthTenure += 1
                pthSaving = max(0, dcA * (cfPTF - cfPreCCO) * rsRel)
                equityContrib = pthSaving * C['PTH_EQUITY_CONTRIB_SHARE']
                a.acreEquity += equityContrib
                a.wealth -= equityContrib
                yrCashSurplus -= equityContrib
                ar = 0.030 + uPthAppr * 0.020 + pthApprBonus
                pbS = a._pbS if (PTHB and PBS) else None
                pbV0 = 0
                pbVn = 0
                if pbS:
                    if not pbS.V:
                        pbS.V = C['PTHB_PR'] * hSA * dcA
                        pbS.D = pbS.V - (a.acreEquity - equityContrib)
                    pbV0 = pbS.V
                    pbVn = pbV0 * (1 + PBS.pi) * (1 + C['PTHB_G'])
                    if PTHB['cap'] == 'hub':
                        ar = min(pbVn / pbV0 - 1, PBS.pi + 0.02)
                appr = a.acreEquity * ar
                lqs = self.pth_liquid_share(a.pthTenure)
                if pbS:
                    lqs *= max(0, appr - PBS.pi * a.acreEquity) / appr if appr > 0 else 0
                a.acreEquity += appr * (1 - lqs) if self.PTH_APPR_CONSERVE else appr
                a.wealth += appr * lqs
                yrCashSurplus += appr * lqs
                if tbY:
                    a._tbPthNow = appr * lqs
                if pbS:
                    pbR = hSA * dcA
                    pbI = ((1 + C['PTHB_RREAL']) * (1 + PBS.pi) - 1) * pbS.D
                    pbU = C['PTHB_UPK'] * (1 - C['PTHB_LAND']) * pbV0
                    pbT = C['PTHB_TAX'] * pbV0
                    pbL = appr * lqs
                    pbS.D -= pbR + equityContrib - pbI - pbU - pbT - pbL
                    pbS.CE += (pbVn - pbV0) + pbR - pbI - pbU - pbT - appr
                    pbS.V = pbVn
                    PBS.n += 1
                    if pbR + equityContrib >= pbI - PBS.pi * (pbS.D + pbR + equityContrib - pbI - pbU - pbT - pbL) + pbU + pbT + pbL:
                        PBS.cover += 1
                    PBS.aP += pbV0 * PBS.pi / PBS.P
                    PBS.aR += pbV0 * (1 + PBS.pi) * C['PTHB_G'] / PBS.P
                    PBS.aC += (pbVn - pbV0 - appr) / PBS.P
                if PRICE:
                    PRICE.acc.pthLiq += appr * lqs
            elif a.pthTenure:
                a.pthTenure = 0
            if p['ptf'] and not a.inPTF and p['ptfShare'] > 0 and yr > 0 and not (HHA and not a._hhHead) and ((not PDON) or pdLive < ptfLiveTotal * pdCap):  # 6.10: adoption
                ap = 0.005 + C['PTF_BASS_Q'] * ptfAdoptFrac
                if bleiCheck / 1 < C['BLEI_PRECARIOUS_MAX']:
                    ap += 0.015
                if uPtfAdopt < ap:
                    a.inPTF = True
                    if PDON:
                        pdLive += 1
            elif PDON and PROD['speed'] == 'oneyear' and p['ptf'] and not a.inPTF and p['ptfShare'] > 0 and yr > 0 and not (HHA and not a._hhHead):
                apB = 0.005 + C['PTF_BASS_Q'] * ptfAdoptFrac
                if bleiCheck / 1 < C['BLEI_PRECARIOUS_MAX']:
                    apB += 0.015
                if uPtfAdopt < apB:
                    PDS.blk += 1
            if HHP:
                a._hhCS = yrCashSurplus
            if SCS > 0 and cashBase and not HHP:  # 6.4: the spending rule
                a.wealth -= SCS * max(0, yrCashSurplus)
            if PRICE:  # the price module's accumulators
                pmW = FLOOR - a.wealth if (not HHP and a.wealth < FLOOR) else 0
                pmB = mlc * cfPreCCO
                pmU = min(1, ((pmW + a._grCut) if (SG and not HHP) else pmW) / pmB) if pmB > 0 else 0
                A = PRICE.acc
                A.n += 1
                A.essD += 1 - pmU
                A.unmet += pmW
                A.basketOwn += pmB
                if pmW > 0:
                    A.unmetN += 1
                A.Y += annualWageUSD + a.yrConvUSD + (a.yrSSUSD or 0)
                A.Yw += annualWageUSD + (a.yrSSUSD or 0)
                if p['ptf'] and a.inPTF:
                    A.ptfN += 1
                if HHP:
                    a._hhPmB = pmB
                A.wageBonus += max(0, a.wage - a._wNB) * 12 * W2U * incomeShock
                A.wageBonusNS += max(0, a.wage - a._wNB) * 12 * W2U
            if LABOR:
                a._labC = a._labCn or 0
                a._labCn = 0
                if LA is not None:
                    LA.conv += a.yrConvUSD or 0
                    if a.inCCO:
                        LA.convP += a.yrConvUSD or 0
            if tbY:
                self.tb_account(a, tbY, yr, mlc, cf, cfPreCCO + hcX, costUSD, annualWageUSD, tbG, tbPT)
            if not HHP and a.wealth < FLOOR:
                a.wealth = FLOOR
        # --- C. year close ----------------------------------------------------------------------
        if HHON:
            if HHPOOL:
                self.hh_pool(yr, bool(tbY))
            self.hh_sync('ptf')
        if FWON:
            nx = FWS.next
            bTaxB = p['tax'] * (1 - p['cipDemo'] * 0.18) if p['cip'] else p['tax']
            taxR = min(C['PROG_TAX_MAX'], bTaxB + max(0, (FW['bizRate'] - C['PROG_PIVOT']) * C['PROG_RATE']))
            taxP = min(C['PROG_TAX_MAX'], bTaxB)
            bzB = nx.bizBU * (1 - ESP['lam']) if ESON else nx.bizBU
            nx.bizGross = bzB * (FW['bizCap'] * FW['bizRate'] + (1 - FW['bizCap']))
            nx.bizTax = bzB * (FW['bizCap'] * FW['bizRate'] * taxR + (1 - FW['bizCap']) * taxP)
            nx.bizNet = 0 if PO['conversion'] else nx.bizGross - nx.bizTax - bzB
            if tbY:
                TB.cur.ctax += nx.bizTax
            if ESON:
                ESS.next = O(pool=nx.bizBU * ESP['lam'])
                ESS.acc.accBU += nx.bizBU / esIdx
                ESS.acc.ownBU += bzB / esIdx
            FWS.prev = nx
        if ESON:
            ESS.prev = ESS.next
        if PJON:
            PJS.prev = PJS.next

    # --- the yearly reports (section 9) -------------------------------------------------------
    def lf_of(self, agents, o):
        if o['lines'] == 'nominal':
            return 1
        a0 = agents[0]
        return a0.yrBasketUSD / self.LWA / (a0._hhF or 1)

    def cash_income(self, a):
        c = (a.yrWageUSD or 0) + (a.yrConvUSD or 0) + (a.yrUbiUSD or 0) + (a.yrSSUSD or 0) + (a.yrTbCash or 0)
        return c - a._snB if (self.SNET and self.SNS and a._snB) else c

    def blei_year(self, BG, agents, p, o, last):
        lf = self.lf_of(agents, o)
        L30 = self.CFG['BLEI_PRECARIOUS_MAX']
        L7 = self.CFG['BLEI_CRISIS_MAX']
        BDC = self.CFG['BASE_DAILY_COST']
        v = [0, 0, 0]
        net = Ag()
        for a in agents:
            m = (a._tbM or 0) / BDC
            g2 = 1 if a._tbPart else 2
            v[0] = (self.blei0(a) + m) / lf
            v[1] = self.blei(a, p['bu'], p['ccoOn'], p['pth'], p['szh'], p['szhCoh'], p['ptf']) / lf
            net.wealth = a.wealth
            net._hhD = a._hhD
            net.wage = max(0, (a.yrWageUSD or 0) - (a.yrTax or 0)) / 12 / self.W2U
            v[2] = (self.blei0(net) + m) / lf
            for d in range(3):
                x = v[d]
                j0 = d * 3
                j1 = j0 + g2
                BG['py'][j0] += 1
                BG['py'][j1] += 1
                if x < L30:
                    BG['pov'][j0] += 1
                    BG['pov'][j1] += 1
                if x < L7:
                    BG['cri'][j0] += 1
                    BG['cri'][j1] += 1
                if last:
                    BG['n20'][j0] += 1
                    BG['n20'][j1] += 1
                    if x < L30:
                        BG['pov20'][j0] += 1
                        BG['pov20'][j1] += 1
                    BG['v20'][j0].append(x)
                    BG['v20'][j1].append(x)

    @staticmethod
    def blei_res(BG, R):
        for di, d in enumerate(['N', 'O', 'X']):
            for gi, g in enumerate(['A', 'P', 'N']):
                j = di * 3 + gi
                k = 'b' + d + g
                R[k + 'Py'] = BG['pov'][j] / BG['py'][j] * 100 if BG['py'][j] else 0
                R[k + 'Cr'] = BG['cri'][j] / BG['py'][j] * 100 if BG['py'][j] else 0
                R[k + '20'] = BG['pov20'][j] / BG['n20'][j] * 100 if BG['n20'][j] else 0
                R[k + 'Md'] = median_of(BG['v20'][j])
        return R

    def housing_distress(self, agents):
        k = 0
        for a in agents:
            inc = (a.yrWageUSD or 0) + (a.yrConvUSD or 0) + (a.yrSSUSD or 0)
            w = a.yrWealthStartUSD or 0
            if inc + max(0, w) < (a.yrCostUSD or 0):
                k += 1
        return k / len(agents)

    def housing_distress0(self, agents):
        k = 0
        for a in agents:
            inc = max(a.wage, 0) * 12 * self.W2U
            if inc + max(0, a.wealth) < self.LWA:
                k += 1
        return k / len(agents)

    def extreme_poverty(self, d, d0, p):
        if d is None or not (d0 > 0):
            return None
        C = self.CFG
        Rr = C['EP_Y0_RATE']
        s = C['EP_SMI_SHARE']
        v = C['EP_VOL_SHARE']
        wz = C['EP_WZ_EFFECT'] * max(0, min(1, p['szhCoh'] or 0)) if (p['pth'] and p['szh']) else 0
        econ = Rr * (1 - s - v) * d / d0
        smi = Rr * s * (1 - wz)
        vol = Rr * v
        return (econ + smi + vol) * 100

    def rep_year(self, R, agents, p, o, yr, T, ep):
        C = self.CFG
        n = len(agents)
        lf = self.lf_of(agents, o)
        thr = C['POVERTY_THRESHOLD_ONE']
        L30 = C['BLEI_PRECARIOUS_MAX']
        BDC = C['BASE_DAILY_COST']
        s = {'fpl': 0, 'fplX': 0, 'fplNom': 0, 'f0': 0, 'bO': 0, 'bN': 0, 'bONom': 0, 'bNNom': 0, 'pov': 0, 'povNom': 0}
        PL = C['POVERTY_LINE']
        for a in agents:
            c = self.cash_income(a)
            bo = self.blei(a, p['bu'], p['ccoOn'], p['pth'], p['szh'], p['szhCoh'], p['ptf'])
            bn = self.blei0(a) + (a._tbM or 0) / BDC
            th = thr
            pf = c < th * lf
            h = a._h52
            if not h:
                h = a._h52 = {'f': [], 'c': []}
                R['hist'].append(h)
            h['f'].append(1 if pf else 0)
            h['c'].append(1 if (a._tbGap or 0) > 0 else 0)
            if self.RISK_MEASURE:
                if 'w' not in h:
                    h['w'] = []
                    h['b'] = []
                    h['y'] = []
                h['w'].append(a.wealth / lf)
                h['b'].append(bo / lf)
                h['y'].append(c / lf)
            if pf:
                s['fpl'] += 1
            if c < th:
                s['fplNom'] += 1
            if (a._tbExt or 0) < th * lf:
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
        R['n'] += n
        for k in ('fpl', 'fplX', 'fplNom'):
            R[k] += s[k]
        R['bONom'] += s['bONom']
        R['bNNom'] += s['bNNom']
        wk = [a.yrWageUSD / 12 / lf for a in agents if (not a._ret and a.yrWageUSD > 0)]
        P_ = R['path']
        P_['f0'][yr] = s['f0'] / n * 100
        P_['pov'][yr] = s['pov'] / n * 100
        P_['bO'][yr] = s['bO'] / n * 100
        P_['medW'][yr] = quantile_of([a.wealth / lf for a in agents], 0.5)
        P_['buR'][yr] = self.PRICE.buY / lf if (p['ccoOn'] and p['bu'] > 0 and self.PRICE and self.PRICE.buY) else 0
        P_['wageR'][yr] = quantile_of(wk, 0.5) if wk else 0
        if yr == 0 or yr == 6 or yr == T - 1:
            gc = n / (n - 1) if (o.get('giniNN1') and n > 1) else 1
            q = {'ep': ep}
            for k in s:
                q[k] = s[k] / n * 100
            q['giniD'] = gini_of([a._tbDisp or 0 for a in agents]) * gc
            q['giniX'] = gini_of([a._tbExt or 0 for a in agents]) * gc
            q['giniW'] = gini_of([a.wealth for a in agents]) * gc
            q['giniWN'] = gini_neg([a.wealth for a in agents]) * gc
            if yr == 0:
                R['y0'] = q
            if yr == 6:
                R['y7'] = q
            if yr == T - 1:
                R['end'] = q

    @staticmethod
    def rep_spells(hist, m, out, key):
        N = [0] * 6
        X = [0] * 6
        RN = 0
        RR = 0
        for h in hist:
            x = h[m]
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

    @staticmethod
    def rk_draw(x):
        pk = x[0]
        d = 0
        for t in range(1, len(x)):
            if x[t] > pk:
                pk = x[t]
            elif pk - x[t] > d:
                d = pk - x[t]
        return d

    @staticmethod
    def rk_reentry(hist, m, K):
        N = [0] * len(K)
        X = [0] * len(K)
        for h in hist:
            x = h[m]
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

    def risk_res(self, hist, out):
        mo = self.LWA / 12
        dW = []
        dB = []
        ev = 0
        ay = 0
        Rk = [[0, 0], [0, 0], [0, 0]]
        B3 = [0, 0]
        rs = 0
        rn = 0
        for h in hist:
            if not h.get('w'):
                continue
            y = h['y']
            b = h['b']
            L = len(y)
            ay += L
            dW.append(self.rk_draw(h['w']) / mo)
            dB.append(self.rk_draw(b))
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
                for i, k in enumerate([1, 3, 5]):
                    if t + k < L:
                        Rk[i][0] += 1
                        if got <= k:
                            Rk[i][1] += 1
                if t + 3 < L:
                    B3[0] += 1
                    for vv in range(t + 1, t + 4):
                        if b[vv] >= b[t - 1]:
                            B3[1] += 1
                            break
        pc = lambda x: x[1] / x[0] * 100 if x[0] else 0
        rc = self.rk_reentry(hist, 'c', [1, 3, 5])
        rf = self.rk_reentry(hist, 'f', [5])
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

    def rep_res(self, R, out):
        pc = lambda k: R[k] / R['n'] * 100 if (R and R['n']) else 0
        out['fplPY'] = pc('fpl')
        out['fplXPY'] = pc('fplX')
        out['fplNomPY'] = pc('fplNom')
        out['bOAPyNom'] = pc('bONom')
        out['bNAPyNom'] = pc('bNNom')
        for k in ['fpl', 'fplX', 'fplNom', 'f0', 'bO', 'bN', 'bONom', 'bNNom', 'pov', 'povNom', 'ep', 'giniD', 'giniX', 'giniW', 'giniWN']:
            K = k[0].upper() + k[1:]
            out['y7' + K] = R['y7'][k] if R['y7'] else 0
            out['e' + K] = R['end'][k] if R['end'] else 0
            out['y0' + K] = R['y0'][k] if R['y0'] else 0
        for m in ['f0', 'pov', 'bO', 'medW', 'buR', 'wageR']:
            for t in range(40):
                v = R['path'][m].get(t)
                out['p' + m + '_' + str(t)] = v if isinstance(v, (int, float)) else 0
        if self.RISK_MEASURE:
            self.risk_res(R['hist'], out)
        self.rep_spells(R['hist'], 'f', out, 'sf')
        self.rep_spells(R['hist'], 'c', out, 'sc')
        out['everFpl'] = len([h for h in R['hist'] if any(h['f'])]) / len(R['hist']) * 100 if R['hist'] else 0
        return out

    def hh_rep_year(self, R, agents, p, o, yr, T):
        C = self.CFG
        lf = self.lf_of(agents, o)
        s = dict(per=0, kid=0, cost=0, costK=0, fpl=0, fplK=0, wlth=0, wlthK=0, blei=0, bleiK=0)
        eq = []
        for H in self.HHS.list:
            nA = len(H.a)
            nK = len(H.kids)
            nn = nA + nK
            inc = cost = need = money = disp = w = b = 0
            for a in H.a:
                inc += a._hhInc
                cost += a._hhCost
                need += a._hhMlc
                disp += a._hhDisp
                money += self.cash_income(a)
                w += a.wealth
                b += self.blei(a, p['bu'], p['ccoOn'], p['pth'], p['szh'], p['szhCoh'], p['ptf']) / lf
            fC = inc < cost
            fF = money < C['HH_FPL']['%da%dk' % (nA, min(4, nK))] * lf
            fW = w < need * C['HH_WEALTH_MONTHS'] / 12
            fB = b / nA < C['BLEI_PRECARIOUS_MAX']
            ty = ('sp' if nK else 'sg') if nA == 1 else ('ck' if nK else 'cn')
            t = R['t_' + ty]
            s['per'] += nn
            s['kid'] += nK
            if fC:
                s['cost'] += nn
                s['costK'] += nK
            if fF:
                s['fpl'] += nn
                s['fplK'] += nK
            if fW:
                s['wlth'] += nn
                s['wlthK'] += nK
            if fB:
                s['blei'] += nn
                s['bleiK'] += nK
            t['py'] += nn
            if fC:
                t['cost'] += nn
            if yr == T - 1:
                t['n'] = t.get('n', 0) + nn
                if fW:
                    t['w'] = t.get('w', 0) + nn
            if not H._sp:
                H._sp = {'c': [], 't': ty}
                R['sp'].append(H._sp)
            H._sp['c'].append(fC)
            if yr == T - 1:
                e = disp / math.sqrt(nn) / lf
                for _ in range(nn):
                    eq.append(e)
        R['py'] += s['per']
        R['kpy'] += s['kid']
        R['per'] = s['per']
        R['kid'] = s['kid']
        for k in ('cost', 'fpl', 'wlth', 'blei'):
            R['c'][k] += s[k]
            R['c'][k + 'K'] += s[k + 'K']

        def snap():
            return dict(cost=s['cost'] / s['per'] * 100, costK=s['costK'] / s['kid'] * 100 if s['kid'] else 0, fpl=s['fpl'] / s['per'] * 100, fplK=s['fplK'] / s['kid'] * 100 if s['kid'] else 0,
                        wlth=s['wlth'] / s['per'] * 100, wlthK=s['wlthK'] / s['kid'] * 100 if s['kid'] else 0, blei=s['blei'] / s['per'] * 100, bleiK=s['bleiK'] / s['kid'] * 100 if s['kid'] else 0)
        if yr == 6:
            R['y7'] = snap()
        if yr == T - 1:
            R['end'] = snap()
            R['gini'] = gini_of(eq)
            R['med'] = quantile_of(eq, 0.5)

    def hh_res(self, R, out):
        def pc(k, kid=False):
            d = R['kpy'] if kid else R['py']
            return R['c'][k] / d * 100 if d else 0
        out['hhPer'] = R['per']
        out['hhKid'] = R['kid']
        out['hhCostPY'] = pc('cost')
        out['hhCostKidPY'] = pc('costK', True)
        out['hhFplPY'] = pc('fpl')
        out['hhFplKidPY'] = pc('fplK', True)
        out['hhWlthPY'] = pc('wlth')
        out['hhWlthKidPY'] = pc('wlthK', True)
        out['hhBleiPY'] = pc('blei')
        out['hhBleiKidPY'] = pc('bleiK', True)
        y7 = R['y7'] or {}
        e = R['end'] or {}
        out['hhFpl7'] = y7.get('fpl') or 0
        out['hhFplKid7'] = y7.get('fplK') or 0
        out['hhCost7'] = y7.get('cost') or 0
        out['hhCostKid7'] = y7.get('costK') or 0
        for a_, b_ in (('Fpl', 'fpl'), ('FplKid', 'fplK'), ('Cost', 'cost'), ('CostKid', 'costK'), ('Wlth', 'wlth'), ('WlthKid', 'wlthK'), ('Blei', 'blei'), ('BleiKid', 'bleiK')):
            out['hh' + a_ + 'End'] = e.get(b_) or 0
        out['hhGiniEq'] = R.get('gini') or 0
        out['hhMedEq'] = R.get('med') or 0
        for t in ('sg', 'sp', 'cn', 'ck'):
            q = R['t_' + t]
            out['hhCost_' + t] = q['cost'] / q['py'] * 100 if q['py'] else 0
            out['hhWlth_' + t] = (q.get('w') or 0) / q['n'] * 100 if q.get('n') else 0
            out['hhShare_' + t] = q['py'] / R['py'] * 100 if R['py'] else 0
        for k in ('a25', 'a35', 'a50', 'a67'):
            out['hhCostA' + k[1:]] = 0  # no ages in these runs

        def sp(L):
            o2 = {}
            self.rep_spells(L, 'c', o2, 'q')
            return (o2['qX1'] / o2['qN1'] if o2['qN1'] else 0, o2['qN1'])
        ex, nn = sp(R['sp'])
        out['hhSpEx1'] = ex
        out['hhSpN'] = nn
        for t in ('sg', 'sp', 'cn', 'ck'):
            ex, nn = sp([x for x in R['sp'] if x['t'] == t])
            out['hhSpEx1_' + t] = ex
            out['hhSpN_' + t] = nn
        return out

    def edc_year(self, E, agents, p):
        def add(rent, inc, w):
            q = min(1, rent / inc) if inc > 0 else 1
            E['s'] += q * w
            E['n'] += w
            E['r'] += rent
            E['y'] += inc
        if self.HOUSEHOLDS and self.HHS:
            for H in self.HHS.list:
                r = 0
                y = 0
                for a in H.a:
                    r += (a._edcR or 0) + (a._edcInt or 0)
                    y += a._edcY or 0
                add(r, y, len(H.a) + len(H.kids))
        else:
            for a in agents:
                add((a._edcR or 0) + (a._edcInt or 0), a._edcY or 0, 1)
        for a in agents:
            r = (a._edcR or 0) + (a._edcInt or 0)
            y = a._edcY or 0
            q = min(1, r / y) if y > 0 else 1
            if p['pth'] and a.inPTH:
                E['sP'] += q
                E['nP'] += 1
            else:
                E['sO'] += q
                E['nO'] += 1
            E['px'] += self.agent_edc(a, p['ccoOn'], p['pth'])
            E['pn'] += 1

    # --- a run: the price-only supply path, then the study run (tbRunCore, tbRun) ------------
    def price_run(self, p, seed):
        """The supply path (s3BaseS / priceRun): a no-programme run without the testbed's accounts,
        job loss stream, safety net or labour response, wages not indexed; returns the yearly
        share of essential need met, D."""
        o = dict(self.pk.atLoad['PM_DEFAULTS'])
        CALM0 = O(active=False, incomeMultiplier=1.0)
        self.RNG = mulberry32(seed + 700003)
        agents = [self.instantiate(l, p) for l in self.make_latent(p['nAgents'])]
        if self.HOUSEHOLDS:
            self.hh_init(agents, seed)
        else:
            self.HHS = None
        recPath = self.recession_path(p['years'], seed) if p['shock'] else None
        self.RNG = mulberry32(seed)
        comp = {k: 1 for k in self.BKEYS}
        self.PRICE = O(bIdx=1, comp=comp, piG=0, colaLevel=1, lastFull=1, wIdx=o['wIdx'], noDamp=o['noDamp'], acc=None)
        self.TB = None
        self.LABOR = None
        self.EMS = None
        self.SNS = None
        self.PBS = None
        self.PFS = None
        self.EDCS = None
        self.FBSS = None
        self.THETA_DENS = None
        PG = 1
        D = []
        try:
            for yr in range(p['years']):
                self.PRICE.acc = self.new_pm_acc()
                self.run_year(agents, yr, p, recPath[yr] if recPath else CALM0)
                A = self.PRICE.acc
                d = A.essD / A.n if A.n else 1
                D.append(d)
                U = (1 - o['a']) * A.conv + (A.pthLiq if o['pthUnmatched'] else 0) + (A.unmet if o['floorUnmatched'] else 0) + 0
                PGn = PG * (1 + o['lamG'] * U / A.Y) if A.Y > 0 else PG
                self.PRICE.piG = PGn / PG - 1
                PG = PGn
                for k in self.BKEYS:
                    comp[k] = (1 * (PG if o['pgOnE'] else 1)) if k in self.CFG['ESSENTIALS'] else PG
                self.PRICE.bIdx = self.basket_idx(comp)
        finally:
            self.PRICE = None
        return D

    @staticmethod
    def new_pm_acc():
        return O(n=0, essD=0, unmet=0, basketOwn=0, unmetN=0, Y=0, Yw=0, ptfN=0, conv=0, pthLiq=0, wageBonus=0, wageBonusNS=0)

    def basket_idx(self, comp):
        b = 1
        for k in self.BKEYS:
            b += self.BASKET[k] * (comp[k] - 1)
        return b

    @staticmethod
    def ess_level(D, S, cap, theta):
        s = S * (1 + cap)
        return max(0, 1 + theta * (D - s) / s) if s > 0 else 1

    def tb_run_core(self, p, seed, o, S, tau0, yMax):
        C = self.CFG
        CALM0 = O(active=False, incomeMultiplier=1.0)
        self.RNG = mulberry32(seed + 700003)
        latent = self.make_latent(p['nAgents'])
        agents = [self.instantiate(l, p) for l in latent]
        recPath = self.recession_path(p['years'], seed) if p['shock'] else None
        spec = p.get('tb') or {}
        gR = mulberry32(seed + 900001)
        grp = o.get('grp') or {'part': 0, 'pth': 0}
        wq = sorted(l.wage for l in latent)
        w1 = wq[len(wq) // 3]
        w2 = wq[(2 * len(wq)) // 3]
        for i, a in enumerate(agents):
            l = latent[i]
            a._tbU = gR()
            a._tbEl = bool(spec.get('endow'))
            a._tbPart = l.uCCO < grp['part']
            a._tbPTH = l.uPTH < grp['pth']
            a._tbLow = l.wage < w1
            a._tbTop = l.wage >= w2
        if self.EMPL:
            self.empl_init(agents, seed)
        else:
            self.EMS = None
        if self.SNET:
            self.sn_init(agents, seed)
        else:
            self.SNS = None
        if self.PTHB and p['pth']:
            self.pthb_init(agents, latent, seed)
        else:
            self.PBS = None
        if self.PTFS and p['ptf']:
            self.PFS = O(r=mulberry32(seed + 600047), cut=0, cn=0, leave=0, mem=0, yrs=0, dens=1)
        else:
            self.PFS = None
        if self.HOUSEHOLDS:
            self.hh_init(agents, seed)
        else:
            self.HHS = None
        RHH = None
        if self.HOUSEHOLDS and self.HHS:
            RHH = dict(py=0, kpy=0, c={k: 0 for k in ('cost', 'costK', 'fpl', 'fplK', 'wlth', 'wlthK', 'blei', 'bleiK')}, y7=None, end=None, per=0, kid=0, sp=[])
            for t in ('sg', 'sp', 'cn', 'ck'):
                RHH['t_' + t] = {'py': 0, 'cost': 0, 'wlth': 0}
        self.EDCS = dict(s=0, n=0, r=0, y=0, sP=0, nP=0, sO=0, nO=0, px=0, pn=0) if self.EDC_MEASURE else None
        self.FBSS = O(n=0, a=0, nK=0, aK=0, f=[]) if self.FBS50 else None
        self.RNG = mulberry32(seed)
        comp = {k: 1 for k in self.BKEYS}
        self.PRICE = O(bIdx=1, comp=comp, piG=0, colaLevel=1, lastFull=1, wIdx=o['wIdx'], noDamp=o['noDamp'], acc=None)
        self.TB = O(fin=o['fin'], tau=tau0, X=o['X'], inkindRho=o['inkindRho'], neutralGate=o['neutralGate'], cur=None, tb=o.get('taxBase'), tauMax=o['tauMax'], xIdx=None)
        if o.get('taxBase') or o.get('aK') or o.get('faceM') or o['fin'] not in ('tax', 'source'):
            raise SystemExit('financing readings other than tax and source are not modelled')
        PG = 1
        path = []
        wbPrev = 0
        labAcc = None
        T = p['years']
        L = O(pjg=0, cost=0, cash=0, endow=0, bu=0, conv=0, cutPT=0, cutG=0, cap=0, pth=0, tax=0, need=0, treas=0, f0=0, f1=0, f2=0, n=0, endowTot=0, need0=0, base0=0, pd=0, tgt=0, emp=0, hrs=0, Er=0, bR=0, bP=0,
              bz=0, es=0, n1=0, nP1=0, nN1=0, pyP=0, pyN=0, nWP1=0, esWP=0, convM=0, buIss=0, ctax=0, cutFree=0, bkP=0, bkU=0, bkY=0, ntR=0)
        self.THETA_DENS = None
        epD0 = self.housing_distress0(agents)
        epSum = 0
        BG = dict(py=[0] * 9, pov=[0] * 9, cri=[0] * 9, pov20=[0] * 9, n20=[0] * 9, v20=[[] for _ in range(9)])
        dbt20 = 0
        dbt40 = 0
        R52 = dict(n=0, fpl=0, fplX=0, fplNom=0, bONom=0, bNNom=0, y7=None, end=None, y0=None, hist=[], path={m: {} for m in ('f0', 'pov', 'bO', 'medW', 'buR', 'wageR')}) if o.get('rep52') else None
        if o.get('labor'):
            labAcc = O(n=0, nP=0, E0=0, E=0, raise_=0, cash=0, bu=0, buR=0, rent=0, disp=0, C=0, U=0, projH=0, zero=0, conv=0, convP=0)
            self.LABOR = dict(o['labor'])
            self.LABOR['acc'] = labAcc
        else:
            self.LABOR = None
        theta = o['theta']
        try:
            for yr in range(yMax):
                self.PRICE.acc = self.new_pm_acc()
                self.run_year(agents, yr, p, recPath[yr] if recPath else CALM0)
                self.blei_year(BG, agents, p, o, yr == T - 1)
                epY = None
                if not o.get('noEP'):
                    epY = self.extreme_poverty(self.housing_distress(agents), epD0, p)
                    epSum += epY / 100 if epY is not None else 0
                if R52 is not None:
                    self.rep_year(R52, agents, p, o, yr, T, epY if (not o.get('noEP') and epY is not None) else 0)
                if RHH is not None:
                    self.hh_rep_year(RHH, agents, p, o, yr, T)
                if yr == 19:
                    dbt20 = self.debt_share(agents)
                elif yr == 39:
                    dbt40 = self.debt_share(agents)
                if self.EDCS is not None:
                    self.edc_year(self.EDCS, agents, p)
                A = self.PRICE.acc
                Cc = self.TB.cur or self.tb_new_acc()
                d = A.essD / A.n if A.n else 1
                tauUsed = self.TB.tau
                wbInc = A.wageBonusNS - wbPrev
                wbPrev = A.wageBonusNS
                extra = (A.unmet if o['floorUnmatched'] else 0) + (1 - o['aw']) * (A.wageBonus if o['awLevel'] else wbInc)
                if yr == 0:
                    L.endowTot = Cc.endow
                L.pjg += Cc.pjg
                gRun = bool(self.PROJ and self.PROJ.get('giftFin') == 'run')
                if gRun:
                    raise SystemExit('the gift paid for over the run is not modelled')
                fin = o['fin']
                need = Cc.cash + L.endowTot / T + (0 if fin == 'source' else Cc.bu) + (0 if fin in ('hybrid', 'source') else Cc.conv) + Cc.cap + (1 - o['eP']) * (Cc.cutPT - Cc.cutFree + Cc.cutG) + Cc.pthLiq
                if fin == 'tax':
                    U = extra + 0
                else:
                    cvS = Cc.conv
                    bkP = Cc.bu + cvS - Cc.convM
                    bkU = (1 - o['a']) * bkP
                    U = bkU + extra
                    L.bkP += bkP / Cc.idx
                    L.bkU += bkU / Cc.idx
                    L.bkY += A.Yw / Cc.idx
                if yr == 0:
                    L.need0 = need
                    L.base0 = Cc.base
                if self.MULT and self.MLS:
                    self.MLS.push = max(0, Cc.bu + Cc.conv - Cc.ctax) if fin == 'source' else 0
                ix = Cc.idx
                L.cost += (Cc.cash + Cc.endow + Cc.bu + Cc.conv + Cc.cap + Cc.cutPT - Cc.cutFree + Cc.cutG + Cc.pthLiq) / ix
                L.cutFree += Cc.cutFree / ix
                L.cash += Cc.cash / ix
                L.endow += Cc.endow / ix
                L.bu += Cc.bu / ix
                L.conv += Cc.conv / ix
                L.cutPT += Cc.cutPT / ix
                L.cutG += Cc.cutG / ix
                L.cap += Cc.cap / ix
                L.pth += Cc.pthLiq / ix
                L.pd += Cc.pd / ix
                L.tgt += Cc.tgt / ix
                L.tax += Cc.tax / ix
                L.need += need / ix
                L.treas += (Cc.tax - need) / ix
                L.f0 += Cc.f0
                L.f1 += Cc.f1
                L.f2 += Cc.f2
                L.n += Cc.n
                L.emp += Cc.emp
                L.hrs += Cc.hrs
                L.Er += Cc.E / ix
                L.bR += Cc.bR
                L.bP += Cc.bP
                L.convM += Cc.convM / ix
                L.buIss += Cc.buIss / ix
                L.ctax += Cc.ctax / ix
                L.bz += Cc.bz / ix
                L.es += Cc.es / ix
                L.pyP += Cc.pyP / ix
                L.pyN += Cc.pyN / ix
                L.esWP += Cc.esWP / ix
                L.n1 += Cc.n1
                L.nP1 += Cc.nP1
                L.nN1 += Cc.nN1
                L.nWP1 += Cc.nWP1
                if fin in ('tax', 'hybrid', 'source'):  # 12.5: next year's flat contribution
                    self.TB.tau = min(o['tauMax'], need / Cc.base) if Cc.base > 0 else 0
                PGn = PG * (1 + o['lamG'] * U / A.Y) if A.Y > 0 else PG  # 6.12
                capShare = o['ptfCap'] * (A.ptfN / A.n if A.n else 0)
                PE = {}
                for k in C['ESSENTIALS']:
                    if not p['ptf']:
                        cut = 0
                    elif self.PTF_MODE == 'shipped':
                        cut = (0.12 + p['szhCoh'] * 0.04) if p['szh'] else 0.12
                    else:
                        cut = self.sw['PTF_FOOD_CUT'][self.PTF_MODE] if k == 'food' else 0
                    if not S or o['essMatched']:
                        PE[k] = 1
                        continue
                    sRef = S[yr] if o['supply'] == 'baseline' else S[0] * math.pow(1 + o['gS'], yr)
                    dEff = d if o['supply'] == 'baseline' else sRef + max(0, d - sRef) - max(0, S[yr] - sRef)
                    PE[k] = self.ess_level(dEff, sRef, capShare * cut, theta[k])
                path.append(O(bIdx=self.PRICE.bIdx, PG=PG, U=U, Y=A.Y, tau=tauUsed, colaLevel=self.PRICE.colaLevel, full=Cc.idx))
                self.PRICE.piG = PGn / PG - 1
                PG = PGn
                for k in self.BKEYS:
                    comp[k] = PE[k] * (PG if o['pgOnE'] else 1) if k in C['ESSENTIALS'] else PG
                self.PRICE.bIdx = self.basket_idx(comp)
        finally:
            self.PRICE = None
            TBk = self.TB
            self.TB = None
            if labAcc is not None:
                self.LABOR = None
        if yMax < T:
            return {'tau0': min(o['tauMax'], L.need0 / L.base0) if L.base0 > 0 else 0}
        return self.results(agents, p, o, T, L, path, BG, R52, RHH, labAcc, epSum, dbt20, dbt40)

    def debt_share(self, agents):
        n = 0
        k = 0
        if self.HHS and self.HHS.list:
            for H in self.HHS.list:
                if not H.a:
                    continue
                w = 0
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

    def results(self, agents, p, o, T, L, path, BG, R52, RHH, labAcc, epSum, dbt20, dbt40):
        C = self.CFG
        n = len(agents)
        NY = n * T
        full = agents[0].yrBasketUSD / self.LWA / (agents[0]._hhF or 1)
        lineF = 1 if o['lines'] == 'nominal' else full
        pov = bpov = g0 = 0
        g1 = 0
        g2 = 0
        nbpov = 0
        BDC = C['BASE_DAILY_COST']
        for a in agents:
            if a.wealth < C['POVERTY_LINE'] * lineF:
                pov += 1
            if self.blei(a, p['bu'], p['ccoOn'], p['pth'], p['szh'], p['szhCoh'], p['ptf']) / lineF < C['BLEI_PRECARIOUS_MAX']:
                bpov += 1
            if (self.blei0(a) + (a._tbM or 0) / BDC) / lineF < C['BLEI_PRECARIOUS_MAX']:
                nbpov += 1
            g = a._tbGap or 0
            if g > 0:
                g0 += 1
            g1 += g
            g2 += g * g

        def grp_of(f):
            m = k = f0 = f2 = wp = 0
            for a in agents:
                if f(a):
                    k += 1
                    m += a._tbRes / a._tbYrs
                    f0 += a._tbF0 / a._tbYrs
                    f2 += (a._tbF2 or 0) / a._tbYrs
                    if a.wealth < C['POVERTY_LINE'] * lineF:
                        wp += 1
            return dict(res=m / k, f0=f0 / k * 100, f2=f2 / k * 100, wp=wp / k * 100, k=k) if k else dict(res=0, f0=0, f2=0, wp=0, k=0)
        gP = grp_of(lambda a: a._tbPart)
        gN = grp_of(lambda a: not a._tbPart)
        gH = grp_of(lambda a: a._tbPTH)
        gL = grp_of(lambda a: a._tbLow)
        gT = grp_of(lambda a: a._tbTop)
        sp = spY = ever = chron = 0
        for a in agents:
            sp += a._tbSp or 0
            spY += a._tbF0 or 0
            if a._tbF0 > 0:
                ever += 1
            if (a._tbF0 or 0) >= T / 2:
                chron += 1
        gcF = n / (n - 1) if (o.get('giniNN1') and n > 1) else 1
        giniD = gini_of([a._tbDisp or 0 for a in agents]) * gcF
        giniX = gini_of([a._tbExt or 0 for a in agents]) * gcF
        pT = path[T - 1]
        p10 = path[min(T - 1, 9)]
        realT = (pT.colaLevel if p.get('cola') else 1) / pT.full
        PJS = self.PJS if self.PROJ else None

        def pjQ(k):
            return PJS.acc[k] / PJS.acc.partY if (PJS and PJS.acc.partY > 0) else 0
        pjSv = 0
        if PJS and PJS.acc.partY > 0:
            for a in agents:
                pjSv += (a._pjSaved or 0) + (a._pjGiftH or 0)
            pjSv /= max(1, PJS.acc.partY / T)
        fw = self.CONVERSION_MODEL == 'framework'
        eA = self.ESS.acc if (self.ESP and self.ESS and fw) else None
        spOn = bool(self.SURP and self.SPS and fw)
        sA = self.SPS.acc if spOn else None

        def spQ(k):
            return sA[k] / L.n1 if (spOn and L.n1) else 0
        jnOn = bool(self.JOIN and self.JNS and fw and p['ccoOn'])

        def jnQ(y):
            return self.JNS.y[y].part * 100 if (jnOn and self.JNS.y.get(y)) else 0

        def pdQ(y, k):
            return self.PDS.y[y][k] * 100 if (self.PROD and self.PDS and self.PDS.y.get(y) and fw) else 0
        bI = path[T - 1].bIdx
        mx = 0
        tauS = 0
        for t in range(1, T):
            mx = max(mx, path[t].bIdx / path[t - 1].bIdx - 1)
        for q in path:
            tauS += q.tau
        r = {
            'endoAnn': math.pow(bI, 1 / (T - 1)) - 1, 'endoMax': mx, 'pov': pov / n * 100, 'bleiPov': bpov / n * 100, 'nbleiPov': nbpov / n * 100, 'tgt': L.tgt / L.pd if L.pd > 0 else 0,
            'medWealthReal': median_of([a.wealth for a in agents]) / full,
            'fgt0': g0 / n * 100, 'fgt1': g1 / n * 100, 'fgt2': g2 / n * 100, 'fgt0PY': L.f0 / L.n * 100, 'fgt1PY': L.f1 / L.n * 100, 'fgt2PY': L.f2 / L.n * 100,
            'cost': L.cost / NY, 'cCash': L.cash / NY, 'cEndow': L.endow / NY, 'cBU': L.bu / NY, 'cConv': L.conv / NY, 'cCut': (L.cutPT + L.cutG) / NY, 'cCap': L.cap / NY, 'cPth': L.pth / NY,
            'tax': L.tax / NY, 'need': L.need / NY, 'treas': L.treas / NY, 'tauMean': tauS / T, 'tauLast': path[T - 1].tau,
            'dE': (labAcc.E - labAcc.E0) / labAcc.E0 if (labAcc and labAcc.E0 > 0) else 0, 'E': labAcc.E / max(1, labAcc.n) if labAcc else 0, 'E0': labAcc.E0 / max(1, labAcc.n) if labAcc else 0,
            'zero': labAcc.zero / max(1, labAcc.n) if labAcc else 0,
            'gPartRes': gP['res'], 'gPartF0': gP['f0'], 'gNonRes': gN['res'], 'gNonF0': gN['f0'], 'gPthRes': gH['res'], 'gPthF0': gH['f0'], 'gLowRes': gL['res'], 'gLowF0': gL['f0'], 'gTopRes': gT['res'], 'gTopF0': gT['f0'],
            'gPartW': gP['wp'], 'gNonW': gN['wp'], 'gPthW': gH['wp'], 'gLowW': gL['wp'], 'gTopW': gT['wp'],
            'pyPoor': spY / n, 'everPoor': ever / n * 100, 'spellMean': spY / sp if sp > 0 else 0, 'chronic': chron / n * 100, 'emp': L.emp / L.n * 100, 'hrs': L.hrs / L.n - 1, 'Er': L.Er / NY,
            'giniD': giniD, 'giniX': giniX, 'pLev10': p10.full, 'pLev20': pT.full, 'realT': realT, 'bleiR': L.bR / L.n * 100, 'bleiP': L.bP / L.n * 100,
            'pjNet': pjQ('net'), 'pjGift': pjQ('giftNet'), 'pjBU': pjQ('alloc'), 'pjExp': pjQ('exp'), 'pjHrs': pjQ('hrs'), 'pjDisp': pjQ('disp'), 'pjWork': pjQ('work') * 100,
            'pjRc': PJS.acc.rc / PJS.acc.rcN if (PJS and PJS.acc.rcN) else 0, 'pjSaved': pjSv,
            'bzPay': L.bz / L.n1 if L.n1 else 0, 'esPrem': L.es / L.n1 if L.n1 else 0, 'payPart': L.pyP / L.nP1 if L.nP1 else 0, 'payNon': L.pyN / L.nN1 if L.nN1 else 0, 'esPremW': L.esWP / L.nWP1 if L.nWP1 else 0,
            'esBUW': eA.alloc / eA.wkY1 if (eA and eA.wkY1) else 0, 'esShare': eA.alloc / eA.wage * 100 if (eA and eA.wage > 0) else 0, 'esRate': eA.rateXbu / eA.conv if (eA and eA.conv > 0) else 0,
            'esCapB': eA.capBind / eA.partWkY * 100 if (eA and eA.partWkY) else 0, 'esConv': eA.conv / L.n1 if (eA and L.n1) else 0, 'esRet': eA.ret / L.n1 if (eA and L.n1) else 0,
            'gPartF2': gP['f2'], 'gNonF2': gN['f2'], 'gPartK': gP['k'], 'gNonK': gN['k'],
            'spPool': spQ('pool'), 'spOwn': spQ('own'), 'spPtfS': sA.ptf / sA.pool * 100 if (spOn and sA.pool > 0) else 0, 'spCut': spQ('cut'), 'spCutN': spQ('cutN'), 'spFreed': spQ('freed'), 'spCash': spQ('cash'),
            'spProfit': spQ('profit'), 'spProfW': sA.profitN / sA.wkY1 if (spOn and sA.wkY1) else 0, 'spReinv': spQ('reinv'), 'spRest': spQ('rest'), 'spCap': self.SPS.capPA if spOn else 0,
            'spSw': (99 if self.SPS.sw < 0 else self.SPS.sw) if spOn else 0,
            'spD1': sA.d1 / sA.n1 * 100 if (spOn and sA.n1) else 0, 'spD2': sA.d2 / sA.n2 * 100 if (spOn and sA.n2) else 0, 'spNon': (sA.non + sA.cutN) / sA.pool * 100 if (spOn and sA.pool > 0) else 0,
            'spCarry': sA.carry / n if spOn else 0,
            'pdC5': pdQ(5, 'cap'), 'pdC10': pdQ(10, 'cap'), 'pdC19': pdQ(T - 1, 'cap'), 'pdMem19': pdQ(T - 1, 'mem'), 'pdMatch': L.convM / L.conv * 100 if L.conv > 0 else 0,
            'srcIss': L.buIss / NY, 'srcPay': (L.bu + L.conv) / NY, 'srcTax': L.ctax / NY, 'srcM': L.convM / NY, 'srcCover': L.ctax / L.buIss * 100 if L.buIss > 0 else 0,
            'jnP5': jnQ(5), 'jnP10': jnQ(10), 'jnP19': jnQ(T - 1), 'jnJoin': self.JNS.join / n * 100 if jnOn else 0, 'jnLeave': self.JNS.leave / n * 100 if jnOn else 0,
            'csFree': L.cutFree / NY, 'epPY': epSum / T * 100,
            'agRet': 0, 'agAge0': 0, 'agAge': 0, 'agDeaths': 0, 'agBorn': 0, 'svInt': 0, 'svIntR': 0,
            'bkA': (1 - L.bkU / L.bkP) * 100 if L.bkP > 0 else 0, 'bkPY': L.bkP / L.bkY * 100 if L.bkY > 0 else 0, 'mlNT': L.ntR / NY,
            'hcM': 0, 'rvX': 0, 'rvC': 0, 'taxAvg': L.tax / L.Er * 100 if L.Er > 0 else 0,
            'hhDebt20': dbt20, 'hhDebt40': dbt40,
        }
        cc = [a for a in agents if a.inCCO]
        om = 0
        for a in agents:
            om += a.octave if a.inCCO else 0
        r['octMean'] = om / max(1, len(cc))
        self.blei_res(BG, r)
        if R52 is not None:
            self.rep_res(R52, r)
        if RHH is not None:
            self.hh_res(RHH, r)
        E = self.EDCS
        if E is not None:
            r['edcM'] = E['s'] / E['n'] * 100 if E['n'] else 0
            r['edcMagg'] = E['r'] / E['y'] * 100 if E['y'] else 0
            r['edcMPth'] = E['sP'] / E['nP'] * 100 if E['nP'] else 0
            r['edcMOut'] = E['sO'] / E['nO'] * 100 if E['nO'] else 0
            r['edcProxy'] = E['px'] / E['pn'] * 100 if E['pn'] else 0
        F = self.FBSS
        if F is not None:
            r['fbsAbove'] = F.a / F.n * 100 if F.n else 0
            r['fbsAboveKids'] = F.aK / F.nK * 100 if F.nK else 0
            v = sorted(F.f)
            r['fbs50Med'] = v[len(v) // 2] if v else 0
        if self.EMPL and self.EMS:
            self.empl_res(r)
        if self.PTHB:
            self.pthb_res(r)
        if self.PTFS:
            self.ptfs_res(r)
        if self.SNET and self.SNS:
            self.sn_res(r)
        for t in range(40):
            r['plv_' + str(t)] = path[t].full if t < len(path) else 0
        return r

    def tb_run(self, p, seed, o, S):
        tau0 = self.tb_run_core(p, seed, o, S, 0, 1)['tau0'] if (o['fin'] in ('tax', 'hybrid', 'source') and p.get('tb') is not None) else 0
        return self.tb_run_core(p, seed, o, S, tau0, p['years'])


# ---------------------------------------------------------------------------------------------
# Driver: one run, a batch of seeds, the comparison
# ---------------------------------------------------------------------------------------------
_PK = None


def get_packet(path=None):
    global _PK
    if _PK is None or (path and _PK.path != path):
        _PK = Packet(path or DEFAULT_PACKET)
    return _PK


def supply_path(pk, env, seed):
    """The essentials' supply path for this seed: the price-only no-programme run, in the
    no-programme row's switch context (the study runs that row first and caches the path)."""
    E = pk.envs[env]
    base = E['rows']['base']
    bp = dict(pk.atLoad['BASELINE'])
    envP = E['rows']['release']['p']
    bp['shock'] = bool(envP['shock'])
    bp['automation'] = bool(envP['automation'])
    bp['inflRate'] = envP['inflRate']
    if envP['years'] > bp['years']:
        bp['years'] = envP['years']
    return Engine(pk, base['sw']).price_run(bp, seed)


def run_one(env, row, seed, pk=None, S=None):
    pk = pk or get_packet()
    R = pk.envs[env]['rows'][row]
    if S is None:
        S = supply_path(pk, env, seed)
    return Engine(pk, R['sw']).tb_run(R['p'], seed, R['o'], S)


def _batch_worker(args):
    env, lo, hi, packet = args
    pk = get_packet(packet)
    out = {'base': {}, 'release': {}}
    for sd in range(lo, hi + 1):
        S = supply_path(pk, env, sd)
        for row in ('base', 'release'):
            r = run_one(env, row, sd, pk, S)
            for k, v in r.items():
                out[row].setdefault(k, []).append(v)
    return lo, out


def batch(env, lo, hi, jobs, packet, outdir):
    import multiprocessing as mp
    t0 = time.time()
    chunks = []
    step = max(1, (hi - lo + 1 + jobs * 4 - 1) // (jobs * 4))
    s = lo
    while s <= hi:
        chunks.append((env, s, min(hi, s + step - 1), packet))
        s += step
    res = {}
    with mp.Pool(jobs) as pool:
        for lo_, out in pool.imap_unordered(_batch_worker, chunks):
            res[lo_] = out
            print('  %s seeds %d.. done (%.0f s)' % (env, lo_, time.time() - t0), file=sys.stderr, flush=True)
    rows = []
    for row, label in (('base', 'No programme'), ('release', 'Release row')):
        seeds = {}
        for lo_ in sorted(res):
            for k, v in res[lo_][row].items():
                seeds.setdefault(k, []).extend(v)
        rows.append({'row': row, 'label': label, 'seeds': seeds})
    doc = {'about': 's50 independent Python implementation, phase 1: per-seed outputs, env %s, seeds %d-%d' % (env, lo, hi), 'env': env, 'lo': lo, 'hi': hi,
           'seconds': round(time.time() - t0, 1), 'python': sys.version.split()[0], 'rows': rows}
    os.makedirs(outdir, exist_ok=True)
    fn = os.path.join(outdir, 's50-py-%s-%d-%d.json.gz' % (env, lo, hi))
    with gzip.open(fn, 'wt', compresslevel=9) as f:
        json.dump(doc, f)
    print(fn)
    return fn


# ---------------------------------------------------------------------------------------------
# The comparison with the packet's reference (00-START-HERE.md, "What counts as a match")
# ---------------------------------------------------------------------------------------------
HEADLINE = ['y0F0', 'y0Pov', 'y0BO', 'y0BN', 'y0Fpl', 'y0GiniW', 'y0Ep', 'fgt0PY', 'fgt2PY', 'pov', 'bOAPy', 'bNAPy', 'medWealthReal', 'giniD', 'giniX', 'epPY',
            'cost', 'tauMean', 'endoAnn', 'pLev20', 'hrs', 'jnP19', 'emUrate', 'snAll']
EXACT_REL = 1e-9   # the brief's exact test: relative difference under 1e-9
EXACT_ABS = 1e-9   # ... or, for a value that is a rounding remainder near zero, an absolute difference under 1e-9


def _load_json(path, packet=None):
    if path.endswith('.gz'):
        with gzip.open(path, 'rt') as f:
            return json.load(f)
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return json.loads(packet_read(path, packet))


def _stats(x):
    n = len(x)
    m = math.fsum(x) / n
    v = math.fsum((t - m) ** 2 for t in x) / (n - 1) if n > 1 else 0
    return m, math.sqrt(v)


def compare(env, mine_path, packet, outdir):
    ref = _load_json('reference/s50-%s-1-500.json' % env, packet)
    mine = _load_json(mine_path)
    lo, hi = mine['lo'], mine['hi']
    rrows = {0: ref['rows'][0]['seeds'], 1: ref['rows'][1]['seeds']}
    mrows = {0: mine['rows'][0]['seeds'], 1: mine['rows'][1]['seeds']}
    keys = sorted(rrows[0].keys())
    lines = []
    summ = {}
    for label, get in (('no programme', lambda R, k: R[0][k]), ('release row', lambda R, k: R[1][k]), ('effect', lambda R, k: [b - a for a, b in zip(R[0][k], R[1][k])])):
        n_exact = n_exact_rel = n_stat = n_fail = n_const = 0
        fails = []
        inexact = []
        for k in keys:
            if k not in mrows[0]:
                fails.append((k, 'missing'))
                n_fail += 1
                continue
            r = get(rrows, k)[lo - 1:hi]
            m = get(mrows, k)
            if len(m) != len(r):
                raise SystemExit('seed ranges differ')
            worst = 0.0
            bad_seeds = 0
            bad_rel = 0
            for x, y in zip(r, m):
                dd = abs(y - x)
                rel = dd / abs(x) if x != 0 else (0 if y == 0 else INF)
                if rel >= EXACT_REL:
                    bad_rel += 1
                if rel >= EXACT_REL and dd >= EXACT_ABS:
                    bad_seeds += 1
                worst = max(worst, rel if dd >= EXACT_ABS else 0)
            if bad_rel == 0:
                n_exact_rel += 1
            mr, sr = _stats(r)
            mm, sm = _stats(m)
            nn = len(r)
            se = math.sqrt(sr * sr / nn + sm * sm / nn)
            dmean = abs(mm - mr)
            ok_stat = dmean <= 2 * se or dmean <= max(1e-12 * abs(mr), 1e-15)  # a difference in the last digits of the mean is rounding, not a test result
            if se == 0:
                n_const += 1
            if bad_seeds == 0:
                n_exact += 1
            else:
                inexact.append((k, bad_seeds, worst, mr, mm))
            if ok_stat:
                n_stat += 1
            else:
                n_fail += 1
                fails.append((k, 'ref mean %.6g, ours %.6g, |difference| %.3g > 2 SE %.3g' % (mr, mm, dmean, 2 * se)))
            if label != 'effect' and k in HEADLINE:
                lines.append((label, k, mr, mm, dmean, 2 * se, ok_stat, bad_seeds, worst))
            if label == 'effect' and k in HEADLINE:
                lines.append((label, k, mr, mm, dmean, 2 * se, ok_stat, bad_seeds, worst))
        summ[label] = dict(keys=len(keys), exact=n_exact, exact_rel=n_exact_rel, stat=n_stat, fail=n_fail, fails=fails, inexact=inexact, const=n_const)
    return summ, lines


def compare_report(envs, files, packet, outdir):
    out = []
    out.append('# S50 phase 1: comparison with the engine\'s reference outputs\n')
    out.append('Generated by `python3 -I s50_release.py --compare` from `results/` and the packet\'s `reference/` (seeds 1-500, both runs, %s).\n' % ', '.join(envs))
    out.append('Exact test, per seed and key: relative difference under 1e-9, or (for a rounding remainder near zero) absolute difference under 1e-9. '
               'Statistical test, per key: |mean ours - mean reference| <= 2 x sqrt(sd_ours^2/500 + sd_ref^2/500); the same on the per-seed effect (release row minus no programme). '
               'A difference under 1e-12 of the mean counts as equal: a key that is nearly constant across seeds has a standard error near zero, and its two means then differ only by rounding in the last binary digit.\n')
    allrows = []
    for env, fn in zip(envs, files):
        summ, lines = compare(env, fn, packet, outdir)
        out.append('\n## %s\n' % {'ref': 'Reference', 'adv': 'Adverse', 'st': 'Stress'}[env])
        out.append('| Run | Keys | Exact on every seed | Exact (relative test only) | Pass the 2-SE test | Fail the 2-SE test |')
        out.append('|---|---|---|---|---|---|')
        for lab in ('no programme', 'release row', 'effect'):
            s = summ[lab]
            out.append('| %s | %d | %d | %d | %d | %d |' % (lab, s['keys'], s['exact'], s['exact_rel'], s['stat'], s['fail']))
        for lab in ('no programme', 'release row', 'effect'):
            s = summ[lab]
            if s['inexact']:
                out.append('\nNot exact on every seed (%s): ' % lab + '; '.join('`%s` (%d seeds, worst relative %.2g)' % (k, b, w) for k, b, w, mr, mm in s['inexact']))
            if s['fails']:
                out.append('\nFailing the 2-SE test (%s): ' % lab + '; '.join('`%s`: %s' % f for f in s['fails']))
        out.append('\n| Run | Key | Reference mean | Our mean | Difference | 2 SE | Match (2 SE) | Seeds not exact |')
        out.append('|---|---|---|---|---|---|---|---|')
        for (lab, k, mr, mm, dmean, se2, ok, bad, worst) in lines:
            out.append('| %s | `%s` | %.6g | %.6g | %.3g | %.3g | %s | %d |' % (lab, k, mr, mm, dmean, se2, 'yes' if ok else '**no**', bad))
            allrows.append((env, lab, k, mr, mm, dmean, se2, ok, bad, worst))
    fn = os.path.join(outdir, 'COMPARISON.md')
    with open(fn, 'w') as f:
        f.write('\n'.join(out) + '\n')
    print(fn)
    return fn


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--packet', default=DEFAULT_PACKET, help='the S50 packet (zip or unzipped folder)')
    ap.add_argument('--env', default='ref', choices=['ref', 'adv', 'st'])
    ap.add_argument('--row', default='release', choices=['release', 'base'])
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--batch', type=int, nargs=2, metavar=('LO', 'HI'))
    ap.add_argument('--jobs', type=int, default=os.cpu_count() or 1)
    ap.add_argument('--out', default=os.path.join(HERE, 'results'))
    ap.add_argument('--compare', nargs='*', metavar='FILE', help='compare per-seed results (default: results/s50-py-ENV-1-500.json.gz for ref, adv, st)')
    a = ap.parse_args()
    if a.compare is not None:
        files = a.compare or [os.path.join(a.out, 's50-py-%s-1-500.json.gz' % e) for e in ('ref', 'adv', 'st')]
        envs = [os.path.basename(f).split('-')[2] for f in files]
        compare_report(envs, files, a.packet, a.out)
        return
    pk = get_packet(a.packet)
    if a.batch:
        batch(a.env, a.batch[0], a.batch[1], a.jobs, a.packet, a.out)
        return
    r = run_one(a.env, a.row, a.seed, pk)
    json.dump(r, sys.stdout, indent=0, sort_keys=True)
    print()


if __name__ == '__main__':
    main()
