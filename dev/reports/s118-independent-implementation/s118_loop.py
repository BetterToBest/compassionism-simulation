#!/usr/bin/env python3
"""A second, independent implementation of the Compassionism Simulation's yearly loop.

Written in Python from the s118 packet (dev/packets/s118-second-implementation.zip):
the written description (ODD.md, MODEL_SPEC.md) first, then the packet's excerpt of
the engine (core-loop.js) only where the description does not settle a question.
Every such question is listed in GAPS.md beside this file, with the line of
core-loop.js that settled it. No constant or rule here was changed to make a number
agree with the engine.

What it runs: the engine's own validation path, runScenario(preset, seed), for the
five presets in the packet's reference file (500 adults, 20 years). In that path
every mechanism listed in the packet's later-modules.md is switched off, so the
yearly loop is the engine's "engine" branch: a monthly BU allowance credited once a
year and converted at the adult's own rate, a cost-of-living relief that scales with
the BU, PTF and PTH price cuts, PTH equity, octave advancement, PTF adoption,
recessions and automation.

Usage:
  python3 -I s118_loop.py --preset baseline --seed 42
  python3 -I s118_loop.py --preset full_integration --seed 42 --json
  python3 -I s118_loop.py --compare reference-outputs.json [--seeds 1-30,42]
  python3 -I s118_loop.py --compare500 python-reference-500.json [--workers 8]

The math and code of this simulation were engineered by Claude, an AI model made by
Anthropic, from the concepts in Duke Johnson's book Better To Best and his related
vision for eradicating extreme poverty while enriching cultures and supporting human
flourishing. The model has not yet been reviewed by an independent economist; the
full code is open for anyone to check, and expert collaborators are welcome.
"""
import argparse
import json
import math
from decimal import Decimal, ROUND_HALF_UP

# ---------------------------------------------------------------------------
# Constants. Each is from ODD.md / MODEL_SPEC.md where they give it; the rest are
# from core-loop.js (CFG, lines 67-283), as GAPS.md records.
# ---------------------------------------------------------------------------
POVERTY_LINE = 25000.0
BLEI_CRISIS_MAX, BLEI_PRECARIOUS_MAX = 7, 30
BLEI_THRESHOLD_MAX, BLEI_STABLE_MAX, BLEI_SECURE_MAX = 120, 365, 730
BASE_DAILY_COST, CCO_PTH_DAILY_COST = 68.33, 31.67
WEALTH_INIT_MU, WEALTH_INIT_SIGMA = 10.5, 1.2
SZH_ALL_RESIDENTS = 0.06
SZH_THETA_THRESHOLD, SZH_THETA_MAX_COH, SZH_THETA_MAX = 0.55, 0.90, 0.25
EDC_PTH_CAP = 0.10
PROG_PIVOT, PROG_RATE, PROG_TAX_MAX = 3.0, 0.040, 0.75
WAGE_MEDIAN_SIU = 35
WEALTH_FLOOR = -10000.0
WAGE_BASE_GROWTH, WAGE_BLEI_BONUS, WAGE_OCTAVE_BONUS = 0.010, 0.008, 0.003
AI_YEAR_1, AI_YEAR_2, AI_RATE_1, AI_RATE_2, AI_CAP = 5, 15, 0.012, 0.022, 0.10
PHI_RATIO, PHI_QUALITY_THRESH = 1.618, 0.70
FBS_LAMBDA_LO, FBS_LAMBDA_HI = 0.0001654, 0.0013233
FBS_EDC_RESIDUAL_BASE, FBS_EDC_RESIDUAL_PTH = 0.12, 0.025
FBS_CIP_LAMBDA_BOOST = 0.20
PTH_EQUITY_CONTRIB_SHARE = 0.25
PTH_LIQUID_SHARE_YEAR1, PTH_LIQUID_SHARE_YEAR5PLUS, PTH_LIQUID_SHARE_MATURE_YR = 0.15, 0.85, 5
PTF_BASS_Q = 0.05
WAGE_TO_USD = 100.52
LIVING_WAGE_ANNUAL = 49370.0
CCO_RELIEF_AT_REF, CCO_RELIEF_REF_BU, CCO_RELIEF_CAP = 0.20, 1200.0, 0.50
AUTO_HIGH_SHARE, AUTO_HIGH_A, AUTO_LOW_B = 0.63, 6, 6
BU_ALLOCATIONS_PER_YEAR = 1   # the page's value (core-loop.js line 1431); see GAPS.md

