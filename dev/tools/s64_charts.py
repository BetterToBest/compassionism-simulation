#!/usr/bin/env python3
"""S64 part 3 (Nov 15, 2026): the round-2 charts the findings page needs (S65), from the tables tool's outputs in dev/runs/s64-round2/.

  python3 dev/tools/s64_charts.py [dev/runs/s64-round2]

Writes charts/ there: one specification-curve chart per headline outcome, design and horizon (spec-<design>-<key>-<years>.svg: the Source rows on top,
the financed rows beside them below, one column per environment), the backing curve per design and horizon (backing-<design>-<years>.svg), and
index.html, a preview of every chart with its caption and table links. Standard library only.

Every chart is static inline SVG (no script, no library), in the replication page's chart style (dev/tools/backing_chart.py): one y axis per panel,
never two; the three environments in the reference palette's first three categorical hues (validated light and dark), and always named by a label,
so colour never carries identity alone; a native tooltip (<title>) on every mark; the numbers behind every chart in a CSV or table beside it.
Specification curve: every preregistered reading of the outcome, sorted by its effect (the tables tool's rank), with its 95% seed interval; the main row
ringed and labelled, the least-favourable bound a diamond; the shaded band is rule 3's materiality around zero (an effect inside it is not material).
Backing curve: the effect at backed shares 0, 25, 50, 75 and 100% (100% is the main row, a design parameter, ledger D25); the mechanism's own point at
its realised backed share (main reading, and with no ceiling), and the break-even share where programme inflation is 5% a year (rule 4).
"""
import csv, html, json, os, sys

D = sys.argv[1] if len(sys.argv) > 1 else 'dev/runs/s64-round2'
OUT = os.path.join(D, 'charts')
S = json.load(open(os.path.join(D, 's64-summary.json')))
ENVS = [('ref', 'Reference', 's1', 'c'), ('adv', 'Adverse', 's2', 's'), ('str', 'Stress', 's3', 't')]
KEYS = [('bNAPy', 'Basic living: adults below 30 days of basic living', 'points'), ('fgt0PY', 'Basket poverty: adult-years with income below the basket', 'points'),
        ('ppovA', 'Wealth poverty: adults under $25,000, yearly average', 'points'), ('wtMedE', 'Median real wealth (weighted, year-0 dollars)', '$'),
        ('endoAnn', 'Programme inflation', 'points a year')]
DES = {'c22': 'the C2.2 design', 'rel': 'the release design'}
MINUS = '−'

STYLE = ('<style>.cv{--su:#fcfcfb;--ink:#0b0b0b;--ink2:#52514e;--grid:#e3e2dc;--axis:#9a9992;--band:#efeee9;--s1:#2a78d6;--s2:#eb6834;--s3:#1baf7a}'
         '@media (prefers-color-scheme:dark){:root:where(:not([data-theme="light"])) .cv{--su:#1a1a19;--ink:#fff;--ink2:#c3c2b7;--grid:#2c2c2a;--axis:#6f6e68;--band:#262624;--s1:#3987e5;--s2:#d95926;--s3:#199e70}}'
         ':root[data-theme="dark"] .cv{--su:#1a1a19;--ink:#fff;--ink2:#c3c2b7;--grid:#2c2c2a;--axis:#6f6e68;--band:#262624;--s1:#3987e5;--s2:#d95926;--s3:#199e70}'
         '.cv{font-family:system-ui,-apple-system,"Segoe UI",sans-serif}.cv .bg{fill:var(--su)}.cv .t{font-size:15px;font-weight:600;fill:var(--ink)}'
         '.cv .h{font-size:13px;font-weight:600;fill:var(--ink)}.cv .sub,.cv .tk,.cv .ax{font-size:11.5px;fill:var(--ink2)}.cv .tk{font-variant-numeric:tabular-nums}'
         '.cv .lab{font-size:11.5px;fill:var(--ink)}.cv .g{stroke:var(--grid);stroke-width:1}.cv .z{stroke:var(--axis);stroke-width:1}.cv .band{fill:var(--band)}'
         '.cv .iv{stroke-width:1;stroke-opacity:.55}.cv .d{stroke:var(--su);stroke-width:1}.cv .m{fill:var(--su);stroke:var(--ink);stroke-width:2}'
         '.cv .ln{fill:none;stroke-width:2}.cv .ref{stroke:var(--ink2);stroke-width:1;stroke-dasharray:4 3}.cv .hit{fill:transparent}'
         '.cv .s1{fill:var(--s1);stroke:var(--s1)}.cv .s2{fill:var(--s2);stroke:var(--s2)}.cv .s3{fill:var(--s3);stroke:var(--s3)}'
         '.cv .ls1{stroke:var(--s1)}.cv .ls2{stroke:var(--s2)}.cv .ls3{stroke:var(--s3)}.cv .o{fill:var(--su);stroke-width:2}</style>')


