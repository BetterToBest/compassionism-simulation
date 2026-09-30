#!/usr/bin/env python3
"""Build the page walk-through from index.html: a captioned video, its caption files and a written tour.

Run from the repository root:

    python3 walkthrough/make_walkthrough.py

Needs Python 3.9+, Playwright for Python with Chromium (pip install playwright, then
python -m playwright install chromium), and ffmpeg on the PATH. The page loads Chart.js and
its fonts from the web, so the build needs a network connection. None of this is part of
`npm test`: the simulation itself still needs nothing but a browser.

Narration (s39, session 16): each caption is read aloud by a synthetic voice, Kokoro-82M
(Apache-2.0) through kokoro-onnx (pip install kokoro-onnx soundfile), voice af_heart, an
American-English female voice. The model files (about 340 MB) are downloaded on the first
run into ~/.cache/compassionism-walkthrough/ and are not part of the repository. A caption
stays on screen for its reading time or its narration, whichever is longer, so the captions,
the voice and the video share one clock. SPOKEN below says how the voice reads acronyms,
file names and dollar figures; the captions themselves are unchanged. --silent builds the
video with no sound, as before.

It takes several minutes (most of it the video encode). Writes into walkthrough/: walkthrough.mp4, captions.vtt, captions.srt, README.md (the written
tour) and img/ (one screenshot per shot, plus the poster).

Every figure in the captions is read from the front door's own data (#fd-data in index.html),
so a rebuild after the comparison is regenerated carries the new figures. The wording around
them makes claims ("still does better", "cuts more"); each such caption lists the conditions
that make its wording true, and the build stops, naming the caption, if one no longer holds.
Edit the captions here, never in README.md, which this script overwrites.
"""
import base64, functools, http.server, io, json, os, re, shutil, subprocess, sys, tempfile, threading

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(ROOT, 'walkthrough')
IMG = os.path.join(OUT, 'img')
PAGE_URL = 'https://bettertobest.github.io/compassionism-simulation/'
VIDEO_URL = PAGE_URL + 'walkthrough/walkthrough.mp4'
REPO_URL = 'https://github.com/BetterToBest/compassionism-simulation'

W, H = 1920, 1080          # video frame
VW, VH, DSF = 1600, 725, 1.2   # page viewport (CSS px) and scale: screenshots are 1920 x 870
BAND = H - int(VH * DSF)   # caption band height: 210 px
CPS, PAD, MIN_S = 17.0, 0.7, 3.6   # reading pace (characters a second), padding, minimum seconds per caption

# ---------------------------------------------------------------- narration (s39)
SILENT = '--silent' in sys.argv
VOICE, SPEED = 'af_heart', 1.0     # Kokoro-82M voice (American-English female) and speaking rate
LEAD, TAIL, LEAD0 = 0.35, 0.5, 0.9  # seconds of quiet before and after each spoken caption; the first waits out the fade-in
KOKORO_URL = 'https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/'
KOKORO_FILES = ('kokoro-v1.0.onnx', 'voices-v1.0.bin')
CACHE = os.path.join(os.path.expanduser('~'), '.cache', 'compassionism-walkthrough')
SPOKEN = [   # (pattern, replacement): how the voice reads the caption text; the on-screen captions are unchanged
    (r'\bv(\d+\.\d+)\b', r'version \1'),            # v4.22 -> version 4.22
    (r'\$([\d,]+)', r'\1 dollars'),                    # $5,800 -> 5,800 dollars (the voice would say "dollar five thousand")
    (r'\bBU\b', 'B U'), (r'\bCIP\b', 'C I P'), (r'\bBLEI\b', 'B L E I'),   # spelled out (the voice would say "boo", "sip", "blay")
    (r'\b2026\b', 'twenty twenty-six'),
    (r'harness\.js', 'harness dot J S'), (r'CONTRIBUTING\.md', 'contributing dot M D'), (r'\bdomtest\b', 'dom test'),
]

def spoken(text):
    for a, b in SPOKEN:
        text = re.sub(a, b, text)
    return text

def narrate(texts):
    """One mono clip per caption (float32 samples) and the sample rate; downloads the model on the first run."""
    import urllib.request
    try:
        from kokoro_onnx import Kokoro
    except ImportError:
        sys.exit('narration needs kokoro-onnx and soundfile (pip install kokoro-onnx soundfile), or build with --silent')
    os.makedirs(CACHE, exist_ok=True)
    for f in KOKORO_FILES:
        dst = os.path.join(CACHE, f)
        if not os.path.exists(dst):
            print('downloading %s (first run only)' % f, flush=True)
            urllib.request.urlretrieve(KOKORO_URL + f, dst + '.part'); os.replace(dst + '.part', dst)
    k = Kokoro(*[os.path.join(CACHE, f) for f in KOKORO_FILES])
    clips, sr = [], None
    for i, t in enumerate(texts):
        a, sr = k.create(spoken(t), voice=VOICE, speed=SPEED, lang='en-us')
        clips.append(a); print('voice %d of %d: %.1f s' % (i + 1, len(texts), len(a) / sr), flush=True)
    return clips, sr

