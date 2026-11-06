#!/usr/bin/env node
/* S47 (Nov 6, 2026; research-update prereg/run-manifest.md section 6 item 4; outside audit E17, dev/reports/s13-engine-audit.md): the 0.593 spending share
 * (SPEND_SOURCED, index.html plan step 7) re-derived by its own stated method on the frozen model's no-programme run. No constant moves here: the tool reports.
 *
 * The method (index.html, plan step 7; harness.js spendUnitSuite): the share of cash surplus consumed that makes the no-programme run's saving rate,
 * (wages - (basket consumed - floor top-ups) - surplus consumed) / wages, from the run's ledger in year-0 dollars over seeds 1-100 in the Reference
 * environment, equal the US personal saving rate in 2025, 5.4% (BEA NIPA Table 2.1, line 35). Bisection on the share.
 *
 * Two runs:
 *   published  the run the share was derived on (spendUnitSuite: the plain Baseline of FULL_INTEGRATION, the testbed profile, study options with sc);
 *              its rate at 0.593 must be 5.4% within 0.2 points (the unit test's tolerance): a check that this tool counts as the method does.
 *   frozen     the batch's no-programme row (prereg/run-manifest.md section 1): relMainCfgs(tbPresets(P))[0] (households, income-graded spending, the
 *              v5.3 accounting corrections, the v5.4 parts), sn {abawd, slope}, the CPS yardstick (lt {s: 'all', m: 'all'}), on the frozen engine (au, fx),
 *              study options {fin: 'tax', aT: 0, a: 0, X: 0, sc} plus REL_V52_STUDY; 500 adults, 20 years.
 *   published1 the published run counted as the method describes: the row alone. The derivation that gave 0.593 (and spendUnitSuite) ran each seed cold, so
 *              its ledger also counted the seed's supply-path run (the price-only run, s3BaseS): about half of the adult-years it averaged were not the
 *              no-programme row's (S47 finding). published1 warms the supply path first, as frozen does.
 * In all, the share is set study-wide (the supply path and the row), as the method sets it. Under fx.sp the row's supply path is a no-programme testbed run
 * of its own; so the ledger counts only the row, each seed is run once with no ledger first (it fills the supply-path cache), then again with the ledger.
 *
 * Beside the method's own rate (wages only), a second reading closer to the BEA concept the target is defined on: saving over disposable income, from the
 * engine's accounting check (ACCT, reporting only) at each year's end: disposable income = wage earnings + Social Security + the UBI comparator and unemployment
 * insurance + cash transfers less the contribution and taxes (the safety net) + conversion proceeds + interest; consumption = own cost less the income-graded
 * spending cut + surplus consumed, less debt written off at the wealth floor (as the method nets floor top-ups); each deflated by the year's basket index. In the published run there are no transfers, no interest and no graded spending, so
 * the two readings should agree there; in the frozen run they need not (households, the safety net, unemployment insurance, graded spending).
 * Usage: node dev/tools/s47_spend.js [--seeds=100] [--procs=4] [--tol=0.0001] [--out=FILE]
 * Writes FILE (default dev/runs/s47-spend/rederive.json): the rate at 0.593 in both runs, each bisection step, the derived share for the frozen run. */
'use strict';
const fs = require('fs'), path = require('path'), cp = require('child_process');
const ROOT = path.join(__dirname, '..', '..');
const arg = (k, d) => { const a = process.argv.find(x => x.startsWith('--' + k + '=')); return a ? a.slice(k.length + 3) : d; };
const TARGET = 0.054;
const DPI0 = () => ({I: 0, C: 0, runs: 0});

function sums(variant, share, lo, hi) {
  const H = require(path.join(ROOT, 'harness.js')), svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), out = {W: 0, C: 0, F: 0, X: 0, dpi: DPI0()};
  try {
    const FI = H.FULL_INTEGRATION;
    let cfg, P, so;
    if (variant === 'published' || variant === 'published1') { cfg = [{p: H.tbPresets(FI).baseline()}]; P = FI; so = {fin: 'tax', aT: 0, a: 0, X: 0, sc: share, rep52: true}; }  /* rep52: reporting only, for the hook */
    else { P = Object.assign({}, FI, {years: 20, nAgents: 500}); const c = H.relMainCfgs(H.tbPresets(P))[0];
      Object.assign(c, {sc: share, sn: {abawd: true, slope: true}, lt: {s: 'all', m: 'all'}}); H.frozenRow(c); cfg = [c];
      so = Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: share}, H.REL_V52_STUDY); }
    for (let sd = lo; sd <= hi; sd++) {
      if (variant !== 'published') H.tbStudy(cfg, sd, P, so, sd);  /* fills the supply-path cache with no ledger */
      let run = null; const T = P.years || 20;
      H.setRepHook(function (agents, yr, TT, lf) {  /* one run's years; a short run (tbRun's one-year rate pass) never reaches the last year and is dropped */
        if (yr === 0) run = {I: 0, C: 0}; if (!run) return;
        agents.forEach(a => { const inc = (+a.yrWageUSD || 0) + (+a.yrSSUSD || 0) + (a._acU || 0) + (a._acT || 0) + (+a.yrConvUSD || 0) + (a._acI || 0);
          const con = (+a.yrCostUSD || 0) - (a._acGr || 0) + (a._acSc || 0) - (a._acFl || 0);  /* less debt written off at the wealth floor (the method's floor term) */ run.I += inc/lf; run.C += con/lf; });
        if (yr === TT - 1){ out.dpi.I += run.I; out.dpi.C += run.C; out.dpi.runs++; run = null; } });
      H.setAcct(H.acctNew());
      const L = H.newLedger(); H.setLedger(L); try { H.tbStudy(cfg, sd, P, so, sd); } finally { H.setLedger(null); H.setRepHook(null); H.setAcct(null); }
      const TL = L.real; out.W += TL.wage || 0; out.C += TL.cost || 0; out.F += TL.floor || 0; out.X += TL.surplusConsumed || 0;
    }
  } finally { H.resetNR6(svN); H.tbSetG(svG); }
  return out;
}