def esc(s):
    return html.escape(str(s), quote=True)


def num(x, unit, sign=True):
    """a figure as the reports print it, with a true minus sign"""
    if unit == '$':
        s = '{:,.0f}'.format(abs(x))
        s = '$' + s
    elif unit == '%':
        s = '{:.0f}%'.format(abs(x))
    else:
        s = '{:.1f}'.format(abs(x)) if abs(x) >= 1 or x == 0 else '{:.2f}'.format(abs(x))
    if x < 0 and s.strip('$0.,%') != '':
        return MINUS + s
    return ('+' if sign and x > 0 else '') + s


def tickfmt(tk, unit):
    if unit == '$':  # compact: $250k, $1M
        def f(t):
            a = abs(t)
            v = ('%gM' % (a / 1e6)) if a >= 1e6 else ('%gk' % (a / 1e3)) if a >= 1e3 else '%g' % a
            return (MINUS if t < 0 else '') + '$' + v
        return f
    if all(abs(t - round(t)) < 1e-9 for t in tk):
        return lambda t: (MINUS if t < 0 else '') + '{:.0f}'.format(abs(t))
    return lambda t: num(t, unit, False)


def ticks(lo, hi, n=4):
    """round tick values covering [lo, hi]"""
    import math
    span = hi - lo or abs(hi) or 1
    raw = span / n
    p = 10 ** math.floor(math.log10(raw))
    step = min((m * p for m in (1, 2, 2.5, 5, 10) if m * p >= raw), default=10 * p)
    t0 = math.floor(lo / step) * step
    out, t = [], t0
    while t <= hi + step * 1e-9:
        out.append(round(t, 10))
        t += step
    return out


def read_curve(blk, des, key, env, yrs):
    f = os.path.join(D, 'curves', '%s-%s-%s-%s-%d.csv' % (blk, des, key, env, yrs))
    if not os.path.exists(f):
        return None
    rows = list(csv.DictReader(open(f)))
    for r in rows:
        for k in ('rank', 'point'):
            r[k] = int(r[k])
        for k in ('estimate', 'lo95', 'hi95'):
            r[k] = float(r[k])
    rows.sort(key=lambda r: r['rank'])
    return rows, os.path.relpath(f, OUT)


