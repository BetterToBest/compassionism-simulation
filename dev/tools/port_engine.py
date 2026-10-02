"""Plan step 10 (Oct 1, 2026): port the release engine from harness.js into index.html.

Copies, verbatim, every top-level declaration of harness.js that the release run needs and the page does not have (the dependency
closure of tbRun, tbStudy and the presets and switches the release uses), plus harness.js's runYear in place of the page's. Every
switch in that code defaults to off, so the page's own runs are unchanged (domtest's page-versus-harness parity checks prove it).
The block sits between the markers below; rerun this script after any engine change in harness.js to keep the copies equal.

Usage: python3 dev/tools/port_engine.py   (rewrites index.html in place)
"""
import re, sys
H = open('harness.js').read()
P = open('index.html').read()
BEGIN = '/* ==== RELEASE ENGINE: ported verbatim from harness.js by dev/tools/port_engine.py (plan step 10). Do not edit here. ==== */'
END = '/* ==== END RELEASE ENGINE ==== */'

eng = H[:H.index("if (require.main === module)")]
lines = eng.split('\n')
starts = re.compile(r'^(function |var |CFG\.[A-Z_]+ *=|Object\.assign\(module\.exports|/\*|if \()')
chunks, cur = [], []
for ln in lines:
    if starts.match(ln) and cur:
        chunks.append('\n'.join(cur)); cur = []
    cur.append(ln)
if cur: chunks.append('\n'.join(cur))
# attach comment-only chunks to the following chunk
merged, pend = [], ''
for c in chunks:
    if c.lstrip().startswith('/*') and re.sub(r'(?s)/\*.*?\*/', '', c).strip() == '':
        pend += c + '\n'; continue
    merged.append((pend, c)); pend = ''

def declared(c):
    m = re.match(r'function ([A-Za-z_$][\w$]*)', c)
    if m: return [m.group(1)]
    if c.startswith('var '):
        first = c.split('\n')[0]
        return re.findall(r'(?:^var |, *)([A-Za-z_$][\w$]*) *=', first)
    m = re.match(r'(CFG\.[A-Z_]+) *=', c)
    if m: return [m.group(1)]
    return []

pscript = P[P.index('<script>'):]
old_at = None
if BEGIN in pscript:
    old_at = pscript.index(BEGIN)
    pscript = pscript[:old_at] + pscript[pscript.index(END) + len(END):]
pnames = set(re.findall(r'(?m)^(?:function|var|const|let)\s+([A-Za-z_$][\w$]*)', pscript))
decl = {}
for i, (cm, c) in enumerate(merged):
    for n in declared(c): decl.setdefault(n, i)
need_names = set(decl) - pnames
need_names.add('runYear')
roots = ['runYear', 'tbRun', 'tbStudy', 'tbPresets', 'n1Row', 'tbDiff', 'TB_KEYS', 'SPEND_SOURCED', 'AVOID_HOMELESS', 'applyNR6', 'resetNR6',
         'TB_PROFILE_G', 'tbSetG', 'FULL_INTEGRATION', 'ADVERSE_REFERENCE', 'STRESS_TEST', 'COST_DEFAULTS', 'JOIN_DEFAULTS', 'OCT_DEFAULTS',
         'REL_V5', 'avoidWide', 'AVOID_WIDE']  # plan step 18: the v5.0 release row and the wider avoided costs
cfg_extra = [i for i, (cm, c) in enumerate(merged) if declared(c) and declared(c)[0].startswith('CFG.')]
take = set(cfg_extra); todo = list(roots)
while todo:
    n = todo.pop()
    if n not in decl or n not in need_names: continue
    i = decl[n]
    if i in take: continue
    take.add(i)
    body = merged[i][1]
    for tok in set(re.findall(r'[A-Za-z_$][\w$]*', body)):
        if tok in need_names and decl.get(tok) not in take: todo.append(tok)
# the page's runYear is replaced
if old_at is not None:
    s0 = e0 = old_at
else:
    m = re.search(r'(?m)^function runYear\(', pscript)
    if not m: sys.exit('page runYear not found')
    s0 = m.start(); depth = 0; k = pscript.index('{', s0)
    for j in range(k, len(pscript)):
        if pscript[j] == '{': depth += 1
        elif pscript[j] == '}':
            depth -= 1
            if depth == 0: e0 = j + 1; break
block = BEGIN + '\n' + '\n'.join(merged[i][0] + merged[i][1] for i in sorted(take)) + '\n' + END
# shared functions whose harness.js version is a superset (identical with every switch off) replace the page's in place
REPLACE = ['agentBLEI']
def span(src, name):
    mm = re.search(r'(?m)^function ' + name + r'\(', src); jj = src.index('{', mm.start()); dd = 0
    for kk in range(jj, len(src)):
        if src[kk] == '{': dd += 1
        elif src[kk] == '}':
            dd -= 1
            if dd == 0: return mm.start(), kk + 1
for name in REPLACE:
    a0, a1 = span(pscript, name); h0, h1 = span(eng, name)
    rep_txt = '/* plan step 10: harness.js version (ported by dev/tools/port_engine.py) */\n' + eng[h0:h1]
    if pscript[a0 - len('/* plan step 10: harness.js version (ported by dev/tools/port_engine.py) */\n'):a0].startswith('/* plan step 10'):
        a0 -= len('/* plan step 10: harness.js version (ported by dev/tools/port_engine.py) */\n')
    if a0 < s0: s0 += len(rep_txt) - (a1 - a0); e0 += len(rep_txt) - (a1 - a0)
    pscript = pscript[:a0] + rep_txt + pscript[a1:]
pscript = pscript[:s0] + block + pscript[e0:]
P = P[:P.index('<script>')] + pscript
open('index.html', 'w').write(P)
print('ported', len(take), 'declarations:', ', '.join(sorted(n for i in take for n in declared(merged[i][1]))))
