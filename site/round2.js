/* Release 2 on the findings page (S65): round 2 of the engine, beside release 1. Every number is read from data/studies/r2-*.json when the page loads and printed
 * with its path (class "snum"); no figure is typed here. The words follow dev/reports/s64-findings-page-text.md, which follows the preregistered rules of
 * prereg/2026-11-s63-round2-freeze.md (a range across the preregistered readings before the main row's figure; every wealth figure names the price rule and has
 * its erosion share; every inflation figure has the backing statement beside it; the financed rows are never led with). Needs site/findings.js (window.CSF). */
(function (root) {
  'use strict';
  var F = root.CSF, esc = F.esc;
  var FILES = ['r2-effects', 'r2-curves', 'r2-backing', 'r2-financed', 'r2-distribution', 'r2-work', 's82-supply', 's82-breakeven'];  /* S82 (Nov 18, 2026): the v6 readings below full backing */
  var OUT = {bl: 'basic living (adult-years below 30 days, points)', bk: 'cost of living (basket poverty, adult-years, points)', wp: 'wealth poverty, yearly average (points)',
             mw: 'median real wealth (year-0 $)', inf: 'programme inflation (points a year)'};
  /* how each outcome counts the simulated adults (S83): the 18 top-tail adults carry population weights; the poverty shares count every simulated adult once */
  var WTL = {bl: 'Counted per simulated adult (unweighted).', bk: 'Counted per simulated adult (unweighted).', wp: 'Counted per simulated adult (unweighted).',
             mw: 'Counted by population weight (weighted).', inf: 'From the price level, which counts every simulated adult once (unweighted).'};
  var WTS = {bl: 'unweighted', bk: 'unweighted', wp: 'unweighted', mw: 'weighted', inf: 'unweighted'};
  var ENVS = ['Reference', 'Adverse', 'Stress'];
  var D = {};

  function find(file, flt, col) {
    var d = D[file], n = d.data[0].length, ci = d.columns.indexOf(col), hit = -1;
    if (ci < 0) throw new Error(file + ' has no column ' + col);
    for (var i = 0; i < n; i++) {
      var ok = true;
      for (var k in flt) if (d.data[d.columns.indexOf(k)][i] !== flt[k]) { ok = false; break; }
      if (ok) { if (hit >= 0) throw new Error('more than one row in ' + file + ' for ' + JSON.stringify(flt)); hit = i; }
    }
    if (hit < 0) throw new Error('no row in ' + file + ' for ' + JSON.stringify(flt));
    return {i: hit, v: d.data[ci][hit], file: file, col: col};
  }
  function snum(file, i, col, text) { return '<span class="snum" data-study="' + file + '" data-src="row ' + i + ' ' + esc(col) + '">' + esc(text) + '</span>'; }
  function fmtN(x, dg) { return (x < 0 ? '−' : '') + Math.abs(x).toLocaleString('en-US', {minimumFractionDigits: dg, maximumFractionDigits: dg}); }
  function fmtS(x, dg) { return (x < 0 ? '−' : '+') + Math.abs(x).toLocaleString('en-US', {minimumFractionDigits: dg, maximumFractionDigits: dg}); }
  function dollars(x) { return (x < 0 ? '−$' : '$') + Math.abs(Math.round(x)).toLocaleString('en-US'); }
  /* a printed value: kind 'pt' points with one decimal, 'sg' signed points, 'usd' dollars, 'sgusd' signed dollars, 'pc' percent */
  function show(file, flt, col, kind, dg) {
    var r = find(file, flt, col), v = r.v, t;
    if (v === null) t = 'not reported';
    else if (kind === 'usd') t = dollars(v);
    else if (kind === 'sgusd') t = (v < 0 ? '−$' : '+$') + Math.abs(Math.round(v)).toLocaleString('en-US');
    else if (kind === 'sg') t = fmtS(v, dg === undefined ? 1 : dg);
    else if (kind === 'pc') t = fmtN(v, dg === undefined ? 1 : dg) + '%';
    else t = fmtN(v, dg === undefined ? 1 : dg);
    return snum(file, r.i, col, t);
  }
  function ci(file, flt, dg, usd) {
    var f = usd ? function (x) { return dollars(x); } : function (x) { return fmtN(x, dg === undefined ? 1 : dg); };
    var lo = find(file, flt, 'lo95'), hi = find(file, flt, 'hi95');
    return '(' + snum(file, lo.i, 'lo95', f(lo.v)) + ' to ' + snum(file, hi.i, 'hi95', f(hi.v)) + ')';
  }
  function colVals(file, flt, col) {
    var d = D[file], n = d.data[0].length, ci_ = d.columns.indexOf(col), out = [];
    for (var i = 0; i < n; i++) { var ok = true; for (var k in flt) if (flt[k] !== undefined && d.data[d.columns.indexOf(k)][i] !== flt[k]) { ok = false; break; } if (ok) out.push([i, d.data[ci_][i]]); }
    return out;
  }
  function extreme(file, flt, col, kind, dg, usd, pred) {
    var d = D[file], rc = d.columns.indexOf('row');
    var vs = colVals(file, flt, col).filter(function (p) { return p[1] !== null && (!pred || pred(d.data[rc][p[0]])); });
    var lo = vs.reduce(function (a, b) { return b[1] < a[1] ? b : a; }), hi = vs.reduce(function (a, b) { return b[1] > a[1] ? b : a; });
    var f = usd ? dollars : function (x) { return fmtN(x, dg === undefined ? 1 : dg); };
    return {lo: snum(file, lo[0], col, f(lo[1])), hi: snum(file, hi[0], col, f(hi[1])), loV: lo[1], hiV: hi[1]};
  }
  function chartFig(name, alt) {
    return '<figure class="fx-figure"><a href="data/studies/r2-charts/' + name + '.svg"><img src="data/studies/r2-charts/' + name + '.svg" alt="' + esc(alt) + '" loading="lazy" style="max-width:100%;height:auto"></a></figure>';
  }
  function table(caption, head, rows) {
    return '<div class="fx-tw" tabindex="0" role="region" aria-label="' + esc(caption) + '"><table class="fx-table"><caption>' + esc(caption) + '</caption><thead><tr>' +
      head.map(function (h) { return '<th>' + esc(h) + '</th>'; }).join('') + '</tr></thead><tbody>' + rows.map(function (r) { return '<tr>' + r.map(function (c) { return '<td>' + (c === 'C2.2' ? 'Full-coverage design' : c === 'release design' ? 'Opt-in design' : c) + '</td>'; }).join('') + '</tr>'; }).join('') + '</tbody></table></div>';
  }
  var C = 'C2.2', RL = 'release design';

  function cards() {
    var f = {design: C, environment: 'Reference', years: 20};
    function card(label, key, kind, extra) {
      var g = Object.assign({outcome: OUT[key]}, f);
      var n = kind === 'usd' ? 'usd' : 'pc';
      return '<div class="fx-card"><div class="fx-card-k">' + esc(label) + '</div><div class="fx-card-v">' + show('r2-effects', g, 'programme', n) + '</div>' +
        '<div class="fx-note">against ' + show('r2-effects', g, 'no programme', n) + ' with no programme (' + show('r2-effects', g, 'effect', kind === 'usd' ? 'sgusd' : 'sg') + (kind === 'usd' ? '' : ' points') + ')' + (extra || '') + '</div><div class="fx-note">' + esc(WTL[key]) + '</div></div>';
    }
    var er = find('r2-effects', Object.assign({outcome: OUT.mw}, f), 'erosion share of the effect');
    return '<div class="fx-cards">' +
      card('Below 30 days of basic living (adult-years)', 'bl', 'pt') + card('Below the cost of living (the basket of essentials, adult-years)', 'bk', 'pt') +
      card('Too little wealth, yearly average (adults)', 'wp', 'pt') +
      card('Median real wealth at year 20', 'mw', 'usd', '. Rests on full backing (corrected Nov 17, 2026: it said today’s price rule, which full backing barely tests); ' + snum('r2-effects', er.i, 'erosion share of the effect', fmtN(er.v, 1) + '%') + ' of the gain is the erosion of opening balances, in the programme’s favour') + '</div>';
  }
  function range(design, env, years, key, kind, usd) {
    var f = {design: design, environment: env, years: years, outcome: OUT[key]};
    var lo = find('r2-curves', f, 'lowest reading'), hi = find('r2-curves', f, 'highest reading');
    var lab = usd ? dollars : function (x) { return fmtN(x, 1); };
    return [snum('r2-curves', lo.i, 'lowest reading', lab(lo.v)), snum('r2-curves', hi.i, 'highest reading', lab(hi.v))];
  }
  function sureTable(years) {
    var rows = [];
    [C, RL].forEach(function (des) {
      ENVS.forEach(function (env) {
        ['bk', 'bl', 'wp', 'mw'].forEach(function (key) {
          var f = {design: des, environment: env, years: years, outcome: OUT[key]}, usd = key === 'mw', r = range(des, env, years, key, null, usd);
          var kept = find('r2-curves', f, 'readings keeping the sign'), n = find('r2-curves', f, 'readings');
          rows.push([esc(des), env, esc(OUT[key].replace(/ \(.*\)/, '')) + ' (' + WTS[key] + ')', r[0] + ' to ' + r[1], show('r2-effects', f, 'effect', usd ? 'sgusd' : 'sg') + ' ' + ci('r2-effects', f, 1, usd),
            snum('r2-curves', kept.i, 'readings keeping the sign', String(kept.v)) + ' of ' + snum('r2-curves', n.i, 'readings', String(n.v)), esc(find('r2-curves', f, 'class').v)]);
        });
      });
    });
    return table('v5.9, ' + years + ' years: the effect at each preregistered reading (lowest to highest), the main row with its seed interval, and whether every reading keeps its sign',
      ['Design', 'Environment', 'Outcome', 'Across the readings', 'Main row (95% seed interval)', 'Readings keeping the sign', 'Class'], rows);
  }
  /* S82 part 3b (Nov 18, 2026; research-update prereg/2026-11-s82-v6-supply-indexing.md, decision rule 5): the curve below full backing under the
   * v6 readings (a limit on supply, wages that follow prices in part, the BU's delay), with the break-even shares under each. Every figure is read
   * from data/studies/s82-supply.json and s82-breakeven.json (dev/tools/s82_page_data.py); the full-coverage design's main pair only. */
  function s82Section() {
    var BK = 'basket poverty (points)', SV = 's82-supply', SB = 's82-breakeven', m = D[SV].meta;
    function eff(env, rd, a) { return show(SV, {environment: env, years: 20, reading: rd, 'backed share': a, outcome: BK}, 'effect', 'sg'); }
    function be(env, rd, yrs, out) {
      var r = find(SB, {environment: env, years: yrs || 20, reading: rd, outcome: out || BK}, 'break-even share');
      return r.v === null ? esc(D[SB].data[D[SB].columns.indexOf('word')][r.i]) : snum(SB, r.i, 'break-even share', fmtN(r.v, 2));
    }
    var RD = [['no limit', 'No limit on supply (the v5.9 engine)'],
      ['sourced, the market\'s rule', 'Supply limit, sourced; the market\'s rule (those least able to pay go short first)'],
      ['sourced, the design\'s rule', 'Supply limit, sourced; the design\'s rule (basics bought with the BU served first)'],
      ['restricted, the market\'s rule', 'Supply limit, restricted (a policy reading: every sourced value halved, for today\'s land-use, residency and farm policies); the market\'s rule'],
      ['strictest case, the market\'s rule', 'The strictest case: no essentials beyond today\'s needs consumption; not the economy and not the design; the market\'s rule'],
      ['the BU a month behind', 'The BU follows the needs\' price a month behind (the design\'s monthly adjustment)'],
      ['the BU a quarter behind', 'The BU a quarter behind'],
      ['the BU a year behind', 'The BU a year behind (as Social Security\'s adjustment)'],
      ['the BU two years behind (a bound)', 'The BU two years behind (a bound)'],
      ['wages follow half, made up a year later', 'Wages follow half of programme inflation, the rest made up a year later'],
      ['wages follow three quarters, never made up', 'Wages follow three quarters of programme inflation, never made up'],
      ['wages follow half of programme inflation, never made up', 'Wages follow half of programme inflation, never made up']];
    var rows = RD.map(function (r) { return [esc(r[1]), eff('Reference', r[0], 0), eff('Reference', r[0], 0.5), eff('Reference', r[0], 1),
      be('Reference', r[0]) + ' / ' + be('Adverse', r[0]) + ' / ' + be('Stress', r[0]), be('Reference', r[0], 40) + ' / ' + be('Adverse', r[0], 40) + ' / ' + be('Stress', r[0], 40)]; });
    var W = 'wages follow half of programme inflation, never made up', ST = 'strictest case, the market\'s rule', SO = 'sourced, the market\'s rule';
    return '<h3 class="fx-h3">Below full backing: limits on supply, wages and the BU’s adjustment (v6 readings, added Nov 18, 2026)</h3>' +
      '<p>The v5.9 engine had no limit on what the economy can supply, and wages, the BU and the cost-of-living basket followed prices in full and at once. A preregistered study adds each of these as a reading, behind its own switch, and runs it at every backed share on ' + esc(String(m.seeds)) + ' paired seeds. Full backing is the main row, and no reading changes it. In order of what moves the curve least to most:</p><ul>' +
      '<li><strong>A limit on supply</strong> of housing, medical care and food, from the economy’s headroom in opened sources, shared by the market’s rule, evenly, or the design’s rule. It costs little. With no backing in Reference, the programme’s effect on basket poverty is ' + eff('Reference', SO, 0) + ' points under the sourced limit with the market’s rule and ' + eff('Reference', ST, 0) + ' in the strictest case, against ' + eff('Reference', 'no limit', 0) + ' with no limit. <em>But the limit as built moves only basket poverty:</em> the money a cut leaves unspent goes to other goods, and the cut moves no price, so wealth, basic living and inflation are the same with and without it. Basket poverty’s effect keeps its sign, with an interval that excludes zero, under the sourced limit at every share, in every environment and with every rule; for the other outcomes that test says nothing.</li>' +
      '<li><strong>The BU’s adjustment to prices.</strong> The design’s monthly and quarterly adjustments cost little; a yearly or two-year delay costs much more (table).</li>' +
      '<li><strong>Wages that follow programme inflation only in part.</strong> This is what makes the results depend on backing. If wages follow half of it and the rest is never made up, the programme with no backing leaves basket poverty ' + eff('Reference', W, 0) + ' points against no programme in Reference (' + eff('Adverse', W, 0) + ' in Adverse, ' + eff('Stress', W, 0) + ' in Stress): worse than no programme. Median real wealth then breaks even at a backed share of ' + be('Reference', W, 20, 'median real wealth, weighted (year-0 $)') + ' at 20 years and ' + be('Reference', W, 40, 'median real wealth, weighted (year-0 $)') + ' at 40 (Reference). If the rest is made up a year later, the cost is small. No source says how wages follow an inflation the programme itself makes: the readings never made up are the pessimistic end of the range swept.</li></ul>' +
      table('Full-coverage design, Reference, 20 years: the change in basket poverty against no programme at each backed share (points), and the break-even backed share (where the effect is no better than no programme; Reference / Adverse / Stress)',
        ['Reading', 'No backing', 'Half backed', 'Full backing (the main row)', 'Break-even share, 20 years', 'Break-even share, 40 years'], rows) +
      '<p class="fx-note">Effects are programme minus no programme, mean over paired seeds; ' + esc(m.intervals) + '. The wage and BU readings are design parameters, as are the building speed of medical care and food and the essentials’ price response; each is swept in the study, and every result above holds at the slowest building speed and at half and double the price response. Programme inflation is unchanged by the supply limit (inflation stays under 5 points a year only above about ' + snum(SB, find(SB, {environment: 'Reference', years: 20, reading: SO, outcome: 'inflation reaches 5 points a year'}, 'break-even share').i, 'break-even share', fmtN(find(SB, {environment: 'Reference', years: 20, reading: SO, outcome: 'inflation reaches 5 points a year'}, 'break-even share').v, 2)) + ' backing in Reference). One reading of the study (adults who age and are replaced, at no backing) measures a defect and is not shown; it is rerun once fixed. Every figure, with the 40-year horizon, who goes short by fifth of income, and the smaller readings: the report <code>' + esc(m.report) + '</code>, the files <code>data/studies/s82-supply.json</code> and <code>s82-breakeven.json</code> (<code>' + esc(m.command) + '</code>), engine <code>' + esc(m.engine) + '</code>, results <code>' + esc(m.resultsFolder) + '</code> in ' + esc(m.resultsRepo) + '; preregistration ' + esc(m.prereg) + '.</p>';
  }
  function backingTable(design) {
    var rows = [], base = {design: design, environment: 'Reference', years: 20};
    function line(label, row, bs) {
      var out = [esc(label), bs];
      ['bk', 'mw', 'inf'].forEach(function (key) {
        var f = Object.assign({}, base, row, {outcome: OUT[key]}), usd = key === 'mw';
        out.push(show('r2-backing', f, 'effect', usd ? 'sgusd' : 'sg', key === 'inf' ? 2 : 1));
      });
      rows.push(out);
    }
    [0, 0.25, 0.5, 0.75, 1].forEach(function (a) {
      var r = find('r2-backing', Object.assign({}, base, {row: 'grid', 'backed share (fraction of the payout)': a, outcome: OUT.bk}), 'backed share (fraction of the payout)');
      line(a === 1 ? 'Full backing (the main row, as the design states)' : 'Backed share', {row: 'grid', 'backed share (fraction of the payout)': a}, snum('r2-backing', r.i, 'backed share (fraction of the payout)', fmtN(a * 100, 0) + '%'));
    });
    ['the model’s own mechanism', 'the model’s own mechanism, no ceiling'].forEach(function (nm) {
      var name = nm.replace('’', "'"), r = find('r2-backing', Object.assign({}, base, {row: name, outcome: OUT.bk}), 'backed share (fraction of the payout)');
      line(nm.charAt(0).toUpperCase() + nm.slice(1) + ' (where it reaches)', {row: name}, snum('r2-backing', r.i, 'backed share (fraction of the payout)', fmtN(r.v * 100, 1) + '%'));
    });
    var be = find('r2-backing', Object.assign({}, base, {row: 'break-even: inflation 5% a year'}), 'backed share (fraction of the payout)');
    rows.push(['Break-even: programme inflation 5% a year', snum('r2-backing', be.i, 'backed share (fraction of the payout)', fmtN(be.v * 100, 0) + '%'), '', '', '']);
    return table((design === C ? 'Full-coverage design' : 'Opt-in design') + ', Reference, 20 years: effects against no programme at each backed share (change in points, change in $, programme inflation in points a year)',
      ['Reading', 'Backed share', 'Cost of living (points)', 'Median real wealth', 'Programme inflation'], rows);
  }
  function financedTable() {
    var rows = [];
    [C, RL].forEach(function (des) {
      ENVS.forEach(function (env) {
        var f = {design: des, environment: env, years: 20};
        function m(meas, kind, dg) { return show('r2-financed', Object.assign({measure: meas}, f), 'estimate', kind, dg); }
        rows.push([esc(des), env, m('mean contribution (% of the base)', 'pc', 0), m('cost of living (basket poverty, adult-years, points), effect', 'sg', 1), m('median real wealth (year-0 $), effect', 'sgusd'),
          m('government debt at the end (% of GDP)', 'pc', 0)]);
      });
    });
    return table('Paid for by a contribution instead, 20 years (shown, never led with; run without the weighted top tail): the contribution needed, the effects, and debt at the end',
      ['Design', 'Environment', 'Mean contribution', 'Cost of living (points)', 'Median real wealth', 'Government debt (% of GDP)'], rows);
  }
  function distTable() {
    var rows = [], M = [['top 1% share of wealth (%)', 'pc'], ['bottom 50% share of wealth (%)', 'pc'], ['families in debt (%)', 'pc'], ['stayed in the lowest wealth fifth (%)', 'pc'],
                         ['wealth P10 ($)', 'usd'], ['wealth P90 ($)', 'usd'], ["labour's share of money income (%)", 'pc']];
    M.forEach(function (m) {
      [C, RL].forEach(function (des) {
        var f = {design: des, environment: 'Reference', years: 20, measure: m[0]}, usd = m[1] === 'usd';
        rows.push([esc(m[0]), esc(des), show('r2-distribution', f, 'no programme', usd ? 'usd' : 'pc'), show('r2-distribution', f, 'programme', usd ? 'usd' : 'pc'),
          show('r2-distribution', f, 'effect', usd ? 'sgusd' : 'sg') + ' ' + ci('r2-distribution', f, 1, usd)]);
      });
    });
    return table('Who gains: Reference, 20 years, main row. Wealth in year-0 dollars; changes with 95% seed intervals', ['Measure', 'Design', 'No programme', 'Programme', 'Change'], rows);
  }
  function workTable() {
    var rows = [];
    ['employment (% of adult-years)', 'participation (% of adult-years)', 'programme leavers (% of adult-years)', 'outside the labour force (% of adult-years)'].forEach(function (m) {
      [C, RL].forEach(function (des) {
        var f = {design: des, environment: 'Reference', years: 20, measure: m};
        rows.push([esc(m), esc(des), show('r2-work', f, 'no programme', 'pc'), show('r2-work', f, 'programme', 'pc'), show('r2-work', f, 'effect', 'sg') + ' ' + ci('r2-work', f, 1)]);
      });
    });
    return table('Work: Reference, 20 years, main row', ['Measure', 'Design', 'No programme', 'Programme', 'Change (points)'], rows);
  }

  function build() {
    var sp = {bl: 'basic living', bk: 'cost of living', wp: 'wealth poverty', mw: 'median real wealth', inf: 'programme inflation'};
    var inflMech = extreme('r2-backing', {outcome: OUT.inf}, 'effect', null, 1, false, function (r) { return r.indexOf('the model\'s own mechanism') === 0; });
    var mr = find('r2-backing', {design: C, environment: 'Reference', years: 20, row: 'the model\'s own mechanism', outcome: OUT.bk}, 'backed share (fraction of the payout)');
    var mechShare = snum('r2-backing', mr.i, 'backed share (fraction of the payout)', fmtN(mr.v * 100, 1) + '%');
    var nread = find('r2-curves', {design: C, environment: 'Reference', years: 20, outcome: OUT.bk}, 'readings');
    var h = '<h3 class="fx-h3">v5.9: the answer in ten seconds</h3>' +
      '<p>With Compassionism (the full-coverage design), against no programme, Reference, 20 years, main row:</p>' + cards() +
      '<p class="fx-note"><em>Dated note, Nov 19, 2026:</em> these figures pay the private businesses’ lower BU price a year late, out of the previous year’s premium; the design sets it at the sale. A preregistered rerun of the main rows with the price at the sale makes every poverty and wealth effect slightly larger in the programme’s favour and changes no sign and no conclusion: the cards would read 0.8%, 3.2%, 5.7% and $432,879, the cut in basket poverty grows by 0.04 to 0.59 points across the designs, environments and horizons, and programme inflation is unchanged. The corrected figures replace these at the next release. The readings, the financed rows and the erosion shares were not rerun. Report: <code>dev/reports/s90-private-price-at-sale.md</code>; tables: <code>s90-tables-b8ccd8d</code> in compassionism-sim-results.</p>' +
      '<p class="fx-note"><strong>Main row:</strong> every dollar the programme pays is matched by new output, as the design states (a design parameter, not a model estimate). The model’s own mechanism for new output reaches about ' + mechShare + ' of that. See “How much new output backs the payout”, below.</p>' +
      '<p><strong>One sentence.</strong> Across the ' + snum('r2-curves', nread.i, 'readings', String(nread.v)) + ' preregistered readings, both designs lower all three poverty measures and raise median real wealth, in every environment and at both horizons (the table “How sure we are” gives the count for each). These results hold when every dollar paid is matched by new output, which is the design’s statement and not something the model shows; with the model’s own backing mechanism (with or without its ceiling), prices rise ' + inflMech.lo + ' to ' + inflMech.hi + ' points a year across the environments and designs at 20 and 40 years.</p>';
    h += '<h3 class="fx-h3">How sure we are: the range across readings</h3>' +
      '<p>Each preregistered reading changes one setting the design leaves open (how much of their spare cash adults spend, how wealth is held, the price rule’s settings, and others). For each outcome, the curve below shows every reading’s effect. The table gives the range, the main row with its seed interval, and whether every reading keeps its sign. The seed interval covers the model’s randomness only, not the choice of reading; the spread across readings shows that. The wealth figures rest on full backing (<em>corrected Nov 17, 2026:</em> this sentence also said they rest on today’s price rule, but at full backing almost no unmatched money reaches prices, so the price rule is barely tested there; below full backing they rest on it), and only a small part of any of them is the erosion of the balances adults held at the start (in the programme’s favour; if all wealth were cash, against it).</p>' +
      sureTable(20) + '<details class="fx-more"><summary>The same at 40 years</summary>' + sureTable(40) + '</details>' +
      '<p class="fx-note">Each dot in a chart is one preregistered reading, sorted by its effect, with its 95% seed interval. The seed interval covers the model’s randomness only, not the choice of reading; the spread of the dots shows that.</p>' +
      '<details class="fx-more"><summary>The curves, one chart per outcome (the full-coverage design, then the opt-in design; the financed rows beside each)</summary>' +
      [['fgt0PY', 'Cost of living (basket poverty)'], ['bNAPy', 'Basic living'], ['ppovA', 'Wealth poverty, yearly average'], ['wtMedE', 'Median real wealth'], ['endoAnn', 'Programme inflation']].map(function (o) {
        return ['c22', 'rel'].map(function (d) { return [20, 40].map(function (y) { return chartFig('spec-' + d + '-' + o[0] + '-' + y, o[1] + ', ' + (d === 'c22' ? 'full-coverage design' : 'opt-in design') + ', ' + y + ' years: effect at each preregistered reading, three environments, with the financed rows beside. The numbers are in the table above and in the file r2-curves.'); }).join(''); }).join('');
      }).join('') + '</details>';
    h += '<h3 class="fx-h3">Prices, and how much new output backs the payout</h3>' +
      '<p>At the main row, programme inflation is ' + show('r2-effects', {design: C, environment: 'Reference', years: 20, outcome: OUT.inf}, 'effect', 'x', 2) + ' points a year above no programme in Reference at 20 years (full-coverage design): no material change. <strong>The main row assumes that every dollar the programme pays is matched by new output</strong>, as the design states (a design parameter). The model’s own mechanism for new output reaches only the share shown below (and the second figure with its ceiling removed). The poverty effects barely depend on backing; inflation and median wealth do. <em>Replaced Nov 18, 2026:</em> the dated note of Nov 17 said this held because the model had no limit on what the economy can supply. The v6 readings below test it: a limit on supply barely moves the curve, but wages that follow programme inflation only in part, never made up, do. All inflation figures rest on the model’s placeholder price rule (all unmatched new money reaches prices); they are not a forecast.</p>' +
      backingTable('C2.2') + '<details class="fx-more"><summary>The opt-in design, and the backing charts</summary>' + backingTable(RL) +
      ['backing-c22-20', 'backing-c22-40', 'backing-rel-20', 'backing-rel-40'].map(function (n) { return chartFig(n, 'Programme inflation by backed share, with the break-even share and the mechanism’s own points marked (' + n + '); the numbers are in the table above and in the file r2-backing.'); }).join('') + '</details>';
    h += s82Section();
    h += '<h3 class="fx-h3">Paid for by a contribution instead (shown, never led with)</h3>' +
      '<p>If the programme is paid for by a contribution, with the rest borrowed, the contribution needed is far larger and the poverty effects are much smaller, and in some cells they reverse. Nearly every financed result is fragile: 46 of the 48 poverty and wealth curves change sign or lose significance at some reading, depending on how the contribution is set up. The two that hold are the opt-in design’s basic-living effect in Reference, at both horizons. These rows were run without the weighted top tail.</p>' + financedTable();
    h += '<h3 class="fx-h3">Who gains</h3>' +
      '<p>The programme lowers the top 1%’s share of wealth, raises the bottom half’s, and sharply reduces the share of families in debt; the opt-in design moves them about half as far. Below the top fifth of starting wealth, slightly higher prices lower what adults owe (a small gain); at the top, where money is lent, they are a loss. Adults outside the labour force stay far more often below the cost of living than adults in it; the Question 6 report and the erosion tables (r2-erosion-104691f/tables.md in the results repository) give the split.</p>' + distTable();
    h += '<h3 class="fx-h3">Unfavourable results, together</h3><ul>' +
      '<li><strong>Prices:</strong> programme inflation is above no programme in every cell: immaterial at the main row, tens of points a year without backing (table above).</li>' +
      '<li><strong>Wages below full backing:</strong> if wages follow half of programme inflation and the rest is never made up, the programme with no backing leaves more people below the cost of living (basket poverty) than no programme does (v6 readings, above).</li>' +
      '<li><strong>Work:</strong> fewer adults work: participation falls (adults who leave work for the programme), with their earnings forgone.</li>' +
      '<li><strong>Mobility:</strong> less movement out of the lowest wealth fifth (“stayed in the lowest wealth fifth”, above).</li>' +
      '<li><strong>Labour’s share</strong> of money income falls, because the programme’s payments are income that is not wages.</li>' +
      '<li><strong>Stress:</strong> the opt-in design’s effects shrink by about two thirds in the Stress environment.</li>' +
      '<li><strong>Financing:</strong> 46 of 48 financed poverty and wealth curves are fragile (the opt-in design’s basic-living effect in Reference holds at both horizons), and the opt-in design paid by a contribution on wages raises basket poverty.</li></ul>' + workTable();
    h += '<h3 class="fx-h3">What no figure here covers</h3>' +
      '<p>The seed intervals measure the model’s randomness only. They do not cover the choice of main row or full backing (a design statement); the readings the screen held fixed; Stress, which was not screened; or the engine’s structure: a fixed population in the main row (no ageing, births or deaths; added Nov 17, 2026), one price rule for the whole economy, no central bank, no migration, no value of care, community work or new ventures, PTFs modelled from the Hub’s statements and measured costs, and 500 adults (a 10,000-adult pair agrees on hours and the top of the wealth distribution). The financed rows leave out the weighted top tail. The model has not been reviewed by an independent economist.</p>' +
      F.weightNote() + '<p class="fx-note">Where each figure comes from (basis class: simulation release and command): engine <code>104691f</code>, v5.9 batch of runs, seeds 1-500, run on GitHub Actions Nov 14-15, 2026, as frozen in the preregistration <code>prereg/2026-11-s63-round2-freeze.md</code> (registered on OSF: <a href="https://osf.io/msdzk/overview">osf.io/msdzk</a>). Results: <code>r2-&lt;part&gt;-&lt;env&gt;-&lt;years&gt;-104691f</code> in compassionism-sim-results; tables <code>r2-tables-104691f</code>; erosion trace <code>r2-erosion-104691f</code>. Commands: <code>dev/tools/s64_tables.py</code>, <code>dev/tools/s64_erosion.js</code>, <code>dev/tools/s64_charts.py</code>, <code>dev/tools/r2_study_files.py</code>. Every row is also in “Every preregistered study” below.</p>';
    return h;
  }
  function mount(host) {
    Promise.all(FILES.map(function (f) { return F.fetchJSON('data/studies/' + f + '.json').then(function (d) { D[f] = d; }); }).concat([F.loadWeights()]))
      .then(function () { host.innerHTML = build(); })
      .catch(function (e) { host.innerHTML = '<p class="fx-banner">Could not load the v5.9 data (' + esc(e.message) + ').</p>'; });
  }
  root.CSS_R2 = {mount: mount};
})(window);
