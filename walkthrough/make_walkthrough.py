#!/usr/bin/env python3
"""Build the page walk-through from index.html and walkthrough/tour.json: a captioned, narrated video, its caption files and a written tour.

Run from the repository root:

    python3 walkthrough/make_walkthrough.py            # narrated (the default)
    python3 walkthrough/make_walkthrough.py --silent   # captions only, no sound

THE SCRIPT IS walkthrough/tour.json: edit the caption text there, never here and never in README.md (which this script
overwrites). walkthrough/UPDATING.md says how to change a sentence, add a shot or refresh the figures. Figures written
{like_this} in a caption are read from the page's own data (#rel-data in index.html) when the video is built, so a page
whose results were regenerated carries the new figures. A caption's "needs" lists conditions its wording depends on; the
build stops, naming the caption, if one no longer holds (for example "the gain is confirmed" after a result turns).

Needs Python 3.9+, ffmpeg on the PATH, and: pip install playwright pillow numpy kokoro-onnx soundfile, then
python -m playwright install chromium. The page loads Chart.js and its fonts from the web, so the build needs a network
connection. None of this is part of `npm test`: the simulation itself still needs nothing but a browser.

Narration (s39, d68): each caption is read aloud by the same synthetic voice as the first walk-through, Kokoro-82M
(Apache-2.0) through kokoro-onnx, voice af_heart, an American-English female voice. The model files (about 340 MB) are
downloaded on the first run into ~/.cache/compassionism-walkthrough/ and are not part of the repository. Each spoken
caption is cached there too, so after an edit only the changed captions are voiced again. A caption stays on screen for
its reading time or its narration, whichever is longer, so the captions, the voice and the video share one clock.
SPOKEN below says how the voice reads acronyms, file names and dollar figures; the captions themselves are unchanged.

Writes into walkthrough/: walkthrough.mp4, captions.vtt, captions.srt, README.md (the written tour) and img/ (one screenshot
per shot, plus the poster).
"""
import base64, functools, hashlib, http.server, io, json, os, re, shutil, subprocess, sys, tempfile, threading

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
    (r'\bH1\b', 'H 1'), (r'\bPTF\b', 'P T F'), (r'\bPTH\b', 'P T H'), (r'\bSZH\b', 'S Z H'),
    (r'\bBU\b', 'B U'), (r'\bCIP\b', 'C I P'), (r'\bBLEI\b', 'B L E I'),   # spelled out (the voice would say "boo", "sip", "blay")
    (r'\b2026\b', 'twenty twenty-six'),
    (r'harness\.js', 'harness dot J S'), (r'\bnpm\b', 'N P M'), (r'CONTRIBUTING\.md', 'contributing dot M D'), (r'\bdomtest\b', 'dom test'),
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
    import numpy as np
    cdir = os.path.join(CACHE, 'clips'); os.makedirs(cdir, exist_ok=True)
    clips, sr = [], None
    for i, t in enumerate(texts):   # a clip is cached by what is spoken, voice and speed, so an edit re-voices only that caption
        sp = spoken(t); key = hashlib.sha1(('%s|%s|%s' % (VOICE, SPEED, sp)).encode('utf-8')).hexdigest()[:20]; f = os.path.join(cdir, key + '.npz')
        if os.path.exists(f):
            z = np.load(f); a, sr = z['a'], int(z['sr']); tag = 'cached'
        else:
            a, sr = k.create(sp, voice=VOICE, speed=SPEED, lang='en-us'); np.savez(f, a=a, sr=sr); tag = 'new'
        clips.append(a); print('voice %d of %d: %.1f s (%s)' % (i + 1, len(texts), len(a) / sr, tag), flush=True)
    return clips, sr

