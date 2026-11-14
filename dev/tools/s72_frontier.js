#!/usr/bin/env node
/* S72 (Nov 14, 2026): the financing frontier preregistered in research-update prereg/2026-11-s72-government-budget.md. Both designs x the share of the
 * payout the flat contribution is set to raise (0, 0.25, 0.5, 0.75, 1) x its base (wages; wages plus conversion proceeds; all money income) x the rate
 * cap (0.5, 0.7, 0.9); the share-0 cell once per design; each cell with the unpaid part as new money (fx.fin 'money') and borrowed ('debt', main values).
 * D21's row is the cell (1, wages, 0.9). The candidate main row in both runs, 500 adults, 20 years.
 * Usage: node dev/tools/s72_frontier.js ENV SEEDS [OUTDIR]     writes OUTDIR/s72-frontier-ENV.json */
'use strict';
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const E = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}, env = process.argv[2] || 'ref', N = +(process.argv[3] || 20);
const OUT = process.argv[4] || path.join(__dirname, '..', 'runs', 's72-government');
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), t0 = Date.now();
try {
  const P = Object.assign({}, H[E[env]], {years: 20, nAgents: 500});
  const row = (d, f, sh, base, cap) => { const c = H.r2MainPair(P, d === 'none' ? 'c22' : d)[d === 'none' ? 0 : 1]; c.gv = {sh, base};
    if (d !== 'none'){ c.o = Object.assign({}, c.o, {fin: 'tax', tauMax: cap}); c.fx.fin = f; } return c; };
  const L = [{id: 'none', d: 'none', c: row('none', null, 1, 'w', 0.9)}];
  ['rel', 'c22'].forEach(d => ['money', 'debt'].forEach(f => {
    L.push({id: [d, f, 0, '-', '-'].join(' '), d, f, sh: 0, base: '-', cap: '-', c: row(d, f, 0, 'w', 0.9)});
    [0.25, 0.5, 0.75, 1].forEach(sh => ['w', 'wc', 'all'].forEach(base => [0.5, 0.7, 0.9].forEach(cap => L.push({id: [d, f, sh, base, cap].join(' '), d, f, sh, base, cap, c: row(d, f, sh, base, cap)})))); }));
  const K = ['endoAnn', 'tauMean', 'finCapYrs', 'gvPay', 'gvTax', 'gvShR', 'gvDef', 'gvMon', 'gvBor', 'gvInt', 'gvDebtY', 'gvDebtY15', 'gvY100', 'gvRReal', 'gvGuard', 'gvEr',
    'fgt0PY', 'pov', 'wtF0E', 'wtPovE', 'hrs', 'snAll'].concat(Array.from({length: 20}, (_, t) => 'ppov_' + t));
  const R = H.tbStudy(L.map(x => x.c), N, P, H.r2MainStudy());
  fs.mkdirSync(OUT, {recursive: true});
  const res = {env, seeds: N, manifest: H.runManifest(), secs: (Date.now() - t0) / 1000,
    rows: L.map((x, i) => ({id: x.id, d: x.d, f: x.f, sh: x.sh, base: x.base, cap: x.cap, s: Object.fromEntries(K.map(k => [k, R[i]._s[k] ? Array.from(R[i]._s[k]) : null]))}))};
  fs.writeFileSync(path.join(OUT, 's72-frontier-' + env + '.json'), JSON.stringify(res));
  console.log(env + ': done in ' + res.secs.toFixed(0) + ' s');
} finally { H.resetNR6(svN); H.tbSetG(svG); }
