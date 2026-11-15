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
    var pts = [['c22', 100, 'kp50', 'C2.2, wages keeping up fully, the Source keeps half of project sales'], ['c22', 100, 'svc', 'C2.2, wages keeping up fully, protected account capped at the first $10,000 of savings'], ['c22', 90, 'svc', 'C2.2, wages at 90%, protected account capped at the first $10,000'], ['c22', 100, 'fflat', 'NOT confirmed: C2.2 paid for by a flat contribution on wages (tax-financed), wages keeping up fully']];
    var h = '<h3 class="fx-h3">Policy levers: what the confirmation on fresh seeds left standing</h3>' +
      '<p>This is a pilot (50 seeds to choose, 50 fresh seeds to confirm). The search looked for a setting of the government’s levers that cuts poverty, harms no one beyond a small margin, and keeps programme inflation under 5 points a year. None met all three, so no best setting is reported. The trade-off front of the search was then rerun on seeds that took no part in choosing it. A point is confirmed when, in all three environments, basket poverty’s interval lies below zero and each no-harm measure’s upper end is at or below half a point (rule 5). Inflation is reported, not required.</p>' +
      '<div class="fx-tw" tabindex="0" role="region" aria-label="Front points entering and passing confirmation"><table class="fx-table"><caption>Points of the front tested on fresh seeds, and how many passed</caption><thead><tr><th>Design</th><th>Wages</th><th>Points entering</th><th>Passed rule 5</th><th>Of those, inflation under 5 points everywhere</th></tr></thead><tbody>' +
      [['rel', 'Release row'], ['c22', 'C2.2 design']].map(function (D) { return [100, 90].map(function (w) { return '<tr><td>' + D[1] + '</td><td>' + w + '%</td><td>' + sn(D[0], w, 4, 'frontPointsTested') + '</td><td>' + sn(D[0], w, 5, 'passedRule5') + '</td><td>' + sn(D[0], w, 6, 'passedRule5AndInflationUnder5') + '</td></tr>'; }).join(''); }).join('') + '</tbody></table></div>' +
      '<div class="fx-tw" tabindex="0" role="region" aria-label="The confirmed points"><table class="fx-table"><caption>The confirmed points, and the tax-financed C2.2 beside them (500 adults, 20 years, 50 fresh seeds): change against no programme on fresh seeds, with 95% interval (basket poverty and wealth poverty in points; non-participants’ big income falls per 100 adult-years; inflation in points a year)</caption><thead><tr><th>Point</th><th>Environment</th><th>Basket poverty</th><th>Wealth poverty</th><th>Non-participants’ big income falls</th><th>Programme inflation</th></tr></thead><tbody>' +
      pts.map(function (q) { return ENV.map(function (e) { return '<tr><td>' + esc(e === 'ref' ? q[3] : '') + '</td><td>' + NAME[e] + '</td><td>' + cellv(q[0], q[1], q[2], e, 'fgt0PY') + '</td><td>' + cellv(q[0], q[1], q[2], e, 'pov') + '</td><td>' + cellv(q[0], q[1], q[2], e, 'secU25X') + '</td><td>' + cellv(q[0], q[1], q[2], e, 'endoAnn') + '</td></tr>'; }).join(''); }).join('') + '</tbody></table></div>' +
      '<p class="fx-note">Every confirmed point cuts poverty and harms no one beyond the margin, and every one runs at inflation far above 5 points a year, which rests on the placeholder price rule above. No point of the release row is confirmed. These three failed the stricter no-harm test (rule 4: no harm at all) on the choosing seeds and pass the margin test (rule 5) here; both rules were written before any run. The last block is the one way found to keep inflation low: pay for the payout with a flat contribution on wages instead of new money. It cuts poverty, but raises non-participants’ big income falls in every environment (its interval’s upper end is above the half-point margin), so it is not confirmed. Every figure here is for 500 adults over 20 years. Adopting a tax-financed design is a change to the design itself and has not been decided.</p>';
    return h;
  }
  function groups(d) {
    var S = 's5-groups', ENV = ['ref', 'adv', 'st'], NAME = {ref: 'Reference', adv: 'Adverse', st: 'Stress'}, LV = [10, 30, 50, 90];
    var idx = {};
    for (var i = 0; i < d.data[0].length; i++) {
      if (col(d, 'study')[i] === 'D10' && col(d, 'yardstick')[i] === 'cps' && col(d, 'raise')[i] === 'off') {
        idx[[col(d, 'env')[i], col(d, 'level_pct')[i], col(d, 'group')[i].charAt(0), col(d, 'measure')[i].charAt(0)].join('|')] = i;
      }
    }
    function sg(x, dg) { return (x >= 0 ? '+' : '−') + Math.abs(x).toFixed(dg === undefined ? 1 : dg); }
    function cellv(e, q, g, m) {
      var k = idx[[e, q, g, m].join('|')];
      return snum(S, 'row ' + k + ' ' + e + ' ' + q + ' ' + g + ' ' + m, sg(col(d, 'change')[k]) + ' (' + sg(col(d, 'lo95')[k]) + ' to ' + sg(col(d, 'hi95')[k]) + ')');
    }
    function part(e, q) { var k = idx[[e, q, 'p', 'b'].join('|')]; return snum(S, 'row ' + k + ' realised_participation_pct', col(d, 'realised_participation_pct')[k].toFixed(1) + '%'); }
    function base(e, g) { var k = idx[[e, 10, g, 't'].join('|')]; return snum(S, 'row ' + k + ' none', col(d, 'none')[k].toFixed(1) + '%'); }
    var h = '<h3 class="fx-h3">Participants and non-participants under opt-in</h3>' +
      '<p>When people opt in, the share with too little wealth rises as participation rises (the participation threshold above). To see who carries that rise, the engine reports two groups separately: the adults who take part and the adults who do not. Each adult carries a take-up flag, so a group is a set of people (assumed the same people with and without the programme, see the note below), and each group is compared with its own figure in the no-programme run (paired by seed). The release row, income yardstick CPS earnings, no pay raise, 10,000 adults, 20 years, 500 seeds.</p>' +
      '<div class="fx-tw" tabindex="0" role="region" aria-label="Participants and non-participants"><table class="fx-table"><caption>Change against the same group with no programme, in percentage points (95% interval over seeds). Without a programme, in Reference, ' + base('ref', 'p') + ' of the future participants and ' + base('ref', 'n') + ' of the non-participants have too little wealth at year 20.</caption>' +
      '<thead><tr><th>Environment</th><th>Take-up</th><th>Participants: below the cost of living</th><th>Non-participants: below the cost of living</th><th>Participants: too little wealth</th><th>Non-participants: too little wealth</th></tr></thead><tbody>' +
      ENV.map(function (e) { return LV.map(function (q, j) { return '<tr><td>' + (j ? '' : NAME[e]) + '</td><td>' + part(e, q) + '</td><td>' + cellv(e, q, 'p', 'b') + '</td><td>' + cellv(e, q, 'n', 'b') + '</td><td>' + cellv(e, q, 'p', 't') + '</td><td>' + cellv(e, q, 'n', 't') + '</td></tr>'; }).join(''); }).join('') +
      '</tbody></table></div>' +
      '<p class="fx-note">Read the two wealth columns together: from 30% take-up upward both groups end with more people short of wealth than without the programme, so the opt-in result does not come from non-participants alone. Non-participants are hit harder in every environment shown, which fits prices rising for everyone while only participants receive the programme’s help. Basket poverty falls for both groups at every level shown, far more for participants until take-up is very high. That the take-up flag is the same in both runs is a modelling assumption; it is read from the no-programme figures of the two groups being equal within a few tenths of a point, not from the engine’s own check. Other levels, the 500-adult study and the pay-raise rows are in the study’s file.</p>';
    return h;
  }
  function spendGroups(d) {
    var S = 's7-spend-groups', G = ['lowest fifth', 'second fifth', 'middle fifth', 'fourth fifth', 'highest fifth', 'all adults'];
    function at(g, m) { for (var i = 0; i < d.data[0].length; i++) { if (col(d, 'group')[i] === g && col(d, 'measure')[i].indexOf(m) === 0) return i; } return -1; }
    function money(g) { var i = at(g, 'income per'); return snum(S, 'row ' + i + ' ' + g + ' income', '$' + Math.round(col(d, 'mean')[i]).toLocaleString('en-US')); }
    function rate(g) { var i = at(g, 'saving rate'); return snum(S, 'row ' + i + ' ' + g + ' saving', col(d, 'mean')[i].toFixed(1) + '% (' + col(d, 'lo95')[i].toFixed(1) + ' to ' + col(d, 'hi95')[i].toFixed(1) + ')'); }
    function sp(g) { var i = at(g, 'spending as'); return snum(S, 'row ' + i + ' ' + g + ' spending', col(d, 'mean')[i].toFixed(0) + '%'); }
    var h = '<h3 class="fx-h3">Saving and spending by income group, with no programme</h3>' +
      '<p>The model lets people with less income spend less than their full cost of living (the income-graded spending rule), and sets one share of any cash surplus to be spent so that the whole population saves what US households save. This table shows what those two rules produce for five income groups. Adults are ranked within each run by their own disposable income over the 20 years; the table is the frozen no-programme run in the Reference environment, 500 adults, 20 years, 100 paired seeds, mean over seeds with a 95% interval.</p>' +
      '<div class="fx-tw" tabindex="0" role="region" aria-label="Saving and spending by income group"><table class="fx-table"><caption>No programme, Reference environment. Saving rate is income less consumption, over income; a negative rate means the group draws down savings or borrows. Spending is shown against the cost-of-living basket (100% = exactly the basket), so it includes surplus the model spends above it.</caption>' +
      '<thead><tr><th>Income group</th><th>Income per adult-year (year-0 dollars)</th><th>Saving rate (95% interval)</th><th>Spending as % of the basket</th></tr></thead><tbody>' +
      G.map(function (g) { return '<tr><td>' + esc(g) + '</td><td>' + money(g) + '</td><td>' + rate(g) + '</td><td>' + sp(g) + '</td></tr>'; }).join('') +
      '</tbody></table></div>' +
      '<p class="fx-note">Read with care. The all-adults saving rate is the calibration target, set by construction, so it is not a finding. The spread across groups is the finding: the lowest fifth draws savings down and the highest fifth saves the most. Ranking by the same income that the saving rate divides by pushes the lowest fifth’s rate down and the highest fifth’s up (a year of low income is a year of low saving), so the spread overstates the gap between lifelong poor and rich households. Whether the model’s spread matches household surveys has not been checked against an outside source; it is a model output, not a measured behaviour.</p>';
    return h;
  }
  function savings(d) {
    var S = 's7-savings', ENVN = ['Reference', 'Adverse', 'Stress'];
    function c(name, i) { return col(d, name)[i]; }
    function sg(x) { return (x >= 0 ? '+' : '−') + Math.abs(x).toFixed(1); }
    var rows = '';
    for (var i = 0; i < d.data[0].length; i++) {
      var first = c('savings', i).indexOf('ordinary') === 0;
      rows += '<tr><td>' + (first ? esc(c('environment', i)) : '') + '</td><td>' + esc(c('savings', i)) + '</td><td>' + snum(S, 'row ' + i + ' none', c('no_programme_pct', i).toFixed(1) + '%') + '</td><td>' +
        snum(S, 'row ' + i + ' programme', c('programme_pct', i).toFixed(1) + '%') + '</td><td>' + snum(S, 'row ' + i + ' change', sg(c('change_pp', i)) + ' (' + sg(c('lo95', i)) + ' to ' + sg(c('hi95', i)) + ')') + '</td></tr>';
    }
    return '<h3 class="fx-h3">Wealth poverty with ordinary and with inflation-protected savings</h3>' +
      '<p>The release programme raises prices, and prices eat savings that earn nothing. The model therefore reports three readings of what savings do, each run with and without the programme so that only the programme’s effect is compared. <strong>Ordinary savings</strong> earn no interest, so inflation erodes them. <strong>Zero real return</strong> pays interest equal to inflation in both runs: savings keep their value and earn nothing more. <strong>Positive real return</strong> pays inflation plus the average real yield on US inflation-protected Treasuries (TIPS, 2003-2025). The second reading is a test of protection, not of a positive return; the third adds the return.</p>' +
      '<div class="fx-tw" tabindex="0" role="region" aria-label="Wealth poverty by savings reading"><table class="fx-table"><caption>Share of adults with too little wealth at year 20 (the wealth-poverty threshold is a design threshold, see the glossary). Change is in percentage points against the same savings reading with no programme, 95% interval over 500 paired seeds, 500 adults, 20 years.</caption>' +
      '<thead><tr><th>Environment</th><th>Savings</th><th>No programme</th><th>Programme</th><th>Change, points</th></tr></thead><tbody>' + rows + '</tbody></table></div>' +
      '<p class="fx-note">The wealth-poverty result of the release programme depends on what happens to savings. With ordinary savings it rises sharply; once savings keep their value it falls instead, and a positive real return on top changes it only slightly. So in this model the rise comes from inflation eroding savings, and the size of that inflation rests on the placeholder price rule above. Stress uses the same no-programme control as Adverse in the panel. These are model results, not forecasts.</p>';
  }
  function pairing(d) {
    var S = 's7-pairing', n = d.data[0].length, lo = 1e9, hi = -1e9, ilo = 0, ihi = 0;
    function c(name, i) { return col(d, name)[i]; }
    for (var i = 0; i < n; i++) { var x = c('variance_reduction_pct', i); if (x < lo) { lo = x; ilo = i; } if (x > hi) { hi = x; ihi = i; } }
    var rows = '';
    for (var j = 0; j < n; j++) {
      rows += '<tr><td>' + esc(c('environment', j)) + '</td><td>' + c('take_up_pct', j) + '%</td><td>' + esc(c('outcome', j)) + '</td><td>' + snum(S, 'row ' + j + ' variance_reduction_pct', c('variance_reduction_pct', j).toFixed(0) + '% (' + c('lo95', j).toFixed(0) + ' to ' + c('hi95', j).toFixed(0) + ')') + '</td><td>' + snum(S, 'row ' + j + ' interval_narrower_pct', c('interval_narrower_pct', j).toFixed(0) + '%') + '</td></tr>';
    }
    return '<h3 class="fx-h3">What pairing the seeds buys</h3>' +
      '<p>Each programme run is paired with a no-programme run that uses the same seed: the same adults and the same shocks. A difference between them then carries only the programme’s effect plus the noise that the two runs do not share. The reduction in variance is one minus the variance of the paired differences divided by the sum of the two runs’ own variances, which is what two independent samples would give. It was measured on study D (500 adults, 500 seeds, 20 years, release row, no raise), at 30% and 90% take-up.</p>' +
      '<div class="fx-tw" tabindex="0" role="region" aria-label="Variance reduction from paired seeds"><table class="fx-table"><caption>Variance reduction from pairing, with a 95% bootstrap interval over seeds. “Interval narrower by” is the matching shrinkage of a confidence interval (its width follows the square root of the variance). Programme inflation and cost are left out: the no-programme run has none, so pairing cannot help them.</caption>' +
      '<thead><tr><th>Environment</th><th>Take-up</th><th>Outcome</th><th>Variance reduction (95% interval)</th><th>Interval narrower by</th></tr></thead><tbody>' + rows + '</tbody></table></div>' +
      '<p class="fx-note">Across these rows pairing removes between ' + snum(S, 'row ' + ilo + ' variance_reduction_pct', lo.toFixed(0) + '%') + ' and ' + snum(S, 'row ' + ihi + ' variance_reduction_pct', hi.toFixed(0) + '%') + ' of the variance. It helps most for the share below the cost of living and least for median wealth at high take-up; the model does not say why, and the reasons were not tested. The reduction measured here is for the contrast of a programme run with its own no-programme run; contrasts between two programme designs were not measured.</p>';
  }
  var NOTES = [['s47-spend', spend], ['s39-crosscheck', xcheck], ['s54-levers', levers], ['s5-groups', groups], ['s7-spend-groups', spendGroups], ['s7-savings', savings], ['s7-pairing', pairing], [null, holm]];
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