def spec_chart(des, key, label, unit, yrs):
    W, PW, PH, L, TOP, GAPX, GAPY = 1000, 290, 190, 76, 84, 28, 74
    blocks = [('S', 'Paid for by the Source (main row: full backing, a design parameter)'), ('F', 'Paid for by a contribution (the financed rows)')]
    H = TOP + len(blocks) * (PH + GAPY) + 8
    o = ['<svg class="cv" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" aria-labelledby="t d">' % (W, H), STYLE,
         '<rect class="bg" width="%d" height="%d"/>' % (W, H)]
    title = '%s: %s against no programme, %d years' % (label, DES[des], yrs)
    o.append('<title id="t">%s</title>' % esc(title))
    desc, csvs = [], []
    o.append('<text class="t" x="16" y="24">%s</text>' % esc(title))
    o.append('<text class="sub" x="16" y="42">Each dot is one preregistered reading, sorted by its effect, with its 95%% seed interval (unit: %s).</text>' % esc(unit))
    o.append('<text class="sub" x="16" y="58">Ringed: the main row. Diamond: the least-favourable bound. Shaded: not material (rule 3). Below each panel: the curve\'s verdict (rule 2).</text>')
    for bi, (blk, bl) in enumerate(blocks):
        y0 = TOP + bi * (PH + GAPY) + 26
        data = {e: read_curve(blk, des, key, e, yrs) for e, *_ in ENVS}
        if not any(data.values()):
            continue
        vals = [v for d in data.values() if d for r in d[0] for v in (r['lo95'], r['hi95'])] + [0.0]
        thr = [S['curves'].get('%s-%s-%s-%s-%d' % (blk, des, key, e, yrs), {}).get('thr') for e, *_ in ENVS]
        thr = [t for t in thr if t]
        mt = max(thr) if thr else 0
        lo, hi = min(vals + [-mt]), max(vals + [mt])
        pad = (hi - lo) * 0.06 or 1
        lo, hi = lo - pad, hi + pad
        o.append('<text class="h" x="16" y="%d">%s</text>' % (y0 - 12, esc(bl)))
        tk = ticks(lo, hi)
        tf = tickfmt(tk, unit)
        lo, hi = min(lo, tk[0]), max(hi, tk[-1])
        Y = lambda v: y0 + PH - (v - lo) / (hi - lo) * PH
        for ci, (e, en, sc, _) in enumerate(ENVS):
            x0 = L + ci * (PW + GAPX)
            d = data[e]
            cs = S['curves'].get('%s-%s-%s-%s-%d' % (blk, des, key, e, yrs), {})
            for t in tk:
                o.append('<line class="g" x1="%d" x2="%d" y1="%.1f" y2="%.1f"/>' % (x0, x0 + PW, Y(t), Y(t)))
                if ci == 0:
                    o.append('<text class="tk" x="%d" y="%.1f" text-anchor="end" dominant-baseline="middle">%s</text>' % (x0 - 6, Y(t), esc(tf(t))))
            if cs.get('thr'):
                o.append('<rect class="band" x="%d" width="%d" y="%.1f" height="%.1f"><title>Not material: within %s of zero (rule 3)</title></rect>'
                         % (x0, PW, Y(cs['thr']), Y(-cs['thr']) - Y(cs['thr']), esc(num(cs['thr'], unit, False))))
            o.append('<line class="z" x1="%d" x2="%d" y1="%.1f" y2="%.1f"/>' % (x0, x0 + PW, Y(0), Y(0)))
            cls = cs.get('class', '')
            o.append('<text class="lab" x="%d" y="%d">%s</text>' % (x0, y0 - 0 + PH + 18, esc(en + (' · ' + cls if cls else ''))))
            if not d:
                o.append('<text class="sub" x="%d" y="%.1f">not run</text>' % (x0 + 8, y0 + PH / 2))
                continue
            rows, rel = d
            csvs.append(rel)
            n = len(rows)
            X = lambda i: x0 + 6 + (PW - 12) * (i / max(1, n - 1))
            main = None
            for i, r in enumerate(rows):
                x = X(i)
                tip = '%s, %s: %s (95%% %s to %s)' % (en, r['reading'], num(r['estimate'], unit), num(r['lo95'], unit, False), num(r['hi95'], unit, False))
                o.append('<g><title>%s</title><line class="iv l%s" x1="%.1f" x2="%.1f" y1="%.1f" y2="%.1f"/>' % (esc(tip), sc, x, x, Y(r['lo95']), Y(r['hi95'])))
                if r['kind'] == 'main':
                    main = (x, r)
                elif r['kind'] == 'bound':
                    yy = Y(r['estimate'])
                    o.append('<path class="o l%s" style="stroke:var(--%s)" d="M%.1f %.1fl4.5 4.5l-4.5 4.5l-4.5-4.5z"/>' % (sc, sc, x, yy - 4.5))
                else:
                    o.append('<circle class="d %s" cx="%.1f" cy="%.1f" r="2.6"/>' % (sc, x, Y(r['estimate'])))
                o.append('<rect class="hit" x="%.1f" y="%d" width="%.1f" height="%d"/></g>' % (x - max(2, (PW - 12) / max(1, n - 1) / 2), y0, max(4, (PW - 12) / max(1, n - 1)), PH))
            if main:
                x, r = main
                yy = Y(r['estimate'])
                o.append('<g><title>%s, main row: %s (95%% %s to %s)</title><circle class="m" cx="%.1f" cy="%.1f" r="5"/></g>'
                         % (esc(en), esc(num(r['estimate'], unit)), esc(num(r['lo95'], unit, False)), esc(num(r['hi95'], unit, False)), x, yy))
                up = yy - 10 if yy - 10 > y0 + 10 else yy + 18
                anchor = 'start' if x < x0 + PW - 90 else 'end'
                o.append('<text class="lab" x="%.1f" y="%.1f" text-anchor="%s">main %s</text>' % (x + (7 if anchor == 'start' else -7), up, anchor, esc(num(r['estimate'], unit))))
            desc.append('%s, %s: %s' % (bl.split(' (')[0], en, cs.get('sentence', '')))
    o.insert(3, '<desc id="d">%s</desc>' % esc(' '.join(desc)))
    o.append('</svg>')
    return '\n'.join(o), desc, csvs


