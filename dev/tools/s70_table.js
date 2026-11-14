#!/usr/bin/env node
/* S70 (Nov 14, 2026): the screen's analysis, as research-update prereg/2026-11-s70-screen.md fixes it. Reads the shard files of one block's study
 * folder (runner/jobs/s70-screen.js in compassionism-sim-results; shard-NNNN.json, seeds split across shards), joins them by seed, and for each cell
 * (block S: design x backing x environment; block F: design x environment) and outcome computes the Morris elementary effects of every input:
 * EE = the programme's effect at the moved point minus at the point before (same seeds; effect = programme run minus its own no-programme run, mean over
 * seeds, or median for the debt keys), mu* = mean |EE|, mu = mean EE, sigma; the noise check on seeds 1-20 against 21-40 (measured when the blocks'
 * mu* differ by less than a quarter of the joined mu*); sigma_adj = sqrt(max(0, sigma^2 - v)), v = mean (EE1 - EE2)^2 / 4; the interaction flag
 * (sigma_adj >= 0.5 mu*, strong at >= mu*); and the preregistration's decision rules:
 *   rules 1-4 (carry in full, at one reading, hold at main) on the primary outcomes;
 *   rule 3's reading (the end with the larger mean effect, from the trajectories' EE per unit moved, or per category step);
 *   rule 5's 2 x 2 pairs (a carried, flagged input with the top-ranked input of its outcome and cell; the next-ranked when it is the top itself);
 *   rule 6 (inactive inputs: the price rule's six readings at full backing; the markdown where the bargaining pass-through is 0; the policy-rate
 *   rule's coefficients under the fixed rate): its tables keep every EE, but the rules read only the cells and steps where the input can act.
 * The secondary outcomes (wealth poverty at year 20, programme cost, the contribution's mean rate) are reported and not ranked by the rules.
 * Nov 14, part 2: rules 3, 5 and 6 and the secondary outcomes added after the results were read (the first version applied rules 1-4 only);
 * no rule changed. The cell's first design point is reported as `firstPointEffect`, not as the main row (the design holds no main-row point).
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
const SPEC = {}; M.inputs.forEach(x => { SPEC[x.name] = x; });
/* the main row's reading of each input (runner/jobs/s70-screen.js, MAIN; sc is H.SPEND_FROZEN, rho H.LABOR_DEFAULTS.rho) */
const MAIN = {prK: 1, prR: 0, prA: 0, prH: 0, prRs: false, prBd: 0, sc: 0.877, wIdx: 1, rho: 0.16, paDem: 0.49, drLim: 2500, lfConv: 'keep', lfFl: 'stock', lfPm: 0.43,
  rtPhi: 0.46, rtNs: 'nom', rtIx: 1, rtChi: 0, bgPi: 0, bgM: 1/1.21, poCost: 'full', poRes: 0.017, poW: 0.20, poTest: 'sales', poHire: null, poBonus: 'workers', poPay: 'source',
  crInc: 'pass', crOut: 1, crPop: 0, wtCut: 'main', wtA: 0, wtM: 3, gvSh: 1, gvBase: 'w', cap: 1, fin: 'debt', gvRr: 0.0097, gvDk: 0.04, gvR: 'fixed', gvA: 0.5, gvB: 0.5, gvRs: 0.0097, gvIp: 'tax'};
/* rule 6: where an input can act. PRICE: the price rule's readings, inactive at full backing (block S cells c22 and rel). STEP: a condition on the
 * point the step leaves (the input moved alone, so the condition holds at both points of the step). */
