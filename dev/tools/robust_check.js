#!/usr/bin/env node
/* v5.2 round, step 7 (Oct 5, 2026; ledger s86; decision C): the robustness readings on paired seeds, for dev/DECISIONS.md (step 7).
 * Runs the release row and, beside it: landlords raising rents outside PTH ($0.50 per BU dollar spent on rent for tenants paying with BU, Collinson and
 * Ganong 2018; $1.41 for every renter outside PTH, Susin 2002); 5%, 10% and 20% of high conversion rates unearned with audits catching half, and 20% with no
 * audits; the launch gift paid for over the run; and the programme paid for by a flat contribution on wages, a progressive income tax and a land-value
 * tax instead of the Source (the Source pays what a tax cannot). Each row is compared with no programme on the same seeds.
 * Writes dev/runs/robust-check-ENV.json.
 *
 * Usage: node dev/tools/robust_check.js ENV [SEEDS] [YEARS]   (ENV ref, adv or st; default 200 seeds, 20 years) */
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const env = process.argv[2] || 'adv', N = +(process.argv[3] || 200), YRS = +(process.argv[4] || 20), NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
if (!NAME) { console.error('environment must be ref, adv or st'); process.exit(1); }
const KEEP = ['release', 'hcap', 'hcaphi', 'rev5', 'rev10', 'rev20', 'rev20n', 'giftrun', 'tax', 'progtax', 'landtax'];
const SC = H.SPEND_SOURCED, svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), t0 = Date.now();
const out = {_meta: {what: 'the v5.2 robustness readings (release row, Source financing unless stated)', env, seeds: N, years: YRS, manifest: H.runManifest(), command: 'node dev/tools/robust_check.js ' + env + ' ' + N + ' ' + YRS}, base: {}, rows: {}};
try {
  const P = Object.assign({}, H[NAME], {years: YRS}), PR = H.tbPresets(P), rows = H.releaseRows(SC).filter(r => KEEP.indexOf(r.j) >= 0);
  const cfg = [{p: PR.baseline(), sc: SC}].concat(rows.map(r => { const c = H.n1Row(PR, 'framework', r.v); if (r.v.o) Object.assign(c.o || (c.o = {}), r.v.o); c.sc = SC; return c; }));
  const R = H.tbStudy(cfg, N, P, {fin: 'tax', aT: 0, a: 0, X: 0, sc: SC}), B = R[0];
  const d3 = (r, k) => { const x = H.tbDiff(r, B, k); return [+x.m.toFixed(2), +x.lo.toFixed(2), +x.hi.toFixed(2)]; };
  out.base = {pov: +B.pov.toFixed(2), fgt0PY: +B.fgt0PY.toFixed(2), bOAPy: +B.bOAPy.toFixed(2)};
  rows.forEach((row, i) => { const r = R[i + 1];
    out.rows[row.j] = {label: row.l.trim(), pov: +r.pov.toFixed(2), fgt0PY: +r.fgt0PY.toFixed(2), bOAPy: +r.bOAPy.toFixed(2), infl: +(r.endoAnn*100).toFixed(2), cost: Math.round(r.cost),
      hcM: +r.hcM.toFixed(2), rvX: Math.round(r.rvX), rvC: Math.round(r.rvC), taxAvg: +r.taxAvg.toFixed(1), taxCover: r.need > 0 ? +Math.min(100, r.tax/r.need*100).toFixed(1) : null,
      dPov: d3(r, 'pov'), dF0: d3(r, 'fgt0PY'), dBO: d3(r, 'bOAPy')};
    const o = out.rows[row.j];
    console.log(env, row.j.padEnd(8), 'too little wealth', o.pov, '(' + o.dPov[0] + ')', 'cost of living', o.fgt0PY, '(' + o.dF0[0] + ')', 'BLEI', o.bOAPy, '(' + o.dBO[0] + ')', 'inflation', o.infl + '%', 'cost $' + o.cost,
      'rent +' + o.hcM + '%', 'unearned $' + o.rvX, 'clawed back $' + o.rvC, 'tax ' + o.taxAvg + '% of wages, covers ' + o.taxCover + '%'); });
} finally { H.resetNR6(svN); H.tbSetG(svG); }
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const file = path.join(__dirname, '..', 'runs', 'robust-check-' + env + '.json');
fs.writeFileSync(file, JSON.stringify(out, null, 1));
console.log('no programme: too little wealth', out.base.pov, 'cost of living', out.base.fgt0PY, 'BLEI', out.base.bOAPy);
console.log('wrote ' + file + ' (' + out._meta.seconds + ' s)');