def backing_chart(des, yrs):
    W, PW, PH, L, TOP, GAP = 1000, 370, 230, 62, 118, 130
    o = ['<svg class="cv" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" aria-labelledby="t d">' % (W, TOP + PH + 70), STYLE,
         '<rect class="bg" width="%d" height="%d"/>' % (W, TOP + PH + 70)]
    title = 'How much of the payout new output backs: %s, %d years' % (DES[des], yrs)
    o.append('<title id="t">%s</title>' % esc(title))
    o.append('<text class="t" x="16" y="24">%s</text>' % esc(title))
    o.append('<text class="sub" x="16" y="44">Effect against no programme at each backed share; 100% is the main row (a design parameter, ledger D25), not an estimate.</text>')
    o.append('<text class="sub" x="16" y="62">Hollow marks: the share the model\'s own backing mechanism reaches (main reading; with no ceiling). Diamonds on the 5% line: the break-even share (rule 4).</text>')
    lg = 16
    for e, en, sc, _ in ENVS:
        o.append('<line class="ln l%s" x1="%d" x2="%d" y1="84" y2="84"/><circle class="d %s" cx="%d" cy="84" r="4"/><text class="lab" x="%d" y="84" dominant-baseline="middle">%s</text>' % (sc, lg, lg + 22, sc, lg + 11, lg + 28, esc(en)))
        lg += 40 + 7 * len(en)
    panels = [('endoAnn', 'Programme inflation (points a year)', 'points a year'), ('ppovA', 'Wealth poverty, yearly average (points)', 'points')]
    desc, rows = [], []
    for pi, (key, pl, unit) in enumerate(panels):
        x0 = L + pi * (PW + GAP)
        series, vals = {}, [0.0]
        for e, en, sc, _ in ENVS:
            B = S['backing'].get('%s-%s-%d' % (des, e, yrs))
            if not B:
                continue
            pts = [(g['a'] * 100, g['eff'][key]) for g in B['grid']]
            mech = [(m['bkA']['est'], m['eff'][key], nm) for nm, m in B.get('mech', {}).items()]
            be = B.get('inflation5', {}).get('est')
            series[e] = (pts, mech, be if isinstance(be, (int, float)) else None)
            vals += [p[1]['lo'] for p in pts] + [p[1]['hi'] for p in pts] + [m[1]['est'] for m in mech]
            if key == 'endoAnn':
                rows.append((en, pts, mech, series[e][2]))
        if key == 'endoAnn':
            vals.append(5.0)
        lo, hi = min(vals), max(vals)
        tk = ticks(lo, hi)
        tf = tickfmt(tk, unit)
        lo, hi = min(lo, tk[0]), max(hi, tk[-1])
        Y = lambda v: TOP + PH - (v - lo) / (hi - lo) * PH
        X = lambda a: x0 + a / 100 * PW
        o.append('<text class="h" x="%d" y="%d">%s</text>' % (x0, TOP - 12, esc(pl)))
        for t in tk:
            o.append('<line class="g" x1="%d" x2="%d" y1="%.1f" y2="%.1f"/><text class="tk" x="%d" y="%.1f" text-anchor="end" dominant-baseline="middle">%s</text>'
                     % (x0, x0 + PW, Y(t), Y(t), x0 - 6, Y(t), esc(tf(t))))
        for a in (0, 25, 50, 75, 100):
            o.append('<text class="tk" x="%.1f" y="%d" text-anchor="middle">%d%%</text>' % (X(a), TOP + PH + 18, a))
        o.append('<text class="ax" x="%.1f" y="%d" text-anchor="middle">share of the payout backed by new output</text>' % (x0 + PW / 2, TOP + PH + 38))
        o.append('<line class="z" x1="%d" x2="%d" y1="%.1f" y2="%.1f"/>' % (x0, x0 + PW, Y(0), Y(0)))
        labs = []
        if key == 'endoAnn':
            o.append('<line class="ref" x1="%d" x2="%d" y1="%.1f" y2="%.1f"/><text class="sub" x="%d" y="%.1f" text-anchor="middle">5%% a year</text>' % (x0, x0 + PW, Y(5), Y(5), x0 + PW * 0.62, Y(5) - 6))
        for e, en, sc, shp in ENVS:
            if e not in series:
                continue
            pts, mech, be = series[e]
            o.append('<polyline class="ln l%s" points="%s"/>' % (sc, ' '.join('%.1f,%.1f' % (X(a), Y(v['est'])) for a, v in pts)))
            for a, v in pts:
                tip = '%s, %d%% backed: %s (95%% %s to %s)' % (en, a, num(v['est'], unit), num(v['lo'], unit, False), num(v['hi'], unit, False))
                o.append('<g><title>%s</title><circle class="d %s" cx="%.1f" cy="%.1f" r="4"/><circle class="hit" cx="%.1f" cy="%.1f" r="10"/></g>' % (esc(tip), sc, X(a), Y(v['est']), X(a), Y(v['est'])))
            for a, v, nm in mech:
                lab = 'mechanism, main reading' if nm.endswith('bkm') else 'mechanism, no ceiling'
                tip = '%s, %s: %.1f%% backed; %s' % (en, lab, a, num(v['est'], unit))
                o.append('<g><title>%s</title><circle class="o l%s" style="stroke:var(--%s)" cx="%.1f" cy="%.1f" r="5.5"/></g>' % (esc(tip), sc, sc, X(a), Y(v['est'])))
            if key == 'endoAnn' and be is not None:
                tip = '%s: programme inflation is 5%% a year at %.0f%% backed (break-even, rule 4)' % (en, be * 100)
                o.append('<g><title>%s</title><path class="%s d" d="M%.1f %.1fl5 5l-5 5l-5-5z"/></g>' % (esc(tip), sc, X(be * 100), Y(5) - 5))
            labs.append([Y(pts[-1][1]['est']), en])
        labs.sort()  # direct labels at the right end of each panel, pushed apart so they never overlap
        for i in range(1, len(labs)):
            labs[i][0] = max(labs[i][0], labs[i - 1][0] + 14)
        for yy, en in (labs if key != 'endoAnn' else []):  # inflation: every line ends at zero, so the legend names them
            o.append('<text class="lab" x="%.1f" y="%.1f" dominant-baseline="middle">%s</text>' % (X(100) + 10, yy, esc(en)))
        if key == 'endoAnn':
            desc += ['%s: inflation %s a year with no backing, %s at full backing; 5%% a year at %s backed; the mechanism reaches %s.' % (
                en, num(p[0][1]['est'], unit, False), num(p[-1][1]['est'], unit, False), ('%.0f%%' % (b * 100)) if b is not None else 'n/a',
                ' and '.join('%.1f%%' % m[0] for m in mc)) for en, p, mc, b in rows]
    o.insert(3, '<desc id="d">%s</desc>' % esc(' '.join(desc)))
    o.append('</svg>')
    return '\n'.join(o), desc, rows


