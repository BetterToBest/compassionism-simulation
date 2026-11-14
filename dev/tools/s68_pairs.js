#!/usr/bin/env node
/* S68 part 2 (Nov 14, 2026; research-update PLAN S68 items 3 and 7): the on-together tests of the round-2 switches. Every round-2 switch's other reading
 * (harness.js R2_ALT), alone and in every pair, on the candidate main row (r2MainRow: every round-2 switch at its recommended reading) and its no-programme
 * run, through harness.js r2PairCheck: accounting identities, eight main-stream draws per adult-year, no non-finite output, each switch's own checks
 * (r2Own), and the run-order test. A test, not a study: no figure here is a result.
 * Usage: node dev/tools/s68_pairs.js ENV [SEEDS] [--design=rel] [--only=a,b] [--out=FILE]   (ENV ref | adv | st; default 5 seeds, the C2.2 design)
 *        writes dev/runs/s68-pairs/s68-pairs-ENV[-rel].json */
'use strict';
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const ARG = process.argv.slice(2).filter(a => !/^--/.test(a)), opt = k => (process.argv.filter(a => a.indexOf('--' + k + '=') === 0)[0] || '').slice(k.length + 3);
const env = ARG[0] || 'ref', N = +(ARG[1] || 5), design = opt('design') || 'c22', t0 = Date.now();
if (['ref', 'adv', 'st'].indexOf(env) < 0) { console.error('ENV must be ref, adv or st'); process.exit(1); }
const R = H.r2PairCheck(env, N, {design, only: opt('only') ? opt('only').split(',') : null, log: x => process.stderr.write(x.id + (x.pass ? ' pass' : ' FAIL') + ' ' + x.secs.toFixed(1) + 's\n')});
R.design = design; R.mainRow = H.R2_MAIN; R.study = H.R2_MAIN_STUDY; R.alts = H.R2_ALT.map(a => [a[0], a[1], String(a[2])]); R.manifest = H.runManifest();
R.command = 'node dev/tools/s68_pairs.js ' + process.argv.slice(2).join(' '); R.secs = (Date.now() - t0)/1000;
R.summary = {rows: R.rows.length, pass: R.rows.filter(x => x.pass).length, threw: R.rows.filter(x => x.threw).map(x => x.id + ': ' + x.threw), fail: R.rows.filter(x => !x.pass && !x.threw).map(x => x.id)};
const out = opt('out') || path.join(__dirname, '..', 'runs', 's68-pairs', 's68-pairs-' + env + (design === 'rel' ? '-rel' : '') + '.json');
fs.mkdirSync(path.dirname(out), {recursive: true}); fs.writeFileSync(out, JSON.stringify(R, null, 1));
console.log(env + ' ' + design + ': ' + R.summary.pass + '/' + R.summary.rows + ' pass; run order ' + JSON.stringify(R.runOrder) + '; ' + R.secs.toFixed(0) + ' s');
