# PROTOTYPE (v5.3 plan item B1, Oct 6, 2026; dev/reports/v5-3-one-engine-feasibility.md). Not used by any check or tool.
# It builds a harness whose engine is read out of index.html: the page's top-level declarations that harness.js also declares, in page order,
# then harness.js's own code (the declarations the page lacks, its exports and its command line). drawAutomationRisk and incomeBasketMetrics
# are kept from harness.js, standing in for moving their two off-by-default branches into the page. B1 proper puts this loader inside harness.js.

"""Prototype (scratch, B1 feasibility): build a harness whose engine is read out of index.html.
Usage: python3 build_from_page.py REPO_DIR OUT_JS"""
import re, sys, os
root, out = sys.argv[1], sys.argv[2]
H = open(os.path.join(root, 'harness.js'), encoding='utf-8').read()
P = open(os.path.join(root, 'index.html'), encoding='utf-8').read()
cut = H.index("if (require.main === module)")
eng, cli = H[:cut], H[cut:]
starts = re.compile(r'^(function |var |CFG\.[A-Z_]+ *=|Object\.assign\(module\.exports|/\*|if *\(|window\.|document\.|REL_HUB\.|[A-Za-z_$][\w$]*\.[\w$.]+ *=[^=]|[A-Za-z_$][\w$]*\()')
def chunks(src):
    out, cur = [], []
    for ln in src.split('\n'):
        if starts.match(ln) and cur: out.append('\n'.join(cur)); cur = []
        cur.append(ln)
    if cur: out.append('\n'.join(cur))
    merged, pend = [], ''
    for c in out:
        if c.lstrip().startswith('/*') and re.sub(r'(?s)/\*.*?\*/', '', c).strip() == '': pend += c + '\n'; continue
        merged.append(pend + c); pend = ''
    if pend: merged.append(pend)
    return merged
def body(c): return re.sub(r'(?s)^(\s*/\*.*?\*/\s*\n)*', '', c)
def declared(c):
    c = body(c)
    m = re.match(r'function ([A-Za-z_$][\w$]*)', c)
    if m: return [m.group(1)]
    if c.startswith('var '):
        first = c.split('\n')[0]
        return re.findall(r'(?:^var |, *)([A-Za-z_$][\w$]*) *=', first)
    m = re.match(r'(CFG\.[A-Z_]+) *=', c)
    if m: return [m.group(1)]
    return []
i = P.rindex('<script>\n'); j = P.index('</script>', i); S = P[i + 9:j]
pch = chunks(S); hch = chunks(eng)
pnames = {}
for c in pch:
    for n in declared(c): pnames.setdefault(n, c)
hnames = set(n for c in hch for n in declared(c))
shared = set(pnames) & hnames
KEEP_HARNESS = {'drawAutomationRisk', 'incomeBasketMetrics'}  # the two harness-only branches (to be moved into the page in B1 proper)
engine_from_page, used = [], set()
for c in pch:
    d = declared(c)
    if not d or not (set(d) & shared): continue
    if set(d) & KEEP_HARNESS: continue
    if set(d) - shared: print('page chunk declares page-only names too:', d, file=sys.stderr)
    if id(c) in used: continue
    used.add(id(c)); engine_from_page.append(c)
extras, partial = [], []
for c in hch:
    d = declared(c)
    if d and set(d) <= (shared - KEEP_HARNESS): continue          # comes from the page
    if d and set(d) & (shared - KEEP_HARNESS): partial.append(d)
    extras.append(c)
src = "'use strict';\n/* BUILT BY build_from_page.py (prototype): the engine read from index.html, then harness.js's own code */\n" + '\n'.join(body(c) if c.startswith("'use strict'") else c for c in engine_from_page) + '\n' + '\n'.join(extras) + '\n' + cli
src = src.replace("'use strict';", '', 2) if False else src
open(out, 'w', encoding='utf-8').write(src)
print('page chunks used', len(engine_from_page), '| shared names', len(shared), '| harness extras chunks', len(extras), '| partial overlaps', partial)