const PRICE = ['prK', 'prR', 'prA', 'prH', 'prRs', 'prBd'];
const STEP = {bgM: x => x.bgPi > 0, gvA: x => x.gvR === 'rule', gvB: x => x.gvR === 'rule', gvRs: x => x.gvR === 'rule'};
const STEPWHY = {bgM: 'steps with a bargaining pass-through above 0', gvA: 'steps under the policy-rate rule', gvB: 'steps under the policy-rate rule', gvRs: 'steps under the policy-rate rule'};
const cellActs = (n, r) => !(block === 'S' && (r === 'c22' || r === 'rel') && PRICE.includes(n));
/* joined per-seed series: rows[name][key] = array over all seeds */
const rows = {}; Object.keys(files[0].rows).forEach(r => { rows[r] = {}; Object.keys(files[0].rows[r]).forEach(k => { rows[r][k] = [].concat(...files.map(f => f.rows[r][k])); }); });
const ENVS = M.env === 'both' ? ['ref', 'adv'] : [M.env], EN = {ref: 'Reference', adv: 'Adverse'};
const CELLS = block === 'S' ? [['c22', 'C2.2, full backing'], ['rel', 'release design, full backing'], ['c22a0', 'C2.2, no assumed backing'], ['rela0', 'release design, no assumed backing']]
  : [['c22', 'C2.2, financed'], ['rel', 'release design, financed']];
/* [key, name, how, threshold (null: 5% of the no-programme median wealth), digits, primary] */
const OUTC = [['bNAPy', 'basic living (points)', 'mean', 1, 2, true], ['fgt0PY', 'cost of living (points)', 'mean', 1, 2, true], ['ppovA', 'wealth poverty, yearly average (points)', 'mean', 1, 2, true],
  ['wtMedE', 'median real wealth ($)', 'mean', null, 0, true], ['endoAnn', 'programme inflation (points a year)', 'mean', 1, 2, true]]
  .concat(block === 'F' ? [['gvDebtY', 'programme debt at year 20 (% of GDP)', 'median', 10, 1, true], ['gvY100', 'year debt passes GDP (21: not within 20 years)', 'median', 2, 1, true]] : [])
  .concat([['pov', 'secondary: wealth poverty at year 20 (points)', 'mean', 0, 2, false], ['cost', 'secondary: programme cost ($)', 'mean', 0, 0, false]])
  .concat(block === 'F' ? [['tauMean', 'secondary: the contribution\'s mean rate (points)', 'mean', 0, 3, false]] : []);
const SCALE = {endoAnn: 100, tauMean: 100};
const mean = a => a.length ? a.reduce((s, x) => s + x, 0)/a.length : 0;
const median = a => { const b = a.slice().sort((x, y) => x - y), n = b.length; return n % 2 ? b[(n - 1)/2] : (b[n/2 - 1] + b[n/2])/2; };
const sd = a => { const m = mean(a); return Math.sqrt(a.reduce((s, x) => s + (x - m)*(x - m), 0)/Math.max(1, a.length - 1)); };
const key = (e, p, r) => e + '.p' + String(p).padStart(4, '0') + '.' + r;
/* the effect at point p for row r and key k over seeds [i0, i1) */
function effect(e, p, r, k, how, i0, i1) {
  const a = rows[key(e, p, r)][k], b = rows[key(e, p, 'none')][k]; if (!a || !b) return null;
  const f = SCALE[k] || 1, d = []; for (let i = i0; i < i1; i++) d.push((a[i] - b[i])*f);
  return how === 'median' ? median(d) : mean(d);
}
/* Morris statistics of one input's steps (EE over all seeds, E1 and E2 the two seed blocks) */
function stats(ee, e1, e2) {
  const ms = mean(ee.map(Math.abs)), mu = mean(ee), sg = sd(ee), m1 = mean(e1.map(Math.abs)), m2 = mean(e2.map(Math.abs));
  const v = mean(e1.map((x, t) => (x - e2[t])*(x - e2[t])/4)), sa = Math.sqrt(Math.max(0, sg*sg - v));
  return {muStar: ms, mu, sigma: sg, sigmaAdj: sa, noiseVar: v, blocks: [m1, m2], measured: Math.abs(m1 - m2) < 0.25*ms, flag: ms > 0 && sa >= ms ? 'I' : ms > 0 && sa >= 0.5*ms ? 'i' : '', steps: ee.length};
}
const ruleOf = (ms, thr) => ms >= thr ? 'full' : ms >= 0.5*thr ? 'one' : 'hold';
const S = {block, seeds, engine: M.manifest && M.manifest.commit, trajectories: M.trajectories, inputs: M.inputs, cells: {}};
const md = ['# S70 screen, block ' + block + ' (' + (block === 'S' ? 'the Source rows' : 'the financed rows') + ')', '',
  'Morris elementary effects, ' + M.trajectories + ' trajectories, ' + inputs.length + ' inputs, seeds ' + seeds.join('-') + ' (noise check: ' + seeds[0] + '-' + (seeds[0] + half - 1) + ' against ' + (seeds[0] + half) + '-' + seeds[1] + '), engine ' + String(S.engine).slice(0, 7) + ', 500 adults, 20 years.',
  'Effect: programme run minus its own no-programme run (mean over seeds; median for the debt keys). EE: the change in the effect for one step of 2/3 of an input\'s range (a categorical input: its switch). mu* ranks; mu gives the sign; sigma_adj is sigma with seed noise removed.',
  'Flags: `*` not measured (the seed blocks\' mu* differ by a quarter or more of mu*); `i` interaction or curvature (sigma_adj >= 0.5 mu*), `I` strong (>= mu*). Rule: `full` (mu* at or above the threshold), `one` (half the threshold or more), `hold` (below half); `inactive` where rule 6 says the input cannot act in this cell; a rule-6 input acting only on some steps is ruled on those steps (its mu* there in the last column). Secondary outcomes are reported, not ruled. "Effects across points": the programme\'s effect at the design\'s points (lowest, median, highest), for scale only; no point is the main row. Generated by `node dev/tools/s70_table.js`.', ''];
