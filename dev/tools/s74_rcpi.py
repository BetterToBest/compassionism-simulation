#!/usr/bin/env python3
"""S74 Amendment 3: the R-CPI-I check (research-update prereg/2026-11-s74-central-bank.md, item 4 and Amendment 3).

A derived calculation outside the engine. Reads BLS's research CPI by income quintile (R-CPI-I and its chained version,
December 2005 = 100) and its relative importance, as Duke supplied them (sources/s74_history/raw/, SHA-256 in
R-CPI-I-README.md), and FRED's CPI-U series already in the history files. Prints:
  (a) each quintile's annual rate, December 2005 to December 2025 (chained: to December 2024), beside CPI-U over the same months;
  (b) the lowest-minus-highest quintile gap;
  (c) the engine's own-inflation method (food, housing and medical care at CPI-U's food at home, shelter and medical care;
      the rest at all items) applied to each quintile's December 2005 BLS shares;
  (d) the engine's own-inflation figures (dev/runs/s74-final/tables.md, History) beside them.
CPIAUCSL and the components are seasonally adjusted; R-CPI-I is not: December to December keeps seasonality out.
Usage: python3 dev/tools/s74_rcpi.py   (writes dev/runs/s74-rcpi/rcpi.md and rcpi.json)
"""
import csv, hashlib, json, os, re
import openpyxl

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
RAW = os.path.join(ROOT, 'sources', 's74_history', 'raw')
OUT = os.path.join(ROOT, 'dev', 'runs', 's74-rcpi')
SHA = {'R-CPI-I.xlsx': 'd3a7ae2554b4e059a3e9f9420483ec6fc8fabc29e5ec4387cd57a0cd0b02e3bc',
       'R-C-CPI-I.xlsx': '4752f7c7c4573549c2772e39df0768963d080a09aa86079d010f683999cf72ad',
       'R-CPI-I-relative-importance.xlsx': 'ea5c845490b3ea4584dcf9fba17336b51471b75c23a5a9a5e6eaf095a9c5190b'}


def sha(f):
    with open(os.path.join(RAW, f), 'rb') as h:
        return hashlib.sha256(h.read()).hexdigest()


for f, s in SHA.items():
    if sha(f) != s:
        raise SystemExit(f + ': SHA-256 differs from R-CPI-I-README.md')


def index(f):
    """{(year, month): [I1..I5]} from a BLS table; '-' months are left out."""
    ws = openpyxl.load_workbook(os.path.join(RAW, f), data_only=True).active
    d = {}
    for r in ws.iter_rows(values_only=True):
        if isinstance(r[0], int) and isinstance(r[1], int) and all(isinstance(v, (int, float)) for v in r[2:7]):
            d[(r[0], r[1])] = [float(v) for v in r[2:7]]
    return d


def fred(name):
    with open(os.path.join(RAW, name + '.csv')) as h:
        return {(int(r[0][:4]), int(r[0][5:7])): float(r[1]) for r in list(csv.reader(h))[1:] if r[1] not in ('', '.')}


def rate(a, b, years):
    return 100 * ((b / a) ** (1 / years) - 1)


R, RC = index('R-CPI-I.xlsx'), index('R-C-CPI-I.xlsx')
U, FOOD, SHEL, MED = fred('CPIAUCSL'), fred('CUSR0000SAF11'), fred('CUSR0000SAH1'), fred('CPIMEDSL')
s0, e1, e2 = (2005, 12), (2025, 12), (2024, 12)
res = {'rcpi': [rate(R[s0][q], R[e1][q], 20) for q in range(5)],
       'rccpi': [rate(RC[s0][q], RC[e2][q], 19) for q in range(5)],
       'cpiu20': rate(U[s0], U[e1], 20), 'cpiu19': rate(U[s0], U[e2], 19)}
comp = {k: rate(v[s0], v[e1], 20) for k, v in (('all', U), ('food', FOOD), ('shelter', SHEL), ('medical', MED))}
res['components'] = comp

# (c) The engine's method on BLS's December 2005 shares: a fixed-weight (Laspeyres) basket over the 20 years, as the engine's
# own-inflation measure is (its basket shares are held at the start). Food and beverages at food at home, housing at shelter.
ws = openpyxl.load_workbook(os.path.join(RAW, 'R-CPI-I-relative-importance.xlsx'), data_only=True)['R-CPI-I RI 200512']
sh = {}
for r in ws.iter_rows(values_only=True):
    if r[0] in ('SAF', 'SAH', 'SAM') and all(isinstance(v, (int, float)) for v in r[2:7]):
        sh[r[0]] = [float(v) / 100 for v in r[2:7]]
