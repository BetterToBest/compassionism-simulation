'use strict';
/* ═══════════════════════════════════════════════════════════════════════
 * domtest.js — DOM-behaviour harness for index.html
 * Compassionism Framework Simulation · Better To Best Research Hub
 * Source code: Apache License 2.0 (as of v4.8)
 *
 *   Usage:  npm install            (v4.20: installs jsdom, pinned in package.json; dev-only)
 *           node domtest.js                 # defaults to ./index.html
 *           node domtest.js path/to/index.html
 *
 * WHY THIS EXISTS (new in v4.13)
 * ------------------------------
 * `harness.js` verifies the ENGINE — it transcribes the pure simulation
 * functions and reproduces the seed-42 regression outside a browser. It
 * cannot see anything about the page: classes, handlers, render order,
 * repeated DOM insertions. Every UI change from v4.8 through v4.12 shipped
 * with an explicit "not verified in an actual browser" caveat for exactly
 * that reason.
 *
 * Two real, user-visible defects had been live for eight releases and were
 * found the first time the page was actually run rather than read:
 *   · applyParamsFromURL() stripped .tip-host from every preset button, so
 *     opening the tool through a shared "Copy parameters as URL" link
 *     silently disabled all five preset tooltips for the whole session;
 *   · renderSens() appended its OAT tip box with insertAdjacentHTML(
 *     'afterend', …) — a sibling of the node it then clears — so N runs in
 *     one session left N stacked copies.
 * Neither is visible from reading the source in isolation. Both are now
 * regression-tested below.
 *
 * WHAT THIS DOES AND DOES NOT COVER
 * ---------------------------------
 * Covers: DOM structure and mutation, class/attribute state, event-handler
 * wiring, render-path execution, export payloads, and a full seed-42 run
 * driven through the real page.
 * Does NOT cover: CSS layout, tooltip positioning, responsive behaviour, or
 * Chart.js pixel output (Chart is stubbed — jsdom has no layout engine and
 * no canvas). Those still need a human look at a few zoom levels and widths
 * after deploying. Do not read a green run here as "the UI is verified."
 *
 * The page is loaded with runScripts:'outside-only' and its script evaluated
 * by makeWindow(). v4.20 correction: this said DOMContentLoaded and load had
 * already fired by then, so the page's auto-run never triggered. They had
 * not, and on a fast machine the auto-run raced the checks (see makeWindow).
 * makeWindow() now drops the page's load handler and runs its DOMContentLoaded
 * handler only when a check dispatches that event, so every function is
 * exercised deliberately, at any machine speed.
 *
 * v4.14 additions: regression guards for two mechanics bugs an external audit
 * found in runYear() — the BU-expiry slider collapsing every value 2-6 into
 * one behaviour, and PTF's inflation-damping term reading a static slider
 * instead of actual adoption — plus checks on the new Wealth Floor Diagnostic
 * KPI and its CSV/JSON export. See CONTRIBUTING.md's v4.14 Release Notes.
 *
 * v4.15 additions: four more checks (25 -> 29), all written to FAIL GRACEFULLY rather than
 * throw against a v4.14 page, so they double as demonstrably-real regression guards — run
 * this file against an unmodified v4.14 index.html and the four new ones fail. They cover:
 * PTH's inflation damping being scaled by realised membership (PTH switched on with zero
 * members must be bit-identical to PTH off — pre-v4.15 the flat 0.90 fired anyway), a
 * missing BU-expiry parameter behaving as the default rather than propagating NaN, the
 * Monte Carlo CI multiplier being Student's t rather than a fixed 1.96, and the rendered
 * CI actually using it. See CONTRIBUTING.md's v4.15 Release Notes.
 *
 * v4.16 additions: nine more checks (29 -> 38), again written to fail gracefully against the
 * previous release — run this file against an unmodified v4.15 index.html and all nine fail.
 * Phase 5 (v4.17) checks version labels, export completeness, the four-measure poverty panel,
 * the Adverse Environment preset against harness.js's recession port, and the 55%/θ relabels.
 * Phase 6 (v4.18) checks the extreme-poverty overlay against harness.js (every component, every
 * scenario, year 0), its structural invariants (year 0 = EP_Y0_RATE; voluntary identical in every
 * scenario; SMI reduced only by PTH+SZH), the restyled card, and both exports. v4.18 also repaired
 * three v4.17 checks: the version-label check dispatched DOMContentLoaded on `document`, which never
 * reaches the page's `window` listener, so it compared static markup with META and never ran the
 * fill it was written to guard; and two checks pinned the panel at exactly six rows, which any new
 * measure breaks. Each still checks what it was written for. See CONTRIBUTING.md v4.18.
 * Phase 7 (v4.19) checks the automatic stabilizers: controls and defaults (all off), URL round-trip,
 * inertness when off or unable to fire, an unchanged RNG draw count with every lever on, page/harness
 * agreement on every lever, emergency enrollment only in triggered years, a seed-42 Adverse Environment
 * run with every lever on against harness.js (Your Settings and CCO Only), the Shock Response card and
 * warnings, the in-page study against harness.shockStudy, and both exports. See CONTRIBUTING.md v4.19.
 * Phase 8 (v4.20) checks keyboard and screen-reader access (every slider, the seed field and every
 * On/Off group has an accessible name; every tooltip is focusable or described, and opens on
 * keyboard focus; sliders announce their formatted value and show a focus ring), the shared-link
 * seed readout, the extreme-poverty JSON basis label, harness.unitSuite() run against the PAGE's
 * own functions (including the five that exist only in the page), source parity between the page
 * and harness.js for every function they share, the recalibrated automationRisk sampler (two
 * draws, and agent construction no longer depending on the high-risk share), and the paired
 * non-participant validation check, and that a test window never starts the page's load-time
 * reference run (a race the first CI run exposed; see makeWindow). v4.20 also moved the seed-42 regression once (automationRisk
 * sampler and share; see CONTRIBUTING.md v4.20), so Phase 2 and Phase 4's pinned figures moved.
 * Phase 10 (session 7) checks that replication.html declares META.VERSION everywhere it names the engine version and
 * that index.html links to it (not to the Hub's old address).
 * Phase 11 (session 8; v4.22 adds the design panel; session 11 the second view) checks the front door: one sentence, a question or a
 * statement (also README.md's first line), comparison data for every environment, model and view, the mechanisms-off row beneath every
 * Compassionism row, the source and reproduce command, one caveats box that runs no longer hide, the preset picker, the method links,
 * the view switch, the change per $1,000 on every costed row, and the X-Cents site link.
 * Phase 9 (v4.21) checks the CCO relief under inflation, through the page's own engine functions:
 * with a cost-of-living adjustment the relief is exactly 20% of the basket in every year, without
 * one it is 20% divided by the price index; at 0% inflation it is 20% either way; the page's
 * runYear() and harness.js agree agent by agent under inflation with and without COLA; and the six
 * presets' seed-42 figures, computed from the page's engine, match the fixtures `harness.js validate`
 * asserts (only Adverse Environment and Stress Test moved from v4.20). Each fails against v4.20.
 * Phase 4 (v4.16) reproduces a reproducibility bug the v4.16 audit found: a seed-42 run started
 * while the previous run's attribution ablation, or the validation suite, was still computing
 * drew from the wrong RNG stream (v4.15 gave $545,506 / $555,354 instead of $559,223). It also
 * cross-checks the new opt-in inflation-matched Baseline against harness.js's independent
 * computation of the same scenario (seed 42, Baseline at 0%: median wealth $13,612, poverty
 * 50.8%). Phases 1-3 gain checks on the new toggle's URL round-trip, its disclosure warning and
 * export fields, and the validation suite's new invariants. See CONTRIBUTING.md v4.16.
 * ═══════════════════════════════════════════════════════════════════════ */

const fs = require('fs');
const path = require('path');
let JSDOM;
try { ({ JSDOM } = require('jsdom')); }
catch (e) { console.error('domtest.js needs jsdom:  npm install jsdom'); process.exit(3); }

const FILE = process.argv.slice(2).filter(a => a.indexOf('--') !== 0)[0] || path.join(__dirname, 'index.html');  // v5.1: flags such as --write-counts are not a file
const html = fs.readFileSync(FILE, 'utf8');
/* v5.2 step 8 (decision D): the earlier engine (v4.22, as coded) has its own page, earlier-engine.html, with the same inline script. Phases 1-9 test the earlier
 * engine there; from Phase 10 on the checks run on the main page (FILE). makeWindow(query, {page: 'early' | 'front'}) picks one; otherwise the phase's own. */
const EARLY_FILE = path.join(path.dirname(FILE), 'earlier-engine.html'), htmlEarly = fs.existsSync(EARLY_FILE) ? fs.readFileSync(EARLY_FILE, 'utf8') : html;
let CUR = htmlEarly;

let fails = 0, checks = 0;
function check(name, ok, detail) {
  checks++;
  console.log((ok ? '  PASS  ' : '  FAIL  ') + name + (detail ? '\n           ' + detail : ''));
  if (!ok) fails++;
}

function makeWindow(query, opts) {
  const dom = new JSDOM(opts && opts.page === 'early' ? htmlEarly : opts && opts.page === 'front' ? html : CUR, {
    runScripts: 'outside-only',
    url: 'https://bettertobest.github.io/compassionism-simulation/' + (query || '')
  });
  const w = dom.window;
  // Chart.js is stubbed: this harness tests DOM wiring, not chart pixels.
  if (!(opts && opts.noChart)) w.Chart = function (ctx, cfg) { this.cfg = cfg; this.destroy = function () {}; };  // audit fix: noChart leaves Chart undefined, as when the CDN is blocked
  w.HTMLCanvasElement.prototype.getContext = function () { return {}; };
  const inline = [...w.document.querySelectorAll('script')].filter(s => !s.src && !s.type);
  if (inline.length !== 1) throw new Error('expected exactly 1 inline JS script, found ' + inline.length);
  /* v4.20 fix: jsdom fires the document's own DOMContentLoaded and load events AFTER this eval
   * (readyState is still 'loading' here), so the page's handlers used to run on their own: the
   * DOMContentLoaded handler re-applied the reference preset, and the load handler started the
   * seed-42 reference run 300ms later. Whether that auto-run overwrote a test's results depended
   * on machine speed: on the first CI runner, Phase 7's Adverse Environment run finished inside
   * 300ms and was replaced by the reference run (page $570,661 against harness $262,968). The
   * header comment's premise, "load has already fired", was never true. The page's load handler
   * (the auto-run) is now never registered, and its DOMContentLoaded handler runs only when a
   * check dispatches the event itself (isTrusted false), as Phases 5 and 8 do. */
  const addEL = w.addEventListener.bind(w);
  w.addEventListener = function (type, fn, opts) {
    if (type === 'load') return;
    if (type === 'DOMContentLoaded') return addEL(type, function (e) { if (!e.isTrusted) return fn.call(this, e); }, opts);
    return addEL(type, fn, opts);
  };
  w.eval(inline[0].textContent);
  w.addEventListener = addEL;
  return w;
}

/* ── Phase 1: synchronous DOM-behaviour checks ─────────────────────────── */
console.log('=== domtest.js — ' + FILE + ' (Phases 1-9 on ' + (htmlEarly === html ? FILE : EARLY_FILE) + ') ===\n--- Phase 1: DOM behaviour ---');
const w1 = makeWindow('?bu=900&part=55&ptfOn=1&seed=42&baseInflMatchOn=1');
const $1 = id => w1.document.getElementById(id);

w1.applyPreset('reference');
const tipBoxes = () => w1.document.querySelectorAll('#sens-oat-tip').length +
  [...w1.document.querySelectorAll('#sec-sens > div')].filter(d => /^💡/.test(d.textContent.trim()) && d.id !== 'sens-oat-tip').length;
w1.renderSens(); const t1 = tipBoxes();
w1.renderSens(); w1.renderSens(); const t3 = tipBoxes();
check('renderSens() is idempotent — no duplicate OAT tip box across runs',
  t1 === 1 && t3 === 1, 'after 1 call: ' + t1 + '; after 3 calls: ' + t3 + '  (pre-v4.13: 1 then 3)');

w1.applyPreset('reference');
const before = [...w1.document.querySelectorAll('.preset-grid .pbtn')].map(b => b.className);
w1.applyParamsFromURL();
const after = [...w1.document.querySelectorAll('.preset-grid .pbtn')].map(b => b.className);
check('applyParamsFromURL() preserves .tip-host on every preset button',
  after.every(c => c.split(/\s+/).indexOf('tip-host') >= 0),
  'before: "' + before[0] + '"   after: "' + after[0] + '"  (pre-v4.13: "pbtn")');
check('applyParamsFromURL() applied the query string',
  $1('s-bu').value === '900' && $1('s-part').value === '55' && $1('s-seed').value === '42',
  'bu=' + $1('s-bu').value + ' part=' + $1('s-part').value + ' seed=' + $1('s-seed').value);
check('v4.16: the Match-Baseline-inflation toggle round-trips through a shared URL',
  w1.ST.baseInflMatch === true && !!$1('baseInflMatch-on') && $1('baseInflMatch-on').getAttribute('aria-pressed') === 'true',
  'ST.baseInflMatch=' + w1.ST.baseInflMatch + '  (pre-v4.16: no such toggle)');
w1.tog('baseInflMatch', false);

w1.tog('phi', true);
check('toggle buttons expose aria-pressed (a11y)',
  $1('phi-on').getAttribute('aria-pressed') === 'true' && $1('phi-off').getAttribute('aria-pressed') === 'false');
check('the ptfCap pair is initialised too (no preset sets it)',
  $1('ptfCap-off').getAttribute('aria-pressed') === 'true' || $1('ptfCap-on').getAttribute('aria-pressed') === 'false');

// structuralStability must not be a degenerate constant on short runs
const inc = n => Array.from({ length: n }, (_, i) => 100 + i * 10);
const s5 = w1.structuralStability(inc(5), inc(5));
check('structuralStability() computes a real value on a 5-year run',
  Math.abs(s5 - 0.99) > 1e-9, 'value=' + s5.toFixed(6) + '  (pre-v4.13: exactly 0.990000 for any 5-7yr run)');
let identical = true;
for (let L = 8; L <= 30; L++) {
  const A = inc(L).map((v, i) => v * Math.pow(1.1, i)), B = inc(L);
  const q1 = Math.max(1, Math.floor(L / 4)), q2 = Math.max(2, Math.floor(L / 4));
  if (q1 !== q2) identical = false;
}
check('the short-run window fix cannot affect runs of 8+ years', identical);

/* ── Phase 2: a full run driven through the real page ──────────────────── */
console.log('\n--- Phase 2: seed-42 / Full Integration / 20yr through the live page ---');
const w2 = makeWindow();
const $2 = id => w2.document.getElementById(id);
const captured = {};
w2.Blob = function (parts) { this.parts = parts; };
w2.URL.createObjectURL = function (b) { captured.last = b.parts.join(''); return 'blob:stub'; };
w2.URL.revokeObjectURL = function () {};
w2.HTMLAnchorElement.prototype.click = function () { captured[this.download] = captured.last; };

w2.applyPreset('reference');
$2('s-seed').value = '42';
w2.runSim();

