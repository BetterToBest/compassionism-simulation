#!/usr/bin/env node
/* S68 (Nov 14, 2026): the pilot preregistered in research-update prereg/2026-11-s68-financing-identity.md.
 * (A) Financing: the C2.2 design and the release design under each financing reading, with fx.fin 'report' (no figure moves) and 'money' (the capped
 *     contribution's gap is new money). (B) Costs at the within-year price level (o.wy) on the quarterly count of today's rule.
 * The frozen row (frozenRow: today's safety net, CPS earnings), round-2 switches off, 500 adults, 20 years, as audits/2026-11-13-financed-row-check.js.
 * Usage: node dev/tools/s68_pilot.js ENV SEEDS [OUTDIR]     ENV ref | adv | st; writes OUTDIR/s68-ENV.json (per-seed values of every key read) */
'use strict';
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const E = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}, env = process.argv[2] || 'ref', N = +(process.argv[3] || 100);
const OUT = process.argv[4] || path.join(__dirname, '..', 'runs', 's68-financing');
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), t0 = Date.now();
try {
  const P = Object.assign({}, H[E[env]], {years: 20, nAgents: 500});
  const SO = Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: H.SPEND_SOURCED}, H.REL_V52_STUDY);
  const pair = () => H.relMainCfgs(H.tbPresets(P)).map(c => { c.sc = H.SPEND_SOURCED; c.sn = {abawd: true, slope: true}; c.lt = {s: 'all', m: 'all'}; return H.frozenRow(c); });
  const row = (d, fin, f) => { const c = d === 'c22' ? H.c22Design(pair()[1]) : d === 'none' ? pair()[0] : pair()[1];
    if (fin) c.o = Object.assign({}, c.o, {fin}); if (f) c.fx = {pthb: true, hb: true, ab: true, sp: true, fin: f}; return c; };
  const A = [['none', row('none', null, 'report')], ['rel source', row('rel', 'source', 'report')], ['c22 source', row('c22', 'source', 'report')],
    ['c22 tax report', row('c22', 'tax', 'report')], ['c22 tax money', row('c22', 'tax', 'money')],
    ['c22 hybrid report', row('c22', 'hybrid', 'report')], ['c22 hybrid money', row('c22', 'hybrid', 'money')],
    ['rel tax report', row('rel', 'tax', 'report')], ['rel tax money', row('rel', 'tax', 'money')]];
  const Q = {q: 4, k: 1, a: 0, r: 0, h: 0, rs: false}, wy = c => { c.pr = Q; c.o = Object.assign({}, c.o, {wy: true}); return c; };
  const B = [['none q4', wy(row('none'))], ['rel q4', wy(row('rel'))], ['c22 q4', wy(row('c22'))]];
  const KA = ['finPay', 'finTax', 'finMoney', 'finMatch', 'finGap', 'finSur', 'finGapM', 'finGapSh', 'finCapYrs', 'tauMean', 'tauLast', 'endoAnn', 'fgt0PY', 'pov', 'hrs', 'cost', 'treas'];
  const KB = ['fgt0PY', 'wyF0PY', 'fgt1PY', 'wyF1PY', 'fgt2PY', 'wyF2PY', 'wyAvg', 'prAvg', 'endoAnn'];
  const RA = H.tbStudy(A.map(x => x[1]), N, P, SO), RB = H.tbStudy(B.map(x => x[1]), N, P, SO);
  const dump = (R, L, K) => L.map((x, i) => ({row: x[0], s: Object.fromEntries(K.map(k => [k, R[i]._s[k] ? Array.from(R[i]._s[k]) : null]))}));
  fs.mkdirSync(OUT, {recursive: true});
  const res = {env, seeds: N, manifest: H.runManifest(), secs: (Date.now() - t0)/1000, A: dump(RA, A, KA), B: dump(RB, B, KB)};
  fs.writeFileSync(path.join(OUT, 's68-' + env + '.json'), JSON.stringify(res));
  console.log(env + ': done in ' + res.secs.toFixed(0) + ' s');
} finally { H.resetNR6(svN); H.tbSetG(svG); }
