"""S34 (Oct 30, 2026): the gap tables of dev/reports/baseline-realism.md, from the result files in dev/runs/baseline-realism/.

The gap rule is the preregistration's (research-update prereg/s34-baseline-realism.md): a share differing by more than 3 points, a dollar level whose ratio
to the outside figure is outside 0.80-1.25, a Gini differing by more than 0.03. "gap" marks a gap at that year; "-" no gap.

Usage: python3 dev/tools/baseline_realism_table.py [ENV] [ROW ...]   (ENV ref, adv or st, default ref; rows default sn none; exploratory rows read the
       -explore file). Prints Markdown.
"""
import json, os, sys
R = os.path.join(os.path.dirname(__file__), '..', 'runs', 'baseline-realism')
A = [a for a in sys.argv[1:]]
ENV = A[0] if A else 'ref'
ROWS = A[1:] or ['sn', 'none']
US = json.load(open(os.path.join(R, 'us-figures.json')))
def load(name):
    p = os.path.join(R, name)
    return json.load(open(p)) if os.path.exists(p) else {'rows': {}}
M = load('baseline-realism-%s.json' % ENV)['rows']; M.update(load('baseline-realism-%s-explore.json' % ENV)['rows'])
c, s25, s22, b = US['cps'], US['scf2025']['withWages'], US['scf2022']['withWages'], US['bls']
TY = {'sg': 'single adults', 'sp': 'single parents', 'cn': 'couples without children', 'ck': 'couples with children'}

def gap(kind, m, u):
    if m is None or u is None: return ''
    if kind == 'share': return 'gap' if abs(m - u) > 3 else '-'
    if kind == 'gini': return 'gap' if abs(m - u) > 0.03 else '-'
    return 'gap' if not (0.8 <= m/u <= 1.25) else '-'
def fmt(kind, x):
    if x is None: return 'n/a'
    return '%.1f%%' % x if kind == 'share' else '%.3f' % x if kind == 'gini' else '$%s' % format(int(round(x, -2)), ',')
def get(row, y, path):
    o = M[row][y]
    for k in path: o = o[k] if o else None
    return o['mean'] if o else None

LINES = [  # (label, kind, outside value, outside source, path in the model's year summary, or a function of the row)
    ('Median earnings, adults with earnings', 'usd', c['earnings25to64']['median'], 'CPS ASEC 2026, ages 25-64', ['earnMed']),
    ('10th percentile of earnings', 'usd', c['earnings25to64']['p10'], 'CPS ASEC 2026', ['earnP10']),
    ('25th percentile', 'usd', c['earnings25to64']['p25'], 'CPS ASEC 2026', ['earnP25']),
    ('75th percentile', 'usd', c['earnings25to64']['p75'], 'CPS ASEC 2026', ['earnP75']),
    ('90th percentile', 'usd', c['earnings25to64']['p90'], 'CPS ASEC 2026', ['earnP90']),
    ('Gini of earnings, adults with earnings', 'gini', c['earnings25to64']['gini'], 'CPS ASEC 2026', ['earnGini']),
    ('Adults with any earnings in the year', 'share', c['earnings25to64']['shareWithEarnings'], 'CPS ASEC 2026, ages 25-64', ['earnShare']),
    ('Official poverty, adults', 'share', c['official']['age25to64'], 'CPS ASEC 2026, ages 25-64', ['fplAdult']),
    ('Official poverty, adults (US: adults with earnings)', 'share', c['official']['age25to64Earners'], 'CPS ASEC 2026, ages 25-64 with earnings', ['fplAdult']),
    ('Official poverty, children', 'share', c['official']['under18'], 'CPS ASEC 2026, under 18', ['fplKid']),
    ('Official poverty, adults and children', 'share', c['official']['age25to64AndUnder18'], 'CPS ASEC 2026, ages 25-64 and under 18', ['fplAll']),
    ('Median household money income', 'usd', c['householdIncome25to64']['median'], 'CPS ASEC 2026, householder 25-64', ['hhIncMed']),
    ('Gini of household money income', 'gini', c['householdIncome25to64']['gini'], 'CPS ASEC 2026, householder 25-64', ['hhIncGini']),
    ('Median family net worth', 'usd', s25['all']['median'], 'SCF 2025, head 25-64 with wages', ['wealth', 'all', 'median']),
    ('Families in debt (net worth below zero)', 'share', s25['all']['neg'], 'SCF 2025', ['wealth', 'all', 'neg']),
    ('Families with net worth below $25,000', 'share', s25['all']['below25k'], 'SCF 2025', ['wealth', 'all', 'below25k'])]
for t, l in TY.items():
    LINES += [('Median net worth, ' + l, 'usd', s25[t]['median'], 'SCF 2025', ['wealth', t, 'median']),
              ('In debt, ' + l, 'share', s25[t]['neg'], 'SCF 2025', ['wealth', t, 'neg'])]

def eng(row, k): return M[row]['engine'].get(k)
for row in ROWS:
    if row not in M: continue
    print('\n**%s, row %s**\n' % ({'ref': 'Reference', 'adv': 'Adverse', 'st': 'Stress Test'}[ENV], row))
    print('| Measure | US | Source | Model, Year 0 | Model, Year 20 | Year 0 | Year 20 |')
    print('|---|---|---|---|---|---|---|')
    for lab, kind, u, src, p in LINES:
        m0, m1 = get(row, 'y0', p), get(row, 'end', p)
        print('| %s | %s | %s | %s | %s | %s | %s |' % (lab, fmt(kind, u), src, fmt(kind, m0), fmt(kind, m1), gap(kind, m0, u), gap(kind, m1, u)))
    w = 100 - eng(row, 'emUrate')
    print('| At work (share of working-age adult-years; whole run) | %s | BLS CPS 2025, employment-population ratio 25-54 | %s | (same) | %s | |' % (fmt('share', b['epop25to54']['mean2025']), fmt('share', w), gap('share', w, b['epop25to54']['mean2025'])))
    print('| Out of work (share of adult-years; whole run) | %s | BLS CPS 2025, unemployment rate 25-54 | %s | (same) | %s | |' % (fmt('share', b['urate25to54']['mean2025']), fmt('share', eng(row, 'emUrate')), gap('share', eng(row, 'emUrate'), b['urate25to54']['mean2025'])))
    if eng(row, 'snSnap') is not None:
        for k, l, u in (('snSnap', 'SNAP', 'snap'), ('snEitc', 'EITC', 'eitc'), ('snCtc', 'refundable CTC', 'actc')):
            print('| Adults in households receiving %s (whole run) | %s | CPS ASEC 2026, ages 25-64 (as reported) | %s | (same) | %s | |' % (l, fmt('share', c['safetyNet25to64'][u]), fmt('share', eng(row, k)), gap('share', eng(row, k), c['safetyNet25to64'][u])))
    print('\nModel\'s own measures (no outside series): adult-years below the cost of living %.1f%%, adults with too little wealth at the end %.1f%%, people in households below the official line (person-years) %.1f%%.' % (eng(row, 'fgt0PY'), eng(row, 'pov'), eng(row, 'hhFplPY')))
