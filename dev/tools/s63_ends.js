#!/usr/bin/env node
/* S63 part 2 (Nov 14, 2026; research-update prereg/2026-11-s63-round2-freeze.md, Design items 3 and 4): the readings the round-2 batch takes for the
 * 2 x 2 pairs and the least-favourable bound, fixed from the S70 screen before any round-2 run.
 *
 *   Pairs (item 3). Each pair in S70's rule-5 list (s70-<block>-summary.json, pairs: the cells where it was flagged). Each input of a pair takes the end
 *   whose effect is larger in the pair's own cells, by S70's rule-3 reading (dev/tools/s70_table.js oneReading): continuous and integer inputs, the
 *   slope (mean EE per unit moved over the steps where the input acts) times the distance from the main reading to each end, added to the cell's mean
 *   effect; categorical inputs (main first), the summed mean EE of the steps from main to each category. Over the pair's cells (each counted once) the
 *   end with the larger sum of |effect at the end| / the cell's threshold is taken.
 *   Bound (item 4). Per design (the full-backing cells c22 and rel of block S; the financed cells c22 and rel of block F) and headline outcome
 *   (bNAPy, fgt0PY, ppovA, wtMedE, endoAnn): every carried input (S70 rule full or one) at the end whose mu (the mean EE, over the steps where it acts,
 *   Reference and Adverse pooled) moves the effect against the programme: poverty and inflation up, median wealth down. mu > 0 against (or mu < 0 for
 *   wealth) takes the top of the range (the last category); the other sign the bottom (the first category, which is main for every categorical input).
 *   An input at rule 3 (one reading) takes that reading when it lies on the unfavourable side, main otherwise. mu equal to 0 at two decimals: main.
 *
 * The EE of each step is recomputed from the S70 shards (the summary keeps the statistics, not the steps), as s70_table.js computes it.
 * Usage: node dev/tools/s63_ends.js S70_S_DIR S70_F_DIR OUT.json
 *   (S70_*_DIR: compassionism-sim-results s70-screen-s-8b96cdd and s70-screen-f-8b96cdd, each with its shards and s70-<block>-summary.json). */
'use strict';
const fs = require('fs'), path = require('path');
const [DS, DF, OUT] = process.argv.slice(2);
if (!DS || !DF || !OUT) { console.error('usage: s63_ends.js S70_S_DIR S70_F_DIR OUT.json'); process.exit(1); }
const mean = a => a.length ? a.reduce((s, x) => s + x, 0)/a.length : 0;
const median = a => { const b = a.slice().sort((x, y) => x - y), n = b.length; return n % 2 ? b[(n - 1)/2] : (b[n/2 - 1] + b[n/2])/2; };
/* the main row's reading of each input (as s70_table.js MAIN) */
const MAIN = {prK: 1, prR: 0, prA: 0, prH: 0, prRs: false, prBd: 0, sc: 0.877, wIdx: 1, rho: 0.16, paDem: 0.49, drLim: 2500, lfConv: 'keep', lfFl: 'stock', lfPm: 0.43,
  rtPhi: 0.46, rtNs: 'nom', rtIx: 1, rtChi: 0, bgPi: 0, bgM: 1/1.21, poCost: 'full', poRes: 0.017, poW: 0.20, poTest: 'sales', poHire: null, poBonus: 'workers', poPay: 'source',
  crInc: 'pass', crOut: 1, crPop: 0, wtCut: 'main', wtA: 0, wtM: 3, gvSh: 1, gvBase: 'w', cap: 1, fin: 'debt', gvRr: 0.0097, gvDk: 0.04, gvR: 'fixed', gvA: 0.5, gvB: 0.5, gvRs: 0.0097, gvIp: 'tax'};