G = {k: v[e1] / v[s0] for k, v in (('all', U), ('food', FOOD), ('shelter', SHEL), ('medical', MED))}
meth = []
for q in range(5):
    f, h, m = sh['SAF'][q], sh['SAH'][q], sh['SAM'][q]
    meth.append(rate(1, f * G['food'] + h * G['shelter'] + m * G['medical'] + (1 - f - h - m) * G['all'], 20))
res['method'] = meth
res['shares2005'] = sh

# (d) The engine's figures, read from the committed table (History, no-programme run, actual rate path).
eng = None
with open(os.path.join(ROOT, 'dev', 'runs', 's74-final', 'tables.md')) as h:
    m = re.search(r"own inflation, 2006-2025\*\*.*?CPI-U ([\d.]+); all households ([\d.]+) \(10th-90th percentile ([\d.]+) to ([\d.]+)\); by fifth ([\d., ]+); top 1% (\d+\.\d+)", h.read())
    if m:
        eng = {'cpiu': float(m.group(1)), 'all': float(m.group(2)), 'p10': float(m.group(3)), 'p90': float(m.group(4)),
               'fifths': [float(x) for x in m.group(5).strip(' ,').split(', ')], 'top1': float(m.group(6))}
res['engine'] = eng

f2 = lambda v: '%.2f' % v
md = ['# S74: the R-CPI-I check (Amendment 3)', '',
      'BLS\'s research CPI by income quintile (R-CPI-I, December 2005 = 100; I1 lowest income, I5 highest), supplied by Duke on Nov 15, 2026 (bls.gov refuses the build machine). '
      'CPI-U is FRED\'s CPIAUCSL. December to December, % a year. Command: `python3 dev/tools/s74_rcpi.py`. A derived calculation; nothing in the engine uses it.', '',
      '| | I1 | I2 | I3 | I4 | I5 | I1 - I5 | CPI-U |', '|---|---|---|---|---|---|---|---|',
      '| R-CPI-I, Dec 2005 - Dec 2025 | ' + ' | '.join(f2(v) for v in res['rcpi']) + ' | ' + f2(res['rcpi'][0] - res['rcpi'][4]) + ' | ' + f2(res['cpiu20']) + ' |',
      '| R-C-CPI-I (chained), Dec 2005 - Dec 2024 | ' + ' | '.join(f2(v) for v in res['rccpi']) + ' | ' + f2(res['rccpi'][0] - res['rccpi'][4]) + ' | ' + f2(res['cpiu19']) + ' |',
      '| the engine\'s method on BLS\'s Dec 2005 shares | ' + ' | '.join(f2(v) for v in meth) + ' | ' + f2(meth[0] - meth[4]) + ' | ' + f2(res['cpiu20']) + ' |', '',
      'BLS\'s December 2005 shares (food and beverages / housing / medical care, %): ' + '; '.join('I%d %.1f / %.1f / %.1f' % (q + 1, 100 * sh['SAF'][q], 100 * sh['SAH'][q], 100 * sh['SAM'][q]) for q in range(5)) + '.',
      'Components, Dec 2005 - Dec 2025 (% a year): all items ' + f2(comp['all']) + ', food at home ' + f2(comp['food']) + ', shelter ' + f2(comp['shelter']) + ', medical care ' + f2(comp['medical']) + '.', '']
if eng:
    md += ['**The engine** (History, 2006-2025, annual averages; its fifths are by wealth, not income): CPI-U %.3f; all households %.3f (10th-90th percentile %.3f to %.3f); by wealth fifth %s; top 1%% %.3f. Spread across fifths %.3f points.'
           % (eng['cpiu'], eng['all'], eng['p10'], eng['p90'], ', '.join('%.3f' % v for v in eng['fifths']), eng['top1'], max(eng['fifths']) - min(eng['fifths'])), '']
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, 'rcpi.md'), 'w') as h:
    h.write('\n'.join(md))
with open(os.path.join(OUT, 'rcpi.json'), 'w') as h:
    json.dump(res, h, indent=1)
print('\n'.join(md))
