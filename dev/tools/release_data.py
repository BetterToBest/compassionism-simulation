"""v5.2.1 (Oct 6, 2026; ledger s90, decision d156): one data file per release, a list of releases, and the headline numbers in the page text.

Every number the simulation page's guided sections, the findings explorer (findings.html) and the replication page's summary show comes from the file this
writes; nothing is typed into the HTML. Run it after the 500-seed regeneration and dev/tools/merge_panel.py (and, for the explore sections,
dev/tools/explore_export.js). It writes:
  data/releases/v<VERSION>.json   the release: meta, the two 500-seed panels exactly as merged, the backing-share sweep, the US-data check, the inputs the
                                  pages quote, a catalogue of headline figures (label, value, unit, environment, horizon, basis, what it means, where it
                                  comes from), the explorer's tables and texts (numbers as pointers into this file, never as typed text);
  data/releases/v<VERSION>/       the lazily loaded extras: bands-20.json, bands-40.json (spread across seeds, savings deciles) and
                                  lives-ENV-YEARS.json (one stated seed's adults), from dev/runs/explore-ENV-YEARS.json;
  data/manifest.json              the list of releases (version, date, tag, file, one-line summary, status current or earlier);
  index.html, findings.html, replication.html: the static headline blocks between <!-- figs:NAME --> and <!-- /figs:NAME --> markers.

Usage:
  python3 dev/tools/release_data.py                       the current release from dev/runs/ (version from index.html's META.VERSION figures line below)
  python3 dev/tools/release_data.py --check               exit 1 if any file above differs from what this would write (domtest runs it)
  python3 dev/tools/release_data.py --backfill v5.1       an earlier release, from the files committed at that tag (git show), status "earlier";
                                                          only for a tag whose regeneration reproduced its published panels exactly (dev/ADDING-A-RELEASE.md)

A number in a table or text is {"src": "<path into the release file>", "f": "<format>"}; in a text it is written {{path|format}}. Formats (the same in
site/findings.js, which renders them): p0 p1 p2 (percent), n1 n2 n3 (plain), s1 s2 (signed, with a true minus sign), usd (whole dollars), int (whole
number with commas), lev (a price level: whole number with commas from 10 up, else two decimals, then "times"), lvn (the same without "times").
"""
import json, os, re, subprocess, sys
from decimal import Decimal, ROUND_HALF_UP, ROUND_FLOOR

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
MINUS = '−'
ENVS = [('ref', 'Reference'), ('adv', 'Adverse'), ('st', 'Stress Test')]
ENV_DESC = {'ref': 'the model\u2019s main settings, with no recessions and no outside inflation',  # the simulation page's own wording (ENV_NOTE in index.html)
            'adv': 'recessions, 2% outside inflation and an automation wave',
            'st': 'the Adverse environment with weaker settings (40% take part, a smaller allowance)'}
# The figures each release's current (presentation) version describes. v5.2.1 changed only how the v5.2 figures are shown; v5.2.2 corrected words and added derived figures.
CURRENT53 = {'version': '5.3', 'date': '2026-10-07', 'tag': 'v5.3',
           'summary': 'Households and children: adults live in households as US adults do, children bring a quarter of the adult allowance, households pool their money, start with the wealth the Federal Reserve\u2019s survey shows and spend less when income is short; and what each part of the design does is measured.'}
CURRENT52 = {'version': '5.2', 'date': '2026-10-06', 'tag': 'v5.2', 'shownIn': '5.2.2',
             'summary': 'The model round: savings that keep up with prices, ageing, the no-programme run against US data, a middle backing reading and robustness readings, each beside an unchanged main result.'}

def current():
    """the release the figures in dev/runs/ are: v5.3's once its panels (households and children, harness.js --v53) are there, else v5.2's"""
    p = load_json(None, 'dev/runs/release-panel.json')
    return CURRENT53 if p and p['_meta'].get('v53') else CURRENT52

BACKFILL = {  # earlier releases whose panels were regenerated from their tags and matched exactly (dev/ADDING-A-RELEASE.md); filled in by --backfill
    'v5.2': {'version': '5.2', 'date': '2026-10-06', 'tag': 'v5.2', 'shownIn': '5.2.2',
             'summary': 'The model round: savings that keep up with prices, ageing, the no-programme run against US data, a middle backing reading and robustness readings, each beside an unchanged main result.'},
    'v5.1': {'version': '5.1', 'date': '2026-10-03', 'tag': 'v5.1',
             'summary': 'Audit fixes: the wage-bonus test reads this year\'s BU spending, the price level as a typical run with a range, the Hub\'s own targets beside the results, and the backing-share curve.'},
    'v5.0.1': {'version': '5.0.1', 'date': '2026-10-03', 'tag': 'v5.0.1',
               'summary': 'The external audit pass on v5.0: text, tests and page fixes, with the 40-year horizon added; the 20-year figures are v5.0\'s.'},
    'v5.0': {'version': '5.0', 'date': '2026-10-02', 'tag': 'v5.0',
             'summary': 'The first release of the release engine: Compassionism as specified on the Hub, every mechanism in, against no programme, in three environments over 20 years.'}}

# ---------------------------------------------------------------------------------------------------------------- formats (JavaScript's toFixed digits)
def fx(x, d=1):
    q = Decimal(abs(x)).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)
    return ('-' if x < 0 and q != 0 else '') + str(q)

def jsround(x):  # JavaScript's Math.round: halves go up (toward +infinity)
    return int((Decimal(x) + Decimal('0.5')).to_integral_value(rounding=ROUND_FLOOR))

def fmt(x, f):
    if x is None: return '–'
    if f in ('p0', 'p1', 'p2'): return fx(x, int(f[1])).replace('-', MINUS) + '%'
    if f in ('n0', 'n1', 'n2', 'n3', 'n4'): return fx(x, int(f[1])).replace('-', MINUS)
    if f in ('s0', 's1', 's2'):
        t = fx(x, int(f[1]))
        return (MINUS + t[1:]) if t.startswith('-') else ('+' + t if x > 0 and float(t) != 0 else t)
    if f == 'usd': n = jsround(x); return (MINUS if n < 0 else '') + '$' + format(abs(n), ',')
    if f == 'int': n = jsround(x); return (MINUS if n < 0 else '') + format(abs(n), ',')
    if f == 'lev': return (format(jsround(x), ',') if x >= 10 else fx(x, 2)) + '×'
    raise ValueError('unknown format ' + f)

def get(obj, path):
    for k in path.split('.'):
        obj = obj[int(k)] if isinstance(obj, list) else obj[k]
    return obj

def has(obj, path):
    try: get(obj, path); return True
    except (KeyError, IndexError, TypeError, ValueError): return False

def kids(R):  # v5.3: a release whose main row has households and children
    return has(R, 'panels.20.envs.ref.rows.release.d53.hhCostKidPY')

def N(path, f): return {'src': path, 'f': f}
def T(path, f): return '{{%s|%s}}' % (path, f)

def esc(s): return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def render_plain(R, text):
    """a text's tokens as plain formatted numbers (the catalogue's meanings, the downloads)"""
    return re.sub(r'\{\{([^|}]+)\|([a-z0-9]+)\}\}', lambda m: fmt(get(R, m.group(1)), m.group(2)), text)

def render_static(R, text):
    """a text's tokens as static HTML: <span class="num" data-src=... data-f=...>formatted</span> (site/findings.js renders them the same way)"""
    return re.sub(r'\{\{([^|}]+)\|([a-z0-9]+)\}\}', lambda m: '<span class="num" data-src="%s" data-f="%s">%s</span>' % (m.group(1), m.group(2), esc(fmt(get(R, m.group(1)), m.group(2)))), text)

# ---------------------------------------------------------------------------------------------------------------- the measures
MEAS = [  # key in the catalogue, label, panel key, change key, unit, basis, what it means
    ('bO', 'Below 30 days of basic living', 'bOAPy', 'dBO', '% of adult-years',
     'In a typical year, the share of adults whose savings, pay and support would cover fewer than 30 days of basic living (the BLEI paper’s measure).'),
    ('f0', 'Below the cost of living', 'fgt0PY', 'dF0', '% of adult-years',
     'In a typical year, the share of adults whose income falls short of the cost of a basic living (the MIT living-wage basket for one adult).'),
    ('pov', 'Too little wealth', 'pov', 'dPov', '% of adults at the last year',  # v5.2.2: the line comes from CFG.POVERTY_LINE (A3) and the measure is net wealth (A4)
     'At the end of the run, the share of adults with less than {{inputs.wealthLine|usd}} of net wealth (what someone owns minus what they owe) in today’s money.'),
    ('bN', 'Below 30 days of basic living, design-neutral', 'bNAPy', 'dBN', '% of adult-years',
     'The same 30-day measure with the no-programme rules applied to everyone, so the design’s own definitions cannot flatter it.'),
    ('kid', 'Children below the cost of living', 'hhCostKidPY', 'd53.hhCostKidPY', '% of child-years',  # v5.3 (B8); the fourth headline card
     'In a typical year, the share of children whose household’s income falls short of the household’s cost of a basic living (the MIT living-wage basket for its adults and children).')]
MEAS53 = {  # v5.3: the adult measures' meanings with households (whether a household is poor is decided for the household as a whole); site/findings.js MEANINGS53
    'bO': 'In a typical year, the share of adults whose savings, pay and support would cover fewer than 30 days of basic living (the BLEI paper’s measure; in a household, its savings, pay and costs).',
    'f0': 'In a typical year, the share of adults whose household’s income falls short of the household’s cost of a basic living (the MIT living-wage basket for its adults and children).',
    'pov': 'At the end of the run, the share of adults with less than {{inputs.wealthLine|usd}} of net wealth (what someone owns minus what they owe; in a couple, half of what the two own) in today’s money.'}
CARDS = ['bO', 'f0', 'pov', 'kid']  # the headline cards, in site/findings.js's order (CARDS); a card shows only when the release has its figures
HH_MEAS = [  # v5.3 (B8): key, label, panel key, unit, what it means (with and without; the change where the panel has it, d53)
    ('kidBO', 'Children below 30 days of basic living', 'hhBleiKidPY', '% of child-years', 'In a typical year, the share of children whose household’s savings, pay and support would cover fewer than 30 days of basic living (the household’s BLEI).'),
    ('kidPov', 'Children in a household with too little wealth', 'hhWlthKidEnd', '% of children at the last year', 'At the end of the run, the share of children whose household’s net wealth is below six months of its own cost of living (the household reading of the wealth line).'),
    ('hhF0', 'Everyone below the cost of living', 'hhCostPY', '% of person-years', 'In a typical year, the share of all people, adults and children, whose household’s income falls short of the household’s cost of a basic living.'),
    ('hhPov', 'Everyone in a household with too little wealth', 'hhWlthEnd', '% of people at the last year', 'At the end of the run, the share of all people whose household’s net wealth is below six months of its own cost of living.'),
    ('edc', 'Income lost to rent and interest (EDC, measured)', 'edcM', '% of income', 'The extractive drain measured from payments: rent paid to landlords and interest on debt as a share of all income, the BU included; community housing payments count as zero.')]
