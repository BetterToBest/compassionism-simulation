"""Audit E2 (v5.1, Oct 3, 2026): the backing-share curve, as one static chart on the replication page.

The page's decisive unknown is how much of what the Source pays out new output backs. The release row says none (a = 0), H1 says all of it (a = 1);
this sweeps the points in between on the same paired seeds. Inputs: dev/runs/backing-share-{ref,adv,st}.json, written by
    node harness.js testbed 500 backing ENV --json=dev/runs/backing-share-ENV.json          (one process per environment)
Usage: python3 dev/tools/backing_chart.py   (merges them into dev/runs/backing-share.json and rewrites the block between the markers
       <!-- backing-share:begin --> and <!-- backing-share:end --> in replication.html, creating it after the provenance line the first time)

The chart is inline SVG (no script, no library): two panels with a shared x axis, never one chart with two y axes. Left: the change in the share of adults
with too little wealth at the last year, against no programme (so the zero line is "no programme" and anything above it is worse), with the 95% interval of
the paired change. Right: the programme's own inflation a year. Three environments are the three categorical hues (first three slots of the reference
palette, validated in light and dark with the all-pairs check), told apart also by marker shape and by direct labels; a table of the numbers sits beside it.
"""
import json, re, sys

ENVS = [('ref', 'Reference'), ('adv', 'Adverse'), ('st', 'Stress Test')]
KEYS = ['a0', 'a25', 'a50', 'a75', 'a100']
MINUS = '−'

def load():
    out = None
    for e, _ in ENVS:
        d = json.load(open('dev/runs/backing-share-%s.json' % e))
        if out is None:
            out = {'_meta': dict(d['_meta']), 'envs': {}}
        if d['_meta'].get('manifest') != out['_meta'].get('manifest'):
            sys.exit('backing_chart: the manifests of the per-environment files differ; rerun all three from one commit')
        out['envs'][e] = d['envs'][e]
    out['_meta']['command'] = 'node harness.js testbed %d backing ref,adv,st (one process per environment: backing ref --json=dev/runs/backing-share-ref.json, and adv, st; then python3 dev/tools/backing_chart.py)' % out['_meta']['seeds']
    json.dump(out, open('dev/runs/backing-share.json', 'w'), indent=1)
    return out

def sg(x, d=1):
    s = ('%.' + str(d) + 'f') % abs(x)
    return ('+' if x > 0 and float(s) != 0 else MINUS if x < 0 and float(s) != 0 else '') + s

def crossing(pts):
    """linear interpolation of the share a at which the change in wealth poverty crosses zero (None if it does not)"""
    for (a0, y0), (a1, y1) in zip(pts, pts[1:]):
        if y0 > 0 >= y1 or y0 < 0 <= y1:
            return a0 + (a1 - a0) * (0 - y0) / (y1 - y0)
    return None

