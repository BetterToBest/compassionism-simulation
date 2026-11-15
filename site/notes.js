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
  function signed(x, d) { return (x >= 0 ? '+' : '−') + Math.abs(x).toFixed(d === undefined ? 1 : d) + '%'; }
  function xcheck(d) {
    var S = 's39-crosscheck';
    function at(sc, q) { var i = -1; for (var k = 0; k < d.data[0].length; k++) { if (col(d, 'scenario')[k] === sc && col(d, 'quarter')[k] === q && col(d, 'scale')[k].indexOf('full') === 0) i = k; } return i; }
    function val(name, i, f) { return snum(S, 'row ' + i + ' ' + name, f(col(d, name)[i])); }
    var a = at('c22-ref-ea', 12), b = at('c22-ref-ea', 80);
    var h = '<h3 class="fx-h3">What the programme does to prices, and what that rests on</h3>' +
      '<p>Every inflation figure on this page rests on the model’s <strong>placeholder price rule</strong>: all new money that is not matched by extra output reaches the general price level a year later. It is a stated assumption, swept from a quarter to the whole of the new money; it is not a measured pass-through. The evidence that does exist (cash-transfer trials, pandemic stimulus, the model literature) covers much smaller payouts than the programme’s 30–50% of household income a year, so none of it can set the value.</p>' +
      '<p>As a cross-check, the same new money was run in a published outside model of a whole economy, BeforeIT.jl (calibrated to Austria, not the US). In it, after 3 years consumer prices end <strong>' + val('cpi', a, function (x) { return signed(x); }) + '</strong> against its own run without the payout (95% interval ' + val('lo', a, function (x) { return signed(x); }) + ' to ' + val('hi', a, function (x) { return signed(x); }) + '), and after 20 years <strong>' + val('cpi', b, function (x) { return signed(x); }) + '</strong> (' + val('lo', b, function (x) { return signed(x); }) + ' to ' + val('hi', b, function (x) { return signed(x); }) + '). The reason is in its price rule, not in the economy: its firms set prices from their own past prices, their costs and the inflation they expect, and nothing in the rule responds to demand. The money shows up instead as output (real GDP ' + val('gdp', a, function (x) { return signed(x); }) + ' after 3 years) and as government debt (' + val('debt', b, function (x) { return x.toFixed(1); }) + ' years of output after 20 years).</p>' +
      '<p>So neither engine measures how much of the money would reach prices, and the zero is an assumption just as the quantity-theory rule is. The two engines mark out how far the answer depends on the price rule; they do not bound the real value, which for payouts this large could lie outside the range between them. Nothing here shows that the pass-through lies between 0 and 1. The engine’s published figures are unchanged (report: <code>' + esc(d.meta.report) + '</code>, sections 4–6).</p>';
    return h;
  }
  function holm() {
    return '<h3 class="fx-h3">Multiple comparisons: which tests form a family</h3>' +
      '<p>Every interval on this page is a plain 95% interval, unadjusted. Where a statement rests on several tests at once, the studies also say whether it survives <strong>Holm’s step-down correction</strong> at the 5% level, applied to two-sided p-values from the same paired bootstrap over seeds. The families were fixed before any run (study programme, “Analysis”):</p>' +
      '<ul><li><strong>The main effect:</strong> the five primary outcomes together (share below 30 days of basic living, share below the cost of living, share with too little wealth, programme cost per adult, cumulative inflation), for one environment, horizon and design.</li>' +
      '<li><strong>A synergy:</strong> for each outcome, the 11 interaction contrasts together: the whole design’s synergy (the five parts together against the sum of the parts alone) and the 10 pair contrasts within the design.</li>' +
      '<li><strong>A scale effect:</strong> for each outcome, the three larger populations (2,000, 10,000 and 50,000 adults) against 500 adults.</li></ul>' +
      '<p>A synergy is claimed only where its own interval excludes zero; whether it also survives Holm is stated beside it. Studies added later (open access, the community layer, the policy levers) name their own family in their tables, and say whether their intervals are adjusted.</p>';
  }
  function levers(d) {
    var S = 's54-levers', ENV = ['ref', 'adv', 'st'], NAME = {ref: 'Reference', adv: 'Adverse', st: 'Stress'};
    function sum(des, w) { for (var i = 0; i < d.meta.summary.length; i++) { var r = d.meta.summary[i]; if (r[0] === des && r[1] === w) return {i: i, r: r}; } }
    function sn(des, w, j, name) { var x = sum(des, w); return snum(S, 'meta.summary[' + x.i + '] ' + name, String(x.r[j])); }
    function cellv(des, w, st, env, m) {
      var c = d.columns, k = -1;
      for (var i = 0; i < d.data[0].length; i++) if (col(d, 'design')[i] === des && col(d, 'wage')[i] === w && col(d, 'setting')[i] === st && col(d, 'environment')[i] === env && col(d, 'measure')[i] === m) k = i;
      var v = col(d, 'change')[k], lo = col(d, 'lo')[k], hi = col(d, 'hi')[k];
      return snum(S, 'row ' + k + ' ' + env + ' ' + m, (v >= 0 ? '+' : '−') + Math.abs(v).toFixed(1) + ' (' + (lo >= 0 ? '+' : '−') + Math.abs(lo).toFixed(1) + ' to ' + (hi >= 0 ? '+' : '−') + Math.abs(hi).toFixed(1) + ')');
    }
    var pts = [['c22', 100, 'kp50', 'C2.2, wages keeping up fully, the Source keeps half of project sales'], ['c22', 100, 'svc', 'C2.2, wages keeping up fully, protected account capped at the first $10,000 of savings'], ['c22', 90, 'svc', 'C2.2, wages at 90%, protected account capped at the first $10,000']];
    var h = '<h3 class="fx-h3">Policy levers: what the confirmation on fresh seeds left standing</h3>' +
      '<p>This is a pilot (50 seeds to choose, 50 fresh seeds to confirm). The search looked for a setting of the government’s levers that cuts poverty, harms no one beyond a small margin, and keeps programme inflation under 5 points a year. None met all three, so no best setting is reported. The trade-off front of the search was then rerun on seeds that took no part in choosing it. A point is confirmed when, in all three environments, basket poverty’s interval lies below zero and each no-harm measure’s upper end is at or below half a point (rule 5). Inflation is reported, not required.</p>' +
      '<div class="fx-tw" tabindex="0" role="region" aria-label="Front points entering and passing confirmation"><table class="fx-table"><caption>Points of the front tested on fresh seeds, and how many passed</caption><thead><tr><th>Design</th><th>Wages</th><th>Points entering</th><th>Passed rule 5</th><th>Of those, inflation under 5 points everywhere</th></tr></thead><tbody>' +
      [['rel', 'Release row'], ['c22', 'C2.2 design']].map(function (D) { return [100, 90].map(function (w) { return '<tr><td>' + D[1] + '</td><td>' + w + '%</td><td>' + sn(D[0], w, 4, 'frontPointsTested') + '</td><td>' + sn(D[0], w, 5, 'passedRule5') + '</td><td>' + sn(D[0], w, 6, 'passedRule5AndInflationUnder5') + '</td></tr>'; }).join(''); }).join('') + '</tbody></table></div>' +
      '<div class="fx-tw" tabindex="0" role="region" aria-label="The confirmed points"><table class="fx-table"><caption>The confirmed points: change against no programme on fresh seeds, with 95% interval (basket poverty and wealth poverty in points; non-participants’ big income falls per 100 adult-years; inflation in points a year)</caption><thead><tr><th>Point</th><th>Environment</th><th>Basket poverty</th><th>Wealth poverty</th><th>Non-participants’ big income falls</th><th>Programme inflation</th></tr></thead><tbody>' +
      pts.map(function (q) { return ENV.map(function (e) { return '<tr><td>' + esc(e === 'ref' ? q[3] : '') + '</td><td>' + NAME[e] + '</td><td>' + cellv(q[0], q[1], q[2], e, 'fgt0PY') + '</td><td>' + cellv(q[0], q[1], q[2], e, 'pov') + '</td><td>' + cellv(q[0], q[1], q[2], e, 'secU25X') + '</td><td>' + cellv(q[0], q[1], q[2], e, 'endoAnn') + '</td></tr>'; }).join(''); }).join('') + '</tbody></table></div>' +
      '<p class="fx-note">Every confirmed point cuts poverty and harms no one beyond the margin, and every one runs at inflation far above 5 points a year, which rests on the placeholder price rule above. No point of the release row is confirmed. These three failed the stricter no-harm test (rule 4: no harm at all) on the choosing seeds and pass the margin test (rule 5) here; both rules were written before any run. A design that pays for the payout with a tax keeps inflation low but raises non-participants’ big income falls; it is a change to the design itself and has not been decided.</p>';
    return h;
  }
  var NOTES = [['s47-spend', spend], ['s39-crosscheck', xcheck], ['s54-levers', levers], [null, holm]];
  function mount(host) {
    NOTES.forEach(function (n) {
      var blk = document.createElement('div'); blk.className = 'fx-note-block'; host.appendChild(blk);
      if (!n[0]) { blk.innerHTML = n[1](); return; }
      F.fetchJSON('data/studies/' + n[0] + '.json').then(function (d) { blk.innerHTML = n[1](d); })
        .catch(function (e) { blk.innerHTML = '<p class="fx-banner">Could not load ' + esc(n[0]) + ' (' + esc(e.message) + ').</p>'; });
    });
  }
  root.CSS_NOTES = {mount: mount};
})(window);