const verdict = {}; inputs.forEach(n => { verdict[n] = {rule: 'hold', where: [], maxRatio: 0, maxCell: '', maxAt: null, flags: [], inactiveCells: 0}; });
const pairs = {};
ENVS.forEach(e => {
  const thrW = 0.05*mean(design.map(pt => mean(rows[key(e, pt.p, 'none')].wtMedE)));
  S.cells[e] = {thrWealth: thrW};
  CELLS.forEach(([r, rname]) => {
    S.cells[e][r] = {};
    md.push('## ' + EN[e] + ': ' + rname, '');
    OUTC.forEach(([k, kname, how, thr0, dg, primary]) => {
      const thr = thr0 === null ? thrW : thr0;
      const yAll = design.map(pt => effect(e, pt.p, r, k, how, 0, N)); if (yAll.some(v => v === null)) return;
      const y1 = design.map(pt => effect(e, pt.p, r, k, how, 0, half)), y2 = design.map(pt => effect(e, pt.p, r, k, how, half, N));
      const EE = {}, E1 = {}, E2 = {}, AT = {}; inputs.forEach(n => { EE[n] = []; E1[n] = []; E2[n] = []; AT[n] = []; });
      design.forEach((pt, j) => { if (!pt.moved) return; const n = pt.moved;
        EE[n].push(yAll[j] - yAll[j - 1]); E1[n].push(y1[j] - y1[j - 1]); E2[n].push(y2[j] - y2[j - 1]); AT[n].push({from: design[j - 1].x[n], to: pt.x[n], x: design[j - 1].x}); });
      const res = inputs.map(n => { const st = Object.assign({name: n}, stats(EE[n], E1[n], E2[n]));
        st.acts = cellActs(n, r);
        if (st.acts && STEP[n]) { const keep = AT[n].map(a => STEP[n](a.x)); const f = a => a.filter((_, t) => keep[t]);
          st.active = stats(f(EE[n]), f(E1[n]), f(E2[n])); }
        const ruled = st.active || st;
        st.rule = !primary ? '' : !st.acts ? 'inactive' : st.active && !st.active.steps ? 'inactive' : ruleOf(ruled.muStar, thr);
        st.eeAt = AT[n].map((a, t) => ({from: a.from, to: a.to, ee: EE[n][t], acts: !STEP[n] || STEP[n](a.x)}));
        return st; }).sort((a, b) => b.muStar - a.muStar);
      const sorted = yAll.slice().sort((a, b) => a - b);
      S.cells[e][r][k] = {threshold: thr, primary, firstPointEffect: yAll[0], pointEffects: {min: sorted[0], median: median(yAll), max: sorted[sorted.length - 1], mean: mean(yAll)}, inputs: res.map(x => { const {eeAt, ...o} = x; return o; })};
      if (primary) {
        const ranked = res.filter(x => x.rule !== 'inactive');
        res.forEach(x => { const V = verdict[x.name];
          if (x.rule === 'inactive') { V.inactiveCells++; return; }
          const ruled = x.active || x, ratio = thr > 0 ? ruled.muStar/thr : 0;
          if (ratio > V.maxRatio) { V.maxRatio = ratio; V.maxCell = EN[e] + ', ' + rname + ', ' + kname; V.maxAt = {e, r, k, thr, mean: mean(yAll), mu: ruled.mu, eeAt: x.eeAt.filter(a => a.acts)}; }
          if (x.rule === 'full') V.rule = 'full'; else if (x.rule === 'one' && V.rule === 'hold') V.rule = 'one';
          if (x.rule !== 'hold') V.where.push(EN[e] + ' / ' + r + ' / ' + k);
          if (ruled.flag && x.rule === 'full') {
            const top = ranked[0].name === x.name ? (ranked[1] || {}).name : ranked[0].name;
            V.flags.push(EN[e] + ' / ' + r + ' / ' + k + ' (' + ruled.flag + ', with ' + top + ')');
            if (top) { const pk = [x.name, top].sort().join(' x '); (pairs[pk] = pairs[pk] || []).push(EN[e] + ' / ' + r + ' / ' + k); }
          } });
      }
      const f = x => x.toFixed(dg), pe = S.cells[e][r][k].pointEffects;
      md.push('### ' + kname + (primary ? ' (threshold ' + f(thr) + ')' : ' (reported, not ruled)'), '', 'Effects across points: ' + f(pe.min) + ' / ' + f(pe.median) + ' / ' + f(pe.max) + '.', '',
        '| rank | input | mu* | mu | sigma_adj | blocks\' mu* | flags | rule | mu* where it acts |', '|---|---|---|---|---|---|---|---|---|');
      res.forEach((x, i) => md.push('| ' + (i + 1) + ' | ' + x.name + ' | ' + f(x.muStar) + ' | ' + f(x.mu) + ' | ' + f(x.sigmaAdj) + ' | ' + f(x.blocks[0]) + ' / ' + f(x.blocks[1]) + ' | ' + (x.measured ? '' : '*') + x.flag + ' | ' + (x.rule || '–') + ' | ' +
        (x.active ? f(x.active.muStar) + ' (' + x.active.steps + ' of ' + x.steps + ' steps)' : '') + ' |'));
      md.push('');
    });
  });
});
/* rule 3: the end with the larger mean effect. Continuous and integer inputs: the slope (mean of EE per unit moved over the steps where it acts) times the
 * distance from the main reading to each end, added to the cell's mean effect; the end whose total is larger in size. Categorical inputs (main first):
 * each other category's shift from main is the sum of the mean EE of the steps that lead to it from main (A->B, then B->C). */
