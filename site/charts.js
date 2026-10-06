/* Compassionism Simulation: shared charts (v5.2.1, Oct 2026). Hand-written SVG, no library.
 * Used by the simulation page (index.html), the findings explorer (findings.html) and the replication page; the compare page will reuse it.
 * Two primitives cover every chart on the pages:
 *   CSC.xy(el, spec)    lines over x (years, or a share), with optional bands (10th-90th percentile), whiskers (95% intervals), extra marks and a zero line;
 *   CSC.rows(el, spec)  one row per item with dots (with / without / a reading), intervals, reference lines and shaded target strips (dumbbells, range charts).
 * Colours come from CSS custom properties in site/findings.css (validated for colour-blind readers in light and dark, dataviz skill validator);
 * identity is never colour alone: series also differ by line style or marker shape and carry a legend and direct labels. Every chart has a text
 * summary (aria-label) and its numbers in a table beside it (site/findings.js). Tooltips enhance, never gate.
 * Numbers a chart prints from the release data carry data-src / data-f, so the figure check can compare them with the data file. */
(function (root) {
  'use strict';
  var NS = 'http://www.w3.org/2000/svg';
  function el(name, attrs, parent) { var e = document.createElementNS(NS, name); if (attrs) for (var k in attrs) if (attrs[k] !== undefined && attrs[k] !== null) e.setAttribute(k, attrs[k]); if (parent) parent.appendChild(e); return e; }
  function txt(parent, x, y, s, attrs) { var t = el('text', Object.assign({x: x, y: y}, attrs || {}), parent); t.textContent = s; return t; }
  function title(parent, x, y, s, maxW) {  /* an axis title, broken onto two lines when it would not fit the chart's width (about 6 px a character) */
    var t = el('text', {x: x, y: y, class: 'fx-axis-t', 'text-anchor': 'middle'}, parent);
    if (s.length*6 <= maxW) { t.textContent = s; return 0; }
    var mid = Math.floor(s.length/2), cut = s.lastIndexOf(' ', mid); if (cut < 0) cut = s.indexOf(' ', mid); if (cut < 0) { t.textContent = s; return 0; }
    var a = el('tspan', {x: x, dy: 0}, t); a.textContent = s.slice(0, cut); var b = el('tspan', {x: x, dy: 13}, t); b.textContent = s.slice(cut + 1); return 13; }
  function nice(lo, hi, n) {  /* round tick steps: 1, 2, 2.5, 5 x 10^k */
    if (hi - lo < 1e-9) { hi = lo + 1; }
    var span = hi - lo, raw = span/(n || 5), p = Math.pow(10, Math.floor(Math.log10(raw))), m = raw/p, step = (m <= 1 ? 1 : m <= 2 ? 2 : m <= 2.5 ? 2.5 : m <= 5 ? 5 : 10)*p;
    var a = Math.floor(lo/step)*step, b = Math.ceil(hi/step)*step, t = []; for (var v = a; v <= b + step*1e-6; v += step) t.push(+v.toFixed(10));
    return {lo: a, hi: b, ticks: t, step: step};
  }
  function width(host) { var w = host.clientWidth || (host.parentNode && host.parentNode.clientWidth) || 640; return Math.max(280, Math.min(w, 1100)); }
  var tipEl = null;
  function tip() { if (!tipEl) { tipEl = document.createElement('div'); tipEl.className = 'fx-tip'; tipEl.setAttribute('role', 'status'); tipEl.setAttribute('aria-live', 'polite'); document.body.appendChild(tipEl); } return tipEl; }
  function showTip(html, x, y) { var t = tip(); t.innerHTML = html; t.classList.add('on'); var r = t.getBoundingClientRect(), vw = window.innerWidth || 800;
    var left = Math.min(Math.max(8, x - r.width/2), vw - r.width - 8), top = y - r.height - 12; if (top < 8) top = y + 16; t.style.left = left + 'px'; t.style.top = top + 'px'; }
  function hideTip() { if (tipEl) tipEl.classList.remove('on'); }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
  function marker(g, shape, x, y, r, cls, hollow) {  /* circle, square, triangle, diamond; hollow = outline only */
    var a = {class: cls + (hollow ? ' fx-hollow' : '')}, m;
    if (shape === 'square') m = el('rect', Object.assign(a, {x: x - r*0.9, y: y - r*0.9, width: r*1.8, height: r*1.8, rx: 1}), g);
    else if (shape === 'triangle') m = el('path', Object.assign(a, {d: 'M' + x + ' ' + (y - r*1.15) + 'L' + (x + r*1.1) + ' ' + (y + r*0.85) + 'L' + (x - r*1.1) + ' ' + (y + r*0.85) + 'Z'}), g);
    else if (shape === 'diamond') m = el('path', Object.assign(a, {d: 'M' + x + ' ' + (y - r*1.25) + 'L' + (x + r*1.25) + ' ' + y + 'L' + x + ' ' + (y + r*1.25) + 'L' + (x - r*1.25) + ' ' + y + 'Z'}), g);
    else m = el('circle', Object.assign(a, {cx: x, cy: y, r: r}), g);
    return m;
  }
  function legend(host, items) {  /* items: {label, cls, shape, line, dash, hollow, band} */
    var L = document.createElement('div'); L.className = 'fx-legend';
    items.forEach(function (it) { var s = document.createElement('span'), sv = el('svg', {width: 22, height: 14, viewBox: '0 0 22 14', 'aria-hidden': 'true'});
      if (it.band) el('rect', {x: 1, y: 2, width: 20, height: 10, class: it.cls + ' fx-band'}, sv);
      if (it.line) el('line', {x1: 1, y1: 7, x2: 21, y2: 7, class: it.cls + ' fx-line' + (it.dash ? ' fx-dash' : '')}, sv);
      if (it.shape) marker(sv, it.shape, 11, 7, 4, it.cls + ' fx-mk', it.hollow);
      s.appendChild(sv); s.appendChild(document.createTextNode(it.label)); L.appendChild(s); });
    host.appendChild(L); return L;
  }

  /* CSC.xy(host, spec)
   * spec: {x: [values], xLabel(v) -> tick text, xTitle, yTitle, yFmt(v) -> tick text, tipFmt(v) -> value text in the tooltip, label (aria summary),
   *        series: [{name, cls, dash, shape, values: [y|null], band: {lo:[], hi:[]}, ci: {lo:[], hi:[]}, endLabel: true}],
   *        extra: [{name, cls, shape, x, y, hollow}], zero: true, yMin, yMax, height, xTicks: [values], refs: [{y, label}]} */
  function xy(host, spec) {
    host.innerHTML = '';
    var W = width(host), H = spec.height || Math.round(Math.min(340, Math.max(220, W*0.5))), m = {l: 52, r: spec.endLabels === false ? 16 : Math.min(118, W*0.24), t: 14, b: 40};
    if (W < 420) m.r = spec.endLabels === false ? 12 : 84;
    var xs = spec.x, ys = [];
    spec.series.forEach(function (s) { s.values.forEach(function (v, i) { if (v != null) ys.push(v); if (s.band) { ys.push(s.band.lo[i]); ys.push(s.band.hi[i]); } if (s.ci) { ys.push(s.ci.lo[i]); ys.push(s.ci.hi[i]); } }); });
    (spec.extra || []).forEach(function (p) { ys.push(p.y); });
    (spec.refs || []).forEach(function (r) { ys.push(r.y); });
    if (spec.zero) ys.push(0);
    var lo = spec.yMin != null ? spec.yMin : Math.min.apply(null, ys), hi = spec.yMax != null ? spec.yMax : Math.max.apply(null, ys), Y = nice(lo, hi, H < 260 ? 4 : 5);
    var x0 = Math.min.apply(null, xs), x1 = Math.max.apply(null, xs);
    var sx = function (v) { return m.l + (x1 === x0 ? 0.5 : (v - x0)/(x1 - x0))*(W - m.l - m.r); }, sy = function (v) { return m.t + (1 - (v - Y.lo)/(Y.hi - Y.lo))*(H0 - m.t - m.b); }, H0 = H;
    var svg = el('svg', {class: 'fx-svg', viewBox: '0 0 ' + W + ' ' + H, width: W, height: H, role: 'img', 'aria-label': spec.label || ''}, host);
    var g = el('g', {class: 'fx-grid'}, svg);
    Y.ticks.forEach(function (t) { el('line', {x1: m.l, x2: W - m.r, y1: sy(t), y2: sy(t), class: t === 0 && spec.zero ? 'fx-zero' : ''}, g); txt(g, m.l - 8, sy(t) + 4, spec.yFmt ? spec.yFmt(t) : String(t), {class: 'fx-tick', 'text-anchor': 'end'}); });
    var xt = spec.xTicks || xs.filter(function (v, i) { var n = xs.length, k = n > 30 ? 10 : n > 12 ? 5 : n > 6 ? 2 : 1; return i === 0 || (v % k === 0) || i === n - 1; });
    xt.forEach(function (v) { txt(g, sx(v), H0 - m.b + 18, spec.xLabel ? spec.xLabel(v) : String(v), {class: 'fx-tick', 'text-anchor': 'middle'}); });
    if (spec.xTitle) { var extra = title(g, m.l + (W - m.l - m.r)/2, H - 4, spec.xTitle, W - 16); if (extra) { H += extra; svg.setAttribute('viewBox', '0 0 ' + W + ' ' + H); svg.setAttribute('height', H); } }
    if (spec.yTitle) txt(g, m.l - 44, m.t - 2, spec.yTitle, {class: 'fx-axis-t'});
    (spec.refs || []).forEach(function (r) { el('line', {x1: m.l, x2: W - m.r, y1: sy(r.y), y2: sy(r.y), class: 'fx-ref'}, svg); if (r.label) txt(svg, W - m.r - 4, sy(r.y) - 5, r.label, {class: 'fx-tick', 'text-anchor': 'end'}); });
    var path = function (vals) { var d = '', pen = false; vals.forEach(function (v, i) { if (v == null) { pen = false; return; } d += (pen ? 'L' : 'M') + sx(xs[i]).toFixed(1) + ' ' + sy(v).toFixed(1); pen = true; }); return d; };
    spec.series.forEach(function (s) {
      if (s.band) { var d = ''; xs.forEach(function (x, i) { d += (i ? 'L' : 'M') + sx(x).toFixed(1) + ' ' + sy(s.band.hi[i]).toFixed(1); }); for (var i = xs.length - 1; i >= 0; i--) d += 'L' + sx(xs[i]).toFixed(1) + ' ' + sy(s.band.lo[i]).toFixed(1); el('path', {d: d + 'Z', class: s.cls + ' fx-band'}, svg); } });
    spec.series.forEach(function (s) {
      el('path', {d: path(s.values), class: s.cls + ' fx-line' + (s.dash ? ' fx-dash' : '')}, svg);
      if (s.ci) xs.forEach(function (x, i) { if (s.values[i] == null) return; el('line', {x1: sx(x), x2: sx(x), y1: sy(s.ci.lo[i]), y2: sy(s.ci.hi[i]), class: s.cls + ' fx-whisker'}, svg); });
      if (s.shape) xs.forEach(function (x, i) { if (s.values[i] != null) marker(svg, s.shape, sx(x), sy(s.values[i]), 4, s.cls + ' fx-mk', s.hollow); });
    });
    (spec.extra || []).forEach(function (p) { marker(svg, p.shape || 'diamond', sx(p.x), sy(p.y), 4.5, p.cls + ' fx-mk', p.hollow); });
    if (spec.endLabels !== false) {  /* direct labels at the right end, moved apart only by a leader line when they would collide */
      var ends = spec.series.filter(function (s) { return s.endLabel !== false; }).map(function (s) { var i = s.values.length - 1; while (i > 0 && s.values[i] == null) i--; return {s: s, y: sy(s.values[i]), y0: sy(s.values[i]), x: sx(xs[i])}; }).sort(function (a, b) { return a.y - b.y; });
      for (var k = 1; k < ends.length; k++) if (ends[k].y - ends[k - 1].y < 14) ends[k].y = ends[k - 1].y + 14;
      ends.forEach(function (e) { if (Math.abs(e.y - e.y0) > 2) el('line', {x1: e.x + 3, y1: e.y0, x2: e.x + 9, y2: e.y - 4, class: 'fx-leader'}, svg); var t = txt(svg, e.x + 10, e.y, e.s.name, {class: 'fx-endlbl'}); t.setAttribute('dominant-baseline', 'middle'); });
    }
    /* crosshair: follows the pointer, snaps to the nearest x; arrow keys move it when the chart has focus */
    var cross = el('line', {class: 'fx-cross', y1: m.t, y2: H0 - m.b, x1: m.l, x2: m.l, visibility: 'hidden'}, svg), hit = el('rect', {x: m.l, y: m.t, width: W - m.l - m.r, height: H0 - m.t - m.b, class: 'fx-hit'}, svg), cur = -1;
    function at(i, cx, cy) { cur = i; var x = sx(xs[i]); cross.setAttribute('x1', x); cross.setAttribute('x2', x); cross.setAttribute('visibility', 'visible');
      var rows = spec.series.map(function (s) { var v = s.values[i]; if (v == null) return ''; return '<div class="fx-tip-r"><i class="fx-key ' + s.cls + (s.dash ? ' fx-dash' : '') + '"></i><b>' + esc(spec.tipFmt ? spec.tipFmt(v) : v) + '</b> ' + esc(s.name) +
        (s.band ? ' <small>(' + esc(spec.tipFmt ? spec.tipFmt(s.band.lo[i]) : s.band.lo[i]) + '–' + esc(spec.tipFmt ? spec.tipFmt(s.band.hi[i]) : s.band.hi[i]) + ')</small>' : '') + (s.ci ? ' <small>(' + esc(spec.tipFmt(s.ci.lo[i])) + ' to ' + esc(spec.tipFmt(s.ci.hi[i])) + ')</small>' : '') + '</div>'; }).join('');
      var b = svg.getBoundingClientRect(); showTip('<div class="fx-tip-h">' + esc(spec.xLabel ? spec.xLabel(xs[i], true) : xs[i]) + '</div>' + rows, cx != null ? cx : b.left + x*(b.width/W), cy != null ? cy : b.top + m.t*(b.height/H) + 10); }
    function nearest(ev) { var b = svg.getBoundingClientRect(), x = (ev.clientX - b.left)*(W/b.width), best = 0, d = 1e9; xs.forEach(function (v, i) { var e = Math.abs(sx(v) - x); if (e < d) { d = e; best = i; } }); return best; }
    hit.addEventListener('pointermove', function (ev) { at(nearest(ev), ev.clientX, ev.clientY); });
    hit.addEventListener('pointerleave', function () { cross.setAttribute('visibility', 'hidden'); hideTip(); });
    host.tabIndex = 0; host.setAttribute('role', 'group'); host.setAttribute('aria-label', (spec.label || 'Chart') + '. Use the left and right arrow keys to read each point.');
    host.onkeydown = function (ev) { if (ev.key !== 'ArrowRight' && ev.key !== 'ArrowLeft') return; ev.preventDefault(); var i = cur < 0 ? (ev.key === 'ArrowRight' ? 0 : xs.length - 1) : Math.max(0, Math.min(xs.length - 1, cur + (ev.key === 'ArrowRight' ? 1 : -1))); at(i); };
    host.onblur = function () { hideTip(); cross.setAttribute('visibility', 'hidden'); cur = -1; };
    if (spec.legend !== false) legend(host, spec.series.map(function (s) { return {label: s.name, cls: s.cls, line: true, dash: s.dash, shape: s.shape, hollow: s.hollow, band: !!s.band && !s.values.length}; }).concat(spec.legendExtra || []));
    return svg;
  }

  /* CSC.rows(host, spec)
   * spec: {rows: [{label, sub, group, marks: [{v, lo, hi, cls, shape, hollow, name, src, f}], note}], xFmt(v), tipFmt(v), xTitle, label,
   *        refs: [{v, label, cls}], strip: {from, to, label}, xMin, xMax, legend: [items], labelWidth} */
  function rows(host, spec) {
    host.innerHTML = '';
    var W = width(host), narrow = W < 560, lw = narrow ? 0 : (spec.labelWidth || Math.min(260, W*0.36)), rh = narrow ? 46 : 30, gh = 26, m = {l: 12 + lw, r: 22, t: 24, b: 40};
    var vals = [];
    spec.rows.forEach(function (r) { r.marks.forEach(function (k) { vals.push(k.v); if (k.lo != null) { vals.push(k.lo); vals.push(k.hi); } }); });
    (spec.refs || []).forEach(function (r) { vals.push(r.v); }); if (spec.strip) { vals.push(spec.strip.from); vals.push(spec.strip.to); }
    var X = nice(spec.xMin != null ? Math.min(spec.xMin, Math.min.apply(null, vals)) : Math.min.apply(null, vals), spec.xMax != null ? Math.max(spec.xMax, Math.max.apply(null, vals)) : Math.max.apply(null, vals), narrow ? 4 : 6);
    var groups = 0, last = null; spec.rows.forEach(function (r) { if (r.group && r.group !== last) { groups++; last = r.group; } });
    var H = m.t + spec.rows.length*rh + groups*gh + m.b, H0 = H, sx = function (v) { return m.l + (v - X.lo)/(X.hi - X.lo)*(W - m.l - m.r); };
    var svg = el('svg', {class: 'fx-svg', viewBox: '0 0 ' + W + ' ' + H, width: W, height: H, role: 'img', 'aria-label': spec.label || ''}, host);
    var g = el('g', {class: 'fx-grid'}, svg);
    if (spec.strip) { el('rect', {x: sx(spec.strip.from), y: m.t - 6, width: Math.max(1, sx(spec.strip.to) - sx(spec.strip.from)), height: H - m.t - m.b + 6, class: 'fx-strip'}, g); if (spec.strip.label) txt(g, sx(spec.strip.to) + 4, m.t - 10, spec.strip.label, {class: 'fx-tick'}); }
    X.ticks.forEach(function (t) { el('line', {x1: sx(t), x2: sx(t), y1: m.t - 6, y2: H - m.b, class: t === 0 ? 'fx-zero' : ''}, g); txt(g, sx(t), H - m.b + 16, spec.xFmt ? spec.xFmt(t) : String(t), {class: 'fx-tick', 'text-anchor': 'middle'}); });
    if (spec.xTitle) { var ex2 = title(g, W/2, H - 6, spec.xTitle, W - 16); if (ex2) { H += ex2; svg.setAttribute('viewBox', '0 0 ' + W + ' ' + H); svg.setAttribute('height', H); } }
    (spec.refs || []).forEach(function (r, i) { el('line', {x1: sx(r.v), x2: sx(r.v), y1: m.t - 6, y2: H0 - m.b, class: 'fx-ref ' + (r.cls || '')}, svg); if (r.label) txt(svg, sx(r.v) + 4, m.t - 10 - i*12, r.label, {class: 'fx-tick'}); });
    var y = m.t; last = null;
    spec.rows.forEach(function (r, ri) {
      if (r.group && r.group !== last) { last = r.group; txt(svg, 12, y + 17, r.group, {class: 'fx-group'}); y += gh; }
      var row = el('g', {class: 'fx-row', tabindex: ri === 0 ? 0 : -1, role: 'listitem'}, svg), cy = narrow ? y + 30 : y + rh/2;
      el('rect', {x: 0, y: y, width: W, height: rh, class: 'fx-rowhit'}, row);
      var lab = txt(row, 12, narrow ? y + 13 : cy + 4, r.label, {class: 'fx-rowlbl'});
      if (!narrow && lab.getComputedTextLength && lw) { try { var L = lab.getComputedTextLength(); if (L > lw - 8) { var s = r.label; while (s.length > 4 && lab.getComputedTextLength() > lw - 14) { s = s.slice(0, -2); lab.textContent = s + '…'; } } } catch (e) {} }
      var ms = r.marks.filter(function (k) { return k.v != null; });
      if (ms.length === 2 && !r.noConnect) el('line', {x1: sx(ms[0].v), x2: sx(ms[1].v), y1: cy, y2: cy, class: 'fx-conn'}, row);
      ms.forEach(function (k) { if (k.lo != null) el('line', {x1: sx(k.lo), x2: sx(k.hi), y1: cy, y2: cy, class: (k.cls || '') + ' fx-whisker'}, row); });
      ms.forEach(function (k) { marker(row, k.shape || 'circle', sx(k.v), cy, 5, (k.cls || '') + ' fx-mk', k.hollow); });
      var aria = r.label + ': ' + ms.map(function (k) { return (k.name ? k.name + ' ' : '') + (spec.tipFmt ? spec.tipFmt(k.v) : k.v) + (k.lo != null ? ' (' + spec.tipFmt(k.lo) + ' to ' + spec.tipFmt(k.hi) + ')' : ''); }).join('; ');
      row.setAttribute('aria-label', aria);
      function show(ev) { var b = svg.getBoundingClientRect(); showTip('<div class="fx-tip-h">' + esc(r.label) + (r.sub ? ' <small>' + esc(r.sub) + '</small>' : '') + '</div>' + ms.map(function (k) { return '<div class="fx-tip-r"><i class="fx-key ' + (k.cls || '') + '"></i><b>' + esc(spec.tipFmt ? spec.tipFmt(k.v) : k.v) + '</b> ' + esc(k.name || '') + (k.lo != null ? ' <small>(' + esc(spec.tipFmt(k.lo)) + ' to ' + esc(spec.tipFmt(k.hi)) + ')</small>' : '') + '</div>'; }).join('') + (r.note ? '<div class="fx-tip-n">' + esc(r.note) + '</div>' : ''),
        ev && ev.clientX ? ev.clientX : b.left + sx(ms.length ? ms[0].v : 0)*(b.width/W), ev && ev.clientY ? ev.clientY : b.top + cy*(b.height/H)); }
      row.addEventListener('pointermove', show); row.addEventListener('pointerleave', hideTip); row.addEventListener('focus', function () { show(); }); row.addEventListener('blur', hideTip);
      if (r.onClick) { row.style.cursor = 'pointer'; row.addEventListener('click', r.onClick); row.addEventListener('keydown', function (ev) { if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); r.onClick(); } }); }
      y += rh;
    });
    svg.setAttribute('role', 'list');
    /* one Tab stop per chart: the arrow keys move between rows (Home and End to the ends) */
    var allRows = Array.prototype.slice.call(svg.querySelectorAll('.fx-row'));
    allRows.forEach(function (rw, i) { rw.addEventListener('keydown', function (ev) { var j = ev.key === 'ArrowDown' || ev.key === 'ArrowRight' ? i + 1 : ev.key === 'ArrowUp' || ev.key === 'ArrowLeft' ? i - 1 : ev.key === 'Home' ? 0 : ev.key === 'End' ? allRows.length - 1 : null;
      if (j === null) return; ev.preventDefault(); j = Math.max(0, Math.min(allRows.length - 1, j)); rw.setAttribute('tabindex', -1); allRows[j].setAttribute('tabindex', 0); allRows[j].focus(); }); });
    if (allRows.length) svg.setAttribute('aria-label', (spec.label || '') + '. Use the arrow keys to read each row.');
    if (spec.legend) legend(host, spec.legend);
    return svg;
  }

  /* Re-draw a chart when its box changes width (phones turning, windows resizing). */
  function responsive(host, draw) { draw(); if (!root.ResizeObserver) return; var w = host.clientWidth, t = null;
    var ro = new ResizeObserver(function () { if (Math.abs(host.clientWidth - w) < 24) return; w = host.clientWidth; clearTimeout(t); t = setTimeout(draw, 120); }); ro.observe(host); host._fxRO = ro; }

  root.CSC = {xy: xy, rows: rows, legend: legend, marker: marker, responsive: responsive, nice: nice, showTip: showTip, hideTip: hideTip, svgEl: el};
})(typeof window !== 'undefined' ? window : this);