const PRICE = ['prK', 'prR', 'prA', 'prH', 'prRs', 'prBd'];
const STEP = {bgM: x => x.bgPi > 0, gvA: x => x.gvR === 'rule', gvB: x => x.gvR === 'rule', gvRs: x => x.gvR === 'rule'};
const SCALE = {endoAnn: 100, tauMean: 100};
const HEAD = ['bNAPy', 'fgt0PY', 'ppovA', 'wtMedE', 'endoAnn'], UP_BAD = {bNAPy: true, fgt0PY: true, ppovA: true, wtMedE: false, endoAnn: true};
const EN = {Reference: 'ref', Adverse: 'adv'};

function load(dir) {
  const files = fs.readdirSync(dir).filter(f => /^shard-\d+\.json$/.test(f)).sort().map(f => JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8')));
  files.sort((a, b) => a._meta.seeds[0] - b._meta.seeds[0]);
  const M = files[0]._meta, rows = {};
  Object.keys(files[0].rows).forEach(r => { rows[r] = {}; Object.keys(files[0].rows[r]).forEach(k => { rows[r][k] = [].concat(...files.map(f => f.rows[r][k])); }); });
  const S = JSON.parse(fs.readFileSync(path.join(dir, 's70-' + M.block + '-summary.json'), 'utf8'));
  const spec = {}; M.inputs.forEach(x => { spec[x.name] = x; });
  return {M, rows, S, spec, block: M.block, design: M.design, inputs: M.inputs.map(x => x.name)};
}
const key = (e, p, r) => e + '.p' + String(p).padStart(4, '0') + '.' + r;
/* the cell's effect at every design point, and each input's steps there (from, to, EE, acts) */
function cell(B, e, r, k) {
  const how = /^gv(DebtY|Y100)$/.test(k) ? 'median' : 'mean', f = SCALE[k] || 1;
  const y = B.design.map(pt => { const a = B.rows[key(e, pt.p, r)][k], b = B.rows[key(e, pt.p, 'none')][k]; const d = a.map((v, i) => (v - b[i])*f); return how === 'median' ? median(d) : mean(d); });
  const steps = {}; B.inputs.forEach(n => { steps[n] = []; });
  B.design.forEach((pt, j) => { if (!pt.moved) return; const n = pt.moved, x0 = B.design[j - 1].x;
    steps[n].push({from: x0[n], to: pt.x[n], ee: y[j] - y[j - 1], acts: !STEP[n] || STEP[n](x0)}); });
  return {mean: mean(y), steps};
}
/* rule 3's candidates for input n in one cell: [{reading, total}] */
function candidates(B, n, c) {
  const sp = B.spec[n], st = c.steps[n].filter(a => a.acts), main = MAIN[n], out = [];
  if (sp.kind === 'c' || sp.kind === 'i') {
    const sl = mean(st.filter(a => a.to !== a.from).map(a => a.ee/(a.to - a.from)));
    sp.spec.forEach(end => { if (end !== main) out.push({reading: end, total: c.mean + sl*(end - main)}); });
  } else {
    const seq = sp.spec; let acc = 0;
    for (let i = 1; i < seq.length; i++) { const s = st.filter(a => a.from === seq[i - 1] && a.to === seq[i]); acc += mean(s.map(a => a.ee)); out.push({reading: seq[i], total: c.mean + acc}); }
  }
  return out;
}
const show = v => v === null ? null : typeof v === 'number' ? +v.toPrecision(6) : v;

function pairs(B) {
  const out = [];
  Object.keys(B.S.pairs).forEach(pk => {
    const cells = Array.from(new Set(B.S.pairs[pk])).map(s => { const [en, r, k] = s.split(' / '); return {e: EN[en], r, k}; });
    const ins = pk.split(' x '), ends = {}, why = {};
    ins.forEach(n => {
      const score = {};
      cells.forEach(c => { const C = cell(B, c.e, c.r, c.k), thr = B.S.cells[c.e][c.r][c.k].threshold || 1;
        candidates(B, n, C).forEach(cd => { const s = JSON.stringify(cd.reading); score[s] = (score[s] || 0) + Math.abs(cd.total)/thr; }); });
      const best = Object.keys(score).sort((a, b) => score[b] - score[a])[0];
      ends[n] = JSON.parse(best); why[n] = Object.fromEntries(Object.entries(score).map(([s, v]) => [s, +v.toFixed(3)]));
    });
    out.push({pair: pk, cells: cells.length, ends, score: why});
  });
  return out;
}
function bound(B, designs) {
  const out = {};
  designs.forEach(d => { out[d] = {};
    HEAD.forEach(k => { const x = {}, mus = {};
      B.inputs.forEach(n => { const V = B.S.verdict[n]; if (V.rule !== 'full' && V.rule !== 'one') return;
        const m = mean(['ref', 'adv'].map(e => { const I = B.S.cells[e][d][k].inputs.find(z => z.name === n); return I ? (I.active ? I.active.mu : I.mu) : 0; }));
        const inactive = B.block === 'S' && (d === 'c22' || d === 'rel') && PRICE.includes(n);
        mus[n] = +m.toPrecision(4);
        if (inactive || Math.round(m*100) === 0) return;  /* main */
        const top = UP_BAD[k] ? m > 0 : m < 0, sp = B.spec[n];
        if (V.rule === 'one') { const r = V.oneReading && V.oneReading.carry; if (r !== undefined && r !== null) { const ix = sp.spec.indexOf(r), hi = sp.kind === 'k' ? ix > 0 : r > MAIN[n]; if (hi === top) x[n] = r; } return; }
        const end = top ? sp.spec[sp.spec.length - 1] : sp.spec[0];
        if (end !== MAIN[n]) x[n] = end; });
      out[d][k] = {readings: x, mu: mus}; }); });
  return out;
}
const BS = load(DS), BF = load(DF);
/* S70 rule 7 (prereg 2026-11-s70-screen.md, Amendment 2): the policy-rate rule's output-gap weight gvB is carried in full on the financed rows, though
 * the screen alone would hold it (S72 moved the rule's two weights together). */
BF.S.verdict.gvB = Object.assign({}, BF.S.verdict.gvB, {rule: 'full', why: 'S70 rule 7'});
const res = {what: 'S63 part 2: the pair ends and least-favourable bound ends of the round-2 batch, from the S70 screen (dev/tools/s63_ends.js)',
  screen: {S: {engine: BS.S.engine, seeds: BS.S.seeds}, F: {engine: BF.S.engine, seeds: BF.S.seeds}},
  carried: {S: BS.inputs.filter(n => ['full', 'one'].includes(BS.S.verdict[n].rule)).map(n => [n, BS.S.verdict[n].rule, BS.S.verdict[n].rule === 'one' ? show(BS.S.verdict[n].oneReading.carry) : null]),
    F: BF.inputs.filter(n => ['full', 'one'].includes(BF.S.verdict[n].rule)).map(n => [n, BF.S.verdict[n].rule, BF.S.verdict[n].rule === 'one' ? show(BF.S.verdict[n].oneReading.carry) : null])},
  pairs: {S: pairs(BS), F: pairs(BF)}, bound: {S: bound(BS, ['c22', 'rel']), F: bound(BF, ['c22', 'rel'])}};
fs.mkdirSync(path.dirname(path.resolve(OUT)), {recursive: true});
fs.writeFileSync(OUT, JSON.stringify(res, null, 1) + '\n');
console.log('carried: S ' + res.carried.S.length + ', F ' + res.carried.F.length + '; pairs: S ' + res.pairs.S.length + ', F ' + res.pairs.F.length + ' -> ' + OUT);
['S', 'F'].forEach(b => ['c22', 'rel'].forEach(d => HEAD.forEach(k => console.log('  bound ' + b + ' ' + d + ' ' + k + ': ' + Object.entries(res.bound[b][d][k].readings).map(([n, v]) => n + '=' + show(v)).join(' ')))));
