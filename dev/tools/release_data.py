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
number with commas), lev (a price level: whole number with commas from 10 up, else two decimals, then "times").
"""
import json, os, re, subprocess, sys
from decimal import Decimal, ROUND_HALF_UP, ROUND_FLOOR

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
MINUS = '−'
ENVS = [('ref', 'Reference'), ('adv', 'Adverse'), ('st', 'Stress Test')]
ENV_DESC = {'ref': 'the model\u2019s main settings, with no recessions and no outside inflation',  # the simulation page's own wording (ENV_NOTE in index.html)
            'adv': 'recessions, 2% outside inflation and an automation wave',
            'st': 'the Adverse environment with weaker settings (40% take part, a smaller allowance)'}
# The figures each release's current (presentation) version describes. v5.2.1 changed only how the v5.2 figures are shown.
CURRENT = {'version': '5.2', 'date': '2026-10-06', 'tag': 'v5.2', 'shownIn': '5.2.1',
           'summary': 'The model round: savings that keep up with prices, ageing, the no-programme run against US data, a middle backing reading and robustness readings, each beside an unchanged main result.'}
BACKFILL = {  # earlier releases whose panels were regenerated from their tags and matched exactly (dev/ADDING-A-RELEASE.md); filled in by --backfill
    'v5.1': {'version': '5.1', 'date': '2026-10-03', 'tag': 'v5.1',
             'summary': 'Audit fixes: the wage-bonus test reads this year\'s BU spending, the price level as a typical run with a range, the Hub\'s own targets beside the results, and the backing-share curve.'},
    'v5.0.1': {'version': '5.0.1', 'date': '2026-10-03', 'tag': 'v5.0.1',
               'summary': 'The first release of the release engine (v5.0, Oct 2), with wording fixes and the 40-year horizon; the 20-year figures are v5.0\'s.'}}

# ---------------------------------------------------------------------------------------------------------------- formats (JavaScript's toFixed digits)
def fx(x, d=1):
    q = Decimal(abs(x)).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)
    return ('-' if x < 0 and q != 0 else '') + str(q)

def jsround(x):  # JavaScript's Math.round: halves go up (toward +infinity)
    return int((Decimal(x) + Decimal('0.5')).to_integral_value(rounding=ROUND_FLOOR))

def fmt(x, f):
    if x is None: return '–'
    if f in ('p0', 'p1', 'p2'): return fx(x, int(f[1])).replace('-', MINUS) + '%'
    if f in ('n0', 'n1', 'n2', 'n3'): return fx(x, int(f[1])).replace('-', MINUS)
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

def N(path, f): return {'src': path, 'f': f}
def T(path, f): return '{{%s|%s}}' % (path, f)

def esc(s): return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def render_static(R, text):
    """a text's tokens as static HTML: <span class="num" data-src=... data-f=...>formatted</span> (site/findings.js renders them the same way)"""
    return re.sub(r'\{\{([^|}]+)\|([a-z0-9]+)\}\}', lambda m: '<span class="num" data-src="%s" data-f="%s">%s</span>' % (m.group(1), m.group(2), esc(fmt(get(R, m.group(1)), m.group(2)))), text)

