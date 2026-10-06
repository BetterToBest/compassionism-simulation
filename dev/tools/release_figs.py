"""Plan step 18 (Oct 2, 2026): write the replication page's release figures from the merged 500-seed panels.

Usage: python3 dev/tools/release_figs.py   (reads dev/runs/release-panel.json and release-panel-40.json; rewrites in replication.html:
       the two release tables (20 and 40 years), the price-level note, the Hub-target table (all six environment and horizon combinations)
       and the provenance line)
Session 33: the 40-year table is created after the 20-year one the first time. v5.0.1: price-level column. v5.1 (audit F3, E1, E5): the price
level is the median over seeds with its 10th to 90th percentile range and the mean; the Hub-target table; the provenance line from the
panel's manifest.
"""
import json, os, re, sys
if '<table class="rel-t">' not in open('replication.html').read():
    sys.exit('release_figs.py: retired in v5.2.1. The release tables moved from the replication page to the findings explorer, which renders them from the release '
             'data file; run python3 dev/tools/release_data.py instead (dev/ADDING-A-RELEASE.md).')
from decimal import Decimal, ROUND_HALF_UP


def fx(x, d=1):
    # the digits JavaScript's toFixed gives (domtest compares them): the number's exact value rounded, ties up; Python's % formatting rounds ties to even
    return ('-' if x < 0 and Decimal(abs(x)).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP) != 0 else '') + str(Decimal(abs(x)).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP))
names = {'ref': 'Reference', 'adv': 'Adverse', 'st': 'Stress Test'}

def lev(x):
    # a price level, in times today's prices (the front door prints no figure above 1,000x, audit finding F3; the exact figures are here)
    return format(round(x), ',') if x >= 10 else '%.2f' % x

def lev_cell(r):
    return '%s&times;<br><small>10th&ndash;90th percentile %s&ndash;%s; mean %s</small>' % (lev(r['pLevEndMed']), lev(r['pLevEndP10']), lev(r['pLevEndP90']), lev(r['pLevEnd']))

def body(D):
    rows = []
    for e in ['ref', 'adv', 'st']:
        E = D['envs'][e]; b = E['base']; r = E['rows']['release']; h = E['rows']['h1']
        rows.append('<tr><td>%s</td><td>%.1f%% vs %.1f%%</td><td>%.1f%% vs %.1f%%</td><td>%.1f%% vs %.1f%%</td><td>%.1f%%</td><td>%s</td><td>%.1f%%</td><td>$%s</td></tr>' % (
            names[e], r['bOAPy'], b['bOAPy'], r['fgt0PY'], b['fgt0PY'], r['pov'], b['pov'], r['infl'], lev_cell(r), h['pov'], format(r['cost'], ',')))
    return rows

PL_TH = '<th>Price level at the last year (times today&rsquo;s): median over 500 seeds, with the 10th to 90th percentile and the mean</th>'
OLD_PL_TH = '<th>Price level at the last year (times today&rsquo;s; mean over 500 seeds)</th>'

def add_col(P, start):
    # the price-level header after "Programme inflation a year" in the table that begins at `start`; replaces the v5.0.1 wording once
    a = P.index(start); z = P.index('</thead>', a)
    head = P[a:z]
    if PL_TH in head: return P
    if OLD_PL_TH in head: return P[:a] + head.replace(OLD_PL_TH, PL_TH) + P[z:]
    h0 = P.index('<th>Programme inflation a year</th>', a) + len('<th>Programme inflation a year</th>')
    return P[:h0] + PL_TH + P[h0:]

def put(P, start, rows):
    a = P.index(start); t0 = P.index('<tbody>', a) + len('<tbody>'); t1 = P.index('</tbody>', t0)
    return P[:t0] + '\n' + '\n'.join(rows) + '\n' + P[t1:]

def pct(x, d=1): return fx(x, d) + '%'

def near(g):
    # within 0.002 of a line: 500 adults (the Gini formula reads 0.2% low; the mean of 500 seeds has its own sampling error) cannot place it on either side
    return abs(g - 0.25) < 0.002 or abs(g - 0.30) < 0.002

def verdict(g):
    return ('at or below 0.25' if g <= 0.25 else 'between 0.25 and 0.30' if g <= 0.30 else 'above 0.30') + (' (on the line: within 0.002)' if near(g) else '')