EXTRA = [  # key, label, panel key in rows.release, unit, format, what it means
    ('infl', 'Price rise caused by the programme', 'infl', '% a year', 'p1', 'How much faster prices rise each year because of the programme’s new money (the cautious reading: what the Source pays out is new money except what new output backs).'),
    ('cost', 'Cost per adult', 'cost', 'dollars a year, today’s prices', 'usd', 'The programme’s gross cost per adult each year, in today’s dollars.'),
    ('lev', 'Price level at the last year (typical run)', 'pLevEndMed', 'times today’s prices', 'lev', 'Where prices end up in the typical (median) one of the 500 runs; it compounds the yearly rise.'),
    ('hrs', 'Change in hours worked', 'hrs', '%', 's1', 'How much less (or more) people work, by the rate measured in the largest US study of unconditional cash.'),
    ('med', 'Median savings at the last year', 'medWealth', 'dollars, today’s prices', 'usd', 'The savings of the adult in the middle, with the programme.')]

def catalogue(R, Y):
    out = []
    P = R['panels'][Y]
    for e, en in ENVS:
        if e not in P['envs']: continue
        E = P['envs'][e]
        for k, lbl, pk, dk, unit, mean in MEAS:
            if pk not in E['rows']['release'] or pk not in E['base']: continue
            base = 'panels.%s.envs.%s' % (Y, e)
            if kids(R) and k in MEAS53: mean = MEAS53[k]
            out.append({'id': '%s.%s.%s.with' % (e, Y, k), 'label': lbl + ', with Compassionism', 'src': base + '.rows.release.' + pk, 'unit': unit, 'f': 'p1', 'env': e, 'years': int(Y), 'basis': 'simulated', 'meaning': render_plain(R, mean)})
            out.append({'id': '%s.%s.%s.without' % (e, Y, k), 'label': lbl + ', no programme', 'src': base + '.base.' + pk, 'unit': unit, 'f': 'p1', 'env': e, 'years': int(Y), 'basis': 'simulated', 'meaning': render_plain(R, mean)})
            if has(E['rows']['release'], dk):
                out.append({'id': '%s.%s.%s.change' % (e, Y, k), 'label': lbl + ', change against no programme', 'src': base + '.rows.release.' + dk + '.0', 'unit': 'percentage points', 'f': 's1', 'env': e, 'years': int(Y), 'basis': 'derived',
                            'ci': [base + '.rows.release.' + dk + '.1', base + '.rows.release.' + dk + '.2'], 'meaning': 'The paired difference over the same 500 runs; the 95% interval is beside it. Negative means fewer people below the line.'})
        for k, lbl, pk, unit, f, mean in EXTRA:
            if pk in E['rows']['release']:
                out.append({'id': '%s.%s.%s' % (e, Y, k), 'label': lbl, 'src': 'panels.%s.envs.%s.rows.release.%s' % (Y, e, pk), 'unit': unit, 'f': f, 'env': e, 'years': int(Y), 'basis': 'simulated', 'meaning': mean})
        for k, lbl, pk, unit, mean in HH_MEAS:
            base = 'panels.%s.envs.%s' % (Y, e)
            if pk not in E['rows']['release']: continue
            out.append({'id': '%s.%s.%s.with' % (e, Y, k), 'label': lbl + ', with Compassionism', 'src': base + '.rows.release.' + pk, 'unit': unit, 'f': 'p1', 'env': e, 'years': int(Y), 'basis': 'simulated', 'meaning': mean})
            if pk in E['base']:
                out.append({'id': '%s.%s.%s.without' % (e, Y, k), 'label': lbl + ', no programme', 'src': base + '.base.' + pk, 'unit': unit, 'f': 'p1', 'env': e, 'years': int(Y), 'basis': 'simulated', 'meaning': mean})
            if has(E['rows']['release'], 'd53.' + pk):
                out.append({'id': '%s.%s.%s.change' % (e, Y, k), 'label': lbl + ', change against no programme', 'src': base + '.rows.release.d53.' + pk + '.0', 'unit': 'percentage points', 'f': 's1', 'env': e, 'years': int(Y), 'basis': 'derived',
                            'ci': [base + '.rows.release.d53.' + pk + '.1', base + '.rows.release.d53.' + pk + '.2'], 'meaning': 'The paired difference over the same 500 runs; the 95% interval is beside it. Negative means fewer people below the line.'})
        if 'h1' in E['rows']:
            out.append({'id': '%s.%s.h1pov' % (e, Y), 'label': 'Too little wealth if every Source dollar were backed (H1)', 'src': 'panels.%s.envs.%s.rows.h1.pov' % (Y, e), 'unit': '% of adults at the last year', 'f': 'p1', 'env': e, 'years': int(Y), 'basis': 'simulated',
                        'meaning': 'The optimistic end: if new output backed every dollar the Source pays, prices would not rise from the programme.'})
    for f in out: f['value'] = get(R, f['src'])
    return out

# ---------------------------------------------------------------------------------------------------------------- tables (cells: {"p": [parts], "s": [parts]})
def C(*p, s=None):
    c = {'p': [x for x in p if x is not None]}
    if s: c['s'] = [x for x in s if x is not None]
    return c

def ci(path):
    return [N(path + '.0', 's1'), ' (', N(path + '.1', 's1'), ' to ', N(path + '.2', 's1'), ')']

def rel_table(R, Y):
    P = R['panels'][Y]; rows = []
    new = 'pLevEndMed' in P['envs']['ref']['rows']['release']
    for e, en in ENVS:
        b = 'panels.%s.envs.%s' % (Y, e); r = b + '.rows.release'
        lev = C(N(r + '.pLevEndMed', 'lev'), s=['10th–90th percentile ', N(r + '.pLevEndP10', 'lvn'), '–', N(r + '.pLevEndP90', 'lvn'), '; mean ', N(r + '.pLevEnd', 'lvn')]) if new else C(N(r + '.pLev20', 'lev'))
        rows.append([C(en), C(N(r + '.bOAPy', 'p1'), ' vs ', N(b + '.base.bOAPy', 'p1')), C(N(r + '.fgt0PY', 'p1'), ' vs ', N(b + '.base.fgt0PY', 'p1')), C(N(r + '.pov', 'p1'), ' vs ', N(b + '.base.pov', 'p1')),
                     C(N(r + '.infl', 'p1')), lev, C(N(b + '.rows.h1.pov', 'p1')), C(N(r + '.cost', 'usd'))] +
                    ([C(N(r + '.hhCostKidPY', 'p1'), ' vs ', N(b + '.base.hhCostKidPY', 'p1'), s=ci(r + '.d53.hhCostKidPY'))] if kids(R) else []))
    return {'id': 'rel-t' + Y, 'title': 'Main result, %s years (Compassionism vs no programme)' % Y, 'years': int(Y),
            'columns': ['Environment', 'Below 30 days of basic living (BLEI)', 'Below the cost of living', 'Too little wealth, year %s' % Y, 'Programme inflation a year',
                        'Price level at the last year (times today’s)' + (': median over the runs, with the 10th to 90th percentile and the mean' if new else ': mean over the runs'),
                        'Too little wealth if every Source dollar were backed (H1)', 'Cost per adult a year'] + (['Children below the cost of living, and the change (95% interval)'] if kids(R) else []), 'rows': rows}

PAIRED = [('bOAPy', 'dBO', 'Below 30 days of basic living (BLEI)'), ('bNAPy', 'dBN', 'Below 30 days, design-neutral'), ('fgt0PY', 'dF0', 'Below the cost of living'), ('pov', 'dPov', 'Too little wealth at the last year'),
          ('hhCostKidPY', 'd53.hhCostKidPY', 'Children below the cost of living'), ('hhWlthKidEnd', 'd53.hhWlthKidEnd', 'Children in a household with too little wealth, last year')]

def paired_table(R):
    """v5.3 (plan item A5): the paired effect run by run, for the main row: the mean of the per-run differences with its 95% interval, the share of runs in which the
    programme does better and worse, and the spread of the differences (10th, 50th, 90th percentile)"""
    if not has(R, 'panels.20.envs.ref.rows.release.paired'): return None
    rows = []
    for Y in ('20', '40'):
        if Y not in R['panels']: continue
        for e, en in ENVS:
            r = 'panels.%s.envs.%s.rows.release' % (Y, e)
            if not has(R, r + '.paired'): continue
            Pr = get(R, r + '.paired')
            for k, dk, lbl in PAIRED:
                if k not in Pr or not has(R, r + '.' + dk): continue
                q = r + '.paired.' + k
                rows.append([C(Y), C(en), C(lbl), C(*ci(r + '.' + dk)), C(N(q + '.better', 'p1')), C(N(q + '.worse', 'p1')), C(N(q + '.p10', 's1'), ' / ', N(q + '.p50', 's1'), ' / ', N(q + '.p90', 's1'))])
    return {'id': 'rel-paired', 'title': 'Run by run: how often the programme does better than no programme on the same draws', 'filter': {'years': 0, 'env': 1},
            'columns': ['Years', 'Environment', 'Measure (lower is better)', 'Mean change, points (95% interval)', 'Runs in which the programme does better', 'Runs in which it does worse', 'Change in the 10th / middle / 90th run, points'], 'rows': rows}

TG_MEASURES = [('fpl', 'Below the US official poverty line (money income)', 'under 2% (from about 12%)', 'p1', 'pov'), ('fplX', 'Below the poverty line, Supplemental-style resources', 'under 2%', 'p1', 'pov'),
               ('bO', 'Below 30 days of basic living (BLEI, BLEI paper)', 'under 2%', 'p1', 'pov'), ('bN', 'Below 30 days of basic living (design-neutral)', 'under 2%', 'p1', 'pov'),
               ('f0', 'Below the cost of living', 'under 2%', 'p1', 'pov'), ('pov', 'Too little wealth', 'under 2%', 'p1', 'pov'), ('ep', 'Unhoused (extreme poverty)', 'under 2%', 'p2', 'pov'),
               ('giniD', 'Gini of disposable income', '0.25 to 0.30 (from 0.48)', 'n3', 'gini'), ('giniX', 'Gini of income counting price cuts', '0.25 to 0.30', 'n3', 'gini'), ('giniW', 'Gini of wealth (debts as zero)', '0.25 (BLEI paper)', 'n3', 'giniW')]

def verdict(g, kind):
    if kind == 'pov': return 'met' if g < 2 else 'not met'
    near = abs(g - 0.25) < 0.002 or (kind == 'gini' and abs(g - 0.30) < 0.002)
    if kind == 'giniW': v = 'at or below 0.25' if g <= 0.25 else 'above 0.25'
    else: v = 'at or below 0.25' if g <= 0.25 else 'between 0.25 and 0.30' if g <= 0.30 else 'above 0.30'
    return v + (' (on the line: within 0.002)' if near else '')

def targets_table(R):
    rows = []
    for Y in ('20', '40'):
        if Y not in R['panels']: continue
        for e, en in ENVS:
            E = R['panels'][Y]['envs'][e]
            if 'rep' not in E['rows']['release']: return None
            b = 'panels.%s.envs.%s' % (Y, e)
            for k, lbl, tgt, f, kind in TG_MEASURES:
                cell = lambda t: C(N('%s.rows.release.rep.%s.%s' % (b, t, k), f), ' vs ', N('%s.base.rep.%s.%s' % (b, t, k), f), s=[verdict(E['rows']['release']['rep'][t][k], kind)])
                rows.append([C(Y), C(en), C(lbl), C(tgt), cell('y7'), cell('end')])
    return {'id': 'rel-tg', 'title': 'Against the Hub’s own targets: Year 7 and the last year', 'filter': {'years': 0, 'env': 1},
            'columns': ['Years', 'Environment', 'Measure (share of adults that year)', 'Hub target', 'Year 7: Compassionism vs no programme', 'Last year: Compassionism vs no programme'], 'rows': rows}

