"""v5.2 round, step 8 (Oct 5, 2026; decision D): keep earlier-engine.html in step with index.html.

The earlier engine (v4.22, as coded) has its own page, earlier-engine.html, with its settings, presets and charts. Both pages are single files and carry the
same inline script (the earlier engine's code, the release engine block (the engine's only copy since v5.3; harness.js reads it from index.html), and the front door's code; each page's set-up
runs only where its own elements exist) and the same style sheet. This script copies index.html's <style> block and its inline script into
earlier-engine.html, leaving that page's own markup alone. dev/tools/set_version.py runs it (and so did dev/tools/port_engine.py until v5.3); domtest checks the two are equal.

Usage: python3 dev/tools/sync_earlier.py [--check]   (--check: exit 1 if earlier-engine.html is out of step, change nothing)
"""
import os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')

def parts(html):
    st = re.search(r'<style>.*?</style>', html, re.S)
    i = html.rindex('<script>\n'); j = html.index('</script>', i) + len('</script>')
    return st.span(), (i, j)

def sync(check=False):
    ip, ep = os.path.join(ROOT, 'index.html'), os.path.join(ROOT, 'earlier-engine.html')
    if not os.path.exists(ep): return True
    I, E = open(ip, encoding='utf-8').read(), open(ep, encoding='utf-8').read()
    (s0, s1), (c0, c1) = parts(I)
    (t0, t1), (d0, d1) = parts(E)
    new = E[:t0] + I[s0:s1] + E[t1:d0] + I[c0:c1] + E[d1:]
    if check: return new == E
    if new != E: open(ep, 'w', encoding='utf-8').write(new)
    return True

if __name__ == '__main__':
    ok = sync('--check' in sys.argv)
    if '--check' in sys.argv:
        print('earlier-engine.html is ' + ('in step with' if ok else 'OUT OF STEP with') + ' index.html')
        sys.exit(0 if ok else 1)
    print('earlier-engine.html synced from index.html')
