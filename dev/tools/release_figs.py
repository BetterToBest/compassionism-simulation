"""Plan step 18 (Oct 2, 2026): write the replication page's release figures from the merged 500-seed panels.

Usage: python3 dev/tools/release_figs.py   (reads dev/runs/release-panel.json and release-panel-40.json; rewrites in replication.html:
       the two release tables (20 and 40 years), the price-level note, the Hub-target table (all six environment and horizon combinations)
       and the provenance line)
Session 33: the 40-year table is created after the 20-year one the first time. v5.0.1: price-level column. v5.1 (audit F3, E1, E5): the price
level is the median over seeds with its 10th to 90th percentile range and the mean; the Hub-target table; the provenance line from the
panel's manifest.
"""
import json, os, re
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

def pct(x, d=1): return ('%.' + str(d) + 'f%%') % x

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
            rows.append('<tr><td>%d</td><td>%s</td><td>%s vs %s</td><td>%s vs %s</td><td>%s vs %s</td><td>%s vs %s</td><td>%.3f vs %.3f<br><small>%s</small></td><td>%.3f vs %.3f<br><small>%s</small></td></tr>' % (
                Y, names[e], pct(r['fgt0PY']), pct(b['fgt0PY']), pct(r['bOAPy']), pct(b['bOAPy']), pct(r['pov']), pct(b['pov']), pct(r['epPY'], 2), pct(b['epPY'], 2),
                r['giniD'], b['giniD'], verdict(r['giniD']), r['giniX'], b['giniX'], verdict(r['giniX'])))
    return rows

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
    if 'id="rel-tg"' not in P:
        end = P.index('</table>', P.index(T40)) + len('</table>')
        P = P[:end] + '\n  ' + TG_HEAD + TG_TABLE + P[end:]
    else:  # refresh the lead-in text too
        a = P.index('<h3 id="rel-targets-h">'); b = P.index('<table class="rel-t" id="rel-tg">')
        P = P[:a] + TG_HEAD + P[b:]
    P = put(P, '<table class="rel-t" id="rel-tg">', targets_rows(D20, D40))
    print('\n'.join(targets_rows(D20, D40)))
    # the provenance line, once, right after the price note
    pv = provenance(D20, D40)
    if pv:
        P = re.sub(r'\s*<p id="rel-provenance">.*?</p>', '', P, flags=re.S)
        a = P.index('<p id="rel-price-note">'); b = P.index('</p>', a) + 4
        P = P[:b] + '\n  ' + pv + P[b:]
open('replication.html', 'w').write(P)
