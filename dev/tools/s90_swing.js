#!/usr/bin/env node
/* S92 (Nov 19, 2026): the swing measure of research-update prereg/2026-11-s90-private-price-at-sale.md (question 1, decision rule 2).
 * For each environment (Reference, Adverse, Stress), rule (lagged: the published setting; at the sale: sp.vAt 'sale') and seed (1-20 by default),
 * it runs dev/tools/s90_trace.js for that one seed (--from=K --seed=K; 500 adults; 20 years; the full-coverage main row) and reads the BU spent per
 * programme adult in each year. The measure is the mean over years 2-12 of |BU spent this year - last year| / this year.
 * Reading of the definition (the preregistration names the series and the years, not the order of averaging): the measure is computed per seed and
 * then averaged over the seeds, so that swings in different seeds cannot cancel. The same measure on the series pooled over the seeds is printed
 * beside it. Decision rule 2: the fix works if, in every environment, the at-sale measure is below half the lagged one.
 * S93 (Nov 21, 2026; prereg Amendment 2 section C1 and F2, with Amendment 3): since v5.9.22 the sale is the engine's default, so each rule is named
 * to the trace (--lag, --sale). --a=X runs both rules at backed share X (section C1: 0 and 0.5); absent, the main row's full backing. --s92=FILE
 * (S92's swing.json, compassionism-sim-results s90-swing-b8ccd8d) prints S92's at-sale measure beside each environment and applies section C1's
 * condition: at the sale below half the lagged measure, or, where the lagged measure is no larger than S92's at-sale measure at full backing in that
 * environment (no swing to remove), at the sale no larger than lagged.
 * Usage: node dev/tools/s90_swing.js [--seeds=1-20] [--procs=4] [--a=X] [--s92=FILE] [--out=FILE]   (FILE: every seed's series and both measures, JSON) */
'use strict';
const cp = require('child_process'), fs = require('fs'), os = require('os'), path = require('path');
const arg = (k, d) => { const a = process.argv.find(x => x.startsWith('--' + k + '=')); return a ? a.slice(k.length + 3) : d; };
const m = /^(\d+)-(\d+)$/.exec(arg('seeds', '1-20')), lo = +m[1], hi = +m[2], procs = +arg('procs', 4), out = arg('out', ''), BA = arg('a', ''), S92 = arg('s92', '') ? JSON.parse(fs.readFileSync(arg('s92', ''), 'utf8')) : null;
const ENVS = ['ref', 'adv', 'st'], RULES = ['lagged', 'sale'], Y0 = 2, Y1 = 12, TRACE = path.join(__dirname, 's90_trace.js');
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 's90swing-'));
const jobs = []; ENVS.forEach(env => RULES.forEach(rule => { for (let s = lo; s <= hi; s++) jobs.push({env, rule, seed: s, file: path.join(tmp, env + '-' + rule + '-' + s + '.json')}); }));
const runOne = j => new Promise((ok, no) => {
  const a = [TRACE, '--env=' + j.env, '--from=' + j.seed, '--seed=' + j.seed, '--n=500', '--years=20', '--json=' + j.file].concat(j.rule === 'sale' ? ['--sale'] : ['--lag'], BA !== '' ? ['--a=' + BA] : []);
  const c = cp.spawn(process.execPath, a, {stdio: ['ignore', 'ignore', 'inherit']});
  c.on('exit', code => code === 0 ? ok() : no(new Error(j.env + ' ' + j.rule + ' seed ' + j.seed + ' exited ' + code))); });