def write_audio(clips, sr, durs, path):
    """Lay each clip at the start of its caption (after LEAD) on one silent track as long as the video; 16-bit mono WAV."""
    import numpy as np, soundfile as sf
    total = sum(durs); track = np.zeros(int(round(total * sr)) + sr, dtype=np.float32); t0 = 0.0
    for i, (a, d) in enumerate(zip(clips, durs)):
        at = int(round((t0 + (LEAD0 if i == 0 else LEAD)) * sr)); track[at:at + len(a)] += a; t0 += d
    peak = float(np.max(np.abs(track))) or 1.0
    sf.write(path, track[:int(round(total * sr))] * min(1.0, 0.89 / peak), sr, subtype='PCM_16')

# ---------------------------------------------------------------- the front door's data
def load_fd():
    html = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
    m = re.search(r'<script type="application/json" id="fd-data">(.*?)</script>', html, re.S)
    if not m:
        sys.exit('index.html has no #fd-data block: the walk-through describes the front door and cannot be built without it')
    return json.loads(m.group(1)), html

FD, HTML = load_fd()
ENGINE_VERSION = FD['_meta']['engine']
HEADLINE = re.sub(r'<[^>]+>', '', re.search(r'<h1 class="fd-q" id="fd-q">(.*?)</h1>', HTML, re.S).group(1)).strip()

def row(env, k, view='cost', model='engine'):
    rows = FD['envs'][env]['rows' if view == 'cost' else 'prop'][model]
    for r in rows:
        if r['k'] == k:
            return r
    sys.exit('no row %r in %s/%s/%s' % (k, env, view, model))

def dp(env, k, **kw): return row(env, k, **kw)['dp'][0]   # change in 20-year poverty severity (FGT2 x 100) vs no program
def cut(env, k, **kw): return '%.2f' % abs(dp(env, k, **kw))
def pct(x): return '%d%%' % round(x)
def worse_dollars(env, k, group, **kw):
    s = re.sub(r'<[^>]+>', '', row(env, k, **kw)['worse'])
    m = re.search(re.escape(group) + r'[^$]*\$([\d,]+) a year', s)
    return int(m.group(1).replace(',', '')) if m else None
def about(x, step):
    return '{:,}'.format(int(round(x / float(step)) * step))

V = {
    'ref_cco': cut('ref', 'cco'), 'ref_ubi': cut('ref', 'ubi'), 'ref_nit': cut('ref', 'nit'),
    'ref_corr': cut('ref', 'corr'), 'ref_top': cut('ref', 'top'),
    'adv_cco': cut('adv', 'cco'), 'adv_corr': cut('adv', 'corr'),
    'share_ref': pct(100 * (1 - dp('ref', 'corr') / dp('ref', 'cco'))),
    'share_adv': pct(100 * (1 - dp('adv', 'corr') / dp('adv', 'cco'))),
    'base_f0': pct(row('ref', 'base')['f0']), 'nit_f0': pct(row('ref', 'nit')['f0']),
    'nit_hrs': pct(abs(row('ref', 'nit')['hrs'])),
    'cco_nonpart': about(worse_dollars('ref', 'cco', 'Adults who chose not to take part') or 0, 100),
    'fw_cost': about(row('ref', 'cco', model='framework')['cost'], 1000),
    'fw_tau': pct(row('ref', 'cco', model='framework')['tau']),
    'agents': FD['_meta']['agents'],
}
ENVS = ('ref', 'adv', 'st')
CHECKS = {   # the conditions each caption's wording depends on
    'no inflation at reference': 'no inflation' in FD['envs']['ref']['name'],
    'Adverse has inflation': '2% inflation' in FD['envs']['adv']['name'],
    'mechanisms-off beats basic income in every environment': all(dp(e, 'corr') < dp(e, 'ubi') for e in ENVS),
    'negative income tax cuts more than mechanisms-off at reference': dp('ref', 'nit') < dp('ref', 'corr'),
    'negative income tax raises the share in poverty': row('ref', 'nit')['f0'] > row('ref', 'base')['f0'],
    'top-up cuts more than the flat design': dp('ref', 'top') < dp('ref', 'cco'),
    'non-participants bear the cost': worse_dollars('ref', 'cco', 'Adults who chose not to take part') is not None,
    'proposed basic income is $12,000': '$12,000' in row('ref', 'ubi', view='prop')['label'],
    'proposed NIT guarantee is $15,960': '$15,960' in row('ref', 'nit', view='prop')['label'],
    'live presets use 500 adults': 'agents:500' in HTML,
}

