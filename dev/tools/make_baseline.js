#!/usr/bin/env node
/* S84 (Nov 17, 2026): writes data/baseline.json, the release's published no-programme rows (seeds 1-20, Reference, Adverse and Stress, 20 years;
 * basket poverty, wealth poverty and median real wealth), read from compassionism-sim-results' round-2 main folders (r2-m-<env>-20-<engine>).
 * harness.js's startRelease().checkBaseline() compares a fresh run of the frozen no-programme arm with these rows per seed before a study runs.
 * Usage: node dev/tools/make_baseline.js RESULTS_REPO_DIR [ENGINE_COMMIT=104691f] [SEEDS=20]
 * The values come from the published results, not from this engine: if the engine ever differs from them, the check fails and says where. */
'use strict';
const fs = require('fs'), path = require('path'), zlib = require('zlib');
const dir = process.argv[2], engine = process.argv[3] || '104691f', N = +(process.argv[4] || 20);
if (!dir) { console.log('usage: node dev/tools/make_baseline.js RESULTS_REPO_DIR [ENGINE] [SEEDS]'); process.exit(1); }
const KEYS = ['fgt0PY', 'pov', 'wtMedE'], FOLDER = {ref: 'r2-m-ref-20-', adv: 'r2-m-adv-20-', st: 'r2-m-str-20-'};
const out = {about: 'The release\'s published no-programme rows (frozen main row, 20 years), seeds 1-' + N + ', read from BetterToBest/compassionism-sim-results. Written by dev/tools/make_baseline.js; read by harness.js startRelease().checkBaseline().',
  engine, years: 20, keys: KEYS, rows: {}};
for (const env of Object.keys(FOLDER)) {
  const f = path.join(dir, FOLDER[env] + engine, 'shard-0000.json.gz'), D = JSON.parse(zlib.gunzipSync(fs.readFileSync(f)).toString('utf8'));
  const names = Object.keys(D.rows).filter(k => /\.none$/.test(k)); if (names.length !== 1) throw new Error(env + ': expected one .none row, found ' + names.join(','));
  const R = D.rows[names[0]]; out.rows[env] = {seeds: N, source: FOLDER[env] + engine + '/shard-0000.json.gz, row ' + names[0]};
  KEYS.forEach(k => { if (!R[k] || R[k].length < N) throw new Error(env + ' ' + k + ' has fewer than ' + N + ' seeds'); out.rows[env][k] = Array.from(R[k]).slice(0, N); });
}
const file = path.join(__dirname, '..', '..', 'data', 'baseline.json'); fs.writeFileSync(file, JSON.stringify(out) + '\n'); console.log('wrote ' + file + ' (' + fs.statSync(file).size + ' bytes)');
