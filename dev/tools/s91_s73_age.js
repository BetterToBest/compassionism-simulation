#!/usr/bin/env node
/* S91 (Nov 18, 2026): S73's pilot ageing rows rerun on the fixed engine (research-update PLAN.md S91; dev/DECISIONS.md "S91").
 * The rows are built exactly as dev/tools/s73_pilot.js builds them (agL0, agP, agS x none, rel, c22; the same keys) and spliced into a copy of the
 * published pilot file, so dev/tools/s73_table.js can rebuild the tables. Only the ageing rows with the flows (agP, agS) can move: the fix touches only an
 * adult drawn out of the labour force at entry who later returns (lf.fl), and agL0 has no flows.
 * Usage: node dev/tools/s91_s73_age.js ENV SEEDS PUBLISHED_DIR OUTDIR    writes OUTDIR/s73-pilot-ENV.json */
'use strict';
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const E = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}, [env, Ns, PUB, OUT] = process.argv.slice(2), N = +Ns;
if (!E[env] || !(N > 0) || !PUB || !OUT) { console.error('usage: s91_s73_age.js ENV SEEDS PUBLISHED_DIR OUTDIR'); process.exit(1); }
const svS = H.startRelease(), t0 = Date.now();
try {
  const P = Object.assign({}, H[E[env]], {years: 20, nAgents: 500});
  const row = (d, lf, x) => { const c = H.r2MainPair(P, d === 'none' ? 'c22' : d)[d === 'none' ? 0 : 1]; c.lf = Object.assign({}, lf); if (x) x(c); return c; };
  const ag = c => { c.ag = {}; }, L0 = {}, M = {fl: 'stock', pm: 0.43}, L = [];
  [['agL0', L0], ['agP', {fl: 'panel', pm: 0.43}], ['agS', M]].forEach(v => ['none', 'rel', 'c22'].forEach(d => L.push([v[0] + ' ' + d, row(d, v[1], ag)])));
  const K = H.LF_KEYS.concat(H.LF_FLOW_KEYS, ['fgt0PY', 'pov', 'hrs', 'E', 'E0', 'emp', 'zero', 'endoAnn', 'tauMean', 'finGapSh', 'cost', 'gvTax', 'gvPay', 'wyF0PY'], Array.from({length: 20}, (_, t) => 'ppov_' + t));
  const pick = r => Object.fromEntries(K.map(k => [k, r._s[k] ? Array.from(r._s[k]) : null]));
  const R = H.tbStudy(L.map(x => x[1]), N, P, H.r2MainStudy());
  const J = JSON.parse(fs.readFileSync(path.join(PUB, 's73-pilot-' + env + '.json'), 'utf8'));
  if (J.seeds !== N) throw new Error('the published file has ' + J.seeds + ' seeds, not ' + N);
  const moved = [];
  L.forEach((x, i) => { const r = J.rows.find(q => q.row === x[0]); if (!r) throw new Error('row ' + x[0] + ' not in the published file'); const s = pick(R[i]);
    if (JSON.stringify(s) !== JSON.stringify(r.s)) moved.push(x[0]); r.s = s; });
  J.s91 = {what: 'S91: the ageing rows rerun on the fixed engine and spliced in; every other row is the published S73 pilot', rerun: L.map(x => x[0]), moved,
    manifest: H.runManifest(), command: 'node dev/tools/s91_s73_age.js ' + process.argv.slice(2).join(' '), secs: (Date.now() - t0)/1000};
  fs.mkdirSync(OUT, {recursive: true});
  fs.writeFileSync(path.join(OUT, 's73-pilot-' + env + '.json'), JSON.stringify(svS.withSettings(J)));
  console.log(env + ': moved ' + (moved.join(', ') || 'none') + ' (' + J.s91.secs.toFixed(0) + ' s)');
} finally { svS.restore(); }