def fixed_table(R):
    rows = []
    for Y in ('20', '40'):
        for e, en in ENVS:
            E = R['panels'][Y]['envs'][e]
            if 'rep' not in E['rows']['release']: return None
            b = 'panels.%s.envs.%s' % (Y, e); r = b + '.rows.release'
            rows.append([C(Y), C(en), C(N(r + '.rep.end.pov', 'p1'), ' vs ', N(r + '.rep.end.povNom', 'p1'), s=['no programme ', N(b + '.base.rep.end.pov', 'p1'), ' vs ', N(b + '.base.rep.end.povNom', 'p1')]),
                         C(N(r + '.bOAPy', 'p1'), ' vs ', N(r + '.rep.py.bONom', 'p1'), s=['no programme ', N(b + '.base.bOAPy', 'p1'), ' vs ', N(b + '.base.rep.py.bONom', 'p1')]),
                         C(N(r + '.rep.end.fpl', 'p1'), ' vs ', N(r + '.rep.end.fplNom', 'p1'), s=['no programme ', N(b + '.base.rep.end.fpl', 'p1'), ' vs ', N(b + '.base.rep.end.fplNom', 'p1')])])
    return {'id': 'rel-fx', 'title': 'Poverty lines moved with prices against lines fixed in dollars', 'filter': {'years': 0, 'env': 1},
            'columns': ['Years', 'Environment', 'Too little wealth at the last year: moved with prices vs fixed', 'Below 30 days of basic living over the run (BLEI paper): moved vs fixed', 'Below the official poverty line at the last year: moved vs fixed'], 'rows': rows}

READINGS = ['release', 'h1', 'face', 'tax', 'cost', 'cap5', 'all', 'free', 'standins', 's30', 'v422', 'sav', 'sav0', 'idx', 'h1idx', 'h1both', 'age', 'agenc', 'agenone', 'agepia', 'fixw', 'fixr', 'fixs', 'fixm', 'fixall', 'mid', 'midlo', 'midhi', 'slack', 'slacku6',
            'hcap', 'hcaphi', 'rev5', 'rev10', 'rev20', 'rev20n', 'giftrun', 'progtax', 'landtax']
OLD_READINGS = ['release', 'h1', 'face', 'tax', 'cost', 'cap5', 's30', 'all', 'free', 'standins', 'v422']
READINGS53 = ['release', 'v52', 'adults', 'core', 'indiv', 'cb0', 'cb50', 'wmodel', 'nosg', 'shock50', 'fbs50', 'h1', 'face', 'cost', 'cap5', 'tax', 'all', 'free', 'standins', 'v422', 'sav', 'sav0', 'idx', 'h1idx',
              'age', 'agenone', 'agepia', 'ageleave', 'agecps', 'fixr', 'fixs', 'fixm', 'fixall', 'mid', 'midlo', 'midhi', 'slack', 'hcap', 'hcaphi', 'rev10', 'rev20n', 'giftrun', 'progtax', 'landtax']  # the page's order (index.html ORDER)
BASE_WORD = {'ag': 'ageing rule', 'lt': 'US-data reading', 'sv': 'savings rule', 'b52': 'population as in v5.2', 'badults': 'adults living alone', 'bindiv': 'money kept by each adult',
             'bwmodel': 'starting savings', 'bnosg': 'full-cost spending', 'bshock50': 'linked income swings'}  # index.html relBaseWord

def base_word(k):
    if k in BASE_WORD: return BASE_WORD[k]
    return BASE_WORD.get(k[:2], 'same rule')

def note_cell(r, p):
    if r.get('svInt') is not None: return C('interest paid ', N(p + '.svInt', 'usd'), ' per adult a year (today’s dollars), ', N(p + '.svIntR', 'usd'), ' of it above inflation')
    if r.get('agRet') is not None: return C(N(p + '.agRet', 'p1'), ' of adults retired at the last year; mean age ', N(p + '.agAge', 'n1'))
    if r.get('taxCover') is not None: return C('the tax takes ', N(p + '.taxAvg', 'p1'), ' of wages and pays ', N(p + '.taxCover', 'p1'), ' of the cost', '' if r['taxCover'] >= 99.5 else '; the Source pays the rest as new money')
    if r.get('rvX') is not None: return C('unearned pay not caught ', N(p + '.rvX', 'usd'), ', pay clawed back by audits ', N(p + '.rvC', 'usd'), ', per adult a year (today’s dollars)')
    if r.get('hcM') is not None: return C('rents rise ', N(p + '.hcM', 'p1'), ' on average where the mark-up applies')
    if r.get('mlNT') is not None: return C('wages added by putting idle workers to work: ', N(p + '.mlNT', 'usd'), ' per adult a year (today’s dollars)')
    if r.get('bkPY') is not None: return C(N(p + '.bkA', 'p1'), ' of the Source’s payout backed by new output; the payout is ', N(p + '.bkPY', 'p1'), ' of earned income')
    return C('')

def readings_table(R):
    rows = []; v52 = 'sav' in R['panels']['20']['envs']['ref']['rows']; k53 = kids(R)
    keys = READINGS53 if k53 else READINGS if v52 else OLD_READINGS
    for Y in ('20', '40'):
        if Y not in R['panels']: continue
        for e, en in ENVS:
            E = R['panels'][Y]['envs'][e]
            for k in keys:
                r = E['rows'].get(k)
                if not r: continue
                p = 'panels.%s.envs.%s.rows.%s' % (Y, e, k)
                bp = 'panels.%s.envs.%s.%s' % (Y, e, ('bases.' + r['vsBase']) if r.get('vsBase') else 'base')
                vs = ['against no programme with the same ' + base_word(r['vsBase'])] if r.get('vsBase') else None
                kc = ([C(*ci(p + '.d53.hhCostKidPY')) if has(r, 'd53.hhCostKidPY') else C('–')] if k53 else [])
                rows.append([C(Y), C(en), C(r['label'], s=vs), C(N(p + '.pov', 'p1'), ' vs ', N(bp + '.pov', 'p1'), s=ci(p + '.dPov')), C(*ci(p + '.dF0')), C(*ci(p + '.dBO'))] + kc +
                            [C(N(p + '.infl', 'p1')), C(N(p + '.cost', 'usd')), note_cell(r, p)])
    return {'id': 'rel-v53' if k53 else 'rel-v52' if v52 else 'rel-readings', 'title': 'The main row and every reading beside it', 'filter': {'years': 0, 'env': 1},
            'columns': ['Years', 'Environment', 'Reading', 'Too little wealth at the last year, and the change (95% interval)', 'Below the cost of living, change', 'Below 30 days of basic living (BLEI), change'] +
                       (['Children below the cost of living, change'] if k53 else []) + ['Programme inflation a year', 'Cost per adult a year', 'Note'], 'rows': rows}

HH_ROWS = [  # v5.3 (B8): the households-and-children table and chart (site/findings.js HHM): group, label, panel key
    ('Children', 'Below the cost of living', 'hhCostKidPY'), ('Children', 'Below 30 days of basic living', 'hhBleiKidPY'), ('Children', 'Too little household wealth, last year', 'hhWlthKidEnd'),
    ('Everyone (adults and children)', 'Below the cost of living', 'hhCostPY'), ('Everyone (adults and children)', 'Too little household wealth, last year', 'hhWlthEnd'),
    ('Below the cost of living, by household', 'Single adults', 'hhCost_sg'), ('Below the cost of living, by household', 'Single parents and their children', 'hhCost_sp'),
    ('Below the cost of living, by household', 'Couples without children', 'hhCost_cn'), ('Below the cost of living, by household', 'Couples with children, and children', 'hhCost_ck'),
    ('Income lost to rent and interest', 'Measured from payments (EDC), share of income', 'edcM'), ('Income lost to rent and interest', 'The earlier engine\u2019s design target proxy', 'edcProxy')]

def hh_table(R):
    if not kids(R): return None
    rows = []
    for Y in ('20', '40'):
        if Y not in R['panels']: continue
        for e, en in ENVS:
            E = R['panels'][Y]['envs'][e]; b = 'panels.%s.envs.%s' % (Y, e); r = b + '.rows.release'
            for g, lbl, k in HH_ROWS:
                if k not in E['rows']['release']: continue
                d = C(*ci(r + '.d53.' + k)) if has(E['rows']['release'], 'd53.' + k) else C('–')
                rows.append([C(Y), C(en), C(g), C(lbl), C(N(r + '.' + k, 'p1'), ' vs ', N(b + '.base.' + k, 'p1')) if k in E['base'] else C(N(r + '.' + k, 'p1')), d])
    return {'id': 'rel-hh', 'title': 'Households and children: Compassionism against no programme', 'filter': {'years': 0, 'env': 1},
            'columns': ['Years', 'Environment', 'Who', 'Measure', 'Compassionism vs no programme', 'Change, points (95% interval)'], 'rows': rows}

ATTRIB_LABELS = {'xRelief': 'without the BU allowance (no BU are issued, so none buy essentials, expire or convert)',
                 'xProj': 'without project hiring (expired BU fund projects by the earlier allocation rule instead)',
                 'xSplit': 'without the premium split (the premium is paid to every adult in proportion to wages, the earlier rule)'}

AT_K = [('fgt0PY', 'Below the cost of living (adult-years)'), ('pov', 'Too little wealth at the last year (adults)'), ('bOAPy', 'Below 30 days of basic living (adult-years)'), ('hhCostKidPY', 'Children below the cost of living'),
        ('endoAnn', 'Programme inflation a year'), ('cost', 'Cost per adult a year')]

def attrib_table(R):
    A = R.get('attrib')
    if not A: return None
    rows = []
    for e, en in ENVS:
        if e not in A: continue
        p = 'attrib.%s' % e
        cell = lambda q, k: C(*([N(q + '.%s.0' % k, 'usd'), ' (', N(q + '.%s.1' % k, 'usd'), ' to ', N(q + '.%s.2' % k, 'usd'), ')'] if k == 'cost' else ci(q + '.' + k)))
        rows.append([C(en), C('The whole programme (every part, against no programme)')] + [cell(p + '.whole', k) for k, _ in AT_K])
        for j, o in A[e]['parts'].items():
            rows.append([C(en), C(o['label'].replace('without ', 'What it adds: ', 1))] + [cell(p + '.parts.' + j, k) for k, _ in AT_K])
        rows.append([C(en), C('Interaction (the whole minus the sum of the parts)')] + [C(N(p + '.interaction.' + k, 'usd' if k == 'cost' else 's1')) for k, _ in AT_K])
    return {'id': 'rel-attrib', 'title': 'What each part of the design does (the main row against the main row without that part, paired, %s years)' % A['ref']['_meta']['years'], 'filter': {'env': 0},
            'columns': ['Environment', 'Part'] + [l + ', change in points' if k not in ('cost',) else l + ', change in dollars' for k, l in AT_K], 'rows': rows}

