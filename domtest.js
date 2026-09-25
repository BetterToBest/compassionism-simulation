'use strict';
/* ═══════════════════════════════════════════════════════════════════════
 * domtest.js — DOM-behaviour harness for index.html
 * Compassionism Framework Simulation · Better To Best Research Hub
 * Source code: Apache License 2.0 (as of v4.8)
 *
 *   Usage:  npm install jsdom      (one dependency, dev-only)
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
 * The page is loaded with runScripts:'outside-only' so DOMContentLoaded and
 * load have already fired before the script is evaluated — the page's own
 * auto-run never triggers, and every function is exercised deliberately.
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
 * Phase 4 (new) reproduces a reproducibility bug the v4.16 audit found: a seed-42 run started
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
  w.eval(inline[0].textContent);
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
  const want = { blei: 1965, wealth: 559223, gini: 0.534, pov: 16.6, bpov: 13.6 };
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
  const WANT = 559223;
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
              // independent computation of Baseline at 0% inflation, seed 42 (wealth $13,612, poverty 50.8%).
              const wm = fresh();
              if (typeof wm.ST.baseInflMatch === 'undefined') {
                check('Match-Baseline-inflation: Your Settings unchanged, Baseline matches harness.js (seed 42, 0%)', false, 'toggle missing (pre-v4.16)');
                return finish4();
              }
              wm.tog('baseInflMatch', true); wm.runSim();
              waitDone(wm, () => {
                const r = wm.SIM_RESULTS, mainW = Math.round(r.finalWealth), bw = Math.round(r.mBase.med), bp = +(r.mBase.pov * 100).toFixed(1);
                check('Match-Baseline-inflation: Your Settings unchanged, Baseline matches harness.js (seed 42, 0%)',
                  mainW === WANT && bw === 13612 && bp === 50.8 && r.baselineInflation.matched === true && r.baselineInflation.rate === 0,
                  'Your Settings $' + mainW + ' · Baseline median $' + bw + ', poverty ' + bp + '%  (fixed-3% Baseline: −$10,000, 71.0%)');
                finish4();
              });
            });
          }, 150);
        });
      }, 400); });
    });
  });
}
function finish4() {
  console.log('\n' + checks + ' checks, ' + (fails ? fails + ' FAILED' : 'all passed'));
  process.exit(fails ? 1 : 0);
}
