"""Plan step 13 (Oct 1, 2026): set the version label everywhere it appears, in one step (domtest checks they all agree).

Usage: python3 dev/tools/set_version.py 5.0
Changes: index.html META.VERSION; replication.html <meta name="sim-version">, its JSON-LD "version" (the first one, the page's own) and
every <span class="repl-ver">. Duke assigns the version; run this only when he says "release".
"""
import re, sys
v = sys.argv[1]
P = open('index.html').read()
P, n1 = re.subn(r"(var META = \{\n  VERSION:')[^']+(')", r"\g<1>" + v + r"\2", P)
open('index.html', 'w').write(P)
R = open('replication.html').read()
R, n2 = re.subn(r'(<meta name="sim-version" content=")[^"]+(")', r'\g<1>' + v + r'\2', R)
R, n3 = re.subn(r'("version": ")[^"]+(")', r'\g<1>' + v + r'\2', R, count=1)
R, n4 = re.subn(r'(<span class="repl-ver">)v[^<]+(</span>)', r'\g<1>v' + v + r'\2', R)
open('replication.html', 'w').write(R)
print('META.VERSION', n1, '| sim-version', n2, '| JSON-LD', n3, '| repl-ver labels', n4)