US_ROWS = [  # label, US figure text parts (fn of the release), model path suffix (relative to us.ENV.rows.none), format, where the gap comes from
    ('Below the official poverty line (money income)', lambda u: ['4.3% of workers; 9.2% of people 18–64; 19.0% of people living alone or with non-relatives; 10.2% of everyone (2025)'], 'fpl.%s', 'p1',
     'The model’s adults all work and live alone, with no children and no one out of work, so the like-for-like US figure is workers’; the first year matches it.'),
    ('Below the line on Supplemental-style resources', lambda u: ['7.1% of workers; 12.3% of people 18–64; 13.1% of everyone'], 'spm.%s', 'p1',
     'With no programme the model has no taxes or transfers in resources (taxes and medical costs are in its cost of living), so this equals the line above.'),
    ('Gini of income', lambda u: ['0.448 after tax, 0.490 before (households)'], 'giniD.%s', 'n3',
     'Wages are drawn with a narrow spread (0.5 in logs; a Gini of 0.28). The wage-spread reading (0.8617, the SCF group’s wage Gini) gives about 0.46.'),
    ('Gini of wage income (comparison group)', lambda u: [N('us.ref.us.scf.wageGini', 'n3')], 'wealth.%s.wageGini', 'n3', 'As above.'),
    ('Median savings (net worth)', lambda u: [N('us.ref.us.scf.median', 'usd'), ' (comparison group)'], 'wealth.%s.median', 'usd',
     'Starting savings are drawn lognormal (median $36,316), not from the survey, and do not depend on wages; the savings reading draws them from the survey and links them to wages.'),
    ('Share in debt (net worth below zero)', lambda u: [N('us.ref.us.scf.neg', 'p1')], 'wealth.%s.neg', 'p1',
     'In the model everyone pays the full living-wage basket ($49,370), which two in three adults earn less than (the model’s median wage is $39,945, the survey group’s $54,698), so many run their savings into debt; in the US people with less income spend less. The largest gap; the wage-median reading narrows it, and no reading here closes it.'),
    (('Share with net wealth under ', N('inputs.wealthLine', 'usd')), lambda u: [N('us.ref.us.scf.below25k', 'p1')], 'wealth.%s.below25k', 'p1', 'As above.'),  # v5.2.2: the line from the data (A3); see US_CUT
    ('Gini of wealth (debts kept)', lambda u: [N('us.ref.us.scf.giniKept', 'n3')], 'wealth.%s.giniKept', 'n3',
     'The lognormal start has a thinner top than the survey; debts widen the spread as the run goes on. With debts kept the Gini can pass 1 when many are in debt (Adverse).'),
    ('Leaving poverty in the first year of a spell', lambda u: [N('us.ref.us.psid.exit1', 'n2'), ' (PSID)'], 'spells.fpl.exit1', 'n2',
     'Spell figures use every year of the run, so they appear in the last-year columns. In the model poverty comes from year-to-year swings in pay around a steady wage path, so spells are short and people move in and out often; long US spells come from not working, disability and changes in a household, which the model does not have.'),
    ('Leaving poverty in the second year', lambda u: [N('us.ref.us.psid.exit2', 'n2')], 'spells.fpl.exit2', 'n2', 'As above.'),
    ('Leaving poverty after five years or more', lambda u: ['0.20 or less'], 'spells.fpl.exit5', 'n2', 'As above (few spells reach five years in the model).'),
    ('Back in poverty after one year out', lambda u: [N('us.ref.us.psid.reentry1', 'n3')], 'spells.fpl.reentry1', 'n2', 'As above.')]

US_CUT = 25000  # the cut at which dev/tools/us_check.js counts the model's adults and sources/scf_singles.py tabulates the SCF share ("below25k")

US_TYPES = [('all', 'All households'), ('coupleKids', 'Couples with children'), ('coupleNoKids', 'Couples without children'), ('singleParent', 'Single parents'), ('single', 'Single adults')]
US_ROWS53 = [  # v5.3: the yardstick with households (us_check.js --v53); label, US figure parts, model path suffix (relative to us.ENV.rows.none, %s = y0/y7/end), format, why
    ('Below the official poverty line, everyone (household thresholds)', lambda u: ['10.2% of everyone; 9.2% of people 18–64 (2025)'], 'hh.fpl.%s', 'p1',
     'Every household in the model starts with a working adult and none has a retiree in the main reading, so it sits below the national figure, which counts households with no earner. Not measured in the first year.'),
    ('Children below the official poverty line', lambda u: ['not compared (no figure in the sources used here)'], 'hh.fplKid.%s', 'p1', 'Shown for the record.'),
    ('Gini of income (adults)', lambda u: ['0.448 after tax, 0.490 before (households)'], 'giniD.%s', 'n3',
     'Wages are drawn with a narrow spread (0.5 in logs; a Gini of 0.28). The wage-spread reading gives a figure near the US one.'),
    ('Leaving poverty in the first year of a spell', lambda u: [N('us.ref.us.psid.exit1', 'n2'), ' (PSID)'], 'spells.fpl.exit1', 'n2',
     'Spell figures use every year of the run, so they appear in the last-year columns. In the model poverty comes from year-to-year swings in pay around a steady wage path, so spells are short; long US spells come from not working, disability and changes in a household, which the main reading does not have.'),
    ('Back in poverty after one year out', lambda u: [N('us.ref.us.psid.reentry1', 'n3')], 'spells.fpl.reentry1', 'n2', 'As above.')]

def us_tables53(R):
    rows = []
    for lbl, us, suf, f, why in US_ROWS53:
        n = R['us']['ref']['rows']['none']
        if '%s' in suf:
            m = C(*sum([[N('us.ref.rows.none.' + suf % t, f) if has(n, suf % t) else '–', ' / ' if t != 'end' else None] for t in ('y0', 'y7', 'end')], []))
            a = C(N('us.adv.rows.none.' + suf % 'end', f))
        else:
            m = C('– / – / ', N('us.ref.rows.none.' + suf, f)); a = C(N('us.adv.rows.none.' + suf, f))
        rows.append([C(lbl), C(*us(R)), m, a, C(why)])
    t1 = {'id': 'rel-us', 'title': 'The no-programme run against US data', 'columns': ['Measure', 'US figure', 'Model, no programme, Reference: first year / Year 7 / year 20', 'Adverse, year 20', 'Where the gap comes from'], 'rows': rows}
    rows3 = []
    for k, lbl in US_TYPES:
        p = 'us.ref.rows.none.hh.wealth'
        rows3.append([C(lbl), C(N('us.ref.us.scfHH.%s.neg' % k, 'p1'), ' (', N('us.ref.us.scfHH.%s.median' % k, 'usd'), ')')] +
                     [C(N('%s.%s.%s.neg' % (p, t, k), 'p1'), ' (', N('%s.%s.%s.median' % (p, t, k), 'usd'), ')') for t in ('y0', 'y7', 'end')] +
                     [C(N('us.adv.rows.none.hh.wealth.end.%s.neg' % k, 'p1'), ' (', N('us.adv.rows.none.hh.wealth.end.%s.median' % k, 'usd'), ')')])
    t3 = {'id': 'rel-us3', 'title': 'Households\u2019 wealth against the survey, by type: share in debt (median net worth)',
          'columns': ['Household', 'US (SCF 2022, families with a head aged 25–66 and wages)', 'Model, no programme, Reference: first year', 'Year 7', 'Year 20', 'Adverse, year 20'], 'rows': rows3}
    rows2 = []
    for k, lbl in [('none', 'As modelled (households, survey wealth, graded spending)'), ('v52', 'v5.2\u2019s population: adults alone, the model\u2019s own savings draw, everyone paying the full basket'), ('ltr', 'Automation risk linked to wages'),
                   ('lts', 'Wages spread as in the survey'), ('ltm', 'Wages centred on the survey’s median'), ('lta', 'All three'), ('ag', 'Ageing: children grow up and are born; estates pass on')]:
        if k not in R['us']['ref']['rows'] or k not in R['us']['adv']['rows']: continue
        p = 'us.ref.rows.' + k
        rows2.append([C(lbl), C(N(p + '.wealth.y0.median', 'usd'), ' / ', N(p + '.wealth.y7.median', 'usd')), C(N(p + '.wealth.y7.neg', 'p1')), C(N(p + '.wealth.y0.giniKept', 'n3')), C(N(p + '.giniD.y7', 'n3')),
                      C(N(p + '.fpl.y7', 'p1'), ' / ', N('us.adv.rows.%s.fpl.end' % k, 'p1')), C(N(p + '.spells.fpl.exit1', 'n2'))])
    t2 = {'id': 'rel-us2', 'title': 'The readings that change a known choice, no programme only (adults)', 'columns': ['Reading', 'Median savings per adult: first year / Year 7', 'In debt, Year 7', 'Wealth Gini, first year', 'Income Gini, Year 7', 'Below the poverty line: Year 7 / Adverse year 20', 'Leaving poverty in a spell’s first year'], 'rows': rows2}
    return [t1, t3, t2]

def us_tables(R):
    if not R.get('us'): return []
    if kids(R) and R['us']['ref']['rows']['none'].get('hh'): return us_tables53(R)
    if R['inputs']['wealthLine'] != US_CUT: sys.exit('release_data: the wealth line (%s) is not the cut the US-data check used (%s): rerun dev/tools/us_check.js and the SCF tabulation at the new line' % (R['inputs']['wealthLine'], US_CUT))
    rows = []
    for lbl, us, suf, f, why in US_ROWS:
        if '%s' in suf:
            m = C(*sum([[N('us.ref.rows.none.' + suf % t, f), ' / ' if t != 'end' else None] for t in ('y0', 'y7', 'end')], []))
            a = C(N('us.adv.rows.none.' + suf % 'end', f))
        else:
            m = C('– / – / ', N('us.ref.rows.none.' + suf, f)); a = C(N('us.adv.rows.none.' + suf, f))
        rows.append([C(*lbl) if isinstance(lbl, tuple) else C(lbl), C(*us(R)), m, a, C(why)])
    t1 = {'id': 'rel-us', 'title': 'The no-programme run against US data', 'columns': ['Measure', 'US figure', 'Model, no programme, Reference: first year / Year 7 / year 20', 'Adverse, year 20', 'Where the gap comes from'], 'rows': rows}
    rows2 = []
    for k, lbl in [('none', 'As modelled'), ('ltw', 'Savings from the survey, linked to wages'), ('ltr', 'Automation risk linked to wages'), ('lts', 'Wages spread as in the survey'), ('ltm', 'Wages centred on the survey’s median'), ('lta', 'All four'), ('ag', 'Adults who age, retire and are replaced')]:
        if k not in R['us']['ref']['rows'] or k not in R['us']['adv']['rows']: continue
        p = 'us.ref.rows.' + k
        rows2.append([C(lbl), C(N(p + '.wealth.y0.median', 'usd'), ' / ', N(p + '.wealth.y7.median', 'usd')), C(N(p + '.wealth.y7.neg', 'p1')), C(N(p + '.wealth.y0.giniKept', 'n3')), C(N(p + '.giniD.y7', 'n3')),
                      C(N(p + '.fpl.y7', 'p1'), ' / ', N('us.adv.rows.%s.fpl.end' % k, 'p1')), C(N(p + '.spells.fpl.exit1', 'n2'))])
    t2 = {'id': 'rel-us2', 'title': 'The readings that change a known choice, no programme only', 'columns': ['Reading', 'Median savings: first year / Year 7', 'In debt, Year 7', 'Wealth Gini, first year', 'Income Gini, Year 7', 'Below the poverty line: Year 7 / Adverse year 20', 'Leaving poverty in a spell’s first year'], 'rows': rows2}
    return [t1, t2]

BK = ['a0', 'a25', 'a50', 'a75', 'a100']

