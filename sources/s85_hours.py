"""Hours worked per worker in the United States, 1870-2023, and how much of the rise in output per hour was taken as shorter hours.
Written Nov 19, 2026 for the study of output per hour and automation (research-update prereg/2026-11-s85-output-per-hour.md). Reporting and
context only: no engine constant is set from this file.

Source (opened Nov 19, 2026): Our World in Data, "Annual working hours per worker" (grapher annual-working-hours-per-worker, full CSV),
which joins Huberman and Minns (2005; 1870-1938) and the Penn World Table 11.0 (Feenstra et al. 2025; from 1950). The United States rows
are saved in s85_owid/us_hours.csv; the full download's SHA-256 is recorded below.
Output per hour: BLS, Productivity and Costs, third quarter 2026 (preliminary): nonfarm business labour productivity "the long-term rate of
2.2 percent since the first quarter of 1947"; 1.5 percent a year over the 2007-2019 cycle.

Run: python3 sources/s85_hours.py
"""
import csv, math, os
FULL_SHA256 = '5277667aa75bc6ba5035b18330245028145b7378a1ff549a425d0fe1f693570d'
H = {}
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 's85_owid', 'us_hours.csv')) as f:
    for r in csv.DictReader(f):
        H[int(r['Year'])] = float(r['Working hours per worker'])
def rate(a, b):
    return (math.log(H[b]) - math.log(H[a]))/(b - a)*100
BLS_LR = 2.2  # % a year, nonfarm business output per hour, 1947Q1 onward (BLS)
for y in (1870, 1900, 1929, 1950, 1973, 2000, 2019, 2023):
    print('%d  %7.1f hours a year' % (y, H[y]))
for a, b in ((1870, 1950), (1950, 2023), (1973, 2023)):
    print('%d-%d  hours per worker %+.2f%% a year' % (a, b, rate(a, b)))
r = -rate(1950, 2023)
print('1950-2023: of output per hour growing about %.1f%% a year, hours per worker fell %.2f%% a year: about %.0f%% of the gain taken as shorter hours'
      % (BLS_LR, r, r/BLS_LR*100))