PRESETS = {
    'full_integration': dict(bu=1200, maxOct=6, expiry=1, tax=0.12, maxMult=9, nAgents=500, partRate=0.78,
                             years=20, ptfShare=0.18, pthUptake=0.2, szhCoh=0.72, cipDemo=0.65, phi=True,
                             ptf=True, pth=True, szh=True, cip=True, shock=False, automation=False,
                             inflRate=0, ccoOn=True),
    'cco_only': dict(bu=1200, maxOct=6, expiry=1, tax=0.12, maxMult=9, nAgents=500, partRate=0.78, years=20,
                     ptfShare=0, pthUptake=0, szhCoh=0, cipDemo=0, phi=True, ptf=False, pth=False, szh=False,
                     cip=False, shock=False, automation=False, inflRate=0, ccoOn=True),
    'baseline_3pct': dict(bu=0, maxOct=1, expiry=1, tax=0, maxMult=1, nAgents=500, partRate=0, years=20,
                          ptfShare=0, pthUptake=0, szhCoh=0, cipDemo=0, phi=False, ptf=False, pth=False,
                          szh=False, cip=False, shock=False, automation=False, inflRate=0.03, ccoOn=False),
    'adverse': dict(bu=1200, maxOct=6, expiry=1, tax=0.12, maxMult=9, nAgents=500, partRate=0.78, years=20,
                    ptfShare=0.18, pthUptake=0.2, szhCoh=0.72, cipDemo=0.65, phi=True, ptf=True, pth=True,
                    szh=True, cip=True, shock=True, automation=True, inflRate=0.02, ccoOn=True),
    'stress': dict(bu=900, maxOct=4, expiry=1, tax=0.18, maxMult=6, nAgents=500, partRate=0.4, years=20,
                   ptfShare=0.08, pthUptake=0.1, szhCoh=0.35, cipDemo=0.3, phi=True, ptf=True, pth=True,
                   szh=True, cip=True, shock=True, automation=True, inflRate=0.02, ccoOn=True),
}
ALIASES = {'baseline': 'baseline_3pct', 'full': 'full_integration', 'cco': 'cco_only'}
ORDER = ['baseline_3pct', 'cco_only', 'full_integration', 'adverse', 'stress']

# ---------------------------------------------------------------------------
# Random numbers: mulberry32 (named in MODEL_SPEC.md section 8; its code is
# core-loop.js line 309), with JavaScript's 32-bit integer arithmetic.
# ---------------------------------------------------------------------------
_M32 = 0xFFFFFFFF


def mulberry32(seed):
    state = [seed & _M32]

    def rng():
        s = (state[0] + 0x6D2B79F5) & _M32
        state[0] = s
        t = ((s ^ (s >> 15)) * (1 | s)) & _M32
        t = ((t + (((t ^ (t >> 7)) * (61 | t)) & _M32)) & _M32) ^ t
        return ((t ^ (t >> 14)) & _M32) / 4294967296.0
    return rng


class Draws:
    """The current random stream, with the samplers the engine draws through."""

    def __init__(self, rng):
        self.rng = rng

    def standard_normal(self):  # core-loop.js line 548
        u = max(1e-14, 1 - self.rng())
        v = self.rng()
        return math.sqrt(-2 * math.log(u)) * math.cos(2 * math.pi * v)

    def lognormal(self, mu, sigma):  # not in the packet; GAPS.md
        return math.exp(mu + sigma * self.standard_normal())

    def gamma(self, k):  # not in the packet: Marsaglia and Tsang (2000); GAPS.md
        if k < 1:
            return self.gamma(1 + k) * self.rng() ** (1 / k)
        d = k - 1 / 3
        c = 1 / math.sqrt(9 * d)
        while True:
            while True:
                x = self.standard_normal()
                v = 1 + c * x
                if v > 0:
                    break
            v = v * v * v
            u = self.rng()
            if u < 1 - 0.0331 * x * x * x * x:
                return d * v
            if math.log(u) < 0.5 * x * x + d * (1 - v + math.log(v)):
                return d * v

    def beta(self, a, b):  # not in the packet; GAPS.md
        x = self.gamma(a)
        y = self.gamma(b)
        return x / (x + y)

    def automation_risk(self):  # core-loop.js lines 571-578; MODEL_SPEC 3 ("exact inverse CDF")
        c = self.rng()
        v = self.rng()
        if c < AUTO_HIGH_SHARE:
            return v ** (1 / AUTO_HIGH_A)
        return 1 - (1 - v) ** (1 / AUTO_LOW_B)


