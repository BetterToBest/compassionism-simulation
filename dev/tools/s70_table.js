#!/usr/bin/env node
/* S70 (Nov 14, 2026): the screen's analysis, as research-update prereg/2026-11-s70-screen.md fixes it. Reads the shard files of one block's study
 * folder (runner/jobs/s70-screen.js in compassionism-sim-results; shard-NNNN.json, seeds split across shards), joins them by seed, and for each cell
 * (block S: design x backing x environment; block F: design x environment) and outcome computes the Morris elementary effects of every input:
 * EE = the programme's effect at the moved point minus at the point before (same seeds; effect = programme run minus its own no-programme run, mean over
 * seeds, or median for the debt keys), mu* = mean |EE|, mu = mean EE, sigma; the noise check on seeds 1-20 against 21-40 (measured when the blocks'
 * mu* differ by less than a quarter of the joined mu*); sigma_adj = sqrt(max(0, sigma^2 - v)), v = mean (EE1 - EE2)^2 / 4; the interaction flag
 * (sigma_adj >= 0.5 mu*, strong at >= mu*); and the preregistration's decision rules 1-4 (carry in full, at one reading, hold at main).
 * Usage: node dev/tools/s70_table.js DIR [OUTDIR]    writes OUTDIR/s70-BLOCK-tables.md and OUTDIR/s70-BLOCK-summary.json (OUTDIR defaults to DIR) */
'use strict';
const fs = require('fs'), path = require('path');
const DIR = process.argv[2], OUT = process.argv[3] || DIR;
if (!DIR) { console.error('usage: s70_table.js DIR [OUTDIR]'); process.exit(1); }
const files = fs.readdirSync(DIR).filter(f => /^shard-\d+\.json$/.test(f)).sort().map(f => JSON.parse(fs.readFileSync(path.join(DIR, f), 'utf8')));
if (!files.length) { console.error('no shard files in ' + DIR); process.exit(1); }
files.sort((a, b) => a._meta.seeds[0] - b._meta.seeds[0]);
const M = files[0]._meta, block = M.block, design = M.design, inputs = M.inputs.map(x => x.name), seeds = [files[0]._meta.seeds[0], files[files.length - 1]._meta.seeds[1]];
files.forEach((f, i) => { if (i && f._meta.seeds[0] !== files[i - 1]._meta.seeds[1] + 1) throw new Error('seed ranges are not consecutive'); if (f._meta.block !== block) throw new Error('mixed blocks'); });
const N = seeds[1] - seeds[0] + 1, half = Math.floor(N/2);
/* joined per-seed series: rows[name][key] = array over all seeds */
const rows = {}; Object.keys(files[0].rows).forEach(r => { rows[r] = {}; Object.keys(files[0].rows[r]).forEach(k => { rows[r][k] = [].concat(...files.map(f => f.rows[r][k])); }); });
const ENVS = M.env === 'both' ? ['ref', 'adv'] : [M.env], EN = {ref: 'Reference', adv: 'Adverse'};
const CELLS = block === 'S' ? [['c22', 'C2.2, full backing'], ['rel', 'release design, full backing'], ['c22a0', 'C2.2, no assumed backing'], ['rela0', 'release design, no assumed backing']]
  : [['c22', 'C2.2, financed'], ['rel', 'release design, financed']];
const OUTC = [['bNAPy', 'basic living (points)', 'mean', 1, 2], ['fgt0PY', 'cost of living (points)', 'mean', 1, 2], ['ppovA', 'wealth poverty, yearly average (points)', 'mean', 1, 2],
  ['wtMedE', 'median real wealth ($)', 'mean', null, 0], ['endoAnn', 'programme inflation (points a year)', 'mean', 1, 2]].concat(block === 'F' ? [['gvDebtY', 'programme debt at year 20 (% of GDP)', 'median', 10, 1], ['gvY100', 'year debt passes GDP', 'median', 2, 1]] : []);
const SCALE = {endoAnn: 100};
const mean = a => a.reduce((s, x) => s + x, 0)/a.length;
const median = a => { const b = a.slice().sort((x, y) => x - y), n = b.length; return n % 2 ? b[(n - 1)/2] : (b[n/2 - 1] + b[n/2])/2; };
const sd = a => { const m = mean(a); return Math.sqrt(a.reduce((s, x) => s + (x - m)*(x - m), 0)/Math.max(1, a.length - 1)); };
const key = (e, p, r) => e + '.p' + String(p).padStart(4, '0') + '.' + r;
/* the effect at point p for row r and key k over seeds [i0, i1) */
function effect(e, p, r, k, how, i0, i1) {
  const a = rows[key(e, p, r)][k], b = rows[key(e, p, 'none')][k]; if (!a || !b) return null;
  const f = SCALE[k] || 1, d = []; for (let i = i0; i < i1; i++) d.push((a[i] - b[i])*f);
  return how === 'median' ? median(d) : mean(d);
}
const S = {block, seeds, engine: M.manifest && M.manifest.commit, trajectories: M.trajectories, inputs: M.inputs, cells: {}};
const md = ['# S70 screen, block ' + block + ' (' + (block === 'S' ? 'the Source rows' : 'the financed rows') + ')', '',
  'Morris elementary effects, ' + M.trajectories + ' trajectories, ' + inputs.length + ' inputs, seeds ' + seeds.join('-') + ' (noise check: ' + seeds[0] + '-' + (seeds[0] + half - 1) + ' against ' + (seeds[0] + half) + '-' + seeds[1] + '), engine ' + String(S.engine).slice(0, 7) + ', 500 adults, 20 years.',
  'Effect: programme run minus its own no-programme run (mean over seeds; median for the debt keys). EE: the change in the effect for one step of 2/3 of an input\'s range (a categorical input: its switch). mu* ranks; mu gives the sign; sigma_adj is sigma with seed noise removed.',
  'Flags: `*` not measured (the seed blocks\' mu* differ by a quarter or more of mu*); `i` interaction or curvature (sigma_adj >= 0.5 mu*), `I` strong (>= mu*). Rule: `full` (mu* at or above the threshold), `one` (half the threshold or more), `hold` (below half). Generated by `node dev/tools/s70_table.js`.', ''];