def backing_table(R):
    if not R.get('backing'): return None
    rows = []
    for k in BK:
        rows.append([C('Release row' if k == 'a0' else 'H1' if k == 'a100' else ''), C(N('backing.envs.ref.rows.%s.a' % k, 'n2'))] +
                    [C(*ci('backing.envs.%s.rows.%s.dPov' % (e, k))) for e, _ in ENVS] + [C(N('backing.envs.%s.rows.%s.infl' % (e, k), 'p1')) for e, _ in ENVS])
    return {'id': 'bs', 'title': 'The backing-share sweep: change in too little wealth and programme inflation, by the share a of the Source’s payout backed by new output',
            'columns': ['Reading', 'Backed share a', 'Reference: change in too little wealth, points (95% interval)', 'Adverse', 'Stress Test', 'Reference: programme inflation a year', 'Adverse', 'Stress Test'], 'rows': rows}

# ---------------------------------------------------------------------------------------------------------------- derived figures and texts
def crossing(pts):
    for (a0, y0), (a1, y1) in zip(pts, pts[1:]):
        if y0 > 0 >= y1 or y0 < 0 <= y1:
            return a0 + (a1 - a0) * (0 - y0) / (y1 - y0)
    return None

GINI_K = [('giniD', 'Gini of disposable income'), ('giniX', 'Gini of income counting price cuts'), ('giniW', 'Gini of wealth (debts counted as zero)')]

def gini_finite(R):
    """v5.2.2 (audit A6): the Gini of the simulated adults themselves, without the n/(n - 1) correction the v5.2 panels apply to every Gini. The mean over
    the runs is linear, so it is the published figure x (n - 1)/n exactly, up to the panel's four decimals. None for a panel without the correction."""
    n = R['meta']['agents']; out = {}
    f = lambda g: round(g * (n - 1) / n, 4)
    for Y, P in R['panels'].items():
        if not (P['_meta'].get('v52') or {}).get('report', {}).get('giniNN1'): continue
        for e, _ in ENVS:
            if e not in P['envs']: continue
            E = P['envs'][e]
            for run, node in (('release', E['rows']['release']), ('base', E['base'])):
                d = {k: f(node[k]) for k in ('giniD', 'giniX') if k in node}
                for t in ('y7', 'end'):
                    if node.get('rep') and t in node['rep']: d[t] = {k: f(node['rep'][t][k]) for k in ('giniD', 'giniX', 'giniW', 'giniWN') if k in node['rep'][t]}
                out.setdefault(Y, {}).setdefault(e, {})[run] = d
    if not out: return None
    return {'n': n, 'how': 'The Gini of the %d simulated adults themselves (a finite-population figure): each published Gini (the sample Gini x n/(n - 1), n = %d) multiplied by (n - 1)/n. '
            'Derived from the panels, no new runs; it can differ from a direct computation in the fourth decimal because the panels keep four.' % (n, n), 'panels': out}

def gini_figures(R, Y):
    """catalogue: each headline Gini (Year 7 and the last year, with and without the programme) as published, and beside it the derived Gini of the adults themselves"""
    G = (R.get('derived') or {}).get('giniFinite')
    if not G or Y not in G['panels']: return []
    out = []
    for e, en in ENVS:
        if e not in G['panels'][Y]: continue
        for run, who in (('release', 'with Compassionism'), ('base', 'no programme')):
            src = 'panels.%s.envs.%s.%s.rep' % (Y, e, 'rows.release' if run == 'release' else 'base')
            for t, tl in (('y7', 'Year 7'), ('end', 'the last year')):
                for k, lbl in GINI_K:
                    if k not in G['panels'][Y][e][run].get(t, {}): continue
                    base = {'unit': 'Gini (0 = equal, 1 = one adult has everything)', 'f': 'n4', 'env': e, 'years': int(Y)}
                    out.append(dict(base, id='%s.%s.%s.%s.%s' % (e, Y, k, t, 'with' if run == 'release' else 'without'), label='%s, %s, %s' % (lbl, tl, who), src='%s.%s.%s' % (src, t, k), basis='simulated',
                                    meaning=render_plain(R, 'As published: the sample Gini of the {{meta.agents|int}} adults multiplied by n/(n − 1), which estimates the Gini of the population the adults are drawn from.')))
                    out.append(dict(base, id='%s.%s.%s.%s.%s.finite' % (e, Y, k, t, 'with' if run == 'release' else 'without'), label='%s, %s, %s: the %d adults themselves, uncorrected' % (lbl, tl, who, G['n']),
                                    src='derived.giniFinite.panels.%s.%s.%s.%s.%s' % (Y, e, run, t, k), basis='derived',
                                    meaning=render_plain(R, 'The Gini of the {{meta.agents|int}} simulated adults themselves, without the small-sample correction: the published figure multiplied by (n − 1)/n.')))
    for f in out: f['value'] = get(R, f['src'])
    return out

def derived(R):
    D = {}
    G = gini_finite(R)
    if G: D['giniFinite'] = G
    if R.get('backing'):
        for e, en in ENVS:
            pts = [(R['backing']['envs'][e]['rows'][k]['a'], R['backing']['envs'][e]['rows'][k]['dPov'][0]) for k in BK]
            c = crossing(pts)
            D['cross_' + e] = {'v': None if c is None else round(c, 4), 'how': 'the share a at which the change in too little wealth against no programme crosses zero, by linear interpolation between the five points of the backing sweep (' + en + ')'}
    return D