# ---------------------------------------------------------------------------
# Construction (MODEL_SPEC 4.1; core-loop.js lines 581-621)
# ---------------------------------------------------------------------------
def make_latent(dr):
    u_cco, u_ptf, u_pth = dr.rng(), dr.rng(), dr.rng()
    wealth = dr.lognormal(WEALTH_INIT_MU, WEALTH_INIT_SIGMA)
    wage = dr.lognormal(3.5, 0.5)
    octave_shape = dr.beta(2, 5)
    quality_z = dr.standard_normal()
    risk = dr.automation_risk()
    lam = FBS_LAMBDA_LO + dr.rng() * (FBS_LAMBDA_HI - FBS_LAMBDA_LO)
    return dict(uCCO=u_cco, uPTF=u_ptf, uPTH=u_pth, wealth=wealth, wage=wage, octaveShape=octave_shape,
                qualityZ=quality_z, automationRisk=risk, lam=lam)


class Adult:
    __slots__ = ('wealth', 'wage', 'octave', 'quality', 'automationRisk', 'lam', 'uCCO', 'inCCO', 'inPTF',
                 'inPTH', 'buBalance', 'acreEquity', 'pthTenure')


def instantiate(lat, p):
    qn = (1 - p['cipDemo'] * 0.5) if p['cip'] else 1.0
    max_oct = p['maxOct'] or 1
    max_mult = p['maxMult'] or 1
    a = Adult()
    a.wealth = lat['wealth']
    a.wage = lat['wage']
    a.octave = math.floor(lat['octaveShape'] * max_oct)
    a.quality = min(max_mult, max(0.0, math.exp(math.log(max_mult * 0.5) + 0.4 * lat['qualityZ']) * qn))
    a.automationRisk = lat['automationRisk']
    a.lam = lat['lam']
    a.uCCO = lat['uCCO']
    a.inCCO = bool(p['ccoOn'] and lat['uCCO'] < p['partRate'])
    a.inPTF = bool(p['ptf'] and lat['uPTF'] < p['ptfShare'])
    a.inPTH = bool(p['pth'] and lat['uPTH'] < p['pthUptake'])
    a.buBalance = 0.0
    a.acreEquity = 5000.0 if a.inPTH else 0.0
    a.pthTenure = 0
    return a


# ---------------------------------------------------------------------------
# Recessions (MODEL_SPEC 4.3; core-loop.js lines 496-520)
# ---------------------------------------------------------------------------
def recession_path(years, seed):
    dr = Draws(mulberry32(seed + 700000))
    active, mult, left = False, 1.0, 0
    path = []
    for y in range(years):
        if y > 0:
            if active:
                left -= 1
                if left <= 0:
                    active, mult = False, 1.0
            elif dr.rng() < 0.10:
                active = True
                left = 1 + math.floor(dr.rng() * 3)
                mult = 0.70 + dr.beta(5, 2) * 0.25
        path.append((active, mult))
    return path


# ---------------------------------------------------------------------------
# BLEI and EDC (MODEL_SPEC 6.2; core-loop.js lines 376-467)
# ---------------------------------------------------------------------------
def szh_theta(coh):
    if coh < SZH_THETA_THRESHOLD:
        return 0.0
    return min(SZH_THETA_MAX, (coh - SZH_THETA_THRESHOLD) / (SZH_THETA_MAX_COH - SZH_THETA_THRESHOLD) * SZH_THETA_MAX)


def pth_liquid_share(tenure):
    t = max(1, min(PTH_LIQUID_SHARE_MATURE_YR, tenure))
    span = PTH_LIQUID_SHARE_MATURE_YR - 1
    return PTH_LIQUID_SHARE_YEAR1 + (t - 1) / span * (PTH_LIQUID_SHARE_YEAR5PLUS - PTH_LIQUID_SHARE_YEAR1)


