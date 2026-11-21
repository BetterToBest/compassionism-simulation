#!/usr/bin/env node
/* S93 (Nov 21, 2026; v5.9.22; research-update prereg/2026-11-s90-private-price-at-sale.md, Amendment 3, conditions A2 and A3): proofs that the release
 * engine changes only what the release says it changes.
 *   A2  With r2FreezePair(P, design, true) (eh false, sn.cdc false, sp.vAt 'lag'), every key of the frozen main pair (no programme, full coverage,
 *       opt-in) on this engine equals r2FreezePair(P, design) on the engine before (OLD: a folder holding that engine's index.html and harness.js),
 *       per seed, in Reference, Adverse and Stress at 20 and 40 years.
 *   A3  With the defaults, every key of the release main pair equals the yardstick study's 'both' rows (none.both, c22.both, rel.both), each run
 *       alone in a fresh process on the engine before with that study's job, per seed, on the keys both hold (Amendment 4: its published shards
 *       carry the supply-path cache defect fixed in this release, so they are compared for information only).
 * Usage: node dev/tools/s93_release_proof.js a2 OLD [--seeds=2] [--n=500]
 *        node dev/tools/s93_release_proof.js a3 OLD RESULTS/runner/jobs/s100.js [--envs=ref,str] [--shard-ref=FILE] [--seeds=2]
 * Exit code 1 on any difference. Each cell runs in its own process (worker mode --emit). */
'use strict';
const fs = require('fs'), path = require('path'), cp = require('child_process');
const ROOT = path.join(__dirname, '..', '..');
const arg = (k, d) => { const a = process.argv.find(x => x.startsWith('--' + k + '=')); return a ? a.split('=')[1] : d; };
const ENVN = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', str: 'STRESS_TEST'};
const SEEDS = +arg('seeds', 2), N = +arg('n', 500);

if (process.argv.includes('--emit')){
  /* worker: --emit --dir=D --mode=old|v59|rel --env=E --years=Y; prints {row: {key: [values by seed]}} */
  const dir = path.resolve(arg('dir')), mode = arg('mode'), env = arg('env'), years = +arg('years');
  const H = require(path.join(dir, 'harness.js')), svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), out = {};
  try {
    const P = Object.assign({}, H[ENVN[env]], {years, nAgents: N}), pair = d => mode === 'v59' ? H.r2FreezePair(P, d, true) : H.r2FreezePair(P, d);
    const c = pair('c22'), r = pair('rel'), rows = [['none', c[0]], ['c22', c[1]], ['rel', r[1]]];
    const R = H.tbStudy(rows.map(x => x[1]), SEEDS, P, H.r2MainStudy());
    R.forEach((x, i) => { const o = out[rows[i][0]] = {}; Object.keys(x._s).forEach(k => { o[k] = Array.from(x._s[k]); }); });
  } finally { H.resetNR6(svN); H.tbSetG(svG); }
  process.stdout.write(JSON.stringify(out)); process.exit(0);
}

function emit(dir, mode, env, years){ return new Promise((ok, no) => {
  const c = cp.spawn(process.execPath, [__filename, '--emit', '--dir=' + dir, '--mode=' + mode, '--env=' + env, '--years=' + years, '--seeds=' + SEEDS, '--n=' + N], {cwd: dir, stdio: ['ignore', 'pipe', 'inherit']});
  let s = ''; c.stdout.on('data', d => { s += d; }); c.on('exit', code => code ? no(new Error(mode + ' ' + env + ' ' + years + ' exited ' + code)) : ok(JSON.parse(s))); }); }
const same = (a, b) => a.length === b.length && a.every((v, i) => Object.is(v, b[i]) || (Number.isNaN(v) && Number.isNaN(b[i])));
function compare(A, B, label, rowsA, rowsB){ let keys = 0, bad = []; rowsA.forEach((ra, i) => { const a = A[ra], b = B[rowsB[i]];
  Object.keys(a).filter(k => k in b).forEach(k => { keys++; const x = a[k], y = b[k].slice(0, x.length); if (!same(x, y)) bad.push(ra + '.' + k); }); });
  console.log(label + ': ' + (bad.length ? 'DIFFERS in ' + bad.length + ' of ' + keys + ' series: ' + bad.slice(0, 8).join(', ') : 'identical, ' + keys + ' series x ' + SEEDS + ' seeds'));
  return bad.length === 0; }
async function pool(jobs, k){ const res = []; let i = 0; const run = async () => { while (i < jobs.length){ const j = i++; res[j] = await jobs[j](); } };
  await Promise.all(Array.from({length: k}, run)); return res; }

(async () => {
  const what = process.argv[2]; let ok = true;
  if (what === 'a2'){
    const OLD = path.resolve(process.argv[3]), cells = [];
    ['ref', 'adv', 'str'].forEach(e => [20, 40].forEach(y => cells.push([e, y])));
    const res = await pool(cells.map(([e, y]) => async () => { const [a, b] = await Promise.all([emit(OLD, 'old', e, y), emit(ROOT, 'v59', e, y)]);
      return compare(b, a, 'A2 ' + e + ' ' + y + ' years (v5.9 row on this engine against the engine before)', ['none', 'c22', 'rel'], ['none', 'c22', 'rel']); }), 2);
    ok = res.every(Boolean);
  } else if (what === 'a3'){
    /* A3 (as amended: Amendment 4): the yardstick study's both rows, each run alone in a fresh process on the engine before (OLD), with its own job
     * (JOB: compassionism-sim-results runner/jobs/s100.js); alone, the supply-path cache cannot hand a row another row's path. --shard=FILE also
     * compares the published shard (seed 1 first), which shows the defect where it acted. */
    const OLD = path.resolve(process.argv[3]), JOB = path.resolve(process.argv[4]), envs = (arg('envs', 'ref,str')).split(','), years = +arg('years', 20), tmp = fs.mkdtempSync(path.join(require('os').tmpdir(), 's93a3-'));
    for (const env of envs){
      const B = {}; [['none', 9], ['c22', 10], ['rel', 11]].forEach(([r, i]) => { const f = path.join(tmp, env + i + '.json');
        cp.execFileSync(process.execPath, [JOB, '--env=' + env, '--years=' + years, '--seeds=1-' + SEEDS, '--rows=' + i + '-' + i, '--out=' + f], {cwd: OLD, stdio: 'ignore'});
        const S = JSON.parse(fs.readFileSync(f, 'utf8')), n = env + '.' + r + '.both'; if (!S.rows[n]) throw new Error('row ' + n + ' not in ' + f); B[r] = S.rows[n]; });
      const A = await emit(ROOT, 'rel', env, years);
      ok = compare(A, B, 'A3 ' + env + ' ' + years + ' years (release main pair against the yardstick study\'s both rows, each run alone on the engine before)', ['none', 'c22', 'rel'], ['none', 'c22', 'rel']) && ok;
      const sh = process.argv.find(x => x.startsWith('--shard-' + env + '='));
      if (sh){ const S = JSON.parse(fs.readFileSync(sh.split('=')[1], 'utf8')), C = {}; ['none', 'c22', 'rel'].forEach(r => { C[r] = S.rows[env + '.' + r + '.both']; });
        compare(A, C, '   (information) the same against the published shard', ['none', 'c22', 'rel'], ['none', 'c22', 'rel']); } }
  } else { console.error('usage: a2 OLD | a3 SHARD...'); process.exit(2); }
  console.log(ok ? 'PROOF PASSED' : 'PROOF FAILED'); process.exit(ok ? 0 : 1);
})().catch(e => { console.error(e); process.exit(1); });
