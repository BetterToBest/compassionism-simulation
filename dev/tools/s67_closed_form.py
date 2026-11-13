#!/usr/bin/env python3
"""S67 (Nov 13, 2026; research-update prereg/2026-11-s67-price-rule-derivation.md, A1): the capacity price rule's closed form.

With wage indexation and the basket both carrying last year's general inflation (phi = a + r), steady money growth m (log, a year), no slack and
prices below the money (the k branch), index.html prStep gives
    pi(t) = (1 + phi - k) pi(t-1) - phi pi(t-2) + k m,
whose roots z solve z^2 - (1 + phi - k) z + phi = 0. Steady inflation is m for any k > 0 and phi < 1 (the one-for-one pass-through is built in);
the steady gap between the money-implied level and prices is (1 - phi) m / k. Complex roots (a damped wave) when (1 + phi - k)^2 < 4 phi:
modulus sqrt(phi), period 2 pi / acos((1 + phi - k) / (2 sqrt(phi))) years. The velocity response bv adds k x bv to phi.

Prints (markdown): (1) the roots of every yearly reading; (2) the rule alone (a scalar copy of prStep and prStepQ, general basket, wage indexation 1)
on a step of money of 0.32 log a year for 40 years: the wave (largest less smallest yearly inflation, years 5-19), the period and damping measured on
the path, level pass-through at years 3 and 19, the mean and last rationed share, whether the gap ever turns negative; (3) the closed form driven by
each S58 pilot row's own money, against that row's yearly inflation in the engine (Reference; results s58-price-74ca1a8).
Usage: python3 dev/tools/s67_closed_form.py [S58_RESULTS_DIR] > dev/runs/s67-price/closed_form.md     (standard library only)
"""
import cmath, json, math, os, sys

A = 62784.912/123630.857  # index.html MULT_LS
MAIN = dict(k=0.445, k2=0.051, r=0.275, a=A, h=0.0, um=0.0593, q=1, bv=0.0, bd=0.0)
YEARLY = [('main', {}), ('k 0.25', dict(k=0.25)), ('k 1', dict(k=1.0)), ('r 0', dict(r=0.0)), ('r 0.45', dict(r=0.45)), ('a 0', dict(a=0.0)), ('k2 0', dict(k2=0.0)), ('k2 0.657', dict(k2=0.657)),
          ('slack 0.0446', dict(h=0.0446)), ("today's rule (k 1, a 0, r 0)", dict(k=1.0, r=0.0, a=0.0)),
          ('vel (bv 0.0043)', dict(bv=0.0043)), ('velh (bv 0.0022)', dict(bv=0.0022)), ('drift (bd 0.132)', dict(bd=0.132)),
          ("qtvel (today's rule, bv 0.0043)", dict(k=1.0, k2=1.0, r=0.0, a=0.0, bv=0.0043)), ("qtdrift (today's rule, bd 0.132)", dict(k=1.0, r=0.0, a=0.0, bd=0.132)),
          ('US 1960-1983 (k 0.282, k2 0.657, persistence 0.922)', dict(k=0.282, k2=0.657, r=0.922 - A)), ('US 1984-2024 (k 0.615, k2 0, persistence 0.488)', dict(k=0.615, k2=0.0, r=0.0, a=0.488)),
          ('high-inflation panel, pooled (k 0.085, persistence 0.663)', dict(k=0.0851, k2=0.0851, r=0.6631 - A)), ('high-inflation panel, episode effects (k 0.178, persistence 0.544)', dict(k=0.1782, k2=0.1782, r=0.5438 - A))]
SUB = [('wy (4 sub-steps; k 0.0788, k2 0, r 0.2333 a quarter)', dict(q=4, k=0.0788, k2=0.0, r=0.2333)),
       ('wyroot (4 sub-steps; a 0, r 0.9406, k 0.0317, k2 0.0036)', dict(q=4, a=0.0, r=0.9406, k=0.0317, k2=0.0036)),
       ("today's rule in 4 sub-steps (k 1, a 0, r 0)", dict(q=4, k=1.0, a=0.0, r=0.0))]