def main():
    os.makedirs(OUT, exist_ok=True)
    page = []
    for des in ('c22', 'rel'):
        for yrs in (20, 40):
            svg, desc, rows = backing_chart(des, yrs)
            fn = 'backing-%s-%d.svg' % (des, yrs)
            open(os.path.join(OUT, fn), 'w').write(svg + '\n')
            t = ['<table><tr><th>Environment</th><th>0%</th><th>25%</th><th>50%</th><th>75%</th><th>100% (main)</th><th>Break-even (5% a year)</th><th>Mechanism reaches</th></tr>']
            for en, pts, mech, be in rows:
                t.append('<tr><td>%s</td>%s<td>%s</td><td>%s</td></tr>' % (en, ''.join('<td>%s</td>' % num(v['est'], 'x', False) for a, v in pts),
                                                                          '%.0f%%' % (be * 100) if be is not None else 'n/a', ' / '.join('%.1f%%' % m[0] for m in mech)))
            t.append('</table>')
            page.append((fn, ' '.join(desc), 'Programme inflation, points a year, by backed share:' + ''.join(t)))
    for key, label, unit in KEYS:
        for des in ('c22', 'rel'):
            for yrs in (20, 40):
                svg, desc, csvs = spec_chart(des, key, label, unit, yrs)
                fn = 'spec-%s-%s-%d.svg' % (des, key, yrs)
                open(os.path.join(OUT, fn), 'w').write(svg + '\n')
                page.append((fn, ' '.join(desc), 'Tables: ' + ', '.join('<a href="%s">%s</a>' % (esc(c), esc(os.path.basename(c))) for c in csvs)))
    css = ('<style>:root{--su:#fcfcfb;--ink:#0b0b0b;--ink2:#52514e;--grid:#e3e2dc}@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--su:#1a1a19;--ink:#fff;--ink2:#c3c2b7;--grid:#2c2c2a}}'
           ':root[data-theme="dark"]{--su:#1a1a19;--ink:#fff;--ink2:#c3c2b7;--grid:#2c2c2a}body{background:var(--su);color:var(--ink);font:15px/1.5 system-ui,sans-serif;margin:0 auto;max-width:1040px;padding:16px}'
           'figure{margin:28px 0}figcaption{color:var(--ink2);font-size:13px}img{width:100%;height:auto;border:1px solid var(--grid);border-radius:6px}'
           'table{border-collapse:collapse;font-size:12.5px;margin:6px 0;font-variant-numeric:tabular-nums;display:block;overflow-x:auto}td,th{border:1px solid var(--grid);padding:3px 7px;text-align:left}a{color:inherit}</style>')
    body = ['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Round 2 charts</title>', css, '</head><body>',
            '<h1>Round 2: the charts for the findings page</h1><p>Generated by <code>python3 dev/tools/s64_charts.py</code> from <code>dev/runs/s64-round2/</code> (engine 104691f, seeds 1-500). '
            'The SVGs carry their own light and dark colours and a tooltip on every mark when placed inline; embedded as images here, the tooltips do not show, and the tables give the numbers.</p>']
    for fn, desc, extra in page:
        body.append('<figure><img src="%s" alt="%s"><figcaption>%s<br>%s</figcaption></figure>' % (fn, esc(desc), esc(desc), extra))
    body.append('</body></html>')
    open(os.path.join(OUT, 'index.html'), 'w').write('\n'.join(body) + '\n')
    print('wrote %d charts and index.html to %s' % (len(page), OUT))


if __name__ == '__main__':
    main()
