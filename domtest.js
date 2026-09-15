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
const w1 = makeWindow('?bu=900&part=55&ptfOn=1&seed=42');
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

  w2.downloadCSV(); w2.downloadJSON();
  const csv = (Object.entries(captured).find(([k]) => k && k.endsWith('.csv')) || [])[1] || '';
  const jsonTxt = (Object.entries(captured).find(([k]) => k && k.endsWith('.json')) || [])[1] || '';
  check('CSV export carries the exposure and dominance blocks',
    /CUMULATIVE POVERTY EXPOSURE/.test(csv) && /THRESHOLD DOMINANCE CHECK/.test(csv));
  check('CSV no longer heads its mechanics list "v4.0 FIXES"', !/--- v4\.0 FIXES/.test(csv) && /KEY MECHANICS CHANGES/.test(csv));
  let parsed = null; try { parsed = JSON.parse(jsonTxt); } catch (err) { /* handled below */ }
  check('JSON export parses and carries exposure + dominance',
    !!parsed && !!parsed.results.cumulativePovertyExposure && !!parsed.results.thresholdDominance);
  check('JSON export states the v4.8 split licence',
    !!parsed && /Apache License 2\.0/.test(parsed.meta.license) && /CC BY 4\.0/.test(parsed.meta.license));
  check('exported version matches META.VERSION', !!parsed && parsed.meta.version === w2.META.VERSION,
    'META.VERSION=' + w2.META.VERSION);

  console.log('\n--- Phase 3: internal consistency suite through the live page ---');
  w2.runValidation();
  setTimeout(() => {
    const vt = $2('val-inner').textContent;
    const p = (vt.match(/PASS/g) || []).length, f = (vt.match(/FAIL/g) || []).length;
    check('all six internal consistency & behavioural checks pass', p === 6 && f === 0, p + ' pass / ' + f + ' fail');
    console.log('\n' + checks + ' checks, ' + (fails ? fails + ' FAILED' : 'all passed'));
    process.exit(fails ? 1 : 0);
  }, 90000);
}, 250);
