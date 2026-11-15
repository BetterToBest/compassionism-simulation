/* Preregistered studies since v5.6 (S7 part 2): every estimate of each study file in data/studies/, filterable, paged, downloadable.
 * No number is typed here: each file's rows are printed as the study wrote them (dev/tools/study_files.py). Needs site/findings.js (window.CSF). */
(function (root) {
  'use strict';
  var F = root.CSF, esc = F.esc;
  var STUDIES = [
    ['r2-effects', 'Round 2: the main effects (release 2)', 'Five outcomes, each design against no programme, at the main row, in three environments and two horizons, with the erosion share of each wealth figure. Engine 104691f, seeds 1-500.'],
    ['r2-curves', 'Round 2: how sure we are (release 2)', 'Every outcome across the preregistered readings: range, how many keep the sign, robust or fragile; the financed rows are marked.'],
    ['r2-backing', 'Round 2: how much new output backs the payout (release 2)', 'Effects at each backed share, the model’s own mechanism’s point and the break-even share.'],
    ['r2-financed', 'Round 2: paid for by a contribution instead (release 2)', 'Shown, never led with: the contribution needed, debt and the effects. Fragile across readings.'],
    ['r2-distribution', 'Round 2: who gains (release 2)', 'Wealth and income shares, percentiles, families in debt, mobility and labour’s share.'],
    ['r2-work', 'Round 2: work (release 2)', 'Employment, hours, participation, leaving the labour force.'],
    ['s36-synergy', 'Synergy of the design’s five parts (S36)', 'Shapley shares and interactions, with 95% intervals; a synergy is claimed only where the interaction’s interval excludes zero.'],
    ['s38-layer', 'What the community and zone layer change (S38)', 'The layer on against off, and its interactions with the other parts.'],
    ['s5-participation', 'Participation threshold (S5)', 'Outcomes at each participation level and each level’s departure from a straight line.'],
    ['s55-open-access', 'Open access to community-owned providers (S55)', 'Anyone may buy at their prices, against members only. A conditional model result: see the report for what it rests on.'],
    ['s6-c22-pilot', 'Coverage and adequacy of the tax-financed design (S6, pilot)', 'A 100-seed pilot, not the full study; the frozen full panel is in the release data.'],
    ['s14-lw-pilot', 'Cost-of-living line weighted by where people live (S14, pilot)', 'A pilot (study L); labelled as such.'],
    ['s47-spend', 'The spending share (S47)', 'What the earlier share, 0.593, and the share that gives the saving-rate target on the frozen model, 0.877, do to each outcome; the bridge between the published figures and the frozen ones.'],
    ['s34-baseline', 'The no-programme baseline against outside data (S34)', 'The model without the programme set beside survey and national-accounts figures.'],
    ['s5-groups', 'Participants and non-participants (S5)', 'Each group against its own no-programme figure, from the participation study.'],
    ['s54-levers', 'Policy levers (S54)', 'Every lever a policymaker could set, the points that entered confirmation and those that survived; pilot seeds are labelled.'],
    ['s39-crosscheck', 'Outside engine cross-check (S39)', 'The same questions put to an outside model (BeforeIT, Austria); its prices follow expected inflation, so it is not a test of the placeholder price rule.'],
    ['s7-spend-groups', 'Saving and spending by income group (S7)', 'The frozen no-programme row split into five income groups; the all-adults rate is the calibration target.'],
    ['s7-savings', 'Ordinary and inflation-protected savings (S7)', 'Wealth poverty under three readings of what savings do, each against its own no-programme control.'],
    ['s7-pairing', 'Variance reduction from paired seeds (S7)', 'How much pairing a programme run with its no-programme run narrows the intervals.']
  ];
  var PAGE = 40;
  function fmt(v) { if (v === null || v === undefined) return ''; if (typeof v !== 'number') return String(v); var a = Math.abs(v); return a >= 100 ? v.toFixed(1) : a >= 1 ? v.toFixed(2) : a === 0 ? '0' : v.toPrecision(3); }
  function csv(cols, rows) { var q = function (x) { x = x === null ? '' : String(x); return /[",\n]/.test(x) ? '"' + x.replace(/"/g, '""') + '"' : x; }; return [cols.map(q).join(',')].concat(rows.map(function (r) { return r.map(q).join(','); })).join('\n') + '\n'; }
  function render(host, id, d) {
    var cols = d.columns, rows = d.data, m = d.meta, flt = {}, page = 0;
    var cat = cols.map(function (c, j) { var s = {}; rows.forEach(function (r) { s[r[j]] = 1; if (Object.keys(s).length > 40) return; }); var k = Object.keys(s); return typeof rows[0][j] === 'number' || k.length > 40 || k.length < 2 ? null : k; });
    var box = document.createElement('div'); host.appendChild(box);
    box.innerHTML = '<p class="fx-note">Preregistration <code>' + esc(m.prereg) + '</code>; report <code>' + esc(m.report) + '</code>; engine <code>' + esc(String(m.engine).slice(0, 7)) + '</code>; ' +
      (m.seeds ? esc(String(m.seeds)) + ' seeds; ' : '') + esc(m.rows) + '. Results folder: <code>' + esc(m.resultsFolders) + '</code> in compassionism-sim-results. Outcome keys are explained in the report.</p>';
    var bar = document.createElement('div'); bar.className = 'fx-strip-bar'; box.appendChild(bar);
    cols.forEach(function (c, j) { if (!cat[j]) return; var l = document.createElement('label'); l.className = 'fx-note'; l.textContent = c + ' ';
      var s = document.createElement('select'); s.innerHTML = '<option value="">all</option>' + cat[j].map(function (k) { return '<option>' + esc(k) + '</option>'; }).join('');
      s.onchange = function () { flt[j] = s.value; page = 0; draw(); }; l.appendChild(s); bar.appendChild(l); });
    var out = document.createElement('div'); box.appendChild(out);
    function sel() { return rows.filter(function (r) { return Object.keys(flt).every(function (j) { return !flt[j] || String(r[j]) === flt[j]; }); }); }
    function draw() {
      var s = sel(), pg = s.slice(page * PAGE, page * PAGE + PAGE);
      out.innerHTML = '<p class="fx-note">' + s.length + ' of ' + rows.length + ' rows</p><div class="fx-tw" tabindex="0" role="region" aria-label="Study estimates"><table class="fx-table"><caption>Estimates, as the study wrote them</caption><thead><tr>' + cols.map(function (c) { return '<th>' + esc(c) + '</th>'; }).join('') + '</tr></thead><tbody>' +
        pg.map(function (r) { return '<tr>' + r.map(function (v) { return '<td>' + esc(fmt(v)) + '</td>'; }).join('') + '</tr>'; }).join('') + '</tbody></table></div>';
      var nav = document.createElement('p'), mk = function (t, f, dis) { var b = document.createElement('button'); b.type = 'button'; b.textContent = t; b.disabled = dis; b.onclick = f; nav.appendChild(b); nav.appendChild(document.createTextNode(' ')); };
      mk('Previous', function () { page--; draw(); }, page === 0); mk('Next', function () { page++; draw(); }, (page + 1) * PAGE >= s.length);
      mk('Download these rows (CSV)', function () { F.download(id + '.csv', csv(cols, s), 'text/csv'); }, false);
      mk('Download the whole file (JSON)', function () { F.download(id + '.json', JSON.stringify(d), 'application/json'); }, false); out.appendChild(nav);
    }
    draw();
  }
  function mount(host) {
    STUDIES.forEach(function (s) { var id = s[0], det = document.createElement('details'); det.className = 'fx-more'; det.id = 'study-' + id;
      det.innerHTML = '<summary>' + esc(s[1]) + '</summary>'; var w = document.createElement('div'); w.innerHTML = '<p class="fx-note">' + esc(s[2]) + '</p>'; det.appendChild(w); host.appendChild(det);
      det.addEventListener('toggle', function () { if (!det.open || w.dataset.done) return; w.dataset.done = '1';
        F.fetchJSON('data/studies/' + id + '.json').then(function (d) { if (d.envs && !d.data) { w.insertAdjacentHTML('beforeend', '<p class="fx-note">This study’s numbers are in the data file: <a href="data/studies/' + id + '.json">data/studies/' + id + '.json</a>.</p>'); return; } render(w, id, d); })
          .catch(function (e) { w.insertAdjacentHTML('beforeend', '<p class="fx-banner">Could not load the file (' + esc(e.message) + ').</p>'); }); }); });
  }
  root.CSS_STUDIES = {mount: mount};
})(window);