def roots(o):
    phi = o['a'] + o['r'] + o['k']*o['bv']; tr = 1 + phi - o['k']; z = [(tr + s*cmath.sqrt(tr*tr - 4*phi))/2 for s in (1, -1)]
    cx = abs(z[0].imag) > 1e-12; mod = max(abs(v) for v in z)
    return dict(phi=phi, cx=cx, mod=mod, period=(2*math.pi/abs(cmath.phase(z[0])) if cx else None), z=z, gap=(1 - phi)/o['k'] if o['k'] > 0 else None)

def run(o, money):
    """The rule alone on the general basket: money[t] = the year's log money growth. Returns yearly log inflation, the levels, n, and each year's record."""
    n = m = p = dg = dl = 0.0; dq = []; pis = []; rec = []; pi_prev = 0.0; Q = int(o['q'])
    for dn in money:
        m += dn; dn *= 1 + o['bd']; p0 = p; w = pi_prev  # wage indexation 1: w = ln(1 + last year's general inflation); the basket = the general level
        if Q <= 1:
            n += dn; x = n + o['bv']*dg - p
            p += o['a']*w + o['r']*pi_prev + o['k']*max(0.0, x - o['h']) + o['k2']*min(0.0, x)
            rec.append(dict(x=x, rat=max(0.0, x - o['h'] - o['um']), avg=0.0))
        else:
            R = dict(x=0.0, rat=0.0, avg=0.0)
            for j in range(Q):
                n += dn/Q; R['avg'] += (p - p0)/Q; x = n + o['bv']*sum(dq) - p; g0 = p
                p += o['a']*w/Q + o['r']*dl + o['k']*max(0.0, x - o['h']) + o['k2']*min(0.0, x)
                dl = p - g0; dq.append(dl); dq = dq[-Q:]; R['x'] += x/Q; R['rat'] += max(0.0, x - o['h'] - o['um'])/Q
            rec.append(R)
        dg = p - p0; pi_prev = dg; pis.append(dg); rec[-1].update(p=p, n=n, m=m)
    return pis, rec

def wave(pis): v = [100*(math.exp(x) - 1) for x in pis[4:19]]; return max(v) - min(v)
def measured(pis, mstar):
    """Period and damping from the path's turning points around the steady inflation."""
    d = [x - mstar for x in pis]; tp = [t for t in range(1, len(d) - 1) if (d[t] - d[t - 1])*(d[t + 1] - d[t]) < 0 and abs(d[t]) > 0.002]
    if len(tp) < 3 or abs(d[tp[0]]) < 0.01: return None, None  # no wave to measure (turning points under 0.2 points of inflation are noise)
    per = 2.0*(tp[-1] - tp[0])/(len(tp) - 1); amp = [abs(d[t]) for t in tp]
    damp = (amp[-1]/amp[0])**(1.0/(tp[-1] - tp[0])) if amp[0] > 0 and amp[-1] > 0 else None
    return per, damp
f = lambda v, d=3: '-' if v is None else ('%.' + str(d) + 'f') % v

print('# The capacity price rule in closed form (S67)\n')
print('Made by `dev/tools/s67_closed_form.py` (research-update `prereg/2026-11-s67-price-rule-derivation.md`, A1). φ = α + ρ (+ κ × bv).\n')
print('## 1. Roots of the yearly rule, π(t) = (1 + φ − κ)π(t−1) − φπ(t−2) + κm\n')
print('| Reading | φ | κ | Roots | Modulus | Period (years) | Steady gap per unit of money growth (1 − φ)/κ | Stable |\n|---|---|---|---|---|---|---|---|')
for nm, d in YEARLY:
    o = dict(MAIN, **d); R = roots(o)
    rt = '%.3f ± %.3fi' % (R['z'][0].real, abs(R['z'][0].imag)) if R['cx'] else '%.3f, %.3f' % (R['z'][0].real, R['z'][1].real)
    print('| %s | %.3f | %.3f | %s | %.3f | %s | %s | %s |' % (nm, R['phi'], o['k'], rt, R['mod'], f(R['period'], 1) if R['cx'] else 'no wave', f(R['gap']), 'yes' if R['mod'] < 1 else 'no'))