def agent_blei(a, bu, cco_on, pth_on, szh_on, szh_coh, ptf_on):
    liquid = max(0.0, a.wealth * 0.20)
    gamma_v = 0.20 if (cco_on and a.inCCO) else 0.12
    m_inc = max(a.wage, 0.1) * WAGE_TO_USD
    bu_food = bu * (990 / 1200) if (cco_on and a.inCCO and bu > 0) else 0.0
    szh_d = szh_coh * SZH_ALL_RESIDENTS if szh_on else 0.0
    if szh_on and ptf_on and a.inPTF:
        szh_d += szh_theta(szh_coh) * 0.20
    base = CCO_PTH_DAILY_COST if (cco_on and a.inCCO and pth_on and a.inPTH) else BASE_DAILY_COST
    dc = max(base * (1 - szh_d), 0.1)
    r = (liquid + gamma_v * m_inc + bu_food) / dc
    if math.isnan(r) or math.isinf(r):
        return 0.0
    return max(0.0, r)


def agent_edc(a, cco_on, pth_on):
    m_inc = max(a.wage, 1)
    w = WAGE_MEDIAN_SIU
    if cco_on and a.inCCO and pth_on and a.inPTH:
        return min(EDC_PTH_CAP, EDC_PTH_CAP * w / m_inc)
    if not cco_on or not a.inCCO:
        return min(0.75, min(0.50, 0.50 * w / m_inc) + 0.08)
    return min(0.42, min(0.35, 0.35 * w / m_inc) + 0.03)


def tier(days):
    if days < BLEI_CRISIS_MAX:
        return 0
    if days < BLEI_PRECARIOUS_MAX:
        return 1
    if days < BLEI_THRESHOLD_MAX:
        return 2
    if days < BLEI_STABLE_MAX:
        return 3
    if days < BLEI_SECURE_MAX:
        return 4
    return 5