def write_audio(clips, sr, durs, path):
    """Lay each clip at the start of its caption (after LEAD) on one silent track as long as the video; 16-bit mono WAV."""
    import numpy as np, soundfile as sf
    total = sum(durs); track = np.zeros(int(round(total * sr)) + sr, dtype=np.float32); t0 = 0.0
    for i, (a, d) in enumerate(zip(clips, durs)):
        at = int(round((t0 + (LEAD0 if i == 0 else LEAD)) * sr)); track[at:at + len(a)] += a; t0 += d
    peak = float(np.max(np.abs(track))) or 1.0
    sf.write(path, track[:int(round(total * sr))] * min(1.0, 0.89 / peak), sr, subtype='PCM_16')

# ---------------------------------------------------------------- the page's data and the script
HTML = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
_m = re.search(r'<script type="application/json" id="rel-data">(.*?)</script>', HTML, re.S)
if not _m:
    sys.exit('index.html has no #rel-data block: the walk-through describes the release results and cannot be built without it')
REL = json.loads(_m.group(1))
VERSION = re.search(r"VERSION:'([^']+)'", HTML).group(1)
HEADLINE = re.sub(r'<[^>]+>', '', re.search(r'<h1 class="fd-q" id="fd-q">(.*?)</h1>', HTML, re.S).group(1)).strip()
TOUR = json.load(open(os.path.join(OUT, 'tour.json'), encoding='utf-8'))
CH, SHOTS, ALT = TOUR['chapters'], TOUR['shots'], TOUR['alt']

def rel(env, k='release'): return REL['envs'][env]['rows'][k]
def base(env): return REL['envs'][env]['base']
def pct(x): return '%.1f%%' % x
def about(x, step): return '{:,}'.format(int(round(x / float(step)) * step))
R, A, S = rel('ref'), rel('adv'), rel('st')
V = {
    'ver': VERSION, 'agents': REL['_meta']['agents'],
    'ref_bo': pct(R['bOAPy']), 'base_bo': pct(base('ref')['bOAPy']),
    'ref_f0': pct(R['fgt0PY']), 'base_f0': pct(base('ref')['fgt0PY']),
    'ref_pov': pct(R['pov']), 'base_pov': pct(base('ref')['pov']),
    'ref_part': about(R['grp']['part'], 100), 'ref_non': about(abs(R['grp']['non']), 100),
    'ref_cost': about(R['cost'], 100), 'ref_infl': pct(R['infl']),
    'adv_bo': pct(A['bOAPy']), 'adv_base_bo': pct(base('adv')['bOAPy']), 'adv_pov': pct(A['pov']), 'adv_base_pov': pct(base('adv')['pov']),
    'st_bo': pct(S['bOAPy']), 'st_base_bo': pct(base('st')['bOAPy']), 'st_pov': pct(S['pov']), 'st_base_pov': pct(base('st')['pov']),
}
CHECKS = {   # the conditions each caption's wording depends on
    'reference confirmed gain': R['dBO'][0] < 0 and R['dF0'][0] < 0 and R['dPov'][0] < 0,
    'non-participants lose at reference': R['grp']['non'] < 0 < R['grp']['part'],
    'prices rise at reference': R['infl'] > 0,
    'H1 flat prices at reference': rel('ref', 'h1')['infl'] == 0 and rel('ref', 'h1')['dPov'][0] < R['dPov'][0],
    'adverse wealth worse': A['dBO'][0] < 0 and A['dPov'][0] > 0,
    'stress wealth worse': S['dBO'][0] < 0 and S['dPov'][0] > 0,
}

def fill(text): return text.format(**V)

def verify():
    bad = []
    for s in SHOTS:
        for c in s['caps']:
            for n in c.get('needs', []):
                if not CHECKS[n]:
                    bad.append('shot %r, caption "%s...": "%s" no longer holds' % (s['id'], c['t'][:60], n))
    if bad:
        sys.exit("The page's data no longer supports these captions; rewrite them in walkthrough/tour.json before rebuilding:\n  " + '\n  '.join(bad))

