#!/usr/bin/env node
/* S64 part 3 (Nov 15, 2026; research-update prereg/2026-11-s63-round2-freeze.md, Amendment 4): the erosion share of each round-2 wealth figure.
 * S66's question (prereg/2026-11-s66-low-share-trace.md, Part B) on the frozen main row: how much of each wealth result is the programme's higher price
 * level eating the real value of the balances adults held at the start, and nothing else? No engine change: the unmodified harness runs the batch's own
 * rows (runner/jobs/r2.js part M: harness.js r2FreezePair, each row alone in its own study, r2MainStudy) and a read-only year hook (setRepHook) reads
 * each adult's balances. S66's tool patched the engine's text; this one needs no patch.
 *
 * Why S66's term is redefined. Round 2 holds wealth by asset class (S59, rt): homes, other property, shares and businesses are revalued with prices, so
 * the erosion falls only on money claims. The term here is the change in the real value of each adult's opening money claims, held untouched at the
 * engine's own returns on them: the rt tracker b.en (opening nominal assets: deposits, bonds, the non-stock part of funds, carried at phi = 0.46 of
 * inflation less the creditor charges, S71), less b.ed (opening floating-rate debt, carried at psi = 1) and b.df (opening fixed-rate debt, chi = 0),
 * programme run minus no-programme run, each deflated by its own run's basket price level:
 *     eN_t = (en - ed - df)_prog,t / lf_prog,t  -  (en - ed - df)_none,t / lf_none,t
 * Opening real holdings carried the same way (b.v: the five real classes) give eR_t, printed as a check (they keep up with prices; only the creditor
 * charge on shares moves them). S66's all-cash term, eU_t = W0 (1/lf_prog,t - 1/lf_none,t) with W0 the opening net worth, is printed beside as the
 * upper bound. Adults not present at year 0 in both runs have no opening balance: their term is 0.
 * "Without erosion": each adult's programme real wealth minus the term (the adult's opening balances fare as in the no-programme run).
 *
 * Usage: node dev/tools/s64_erosion.js --check
 *        node dev/tools/s64_erosion.js ref|adv|str [--years=40] [--seeds=1-500] [--out=FILE]   (writes dev/runs/s64-erosion/raw/ero-ENV-A-B.json.gz)
 * Every run checks itself against the engine's own outputs: the hook's wealth poverty and median wealth in every year (ppov_t, pmedW_t) and the
 * weighted end-of-run median (wtMedE) must equal the run's keys exactly, and basket poverty summed over labour-force status must equal fgt0PY; the run stops otherwise.
 * Item 2 of part 3: basket poverty (adult-years whose income is below their basket, fgt0PY's count) by labour-force status in the year: in the labour
 * force, or outside it for disability, early retirement, care or school (a._lf, S61; the status moves year to year under lf.fl, S73). */
'use strict';
let RUNSET = null;  /* the run's start (harness.js startRelease), kept for the output's _settings */
const fs = require('fs'), path = require('path'), zlib = require('zlib');
const ROOT = path.join(__dirname, '..', '..'), H = require(path.join(ROOT, 'harness.js'));
const arg = (k, d) => { const a = process.argv.find(x => x.startsWith('--' + k + '=')); return a ? a.slice(k.length + 3) : d; };
const ENVN = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', str: 'STRESS_TEST'};
const SNAP = [19, 39], L = H.CFG.POVERTY_LINE;
const r7 = x => typeof x === 'number' && isFinite(x) ? +x.toPrecision(7) : x;

function rowsFor(P) { const M = H.r2FreezePair(P, 'c22'), R = H.r2FreezePair(P, 'rel')[1]; return [['none', M[0]], ['c22', M[1]], ['rel', R]]; }
const sum = v => v.reduce((s, x) => s + x, 0), mean = v => v.length ? sum(v)/v.length : 0;

