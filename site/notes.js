/* Method notes on the findings page (S7 part 2): text sections written from data/studies/*.json. No number is typed here; each is read from the study file
 * and printed with its path (class "snum"). Needs site/findings.js (window.CSF). */
(function (root) {
  'use strict';
  var F = root.CSF, esc = F.esc;
  function pct(x, d) { return (x * 100).toFixed(d === undefined ? 1 : d) + '%'; }
  function snum(file, path, text) { return '<span class="snum" data-study="' + file + '" data-src="' + esc(path) + '">' + esc(text) + '</span>'; }
  function col(d, name) { return d.data[d.columns.indexOf(name)]; }
  function rowsOf(d, f) { var n = d.data[0].length, out = []; for (var i = 0; i < n; i++) { var r = {}; d.columns.forEach(function (c, j) { r[c] = d.data[j][i]; }); if (f(r)) out.push(r); } return out; }
  function spend(d) {
    var c = d.meta.calib, S = 's47-spend';
    var h = '<h3 class="fx-h3">The saving-rate target, stated exactly</h3>' +
      '<p>The model’s spending share is set so that its no-programme run saves what US households save. The target is the personal saving rate in the Bureau of Economic Analysis’s national accounts: NIPA Table 2.1, line 35, saving as a share of disposable personal income (FRED series A072RC1A156NBEA), annual 2025, <strong>' + snum(S, 'meta.calib.targetRate', pct(c.targetRate)) + '</strong> (value as updated September 30, 2026). The model’s numerator is its adults’ disposable income less everything they spend in the year (the cost of living and their discretionary spending, net of the debt written off at the wealth floor); its denominator is their disposable income (pay, Social Security, unemployment insurance, the safety net’s cash net of tax, and interest). Both are summed over the run’s own 20 years only.</p>' +
      '<p>The share that reaches the target in the frozen no-programme run is <strong>' + snum(S, 'meta.calib.spendFrozen', String(c.spendFrozen)) + '</strong>. It is an aggregate calibration: it makes the whole population’s saving match one national figure. It is not a measurement of how any household behaves, and no programme result was looked at to choose it (report: <code>' + esc(d.meta.report) + '</code>).</p>';
    h += '<h3 class="fx-h3">The 0.593 rows, as a bridge to the published figures</h3>' +
      '<p>The published engine keeps the earlier share, <strong>' + snum(S, 'meta.calib.spendSourced', String(c.spendSourced)) + '</strong>, which reproduced the target on the earlier, simpler run (' + snum(S, 'meta.calib.publishedSavingRate', pct(c.publishedSavingRate, 2)) + '). On the frozen model, the same share saves <strong>' + snum(S, 'meta.calib.frozenSavingAtSourced', pct(c.frozenSavingAtSourced)) + '</strong> of income, nearly four times the target. The rows below are shown as a bridge from the published figures to the frozen ones. They are not an alternative reading of the frozen model.</p>';
    var rows = rowsOf(d, function (r) { return r.section === 'levels' && r.environment === 'Reference' && (r.measure === 'wealth poverty, year 20 (%)' || r.measure === 'median real wealth, year 20 ($)'); });
    h += '<div class="fx-tw" tabindex="0" role="region" aria-label="Bridge from 0.593 to 0.877"><table class="fx-table"><caption>Reference environment, 50 paired seeds, 20 years: the same runs at the two spending shares (the study’s own table; change shown with its 95% interval)</caption><thead><tr><th>Design</th><th>Measure</th><th>At 0.593</th><th>At 0.877</th><th>Change</th></tr></thead><tbody>' +
      rows.map(function (r) { return '<tr><td>' + esc(r.design) + '</td><td>' + esc(r.measure) + '</td><td>' + esc(String(r['at share 0.593'])) + '</td><td>' + esc(String(r['at share 0.877'])) + '</td><td>' + esc(r['change, 0.877 against 0.593']) + '</td></tr>'; }).join('') + '</tbody></table></div>' +
      '<p class="fx-note">Every environment and design is in the study’s file (“The spending share”, under Every preregistered study below). A higher share leaves less saved, so wealth poverty rises most where the programme’s inflation erodes savings.</p>';
    return h;
  }
  var NOTES = [['s47-spend', spend]];
  function mount(host) {
    NOTES.forEach(function (n) { F.fetchJSON('data/studies/' + n[0] + '.json').then(function (d) { var s = document.createElement('div'); s.className = 'fx-note-block'; s.innerHTML = n[1](d); host.appendChild(s); })
      .catch(function (e) { host.insertAdjacentHTML('beforeend', '<p class="fx-banner">Could not load ' + esc(n[0]) + ' (' + esc(e.message) + ').</p>'); }); });
  }
  root.CSS_NOTES = {mount: mount};
})(window);