if (process.argv[2] === '--child') {
  const [variant, share, lo, hi] = process.argv.slice(3);
  process.send(sums(variant, +share, +lo, +hi)); process.exit(0);
}

const N = +arg('seeds', 100), K = Math.max(1, +arg('procs', 4)), TOL = +arg('tol', 0.0001), OUT = arg('out', path.join(ROOT, 'dev', 'runs', 's47-spend', 'rederive.json'));
function rate(variant, share) {
  const per = Math.ceil(N/K), jobs = [];
  for (let k = 0; k < K; k++) { const lo = k*per + 1, hi = Math.min(N, (k + 1)*per); if (lo > hi) continue;
    jobs.push(new Promise((res, rej) => { const c = cp.fork(__filename, ['--child', variant, String(share), String(lo), String(hi)]); let got = null;
      c.on('message', m => { got = m; }); c.on('exit', code => code === 0 && got ? res(got) : rej(new Error('child ' + lo + '-' + hi + ' exited ' + code))); })); }
  return Promise.all(jobs).then(rs => { const s = rs.reduce((a, r) => ({W: a.W + r.W, C: a.C + r.C, F: a.F + r.F, X: a.X + r.X, I: a.I + r.dpi.I, Q: a.Q + r.dpi.C, runs: a.runs + r.dpi.runs}), {W: 0, C: 0, F: 0, X: 0, I: 0, Q: 0, runs: 0});
    if (s.runs !== N) throw new Error('the hook saw ' + s.runs + ' full runs, expected ' + N);
    return {share, rate: (s.W - (s.C - s.F) - s.X)/s.W, rateDPI: (s.I - s.Q)/s.I, sums: s}; });
}
(async () => {
  const t0 = Date.now(), H = require(path.join(ROOT, 'harness.js')), cur = H.SPEND_SOURCED, rec = {_meta: {what: 'S47: the spending share re-derived by its stated method (audit E17)', seeds: '1-' + N, env: 'Reference',
    target: TARGET, current: cur, tol: TOL, manifest: H.runManifest(), command: 'node dev/tools/s47_spend.js --seeds=' + N + ' --procs=' + K + ' --tol=' + TOL}};
  const pub = await rate('published', cur); rec.published = pub; console.log('published run, share ' + cur + ': saving rate ' + (pub.rate*100).toFixed(3) + '% (over disposable income ' + (pub.rateDPI*100).toFixed(3) + '%)');
  if (N === 100 && Math.abs(pub.rate - TARGET) >= 0.002) {  /* the share was derived on seeds 1-100: only there must it reproduce 5.4% */ console.error('the published run does not reproduce 5.4% within 0.2 points: this tool does not count as the method does'); process.exit(1); }
  const p1 = await rate('published1', cur); rec.published1 = p1; console.log('published run, the row alone, share ' + cur + ': saving rate ' + (p1.rate*100).toFixed(3) + '% (over disposable income ' + (p1.rateDPI*100).toFixed(3) + '%)');
  const fz = await rate('frozen', cur); rec.frozenAtCurrent = fz; console.log('frozen run, share ' + cur + ': saving rate ' + (fz.rate*100).toFixed(3) + '% (over disposable income ' + (fz.rateDPI*100).toFixed(3) + '%)');
  /* The saving rate falls as the share consumed rises. Bisection on [0.3, 0.9], for each reading. */
  const memo = {}, at = async x => memo[x] || (memo[x] = await rate('frozen', x));
  for (const key of ['rate', 'rateDPI']) {
    let a = 0.3, b = 0.9; const ra = await at(a), rb = await at(b), R = rec[key === 'rate' ? 'method' : 'dpi'] = {steps: [ra, rb]};
    if (!(ra[key] > TARGET && rb[key] < TARGET)) { console.error(key + ': the target is not bracketed: ' + ra[key] + ' at ' + a + ', ' + rb[key] + ' at ' + b); R.error = 'not bracketed'; continue; }
    for (let i = 0; i < 20; i++) { const m = +((a + b)/2).toFixed(6), rm = await at(m); R.steps.push(rm); console.log('  ' + key + ', share ' + m.toFixed(5) + ': ' + (rm[key]*100).toFixed(4) + '%');
      if (rm[key] > TARGET) a = m; else b = m; if (Math.abs(rm[key] - TARGET) < TOL || b - a < 0.0005) break; }
    R.derived = +((a + b)/2).toFixed(3); R.derivedExact = (a + b)/2;
    console.log('derived share on the frozen no-programme run (' + (key === 'rate' ? 'the method\'s rate, over wages' : 'over disposable income') + '): ' + R.derived + ' (current ' + cur + ')'); }
  rec._meta.seconds = Math.round((Date.now() - t0)/1000);
  fs.mkdirSync(path.dirname(OUT), {recursive: true}); fs.writeFileSync(OUT, JSON.stringify(rec, null, 1)); console.log('wrote ' + OUT + ' (' + rec._meta.seconds + ' s)');
})().catch(e => { console.error(e); process.exit(1); });
