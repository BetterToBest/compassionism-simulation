#!/usr/bin/env node
/* v5.2 round, step 3 (Oct 3, 2026): how much of the wealth-poverty gap in the Adverse Environment and the Stress Test (the release row ends with more adults
 * holding too little wealth than no programme) each reading closes: savings that keep up with prices (in both runs; SAVE), the same with no real rate, and the
 * BU indexed every year (row option ci), at the cautious end (the release row) and at H1. A study for the step's note, not the release panel (which is regenerated
 * once, at step 9). It changes no shipped figure.
 *
 * Usage: node dev/tools/save_check.js ENV [SEEDS]   (ENV ref, adv or st; default 200 seeds; writes dev/runs/save-check-ENV.json) */
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const env = process.argv[2] || 'adv', N = +(process.argv[3] || 200), NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
if (!NAME) { console.error('environment must be ref, adv or st'); process.exit(1); }
const SC = H.SPEND_SOURCED, svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), t0 = Date.now();
const out = {_meta: {what: 'wealth-poverty gap closed by savings that keep up with prices and by the BU indexed every year', env, seeds: N, years: 20, manifest: H.runManifest(), command: 'node dev/tools/save_check.js ' + env + ' ' + N}, rows: {}};
try {
  const P = Object.assign({}, H[NAME]), PR = H.tbPresets(P), ALL = Object.assign({fin: 'source', a: 0, jn: {}, cs: {}, sc: SC}, H.REL_V5), W = x => Object.assign({}, ALL, x);
  const ROWS = [['release', W({}), null], ['sav', W({sv: {}}), 'sv'], ['sav0', W({sv: {r: 0}}), 'sv0'], ['idx', W({ci: true}), null], ['h1', W({a: 1}), null], ['h1idx', W({a: 1, ci: true}), null], ['h1sav', W({a: 1, sv: {}}), 'sv'], ['h1both', W({a: 1, sv: {}, ci: true}), 'sv']];
  const BASES = {none: {p: PR.baseline(), sc: SC}, sv: {p: PR.baseline(), sc: SC, sv: {}}, sv0: {p: PR.baseline(), sc: SC, sv: {r: 0}}}, BK = Object.keys(BASES);
  const cfg = BK.map(k => BASES[k]).concat(ROWS.map(r => H.n1Row(PR, 'framework', r[1])));
  const R = H.tbStudy(cfg, N, P, {fin: 'tax', aT: 0, a: 0, X: 0, sc: SC}), B = {}; BK.forEach((k, i) => { B[k] = R[i]; });
  const d3 = (x, y, k) => { const d = H.tbDiff(x, y, k); return [+d.m.toFixed(2), +d.lo.toFixed(2), +d.hi.toFixed(2)]; };
  BK.forEach(k => { out.rows['base_' + k] = {pov: +B[k].pov.toFixed(1), fgt0PY: +B[k].fgt0PY.toFixed(1), bOAPy: +B[k].bOAPy.toFixed(1), svInt: Math.round(B[k].svInt), svIntR: Math.round(B[k].svIntR)}; });
  ROWS.forEach((r, i) => { const x = R[BK.length + i], b = B[r[2] || 'none'];
    out.rows[r[0]] = {vs: r[2] || 'none', pov: +x.pov.toFixed(1), dPov: d3(x, b, 'pov'), fgt0PY: +x.fgt0PY.toFixed(1), dF0: d3(x, b, 'fgt0PY'), bOAPy: +x.bOAPy.toFixed(1), dBO: d3(x, b, 'bOAPy'), infl: +(x.endoAnn * 100).toFixed(1), cost: Math.round(x.cost),
      svInt: Math.round(x.svInt), svIntR: Math.round(x.svIntR), realT: +x.realT.toFixed(3)}; });
  const g0 = out.rows.release.dPov[0];
  ROWS.forEach(r => { const g = out.rows[r[0]].dPov[0]; out.rows[r[0]].gapClosedPct = g0 > 0 ? Math.round((g0 - g) / g0 * 100) : null; });
} finally { H.resetNR6(svN); H.tbSetG(svG); }
out._meta.seconds = Math.round((Date.now() - t0) / 1000);
const file = path.join(__dirname, '..', 'runs', 'save-check-' + env + '.json');
fs.writeFileSync(file, JSON.stringify(out, null, 1));
Object.keys(out.rows).forEach(k => console.log(env, k, JSON.stringify(out.rows[k])));
console.log('wrote ' + file + ' (' + out._meta.seconds + ' s)');