const series = Y => Object.keys(Y).map(Number).sort((a, b) => a - b).map(y => ({y, bu: Y[y].n ? Y[y].fwB/Y[y].n : 0, fwB: Y[y].fwB, n: Y[y].n}));
const swing = S => { const by = {}; S.forEach(r => { by[r.y] = r.bu; }); let t = 0, k = 0; for (let y = Y0; y <= Y1; y++) { t += Math.abs(by[y] - by[y - 1])/by[y]; k++; } return t/k; };
(async () => {
  const t0 = Date.now(); let i = 0;
  await Promise.all(Array.from({length: Math.min(procs, jobs.length)}, async () => { while (i < jobs.length) await runOne(jobs[i++]); }));
  const res = {what: 'S92 swing measure (prereg 2026-11-s90, question 1)', seeds: [lo, hi], years: [Y0, Y1], adults: 500, horizon: 20, row: 'r2FreezePair c22 (the full-coverage main row)' + (BA !== '' ? ', programme run at backed share ' + BA : ''), backedShare: BA !== '' ? +BA : 1, cells: {}};
  ENVS.forEach(env => { res.cells[env] = {};
    RULES.forEach(rule => {
      const per = [], pool = {};
      for (let s = lo; s <= hi; s++) { const d = JSON.parse(fs.readFileSync(path.join(tmp, env + '-' + rule + '-' + s + '.json'), 'utf8')), S = series(d.Y);
        per.push({seed: s, swing: swing(S), bu: S.map(r => +r.bu.toFixed(2))});
        S.forEach(r => { pool[r.y] = pool[r.y] || {fwB: 0, n: 0}; pool[r.y].fwB += r.fwB; pool[r.y].n += r.n; }); }
      const P = Object.keys(pool).map(Number).sort((a, b) => a - b).map(y => ({y, bu: pool[y].fwB/pool[y].n}));
      res.cells[env][rule] = {swing: per.reduce((a, r) => a + r.swing, 0)/per.length, swingPooled: swing(P), pooledBU: P.map(r => +r.bu.toFixed(2)), perSeed: per};
    });
    const c = res.cells[env]; c.ratio = c.sale.swing/c.lagged.swing; c.ratioPooled = c.sale.swingPooled/c.lagged.swingPooled; c.passes = c.ratio < 0.5;
    if (S92) { c.s92sale = S92.cells[env].sale.swing; c.noSwing = c.lagged.swing <= c.s92sale; c.passesC1 = c.noSwing ? c.sale.swing <= c.lagged.swing : c.passes; } });
  res.rule2 = ENVS.every(e => res.cells[e].passes);
  if (S92) res.conditionC1 = ENVS.every(e => res.cells[e].passesC1);
  fs.rmSync(tmp, {recursive: true, force: true});
  const p = x => (100*x).toFixed(2) + '%';
  console.log('environment  lagged (per seed)  at the sale  ratio   | pooled: lagged  at the sale  ratio');
  ENVS.forEach(e => { const c = res.cells[e]; console.log(e.padEnd(11) + '  ' + p(c.lagged.swing).padStart(17) + '  ' + p(c.sale.swing).padStart(11) + '  ' + c.ratio.toFixed(3).padStart(5) + '   |  ' + p(c.lagged.swingPooled).padStart(13) + '  ' + p(c.sale.swingPooled).padStart(11) + '  ' + c.ratioPooled.toFixed(3)); });
  if (S92) { ENVS.forEach(e => { const c = res.cells[e]; console.log(e.padEnd(11) + '  S92 at the sale (full backing, v5.9 row): ' + p(c.s92sale) + (c.noSwing ? '; no lagged swing to remove here: at the sale must be no larger than lagged' : '') + ': ' + (c.passesC1 ? 'passes' : 'FAILS')); });
    console.log('section C1 condition: ' + (res.conditionC1 ? 'holds' : 'does NOT hold')); }
  console.log('decision rule 2 (at the sale below half of lagged in every environment): ' + (res.rule2 ? 'holds' : 'does NOT hold') + '; ' + ((Date.now() - t0)/1000).toFixed(0) + ' s');
  if (out) fs.writeFileSync(out, JSON.stringify(res, null, 1));
})().catch(e => { console.error(e.message); process.exit(1); });