# ---------------------------------------------------------------- the tour
# state: tab ('cmp'/'live'), env, v ('cost'/'prop'), m ('engine'/'framework'), about (open the design panel)
# scroll: a selector brought to `off` CSS px below the top, or 0; dim: one element spotlit, the rest dimmed;
# mark: rows or cells outlined; hover: an element hovered (tooltips); card: a full-frame card instead of the page.
# Each caption is (text, [conditions from CHECKS its wording needs]).
CH = ['What the page is for', 'How Compassionism works', 'Reading the comparison', 'What the model finds so far',
      'Run a scenario yourself', 'Check the work', 'Help improve it']
ROWS = lambda *ks: ['#fd-rows tr[data-k="%s"]' % k for k in ks]

SHOTS = [
    dict(id='title', card='title', caps=[('A walk-through of the Compassionism Framework Simulation, v{ver}: what the page shows, how the model works, what it finds so far, and how to check it or help.', [])]),
    dict(id='headline', ch=1, scroll=0, dim='#fd-q', caps=[
        ('The first screen says what the tool is for: set Compassionism beside five other anti-poverty designs and see how each does on poverty and work.', [])]),
    dict(id='rules', ch=1, scroll=0, dim='.fd-sub', caps=[
        ('Every design runs on the same {agents} simulated adults for 20 years, is paid for the same way, and faces the same rules for how people respond.', [])]),
    dict(id='caveats', ch=1, scroll='#uncertainty-notice', off=12, dim='#uncertainty-notice', caps=[
        ('Read this first: it is an exploratory model, not a forecast. Its results show what its assumptions imply, not that the assumptions are true.', [])]),
    dict(id='design', ch=2, about=True, scroll='#fd-about-cco', off=16, dim='#fd-about-cco', caps=[
        ('Each participant receives a monthly allowance of Basic Units (BU): a restricted currency for essentials that expires if it is not used.', []),
        ('BU can be converted to dollars at elevated rates, set by market demand and by the quality of work the community validates through creative collectives.', []),
        ("A participant's octave is their conversion capacity: a safeguard against exploitation, and an open ceiling for creators whose work draws demand.", []),
        ('Wage work is still paid in dollars. Community-owned businesses and housing (PTF, PTH) lower living costs, zone coordination (SZH) adds a cooperative benefit, and a civic portal (CIP) runs the currency and the votes.', []),
        ("Taking part is open to every adult. In the model, 78% do at the reference settings, and each adult's choice holds for all 20 years.", [])]),
    dict(id='table', ch=3, scroll='.fd-tabs', off=8, mark=ROWS('cco'), caps=[
        ('Each row is a design. Cost is per adult per year, shown with the wage contribution that pays for it and the change in poverty per $1,000.', [])]),
    dict(id='measure', ch=3, scroll='.fd-tabs', off=8, hover='#fd-table thead th:nth-child(3) .abbr-link', caps=[
        ("The main measure is poverty severity: each adult's shortfall below a living-wage basket, squared so the deepest count most, averaged over 20 years.", []),
        ('Beside it: the final year alone, the share of adults in poverty, hours worked, and any group left worse off than with no program.', [])]),
    dict(id='controls', ch=3, scroll='.fd-tabs', off=8, dim='.fd-ctl', caps=[
        ('The controls switch the environment, compare the designs at equal cost or at the size their proponents propose, and model Compassionism as coded or as specified on the Hub.', [])]),
    dict(id='proposed', ch=3, v='prop', scroll='.fd-tabs', off=8, mark=ROWS('ubi', 'nit'), caps=[
        ('At proposed size, the basic income pays $12,000 a year and the negative income tax guarantees the 2026 poverty guideline for one adult, $15,960.',
         ['proposed basic income is $12,000', 'proposed NIT guarantee is $15,960'])]),
    dict(id='headline-result', ch=4, scroll='.fd-tabs', off=8, mark=ROWS('cco', 'ubi', 'nit'), caps=[
        ('At the reference settings and equal cost, Compassionism as coded cuts poverty severity by {ref_cco} points, against {ref_ubi} for a basic income and {ref_nit} for a negative income tax.', [])]),
    dict(id='mechanisms', ch=4, scroll='.fd-tabs', off=8, mark=ROWS('cco', 'corr'), caps=[
        ('The shaded row switches off two mechanisms that are theoretical, yet to be empirically tested, and cost nothing in the model: a yearly wage raise per octave, and slower inflation.', []),
        ('At reference, with no inflation, only the wage raise acts. Without it the cut falls from {ref_cco} to {ref_corr}, about {share_ref} less.', ['no inflation at reference'])]),
    dict(id='adverse', ch=4, env='adv', scroll='.fd-tabs', off=8, mark=ROWS('cco', 'corr'), caps=[
        ('In the Adverse Environment, with recessions and 2% inflation, the two carry about {share_adv} of the cut: {adv_cco} falls to {adv_corr}. The next round replaces them or switches them off.', ['Adverse has inflation'])]),
    dict(id='without', ch=4, scroll='.fd-tabs', off=8, mark=ROWS('corr', 'ubi'), caps=[
        ('Without them, Compassionism still does better than a basic income of equal cost, in all three environments.', ['mechanisms-off beats basic income in every environment'])]),
    dict(id='nit', ch=4, scroll='.fd-tabs', off=8, mark=ROWS('corr', 'nit'), caps=[
        ('The negative income tax cuts severity more at reference, {ref_nit}, by focusing on the deepest shortfalls, but it raises the share in poverty from {base_f0} to {nit_f0} and cuts hours by {nit_hrs}.',
         ['negative income tax cuts more than mechanisms-off at reference', 'negative income tax raises the share in poverty'])]),
    dict(id='topup', ch=4, scroll='.fd-tabs', off=8, mark=ROWS('cco', 'top'), caps=[
        ('A variant that moves a tenth of the flat allowance into a top-up for low earners cuts a little more: {ref_top}.', ['top-up cuts more than the flat design'])]),
    dict(id='who-pays', ch=4, scroll='.fd-tabs', off=8, mark=['#fd-rows tr[data-k="cco"] td:last-child', '#fd-rows tr[data-k="ubi"] td:last-child'], caps=[
        ('Someone always pays. Each design is funded by a contribution on wages; under Compassionism the cost falls mainly on adults who chose not to take part, about ${cco_nonpart} a year.',
         ['non-participants bear the cost'])]),
    dict(id='hub-scale', ch=4, m='framework', scroll='.fd-tabs', off=8, mark=ROWS('cco'), caps=[
        ('At the scale specified on the Hub, Compassionism costs about ${fw_cost} per adult a year, which would take a contribution of {fw_tau} of wages.', [])]),
    dict(id='limits', ch=4, scroll='#uncertainty-notice', off=12, dim='#uncertainty-notice', caps=[
        ('What the model cannot test: whether conversion rewards pay for new output (it has no production side), households and children, or savings from poverty removed.', [])]),
    dict(id='live', ch=5, tab='live', scroll='.fd-tabs', off=8, dim='.fd-chips', caps=[
        ("Compassionism's own scenarios run live in your browser: pick a preset, or change any control and press Run Simulation.", ['live presets use 500 adults'])]),
    dict(id='results', ch=5, tab='live', scroll='.layout', off=6, caps=[
        ("Each run follows {agents} adults year by year and reports poverty, wealth and the BLEI: how many days of basic living each adult's resources cover.", [])]),
    dict(id='panels', ch=5, tab='live', scroll='#sec-poverty4', off=20, caps=[
        ('Panels below show poverty by five measures, BLEI tiers over time, participants beside non-participants, and what each system contributes.', []),
        ("These live runs use the engine's own settings, not the comparison's testbed profile, so their figures differ from the table's.", [])]),
    dict(id='assumptions', ch=5, tab='live', scroll='#sec-assumptions', off=300, dim='#sec-assumptions', caps=[
        ('At the foot of the page: the assumptions, the ODD protocol, known limitations and references.', [])]),
    dict(id='replication', ch=6, url='replication.html', scroll=0, caps=[
        ('The Replication framework page holds the formulas, the calibration and the full version history.', [])]),
    dict(id='checks', ch=6, card='terminal', caps=[
        ('The simulation is one HTML file. harness.js runs the same engine from the command line; the comparison table comes from node harness.js testbed 500 a5 ref.', []),
        ('npm test runs the three checks, validate, unit and domtest, and GitHub runs them on every push.', [])]),
    dict(id='contribute', ch=7, card='contribute', caps=[
        ('Contributions most wanted: sources for the untested constants, scenario tests from places you know, reproductions, and critiques of the design.', []),
        ('Changes follow the project rules: the old behaviour stays behind a switch, results are compared on 500 paired seeds, and no constant is tuned to hit a target.', []),
        ('Open an issue or a pull request on GitHub. CONTRIBUTING.md explains how.', [])]),
    dict(id='end', card='end', caps=[('Open the simulation, read the code, and test the claims yourself.', [])]),
]

