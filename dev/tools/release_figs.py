"""Plan step 18 (Oct 2, 2026): write the replication page's release-figures table from the merged 500-seed panel.

Usage: python3 dev/tools/release_figs.py   (reads dev/runs/release-panel.json; rewrites the table body in replication.html)
"""
import json, re
D = json.load(open('dev/runs/release-panel.json'))
names = {'ref': 'Reference', 'adv': 'Adverse', 'st': 'Stress Test'}
rows = []
for e in ['ref', 'adv', 'st']:
    E = D['envs'][e]; b = E['base']; r = E['rows']['release']; h = E['rows']['h1']
    rows.append('<tr><td>%s</td><td>%.1f%% vs %.1f%%</td><td>%.1f%% vs %.1f%%</td><td>%.1f%% vs %.1f%%</td><td>%.1f%%</td><td>%.1f%%</td><td>$%s</td></tr>' % (
        names[e], r['bOAPy'], b['bOAPy'], r['fgt0PY'], b['fgt0PY'], r['pov'], b['pov'], r['infl'], h['pov'], format(r['cost'], ',')))
P = open('replication.html').read()
a = P.index('<table class="rel-t">'); t0 = P.index('<tbody>', a) + len('<tbody>'); t1 = P.index('</tbody>', t0)
P = P[:t0] + '\n' + '\n'.join(rows) + '\n' + P[t1:]
open('replication.html', 'w').write(P)
print('\n'.join(rows))
