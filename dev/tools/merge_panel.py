"""Plan step 12 (Oct 1, 2026): merge the 500-seed release panel written per environment (seeds are paired, so splitting the run by
environment changes no figure) and embed it in index.html as <script type="application/json" id="rel-data">.

Usage: python3 dev/tools/merge_panel.py   (reads dev/runs/release-panel-{ref,adv,st}.json; writes dev/runs/release-panel.json and index.html)
       python3 dev/tools/merge_panel.py 40   (session 33: the 40-year panel; reads dev/runs/release-panel-40-{ref,adv,st}.json, writes
                                              dev/runs/release-panel-40.json and <script id="rel-data-40"> after the 20-year block)
"""
import json, sys
Y = sys.argv[1] if len(sys.argv) > 1 else ''
SUF = '-' + Y if Y else ''
out = None
for e in ['ref', 'adv', 'st']:
    d = json.load(open('dev/runs/release-panel%s-%s.json' % (SUF, e)))
    if out is None:
        out = {'_meta': dict(d['_meta']), 'envs': {}}
    # v5.1 (audit E5): the three per-environment runs must come from one build, or the merged panel's manifest would be a lie
    if d['_meta'].get('manifest') != out['_meta'].get('manifest'):
        sys.exit('merge_panel: the manifests of the per-environment panels differ (commit, file hashes or Node version); rerun all three from one commit')
    out['envs'][e] = d['envs'][e]
YF = ' --years=' + Y if Y else ''
out['_meta']['command'] = 'node harness.js testbed %d release ref,adv,st%s (one process per environment: release ref%s --json=dev/runs/release-panel%s-ref.json, and adv, st; then python3 dev/tools/merge_panel.py%s)' % (out['_meta']['seeds'], YF, YF, SUF, ' ' + Y if Y else '')
def rnd(x, nd=3):
    if isinstance(x, float): return round(x, nd)
    if isinstance(x, dict): return {k: rnd(v, 4 if k in ('giniD', 'giniX') else nd) for k, v in x.items()}  # v5.1: Gini keeps four decimals (E1)
    if isinstance(x, list): return [rnd(v, nd) for v in x]
    return x
out = rnd(out)
json.dump(out, open('dev/runs/release-panel%s.json' % SUF, 'w'), indent=1)
s = json.dumps(out, separators=(',', ':')).replace('<', '\\u003c')
P = open('index.html').read()
tag = '<script type="application/json" id="rel-data%s">' % SUF
if tag in P:
    a = P.index(tag); b = P.index('</script>', a)
    P = P[:a] + tag + s + P[b:]
elif Y:
    a = P.index('</script>', P.index('<script type="application/json" id="rel-data">')) + len('</script>\n')
    P = P[:a] + tag + s + '</script>\n' + P[a:]
else:
    a = P.index('<script>', P.index('</section>', P.index('id="front-door"')))
    P = P[:a] + tag + s + '</script>\n' + P[a:]
open('index.html', 'w').write(P)
print('embedded', len(s), 'bytes; environments', list(out['envs']))