def targets_rows(D20, D40):
    rows = []
    for Y, D in ((20, D20), (40, D40)):
        for e in ['ref', 'adv', 'st']:
            E = D['envs'][e]; b = E['base']; r = E['rows']['release']
            rows.append('<tr><td>%d</td><td>%s</td><td>%s vs %s</td><td>%s vs %s</td><td>%s vs %s</td><td>%s vs %s</td><td>%s vs %s<br><small>%s</small></td><td>%s vs %s<br><small>%s</small></td></tr>' % (
                Y, names[e], pct(r['fgt0PY']), pct(b['fgt0PY']), pct(r['bOAPy']), pct(b['bOAPy']), pct(r['pov']), pct(b['pov']), pct(r['epPY'], 2), pct(b['epPY'], 2),
                fx(r['giniD'], 3), fx(b['giniD'], 3), verdict(r['giniD']), fx(r['giniX'], 3), fx(b['giniX'], 3), verdict(r['giniX'])))
    return rows

# v5.2 round, step 2 (Oct 3, 2026; Duke's answers d148 and d149): with the v5.2 block in the panel (rows carry 'rep'), the Hub-target table reads each measure at Year 7 and at the
# run's last year, with the official poverty line, a BLEI figure, and an income and a wealth Gini, one row per environment, horizon and measure; and a second table gives the
# readings on poverty lines fixed in dollars beside the main, price-indexed ones.
V52_MEASURES = [  # (key, label, Hub target, decimals, kind)
    ('fpl', 'Below the US official poverty line (money income)', 'under 2% (from about 12%)', 1, 'pov'),
    ('fplX', 'Below the poverty line, Supplemental-style resources', 'under 2%', 1, 'pov'),
    ('bO', 'Below 30 days of basic living (BLEI, BLEI paper)', 'under 2%', 1, 'pov'),
    ('bN', 'Below 30 days of basic living (design-neutral)', 'under 2%', 1, 'pov'),
    ('f0', 'Below the cost of living', 'under 2%', 1, 'pov'),
    ('pov', 'Too little wealth', 'under 2%', 1, 'pov'),
    ('ep', 'Unhoused (extreme poverty)', 'under 2%', 2, 'pov'),
    ('giniD', 'Gini of disposable income', '0.25 to 0.30 (from 0.48)', 3, 'gini'),
    ('giniX', 'Gini of income counting price cuts', '0.25 to 0.30', 3, 'gini'),
    ('giniW', 'Gini of wealth (debts as zero)', '0.25 (BLEI paper)', 3, 'giniW')]

def verdict_w(g):
    return ('at or below 0.25' if g <= 0.25 else 'above 0.25') + (' (on the line: within 0.002)' if abs(g - 0.25) < 0.002 else '')

def v52_cell(R, B, kind, d):
    v = 'met' if R < 2 else 'not met'
    if kind == 'gini': v = verdict(R)
    if kind == 'giniW': v = verdict_w(R)
    u = '' if kind != 'pov' else '%'
    return '%s%s vs %s%s<br><small>%s</small>' % (fx(R, d), u, fx(B, d), u, v)

