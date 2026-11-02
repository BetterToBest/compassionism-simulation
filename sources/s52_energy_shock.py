"""S52 (Nov 2, 2026): the outside supply-shock environment's calibration (index.html SX_DEFAULTS; research-update prereg/2026-11-supply-shock-addendum.md).

Data: US Bureau of Labor Statistics consumer price indexes, seasonally adjusted, monthly, via FRED (fred.stlouisfed.org/graph/fredgraph.csv?id=<series>),
downloaded Nov 2, 2026 into sources/energy/:
  CPIENGSL      energy                         CPIUFDSL       food
  CPITRNSL      transportation                 CPIMEDSL       medical care
  CUSR0000SAH21 household energy (utilities and heating)
  CUSR0000SAH1  shelter                        CPILFESL       all items less food and energy ("core")
  CPIAUCSL      all items (not used in the fit; kept for checks)
Annual means of complete calendar years, 1967-2024 (the years every series covers in full).

1. Episodes. The real energy price is energy over core. The three largest two-year rises from a trough since 1967 (1972-74, 1978-80, 2020-22) give
   the shock's size (the rise to the peak, two years after the trough) and how much of it was still there two years after the peak (retained share,
   capped at 1). The environment's main shock takes the median of each across the three; the others are swept. Calibration, not a target.
2. Pass-through. For each basket category, the two-year change in its price relative to core regressed on the two-year change in the real energy
   price (ordinary least squares, 1969-2024, overlapping two-year windows, so the standard errors are understated and are printed only as a guide).
   Shelter and medical care are not different from zero and have no cost channel from energy over two years: the engine uses 0 for both.
   The engine's housing category includes tenant-paid utilities (HUD Fair Market Rent): its pass-through is the utilities' share of housing
   (CFG.PTFS_UTIL, 12.8%) times household energy's.
Run: python3 -I sources/s52_energy_shock.py   (prints every figure the engine uses)
"""
import csv, math, os

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'energy')

def load(s):
    r = {}
    for row in csv.DictReader(open(os.path.join(D, s + '.csv'))):
        k = list(row.keys()); v = row[k[1]]
        if v in ('', '.'): continue
        r.setdefault(int(row[k[0]][:4]), []).append(float(v))
    return {y: sum(v)/len(v) for y, v in r.items() if len(v) == 12}

SER = ['CPIENGSL', 'CPIUFDSL', 'CPITRNSL', 'CPIMEDSL', 'CUSR0000SAH21', 'CUSR0000SAH1', 'CPILFESL']
S = {s: load(s) for s in SER}
YRS = [y for y in sorted(set.intersection(*[set(v) for v in S.values()])) if y <= 2024]
re = {y: S['CPIENGSL'][y]/S['CPILFESL'][y] for y in YRS}

print('Real energy price (energy over core), years', YRS[0], '-', YRS[-1])
EP = [(1972, 1974), (1978, 1980), (2020, 2022)]
size, kept = [], []
for t, pk in EP:
    rise = re[pk]/re[t] - 1; later = re[pk + 2]/re[t] - 1; k = min(1.0, later/rise)
    size.append(rise); kept.append(k)
    print('  trough %d, peak %d: rise %.1f%%; two years after the peak %.1f%% above the trough, retained share %.2f' % (t, pk, rise*100, later*100, k))
med = lambda v: sorted(v)[len(v)//2]
print('  main shock: rise %.3f (median), retained %.2f (median); swept: rise %.3f and %.3f (the other episodes), %.3f (twice the median, beyond history); retained %.2f and %.2f'
      % (med(size), med(kept), min(size), max(size), 2*med(size), min(kept), max(kept)))

def ols(x, y):
    n = len(x); mx = sum(x)/n; my = sum(y)/n
    sxx = sum((a - mx)**2 for a in x); b = sum((a - mx)*(c - my) for a, c in zip(x, y))/sxx
    res = [c - my - b*(a - mx) for a, c in zip(x, y)]
    return b, math.sqrt(sum(r*r for r in res)/(n - 2)/sxx)

print('Pass-through to each category (two-year changes, relative to core), 1969-2024')
B = {}
for s, name in [('CPIUFDSL', 'food'), ('CPITRNSL', 'transport'), ('CUSR0000SAH21', 'household energy'), ('CUSR0000SAH1', 'shelter'), ('CPIMEDSL', 'medical care')]:
    ys = YRS[2:]
    X = [math.log(re[y]/re[y - 2]) for y in ys]
    Y = [math.log(S[s][y]/S[s][y - 2]) - math.log(S['CPILFESL'][y]/S['CPILFESL'][y - 2]) for y in ys]
    b, se = ols(X, Y); B[name] = b
    print('  %-17s %.3f (se %.3f, n %d)' % (name, b, se, len(ys)))
UTIL = 487.685/(3326.284 + 487.685)
print('Engine: food %.3f, transport %.3f, utilities %.3f, housing (utilities share %.4f) %.4f, medical 0, other categories 0'
      % (B['food'], B['transport'], B['household energy'], UTIL, UTIL*B['household energy']))