const t0 = Date.now();
const iv = setInterval(() => {
  if (Date.now() - t0 > 300000) { clearInterval(iv); console.log('  TIMEOUT'); process.exit(2); }
  if (!w2.SIM_RESULTS || w2.running) return;
  clearInterval(iv);
  const r = w2.SIM_RESULTS;
  const got = { blei: Math.round(r.blei.med), wealth: Math.round(r.finalWealth), gini: +r.finalGini.toFixed(3), pov: +r.finalPov.toFixed(1), bpov: +r.bleiPovPct.toFixed(1) };
  const want = { blei: 1975, wealth: 570661, gini: 0.518, pov: 15.8, bpov: 13.2 };  // v4.20 (v4.19: 1965, 559223, 0.534, 16.6, 13.6)
  check('seed-42 regression reproduces exactly through the live page',
    JSON.stringify(got) === JSON.stringify(want), 'got ' + JSON.stringify(got) + '\n           want ' + JSON.stringify(want));

  check('threshold-sensitivity callouts carry a dominance line (both charts)',
    /Dominance check/.test($2('thresh-wealth-callout').textContent) && /Dominance check/.test($2('thresh-blei-callout').textContent));
  w2.setThreshView('gap');
  check('the gap view redraws without throwing and keeps the dominance line',
    /Dominance check/.test($2('thresh-wealth-callout').textContent));
  w2.setThreshView('headcount');

  const e = r.exposure;
  check('Cumulative Poverty Exposure computed and bounded by run length',
    !!e && e.years === 20 && e.pyWealthMain >= 0 && e.pyWealthMain <= 20 && e.pyBleiBase <= 20,
    e ? 'wealth ' + e.pyWealthMain.toFixed(2) + 'yr (baseline ' + e.pyWealthBase.toFixed(2) + ') · BLEI ' +
        e.pyBleiMain.toFixed(2) + 'yr (baseline ' + e.pyBleiBase.toFixed(2) + ')' : 'missing');
  check('exposure exceeds the final-year rate it complements (a run has history)',
    !!e && e.pyWealthMain > r.finalPov / 100, 'final-year wealth poverty ' + r.finalPov + '% vs ' + (e ? e.pyWealthMain.toFixed(2) : '?') + ' mean years poor');
  check('dominance result attached to the run snapshot', !!r.thresholdDominance);

  const fd = r.floorDiagnostic;
  check('Wealth Floor Diagnostic computed and bounded to [0,1]',
    !!fd && fd.main >= 0 && fd.main <= 1 && fd.base >= 0 && fd.base <= 1 && fd.floor === -10000,
    fd ? 'main=' + (fd.main * 100).toFixed(1) + '% base=' + (fd.base * 100).toFixed(1) + '%' : 'missing');
  check('Baseline is pinned at the floor at least as much as Your Settings (no cost-reduction mechanism to keep it off the floor)',
    !!fd && fd.base >= fd.main, fd ? fd.base + ' vs ' + fd.main : '');

  // Regression guard for the v4.14 BU-expiry fix: expiry=3 and expiry=6 must no longer
  // collapse to the same value (the exact bug this release fixed).
  const pBase = { bu: 1200, maxOct: 6, tax: 0.12, maxMult: 9, nAgents: 200, partRate: 0.78, years: 10,
    ptfShare: 0, pthUptake: 0, szhCoh: 0, cipDemo: 0, phi: true, ptf: false, pth: false, szh: false,
    cip: false, shock: false, automation: false, inflRate: 0, ccoOn: true };
  function runIsolated(expiry, seed) {
    const mainRNG = w2.RNG; w2.RNG = w2.mulberry32(seed + 700003);
    const latentPop = w2.makeLatentPopulation(pBase.nAgents);
    w2.RNG = w2.mulberry32(seed);
    const p = Object.assign({}, pBase, { expiry: expiry, bu: pBase.bu });
    const agents = latentPop.map(lat => w2.instantiateAgent(lat, p));
    for (let yr = 0; yr < p.years; yr++) w2.runYear(agents, yr, p, { active: false, incomeMultiplier: 1.0, yearsLeft: 0 });
    w2.RNG = mainRNG;
    return Math.round(w2.calcMetrics(agents, p.ccoOn, p.pth).med);
  }
  const w3 = runIsolated(3, 7), w6 = runIsolated(6, 7), w1 = runIsolated(1, 7);
  check('BU expiry: slider values 3 and 6 no longer collapse to the same behaviour',
    w3 !== w6, 'expiry=3 → $' + w3 + '   expiry=6 → $' + w6);
  check('BU expiry: the shipped default (1) is untouched by this fix', typeof w1 === 'number' && isFinite(w1));

  // ── v4.15 regression guards ───────────────────────────────────────────────
  // Same isolated-run pattern as runIsolated() above, but returns every agent's final wealth
  // and the BU/conversion totals so a check can assert BIT-IDENTICAL behaviour, not just a
  // similar median. pBase (above) has no expiry/pth keys — each check supplies what it needs.
  function runIsolatedFull(overrides, seed) {
    const mainRNG = w2.RNG; w2.RNG = w2.mulberry32(seed + 700003);
    const latentPop = w2.makeLatentPopulation(pBase.nAgents);
    w2.RNG = w2.mulberry32(seed);
    const p = Object.assign({}, pBase, overrides);
    const agents = latentPop.map(lat => w2.instantiateAgent(lat, p));
    let bu = 0, conv = 0;
    for (let yr = 0; yr < p.years; yr++) {
      const r = w2.runYear(agents, yr, p, { active: false, incomeMultiplier: 1.0, yearsLeft: 0 });
      bu += r.bu; conv += r.conversion;
    }
    w2.RNG = mainRNG;
    return { wealth: JSON.stringify(agents.map(a => a.wealth)), bu: bu, conv: conv, med: Math.round(w2.calcMetrics(agents, p.ccoOn, p.pth).med) };
  }
  // (1) PTH inflation damping must scale with realised membership. With PTH toggled on but
  // pthUptake=0 nobody is in PTH, and nothing else in runYear() reads p.pth without also
  // requiring a.inPTH — so the run must be bit-identical to PTH off. Pre-v4.15 the flat
  // `inflRate*=0.90` fired on the bare toggle and the two diverged.
  const pthInfl = { expiry: 1, inflRate: 0.04, pth: true, pthUptake: 0 };
  const pthZeroOn = runIsolatedFull(pthInfl, 7), pthZeroOff = runIsolatedFull(Object.assign({}, pthInfl, { pth: false }), 7);
  check('PTH inflation damping: PTH on with zero members is inert (bit-identical to PTH off)',
    pthZeroOn.wealth === pthZeroOff.wealth && pthZeroOn.bu === pthZeroOff.bu,
    'median wealth PTH-on/zero-members $' + pthZeroOn.med + ' vs PTH-off $' + pthZeroOff.med + '  (pre-v4.15: flat 0.90 damped regardless of membership)');
  // (2) A missing expiry must behave as the default (1), not propagate NaN. Pre-v4.15,
  // Math.max(1,undefined) was NaN: BU/conversion totals went NaN and the isNaN rescue on
  // a.wealth silently zeroed every CCO participant's wealth each year.
  const expUndef = runIsolatedFull({ expiry: undefined }, 7), expOne = runIsolatedFull({ expiry: 1 }, 7);
  check('BU expiry: a missing expiry parameter behaves as the default (no NaN propagation)',
    Number.isFinite(expUndef.bu) && Number.isFinite(expUndef.conv) && expUndef.wealth === expOne.wealth && expUndef.bu === expOne.bu,
    'totalBU=' + expUndef.bu + ' median wealth $' + expUndef.med + '  (pre-v4.15: NaN totals, median $0)');
  // (3) + (4) The Monte Carlo CI multiplier is Student's t, and the rendered summary uses it.
  const hasT = typeof w2.tCritical95 === 'function';
  check("Monte Carlo CI: tCritical95 gives Student's t (df=9 -> 2.262, df=49 ~ 2.010, large df -> 1.96)",
    hasT && Math.abs(w2.tCritical95(9) - 2.262) < 1e-9 && Math.abs(w2.tCritical95(49) - 2.0096) < 0.002 && w2.tCritical95(1) === 12.706 && w2.tCritical95(500) === 1.96,
    hasT ? 't(9)=' + w2.tCritical95(9) + ' t(49)=' + w2.tCritical95(49).toFixed(4) + ' t(500)=' + w2.tCritical95(500) : 'tCritical95 not defined (pre-v4.15: fixed z=1.96)');
  let ciOK = false, ciDetail = 'tCritical95 not defined (pre-v4.15: fixed z=1.96)';
  if (hasT) {
    const fake = Array.from({ length: 10 }, (_, i) => ({ pov: 10 + i, bleiPov: 10 + i, gini: 0.5, wealth: 100000, blei: 500, flour: 50 }));
    w2.renderMultiRunSummary(fake, 10, 1);
    const shown = $2('multirun-inner').textContent, hdr = $2('multirun-header').textContent;
    const mean = 14.5, sd = Math.sqrt(fake.reduce((s, r) => s + (r.pov - mean) * (r.pov - mean), 0) / 9), ci = 2.262 * sd / Math.sqrt(10);
    const want = '95% CI: ' + (mean - ci).toFixed(1) + '% \u2013 ' + (mean + ci).toFixed(1) + '%';
    ciOK = shown.indexOf(want) >= 0 && /t=2\.262/.test(hdr) && /df=9/.test(hdr);
    ciDetail = 'expected "' + want + '" (z=1.96 would show 12.6% - 16.4%); header: "' + hdr.slice(-45) + '"';
  }
  check('Monte Carlo CI: the rendered 95% interval uses the t multiplier and states t and df', ciOK, ciDetail);

  w2.downloadCSV(); w2.downloadJSON();
  const csv = (Object.entries(captured).find(([k]) => k && k.endsWith('.csv')) || [])[1] || '';
  const jsonTxt = (Object.entries(captured).find(([k]) => k && k.endsWith('.json')) || [])[1] || '';
  check('CSV export carries the exposure and dominance blocks',
    /CUMULATIVE POVERTY EXPOSURE/.test(csv) && /THRESHOLD DOMINANCE CHECK/.test(csv));
  check('CSV export carries the Wealth Floor Diagnostic block', /WEALTH FLOOR DIAGNOSTIC/.test(csv));
  check('CSV no longer heads its mechanics list "v4.0 FIXES"', !/--- v4\.0 FIXES/.test(csv) && /KEY MECHANICS CHANGES/.test(csv));
  let parsed = null; try { parsed = JSON.parse(jsonTxt); } catch (err) { /* handled below */ }
  check('JSON export parses and carries exposure + dominance',
    !!parsed && !!parsed.results.cumulativePovertyExposure && !!parsed.results.thresholdDominance);
  check('JSON export carries the Wealth Floor Diagnostic', !!parsed && !!parsed.results.wealthFloorDiagnostic);
  check('JSON export states the v4.8 split licence',
    !!parsed && /Apache License 2\.0/.test(parsed.meta.license) && /CC BY 4\.0/.test(parsed.meta.license));
  check('exported version matches META.VERSION', !!parsed && parsed.meta.version === w2.META.VERSION,
    'META.VERSION=' + w2.META.VERSION);
  // v4.16: the default run keeps the fixed 3% Baseline (so every documented figure is unchanged)
  // but must now disclose the mismatch and record it in both exports.
  const bi = r.baselineInflation;
  check('v4.16: default run records Baseline inflation (fixed 3%, unmatched) and warns about the mismatch',
    !!bi && Math.abs(bi.rate - 0.03) < 1e-12 && bi.matched === false && /Baseline comparison runs at a fixed 3\.0% CPI/.test($2('warn-note').textContent),
    bi ? 'rate=' + bi.rate + ' matched=' + bi.matched + ' warn="' + $2('warn-note').textContent.slice(0, 70) + '…"' : 'SIM_RESULTS.baselineInflation missing (pre-v4.16)');
  check('v4.16: CSV and JSON exports carry the Baseline inflation rate',
    /Baseline Inflation Rate/.test(csv) && !!parsed && !!parsed.results.baselineInflation && parsed.parameters.baseInflMatch === false);

  console.log('\n--- Phase 3: internal consistency suite through the live page ---');
  w2.runValidation();
  setTimeout(() => {
    const vt = $2('val-inner').textContent;
    const p = (vt.match(/PASS/g) || []).length, f = (vt.match(/FAIL/g) || []).length;
    check('all six internal consistency & behavioural checks pass', p === 6 && f === 0, p + ' pass / ' + f + ' fail');
    const inv = w2.VAL_STATE.results.invariants, ben = w2.VAL_STATE.results.benefit;
    check('v4.16: invariants check asserts determinism, the 8-draw RNG schedule, bounds and the PTF cap — all OK',
      !!inv && inv.pass && /8 RNG draws\/agent-year OK/.test(inv.detail) && /same seed identical OK/.test(inv.detail) && /new seed differs OK/.test(inv.detail) && /PTF cap \d+\/300 OK/.test(inv.detail),
      inv ? inv.detail : 'missing');
    check('v4.16: benefit check is paired (shocks and inflation matched) and still passes 5/5',
      !!ben && ben.pass && /matched/.test(ben.detail), ben ? ben.detail : 'missing');
    phase4();
  }, 90000);
}, 250);

/* ── Phase 4 (v4.16): reproducibility under interleaved background work ──── */
function phase4() {
  console.log('\n--- Phase 4: seeded runs must reproduce while other work is in flight ---');
  const WANT = 570661;  // v4.20 (v4.19: 559223)
  function waitDone(w, cb) { const t0 = Date.now(); const iv = setInterval(() => {
    if (Date.now() - t0 > 300000) { clearInterval(iv); console.log('  TIMEOUT'); process.exit(2); }
    if (w.SIM_RESULTS && !w.running) { clearInterval(iv); cb(); } }, 5); }
  function fresh() { const w = makeWindow(); w.applyPreset('reference'); w.document.getElementById('s-seed').value = '42'; return w; }
  const wa = fresh();
  wa.runSim();
  waitDone(wa, () => {
    wa.SIM_RESULTS = null; wa.runSim();          // (a) immediately: the 80ms ablation timer is still pending
    waitDone(wa, () => {
      const ra = Math.round(wa.SIM_RESULTS.finalWealth);
      check('seed 42 reproduces when re-run the instant a run finishes (ablation pending)', ra === WANT,
        'got $' + ra + '  (v4.15: $545,506)');
      // (b) mid-flight, triggered deterministically rather than by a delay: a first draft of this
      // check waited 120ms, by which time the ablation had already finished — so it passed on
      // v4.15 too and guarded nothing. The ablation's buildPop() is the only caller of
      // mulberry32(9973); hooking that call queues the rerun behind the ablation's FIRST chunk,
      // so the remaining chunks are genuinely pending when the new run starts.
      const origM = wa.mulberry32; let hooked = false;
      wa.mulberry32 = function (s) {
        if (!hooked && s === 9973) { hooked = true; wa.setTimeout(() => { wa.SIM_RESULTS = null; wa.runSim(); }, 0); }
        return origM(s);
      };
      wa.SIM_RESULTS = null; wa.runSim();          // run 3: its finish() launches the hooked ablation
      waitDone(wa, () => { setTimeout(() => {
        waitDone(wa, () => {
          wa.mulberry32 = origM;
          const rb = Math.round(wa.SIM_RESULTS.finalWealth);
          check('seed 42 reproduces when re-run while the attribution ablation is mid-flight', hooked && rb === WANT,
            hooked ? 'got $' + rb + '  (rerun queued inside the ablation\'s first chunk)' : 'ablation hook never fired');
          const wv = fresh();                        // (c) during the validation suite
          wv.runValidation();
          setTimeout(() => {
            wv.SIM_RESULTS = null; wv.runSim();
            waitDone(wv, () => {
              const rc = Math.round(wv.SIM_RESULTS.finalWealth);
              check('seed 42 reproduces when run while the validation suite is computing', rc === WANT,
                'got $' + rc + '  (v4.15: $555,354)');
              // (d) opt-in inflation matching: Your Settings untouched, Baseline equals harness.js's
              // independent computation of Baseline at 0% inflation, seed 42 (v4.20: wealth $49,876, poverty 48.2%;
              // v4.19: $13,612, 50.8%).
              const wm = fresh();
              if (typeof wm.ST.baseInflMatch === 'undefined') {
                check('Match-Baseline-inflation: Your Settings unchanged, Baseline matches harness.js (seed 42, 0%)', false, 'toggle missing (pre-v4.16)');
                return finish4();
              }
              wm.tog('baseInflMatch', true); wm.runSim();
              waitDone(wm, () => {
                const r = wm.SIM_RESULTS, mainW = Math.round(r.finalWealth), bw = Math.round(r.mBase.med), bp = +(r.mBase.pov * 100).toFixed(1);
                check('Match-Baseline-inflation: Your Settings unchanged, Baseline matches harness.js (seed 42, 0%)',
                  mainW === WANT && bw === 49876 && bp === 48.2 && r.baselineInflation.matched === true && r.baselineInflation.rate === 0,
                  'Your Settings $' + mainW + ' · Baseline median $' + bw + ', poverty ' + bp + '%  (fixed-3% Baseline: −$10,000, 68.8%)');
                finish4();
              });
            });
          }, 150);
        });
      }, 400); });
    });
  });
}
function finish4() { phase5(function () {
  /* v5.1 (audit E6): the number of checks quoted in README.md and CONTRIBUTING.md is verified here so it cannot drift (this check counts itself); --write-counts rewrites it. */
  const HC = require('./harness.js'), nChecks = checks + 1, wc = process.argv.indexOf('--write-counts') >= 0, cc = HC.docCounts('domtest', nChecks, wc);
  check('audit E6 (v5.1): the number of domtest checks quoted in README.md and CONTRIBUTING.md equals the number run (' + nChecks + ')', cc.found.length >= 2 && (cc.stale.length === 0 || wc),
    cc.found.length < 2 ? 'markers found: ' + cc.found.length + ' (need one in each file)' : cc.stale.length === 0 ? 'quoted in ' + cc.found.join(', ') : wc ? 'rewritten (was ' + cc.stale.join(', ') + ')' : 'STALE: ' + cc.stale.join(', ') + '; run node domtest.js --write-counts');
  console.log('\n' + checks + ' checks, ' + (fails ? fails + ' FAILED' : 'all passed'));
  process.exit(fails ? 1 : 0);
}); }

/* ── Phase 5 (v4.17): version labels, export completeness, the four-measure poverty panel,
 * the Adverse Environment preset (checked against harness.js's independent recession port),
 * and the 55%/θ relabels. Run against an unmodified v4.16 index.html, all of these fail. */