ALT = {  # alt text for the written tour's screenshots
    'headline': "The page's opening sentence, highlighted", 'rules': 'The subtitle: the rules every design shares, highlighted',
    'caveats': 'The "Read this first" caveats box, highlighted', 'design': "The design panel's description of Compassionism, highlighted",
    'table': "The comparison table at reference settings and equal cost, with Compassionism's row marked",
    'measure': 'The comparison table with the poverty-severity tooltip open', 'controls': "The table's controls, highlighted",
    'proposed': 'The proposed-size view, with the basic income and negative income tax rows marked',
    'headline-result': 'Compassionism, basic income and negative income tax rows marked, reference settings',
    'mechanisms': "Compassionism's row and the shaded row without its two theoretical mechanisms, marked",
    'adverse': 'The same two rows in the Adverse Environment', 'without': 'The mechanisms-off row and the basic income row, marked',
    'nit': 'The mechanisms-off row and the negative income tax row, marked', 'topup': "Compassionism's row and the needs-based top-up row, marked",
    'who-pays': 'The worse-off cells for Compassionism and the basic income, marked', 'hub-scale': 'Compassionism as specified on the Hub, marked',
    'limits': 'The caveats box, highlighted', 'live': "The live tab's scenario presets, highlighted",
    'results': 'The live simulation: controls on the left, results on the right', 'panels': 'The Poverty by five measures panel',
    'assumptions': 'The Assumptions, ODD Protocol and Known Limitations panel, highlighted', 'replication': 'The Replication framework page',
}