def median_sorted(xs):
    n = len(xs)
    return (xs[n // 2 - 1] + xs[n // 2]) / 2 if n % 2 == 0 else xs[n // 2]


def blei_metrics(agents, bu, cco_on, pth_on, szh_on, szh_coh, ptf_on):
    sc = sorted(agent_blei(a, bu, cco_on, pth_on, szh_on, szh_coh, ptf_on) for a in agents)
    n = len(sc)
    tc = [0] * 6
    for d in sc:
        tc[tier(d)] += 1
    edc = sum(agent_edc(a, cco_on, pth_on) for a in agents) / n
    return dict(med=median_sorted(sc), pctF=tc[5] / n * 100, avgEDC=edc, tc=tc, n=n)


# ---------------------------------------------------------------------------
# Wealth measures. calcMetrics is not in the packet (GAPS.md); these follow
# MODEL_SPEC section 9 where it defines them: the Gini of wealth with debts as
# zero, times n/(n - 1) (giniPlain: without that factor). The wealth line and the
# median are read in nominal dollars: the validation path has no price module,
# and the engine's median sits exactly at the nominal floor in the 3% baseline.
# ---------------------------------------------------------------------------
def gini_nonneg(xs):
    v = sorted(max(0.0, x) for x in xs)
    n = len(v)
    s = sum(v)
    if s <= 0:
        return 0.0
    cum = 0.0
    for i, x in enumerate(v):
        cum += (2 * (i + 1) - n - 1) * x
    return cum / (n * s)


def wealth_metrics(agents):
    w = sorted(a.wealth for a in agents)
    n = len(w)
    pov = sum(1 for x in w if x < POVERTY_LINE) / n
    g = gini_nonneg(w)
    return dict(pov=pov, gini=g * n / (n - 1), giniPlain=g, med=median_sorted(w), p10=w[int(n * 0.10)],
                p90=w[int(n * 0.90)])


# ---------------------------------------------------------------------------
# One simulated year (MODEL_SPEC 5; the engine branch of core-loop.js runYear,
# lines 990-1525, with every later module off)
# ---------------------------------------------------------------------------
def run_year(agents, yr, p, rec, dr):
    active, mult = rec
    n = len(agents)
    pth_appr_bonus = p['szhCoh'] * 0.01 if p['szh'] else 0.0
    szh_theta_val = szh_theta(p['szhCoh']) if p['szh'] else 0.0
    ptf_conv_bonus = 1.30 + (szh_theta_val if (p['szh'] and p['ptf']) else 0.0)
    szh_part_boost = szh_theta_val * 0.16 if (p['szh'] and p['ccoOn']) else 0.0
    ptf_adopt_frac = 0.0
    if p['ptf'] and p['ptfShare'] > 0:
        ptf_adopt_frac = sum(1 for a in agents if a.inPTF) / max(1, n)
    pth_member_frac = 0.0
    if p['pth']:
        pth_member_frac = sum(1 for a in agents if a.inPTH) / max(1, n)
    infl = p['inflRate'] or 0
    if p['ptf'] and infl > 0:
        infl *= (1 - ptf_adopt_frac * 0.5)
    if p['pth'] and infl > 0:
        infl *= (1 - pth_member_frac * 0.10)
    price = (1 + infl) ** yr
    dollar_cost = BASE_DAILY_COST * 365 * price
    pop_shock = mult if active else 1.0
    ai_disp = 0.0
    if p['automation']:
        if yr >= AI_YEAR_2:
            ai_disp = AI_RATE_1 * (AI_YEAR_2 - AI_YEAR_1) + AI_RATE_2 * (yr - AI_YEAR_2 + 1)
        elif yr >= AI_YEAR_1:
            ai_disp = AI_RATE_1 * (yr - AI_YEAR_1 + 1)
        ai_disp = min(AI_CAP, ai_disp)
    bu_eff = p['bu']
    relief_f = 1 - min(CCO_RELIEF_CAP, CCO_RELIEF_AT_REF * bu_eff / (CCO_RELIEF_REF_BU * price))
    basket = LIVING_WAGE_ANNUAL * price
    ptf_cut = (0.12 + p['szhCoh'] * 0.04) if p['szh'] else 0.12
    decay = max(0, 1 - 1 / max(1, p['expiry'] or 1))
    for a in agents:
        if math.isnan(a.wealth):
            a.wealth = 0.0
        if math.isnan(a.wage) or a.wage <= 0:
            a.wage = 1.0
        agent_var = 0.90 + dr.rng() * 0.20
        income_shock = pop_shock * agent_var
        u_spend = 0.60 + dr.rng() * 0.30
        u_cip_quality = dr.rng()
        u_advance = dr.rng()
        u_szh_induce = dr.rng()
        u_szh_ptf_share = dr.rng()
        u_pth_appr = dr.rng()
        u_ptf_adopt = dr.rng()
        # wages (6.1)
        blei_check = agent_blei(a, bu_eff, p['ccoOn'], p['pth'], p['szh'], p['szhCoh'], p['ptf'])
        wg = WAGE_BASE_GROWTH
        if blei_check > BLEI_PRECARIOUS_MAX:
            dr_factor = 1 / (1 + 0.5 * max(0, a.wage / WAGE_MEDIAN_SIU - 1))
            wg += WAGE_BLEI_BONUS * max(0.1, dr_factor)
        wg += a.octave * WAGE_OCTAVE_BONUS
        if p['cip']:
            wg += p['cipDemo'] * 0.005
        wg -= ai_disp * a.automationRisk
        a.wage = max(a.wage * 0.80, a.wage * (1 + wg))
        # cost factor: PTF, PTH, the CCO relief (6.3)
        cf = 1.0
        if p['ptf'] and a.inPTF:
            cf *= (1 - ptf_cut)
        if p['pth'] and a.inPTH:
            cf *= 0.65
        if p['ccoOn'] and a.inCCO and p['bu'] > 0:
            cf *= relief_f
        wage_usd = a.wage * 12 * WAGE_TO_USD * income_shock
        cost_usd = basket * cf
        a.wealth += wage_usd - cost_usd
        if math.isnan(a.wealth):
            a.wealth = 0.0
        if p['ccoOn'] and a.inCCO:
            # BU allowance, spending and conversion (6.4, 6.6)
            a.buBalance = min(a.buBalance * decay + bu_eff * BU_ALLOCATIONS_PER_YEAR,
                              bu_eff * 3 * BU_ALLOCATIONS_PER_YEAR)
            spend = a.buBalance * u_spend
            a.buBalance -= spend
            if p['cip'] and u_cip_quality < p['cipDemo'] * 0.15:
                a.quality = min(p['maxMult'], a.quality + 0.1)
            oct_ceiling = 1 + (a.octave / max(1, p['maxOct'])) * (max(1, p['maxMult']) - 1)
            q_factor = min(1, a.quality / max(1, p['maxMult']))
            base_rate = 1 + q_factor * (oct_ceiling - 1)
            phi = PHI_RATIO if (p['phi'] and a.quality > p['maxMult'] * PHI_QUALITY_THRESH) else 1.0
            ptf_b = ptf_conv_bonus if (p['ptf'] and a.inPTF) else 1.0
            cip_b = (1 + p['cipDemo'] * 0.12) if p['cip'] else 1.0
            rate = min(base_rate * phi * ptf_b, p['maxMult'] * (PHI_RATIO if p['phi'] else 1.0))
            b_tax = p['tax'] * (1 - p['cipDemo'] * 0.18) if p['cip'] else p['tax']
            prog_tax = min(PROG_TAX_MAX, b_tax + max(0, (rate - PROG_PIVOT) * PROG_RATE))
            a.wealth += spend * rate * (1 - prog_tax) * cip_b * income_shock
            if math.isnan(a.wealth):
                a.wealth = 0.0
            # octave advancement (6.8)
            if a.octave < p['maxOct']:
                y_usd = a.wage * WAGE_TO_USD
                c_basic = dollar_cost * cf / 12
                edc_res = FBS_EDC_RESIDUAL_PTH if (p['pth'] and a.inPTH) else FBS_EDC_RESIDUAL_BASE
                fbs = max(0, y_usd + bu_eff - c_basic - edc_res * y_usd)
                lam = a.lam * (1 + p['cipDemo'] * FBS_CIP_LAMBDA_BOOST) if p['cip'] else a.lam
                if u_advance < 1 - math.exp(-lam * fbs):
                    a.octave += 1
            # SZH induction into PTF (6.10)
            if u_szh_induce < szh_part_boost and not a.inPTF and p['ptf']:
                a.inPTF = u_szh_ptf_share < p['ptfShare']
        # PTH equity and appreciation (6.10)
        if p['pth'] and a.inPTH:
            a.pthTenure += 1
            pth_saving = max(0.0, dollar_cost * (cf / 0.65) * (1 - 0.65))
            contrib = pth_saving * PTH_EQUITY_CONTRIB_SHARE
            a.acreEquity += contrib
            a.wealth -= contrib
            ar = 0.030 + u_pth_appr * 0.020 + pth_appr_bonus
            appr = a.acreEquity * ar
            lqs = pth_liquid_share(a.pthTenure)
            a.acreEquity += appr
            a.wealth += appr * lqs
        elif a.pthTenure:
            a.pthTenure = 0
        # PTF adoption, Bass diffusion (6.10)
        if p['ptf'] and not a.inPTF and p['ptfShare'] > 0 and yr > 0:
            ap = 0.005 + PTF_BASS_Q * ptf_adopt_frac
            if blei_check < BLEI_PRECARIOUS_MAX:
                ap += 0.015
            if u_ptf_adopt < ap:
                a.inPTF = True
        # wealth floor
        if a.wealth < WEALTH_FLOOR:
            a.wealth = WEALTH_FLOOR


# ---------------------------------------------------------------------------
# One run (core-loop.js runScenario, lines 4-63)
# ---------------------------------------------------------------------------
def run_scenario(p, seed):
    dr = Draws(mulberry32(seed + 700003))
    latent = [make_latent(dr) for _ in range(p['nAgents'])]
    agents = [instantiate(lat, p) for lat in latent]
    m0 = wealth_metrics(agents)
    bn0 = blei_metrics(agents, 0, False, False, False, 0, False)
    by0 = blei_metrics(agents, p['bu'], p['ccoOn'], p['pth'], p['szh'], p['szhCoh'], p['ptf'])
    year_zero = dict(pov=round(m0['pov'] * 100, 1),
                     bleiPovNeutral=round((bn0['tc'][0] + bn0['tc'][1]) / bn0['n'] * 100, 1),
                     bleiPovScenario=round((by0['tc'][0] + by0['tc'][1]) / by0['n'] * 100, 1))
    rec = recession_path(p['years'], seed) if p['shock'] else None
    dr = Draws(mulberry32(seed))
    for yr in range(p['years']):
        run_year(agents, yr, p, rec[yr] if rec else (False, 1.0), dr)
    fm = wealth_metrics(agents)
    bm = blei_metrics(agents, p['bu'], p['ccoOn'], p['pth'], p['szh'], p['szhCoh'], p['ptf'])
    at_floor = sum(1 for a in agents if a.wealth <= WEALTH_FLOOR + 1e-6)
    return dict(
        pov=js_round1(fm['pov'] * 100), gini=js_round(fm['gini'], 3), giniPlain=js_round(fm['giniPlain'], 3),
        wealth=js_round0(fm['med']),
        p10=js_round0(fm['p10']), p90=js_round0(fm['p90']), bleiMed=js_round0(bm['med']),
        bleiPovPct=js_round1((bm['tc'][0] + bm['tc'][1]) / bm['n'] * 100), pctFlourishing=js_round1(bm['pctF']),
        avgEDC=js_round1(bm['avgEDC'] * 100), fracAtFloor=at_floor / len(agents),
        medianPinned=js_round0(fm['med']) == WEALTH_FLOOR, yearZero=year_zero,
        recessionYears=sum(1 for r in rec if r[0]) if rec else 0)


# JavaScript's toFixed (exact decimal value, ties away from zero) and Math.round
# (ties toward +infinity), for reporting.
def js_round(x, nd):
    return float(Decimal(x).quantize(Decimal(1).scaleb(-nd), rounding=ROUND_HALF_UP))


def js_round1(x):
    return js_round(x, 1)


def js_round0(x):
    r = math.floor(x)
    return int(r + 1 if x - r >= 0.5 else r)


# ---------------------------------------------------------------------------
# Comparison with the engine's reference outputs (00-START-HERE.md, "What
# counts as a match")
# ---------------------------------------------------------------------------
HEADLINE = [('pov', 'wealth poverty %'), ('wealth', 'median wealth $'), ('bleiMed', 'median BLEI days'),
            ('gini', 'Gini'), ('bleiPovPct', 'BLEI poverty %')]
OTHER = ['p10', 'p90', 'pctFlourishing', 'avgEDC', 'fracAtFloor', 'medianPinned', 'recessionYears',
         'yearZero.pov', 'yearZero.bleiPovNeutral', 'yearZero.bleiPovScenario']


def get_key(d, k):
    for part in k.split('.'):
        d = d[part]
    return d


def parse_seeds(text):
    out = []
    for part in text.split(','):
        if '-' in part:
            lo, hi = part.split('-')
            out.extend(range(int(lo), int(hi) + 1))
        elif part:
            out.append(int(part))
    return out


def mean_sd(xs):
    n = len(xs)
    m = sum(xs) / n
    sd = math.sqrt(sum((x - m) ** 2 for x in xs) / (n - 1)) if n > 1 else 0.0
    return m, sd


def compare(ref_path, seeds):
    ref = json.load(open(ref_path))
    report = {}
    for name in ORDER:
        rp = ref['presets'][name]
        p = dict(PRESETS[name])
        for k, v in rp['params'].items():
            if k in p and p[k] != v:
                raise SystemExit(f'{name}: parameter {k} differs from the reference file ({p[k]} vs {v})')
        mine = {s: run_scenario(p, s) for s in seeds}
        exact = {}
        for k in [h[0] for h in HEADLINE] + OTHER:
            same = [s for s in seeds if str(s) in rp['seeds'] and get_key(mine[s], k) == get_key(rp['seeds'][str(s)], k)]
            exact[k] = (len(same), len([s for s in seeds if str(s) in rp['seeds']]))
        stat = {}
        s30 = [s for s in seeds if 1 <= s <= 30 and str(s) in rp['seeds']]
        if len(s30) >= 2:
            for k in [h[0] for h in HEADLINE] + OTHER:
                rv = [float(get_key(rp['seeds'][str(s)], k)) for s in s30]
                mv = [float(get_key(mine[s], k)) for s in s30]
                rm, rsd = mean_sd(rv)
                mm, msd = mean_sd(mv)
                se = rsd / math.sqrt(len(s30))
                ok = abs(mm - rm) <= 2 * se if se > 0 else abs(mm - rm) < 1e-12
                stat[k] = dict(ref_mean=rm, ref_sd=rsd, mean=mm, sd=msd, se=se, match=ok)
        s42 = None
        if 42 in mine and '42' in rp['seeds']:
            s42 = {k: (get_key(mine[42], k), get_key(rp['seeds']['42'], k)) for k in [h[0] for h in HEADLINE] + OTHER}
        report[name] = dict(exact=exact, stat=stat, seed42=s42)
    return report


def print_report(report):
    for name in ORDER:
        r = report[name]
        print(f'\n## {name}')
        if r['seed42']:
            print('seed 42, key: mine / engine')
            for k, (m, e) in r['seed42'].items():
                print(f'  {k:26s} {m!s:>12} {e!s:>12}  {"same" if m == e else "DIFFERENT"}')
        print('exact agreement, seeds compared: ' + ', '.join(f'{k} {a}/{b}' for k, (a, b) in r['exact'].items()))
        if r['stat']:
            print('seeds 1-30: key, engine mean, my mean, 2 SE, match')
            for k, s in r['stat'].items():
                print(f'  {k:26s} {s["ref_mean"]:14.4f} {s["mean"]:14.4f} {2 * s["se"]:10.4f}  {"yes" if s["match"] else "NO"}')


# ---------------------------------------------------------------------------
# 500-seed means against the engine's python-reference-500.json. Two tests per
# key: the brief's (my mean within two of the engine's standard errors) and a
# two-sample one (the difference within two standard errors of a difference of
# two independent means), since this program's adults are not the engine's.
# ---------------------------------------------------------------------------
KEYS500 = [h[0] for h in HEADLINE] + ['giniPlain'] + OTHER


def _run500(args):
    name, seed = args
    return name, seed, run_scenario(PRESETS[name], seed)


def run_many(seeds, workers):
    jobs = [(name, s) for name in ORDER for s in seeds]
    if workers > 1:
        import multiprocessing as mp
        with mp.Pool(workers) as pool:
            res = pool.map(_run500, jobs, chunksize=4)
    else:
        res = [_run500(j) for j in jobs]
    mine = {}
    for name, s, out in res:
        mine.setdefault(name, {})[str(s)] = out
    return mine


def table500(ref, mine):
    lines = []
    for name in ORDER:
        seeds = sorted(mine[name], key=int)
        n = len(seeds)
        lines.append(f'\n## {name} (seeds {seeds[0]}-{seeds[-1]}, n = {n})')
        lines.append(f'| key | engine mean | my mean | difference | brief: 2 SE | brief | two-sample z | two-sample |')
        lines.append('|---|---|---|---|---|---|---|---|')
        for k in KEYS500:
            rk = 'gini' if k == 'giniPlain' else k
            rv = [float(get_key(ref['presets'][name]['seeds'][s], rk)) for s in seeds]
            mv = [float(get_key(mine[name][s], k)) for s in seeds]
            rm, rsd = mean_sd(rv)
            mm, msd = mean_sd(mv)
            se = rsd / math.sqrt(n)
            se2 = math.sqrt((rsd ** 2 + msd ** 2) / n)
            d = mm - rm
            z = d / se2 if se2 > 0 else (0.0 if abs(d) < 1e-12 else float('inf'))
            ok1 = abs(d) <= 2 * se + 1e-12
            ok2 = abs(z) <= 2
            label = 'gini (without n/(n-1))' if k == 'giniPlain' else k
            lines.append(f'| {label} | {rm:.4f} | {mm:.4f} | {d:+.4f} | {2 * se:.4f} | {"yes" if ok1 else "no"} | '
                         f'{z:+.2f} | {"yes" if ok2 else "no"} |')
    return '\n'.join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--preset', default='baseline')
    ap.add_argument('--seed', type=int, default=42)
    ap.add_argument('--json', action='store_true')
    ap.add_argument('--compare')
    ap.add_argument('--seeds', default='1-30,42')
    ap.add_argument('--compare500')
    ap.add_argument('--workers', type=int, default=1)
    ap.add_argument('--mine', help='reuse a saved --compare500 run instead of running again')
    ap.add_argument('--out')
    args = ap.parse_args(argv)
    if args.compare:
        rep = compare(args.compare, parse_seeds(args.seeds))
        print_report(rep)
        if args.out:
            json.dump(rep, open(args.out, 'w'), indent=1)
        return
    if args.compare500:
        ref = json.load(open(args.compare500))
        if args.mine:
            mine = json.load(open(args.mine))['mine']
        else:
            mine = run_many(parse_seeds(args.seeds), args.workers)
            if args.out:
                with open(args.out, 'w') as fh:
                    json.dump(dict(mine=mine), fh, separators=(',', ':'))
        print(table500(ref, mine))
        return
    name = ALIASES.get(args.preset, args.preset)
    out = run_scenario(PRESETS[name], args.seed)
    if args.json:
        print(json.dumps(out, indent=1))
    else:
        print(f'{name}, seed {args.seed}')
        for k, label in HEADLINE:
            print(f'  {label:20s} {out[k]}')


if __name__ == '__main__':
    main()
