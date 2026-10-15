"""Builds the s118 chat packet: everything a plain chat (no repository access) needs to write a second, independent implementation of the
core yearly loop and check it against the real engine. Usage: python3 dev/packets/build_s118_packet.py <reference.json> <out.zip>
The reference file comes from `node dev/packets/make_s118_reference.js`."""
import re, sys, zipfile, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ref, out = sys.argv[1], sys.argv[2]
L = open(os.path.join(ROOT, 'index.html')).read().split('\n')
H = open(os.path.join(ROOT, 'harness.js')).read().split('\n')
defs, cur = {}, None
for i in range(2071, 6400):
    m = re.match(r'(?:function\s+([A-Za-z_$][\w$]*)|(?:var|const|let)\s+([A-Za-z_$][\w$]*)\s*=)', L[i])
    if m:
        cur = m.group(1) or m.group(2); defs.setdefault(cur, [i + 1, i + 1])
    if cur: defs[cur][1] = i + 1
body = lambda n: '\n'.join(L[defs[n][0] - 1:defs[n][1]])
runScenario = '\n'.join(H[70:132]).split('/* v4.20')[0]
need = {t for t in re.findall(r'[A-Za-z_$][\w$]*', runScenario) if t in defs} | {'runYear'}
ch = True
while ch:
    ch = False
    for n in list(need):
        for t in re.findall(r'[A-Za-z_$][\w$]*', body(n)):
            if t in defs and t not in need: need.add(t); ch = True
core = sorted((n for n in need if defs[n][0] < 3400 or n == 'runYear'), key=lambda n: defs[n][0])
later = sorted((n for n in need if n not in core), key=lambda n: defs[n][0])
core_js = '// Real engine, core part (index.html). Excerpted by dev/packets/build_s118_packet.py. runScenario is from harness.js.\n// Mechanisms listed in later-modules.md are OFF in every preset used here (the switches default to off), so their branches never run.\n\n' + runScenario + '\n\n' + '\n\n'.join('// index.html line %d\n%s' % (defs[n][0], body(n)) for n in core) + '\n'
idx = '# Mechanism modules referenced by runYear but off in these presets\n\nEach is a switch that defaults to off; with it off, the branch never runs, so you do not need to read it. Index.html line numbers refer to the full file, which is not in this packet.\n\n' + '\n'.join('- `%s` (index.html line %d, %d lines)' % (n, defs[n][0], defs[n][1] - defs[n][0] + 1) for n in later) + '\n'
brief = open(os.path.join(ROOT, 'dev/packets/s118-brief.md')).read()
prompt = open(os.path.join(ROOT, 'dev/packets/s118-prompt.md')).read()
with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
    z.writestr('00-START-HERE.md', brief); z.writestr('01-PROMPT-to-paste.md', prompt)
    z.write(os.path.join(ROOT, 'ODD.md'), 'ODD.md'); z.write(os.path.join(ROOT, 'MODEL_SPEC.md'), 'MODEL_SPEC.md')
    z.writestr('core-loop.js', core_js); z.writestr('later-modules.md', idx); z.write(ref, 'reference-outputs.json')
print(out, os.path.getsize(out), 'bytes; core-loop.js', len(core_js), 'bytes;', len(core), 'core defs,', len(later), 'later')