const verdict = {};
ENVS.forEach(e => {
  const thrW = 0.05*mean(design.map(pt => mean(rows[key(e, pt.p, 'none')].wtMedE)));
  S.cells[e] = {thrWealth: thrW};
  CELLS.forEach(([r, rname]) => {
    S.cells[e][r] = {};
    md.push('## ' + EN[e] + ': ' + rname, '');
    OUTC.forEach(([k, kname, how, thr0, dg]) => {
      const thr = thr0 === null ? thrW : thr0;
      const yAll = design.map(pt => effect(e, pt.p, r, k, how, 0, N)); if (yAll.some(v => v === null)) return;
      const y1 = design.map(pt => effect(e, pt.p, r, k, how, 0, half)), y2 = design.map(pt => effect(e, pt.p, r, k, how, half, N));
      const EE = {}, E1 = {}, E2 = {}; inputs.forEach(n => { EE[n] = []; E1[n] = []; E2[n] = []; });
      design.forEach((pt, j) => { if (!pt.moved) return; EE[pt.moved].push(yAll[j] - yAll[j - 1]); E1[pt.moved].push(y1[j] - y1[j - 1]); E2[pt.moved].push(y2[j] - y2[j - 1]); });
      const res = inputs.map(n => { const ee = EE[n], ms = mean(ee.map(Math.abs)), mu = mean(ee), sg = sd(ee), m1 = mean(E1[n].map(Math.abs)), m2 = mean(E2[n].map(Math.abs));
        const v = mean(E1[n].map((x, t) => (x - E2[n][t])*(x - E2[n][t])/4)), sa = Math.sqrt(Math.max(0, sg*sg - v));
        const measured = Math.abs(m1 - m2) < 0.25*ms, fl = ms > 0 && sa >= ms ? 'I' : ms > 0 && sa >= 0.5*ms ? 'i' : '';
        const rule = ms >= thr ? 'full' : ms >= 0.5*thr ? 'one' : 'hold';
        return {name: n, muStar: ms, mu, sigma: sg, sigmaAdj: sa, noiseVar: v, blocks: [m1, m2], measured, flag: fl, rule}; }).sort((a, b) => b.muStar - a.muStar);
      S.cells[e][r][k] = {threshold: thr, mainEffect: yAll[0], inputs: res};
      res.forEach(x => { const V = verdict[x.name] = verdict[x.name] || {rule: 'hold', where: [], maxRatio: 0, maxCell: '', flags: []};
        const ratio = thr > 0 ? x.muStar/thr : 0; if (ratio > V.maxRatio) { V.maxRatio = ratio; V.maxCell = EN[e] + ', ' + rname + ', ' + kname; }
        if (x.rule === 'full' || (x.rule === 'one' && V.rule === 'hold')) V.rule = x.rule === 'full' ? 'full' : (V.rule === 'full' ? 'full' : 'one');
        if (x.rule !== 'hold') V.where.push(EN[e] + ' / ' + r + ' / ' + k);
        if (x.flag && x.rule === 'full') V.flags.push(EN[e] + ' / ' + r + ' / ' + k + ' (' + x.flag + ', top input ' + res[0].name + ')'); });
      const f = x => x.toFixed(dg);
      md.push('### ' + kname + ' (threshold ' + f(thr) + ')', '', '| rank | input | mu* | mu | sigma_adj | blocks\' mu* | flags | rule |', '|---|---|---|---|---|---|---|---|');
      res.forEach((x, i) => md.push('| ' + (i + 1) + ' | ' + x.name + ' | ' + f(x.muStar) + ' | ' + f(x.mu) + ' | ' + f(x.sigmaAdj) + ' | ' + f(x.blocks[0]) + ' / ' + f(x.blocks[1]) + ' | ' + (x.measured ? '' : '*') + x.flag + ' | ' + x.rule + ' |'));
      md.push('');
    });
  });
});
S.verdict = verdict;
md.push('## Decision rules applied (prereg rules 2-5; every cell of this block)', '', '| input | rule | largest mu* / threshold | in | cells at or above half the threshold | flagged where carried in full |', '|---|---|---|---|---|---|');
inputs.slice().sort((a, b) => verdict[b].maxRatio - verdict[a].maxRatio).forEach(n => { const V = verdict[n];
  md.push('| ' + n + ' | ' + V.rule + ' | ' + V.maxRatio.toFixed(2) + ' | ' + V.maxCell + ' | ' + V.where.length + ' | ' + (V.flags.join('; ') || '–') + ' |'); });
fs.mkdirSync(OUT, {recursive: true});
fs.writeFileSync(path.join(OUT, 's70-' + block + '-tables.md'), md.join('\n') + '\n');
fs.writeFileSync(path.join(OUT, 's70-' + block + '-summary.json'), JSON.stringify(S, null, 1) + '\n');
console.log('block ' + block + ': ' + inputs.length + ' inputs, ' + design.length + ' points, seeds ' + seeds.join('-') + ' -> ' + path.join(OUT, 's70-' + block + '-tables.md'));
inputs.slice().sort((a, b) => verdict[b].maxRatio - verdict[a].maxRatio).slice(0, 12).forEach(n => console.log('  ' + n + ': ' + verdict[n].rule + ' (' + verdict[n].maxRatio.toFixed(2) + ' x threshold, ' + verdict[n].maxCell + ')'));