def texts(R):
    m = R['meta']; Tx = {}; K53 = kids(R)
    Tx['lede'] = ('The same {{meta.agents|int}} simulated adults' + (' and their children, living in households as US adults do,' if K53 else '') + ' are followed for 20 or 40 years, once with Compassionism and once with no programme, in three environments; every figure is an average over {{meta.seeds|int}} paired runs. '
                  'These pages show what the model’s assumptions imply, not a forecast. The model has not yet been reviewed by an independent economist.')
    Tx['results.lead'] = ('Compassionism as specified on the Research Hub, every mechanism in, against no programme. Paid for by a Source that issues the BU; in the cautious main reading, what the Source pays out is new money except what new output backs. '
                          'Each environment is a different world the same adults live in: Reference (' + ENV_DESC['ref'] + '), Adverse (' + ENV_DESC['adv'] + ') and Stress Test (' + ENV_DESC['st'] + ').')
    Tx['results.read'] = ('Each row of the chart is one measure in one environment. The hollow mark is no programme, the filled mark is Compassionism, and the line between them is the change. '
                          'A mark further left means fewer people below the line. All three measures are shares of adults: of adult-years for the first two (averaged over the run), of adults at the last year for the third.')
    Tx['results.limits'] = ('It does not show a forecast: it shows what the model’s rules imply. The cautious main reading treats the Source’s payout as new money; the optimistic end (H1, every dollar backed by new output) is in the table. '
                            'The adults are single and working-age, with no children or households, in one country’s prices and wages (US). In the Adverse and Stress environments more adults end with too little wealth than with no programme, because prices rise and savings in the model earn nothing.')
    if K53:  # plan item B10: so readers do not compare across the break
        Tx['release.changed'] = ('What changed for the figures in v5.3: the adults now live in households with their children, as US adults do; each household starts with the wealth the Federal Reserve\u2019s survey shows for its kind of household; '
                                 'people spend less in a year their income is short; and BU buy the Hub\u2019s full list (transport and childcare included). These change the no-programme run as well as the programme, so v5.3\u2019s figures are not comparable with earlier releases\u2019: compare within a release. '
                                 'v5.2\u2019s main row, run on the v5.3 engine, is shown beside the main result as the reading \u201cv5.2\u2019s main row\u201d.')
        E20 = R['panels']['20']['envs']; w = [en for e, en in ENVS if E20[e]['rows']['release']['pov'] > E20[e]['base']['pov']]
        Tx['results.limits'] = ('It does not show a forecast: it shows what the model’s rules imply. The cautious main reading treats the Source’s payout as new money; the optimistic end (H1, every dollar backed by new output) is in the table. '
                                'The adults live in households as US adults do (single adults, single parents, couples with and without children), in one country’s prices and wages (US). In the main reading nobody ages: children stay children, and couples neither form nor part (the ageing reading lets children grow up, be born and leave home). '
                                + ('More adults end with too little wealth than with no programme in ' + ' and '.join(w) + ' over 20 years, because prices rise with the programme’s new money and savings in the model earn nothing.' if w else
                                   'In every environment fewer adults end with too little wealth than with no programme over 20 years.'))
    if has(R, 'panels.20.envs.ref.rows.release.paired'):
        Tx['results.read'] += (' The table \u201cRun by run\u201d takes each of the {{meta.seeds|int}} runs on its own: the change on the same draws, how often the programme does better or worse than no programme, '
                               'and the change in the 10th, middle and 90th run. In Reference, 20 years, the programme does better on the cost of living in {{panels.20.envs.ref.rows.release.paired.fgt0PY.better|p1}} of the runs '
                               'and on too little wealth in {{panels.20.envs.ref.rows.release.paired.pov.better|p1}}.')
    if 'pLevEndMed' in R['panels']['20']['envs']['ref']['rows']['release']:
        Tx['results.prices'] = ('The price-level column gives the typical run first: the median over the {{meta.seeds|int}} runs, then the 10th to 90th percentile and the mean. The price level compounds, so the mean runs above the typical run, and the gap grows with the horizon. '
                                'Above 1,000 times today’s prices the figure shows the model’s price rule running away (it has no central bank, no interest rate and no protection for savings): a limit of the model, not a forecast.')
    if 'path' in R['panels']['20']['envs']['ref']['rows']['release']:
        parts = []
        for Y in ('20', '40'):
            if Y not in R['panels']: continue
            n = int(R['panels'][Y]['_meta']['years']) - 1
            w = ', '.join('%s %s (%s)' % (en, T('panels.%s.envs.%s.rows.release.path.wageR.%d' % (Y, e, n), 'usd'), T('panels.%s.envs.%s.base.path.wageR.%d' % (Y, e, n), 'usd')) for e, en in ENVS)
            b = ', '.join('%s %s' % (en, T('panels.%s.envs.%s.rows.release.path.buR.%d' % (Y, e, n), 'usd')) for e, en in ENVS)
            parts.append('At year %s a month of the median wage buys %s, and a month of the BU %s.' % (Y, w, b))
        Tx['results.month'] = 'What a month still buys, in today’s dollars (Compassionism; no programme in brackets). ' + ' '.join(parts)
    man = m.get('manifest')
    if man:
        Tx['results.provenance'] = ('Provenance: produced by harness.js at commit <code>%s</code>%s with Node %s; SHA-256 of harness.js as run <code>%s</code>, of the page’s ported release engine <code>%s</code>. '
                                    'The checks confirm that the engine hash equals the page’s. Reproduce: <code>%s</code>, then <code>%s</code>.') % (
            man['commit'], '' if not man.get('dirty') else ' (tracked files differed from it)', man['node'], man['harnessSha256'], man['engineBlockSha256'], esc(m['commands']['20']), esc(m['commands'].get('40', '')))
    Tx['targets.lead'] = ('The Research Hub sets two targets for Year 7 of a programme: a poverty rate under 2% (from about 12%) and a Gini coefficient of 0.25 to 0.30 (from 0.48), in the '
                          '<a href="https://bettertobest.github.io/research-hub/integrated-implementation-roadmap.html" rel="noopener">Integrated Implementation Roadmap</a> (Success Metrics by Year 7; Appendix I); the BLEI paper adds 0.25 as its design target for the spread of wealth.')
    Tx['targets.read'] = ('Each mark is the share of adults below a line in one year: Year 7 (the Hub’s date) and the run’s last year, with Compassionism (filled) and no programme (hollow). The shaded strip is the Hub’s target of under 2%. '
                          'The first measure is the one behind the Hub’s starting point: the US official poverty threshold for one person under 65 ({{inputs.povertyLine2025|usd}} in 2025; Census, quoted by CRS IN12737), moved with prices, against money income before tax (the BU, like food stamps, are not money income). '
                          'The second keeps the same threshold but counts resources closer to the Census Supplemental Poverty Measure (income after the contribution, plus the value of the BU and the price cuts).')
    Tx['targets.limits'] = (('The targets are read on the adults. The model’s adults are working-age and all start with a wage, so its no-programme rate sits below the national 10.2% of 2025: the same definition, a different population. ' if K53 else
                             'The model’s adults are working-age, live alone and all earn wages, with no children, so its no-programme rate sits below the national 10.2% of 2025: the same definition, a different population. ') +
                            'The Hub does not say which measure its rate is, so the 2% line is also read against each of the model’s own measures, which are stricter. The unhoused figure starts from 0.22% at year 0 by construction, so it sits under 2% whatever the programme does. '
                            'The income Gini is the like-for-like figure for the Roadmap’s 0.48 start (the model’s no-programme Gini is already below it); the BLEI paper’s 0.25 is for wealth less a year of extraction costs, which this engine does not model, so the plain wealth Gini (debts counted as zero) is the nearest figure. '
                            'Every Gini carries the small-sample correction (×500/499), and a reading within 0.002 of a line is labelled as on it.')
    Tx['fixed.lead'] = ('The main readings move every line with the price level (the wealth line of {{inputs.wealthLine|usd}}, the 30-day BLEI line and the poverty threshold), so a line means the same living standard every year. '
                        'Held fixed in dollars instead, the lines fall behind prices and the shares read lower.')
    Tx['fixed.read'] = 'For each measure, the filled mark is the share with the line moved with prices (the main reading) and the hollow mark the share with the line fixed in dollars, with Compassionism. The gap is how much of a result depends on keeping the line’s value.'
    Tx['fixed.limits'] = 'A fixed-dollar line is not a better measure: as prices rise it describes a lower and lower standard of living. It is shown so that no one has to take the indexing on trust.'
    if R.get('backing'):
        B = R['backing']['_meta']
        Tx['backing.lead'] = ('The decisive unknown is how much of what the Source pays out new output backs. The main row assumes none of the Source’s net payout is backed by new output (a = 0); H1 assumes all of it is (a = 1). '
                              'This sweeps the share a at 0, 0.25, 0.5, 0.75 and 1 on the same {{backing._meta.seeds|int}} paired runs of {{backing._meta.agents|int}} adults over {{backing._meta.years|int}} years, every other mechanism as in the main row; the two ends are the main row and H1, to the last digit.')
        Tx['backing.read'] = ('Each line is an environment; each point is the change in the share of adults with too little wealth at year {{backing._meta.years|int}} against no programme, with its 95% interval. Above zero means worse than no programme. '
                              'Where the line crosses zero is the share of backing the result needs: Reference ' + ('better than no programme at every point' if R['derived']['cross_ref']['v'] is None else 'about {{derived.cross_ref.v|n2}}') +
                              '; Adverse ' + ('at every point' if R['derived']['cross_adv']['v'] is None else 'about {{derived.cross_adv.v|n2}}') + '; Stress Test ' + ('at every point' if R['derived']['cross_st']['v'] is None else 'about {{derived.cross_st.v|n2}}') + '.')
        if 'mid' in R['panels']['20']['envs']['ref']['rows'] and R['panels']['20']['envs']['ref']['rows']['mid'].get('bkA') is not None:
            Tx['backing.read'] += (' The diamonds are the middle reading (Claude’s reading of the evidence): new output backs the payout up to 8%, 12% or 16% of a year’s earned income, anchored by the Kenya cash-transfer study (Egger, Haushofer, Miguel, Niehaus and Walker, <em>Econometrica</em> 2022); '
                                   'each sits at the share of the payout it actually backs.')
        Tx['backing.limits'] = ('It is a sweep of a design parameter, not a forecast: the Hub does not give the share, and nothing in the model fixes it. Kenya does not set the US number (the transfers were paid once, from outside the area, into villages with idle capacity), so the main row stays at a = 0. '
                                'In the Adverse and Stress environments the right end bends: the BU is indexed to prices only in a year when they rise faster than 5% (the Hub’s rule), so with no programme inflation (a = 1) the BU loses value to the 2% outside inflation; that is a finding about the rule, not a proposal to change it.')
    v52r = 'sav' in R['panels']['20']['envs']['ref']['rows']
    Tx['readings.lead'] = ('Each reading changes one assumption beside the main row, over the same paired runs, and none of them is in the main row.' + (
        ' A reading that changes something outside the design (savings that keep up with prices, ageing, the US-data readings) applies to the no-programme run too, so its change is against no programme with the same rule.' if v52r else ''))
    Tx['readings.read'] = ('Each row is a reading; the mark is the change against no programme in the chosen measure, with its 95% interval, and the vertical line is the main row. A mark left of the main row means the reading helps; right of it, the reading hurts.' +
        (' Rows are grouped: the optimistic end and the middle backing band; savings and the BU; ageing; closer to US data; robustness risks (rent capture, review errors); and other ways to pay.' if v52r else ''))
    if K53:
        Tx['readings.lead'] = ('Each reading changes one assumption beside the main row, over the same paired runs, and none of them is in the main row. The first group undoes, one at a time, each choice v5.3 added to the main row (households, pooling, the child allowance, the wider list of what BU buy, starting wealth from the survey, spending that follows income), and one row undoes them all (v5.2’s main row). '
                               'A reading that changes the population or something outside the design (households, starting wealth, spending, savings that keep up with prices, ageing, the US-data readings) applies to the no-programme run too, so its change is against no programme with the same rule.')
        Tx['readings.read'] = ('Each row is a reading; the mark is the change against no programme in the chosen measure, with its 95% interval, and the vertical line is the main row. A mark left of the main row means the reading helps; right of it, the reading hurts. '
                               'Rows are grouped: v5.3’s new choices; the optimistic end and the middle backing band; savings and the BU; ageing; closer to US data; robustness risks (rent capture, review errors); and other ways to pay.')
        Tx['readings.limits'] = ('Savings that keep up with prices: the model has no bank, so who pays that interest is not modelled. Ageing: couples are fixed for life (nobody new pairs up or separates), so over the years the population drifts from the US mix; retirees are measured against a working-age basket. Rents: the evidence measured vouchers for a minority of renters, an upper-end reading here. '
                                 'Review errors: audits catching half is a design parameter, not in the Hub. The progressive and land taxes are modelling alternatives, not the Hub\u2019s design; the model has no land, so the land tax falls on savings.')
    elif v52r:
        Tx['readings.limits'] = ('Savings that keep up with prices: the model has no bank, so who pays that interest is not modelled. Ageing: the model does not yet report results by age. Rents: the evidence measured vouchers for a minority of renters, an upper-end reading here. '
                                 'Review errors: audits catching half is a design parameter, not in the Hub. The progressive and land taxes are modelling alternatives, not the Hub\u2019s design; the model has no land, so the land tax falls on savings.')
    else:
        Tx['readings.limits'] = 'Each reading changes one assumption at a time; readings are not added together, and none is a forecast.'
    if R.get('us') and K53:
        Tx['us.lead'] = ('The no-programme run is the yardstick for every result, so it is checked against published US figures: poverty (Census Bureau, Poverty in the United States: 2025), income inequality (Census Bureau, Income in the United States: 2025), '
                         'wealth (Federal Reserve, 2022 Survey of Consumer Finances: families with a head aged 25–66 and wages, by type, in 2025 dollars) and how poverty spells end (Panel Study of Income Dynamics, Stevens 1994). '
                         'Households start with the survey’s wealth for their type, so the first year matches it by construction; the check is how the yardstick holds up over the years. No setting was changed to bring a later figure closer.')
        Tx['us.read'] = 'Each pair compares the model’s no-programme run (filled) with the US figure for the closest group (hollow): the share of households in debt by type at Year 7, and the share of people below the official poverty line (Reference). Close marks mean the yardstick matches; far marks are gaps, explained in the table.'
        Tx['us.limits'] = ('Single parents and single adults run into debt far more than in the survey: their living-wage budgets, with childcare for single parents, are far above what the model’s wages pay, and the model’s wages are lower and less spread out than the survey’s. '
                           'Its poverty spells are short because every adult starts with a wage and the main reading has no one out of work for long, no disability and no changes in a household.')
    elif R.get('us'):
        Tx['us.lead'] = ('The no-programme run is the yardstick for every result, so it is checked against published US figures: poverty (Census Bureau, Poverty in the United States: 2025), income inequality (Census Bureau, Income in the United States: 2025), '
                         'wealth (Federal Reserve, 2022 Survey of Consumer Finances: single adults aged 25–66, no children, with wages, in 2025 dollars) and how poverty spells end (Panel Study of Income Dynamics, Stevens 1994). '
                         'No setting was changed to bring a figure closer; where a gap traces to a known choice, a reading beside the main one changes it.')
        Tx['us.read'] = 'Each pair compares the model’s no-programme run (filled) with the US figure for the closest group (hollow), at the model’s first year (Reference). Close marks mean the yardstick matches; far marks are gaps, explained in the table.'
        Tx['us.limits'] = ('The model is far more in debt than US single workers (the largest gap) because everyone pays the full living-wage basket and people with less income do not spend less; its poverty spells are short because nobody is out of work, disabled or in a changing household. '
                           'Its income is more equal than the US because wages are drawn with a narrow spread.')
    if K53:
        Tx['hh.lead'] = ('Children, and everyone in the household, with Compassionism against no programme. A household is poor when its pooled income falls short of its own cost of living: the MIT living-wage basket for its adults and children, childcare included. '
                         'Each child brings a quarter of the adult BU, shared between the household’s adults (Duke’s choice, d167).')
        Tx['hh.read'] = ('Each row is a share of people in a typical year (or at the last year, where it says so). The hollow mark is no programme, the filled mark is Compassionism; a mark further left means fewer people below the line. '
                         'The household rows count everyone in that kind of household, children included. The last two rows are the share of income lost to rent and interest: measured from what people pay, and the earlier engine’s design target proxy, which this release replaces with the measurement.')
        Tx['hh.limits'] = ('In the main reading children stay children and couples neither form nor part; the ageing reading lets children grow up, be born and leave home. Partners are paired at random, not by similar pay. '
                           'Childcare is at MIT’s prices for every child under 13, whether or not a parent stays home. The households are working households: every adult starts with a wage.')
    if R.get('attrib'):
        Tx['attrib.lead'] = ('What each part of the design does on the main row: the main row against the main row without that part, on the same {{attrib.ref._meta.seeds|int}} paired runs over {{attrib.ref._meta.years|int}} years. '
                             'The top row is the whole programme against no programme. Parts work together, so the parts need not add up to the whole; the gap is the interaction, in the table.')
        Tx['attrib.read'] = ('Each row is one part; the mark is how much the main row changes the measure because that part is in it, with its 95% interval. Left of zero means the part lowers the share below the line; right of zero, it raises it. '
                             'A part that pays out more (the BU buying essentials, conversion) can lower poverty and raise prices at once; the table gives each part’s effect on inflation and cost beside its effect on poverty.')
        Tx['attrib.limits'] = ('Removing a part is a reading of what the design would be without it, not a proposal. Each part is removed alone, so a part whose work another part can take over shows a small effect. '
                               'The intervals cover the luck of the draws, not the model’s assumptions, which the readings test.')
    return Tx

