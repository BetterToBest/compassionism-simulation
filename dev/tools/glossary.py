#!/usr/bin/env python3
"""Session 7 (Oct 14, 2026; ledger s160, decision d204): one glossary for the front page and the findings page.

  python3 dev/tools/glossary.py           writes the glossary entries from site/glossary.json into index.html and findings.html
  python3 dev/tools/glossary.py --check   exits 1 if either page's glossary is not what this writes

The entries live once, in site/glossary.json (term, definition; the definition is HTML). Each page holds them between
<!-- glossary:items --> and <!-- /glossary:items --> markers, so the two pages cannot drift apart. Edit the JSON, then run this.
"""
import json, os, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
PAGES = {'index.html': '      ', 'findings.html': '      '}
A, B = '<!-- glossary:items -->', '<!-- /glossary:items -->'


def block(indent):
    entries = json.load(open(os.path.join(ROOT, 'site', 'glossary.json'), encoding='utf-8'))
    rows = ['%s<div class="gloss-item"><div class="gloss-term">%s</div><p class="gloss-def">%s</p></div>' % (indent, e['term'], e['def']) for e in entries]
    return A + '\n' + '\n'.join(rows) + '\n' + indent + B


def main():
    stale = []
    for page, indent in PAGES.items():
        p = os.path.join(ROOT, page)
        s = open(p, encoding='utf-8').read()
        i, j = s.find(A), s.find(B)
        if i < 0 or j < i:
            sys.exit('glossary.py: markers not found in ' + page)
        new = s[:i] + block(indent) + s[j + len(B):]
        if new != s:
            stale.append(page)
            if '--check' not in sys.argv:
                open(p, 'w', encoding='utf-8').write(new)
    if '--check' in sys.argv:
        if stale:
            print('glossary.py --check: not what the generator writes: ' + ', '.join(stale)); sys.exit(1)
        print('glossary.py --check: both pages hold the shared glossary (%d entries)' % len(json.load(open(os.path.join(ROOT, 'site', 'glossary.json')))))
    else:
        print('wrote the glossary into ' + (', '.join(stale) if stale else 'nothing (already current)'))


if __name__ == '__main__':
    main()