def fill(text):
    return text.format(ver=ENGINE_VERSION, **V)

def verify():
    bad = []
    for s in SHOTS:
        for text, needs in s['caps']:
            for n in needs:
                if not CHECKS[n]:
                    bad.append('shot %r, caption "%s...": "%s" no longer holds' % (s['id'], text[:60], n))
    if bad:
        sys.exit('The front door\'s data no longer supports these captions; rewrite them before rebuilding:\n  ' + '\n  '.join(bad))

# ---------------------------------------------------------------- page capture
SPOT_CSS = """
.wt-dim{position:relative!important;z-index:9000!important;outline:4px solid #F2B705!important;outline-offset:4px;
  box-shadow:0 0 0 200vmax rgba(8,16,14,.46)!important;border-radius:6px}
tr.wt-mark>td, td.wt-mark{background:rgba(242,183,5,.17)!important}
tr.wt-mark, td.wt-mark{outline:3px solid #D99A00!important;outline-offset:-3px}
"""

APPLY = """(s) => {
  document.querySelectorAll('.wt-dim,.wt-mark').forEach(e => e.classList.remove('wt-dim','wt-mark'));
  if (window.fdTab) fdTab(s.tab || 'cmp');
  if (window.fdSet) { fdSet('env', s.env || 'ref'); fdSet('v', s.v || 'cost'); fdSet('m', s.m || 'engine'); fdSet('sens', false); }
  const sens = document.getElementById('fd-sens'); if (sens) sens.checked = false;
  const ab = document.getElementById('fd-about'); if (ab) ab.open = !!s.about;
  const tw = document.querySelector('.fd-tw'); if (tw) tw.scrollTop = 0;
  if (s.scroll === 0 || s.scroll === undefined) window.scrollTo(0, 0);
  else { const e = document.querySelector(s.scroll); if (!e) return 'missing ' + s.scroll;
         if (e.tagName === 'DETAILS') e.open = false;
         window.scrollTo(0, e.getBoundingClientRect().top + window.scrollY - (s.off || 0)); }
  if (s.dim) { const e = document.querySelector(s.dim); if (!e) return 'missing ' + s.dim; e.classList.add('wt-dim'); }
  const marks = [];
  for (const sel of (s.mark || [])) { const e = document.querySelector(sel); if (!e) return 'missing ' + sel; e.classList.add('wt-mark'); marks.push(e); }
  if (marks.length) {   // bring every marked row into view, keeping as much of the table's head in view as possible
    const top = Math.min(...marks.map(e => e.getBoundingClientRect().top)), bot = Math.max(...marks.map(e => e.getBoundingClientRect().bottom));
    if (bot > window.innerHeight - 12) window.scrollBy(0, Math.min(top - 60, bot - window.innerHeight + 24));
    const b2 = Math.max(...marks.map(e => e.getBoundingClientRect().bottom));
    if (b2 > window.innerHeight + 4) return 'marked rows do not fit in the viewport';
  }
  return 'ok';
}"""

def serve(root):
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=root)
    handler.log_message = lambda *a: None
    httpd = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, 'http://127.0.0.1:%d/' % httpd.server_address[1]

