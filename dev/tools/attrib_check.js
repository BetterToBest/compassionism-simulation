#!/usr/bin/env node
/* v5.3 B9 (Oct 7, 2026; plan item B9; dev/DECISIONS.md Session 39, "B10"): what each part of the design does, on the v5.3 main row, 500 paired seeds.
 * The attribution rows of the v5.3 panel (releaseRowsV53, k 'a') each remove one part; a part's effect is the main row minus the row without it, paired run by
 * run on the same seeds, with a 95% interval (the method of the v4.21 pathway decomposition, harness.js mode 'pathways', now on the release engine). Parts
 * interact, so the single effects need not add up to the whole programme's (the main row against no programme); the gap is reported as the interaction.
 * For each part also: who gains through it (real resources a year by group: participants, non-participants, poorest and richest third by starting wage).
 * Measures: below the cost of living (adult-years), too little wealth at the end, below 30 days of basic living, children below the cost of living, people
 * in households with too little wealth at the end, programme inflation, cost. Diagnostic and the source of the page's "What each part does" (B10).
 * Usage: node dev/tools/attrib_check.js [ENV] [SEEDS] [YEARS]   (ENV ref, adv or st; default ref, 500 seeds, 20 years); writes dev/runs/attrib-check-ENV[-40].json */
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const env = process.argv[2] || 'ref', N = +(process.argv[3] || 500), YRS = +(process.argv[4] || 20), NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
if (!NAME || !(N >= 2) || (YRS !== 20 && YRS !== 40)) { console.error('usage: attrib_check.js ref|adv|st [SEEDS >= 2] [20|40]'); process.exit(1); }
const ROOT = path.join(__dirname, '..', '..'), t0 = Date.now(), SC = H.SPEND_SOURCED, C = H.CFG;
const K = ['fgt0PY', 'pov', 'bOAPy', 'hhCostKidPY', 'hhWlthEnd', 'endoAnn', 'cost', 'gPartRes', 'gNonRes', 'gLowRes', 'gTopRes'];
const wf0 = C.WEALTH_FLOOR; C.WEALTH_FLOOR = -10000;  /* as the testbed command sets it */
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G);
const out = {_meta: {what: 'v5.3 B9: what each part of the design does on the v5.3 main row (main minus the row without it), paired by seed', env, seeds: N, years: YRS,
  manifest: H.runManifest(), command: 'node dev/tools/attrib_check.js ' + env + ' ' + N + ' ' + YRS}, whole: {}, parts: {}, interaction: {}};
try {
  const P = Object.assign({}, H[NAME], {years: YRS}), PR = H.tbPresets(P), rows = H.releaseRowsV53(SC), main = rows.find(r => r.j === 'release'), A = rows.filter(r => r.k === 'a');
  const mk = r => { const c = H.n1Row(PR, 'framework', r.v); if (r.v.o) Object.assign(c.o || (c.o = {}), r.v.o); return c; };
  const cfg = [Object.assign({p: PR.baseline(), sc: SC}, {hh: H.REL_V53.hh, sg: H.REL_V53.sg, g: H.REL_V53.g}), mk(main)].concat(A.map(mk));
  const R = H.tbStudy(cfg, N, P, Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: SC}, H.REL_V52_STUDY)), B = R[0], M = R[1];
  const d = (x, y, k) => { const q = H.tbDiff(x, y, k), f = k === 'endoAnn' ? 100 : 1; return [+(q.m*f).toFixed(3), +(q.lo*f).toFixed(3), +(q.hi*f).toFixed(3)]; };
  K.forEach(k => { out.whole[k] = d(M, B, k); });
  A.forEach((r, i) => { const X = R[i + 2], o = out.parts[r.j] = {label: r.l.trim()}; K.forEach(k => { o[k] = d(M, X, k); }); });
  K.forEach(k => { const sum = A.reduce((s, r) => s + out.parts[r.j][k][0], 0); out.interaction[k] = +(out.whole[k][0] - sum).toFixed(3); });
} finally { H.resetNR6(svN); H.tbSetG(svG); C.WEALTH_FLOOR = wf0; }
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const file = path.join(ROOT, 'dev', 'runs', 'attrib-check-' + env + (YRS === 40 ? '-40' : '') + '.json');
fs.writeFileSync(file, JSON.stringify(out, null, 1) + '\n');
const f = x => (x >= 0 ? '+' : '') + (Math.abs(x) >= 100 ? x.toFixed(0) : x.toFixed(2));
console.log('v5.3 B9 attribution, ' + env + ', seeds 1-' + N + ', ' + YRS + ' years (' + out._meta.seconds + ' s) -> ' + path.relative(ROOT, file));
console.log('the whole programme (main row against no programme): ' + K.map(k => k + ' ' + f(out.whole[k][0])).join('; '));
Object.keys(out.parts).forEach(j => { const o = out.parts[j]; console.log(j.padEnd(8) + ' ' + K.map(k => k + ' ' + f(o[k][0]) + ' [' + f(o[k][1]) + ', ' + f(o[k][2]) + ']').join('; ')); });
console.log('interaction (whole minus the sum of parts): ' + K.map(k => k + ' ' + f(out.interaction[k])).join('; '));
