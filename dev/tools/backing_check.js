#!/usr/bin/env node
/* v5.2 round, step 6 (Oct 5, 2026; ledger s85; decision B): the sweep behind the middle backing reading and the spending layer in normal years.
 * Runs the release row on paired seeds with:
 *  - the middle backing reading at caps of 4%, 8%, 12%, 16% and 24% of the year's earned income (new output backs the Source's net payout up to the cap;
 *    12% and 16% are the Kenya study's two-year rollout and peak year, 8% is all of the US's underused labour (BLS U-6, 2025), 24% is the Kenya study's
 *    whole two-year rollout absorbed in one year, and 4% is half of U-6; the two ends, no backing and full backing (H1), are the release row and H1);
 *  - the spending layer in normal years, with idle labour of 1.1% of wages (U-6 above its lowest annual level) and 8% (all of U-6), at normal-times
 *    multipliers of 0.3, 0.6 (the main reading) and 1.0;
 *  - the middle reading and the normal-times layer together.
 * Each row is compared with no programme on the same seeds. Writes dev/runs/backing-check-ENV.json; the figures in dev/DECISIONS.md (step 6) come from it.
 *
 * Usage: node dev/tools/backing_check.js ENV [SEEDS] [YEARS]   (ENV ref, adv or st; default 200 seeds, 20 years) */
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const env = process.argv[2] || 'adv', N = +(process.argv[3] || 200), YRS = +(process.argv[4] || 20), NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
if (!NAME) { console.error('environment must be ref, adv or st'); process.exit(1); }
const C = H.CFG, s1 = +(C.US_UNDERUSE - C.US_UNDERUSE_LOW).toFixed(4);
const ROWS = [['release', {}], ['h1', {a: 1}]]
  .concat([0.04, 0.08, 0.12, 0.16, 0.24].map(k => ['aK' + Math.round(k*100), {aK: k}]))
  .concat([[s1, 'slack'], [C.US_UNDERUSE, 'u6']].reduce((r, s) => r.concat([0.3, C.MULT_NORMAL, 1.0].map(m => [s[1] + '_m' + Math.round(m*10), {ml: {nt: {m: m, s: s[0]}}}])), []))
  .concat([['mid+slack', {aK: C.KENYA_ABSORB_ROLLOUT, ml: {nt: {m: C.MULT_NORMAL, s: s1}}}]]);
const SC = H.SPEND_SOURCED, svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), t0 = Date.now();
const out = {_meta: {what: 'the middle backing reading and the spending layer in normal years, swept (release row, Source financing)', env, seeds: N, years: YRS, manifest: H.runManifest(),
  command: 'node dev/tools/backing_check.js ' + env + ' ' + N + ' ' + YRS, idleMain: s1, idleAll: C.US_UNDERUSE, multNormal: C.MULT_NORMAL}, base: {}, rows: {}};
try {
  const P = Object.assign({}, H[NAME], {years: YRS}), PR = H.tbPresets(P);
  const ALL = Object.assign({fin: 'source', a: 0, jn: {}, cs: {}}, H.REL_V5);
  const cfg = [{p: PR.baseline(), sc: SC}].concat(ROWS.map(r => { const c = H.n1Row(PR, 'framework', Object.assign({}, ALL, r[1])); c.sc = SC; return c; }));
  const R = H.tbStudy(cfg, N, P, {fin: 'tax', aT: 0, a: 0, X: 0, sc: SC}), B = R[0];
  const d3 = (r, k) => { const x = H.tbDiff(r, B, k); return [+x.m.toFixed(2), +x.lo.toFixed(2), +x.hi.toFixed(2)]; };
  out.base = {pov: +B.pov.toFixed(2), fgt0PY: +B.fgt0PY.toFixed(2), bOAPy: +B.bOAPy.toFixed(2)};
  ROWS.forEach((row, i) => { const r = R[i + 1];
    out.rows[row[0]] = {pov: +r.pov.toFixed(2), fgt0PY: +r.fgt0PY.toFixed(2), bOAPy: +r.bOAPy.toFixed(2), infl: +(r.endoAnn*100).toFixed(2), pLevEndMed: +H.quantileOf(r._s.pLev20, 0.5).toFixed(3),
      cost: Math.round(r.cost), bkA: +r.bkA.toFixed(2), bkPY: +r.bkPY.toFixed(2), mlNT: Math.round(r.mlNT), dPov: d3(r, 'pov'), dF0: d3(r, 'fgt0PY'), dBO: d3(r, 'bOAPy')};
    const o = out.rows[row[0]];
    console.log(env, row[0].padEnd(10), 'too little wealth', o.pov, '(' + o.dPov[0] + ')', 'cost of living', o.fgt0PY, '(' + o.dF0[0] + ')', 'BLEI', o.bOAPy, '(' + o.dBO[0] + ')', 'inflation', o.infl + '%', 'backed', o.bkA + '%', 'payout', o.bkPY + '% of earned income', 'wages added $' + o.mlNT, 'cost $' + o.cost); });
} finally { H.resetNR6(svN); H.tbSetG(svG); }
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const file = path.join(__dirname, '..', 'runs', 'backing-check-' + env + '.json');
fs.writeFileSync(file, JSON.stringify(out, null, 1));
console.log('no programme: too little wealth', out.base.pov, 'cost of living', out.base.fgt0PY, 'BLEI', out.base.bOAPy);
console.log('wrote ' + file + ' (' + out._meta.seconds + ' s)');
