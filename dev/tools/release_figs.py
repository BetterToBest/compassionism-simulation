"""Plan step 18 (Oct 2, 2026): write the replication page's release-figures table from the merged 500-seed panel.

Usage: python3 dev/tools/release_figs.py   (reads dev/runs/release-panel.json; rewrites the table body in replication.html)
Session 33: if dev/runs/release-panel-40.json exists, also writes the 40-year table (created after the 20-year one the first time).
"""
import json, os
names = {'ref': 'Reference', 'adv': 'Adverse', 'st': 'Stress Test'}

def body(D):
    rows = []
    for e in ['ref', 'adv', 'st']:
        E = D['envs'][e]; b = E['base']; r = E['rows']['release']; h = E['rows']['h1']
        rows.append('<tr><td>%s</td><td>%.1f%% vs %.1f%%</td><td>%.1f%% vs %.1f%%</td><td>%.1f%% vs %.1f%%</td><td>%.1f%%</td><td>%.1f%%</td><td>$%s</td></tr>' % (
            names[e], r['bOAPy'], b['bOAPy'], r['fgt0PY'], b['fgt0PY'], r['pov'], b['pov'], r['infl'], h['pov'], format(r['cost'], ',')))
    return rows

def put(P, start, rows):
    a = P.index(start); t0 = P.index('<tbody>', a) + len('<tbody>'); t1 = P.index('</tbody>', t0)
    return P[:t0] + '\n' + '\n'.join(rows) + '\n' + P[t1:]

P = open('replication.html').read()
rows = body(json.load(open('dev/runs/release-panel.json')))
P = put(P, '<table class="rel-t">', rows)
print('\n'.join(rows))
if os.path.exists('dev/runs/release-panel-40.json'):
    rows40 = body(json.load(open('dev/runs/release-panel-40.json')))
    T40 = '<table class="rel-t" id="rel-t40">'
    if T40 not in P:
        end = P.index('</table>', P.index('<table class="rel-t">')) + len('</table>')
        P = P[:end] + ('\n  <p id="rel-40-h">Over 40 years, the same adults and rules (they do not age in the model). Reproduce: <code>node harness.js testbed 500 release ref --years=40</code>'
                       ' (and <code>adv</code>, <code>st</code>) <code>--json=dev/runs/release-panel-40-ENV.json</code>, then <code>python3 dev/tools/merge_panel.py 40</code>.</p>\n  ' + T40 +
                       '<thead><tr><th>Environment</th><th>Below 30 days of basic living (BLEI)</th><th>Below the cost of living</th><th>Too little wealth, year 40</th><th>Programme inflation a year</th>'
                       '<th>Too little wealth if every Source dollar were backed (H1)</th><th>Cost per adult a year</th></tr></thead><tbody></tbody></table>') + P[end:]
    P = put(P, T40, rows40)
    print('\n'.join(rows40))
open('replication.html', 'w').write(P)