def capture(pw, base):
    b = pw.chromium.launch()
    ctx = b.new_context(viewport={'width': VW, 'height': VH}, device_scale_factor=DSF, color_scheme='light')
    pg = ctx.new_page()
    shots, current = {}, None
    for s in SHOTS:
        if 'card' in s:
            continue
        url = base + s.get('url', 'index.html')
        if url != current:
            pg.goto(url, wait_until='networkidle'); pg.wait_for_timeout(3500)
            pg.add_style_tag(content=SPOT_CSS); current = url
        pg.mouse.move(2, VH - 2)
        state = {k: s[k] for k in ('tab', 'env', 'v', 'm', 'about', 'scroll', 'off', 'dim', 'mark') if k in s}
        res = pg.evaluate(APPLY, state)
        if res != 'ok':
            sys.exit('shot %r: %s' % (s['id'], res))
        pg.wait_for_timeout(500)
        if s.get('hover'):
            pg.hover(s['hover']); pg.wait_for_timeout(500)
        shots[s['id']] = pg.screenshot(type='png')
    b.close()
    return shots

# ---------------------------------------------------------------- frames
FONT = ("<link rel='stylesheet' href='https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&display=swap'>"
        "<style>*{box-sizing:border-box;margin:0}body{width:%dpx;height:%dpx;overflow:hidden;background:#0F1715;color:#E9F0EC;"
        "font-family:'Atkinson Hyperlegible','DejaVu Sans',system-ui,sans-serif}</style>" % (W, H))

def band(ch, text, progress):
    label = ('%d / %d · %s' % (ch, len(CH), CH[ch - 1])) if ch else ''
    return ("<div style='position:absolute;left:0;right:0;bottom:0;height:%dpx;background:#0F1715;padding:22px 64px 0'>"
            "<div style='font-size:22px;letter-spacing:.06em;text-transform:uppercase;color:#5CC2B6;font-weight:700;height:30px'>%s</div>"
            "<div style='font-size:38px;line-height:1.3;margin-top:8px;max-width:1790px'>%s</div>"
            "<div style='position:absolute;left:0;bottom:0;height:6px;width:%.1f%%;background:#5CC2B6'></div></div>") % (BAND, label, esc(text), 100 * progress)

def esc(t): return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def card_html(kind):
    if kind == 'title':
        return ("<div style='padding:150px 140px'><div style='font-size:30px;color:#5CC2B6;font-weight:700;letter-spacing:.06em;text-transform:uppercase'>A walk-through · v%s</div>"
                "<div style='font-size:92px;font-weight:700;line-height:1.05;margin-top:26px'>Compassionism<br>Framework Simulation</div>"
                "<div style='font-size:36px;line-height:1.45;margin-top:40px;color:#B9C8C2;max-width:1500px'>%s</div></div>") % (ENGINE_VERSION, esc(HEADLINE))
    if kind == 'end':
        items = [('Open the simulation', PAGE_URL), ('Code and checks', REPO_URL), ('Replication framework', PAGE_URL + 'replication.html'),
                 ('Archive', 'doi.org/10.17605/OSF.IO/QWTE2')]
        li = ''.join("<div style='margin-top:30px'><div style='font-size:28px;color:#5CC2B6;font-weight:700'>%s</div><div style='font-size:44px'>%s</div></div>" % (a, esc(b.replace('https://', ''))) for a, b in items)
        return "<div style='padding:120px 140px'><div style='font-size:72px;font-weight:700'>See for yourself</div>%s</div>" % li
    if kind == 'terminal':
        lines = [('$', 'git clone %s' % REPO_URL.replace('https://', 'https://')), ('$', 'cd compassionism-simulation && npm install'),
                 ('$', 'npm test'), ('', 'VALIDATION PASSED: the documented regressions and all preset fixtures reproduce exactly.'),
                 ('', '95 checks, all passed'), ('$', 'node harness.js testbed 500 a5 ref'), ('', '# the comparison table, reference environment, 500 paired seeds')]
        body = ''.join("<div style='white-space:pre'><span style='color:#5CC2B6'>%s </span>%s</div>" % (p, esc(t)) if p else
                       "<div style='white-space:pre;color:#98A8A2'>  %s</div>" % esc(t) for p, t in lines)
        return ("<div style='padding:90px 110px'><div style='font-size:30px;color:#5CC2B6;font-weight:700;letter-spacing:.06em;text-transform:uppercase'>Reproduce it</div>"
                "<div style='margin-top:30px;background:#16211E;border:2px solid #2A3935;border-radius:14px;padding:44px 50px;font:27px/1.75 \"DejaVu Sans Mono\",monospace'>%s</div></div>") % body
    if kind == 'contribute':
        ways = [('Scenario testing', 'Run conditions you know, export CSV or JSON, open an issue. The highest-value contribution.'),
                ('Calibration', 'Better sources for the constants in CFG, cited.'),
                ('Reproducibility', 'Same seed and settings, same result, in your browser.'),
                ('Model architecture', 'Critiques of the design and of how the model represents it.'),
                ('Code', 'One HTML file, no build step; npm test before a pull request.'),
                ('Peer review', 'Formal comments on the papers and the replication framework.')]
        cells = ''.join("<div style='background:#16211E;border:2px solid #2A3935;border-radius:12px;padding:26px 30px'><div style='font-size:34px;font-weight:700;color:#E9F0EC'>%s</div>"
                        "<div style='font-size:27px;line-height:1.4;color:#B9C8C2;margin-top:8px'>%s</div></div>" % w for w in ways)
        return ("<div style='padding:70px 110px'><div style='font-size:30px;color:#5CC2B6;font-weight:700;letter-spacing:.06em;text-transform:uppercase'>How to contribute · CONTRIBUTING.md</div>"
                "<div style='display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:32px'>%s</div></div>") % cells
    raise ValueError(kind)

