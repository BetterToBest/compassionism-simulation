/* Compassionism Simulation: the simulation page's guided sections (v5.2.1, Oct 2026; ledger s93, decision d158).
 * One control strip (environment, 20 or 40 years, with or without Compassionism) drives every section; the first two are the page's own controls
 * (relSet, relYears in index.html's script, which keep ?env= and ?years= in the address), the third adds ?view=. The sections draw only from the
 * release data: the 500-seed panels embedded in the page (#rel-data, #rel-data-40, identical to data/releases/v<version>.json) and, loaded when
 * their section comes into view, the spread across the runs and one run's 500 adults (data/releases/v<version>/bands-*.json, lives-*.json).
 * Numbers are printed by site/findings.js with their path into the data (data-src), so the figure check can compare each with the data.
 * This file is not part of the page's inline script, so earlier-engine.html (which shares that script) does not load it. */
(function () {
  'use strict';
  var F = window.CSF, C = window.CSC, REL = window.REL, doc = document;
  if (!F || !C || !REL) return;
  var R = {panels: {}, meta: {}, x: {bands: {}, lives: {}}}, ST = {view: 'with', measure: 'f0', sure: 'pov', extra: false, year: null, person: null}, MAN = null, VER = null;
  var $ = function (id) { return doc.getElementById(id); }, num = function (p, f) { return F.num(R, p, f); };
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function yrs() { return String(REL.yrs); }
  function WL() { return window.CFG && window.CFG.POVERTY_LINE; }  /* the wealth line in today's dollars, from the page's engine */
  function base() { return 'panels.' + yrs() + '.envs.' + REL.env; }
  function E() { return R.panels[yrs()].envs[REL.env]; }
  function T() { return +R.panels[yrs()]._meta.years; }

  /* ---- data: the page's embedded panels; the extras on demand ---- */
  function loadPanels() { R.panels['20'] = REL.data; if (REL.data40 && REL.data40.envs) R.panels['40'] = REL.data40; R.meta = {seeds: REL.data._meta.seeds, agents: REL.data._meta.agents}; }
  function manifest() { if (MAN) return Promise.resolve(MAN); return F.fetchJSON('data/manifest.json').then(function (m) { MAN = m; VER = (m.releases.filter(function (r) { return r.status === 'current'; })[0] || m.releases[0]).version; return m; }); }
  function bands(y) { if (R.x.bands[y]) return Promise.resolve(R.x.bands[y]); return manifest().then(function () { return F.fetchJSON('data/releases/v' + VER + '/bands-' + y + '.json'); }).then(function (d) { R.x.bands[y] = d; return d; }); }
  function lives(e, y) { var k = e + '-' + y; if (R.x.lives[k]) return Promise.resolve(R.x.lives[k]); return manifest().then(function () { return F.fetchJSON('data/releases/v' + VER + '/lives-' + k + '.json'); }).then(function (d) { R.x.lives[k] = d; return d; }); }
  function whenVisible(el, fn) { if (!window.IntersectionObserver) { fn(); return; } var io = new IntersectionObserver(function (es) { if (es.some(function (x) { return x.isIntersecting; })) { io.disconnect(); fn(); } }, {rootMargin: '600px 0px'}); io.observe(el); }
  function failNote(e) { return '<p class="fx-note">This part loads its data from the site (data/releases/); it could not be loaded here (' + F.esc(e && e.message || 'offline') + '). Open the page on the live site to see it. Every other figure on this page still shows.</p>'; }

  /* ---- 1. the answer in ten seconds ---- */
  function renderAnswer() {
    $('fx-cards').innerHTML = F.cardsHTML(R, REL.env, yrs(), {count: true, view: ST.view});
    $('fx-under').innerHTML = F.underCards(R, REL.env, yrs());
    F.animateCounts($('fx-cards'));
    var go = 'findings.html?env=' + REL.env + '&years=' + yrs();
    Array.prototype.forEach.call(doc.querySelectorAll('[data-go]'), function (a) { a.href = go + '#' + a.getAttribute('data-go'); });
  }

  /* ---- 2. meet the 500 ---- */
  var STATUS = [['secure', 'Secure', 'circle', true], ['wealth', 'Too little wealth', 'circle', false], ['col', 'Below the cost of living', 'square', false], ['b30', 'Below 30 days of basic living', 'diamond', false]];
  function status(hex) { var f = parseInt(hex, 16); return f & 1 ? 3 : f & 2 ? 2 : f & 4 ? 1 : 0; }
  function glyph(s) { var g = STATUS[s];
    if (g[2] === 'square') return '<svg viewBox="0 0 10 10" aria-hidden="true"><rect x="1.2" y="1.2" width="7.6" height="7.6" rx="1" class="st' + s + '"/></svg>';
    if (g[2] === 'diamond') return '<svg viewBox="0 0 10 10" aria-hidden="true"><path d="M5 .4L9.6 5L5 9.6L.4 5Z" class="st' + s + '"/></svg>';
    return '<svg viewBox="0 0 10 10" aria-hidden="true"><circle cx="5" cy="5" r="' + (g[3] ? 3.4 : 4.2) + '" class="st' + s + '"/></svg>'; }
  function keyHTML() { return '<p class="fx-counts" aria-hidden="true">' + STATUS.map(function (g, i) { return '<span><span class="fx-sevkey">' + glyph(i) + '</span>' + g[1] + '</span>'; }).join('') + '</p>'; }
  var people = {data: null, key: null};
  function renderPeople() {
    var host = $('fx-people-body'); if (!host || !people.visible) return;
    var k = REL.env + '-' + yrs();
    if (people.key !== k) { people.key = k; host.innerHTML = '<p class="fx-loading">Loading one run’s 500 adults…</p>';
      lives(REL.env, yrs()).then(function (d) { if (people.key !== k) return; people.data = d; ST.year = d._meta.years; buildPeople(); }).catch(function (e) { host.innerHTML = failNote(e); }); return; }
    if (people.data) updatePeople();
  }
  function buildPeople() {
    var d = people.data, n = d.lives.release.f.length, Y = d._meta.years, host = $('fx-people-body');
    host.innerHTML = '<div class="fx-scrub"><label for="fx-year">Year</label><input type="range" id="fx-year" min="1" max="' + Y + '" step="1" value="' + ST.year + '" aria-describedby="fx-year-out">' +
      '<output id="fx-year-out" for="fx-year"></output><button type="button" class="fx-btn" id="fx-play"' + (reduce ? ' hidden' : '') + '>Play the years</button></div>' + keyHTML() +
      '<div class="fx-people">' + ['release', 'base'].map(function (run) { return '<div class="fx-people-run" data-run="' + run + '"><h3>' + (run === 'release' ? 'With Compassionism' : 'No programme') + ' <small id="fx-cnt-' + run + '"></small></h3>' +
        '<div class="fx-grid500" role="grid" aria-label="' + (run === 'release' ? 'With Compassionism' : 'No programme') + ': the ' + n + ' adults of one run; use the arrow keys to move, Enter to see an adult’s life path">' +
        Array.apply(null, {length: n}).map(function (_, i) { return '<button type="button" role="gridcell" data-i="' + i + '" tabindex="' + (i === 0 ? 0 : -1) + '"></button>'; }).join('') + '</div><p class="fx-counts" id="fx-tally-' + run + '"></p></div>'; }).join('') + '</div>' +
      '<div class="fx-person" id="fx-person" hidden></div>';
    var rng = $('fx-year'); rng.oninput = function () { ST.year = +rng.value; updatePeople(); };
    var playing = null; $('fx-play').onclick = function () { var b = this; if (playing) { clearInterval(playing); playing = null; b.textContent = 'Play the years'; return; }
      if (ST.year >= Y) ST.year = 0; b.textContent = 'Pause'; playing = setInterval(function () { ST.year++; rng.value = ST.year; updatePeople(); if (ST.year >= Y) { clearInterval(playing); playing = null; b.textContent = 'Play the years'; } }, 450); };
    Array.prototype.forEach.call(host.querySelectorAll('.fx-grid500'), function (g) {
      g.addEventListener('click', function (ev) { var b = ev.target.closest('button'); if (b) person(+b.getAttribute('data-i')); });
      g.addEventListener('keydown', function (ev) { var b = ev.target.closest('button'); if (!b) return; var i = +b.getAttribute('data-i'), j = i;
        if (ev.key === 'ArrowRight') j = i + 1; else if (ev.key === 'ArrowLeft') j = i - 1; else if (ev.key === 'ArrowDown') j = i + 25; else if (ev.key === 'ArrowUp') j = i - 25; else if (ev.key === 'Home') j = 0; else if (ev.key === 'End') j = n - 1; else return;
        ev.preventDefault(); j = Math.max(0, Math.min(n - 1, j)); var t = g.children[j]; b.tabIndex = -1; t.tabIndex = 0; t.focus(); });
    });
    updatePeople(); if (ST.person != null) person(ST.person);
  }
  function updatePeople() {
    var d = people.data; if (!d || !$('fx-year')) return; var y = ST.year - 1, Y = d._meta.years;
    $('fx-year-out').textContent = 'year ' + ST.year + ' of ' + Y;
    ['release', 'base'].forEach(function (run) {
      var L = d.lives[run], g = doc.querySelector('.fx-people-run[data-run="' + run + '"] .fx-grid500'), cnt = [0, 0, 0, 0], part = 0;
      L.f.forEach(function (row, i) { var s = status(row[y]), b = g.children[i]; cnt[s]++; if (parseInt(row[y], 16) & 8) part++;
        if (b._s !== s) { b.innerHTML = glyph(s); b._s = s; }
        b.setAttribute('aria-label', 'Adult ' + (i + 1) + ': ' + STATUS[s][1].toLowerCase() + ' in year ' + ST.year + (run === 'release' ? ((parseInt(row[y], 16) & 8) ? ', taking part' : ', not taking part') : '')); b.setAttribute('aria-pressed', String(ST.person === i)); });
      $('fx-tally-' + run).innerHTML = STATUS.map(function (g2, i) { return '<span><span class="fx-sevkey">' + glyph(i) + '</span>' + cnt[i] + ' ' + g2[1].toLowerCase() + '</span>'; }).join('') + (run === 'release' ? '<span>' + part + ' taking part</span>' : '');
    });
    var pr = doc.querySelector('.fx-people'); if (pr) pr.setAttribute('data-view', ST.view);
  }
  function person(i) {
    var d = people.data; if (!d) return; ST.person = i; var Y = d._meta.years, box = $('fx-person'), rel = d.lives.release, b = d.lives.base;
    var yrsIn = rel.f[i].split('').filter(function (h) { return parseInt(h, 16) & 8; }).length;
    box.hidden = false;
    box.innerHTML = '<h4>Adult ' + (i + 1) + ' of run ' + d._meta.lifeSeed + ', ' + F.envName(REL.env) + '</h4><p class="fx-note">Savings each year in today’s dollars, with Compassionism and with no programme; below, the adult’s situation each year. Took part in the programme in ' + yrsIn + ' of ' + Y + ' years.</p>' +
      '<div class="fx-chart" id="fx-life"></div>' + ['release', 'base'].map(function (run) { var L = d.lives[run].f[i];
        return '<p class="fx-note" style="margin:6px 0 2px">' + (run === 'release' ? 'With Compassionism' : 'No programme') + '</p><div class="fx-statusrow" style="grid-template-columns:repeat(' + Y + ',1fr)" role="img" aria-label="' + (run === 'release' ? 'With Compassionism' : 'No programme') + ', year by year: ' +
          L.split('').map(function (h, t) { return 'year ' + (t + 1) + ' ' + STATUS[status(h)][1].toLowerCase(); }).join('; ') + '">' + L.split('').map(function (h) { var s = status(h); return '<i class="st' + s + '" style="' + (s ? 'background:var(--fx-sev' + s + ')' : 'background:var(--fx-sev0)') + '"></i>'; }).join('') + '</div>'; }).join('') +
      '<p class="fx-note">One adult in one run, to show what the averages are made of; the figures to quote are the averages over all ' + num('meta.seeds', 'int') + ' runs above.</p>';
    var xs = Array.apply(null, {length: Y}).map(function (_, t) { return t + 1; });
    C.responsive($('fx-life'), function () { C.xy($('fx-life'), {x: xs, xLabel: function (v, full) { return full ? 'Year ' + v : String(v); }, yFmt: function (v) { return F.fmt(v, 'usd').replace(/,000$/, 'k'); }, tipFmt: function (v) { return F.fmt(v, 'usd'); }, height: 220,
      series: [{name: 'No programme', cls: 's-without', dash: true, values: b.w[i].map(function (v) { return v*100; })}, {name: 'Compassionism', cls: 's-with', values: rel.w[i].map(function (v) { return v*100; })}],
      refs: [{y: WL(), label: 'too little wealth below this line'}], label: 'Savings of adult ' + (i + 1) + ' each year, with and without the programme'}); });
    updatePeople();
    if (box.scrollIntoView && !reduce) box.scrollIntoView({block: 'nearest', behavior: 'smooth'});
  }

  /* ---- 3. how poverty moves over time ---- */
  var TM = {f0: ['Below the cost of living', 'p1', '% of adults that year'], pov: ['Too little wealth', 'p1', '% of adults that year'], bO: ['Below 30 days of basic living', 'p1', '% of adults that year'], medW: ['Median savings (today’s dollars)', 'usd', 'today’s dollars']};
  function renderTime() {
    var host = $('fx-time-chart'); if (!host) return; var m = ST.measure, y = yrs(), e = REL.env, P = E(), B = R.x.bands[y] && R.x.bands[y].envs[e] ? R.x.bands[y].envs[e].bands : null, n = T();
    var xs = Array.apply(null, {length: n}).map(function (_, t) { return t + 1; }), M = TM[m];
    var ser = [{name: 'No programme', cls: 's-without', dash: true, values: P.base.path[m].slice(0, n)}, {name: 'Compassionism', cls: 's-with', values: P.rows.release.path[m].slice(0, n)}];
    if (B) { var bandOf = function (k) { return {lo: B[k][m].p10, hi: B[k][m].p90}; }; ser[0].band = bandOf('base'); ser[1].band = bandOf('release'); if (ST.view === 'with') delete ser[0].band; else delete ser[1].band; }
    if (ST.extra) { if (P.rows.h1.path) ser.push({name: 'Every dollar backed (H1)', cls: 's-alt', values: P.rows.h1.path[m].slice(0, n)}); if (P.rows.mid && P.rows.mid.path) ser.push({name: 'Middle reading', cls: 's-mid', dash: true, values: P.rows.mid.path[m].slice(0, n)}); }
    C.responsive(host, function () { C.xy(host, {x: xs, xLabel: function (v, full) { return full ? 'Year ' + v : String(v); }, xTitle: 'Year', yFmt: m === 'medW' ? function (v) { return F.fmt(v, 'usd').replace(/,000$/, 'k'); } : function (v) { return v + '%'; },
      tipFmt: function (v) { return F.fmt(v, M[1]); }, yMin: m === 'medW' ? undefined : 0, series: ser, label: M[0] + ' each year in ' + F.envName(e) + ', with and without the programme, means over the runs' + (B ? ' with the 10th to 90th percentile across the runs shaded' : ''),
      legendExtra: B ? [{label: '10th–90th percentile across the ' + R.meta.seeds + ' runs (' + (ST.view === 'with' ? 'Compassionism' : 'no programme') + ')', cls: ST.view === 'with' ? 's-with' : 's-without', band: true}] : []}); });
    var bp = 'x.bands.' + y + '.envs.' + e + '.bands.';
    $('fx-time-table').innerHTML = '<div class="fx-tw" tabindex="0" role="region" aria-label="' + F.esc(M[0]) + ' each year"><table class="fx-table"><caption>' + F.esc(M[0]) + ', ' + F.esc(F.envName(e)) + ' (means over the runs' + (B ? '; 10th to 90th percentile in brackets' : '') + ')</caption><thead><tr><th scope="col">Year</th><th scope="col">No programme</th><th scope="col">Compassionism</th>' +
      (ST.extra ? '<th scope="col">Every dollar backed (H1)</th>' : '') + '</tr></thead><tbody>' + xs.map(function (v, t) {
        var c = function (run, pr) { return num(base() + '.' + pr + '.path.' + m + '.' + t, M[1]) + (B ? '<small>' + num(bp + run + '.' + m + '.p10.' + t, M[1]) + '–' + num(bp + run + '.' + m + '.p90.' + t, M[1]) + '</small>' : ''); };
        return '<tr><td>' + v + '</td><td>' + c('base', 'base') + '</td><td>' + c('release', 'rows.release') + '</td>' + (ST.extra ? '<td>' + num(base() + '.rows.h1.path.' + m + '.' + t, M[1]) + '</td>' : '') + '</tr>'; }).join('') + '</tbody></table></div>';
    if (!B) whenVisible(host, function () { bands(y).then(function () { renderTime(); renderWho(); }).catch(function () {}); });
  }

  /* ---- 4. who gains ---- */
  function renderWho() {
    var host = $('fx-who-dec'), y = yrs(), e = REL.env, Bx = R.x.bands[y] && R.x.bands[y].envs[e], n = T();
    if (host) {
      if (!Bx) { host.innerHTML = '<p class="fx-loading">Loading the spread of savings…</p>'; whenVisible(host, function () { bands(y).then(function () { renderWho(); renderTime(); }).catch(function (er) { host.innerHTML = failNote(er); }); }); }
      else { var D = Bx.deciles, rows = [], P = ['10th', '20th', '30th', '40th', '50th (median)', '60th', '70th', '80th', '90th'];
        [['y7', 'Year 7'], ['end', 'Year ' + n + ' (last year)']].forEach(function (t) { P.forEach(function (lbl, i) { rows.push({group: t[1], label: lbl + ' percentile', marks: [{v: D.base[t[0]][i], cls: 's-without', hollow: true, name: 'no programme'}, {v: D.release[t[0]][i], cls: 's-with', name: 'Compassionism'}]}); }); });
        C.responsive(host, function () { C.rows(host, {rows: rows, xFmt: function (v) { return (v < 0 ? '−' : '') + '$' + Math.abs(v/1000) + 'k'; }, tipFmt: function (v) { return F.fmt(v, 'usd'); }, refs: [{v: WL(), label: 'too little wealth below'}],
          xTitle: 'Savings in today’s dollars (the adult at each percentile, averaged over the runs)', label: 'Savings at each tenth of the distribution, with and without the programme, ' + F.envName(e),
          legend: [{label: 'No programme', cls: 's-without', shape: 'circle', hollow: true}, {label: 'Compassionism', cls: 's-with', shape: 'circle'}]}); });
        var dp = 'x.bands.' + y + '.envs.' + e + '.deciles.';
        $('fx-who-table').innerHTML = '<div class="fx-tw" tabindex="0" role="region" aria-label="Savings by percentile"><table class="fx-table"><caption>Savings at each percentile, today’s dollars: no programme against Compassionism</caption><thead><tr><th scope="col">Percentile</th><th scope="col">Year 7</th><th scope="col">Year ' + n + '</th></tr></thead><tbody>' +
          P.map(function (lbl, i) { return '<tr><td>' + lbl + '</td><td>' + num(dp + 'base.y7.' + i, 'usd') + ' vs ' + num(dp + 'release.y7.' + i, 'usd') + '</td><td>' + num(dp + 'base.end.' + i, 'usd') + ' vs ' + num(dp + 'release.end.' + i, 'usd') + '</td></tr>'; }).join('') + '</tbody></table></div>'; 
        var hi = D.release.end.map(function (v, i) { return v > D.base.end[i]; }), up = hi.filter(Boolean).length, dn = hi.length - up, inf = E().rows.release.infl > 0, low = hi.every(function (h, i) { return h === (i < up); });
        $('fx-who-shift').textContent = 'At the last year, ' + (up === D.release.end.length ? 'savings are higher with Compassionism at every tenth of the distribution.' : up === 0 ? 'savings are lower with Compassionism at every tenth of the distribution' + (inf ? ': prices rise with the programme\u2019s new money, and savings in the model earn nothing.' : '.') :
          'savings are higher with Compassionism at ' + (low ? 'the lowest ' + up : up) + ' of the nine tenths shown and lower at ' + (low ? 'the top ' + dn : dn) + (inf && low ? ': the programme lifts those with little, while prices rise with its new money and savings in the model earn nothing, so larger savings lose value.' : '.')); }
    }
    var g = E().rows.release.grp, gp = base() + '.rows.release.grp.', G = [['part', 'Adults who took part'], ['non', 'Adults who did not take part'], ['low', 'The poorest third by starting wage'], ['top', 'The richest third by starting wage']];
    var gh = $('fx-who-grp'); if (!gh) return;
    C.responsive(gh, function () { C.rows(gh, {rows: G.map(function (q) { return {label: q[1], marks: [{v: g[q[0]], cls: g[q[0]] < 0 ? 's-without' : 's-with', shape: g[q[0]] < 0 ? 'square' : 'circle', name: 'change in real resources a year'}]}; }), refs: [{v: 0, label: 'no programme'}],
      xFmt: function (v) { return (v < 0 ? '−' : '') + '$' + Math.abs(v/1000) + 'k'; }, tipFmt: function (v) { return F.fmt(v, 'usd'); }, xTitle: 'Change in real resources per adult a year against no programme (today’s dollars)', label: 'Who gains: change in real resources by group'}); });
    var losers = G.filter(function (q) { return g[q[0]] < 0; });
    $('fx-who-txt').innerHTML = 'Real resources a year against no programme: ' + G.map(function (q) { return q[1].toLowerCase() + ' ' + num(gp + q[0], 'usd'); }).join('; ') + '. ' +
      (losers.length ? 'Worse off than with no programme in real resources: ' + losers.map(function (q) { return q[1].toLowerCase(); }).join(' and ') + '.' : 'No group has fewer real resources than with no programme.') +
      ' Median savings at the last year with Compassionism: ' + num(base() + '.rows.release.medWealth', 'usd') + '. Results by age group are a later step; the model does not report them yet.';
  }

  /* ---- 5. what each part does ---- */
  var PARTS = [
    {h: 'Basic Units (CCO)', mech: 'Every adult who takes part receives a monthly allowance of Basic Units (BU): a currency that buys only essentials (food, housing, utilities, health care) and expires if it is not spent.',
      ev: 'How much people work when they receive money they did not work for: the rate measured in the largest US study of unconditional cash.', lim: 'The BU keeps its value only through the Hub’s rule of indexing it only in a year of high inflation (its Inflation Surge Protocol); savings have no such protection in the main reading.', rd: ['idx', 'all'], hrs: true},
    {h: 'Creative Collectives and conversion', mech: 'Expired BU can be converted to dollars at higher rates, for work the community values, through creative projects organised by the Creative Collectives. A person’s octave sets how much they can convert; it rises with their financial stability.',
      ev: 'Claude’s reading of the design: what the projects deliver counts as new output at market value; the cautious reading counts only the cost of their hours.', lim: 'How much new output conversion calls forth is the decisive unknown; review errors and collusion are tested as readings.', rd: ['cost', 'rev20']},
    {h: 'Essential-service providers (PTF and private)', mech: 'Grocers, utilities and clinics accept BU and convert them to dollars. Community-owned ones (Public Trust Foundations) split what they earn between lower prices, new capacity and their workers; private ones pass what conversion adds to their BU customers as lower prices.',
      ev: 'Running costs from sourced figures; community capacity grows within a year when demand outgrows it, paying for the capital it borrows.', lim: 'No places: community businesses are national averages, and the design’s local charters cannot be represented.', rd: ['free', 'cap5', 'face']},
    {h: 'Community housing (PTH)', mech: 'Public Trust Housing lowers housing costs and builds residents’ equity (Acre Equity) instead of paying market rent.',
      ev: 'Where landlords outside community housing raise rents when BU pay the rent: housing-voucher evidence (Collinson and Ganong 2018; Susin 2002), tested as readings.', lim: 'Single adults only, with no households; rent capture is the largest robustness risk the readings found.', rd: ['hcap', 'hcaphi']},
    {h: 'Zones and the civic portal (SZH, CIP)', mech: 'Zone coordination (Social Zone Harmonization) and a civic internet portal (Citizens Internet Portal) complete the design, organising where the community businesses and housing go and how members decide.',
      ev: 'Claude’s reading of the design: the model represents them only through the other parts, as national averages.', lim: 'The model has no places, so zone coordination cannot be shown on its own.', rd: []},
    {h: 'Joining and leaving', mech: 'Any adult can join or leave each year, weighing what taking part costs them against what it brings.',
      ev: 'Participation comes out of the model rather than being set; the reading in which taking part costs nothing has every adult join.', lim: 'Nothing in the model collapses if participation falls below the Hub’s participation threshold.', rd: ['all']},
    {h: 'Spending creates jobs', mech: 'In recessions, the programme’s spending fills the idle capacity a recession leaves, at a multiplier from published estimates.',
      ev: 'Normal-times multiplier from Ramey and Zubairy (2018); idle labour from the BLS U-6 measure, tested as readings in years without a recession.', lim: 'In the main reading spending creates jobs only in recessions.', rd: ['slack', 'slacku6']},
    {h: 'The Source (how it is paid for)', mech: 'A Source (the Treasury) issues the BU and pays for every conversion, keeping the conversion tax.',
      ev: 'Claude’s reading of the design: the Hub names no tax that pays the Source, so the model treats what it pays out as new money, except what new output backs; the Kenya cash-transfer study (Egger et al., 2022) anchors a middle reading.', lim: 'With unbacked new money prices rise and erode savings; the optimistic end (every dollar backed) and other ways to pay are readings.', rd: ['h1', 'mid', 'tax']}];
  function readingLine(j) {
    var r = E().rows[j]; if (!r) return ''; var M = F.MEAS[ST.sure], p = base() + '.rows.' + j + '.' + M[2];
    return '<li>' + F.esc(F.SHORT[j] || r.label) + ': ' + num(p + '.0', 's1') + ' points</li>';
  }
  function renderParts() {
    var host = $('fx-parts'); if (!host) return; var M = F.MEAS[ST.sure];
    host.innerHTML = PARTS.map(function (P) { var rl = P.rd.map(readingLine).join('');
      return '<div class="fx-part"><h3>' + F.esc(P.h) + '</h3><dl><dt>What it does</dt><dd>' + F.esc(P.mech) + '</dd><dt>Evidence</dt><dd>' + F.esc(P.ev) + (P.hrs ? ' Hours worked change by ' + num(base() + '.rows.release.hrs', 's1') + '%.' : '') + '</dd><dt>Limit</dt><dd>' + F.esc(P.lim) + '</dd>' +
        (rl ? '<dt>Read differently (' + F.esc(M[0].toLowerCase()) + ', change against no programme; main row ' + num(base() + '.rows.release.' + M[2] + '.0', 's1') + ')</dt><dd><ul style="margin:2px 0 0 1.1em;padding:0">' + rl + '</ul></dd>' : '') + '</dl></div>'; }).join('');
    var X = F.readingsRows(R, yrs(), REL.env, ST.sure, {only: ['face', 'cost', 'cap5', 'free', 'all', 'standins', 'tax']}), ch = $('fx-parts-chart');
    if (X && X.rows.length) C.responsive(ch, function () { C.rows(ch, {rows: X.rows, tipFmt: function (v) { return F.fmt(v, 's1') + ' points'; }, xFmt: function (v) { return (v > 0 ? '+' : v < 0 ? '−' : '') + Math.abs(v); }, refs: [{v: X.main, label: 'main row ' + F.fmt(X.main, 's1')}, {v: 0, label: 'no programme'}],
      xTitle: M[0] + ': change against no programme, points (left is better)', label: 'How the result moves when one part of the design is read differently', legend: [{label: 'Reading (95% interval)', cls: 's-alt', shape: 'circle'}]}); });
  }

  /* ---- 6. what it costs and who pays ---- */
  function renderCost() {
    var host = $('fx-cost'); if (!host) return; var r = E().rows.release, p = base() + '.rows.release.';
    var tile = function (v, t) { return '<div><b>' + v + '</b><span>' + t + '</span></div>'; };
    host.innerHTML = '<div class="fx-kv">' + tile(num(p + 'cost', 'usd'), 'cost per adult a year, today’s dollars (every programme dollar at face value)') + tile(num(p + 'srcPay', 'usd'), 'what the Source pays at conversion, per adult a year') +
      tile(num(p + 'srcTax', 'usd'), 'conversion tax the Source keeps') + tile(num(p + 'srcM', 'usd'), 'of what it pays, backed by new output (capacity built and project work)') + tile(num(p + 'tau', 'p1'), 'of wages: a flat contribution that pays for the community price cuts') + '</div>';
    var pay = ['tax', 'progtax', 'landtax'].filter(function (j) { return E().rows[j]; }), M = F.MEAS[ST.sure], ch = $('fx-pay-chart');
    if (ch) C.responsive(ch, function () { C.rows(ch, {rows: [{label: 'The Source (the main reading)', marks: [{v: r[M[2]][0], lo: r[M[2]][1], hi: r[M[2]][2], cls: 's-with', name: 'change against no programme'}]}].concat(pay.map(function (j) { var x = E().rows[j];
        return {label: F.SHORT[j], marks: [{v: x[M[2]][0], lo: x[M[2]][1], hi: x[M[2]][2], cls: 's-alt', name: 'change against no programme'}], note: x.label + (x.taxCover != null ? '; the tax pays ' + F.fmt(x.taxCover, 'p1') + ' of the cost' : '')}; })),
      refs: [{v: 0, label: 'no programme'}], tipFmt: function (v) { return F.fmt(v, 's1') + ' points'; }, xFmt: function (v) { return (v > 0 ? '+' : v < 0 ? '−' : '') + Math.abs(v); }, xTitle: M[0] + ': change against no programme, points (left is better)', label: 'Ways of paying for it compared', legend: [{label: 'Main reading', cls: 's-with', shape: 'circle'}, {label: 'Another way to pay (not specified by the Hub)', cls: 's-alt', shape: 'circle'}]}); });
    $('fx-pay-txt').innerHTML = pay.map(function (j) { var x = E().rows[j]; return F.esc(F.SHORT[j]) + (x.taxCover != null ? ': the tax takes ' + num(base() + '.rows.' + j + '.taxAvg', 'p1') + ' of wages and pays ' + num(base() + '.rows.' + j + '.taxCover', 'p1') + ' of the cost' + (x.taxCover < 99.5 ? ' (the Source pays the rest as new money)' : '') : ''); }).join('; ') + '.';
    var small = (r.avoidHi + r.avoidW) < 0.1*r.cost;
    $('fx-avoid').innerHTML = '<div class="fx-kv">' + tile(num(p + 'unhousedAvoided', 'n1'), 'fewer unhoused person-years per 1,000 adults a year') + tile(num(p + 'avoidLo', 'usd') + ' to ' + num(p + 'avoidHi', 'usd'), 'saved in shelter, health care and justice costs of homelessness, per adult a year') +
      tile(num(p + 'avoidJail', 'usd'), 'saved from fewer people in prison, per adult a year') + tile(num(p + 'avoidHealth', 'usd'), 'saved from fewer hospital and psychiatric stays, per adult a year') + tile(num(p + 'avoidWHi', 'usd'), 'prisons and health care if the largest published prison effect applied to everyone') + '</div>' +
      '<p class="fx-note">Each from a published causal estimate; child welfare is not counted (the model has no children).' + (small ? ' Together these are a small share of the programme’s cost.' : '') + '</p>';
  }

  /* ---- 7. how sure are we ---- */
  function renderSure() { var host = $('fx-sure-chart'); if (!host) return; if (!F.charts.readings(R, host, {env: REL.env, years: yrs(), measure: ST.sure})) host.innerHTML = '<p class="fx-note">No readings for this view.</p>'; }

  /* ---- the control strip and the change hook ---- */
  function renderAll() { if (!R.panels[yrs()]) return; renderAnswer(); renderPeople(); renderTime(); renderWho(); renderParts(); renderCost(); renderSure(); }
  function viewSeg() {
    var w = $('fx-view'); if (!w) return;
    w.innerHTML = '<span>Show</span><span class="fd-seg" role="group" aria-label="With or without Compassionism"><button type="button" data-v="with">With Compassionism</button><button type="button" data-v="without">No programme</button></span>';
    Array.prototype.forEach.call(w.querySelectorAll('button'), function (b) { b.setAttribute('aria-pressed', String(b.getAttribute('data-v') === ST.view));
      b.onclick = function () { ST.view = b.getAttribute('data-v'); Array.prototype.forEach.call(w.querySelectorAll('button'), function (x) { x.setAttribute('aria-pressed', String(x === b)); }); F.writeState({view: ST.view}, ['view']); renderAll(); }; });
  }
  function measureSeg(id, key, opts, after) { var h = $(id); if (!h) return; h.innerHTML = ''; h.appendChild(F.seg('Measure', opts, ST[key], function (v) { ST[key] = v; F.writeState(key === 'sure' ? {measure: v} : {}, key === 'sure' ? ['measure'] : []); after(); })); }
  function init() {
    if (!REL.data || !REL.data.envs) return;
    loadPanels();
    var q = F.readState({}); if (q.view) ST.view = q.view; if (q.measure) ST.sure = q.measure;
    viewSeg();
    measureSeg('fx-time-measure', 'measure', [['f0', 'Cost of living'], ['pov', 'Too little wealth'], ['bO', '30 days (BLEI)'], ['medW', 'Median savings']], renderTime);
    measureSeg('fx-sure-measure', 'sure', [['pov', 'Too little wealth'], ['f0', 'Cost of living'], ['bO', '30 days (BLEI)']], function () { renderSure(); renderParts(); renderCost(); });
    var ex = $('fx-time-extra'); if (ex) ex.onchange = function () { ST.extra = ex.checked; renderTime(); };
    var orig = window.relRender; window.relRender = function () { var r = orig.apply(this, arguments); try { renderAll(); } catch (e) { if (window.console) console.error(e); } return r; };
    renderAll();
    whenVisible($('people') || doc.body, function () { people.visible = true; renderPeople(); });
    var nav = doc.querySelector('.fx-nav'); if (nav) F.spy(nav);
  }
  if (doc.readyState === 'loading') doc.addEventListener('DOMContentLoaded', function () { setTimeout(init, 0); }); else setTimeout(init, 0);
})();