function oneReading(n) {
  const V = verdict[n], sp = SPEC[n], at = V.maxAt; if (!at) return null;
  const main = MAIN[n], m = at.mean, cand = [];
  if (sp.kind === 'c' || sp.kind === 'i') {
    const sl = mean(at.eeAt.filter(a => a.to !== a.from).map(a => a.ee/(a.to - a.from)));
    sp.spec.forEach(end => { if (end !== main) cand.push({reading: end, shift: sl*(end - main)}); });
  } else {
    const cats = sp.spec, seq = [cats[0]].concat(cats.length > 2 ? [cats[1], cats[2]] : [cats[1]]);
    let acc = 0; for (let i = 1; i < seq.length; i++) { const st = at.eeAt.filter(a => a.from === seq[i - 1] && a.to === seq[i]); acc += mean(st.map(a => a.ee)); cand.push({reading: seq[i], shift: acc}); }
  }
  cand.forEach(c => { c.total = m + c.shift; });
  cand.sort((a, b) => Math.abs(b.total) - Math.abs(a.total));
  return {cell: V.maxCell, cellMeanEffect: m, candidates: cand, carry: cand.length ? cand[0].reading : null};
}
inputs.forEach(n => { if (verdict[n].rule === 'one') verdict[n].oneReading = oneReading(n); });
S.verdict = {}; inputs.forEach(n => { const {maxAt, ...o} = verdict[n]; S.verdict[n] = o; });
S.pairs = pairs;
const show = v => v === null ? 'none' : typeof v === 'number' ? String(+v.toPrecision(4)) : String(v);
md.push('## Decision rules applied (prereg rules 2-6; the primary outcomes of every cell of this block)', '',
  'Largest mu* / threshold: over the cells and steps where the input can act (rule 6). Inactive cells: cells rule 6 leaves out.', '',
  '| input | rule | largest mu* / threshold | in | cells at or above half the threshold | inactive cells | flagged where carried in full |', '|---|---|---|---|---|---|---|');