# ---------------------------------------------------------------- page capture
SPOT_CSS = """
.wt-dim{position:relative!important;z-index:9000!important;outline:4px solid #F2B705!important;outline-offset:4px;
  box-shadow:0 0 0 200vmax rgba(8,16,14,.46)!important;border-radius:6px}
tr.wt-mark>td, td.wt-mark{background:rgba(242,183,5,.17)!important}
tr.wt-mark, td.wt-mark{outline:3px solid #D99A00!important;outline-offset:-3px}
"""

APPLY = """(s) => {
  document.querySelectorAll('.wt-dim,.wt-mark').forEach(e => e.classList.remove('wt-dim','wt-mark'));
  relSet(s.env || 'ref');
  const mo = document.getElementById('rel-more'); if (mo) mo.open = !!s.more;
  const old = document.getElementById('fd-old'); if (old) old.open = false;
  const live = document.getElementById('rel-live-out'); if (live && !s.run) live.innerHTML = '';
  if (s.scroll === 0 || s.scroll === undefined) window.scrollTo(0, 0);
  else { const e = document.querySelector(s.scroll); if (!e) return 'missing ' + s.scroll;
         if (e.tagName === 'DETAILS' && !s.more) e.open = false;
         window.scrollTo(0, e.getBoundingClientRect().top + window.scrollY - (s.off || 0)); }
  if (s.dim) { const e = document.querySelector(s.dim); if (!e) return 'missing ' + s.dim; e.classList.add('wt-dim'); }
  const d = s.dim && document.querySelector(s.dim);
  if (d) { const r = d.getBoundingClientRect(); if (r.height > window.innerHeight - 24) return 'spotlit element is taller than the viewport: ' + s.dim; if (r.bottom > window.innerHeight - 8) window.scrollBy(0, r.bottom - window.innerHeight + 24); }
  return 'ok';
}"""

def launch(pw):
    """Chromium: Playwright's own build if installed, else a pre-installed one (PLAYWRIGHT_BROWSERS_PATH, the sandbox's /opt/pw-browsers)."""
    import glob
    try:
        return pw.chromium.launch()
    except Exception:
        found = sorted(glob.glob(os.path.join(os.environ.get('PLAYWRIGHT_BROWSERS_PATH', '/opt/pw-browsers'), 'chromium-*', 'chrome-linux*', 'chrome')))
        if not found:
            raise
        return pw.chromium.launch(executable_path=found[-1])

def serve(root):
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=root)
    handler.log_message = lambda *a: None
    httpd = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, 'http://127.0.0.1:%d/' % httpd.server_address[1]

def capture(pw, base):
    b = launch(pw)
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
        state = {k: s[k] for k in ('env', 'more', 'run', 'scroll', 'off', 'dim') if k in s}
        res = pg.evaluate(APPLY, state)
        if res != 'ok':
            sys.exit('shot %r: %s' % (s['id'], res))
        pg.wait_for_timeout(500)
        if s.get('run'):   # a fixed seed, so the live run on screen is the same every build
            pg.fill('#rel-seed', '42'); pg.click('#rel-run-btn'); pg.wait_for_selector('#rel-live-out .fd-note', timeout=120000); pg.wait_for_timeout(500)
            pg.evaluate(APPLY, state)
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
                "<div style='font-size:36px;line-height:1.45;margin-top:40px;color:#B9C8C2;max-width:1500px'>%s</div></div>") % (VERSION, esc(HEADLINE))
    if kind == 'end':
        items = [('Open the simulation', PAGE_URL), ('Code and checks', REPO_URL), ('Replication framework', PAGE_URL + 'replication.html'),
                 ('Archive', 'doi.org/10.17605/OSF.IO/QWTE2')]
        li = ''.join("<div style='margin-top:30px'><div style='font-size:28px;color:#5CC2B6;font-weight:700'>%s</div><div style='font-size:44px'>%s</div></div>" % (a, esc(b.replace('https://', ''))) for a, b in items)
        return "<div style='padding:120px 140px'><div style='font-size:72px;font-weight:700'>See for yourself</div>%s</div>" % li
    if kind == 'terminal':
        lines = [('$', 'git clone %s' % REPO_URL.replace('https://', 'https://')), ('$', 'cd compassionism-simulation && npm install'),
                 ('$', 'npm test'), ('', 'VALIDATION PASSED: the documented regressions and all preset fixtures reproduce exactly.'),
                 ('$', 'node harness.js testbed 500 release ref,adv,st'), ('', '# the figures on the page: 500 paired seeds, three environments')]
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
    return [(s, fill(c['t'])) for s in SHOTS for c in s['caps']]

