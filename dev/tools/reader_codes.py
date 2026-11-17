#!/usr/bin/env python3
"""Reader-facing wording check (S80).

Lists, or with --check fails on, internal project bookkeeping in text a reader sees:
step and ledger codes (S55, D26, I5, N-S72), "session 12", "part M", job ids (X3),
"round 2", "release 1"/"release 2", "C2.2", and internal labels (row ids, key and switch
names in prose).

What counts as reader-visible text:
  * HTML pages: text outside <script>, <style> and <code>/<pre>, plus the title, alt,
    aria-label and placeholder attributes. Inline scripts are read like site/*.js.
  * site/*.js and inline scripts: string literals that read as prose (contain a space and a
    letter), with HTML tags stripped and <code> spans removed.
  * Markdown: everything outside fenced code blocks and `inline code`.
  * JSON files the pages render: the string values of the named text fields.
A path, file name or command inside <code> or backticks is where a reader finds something,
so it is not counted.

Usage:
  python3 dev/tools/reader_codes.py                 # counts per file (this repository)
  python3 dev/tools/reader_codes.py --list          # every occurrence
  python3 dev/tools/reader_codes.py --check         # exit 1 on any step/ledger code, release 1/2 or C2.2
  python3 dev/tools/reader_codes.py --root ../research-hub --preset hub
"""
import argparse, glob, html, json, os, re, sys
from html.parser import HTMLParser

PRESETS = {
    'sim': {
        'html': ['index.html', 'findings.html', 'suite.html', 'study.html', 'replication.html',
                 'earlier-engine.html', 'compare.html'],
        'js': ['site/*.js'],
        'md': ['README.md', 'CONTRIBUTING.md', 'CHANGELOG.md', 'REPRODUCE.md', 'dev/reports/*.md'],
        'json': {'data/manifest.json': ['summary', 'about'], 'site/glossary.json': None},
    },
    'hub': {
        'html': ['*.html', 'wiki/*.html', 'papers/*.html'],
        'js': [],
        'md': ['README.md', '*.md', 'data/claims-summary.md', 'cco-ptf-simulation/README.md'],
        'json': {},
        # the claims ledger's summary is generated from data/claims.csv, which quotes every page; it is rebuilt with the ledger, not reworded by hand
        'pending': ['data/claims-summary.md'],
    },
    'root': {
        'html': ['index.html'],
        'js': [],
        'md': ['llms.txt'],
        'json': {'ai-index.json': None, 'research-index.json': None, 'ai-manifest.json': None},
    },
}

# Categories. "hard" ones fail --check; "soft" ones are listed for the edit pass only.
PATTERNS = [
    ('step/ledger code', True, re.compile(
        r'(?<![\w./#?=&-])(?:N-S\d+|H-S\d+|S\d{1,3}[a-z]?(?:\.\d+)?|D\d{1,3}|I\d{1,2}|i\d{1,2})(?![\w/-]|\.\w)')),
    ('step/ledger code', True, re.compile(r'(?<![\w./#?=&-])S\d{1,3}/S\d{1,3}\b')),  # a pair such as S47/S7
    ('session number', True, re.compile(r'\b[Ss]ession \d+[a-z]?\b')),
    ('part letter', True, re.compile(r'\b[Pp]art (?![IVX]\b)[A-Z]\b')),
    ('job id', True, re.compile(r'(?<![\w./-])(?:job )?X\d\b')),
    ('round 2', True, re.compile(r'(?<![\w/-])[Rr]ound[ -]?[12](?!\w|\.\d)')),
    ('release 1/2', True, re.compile(r'(?<![\w/-])[Rr]elease[ -]?[12](?!\w|\.\d)|\b[Rr]eleases? 1 and 2\b|\b[Rr]elease 1/2\b')),
    ('C2.2', True, re.compile(r'(?<!criterion )\bC2\.2\b')),
    ('row id or key', False, re.compile(r'(?<![\w./-])(?:c22|rel|giniW|giniD|gTop\d*|wt[A-Z]\w*|dm[A-Z]\w*|CFG\.\w+)(?![\w/.-])')),
]

JEL = re.compile(r'\s*(?:JEL[^:]*:\s*)?(?:[A-Z]\d{2}\s*[,·]\s*)+[A-Z]\d{2}\s*')

# Words that look like codes but are not ours.
NOT_CODES = {'S1', 'I1'}  # filled in from the inventory where a match is ordinary prose


class Text(HTMLParser):
    """Collects visible text and inline script bodies from an HTML page."""
    ATTRS = ('title', 'alt', 'aria-label', 'placeholder')

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.scripts, self.stack = [], [], []
        self.line = 1

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style', 'code', 'pre'):
            self.stack.append(tag)
        for k, v in attrs:
            if k in self.ATTRS and v:
                self.out.append((self.getpos()[0], v))

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()

    def handle_data(self, data):
        if not self.stack:
            self.out.append((self.getpos()[0], data))
        elif self.stack[-1] == 'script':
            self.scripts.append((self.getpos()[0], data))


STR = re.compile(r"'(?:[^'\\\n]|\\.)*'|\"(?:[^\"\\\n]|\\.)*\"|`(?:[^`\\]|\\.)*`", re.S)
TAG = re.compile(r'<code>.*?</code>|<pre>.*?</pre>', re.S)
ANY_TAG = re.compile(r'<[^>]+>')