/* one seed, the three rows in order; the no-programme run's balances are kept year by year for the two programme runs */
function runSeed(P, sd, hooked) {
  const T = P.years, base = {}, out = {}, keys = {};
  rowsFor(P).forEach(([nm, cfg]) => {
    const rec = {y: []}; let runs = 0, id0 = null;
    if (hooked) H.setRepHook(function (agents, yr, TT, lf) {
      if (TT !== T) return;  /* the one-year run that sets the starting tax rate is not traced */
      if (yr === 0) { runs++; id0 = new Set(); rec.y = []; }  /* a row can make more than one full-length run (its supply path); the last is the reported one, which the key check below proves */
      const n = agents.length, real = new Float64Array(n), nom = new Float64Array(n), rc = new Float64Array(n), w = new Float64Array(n), ids = new Array(n), w0 = new Float64Array(n);
      agents.forEach((a, j) => { const b = a._rt, id = a._id !== undefined ? a._id : j; ids[j] = id; if (yr === 0) id0.add(id);
        real[j] = a.wealth/lf; w[j] = a._w === undefined ? 1 : +a._w;
        if (b) { nom[j] = (b.en - b.ed - b.df)/lf; rc[j] = (b.v[0] + b.v[1] + b.v[2] + b.v[3] + b.v[4])/lf; w0[j] = b.w0; } });
      const d = {lf, pov: 0, med: H.quantileOf(real, 0.5)};
      real.forEach(x => { if (x < L) d.pov++; }); d.pov = d.pov/n*100;
      /* basket poverty by labour-force status in the year (item 2): a._lf the reason an adult is outside the labour force (S61), null in it */
      d.lr = {}; agents.forEach(a => { const c = d.lr[a._lf || 'in'] = d.lr[a._lf || 'in'] || [0, 0]; c[0]++; if ((a._tbGap || 0) > 0) c[1]++; });
      if (nm === 'none') {
        const m = new Map(); ids.forEach((id, j) => { if (id0.has(id)) m.set(id, [nom[j], rc[j], real[j]]); }); d.map = m;
        if (SNAP.includes(yr) && yr < T) d.wtMed = H.dmQuantiles(Array.from(real), Array.from(w), [0.5])[0];
      } else {
        const B = base.y[yr], eN = new Float64Array(n), eR = new Float64Array(n), eU = new Float64Array(n), mt = new Uint8Array(n);
        ids.forEach((id, j) => { const q = id0.has(id) ? B.map.get(id) : undefined; if (!q) return; mt[j] = 1;
          eN[j] = nom[j] - q[0]; eR[j] = rc[j] - q[1]; eU[j] = w0[j]*(1/lf - 1/B.lf); });
        const vN = real.map((x, j) => x - eN[j]), vU = real.map((x, j) => x - eU[j]);
        d.povN = 0; d.povU = 0; vN.forEach(x => { if (x < L) d.povN++; }); vU.forEach(x => { if (x < L) d.povU++; }); d.povN = d.povN/n*100; d.povU = d.povU/n*100;
        d.medN = H.quantileOf(vN, 0.5); d.medU = H.quantileOf(vU, 0.5);
        if (SNAP.includes(yr) && yr < T) {
          const W = Array.from(w); d.wtMed = H.dmQuantiles(Array.from(real), W, [0.5])[0]; d.wtMedN = H.dmQuantiles(Array.from(vN), W, [0.5])[0]; d.wtMedU = H.dmQuantiles(Array.from(vU), W, [0.5])[0];
          const J = []; mt.forEach((m, j) => { if (m) J.push(j); });
          const gap = J.map(j => real[j] - B.map.get(ids[j])[2]);
          Object.assign(d, {nM: J.length, gap: mean(gap), eN: mean(J.map(j => eN[j])), eR: mean(J.map(j => eR[j])), eU: mean(J.map(j => eU[j]))});
          /* by fifth of opening net worth (matched adults; ties by order) */
          const ord = J.slice().sort((x, y) => w0[x] - w0[y] || x - y), fifth = [];
          for (let f = 0; f < 5; f++) { const S = ord.slice(Math.floor(f*ord.length/5), Math.floor((f + 1)*ord.length/5)), ix = S.map(j => J.indexOf(j));
            fifth.push([r7(mean(ix.map(i => gap[i]))), r7(mean(S.map(j => eN[j]))), r7(mean(S.map(j => eU[j])))]); }
          d.fifth = fifth;
        }
      }
      rec.y[yr] = d;
    });
    let R; try { R = H.tbStudy([cfg], sd, P, H.r2MainStudy(), sd); } finally { H.setRepHook(null); }
    const s = R[0]._s; keys[nm] = s;
    if (!hooked) return;
    if (runs < 1) throw new Error(nm + ' seed ' + sd + ': no traced run'); rec.runs = runs;
    /* the hook against the engine's own keys */
    for (let t = 0; t < T; t++) {
      const d = rec.y[t]; if (!d) throw new Error(nm + ' seed ' + sd + ': no year ' + t);
      if (d.pov !== s['ppov_' + t][0] || d.med !== s['pmedW_' + t][0]) throw new Error(nm + ' seed ' + sd + ' year ' + t + ': hook ' + d.pov + ', ' + d.med + ' engine ' + s['ppov_' + t][0] + ', ' + s['pmedW_' + t][0]);
    }
    if (rec.y[T - 1].wtMed !== s.wtMedE[0]) throw new Error(nm + ' seed ' + sd + ': weighted median ' + rec.y[T - 1].wtMed + ' engine ' + s.wtMedE[0]);
    const lrH = h => { const z = {}; for (let t = 0; t < h; t++) Object.keys(rec.y[t].lr).forEach(k => { const c = z[k] = z[k] || [0, 0]; c[0] += rec.y[t].lr[k][0]; c[1] += rec.y[t].lr[k][1]; }); return z; };
    const all = Object.values(lrH(T)).reduce((x, c) => [x[0] + c[0], x[1] + c[1]], [0, 0]), f0 = all[1]/all[0]*100;
    if (Math.abs(f0 - s.fgt0PY[0]) > 1e-9*Math.max(1, Math.abs(f0))) throw new Error(nm + ' seed ' + sd + ': basket poverty by status sums to ' + f0 + ', engine fgt0PY ' + s.fgt0PY[0]);
    if (nm === 'none') base.y = rec.y;
    const o = {}; ['pov', 'med', 'lf'].concat(nm === 'none' ? [] : ['povN', 'povU', 'medN', 'medU']).forEach(k => { o[k] = rec.y.map(d => r7(d[k])); });
    SNAP.filter(t => t < T).forEach(t => { const d = rec.y[t], z = {wtMed: r7(d.wtMed)};
      if (nm !== 'none') Object.assign(z, {wtMedN: r7(d.wtMedN), wtMedU: r7(d.wtMedU), nM: d.nM, gap: r7(d.gap), eN: r7(d.eN), eR: r7(d.eR), eU: r7(d.eU), fifth: d.fifth});
      o['y' + (t + 1)] = z; });
    o.endoAnn = r7(s.endoAnn[0]);
    [20, 40].filter(h => h <= T).forEach(h => { o['lr' + h] = lrH(h); });
    o.fgt0PY = r7(s.fgt0PY[0]);
    out[nm] = o;
  });
  return hooked ? out : keys;
}