inputs.slice().sort((a, b) => verdict[b].maxRatio - verdict[a].maxRatio).forEach(n => { const V = verdict[n];
  md.push('| ' + n + ' | ' + V.rule + ' | ' + V.maxRatio.toFixed(2) + ' | ' + V.maxCell + ' | ' + V.where.length + ' | ' + V.inactiveCells + ' | ' + (V.flags.length ? V.flags.length + ' cells' : '–') + ' |'); });
md.push('', '## Rule 3: the one reading carried', '', '| input | main | cell | candidates (reading: effect there) | carry |', '|---|---|---|---|---|');
inputs.filter(n => verdict[n].oneReading).forEach(n => { const o = verdict[n].oneReading;
  md.push('| ' + n + ' | ' + show(MAIN[n]) + ' | ' + o.cell + ' | ' + o.candidates.map(c => show(c.reading) + ': ' + c.total.toFixed(2)).join('; ') + ' | ' + show(o.carry) + ' |'); });
md.push('', '## Rule 5: the 2 x 2 pairs (a carried, flagged input with the top-ranked input of its outcome and cell)', '', '| pair | cells |', '|---|---|');
Object.keys(pairs).sort((a, b) => pairs[b].length - pairs[a].length).forEach(p => md.push('| ' + p + ' | ' + pairs[p].length + ' |'));
md.push('', '## Rule 6: inputs ruled on part of the screen', '', PRICE.join(', ') + ': ' + (block === 'S' ? 'the full-backing cells are inactive (almost no new money reaches prices); ruled on the no-assumed-backing cells.' : 'active in every financed cell.'),
  Object.keys(STEP).filter(n => inputs.includes(n)).map(n => n + ': ruled on the ' + STEPWHY[n] + '.').join(' '), '');
fs.mkdirSync(OUT, {recursive: true});
fs.writeFileSync(path.join(OUT, 's70-' + block + '-tables.md'), md.join('\n') + '\n');
fs.writeFileSync(path.join(OUT, 's70-' + block + '-summary.json'), JSON.stringify(S, null, 1) + '\n');
console.log('block ' + block + ': ' + inputs.length + ' inputs, ' + design.length + ' points, seeds ' + seeds.join('-') + ' -> ' + path.join(OUT, 's70-' + block + '-tables.md'));
['full', 'one', 'hold'].forEach(rl => console.log('  ' + rl + ': ' + inputs.filter(n => verdict[n].rule === rl).sort((a, b) => verdict[b].maxRatio - verdict[a].maxRatio).map(n => n + ' ' + verdict[n].maxRatio.toFixed(2)).join(', ')));
inputs.filter(n => verdict[n].oneReading).forEach(n => console.log('  rule 3 ' + n + ': carry ' + show(verdict[n].oneReading.carry) + ' (' + verdict[n].oneReading.cell + ')'));
console.log('  rule 5 pairs: ' + Object.keys(pairs).length);