def caption_list():
    return [(s, fill(t)) for s in SHOTS for t, _ in s['caps']]

def render_frames(pw, shots, tmp, voice=None):
    caps = caption_list()
    durs = [6.5 if s['id'] == 'title' else 7.0 if s['id'] == 'end' else max(MIN_S, len(t) / CPS + PAD) for s, t in caps]
    if voice:   # s39: a caption stays up for its reading time or its narration, whichever is longer
        clips, sr = voice
        durs = [max(d, (LEAD0 if i == 0 else LEAD) + len(a) / sr + TAIL) for i, (d, a) in enumerate(zip(durs, clips))]
    total, t0, frames, cues = sum(durs), 0.0, [], []
    b = pw.chromium.launch(); pg = b.new_page(viewport={'width': W, 'height': H})
    for i, ((s, text), d) in enumerate(zip(caps, durs)):
        if 'card' in s:
            top = "<div style='position:absolute;left:0;top:0;width:%dpx;height:%dpx'>%s</div>" % (W, H - BAND, card_html(s['card']))
        else:
            data = base64.b64encode(shots[s['id']]).decode()
            top = "<img src='data:image/png;base64,%s' style='position:absolute;left:0;top:0;width:%dpx;height:%dpx'>" % (data, W, H - BAND)
        pg.set_content('<html><head>%s</head><body>%s%s</body></html>' % (FONT, top, band(s.get('ch', 0), text, (t0 + d) / total)))
        pg.wait_for_timeout(250 if i else 1500)
        f = os.path.join(tmp, 'f%03d.png' % i); pg.screenshot(path=f); frames.append((f, d))
        cues.append((t0, t0 + d, text)); t0 += d
        print('frame %d of %d' % (i + 1, len(caps)), flush=True)
    b.close()
    return frames, cues, total, durs

def ts(t, sep):
    h, m, s = int(t // 3600), int(t % 3600 // 60), t % 60
    return '%02d:%02d:%06.3f' % (h, m, s) if sep == '.' else ('%02d:%02d:%06.3f' % (h, m, s)).replace('.', ',')

def write_captions(cues):
    with open(os.path.join(OUT, 'captions.vtt'), 'w', encoding='utf-8') as f:
        f.write('WEBVTT\n\n' + ''.join('%d\n%s --> %s\n%s\n\n' % (i + 1, ts(a, '.'), ts(b, '.'), t) for i, (a, b, t) in enumerate(cues)))
    with open(os.path.join(OUT, 'captions.srt'), 'w', encoding='utf-8') as f:
        f.write(''.join('%d\n%s --> %s\n%s\n\n' % (i + 1, ts(a, ','), ts(b, ','), t) for i, (a, b, t) in enumerate(cues)))

def build_video(frames, total, tmp, audio=None):
    lst = os.path.join(tmp, 'list.txt')
    with open(lst, 'w') as f:
        for p, d in frames:
            f.write("file '%s'\nduration %.3f\n" % (p, d))
        f.write("file '%s'\n" % frames[-1][0])
    vf = 'fps=15,fade=t=in:st=0:d=0.6,fade=t=out:st=%.2f:d=0.8,format=yuv420p' % (total - 0.8)
    aud = ['-i', audio, '-map', '0:v', '-map', '1:a', '-c:a', 'aac', '-b:a', '96k', '-af', 'afade=t=out:st=%.2f:d=0.8' % (total - 0.8)] if audio else []
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst] + aud + ['-vf', vf,
                    '-c:v', 'libx264', '-preset', 'medium', '-tune', 'stillimage', '-crf', '21', '-movflags', '+faststart', '-t', '%.3f' % total,
                    '-metadata', 'title=Compassionism Framework Simulation: a walk-through (v%s)' % ENGINE_VERSION,
                    os.path.join(OUT, 'walkthrough.mp4')], check=True)