function withEngine(f) { const svS = RUNSET = H.startRelease(), svN = svS.svN, svG = svS.svG; try { return f(); } finally { H.resetNR6(svN); H.tbSetG(svG); } }

/* --check: the hook changes no output (seed 1, Reference, 20 years: every key of the three rows, with and without the hook) */
function check() {
  const P = Object.assign({}, H.FULL_INTEGRATION, {years: 20, nAgents: 500});
  const a = withEngine(() => runSeed(P, 1, false)), bad = []; let nk = 0;
  const b = {}; withEngine(() => { rowsFor(P).forEach(([nm, cfg]) => { let R; H.setRepHook(function () {}); try { R = H.tbStudy([cfg], 1, P, H.r2MainStudy(), 1); } finally { H.setRepHook(null); } b[nm] = R[0]._s; }); });
  Object.keys(a).forEach(nm => Object.keys(a[nm]).forEach(k => { nk++; const x = Array.from(a[nm][k]), y = b[nm][k] ? Array.from(b[nm][k]) : null;
    if (!y || x.some((v, j) => !(v === y[j] || (isNaN(v) && isNaN(y[j]))))) bad.push(nm + ' ' + k); }));
  console.log('check: ' + nk + ' row-keys, seed 1, Reference, 20 years, with and without a hook: ' + (bad.length ? bad.length + ' DIFFER: ' + bad.slice(0, 20).join(', ') : 'all identical'));
  const t0 = Date.now(); withEngine(() => runSeed(P, 1, true));
  console.log('check: the traced seed reproduces ppov_t, pmedW_t, wtMedE and fgt0PY in all three rows (' + ((Date.now() - t0)/1000).toFixed(1) + ' s)');
  return bad.length;
}

if (require.main === module) {
  if (process.argv.includes('--check')) process.exit(check() ? 1 : 0);
  const env = process.argv[2], years = +arg('years', '40'), sd = arg('seeds', '1-500').split('-').map(Number);
  if (!ENVN[env]) { console.error('usage: s64_erosion.js ref|adv|str [--years=40] [--seeds=A-B] [--out=FILE]'); process.exit(1); }
  const P = Object.assign({}, H[ENVN[env]], {years, nAgents: 500}), t0 = Date.now(), seeds = {};
  withEngine(() => { for (let s = sd[0]; s <= sd[1]; s++) seeds[s] = runSeed(P, s, true); });
  const out = {_meta: {what: 'S64 part 3 erosion trace (research-update prereg/2026-11-s63-round2-freeze.md, Amendment 4)', env, years, seeds: sd, manifest: H.runManifest(),
    command: 'node dev/tools/s64_erosion.js ' + process.argv.slice(2).join(' '), seconds: Math.round((Date.now() - t0)/1000)}, seeds};
  const file = arg('out', path.join(ROOT, 'dev', 'runs', 's64-erosion', 'raw', 'ero-' + env + '-' + years + '-' + sd.join('-') + '.json.gz'));
  fs.mkdirSync(path.dirname(file), {recursive: true}); fs.writeFileSync(file, zlib.gzipSync(JSON.stringify(RUNSET.withSettings(out))));
  console.log('wrote ' + file + ' (' + out._meta.seconds + ' s)');
}
module.exports = {rowsFor, runSeed};
