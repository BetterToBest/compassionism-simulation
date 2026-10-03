"""Plan step 18 (Oct 2, 2026): write the replication page's release figures from the merged 500-seed panels.

Usage: python3 dev/tools/release_figs.py   (reads dev/runs/release-panel.json and release-panel-40.json; rewrites in replication.html:
       the two release tables (20 and 40 years), the price-level note, the Hub-target table (all six environment and horizon combinations)
       and the provenance line)
Session 33: the 40-year table is created after the 20-year one the first time. v5.0.1: price-level column. v5.1 (audit F3, E1, E5): the price
level is the median over seeds with its 10th to 90th percentile range and the mean; the Hub-target table; the provenance line from the
panel's manifest.
"""
import json, os, re
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
V52_READINGS = ['release', 'sav', 'sav0', 'idx', 'h1', 'h1idx', 'h1both']

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
                rows.append('<tr><td>%d</td><td>%s</td><td>%s%s</td><td>%s vs %s<br><small>%s</small></td><td>%s</td><td>%s</td><td>%s%%</td><td>$%s</td><td>%s</td></tr>' % (
                    Y, names[e], r['label'], '<br><small>against no programme with the same savings rule</small>' if r.get('vsBase') else '', pct(r['pov']), pct(b['pov']), ci_cell(r['dPov']), ci_cell(r['dF0']), ci_cell(r['dBO']), fx(r['infl'], 1), format(r['cost'], ','), note))
    return rows

RD_HEAD = ('<h3 id="rel-v52-h">Readings added in v5.2</h3>\n  <p id="rel-v52-p">Each reading beside the main row, over 500 paired seeds. A reading that changes something outside the design (savings that keep up with prices) applies to the no-programme run too, '
           'so its changes are against no programme with the same rule. Savings that keep up with prices: each year every adult&rsquo;s savings earn the year&rsquo;s price rise plus 0.97% (the average real yield on 10-year inflation-protected Treasury bonds, 2003&ndash;2025, FRED DFII10); '
           'the interest is reinvested, and the model does not say who pays it (it is not counted as new money in the price rule), so the reading measures how much of a result is the missing protection of savings. '
           'The BU indexed every year: the Hub indexes the BU to prices only in a year when they rise faster than 5% (the main reading, Duke&rsquo;s answer of Oct 3); this reading indexes it every year.</p>\n  ')
RD_TABLE = ('<table class="rel-t" id="rel-v52"><thead><tr><th>Years</th><th>Environment</th><th>Reading</th><th>Too little wealth at the last year, and the change (95% interval)</th><th>Below the cost of living, change</th>'
            '<th>Below 30 days of basic living (BLEI), change</th><th>Programme inflation a year</th><th>Cost per adult a year</th><th>Note</th></tr></thead><tbody></tbody></table>')

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
    P = re.sub(r'<p id="rel-price-note">.*?</p>', PRICE_NOTE.replace('\\', '\\\\'), P, count=1, flags=re.S)
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
    # the provenance line, once, right after the price note
    pv = provenance(D20, D40)
    if pv:
        P = re.sub(r'\s*<p id="rel-provenance">.*?</p>', '', P, flags=re.S)
        a = P.index('<p id="rel-price-note">'); b = P.index('</p>', a) + 4
        P = P[:b] + '\n  ' + pv + P[b:]
open('replication.html', 'w').write(P)