def targets_rows_v52(D20, D40):
    rows = []
    for Y, D in ((20, D20), (40, D40)):
        for e in ['ref', 'adv', 'st']:
            E = D['envs'][e]; b = E['base']['rep']; r = E['rows']['release']['rep']
            for k, lbl, tgt, d, kind in V52_MEASURES:
                rows.append('<tr><td>%d</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (Y, names[e], lbl, tgt, v52_cell(r['y7'][k], b['y7'][k], kind, d), v52_cell(r['end'][k], b['end'][k], kind, d)))
    return rows

def fixed_rows(D20, D40):
    rows = []
    for Y, D in ((20, D20), (40, D40)):
        for e in ['ref', 'adv', 'st']:
            E = D['envs'][e]; B = E['base']; R = E['rows']['release']; b = B['rep']; r = R['rep']
            rows.append('<tr><td>%d</td><td>%s</td><td>%s vs %s<br><small>no programme %s vs %s</small></td><td>%s vs %s<br><small>no programme %s vs %s</small></td><td>%s vs %s<br><small>no programme %s vs %s</small></td></tr>' % (
                Y, names[e], pct(r['end']['pov']), pct(r['end']['povNom']), pct(b['end']['pov']), pct(b['end']['povNom']),
                pct(R['bOAPy']), pct(r['py']['bONom']), pct(B['bOAPy']), pct(b['py']['bONom']),
                pct(r['end']['fpl']), pct(r['end']['fplNom']), pct(b['end']['fpl']), pct(b['end']['fplNom'])))
    return rows

TG_HEAD_V52 = ('<h3 id="rel-targets-h">Against the Hub&rsquo;s own targets (v5.2: Year 7, the official poverty line, income and wealth Gini)</h3>\n  <p>The Research Hub sets two targets for Year 7 of a programme: a poverty rate under 2% (from about 12%) and a Gini coefficient of 0.25 to 0.30 (from 0.48), in the '
           '<a href="https://bettertobest.github.io/research-hub/integrated-implementation-roadmap.html" rel="noopener">Integrated Implementation Roadmap</a> (Success Metrics by Year 7; Appendix I); the BLEI paper adds 0.25 as its design target for the spread of wealth. '
           'Each cell gives Compassionism against no programme, the mean over 500 paired seeds of the share of adults in that year (Year 7, the Hub&rsquo;s date, and the run&rsquo;s last year). '
           'The first measure is the one behind the Hub&rsquo;s starting point: the US official poverty threshold for one person under 65 ($16,749 in 2025; Census, quoted by CRS IN12737), moved with the model&rsquo;s price level as the Census moves it with prices, against money income before tax (earnings, conversion proceeds and cash transfers; the BU, like food stamps, are not money income). '
           'The second keeps the same threshold but counts resources closer to the Census Supplemental Poverty Measure (income after the contribution, plus the value of the BU and the price cuts). '
           'The model&rsquo;s adults are working-age, live alone and all earn wages, with no children, so its no-programme rate sits below the national 10.2% of 2025: the same definition, a different population. '
           'The Hub does not say which measure its rate is, so the 2% line is also read against each of the model&rsquo;s own measures, which are stricter. The unhoused figure starts from 0.22% at year 0 by construction. '
           'The income Gini is the like-for-like figure for the Roadmap&rsquo;s 0.48 start; the BLEI paper&rsquo;s 0.25 is for wealth less a year of extraction costs, which this engine does not model, so the plain wealth Gini (debts counted as zero) is the nearest figure. '
           'Every Gini carries the small-sample correction (&times;500/499, v5.2), and a reading within 0.002 of a line is labelled as on it.</p>\n  ')
TG_TABLE_V52 = ('<table class="rel-t" id="rel-tg"><thead><tr><th>Years</th><th>Environment</th><th>Measure (share of adults that year)</th><th>Hub target</th><th>Year 7: Compassionism vs no programme</th><th>Last year: Compassionism vs no programme</th></tr></thead><tbody></tbody></table>')
FX_HEAD = ('<p id="rel-fixed-h">Poverty lines fixed in dollars (v5.2). The main readings move every line with the price level (the wealth line of $25,000, the 30-day BLEI line and the poverty threshold), '
           'so a line means the same living standard every year. Held fixed in dollars instead, the lines fall behind prices and the shares read lower; this table shows by how much (Compassionism, with no programme below).</p>\n  ')
FX_TABLE = ('<table class="rel-t" id="rel-fx"><thead><tr><th>Years</th><th>Environment</th><th>Too little wealth at the last year: moved with prices vs fixed</th><th>Below 30 days of basic living over the run (BLEI paper): moved vs fixed</th><th>Below the official poverty line at the last year: moved vs fixed</th></tr></thead><tbody></tbody></table>')

# v5.2 round: the readings added in this round, each against its own no-programme pair where it has one (a mechanism that is not design-specific applies to the
# no-programme run too). Each step appends its keys; the table is written after the fixed-dollar table.
V52_READINGS = ['release', 'sav', 'sav0', 'idx', 'h1', 'h1idx', 'h1both', 'age', 'agenc', 'agenone', 'agepia', 'fixw', 'fixr', 'fixs', 'fixm', 'fixall', 'mid', 'midlo', 'midhi', 'slack', 'slacku6', 'hcap', 'hcaphi', 'rev5', 'rev10', 'rev20', 'rev20n', 'giftrun', 'progtax', 'landtax']

def sg(x, d=1):
    t = fx(x, d)
    return t.replace('-', '&minus;') if t.startswith('-') else ('+' + t if x > 0 and t.strip('0.') else t)

def ci_cell(d):
    return '%s <small>(%s to %s)</small>' % (sg(d[0]), sg(d[1]), sg(d[2]))

def readings_rows(D20, D40):
    rows = []
    for Y, D in ((20, D20), (40, D40)):
        for e in ['ref', 'adv', 'st']:
            E = D['envs'][e]
            for k in V52_READINGS:
                r = E['rows'].get(k)
                if not r: continue
                b = E['bases'][r['vsBase']] if r.get('vsBase') else E['base']
                note = ('interest paid $%s per adult a year (today&rsquo;s dollars), $%s of it above inflation' % (format(r['svInt'], ','), format(r['svIntR'], ','))) if r.get('svInt') is not None else ''
                if r.get('agRet') is not None: note = '%s%% of adults retired at the last year; mean age %s' % (fx(r['agRet'], 1), fx(r['agAge'], 1))
                if r.get('bkPY') is not None: note = '%s%% of the Source&rsquo;s payout backed by new output; the payout is %s%% of earned income' % (fx(r['bkA'], 1), fx(r['bkPY'], 1))
                if r.get('mlNT') is not None: note = 'wages added by putting idle workers to work: $%s per adult a year (today&rsquo;s dollars)' % format(r['mlNT'], ',')
                if r.get('hcM') is not None: note = 'rents rise %s%% on average where the mark-up applies' % fx(r['hcM'], 1)
                if r.get('rvX') is not None: note = 'unearned pay not caught $%s, pay clawed back by audits $%s, per adult a year (today&rsquo;s dollars)' % (format(r['rvX'], ','), format(r['rvC'], ','))
                if r.get('taxCover') is not None: note = 'the tax takes %s%% of wages and pays %s%% of the cost%s' % (fx(r['taxAvg'], 1), fx(r['taxCover'], 1), '' if r['taxCover'] >= 99.5 else '; the Source pays the rest as new money')
                rows.append('<tr><td>%d</td><td>%s</td><td>%s%s</td><td>%s vs %s<br><small>%s</small></td><td>%s</td><td>%s</td><td>%s%%</td><td>$%s</td><td>%s</td></tr>' % (
                    Y, names[e], r['label'], ('<br><small>against no programme with the same %s</small>' % ('ageing rule' if r['vsBase'].startswith('ag') else 'US-data reading' if r['vsBase'].startswith('lt') else 'savings rule')) if r.get('vsBase') else '', pct(r['pov']), pct(b['pov']), ci_cell(r['dPov']), ci_cell(r['dF0']), ci_cell(r['dBO']), fx(r['infl'], 1), format(r['cost'], ','), note))
    return rows

RD_HEAD = ('<h3 id="rel-v52-h">Readings added in v5.2</h3>\n  <p id="rel-v52-p">Each reading beside the main row, over 500 paired seeds. A reading that changes something outside the design (savings that keep up with prices) applies to the no-programme run too, '
           'so its changes are against no programme with the same rule. Savings that keep up with prices: each year every adult&rsquo;s savings earn the year&rsquo;s price rise plus 0.97% (the average real yield on 10-year inflation-protected Treasury bonds, 2003&ndash;2025, FRED DFII10); '
           'the interest is reinvested, and the model does not say who pays it (it is not counted as new money in the price rule), so the reading measures how much of a result is the missing protection of savings. '
           'The BU indexed every year: the Hub indexes the BU to prices only in a year when they rise faster than 5% (the main reading, Duke&rsquo;s answer of Oct 3); this reading indexes it every year. '
           'Ageing: every adult has an age (drawn from the Census population aged 25&ndash;66), retires at 67 on the average Social Security benefit ($24,180 in 2025, moved with prices; or, in one reading, the benefit formula on the adult&rsquo;s own wage), dies at the rates of the 2022 US life table (NCHS; the SSA&rsquo;s own table could not be read from the build environment) and is replaced by a new 25-year-old; it applies to the no-programme run too. '
           'Retirees keep the BU for life and may convert expired BU through creative work (Claude&rsquo;s reading of the design, decision A); the other readings take that away or take them out of the programme. '
           'US-data readings: the adults are drawn closer to US data (savings from the Federal Reserve&rsquo;s 2022 Survey of Consumer Finances linked to wages; automation risk linked to wages as in Frey and Osborne&rsquo;s occupations; the survey&rsquo;s wage spread and median wage), with and without the programme (the table of the no-programme run against US data, below, shows what each changes). '
           'The middle backing reading: new output backs the Source&rsquo;s payout up to a share of the year&rsquo;s earned income, 12% (the Kenya cash-transfer study&rsquo;s two-year rollout, Egger et al., <em>Econometrica</em> 2022), with a band from 8% (all of the US&rsquo;s underused labour, BLS U-6, 2025) to 16% (the Kenya study&rsquo;s peak year); '
           'Kenya does not set the US number (the transfers were paid once, from outside the area, into villages with idle capacity), so the main row stays at the cautious end (Claude&rsquo;s reading of the evidence). '
           'The spending layer in normal years: the programme&rsquo;s spending also puts idle workers to work in years without a recession, up to the part of U-6 above its lowest annual level (1.1% of wages) or, as an upper bound, all of U-6 (8%), at a normal-times multiplier of 0.6 (Ramey and Zubairy 2018). '
           'Robustness: landlords raising rents where community housing (PTH) does not cover demand, by $0.50 per BU dollar spent on rent for tenants paying with BU (Collinson and Ganong 2018) or by $1.41 for every renter outside PTH (Susin 2002); the studies measured vouchers that covered a minority of renters, so applying them to an allowance that covers most rent is an upper-end reading. '
           'Mistakes and collusion in the Collectives&rsquo; review of work: 5%, 10% or 20% of conversions at rates above 1&times; are unearned (the work is worth 1&times;), with audits catching half (not specified by the Hub; a labelled design parameter) or none. '
           'The launch gift paid for over the run: the Source&rsquo;s new money for the gift is spread over the run instead of entering in the years it is paid. '
           'Other ways to pay (decision C; not specified by the Hub): a progressive income tax with the 2025 federal brackets&rsquo; shape, scaled until it pays for the programme (marginal rates capped at 90%, brackets moving with average earnings), and a land-value tax; the model has no land, so the land tax falls on adults in proportion to their savings. Where a tax cannot raise the cost, the Source pays the rest as new money.</p>\n  ')
RD_TABLE = ('<table class="rel-t" id="rel-v52"><thead><tr><th>Years</th><th>Environment</th><th>Reading</th><th>Too little wealth at the last year, and the change (95% interval)</th><th>Below the cost of living, change</th>'
            '<th>Below 30 days of basic living (BLEI), change</th><th>Programme inflation a year</th><th>Cost per adult a year</th><th>Note</th></tr></thead><tbody></tbody></table>')

# v5.2 round, step 5: the no-programme run against US data (dev/runs/us-check-ENV.json, written by dev/tools/us_check.js), a match/gap table.
def us_tables():
    if not (os.path.exists('dev/runs/us-check-ref.json') and os.path.exists('dev/runs/us-check-adv.json')): return None
    R = json.load(open('dev/runs/us-check-ref.json')); A = json.load(open('dev/runs/us-check-adv.json')); U = R['us']
    r = R['rows']['none']; a = A['rows']['none']
    def p(x, d=1): return '&ndash;' if x is None else fx(x, d) + '%'
    def g(x): return '&ndash;' if x is None else fx(x, 3)
    def m(x): return '&ndash;' if x is None else ('&minus;$' if x < 0 else '$') + format(int(round(abs(x))), ',')
    def h(x): return '&ndash;' if x is None else fx(x, 2)
    def row(lbl, us, f, why):
        return '<tr><td>%s</td><td>%s</td><td>%s / %s / %s</td><td>%s</td><td>%s</td></tr>' % (lbl, us, f(r, 'y0'), f(r, 'y7'), f(r, 'end'), f(a, 'end'), why)
    rows = [
        row('Below the official poverty line (money income)', '4.3% of workers; 9.2% of people 18&ndash;64; 19.0% of people living alone or with non-relatives; 10.2% of everyone (2025)', lambda x, t: p(x['fpl'][t]),
            'The model&rsquo;s adults all work and live alone, with no children and no one out of work, so the like-for-like US figure is workers&rsquo;; the first year matches it.'),
        row('Below the line on Supplemental-style resources', '7.1% of workers; 12.3% of people 18&ndash;64; 13.1% of everyone', lambda x, t: p(x['spm'][t]),
            'With no programme the model has no taxes or transfers in resources (taxes and medical costs are in its cost of living), so this equals the line above.'),
        row('Gini of income', '0.448 after tax, 0.490 before (households)', lambda x, t: g(x['giniD'][t]),
            'Wages are drawn with a narrow spread (0.5 in logs; a Gini of 0.28). The wage-spread reading (0.8617, the SCF group&rsquo;s wage Gini) gives about 0.46.'),
        row('Gini of wage income (comparison group)', '0.458', lambda x, t: g(x['wealth'][t]['wageGini']), 'As above.'),
        row('Median savings (net worth)', m(U['scf']['median']) + ' (comparison group)', lambda x, t: m(x['wealth'][t]['median']),
            'Starting savings are drawn lognormal (median $36,316), not from the survey, and do not depend on wages; the savings reading draws them from the survey and links them to wages.'),
        row('Share in debt (net worth below zero)', fx(U['scf']['neg'], 1) + '%', lambda x, t: p(x['wealth'][t]['neg']),
            'In the model everyone pays the full living-wage basket ($49,370), which two in three adults earn less than (the model&rsquo;s median wage is $39,945, the survey group&rsquo;s $54,698), so many run their savings into debt; in the US people with less income spend less. The largest gap; the wage-median reading narrows it, and no reading here closes it.'),
        row('Share with savings under $25,000', fx(U['scf']['below25k'], 1) + '%', lambda x, t: p(x['wealth'][t]['below25k']), 'As above.'),
        row('Gini of wealth (debts kept)', g(U['scf']['giniKept']), lambda x, t: g(x['wealth'][t]['giniKept']), 'The lognormal start has a thinner top than the survey; debts widen the spread as the run goes on. With debts kept the Gini can pass 1 when many are in debt (Adverse).'),
        row('Leaving poverty in the first year of a spell', h(U['psid']['exit1']) + ' (PSID)', lambda x, t: h(x['spells']['fpl']['exit1']) if t == 'end' else '&ndash;',
            'Spell figures use every year of the run, so they appear in the last-year columns. In the model poverty comes from year-to-year swings in pay around a steady wage path, so spells are short and people move in and out often; long US spells come from not working, disability and changes in a household, which the model does not have.'),
        row('Leaving poverty in the second year', h(U['psid']['exit2']), lambda x, t: h(x['spells']['fpl']['exit2']) if t == 'end' else '&ndash;', 'As above.'),
        row('Leaving poverty after five years or more', '0.20 or less', lambda x, t: h(x['spells']['fpl']['exit5']) if t == 'end' else '&ndash;', 'As above (few spells reach five years in the model).'),
        row('Back in poverty after one year out', h(U['psid']['reentry1']), lambda x, t: h(x['spells']['fpl']['reentry1']) if t == 'end' else '&ndash;', 'As above.')]
    head = ('<h3 id="rel-us-h">The no-programme run against US data (v5.2)</h3>\n  <p id="rel-us-p">The no-programme run is the yardstick for every result, so it is checked here against published US figures: '
            'poverty rates (Census Bureau, Poverty in the United States: 2025), income inequality (Census Bureau, Income in the United States: 2025), wealth (Federal Reserve, 2022 Survey of Consumer Finances, single adults aged 25&ndash;66 with no children and with wages, the group closest to the model&rsquo;s adults, in 2025 dollars) '
            'and how poverty spells end (Panel Study of Income Dynamics, Stevens 1994). Model figures are means over %d paired runs of the no-programme run, in the first year, at Year 7 and at year 20 (Reference), and at year 20 in the Adverse Environment; '
            'poverty uses the official threshold for one person moved with prices. Reproduce: <code>node dev/tools/us_check.js ref %d</code> and <code>adv</code>. No setting was changed to bring a figure closer; where a gap traces to a known choice, a reading beside the main one changes it (next table).</p>\n  ' % (R['_meta']['seeds'], R['_meta']['seeds']))
    table = ('<table class="rel-t" id="rel-us"><thead><tr><th>Measure</th><th>US figure</th><th>Model, no programme, Reference: first year / Year 7 / year 20</th><th>Adverse, year 20</th><th>Where the gap comes from</th></tr></thead><tbody>\n' + '\n'.join(rows) + '\n</tbody></table>')
    names2 = [('none', 'As modelled'), ('ltw', 'Savings from the survey, linked to wages'), ('ltr', 'Automation risk linked to wages'), ('lts', 'Wages spread as in the survey'), ('ltm', 'Wages centred on the survey&rsquo;s median'), ('lta', 'All four'), ('ag', 'Adults who age, retire and are replaced')]
    rows2 = []
    for k, lbl in names2:
        x = R['rows'].get(k); y = A['rows'].get(k)
        if not x or not y: continue
        rows2.append('<tr><td>%s</td><td>%s / %s</td><td>%s</td><td>%s</td><td>%s</td><td>%s / %s</td><td>%s</td></tr>' % (lbl, m(x['wealth']['y0']['median']), m(x['wealth']['y7']['median']), p(x['wealth']['y7']['neg']), g(x['wealth']['y0']['giniKept']),
            g(x['giniD']['y7']), p(x['fpl']['y7']), p(y['fpl']['end']), h(x['spells']['fpl']['exit1'])))
    head2 = '<p id="rel-us2-p">The readings that change a known choice, no programme only (Reference unless stated). Each also runs with the programme, against no programme under the same choice, in the table of v5.2 readings above.</p>\n  '
    table2 = ('<table class="rel-t" id="rel-us2"><thead><tr><th>Reading</th><th>Median savings: first year / Year 7</th><th>In debt, Year 7</th><th>Wealth Gini, first year</th><th>Income Gini, Year 7</th><th>Below the poverty line: Year 7 / Adverse year 20</th><th>Leaving poverty in a spell&rsquo;s first year</th></tr></thead><tbody>\n' + '\n'.join(rows2) + '\n</tbody></table>')
    return head + table + '\n  ' + head2 + table2

TG_HEAD = ('<h3 id="rel-targets-h">Against the Hub&rsquo;s own targets (audit E1, v5.1)</h3>\n  <p>The Research Hub sets two targets for Year 7 of a programme: a poverty rate under 2% (from about 12%) and a Gini coefficient of 0.25 to 0.30 (from 0.48), in the '
           '<a href="https://bettertobest.github.io/research-hub/integrated-implementation-roadmap.html" rel="noopener">Integrated Implementation Roadmap</a> (Success Metrics by Year 7; Appendix I). '
           'Each cell gives Compassionism against no programme, over 500 paired seeds, at the last year of the run (the adult-year measures are averages over the run). '
           'The Hub does not say which poverty measure its rate is, so the 2% line is read against each of the model&rsquo;s; they are stricter than the official rate (the Hub starts from about 12%), so none of them is the Hub&rsquo;s rate. '
           'The unhoused figure (the model&rsquo;s extreme-poverty figure) starts from 0.22% at year 0 by construction, so it sits under 2% whatever the programme does. '
           'The Gini is that of one year&rsquo;s disposable income across the 500 adults (earnings plus transfers, less the contribution; the second figure also counts the value of price cuts), the like-for-like figure for the Hub&rsquo;s 0.48 start; the model&rsquo;s no-programme Gini is already below 0.48, so the model does not start where the Hub&rsquo;s path starts. '
           'The Gini formula reads about 0.2% low with 500 adults, and a mean over 500 runs has its own sampling error, so a reading within 0.002 of a line is labelled as on it; <code>domtest</code> checks that the formula\'s bias changes no other verdict.</p>\n  ')
TG_TABLE = ('<table class="rel-t" id="rel-tg"><thead><tr><th>Years</th><th>Environment</th><th>Below the cost of living (target under 2%)</th><th>Below 30 days of basic living (under 2%)</th>'
            '<th>Too little wealth at the last year (under 2%)</th><th>Unhoused, extreme poverty (under 2%)</th><th>Gini of disposable income (0.25 to 0.30)</th><th>Gini counting price cuts (0.25 to 0.30)</th></tr></thead><tbody></tbody></table>')

PRICE_NOTE = ('<p id="rel-price-note">The price-level column gives the typical run first: the median over 500 seeds, then the 10th to 90th percentile and the mean. The price level compounds, so the mean runs above the typical seed, '
              'and the gap grows with the horizon. Above 1,000 times today&rsquo;s prices the figure shows the model&rsquo;s price rule running away (it has no central bank, no interest rate and no protection for savings), '
              'a limit of the model and not a forecast; the front door says so in words and keeps the exact figures here.</p>')

def price_note(D20, D40):
    """v5.2 step 8: beside the price levels, what a month of the median wage and of the BU still buys at the last year, in today's dollars (from the panels' year-by-year path)."""
    names = {'ref': 'Reference', 'adv': 'Adverse', 'st': 'Stress Test'}
    if not all('path' in D['envs'][e]['rows']['release'] and 'path' in D['envs'][e]['base'] for D in (D20, D40) for e in names): return PRICE_NOTE
    m = lambda x: '$' + format(int(round(x)), ',')
    parts = []
    for yrs, D in ((20, D20), (40, D40)):
        E = D['envs']
        wages = ', '.join('%s %s (%s)' % (nm, m(E[e]['rows']['release']['path']['wageR'][-1]), m(E[e]['base']['path']['wageR'][-1])) for e, nm in names.items())
        bus = ', '.join('%s %s' % (nm, m(E[e]['rows']['release']['path']['buR'][-1])) for e, nm in names.items())
        parts.append('At year %d a month of the median wage buys %s, and a month of the BU %s.' % (yrs, wages, bus))
    return PRICE_NOTE[:-4] + (' What a month still buys, in today&rsquo;s dollars (the release row; no programme in brackets): ' + ' '.join(parts) +
                              ' The year-by-year path is in the panel files and on the front door.</p>')

def provenance(D20, D40):
    m, m4 = D20['_meta'].get('manifest'), D40['_meta'].get('manifest')
    if not m or not m4: return None
    same = all(m[k] == m4[k] for k in ('commit', 'dirty', 'harnessSha256', 'engineBlockSha256', 'node'))
    return ('<p id="rel-provenance">Provenance of these figures (<code>_meta.manifest</code> of each panel): produced by <code>harness.js</code> at commit <code>%s</code>%s with Node %s; SHA-256 of <code>harness.js</code> as run <code>%s</code>, '
            'of the page&rsquo;s ported release engine <code>%s</code>, of <code>index.html</code> with the embedded panels blanked <code>%s</code> (20 years) and <code>%s</code> (40 years)%s. <code>domtest</code> checks that the engine hash equals the page&rsquo;s.</p>' % (
                m['commit'], '' if not m['dirty'] else ' (tracked files differed from it)', m['node'], m['harnessSha256'], m['engineBlockSha256'], m['indexSha256'], m4['indexSha256'],
                '' if same else ' (the two panels differ in some field: see the data)'))

P = open('replication.html').read()
D20 = json.load(open('dev/runs/release-panel.json'))
P = add_col(P, '<table class="rel-t">')
rows = body(D20)
P = put(P, '<table class="rel-t">', rows)
print('\n'.join(rows))
if os.path.exists('dev/runs/release-panel-40.json'):
    D40 = json.load(open('dev/runs/release-panel-40.json'))
    rows40 = body(D40)
    T40 = '<table class="rel-t" id="rel-t40">'
    if T40 not in P:
        end = P.index('</table>', P.index('<table class="rel-t">')) + len('</table>')
        P = P[:end] + ('\n  <p id="rel-40-h">Over 40 years, the same adults and rules (they do not age in the model). Reproduce: <code>node harness.js testbed 500 release ref --years=40</code>'
                       ' (and <code>adv</code>, <code>st</code>) <code>--json=dev/runs/release-panel-40-ENV.json</code>, then <code>python3 dev/tools/merge_panel.py 40</code>.</p>\n  ' + T40 +
                       '<thead><tr><th>Environment</th><th>Below 30 days of basic living (BLEI)</th><th>Below the cost of living</th><th>Too little wealth, year 40</th><th>Programme inflation a year</th>' + PL_TH +
                       '<th>Too little wealth if every Source dollar were backed (H1)</th><th>Cost per adult a year</th></tr></thead><tbody></tbody></table>') + P[end:]
    P = add_col(P, T40)
    P = put(P, T40, rows40)
    print('\n'.join(rows40))
    # the price-level note (replaces the v5.0.1 paragraph)
    P = re.sub(r'<p id="rel-price-note">.*?</p>', price_note(D20, D40).replace('\\', '\\\\'), P, count=1, flags=re.S)
    # the Hub-target table, once, after the 40-year table; its rows regenerated every time
    V52 = 'rep' in D20['envs']['ref']['rows']['release'] and 'rep' in D40['envs']['ref']['rows']['release']
    head, table, trows = (TG_HEAD_V52, TG_TABLE_V52, targets_rows_v52(D20, D40)) if V52 else (TG_HEAD, TG_TABLE, targets_rows(D20, D40))
    if 'id="rel-tg"' not in P:
        end = P.index('</table>', P.index(T40)) + len('</table>')
        P = P[:end] + '\n  ' + head + table + P[end:]
    else:  # refresh the lead-in text and the header too (the v5.2 table has other columns)
        a = P.index('<h3 id="rel-targets-h">'); b = P.index('</table>', P.index('<table class="rel-t" id="rel-tg">')) + len('</table>')
        P = P[:a] + head + table + P[b:]
    P = put(P, '<table class="rel-t" id="rel-tg">', trows)
    print('\n'.join(trows))
    # v5.2: the fixed-dollar lines, once, after the Hub-target table
    if V52:
        P = re.sub(r'\s*<p id="rel-fixed-h">.*?</p>\s*<table class="rel-t" id="rel-fx">.*?</table>', '', P, flags=re.S)
        end = P.index('</table>', P.index('<table class="rel-t" id="rel-tg">')) + len('</table>')
        P = P[:end] + '\n  ' + FX_HEAD + FX_TABLE + P[end:]
        P = put(P, '<table class="rel-t" id="rel-fx">', fixed_rows(D20, D40))
        print('\n'.join(fixed_rows(D20, D40)))
        # v5.2: the readings added in this round, once, after the fixed-dollar table
        P = re.sub(r'\s*<h3 id="rel-v52-h">.*?</h3>\s*<p id="rel-v52-p">.*?</p>\s*<table class="rel-t" id="rel-v52">.*?</table>', '', P, flags=re.S)
        end = P.index('</table>', P.index('<table class="rel-t" id="rel-fx">')) + len('</table>')
        P = P[:end] + '\n  ' + RD_HEAD + RD_TABLE + P[end:]
        P = put(P, '<table class="rel-t" id="rel-v52">', readings_rows(D20, D40))
        print('\n'.join(readings_rows(D20, D40)[:3]))
    # v5.2 step 5: the US-data check, once, after the readings table (or after the Hub-target table for a v5.1 panel)
    us = us_tables()
    P = re.sub(r'\s*<h3 id="rel-us-h">.*?</table>\s*<p id="rel-us2-p">.*?</p>\s*<table class="rel-t" id="rel-us2">.*?</table>', '', P, flags=re.S)
    if us:
        anchor = '<table class="rel-t" id="rel-v52">' if '<table class="rel-t" id="rel-v52">' in P else '<table class="rel-t" id="rel-tg">'
        end = P.index('</table>', P.index(anchor)) + len('</table>')
        P = P[:end] + '\n  ' + us + P[end:]
    # the provenance line, once, right after the price note
    pv = provenance(D20, D40)
    if pv:
        P = re.sub(r'\s*<p id="rel-provenance">.*?</p>', '', P, flags=re.S)
        a = P.index('<p id="rel-price-note">'); b = P.index('</p>', a) + 4
        P = P[:b] + '\n  ' + pv + P[b:]
open('replication.html', 'w').write(P)