M = 0.32
print('\n## 2. The rule alone on a step of money (%.2f log a year, 40 years; wage indexation 1; general basket)\n' % M)
print('| Reading | Wave, years 5-19 (points) | Period on the path | Damping a year on the path | Pass-through, year 3 | Year 19 | Year 40 | Rationed share, mean of 20 years (%) | Within-year average level over opening, mean | Gap turns negative |\n|---|---|---|---|---|---|---|---|---|---|')
for nm, d in YEARLY[:10] + SUB + YEARLY[10:]:
    o = dict(MAIN, **d); pis, rec = run(o, [M]*40); per, damp = measured(pis, M*(1 + o['bd']))
    pt = lambda t: rec[t - 1]['p']/rec[t - 1]['m']
    print('| %s | %.1f | %s | %s | %.3f | %.3f | %.3f | %.1f | %.3f | %s |' % (nm, wave(pis), f(per, 1), f(damp), pt(3), pt(19), pt(40), 100*sum(1 - math.exp(-r['rat']) for r in rec[:20])/20,
          sum(math.exp(r['avg']) for r in rec[:20])/20, 'yes, year %d' % (1 + min(t for t, r in enumerate(rec) if r['x'] < 0)) if any(r['x'] < 0 for r in rec) else 'no'))
D = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), '..', '..', '..', 'compassionism-sim-results', 's58-price-74ca1a8')
fn = os.path.join(D, 's58-price-ref.json')
if os.path.exists(fn):
    J = json.load(open(fn))['rows']; T = 19
    def path(row, s): return [math.log(J[row]['plv_%d' % t][s]/J[row]['plv_%d' % (t - 1)][s]) for t in range(1, T + 1)]
    S58 = [('c22-cap', {}), ('c22-k25', dict(k=0.25)), ('c22-k1', dict(k=1.0)), ('c22-r0', dict(r=0.0)), ('c22-r45', dict(r=0.45)), ('c22-a0', dict(a=0.0)), ('c22-h', dict(h=0.0446)),
           ('c22-k2z', dict(k2=0.0)), ('c22-k2h', dict(k2=0.657)), ('c22-nest', dict(k=1.0, r=0.0, a=0.0)), ('rel-cap', {}), ('rel-k25', dict(k=0.25))]
    print('\n## 3. The closed form against the engine (S58 pilot, Reference, seeds 1-100)\n')
    print("Each seed's closed-form path is driven by the money of the same design under today's rule on that seed (its yearly log price change), then compared with the capacity row's yearly inflation in the engine. Differences in points of yearly inflation; wave = largest less smallest yearly inflation over years 5-19 on the mean path.\n")
    print('| S58 row | Mean absolute difference | Largest (mean path) | In year | Wave, engine | Wave, closed form | Period on the engine path | Closed-form period |\n|---|---|---|---|---|---|---|---|')
    for row, d in S58:
        o = dict(MAIN, **d); base = 'c22' if row[:3] == 'c22' else 'rel'; N = len(J[row]['plv_0']); E = [0.0]*T; C = [0.0]*T; mad = 0.0
        for s in range(N):
            mny = path(base, s); eng = path(row, s); cf, _ = run(o, mny)
            for t in range(T): E[t] += eng[t]/N; C[t] += cf[t]/N; mad += abs(100*(math.exp(eng[t]) - math.exp(cf[t])))/N/T
        dif = [100*(math.exp(E[t]) - math.exp(C[t])) for t in range(T)]; big = max(range(T), key=lambda t: abs(dif[t]))
        mm = sum(sum(path(base, s)) for s in range(N))/N/T; per, _ = measured(E, mm); R = roots(o)
        print('| %s | %.2f | %+.2f | %d | %.1f | %.1f | %s | %s |' % (row, mad, dif[big], big + 1, wave(E), wave(C), f(per, 1), f(R['period'], 1) if R['cx'] else 'no wave'))
