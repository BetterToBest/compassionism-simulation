#!/usr/bin/env node
/* Audit E2 follow-up (v5.1, Oct 3, 2026): why the right end of the backing-share curve bends in the Adverse Environment and the Stress Test.
 *
 * In those environments outside inflation is 2% a year. The model indexes the BU to prices only in a year when the headline rate passes 5% (CFG.COLA_HUB_THRESH, the Hub's Inflation Surge
 * Protocol). At a = 1 (every Source dollar backed by new output) the programme adds no inflation of its own, so the headline rate stays at 2%, the BU is never indexed, and it loses real value;
 * at a = 0.75 the programme's own inflation (about 11% a year) keeps the trigger on. This reruns a = 0.75 and a = 1 with the trigger as modelled and with the BU indexed every year
 * (the engine's "COLA continuous" alternative, threshold -1), on seeds 1-500, to show how much of the bend that rule accounts for. It changes nothing in any shipped figure: the constant is restored.
 *
 * Usage: node dev/tools/cola_check.js [adv|st]   (writes dev/runs/cola-check-ENV.json; dev/tools/backing_chart.py merges them into the chart's caption) */
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const env = process.argv[2] || 'adv', NAME = {adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
if (!NAME) { console.error('environment must be adv or st (Reference has no outside inflation, so the rule never binds)'); process.exit(1); }
const N = 500, SC = H.SPEND_SOURCED, orig = H.CFG.COLA_HUB_THRESH, svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G);
const out = {_meta: {what: 'a = 0.75 and a = 1 with the BU indexed only above 5% a year (as modelled) and indexed every year', env, seeds: N, years: 20, manifest: H.runManifest(), command: 'node dev/tools/cola_check.js ' + env}, rows: {}};
try {
  [['modelled', orig], ['every_year', -1]].forEach(function (t) {
    H.CFG.COLA_HUB_THRESH = t[1];
    const P = Object.assign({}, H[NAME]), PR = H.tbPresets(P), shares = [0.75, 1];
    const cfg = [{p: PR.baseline(), sc: SC}].concat(shares.map(a => H.n1Row(PR, 'framework', Object.assign({fin: 'source', a: a, jn: {}, cs: {}, sc: SC}, H.REL_V5))));
    const R = H.tbStudy(cfg, N, P, {fin: 'tax', aT: 0, a: 0, X: 0, sc: SC}), B = R[0];
    shares.forEach(function (a, i) { const r = R[i + 1], d = H.tbDiff(r, B, 'pov'), f = H.tbDiff(r, B, 'fgt0PY');
      out.rows[t[0] + '_a' + Math.round(a * 100)] = {rule: t[0], a: a, cost: Math.round(r.cost), fgt0PY: +r.fgt0PY.toFixed(1), bOAPy: +r.bOAPy.toFixed(1), pov: +r.pov.toFixed(1), infl: +(r.endoAnn * 100).toFixed(1),
        dPov: [+d.m.toFixed(2), +d.lo.toFixed(2), +d.hi.toFixed(2)], dF0: [+f.m.toFixed(2), +f.lo.toFixed(2), +f.hi.toFixed(2)]}; });
  });
} finally { H.CFG.COLA_HUB_THRESH = orig; H.resetNR6(svN); H.tbSetG(svG); }
const file = path.join(__dirname, '..', 'runs', 'cola-check-' + env + '.json');
fs.writeFileSync(file, JSON.stringify(out, null, 1));
Object.keys(out.rows).forEach(k => { const r = out.rows[k]; console.log(env, k, 'cost', r.cost, 'cost-of-living poverty', r.fgt0PY, 'BLEI', r.bOAPy, 'wealth poverty', r.pov, 'change vs none', r.dPov[0], 'inflation', r.infl); });
console.log('wrote ' + file);