STORIES = [  # the explorer's guided reads: id, title, chart kind, tables, required data
    ('results', 'Results by environment and horizon', 'dumbbell', ['rel-t20', 'rel-t40', 'rel-paired']),
    ('hh', 'Households and children', 'hh', ['rel-hh']),
    ('targets', 'Against the Hub’s own targets', 'targets', ['rel-tg']),
    ('fixed', 'Poverty lines fixed in dollars', 'fixed', ['rel-fx']),
    ('backing', 'The decisive unknown: how much of the payout new output backs', 'backing', ['bs']),
    ('readings', 'How far the answer moves: the readings beside the main row', 'readings', ['rel-v53', 'rel-v52', 'rel-readings']),
    ('attrib', 'What each part of the design does', 'attrib', ['rel-attrib']),
    ('us', 'The no-programme run against US data', 'us', ['rel-us', 'rel-us3', 'rel-us2'])]

# ---------------------------------------------------------------------------------------------------------------- assembling a release
def load_json(src, path):
    if src is None:
        p = os.path.join(ROOT, path)
        return json.load(open(p)) if os.path.exists(p) else None
    try:
        return json.loads(subprocess.check_output(['git', 'show', '%s:%s' % (src, path)], cwd=ROOT, stderr=subprocess.DEVNULL))
    except subprocess.CalledProcessError:
        return None

CONST_KEYS = ('POVERTY_LINE', 'POVERTY_THRESHOLD_ONE', 'BLEI_PRECARIOUS_MAX')

def constants(src=None):
    """the constants the pages quote, from dev/runs/constants.json (written by node harness.js constants, v5.2.2); for an earlier tag, which has no such
    file, from that tag's own harness.js CFG (a constant the tag's harness lacks falls back to the current file's, which is said in a warning)"""
    c = load_json(src, 'dev/runs/constants.json')
    if c is not None: return c
    if src is None: sys.exit('release_data: dev/runs/constants.json is missing (run node harness.js constants)')
    import tempfile
    cur = load_json(None, 'dev/runs/constants.json') or {}
    with tempfile.TemporaryDirectory() as d:
        hp = os.path.join(d, 'harness.js')
        open(hp, 'wb').write(subprocess.check_output(['git', 'show', '%s:harness.js' % src], cwd=ROOT))
        js = 'const H=require(process.argv[1]);console.log(JSON.stringify(Object.fromEntries(%s.map(k=>[k,H.CFG[k]]))))' % json.dumps(list(CONST_KEYS))
        got = json.loads(subprocess.check_output(['node', '-e', js, hp], cwd=d, stderr=subprocess.DEVNULL))
    for k in CONST_KEYS:
        if got.get(k) is None: got[k] = cur.get(k); print('release_data: %s has no CFG.%s; using the current value %s' % (src, k, got[k]), file=sys.stderr)
    return got

def build(info, src=None):
    p20 = load_json(src, 'dev/runs/release-panel.json'); p40 = load_json(src, 'dev/runs/release-panel-40.json')
    if p20 is None: sys.exit('release_data: no 20-year panel')
    R = {'schema': 1, 'version': info['version'], 'date': info['date'], 'tag': info['tag'], 'summary': info['summary']}
    if info.get('shownIn'): R['shownIn'] = info['shownIn']
    cmds = {'20': p20['_meta']['command']}
    if p40: cmds['40'] = p40['_meta']['command']
    R['meta'] = {'seeds': p20['_meta']['seeds'], 'agents': p20['_meta']['agents'], 'written': p20['_meta'].get('written'), 'engine': p20['_meta'].get('engine'), 'manifest': p20['_meta'].get('manifest'), 'commands': cmds,
                 'envs': {e: {'name': en, 'about': ENV_DESC[e]} for e, en in ENVS}}
    K = constants(src)  # v5.2.2 (audit A3): the lines come from the harness's CFG (node harness.js constants), not from numbers typed here
    R['inputs'] = {'wealthLine': K['POVERTY_LINE'], 'povertyLine2025': K['POVERTY_THRESHOLD_ONE'], 'bleiDays': K['BLEI_PRECARIOUS_MAX'], 'hubPovertyTarget': 2, 'hubGini': [0.25, 0.30], 'hubGiniStart': 0.48,
                   'sources': {'wealthLine': 'the model’s wealth line (CFG.POVERTY_LINE), moved with prices', 'povertyLine2025': 'US official poverty threshold for one person under 65, 2025 (Census, quoted by CRS IN12737)',
                               'hub': 'Research Hub, Integrated Implementation Roadmap (Success Metrics by Year 7; Appendix I); BLEI paper'}}
    R['panels'] = {'20': p20}
    if p40: R['panels']['40'] = p40
    bk = load_json(src, 'dev/runs/backing-share.json')
    if bk: R['backing'] = bk
    us_r, us_a = load_json(src, 'dev/runs/us-check-ref.json'), load_json(src, 'dev/runs/us-check-adv.json')
    if us_r and us_a: R['us'] = {'ref': us_r, 'adv': us_a}
    at = {e: load_json(src, 'dev/runs/attrib-check-%s.json' % e) for e, _ in ENVS}  # v5.3 (B9): dev/tools/attrib_check.js
    if all(at.values()):
        if len({json.dumps(a['_meta']['manifest'], sort_keys=True) for a in at.values()}) != 1 or any(a['_meta']['seeds'] != p20['_meta']['seeds'] for a in at.values()):
            sys.exit('release_data: the attribution runs are not from one build on the panel\'s seeds')
        for a in at.values():  # the parts' labels as harness.js now words them (two were corrected after the 500-seed runs; the configurations are unchanged: DECISIONS Session 39, B9)
            for j, o in a['parts'].items():
                if j in ATTRIB_LABELS: o['label'] = ATTRIB_LABELS[j]
        R['attrib'] = at
    R['derived'] = derived(R)
    R['figures'] = catalogue(R, '20') + (catalogue(R, '40') if p40 else []) + gini_figures(R, '20') + (gini_figures(R, '40') if p40 else [])
    tables = [rel_table(R, '20')] + ([rel_table(R, '40')] if p40 else []) + [t for t in [paired_table(R)] if t] + [t for t in [targets_table(R) if p40 else None, fixed_table(R) if p40 else None, hh_table(R), readings_table(R), attrib_table(R), backing_table(R)] if t] + us_tables(R)
    R['tables'] = tables
    R['text'] = texts(R)
    have = {t['id'] for t in tables}
    R['stories'] = [{'id': i, 'title': t, 'chart': k, 'tables': [x for x in tb if x in have]} for i, t, k, tb in STORIES if any(x in have for x in tb)]
    R['explore'] = None
    return R

def explore_files(R):
    """the lazily loaded extras from dev/runs/explore-ENV-YRS.json (current release only)"""
    out = {}; idx = {'bands': {}, 'lives': {}}
    for Y in ('20', '40'):
        bands = {'_meta': None, 'envs': {}}
        for e, _ in ENVS:
            p = os.path.join(ROOT, 'dev', 'runs', 'explore-%s-%s.json' % (e, Y))
            if not os.path.exists(p): return None, None
            X = json.load(open(p))
            m = X['_meta']
            if m['seeds'] != R['meta']['seeds'] or 'NOT COMPARED' in m.get('selfCheck', ''): sys.exit('release_data: %s was not made on the panel\'s seeds' % p)
            meta = {k: m[k] for k in ('what', 'seeds', 'lifeSeed', 'rows', 'manifest', 'flags', 'selfCheck')}
            meta['commands'] = 'node dev/tools/explore_export.js ENV %s %d %d (ENV ref, adv, st)' % (Y, m['seeds'], m['lifeSeed'])
            bands['_meta'] = bands['_meta'] or dict(meta, years=int(Y))
            bands['envs'][e] = {'bands': X['bands'], 'deciles': X['deciles']}
            out['lives-%s-%s.json' % (e, Y)] = {'_meta': dict(meta, env=e, years=int(Y), command=m['command']), 'lives': X['lives']}
            idx['lives']['%s-%s' % (e, Y)] = 'v%s/lives-%s-%s.json' % (R['version'], e, Y)
        out['bands-%s.json' % Y] = bands
        idx['bands'][Y] = 'v%s/bands-%s.json' % (R['version'], Y)
    idx['lifeSeed'] = out['bands-20.json']['_meta']['lifeSeed']
    return out, idx

def dumps(o): return json.dumps(o, ensure_ascii=False, separators=(',', ':'))

# ---------------------------------------------------------------------------------------------------------------- static headline blocks
def headline_html(R, e='ref', Y='20'):
    """three cards, as the simulation page and the explorer render them for their default view (site/findings.js re-renders them on a change)"""
    cards = []
    for k, lbl, pk, dk, unit, mean in [x for c in CARDS for x in MEAS if x[0] == c]:
        b = 'panels.%s.envs.%s' % (Y, e)
        if not has(R, b + '.rows.release.' + pk) or not has(R, b + '.rows.release.' + dk): continue
        if kids(R) and k in MEAS53: mean = MEAS53[k]
        d = get(R, b + '.rows.release.%s.0' % dk); worse = d > 0
        cards.append(('<div class="fx-card%s"><p class="fx-card-k">%s</p><p class="fx-card-v">{{%s.rows.release.%s|p1}}</p><p class="fx-card-vs">with Compassionism, against {{%s.base.%s|p1}} with no programme</p>'
                      '<p class="fx-card-d">%s {{%s.rows.release.%s.0|s1}} points</p><p class="fx-card-m" data-rel-text="meaning">%s</p></div>') % (
            ' fx-worse' if worse else '', lbl, b, pk, b, pk, 'Worse:' if worse else 'Change:', b, dk, mean))
    head = ('<p class="fx-static-note">%s environment, %s years; averages over {{meta.seeds|int}} paired runs of {{meta.agents|int}} simulated adults%s (release v%s data).</p>' % (R['meta']['envs'][e]['name'], Y, ' and their children, in households' if kids(R) else '', R['version']))
    return render_static(R, '<div class="fx-cards">' + ''.join(cards) + '</div>' + head)

