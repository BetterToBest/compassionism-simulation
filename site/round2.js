/* Release 2 on the findings page (S65): round 2 of the engine, beside release 1. Every number is read from data/studies/r2-*.json when the page loads and printed
 * with its path (class "snum"); no figure is typed here. The words follow dev/reports/s64-findings-page-text.md, which follows the preregistered rules of
 * prereg/2026-11-s63-round2-freeze.md (a range across the preregistered readings before the main row's figure; every wealth figure names the price rule and has
 * its erosion share; every inflation figure has the backing statement beside it; the financed rows are never led with). Needs site/findings.js (window.CSF). */
(function (root) {
  'use strict';
  var F = root.CSF, esc = F.esc;
  var FILES = ['r2-effects', 'r2-curves', 'r2-backing', 'r2-financed', 'r2-distribution', 'r2-work', 's82-supply', 's82-breakeven', 's85-automation', 's85-backing', 's85-free-time', 's94-fund', 's94-charters', 's94-interaction', 's94-levels'];  /* S82 (Nov 18, 2026): the v6 readings below full backing; S85 (Nov 20): automation */
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
  /* S85 part 5 (Nov 20, 2026; research-update prereg/2026-11-s85-output-per-hour.md, Amendments 1-4): automation in both runs, at full backing, and the
   * backing the programme's own work produces. Words follow dev/reports/s85-output-per-hour.md section 14; every figure is read from
   * data/studies/s85-automation.json, s85-backing.json and s85-free-time.json (dev/tools/s85_page_data.py). Ranges are the lowest and highest row of a
   * named set; counts are counted from the files' category column. */
  var RC = {};
  function recs(file) {
    if (!RC[file]) { var d = D[file], n = d.data[0].length, out = []; for (var i = 0; i < n; i++) { var o = {_i: i}; d.columns.forEach(function (c, j) { o[c] = d.data[j][i]; }); out.push(o); } RC[file] = out; }
    return RC[file];
  }
  function where(file, pred) { return recs(file).filter(pred); }
  function span(file, rows, col, fmt) {
    if (!rows.length) throw new Error('no rows in ' + file + ' for a range of ' + col);
    var lo = rows.reduce(function (a, b) { return b[col] < a[col] ? b : a; }), hi = rows.reduce(function (a, b) { return b[col] > a[col] ? b : a; });
    if (fmt(lo[col]) === fmt(hi[col])) return snum(file, lo._i, col, fmt(lo[col]));
    return snum(file, lo._i, col, fmt(lo[col])) + ' to ' + snum(file, hi._i, col, fmt(hi[col]));
  }
  function pc0(x) { return fmtN(x, 0) + '%'; }
  function pt0(x) { return fmtN(x, 0); }
  function s85Section() {
    var SA = 's85-automation', SK = 's85-backing', ST = 's85-free-time', m = D[SA].meta;
    var BK = 'basket poverty (points)', SV = 'savings under three months of need (points)', WY = 'wealth poverty, yearly average (points)';
    var FC = 'full coverage', OI = 'opt-in', LJ = 'lost jobs', SH = 'shorter hours', SHARE = 'offset share (%)', NONE = 'cost, no programme';
    function A(o) { return function (r) { for (var k in o) if (typeof o[k] === 'function' ? !o[k](r[k]) : r[k] !== o[k]) return false; return true; }; }
    function mw(x) { return x.indexOf('median real wealth') === 0; }
    function shareR(flt) { return span(SA, where(SA, A(flt)), SHARE, pc0); }
    function count(flt, cat) { return where(SA, A(Object.assign({category: cat}, flt))).length; }
    function counts(des, yrs) {
      var f = {design: des, years: yrs}, n = where(SA, A(f)).length;
      var said = {'offsets fully': 'offset fully', 'offsets in part': 'offset in part', 'does not offset': 'do not offset', 'worsens': 'worsen'};
      return n + ' tests, ' + ['offsets fully', 'offsets in part', 'does not offset', 'worsens'].map(function (c) { return [count(f, c), said[c]]; })
        .filter(function (p) { return p[0] > 0; }).map(function (p) { return p[0] + ' ' + p[1]; }).join(', ');
    }
    function cells(flt) {  /* the cells of one category, named by environment and displacement level */
      var rs = where(SA, A(flt));
      return ENVS.map(function (e) {
        var es = rs.filter(function (r) { return r.environment === e; });
        return es.length ? e + ' at ' + es.map(function (r) { return snum(SA, r._i, 'displaced (%)', pc0(r['displaced (%)'])); }).join(', ') : null;
      }).filter(Boolean).join('; ');
    }
    function worse(flt) {  /* the worsening cells of one design and outcome, by form; "none" if there are none */
      var t = [LJ, SH].map(function (fm) { var c = cells(Object.assign({form: fm, category: 'worsens'}, flt)); return c ? c + ' (' + fm + ')' : null; }).filter(Boolean);
      return t.length ? t.join('; ') : 'none';
    }
    function free(run) { return span(ST, where(ST, A({run: run, years: 20, form: LJ, 'displaced (%)': 50})), 'insecure share (%)', pc0); }
    function bk(des, yrs, env, rd) { return where(SK, A({design: des, years: yrs, reading: rd || 'main reading', environment: env || function () { return true; }})); }
    var IN = 'programme inflation (points a year)', PS = 'produced share (%)';
    var allE = where(SK, function () { return true; }), above = allE.filter(function (r) { return r['infl lo95'] > 5; }).length;
    var nLJ = where(SA, A({design: OI, years: 20, form: LJ, outcome: BK})).length, wLJ = count({design: OI, years: 20, form: LJ, outcome: BK}, 'worsens');
    function offTable(out, yrs, cap) {
      var rows = [];
      [FC, OI].forEach(function (des) { [LJ, SH].forEach(function (fm) { [10, 30, 50, 70].forEach(function (dp) {
        rows.push([esc((des === FC ? 'Full coverage' : 'Opt-in') + ', ' + fm + ', ' + dp + '%')].concat(ENVS.map(function (e) {
          var f = {environment: e, years: yrs, design: des, form: fm, 'displaced (%)': dp, outcome: out}, r = find(SA, f, SHARE);
          return snum(SA, r.i, SHARE, pc0(r.v)) + ' ' + ci(SA, f, 0) + ', ' + esc(D[SA].data[D[SA].columns.indexOf('category')][r.i]);
        })));
      }); }); });
      return table(cap, ['Design, form, share of paid work displaced by year 20', 'Reference', 'Adverse', 'Stress'], rows);
    }
    function bkTable() {
      var rows = [];
      [FC, OI].forEach(function (des) { ENVS.forEach(function (e) {
        rows.push([esc((des === FC ? 'Full coverage' : 'Opt-in') + ', ' + e), span(SK, bk(des, 20, e), PS, pc0), span(SK, bk(des, 20, e), IN, pt0),
          span(SK, bk(des, 20, e, 'nothing produced (the floor)'), IN, pt0), span(SK, bk(des, 40, e), PS, pc0), span(SK, bk(des, 40, e), IN, pt0),
          where(SK, A({design: des, environment: e, category: 'does not back enough'})).length + ' of ' + where(SK, A({design: des, environment: e})).length]);
      }); });
      return table('The backing the programme’s own work produces (nothing assumed backed; displacement as lost jobs at 0-70%): the main reading’s rows (m 0.25 to 1, low or high automation gain)',
        ['Design, environment', 'Produced share of the payout, 20 years', 'Programme inflation, points a year, 20 years', 'With nothing produced, 20 years', 'Produced share, 40 years', 'Programme inflation, 40 years', 'Rows that do not back enough (every reading, both horizons)'], rows);
    }
    var nf = {design: FC, years: 20, form: LJ, outcome: BK};
    return '<h3 class="fx-h3">Automation: displacement in both runs, and the backing the programme’s own work produces (added Nov 20, 2026)</h3>' +
      '<p>A preregistered study runs automation in both runs of every pair, so the no-programme run faces the same displacement: 10%, 30%, 50% or 70% of today’s paid work gone by year 20, net of new work, as <strong>lost jobs</strong> (the most exposed adults leave paid work first) or as <strong>shorter hours</strong> for everyone. 50% and 70% are stress readings, beyond every forecast the study opened. The automated work is still done: output per hour grows by a sourced forecast, part of the gain reaches pay, and the rest goes to owners by their holdings. Two designs, ' + esc(String(m.seeds)) + ' paired seeds, three environments; figures are for 20 years unless named.</p><ul>' +
      '<li><strong>With no programme</strong>, displacement raises basket poverty (adult-years below one’s own cost of living) by ' + span(SA, where(SA, A({design: FC, years: 20, form: LJ, outcome: BK, environment: 'Reference'})), NONE, function (x) { return fmtN(x, 1); }) + ' points with lost jobs in Reference (' + span(SA, where(SA, A({design: FC, years: 20, form: LJ, outcome: BK, environment: function (e) { return e !== 'Reference'; }})), NONE, function (x) { return fmtN(x, 1); }) + ' in Adverse and Stress), and median real wealth (weighted) falls by ' + span(SA, where(SA, A({design: FC, years: 20, form: LJ, outcome: 'median real wealth, weighted (year-0 $)', environment: 'Reference'})), NONE, dollars) + ' (Reference).</li>' +
      '<li><strong>With every adult taking part and full backing</strong> (the full-coverage design), the programme takes away ' + shareR({design: FC, years: 20, outcome: BK}) + ' of the rise in basket poverty (lost jobs and shorter hours, three environments), ' + shareR({design: FC, years: 20, outcome: WY}) + ' of the rise in wealth poverty, ' + shareR({design: FC, years: 20, outcome: SV}) + ' of the rise in the share of adult-years with under three months of savings, and ' + shareR({design: FC, years: 20, outcome: mw}) + ' of the fall in median real wealth (weighted and unweighted). Of its ' + counts(FC, 20) + ', every one significant. At 50% lost jobs, ' + free(FC) + ' of the hours no longer paid fall in households below their cost of living, against ' + free('no programme') + ' with no programme.</li>' +
      '<li><strong>In the opt-in design</strong> it takes away much less: ' + shareR({design: OI, years: 20, form: LJ, outcome: BK}) + ' of the rise in basket poverty with lost jobs, and ' + shareR({design: OI, years: 20, form: SH, outcome: BK}) + ' with shorter hours. <strong>With lost jobs it often makes the rise in poverty larger:</strong> in ' + wLJ + ' of its ' + nLJ + ' lost-jobs cells the rise in basket poverty is larger with the programme than without it. The cells where it is larger: ' + worse({design: OI, years: 20, outcome: BK}) + '. Where the rise in the share with under three months of savings is larger with the programme: ' + worse({design: OI, years: 20, outcome: SV}) + '. ' + (count({design: FC}, 'worsens') ? 'With full coverage, ' + count({design: FC}, 'worsens') + ' tests worsen.' : 'With full coverage no test worsens, for any reading, in any cell, at either horizon.') + ' Of its ' + counts(OI, 20) + ' (40 years: ' + counts(OI, 40) + '). At 50% lost jobs, ' + free(OI) + ' of the freed hours fall below the cost of living. The opt-in programme still cuts basket poverty against no programme at every level; “larger” means that cut shrinks as displacement grows. A trace of these cells finds that the adults who would take part carry most of the extra rise, as more of them sit just below the line rather than far below it, and that enrolment does not fall (the report gives the figures).</li>' +
      '<li><strong>Full backing is assumed, not produced.</strong> Every figure above assumes that each programme dollar is matched by new output (a design parameter). Counting only what the programme’s own work produces (project hours valued at their pay over the labour share, times m, the share of that work whose output people would otherwise buy, a design parameter; plus the yield of the providers’ reinvested capital), it matches ' + span(SK, bk(FC, 20), PS, pc0) + ' of the payout in the full-coverage design at 20 years (' + span(SK, bk(FC, 40), PS, pc0) + ' at 40) and ' + span(SK, bk(OI, 20), PS, pc0) + ' opt-in (' + span(SK, bk(OI, 40), PS, pc0) + ' at 40). At that backing programme inflation is ' + span(SK, bk(FC, 20), IN, pt0) + ' points a year with full coverage across the three environments (Reference: ' + span(SK, bk(FC, 20, 'Reference'), IN, pt0) + ') and ' + span(SK, bk(OI, 20), IN, pt0) + ' opt-in, at 20 years. In ' + above + ' of the block’s ' + allE.length + ' rows (every reading, design, environment and horizon, m 1 included) the interval of programme inflation lies above 5 points a year: no row backs enough.</li></ul>' +
      offTable(BK, 20, 'The share of displacement’s rise in basket poverty that the programme takes away, 20 years, at full backing (95% interval; category after the multiple-testing correction). Negative: the rise is larger with the programme.') +
      '<details class="fx-more"><summary>The same for savings, wealth poverty and median real wealth, and at 40 years</summary>' +
      offTable(SV, 20, 'Savings under three months of need: the share of displacement’s rise the programme takes away, 20 years, at full backing') +
      offTable(WY, 20, 'Wealth poverty, yearly average: the share of displacement’s rise the programme takes away, 20 years, at full backing') +
      offTable('median real wealth, weighted (year-0 $)', 20, 'Median real wealth (weighted): the share of displacement’s fall the programme takes away, 20 years, at full backing; today’s price rule, barely tested at full backing') +
      offTable(BK, 40, 'Basket poverty: the share of displacement’s rise the programme takes away, 40 years, at full backing') + '</details>' +
      bkTable() +
      '<p class="fx-note">Cost: a run at a displacement level minus the same run with none, positive is harm. Offset share: the cost with no programme minus the cost with it, over the cost with no programme. ' + esc(m.intervals) + '; each category holds after a Holm correction over the 48 tests of its environment, horizon and design. <strong>Wealth figures</strong> are real wealth at year-0 prices under the engine’s price rule; in the headline block that rule is barely tested, because at full backing almost no unmatched money reaches prices. <strong>Inflation figures</strong> are at the produced backing, under the model’s placeholder price rule (all unmatched new money reaches prices), with no central bank and no general equilibrium: they measure the size of the unbacked money, not a forecast of prices. Not modelled: a fall in owners’ spending, investment out of the dividend, pay that differs by wage level in the pass-through, adults under 25 or over 64. Every figure, with the 40-year tables, displaced adults’ own outcomes, the design’s maintained take-home and the readings together: the report <code>' + esc(m.report) + '</code>, the files <code>data/studies/s85-automation.json</code>, <code>s85-backing.json</code> and <code>s85-free-time.json</code> (<code>' + esc(m.command) + '</code>), engine <code>' + esc(m.engine) + '</code>, results <code>' + esc(m.resultsFolder) + '</code> and <code>s85-trace-503fa48</code> in ' + esc(m.resultsRepo) + '; preregistration ' + esc(m.prereg) + '.</p>';
  }
  function s85Unfavourable() {
    var SA = 's85-automation', SK = 's85-backing', f = {design: 'opt-in', years: 20, form: 'lost jobs', outcome: 'basket poverty (points)'};
    var all = where(SA, function (r) { for (var k in f) if (r[k] !== f[k]) return false; return true; });
    var fc = where(SK, function (r) { return r.design === 'full coverage' && r.years === 20 && r.reading === 'main reading'; });
    return '<li><strong>Automation:</strong> in the opt-in design with lost jobs, the rise in basket poverty is larger with the programme than without it in ' + all.filter(function (r) { return r.category === 'worsens'; }).length + ' of ' + all.length + ' cells at 20 years; and the programme’s own work produces ' + span(SK, fc, 'produced share (%)', pc0) + ' of the backing the full-coverage figures assume, at programme inflation of ' + span(SK, fc, 'programme inflation (points a year)', pt0) + ' points a year (automation study, above).</li>';
  }
  /* S94 part 5 (Nov 21, 2026; research-update prereg/2026-11-s94-collectives-lending.md, Amendments 1-2): the Creative Collectives' lending to community
   * businesses, and charters of public utilities. Words follow dev/reports/s94-collectives-lending.md section 10; every figure is read from
   * data/studies/s94-fund.json, s94-charters.json, s94-interaction.json and s94-levels.json (dev/tools/s94_page_data.py). Counts come from the files'
   * category column; ranges are the lowest and highest row of a named set. */
  var S94 = {F: 's94-fund', C: 's94-charters', I: 's94-interaction', L: 's94-levels'};
  var BKO = 'basket poverty (points)', WYO = 'wealth poverty, yearly average (points)', WLO = 'wealth poverty, last year (points)', MWO = 'median real wealth, weighted (year-0 $)',
      MUO = 'median real wealth, unweighted (year-0 $)', SVO = 'savings under three months of need (points)', CSO = 'programme cost per adult a year ($)';
  var S94OUT = [[BKO, 'Basket poverty'], [WYO, 'Wealth poverty, yearly average'], [WLO, 'Wealth poverty, last year'], [MWO, 'Median wealth, weighted'], [MUO, 'Median wealth, unweighted'], [SVO, 'Savings shortfall']];
  function s94A(o) { return function (r) { for (var k in o) if (typeof o[k] === 'function' ? !o[k](r[k]) : r[k] !== o[k]) return false; return true; }; }
  function s94Cells(years) {  /* every environment and design, in the page's order */
    var out = []; ENVS.forEach(function (e) { ['full coverage', 'opt-in'].forEach(function (d) { out.push({environment: e, design: d, years: years}); }); }); return out;
  }
  function s94Helps(cell, reading) {  /* decision rule 3: improves basket poverty or yearly wealth poverty, and worsens none of the six readings */
    var rs = where(S94.F, s94A(Object.assign({reading: reading}, cell))).filter(function (r) { return S94OUT.some(function (o) { return o[0] === r.outcome; }); });
    return rs.some(function (r) { return (r.outcome === BKO || r.outcome === WYO) && r.category === 'improves'; }) && !rs.some(function (r) { return r.category === 'worsens'; });
  }
  function s94Worse(cell, reading, file) {  /* the readings of one cell and reading that worsen, by name */
    return where(file || S94.F, s94A(Object.assign({reading: reading, category: 'worsens'}, cell)));
  }
  function s94Fig(file, cell, reading, outcome, kind, dg) {
    var f = Object.assign({reading: reading, outcome: outcome}, cell);
    return show(file, f, 'change', kind, dg) + ' ' + ci(file, f, dg === undefined ? 1 : dg, kind === 'sgusd');
  }
  function s94Cell(file, cell, reading, outcome, kind, dg) {
    var f = Object.assign({reading: reading, outcome: outcome}, cell), r = find(file, f, 'change'), cat = D[file].data[D[file].columns.indexOf('category')][r.i];
    var t = s94Fig(file, cell, reading, outcome, kind, dg);
    return cat === 'worsens' ? '<strong>' + t + '</strong>' : t;
  }
  function s94Section() {
    var F = S94.F, Ch = S94.C, I = S94.I, L = S94.L, m = D[F].meta, MAIN = 'main reading', CH3 = 'charters at 1/3', CH23 = 'charters at 2/3', CH7 = 'charters at 1/7 (public power today)';
    var SH = function (y) { return "community businesses' share of essential sales, " + y + ' (points)'; };
    var cells20 = s94Cells(20), cells40 = s94Cells(40), all12 = cells20.concat(cells40);
    var readings = []; D[F].data[D[F].columns.indexOf('reading')].forEach(function (x) { if (readings.indexOf(x) < 0) readings.push(x); });
    var helpM = all12.filter(function (c) { return s94Helps(c, MAIN); }).length;
    var helpO = 0, nO = 0; all12.forEach(function (c) { readings.filter(function (x) { return x !== MAIN; }).forEach(function (x) { nO++; if (s94Helps(c, x)) helpO++; }); });
    var worse2 = all12.filter(function (c) { return s94Worse(c, MAIN).length >= 2; }).length;
    /* the five cells at 20 years where the share reaches its ceiling without the fund */
    var ceil = cells20.filter(function (c) { return !(c.environment === 'Stress' && c.design === 'opt-in'); });
    var S5 = {environment: 'Stress', design: 'opt-in', years: 20};
    function lvl(row, out, cell) { return show(L, Object.assign({row: row, outcome: out}, cell), 'value', 'pc', 0); }
    function fnd(out, cell, kind, dg) { return show(F, Object.assign({reading: MAIN, outcome: out}, cell), 'change', kind, dg); }
    function mn(x) { return fmtN(x, 0); }
    var usd0 = function (x) { return '$' + fmtN(x, 0); };
    var costRange = span(F, ceil.reduce(function (a, c) { return a.concat(where(F, s94A(Object.assign({reading: MAIN, outcome: CSO}, c)))); }, []), 'change', usd0);
    var wyRange = span(F, ceil.reduce(function (a, c) { return a.concat(where(F, s94A(Object.assign({reading: MAIN, outcome: WYO}, c)))); }, []), 'change', function (x) { return fmtN(x, 3); });
    var chart23 = function (out, f2) { return span(Ch, cells20.reduce(function (a, c) { return a.concat(where(Ch, s94A(Object.assign({reading: CH23, outcome: out}, c)))); }, []), 'change', f2); };
    var chart7 = where(Ch, s94A({reading: CH7, years: 20, outcome: BKO}));
    var c7moved = chart7.filter(function (r) { return r.category !== 'no change'; });
    var c7s = c7moved.map(function (r) { return r.environment + ', ' + r.design; });
    function chWorse(years) { return where(Ch, s94A({years: years, category: 'worsens'})).filter(function (r) { return r.reading !== 'the fund and charters at 1/7'; }).length; }
    function fundTable(years) {
      var rows = s94Cells(years).map(function (c) {
        return [esc(c.environment + ', ' + c.design),
          show(F, Object.assign({reading: MAIN, outcome: SH('year 5')}, c), 'change', 'sg', 1), s94Cell(F, c, MAIN, CSO, 'sgusd', 0), s94Cell(F, c, MAIN, BKO, 'sg', 3), s94Cell(F, c, MAIN, WYO, 'sg', 3),
          s94Cell(F, c, MAIN, MWO, 'sgusd', 0), s94Cell(F, c, MAIN, SVO, 'sg', 3)];
      });
      return table('The fund, main reading, ' + years + ' years: change against the main row of the same design (95% seed interval; bold: worsens after the multiple-testing correction). Share in points at year 5; cost in dollars per adult a year; poverty and savings in points; median wealth in year-0 dollars.',
        ['Environment, design', 'Share of essential sales, year 5', 'Programme cost', 'Basket poverty', 'Wealth poverty, yearly average', 'Median wealth, weighted', 'Savings shortfall'], rows);
    }
    function readingsTable() {
      var rows = readings.filter(function (x) { return x !== MAIN; }).concat([]).map(function (x) {
        var nW = 0, nI = 0; cells20.forEach(function (c) { nW += s94Worse(c, x).length; nI += where(F, s94A(Object.assign({reading: x, category: 'improves'}, c))).length; });
        var ps = cells20.filter(function (c) { return s94Helps(c, x); }).length;
        return [esc(x), span(F, cells20.reduce(function (a, c) { return a.concat(where(F, s94A(Object.assign({reading: x, outcome: CSO}, c)))); }, []), 'change', mn),
          nI + ' of ' + 6 * cells20.length, nW + ' of ' + 6 * cells20.length, ps + ' of ' + cells20.length];
      });
      return table('The other readings of the fund, 20 years, six cells (three environments, two designs): the added cost, the number of its 36 readings that improve or worsen after the correction, and the cells where the preregistered rule counts it as helping',
        ['Reading of the fund', 'Added programme cost, $ per adult a year (lowest to highest cell)', 'Readings that improve', 'Readings that worsen', 'Cells where it helps'], rows);
    }
    function charterTable(years) {
      var rows = [];
      [CH7, CH3, CH23].forEach(function (rd) {
        var f = {reading: rd, years: years};
        rows.push([esc(rd), span(Ch, where(Ch, s94A(Object.assign({outcome: 'added subsidy from charters, per adult a year ($)'}, f))), 'change', mn),
          span(Ch, where(Ch, s94A(Object.assign({outcome: CSO}, f))), 'change', function (x) { return fmtN(x, 0); }),
          span(Ch, where(Ch, s94A(Object.assign({outcome: BKO}, f))), 'change', function (x) { return fmtN(x, 3); }),
          span(Ch, where(Ch, s94A(Object.assign({outcome: WYO}, f))), 'change', function (x) { return fmtN(x, 3); }),
          span(Ch, where(Ch, s94A(Object.assign({outcome: MWO}, f))), 'change', mn),
          span(Ch, where(Ch, s94A(Object.assign({outcome: SVO}, f))), 'change', function (x) { return fmtN(x, 3); })]);
      });
      return table('Charters of public utilities (no fund), ' + years + ' years: the range of the change against the main row over the six cells (three environments, two designs). Subsidy and cost in dollars per adult a year; poverty and savings in points; median wealth in year-0 dollars.',
        ['Charters', 'Subsidy', 'Programme cost', 'Basket poverty', 'Wealth poverty, yearly average', 'Median wealth, weighted', 'Savings shortfall'], rows);
    }
    function absSpan(file, rows, col, fmt) {  /* the smallest and largest size, ignoring sign, with the rows they come from */
      var lo = rows.reduce(function (x, y) { return Math.abs(y[col]) < Math.abs(x[col]) ? y : x; }), hi = rows.reduce(function (x, y) { return Math.abs(y[col]) > Math.abs(x[col]) ? y : x; });
      return snum(file, hi._i, col, fmt(Math.abs(hi[col])));
    }
    function interactionLine() {
      var n = 0, sig = where(I, function (r) { return r.outcome !== CSO && r['interval excludes zero']; });
      all12.forEach(function (c) { if (where(I, s94A(c)).some(function (r) { return r.outcome !== CSO && r['interval excludes zero']; })) n++; });
      var cst = all12.filter(function (c) { return where(I, s94A(Object.assign({outcome: CSO}, c)))[0]['interval excludes zero']; }).length;
      var bad = sig.filter(function (r) { return r.interaction * (r.outcome.indexOf('median real wealth') === 0 ? -1 : 1) > 0; }).length;
      var good = sig.filter(function (r) { return r.interaction * (r.outcome.indexOf('median real wealth') === 0 ? -1 : 1) < 0; }).length;
      return {n: n, cost: cst, sig: sig.length, bad: bad, good: good,
        share: absSpan(I, where(I, function (r) { return r.outcome.indexOf('(points)') > 0; }), 'interaction', function (x) { return fmtN(x, 3); }),
        usd: absSpan(I, where(I, function (r) { return r.outcome.indexOf('median real wealth') === 0; }), 'interaction', function (x) { return fmtN(x, 0); })};
    }
    var it = interactionLine();
    var main20 = show(L, Object.assign({row: 'the main row against no programme', outcome: BKO}, {environment: 'Reference', design: 'full coverage', years: 20}), 'value', 'sg', 1);
    return '<h3 class="fx-h3">The Creative Collectives’ lending, and charters of public utilities (added Nov 21, 2026)</h3>' +
      '<p>The proposal: the Creative Collectives lend to community businesses that sell essentials, for premises, equipment and set-up costs, where banks will not, and public utilities move to Collective charters. These are Duke’s statements; the Hub’s papers give the Collectives no lending role, so the study adds them to the design and models them as stated. A preregistered study adds a <strong>fund</strong> for the community businesses (grocers, counter-service restaurants, utilities), paced at the rate new establishments open in these sectors, with young firms’ failure rates, 14% of it in grants (the share Pennsylvania’s fresh-food financing gave), and <strong>charters</strong> under which public power’s customers pay the community-business price for electricity. Public power serves one customer in seven (APPA), so a third and two thirds are design parameters, swept. Both run in the full-coverage and the opt-in designs, in the three environments, at 20 and 40 years, on ' + esc(String(m.seeds)) + ' paired seeds. The model has no private firms, so the fund finances community-business capacity only. Each figure is a row minus the main row of the same design; the main row is unchanged.</p>' +
      '<ul>' +
      '<li><strong>The fund helps in no cell.</strong> Under the preregistered rule (it helps where it lowers basket poverty or yearly wealth poverty and worsens none of the six readings), it helps in ' + helpM + ' of ' + all12.length + ' cells (three environments, two designs, 20 and 40 years), and it worsens at least two of the six readings in ' + worse2 + ' of them. Of the eight other readings of the fund (half and double the pace, no pace limit, and others), ' + helpO + ' of ' + nO + ' cells and readings pass. No reading changes the verdict.</li>' +
      '<li><strong>Where the share would reach its ceiling anyway, the fund only brings the gain forward.</strong> In five of the six cells at 20 years (everywhere but Stress with the opt-in design) the community businesses’ share of essential sales reaches the 49% ceiling by year 10 without the fund. The fund raises the share at year 5 and costs ' + costRange + ' per adult a year; yearly wealth poverty rises by ' + wyRange + ' points in these cells.</li>' +
      '<li><strong>Where capital holds the share back (Stress, opt-in)</strong>, the fund lifts the share at year 20 from ' + lvl('the main row, no fund', SH('year 20').replace('(points)', '(%)'), S5) + ' to ' + lvl('the fund, main reading', SH('year 20').replace('(points)', '(%)'), S5) + ', but it makes every reading worse. Changes at 20 years, in dollars per adult a year: programme cost ' + fnd(CSO, S5, 'sgusd', 0) + ' (running-cost subsidy on the extra sales ' + fnd("community businesses' running-cost subsidy, per adult a year ($)", S5, 'sgusd', 0) + ', the fund’s net outlay ' + fnd("the fund's net outlay (outlay less interest), per adult a year ($)", S5, 'usd', 0) + '), the contribution that finances it ' + fnd('the contribution that finances the programme, per adult a year ($)', S5, 'sgusd', 0) + '. Basket poverty changes by ' + fnd(BKO, S5, 'sg', 3) + ' points and weighted median wealth by ' + fnd(MWO, S5, 'sgusd', 0) + '.</li>' +
      '<li><strong>The changes are small beside the programme’s own effect</strong> (for example, ' + main20 + ' points of basket poverty against no programme in Reference with full coverage), but they are on the unfavourable side.</li>' +
      '<li><strong>Charters of public utilities improve basket poverty, yearly wealth poverty and savings wherever they act, and worsen no reading:</strong> at one customer in seven (the share public power serves today) only in ' + c7s.length + ' of the six cells at 20 years' + (c7s.length ? ' (' + esc(c7s.join('; ')) + ')' : '') + ', because elsewhere every zone already has more than that share; at two in three, basket poverty changes by ' + chart23(BKO, function (x) { return fmtN(x, 3); }) + ' points at an added cost of ' + chart23(CSO, usd0) + ' per adult a year (20 years, six cells). Charter rows that worsen a reading: ' + chWorse(20) + ' at 20 years and ' + chWorse(40) + ' at 40.</li>' +
      '<li><strong>The fund and charters together</strong> give the fund’s result: the interaction’s interval excludes zero for at least one reading in ' + it.n + ' of the ' + all12.length + ' cells and for the programme’s cost in ' + it.cost + ', but it is negligible: at most ' + it.share + ' points of any share and $' + it.usd + ' of median wealth. Of the ' + it.sig + ' readings whose interval excludes zero, ' + it.bad + ' are on the unfavourable side, ' + it.good + ' on the favourable side and ' + (it.sig - it.bad - it.good) + ' too small to show at six decimals. No headline joins the two.</li>' +
      '</ul>' + fundTable(20) +
      '<details class="fx-more"><summary>The fund at 40 years, its other readings, and charters</summary>' + fundTable(40) + readingsTable() + charterTable(20) + charterTable(40) + '</details>' +
      '<p class="fx-note">Limits, stated in advance: the model has no private firms, so lending to private start-ups that are not community businesses cannot be represented; transport, health care and child care have no community-business price, so charters of roads, transit, airports and ports change nothing in it; capacity is for the whole population, not by zone; the pace limit is a whole-economy rate, generous to one network; no concessional rate and no recovery on failures were opened as sources, and the loan’s principal is never repaid; charters act on electricity only; the fund’s money is new programme money, matched by full backing as every programme dollar is, and under a limit on supply it would compete for real resources, which is not in this design; and the trace of the cost reads stored totals and does not test a cause by switching each part off. ' + esc(m.intervals) + '. Categories after the multiple-testing correction across the six readings of each row. Dollars are year-0 dollars; poverty and savings are unweighted, median wealth as labelled.</p>';
  }
  function s94Unfavourable() {
    var F = S94.F, MAIN = 'main reading', cells = s94Cells(20).concat(s94Cells(40)), S5 = {environment: 'Stress', design: 'opt-in', years: 20};
    var nw = cells.filter(function (c) { return s94Worse(c, MAIN).length >= 2; }).length;
    return '<li><strong>Lending:</strong> the Creative Collectives’ fund for community businesses helps in no cell and worsens at least two of the six readings in ' + nw + ' of ' + cells.length + ' cells; where capital does hold the share back (Stress, opt-in, 20 years) it changes the programme’s cost by ' + show(F, Object.assign({reading: MAIN, outcome: CSO}, S5), 'change', 'sgusd', 0) + ' per adult a year and basket poverty by ' + show(F, Object.assign({reading: MAIN, outcome: BKO}, S5), 'change', 'sg', 3) + ' points.</li>';
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
    h += s85Section();
    h += s94Section();
    h += '<h3 class="fx-h3">Paid for by a contribution instead (shown, never led with)</h3>' +
      '<p>If the programme is paid for by a contribution, with the rest borrowed, the contribution needed is far larger and the poverty effects are much smaller, and in some cells they reverse. Nearly every financed result is fragile: 46 of the 48 poverty and wealth curves change sign or lose significance at some reading, depending on how the contribution is set up. The two that hold are the opt-in design’s basic-living effect in Reference, at both horizons. These rows were run without the weighted top tail.</p>' + financedTable();
    h += '<h3 class="fx-h3">Who gains</h3>' +
      '<p>The programme lowers the top 1%’s share of wealth, raises the bottom half’s, and sharply reduces the share of families in debt; the opt-in design moves them about half as far. Below the top fifth of starting wealth, slightly higher prices lower what adults owe (a small gain); at the top, where money is lent, they are a loss. Adults outside the labour force stay far more often below the cost of living than adults in it; the Question 6 report and the erosion tables (r2-erosion-104691f/tables.md in the results repository) give the split.</p>' + distTable();
    h += '<h3 class="fx-h3">Unfavourable results, together</h3><ul>' +
      '<li><strong>Prices:</strong> programme inflation is above no programme in every cell: immaterial at the main row, tens of points a year without backing (table above).</li>' +
      '<li><strong>Wages below full backing:</strong> if wages follow half of programme inflation and the rest is never made up, the programme with no backing leaves more people below the cost of living (basket poverty) than no programme does (v6 readings, above).</li>' +
      s85Unfavourable() +
      s94Unfavourable() +
      '<li><strong>Work:</strong> fewer adults work: participation falls (adults who leave work for the programme), with their earnings forgone.</li>' +
      '<li><strong>Mobility:</strong> less movement out of the lowest wealth fifth (“stayed in the lowest wealth fifth”, above).</li>' +
      '<li><strong>Labour’s share</strong> of money income falls, because the programme’s payments are income that is not wages.</li>' +
      '<li><strong>Stress:</strong> the opt-in design’s effects shrink by about two thirds in the Stress environment.</li>' +
      '<li><strong>Financing:</strong> 46 of 48 financed poverty and wealth curves are fragile (the opt-in design’s basic-living effect in Reference holds at both horizons), and the opt-in design paid by a contribution on wages raises basket poverty.</li></ul>' + workTable();
    h += '<h3 class="fx-h3">What no figure here covers</h3>' +
      '<p>The seed intervals measure the model’s randomness only. They do not cover the choice of main row or full backing (a design statement); the readings the screen held fixed; Stress, which was not screened; or the engine’s structure: a fixed population in the main row (no ageing, births or deaths; added Nov 17, 2026), one price rule for the whole economy, no central bank, no migration, no value of care, community work or new ventures, PTFs modelled from the Hub’s statements and measured costs, and 500 adults (a 10,000-adult pair agrees on hours and the top of the wealth distribution). The financed rows leave out the weighted top tail. The model has not been reviewed by an independent economist.</p>' +
      F.weightNote() + '<p class="fx-note">Where each figure comes from (basis class: simulation release and command): engine <code>104691f</code> (the frozen model, first published as v5.8), batch of runs shown as v5.9, seeds 1-500, run on GitHub Actions Nov 14-15, 2026, as frozen in the preregistration <code>prereg/2026-11-s63-round2-freeze.md</code> (registered on OSF: <a href="https://osf.io/msdzk/overview">osf.io/msdzk</a>). Results: <code>r2-&lt;part&gt;-&lt;env&gt;-&lt;years&gt;-104691f</code> in compassionism-sim-results; tables <code>r2-tables-104691f</code>; erosion trace <code>r2-erosion-104691f</code>. Commands: <code>dev/tools/s64_tables.py</code>, <code>dev/tools/s64_erosion.js</code>, <code>dev/tools/s64_charts.py</code>, <code>dev/tools/r2_study_files.py</code>. Every row is also in “Every preregistered study” below.</p>';
    return h;
  }
  function mount(host) {
    Promise.all(FILES.map(function (f) { return F.fetchJSON('data/studies/' + f + '.json').then(function (d) { D[f] = d; }); }).concat([F.loadWeights()]))
      .then(function () { host.innerHTML = build(); })
      .catch(function (e) { host.innerHTML = '<p class="fx-banner">Could not load the v5.9 data (' + esc(e.message) + ').</p>'; });
  }
  root.CSS_R2 = {mount: mount};
})(window);
