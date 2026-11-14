"""S69: the random generator, the samplers and the numerical helpers (MODEL_SPEC.md 4.1 and Appendix C, items 9-10).

Everything here is written from the description; GAPS.md says where the code excerpt settled a detail.
"""
import math

M32 = 0xFFFFFFFF


def imul(a, b):
    """32-bit integer multiplication, as unsigned bits (JavaScript's Math.imul, read modulo 2^32)."""
    return (a * b) & M32


class Mulberry32:
    """mulberry32(seed): MODEL_SPEC.md 4.1. Calling the object draws the next uniform in [0, 1)."""
    __slots__ = ('s',)

    def __init__(self, seed):
        self.s = int(seed) & M32

    def __call__(self):
        s = (self.s + 0x6D2B79F5) & M32
        self.s = s
        t = imul(s ^ (s >> 15), 1 | s)
        t = ((t + imul(t ^ (t >> 7), 61 | t)) & M32) ^ t
        return ((t ^ (t >> 14)) & M32) / 4294967296.0


def hl_u(s, ident, yr, j):
    """The safety net's take-up uniform: a hash of (seed + 700001, the head's index, 0, slot) (Appendix C, item 22).
    The hash itself (murmur3's finaliser over the mixed integers) is from the code excerpt (GAPS.md)."""
    h = (imul((s ^ 0x5bd1e995) & M32, 0x85ebca6b) ^ imul((int(ident) + 0x632be5ab) & M32, 0xc2b2ae35)
         ^ imul((int(yr) + 0x7f4a7c15) & M32, 0x27d4eb2f) ^ imul((int(j) + 0x165667b1) & M32, 0x9e3779b1))
    h ^= h >> 16
    h = imul(h, 0x85ebca6b)
    h ^= h >> 13
    h = imul(h, 0xc2b2ae35)
    h ^= h >> 16
    return ((h & M32) + 0.5) / 4294967296.0


class Sampler:
    """The samplers of 4.1, drawing from whichever stream is current (the engine's global RNG)."""

    def __init__(self):
        self.rng = None

    def normal(self):
        r = self.rng
        u = max(1e-14, 1 - r())
        v = r()
        return math.sqrt(-2 * math.log(u)) * math.cos(2 * math.pi * v)

    def lognormal(self, mu, sigma):
        r = self.rng
        u = max(1e-14, 1 - r())
        v = r()
        return math.exp(mu + sigma * math.sqrt(-2 * math.log(u)) * math.cos(2 * math.pi * v))

    def gamma(self, a):
        r = self.rng
        if a == 1:
            return -math.log(max(1e-14, r()))
        if a < 1:
            g = self.gamma(1 + a)
            return g * math.pow(max(1e-14, r()), 1 / a)
        c = math.sqrt(2 * a - 1)
        for _ in range(5000):
            u = r()
            v = r()
            y = math.tan(math.pi * u)
            x = c * y + a - 1
            if x > 0 and v <= (1 + y * y) * math.exp((a - 1) * math.log(x / (a - 1)) - c * y):
                return x
        return a

    def beta(self, a, b):
        x = self.gamma(a)
        return x / (x + self.gamma(b))


def norm_cdf(z):
    """Appendix C, item 9: the complementary error function series (Numerical Recipes' erfcc)."""
    x = abs(z) / math.sqrt(2)
    t = 1 / (1 + 0.5 * x)
    r = t * math.exp(-x * x - 1.26551223 + t * (1.00002368 + t * (0.37409196 + t * (0.09678418 + t * (-0.18628806 + t * (0.27886807 + t * (-1.13520398 + t * (1.48851587 + t * (-0.82215223 + t * 0.17087277)))))))))
    return 1 - r / 2 if z >= 0 else r / 2


_A = [-39.69683028665376, 220.9460984245205, -275.9285104469687, 138.3577518672690, -30.66479806614716, 2.506628277459239]
_B = [-54.47609879822406, 161.5858368580409, -155.6989798598866, 66.80131188771972, -13.28068155288572]
_C = [-0.007784894002430293, -0.3223964580411365, -2.400758277161838, -2.549732539343734, 4.374664141464968, 2.938163982698783]
_D = [0.007784695709041462, 0.3224671290700398, 2.445134137142996, 3.754408661907416]


def norm_inv(p):
    """Appendix C, item 9: Acklam's rational approximation, argument clamped to [1e-12, 1 - 1e-12]."""
    a, b, c, d = _A, _B, _C, _D
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


def js_round(x):
    """JavaScript's Math.round (halves round up), not Python's banker's rounding."""
    return math.floor(x + 0.5)


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


def gini_of(x):
    """Section 9: values floored at 0, sorted; G = 2 sum(i v_i)/(n sum v) - (n + 1)/n."""
    v = sorted(max(0.0, (z if z == z else 0.0) if z is not None else 0.0) for z in x)
    n = len(v)
    t = 0.0
    w = 0.0
    for i in range(n):
        t += v[i]
        w += (i + 1) * v[i]
    return 2 * w / (n * t) - (n + 1) / n if n > 0 and t > 0 else 0


def gini_neg(x):
    """The same Gini with debts kept (giniWN)."""
    v = sorted(float(z) for z in x)
    n = len(v)
    t = 0.0
    w = 0.0
    for i in range(n):
        t += v[i]
        w += (i + 1) * v[i]
    return 2 * w / (n * t) - (n + 1) / n if n > 0 and t > 0 else 0
