"""v5.2 round, step 4 (Oct 3, 2026): the inputs of the ageing switch (harness.js AGE), derived from primary sources.

1. Starting ages: US Census Bureau, Vintage 2024 national population estimates by single year of age, both sexes, July 1, 2024 (file
   nc-est2024-agesex-res.csv, column POPESTIMATE2024, SEX = 0). The model's adults are working-age earners, so ages are drawn in proportion to the
   resident population aged 25 to 66 (CFG.AGE_WEIGHTS, people at each age 25..66, in thousands).
2. Deaths: the 2022 US period life table for the total population, probability of dying between ages x and x + 1 (Arias, Xu and Kochanek,
   "United States Life Tables, 2022", National Vital Statistics Reports 74(2), April 8, 2025, Table 1; 100 and older: 1.0) (CFG.DEATH_Q, ages
   25..100). The Social Security Administration's own period life table for the same year (2022, used in the 2025 Trustees Report) could not be read
   from this environment (ssa.gov refuses the connection), so the NCHS table for the same year and population stands in; at age 67 the two agree to
   within 0.3% (NCHS 0.016329 for both sexes; SSA 0.020213 male and 0.012532 female, mean 0.016373).

Usage: python3 sources/demography.py   (downloads both files, needs network access and pdftotext; prints the two arrays as they appear in harness.js)
"""
import csv, io, re, subprocess, tempfile, urllib.request, os
CENSUS = 'https://www2.census.gov/programs-surveys/popest/datasets/2020-2024/national/asrh/nc-est2024-agesex-res.csv'
NCHS = 'https://www.cdc.gov/nchs/data/nvsr/nvsr74/nvsr74-02.pdf'
rows = [r for r in csv.DictReader(io.StringIO(urllib.request.urlopen(CENSUS, timeout=60).read().decode())) if r['SEX'] == '0']
pop = {int(r['AGE']): int(r['POPESTIMATE2024']) for r in rows}
w = [round(pop[a] / 1000) for a in range(25, 67)]
with tempfile.TemporaryDirectory() as d:
    pdf = os.path.join(d, 'lt.pdf'); open(pdf, 'wb').write(urllib.request.urlopen(NCHS, timeout=60).read())
    subprocess.run(['pdftotext', '-layout', pdf, os.path.join(d, 'lt.txt')], check=True)
    t = open(os.path.join(d, 'lt.txt')).read().split('\n')
a = [i for i, l in enumerate(t) if l.startswith('Table 1. Life table for the total population')][0]
b = [i for i, l in enumerate(t) if l.startswith('Table 2. Life table for males')][0]
q = {}
for l in t[a:b]:
    m = re.match(r'\s*(\d+)[–-](\d+)\.[ .]*\s+([0-9.]+)\s+([\d,]+)', l)
    if m: q[int(m.group(1))] = float(m.group(3))
q[100] = 1.0
print('CFG.AGE_WEIGHTS = ' + str(w).replace(' ', '') + ';')
print('CFG.DEATH_Q = ' + str([q[x] for x in range(25, 101)]).replace(' ', '') + ';')