def summary_html(R):
    """the replication page's five-line summary of the current findings; every claim in it is chosen from the numbers"""
    E = R['panels']['20']['envs']
    lines = ['Reference, 20 years: below the cost of living {{panels.20.envs.ref.rows.release.fgt0PY|p1}} of adult-years with Compassionism against {{panels.20.envs.ref.base.fgt0PY|p1}} with no programme; too little wealth {{panels.20.envs.ref.rows.release.pov|p1}} against {{panels.20.envs.ref.base.pov|p1}}.',
             'Below 30 days of basic living (BLEI): ' + ', '.join('{{panels.20.envs.%s.rows.release.bOAPy|p1}} against {{panels.20.envs.%s.base.bOAPy|p1}} (%s)' % (e, e, en) for e, en in ENVS) + '.']
    w = [(e, en) for e, en in ENVS if E[e]['rows']['release']['pov'] > E[e]['base']['pov']]
    lines.append(('More adults end with too little wealth than with no programme in ' + '; '.join('%s ({{panels.20.envs.%s.rows.release.pov|p1}} against {{panels.20.envs.%s.base.pov|p1}}; prices rise {{panels.20.envs.%s.rows.release.infl|p1}} a year)' % (en, e, e, e) for e, en in w) +
                  ': prices rise with the programme’s new money and savings in the model earn nothing.') if w else 'In every environment fewer adults end with too little wealth than with no programme.')
    if kids(R):
        lines.append('Children (Reference, 20 years): below the cost of living {{panels.20.envs.ref.rows.release.hhCostKidPY|p1}} of child-years with Compassionism against {{panels.20.envs.ref.base.hhCostKidPY|p1}} with no programme; '
                     'in a household with too little wealth at the last year {{panels.20.envs.ref.rows.release.hhWlthKidEnd|p1}} against {{panels.20.envs.ref.base.hhWlthKidEnd|p1}}.')
    lines.append('The decisive unknown is how much of the Source’s payout new output backs: if all of it were, too little wealth would be {{panels.20.envs.ref.rows.h1.pov|p1}} (Reference). Cost: {{panels.20.envs.ref.rows.release.cost|usd}} per adult a year (Reference).')
    rep = E['ref']['rows']['release'].get('rep')
    if rep:  # which of the poverty measures meet the Hub's Year 7 target of under 2% (Reference)
        SH = {'fpl': 'the official poverty line ({{panels.20.envs.ref.rows.release.rep.y7.fpl|p1}})', 'fplX': 'the poverty line on Supplemental-style resources ({{panels.20.envs.ref.rows.release.rep.y7.fplX|p1}})',
              'bO': '30 days of basic living ({{panels.20.envs.ref.rows.release.rep.y7.bO|p1}})', 'bN': '30 days, design-neutral ({{panels.20.envs.ref.rows.release.rep.y7.bN|p1}})',
              'f0': 'the cost of living ({{panels.20.envs.ref.rows.release.rep.y7.f0|p1}})', 'pov': 'too little wealth ({{panels.20.envs.ref.rows.release.rep.y7.pov|p1}})', 'ep': 'unhoused ({{panels.20.envs.ref.rows.release.rep.y7.ep|p2}})'}
        met = [SH[k] for k, lbl, tgt, f, kind in TG_MEASURES if kind == 'pov' and rep['y7'][k] < 2]
        nmet = [SH[k] for k, lbl, tgt, f, kind in TG_MEASURES if kind == 'pov' and rep['y7'][k] >= 2]
        lines.append('Against the Hub’s Year 7 target of under 2%% poverty (Reference): met on %s; not met on %s.' % (', '.join(met) if met else 'no measure', ', '.join(nmet) if nmet else 'no measure'))
    return render_static(R, '<ul class="fx-sum">' + ''.join('<li>' + x + '</li>' for x in lines) + '</ul>')

def concepts_html(R):
    """the replication page's key concepts: what is being replicated, with every number from the release file"""
    y40 = ' or {{panels.40._meta.years|int}}' if '40' in R['panels'] else ''
    t = ('<div class="kc-grid">'
         '<div class="kc"><h3>The five components</h3><ul>'
         '<li><strong>CCO, Creative Currency Octaves:</strong> every adult who takes part receives a monthly allowance of Basic Units (BU) that buy only essentials and expire; expired BU convert to dollars at higher rates, for work the community values, through the Creative Collectives.</li>'
         '<li><strong>PTF, Public Trust Foundations:</strong> community-owned essential-service providers that accept BU and split what they earn between lower prices, new capacity and their workers.</li>'
         '<li><strong>PTH, Public Trust Housing:</strong> community-owned housing whose payments build the resident\u2019s equity (Acre Equity) instead of paying rent.</li>'
         '<li><strong>SZH, Social Zone Harmonization:</strong> zone coordination of where community businesses and housing go.</li>'
         '<li><strong>CIP, Citizens Internet Portal:</strong> the civic platform that runs the currency and the community\u2019s votes.</li></ul></div>'
         '<div class="kc"><h3>How the runs are set up</h3><ul>'
         + ('<li><strong>{{meta.agents|int}} simulated adults</strong> of working age, living in households as US adults do (single adults, single parents, couples with and without children; Census Bureau figures), with their children, followed for' if kids(R) else
            '<li><strong>{{meta.agents|int}} simulated adults</strong>, single and of working age, followed for') + ' {{panels.20._meta.years|int}}' + y40 + ' years, once with Compassionism and once with no programme, on the same random draws (common random numbers), so a difference comes from the programme and not from luck.</li>'
         '<li><strong>{{meta.seeds|int}} paired runs</strong> (seeds 1 to {{meta.seeds|int}}); every figure is their average, with a 95% interval for each change. '
         'Each change is the mean of the per-run differences (Compassionism minus no programme on the same draws), and its 95% interval is computed on those paired differences, not from two separate averages.'
         + (' The findings explorer also counts, for each headline measure, the runs in which the programme does better (\u201cRun by run\u201d).' if has(R, 'panels.20.envs.ref.rows.release.paired') else '') + '</li>'
         '<li><strong>Three environments:</strong> Reference (' + ENV_DESC['ref'] + '); Adverse (' + ENV_DESC['adv'] + '); Stress Test (' + ENV_DESC['st'] + ').</li>'
         '<li><strong>The main reading</strong> is Compassionism as specified on the Research Hub, every mechanism in, paid for by a Source that issues the BU; cautiously, what the Source pays out is new money except what new output backs. Every other assumption is a labelled reading beside it.</li></ul></div>'
         '<div class="kc"><h3>The measures</h3><ul>'
         '<li><strong>Below {{inputs.bleiDays|int}} days of basic living</strong> (the Basic Living Economic Index, BLEI): savings, pay and support cover fewer than {{inputs.bleiDays|int}} days of basic costs. The BLEI paper\u2019s definition, with a design-neutral reading beside it.</li>'
         + ('<li><strong>Below the cost of living:</strong> a household’s income short of the MIT living-wage basket for its adults and children; counted for adults, for children and for everyone.</li>' if kids(R) else
            '<li><strong>Below the cost of living:</strong> income short of the MIT living-wage basket for one adult.</li>') +
         '<li><strong>Too little wealth:</strong> net wealth (what someone owns minus what they owe) under {{inputs.wealthLine|usd}} in today\u2019s money.</li>'
         '<li>Also: the US official poverty line ({{inputs.povertyLine2025|usd}} for one person in 2025), the unhoused share, and the spread of income and wealth (Gini).</li>'
         '<li><strong>What each Gini estimates:</strong> every Gini is the sample Gini of the {{meta.agents|int}} adults multiplied by n/(n − 1), with n the number of adults. The adults are a random draw from the model\u2019s population, so the corrected figure estimates the Gini of that population (the one compared with the Hub\u2019s national targets) without the small downward bias of a sample. '
         'The Gini of the {{meta.agents|int}} adults themselves, without the correction and slightly lower, is in the release file beside it as a derived figure.</li>'
         '<li><strong>Poverty lines move with prices</strong> every year, so a line means the same standard of living; the findings explorer also shows them fixed in dollars.</li></ul></div>'
         '</div>')
    return render_static(R, t)

def put_block(html, name, block):
    a, b = '<!-- figs:%s -->' % name, '<!-- /figs:%s -->' % name
    if a not in html: return html, False
    i = html.index(a) + len(a); j = html.index(b, i)
    return html[:i] + block + html[j:], True

# ---------------------------------------------------------------------------------------------------------------- main
def plan(backfill=None):
    """every file this would write: {relative path: text}"""
    files = {}
    man_p = os.path.join(ROOT, 'data', 'manifest.json')
    manifest = json.load(open(man_p)) if os.path.exists(man_p) else {'about': 'The releases of the Compassionism Simulation’s findings, newest first. Written by dev/tools/release_data.py; see dev/ADDING-A-RELEASE.md.', 'releases': []}
    if backfill:
        info = BACKFILL[backfill]; R = build(info, src=backfill); R['status'] = 'earlier'
        files['data/releases/v%s.json' % R['version']] = dumps(R)
        ent = {'version': R['version'], 'date': R['date'], 'tag': R['tag'], 'file': 'releases/v%s.json' % R['version'], 'summary': R['summary'], 'status': 'earlier'}
        manifest['releases'] = [r for r in manifest['releases'] if r['version'] != R['version']] + [ent]
    else:
        R = build(current()); R['status'] = 'current'
        ex, idx = explore_files(R)
        if ex:
            R['explore'] = idx
            for n, o in ex.items(): files['data/releases/v%s/%s' % (R['version'], n)] = dumps(o)
        files['data/releases/v%s.json' % R['version']] = dumps(R)
        if R.get('attrib'):  # v5.3: the attribution alone, for the simulation page's "What each part does" (the same numbers, at the same paths, as in the release file)
            files['data/releases/v%s/attrib.json' % R['version']] = dumps({'version': R['version'], 'attrib': R['attrib']})
        for r in manifest['releases']:
            if r['version'] != R['version']:
                r['status'] = 'earlier'
                fp = os.path.join(ROOT, 'data', r['file'])  # v5.3: the release that was current says so in its own file too (check_figures compares them)
                if os.path.exists(fp):
                    old = json.load(open(fp, encoding='utf-8'))
                    if old.get('status') != 'earlier': old['status'] = 'earlier'; files['data/' + r['file']] = dumps(old)
        ent = {'version': R['version'], 'date': R['date'], 'tag': R['tag'], 'file': 'releases/v%s.json' % R['version'], 'summary': R['summary'], 'status': 'current', 'shownIn': R.get('shownIn')}
        manifest['releases'] = [r for r in manifest['releases'] if r['version'] != R['version']] + [ent]
        for page, blocks in (('index.html', [('headline', headline_html(R))]), ('findings.html', [('headline', headline_html(R))]), ('replication.html', [('summary', summary_html(R)), ('concepts', concepts_html(R))])):
            p = os.path.join(ROOT, page)
            if not os.path.exists(p): continue
            H = open(p, encoding='utf-8').read(); H0 = H
            for name, blk in blocks: H, _ = put_block(H, name, blk)
            files[page] = H
    key = lambda r: [int(x) for x in r['version'].split('.')]
    manifest['releases'].sort(key=key, reverse=True)
    files['data/manifest.json'] = json.dumps(manifest, ensure_ascii=False, indent=1) + '\n'
    return files

if __name__ == '__main__':
    args = sys.argv[1:]
    bf = args[args.index('--backfill') + 1] if '--backfill' in args else None
    files = plan(bf)
    if '--check' in args:
        bad = [p for p, t in files.items() if not os.path.exists(os.path.join(ROOT, p)) or open(os.path.join(ROOT, p), encoding='utf-8').read() != t]
        if bad: print('release data OUT OF DATE (rerun python3 dev/tools/release_data.py): ' + ', '.join(bad)); sys.exit(1)
        print('release data, manifest and static headline blocks are up to date (%d files)' % len(files)); sys.exit(0)
    for p, t in files.items():
        fp = os.path.join(ROOT, p); os.makedirs(os.path.dirname(fp), exist_ok=True)
        old = open(fp, encoding='utf-8').read() if os.path.exists(fp) else None
        if old != t: open(fp, 'w', encoding='utf-8').write(t); print('wrote', p, len(t), 'bytes')
