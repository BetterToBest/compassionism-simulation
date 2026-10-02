"""Plan step 12 (Oct 1, 2026): merge the 500-seed release panel written per environment (seeds are paired, so splitting the run by
environment changes no figure) and embed it in index.html as <script type="application/json" id="rel-data">.

Usage: python3 dev/tools/merge_panel.py   (reads dev/runs/release-panel-{ref,adv,st}.json; writes dev/runs/release-panel.json and index.html)
"""
import json
out = None
for e in ['ref', 'adv', 'st']:
    d = json.load(open('dev/runs/release-panel-%s.json' % e))
    if out is None:
        out = {'_meta': dict(d['_meta']), 'envs': {}}
    out['envs'][e] = d['envs'][e]
out['_meta']['command'] = 'node harness.js testbed %d release ref,adv,st (one process per environment: release ref --json=dev/runs/release-panel-ref.json, and adv, st; then python3 dev/tools/merge_panel.py)' % out['_meta']['seeds']
def rnd(x):
    if isinstance(x, float): return round(x, 3)
    if isinstance(x, dict): return {k: rnd(v) for k, v in x.items()}
    if isinstance(x, list): return [rnd(v) for v in x]
    return x
out = rnd(out)
json.dump(out, open('dev/runs/release-panel.json', 'w'), indent=1)
s = json.dumps(out, separators=(',', ':')).replace('<', '\\u003c')
P = open('index.html').read()
tag = '<script type="application/json" id="rel-data">'
if tag in P:
    a = P.index(tag); b = P.index('</script>', a)
    P = P[:a] + tag + s + P[b:]
else:
    a = P.index('<script>', P.index('</section>', P.index('id="front-door"')))
    P = P[:a] + tag + s + '</script>\n' + P[a:]
open('index.html', 'w').write(P)
print('embedded', len(s), 'bytes; environments', list(out['envs']))
