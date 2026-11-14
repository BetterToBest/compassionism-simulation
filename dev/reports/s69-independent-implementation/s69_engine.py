"""S69: the candidate main row of round 2 and its no-programme run, written again in Python.

Written from MODEL_SPEC.md and ODD.md in the S69 packet, with every setting read from main-row-config.json (the switches in
effect while each run goes). Where the description did not settle a rule, the code excerpt did; GAPS.md lists each such
place with the line of the excerpt that settled it. The structure follows section 5's order of events.
"""
import math
from s69_rng import (Mulberry32, Sampler, hl_u, norm_cdf, norm_inv, js_round, median_of, quantile_of, gini_of, gini_neg)

INF = float('inf')


class Ag:
    """An adult. A field never set reads as None (the engine's 'undefined')."""

    def __getattr__(self, k):
        if k.startswith('__'):
            raise AttributeError(k)
        return None


class HH:
    """A household (section 6.13)."""

    def __getattr__(self, k):
        if k.startswith('__'):
            raise AttributeError(k)
        return None


class NS:
    """A plain record."""

    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __getattr__(self, k):
        if k.startswith('__'):
            raise AttributeError(k)
        return None


def nz(x):
    """JavaScript's `x || 0` for numbers (undefined, null, NaN and 0 all give 0)."""
    return x if (x is not None and x == x and x != 0) else 0


def fnum(x):
    """JavaScript's `+x || 0`."""
    if x is None or x is False:
        return 0
    if x is True:
        return 1
    return x if x == x else 0


class Engine:
    """One run's switches (the config's atLoad values with the row's switchesDifferentFromLoad on top)."""

    def __init__(self, state, tables):
        S = dict(state)
        self.S = S
        C = dict(S['CFG'])
        # Infinity is written as a string or null in the JSON files; restore it where the brackets need it.
        T = C.get('SN_TAX')
        if T:
            T = {'std': T['std'], 'br': {f: [[INF if (b[0] is None or b[0] == 'Infinity') else b[0], b[1]] for b in L] for f, L in T['br'].items()}}
            C['SN_TAX'] = T
        self.CFG = C
        for k, v in tables.items():
            S.setdefault(k, v)
        g = S.get
        self.HOUSEHOLDS = g('HOUSEHOLDS')
        self.SPEND_GRADE = g('SPEND_GRADE')
        self.DEBT_READ = g('DEBT_READ')
        self.RETURNS = g('RETURNS')
        self.WEALTH_TAIL = g('WEALTH_TAIL')
        self.LF_SCOPE = g('LF_SCOPE')
        self.AUD = g('AUD')
        self.FX = g('FX')
        self.BARGAIN = g('BARGAIN')
        self.THETA_GATE = g('THETA_GATE')
        self.PTH_MODE = g('PTH_MODE')
        self.DISC_BASE = g('DISC_BASE')
        self.GOV = g('GOV')
        self.RISK_MEASURE = g('RISK_MEASURE')
        self.EMPL = g('EMPL')
        self.PTHB = g('PTHB')
        self.PTFS = g('PTFS')
        self.PTF_ACCESS = g('PTF_ACCESS')
        self.PA = g('PA')
        self.PTF_OPS = g('PTF_OPS')
        self.SNET = g('SNET')
        self.SCS = g('SURPLUS_CONSUMPTION_SHARE')
        self.SCB = g('SURPLUS_CONSUMPTION_BASE')
        self.N7_BLEI = g('N7_BLEI')
        self.PTH_APPR_CONSERVE = g('PTH_APPR_CONSERVE')
        self.SURP_CUT_MARKUP = g('SURP_CUT_MARKUP')
        self.LATENT = g('LATENT')
        self.BU_SCOPE = g('BU_SCOPE')
        self.CONVERSION_MODEL = g('CONVERSION_MODEL')
        self.GATE_CURRENT = g('GATE_CURRENT')
        self.PROJ = g('PROJ')
        self.ESP = g('ESP')
        self.SURP = g('SURP')
        self.PROD = g('PROD')
        self.MULT = g('MULT')
        self.OCT = g('OCT')
        self.COST = g('COST')
        self.JOIN = g('JOIN')
        self.C22 = g('C22')
        self.PATHWAY_OFF = g('PATHWAY_OFF')
        self.PRICE_RULE = g('PRICE_RULE')
        self.PR_OPTS = g('PR_OPTS')
        self.FW = g('FW')
        for k in ('AGE', 'HEALTH', 'DIS', 'COMM', 'HCAP', 'REVIEW', 'SAVE', 'LEDGER', 'ACCT', 'FBS50', 'EDC_MEASURE', 'REC_SCRIPT'):
            if g(k):
                raise NotImplementedError('switch on that the candidate main row does not use: ' + k)


def tb_opts(o, S):
    """tbOpts: PM_DEFAULTS, TB_DEFAULTS, TB_RUN, then the row's options."""
    r = {}
    r.update(S['PM_DEFAULTS'])
    r.update(S['TB_DEFAULTS'])
    r.update(S['TB_RUN'])
    r.update(o)
    th = dict(S['PM_DEFAULTS']['theta'])
    th.update(o.get('theta') or {})
    r['theta'] = th
    return r
