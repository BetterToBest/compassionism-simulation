#!/usr/bin/env python3
"""S75 part 2: the engine's copy of the era paths (index.html `var HXE = ...`), built from sources/s75_hx.json. Usage:
  python3 dev/tools/s75_hx_copy.py          print the line
  python3 dev/tools/s75_hx_copy.py write    replace index.html's line with it
  python3 dev/tools/s75_hx_copy.py check    fail if index.html's line differs from the sources
"""
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'sources'))
import s75_hx  # noqa: E402
def line():
    return s75_hx.line(json.load(open(os.path.join(ROOT, 'sources', 's75_hx.json'))))
if __name__ == '__main__':
    L = line(); p = os.path.join(ROOT, 'index.html')
    src = open(p, encoding='utf-8').read().split('\n')
    got = [i for i, x in enumerate(src) if x.startswith('var HXE = {')]
    if len(sys.argv) > 1 and sys.argv[1] == 'check':
        if len(got) != 1 or src[got[0]] != L: print('index.html HXE differs from the sources'); sys.exit(1)
        print('HXE matches the sources')
    elif len(sys.argv) > 1 and sys.argv[1] == 'write':
        if len(got) != 1: print('index.html needs exactly one line starting "var HXE = {"'); sys.exit(1)
        src[got[0]] = L; open(p, 'w', encoding='utf-8').write('\n'.join(src)); print('written')
    else: print(L)
