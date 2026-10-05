"""Plan step 13 (Oct 1, 2026): set the version label everywhere it appears, in one step (domtest checks they all agree).

Usage: python3 dev/tools/set_version.py 5.0
Changes: index.html META.VERSION, static <title>, JSON-LD softwareVersion, static .meta-ver labels and script banner; CONTRIBUTING.md signature line;
replication.html JSON-LD name, seal tooltip and 'now at v' caveats (audit fix V5-01); replication.html <meta name="sim-version">, its JSON-LD "version" (the first one, the page's own) and
every <span class="repl-ver">. Duke assigns the version; run this only when he says "release".
"""
import re, sys
v = sys.argv[1]
P = open('index.html').read()
P, n1 = re.subn(r"(var META = \{\n  VERSION:')[^']+(')", r"\g<1>" + v + r"\2", P)
P, n1b = re.subn(r'(<title>Compassionism Framework Simulation v)[^ |<]+', r'\g<1>' + v, P)
P, n1c = re.subn(r'("softwareVersion":")[^"]+(")', r'\g<1>' + v + r'\2', P)
P, n1d = re.subn(r'(class="meta-ver">v)[^<]+(</span>)', r'\g<1>' + v + r'\2', P)
P, n1e = re.subn(r'(COMPASSIONISM FRAMEWORK SIMULATION  v)\d+(?:\.\d+)+', r'\g<1>' + v, P)
open('index.html', 'w').write(P)
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import sync_earlier; sync_earlier.sync()  # v5.2 step 8: the same script (META.VERSION, banner) on earlier-engine.html
E = open('earlier-engine.html').read()  # v5.2 step 8: its own static title, JSON-LD and labels
E, n1f = re.subn(r'(<title>Compassionism Framework Simulation v)[^ |<,]+', r'\g<1>' + v, E)
E, n1g = re.subn(r'("softwareVersion":")[^"]+(")', r'\g<1>' + v + r'\2', E)
E, n1h = re.subn(r'(class="meta-ver">v)[^<]+(</span>)', r'\g<1>' + v + r'\2', E)
open('earlier-engine.html', 'w').write(E)
R = open('replication.html').read()
R, n2 = re.subn(r'(<meta name="sim-version" content=")[^"]+(")', r'\g<1>' + v + r'\2', R)
R, n3 = re.subn(r'("version": ")[^"]+(")', r'\g<1>' + v + r'\2', R, count=1)
R, n4 = re.subn(r'(<span class="repl-ver">)v[^<]+(</span>)', r'\g<1>v' + v + r'\2', R)
R, n5 = re.subn(r'("name": "Compassionism Framework Simulation v)[^"]+(")', r'\g<1>' + v + r'\2', R)
R, n6 = re.subn(r'(describes engine version )\d+(?:\.\d+)+', r'\g<1>' + v, R)
R, n7 = re.subn(r'((?:now at v|shipped v))\d+(?:\.\d+)+', r'\g<1>' + v, R)
open('replication.html', 'w').write(R)
C = open('CONTRIBUTING.md').read()
C, n8 = re.subn(r'(\*Better To Best Research Hub · Compassionism Framework Simulation v)[^*]+(\*)', r'\g<1>' + v + r'\2', C)
open('CONTRIBUTING.md', 'w').write(C)
print('title/JSON-LD/meta-ver/banner', n1b, n1c, n1d, n1e, '| earlier-engine.html', n1f, n1g, n1h, '| replication name/seal/caveats', n5, n6, n7, '| CONTRIBUTING signature', n8)
print('META.VERSION', n1, '| sim-version', n2, '| JSON-LD', n3, '| repl-ver labels', n4)
print('now run: node dev/tools/check_versions.js')