# ---------------------------------------------------------------------------------------------------------------- the measures
MEAS = [  # key in the catalogue, label, panel key, change key, unit, basis, what it means
    ('bO', 'Below 30 days of basic living', 'bOAPy', 'dBO', '% of adult-years',
     'In a typical year, the share of adults whose savings, pay and support would cover fewer than 30 days of basic living (the BLEI paper’s measure).'),
    ('f0', 'Below the cost of living', 'fgt0PY', 'dF0', '% of adult-years',
     'In a typical year, the share of adults whose income falls short of the cost of a basic living (the MIT living-wage basket for one adult).'),
    ('pov', 'Too little wealth', 'pov', 'dPov', '% of adults at the last year',
     'At the end of the run, the share of adults with less than $25,000 of savings in today’s money.'),
    ('bN', 'Below 30 days of basic living, design-neutral', 'bNAPy', 'dBN', '% of adult-years',
     'The same 30-day measure with the no-programme rules applied to everyone, so the design’s own definitions cannot flatter it.')]
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
            if pk not in E['rows']['release']: continue
            base = 'panels.%s.envs.%s' % (Y, e)
            out.append({'id': '%s.%s.%s.with' % (e, Y, k), 'label': lbl + ', with Compassionism', 'src': base + '.rows.release.' + pk, 'unit': unit, 'f': 'p1', 'env': e, 'years': int(Y), 'basis': 'simulated', 'meaning': mean})
            out.append({'id': '%s.%s.%s.without' % (e, Y, k), 'label': lbl + ', no programme', 'src': base + '.base.' + pk, 'unit': unit, 'f': 'p1', 'env': e, 'years': int(Y), 'basis': 'simulated', 'meaning': mean})
            if dk in E['rows']['release']:
                out.append({'id': '%s.%s.%s.change' % (e, Y, k), 'label': lbl + ', change against no programme', 'src': base + '.rows.release.' + dk + '.0', 'unit': 'percentage points', 'f': 's1', 'env': e, 'years': int(Y), 'basis': 'derived',
                            'ci': [base + '.rows.release.' + dk + '.1', base + '.rows.release.' + dk + '.2'], 'meaning': 'The paired difference over the same 500 runs; the 95% interval is beside it. Negative means fewer people below the line.'})
        for k, lbl, pk, unit, f, mean in EXTRA:
            if pk in E['rows']['release']:
                out.append({'id': '%s.%s.%s' % (e, Y, k), 'label': lbl, 'src': 'panels.%s.envs.%s.rows.release.%s' % (Y, e, pk), 'unit': unit, 'f': f, 'env': e, 'years': int(Y), 'basis': 'simulated', 'meaning': mean})
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
        lev = C(N(r + '.pLevEndMed', 'lev'), s=['10th–90th percentile ', N(r + '.pLevEndP10', 'lev'), '–', N(r + '.pLevEndP90', 'lev'), '; mean ', N(r + '.pLevEnd', 'lev')]) if new else C(N(r + '.pLev20', 'lev'))
        rows.append([C(en), C(N(r + '.bOAPy', 'p1'), ' vs ', N(b + '.base.bOAPy', 'p1')), C(N(r + '.fgt0PY', 'p1'), ' vs ', N(b + '.base.fgt0PY', 'p1')), C(N(r + '.pov', 'p1'), ' vs ', N(b + '.base.pov', 'p1')),
                     C(N(r + '.infl', 'p1')), lev, C(N(b + '.rows.h1.pov', 'p1')), C(N(r + '.cost', 'usd'))])
    return {'id': 'rel-t' + Y, 'title': 'Main result, %s years (Compassionism vs no programme)' % Y, 'years': int(Y),
            'columns': ['Environment', 'Below 30 days of basic living (BLEI)', 'Below the cost of living', 'Too little wealth, year %s' % Y, 'Programme inflation a year',
                        'Price level at the last year (times today’s)' + (': median over the runs, with the 10th to 90th percentile and the mean' if new else ': mean over the runs'),
                        'Too little wealth if every Source dollar were backed (H1)', 'Cost per adult a year'], 'rows': rows}

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
    rows = []; v52 = 'sav' in R['panels']['20']['envs']['ref']['rows']
    keys = READINGS if v52 else OLD_READINGS
    for Y in ('20', '40'):
        if Y not in R['panels']: continue
        for e, en in ENVS:
            E = R['panels'][Y]['envs'][e]
            for k in keys:
                r = E['rows'].get(k)
                if not r: continue
                p = 'panels.%s.envs.%s.rows.%s' % (Y, e, k)
                bp = 'panels.%s.envs.%s.%s' % (Y, e, ('bases.' + r['vsBase']) if r.get('vsBase') else 'base')
                vs = ['against no programme with the same ' + ('ageing rule' if r['vsBase'].startswith('ag') else 'US-data reading' if r['vsBase'].startswith('lt') else 'savings rule')] if r.get('vsBase') else None
                rows.append([C(Y), C(en), C(r['label'], s=vs), C(N(p + '.pov', 'p1'), ' vs ', N(bp + '.pov', 'p1'), s=ci(p + '.dPov')), C(*ci(p + '.dF0')), C(*ci(p + '.dBO')),
                             C(N(p + '.infl', 'p1')), C(N(p + '.cost', 'usd')), note_cell(r, p)])
    return {'id': 'rel-v52' if v52 else 'rel-readings', 'title': 'The main row and every reading beside it', 'filter': {'years': 0, 'env': 1},
            'columns': ['Years', 'Environment', 'Reading', 'Too little wealth at the last year, and the change (95% interval)', 'Below the cost of living, change', 'Below 30 days of basic living (BLEI), change', 'Programme inflation a year', 'Cost per adult a year', 'Note'], 'rows': rows}

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
    ('Share with savings under $25,000', lambda u: [N('us.ref.us.scf.below25k', 'p1')], 'wealth.%s.below25k', 'p1', 'As above.'),
    ('Gini of wealth (debts kept)', lambda u: [N('us.ref.us.scf.giniKept', 'n3')], 'wealth.%s.giniKept', 'n3',
     'The lognormal start has a thinner top than the survey; debts widen the spread as the run goes on. With debts kept the Gini can pass 1 when many are in debt (Adverse).'),
    ('Leaving poverty in the first year of a spell', lambda u: [N('us.ref.us.psid.exit1', 'n2'), ' (PSID)'], 'spells.fpl.exit1', 'n2',
     'Spell figures use every year of the run, so they appear in the last-year columns. In the model poverty comes from year-to-year swings in pay around a steady wage path, so spells are short and people move in and out often; long US spells come from not working, disability and changes in a household, which the model does not have.'),
    ('Leaving poverty in the second year', lambda u: [N('us.ref.us.psid.exit2', 'n2')], 'spells.fpl.exit2', 'n2', 'As above.'),
    ('Leaving poverty after five years or more', lambda u: ['0.20 or less'], 'spells.fpl.exit5', 'n2', 'As above (few spells reach five years in the model).'),
    ('Back in poverty after one year out', lambda u: [N('us.ref.us.psid.reentry1', 'n3')], 'spells.fpl.reentry1', 'n2', 'As above.')]