def render_frames(pw, shots, tmp, voice=None):
    caps = caption_list()
    durs = [6.5 if s['id'] == 'title' else 7.0 if s['id'] == 'end' else max(MIN_S, len(t) / CPS + PAD) for s, t in caps]
    if voice:   # s39: a caption stays up for its reading time or its narration, whichever is longer
        clips, sr = voice
        durs = [max(d, (LEAD0 if i == 0 else LEAD) + len(a) / sr + TAIL) for i, (d, a) in enumerate(zip(durs, clips))]
    total, t0, frames, cues = sum(durs), 0.0, [], []
    b = launch(pw); pg = b.new_page(viewport={'width': W, 'height': H})
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
                    '-metadata', 'title=Compassionism Framework Simulation: a walk-through (v%s)' % VERSION,
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
    out = ['# Walk-through: the Compassionism Framework Simulation (v%s)' % VERSION, '',
           '<!-- Written by walkthrough/make_walkthrough.py. Edit the captions there and rebuild; edits here are overwritten. -->', '',
           '[![The walk-through video](img/poster.jpg)](%s)' % VIDEO_URL, '',
           '**[Watch the walk-through](%s)** (%s, %s; [caption file](captions.vtt)). The same tour follows as text, one screenshot per step.' % (VIDEO_URL, mins, 'captions on screen, no sound' if SILENT else 'narrated by a synthetic voice, with captions'), '',
           'It covers what the page shows, how Compassionism works, what the model finds so far (including where the gain is not confirmed), how to run a scenario, what the model cannot tell you, how to check the work, and how to help. '
           'Every figure below is read from the page\'s own results data when the tour is built (`python3 walkthrough/make_walkthrough.py`; the script is `tour.json`, see [UPDATING.md](UPDATING.md)), so it matches the page it was built from. '
           'The figures are results of the model under its stated assumptions, not forecasts.', '']
    for c, title in enumerate(CH, 1):
        out += ['## %d. %s' % (c, title), '']
        for s in [s for s in SHOTS if s.get('ch') == c]:
            if s['id'] in names:
                out += ['![%s](img/%s)' % (ALT.get(s['id'], s['id']), names[s['id']]), '']
            if s.get('card') == 'terminal':
                out += ['```', 'git clone %s' % REPO_URL, 'cd compassionism-simulation && npm install', 'npm test                              # validate, unit and domtest',
                        'node harness.js testbed 500 release ref,adv,st   # the page\'s figures', '```', '']
            if s.get('card') == 'contribute':
                out += ['Ways to contribute, from [CONTRIBUTING.md](../CONTRIBUTING.md#how-to-contribute): scenario testing (the highest-value contribution), '
                        'calibration with cited sources, reproducibility testing, model architecture feedback, code, and peer review.', '']
            out += [' '.join(fill(c['t']) for c in s['caps']), '']
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
        print('walk-through built: %d captions, %d:%02d, v%s, %s' % (len(cues), total // 60, total % 60, VERSION, 'no sound' if SILENT else 'voice ' + VOICE))
    finally:
        httpd.shutdown(); shutil.rmtree(tmp, ignore_errors=True)

if __name__ == '__main__':
    main()