def save_images(shots, poster):
    from PIL import Image   # Pillow: downscale and palettise the screenshots for the written tour
    if os.path.isdir(IMG):
        shutil.rmtree(IMG)
    os.makedirs(IMG)
    names = {}
    for n, s in enumerate([s for s in SHOTS if s['id'] in shots], 1):
        im = Image.open(io.BytesIO(shots[s['id']])).convert('RGB').resize((1280, 580), Image.LANCZOS)
        name = '%02d-%s.png' % (n, s['id'])
        im.quantize(colors=192, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(os.path.join(IMG, name), optimize=True)
        names[s['id']] = name
    Image.open(poster).convert('RGB').resize((960, 540), Image.LANCZOS).save(os.path.join(IMG, 'poster.jpg'), quality=86)
    return names

def write_tour(names, total):
    mins = '%d:%02d' % (total // 60, total % 60)
    out = ['# Walk-through: the Compassionism Framework Simulation (v%s)' % ENGINE_VERSION, '',
           '<!-- Written by walkthrough/make_walkthrough.py. Edit the captions there and rebuild; edits here are overwritten. -->', '',
           '[![The walk-through video](img/poster.jpg)](%s)' % VIDEO_URL, '',
           '**[Watch the walk-through](%s)** (%s, %s; [caption file](captions.vtt)). The same tour follows as text, one screenshot per step.' % (VIDEO_URL, mins, 'captions on screen, no sound' if SILENT else 'narrated by a synthetic voice, with captions'), '',
           'It covers what the page shows, how Compassionism works, what the model finds so far, how to run a scenario, how to check the work, and how to help. '
           'Every figure below is read from the page\'s own comparison data when the tour is built (`python3 walkthrough/make_walkthrough.py`), so it matches the page it was built from. '
           'The figures are results of the model under its stated assumptions, not forecasts.', '']
    for c, title in enumerate(CH, 1):
        out += ['## %d. %s' % (c, title), '']
        for s in [s for s in SHOTS if s.get('ch') == c]:
            if s['id'] in names:
                out += ['![%s](img/%s)' % (ALT.get(s['id'], s['id']), names[s['id']]), '']
            if s.get('card') == 'terminal':
                out += ['```', 'git clone %s' % REPO_URL, 'cd compassionism-simulation && npm install', 'npm test                              # validate, unit and domtest',
                        'node harness.js testbed 500 a5 ref    # the comparison table, reference environment', '```', '']
            if s.get('card') == 'contribute':
                out += ['Ways to contribute, from [CONTRIBUTING.md](../CONTRIBUTING.md#how-to-contribute): scenario testing (the highest-value contribution), '
                        'calibration with cited sources, reproducibility testing, model architecture feedback, code, and peer review.', '']
            out += [' '.join(fill(t) for t, _ in s['caps']), '']
    out += ['## Links', '', '- Simulation: %s' % PAGE_URL, '- Code and checks: %s' % REPO_URL, '- Replication framework: %sreplication.html' % PAGE_URL,
            '- Archive: https://doi.org/10.17605/OSF.IO/QWTE2', '']
    open(os.path.join(OUT, 'README.md'), 'w', encoding='utf-8').write('\n'.join(out))

def main():
    verify()
    from playwright.sync_api import sync_playwright
    if not shutil.which('ffmpeg'):
        sys.exit('ffmpeg is not on the PATH')
    httpd, base = serve(ROOT)
    tmp = tempfile.mkdtemp(prefix='walkthrough-')
    try:
        voice = None if SILENT else narrate([t for _, t in caption_list()])
        with sync_playwright() as pw:
            shots = capture(pw, base)
            frames, cues, total, durs = render_frames(pw, shots, tmp, voice)
        write_captions(cues)
        audio = None
        if voice:
            audio = os.path.join(tmp, 'voice.wav'); write_audio(voice[0], voice[1], durs, audio)
        build_video(frames, total, tmp, audio)
        names = save_images(shots, frames[0][0])
        write_tour(names, total)
        print('walk-through built: %d captions, %d:%02d, engine v%s, %s' % (len(cues), total // 60, total % 60, ENGINE_VERSION, 'no sound' if SILENT else 'voice ' + VOICE))
    finally:
        httpd.shutdown(); shutil.rmtree(tmp, ignore_errors=True)

if __name__ == '__main__':
    main()
