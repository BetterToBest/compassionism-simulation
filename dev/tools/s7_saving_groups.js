#!/usr/bin/env node
/* S7 part 2, item 2 (Nov 15, 2026): saving and spending by income group, on the frozen no-programme row (Reference environment, 500 adults, 20 years).
 * Same row, share, hook and income and spending definitions as dev/tools/s47_spend.js ('frozen' variant, at the engine's frozen spending share); nothing in the engine changes.
 * Groups: within each seed, the adults are ranked by their disposable income summed over the 20 years and cut into five equal groups (lowest to highest fifth).
 * Per group: disposable income, spending (cost of living less the income-graded cut, plus surplus consumed, less debt written off at the wealth floor), saving = income - spending,
 * all in year-0 dollars. Reported: group shares of total income and spending, and the saving rate (saving / income), each over the seeds with a 95% interval across seeds (t, df = n-1).
 * Usage: node dev/tools/s7_saving_groups.js [--seeds=100] [--procs=4] [--out=FILE]   Writes dev/runs/s7-saving-groups/groups.json (+ groups.csv). */
'use strict';
const fs = require('fs'), path = require('path'), cp = require('child_process');
const ROOT = path.join(__dirname, '..', '..');
const arg = (k, d) => { const a = process.argv.find(x => x.startsWith('--' + k + '=')); return a ? a.slice(k.length + 3) : d; };
const G = 5;

function run(lo, hi) {
  const H = require(path.join(ROOT, 'harness.js')), svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), out = [];
  let scUsed = null;
  try {
    const P = Object.assign({}, H.FULL_INTEGRATION, {years: 20, nAgents: 500}), c = H.relMainCfgs(H.tbPresets(P))[0];
    H.frozenRow(c); Object.assign(c, {sn: {abawd: true, slope: true}, lt: {s: 'all', m: 'all'}}); const cfg = [c];
    const so = Object.assign({fin: 'tax', aT: 0, a: 0, X: 0}, H.REL_V52_STUDY); so.sc = c.sc;  /* the share the frozen row carries */ scUsed = c.sc;
    for (let sd = lo; sd <= hi; sd++) {
      H.tbStudy(cfg, sd, P, so, sd);  /* fills the supply-path cache with no ledger, as s47_spend.js does */
      let run = null; const T = P.years || 20, fin = [];
      H.setRepHook(function (agents, yr, TT, lf) {
        if (yr === 0) run = agents.map(() => ({I: 0, C: 0})); if (!run || run.length !== agents.length) return;
        agents.forEach((a, i) => { run[i].I += ((+a.yrWageUSD || 0) + (+a.yrSSUSD || 0) + (a._acU || 0) + (a._acT || 0) + (+a.yrConvUSD || 0) + (a._acI || 0))/lf;
          run[i].C += ((+a.yrCostUSD || 0) - (a._acGr || 0) + (a._acSc || 0) - (a._acFl || 0))/lf; });
        if (yr === TT - 1) { fin.push(run); run = null; } });
      H.setAcct(H.acctNew()); try { H.tbStudy(cfg, sd, P, so, sd); } finally { H.setRepHook(null); H.setAcct(null); }
      if (fin.length !== 1) throw new Error('seed ' + sd + ': ' + fin.length + ' full runs');
      const r = fin[0].slice().sort((a, b) => a.I - b.I), n = r.length, g = [];
      for (let k = 0; k < G; k++) { let I = 0, C = 0; for (let j = Math.floor(k*n/G); j < Math.floor((k + 1)*n/G); j++) { I += r[j].I; C += r[j].C; } g.push({I, C}); }
      out.push({seed: sd, g});
    }
  } finally { H.resetNR6(svN); H.tbSetG(svG); }
  out.sc = scUsed; return out;
}
if (process.argv[2] === '--child') { process.send(run(+process.argv[3], +process.argv[4])); process.exit(0); }

const N = +arg('seeds', 100), K = Math.max(1, +arg('procs', 4)), OUT = arg('out', path.join(ROOT, 'dev', 'runs', 's7-saving-groups', 'groups.json'));
const tq = df => 1.96 + 2.37/df;
const ci = a => { const n = a.length, m = a.reduce((s, x) => s + x, 0)/n, sd = Math.sqrt(a.reduce((s, x) => s + (x - m)*(x - m), 0)/(n - 1)), h = tq(n - 1)*sd/Math.sqrt(n); return [m, m - h, m + h]; };
(async () => {
  const per = Math.ceil(N/K), jobs = [];
  for (let k = 0; k < K; k++) { const lo = k*per + 1, hi = Math.min(N, (k + 1)*per); if (lo > hi) continue;
    jobs.push(new Promise((res, rej) => { const c = cp.fork(__filename, ['--child', String(lo), String(hi)]); let got = null; c.on('message', m => { got = m; });
      c.on('exit', code => code === 0 && got ? res(got) : rej(new Error('child ' + lo + '-' + hi + ' exited ' + code))); })); }
  const parts = await Promise.all(jobs), scUsed = parts[0].sc, seeds = [].concat(...parts).sort((a, b) => a.seed - b.seed);
  const rows = [], names = ['lowest fifth', 'second fifth', 'middle fifth', 'fourth fifth', 'highest fifth'];
  for (let k = 0; k < G; k++) {
    const sI = seeds.map(s => s.g.reduce((t, x) => t + x.I, 0)), sC = seeds.map(s => s.g.reduce((t, x) => t + x.C, 0));
    const inc = ci(seeds.map((s, i) => s.g[k].I/sI[i]*100)), spe = ci(seeds.map((s, i) => s.g[k].C/sC[i]*100)), sav = ci(seeds.map(s => (s.g[k].I - s.g[k].C)/s.g[k].I*100));
    const perAdult = ci(seeds.map(s => s.g[k].I/(500/G)));
    rows.push({group: names[k], income_share_pct: inc[0], income_lo: inc[1], income_hi: inc[2], spending_share_pct: spe[0], spending_lo: spe[1], spending_hi: spe[2],
      saving_rate_pct: sav[0], saving_lo: sav[1], saving_hi: sav[2], income_per_adult_20y_usd: perAdult[0]});
  }
  const tot = ci(seeds.map(s => { const I = s.g.reduce((t, x) => t + x.I, 0), C = s.g.reduce((t, x) => t + x.C, 0); return (I - C)/I*100; }));
  const rec = {_meta: {what: 'S7: saving and spending by income group, frozen no-programme row, Reference', seeds: '1-' + N, spending_share: scUsed, adults: 500, years: 20, groups: 'fifths of disposable income summed over the run, within each seed',
    command: 'node dev/tools/s7_saving_groups.js --seeds=' + N + ' --procs=' + K, total_saving_rate_pct: tot}, rows};
  fs.mkdirSync(path.dirname(OUT), {recursive: true}); fs.writeFileSync(OUT, JSON.stringify(rec, null, 1));
  const cols = Object.keys(rows[0]); fs.writeFileSync(OUT.replace(/\.json$/, '.csv'), cols.join(',') + '\n' + rows.map(r => cols.map(c => typeof r[c] === 'number' ? r[c].toFixed(4) : r[c]).join(',')).join('\n') + '\n');
  console.log(JSON.stringify(rec, null, 1));
})().catch(e => { console.error(e); process.exit(1); });