def panel(title, sub, ytitle, series, ymin, ymax, step, fmt, labels_at, whiskers, uid):
    """series: [(name, colour var, shape, [(a, y, lo, hi)])]"""
    W, H, L, R, T, B = 520, 348, 60, 96, 64, 58
    pw, ph = W - L - R, H - T - B
    X = lambda a: L + a * pw
    Y = lambda y: T + (ymax - y) / (ymax - ymin) * ph
    o = ['<svg viewBox="0 0 %d %d" role="img" aria-labelledby="%s-t %s-d" class="bs-svg">' % (W, H, uid, uid), '<title id="%s-t">%s</title>' % (uid, title)]
    desc = '; '.join('%s: %s' % (n, ', '.join('a = %s, %s' % (('%g' % p[0]), fmt(p[1])) for p in pts)) for n, c, s, pts in series)
    o.append('<desc id="%s-d">%s. %s</desc>' % (uid, ytitle, desc))
    o.append('<text x="%d" y="22" class="bs-t">%s</text>' % (L, title))
    o.append('<text x="%d" y="40" class="bs-sub">%s</text>' % (L, sub))
    y = ymin
    while y <= ymax + 1e-9:                                    # gridlines: hairline, solid, recessive; the zero line is the baseline
        base = abs(y) < 1e-9 and ymin < 0
        o.append('<line x1="%d" x2="%d" y1="%.1f" y2="%.1f" class="%s"/>' % (L, L + pw, Y(y), Y(y), 'bs-axis' if base else 'bs-grid'))
        o.append('<text x="%d" y="%.1f" class="bs-tick" text-anchor="end">%s</text>' % (L - 8, Y(y) + 4, fmt(y, True)))
        y += step
    for a in (0, 0.25, 0.5, 0.75, 1):
        o.append('<text x="%.1f" y="%d" class="bs-tick" text-anchor="middle">%d%%</text>' % (X(a), T + ph + 18, round(a * 100)))
    o.append('<text x="%.1f" y="%d" class="bs-ax" text-anchor="middle">Share of the Source&rsquo;s net payout backed by new output (a)</text>' % (L + pw / 2, H - 14))
    o.append('<text x="14" y="%.1f" class="bs-ax" text-anchor="middle" transform="rotate(-90 14 %.1f)">%s</text>' % (T + ph / 2, T + ph / 2, ytitle))
    if ymin < 0:
        o.append('<text x="%d" y="%.1f" class="bs-note">no programme</text>' % (L + pw + 8, Y(0) + 4))
    for n, c, shape, pts in series:
        poly = ' '.join('%.1f,%.1f' % (X(p[0]), Y(p[1])) for p in pts)
        o.append('<polyline points="%s" class="bs-line" style="stroke:var(%s)"/>' % (poly, c))
        if whiskers:
            for p in pts:
                o.append('<line x1="%.1f" x2="%.1f" y1="%.1f" y2="%.1f" class="bs-wh" style="stroke:var(%s)"/>' % (X(p[0]), X(p[0]), Y(p[2]), Y(p[3]), c))
        for p in pts:
            cx, cy = X(p[0]), Y(p[1])
            tip = '<title>%s, a = %g: %s</title>' % (n, p[0], fmt(p[1]) + ((' (95%% interval %s to %s)' % (fmt(p[2]), fmt(p[3]))) if whiskers else ''))
            if shape == 'circle':
                o.append('<circle cx="%.1f" cy="%.1f" r="4.5" class="bs-dot" style="fill:var(%s)">%s</circle>' % (cx, cy, c, tip))
            elif shape == 'square':
                o.append('<rect x="%.1f" y="%.1f" width="9" height="9" class="bs-dot" style="fill:var(%s)">%s</rect>' % (cx - 4.5, cy - 4.5, c, tip))
            else:
                o.append('<path d="M%.1f %.1fL%.1f %.1fL%.1f %.1fZ" class="bs-dot" style="fill:var(%s)">%s</path>' % (cx, cy - 5.5, cx + 5.5, cy + 4.5, cx - 5.5, cy + 4.5, c, tip))
        lp = pts[-1] if labels_at == 'right' else pts[0]
        if labels_at == 'right':
            o.append('<text x="%.1f" y="%.1f" class="bs-lab">%s</text>' % (X(lp[0]) + 12, Y(lp[1]) + 4, n))
        else:
            o.append('<text x="%.1f" y="%.1f" class="bs-lab">%s</text>' % (X(lp[0]) + 10, Y(lp[1]) - 9, n))
    o.append('</svg>')
    return '\n'.join(o)

CSS = """<style>
.bs-chart{--bs-surface:#fcfcfb;--bs-ink:#0b0b0b;--bs-ink2:#52514e;--bs-grid:#e3e2dc;--bs-axis:#9a9992;--bs-s1:#2a78d6;--bs-s2:#eb6834;--bs-s3:#1baf7a;background:var(--bs-surface);color:var(--bs-ink);border:1px solid var(--bs-grid);border-radius:10px;padding:14px 14px 10px;margin:.8rem 0}
@media (prefers-color-scheme:dark){:root:where(:not([data-theme="light"])) .bs-chart{--bs-surface:#1a1a19;--bs-ink:#fff;--bs-ink2:#c3c2b7;--bs-grid:#2c2c2a;--bs-axis:#6f6e68;--bs-s1:#3987e5;--bs-s2:#d95926;--bs-s3:#199e70}}
:root[data-theme="dark"] .bs-chart{--bs-surface:#1a1a19;--bs-ink:#fff;--bs-ink2:#c3c2b7;--bs-grid:#2c2c2a;--bs-axis:#6f6e68;--bs-s1:#3987e5;--bs-s2:#d95926;--bs-s3:#199e70}
.bs-panels{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:6px 18px}
.bs-svg{width:100%;height:auto;display:block;font-family:inherit}
.bs-t{font-size:13.5px;font-weight:600;fill:var(--bs-ink)}.bs-tick{font-size:11.5px;fill:var(--bs-ink2);font-variant-numeric:tabular-nums}.bs-ax{font-size:11.5px;fill:var(--bs-ink2)}
.bs-sub{font-size:11.5px;fill:var(--bs-ink2)}.bs-note{font-size:11.5px;fill:var(--bs-ink2)}.bs-lab{font-size:12.5px;fill:var(--bs-ink)}
.bs-grid{stroke:var(--bs-grid);stroke-width:1}.bs-axis{stroke:var(--bs-axis);stroke-width:1}
.bs-line{fill:none;stroke-width:2;stroke-linejoin:round;stroke-linecap:round}.bs-wh{stroke-width:1.5;stroke-opacity:.6}
.bs-dot{stroke:var(--bs-surface);stroke-width:2;paint-order:stroke}
.bs-legend{display:flex;flex-wrap:wrap;gap:4px 18px;margin:0 0 6px;font-size:13px;color:var(--bs-ink)}.bs-legend span{display:inline-flex;align-items:center;gap:6px}
.bs-key{width:14px;height:14px;display:inline-block}
.bs-cap{font-size:12.5px;color:var(--bs-ink2);margin:8px 2px 0;line-height:1.5}.bs-cap code{overflow-wrap:anywhere;white-space:normal}.bs-tw{overflow-x:auto;max-width:100%}
.bs-table{border-collapse:collapse;font-size:12.5px;margin:.5rem 0;font-variant-numeric:tabular-nums}.bs-table th,.bs-table td{border:1px solid var(--bs-grid);padding:.25rem .5rem;text-align:left}
@media (forced-colors:active){.bs-line,.bs-wh{stroke:CanvasText!important}.bs-dot{fill:CanvasText!important}}
</style>"""