function phase5(done) {
  console.log('\n--- Phase 5: v4.17 ---');
  const H = require('./harness.js');
  const wv = makeWindow();
  /* v4.18 repair: stale every label first, then fire the event where the page listens (window).
   * Through v4.17 this dispatched on `document`; a non-bubbling event there never reaches a window
   * listener, so the check only compared static markup with META and never exercised the fill. */
  [...wv.document.querySelectorAll('.meta-ver')].forEach(e => { e.textContent = 'stale'; });
  wv.dispatchEvent(new wv.Event('DOMContentLoaded'));
  const labels = [...wv.document.querySelectorAll('.meta-ver')].map(e => e.textContent);
  const hd = (wv.document.querySelector('.hd-title') || {}).textContent || '';
  check('v4.17: every visible version label reads META.VERSION (header, footer; the assumptions panel moved to the replication page at the release, plan step 12)',
    labels.length >= 2 && labels.every(t => t === 'v' + wv.META.VERSION) && hd.indexOf('v' + wv.META.VERSION) >= 0 && wv.document.title.indexOf('v' + wv.META.VERSION) >= 0,
    'labels=' + JSON.stringify(labels) + ' header="' + hd.trim().slice(-12) + '" (v4.16: header/footer hardcoded v4.15)');
  check('v4.17: the 55% participation warning and sensitivity row no longer claim a network collapse',
    !/network threshold not met/.test(html) && !/network effects collapse/.test(html));
  check('v4.17: θ is no longer described as gated on PTF density in the exported mechanics line',
    !/network-density-gated \(0 below 55% PTF density/.test(html));

  const w5 = makeWindow();
  const cap = {};
  w5.Blob = function (parts) { this.parts = parts; };
  w5.URL.createObjectURL = function (b) { cap.last = b.parts.join(''); return 'blob:stub'; };
  w5.URL.revokeObjectURL = function () {};
  w5.HTMLAnchorElement.prototype.click = function () { cap[this.download] = cap.last; };
  // LHS: with the page's PTF toggle OFF, the sampled ptfShare column must still be live.
  w5.applyPreset('reference'); w5.tog('ptf', false);
  const rng0 = w5.RNG; w5.runLHSSensitivity();
  const rows = w5.LHS_STATE.rows || [];
  const livePTF = rows.filter(r => r.params.ptf === true).length;
  check('v4.17: LHS design keeps PTF live in every row when the page toggle is off (was 0/100)',
    rows.length === 100 && livePTF === 100, livePTF + '/' + rows.length + ' rows with PTF on');
  w5.LHS_STATE.active = false; w5.LHS_STATE.rows = []; w5.RNG = rng0;
  const waitLHS = setInterval(() => {
    if (w5.document.getElementById('lhs-btn').disabled) return;
    clearInterval(waitLHS);
    const lhsCsv = (Object.entries(cap).find(([k]) => k && /lhs/.test(k)) || [])[1] || '';
    check('v4.17: LHS CSV records the fixed settings every row inherits', /Fixed settings \(v4\.17\)/.test(lhsCsv) && /PTF on in every row/.test(lhsCsv));
    // Adverse Environment preset, seed 42, through the page vs harness.js (independent recession port).
    w5.applyPreset('adverse'); w5.document.getElementById('s-seed').value = '42'; w5.SIM_RESULTS = null; w5.runSim();
    const t5 = Date.now();
    const iv5 = setInterval(() => {
      if (Date.now() - t5 > 300000) { clearInterval(iv5); check('v4.17 adverse run finished', false, 'timeout'); return done(); }
      if (!w5.SIM_RESULTS || w5.running) return;
      clearInterval(iv5);
      const r = w5.SIM_RESULTS, hr = H.runScenario(H.ADVERSE_REFERENCE, 42);
      const got = { pov: +r.finalPov.toFixed(1), wealth: Math.round(r.finalWealth), blei: Math.round(r.blei.med), gini: +r.finalGini.toFixed(3) };
      const want = { pov: hr.pov, wealth: hr.wealth, blei: hr.bleiMed, gini: hr.gini };
      check('v4.17: Adverse Environment preset exists and matches harness.js with recessions ported (seed 42)',
        !!w5.PRESETS.adverse && w5.PRESET_IDS.indexOf('adverse') >= 0 && JSON.stringify(got) === JSON.stringify(want),
        'page ' + JSON.stringify(got) + '\n           harness ' + JSON.stringify(want));
      const pp = r.povertyPanel, byK = {}; (pp ? pp.rows : []).forEach(x => { byK[x.k] = x; });
      const hy = hr.yearZero;
      check('v4.17: four-measure panel matches harness.js (final year and year 0)',
        !!pp && ['wealth','blei','inc','incExt','basket','basketGross'].every(k => !!byK[k]) && Math.abs(byK.inc.main - hr.incPov) < 0.05 && Math.abs(byK.basket.main - hr.basketPov) < 0.05 &&
        Math.abs(byK.incExt.main - hr.incPovExt) < 0.05 && Math.abs(byK.basketGross.main - hr.basketPovGross) < 0.05 &&
        Math.abs(byK.wealth.y0 - hy.pov) < 0.05 && Math.abs(byK.blei.y0 - hy.bleiPovNeutral) < 0.05 && Math.abs(byK.blei.y0Scenario - hy.bleiPovScenario) < 0.05 &&
        Math.abs(byK.basket.y0 - hy.basketPov) < 0.05,
        pp ? 'page inc ' + byK.inc.main.toFixed(1) + ' basket ' + byK.basket.main.toFixed(1) + ' y0 basket ' + byK.basket.y0.toFixed(1) + ' | harness ' + hr.incPov + ' / ' + hr.basketPov + ' / ' + hy.basketPov : 'panel missing (pre-v4.17)');
      /* v4.18: was "=== 6 rows"; now every panel row renders once (group-header rows aside). */
      check('v4.17: poverty card renders one table row per panel row',
        !!w5.document.getElementById('sec-poverty4') && w5.document.getElementById('sec-poverty4').style.display === 'block' && !!pp &&
        w5.document.querySelectorAll('#poverty4-inner tbody tr:not(.p5-grp)').length === pp.rows.length && pp.rows.length >= 6,
        (pp ? pp.rows.length : 0) + ' panel rows, ' + w5.document.querySelectorAll('#poverty4-inner tbody tr:not(.p5-grp)').length + ' rendered');
      w5.downloadCSV(); w5.downloadJSON();
      const csv = (Object.entries(cap).find(([k]) => k && k.endsWith('.csv') && !/lhs/.test(k)) || [])[1] || '';
      const js = (Object.entries(cap).find(([k]) => k && k.endsWith('.json')) || [])[1] || '';
      let pj = null; try { pj = JSON.parse(js); } catch (e) { /* below */ }
      check('v4.17: CSV export carries BU Expiry (the one run parameter it omitted)', /BU Expiry \(months\)/.test(csv));
      check('v4.17: CSV and JSON exports carry the four-measure poverty block',
        /POVERTY BY (FOUR|FIVE) MEASURES/.test(csv) && !!pj && !!pj.results.povertyByFourMeasures && pj.results.povertyByFourMeasures.rows.length >= 6);
      phase6(w5, r, csv, pj, H, done);
    }, 200);
  }, 200);
}

/* ── Phase 6 (v4.18): the extreme-poverty overlay, the restyled card, and the exports.
 * Reuses Phase 5's completed seed-42 Adverse Environment run (PTH and SZH on, so the SMI
 * pathway's wellness-zone term is exercised; recessions on, so the economic pathway sees them).
 * Written to fail gracefully against an unmodified v4.17 page, where every check below fails. */
function phase6(w5, r, csv, pj, H, done) {
  console.log('\n--- Phase 6: v4.18 ---');
  const ep = r.extremePoverty || null, C = w5.CFG, near = (a, b) => a !== null && a !== undefined && b !== null && b !== undefined && Math.abs(a - b) < 1e-9;
  const hA = H.runScenario(H.ADVERSE_REFERENCE, 42), hB = H.runScenario(H.baselineFor(H.ADVERSE_REFERENCE, false), 42), hC = H.runScenario(H.ccoOnlyFor(H.ADVERSE_REFERENCE), 42);
  const g = (o, k) => o && o[k] !== undefined ? o[k] : null;
  const parity = !!ep && ['total', 'econ', 'smi', 'vol'].every(k => {
    const hk = 'ep' + k[0].toUpperCase() + k.slice(1);
    return near(g(ep.main, k), hA[hk]) && near(g(ep.base, k), hB[hk]) && near(g(ep.cco, k), hC[hk]);
  }) && near(g(ep.main, 'distress'), hA.distress) && near(g(ep.base, 'distress'), hB.distress) && near(g(ep.cco, 'distress'), hC.distress);
  check('v4.18: extreme-poverty overlay matches harness.js in every component and scenario (seed 42, Adverse Environment)', parity,
    ep ? 'page total ' + [ep.base, ep.cco, ep.main].map(o => g(o, 'total').toFixed(4)).join(' / ') + ' | harness ' + [hB, hC, hA].map(o => o.epTotal.toFixed(4)).join(' / ') + '  (Baseline / CCO Only / Your Settings)' : 'no extremePoverty in SIM_RESULTS (pre-v4.18)');
  const R = C.EP_Y0_RATE * 100;
  check('v4.18: year 0 equals EP_Y0_RATE by construction, and housing distress at year 0 matches harness.js',
    !!ep && near(g(ep.y0, 'total'), R) && near(g(ep.y0, 'distress'), hA.distressY0), ep ? 'year 0 ' + g(ep.y0, 'total') + '%, distress ' + g(ep.y0, 'distress') : '');
  const vol = ep ? [ep.y0, ep.base, ep.cco, ep.main].map(o => g(o, 'vol')) : [];
  check('v4.18: the voluntary pathway is identical in every scenario (policy-invariant by construction)',
    vol.length === 4 && vol.every(v => near(v, R * C.EP_VOL_SHARE)));
  const smi0 = R * (C.EP_SMI_SHARE || 0);
  check('v4.18: SMI pathway — unchanged by Baseline and CCO Only, reduced by PTH+SZH wellness zones in proportion to zone coherence',
    !!ep && near(g(ep.base, 'smi'), smi0) && near(g(ep.cco, 'smi'), smi0) && near(g(ep.y0, 'smi'), smi0) &&
    near(g(ep.main, 'smi'), smi0 * (1 - C.EP_WZ_EFFECT * r.params.szhCoh)) && g(ep.main, 'smi') < smi0,
    ep ? 'Baseline ' + g(ep.base, 'smi').toFixed(4) + ', CCO Only ' + g(ep.cco, 'smi').toFixed(4) + ', Your Settings ' + g(ep.main, 'smi').toFixed(4) + ' (szhCoh ' + r.params.szhCoh + ')' : '');
  const f = w5.extremePovertyOf, base = { pth: true, szh: true, szhCoh: 0.72 };
  check('v4.18: wellness zones need both PTH and SZH; income alone never moves the SMI pathway',
    typeof f === 'function' && near(f(0.1, 0.2, Object.assign({}, base, { szh: false })).smi, smi0) && near(f(0.1, 0.2, Object.assign({}, base, { pth: false })).smi, smi0) &&
    near(f(0.05, 0.2, { pth: false, szh: false }).smi, f(0.4, 0.2, { pth: false, szh: false }).smi) && f(0.05, 0.2, {}).econ < f(0.4, 0.2, {}).econ && f(0.1, 0, {}) === null);
  const doc = w5.document, th = doc.querySelector('#poverty4-inner thead');
  const extRows = ['extreme', 'extremeEcon', 'extremeSmi', 'extremeVol'].every(k => !!doc.querySelector('#poverty4-inner tr[data-k="' + k + '"]'));
  check('v4.18: card restyled — scenario badges in the header, three row groups, coloured change cells, extreme rows present',
    !!th && ['sb-y0', 'sb-base', 'sb-cco', 'sb-user'].every(c => !!th.querySelector('.' + c)) && doc.querySelectorAll('#poverty4-inner tr.p5-grp').length === 3 &&
    doc.querySelectorAll('#poverty4-inner td.p5-chg.good').length > 0 && extRows && /Five Measures/.test((doc.querySelector('#sec-poverty4 .slabel') || {}).textContent || ''));
  const wt = makeWindow();
  wt.document.title = wt.document.title.replace(/v\d+\.\d+/, 'v0.0');
  wt.dispatchEvent(new wt.Event('DOMContentLoaded'));
  check('v4.18: the tab title is filled from META.VERSION as well', wt.document.title.indexOf('v' + wt.META.VERSION) >= 0, 'title="' + wt.document.title.slice(0, 44) + '…"');
  check('v4.18: CSV and JSON exports carry the extreme-poverty rows, constants and housing distress',
    /Extreme poverty \(v4\.18\)/.test(csv) && /EP_Y0_RATE/.test(csv) && /Housing distress/.test(csv) && !!pj && !!pj.results.extremePoverty &&
    !!pj.results.extremePoverty.main && pj.results.povertyByFourMeasures.rows.some(x => x.k === 'extreme'));
  phase7(function () { phase8(done); });  // v4.19; v4.20 adds Phase 8
}

/* ── Phase 7 (v4.19): automatic stabilizers and the Shock Response card.
 * Every check is written to fail gracefully, not throw, against an unmodified v4.18 page. */
function phase7(done) {
  console.log('\n--- Phase 7: v4.19 ---');
  const H = require('./harness.js');
  const has = w => typeof w.shockRun === 'function' && typeof w.stabParamsFromUI === 'function';

  // 7a. controls, defaults, URL round-trip
  const wu = makeWindow('?stabOn=1&stabm=1.75&stabSevOn=0&emergOn=1&emtk=80&colaOn=1&colath=2.5&stabSuspOn=1');
  wu.applyParamsFromURL();
  const $u = id => wu.document.getElementById(id);
  const d0 = makeWindow(), $0 = id => d0.document.getElementById(id);
  const defaultsOff = has(d0) && ['stab', 'stabSev', 'stabSusp', 'emerg', 'cola'].every(k => d0.ST[k] === false) &&
    !!$0('stab-off') && $0('stab-off').getAttribute('aria-pressed') === 'true' && $0('s-stabm').value === '1.35' && $0('s-stabk').value === '2.8';
  check('v4.19: stabilizer controls exist and every lever is off by default (multiplier default x1.35, scaled gain 2.8)', defaultsOff);
  check('v4.19: stabilizer settings round-trip through a shared URL',
    has(wu) && wu.ST.stab === true && wu.ST.emerg === true && wu.ST.cola === true && wu.ST.stabSusp === true && wu.ST.stabSev === false &&
    $u('s-stabm').value === '1.75' && $u('s-emtk').value === '80' && $u('s-colath').value === '2.5' && $u('stab-on').getAttribute('aria-pressed') === 'true',
    has(wu) ? 'ST.stab=' + wu.ST.stab + ' s-stabm=' + $u('s-stabm').value : 'no stabilizer controls (pre-v4.19)');

  // 7b. engine: inert when off, inert when it cannot fire, RNG schedule unchanged
  if (!has(d0)) {
    ['inert when off or unable to fire', 'no RNG draw added', 'page and harness agree on every lever', 'emergency enrollment only in triggered years',
     'in-page study matches harness', 'card, warnings, exports and CCO Only'].forEach(n => check('v4.19: ' + n, false, 'pre-v4.19 page'));
    return done();
  }
  const FI = Object.assign({}, H.FULL_INTEGRATION);
  const off = Object.assign({}, FI, {shock: true, stab: false});
  const onNoShock = Object.assign({}, FI, {shock: false, stab: true, stabMult: 3, stabSusp: true, emerg: true, emergTakeup: 1, stabThresh: 0});
  const offNoShock = Object.assign({}, FI, {shock: false, stab: false});
  const x1 = Object.assign({}, off, {stab: true, stabMult: 1, stabThresh: 0});
  const colaNoInfl = Object.assign({}, off, {cola: true, colaThresh: 0});   // inflation 0: nothing to index
  const same = (a, b) => JSON.stringify(a.dAll) === JSON.stringify(b.dAll) && JSON.stringify(a.dPart) === JSON.stringify(b.dPart);
  check('v4.19: inert when off or unable to fire (recessions off; x1.00; COLA at 0% inflation) — bit-identical to off',
    same(d0.shockRun(onNoShock, 42), d0.shockRun(offNoShock, 42)) && same(d0.shockRun(x1, 42), d0.shockRun(off, 42)) && same(d0.shockRun(colaNoInfl, 42), d0.shockRun(off, 42)));
  let cnt = 0; const orig = d0.mulberry32;
  d0.mulberry32 = function (s) { const f = orig(s); return function () { cnt++; return f(); }; };
  d0.shockRun(off, 11); const cOff = cnt; cnt = 0;
  const all = Object.assign({}, FI, {shock: true, stab: true, stabSev: true, stabK: 11, stabSusp: true, emerg: true, emergTakeup: 0.5, cola: true, colaThresh: 0, inflRate: 0.02});
  d0.shockRun(Object.assign({}, all, {stab: false, cola: false}), 11); const cBase2 = cnt; cnt = 0;
  d0.shockRun(all, 11); const cAll = cnt;
  d0.mulberry32 = orig;
  check('v4.19: no RNG draw added — every lever on draws exactly as many random numbers as every lever off',
    cOff > 0 && cAll === cBase2 && cOff === cBase2, 'off ' + cOff + ', off at 2% inflation ' + cBase2 + ', all levers on ' + cAll);
  const pairs = [off, Object.assign({}, off, {stab: true, stabMult: 2.35, stabThresh: 0.02}), all,
    Object.assign({}, H.STRESS_TEST, {stab: true, stabSev: true, stabK: 15, emerg: true, emergTakeup: 0.3, cola: true, colaThresh: 0.01})];
  const agree = pairs.every(p => { const a = d0.shockRun(p, 5), b = H.shockRun(p, 5); return same(a, b) && a.extra === b.extra && a.base === b.base; });
  check('v4.19: page and harness agree on every lever (fixed, scaled, expiry, emergency, COLA; seed 5)', agree);
  // Option B: relief scales with BU — identical to the old flat 0.80 at $1,200, different elsewhere
  const at = (bu, w) => { const p = Object.assign({}, FI, {shock: false, bu: bu}); return JSON.stringify(w.shockRun(p, 9).dPart); };
  H.setStabSwitches(1, true);
  const flat1200 = JSON.stringify(H.shockRun(Object.assign({}, FI, {shock: false, bu: 1200}), 9).dPart), flat900 = JSON.stringify(H.shockRun(Object.assign({}, FI, {shock: false, bu: 900}), 9).dPart);
  H.setStabSwitches(1, false);
  check('v4.19: CCO cost relief scales with BU — bit-identical to the v4.18 flat rule at $1,200, different at $900',
    typeof d0.CFG.CCO_RELIEF_CAP === 'number' && at(1200, d0) === flat1200 && at(900, d0) !== flat900);
  // emergency enrollment: count from runYear's return, triggered vs not
  d0.RNG = d0.mulberry32(3);
  const pE = Object.assign({}, FI, {stab: true, stabMult: 1, stabThresh: 0, emerg: true, emergTakeup: 0.5});
  const pop = d0.makeLatentPopulation(500).map(l => d0.instantiateAgent(l, pE));
  const line = pE.partRate + 0.5 * (1 - pE.partRate);
  const expect = pop.filter(a => !a.inCCO && a.uCCO < line).length;
  const rOn = d0.runYear(pop, 0, pE, {active: true, incomeMultiplier: 0.88, yearsLeft: 1});
  const rOff = d0.runYear(pop, 1, pE, {active: false, incomeMultiplier: 1, yearsLeft: 0});
  check('v4.19: emergency enrollment only in triggered years, and exactly the non-participants below the take-up line',
    rOn.stabOn === true && rOn.emergN === expect && expect > 0 && rOff.stabOn === false && rOff.emergN === 0,
    'triggered ' + rOn.emergN + ' (expected ' + expect + '), untriggered ' + rOff.emergN);

  // 7c. a full run through the live page with every lever on, then the in-page study
  const w7 = makeWindow(), $7 = id => w7.document.getElementById(id);
  const cap = {};
  w7.Blob = function (parts) { this.parts = parts; };
  w7.URL.createObjectURL = function (b) { cap.last = b.parts.join(''); return 'blob:stub'; };
  w7.URL.revokeObjectURL = function () {};
  w7.HTMLAnchorElement.prototype.click = function () { cap[this.download] = cap.last; };
  w7.applyPreset('adverse');
  w7.tog('stab', true); w7.tog('stabSusp', true); w7.tog('emerg', true); w7.tog('cola', true);
  $7('s-seed').value = '42';
  w7.SIM_RESULTS = null; w7.runSim();
  const t7 = Date.now();
  const iv7 = setInterval(() => {
    if (Date.now() - t7 > 300000) { clearInterval(iv7); check('v4.19 run finished', false, 'timeout'); return done(); }
    if (!w7.SIM_RESULTS || w7.running) return;
    clearInterval(iv7);
    const r = w7.SIM_RESULTS, P = r.params;
    const hp = Object.assign({}, H.ADVERSE_REFERENCE, {stab: true, stabSev: false, stabMult: 1.35, stabK: 2.8, stabThresh: 0.02, stabSusp: true, emerg: true, emergTakeup: 0.5, cola: true, colaThresh: 0});
    const hr = H.runScenario(hp, 42), hc = H.runScenario(H.ccoOnlyFor(hp), 42);
    const got = {pov: +r.finalPov.toFixed(1), wealth: Math.round(r.finalWealth), blei: Math.round(r.blei.med), gini: +r.finalGini.toFixed(3), cco: Math.round(r.mCCO.med)};
    const want = {pov: hr.pov, wealth: hr.wealth, blei: hr.bleiMed, gini: hr.gini, cco: hc.wealth};
    const sr = r.shockResponse || {};
    check('v4.19: card, warnings, exports and CCO Only — a seed-42 Adverse Environment run with every lever on matches harness.js (Your Settings and CCO Only)',
      JSON.stringify(got) === JSON.stringify(want) && !!sr.run && sr.run.recYears > 0 && sr.run.firedYears === sr.run.recYears && sr.run.colaExtra > 0 && sr.run.emergAgentYears > 0,
      'page ' + JSON.stringify(got) + '\n           harness ' + JSON.stringify(want));
    const warn = ($7('warn-note') || {}).textContent || '';
    check('v4.19: the run warns that the stabilizer and COLA are on, and the Shock Response card and run-config line show them',
      /Automatic BU increase on/.test(warn) && /BU indexed to inflation/.test(warn) && $7('sec-shock').style.display === 'block' &&
      /fired in/.test($7('shock-run-inner').textContent) && /Stabilizers:/.test(($7('run-conf-inner') || {}).innerHTML || ''));
    // in-page study, reduced to 3 seeds, against harness.shockStudy on the same parameters
    w7.CFG.STAB_STUDY_SEEDS = 3;
    const Pst = w7.shockStudyParams();
    w7.runShockStudy();
    const ivS = setInterval(() => {
      if (w7.SHOCK_STATE.active) return;
      clearInterval(ivS);
      const ps = r.shockResponse.study, hs = H.shockStudy(JSON.parse(JSON.stringify(Pst)), 3);
      const near = (a, b) => Math.abs(a - b) < 1e-9;
      const keys = ['partPP', 'nonPartPP', 'allPP', 'extremePer10k', 'extraPctOfBase'];
      const ok = !!ps && !ps.error && ['none', 'hub', 'yours'].every(k => keys.every(q => near(ps[k][q], hs[k][q]))) &&
        ps.neutral.m === hs.neutral.m && ps.neutral.reached === hs.neutral.reached;
      check('v4.19: the in-page shock-response study matches harness.shockStudy exactly (3 seeds: every arm, and the shock-neutral multiplier)', ok,
        ps && !ps.error ? 'page neutral x' + ps.neutral.m + ', harness x' + hs.neutral.m : 'no study result');
      const rows = w7.document.querySelectorAll('#shock-study-inner tbody tr').length;
      w7.setStabToNeutral();
      check('v4.19: the study table renders three rules and "Set the multiplier slider" applies the neutral value',
        rows === 3 && Math.abs(parseFloat($7('s-stabm').value) - ps.neutral.m) < 1e-9, rows + ' rows; slider ' + $7('s-stabm').value);
      w7.downloadCSV(); w7.downloadJSON();
      const csv = (Object.entries(cap).find(([k]) => k && k.endsWith('.csv')) || [])[1] || '';
      const js = (Object.entries(cap).find(([k]) => k && k.endsWith('.json')) || [])[1] || '';
      let pj = null; try { pj = JSON.parse(js); } catch (e) { /* below */ }
      check('v4.19: CSV and JSON exports carry the stabilizer settings, this run\'s tally and the study',
        /Auto BU Increase in Recessions \(v4\.19\)/.test(csv) && /SHOCK RESPONSE/.test(csv) && /Shock-neutral multiplier/.test(csv) &&
        !!pj && pj.parameters.stab === true && !!pj.results.shockResponse && !!pj.results.shockResponse.study && pj.results.shockResponse.run.firedYears > 0);
      done();
    }, 200);
  }, 200);
}

/* ── Phase 8 (v4.20): accessibility, the shared-link seed readout, the JSON basis label, the
 * unit suite against the page, page/harness source parity, the automationRisk sampler, and the
 * paired non-participant check. Every check here fails against an unmodified v4.19 page. jsdom
 * renders nothing, so the focus-visible checks confirm the CSS rules exist, not how they look. */
function phase8(done) {
  console.log('\n--- Phase 8: v4.20 ---');
  const H = require('./harness.js');
  const w = makeWindow(), d = w.document, $ = id => d.getElementById(id);
  w.applyPreset('reference');
  w.dispatchEvent(new w.Event('DOMContentLoaded'));   // where the page listens (see the v4.18 repair)
  const txt = el => (el ? el.textContent : '').replace(/\s+/g, ' ').trim();
  const nameOf = el => { const ids = (el.getAttribute('aria-labelledby') || '').split(/\s+/).filter(Boolean);
    return ids.map(id => txt($(id))).join(' ').trim() || (el.getAttribute('aria-label') || '').trim(); };

  // 8-0. the page's own load-time run never fires inside a test window (the v4.20 CI failure)
  const wq = makeWindow();
    // checked at the end of this phase, after other synchronous work has given jsdom time to fire its events
  // 8a. accessible names
  const sliders = [...d.querySelectorAll('input[type="range"]')], groups = [...d.querySelectorAll('.tg')];
  const cnOf = el => { const cr = el.closest('.cr'); const cn = cr && cr.querySelector('.cn'); if (!cn) return '';
    const c = cn.cloneNode(true); c.querySelectorAll('.abbr-link').forEach(x => x.remove()); return txt(c); };
  const badS = sliders.concat([$('s-seed')]).filter(el => !nameOf(el) || nameOf(el) !== cnOf(el) || /ⓘ/.test(nameOf(el)));
  const badG = groups.filter(g => g.getAttribute('role') !== 'group' || !nameOf(g) || (g.closest('.cr') && nameOf(g) !== cnOf(g)));  // groups outside a sidebar row (the threshold-view pair) carry their own aria-label
  const lblIds = [...d.querySelectorAll('[id^="lbl-"]')].map(e => e.id);
  check('v4.20: every slider, the seed field and every On/Off group is named by its visible label (a11y)',
    sliders.length >= 18 && groups.length >= 14 && !badS.length && !badG.length && new Set(lblIds).size === lblIds.length,
    sliders.length + ' sliders, ' + groups.length + ' groups; unnamed or mismatched: ' + (badS.concat(badG).map(e => e.id || e.className).join(', ') || 'none') +
    '; e.g. s-bu "' + nameOf($('s-bu')) + '", PTF cap group "' + (groups.find(g => /ptfCap/.test(g.innerHTML)) ? nameOf(groups.find(g => /ptfCap/.test(g.innerHTML))) : '') + '"');

  // 8b. tooltips reachable by keyboard and exposed to assistive technology
  const tips = [...d.querySelectorAll('[data-tip]')];
  const icons = tips.filter(el => el.tagName !== 'A' && el.tagName !== 'BUTTON'), hosts = tips.filter(el => el.tagName === 'A' || el.tagName === 'BUTTON');
  const iconsOK = icons.length >= 10 &&  /* plan step 12: the comparison's tooltips left with it */ icons.every(el => el.getAttribute('tabindex') === '0' && el.getAttribute('role') === 'img' && el.getAttribute('aria-label') === el.getAttribute('data-tip'));
  const hostsOK = hosts.length >= 14 && hosts.every(el => { const dd = $(el.getAttribute('aria-describedby') || ''); return !!dd && dd.textContent === el.getAttribute('data-tip'); });
  const nDesc = $('tip-desc') ? $('tip-desc').children.length : -1;
  if (typeof w.initA11y === 'function') w.initA11y();
  const nDesc2 = $('tip-desc') ? $('tip-desc').children.length : -1;
  const css = [...d.querySelectorAll('style')].map(x => x.textContent).join('\n');
  const cssOK = /\.abbr-link:focus-visible::after/.test(css) && /\.tip-host\[data-tip\]:focus-visible::after/.test(css) && /input\[type=range\]:focus-visible\{outline:/.test(css);
  check('v4.20: every tooltip is keyboard-reachable and exposed (ⓘ focusable and named, buttons and links described), opens on focus, and init is idempotent',
    iconsOK && hostsOK && nDesc === hosts.length && nDesc2 === hosts.length && cssOK,
    icons.length + ' ⓘ icons ' + (iconsOK ? 'OK' : 'NOT OK') + ', ' + hosts.length + ' buttons/links ' + (hostsOK ? 'OK' : 'NOT OK') + ', descriptions ' + nDesc + ' then ' + nDesc2 + ', focus CSS ' + (cssOK ? 'present' : 'missing'));

  // 8b2. v4.22: one floating tooltip, placed by script, serves every tip. The ::after boxes were clipped by the front door's
  // scroll box and widened the page on phones; they now apply only without scripts. jsdom has no layout, so this checks
  // behaviour (opens with the host's text on hover and on keyboard focus, not on a mouse-click focus; closes on leave and
  // Escape; one box however often init runs), not placement. Placement was checked in a headless Chromium (session 10).
  {
    let tipOK = false, tipDetail = 'no initTips (pre-v4.22 page)';
    if (typeof w.initTips === 'function') {
      w.initTips(); w.initTips();
      const boxes = d.querySelectorAll('#tip-float'), box = boxes[0], ic = icons.find(el => el.closest('#front-door')) || icons[0], pb = $('pb-adverse');
      const on = () => !!box && box.classList.contains('on'), is = el => on() && box.textContent === el.getAttribute('data-tip');
      const kb0 = w.tipByKey, st = {};
      try {
        w.tipByKey = () => false; ic.focus(); st.clickFocus = !on(); ic.blur();
        w.tipByKey = () => true; ic.focus(); st.keyFocus = is(ic);
        ic.dispatchEvent(new w.KeyboardEvent('keydown', {key: 'Escape', bubbles: true})); st.esc = !on(); ic.blur();
        ic.dispatchEvent(new w.MouseEvent('mouseover', {bubbles: true})); st.hover = is(ic);
        d.body.dispatchEvent(new w.MouseEvent('mouseover', {bubbles: true})); st.leave = !on();
        if (pb) { pb.dispatchEvent(new w.MouseEvent('mouseover', {bubbles: true})); st.preset = is(pb); w.tipHide(); }
      } finally { w.tipByKey = kb0; }
      const css2 = /html:not\(\.js-tips\) \.abbr-link::after\{content:attr\(data-tip\)/.test(css) && /html:not\(\.js-tips\) \.tip-host\[data-tip\]::after\{content:attr\(data-tip\)/.test(css) && /#tip-float\{position:fixed/.test(css);
      tipOK = boxes.length === 1 && box.getAttribute('aria-hidden') === 'true' && d.documentElement.classList.contains('js-tips') && css2 && Object.keys(st).length === 6 && Object.values(st).every(Boolean);
      tipDetail = boxes.length + ' box(es); ' + Object.keys(st).map(k => k + ' ' + (st[k] ? 'ok' : 'FAIL')).join(', ') + '; fallback CSS scoped to no-script: ' + css2;
    }
    check('v4.22: one floating tooltip serves every tip: it opens on hover and on keyboard focus (not a mouse-click focus), closes on leave and Escape, and the CSS boxes apply only without scripts', tipOK, tipDetail);
  }

  // 8c. sliders announce their formatted value
  const vt0 = $('s-bu').getAttribute('aria-valuetext');
  $('s-bu').value = '900'; w.sv('bu', '900');
  const vt1 = $('s-bu').getAttribute('aria-valuetext');
  const allVT = w.SLIDER_KEYS.every(k => $('s-' + k).getAttribute('aria-valuetext') === $('v-' + k).textContent);
  check('v4.20: sliders carry aria-valuetext equal to the displayed value, kept current by sv()',
    vt0 === '$1,200' && vt1 === $('v-bu').textContent && vt1 !== vt0 && allVT, 's-bu "' + vt0 + '" then "' + vt1 + '"');

  // 8d. shared-link seed readout
  const seedCase = q => { const ws = makeWindow(q); ws.applyParamsFromURL(); return [ws.document.getElementById('s-seed').value, ws.document.getElementById('v-seed').textContent]; };
  const sA = seedCase('?seed=abc'), sB = seedCase('?seed=12abc'), sC = seedCase('?seed=17');
  check('v4.20: a shared link\'s seed readout shows the seed the run will use (malformed seeds read "variable", not "NaN" or a partial number)',
    sA[0] === '' && sA[1] === 'variable' && sB[0] === '' && sB[1] === 'variable' && sC[0] === '17' && sC[1] === '17',
    '?seed=abc -> "' + sA[1] + '", ?seed=12abc -> "' + sB[1] + '", ?seed=17 -> "' + sC[1] + '"  (v4.19: "NaN", "12", "17")');

  // 8e. the extreme-poverty block of the JSON export says what it is
  const pp = w.buildPovertyPanel({}, {});
  check('v4.20: the JSON export\'s extreme-poverty block carries an explicit "overlay" basis',
    !!pp && !!pp.extremePoverty && /overlay/.test(pp.extremePoverty.basis || '') && /no random number/.test(pp.extremePoverty.basis || ''), pp && pp.extremePoverty ? String(pp.extremePoverty.basis) : 'missing');

  // 8f. the shared unit suite, against the page's own functions
  const T = {CFG: w.CFG, getRNG: () => w.RNG, setRNG: r => { w.RNG = r; }};
  ['mulberry32', 'gamma', 'beta', 'lognormal', 'drawAutomationRisk', 'szhTheta', 'pthLiquidShare', 'getTier', 'medianOf', 'coeffVar', 'structuralStability',
   'povertyCDF', 'buildPrefixSum', 'povertyGapAvg', 'checkDominance', 'tCritical95'].forEach(n => { if (typeof w[n] === 'function') T[n] = w[n]; });
  const U = H.unitSuite(T), uf = U.filter(x => !x.pass), us = U.filter(x => x.skipped);
  check('v4.20: harness.unitSuite() passes against the page\'s own functions, none skipped (' + U.length + ' tests)',
    U.length === 15 && !uf.length && !us.length, uf.length ? 'failed: ' + uf.map(x => x.name + ' [' + x.detail + ']').join('; ') : U.find(x => /drawAutomationRisk/.test(x.name)).detail);

  // 8g. source parity: every function the page and harness.js share is the same code. v5.3 (B1, one engine copy): harness.js reads the engine out of the page, so
  // the script it runs (H.builtSource()) is compared; the five known differences of v4.20-v5.2.2 are gone (two moved into the page behind off-switches).
  const src = H.builtSource();
  const names = [...src.matchAll(/^function ([A-Za-z0-9_]+)\(/gm)].map(m => m[1]);
  const hf = new Function('module', 'require', '__dirname', '__filename', src + ';return {' + names.join(',') + '};')({exports: {}}, require, __dirname, path.join(__dirname, 'harness.js'));
  const norm = f => f.toString().replace(/\/\*[\s\S]*?\*\//g, '').replace(/\/\/[^\n]*/g, '').replace(/\s+/g, '');
  const KNOWN = {};  /* v5.3 (B1): none; until v5.2.2 runYear, drawAutomationRisk, getTier, agentBLEI and incomeBasketMetrics differed by known amounts */
  const shared = names.filter(n => typeof w[n] === 'function');
  const drift = shared.filter(n => !KNOWN[n] && norm(w[n]) !== norm(hf[n]));
  const seqP = [], seqH = [];
  w.RNG = w.mulberry32(77); for (let i = 0; i < 1000; i++) seqP.push(w.drawAutomationRisk());
  const HT = H.unitTargets(), savedH = HT.getRNG(); HT.setRNG(H.mulberry32(77)); for (let i = 0; i < 1000; i++) seqH.push(HT.drawAutomationRisk()); HT.setRNG(savedH);
  check('v4.20: every function shared by the page and harness.js is identical source (' + (shared.length - Object.keys(KNOWN).length) + ' functions), and drawAutomationRisk() draws identical sequences',
    shared.length >= 40 && !drift.length && seqP.every((x, i) => x === seqH[i]), drift.length ? 'DRIFTED: ' + drift.join(', ') : shared.length + ' shared, all identical (v5.3: harness.js runs the page\'s engine)');

  // 8h. agent construction no longer depends on the high-risk share
  const latent = share => { w.CFG.AUTO_HIGH_SHARE = share; w.RNG = w.mulberry32(42 + 700003); const L = w.makeLatentPopulation(500); return L; };
  const saveShare = w.CFG.AUTO_HIGH_SHARE, La = latent(0.47), Lb = latent(0.63); w.CFG.AUTO_HIGH_SHARE = saveShare;
  const sameRest = La.every((a, i) => ['wealth', 'wage', 'octaveShape', 'qualityZ', 'lambda', 'uCCO', 'uPTF', 'uPTH'].every(k => a[k] === Lb[i][k]));
  const hiShare = Lb.filter(a => a.automationRisk >= 0.5).length / Lb.length;
  check('v4.20: changing the automation high-risk share changes automationRisk and nothing else in agent construction',
    sameRest && La.some((a, i) => a.automationRisk !== Lb[i].automationRisk) && w.CFG.AUTO_HIGH_SHARE === 0.63,
    'every other latent trait identical across shares 0.47 and 0.63: ' + sameRest + '; share of agents at or above 0.5 at 0.63: ' + (hiShare * 100).toFixed(1) + '%  (v4.19: construction re-streamed)');

  // 8i. the paired non-participant validation check
  const np = w.VAL_TESTS.find(t => t.id === 'nonpart');
  const saved = w.RNG; const rnp = np ? np.fn() : null; w.RNG = saved;
  const worst = rnp ? parseFloat((rnp.detail.match(/largest difference ([+-]?[\d.]+)pp/) || [])[1]) : NaN;
  check('v4.20: the non-participant check compares the same people in both arms, and passes with room',
    !!rnp && rnp.pass && /paired/.test(rnp.detail) && worst <= 0, rnp ? rnp.detail : 'missing');
  setTimeout(() => {
    check('v4.20: a test window never starts the page\'s load-time reference run, whatever the machine speed (the first CI run failed on this race)',
      wq.document.readyState === 'complete' && !wq.SIM_RESULTS && !wq.running,
      'readyState ' + wq.document.readyState + ', results ' + (wq.SIM_RESULTS ? 'present (auto-run fired)' : 'none') + ' after 1.5 s');
    phase9(done);  // v4.21
  }, 1500);
}

/* ── Phase 9 (v4.21): CCO relief under inflation. Through v4.20 the relief share was read off
 * NOMINAL effective BU against the year-0 $1,200 reference, so an unindexed BU kept its full real
 * relief and a COLA-indexed one counted inflation twice. Every check fails against v4.20. */
function phase9(done) {
  console.log('\n--- Phase 9: v4.21 ---');
  const H = require('./harness.js');
  const w = makeWindow();
  const CALM = {active: false, incomeMultiplier: 1, yearsLeft: 0};
  function pop(win, p, seed) { win.RNG = win.mulberry32(seed + 700003); return win.makeLatentPopulation(p.nAgents).map(l => win.instantiateAgent(l, p)); }
  function reliefPath(win, p, seed) {  // relief share seen by a CCO participant outside PTF and PTH, and the price index, by year
    const ag = pop(win, p, seed); win.RNG = win.mulberry32(seed); const out = [];
    for (let y = 0; y < p.years; y++) { win.runYear(ag, y, p, CALM); const a = ag.find(x => x.inCCO && !x.inPTF && !x.inPTH);
      out.push({r: 1 - a.yrCostUSD / a.yrBasketUSD, P: a.yrBasketUSD / win.CFG.LIVING_WAGE_ANNUAL}); }
    return out;
  }
  const ADV = Object.assign({}, H.ADVERSE_REFERENCE, {shock: false});
  const noCola = reliefPath(w, ADV, 1), cola = reliefPath(w, Object.assign({}, ADV, {cola: true, colaThresh: 0}), 1);
  const exactCola = cola.every(x => Math.abs(x.r - 0.20) < 1e-12);
  const exactNo = noCola.every(x => Math.abs(x.r - 0.20 / x.P) < 1e-12) && noCola[19].r < 0.16 && noCola[19].P > 1.2;
  check('v4.21: under inflation, CCO relief holds 20% of the basket with COLA and erodes with the price index without it (Adverse settings, seed 1)',
    exactCola && exactNo, 'year 20: no COLA ' + (noCola[19].r * 100).toFixed(2) + '% at price index ' + noCola[19].P.toFixed(3) + ', COLA ' + (cola[19].r * 100).toFixed(2) + '%  (v4.20: 20.00% and ' + (20 * noCola[19].P).toFixed(2) + '%)');
  const FI0 = Object.assign({}, H.FULL_INTEGRATION), z1 = reliefPath(w, FI0, 1), z2 = reliefPath(w, Object.assign({}, FI0, {cola: true, colaThresh: 0}), 1);
  check('v4.21: at 0% inflation the relief is exactly 20% with or without COLA (the fix is inert there)',
    z1.concat(z2).every(x => x.r === 0.2 || Math.abs(x.r - 0.2) < 1e-15) && z1.every(x => x.P === 1));
  const same = (p, seed) => { const a = pop(w, p, seed), b = (H.setRNG(H.mulberry32(seed + 700003)), H.makeLatentPopulation(p.nAgents).map(l => H.instantiateAgent(l, p)));
    w.RNG = w.mulberry32(seed); H.setRNG(H.mulberry32(seed)); const rp = p.shock ? H.buildRecessionPath(p.years, seed) : null;
    for (let y = 0; y < p.years; y++) { const rs = rp ? rp[y] : CALM; const sv = H.getRNG(); w.runYear(a, y, p, rs); H.setRNG(sv); H.runYear(b, y, p, rs); }
    return a.every((x, i) => x.wealth === b[i].wealth && x.wage === b[i].wage && x.yrCostUSD === b[i].yrCostUSD); };
  const par = [H.ADVERSE_REFERENCE, Object.assign({}, H.ADVERSE_REFERENCE, {cola: true, colaThresh: 0, stab: true, stabMult: 1.35, stabThresh: 0.02, emerg: true, emergTakeup: 0.5}),
    Object.assign({}, H.STRESS_TEST, {inflRate: 0.05, cola: true, colaThresh: 0.01})].every(p => same(p, 7));
  check('v4.21: the page\'s runYear() and harness.js agree agent by agent under inflation, with and without COLA and stabilizers (seed 7)', par);
  function pageRun(p, seed) { const ag = pop(w, p, seed), rp = p.shock ? w.buildRecessionPath(p.years, seed) : null; w.RNG = w.mulberry32(seed);
    for (let y = 0; y < p.years; y++) w.runYear(ag, y, p, rp ? rp[y] : CALM);
    const m = w.calcMetrics(ag, p.ccoOn, p.pth), b = w.bleiMetrics(ag, p.bu, p.ccoOn, p.pth, p.szh, p.szhCoh, p.ptf);
    return [+(m.pov * 100).toFixed(1), Math.round(m.med), Math.round(b.med), +m.gini.toFixed(3)]; }
  const FIX = [['Full Integration', H.FULL_INTEGRATION, [15.8, 570661, 1975, 0.518]], ['CCO Only', H.CCO_ONLY, [24.8, 427239, 1283, 0.575]], ['Baseline', H.BASELINE, [68.8, -10000, 8, 0.824]],
    ['High Automation', H.HIGH_AUTOMATION, [27.8, 382123, 1351, 0.603]], ['Adverse Environment', H.ADVERSE_REFERENCE, [36.8, 205005, 723, 0.658]], ['Stress Test', H.STRESS_TEST, [59.8, -10000, 16, 0.785]]];
  const got = FIX.map(f => pageRun(f[1], 42)), bad = FIX.filter((f, i) => got[i].join() !== f[2].join());
  check('v4.21: every preset\'s seed-42 figures from the page\'s engine match the fixtures harness.js validate asserts (Adverse Environment and Stress Test moved)',
    !bad.length, bad.length ? bad.map(f => f[0] + ' ' + got[FIX.indexOf(f)].join(' / ') + ' (expected ' + f[2].join(' / ') + ')').join('; ') : FIX.map((f, i) => f[0] + ' ' + got[i].join(' / ')).slice(4).join('; ') + ' (v4.20: 35.0 / 218851 / 819 / 0.646; 59.0 / -10000 / 16 / 0.781)');
  phase10(done);  // session 7: the replication page
}

/* ── Phase 10 (session 7, dashboard i1 and s10): the replication page lives in this repository (replication.html) and
 * must describe the engine it ships with. Through v4.21 it sat in the Research Hub's repository, and its version labels went
 * stale four times (CONTRIBUTING.md v4.9, v4.13). Every label that names the engine version carries class repl-ver, the
 * page declares the version in <meta name="sim-version"> and in its JSON-LD, and all of them must equal META.VERSION, so a
 * release that bumps META without the page fails CI. The page's links from index.html must point here, not to the Hub. */
function phase10(done) {
  CUR = html;  /* v5.2 step 8: from here on, the main page */
  console.log('\n--- Phase 10: the replication page (session 7) ---');
  const RP = path.join(path.dirname(FILE), 'replication.html'), NEW = 'https://bettertobest.github.io/compassionism-simulation/replication.html';
  if (!fs.existsSync(RP)) { check('session 7: replication.html exists beside index.html', false, 'missing: ' + RP); return done(); }
  const w = makeWindow(), V = w.META.VERSION, rd = new JSDOM(fs.readFileSync(RP, 'utf8')).window.document;
  const meta = (rd.querySelector('meta[name="sim-version"]') || {}).content, labels = [...rd.querySelectorAll('.repl-ver')].map(e => e.textContent.trim());
  let ld = null; try { ld = JSON.parse(rd.querySelector('script[type="application/ld+json"]').textContent); } catch (e) {}
  check('session 7: the replication page declares the engine version (meta sim-version, JSON-LD) and every version label reads v' + V,
    meta === V && !!ld && ld.version === V && labels.length >= 4 && labels.every(t => t === 'v' + V),
    'META.VERSION=' + V + ', meta=' + meta + ', JSON-LD=' + (ld && ld.version) + ', labels=' + JSON.stringify(labels));
  const canon = (rd.querySelector('link[rel="canonical"]') || {}).href;
  check('session 7: the replication page\'s canonical address is in this repository', canon === NEW && !!ld && ld.url === NEW, 'canonical=' + canon);
  const links = [...w.document.querySelectorAll('a[href*="replication"]')].map(a => a.getAttribute('href'));
  check('session 7: every index.html link to the replication page points here, none to the Hub\'s old address',
    links.length >= 4 && links.every(h => h.split('#')[0] === NEW),  /* plan step 12: a link may name a section */ links.length + ' links' + (links.some(h => h !== NEW) ? '; stale: ' + links.filter(h => h !== NEW).join(', ') : ''));
  phase11(done);  // session 8: the front door
}

/* ── Phase 11 (session 8, dashboard s18; the plan's A6): the front door. The first screen states in one sentence the question
 * the tool answers (and README.md opens with the same sentence), offers a design comparison and a preset picker, has one
 * caveats box that stays visible, and links to the method. The comparison is data written by `node harness.js frontdoor`
 * from the testbed's a5 output; wherever Compassionism is shown, the row with its two unsourced mechanisms switched off
 * (the octave wage raise, d19; the PTF/PTH inflation damping, d33) must sit directly beneath it. */
function phase11(done) {
  console.log('\n--- Phase 11: the front door (plan step 12; session 8 before it) ---');
  const H = require('./harness.js'), w = makeWindow(), d = w.document, fdEl = d.getElementById('front-door');
  if (!fdEl || typeof w.relRender !== 'function') { check('step 12: the release front door exists', false, 'no #front-door or relRender'); return done(); }
  w.relInit();  // its DOMContentLoaded handler runs only when a check dispatches the event (see makeWindow)
  const q = (d.getElementById('fd-q') || {}).textContent || '', qs = q.trim();
  const readme = fs.readFileSync(path.join(path.dirname(FILE), 'README.md'), 'utf8').split('\n').filter(l => l.trim())[1] || '';
  check('the first screen states in one sentence what the tool tests, before the layout, and README.md opens with the same sentence',
    /^[^.?!]+[.?]$/.test(qs) && fdEl.compareDocumentPosition(d.querySelector('footer')) === 4 /* v5.2 step 8: the earlier engine's layout left for its own page */ && readme.replace(/\*\*/g, '').trim() === qs,
    '"' + qs.slice(0, 70) + '..."; README line 2 ' + (readme.replace(/\*\*/g, '').trim() === qs ? 'matches' : 'differs: ' + readme.slice(0, 60)));
  const ATTR = 'The math and code of this simulation were engineered by Claude, an AI model made by Anthropic, from the concepts in Duke Johnson\'s book Better To Best and his related vision for eradicating extreme poverty while enriching cultures and supporting human flourishing. The model has not yet been reviewed by an independent economist; the full code is open for anyone to check, and expert collaborators are welcome.';
  const at = (d.getElementById('fd-attr') || {}).textContent || '', rd = fs.readFileSync(path.join(path.dirname(FILE), 'README.md'), 'utf8').replace(/[*_]/g, ''), rp = new JSDOM(fs.readFileSync(path.join(path.dirname(FILE), 'replication.html'), 'utf8')).window.document.body.textContent.replace(/\s+/g, ' ');
  check('step 12: the attribution (CLAUDE.md wording) sits directly under the title, and in the README and on the replication page',
    at.replace(/\s+/g, ' ').trim() === ATTR && d.getElementById('fd-q').nextElementSibling === d.getElementById('fd-attr') && rd.replace(/\s+/g, ' ').indexOf(ATTR) >= 0 && rp.indexOf(ATTR) >= 0,
    'page ' + (at.replace(/\s+/g, ' ').trim() === ATTR ? 'ok' : 'DIFFERS') + '; README ' + (rd.replace(/\s+/g, ' ').indexOf(ATTR) >= 0 ? 'ok' : 'missing') + '; replication ' + (rp.indexOf(ATTR) >= 0 ? 'ok' : 'missing'));
  let D = null; try { D = JSON.parse(d.getElementById('rel-data').textContent); } catch (e) {}
  const envs = D && D.envs ? Object.keys(D.envs) : [], NEEDR = ['release', 'h1', 'face', 'cost', 'cap5', 'tax', 'all', 'free', 'standins', 's30', 'v422'];  /* plan step 18: the v5.0 readings */
  check('step 12: the 500-seed panel parses, covers all three environments with every reading, and names its command',
    envs.join() === 'ref,adv,st' && envs.every(e => NEEDR.every(k => D.envs[e].rows[k] && D.envs[e].rows[k].dBO.length === 3)) && D._meta && D._meta.seeds === 500 && /node harness\.js testbed 500 release/.test(D._meta.command || ''),
    'environments: ' + envs.join(', ') + '; seeds ' + (D && D._meta ? D._meta.seeds : '?'));
  const txts = {}; ['ref', 'adv', 'st'].forEach(e => { w.relSet(e); txts[e] = (d.getElementById('rel-out') || {}).textContent || ''; });
  const blFirst = ['ref', 'adv', 'st'].every(e => { const t = txts[e]; const i = t.indexOf('Basic living covered'); return i >= 0 && i < t.indexOf('Living below the cost of living') && /design-neutral/.test(t) && /Savings\./.test(t) && /Who gains/.test(t) && /Work\./.test(t) && /Prices\./.test(t) && /Cost and how it is paid/.test(t) && /Public costs avoided/.test(t) && /optimistic end/.test(t); });
  const rows = d.querySelectorAll('#rel-rows tr').length, srcT = (d.getElementById('rel-src') || {}).textContent || '';
  check('step 12: every environment opens with BLEI (Duke\'s definition, the design-neutral reading beside it), then one sentence each on poverty, savings, groups, work, prices, cost and avoided costs, the optimistic end, the other readings and the command',
    blFirst && rows >= NEEDR.length && rows === w.REL_CSV_ORDER.filter(k => D && D.envs.st && D.envs.st.rows[k]).length && /500 paired runs/.test(srcT) && /node harness\.js testbed 500 release/.test(srcT), 'sentences ' + (blFirst ? 'in order' : 'MISSING') + '; readings ' + rows + '; source "' + srcT.slice(0, 60) + '"');
  const conf = ['ref', 'adv', 'st'].map(e => { const r = D.envs[e].rows.release; const ok = r.dF0[2] < 0 && r.dPov[2] < 0 && r.dBO[2] < 0; return e + ':' + (ok ? 'confirmed' : 'not') + (/A confirmed gain/.test(txts[e]) === ok ? '' : ' MISLABELLED'); });
  check('step 12: the panel calls a gain confirmed only where basket poverty, wealth poverty and BLEI poverty all fall (95% intervals below zero)', conf.every(x => !/MISLABELLED/.test(x)), conf.join(', '));
  /* Session 33 (Duke's 40-year horizon): the 40-year panel parses with every reading in all three environments, says 40 years in its
   * command, and the Years switch shows it ("year 40") and switches back to the 20-year text. */
  let D40 = null; try { D40 = JSON.parse(d.getElementById('rel-data-40').textContent); } catch (e) {}
  w.relSet('ref'); w.relYears(40); const t40 = (d.getElementById('rel-out') || {}).textContent || '', th40 = (d.getElementById('rel-th-pov') || {}).textContent || '';
  w.relYears(20); const t20b = (d.getElementById('rel-out') || {}).textContent || '';
  check('session 33: the 40-year panel covers all three environments with every reading, and the Years switch shows it and switches back',
    !!D40 && D40._meta && D40._meta.years === 40 && /--years=40/.test(D40._meta.command || '') && ['ref', 'adv', 'st'].every(e => D40.envs[e] && NEEDR.every(k => D40.envs[e].rows[k] && D40.envs[e].rows[k].dBO.length === 3)) &&
    /at year 40/.test(t40) && /Over 40 years/.test(t40) && th40 === 'Too little wealth, year 40' && /at year 20/.test(t20b) && !/Over 40 years/.test(t20b) && t20b === txts.ref,
    D40 ? '40-year panel: ' + Object.keys(D40.envs).join(', ') + '; text ' + (/at year 40/.test(t40) ? 'year 40' : 'MISSING') : 'no #rel-data-40');
  w.relSet('adv'); const si = d.getElementById('rel-seed'); si.value = '3'; const st0 = w.setTimeout; w.setTimeout = function (f) { f(); }; w.relRun(); w.setTimeout = st0;
  const live = w.REL.last, hR = (function(){ const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G); try { const P = Object.assign({}, H.ADVERSE_REFERENCE), PR = H.tbPresets(P);
    return H.tbStudy([{p:PR.baseline()}, H.n1Row(PR, 'framework', Object.assign({fin:'source', a:0, jn:{}, cs:{}}, H.REL_V5))], 3, P, {fin:'tax', aT:0, a:0, X:0, sc:H.SPEND_SOURCED}, 3); } finally { H.resetNR6(svN); H.tbSetG(svG); } })();
  const liveOK = !!live && live.seed === 3 && live.x.r.bOAPy === hR[1].bOAPy && live.x.b.pov === hR[0].pov && live.x.r.cost === hR[1].cost && /Basic living covered/.test((d.getElementById('rel-live-out') || {}).textContent || '');
  check('step 12: "Run it yourself" runs the page\'s release engine and matches harness.js on the same seed (Adverse, seed 3), and the earlier settings stay restored after it',
    liveOK && w.SURPLUS_CONSUMPTION_SHARE === 0 && w.CONVERSION_MODEL === 'engine', live ? 'BLEI poverty page ' + live.x.r.bOAPy.toFixed(2) + ' / harness ' + hR[1].bOAPy.toFixed(2) + '; spending share after ' + w.SURPLUS_CONSUMPTION_SHARE : 'no run');
  const vis = fdEl.textContent + ' ' + fs.readFileSync(path.join(path.dirname(FILE), 'README.md'), 'utf8');
  const lim = [...d.querySelectorAll('#uncertainty-notice li')].length, draft = fs.existsSync(path.join(path.dirname(FILE), 'dev', 'drafts', 'compare-designs.html'));
  /* Oct 7, 2026 (Duke): the walk-through (v5.0, s65) is off the page and out of the README until the model settles (it showed an earlier version); its files stay
   * in walkthrough/ for the one re-recording when the simulation is settled. */
  const wtDir = path.join(path.dirname(FILE), 'walkthrough'), wtKept = ['walkthrough.mp4', 'tour.json', 'README.md'].every(f => fs.existsSync(path.join(wtDir, f)));
  check('step 12: the comparison has left the page (no table, no "other designs", saved unlinked in dev/drafts/), the out-of-date walk-through is neither on the page nor linked from the README (its files kept for the re-recording), and a short list of limits remains',
    !d.getElementById('fd-table') && !d.getElementById('fd-data') && !/other designs/i.test(vis) && !/walkthrough\/walkthrough\.mp4/.test(fs.readFileSync(path.join(path.dirname(FILE), 'README.md'), 'utf8')) && !d.querySelector('video, #fd-video *') && ![...d.querySelectorAll('[href], [src]')].some(e => /walkthrough\//.test(e.getAttribute('href') || e.getAttribute('src'))) && wtKept && draft && lim >= 5 && lim <= 8,
    'limits ' + lim + '; draft ' + (draft ? 'saved' : 'MISSING') + '; walk-through files ' + (wtKept ? 'kept' : 'MISSING'));
  /* v5.2 step 8 (decision D): the earlier engine moved to its own page, linked from the front door; that page links back, carries the same script as this one
   * (dev/tools/sync_earlier.py), keeps every preset, and a pick loads that preset and runs it. This page no longer carries the earlier engine's controls. */
  const we = makeWindow('', {page: 'early'}), de = we.document, ln = d.getElementById('fd-old-link'), back = de.querySelector('#ee-head a[href="index.html"]');
  const pbs = [...de.querySelectorAll('.preset-grid .pbtn')].map(b => b.id.replace(/^pb-/, '')), scr = h => { const i = h.lastIndexOf('<script>\n'); return h.slice(i, h.indexOf('</script>', i)); };
  const saveRun = we.runSim; let ran = 0; we.runSim = function () { ran++; }; we.fdRun('adverse'); we.runSim = saveRun;
  const pbA = de.getElementById('pb-adverse'), same = htmlEarly !== html && scr(htmlEarly) === scr(html), gone = !d.getElementById('pb-reference') && !d.querySelector('.layout');
  check('step 12 (v5.2 decision D): the earlier engine has its own page, linked as "Explore the earlier engine" and linking back, with the same script as this page; every preset is there, and a pick loads that preset and runs it; this page carries none of its controls',
    !!ln && ln.getAttribute('href') === 'earlier-engine.html' && /Explore the earlier engine/.test(ln.textContent) && !!back && same && gone && pbs.length === 6 && pbs.every(c => we.PRESET_IDS.indexOf(c) >= 0) && ran === 1 && we.ST.shock === true && pbA && /pbtn-active/.test(pbA.className) && /v4\.22/.test((de.getElementById('ee-head') || {}).textContent || ''),
    'link ' + (ln ? ln.getAttribute('href') : 'MISSING') + '; back link ' + !!back + '; same script ' + same + '; controls gone here ' + gone + '; presets ' + pbs.join(', ') + '; runs started ' + ran);
  const fourGone = !/Four Measures/.test(d.body.innerHTML), buOK = !/redeemable at PTF|redeemable below market price at PTF/.test((d.getElementById('sec-glossary') || {}).textContent || 'missing') && !!d.getElementById('sec-glossary'), distOK = !/efficiency losses from reducing market competition/.test(d.body.innerHTML);
  check('step 12: the three wording fixes: the poverty card is "Five Measures" everywhere; the BU glossary no longer says BU are spent at PTFs only; the 30% PTF caution is labelled a placeholder with no efficiency loss in the model',
    fourGone && buOK && distOK, 'Five Measures ' + fourGone + '; BU glossary ' + buOK + '; 30% label ' + distOK);
  phase12(done);  // plan step 10: the release engine
}

/* ── Phase 12 (plan step 10, Oct 1, 2026): the release engine. dev/tools/port_engine.py copies harness.js's engine (the Hub-spec model,
 * project hiring, ESP payroll, the ESP split, the production side, joining and leaving, PTF running costs, the octave rule, the spending
 * rule, the price, labour and financing modules, and the testbed runner) into index.html verbatim, in place of the page's runYear. Two
 * checks keep the copies equal: every ported function's source text matches harness.js, and the release configuration (every mechanism,
 * paid for by the Source, at the sourced spending share) gives identical results on the same seeds in all three environments. */
function phase12(done) {
  console.log('\n--- Phase 12: the release engine (plan step 10) ---');
  const H = require('./harness.js'), w = makeWindow(), html = fs.readFileSync(FILE, 'utf8');
  const blk = html.slice(html.indexOf('RELEASE ENGINE: ported verbatim'), html.indexOf('END RELEASE ENGINE')) + html.slice(html.indexOf('plan step 10: harness.js version'), html.indexOf('plan step 10: harness.js version') + 2000);
  const fnames = [...blk.matchAll(/^function ([A-Za-z_$][\w$]*)/gm)].map(m => m[1]), hsrc = H.builtSource();  /* v5.3 (B1): the script harness.js runs, read out of the page */
  const diff = fnames.filter(n => { const re = new RegExp('^function ' + n.replace(/\$/g, '\\$') + '\\(', 'm'), a = blk.search(re), b = hsrc.search(re);
    if (a < 0 || b < 0) return true; const grab = (t, i) => { let d = 0, j = t.indexOf('{', i); for (; j < t.length; j++){ if (t[j] === '{') d++; else if (t[j] === '}' && --d === 0) break; } return t.slice(i, j + 1); };
    return grab(blk, a) !== grab(hsrc, b); });
  check('step 10 (v5.3: one engine copy): every function in the page\'s release engine is the one harness.js runs (harness.js reads the engine out of index.html)',
    fnames.length > 40 && diff.length === 0, fnames.length + ' functions; differing: ' + (diff.length ? diff.join(', ') : 'none'));
  /* v5.1 (audit V5-04): the behavioural parity check now covers every row of the release panel (the no-programme baseline and the eleven readings, built from harness.js's
   * releaseRows so the page and the harness run the same row options, including the V5-02 gate), in all three environments, at 20 and at 40 years, on seeds 1-2. */
  const SC = H.SPEND_SOURCED;
  function relAll(X, envName, seeds, years){ const svN = X.applyNR6(), svG = X.tbSetG(X.TB_PROFILE_G); try { const P = Object.assign({}, X[envName], years ? {years} : {}), PR = X.tbPresets(P), rows = H.releaseRows(SC);
      const cfg = [Object.assign({p: PR.baseline()}, {sc: SC})].concat(rows.map(r => { const c = X.n1Row(PR, 'framework', r.v); if (r.v.o) Object.assign(c.o || (c.o = {}), r.v.o); return c; }), H.releaseBases(SC).map(b => Object.assign({p: PR.baseline()}, b.v)));  /* v5.2: + the paired no-programme rows */
      return X.tbStudy(cfg, seeds, P, {fin:'tax', aT:0, a:0, X:0, sc:SC}); } finally { X.resetNR6(svN); X.tbSetG(svG); } }
  const keys = H.TB_KEYS, nRows = H.releaseRows(SC).length + H.releaseBases(SC).length + 1, nRows51 = H.releaseRows(SC, true).length + 1; let fg = [];
  [20, 40].forEach(yrs => { const bad = []; let n = 0, rowsSeen = 0;
    ['FULL_INTEGRATION', 'ADVERSE_REFERENCE', 'STRESS_TEST'].forEach(e => { const a = relAll(w, e, 2, yrs === 20 ? 0 : yrs), b = relAll(H, e, 2, yrs === 20 ? 0 : yrs); rowsSeen = a.length;
      a.forEach((r, i) => keys.forEach(k => { n++; for (let s = 0; s < 2; s++) if (r._s[k][s] !== b[i]._s[k][s]) { bad.push(e + ' row ' + i + ' ' + k); break; } })); fg.push(yrs + 'y ' + e + ' ' + (a[2].fgt2PY - a[0].fgt2PY).toFixed(2)); });
    check('step 10 (v5.1, V5-04; v5.2): page and harness agree on every row of the release panel, every measure, same seeds (seeds 1-2; Reference, Adverse and Stress; ' + yrs + ' years; the no-programme baseline, every reading and the paired no-programme rows)',
      bad.length === 0 && rowsSeen === nRows && nRows51 === 12, rowsSeen + ' rows x ' + n/rowsSeen/3 + ' measures x 3 environments compared; differing: ' + (bad.length ? bad.slice(0, 5).join('; ') : 'none') + (yrs === 20 ? '' : '; release poverty severity vs no programme: ' + fg.filter(x => x.startsWith('40')).join(', '))); });
  /* The bindings fingerprint: every top-level name the page and harness.js share (values and functions) is compared, the values by a canonical serialisation, the functions by their
   * source (exactly, or with comments and white space removed, which is what a comment-only edit changes). The only differences allowed are the ones listed, each with its reason,
   * and each must still be there (a stale allow-list entry fails). The names come from the two global scopes (the page's window, harness.js run in a vm context), so no parser is needed. */
  const vm = require('vm'), root = path.dirname(FILE), blank = new JSDOM('', {runScripts: 'outside-only'}).window, blankNames = new Set(Object.getOwnPropertyNames(blank));
  const wf = makeWindow(), pageNames = Object.getOwnPropertyNames(wf).filter(n => !blankNames.has(n)), mod = {exports: {}}, req = Object.assign(n => require(n.startsWith('.') ? path.join(root, n) : n), {main: undefined});
  const shims = ['require', 'module', 'exports', 'process', '__dirname', '__filename', 'console', 'Buffer', 'setTimeout', 'clearTimeout', 'builtSource', 'csEngineSource'];
  const ctx = vm.createContext({require: req, module: mod, exports: mod.exports, process, __dirname: root, __filename: path.join(root, 'harness.js'), console, Buffer, setTimeout, clearTimeout, builtSource: H.builtSource, csEngineSource: H.csEngineSource});
  vm.runInContext(H.builtSource(), ctx, {filename: 'harness.js (built: the page\'s engine, then harness.js\'s own code)'});  /* v5.3 (B1): the script harness.js runs */
  const builtin = new Set(Object.getOwnPropertyNames(vm.runInContext('globalThis', vm.createContext({}))).concat(shims)), harnessNames = Object.getOwnPropertyNames(ctx).filter(n => !builtin.has(n));
  const shared = pageNames.filter(n => harnessNames.includes(n)), isFn = n => typeof ctx[n] === 'function';
  function canon(v, seen) { seen = seen || new Set(); if (v === undefined) return 'undefined'; if (v === null) return 'null'; if (typeof v === 'function') return 'fn:' + v.toString();
    if (typeof v === 'number') return Object.is(v, -0) ? '-0' : String(v); if (typeof v !== 'object') return typeof v + ':' + JSON.stringify(v); if (seen.has(v)) return '[circular]'; seen.add(v);
    if (ArrayBuffer.isView(v)) return 'ta:' + Array.prototype.join.call(v, ','); if (Array.isArray(v)) return '[' + v.map(x => canon(x, seen)).join(',') + ']';
    return '{' + Object.keys(v).sort().map(k => JSON.stringify(k) + ':' + canon(v[k], seen)).join(',') + '}'; }
  const strip = t => t.replace(/\/\*[\s\S]*?\*\//g, '').replace(/\/\/[^\n]*/g, '').replace(/\s+/g, '');
  /* v5.3 (B1, one engine copy): no allowed differences. Until v5.2.2 five were listed: the page's display-only additions to CFG, TIERS and getTier, and the harness's
   * legacy automation sampler and UBI term (both now in the page behind their off-switches). */
  const ALLOWED = {};
  const unexpected = [], commentOnly = [], stale = [], shapeBad = [], present = [];
  shared.forEach(n => { const a = wf[n], b = ctx[n]; let same, cmt = false;
    if (isFn(n)) { const x = a.toString(), y = b.toString(); same = x === y; if (!same && strip(x) === strip(y)) { same = true; cmt = true; } } else same = canon(a) === canon(b);
    if (cmt) commentOnly.push(n);
    if (!same) { if (ALLOWED[n] && ALLOWED[n].fn === isFn(n)) { present.push(n); if (ALLOWED[n].shape && !ALLOWED[n].shape(a, b)) shapeBad.push(n); } else unexpected.push(n); } });
  Object.keys(ALLOWED).forEach(n => { if (!present.includes(n)) stale.push(n); });
  const nVal = shared.filter(n => !isFn(n)).length, nFn = shared.filter(isFn).length;
  check('step 10 (v5.1, V5-04): every top-level name the page and harness.js share (' + nVal + ' values, ' + nFn + ' functions) is identical, except the allow-listed differences, each of which is still there and has the stated shape',
    nVal >= 80 && nFn >= 80 && unexpected.length === 0 && stale.length === 0 && shapeBad.length === 0,
    shared.length + ' shared; allowed differences present: ' + present.join(', ') + '; comment-only differences: ' + commentOnly.length + (commentOnly.length ? ' (' + commentOnly.join(', ') + ')' : '') +
    (unexpected.length ? '; UNEXPECTED: ' + unexpected.join(', ') : '') + (stale.length ? '; STALE allow-list entries: ' + stale.join(', ') : '') + (shapeBad.length ? '; WRONG SHAPE: ' + shapeBad.join(', ') : ''));
  phase13(done);  // audit fixes (Oct 2, 2026)
}

/* ── Phase 13 (audit pass on v5.0, Oct 2, 2026): four defects the earlier phases could not see.
 *  (a) static version fields (title, JSON-LD, banner, replication page, CONTRIBUTING signature) all equal META.VERSION;
 *  (b) relLiveWorse reads a run's own numbers (a live run used to say "No group is worse off" whatever it showed);
 *  (c) real live runs (Reference and Adverse, seed 1) never say "No group is worse off" while their own numbers show a loss;
 *  (d) with Chart.js missing the page still loads, shows the note, and an earlier-engine run completes (it used to stall at 100%). */
function phase13(done) {
  console.log('\n--- Phase 13: audit fixes (Oct 2, 2026) ---');
  const stale = require(path.join(path.dirname(FILE), 'dev', 'tools', 'check_versions.js')).findStale(path.dirname(FILE));
  check('audit V5-01: every static version field (title, JSON-LD, banner, replication page, CONTRIBUTING signature) equals META.VERSION',
    stale.length === 0, stale.length ? stale.slice(0, 4).map(x => x.file + ' ' + x.field + ' ' + x.found).join('; ') : 'none stale');
  const w = makeWindow();
  const L = w.relLiveWorse || function () { return ''; };  // absent before this fix: the checks below then FAIL instead of throwing
  const t1 = L({grp: {part: 5, non: -3, low: 1, top: 2}, dPov: [-1]}), t2 = L({grp: {part: 5, non: 3, low: 1, top: 2}, dPov: [2]}), t3 = L({grp: {part: 5, non: 3, low: 1, top: 2}, dPov: [-2]});
  check('audit finding 1: relLiveWorse names a group that loses, names rising wealth poverty, and says "no group" only when neither happens',
    /did not \(less real income\)/.test(t1) && !/no group is worse off/.test(t1) && /overall \(more wealth poverty\)/.test(t2) && /no group is worse off in this run/.test(t3) && !/Worse off/.test(t3),
    'loss: ' + /did not/.test(t1) + '; poverty up: ' + /overall/.test(t2) + '; neither: ' + /no group/.test(t3));
  const bad = [];
  [['ref', 'FULL_INTEGRATION'], ['adv', 'ADVERSE_REFERENCE']].forEach(e => {
    w.REL.env = e[0]; w.REL.yrs = 20; const x = w.relLiveRows(e[0], 1), txt = w.relSentences(x.b, x.r, null, 20).replace(/<[^>]+>/g, ''),
      loses = ['part', 'non', 'low', 'top'].some(k => x.r.grp[k] < 0) || x.r.dPov[0] > 0;
    if (loses && /No group is worse off than with no programme on any test/.test(txt)) bad.push(e[0] + ' seed 1');
    if (loses && !/Worse off than with no programme in this run/.test(txt)) bad.push(e[0] + ' seed 1 (no loss named)'); });
  check('audit finding 1: live runs (Reference and Adverse, seed 1) state the losses their own numbers show', bad.length === 0, bad.length ? bad.join('; ') : 'both consistent');
  /* v5.1 (audit F3, E1, E5): the regenerated 500-seed panels. (a) every row carries the price level as mean, median and 10th/90th percentiles under the new key names (the old key
   * pLev20 is gone from the export); the Prices sentence gives the typical run and its range, and above 1,000 times today's names the price rule and says "a limit of the model, not a forecast"
   * with no figure; the replication page carries the exact figures. (b) the Hub-target table is on the front door for every environment and horizon, with the sourced targets, the
   * panel's own numbers and the right verdicts, and on the replication page for all six combinations. (c) no Gini verdict depends on the small-sample bias of the Gini formula.
   * (d) the manifest. */
  const root = path.dirname(FILE), HB = require('./harness.js'), P20 = JSON.parse(fs.readFileSync(path.join(root, 'dev', 'runs', 'release-panel.json'), 'utf8')), P40 = JSON.parse(fs.readFileSync(path.join(root, 'dev', 'runs', 'release-panel-40.json'), 'utf8'));
  const wr = makeWindow(); wr.relInit(); const dr = wr.document, ENVN = ['ref', 'adv', 'st'], ROWS = ['release', 'h1', 'face', 'cost', 'cap5', 'tax', 'all', 'free', 'standins', 's30', 'v422'];
  const emb20 = JSON.parse(dr.getElementById('rel-data').textContent), emb40 = JSON.parse(dr.getElementById('rel-data-40').textContent);
  const fmtLev = x => x >= 10 ? Math.round(x).toLocaleString('en-US') : x.toFixed(2);
  const keysOK = [P20, P40].every(Pn => ENVN.every(e => ROWS.every(k => { const r = Pn.envs[e].rows[k]; return r && ['pLevEnd', 'pLevEndMed', 'pLevEndP10', 'pLevEndP90', 'giniD', 'giniX', 'epPY'].every(q => typeof r[q] === 'number' && isFinite(r[q])) && !('pLev20' in r) &&
    r.pLevEndP10 <= r.pLevEndMed && r.pLevEndMed <= r.pLevEndP90 && r.pLevEnd > 0; }) && ['giniD', 'giniX', 'epPY'].every(q => typeof Pn.envs[e].base[q] === 'number')));
  const prices = (env, yrs) => { wr.relSet(env); wr.relYears(yrs); return [...dr.querySelectorAll('#rel-out p')].map(p => p.textContent).filter(t => /^Prices\./.test(t))[0] || ''; };
  /* v5.2.2 (Muse audit F1): v5.1 to v5.2.1 said "nine runs in ten" for the 10th to 90th percentile band, which holds eight in ten, and this check asserted the
   * same wrong words. It now derives the words from the percentile pair the sentence actually prints: it finds which stored percentile keys (pLevEndP<q>) the two
   * numbers in the sentence are, and expects the words for hi - lo percent of the runs (p10/p90 => "eight runs in ten", p5/p95 => "nine runs in ten"). */
  const NUMW = ['no', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'all ten'], bandWords = (lo, hi) => { const n = Math.round((hi - lo) / 10); return NUMW[n] + (n === 1 ? ' run' : ' runs') + (n === 10 ? '' : ' in ten'); };
  const bandSeen = [], bandOK = (r, t) => { const m = /and ((?:\w+ runs? in ten)|all ten runs) fall between (\d[\d,]*(?:\.\d+)?) and (more than 1,000|\d[\d,]*(?:\.\d+)?)/.exec(t); if (!m) return false;
    const qs = Object.keys(r).map(k => /^pLevEndP(\d+)$/.exec(k)).filter(Boolean).map(x => +x[1]), lo = qs.filter(q => fmtLev(r['pLevEndP' + q]) === m[2]),
      hi = qs.filter(q => m[3] === 'more than 1,000' ? r['pLevEndP' + q] > 1000 : fmtLev(r['pLevEndP' + q]) === m[3]).filter(q => !lo.length || q > lo[0]);
    if (lo.length !== 1 || hi.length !== 1) return false; bandSeen.push(lo[0] + '/' + hi[0] + ' "' + m[1] + '"'); return m[1] === bandWords(lo[0], hi[0]); };
  const bandSelf = bandWords(10, 90) === 'eight runs in ten' && bandWords(5, 95) === 'nine runs in ten' && bandWords(25, 75) === 'five runs in ten';
  const pr = [];
  [[20, P20], [40, P40]].forEach(([yrs, Pn]) => ENVN.forEach(e => { const r = Pn.envs[e].rows.release, t = prices(e, yrs);
    if (r.pLevEndMed > 1000) { if (!(/no central bank, no interest rate and no protection for savings/.test(t) && /limit of the model, not a forecast/.test(t) && /exact 500-seed figures are on the replication page/.test(t)) || t.indexOf(fmtLev(r.pLevEndMed)) >= 0 || t.indexOf(fmtLev(r.pLevEnd)) >= 0) pr.push(e + ' ' + yrs + 'y high'); }
    else if (t.indexOf('the typical run (the median of the 500) is ' + fmtLev(r.pLevEndMed) + ' times today') < 0 || !bandOK(r, t) || /limit of the model/.test(t)) pr.push(e + ' ' + yrs + 'y low'); }));
  wr.relYears(20); wr.relSet('ref');
  /* v5.2.1: the v5.2 tables and the backing-share chart moved from the replication page to the findings explorer (findings.html), which renders them from the release
   * data file with site/findings.js and site/charts.js; the checks below read the explorer's rendered tables and chart, with the same assertions as before. */
  const expW = new JSDOM('<!DOCTYPE html><body></body>', {runScripts: 'outside-only'}).window, MANI = JSON.parse(fs.readFileSync(path.join(root, 'data', 'manifest.json'), 'utf8'));
  expW.eval(fs.readFileSync(path.join(root, 'site', 'charts.js'), 'utf8')); expW.eval(fs.readFileSync(path.join(root, 'site', 'findings.js'), 'utf8'));
  const RELF = JSON.parse(fs.readFileSync(path.join(root, 'data', MANI.releases.filter(r => r.status === 'current')[0].file), 'utf8'));
  expW.document.body.innerHTML = RELF.tables.map(t => expW.CSF.tableHTML(RELF, t, null)).join('') + '<div id="backing-chart"></div>'; expW.CSF.charts.backing(RELF, expW.document.getElementById('backing-chart'));
  const repDoc = expW.document, tcell = (sel, i, j) => (repDoc.querySelectorAll(sel + ' tbody tr')[i] || {children: []}).children[j];
  const levCellOK = [['[data-table="rel-t20"]', P20], ['[data-table="rel-t40"]', P40]].every(([sel, Pn]) => ENVN.every((e, i) => { const r = Pn.envs[e].rows.release, c = tcell(sel, i, 5), tx = c ? c.textContent.replace(/\s+/g, ' ') : '';
    return tx.indexOf(fmtLev(r.pLevEndMed) + '×') === 0 && tx.indexOf('10th–90th percentile ' + fmtLev(r.pLevEndP10) + '–' + fmtLev(r.pLevEndP90)) > 0 && tx.indexOf('mean ' + fmtLev(r.pLevEnd)) > 0; }));
  check('audit F3 (v5.1): the panels carry the price level as mean, median and 10th/90th percentiles (the key pLev20 is gone from the export); the Prices sentence gives the typical run and its range, in words derived from the percentile pair it prints (v5.2.2, Muse F1), and above 1,000 times today\'s says the price rule runs away, a model limit and not a forecast, with no figure; the findings explorer\'s tables keep the exact figures',
    keysOK && pr.length === 0 && levCellOK && bandSelf, 'keys ' + (keysOK ? 'ok' : 'MISSING') + '; sentences ' + (pr.length ? 'WRONG: ' + pr.join(', ') : 'ok (median ' + [P20, P40].map(Pn => ENVN.map(e => fmtLev(Pn.envs[e].rows.release.pLevEndMed)).join(' / ')).join(' ; ') + ')') + '; explorer cells ' + (levCellOK ? 'match' : 'DIFFER') +
    '; range words derived from the percentile pair: ' + (bandSelf ? '' : 'DERIVATION WRONG ') + ([...new Set(bandSeen)].join(', ') || 'none shown'));
  /* (b) the Hub-target table */
  const nearL = g => Math.abs(g - 0.25) < 0.002 || Math.abs(g - 0.30) < 0.002, verd = g => (g <= 0.25 ? 'at or below 0.25' : g <= 0.30 ? 'between 0.25 and 0.30' : 'above 0.30') + (nearL(g) ? ' (on the line: within 0.002)' : ''), plainV = g => g <= 0.25 ? 'low' : g <= 0.30 ? 'mid' : 'high', tb = [];
  /* v5.2 round, step 2: a panel with the v5.2 block (rows carry .rep) gets the v5.2 table: each measure at Year 7 and the last year, Compassionism with no programme beside it, the
   * official poverty line first, a BLEI figure, and the income and wealth Ginis against their own Hub numbers; the v5.1 table is checked as before for a panel without the block. */
  const V52 = [emb20, emb40].every(Pn => ENVN.every(e => Pn.envs[e].rows.release.rep && Pn.envs[e].base.rep));
  const nearW = g => Math.abs(g - 0.25) < 0.002, verdW = g => (g <= 0.25 ? 'at or below 0.25' : 'above 0.25') + (nearW(g) ? ' (on the line: within 0.002)' : '');
  const V52M = [['fpl', 1, 'p'], ['fplX', 1, 'p'], ['bO', 1, 'p'], ['bN', 1, 'p'], ['f0', 1, 'p'], ['pov', 1, 'p'], ['ep', 2, 'p'], ['giniD', 3, 'g'], ['giniX', 3, 'g'], ['giniW', 3, 'w']];
  const v52Cell = (x, bx, d, kind) => (+x).toFixed(d) + (kind === 'p' ? '%' : '') + (kind === 'p' ? (x < 2 ? 'met' : 'not met') : kind === 'g' ? verd(x) : verdW(x)) + 'no programme ' + (+bx).toFixed(d) + (kind === 'p' ? '%' : '');
  if (V52) [[20, emb20], [40, emb40]].forEach(([yrs, Pn]) => ENVN.forEach(e => { wr.relSet(e); wr.relYears(yrs); const E = Pn.envs[e], b = E.base.rep, r = E.rows.release.rep, el = dr.getElementById('rel-targets'), tr = el ? [...el.querySelectorAll('tbody tr')].map(x => [...x.children].map(c => c.textContent)) : [], tx = el ? el.textContent : '';
    const okRows = tr.length === V52M.length && tr.every((c, i) => { const m = V52M[i]; return c.length === 4 && c[2] === v52Cell(r.y7[m[0]], b.y7[m[0]], m[1], m[2]) && c[3] === v52Cell(r.end[m[0]], b.end[m[0]], m[1], m[2]) && (m[2] === 'p' ? c[1] === 'under 2%' : m[2] === 'g' ? c[1] === '0.25 to 0.30' : c[1] === '0.25 (BLEI paper)'); });
    const a = el ? el.querySelector('a') : null;
    if (!(okRows && /Year 7/.test(tx) && /official poverty line/.test(tx) && /\$16,749 in 2025/.test(tx) && a && a.getAttribute('href') === 'https://bettertobest.github.io/research-hub/integrated-implementation-roadmap.html' && /Integrated Implementation Roadmap/.test(tx) && /starts from 0\.22% at year 0 by construction/.test(tx) && /small sample \(×500\/499\)/.test(tx) && new RegExp('Year ' + yrs).test(tx))) tb.push(e + ' ' + yrs + 'y'); }));
  else [[20, emb20], [40, emb40]].forEach(([yrs, Pn]) => ENVN.forEach(e => { wr.relSet(e); wr.relYears(yrs); const E = Pn.envs[e], b = E.base, r = E.rows.release, el = dr.getElementById('rel-targets'), tr = el ? [...el.querySelectorAll('tbody tr')].map(x => [...x.children].map(c => c.textContent)) : [], tx = el ? el.textContent : '';
    const want = [['fgt0PY', 1], ['bOAPy', 1], ['pov', 1], ['epPY', 2]].map(q => [(+b[q[0]]).toFixed(q[1]) + '%', (+r[q[0]]).toFixed(q[1]) + '%', r[q[0]] < 2 ? 'met' : 'not met']).concat([['giniD', 'giniD'], ['giniX', 'giniX']].map(q => [(+b[q[0]]).toFixed(3), (+r[q[0]]).toFixed(3), verd(r[q[0]])]));
    const okRows = tr.length === 6 && tr.every((c, i) => c.length === 4 && c[2] === want[i][0] && c[3] === want[i][1] + want[i][2] && (i < 4 ? c[1] === 'under 2%' : c[1] === '0.25 to 0.30'));
    const a = el ? el.querySelector('a') : null;
    if (!(okRows && /Year 7/.test(tx) && a && a.getAttribute('href') === 'https://bettertobest.github.io/research-hub/integrated-implementation-roadmap.html' && /Integrated Implementation Roadmap/.test(tx) && /starts from 0\.22% at year 0 by construction/.test(tx) && new RegExp('by year ' + yrs).test(tx))) tb.push(e + ' ' + yrs + 'y'); }));
  wr.relYears(20); wr.relSet('ref');
  const tgRows = [...repDoc.querySelectorAll('[data-table="rel-tg"] tbody tr')].map(x => [...x.children].map(c => c.textContent.replace(/\s+/g, ' ')));
  const fxJ = (x, d) => (+x).toFixed(d), repCell = (x, bx, d, kind) => fxJ(x, d) + (kind === 'p' ? '%' : '') + ' vs ' + fxJ(bx, d) + (kind === 'p' ? '%' : '') + (kind === 'p' ? (x < 2 ? 'met' : 'not met') : kind === 'g' ? verd(x) : verdW(x));
  const tgOK = V52 ? (tgRows.length === 6 * V52M.length && [[20, P20], [40, P40]].every(([yrs, Pn], yi) => ENVN.every((e, ei) => V52M.every((m, mi) => { const c = tgRows[(yi * 3 + ei) * V52M.length + mi], b = Pn.envs[e].base.rep, r = Pn.envs[e].rows.release.rep;
    return c && +c[0] === yrs && c[4] === repCell(r.y7[m[0]], b.y7[m[0]], m[1], m[2]) && c[5] === repCell(r.end[m[0]], b.end[m[0]], m[1], m[2]); }))))
    : tgRows.length === 6 && [[20, P20], [40, P40]].every(([yrs, Pn], yi) => ENVN.every((e, ei) => { const c = tgRows[yi * 3 + ei], b = Pn.envs[e].base, r = Pn.envs[e].rows.release;
    return c && +c[0] === yrs && c[2] === r.fgt0PY.toFixed(1) + '% vs ' + b.fgt0PY.toFixed(1) + '%' && c[3] === r.bOAPy.toFixed(1) + '% vs ' + b.bOAPy.toFixed(1) + '%' && c[4] === r.pov.toFixed(1) + '% vs ' + b.pov.toFixed(1) + '%' && c[5] === r.epPY.toFixed(2) + '% vs ' + b.epPY.toFixed(2) + '%' &&
      c[6].indexOf(r.giniD.toFixed(3) + ' vs ' + b.giniD.toFixed(3)) === 0 && c[6].indexOf(verd(r.giniD)) > 0 && c[7].indexOf(r.giniX.toFixed(3) + ' vs ' + b.giniX.toFixed(3)) === 0 && c[7].indexOf(verd(r.giniX)) > 0; }));
  check('audit E1 (v5.1): the Hub\'s Year 7 targets (poverty under 2%, Gini 0.25 to 0.30) are shown against the model\'s results on the front door for every environment and horizon, with the source named and linked, the panel\'s own numbers and the right verdicts, and on the findings explorer for all six combinations',
    keysOK && tb.length === 0 && tgOK, 'front door ' + (tb.length ? 'WRONG: ' + tb.join(', ') : 'ok in 6 views') + '; explorer table ' + (tgOK ? 'matches the panels' : 'DIFFERS') + '; Gini (cash / with price cuts), release row: ' + [[20, P20], [40, P40]].map(([y, Pn]) => y + 'y ' + ENVN.map(e => Pn.envs[e].rows.release.giniD.toFixed(3) + '/' + Pn.envs[e].rows.release.giniX.toFixed(3)).join(' ')).join('; '));
  /* v5.2 round, step 8: the year-by-year charts and what a month still buys. A panel whose rows carry .path (v5.2) gets three small charts (cost-of-living poverty, median savings,
   * what a month of the wage and of the BU buys), no programme beside Compassionism, each with a title and a text description, and a table of the numbers; the Prices
   * sentence says what a month of the median wage and of the BU buys at the last year, from the same path. A panel without .path (v5.1) shows no charts. */
  const PATH = [emb20, emb40].every(Pn => ENVN.every(e => Pn.envs[e].rows.release.path && Pn.envs[e].base.path)), pathBad = [];
  [[20, emb20], [40, emb40]].forEach(([yrs, Pn]) => ENVN.forEach(e => { wr.relSet(e); wr.relYears(yrs); const E = Pn.envs[e], el = dr.getElementById('rel-paths'), svg = el ? [...el.querySelectorAll('svg.fd-pc')] : [];
    if (!PATH){ if (el) pathBad.push(e + ' ' + yrs + 'y charts without a path'); return; }
    const P = E.rows.release.path, B = E.base.path, n = Math.min(yrs, P.f0.length) - 1, t = prices(e, yrs), money = x => wr.fdMoney(x);
    const titled = svg.length === 3 && svg.every(g => g.querySelector('title') && g.querySelector('desc') && /year 1/.test(g.querySelector('desc').textContent) && g.querySelectorAll('polyline').length >= 2);
    const tbl = el.querySelector('table.fd-pt'), cells = tbl ? tbl.querySelectorAll('tbody tr').length : 0;
    const buys = E.rows.release.infl > 0 ? t.indexOf('a month of the median wage buys what ' + money(P.wageR[n]) + ' bought at the start') > 0 && t.indexOf('with no programme ' + money(B.wageR[n])) > 0 : true;
    if (!(titled && cells === 7 && buys)) pathBad.push(e + ' ' + yrs + 'y (charts ' + svg.length + ', titled ' + titled + ', table rows ' + cells + ', purchasing power ' + buys + ')'); }));
  wr.relYears(20); wr.relSet('ref');
  check('v5.2 step 8: year-by-year charts (cost-of-living poverty, savings, what a month buys) beside no programme in every view, each described in text with a table of the numbers, and the Prices sentence says what a month of the wage and of the BU still buys' + (PATH ? '' : ' (the embedded panels predate the path: no charts shown)'),
    pathBad.length === 0, pathBad.length ? pathBad.slice(0, 4).join('; ') : (PATH ? '6 views' : 'v5.1 panels: none shown'));
  /* (c) the Gini formula's small-sample bias (n/(n-1) with n adults) may change a verdict only where the table labels the reading as on the line (within 0.002 of it) */
  const flips = [], unlabelled = [], onLine = [];
  /* v5.2: with the correction applied (the panel's _meta.v52.report.giniNN1), the other reading is the uncorrected one, g x (n - 1)/n; the wealth Gini (line 0.25) is checked the same way */
  [[20, P20], [40, P40]].forEach(([yrs, Pn]) => { const n = Pn._meta.agents, nn1 = !!(Pn._meta.v52 && Pn._meta.v52.report && Pn._meta.v52.report.giniNN1), other = g => nn1 ? g*(n - 1)/n : g*n/(n - 1);
    ENVN.forEach(e => { [['base', Pn.envs[e].base], ['release', Pn.envs[e].rows.release]].forEach(([nm, r]) => {
      ['giniD', 'giniX'].forEach(q => { const g = r[q], c = other(g), tag = yrs + 'y ' + e + ' ' + nm + ' ' + q + ' ' + g.toFixed(4);
        if (nearL(g)) onLine.push(tag); if (plainV(g) !== plainV(c)) { flips.push(tag + ' (' + (nn1 ? 'uncorrected ' : 'corrected ') + c.toFixed(4) + ')'); if (!nearL(g)) unlabelled.push(tag); } });
      if (r.rep) ['y7', 'end'].forEach(t => [['giniD', nearL, plainV], ['giniX', nearL, plainV], ['giniW', nearW, g => g <= 0.25 ? 'low' : 'high']].forEach(([q, nr, pv]) => { const g = r.rep[t][q], c = other(g), tag = yrs + 'y ' + e + ' ' + nm + ' ' + t + ' ' + q + ' ' + g.toFixed(4);
        if (nr(g)) onLine.push(tag); if (pv(g) !== pv(c)) { flips.push(tag + ' (' + (nn1 ? 'uncorrected ' : 'corrected ') + c.toFixed(4) + ')'); if (!nr(g)) unlabelled.push(tag); } })); }); }); });
  check('audit E1 (v5.1; v5.2 applies the correction): the small-sample bias of the Gini formula (a factor n/(n-1), 0.2% at 500 adults) changes a verdict in the table only where the reading is labelled as on the line',
    unlabelled.length === 0, unlabelled.length ? 'UNLABELLED FLIPS: ' + unlabelled.join('; ') : (flips.length ? 'flips, all labelled on the line: ' + flips.join('; ') : 'no verdict changes') + '; readings labelled on the line: ' + (onLine.length ? onLine.join(', ') : 'none'));
  /* (d) the manifest: every field well formed, shipped panels come from a committed tree, the engine hash is the page's, both panels from one build, the embedded panels equal dev/runs, and (where the commit is in this clone) harness.js at that commit hashes to the recorded value */
  const cp = require('child_process'), page = fs.readFileSync(FILE, 'utf8'), blk = HB.pageEngineBlock(page), blkSha = blk ? HB.sha256Of(blk) : null, hexOK = (x, n) => typeof x === 'string' && new RegExp('^[0-9a-f]{' + n + '}$').test(x);
  const mans = [P20._meta.manifest, P40._meta.manifest], emb = [emb20, emb40], mProb = [];
  /* v5.3 (B2): during a model round the engine gains code that is off by default before the round's new panels are made; a published panel whose engine differs
   * from the page's passes only when dev/runs/engine-lineage.json links the two by recorded proofs (the six 12-seed release panels reproduce the base's fingerprints) */
  const LN = require('./dev/tools/engine_lineage.js'), linkOf = h => h === blkSha ? {ok: true, links: 0} : LN.reaches(h, blkSha); let linkN = 0;
  mans.forEach((m, i) => { const t = i ? '40y' : '20y'; if (!m) { mProb.push(t + ' no manifest'); return; }
    if (!hexOK(m.commit, 40)) mProb.push(t + ' commit'); if (m.dirty !== false) mProb.push(t + ' dirty is ' + m.dirty + ' (a shipped panel must come from a committed tree)'); if (!/^v\d+\.\d+\.\d+$/.test(m.node || '')) mProb.push(t + ' node');
    ['harnessSha256', 'engineBlockSha256', 'indexSha256'].forEach(k => { if (!hexOK(m[k], 64)) mProb.push(t + ' ' + k); }); const lk = linkOf(m.engineBlockSha256); if (!lk.ok) mProb.push(t + ' engine block hash differs from the page\'s and no recorded proof links them (the engine changed after these panels were made: prove it changed no result with dev/tools/engine_lineage.js, or regenerate them)'); else linkN = Math.max(linkN, lk.links);
    if (JSON.stringify(emb[i]._meta.manifest) !== JSON.stringify(m)) mProb.push(t + ' embedded manifest differs from dev/runs'); });
  if (mans[0] && mans[1]) ['commit', 'harnessSha256', 'engineBlockSha256', 'node'].forEach(k => { if (mans[0][k] !== mans[1][k]) mProb.push('the two panels differ in ' + k); });
  const embEq = [[P20, emb20], [P40, emb40]].every(([a, b]) => ENVN.every(e => JSON.stringify(a.envs[e].rows.release) === JSON.stringify(b.envs[e].rows.release) && JSON.stringify(a.envs[e].base) === JSON.stringify(b.envs[e].base)));
  if (!embEq) mProb.push('embedded panels differ from dev/runs');
  let gitNote = 'not checkable here (commit not in this clone)';
  try { const h = cp.execFileSync('git', ['show', mans[0].commit + ':harness.js'], {cwd: root, stdio: ['ignore', 'pipe', 'ignore'], maxBuffer: 64*1024*1024}); if (HB.sha256Of(h) !== mans[0].harnessSha256) mProb.push('harness.js at commit ' + mans[0].commit.slice(0, 8) + ' does not hash to the recorded value'); else gitNote = 'harness.js at commit ' + mans[0].commit.slice(0, 8) + ' hashes to the recorded value'; } catch (e) {}
  check('audit E5 / V5-08 (v5.1): each panel\'s manifest names a commit (clean tree), the Node version and file hashes; the engine hash equals the page\'s (or is linked to it by recorded proofs that no result changed, v5.3), both panels come from one build, and the embedded panels equal the files in dev/runs',
    mProb.length === 0, mProb.length ? mProb.slice(0, 4).join('; ') : 'commit ' + mans[0].commit.slice(0, 8) + ', Node ' + mans[0].node + ', engine block ' + mans[0].engineBlockSha256.slice(0, 12) + (linkN ? ' (the page\'s engine has changed since without changing a result: ' + linkN + ' proven link' + (linkN === 1 ? '' : 's') + ', dev/runs/engine-lineage.json)' : '') + '; ' + gitNote);
  /* v5.1 (audit E4): deep links. ?env=&years= opens that view; anything else is ignored; choosing a view rewrites the address but keeps other keys; the link on the page reopens the same view. */
  const dl = q => { const x = makeWindow(q); x.relInit(); return x; }, pressed = (x, id) => x.document.getElementById(id).getAttribute('aria-pressed') === 'true';
  const wa = dl('?env=adv&years=40'), wb = dl('?env=zzz&years=7'), wc = dl('?bu=900&env=st'); wc.relYears(40);
  const linkA = wa.document.getElementById('rel-link').getAttribute('href'), wd = dl(linkA.replace(/#.*$/, '')), qc = new wc.URLSearchParams(wc.location.search);
  const txtA = (wa.document.getElementById('rel-out') || {}).textContent || '', thA = wa.document.getElementById('rel-th-pov').textContent;
  const dlOK = wa.REL.env === 'adv' && wa.REL.yrs === 40 && pressed(wa, 'rel-env-adv') && !pressed(wa, 'rel-env-ref') && pressed(wa, 'rel-yrs-40') && !pressed(wa, 'rel-yrs-20') && /at year 40/.test(txtA) && thA === 'Too little wealth, year 40' && /env=adv/.test(linkA) && /years=40/.test(linkA) &&
    wb.REL.env === 'ref' && wb.REL.yrs === 20 && pressed(wb, 'rel-env-ref') && pressed(wb, 'rel-yrs-20') && wc.REL.env === 'st' && wc.REL.yrs === 40 && qc.get('bu') === '900' && qc.get('env') === 'st' && qc.get('years') === '40' &&
    wd.REL.env === 'adv' && wd.REL.yrs === 40 && ((wd.document.getElementById('rel-out') || {}).textContent || '') === txtA;
  check('audit E4 (v5.1): ?env=adv&years=40 opens that view (buttons, text and link agree), bad values are ignored, choosing a view rewrites the address and keeps other keys, and the page\'s own link reopens the same view',
    dlOK, 'adv/40: ' + wa.REL.env + '/' + wa.REL.yrs + '; bad values: ' + wb.REL.env + '/' + wb.REL.yrs + '; kept bu=' + qc.get('bu') + ' and now ' + wc.location.search + '; link ' + linkA);
  /* v5.1 (audit E3): the figures on view as a file. JSON and CSV for each of the six views carry the version, the command and the manifest, and every number equals the panel's. */
  const csvRows = t => t.split('\n').filter(l => l && l[0] !== '#').map(l => { const o = []; let cur = '', q = false; for (let i = 0; i < l.length; i++) { const ch = l[i]; if (q) { if (ch === '"' && l[i + 1] === '"') { cur += '"'; i++; } else if (ch === '"') q = false; else cur += ch; } else if (ch === '"') q = true; else if (ch === ',') { o.push(cur); cur = ''; } else cur += ch; } o.push(cur); return o; });
  const exProb = [], REL_ORDER = wr.REL_CSV_ORDER; let exInfo = '';
  [[20, emb20], [40, emb40]].forEach(([yrs, Pn]) => ENVN.forEach(e => { wr.relSet(e); wr.relYears(yrs); const E = Pn.envs[e], jx = wr.relExport('json'), cx = wr.relExport('csv'), tag = e + ' ' + yrs + 'y';
    let J = null; try { J = JSON.parse(jx.text); } catch (x) {}
    if (!J || J._meta.version !== wr.META.VERSION || J._meta.command !== Pn._meta.command || J._meta.years !== yrs || J._meta.environmentKey !== e || JSON.stringify(J._meta.manifest) !== JSON.stringify(Pn._meta.manifest) || JSON.stringify(J.rows) !== JSON.stringify(E.rows) || JSON.stringify(J.base) !== JSON.stringify(E.base) || jx.name !== 'compassionism-v' + wr.META.VERSION + '-' + e + '-' + yrs + 'y.json') exProb.push(tag + ' json');
    const com = cx.text.split('\n').filter(l => l[0] === '#').join('\n'), R = csvRows(cx.text), head = R[0] || [], col = n => head.indexOf(n), body = R.slice(1), rel = body.find(r => r[0] === 'release') || [], base = body.find(r => r[0] === 'no_programme') || [], rr = E.rows.release;
    const nRowsE = 1 + REL_ORDER.filter(k => E.rows[k]).length;  /* v5.2: the readings present in this panel, plus the no-programme row */
    if (!(R.length === nRowsE + 1 && R.every(r => r.length === head.length) && com.indexOf('v' + wr.META.VERSION) > 0 && com.indexOf('Reproduce: ' + Pn._meta.command) > 0 && com.indexOf('commit ' + Pn._meta.manifest.commit) > 0 && cx.name === 'compassionism-v' + wr.META.VERSION + '-' + e + '-' + yrs + 'y.csv')) exProb.push(tag + ' csv shape');
    const eq = (row, c, v) => +row[col(c)] === v;
    if (!(eq(rel, 'too_little_wealth_pct', rr.pov) && eq(rel, 'too_little_wealth_change_lo', rr.dPov[1]) && eq(rel, 'below_30_days_change_hi', rr.dBO[2]) && eq(rel, 'design_neutral_change_pts', rr.dBN[0]) && eq(rel, 'programme_inflation_pct_a_year', rr.infl) && eq(rel, 'price_level_median', rr.pLevEndMed) && eq(rel, 'price_level_p90', rr.pLevEndP90) &&
      eq(rel, 'cost_per_adult_a_year_usd', rr.cost) && eq(rel, 'gini_disposable_income', rr.giniD) && eq(rel, 'unhoused_pct', rr.epPY) && eq(base, 'too_little_wealth_pct', E.base.pov) && eq(base, 'gini_with_price_cuts', E.base.giniX) && base[col('below_30_days_change_pts')] === '' && body.length === nRowsE && body[1][0] === 'release')) exProb.push(tag + ' csv numbers');
    if (rr.rep && !(eq(rel, 'below_official_poverty_line_year7_pct', rr.rep.y7.fpl) && eq(rel, 'gini_wealth_last_year', rr.rep.end.giniW) && eq(base, 'below_official_poverty_line_last_year_pct', E.base.rep.end.fpl) && eq(base, 'too_little_wealth_fixed_dollar_line_last_year_pct', E.base.rep.end.povNom))) exProb.push(tag + ' csv v5.2 columns');  /* v5.2 step 2 */
    exInfo = jx.text.length + ' + ' + cx.text.length + ' characters (last view)'; }));
  const clicked = [], wdl = makeWindow(); wdl.relInit(); wdl.URL.createObjectURL = () => 'blob:test'; wdl.URL.revokeObjectURL = () => {}; wdl.HTMLAnchorElement.prototype.click = function () { clicked.push(this.download + ' ' + this.getAttribute('href')); };
  wdl.relSet('adv'); wdl.relYears(40); const wired = ['csv', 'json'].every(f => wdl.document.getElementById('rel-dl-' + f).getAttribute('onclick') === "relDownload('" + f + "')" && wdl.document.getElementById('rel-dl-' + f).tagName === 'BUTTON'); wdl.relDownload('csv'); wdl.relDownload('json');  // the page's inline onclick handlers do not run under jsdom's outside-only scripts, so the functions they name are called directly
  const btnOK = wired && clicked.length === 2 && clicked[0] === 'compassionism-v' + wdl.META.VERSION + '-adv-40y.csv blob:test' && clicked[1] === 'compassionism-v' + wdl.META.VERSION + '-adv-40y.json blob:test';
  check('audit E3 (v5.1): "Download this view" gives a CSV and a JSON for each of the six views, with the version, the command, the build manifest and every number equal to the panel\'s, and the buttons download the right file names',
    exProb.length === 0 && btnOK, exProb.length ? exProb.slice(0, 4).join('; ') : '6 views x 2 formats match the panels (' + exInfo + '); buttons: ' + clicked.join(' | '));
  /* v5.1 (audit E2): the backing-share chart on the replication page is the data in dev/runs/backing-share.json: two panels (never one chart with two y axes), three series each, five points each; the table
   * view carries every number; both end points equal the panel's own release and H1 rows (same paired seeds, same build of the engine); inflation falls as more is backed; and the manifest names a clean commit and the page's engine. */
  const BS = JSON.parse(fs.readFileSync(path.join(root, 'dev', 'runs', 'backing-share.json'), 'utf8')), BK = ['a0', 'a25', 'a50', 'a75', 'a100'], bsProb = [];
  const bsFig = repDoc.getElementById('backing-chart'), bsSvgs = bsFig ? [...bsFig.querySelectorAll('svg.fx-svg')] : [], bsTab = [...repDoc.querySelectorAll('[data-table="bs"] tbody tr')].map(x => [...x.children].map(c => c.textContent));
  const sgn = (x, d) => { const t = Math.abs(x).toFixed(d === undefined ? 1 : d); return (x > 0 && +t !== 0 ? '+' : x < 0 && +t !== 0 ? '−' : '') + t; };
  if (bsSvgs.length !== 2 || !bsSvgs.every(sv => sv.getAttribute('role') === 'img' && /backed share|by backed share/.test(sv.getAttribute('aria-label') || '') && sv.querySelectorAll('path.fx-line').length === 3 && sv.querySelectorAll('.fx-mk').length >= 15)) bsProb.push('chart structure');
  if (!bsFig || ['Reference', 'Adverse', 'Stress Test'].some(n => (bsFig.querySelector('.fx-legend') || {textContent: ''}).textContent.indexOf(n) < 0)) bsProb.push('legend');
  if (BS._meta.seeds !== 500 || BS._meta.years !== 20 || JSON.stringify(BS._meta.shares) !== '[0,0.25,0.5,0.75,1]') bsProb.push('meta');
  if (bsTab.length !== 5) bsProb.push('table rows'); else BK.forEach((k, i) => { const c = bsTab[i], e3 = ENVN.map(e => BS.envs[e].rows[k]);
    const okRow = c[1] === e3[0].a.toFixed(2) && ENVN.every((e, j) => c[2 + j] === sgn(e3[j].dPov[0]) + ' (' + sgn(e3[j].dPov[1]) + ' to ' + sgn(e3[j].dPov[2]) + ')' && c[5 + j] === e3[j].infl.toFixed(1) + '%') && c[0] === (k === 'a0' ? 'Release row' : k === 'a100' ? 'H1' : '');
    if (!okRow) bsProb.push('table row ' + k); });
  ENVN.forEach(e => { const R = BS.envs[e].rows, pr = P20.envs[e].rows, same = (a, b) => ['pov', 'fgt0PY', 'bOAPy', 'bNAPy', 'infl', 'pLevEnd', 'pLevEndMed', 'pLevEndP10', 'pLevEndP90', 'cost', 'srcPay', 'srcM'].every(q => a[q] === b[q]);
    if (!same(R.a0, pr.release)) bsProb.push(e + ' a=0 is not the release row'); if (!same(R.a100, pr.h1)) bsProb.push(e + ' a=1 is not the H1 row');
    for (let i = 1; i < BK.length; i++) if (R[BK[i]].infl > R[BK[i - 1]].infl + 1e-9) bsProb.push(e + ' inflation rises with the backed share'); if (R.a100.infl !== 0) bsProb.push(e + ' programme inflation at a=1 is not zero'); });
  const bm = BS._meta.manifest || {}, bl = linkOf(bm.engineBlockSha256); if (!hexOK(bm.commit, 40) || bm.dirty !== false || !bl.ok) bsProb.push('manifest (commit ' + (bm.commit || '?').slice(0, 8) + ', dirty ' + bm.dirty + ', engine ' + (bm.engineBlockSha256 === blkSha ? 'equals the page\'s' : bl.ok ? 'linked to the page\'s' : 'DIFFERS, no recorded proof links it to the page\'s') + ')');  /* v5.3 (B2): or linked by proofs (dev/runs/engine-lineage.json) */
  check('audit E2 (v5.1; on the findings explorer since v5.2.1): the backing-share chart is the 500-seed data (two charts of three series and five points, the table carries every number), its end points are the release and H1 rows exactly, inflation falls as more is backed, and its manifest names a clean commit and the page\'s engine (or one linked to it by recorded proofs, v5.3)',
    bsProb.length === 0, bsProb.length ? bsProb.slice(0, 5).join('; ') : 'a = 0, 0.25, 0.5, 0.75, 1 in three environments; commit ' + bm.commit.slice(0, 8) + '; Adverse change in wealth poverty ' + BK.map(k => sgn(BS.envs.adv.rows[k].dPov[0])).join(' / ') + ' points');
  const wn = makeWindow('', {noChart: true, page: 'early'});  /* v5.2 step 8: an earlier-engine run, on its page */
  let ok = true, why = '';
  try { wn.applyPreset('reference'); wn.runSim(); } catch (e) { ok = false; why = e.message; }
  const note = !!(wn.Chart && wn.Chart.__missing === true);  /* v5.2 step 8: the earlier engine's page has no other .fd-note to find before the note is added */
  wn.document.dispatchEvent(new wn.Event('DOMContentLoaded'));
  const noteShown = [...wn.document.querySelectorAll('p.fd-note[role="status"]')].some(n => /did not load/.test(n.textContent));
  const t0 = Date.now(), iv = setInterval(function () {
    const st = ((wn.document.querySelector('.status-bar') || {}).textContent || '');
    if (/Complete/.test(st) || Date.now() - t0 > 90000) { clearInterval(iv);
      check('audit finding 2: with Chart.js missing the page loads, shows the charts note, and an earlier-engine run completes (it used to stall at "year 20 of 20…100%")',
        ok && !!note && noteShown && /Complete/.test(st), 'start ok ' + ok + (why ? ' (' + why + ')' : '') + '; Chart fallback ' + !!note + '; note shown ' + noteShown + '; status "' + st.replace(/\s+/g, ' ').slice(0, 50) + '"');
      phase14(done); } }, 500);
}

/* ── Phase 14 (v5.2.1, Oct 6, 2026; ledger s90 and s94): every figure on the pages equals the release data. The simulation page's guided sections, the findings
 * explorer and the replication page's summary print every number from the release data file (data/releases/v<version>.json) with its path; dev/tools/check_figures.js
 * checks the list of releases against the files, the files against the 500-seed panels, every number on the three pages (static and rendered, every view and release)
 * against the data, that no figure is typed into the new sections, that every v5.2 anchor still exists, and that the generator's output is current. */
function phase14(done) {
  console.log('\n--- Phase 14: every figure on the pages equals the release data (v5.2.1) ---');
  require(path.join(path.dirname(FILE), 'dev', 'tools', 'check_figures.js')).run().then(r => { r.forEach(x => check(x.name, x.pass, x.detail));
    /* v5.2.2 (audit A2, Muse F2): retired claims (dev/tools/check_stale_claims.js lists each one, the version that retired it and what is true now) must not
     * come back to a public page: the pages' visible text and their scripts' strings, the release data, README and the walk-through script. */
    const sc = require(path.join(path.dirname(FILE), 'dev', 'tools', 'check_stale_claims.js')).run();
    check('v5.2.2 (audit A2): no retired claim reappears on a public page (dev/tools/check_stale_claims.js; the replication page\'s version history and the notes headed as describing the v4.22 engine are history and skipped)', sc.pass,
      sc.pass ? sc.claims + ' retired claims, ' + sc.files + ' files' : sc.hits.slice(0, 4).join('; '));
    done(); })
    .catch(e => { check('v5.2.1: the figure check runs', false, String(e && e.stack || e).slice(0, 300)); done(); });
}
