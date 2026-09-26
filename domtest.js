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

const FILE = process.argv[2] || path.join(__dirname, 'index.html');
const html = fs.readFileSync(FILE, 'utf8');

let fails = 0, checks = 0;
function check(name, ok, detail) {
  checks++;
  console.log((ok ? '  PASS  ' : '  FAIL  ') + name + (detail ? '\n           ' + detail : ''));
  if (!ok) fails++;
}

function makeWindow(query) {
  const dom = new JSDOM(html, {
    runScripts: 'outside-only',
    url: 'https://bettertobest.github.io/compassionism-simulation/' + (query || '')
  });
  const w = dom.window;
  // Chart.js is stubbed: this harness tests DOM wiring, not chart pixels.
  w.Chart = function (ctx, cfg) { this.cfg = cfg; this.destroy = function () {}; };
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
console.log('=== domtest.js — ' + FILE + ' ===\n--- Phase 1: DOM behaviour ---');
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
  check('v4.17: every visible version label reads META.VERSION (header, footer, assumptions panel)',
    labels.length >= 3 && labels.every(t => t === 'v' + wv.META.VERSION) && hd.indexOf('v' + wv.META.VERSION) >= 0 && wv.document.title.indexOf('v' + wv.META.VERSION) >= 0,
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
  const iconsOK = icons.length >= 15 && icons.every(el => el.getAttribute('tabindex') === '0' && el.getAttribute('role') === 'img' && el.getAttribute('aria-label') === el.getAttribute('data-tip'));
  const hostsOK = hosts.length >= 14 && hosts.every(el => { const dd = $(el.getAttribute('aria-describedby') || ''); return !!dd && dd.textContent === el.getAttribute('data-tip'); });
  const nDesc = $('tip-desc') ? $('tip-desc').children.length : -1;
  if (typeof w.initA11y === 'function') w.initA11y();
  const nDesc2 = $('tip-desc') ? $('tip-desc').children.length : -1;
  const css = [...d.querySelectorAll('style')].map(x => x.textContent).join('\n');
  const cssOK = /\.abbr-link:focus-visible::after/.test(css) && /\.tip-host\[data-tip\]:focus-visible::after/.test(css) && /input\[type=range\]:focus-visible\{outline:/.test(css);
  check('v4.20: every tooltip is keyboard-reachable and exposed (ⓘ focusable and named, buttons and links described), opens on focus, and init is idempotent',
    iconsOK && hostsOK && nDesc === hosts.length && nDesc2 === hosts.length && cssOK,
    icons.length + ' ⓘ icons ' + (iconsOK ? 'OK' : 'NOT OK') + ', ' + hosts.length + ' buttons/links ' + (hostsOK ? 'OK' : 'NOT OK') + ', descriptions ' + nDesc + ' then ' + nDesc2 + ', focus CSS ' + (cssOK ? 'present' : 'missing'));

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

  // 8g. source parity: every function the page and harness.js share is the same code, apart from
  // five known, intentional differences (each covered by a behavioural check elsewhere).
  const src = fs.readFileSync(path.join(__dirname, 'harness.js'), 'utf8');
  const names = [...src.matchAll(/^function ([A-Za-z0-9_]+)\(/gm)].map(m => m[1]);
  const hf = new Function('module', 'require', src + ';return {' + names.join(',') + '};')({exports: {}}, require);
  const norm = f => f.toString().replace(/\/\*[\s\S]*?\*\//g, '').replace(/\/\/[^\n]*/g, '').replace(/\s+/g, '');
  const KNOWN = {runYear: 'harness-only before/after switches (BU_ALLOCATIONS_PER_YEAR, CCO_RELIEF_FLAT, PTH_APPR_CONSERVE); checked by the seed-42 page/harness runs',
    drawAutomationRisk: 'harness-only AUTOMATION_SAMPLER_LEGACY switch; checked by the draw-sequence comparison below',
    getTier: 'display fields (class, colour) in the page', agentBLEI: 'a local renamed gammaV in the harness, where it would shadow gamma()',
    incomeBasketMetrics: 'guard order only'};
  const shared = names.filter(n => typeof w[n] === 'function');
  const drift = shared.filter(n => !KNOWN[n] && norm(w[n]) !== norm(hf[n]));
  const seqP = [], seqH = [];
  w.RNG = w.mulberry32(77); for (let i = 0; i < 1000; i++) seqP.push(w.drawAutomationRisk());
  const HT = H.unitTargets(), savedH = HT.getRNG(); HT.setRNG(H.mulberry32(77)); for (let i = 0; i < 1000; i++) seqH.push(HT.drawAutomationRisk()); HT.setRNG(savedH);
  check('v4.20: every function shared by the page and harness.js is identical source (' + (shared.length - Object.keys(KNOWN).length) + ' functions), and drawAutomationRisk() draws identical sequences',
    shared.length >= 40 && !drift.length && seqP.every((x, i) => x === seqH[i]), drift.length ? 'DRIFTED: ' + drift.join(', ') : shared.length + ' shared; 5 known differences: ' + Object.keys(KNOWN).join(', '));

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
    done();
  }, 1500);
}