def build(D):
    cols = {'ref': '--bs-s1', 'adv': '--bs-s2', 'st': '--bs-s3'}
    shapes = {'ref': 'circle', 'adv': 'square', 'st': 'triangle'}
    seeds, years = D['_meta']['seeds'], D['_meta']['years']
    wser, iser = [], []
    for e, nm in ENVS:
        E, R = D['envs'][e], D['envs'][e]['rows']
        wser.append((nm, cols[e], shapes[e], [(R[k]['a'], R[k]['dPov'][0], R[k]['dPov'][1], R[k]['dPov'][2]) for k in KEYS]))
        iser.append((nm, cols[e], shapes[e], [(R[k]['a'], R[k]['infl'], R[k]['infl'], R[k]['infl']) for k in KEYS]))
    lo = min(p[2] for s in wser for p in s[3]); hi = max(p[3] for s in wser for p in s[3])
    ymin = 10 * int((lo - 9.999) // 10); ymax = max(10, 10 * int((hi + 9.999) // 10))
    imax = max(10, 10 * int((max(p[1] for s in iser for p in s[3]) + 9.999) // 10))
    f1 = lambda y, tick=False: (('%d' % y) if y == 0 else sg(y, 0)) if tick else sg(y, 1) + ' points'
    f2 = lambda y, tick=False: ('%d%%' % y) if tick else '%.1f%% a year' % y
    A = panel('Wealth poverty against no programme', 'Adults with too little wealth, year %d. Above zero: worse.' % years, 'Change, percentage points', wser, ymin, ymax, 10, f1, 'right', True, 'bs-w')
    Bp = panel('Programme inflation', 'Price rise the programme itself causes (all three reach zero at a = 1).', 'Programme inflation, % a year', iser, 0, imax, 10, f2, 'left', False, 'bs-i')
    legend = '<div class="bs-legend" aria-label="Environments">' + ''.join(
        '<span><svg class="bs-key" viewBox="0 0 14 14" aria-hidden="true">%s</svg>%s</span>' % (
            {'circle': '<circle cx="7" cy="7" r="5" style="fill:var(%s)"/>', 'square': '<rect x="2" y="2" width="10" height="10" style="fill:var(%s)"/>', 'triangle': '<path d="M7 1.5L13 12.5H1Z" style="fill:var(%s)"/>'}[shapes[e]] % cols[e], nm) for e, nm in ENVS) + '</div>'
    # the words, from the numbers
    pts = {e: [(D['envs'][e]['rows'][k]['a'], D['envs'][e]['rows'][k]['dPov'][0]) for k in KEYS] for e, _ in ENVS}
    r0 = {e: D['envs'][e]['rows']['a0'] for e, _ in ENVS}; r1 = {e: D['envs'][e]['rows']['a100'] for e, _ in ENVS}
    def word(x): return 'worse' if x > 0 else 'better'
    s1 = 'At the release reading (a = 0) the share of adults with too little wealth at year %d changes against no programme by %s points in the Reference Environment, %s in the Adverse Environment and %s in the Stress Test (%s, %s and %s than no programme); at a = 1 (H1) by %s, %s and %s.' % (
        years, sg(r0['ref']['dPov'][0]), sg(r0['adv']['dPov'][0]), sg(r0['st']['dPov'][0]), word(r0['ref']['dPov'][0]), word(r0['adv']['dPov'][0]), word(r0['st']['dPov'][0]),
        sg(r1['ref']['dPov'][0]), sg(r1['adv']['dPov'][0]), sg(r1['st']['dPov'][0]))
    bits = []
    for e, nm in ENVS:
        c = crossing(pts[e])
        if c is None:
            bits.append('%s: %s than no programme at every point' % (nm, word(pts[e][0][1])))
        else:
            bits.append('%s: %s than no programme below a of about %.2f and %s above it' % (nm, 'worse' if pts[e][0][1] > 0 else 'better', c, 'better' if pts[e][0][1] > 0 else 'worse'))
    s2 = 'Where the change crosses zero (linear interpolation between the five points): ' + '; '.join(bits) + '.'
    s3 = 'Programme inflation falls from %.1f%%, %.1f%% and %.1f%% a year (Reference, Adverse, Stress Test) at a = 0 to %.1f%%, %.1f%% and %.1f%% at a = 1.' % (
        r0['ref']['infl'], r0['adv']['infl'], r0['st']['infl'], r1['ref']['infl'], r1['adv']['infl'], r1['st']['infl'])
    rows = ''.join('<tr><td>%s</td><td>%g%%</td><td>%s</td><td>%s</td><td>%s</td><td>%.1f%%</td><td>%.1f%%</td><td>%.1f%%</td></tr>' % (
        'Release row' if k == 'a0' else 'H1' if k == 'a100' else '', D['envs']['ref']['rows'][k]['a'] * 100,
        *['%s (%s to %s)' % (sg(D['envs'][e]['rows'][k]['dPov'][0]), sg(D['envs'][e]['rows'][k]['dPov'][1]), sg(D['envs'][e]['rows'][k]['dPov'][2])) for e, _ in ENVS],
        *[D['envs'][e]['rows'][k]['infl'] for e, _ in ENVS]) for k in KEYS)
    table = ('<details class="bs-details"><summary>Show the numbers</summary><div class="bs-tw"><table class="bs-table"><thead><tr><th>Reading</th><th>Backed share a</th><th>Reference: change in wealth poverty, points (95%% interval)</th><th>Adverse</th><th>Stress Test</th>'
             '<th>Reference: programme inflation a year</th><th>Adverse</th><th>Stress Test</th></tr></thead><tbody>%s</tbody></table></div></details>' % rows)
    head = ('<h3 id="backing-share">The decisive unknown: how much of what the Source pays out new output backs (audit E2, v5.1)</h3>\n  <p>The release row assumes none of the Source&rsquo;s net payout is backed by new output; H1 assumes all of it is. The model parameter <code>a</code> is the share in between. '
            'This sweeps it at 0, 0.25, 0.5, 0.75 and 1 on the same %d paired seeds of %d adults over %d years, in each environment, with every other mechanism as in the release row; the two end points are the release and H1 rows of the tables above, to the last digit. '
            'The whiskers are the 95%% interval of the paired change against no programme. It is a sweep of a design parameter, not a forecast: the Hub does not give the share, and nothing in the model fixes it.</p>' % (seeds, D['_meta']['agents'], years))
    cap = ('<p class="bs-cap">%s %s %s Reproduce: <code>%s</code></p>' % (s1, s2, s3, D['_meta']['command']))
    fig = ('<figure class="bs-chart" id="backing-chart" aria-label="Backing-share curve">%s%s\n<div class="bs-panels">\n%s\n%s\n</div></figure>' % (CSS, legend, A, Bp))
    return '<!-- backing-share:begin -->\n  ' + head + '\n  ' + fig + '\n  ' + cap + '\n  ' + table + '\n  <!-- backing-share:end -->'

D = load()
block = build(D)
P = open('replication.html').read()
if '<!-- backing-share:begin -->' in P:
    a = P.index('<!-- backing-share:begin -->'); b = P.index('<!-- backing-share:end -->') + len('<!-- backing-share:end -->')
    P = P[:a] + block + P[b:]
else:
    anchor = '<p id="rel-provenance">' if '<p id="rel-provenance">' in P else '<p id="rel-price-note">'
    a = P.index(anchor); b = P.index('</p>', a) + 4
    P = P[:b] + '\n  ' + block + P[b:]
open('replication.html', 'w').write(P)
print('backing-share block written:', len(block), 'bytes')
