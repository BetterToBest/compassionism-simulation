#!/usr/bin/env node
/* S7 part 2, item 2 (Nov 15, 2026): saving and spending by income group, on the frozen no-programme row (what the income-graded spending rule does).
 * Same row as dev/tools/s47_spend.js 'frozen' (relMainCfgs(tbPresets(P))[0], frozenRow, CPS yardstick, share as frozen, REL_V52_STUDY; 500 adults, 20 years,
 * Reference environment). Reporting only: the engine is not edited. Per seed, adults are ranked by their disposable income over the 20 years (the s47_spend.js
 * counting: wages + Social Security + transfers + conversion + interest) and split into five equal groups; for each group: income, consumption (own cost less the
 * income-graded cut, plus surplus consumed, less debt written off at the floor), the full cost, all in year-0 dollars. Saving rate = (income - consumption)/income.
 * Usage: node dev/tools/s7_spend_groups.js [--seeds=50] [--procs=4] [--out=FILE]   Writes dev/runs/s7-spend-groups/groups.json (per seed, per group sums). */
'use strict';
const fs = require('fs'), path = require('path'), cp = require('child_process');
const ROOT = path.join(__dirname, '..', '..');
const arg = (k, d) => { const a = process.argv.find(x => x.startsWith('--' + k + '=')); return a ? a.slice(k.length + 3) : d; };
function runSeeds(lo, hi) {
  const H = require(path.join(ROOT, 'harness.js')), svS = H.startRelease(), svN = svS.svN, svG = svS.svG, res = [];
  try {
    const P = Object.assign({}, H.FULL_INTEGRATION, {years: 20, nAgents: 500}), c = H.relMainCfgs(H.tbPresets(P))[0];
    H.frozenRow(c); Object.assign(c, {sn: {abawd: true, slope: true}, lt: {s: 'all', m: 'all'}});
    const so = Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: c.sc}, H.REL_V52_STUDY), cfg = [c];
    for (let sd = lo; sd <= hi; sd++) {
      H.tbStudy(cfg, sd, P, so, sd);  /* fills the supply-path cache */
      let run = null, rec = null;
      H.setRepHook(function (agents, yr, TT, lf) {
        if (yr === 0) run = agents.map(() => ({I: 0, C: 0, K: 0, W: 0})); if (!run) return;
        agents.forEach((a, i) => { const r = run[i]; if (!r) return;
          r.I += ((+a.yrWageUSD || 0) + (+a.yrSSUSD || 0) + (a._acU || 0) + (a._acT || 0) + (+a.yrConvUSD || 0) + (a._acI || 0))/lf;
          r.C += ((+a.yrCostUSD || 0) - (a._acGr || 0) + (a._acSc || 0) - (a._acFl || 0))/lf; r.K += (+a.yrCostUSD || 0)/lf; r.W += (+a.yrWageUSD || 0)/lf; });
        if (yr === TT - 1) { rec = run; run = null; } });
      H.setAcct(H.acctNew());
      try { H.tbStudy(cfg, sd, P, so, sd); } finally { H.setRepHook(null); H.setAcct(null); }
      if (!rec) throw new Error('seed ' + sd + ': no full run seen');
      const s = rec.slice().sort((a, b) => a.I - b.I), n = s.length, g = [];
      for (let q = 0; q < 5; q++) { const part = s.slice(Math.floor(q*n/5), Math.floor((q + 1)*n/5)), t = {I: 0, C: 0, K: 0, W: 0, n: part.length};
        part.forEach(r => { t.I += r.I; t.C += r.C; t.K += r.K; t.W += r.W; }); g.push(t); }
      res.push({seed: sd, groups: g});
    }
  } finally { H.resetNR6(svN); H.tbSetG(svG); }
  return res;
}
if (process.argv[2] === '--child') { process.send(runSeeds(+process.argv[3], +process.argv[4])); process.exit(0); }
const N = +arg('seeds', 50), K = Math.max(1, +arg('procs', 4)), OUT = arg('out', path.join(ROOT, 'dev', 'runs', 's7-spend-groups', 'groups.json'));
const per = Math.ceil(N/K), jobs = [];
for (let k = 0; k < K; k++) { const lo = k*per + 1, hi = Math.min(N, (k + 1)*per); if (lo > hi) continue;
  jobs.push(new Promise((res, rej) => { const c = cp.fork(__filename, ['--child', String(lo), String(hi)]); let got = null;
    c.on('message', m => { got = m; }); c.on('exit', code => code === 0 && got ? res(got) : rej(new Error('child ' + lo + '-' + hi + ' exited ' + code))); })); }
Promise.all(jobs).then(rs => { const H = require(path.join(ROOT, 'harness.js')), svS = H.startRelease();  /* the children started the same way */
  const all = [].concat(...rs).sort((a, b) => a.seed - b.seed);
  fs.mkdirSync(path.dirname(OUT), {recursive: true});
  fs.writeFileSync(OUT, JSON.stringify({_meta: {what: 'S7 part 2 item 2: saving and spending by income group, frozen no-programme row, Reference, 500 adults, 20 years', seeds: '1-' + N,
    groupBy: 'five equal groups of adults by disposable income over the 20 years, per seed', command: 'node dev/tools/s7_spend_groups.js --seeds=' + N + ' --procs=' + K, manifest: H.runManifest(), settings: svS.settings}, seeds: all}));
  console.log('wrote ' + OUT + ' (' + all.length + ' seeds)'); }).catch(e => { console.error(e); process.exit(1); });