def js_prose(src, line0=1):
    """Prose string literals of a script, as (line, text)."""
    out = []
    # drop // and /* */ comments first (keep line count)
    src = re.sub(r'/\*.*?\*/', lambda m: '\n' * m.group(0).count('\n'), src, flags=re.S)
    src = re.sub(r'(?m)(^|[^:\\\'"])//[^\n]*', r'\1', src)
    for m in STR.finditer(src):
        s = m.group(0)[1:-1]
        if not re.search(r'[A-Za-z]{2,}', s) or ' ' not in s:
            continue
        s = TAG.sub(' ', s)
        s = re.sub(r'\$\{[^}]*\}', ' ', s)
        s = html.unescape(ANY_TAG.sub(' ', s))
        out.append((line0 + src.count('\n', 0, m.start()), s))
    return out


def md_text(src):
    src = re.sub(r'<!--.*?-->', lambda m: '\n' * m.group(0).count('\n'), src, flags=re.S)
    out, fence = [], False
    for i, ln in enumerate(src.split('\n'), 1):
        if ln.lstrip().startswith('```'):
            fence = not fence
            continue
        if fence:
            continue
        out.append((i, re.sub(r'`[^`]*`', ' ', ln)))
    return out


def json_text(obj, fields, path=''):
    out = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, str):
                if fields is None or k in fields:
                    out.append((path + '.' + k, v))
            else:
                out += json_text(v, fields, path + '.' + k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            if isinstance(v, str) and fields is None:
                out.append((path + '[%d]' % i, v))
            else:
                out += json_text(v, fields, path + '[%d]' % i)
    return out


def texts(root, preset):
    p = PRESETS[preset]
    for pat in p['html']:
        for f in sorted(glob.glob(os.path.join(root, pat))):
            src = open(f, encoding='utf-8').read()
            t = Text()
            t.feed(src)
            rel = os.path.relpath(f, root)
            for ln, s in t.out:
                yield rel, ln, s
            for ln, s in t.scripts:
                for l2, s2 in js_prose(s, ln):
                    yield rel, l2, s2
    for pat in p['js']:
        for f in sorted(glob.glob(os.path.join(root, pat))):
            rel = os.path.relpath(f, root)
            for ln, s in js_prose(open(f, encoding='utf-8').read()):
                yield rel, ln, s
    for pat in p['md']:
        for f in sorted(glob.glob(os.path.join(root, pat))):
            rel = os.path.relpath(f, root)
            if os.path.basename(f) in ('CLAUDE.md', 'HANDOFF.md'):
                continue
            for ln, s in md_text(open(f, encoding='utf-8').read()):
                yield rel, ln, s
    for f, fields in p['json'].items():
        fp = os.path.join(root, f)
        if os.path.exists(fp):
            for path, s in json_text(json.load(open(fp, encoding='utf-8')), fields):
                yield f, path, s


def load_allow(root):
    fp = os.path.join(root, 'dev', 'tools', 'reader_codes_allow.txt')
    allow = set()
    if os.path.exists(fp):
        for ln in open(fp, encoding='utf-8'):
            ln = ln.split('#', 1)[0].strip()
            if ln:
                allow.add(ln)
    return allow


def scan(root, preset, allow):
    hits = []
    seen = set()
    for f, ln, s in texts(root, preset):
        if JEL.fullmatch(s) or 'jel' in str(ln).lower():  # a paper's JEL classification codes (D60 · I32 …), not ours
            continue
        for name, hard, rx in PATTERNS:
            for m in rx.finditer(s):
                tok = m.group(0)
                if tok in NOT_CODES or tok in allow or (f + ':' + tok) in allow:
                    continue
                key = (f, ln, name, tok, s.strip()[:60])
                if key in seen:
                    continue
                seen.add(key)
                a, b = max(0, m.start() - 50), min(len(s), m.end() + 50)
                hits.append((f, ln, name, hard, tok, ' '.join(s[a:b].split())))
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=os.path.join(os.path.dirname(__file__), '..', '..'))
    ap.add_argument('--preset', default='sim', choices=PRESETS)
    ap.add_argument('--list', action='store_true')
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--only', help='a file (relative path) to list')
    ap.add_argument('--all', action='store_true', help='--check every file, the pending ones too')
    a = ap.parse_args()
    hits = scan(a.root, a.preset, load_allow(a.root))
    if a.only:
        hits = [h for h in hits if h[0] == a.only]
    if a.list:
        for f, ln, name, hard, tok, ctx in hits:
            print('%s:%s  [%s] %s  …%s…' % (f, ln, name, tok, ctx))
    elif not a.check:
        files = {}
        for f, ln, name, hard, tok, ctx in hits:
            files.setdefault(f, {}).setdefault(name, 0)
            files[f][name] += 1
        names = [n for n, _, _ in PATTERNS]
        print('| file | ' + ' | '.join(names) + ' | total |')
        print('|---|' + '---|' * (len(names) + 1))
        tot = {n: 0 for n in names}
        for f in sorted(files):
            row = [files[f].get(n, 0) for n in names]
            for n, v in zip(names, row):
                tot[n] += v
            print('| %s | %s | %d |' % (f, ' | '.join(str(v) for v in row), sum(row)))
        print('| **all** | %s | %d |' % (' | '.join(str(tot[n]) for n in names), sum(tot.values())))
    if a.check:
        pend = [] if a.all else PRESETS[a.preset].get('pending', [])
        import fnmatch
        hard = [h for h in hits if h[3] and not any(fnmatch.fnmatch(h[0], g) for g in pend)]
        for f, ln, name, _, tok, ctx in hard:
            print('%s:%s  [%s] %s  …%s…' % (f, ln, name, tok, ctx))
        print('reader_codes: %d reader-visible internal code(s)%s' % (len(hard), '' if hard else ' — OK'))
        sys.exit(1 if hard else 0)


if __name__ == '__main__':
    main()