def us_tables(R):
    if not R.get('us'): return []
    rows = []
    for lbl, us, suf, f, why in US_ROWS:
        if '%s' in suf:
            m = C(*sum([[N('us.ref.rows.none.' + suf % t, f), ' / ' if t != 'end' else None] for t in ('y0', 'y7', 'end')], []))
            a = C(N('us.adv.rows.none.' + suf % 'end', f))
        else:
            m = C('– / – / ', N('us.ref.rows.none.' + suf, f)); a = C(N('us.adv.rows.none.' + suf, f))
        rows.append([C(lbl), C(*us(R)), m, a, C(why)])
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

def derived(R):
    D = {}
    if R.get('backing'):
        for e, en in ENVS:
            pts = [(R['backing']['envs'][e]['rows'][k]['a'], R['backing']['envs'][e]['rows'][k]['dPov'][0]) for k in BK]
            c = crossing(pts)
            D['cross_' + e] = {'v': None if c is None else round(c, 4), 'how': 'the share a at which the change in too little wealth against no programme crosses zero, by linear interpolation between the five points of the backing sweep (' + en + ')'}
    return D

def texts(R):
    m = R['meta']; Tx = {}
    Tx['lede'] = ('The same {{meta.agents|int}} simulated adults are followed for 20 or 40 years, once with Compassionism and once with no programme, in three environments; every figure is an average over {{meta.seeds|int}} paired runs. '
                  'These pages show what the model’s assumptions imply, not a forecast. The model has not yet been reviewed by an independent economist.')
    Tx['results.lead'] = ('Compassionism as specified on the Research Hub, every mechanism in, against no programme. Paid for by a Source that issues the BU; in the cautious main reading, what the Source pays out is new money except what new output backs. '
                          'Each environment is a different world the same adults live in: Reference (' + ENV_DESC['ref'] + '), Adverse (' + ENV_DESC['adv'] + ') and Stress Test (' + ENV_DESC['st'] + ').')
    Tx['results.read'] = ('Each row of the chart is one measure in one environment. The hollow mark is no programme, the filled mark is Compassionism, and the line between them is the change. '
                          'A mark further left means fewer people below the line. All three measures are shares of adults: of adult-years for the first two (averaged over the run), of adults at the last year for the third.')
    Tx['results.limits'] = ('It does not show a forecast: it shows what the model’s rules imply. The cautious main reading treats the Source’s payout as new money; the optimistic end (H1, every dollar backed by new output) is in the table. '
                            'The adults are single and working-age, with no children or households, in one country’s prices and wages (US). In the Adverse and Stress environments more adults end with too little wealth than with no programme, because prices rise and savings in the model earn nothing.')
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
    Tx['targets.limits'] = ('The model’s adults are working-age, live alone and all earn wages, with no children, so its no-programme rate sits below the national 10.2% of 2025: the same definition, a different population. '
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
    if 'sav' in R['panels']['20']['envs']['ref']['rows']:
        Tx['readings.lead'] = ('Each reading changes one assumption beside the main row, over the same paired runs. A reading that changes something outside the design (savings that keep up with prices, ageing, the US-data readings) applies to the no-programme run too, so its change is against no programme with the same rule. '
                               'None of them is in the main row: each new mechanism first appears as a labelled reading.')
        Tx['readings.read'] = ('Each row is a reading; the mark is the change against no programme in the chosen measure, with its 95% interval, and the vertical line is the main row. A mark left of the main row means the reading helps; right of it, the reading hurts. '
                               'Rows are grouped: the optimistic end and the middle backing band; savings and the BU; ageing; closer to US data; robustness risks (rent capture, review errors); and other ways to pay.')
        Tx['readings.limits'] = ('Savings that keep up with prices: the model has no bank, so who pays that interest is not modelled. Ageing: the model does not yet report results by age. Rents: the evidence measured vouchers for a minority of renters, an upper-end reading here. '
                                 'Review errors: audits catching half is a design parameter, not in the Hub. The progressive and land taxes are modelling alternatives, not the Hub’s design; the model has no land, so the land tax falls on savings.')
    if R.get('us'):
        Tx['us.lead'] = ('The no-programme run is the yardstick for every result, so it is checked against published US figures: poverty (Census Bureau, Poverty in the United States: 2025), income inequality (Census Bureau, Income in the United States: 2025), '
                         'wealth (Federal Reserve, 2022 Survey of Consumer Finances: single adults aged 25–66, no children, with wages, in 2025 dollars) and how poverty spells end (Panel Study of Income Dynamics, Stevens 1994). '
                         'No setting was changed to bring a figure closer; where a gap traces to a known choice, a reading beside the main one changes it.')
        Tx['us.read'] = 'Each pair compares the model’s no-programme run (filled) with the US figure for the closest group (hollow), at the model’s first year (Reference). Close marks mean the yardstick matches; far marks are gaps, explained in the table.'
        Tx['us.limits'] = ('The model is far more in debt than US single workers (the largest gap) because everyone pays the full living-wage basket and people with less income do not spend less; its poverty spells are short because nobody is out of work, disabled or in a changing household. '
                           'Its income is more equal than the US because wages are drawn with a narrow spread.')
    return Tx

STORIES = [  # the explorer's guided reads: id, title, chart kind, tables, required data
    ('results', 'Results by environment and horizon', 'dumbbell', ['rel-t20', 'rel-t40']),
    ('targets', 'Against the Hub’s own targets', 'targets', ['rel-tg']),
    ('fixed', 'Poverty lines fixed in dollars', 'fixed', ['rel-fx']),
    ('backing', 'The decisive unknown: how much of the payout new output backs', 'backing', ['bs']),
    ('readings', 'How far the answer moves: the readings beside the main row', 'readings', ['rel-v52', 'rel-readings']),
    ('us', 'The no-programme run against US data', 'us', ['rel-us', 'rel-us2'])]

# ---------------------------------------------------------------------------------------------------------------- assembling a release
def load_json(src, path):
    if src is None:
        p = os.path.join(ROOT, path)
        return json.load(open(p)) if os.path.exists(p) else None
    try:
        return json.loads(subprocess.check_output(['git', 'show', '%s:%s' % (src, path)], cwd=ROOT, stderr=subprocess.DEVNULL))
    except subprocess.CalledProcessError:
        return None

def build(info, src=None):
    p20 = load_json(src, 'dev/runs/release-panel.json'); p40 = load_json(src, 'dev/runs/release-panel-40.json')
    if p20 is None: sys.exit('release_data: no 20-year panel')
    R = {'schema': 1, 'version': info['version'], 'date': info['date'], 'tag': info['tag'], 'summary': info['summary']}
    if info.get('shownIn'): R['shownIn'] = info['shownIn']
    cmds = {'20': p20['_meta']['command']}
    if p40: cmds['40'] = p40['_meta']['command']
    R['meta'] = {'seeds': p20['_meta']['seeds'], 'agents': p20['_meta']['agents'], 'written': p20['_meta'].get('written'), 'engine': p20['_meta'].get('engine'), 'manifest': p20['_meta'].get('manifest'), 'commands': cmds,
                 'envs': {e: {'name': en, 'about': ENV_DESC[e]} for e, en in ENVS}}
    R['inputs'] = {'wealthLine': 25000, 'povertyLine2025': 16749, 'bleiDays': 30, 'hubPovertyTarget': 2, 'hubGini': [0.25, 0.30], 'hubGiniStart': 0.48,
                   'sources': {'wealthLine': 'the model’s wealth line (CFG.POVERTY_LINE), moved with prices', 'povertyLine2025': 'US official poverty threshold for one person under 65, 2025 (Census, quoted by CRS IN12737)',
                               'hub': 'Research Hub, Integrated Implementation Roadmap (Success Metrics by Year 7; Appendix I); BLEI paper'}}
    R['panels'] = {'20': p20}
    if p40: R['panels']['40'] = p40
    bk = load_json(src, 'dev/runs/backing-share.json')
    if bk: R['backing'] = bk
    us_r, us_a = load_json(src, 'dev/runs/us-check-ref.json'), load_json(src, 'dev/runs/us-check-adv.json')
    if us_r and us_a: R['us'] = {'ref': us_r, 'adv': us_a}
    R['derived'] = derived(R)
    R['figures'] = catalogue(R, '20') + (catalogue(R, '40') if p40 else [])
    tables = [rel_table(R, '20')] + ([rel_table(R, '40')] if p40 else []) + [t for t in [targets_table(R) if p40 else None, fixed_table(R) if p40 else None, readings_table(R), backing_table(R)] if t] + us_tables(R)
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
    for k, lbl, pk, dk, unit, mean in MEAS[:3]:
        b = 'panels.%s.envs.%s' % (Y, e)
        d = get(R, b + '.rows.release.%s.0' % dk); worse = d > 0
        cards.append(('<div class="fx-card%s"><p class="fx-card-k">%s</p><p class="fx-card-v">{{%s.rows.release.%s|p1}}</p><p class="fx-card-vs">with Compassionism, against {{%s.base.%s|p1}} with no programme</p>'
                      '<p class="fx-card-d">%s {{%s.rows.release.%s.0|s1}} points</p><p class="fx-card-m">%s</p></div>') % (
            ' fx-worse' if worse else '', lbl, b, pk, b, pk, 'Worse:' if worse else 'Change:', b, dk, mean))
    head = ('<p class="fx-static-note">%s environment, %s years; averages over {{meta.seeds|int}} paired runs of {{meta.agents|int}} simulated adults (release v%s data).</p>' % (R['meta']['envs'][e]['name'], Y, R['version']))
    return render_static(R, '<div class="fx-cards">' + ''.join(cards) + '</div>' + head)

def summary_html(R):
    """the replication page's five-line summary of the current findings"""
    t = ('<ul class="fx-sum">'
         '<li>Reference, 20 years: below the cost of living {{panels.20.envs.ref.rows.release.fgt0PY|p1}} of adult-years with Compassionism against {{panels.20.envs.ref.base.fgt0PY|p1}} with no programme; too little wealth {{panels.20.envs.ref.rows.release.pov|p1}} against {{panels.20.envs.ref.base.pov|p1}}.</li>'
         '<li>Below 30 days of basic living (BLEI): {{panels.20.envs.ref.rows.release.bOAPy|p1}} against {{panels.20.envs.ref.base.bOAPy|p1}} (Reference), {{panels.20.envs.adv.rows.release.bOAPy|p1}} against {{panels.20.envs.adv.base.bOAPy|p1}} (Adverse), {{panels.20.envs.st.rows.release.bOAPy|p1}} against {{panels.20.envs.st.base.bOAPy|p1}} (Stress Test).</li>'
         '<li>In the Adverse and Stress environments more adults end with too little wealth than with no programme ({{panels.20.envs.adv.rows.release.pov|p1}} against {{panels.20.envs.adv.base.pov|p1}}; {{panels.20.envs.st.rows.release.pov|p1}} against {{panels.20.envs.st.base.pov|p1}}), because prices rise ({{panels.20.envs.adv.rows.release.infl|p1}} and {{panels.20.envs.st.rows.release.infl|p1}} a year) and savings are not protected.</li>'
         '<li>The decisive unknown is how much of the Source’s payout new output backs: if all of it were, too little wealth would be {{panels.20.envs.ref.rows.h1.pov|p1}} (Reference). Cost: {{panels.20.envs.ref.rows.release.cost|usd}} per adult a year (Reference).</li>'
         '</ul>')
    rep = R['panels']['20']['envs']['ref']['rows']['release'].get('rep')
    if rep:  # the fifth line, from the numbers: which of the poverty measures meet the Hub's Year 7 target of under 2% (Reference)
        met = [lbl.lower() for k, lbl, tgt, f, kind in TG_MEASURES if kind == 'pov' and rep['y7'][k] < 2]
        nmet = [lbl.lower() for k, lbl, tgt, f, kind in TG_MEASURES if kind == 'pov' and rep['y7'][k] >= 2]
        t = t[:-len('</ul>')] + ('<li>Against the Hub\u2019s Year 7 target of under 2%% poverty (Reference): met on %s; not met on %s (the official line: {{panels.20.envs.ref.rows.release.rep.y7.fpl|p1}}).</li></ul>' % (
            ', '.join(met) if met else 'no measure', ', '.join(nmet) if nmet else 'no measure'))
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
        R = build(CURRENT); R['status'] = 'current'
        ex, idx = explore_files(R)
        if ex:
            R['explore'] = idx
            for n, o in ex.items(): files['data/releases/v%s/%s' % (R['version'], n)] = dumps(o)
        files['data/releases/v%s.json' % R['version']] = dumps(R)
        for r in manifest['releases']:
            if r['version'] != R['version']: r['status'] = 'earlier'
        ent = {'version': R['version'], 'date': R['date'], 'tag': R['tag'], 'file': 'releases/v%s.json' % R['version'], 'summary': R['summary'], 'status': 'current', 'shownIn': R.get('shownIn')}
        manifest['releases'] = [r for r in manifest['releases'] if r['version'] != R['version']] + [ent]
        for page, blocks in (('index.html', [('headline', headline_html(R))]), ('findings.html', [('headline', headline_html(R))]), ('replication.html', [('summary', summary_html(R)), ('headline', headline_html(R))])):
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
