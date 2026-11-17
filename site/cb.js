/* Release 2 with the central-bank switch (S76). Two mounts:
 *   CSS_CB.lead(host)      the simulation page's opening section: v5.9's main row (full backing), C2.2 or the release design, three environments,
 *                          with the central bank off (release 2 as frozen, 500 seeds: data/studies/r2-effects.json) or on (the policy-rate rule, S74's
 *                          corrected 100-seed rerun: data/studies/s74-cb.json), and what turning it on changes on the same 100 seeds.
 *   CSS_CB.section(host)   the findings page's central-bank section: every outcome of S74, both designs, four environments, each arm, with intervals.
 * Every number is read from those files when the page loads and printed with its row and column (class "snum", data-study, data-src); none is typed
 * here. Needs site/findings.js (window.CSF). */
(function (root) {
  'use strict';
  var F = root.CSF; if (!F) return;
  var esc = F.esc, D = {}, C = 'C2.2', RL = 'release design';
  var O = {bl: 'basic living (adult-years below 30 days, points)', bk: 'cost of living (basket poverty, adult-years, points)', kid: 'children below the cost of living (child-years, points)',
           wp: 'wealth poverty, yearly average (points)', mw: 'median real wealth (year-0 $)', inf: 'programme inflation (points a year)',
           p5: 'pushed below the basket line in a recession year (%)', p3: 'largest fall in real wealth (year-0 $, median adult)', p1: 'spread of the basket price level\'s yearly change (points)',
           t1: 'top 1% share of net worth at the end (%)', b50: 'bottom half\'s share of net worth at the end (%)', fs: 'adult-years with a forced sale (%)'};
  /* how each outcome counts the simulated adults (S83): poverty shares once per simulated adult; wealth, distribution and stability measures by population weight */
  var WT = {bl: 'unweighted', bk: 'unweighted', kid: 'unweighted', wp: 'unweighted', mw: 'weighted', inf: 'unweighted', p5: 'weighted', p3: 'weighted', p1: 'unweighted',
            t1: 'weighted', b50: 'weighted', fs: 'weighted'};
  var WTN = {unweighted: 'Counted per simulated adult (unweighted).', weighted: 'Counted by population weight (weighted).'};
  var RULE = 'the policy-rate rule', NONE = 'no central bank', ACT = 'the actual rate path';
  var S75 = 'https://bettertobest.github.io/research-hub/us-policy-eras.html';

  function tab(file, sub) { var d = D[file]; return sub ? d[sub] : d; }
  function find(file, flt, col, sub) {
    var d = tab(file, sub), ci = d.columns.indexOf(col), n = d.data[0].length, hit = -1;
    if (ci < 0) throw new Error(file + ' has no column ' + col);
    for (var i = 0; i < n; i++) { var ok = true; for (var k in flt) if (d.data[d.columns.indexOf(k)][i] !== flt[k]) { ok = false; break; } if (ok) { if (hit >= 0) throw new Error('two rows in ' + file + ' for ' + JSON.stringify(flt)); hit = i; } }
    if (hit < 0) return null;
    return {i: hit, v: d.data[ci][hit]};
  }
  function fmt(v, kind) {
    var a = Math.abs(v), dg = kind === 'pp2' ? 2 : 1;
    if (kind === 'usd') return (v < 0 ? '−$' : '$') + Math.round(a).toLocaleString('en-US');
    if (kind === 'sgusd') return (v < 0 ? '−$' : '+$') + Math.round(a).toLocaleString('en-US');
    var t = a.toLocaleString('en-US', {minimumFractionDigits: dg, maximumFractionDigits: dg});
    if (kind === 'sg2' && a < 0.005) return 'less than 0.01';
    if (kind === 'sg' || kind === 'sg2') return (v < 0 ? '−' : '+') + (kind === 'sg2' ? a.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2}) : t);
    if (kind === 'pc') return (v < 0 ? '−' : '') + t + '%';
    return (v < 0 ? '−' : '') + t;
  }
  /* a printed value with its source; sub 'cb' reads the central bank's own-effect table */
  function show(file, flt, col, kind, sub) {
    var r = find(file, flt, col, sub); if (!r || r.v === null) return '<span class="fx-na">not reported</span>';
    return '<span class="snum" data-study="' + file + (sub ? '.' + sub : '') + '" data-src="row ' + r.i + ' ' + esc(col) + '">' + esc(fmt(r.v, kind)) + '</span>';
  }
  function ci(file, flt, kind, sub) { return show(file, flt, 'lo95', kind, sub) + ' to ' + show(file, flt, 'hi95', kind, sub); }
  function val(file, flt, col, sub) { var r = find(file, flt, col, sub); return r ? r.v : null; }
  function seg(label, opts, cur, on) { return F.seg(label, opts, cur, on); }
  function load(files) { return Promise.all(files.filter(function (f) { return !D[f]; }).map(function (f) { return F.fetchJSON('data/studies/' + f + '.json').then(function (d) { D[f] = d; }); })); }
  function basis(cbOn) {
    var m = D['s74-cb'].meta, r = D['r2-effects'].meta;
    return '<p class="fx-note"><strong>Where these figures come from</strong> (simulation release and command). Central bank off: v5.9 as frozen, engine <code>' + esc(r.engine) + '</code>, seeds 1-' + esc(String(r.seeds)) +
      ', results <code>r2-m-&lt;env&gt;-20-' + esc(r.engine) + '</code> (file <code>data/studies/r2-effects.json</code>). Central bank on: the central-bank study’s rerun with the release’s settings, engine <code>' + esc(m.engine) + '</code>, seeds 1-' + esc(String(m.seeds)) +
      ', results <code>' + esc(m.resultsFolder) + '</code> (file <code>data/studies/s74-cb.json</code>; <code>' + esc(m.command) + '</code>). Both in BetterToBest/compassionism-sim-results. Intervals cover the model’s randomness only.</p>';
  }

  /* ---- the simulation page's opening section ---- */
  var LS = {design: C, cb: 'off', env: 'Reference'};
  function leadCard(label, key, kind, note) {
    var e = LS.env, on = LS.cb === 'on', des = LS.design, h;
    if (!on) {
      var g = {design: des, environment: e, years: 20, outcome: O[key]};
      h = '<p class="fx-card-v">' + show('r2-effects', g, 'programme', kind === 'usd' ? 'usd' : 'pc') + '</p>' +
        '<p class="fx-card-vs">with Compassionism, against ' + show('r2-effects', g, 'no programme', kind === 'usd' ? 'usd' : 'pc') + ' with no program</p>' +
        '<p class="fx-card-d">Change: ' + show('r2-effects', g, 'effect', kind === 'usd' ? 'sgusd' : 'sg') + (kind === 'usd' ? '' : ' points') + '</p>';
    } else {
      var f = {design: des, environment: e, 'central bank': RULE, outcome: O[key]}, c = {design: des, environment: e, run: 'programme', outcome: O[key]};
      h = '<p class="fx-card-v">' + show('s74-cb', f, 'programme', kind === 'usd' ? 'usd' : 'pc') + '</p>' +
        '<p class="fx-card-vs">with Compassionism, against ' + show('s74-cb', f, 'no programme', kind === 'usd' ? 'usd' : 'pc') + ' with no program</p>' +
        '<p class="fx-card-d">Change: ' + show('s74-cb', f, 'effect', kind === 'usd' ? 'sgusd' : 'sg') + (kind === 'usd' ? '' : ' points') + '</p>' +
        '<p class="fx-card-m">Turning the central bank on moves the program run by ' + show('s74-cb', c, 'change', kind === 'usd' ? 'sgusd' : 'sg2', 'cb') + (kind === 'usd' ? '' : ' points') + ' (same seeds).</p>';
    }
    var worse = (function () { var v = on ? val('s74-cb', {design: des, environment: e, 'central bank': RULE, outcome: O[key]}, 'effect') : val('r2-effects', {design: des, environment: e, years: 20, outcome: O[key]}, 'effect'); return kind === 'usd' ? v < 0 : v > 0; })();
    return '<div class="fx-card' + (worse ? ' fx-worse' : '') + '"><p class="fx-card-k">' + esc(label) + '</p>' + h + (note ? '<p class="fx-card-m">' + note + '</p>' : '') +
      '<p class="fx-card-m">' + esc(WTN[WT[key]]) + (on ? ' Central bank on: ' + '<span class="snum" data-study="s74-cb" data-src="meta seeds">' + esc(String(D['s74-cb'].meta.seeds)) + '</span> paired runs.' : '') + '</p></div>';
  }
  function leadBody() {
    var on = LS.cb === 'on', des = LS.design, e = LS.env;
    var p5 = {design: des, environment: e, 'central bank': RULE, outcome: O.p5};
    var h = '<div class="fx-cards fx-c4">' +
      leadCard('Below 30 days of basic living', 'bl', 'pt', 'Share of adult-years whose savings, pay and support would cover fewer than 30 days of basic living.') +
      leadCard('Below the cost of living', 'bk', 'pt', 'Share of adult-years whose household income falls short of the cost of a basket of essentials.') +
      leadCard('Too little wealth (yearly average)', 'wp', 'pt', 'Share of adults whose net wealth is below six months of their own cost of living, averaged over the years.') +
      leadCard('Median real wealth at year 20', 'mw', 'usd', 'In today’s dollars. Rests on full backing (corrected Nov 17, 2026: it said today’s price rule, which full backing barely tests).') + '</div>';
    var inf = on ? show('s74-cb', {design: des, environment: e, 'central bank': RULE, outcome: O.inf}, 'effect', 'sg2') : show('r2-effects', {design: des, environment: e, years: 20, outcome: O.inf}, 'effect', 'sg2');
    h += '<p class="fx-static-note">' + esc(e) + ' environment, 20 years, ' + (des === C ? 'the full-coverage design' : 'the opt-in design') + ', v5.9’s main row. Averages over ' +
      (on ? '<span class="snum" data-study="s74-cb" data-src="meta seeds">' + esc(String(D['s74-cb'].meta.seeds)) + '</span>' : '<span class="snum" data-study="r2-effects" data-src="meta seeds">' + esc(String(D['r2-effects'].meta.seeds)) + '</span>') +
      ' paired runs of 500 simulated adults and their children. The program’s own inflation: ' + inf + ' points a year above no program.' +
      (on && e !== 'Reference' ? ' In a recession year, ' + show('s74-cb', p5, 'no programme', 'pc') + ' of households are pushed below the basket line with no program and ' + show('s74-cb', p5, 'programme', 'pc') + ' with it.' : '') + '</p>';
    return h;
  }
  function leadRender(host) {
    var sw = host.querySelector('#r2l-sw'), body = host.querySelector('#r2l-body');
    sw.innerHTML = '';
    sw.appendChild(seg('Design', [[C, 'Full coverage (everyone)'], [RL, 'Opt-in design']], LS.design, function (v) { LS.design = v; leadRender(host); }));
    sw.appendChild(seg('Central bank', [['off', 'Off'], ['on', 'On']], LS.cb, function (v) { LS.cb = v; leadRender(host); }));
    sw.appendChild(seg('Environment', [['Reference', 'Reference'], ['Adverse', 'Adverse'], ['Stress', 'Stress']], LS.env, function (v) { LS.env = v; leadRender(host); }));
    body.innerHTML = leadBody();
    host.querySelector('#r2l-cbnote').hidden = LS.cb !== 'on';
    try { var u = new URL(location.href); u.searchParams.set('r2', [LS.design === C ? 'c22' : 'rel', LS.cb, LS.env.slice(0, 3).toLowerCase()].join('.')); history.replaceState(null, '', u); } catch (e) { /* file:// or old browser */ }
  }
  function lead(host) {
    try { var q = new URL(location.href).searchParams.get('r2'); if (q) { var p = q.split('.'); if (p[0] === 'rel') LS.design = RL; if (p[1] === 'on') LS.cb = 'on'; var en = {ref: 'Reference', adv: 'Adverse', str: 'Stress'}[p[2]]; if (en) LS.env = en; } } catch (e) { /* ignore */ }
    var body = host.querySelector('#r2l-body');
    return load(['r2-effects', 's74-cb']).then(function () { leadRender(host); host.querySelector('#r2l-basis').innerHTML = basis(); })
      .catch(function (e) { body.innerHTML = '<p class="fx-banner">v5.9’s data could not be loaded (' + esc(e.message) + '). The figures are on the <a href="findings.html#round2">findings page</a>.</p>'; });
  }

  /* ---- the findings page's central-bank section ---- */
  var SS = {design: C, env: 'Adverse'};
  var ROWS = [['bl', 'Below 30 days of basic living (points)', 'sg'], ['bk', 'Below the cost of living (points)', 'sg'], ['kid', 'Children below the cost of living (points)', 'sg'],
              ['wp', 'Too little wealth, yearly average (points)', 'sg'], ['mw', 'Median real wealth at the end', 'sgusd'], ['inf', 'Programme inflation (points a year)', 'sg2'],
              ['p5', 'Pushed below the basket line in a recession year (points)', 'sg'], ['p3', 'Largest fall in real wealth, median adult', 'sgusd'],
              ['p1', 'Spread of the basket price level’s yearly change (points)', 'sg2'], ['t1', 'Top 1% share of net worth at the end (points)', 'sg2'],
              ['b50', 'Bottom half’s share of net worth at the end (points)', 'sg2'], ['fs', 'Adult-years with a forced sale (points)', 'sg2']];
  function effTable() {
    var des = SS.design, e = SS.env, arms = e.indexOf('History') === 0 ? [NONE, ACT, RULE] : [NONE, RULE];
    var head = '<tr><th scope="col">Outcome</th>' + arms.map(function (a) { return '<th scope="col">Programme’s effect, ' + esc(a) + ' (95%)</th>'; }).join('') + '<th scope="col">The rule’s own effect, no programme</th><th scope="col">The rule’s own effect, programme</th></tr>';
    var body = ROWS.map(function (r) {
      var cells = arms.map(function (a) { var f = {design: des, environment: e, 'central bank': a, outcome: O[r[0]]}; if (!find('s74-cb', f, 'effect')) return '<td>—</td>'; return '<td>' + show('s74-cb', f, 'effect', r[2]) + '<br><span class="fx-ci">' + ci('s74-cb', f, r[2]) + '</span></td>'; }).join('');
      var cc = ['no programme', 'programme'].map(function (run) { var f = {design: des, environment: e, run: run, outcome: O[r[0]]}; if (!find('s74-cb', f, 'change', 'cb')) return '<td>—</td>'; return '<td>' + show('s74-cb', f, 'change', r[2], 'cb') + '<br><span class="fx-ci">' + ci('s74-cb', f, r[2], 'cb') + '</span></td>'; }).join('');
      return '<tr><th scope="row">' + esc(r[1] === 'C2.2' ? 'Full-coverage design' : r[1] === 'release design' ? 'Opt-in design' : r[1]) + ' <span class="fx-ci">(' + esc(WT[r[0]]) + ')</span></th>' + cells + cc + '</tr>';
    }).join('');
    return '<div class="fx-tw" tabindex="0" role="region" aria-label="Central bank table"><table class="fx-table"><caption>' + esc(des === C ? 'Full-coverage design' : 'Opt-in design') + ', ' + esc(e) + ': the programme’s effect with no central bank and with the rule, and the rule’s own effect (with the rule minus without it) in each run. Means over the same ' + esc(String(D['s74-cb'].meta.seeds)) + ' paired seeds (not the 500 of v5.9’s main row).</caption><thead>' + head + '</thead><tbody>' + body + '</tbody></table></div>';
  }
  function sectionRender(host) {
    var sw = host.querySelector('#cb-sw'); sw.innerHTML = '';
    sw.appendChild(seg('Design', [[C, 'Full coverage'], [RL, 'Opt-in design']], SS.design, function (v) { SS.design = v; sectionRender(host); }));
    sw.appendChild(seg('Environment', [['History 2005-2025', 'History 2005-2025'], ['Adverse', 'Adverse'], ['Stress', 'Stress'], ['Reference', 'Reference']], SS.env, function (v) { SS.env = v; sectionRender(host); }));
    host.querySelector('#cb-table').innerHTML = effTable();
  }
  function section(host) {
    return load(['r2-effects', 's74-cb']).then(function () {
      host.querySelector('#cb-words').innerHTML = sectionWords();
      sectionRender(host); host.querySelector('#cb-basis').innerHTML = basis(true);
    }).catch(function (e) { host.querySelector('#cb-table').innerHTML = '<p class="fx-banner">The central-bank study’s data could not be loaded (' + esc(e.message) + ').</p>'; });
  }
  /* the plain-words summary: each sentence's numbers from the file */
  function sectionWords() {
    function p5(des, e, col) { return show('s74-cb', {design: des, environment: e, 'central bank': RULE, outcome: O.p5}, col, 'pc'); }
    function cbn(e, k, kind) { return show('s74-cb', {design: C, environment: e, run: 'no programme', outcome: O[k]}, 'change', kind, 'cb'); }
    function cbp(e, k, kind) { return show('s74-cb', {design: C, environment: e, run: 'programme', outcome: O[k]}, 'change', kind, 'cb'); }
    function eff(des, e, k, kind) { return show('s74-cb', {design: des, environment: e, 'central bank': RULE, outcome: O[k]}, 'effect', kind); }
    var H = 'History 2005-2025';
    return '<p class="fx-static-note">Every figure in this section is a mean over <span class="snum" data-study="s74-cb" data-src="meta seeds">' + esc(String(D['s74-cb'].meta.seeds)) + '</span> paired runs (seeds 1-' + esc(String(D['s74-cb'].meta.seeds)) + '), not the 500 of v5.9’s main row; the intervals measure the model’s randomness over those runs.</p><ul>' +
      '<li><strong>Steadier at the bottom.</strong> With the central bank on, a recession year pushes ' + p5(C, 'Adverse', 'no programme') + ' of households below the basket line with no programme, ' + p5(C, 'Adverse', 'programme') + ' with the full-coverage design and ' + p5(RL, 'Adverse', 'programme') + ' with the opt-in design (Adverse). With the full-coverage design the median adult’s largest fall in real wealth changes by ' + eff(C, 'Adverse', 'p3', 'sgusd') + ' against no programme.</li>' +
      '<li><strong>Less steady in prices.</strong> Both designs widen the year-to-year spread of the basket’s price level (full-coverage design: ' + eff(C, 'Adverse', 'p1', 'sg2') + ' points in Adverse; ' + eff(C, H, 'p1', 'sg2') + ' in History). In Reference, Adverse and Stress outside inflation is fixed, so the programme’s own price changes are the larger source of price swings there.</li>' +
      '<li><strong>The damping claim is not supported.</strong> The design says its share of essentials should damp what the central bank and outside shocks do to the cost of basic living. In this engine the rule moves rates, asset prices and job loss, not the price of essentials, so it cannot show that damping, for either design. That is a limit of the model, not evidence about the world.</li>' +
      '<li><strong>The rule moves wealth up the ladder; the programme shrinks that.</strong> Over 2005-2025 with no programme, the rule changes the top 1%’s share of net worth by ' + cbn(H, 't1', 'sg2') + ' points and the bottom half’s by ' + cbn(H, 'b50', 'sg2') + '; with the full-coverage design on, by ' + cbp(H, 't1', 'sg2') + ' and ' + cbp(H, 'b50', 'sg2') + '.</li>' +
      '<li><strong>Forced sales.</strong> With the rule and no programme, ' + show('s74-cb', {design: C, environment: H, 'central bank': RULE, outcome: O.fs}, 'no programme', 'pc') + ' of adult-years in History involve a forced sale of real assets by a household past its borrowing limit, bought by households with cash; with the full-coverage design, ' + show('s74-cb', {design: C, environment: H, 'central bank': RULE, outcome: O.fs}, 'programme', 'pc') + '.</li>' +
      '<li><strong>The poverty results barely move.</strong> Turning the rule on changes the full-coverage design’s basket poverty by ' + cbp(H, 'bk', 'sg2') + ' points in History and ' + cbp('Adverse', 'bk', 'sg2') + ' in Adverse; under full backing the programme’s own inflation is near zero, so the rule rarely responds to it.</li></ul>';
  }
  root.CSS_CB = {lead: lead, section: section};
  /* the simulation page mounts its opening section itself (its inline script is shared with earlier-engine.html and is not changed) */
  function auto() { var h = document.getElementById('release2'); if (h && h.querySelector('#r2l-body')) lead(h); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', auto); else auto();
})(window);
