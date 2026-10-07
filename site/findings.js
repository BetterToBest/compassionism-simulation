/* Compassionism Simulation: shared findings components (v5.2.1, Oct 2026).
 * Renders a release data file (data/releases/v<version>.json, written by dev/tools/release_data.py) into headline cards, guided reads with charts,
 * full tables, "view as table" toggles and CSV/JSON downloads. Used by findings.html (the explorer), index.html (the guided sections) and
 * replication.html; the compare page will reuse it. Nothing here holds a figure: every number is read from the release file through a path
 * ("src") and printed in a <span class="num" data-src=... data-f=...>, which the figure check (dev/tools/check_figures.js) compares with the data.
 * A release that lacks a table or a reading simply does not show it, so an older release (or the next one) needs no new code unless it brings a new
 * kind of figure. */
(function (root) {
  'use strict';
  var ENVS = [['ref', 'Reference'], ['adv', 'Adverse'], ['st', 'Stress Test']], MINUS = '−';

  /* ---- formats: the same digits as dev/tools/release_data.py (JavaScript's toFixed; halves round up) ---- */
  function fx(x, d) { var t = Math.abs(x).toFixed(d); return (x < 0 && +t !== 0 ? '-' : '') + t; }
  function fmt(x, f) {
    if (x === null || x === undefined || (typeof x === 'number' && !isFinite(x))) return '–';
    if (/^p\d$/.test(f)) return fx(x, +f[1]).replace('-', MINUS) + '%';
    if (/^n\d$/.test(f)) return fx(x, +f[1]).replace('-', MINUS);
    if (/^s\d$/.test(f)) { var t = fx(x, +f[1]); return t.charAt(0) === '-' ? MINUS + t.slice(1) : (x > 0 && +t !== 0 ? '+' + t : t); }
    if (f === 'usd') { var n = Math.round(x); return (n < 0 ? MINUS : '') + '$' + Math.abs(n).toLocaleString('en-US'); }
    if (f === 'int') { var k = Math.round(x); return (k < 0 ? MINUS : '') + Math.abs(k).toLocaleString('en-US'); }
    if (f === 'lev') return (x >= 10 ? Math.round(x).toLocaleString('en-US') : x.toFixed(2)) + '×';
    if (f === 'lvn') return x >= 10 ? Math.round(x).toLocaleString('en-US') : x.toFixed(2);  /* a price level without the times sign, inside a range */
    throw new Error('unknown format ' + f);
  }
  function get(R, path) { var o = R, ks = String(path).split('.'); for (var i = 0; i < ks.length; i++) { if (o == null) return undefined; o = Array.isArray(o) ? o[+ks[i]] : o[ks[i]]; } return o; }
  function has(R, path) { return get(R, path) !== undefined; }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
  function num(R, path, f) { return '<span class="num" data-src="' + esc(path) + '" data-f="' + f + '">' + esc(fmt(get(R, path), f)) + '</span>'; }
  function text(R, key) { var t = R.text && R.text[key]; if (!t) return ''; return t.replace(/\{\{([^|}]+)\|([a-z0-9]+)\}\}/g, function (m, p, f) { return num(R, p, f); }); }
  function parts(R, ps) { return (ps || []).map(function (p) { return typeof p === 'string' ? esc(p) : num(R, p.src, p.f); }).join(''); }
  function plain(R, ps) { return (ps || []).map(function (p) { return typeof p === 'string' ? p : fmt(get(R, p.src), p.f); }).join(''); }
  function cellHTML(R, c) { return parts(R, c.p) + (c.s ? '<small>' + parts(R, c.s) + '</small>' : ''); }
  function cellText(R, c) { return plain(R, c.p) + (c.s ? ' (' + plain(R, c.s) + ')' : ''); }

  /* ---- tables ---- */
  function tableById(R, id) { return (R.tables || []).filter(function (t) { return t.id === id; })[0] || null; }
  function rowsFor(t, filt) {  /* a table with a filter spec keeps the rows of the chosen horizon and environment */
    if (!filt || !t.filter) return t.rows;
    return t.rows.filter(function (r) { return (filt.years == null || t.filter.years == null || r[t.filter.years].p[0] === String(filt.years)) && (filt.env == null || t.filter.env == null || r[t.filter.env].p[0] === envName(filt.env)); });
  }
  function envName(e) { for (var i = 0; i < ENVS.length; i++) if (ENVS[i][0] === e) return ENVS[i][1]; return e; }
  function tableHTML(R, t, filt, caption) {
    var rs = rowsFor(t, filt);
    return '<div class="fx-tw" tabindex="0" role="region" data-rel-text="table" aria-label="' + esc(t.title) + '"><table class="fx-table" data-table="' + esc(t.id) + '"><caption>' + esc(caption || t.title) + '</caption><thead><tr>' +
      t.columns.map(function (c) { return '<th scope="col">' + esc(c) + '</th>'; }).join('') + '</tr></thead><tbody>' +
      rs.map(function (r) { return '<tr>' + r.map(function (c) { return '<td>' + cellHTML(R, c) + '</td>'; }).join('') + '</tr>'; }).join('') + '</tbody></table></div>';
  }
  function csvOf(R, t, filt) {
    var q = function (s) { s = String(s); return /[",\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s; };
    return [t.columns.map(q).join(',')].concat(rowsFor(t, filt).map(function (r) { return r.map(function (c) { return q(cellText(R, c)); }).join(','); })).join('\n') + '\n';
  }
  function jsonOf(R, t, filt) {  /* the table with each number resolved and its path, so a reader can trace every value */
    return JSON.stringify({release: R.version, table: t.id, title: t.title, columns: t.columns, rows: rowsFor(t, filt).map(function (r) { return r.map(function (c) {
      var vals = []; (c.p || []).concat(c.s || []).forEach(function (p) { if (typeof p !== 'string') vals.push({value: get(R, p.src), path: p.src}); }); return {text: cellText(R, c), values: vals}; }); }),
      source: 'data/releases/v' + R.version + '.json', commands: R.meta && R.meta.commands}, null, 1);
  }
  function download(name, body, type) {
    var b = new Blob([body], {type: type}), a = document.createElement('a'); a.href = URL.createObjectURL(b); a.download = name; document.body.appendChild(a); a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 400);
  }
  function tableTools(R, t, filt) {
    var w = document.createElement('div'); w.className = 'fx-tools';
    var c = document.createElement('button'); c.type = 'button'; c.className = 'fx-btn'; c.textContent = 'Download CSV';
    c.onclick = function () { download('compassionism-v' + R.version + '-' + t.id + '.csv', csvOf(R, t, filt), 'text/csv'); };
    var j = document.createElement('button'); j.type = 'button'; j.className = 'fx-btn'; j.textContent = 'Download JSON';
    j.onclick = function () { download('compassionism-v' + R.version + '-' + t.id + '.json', jsonOf(R, t, filt), 'application/json'); };
    w.appendChild(c); w.appendChild(j); return w;
  }

  /* ---- headline cards (layer 1). The same markup release_data.py writes statically for the default view. ---- */
  var CARDS = [['bO', 'Below 30 days of basic living', 'bOAPy', 'dBO'], ['f0', 'Below the cost of living', 'fgt0PY', 'dF0'], ['pov', 'Too little wealth', 'pov', 'dPov'],
    ['kid', 'Children below the cost of living', 'hhCostKidPY', 'd53.hhCostKidPY']];  /* v5.3: the fourth card shows only for a release with households and children */
  /* the cards' plain meanings; the release file's figure catalogue carries the same words (dev/tools/release_data.py MEAS; the figure check compares them).
   * v5.2.2: a number in a meaning is a {{path|format}} token into the release file (the wealth line comes from CFG.POVERTY_LINE through the release data, audit
   * A3), so no amount is typed here; "Too little wealth" counts net wealth, what someone owns minus what they owe (audit A4). */
  var MEANINGS = {bO: 'In a typical year, the share of adults whose savings, pay and support would cover fewer than 30 days of basic living (the BLEI paper\u2019s measure).',
    f0: 'In a typical year, the share of adults whose income falls short of the cost of a basic living (the MIT living-wage basket for one adult).',
    pov: 'At the end of the run, the share of adults with less than {{inputs.wealthLine|usd}} of net wealth (what someone owns minus what they owe) in today\u2019s money.',
    kid: 'In a typical year, the share of children whose household\u2019s income falls short of the household\u2019s cost of a basic living (the MIT living-wage basket for its adults and children).'};
  /* v5.3: with households, whether a household is poor is decided for the household as a whole, so the adult measures read through it (release_data.py MEAS53) */
  var MEANINGS53 = {bO: 'In a typical year, the share of adults whose savings, pay and support would cover fewer than 30 days of basic living (the BLEI paper\u2019s measure; in a household, its savings, pay and costs).',
    f0: 'In a typical year, the share of adults whose household\u2019s income falls short of the household\u2019s cost of a basic living (the MIT living-wage basket for its adults and children).',
    pov: 'At the end of the run, the share of adults with less than {{inputs.wealthLine|usd}} of net wealth (what someone owns minus what they owe; in a couple, half of what the two own) in today\u2019s money.'};
  function meaningOf(R, k) { return (hasKids(R) && MEANINGS53[k]) || MEANINGS[k]; }
  var TOK = /\{\{([^|}]+)\|([a-z0-9]+)\}\}/g;
  function fillPlain(R, t) { return String(t).replace(TOK, function (m, p, f) { return fmt(get(R, p), f); }); }
  function fillHTML(R, t) { return String(t).replace(/\{\{([^|}]+)\|([a-z0-9]+)\}\}|[^{]+|\{/g, function (m, p, f) { return p ? num(R, p, f) : esc(m); }); }
  function cardsHTML(R, env, yrs, opt) {
    opt = opt || {};
    var b = 'panels.' + yrs + '.envs.' + env, out = '<div class="fx-cards">';
    CARDS.forEach(function (c) {
      if (!has(R, b + '.rows.release.' + c[2]) || !has(R, b + '.rows.release.' + c[3])) return;
      var d = get(R, b + '.rows.release.' + c[3] + '.0'), worse = d > 0;
      var wo = opt.view === 'without', big = wo ? b + '.base.' + c[2] : b + '.rows.release.' + c[2], other = wo ? b + '.rows.release.' + c[2] : b + '.base.' + c[2];
      out += '<div class="fx-card' + (worse ? ' fx-worse' : '') + '"><p class="fx-card-k">' + c[1] + '</p><p class="fx-card-v"' + (opt.count ? ' data-count="1"' : '') + '>' + num(R, big, 'p1') + '</p>' +
        '<p class="fx-card-vs">' + (wo ? 'with no programme, against ' + num(R, other, 'p1') + ' with Compassionism' : 'with Compassionism, against ' + num(R, other, 'p1') + ' with no programme') + '</p>' +
        '<p class="fx-card-d">' + (worse ? 'Worse:' : 'Change:') + ' ' + num(R, b + '.rows.release.' + c[3] + '.0', 's1') + ' points</p>' +
        '<p class="fx-card-m" data-rel-text="meaning">' + fillHTML(R, meaningOf(R, c[0])) + '</p></div>';
    });
    return out + '</div>';
  }
  function underCards(R, env, yrs) {  /* decision 1 (v5.2.1): the price rise and the cost sit directly under the three cards */
    var r = 'panels.' + yrs + '.envs.' + env + '.rows.release';
    var lev = has(R, r + '.pLevEndMed') ? 'by the last year the typical run is at ' + num(R, r + '.pLevEndMed', 'lev') : 'by the last year prices are on average at ' + num(R, r + '.pLev20', 'lev');
    return '<p class="fx-under">The programme raises prices by ' + num(R, r + '.infl', 'p1') + ' a year (the cautious reading); ' + lev +
      ' today’s prices. Cost: ' + num(R, r + '.cost', 'usd') + ' per adult a year. If every dollar the Source pays were backed by new output (H1), ' + num(R, 'panels.' + yrs + '.envs.' + env + '.rows.h1.pov', 'p1') + ' would end with too little wealth.</p>';
  }
  /* counters: the three card values count up once when they come into view; never under reduced motion */
  function animateCounts(host) {
    var reduce = root.matchMedia && root.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduce || !root.IntersectionObserver || !root.requestAnimationFrame) return;
    var els = host.querySelectorAll('[data-count] .num'); if (!els.length) return;
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (!e.isIntersecting) return; io.unobserve(e.target); var s = e.target, fin = s.textContent, m = /^(.*?)([\d.,]+)(.*)$/.exec(fin); if (!m) return;
      var to = parseFloat(m[2].replace(/,/g, '')), dec = (m[2].split('.')[1] || '').length, t0 = null;
      function step(t) { if (t0 === null) t0 = t; var k = Math.min(1, (t - t0)/700), v = to*(1 - Math.pow(1 - k, 3)); s.textContent = m[1] + v.toFixed(dec) + m[3]; if (k < 1) requestAnimationFrame(step); else s.textContent = fin; }
      requestAnimationFrame(step); }); }, {threshold: 0.4});
    Array.prototype.forEach.call(els, function (s) { io.observe(s); });
  }

  /* ---- URL state: ?v=5.2&env=ref&years=20&view=with#section ---- */
  function readState(def) {
    var q = new URLSearchParams(root.location.search), s = Object.assign({}, def);
    if (q.get('env') && /^(ref|adv|st)$/.test(q.get('env'))) s.env = q.get('env');
    if (q.get('years') && /^(20|40)$/.test(q.get('years'))) s.years = q.get('years');
    if (q.get('v') && /^\d+(\.\d+)+$/.test(q.get('v'))) s.v = q.get('v');
    if (q.get('view') && /^(with|without)$/.test(q.get('view'))) s.view = q.get('view');
    if (q.get('measure') && /^(pov|f0|bO|kid)$/.test(q.get('measure'))) s.measure = q.get('measure');
    return s;
  }
  function writeState(s, keys) {
    try { var q = new URLSearchParams(root.location.search); (keys || Object.keys(s)).forEach(function (k) { if (s[k] != null) q.set(k, s[k]); });
      history.replaceState(null, '', root.location.pathname + '?' + q.toString() + root.location.hash); } catch (e) {}
  }

  /* ---- segmented control ---- */
  function seg(label, opts, cur, on) {  /* opts: [[value, text]] */
    var w = document.createElement('span'); w.className = 'fx-ctl'; var l = document.createElement('span'); l.textContent = label; w.appendChild(l);
    var g = document.createElement('span'); g.className = 'fx-seg'; g.setAttribute('role', 'group'); g.setAttribute('aria-label', label);
    opts.forEach(function (o) { var b = document.createElement('button'); b.type = 'button'; b.textContent = o[1]; b.dataset.value = o[0]; b.setAttribute('aria-pressed', String(String(o[0]) === String(cur)));
      b.onclick = function () { Array.prototype.forEach.call(g.children, function (x) { x.setAttribute('aria-pressed', String(x === b)); }); on(o[0]); }; g.appendChild(b); });
    w.appendChild(g); return w;
  }

  /* ---- sticky navigation with scroll-spy ---- */
  function spy(nav) {
    var links = Array.prototype.slice.call(nav.querySelectorAll('a[href^="#"]')), secs = links.map(function (a) { return document.getElementById(a.getAttribute('href').slice(1)); });
    if (!root.IntersectionObserver) return;
    var vis = {};
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { vis[e.target.id] = e.isIntersecting ? e.intersectionRatio : 0; });
      var best = null; secs.forEach(function (s) { if (s && vis[s.id] > 0 && best === null) best = s.id; });
      if (best) links.forEach(function (a) { var on = a.getAttribute('href') === '#' + best; a.setAttribute('aria-current', on ? 'true' : 'false'); if (on && a.scrollIntoView && nav.querySelector('.fx-nav-in')) { var c = nav.querySelector('.fx-nav-in'), r = a.offsetLeft - c.clientWidth/2 + a.clientWidth/2; c.scrollTo ? c.scrollTo({left: r, behavior: 'auto'}) : (c.scrollLeft = r); } }); },
      {rootMargin: '-30% 0px -60% 0px', threshold: [0, 0.01]});
    secs.forEach(function (s) { if (s) io.observe(s); });
  }

  /* ---- the guided reads' charts (layer 2). Each draws from the release file only. ---- */
  var MEAS = {pov: ['Too little wealth', 'pov', 'dPov'], f0: ['Below the cost of living', 'fgt0PY', 'dF0'], bO: ['Below 30 days of basic living', 'bOAPy', 'dBO'],
    kid: ['Children below the cost of living', 'hhCostKidPY', 'd53.hhCostKidPY']};  /* [label, key, change key (a path inside the row)] */
  function hasKids(R) { return has(R, 'panels.20.envs.ref.rows.release.d53.hhCostKidPY'); }
  var pct = function (v) { return fmt(v, 'p1'); }, pts = function (v) { return fmt(v, 's1') + ' points'; };
  var CHARTS = {};
  CHARTS.dumbbell = function (R, host, st) {
    var P = R.panels[st.years]; if (!P) return false;
    var rows = [];
    var ks = ['bO', 'f0', 'pov'].concat(hasKids(R) ? ['kid'] : []);
    ENVS.forEach(function (e) { ks.forEach(function (k) { var E = P.envs[e[0]], M = MEAS[k], d = get(E.rows.release, M[2]);
      rows.push({group: e[1], label: M[0], marks: [{v: E.base[M[1]], cls: 's-without', hollow: true, name: 'no programme'}, {v: E.rows.release[M[1]], cls: 's-with', name: 'Compassionism'}],
        note: 'Change ' + pts(d[0]) + ' (95% interval ' + fmt(d[1], 's1') + ' to ' + fmt(d[2], 's1') + ')'}); }); });
    root.CSC.responsive(host, function () { root.CSC.rows(host, {rows: rows, xMin: 0, xMax: 100, xFmt: function (v) { return v + '%'; }, tipFmt: pct, xTitle: 'Share below the line (' + st.years + ' years)' + (ks.length > 3 ? ': adults, and children for the last row' : ''),
      label: 'Compassionism against no programme on ' + ks.length + ' poverty measures in three environments over ' + st.years + ' years',
      legend: [{label: 'No programme', cls: 's-without', shape: 'circle', hollow: true}, {label: 'Compassionism', cls: 's-with', shape: 'circle'}]}); });
    return true;
  };
  function tgt(R) { return R.inputs ? R.inputs.hubPovertyTarget : 2; }
  function gin(R) { return R.inputs ? R.inputs.hubGini : [0.25, 0.3]; }
  var TG = [['fpl', 'Official poverty line'], ['fplX', 'Poverty line, Supplemental-style'], ['bO', 'Below 30 days (BLEI paper)'], ['bN', 'Below 30 days (design-neutral)'], ['f0', 'Below the cost of living'], ['pov', 'Too little wealth'], ['ep', 'Unhoused']];
  CHARTS.targets = function (R, host, st) {
    var E = R.panels[st.years] && R.panels[st.years].envs[st.env]; if (!E || !E.rows.release.rep) return false;
    var rows = [], mk = function (t, k) { return [{v: E.base.rep[t][k], cls: 's-without', hollow: true, name: 'no programme'}, {v: E.rows.release.rep[t][k], cls: 's-with', name: 'Compassionism'}]; };
    [['y7', 'Year 7 (the Hub’s date)'], ['end', 'Year ' + st.years + ' (last year)']].forEach(function (t) { TG.forEach(function (m) { rows.push({group: t[1], label: m[1], marks: mk(t[0], m[0])}); }); });
    var g1 = document.createElement('div'), g2 = document.createElement('div'); g1.className = g2.className = 'fx-chart'; host.innerHTML = ''; host.appendChild(g1);
    var cap = document.createElement('p'); cap.className = 'fx-note'; cap.textContent = 'The spread of income and wealth (Gini), against the Hub’s target band for income (shaded):'; host.appendChild(cap); host.appendChild(g2);
    root.CSC.responsive(g1, function () { root.CSC.rows(g1, {rows: rows, xMin: 0, xFmt: function (v) { return v + '%'; }, tipFmt: pct, strip: {from: 0, to: tgt(R), label: 'Hub target: under ' + tgt(R) + '%'}, xTitle: 'Share of adults below the line that year',
      label: 'Poverty measures at Year 7 and the last year against the Hub target of under 2 percent, ' + envName(st.env) + ', ' + st.years + ' years', legend: [{label: 'No programme', cls: 's-without', shape: 'circle', hollow: true}, {label: 'Compassionism', cls: 's-with', shape: 'circle'}]}); });
    var gr = []; [['y7', 'Year 7'], ['end', 'Year ' + st.years]].forEach(function (t) { [['giniD', 'Income'], ['giniX', 'Income counting price cuts'], ['giniW', 'Wealth (debts as zero)']].forEach(function (m) { gr.push({group: t[1], label: m[1], marks: mk(t[0], m[0])}); }); });
    root.CSC.responsive(g2, function () { root.CSC.rows(g2, {rows: gr, xMin: 0, xMax: 1, xFmt: function (v) { return v.toFixed(1); }, tipFmt: function (v) { return fmt(v, 'n3'); }, strip: {from: 0.25, to: 0.30, label: '0.25–0.30'}, xTitle: 'Gini coefficient (0 = equal, 1 = one person has everything)',
      label: 'Gini coefficients against the Hub target', legend: [{label: 'No programme', cls: 's-without', shape: 'circle', hollow: true}, {label: 'Compassionism', cls: 's-with', shape: 'circle'}]}); });
    return true;
  };
  CHARTS.fixed = function (R, host, st) {
    var E = R.panels[st.years] && R.panels[st.years].envs[st.env]; if (!E || !E.rows.release.rep) return false;
    var r = E.rows.release, b = E.base, rows = [];
    [['Compassionism', r], ['No programme', b]].forEach(function (g) { var x = g[1];
      rows.push({group: g[0], label: 'Too little wealth, last year', marks: [{v: x.rep.end.povNom, cls: 's-alt', shape: 'diamond', hollow: true, name: 'line fixed in dollars'}, {v: x.rep.end.pov, cls: 's-with', name: 'line moved with prices'}]});
      rows.push({group: g[0], label: 'Below 30 days, over the run', marks: [{v: x.rep.py.bONom, cls: 's-alt', shape: 'diamond', hollow: true, name: 'line fixed in dollars'}, {v: x.bOAPy, cls: 's-with', name: 'line moved with prices'}]});
      rows.push({group: g[0], label: 'Official poverty line, last year', marks: [{v: x.rep.end.fplNom, cls: 's-alt', shape: 'diamond', hollow: true, name: 'line fixed in dollars'}, {v: x.rep.end.fpl, cls: 's-with', name: 'line moved with prices'}]}); });
    root.CSC.responsive(host, function () { root.CSC.rows(host, {rows: rows, xMin: 0, xFmt: function (v) { return v + '%'; }, tipFmt: pct, xTitle: 'Share of adults below the line', label: 'Poverty lines moved with prices against lines fixed in dollars, ' + envName(st.env) + ', ' + st.years + ' years',
      legend: [{label: 'Line moved with prices (the main reading)', cls: 's-with', shape: 'circle'}, {label: 'Line fixed in dollars', cls: 's-alt', shape: 'diamond', hollow: true}]}); });
    return true;
  };
  CHARTS.backing = function (R, host) {
    var B = R.backing; if (!B) return false;
    var K = ['a0', 'a25', 'a50', 'a75', 'a100'], xs = K.map(function (k) { return B.envs.ref.rows[k].a; }), cls = {ref: 's-e1', adv: 's-e2', st: 's-e3'}, shp = {ref: 'circle', adv: 'square', st: 'triangle'};
    var series = ENVS.map(function (e) { var rs = B.envs[e[0]].rows; return {name: e[1], cls: cls[e[0]], shape: shp[e[0]], values: K.map(function (k) { return rs[k].dPov[0]; }), ci: {lo: K.map(function (k) { return rs[k].dPov[1]; }), hi: K.map(function (k) { return rs[k].dPov[2]; })}}; });
    var extra = [], P = R.panels['20'];
    ENVS.forEach(function (e) { ['midlo', 'mid', 'midhi'].forEach(function (k) { var r = P && P.envs[e[0]].rows[k]; if (r && r.bkA != null) extra.push({x: r.bkA/100, y: r.dPov[0], cls: cls[e[0]], shape: 'diamond', hollow: true}); }); });
    var g1 = document.createElement('div'), g2 = document.createElement('div'); g1.className = g2.className = 'fx-chart'; host.innerHTML = ''; host.appendChild(g1);
    var cap = document.createElement('p'); cap.className = 'fx-note'; cap.textContent = 'The price rise the programme itself causes, at each share:'; host.appendChild(cap); host.appendChild(g2);
    root.CSC.responsive(g1, function () { root.CSC.xy(g1, {x: xs, xTicks: xs, xLabel: function (v) { return 'a = ' + v; }, xTitle: 'Share of the Source’s payout backed by new output (a)', yFmt: function (v) { return (v > 0 ? '+' : v < 0 ? MINUS : '') + Math.abs(v); }, tipFmt: pts,
      series: series, extra: extra, zero: true, label: 'Change in too little wealth against no programme as the backed share rises from 0 to 1, three environments',
      legendExtra: extra.length ? [{label: 'Middle reading (the Kenya-anchored band)', cls: 's-without', shape: 'diamond', hollow: true}] : []}); });
    var inf = ENVS.map(function (e) { var rs = B.envs[e[0]].rows; return {name: e[1], cls: cls[e[0]], shape: shp[e[0]], values: K.map(function (k) { return rs[k].infl; })}; });
    root.CSC.responsive(g2, function () { root.CSC.xy(g2, {x: xs, xTicks: xs, xLabel: function (v) { return 'a = ' + v; }, yFmt: function (v) { return v + '%'; }, tipFmt: function (v) { return fmt(v, 'p1') + ' a year'; }, series: inf, yMin: 0, height: 200, label: 'Programme inflation by backed share', legend: false, endLabels: false}); });
    return true;
  };
  var GROUPS = [['v5.4\u2019s choices, and a disaster', ['v53', 'cut0', 'cut20', 'autopay', 'pthbold', 'ptfs25', 'dis']], ['v5.3\u2019s new choices, each undone in turn', ['v52', 'adults', 'core', 'indiv', 'cb0', 'cb50', 'wmodel', 'nosg', 'shock50', 'fbs50']],
    ['The two ends and the middle backing band', ['h1', 'mid', 'midlo', 'midhi']], ['Savings and the BU', ['sav', 'sav0', 'idx', 'h1idx', 'h1both']], ['Ageing', ['age', 'agenc', 'agenone', 'agepia', 'ageleave', 'agecps']],
    ['Closer to US data', ['fixw', 'fixr', 'fixs', 'fixm', 'fixall']], ['Idle workers in normal years', ['slack', 'slacku6']], ['Robustness risks', ['hcap', 'hcaphi', 'rev5', 'rev10', 'rev20', 'rev20n', 'giftrun']],
    ['Other ways to pay (not specified by the Hub)', ['tax', 'progtax', 'landtax']], ['Other readings of the design', ['face', 'cost', 'cap5', 'all', 'free', 'standins']]];
  var SHORT = {h1: 'H1: every Source dollar backed', mid: 'Middle backing reading (Kenya-anchored)', midlo: 'Middle band, low end (US idle labour)', midhi: 'Middle band, high end (Kenya peak year)', sav: 'Savings keep up with prices (plus a real yield)', sav0: 'Savings keep only their value',
    idx: 'BU indexed every year', h1idx: 'H1 with the BU indexed every year', h1both: 'H1 with both', age: 'Adults age, retire and are replaced', agenc: 'Ageing, no conversion after retirement', agenone: 'Ageing, retirees leave the programme', agepia: 'Ageing, benefit from own wage',
    fixw: 'Savings from the US survey', fixr: 'Automation risk linked to wages', fixs: 'Wages spread as in the survey', fixm: 'Wages centred on the survey median', fixall: 'All four US-data readings', slack: 'Idle labour in normal years', slacku6: 'All of U-6 idle (upper bound)',
    hcap: 'Rent capture, BU tenants (voucher evidence)', hcaphi: 'Rent capture, every renter (upper end)', rev5: 'Review errors, low (audits catch half)', rev10: 'Review errors, middle', rev20: 'Review errors, high', rev20n: 'Review errors, high, no audits', giftrun: 'Launch gift paid over the run',
    tax: 'Flat contribution on wages', progtax: 'Progressive income tax', landtax: 'Land-value tax', face: 'BU essentials counted as backed', cost: 'Creative work at the cost of its hours', cap5: 'Capacity only as reinvestment pays', all: 'Taking part costs nothing', free: 'Price cuts free', standins: 'The two former stand-ins on',
    v53: 'v5.3\u2019s main row (no job loss; PTH and PTF as in v5.3)', cut0: 'No pay cut on return to work', cut20: 'A 20% pay cut on return to work', autopay: 'Automation as a lasting pay drag (the earlier rule)',
    pthbold: 'Acre Equity by the earlier 3\u20135% rule', ptfs25: 'PTF cuts 25% in transport, health care and childcare', dis: 'A disaster in Year 7 (a scenario)',
    v52: 'v5.2\u2019s main row (adults alone, v5.2\u2019s choices)', adults: 'Adults living alone (no households)', core: 'BU buy only food, housing and medical care', indiv: 'Each adult keeps their own money (no pooling)',
    cb0: 'No child allowance', cb50: 'A child allowance of half the adult BU', wmodel: 'Starting savings from the model\u2019s own draw', nosg: 'Everyone pays their full cost (no graded spending)',
    shock50: 'Partners\u2019 income swings strongly linked', fbs50: 'FBS50 spread evenly over its range', ageleave: 'Ageing, every estate leaves the model', agecps: 'Ageing, wages follow US earnings by age'};
  var SHORT53 = {age: 'Ageing: children grow up and are born; estates pass on', agenone: 'Ageing, retirees leave the programme', agepia: 'Ageing, benefit from own wage', fixall: 'All three wage and risk readings'};  /* v5.3: the ageing row is the households' (children's lives) */
  function readingsRows(R, yrs, env, k, opts) {
    var E = R.panels[yrs] && R.panels[yrs].envs[env]; if (!E) return null; var M = MEAS[k], rows = [], mm = M && get(E.rows.release, M[2]); if (!mm) return null;
    var v53 = E.rows.release.hhCostKidPY !== undefined;
    GROUPS.forEach(function (G) { G[1].forEach(function (j) { var r = E.rows[j], d = r && get(r, M[2]); if (!d) return; if (opts && opts.only && opts.only.indexOf(j) < 0) return;
      rows.push({group: G[0], label: (v53 && SHORT53[j]) || SHORT[j] || r.label, marks: [{v: d[0], lo: d[1], hi: d[2], cls: 's-alt', shape: 'circle', name: 'change against no programme'}], note: r.label}); }); });
    return {rows: rows, main: mm[0]};
  }
  CHARTS.readings = function (R, host, st) {
    var k = st.measure || 'pov', X = readingsRows(R, st.years, st.env, k); if (!X || !X.rows.length) return false;
    root.CSC.responsive(host, function () { root.CSC.rows(host, {rows: X.rows, tipFmt: pts, xFmt: function (v) { return (v > 0 ? '+' : v < 0 ? MINUS : '') + Math.abs(v); }, refs: [{v: X.main, label: 'main row ' + fmt(X.main, 's1')}, {v: 0, label: 'no programme'}],
      xTitle: MEAS[k][0] + ': change against no programme, points (left is better)', label: 'How far each reading moves the change in ' + MEAS[k][0].toLowerCase() + ', ' + envName(st.env) + ', ' + st.years + ' years',
      legend: [{label: 'Reading (95% interval)', cls: 's-alt', shape: 'circle'}, {label: 'Vertical line: the main row', cls: 's-without', line: true}]}); });
    return true;
  };
  /* v5.3 (B9): what each part of the design does on the main row: the main row minus the main row without that part, paired run by run (dev/tools/attrib_check.js) */
  var AT = {pov: 'pov', f0: 'fgt0PY', bO: 'bOAPy', kid: 'hhCostKidPY'};
  CHARTS.attrib = function (R, host, st) {
    var A = R.attrib && R.attrib[st.env], k = AT[st.measure || 'pov']; if (!A || !A.whole[k]) return false;
    var rows = [{group: 'The whole programme', label: 'Every part together', note: 'The main row against no programme', marks: [{v: A.whole[k][0], lo: A.whole[k][1], hi: A.whole[k][2], cls: 's-with', shape: 'circle', name: 'change'}]}];
    Object.keys(A.parts).forEach(function (j) { var q = A.parts[j][k]; var L = A.parts[j].label.replace(/^without /, ''); rows.push({group: 'What each part adds (the main row against the main row without it)', label: L.replace(/ \(.*\)$/, ''), note: L, marks: [{v: q[0], lo: q[1], hi: q[2], cls: 's-alt', shape: 'circle', name: 'what the part adds'}]}); });
    root.CSC.responsive(host, function () { root.CSC.rows(host, {rows: rows, tipFmt: pts, xFmt: function (v) { return (v > 0 ? '+' : v < 0 ? MINUS : '') + Math.abs(v); }, refs: [{v: 0, label: 'no effect'}],
      xTitle: MEAS[st.measure || 'pov'][0] + ': change, points (left is better)', label: 'What each part of the design does to ' + MEAS[st.measure || 'pov'][0].toLowerCase() + ', ' + envName(st.env) + ', ' + A._meta.years + ' years',
      legend: [{label: 'The whole programme against no programme (95% interval)', cls: 's-with', shape: 'circle'}, {label: 'What the part adds (95% interval)', cls: 's-alt', shape: 'circle'}]}); });
    return true;
  };
  /* v5.3 (B8): households and children, with Compassionism against no programme */
  var HHM = [['Children', 'Below the cost of living', 'hhCostKidPY'], ['Children', 'Below 30 days of basic living', 'hhBleiKidPY'], ['Children', 'Too little household wealth, last year', 'hhWlthKidEnd'],
    ['Everyone (adults and children)', 'Below the cost of living', 'hhCostPY'], ['Everyone (adults and children)', 'Too little household wealth, last year', 'hhWlthEnd'],
    ['Below the cost of living, by household', 'Single adults', 'hhCost_sg'], ['Below the cost of living, by household', 'Single parents and their children', 'hhCost_sp'],
    ['Below the cost of living, by household', 'Couples without children', 'hhCost_cn'], ['Below the cost of living, by household', 'Couples with children, and children', 'hhCost_ck']];
  CHARTS.hh = function (R, host, st) {
    var E = R.panels[st.years] && R.panels[st.years].envs[st.env]; if (!E || E.rows.release.hhCostKidPY === undefined) return false;
    var rows = HHM.filter(function (m) { return E.rows.release[m[2]] !== undefined && E.base[m[2]] !== undefined; }).map(function (m) {
      return {group: m[0], label: m[1], marks: [{v: E.base[m[2]], cls: 's-without', hollow: true, name: 'no programme'}, {v: E.rows.release[m[2]], cls: 's-with', name: 'Compassionism'}]}; });
    root.CSC.responsive(host, function () { root.CSC.rows(host, {rows: rows, xMin: 0, xMax: 100, xFmt: function (v) { return v + '%'; }, tipFmt: pct, xTitle: 'Share of people below the line (' + st.years + ' years)',
      label: 'Households and children: Compassionism against no programme, ' + envName(st.env) + ', ' + st.years + ' years',
      legend: [{label: 'No programme', cls: 's-without', shape: 'circle', hollow: true}, {label: 'Compassionism', cls: 's-with', shape: 'circle'}]}); });
    return true;
  };
  /* v5.4: jobs and risk, with Compassionism against no programme (the measures both runs have; PTH's books and PTF's cut are in the table) */
  var WKM = [['Work', 'Out of work (share of working-age adult-years)', 'emUrate'], ['Work', 'Spells out of work longer than 26 weeks', 'emLong'],
    ['Risk', 'Savings fell by more than six months of basic living', 'rkDdW6'], ['Risk', 'Days of basic living fell by more than 30', 'rkDdB30'],
    ['Risk', 'Income back within three years of a shock', 'rkRec3'], ['Risk', 'Back below the cost of living within five years', 'rkReC5']];
  CHARTS.work = function (R, host, st) {
    var E = R.panels[st.years] && R.panels[st.years].envs[st.env]; if (!E || E.rows.release.emUrate === undefined) return false;
    var rows = WKM.filter(function (m) { return E.rows.release[m[2]] !== undefined && E.base[m[2]] !== undefined; }).map(function (m) {
      return {group: m[0], label: m[1], marks: [{v: E.base[m[2]], cls: 's-without', hollow: true, name: 'no programme'}, {v: E.rows.release[m[2]], cls: 's-with', name: 'Compassionism'}]}; });
    root.CSC.responsive(host, function () { root.CSC.rows(host, {rows: rows, xMin: 0, xMax: 100, xFmt: function (v) { return v + '%'; }, tipFmt: pct, xTitle: 'Share of adults, of adult-years or of spells (' + st.years + ' years)',
      label: 'Jobs and risk: Compassionism against no programme, ' + envName(st.env) + ', ' + st.years + ' years',
      legend: [{label: 'No programme', cls: 's-without', shape: 'circle', hollow: true}, {label: 'Compassionism', cls: 's-with', shape: 'circle'}]}); });
    return true;
  };
  CHARTS.us = function (R, host) {
    var U = R.us; if (!U) return false; var n = U.ref.rows.none, us = U.ref.us;
    if (hasKids(R) && n.hh && us.scfHH) {  /* v5.3: the households' yardstick (us_check.js --v53): debt by household type at Year 7 against the SCF, and everyone's official poverty rate */
      var T5 = [['all', 'All households'], ['coupleKids', 'Couples with children'], ['coupleNoKids', 'Couples without children'], ['singleParent', 'Single parents'], ['single', 'Single adults']];
      var rows5 = T5.filter(function (t) { return us.scfHH[t[0]] && n.hh.wealth.y7[t[0]]; }).map(function (t) { return {group: 'Households in debt (net worth below zero)', label: t[1],
        marks: [{v: us.scfHH[t[0]].neg, cls: 's-alt', shape: 'diamond', hollow: true, name: 'US (SCF 2022)'}, {v: n.hh.wealth.y7[t[0]].neg, cls: 's-without', name: 'model, Year 7'}]}; });
      rows5.push({group: 'Below the official poverty line', label: 'Everyone (household thresholds)', marks: [{v: us.official.all, cls: 's-alt', shape: 'diamond', hollow: true, name: 'US, everyone (2025)'}, {v: n.hh.fpl.y7, cls: 's-without', name: 'model, Year 7'}]});
      root.CSC.responsive(host, function () { root.CSC.rows(host, {rows: rows5, xMin: 0, xFmt: function (v) { return v + '%'; }, tipFmt: pct, xTitle: 'Share of households (debt) or of people (poverty)', label: 'The no-programme run at Year 7 against US figures',
        legend: [{label: 'US figure', cls: 's-alt', shape: 'diamond', hollow: true}, {label: 'Model, no programme, Year 7 (Reference)', cls: 's-without', shape: 'circle'}]}); });
      return true;
    }
    var rows = [{label: 'Below the official poverty line', marks: [{v: us.official.workers, cls: 's-alt', shape: 'diamond', hollow: true, name: 'US workers (2025)'}, {v: n.fpl.y0, cls: 's-without', name: 'model, first year'}]},
      {label: 'Below the line, Supplemental-style', marks: [{v: us.spm.workers, cls: 's-alt', shape: 'diamond', hollow: true, name: 'US workers (2025)'}, {v: n.spm.y0, cls: 's-without', name: 'model, first year'}]},
      {label: 'In debt (net worth below zero)', marks: [{v: us.scf.neg, cls: 's-alt', shape: 'diamond', hollow: true, name: 'US comparison group (SCF 2022)'}, {v: n.wealth.y0.neg, cls: 's-without', name: 'model, first year'}]},
      {label: 'Net wealth under ' + fmt(R.inputs.wealthLine, 'usd'), marks: [{v: us.scf.below25k, cls: 's-alt', shape: 'diamond', hollow: true, name: 'US comparison group (SCF 2022)'}, {v: n.wealth.y0.below25k, cls: 's-without', name: 'model, first year'}]}];
    root.CSC.responsive(host, function () { root.CSC.rows(host, {rows: rows, xMin: 0, xFmt: function (v) { return v + '%'; }, tipFmt: pct, xTitle: 'Share of adults', label: 'The no-programme run in its first year against US figures',
      legend: [{label: 'US figure', cls: 's-alt', shape: 'diamond', hollow: true}, {label: 'Model, no programme, first year (Reference)', cls: 's-without', shape: 'circle'}]}); });
    return true;
  };

  /* ---- one guided read (layer 2) with its tables (layer 3) ---- */
  function storyEl(R, s, st, opts) {
    opts = opts || {};
    var sec = document.createElement('section'); sec.className = 'fx-sec'; sec.id = s.id; sec.setAttribute('aria-labelledby', s.id + '-h');
    var needsEnv = /^(targets|fixed|readings|attrib|hh|work)$/.test(s.chart), needsYears = /^(dumbbell|targets|fixed|readings|hh|work)$/.test(s.chart), measured = /^(readings|attrib)$/.test(s.chart);
    var scope = (needsEnv ? envName(st.env) + ', ' : '') + (needsYears ? st.years + ' years' : (s.chart === 'backing' && R.backing ? (R.backing._meta.years + ' years') : s.chart === 'attrib' && R.attrib ? R.attrib.ref._meta.years + ' years' : ''));
    if (st.measure === 'kid' && !hasKids(R)) st.measure = 'pov';
    sec.innerHTML = '<p class="fx-kicker">' + esc(opts.kicker || 'Guided read') + '</p><h2 class="fx-h2" id="' + s.id + '-h">' + esc(s.title) + ' <a class="fx-anchor" href="#' + s.id + '" aria-label="Link to this section">#</a></h2>' +
      '<p class="fx-lead" data-rel-text="1">' + text(R, s.id + '.lead') + '</p>';
    var fig = document.createElement('figure'); fig.className = 'fx-figure';
    var cap = document.createElement('figcaption'); cap.textContent = scope ? 'Showing: ' + scope + (measured ? '; measure: ' + MEAS[st.measure || 'pov'][0].toLowerCase() : '') : ''; fig.appendChild(cap);
    if (measured) { var sel = seg('Measure', [['pov', 'Too little wealth'], ['f0', 'Cost of living'], ['bO', '30 days (BLEI)']].concat(hasKids(R) ? [['kid', 'Children']] : []), st.measure || 'pov', function (v) { st.measure = v; if (opts.onState) opts.onState({measure: v}); });
      sel.style.margin = '0 0 8px'; fig.appendChild(sel); }
    var ch = document.createElement('div'); ch.className = 'fx-chart'; ch.setAttribute('data-rel-text', 'chart'); fig.appendChild(ch);
    sec.appendChild(fig);
    var ok = CHARTS[s.chart] ? CHARTS[s.chart](R, ch, st) : false;
    if (!ok) ch.innerHTML = '<p class="fx-note">This release has no data for this chart.</p>';
    var more = '';
    if (R.text[s.id + '.read']) more += '<details class="fx-more"><summary>How to read this</summary><div data-rel-text="1">' + text(R, s.id + '.read') + '</div></details>';
    if (R.text[s.id + '.limits']) more += '<details class="fx-more"><summary>What it does not show</summary><div data-rel-text="1">' + text(R, s.id + '.limits') + '</div></details>';
    ['prices', 'month', 'provenance'].forEach(function (k) { if (R.text[s.id + '.' + k]) more += '<details class="fx-more"><summary>' + {prices: 'About the price levels', month: 'What a month still buys', provenance: 'Where these figures come from'}[k] + '</summary><div data-rel-text="1">' + text(R, s.id + '.' + k) + '</div></details>'; });
    var m = document.createElement('div'); m.innerHTML = more; sec.appendChild(m);
    var nT = s.tables.filter(function (id) { return tableById(R, id) && !/^rel-t(20|40)$/.test(id); }).length;  /* v5.3: a read with several tables names each */
    s.tables.forEach(function (id) { var t = tableById(R, id); if (!t) return;
      var filt = t.filter ? {years: st.years, env: st.env} : null; if (/^rel-t(20|40)$/.test(id) && id !== 'rel-t' + st.years) return;
      var d = document.createElement('details'); d.className = 'fx-more fx-tabledet'; d.id = s.id + '-' + id + '-table';
      d.innerHTML = '<summary>View as table' + (nT > 1 ? ': ' + esc(t.title) : '') + (filt ? ' (' + envName(st.env) + ', ' + st.years + ' years)' : '') + '</summary>';
      var w = document.createElement('div'); w.innerHTML = tableHTML(R, t, filt); w.appendChild(tableTools(R, t, filt)); d.appendChild(w); sec.appendChild(d); });
    return sec;
  }
  function allTables(R, host) {  /* layer 3: every table of the release, unfiltered, with downloads */
    host.innerHTML = '';
    (R.tables || []).forEach(function (t) { var d = document.createElement('details'); d.className = 'fx-more'; d.id = 'table-' + t.id;
      d.innerHTML = '<summary>' + esc(t.title) + ' <span class="fx-note">(' + t.rows.length + ' rows)</span></summary>'; var w = document.createElement('div');
      d.addEventListener('toggle', function () { if (d.open && !w.firstChild) { w.innerHTML = tableHTML(R, t, null); w.appendChild(tableTools(R, t, null)); } });
      d.appendChild(w); host.appendChild(d); });
  }
  function fetchJSON(url) { return fetch(url, {cache: 'no-cache'}).then(function (r) { if (!r.ok) throw new Error(url + ': ' + r.status); return r.json(); }); }

  root.CSF = {fmt: fmt, get: get, has: has, num: num, text: text, esc: esc, cellHTML: cellHTML, tableHTML: tableHTML, tableById: tableById, csvOf: csvOf, jsonOf: jsonOf, download: download, tableTools: tableTools,
    cardsHTML: cardsHTML, MEANINGS: MEANINGS, MEANINGS53: MEANINGS53, meaningOf: meaningOf, fillPlain: fillPlain, underCards: underCards, animateCounts: animateCounts, readState: readState, writeState: writeState, seg: seg, spy: spy, charts: CHARTS, storyEl: storyEl, allTables: allTables,
    readingsRows: readingsRows, fetchJSON: fetchJSON, envName: envName, ENVS: ENVS, MEAS: MEAS, SHORT: SHORT, SHORT53: SHORT53, GROUPS: GROUPS, hasKids: hasKids, HHM: HHM, WKM: WKM, AT: AT};
})(typeof window !== 'undefined' ? window : this);
