#!/usr/bin/env node
/* S66 (Nov 10, 2026; research-update prereg/2026-11-s66-low-share-trace.md): the trace of the low end of S55's fixed-share curve, the erosion of opening
 * balances, and the wealth harm with adults outside the labour force. No engine change: index.html is not edited.
 *
 * How it reads the run. The tool builds its own copy of the script harness.js runs (harness.js builtSource(): the page's engine, then the harness code),
 * adds a read-only probe at the end, and runs that copy in its own scope. The probe reads the engine's year accumulators (TB.cur), the surplus split's
 * accumulators (SPS.acc), each run's price path, and each adult's price cuts (one call inserted before the testbed's price-cut accounting that only
 * records mlc x (1 - cfPTF), mlc x (cfPTF - cfPreCCO), mlc x (cfPreCCO - cf)). It draws nothing and writes nothing any rule reads. Check 1 (--check)
 * proves the copy gives the harness's own outputs exactly.
 * The switch-offs (prereg, Part A): K1 CFG.PTFS_LOW_DENS = 0; K2 the PTF damping line does not run; K3 the row option pw {conversion: true}; K4 the
 * surplus split reads the share 0.10 (s66W(a, 'split')); K5 the PTF price cut's scale and the forgone-profit accounting read 0.10 (s66W(a, 'cut')).
 * K2, K4 and K5 are exact text substitutions in the tool's copy, each asserted to match exactly once.
 *
 * Usage: node dev/tools/s66_trace.js --check
 *        node dev/tools/s66_trace.js A|B|C ENV [--seeds=1-100] [--out=FILE]   (ENV ref, adv or st; writes dev/runs/s66-trace/s66-PART-ENV.json.gz) */
const fs = require('fs'), path = require('path'), zlib = require('zlib'), vm = require('vm');
const ROOT = path.join(__dirname, '..', '..'), H = require(path.join(ROOT, 'harness.js'));
const arg = (k, d) => { const a = process.argv.find(x => x.startsWith('--' + k + '=')); return a ? a.slice(k.length + 3) : d; };
const ENVN = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'};

/* ---- the tool's copy of the engine, with the probe ---- */
const PATCH = [  /* [what, exact text, replacement] */
  ['K2 damping', 'if(p.ptf&&inflRate>0&&!(PRICE&&PRICE.noDamp))inflRate*=', 'if(p.ptf&&inflRate>0&&!(PRICE&&PRICE.noDamp)&&S66.K.damp)inflRate*='],
  ['K5 cut scale', 'if (PAS && !full) c = paW(a)*Math.min(0.95, c);', 'if (PAS && !full) c = s66W(a, \'cut\')*Math.min(0.95, c);'],
  ['K5 forgone profit', 'PAS?mainLoopCostUSD*(fSA*COST.food+hSA*COST.util)*paW(a):', 'PAS?mainLoopCostUSD*(fSA*COST.food+hSA*COST.util)*s66W(a,\'cut\'):'],
  ['K4 price pool base', 'if(spPw)e*=paW(a);', 'if(spPw)e*=s66W(a,\'split\');'],
  ['K4 private BU', 'vBu=PAS?(bp?Math.max(0,a._spBU||0)*(1-paW(a)):0)', 'vBu=PAS?(bp?Math.max(0,a._spBU||0)*(1-s66W(a,\'split\')):0)'],
  ['K4 private essentials', 'if(PAS)vE*=1-paW(a);', 'if(PAS)vE*=1-s66W(a,\'split\');'],
  ['K4 PTF part', 'FWS.next.bizBUptf=(FWS.next.bizBUptf||0)+fwB*paW(a)', 'FWS.next.bizBUptf=(FWS.next.bizBUptf||0)+fwB*s66W(a,\'split\')'],
  ['probe: price cuts', '    var tbG=0,tbPT=0;if(tbY&&COST', '    if(S66.on)S66.cut.set(a,[mainLoopCostUSD*(1-cfPTF),mainLoopCostUSD*(cfPTF-cfPreCCO),mainLoopCostUSD*(cfPreCCO-cf)]);var tbG=0,tbPT=0;if(tbY&&COST']];
const PROBE = `
var S66 = {on:false, K:{damp:true, split:null, cut:null}, cut:new Map(), runs:[], full:false};
function s66W(a, k){ return S66.K[k] !== null ? S66.K[k] : paW(a); }
var s66Core = tbRunCore;
tbRunCore = function(p, seed, o, S, tau0, yMax){ var watched = S66.on && REP_HOOK !== null && yMax === p.years, f0 = S66.full; S66.full = watched;
  try { var r = s66Core.apply(this, arguments); if (watched) S66.runs.push(r.path.map(function(q){ return {U:q.U, Y:q.Y, idx:q.full, PG:q.PG, bIdx:q.bIdx}; })); return r; }
  finally { S66.full = f0; } };
module.exports._s66 = {S66:S66, tb:function(){ return TB; }, sps:function(){ return SPS; }, CFG:CFG};
`;
function engineCopy() {
  let src = H.builtSource();
  PATCH.forEach(([w, a, b]) => { const n = src.split(a).length - 1; if (n !== 1) throw new Error('patch "' + w + '" matches ' + n + ' times'); src = src.replace(a, () => b); });
  const mod = {exports: {}};
  vm.runInThisContext('(function (require, module, exports, __dirname, __filename, builtSource, csEngineSource) {' + src + '\n' + PROBE + '\n})', {filename: 's66-engine-copy.js'})
    (require, mod, mod.exports, ROOT, path.join(ROOT, 'harness.js'), H.builtSource, H.csEngineSource);
  return mod.exports;
}

/* ---- rows, as runner/jobs/program.js builds them ---- */
const SN = {abawd: true, slope: true}, LT = {lt: {s: 'all', m: 'all'}};
function rowsFor(E, P, part) {
  const pair = () => E.relMainCfgs(E.tbPresets(P)).map(c => Object.assign(c, {sc: E.SPEND_SOURCED, sn: SN})).map(c => E.frozenRow(c)), out = [];
  const add = (nm, c, k) => { Object.assign(c, JSON.parse(JSON.stringify(LT))); out.push({nm, c, k: k || null}); };
  if (part === 'A') {
    add('none', pair()[0]); add('members', E.c22Design(pair()[1]));
    [5, 10, 15, 20, 25, 30, 35, 40, 50].forEach(q => { const c = E.c22Design(pair()[1]); c.pa = {fix: q/100}; add('fix' + q, c); });
    ['K1', 'K2', 'K3', 'K4', 'K5'].forEach(k => [10, 20, 30, 40].forEach(q => { const c = E.c22Design(pair()[1]); c.pa = {fix: q/100}; if (k === 'K3') c.pw = {conversion: true}; add(k + '.fix' + q, c, k); }));
  }
  if (part === 'A40') { add('none', pair()[0]); add('members', E.c22Design(pair()[1])); [10, 20, 30, 40].forEach(q => { const c = E.c22Design(pair()[1]); c.pa = {fix: q/100}; add('fix' + q, c); }); }
  if (part === 'B') { add('none', pair()[0]); add('rls', pair()[1]); add('c22', E.c22Design(pair()[1])); }
  if (part === 'C') { [['', {}], ['lf.', {lf: {}}]].forEach(([t, o]) => { const p0 = pair(); add(t + 'none', Object.assign(p0[0], o)); add(t + 'c22', Object.assign(E.c22Design(p0[1]), JSON.parse(JSON.stringify(o)))); }); }
  return out;
}
const SO = E => Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: E.SPEND_SOURCED}, E.REL_V52_STUDY);
function setK(E, k) { const S = E._s66.S66; S.K.damp = k !== 'K2'; S.K.split = k === 'K4' ? 0.10 : null; S.K.cut = k === 'K5' ? 0.10 : null; E._s66.CFG.PTFS_LOW_DENS = k === 'K1' ? 0 : 0.40; }

/* ---- one run's record, year by year ---- */
const BANDS = 20, BW = 2500, SNAP = [4, 9, 14, 19, 39];
function median(v) { if (!v.length) return 0; const s = Float64Array.from(v).sort(), h = (s.length - 1)/2; return (s[Math.floor(h)] + s[Math.ceil(h)])/2; }
function newRec() { return {y: [], adults: null, w0: null}; }
function hookFor(E, rec, part) {
  const S = E._s66.S66, L = E._s66.CFG.POVERTY_LINE;
  let accPrev = null;
  return function (agents, yr, T, lf) {
    if (!S.full) return;  /* the one-year run that sets the starting tax rate is not traced */
    if (yr === 0) { accPrev = null; rec.w0 = agents.map(a => a.yrWealthStartUSD); rec.id = agents.map((a, j) => a._id !== undefined ? a._id : j); }
    const C = E._s66.tb().cur, sp = E._s66.sps(), A = sp && sp.acc ? {pool: sp.acc.pool || 0, own: sp.acc.own || 0, privP: sp.acc.privP || 0, ptf: sp.acc.ptf || 0, pricePool: sp.acc.pricePool || 0, reinv: sp.acc.reinv || 0, rest: sp.acc.rest || 0} : null;
    const n = agents.length, i0 = C.idx || 1, d = {};
    d.lf = lf; d.pay = (C.bu + C.conv)/i0/n; d.bu = C.bu/i0/n; d.conv = C.conv/i0/n; d.ctax = (C.ctax || 0)/i0/n; d.convM = (C.convM || 0)/i0/n; d.cutPT = (C.cutPT || 0)/i0/n;
    if (A) { const P = accPrev || {}; Object.keys(A).forEach(k => { d['sp_' + k] = (A[k] - (P[k] || 0))/n; }); accPrev = A; }
    let nCut = 0, sCut = 0, sPth = 0, sBuR = 0, rW = [], nW = [], debt = 0, debtS = 0, pov = 0, near = 0, wage = 0, conv = 0, disp = 0, cost = 0, spend = 0;
    const band = new Float64Array(BANDS + 1);
    agents.forEach(a => {
      const c = S.cut.get(a) || [0, 0, 0]; if (c[0] > 1e-9) { nCut++; sCut += c[0]/lf; } sPth += c[1]/lf; sBuR += c[2]/lf;
      const w = a.wealth, r = w/lf; rW.push(r); nW.push(w); if (w < 0) { debt++; debtS += -r; } if (w < L*lf) pov++; if (Math.abs(r - L) < 5000) near++;
      if (r >= 0 && r < BANDS*BW) band[Math.floor(r/BW)]++; else if (r >= BANDS*BW) band[BANDS]++;
      wage += (a.yrWageUSD || 0)/lf; conv += (a.yrConvUSD || 0)/lf; disp += (a._tbDisp || 0)/lf; cost += (a.yrCostUSD || 0)/lf;
      spend += ((a.yrWealthStartUSD || 0) + (a._tbDisp || 0) - w)/lf; });
    Object.assign(d, {cutN: nCut/n*100, cutPer: nCut ? sCut/nCut : 0, cutPtfPA: sCut/n, cutPthPA: sPth/n, buRelPA: sBuR/n, wage: wage/n, convI: conv/n, disp: disp/n, cost: cost/n, spend: spend/n,
      rMean: rW.reduce((s, x) => s + x, 0)/n, rMed: median(rW), nMean: nW.reduce((s, x) => s + x, 0)/n, nMed: median(nW), debt: debt/n*100, debtMean: debt ? debtS/debt : 0, pov: pov/n*100, near: near/n*100});
    if (SNAP.indexOf(yr) >= 0) d.band = Array.from(band, x => x/n*100);
    rec.y[yr] = d;
    if (part !== 'A' && part !== 'A40' && yr === T - 1) rec.adults = agents.map((a, j) => ({id: a._id !== undefined ? a._id : j, wEnd: a.wealth, lf: a._lf || null,
      wage: (a.yrWageUSD || 0)/lf, conv: (a.yrConvUSD || 0)/lf, disp: (a._tbDisp || 0)/lf, cost: (a.yrCostUSD || 0)/lf}));
    S.cut.clear();
  };
}

/* ---- a block: one environment, one part, a range of seeds; rows run seed by seed as tbStudy runs them ---- */
function runPart(E, part, env, lo, hi) {
  const years = part === 'A40' ? 40 : 20, P = Object.assign({}, E[ENVN[env]], {years, nAgents: 500}), rows = rowsFor(E, P, part), S = E._s66.S66, out = {};
  const svN = E.applyNR6(), svG = E.tbSetG(E.TB_PROFILE_G);
  try {
    S.on = true; const groups = {}; rows.forEach(r => { (groups[r.k || ''] = groups[r.k || ''] || []).push(r); });
    Object.keys(groups).forEach(k => {
      setK(E, k || null); const g = groups[k];
      for (let sd = lo; sd <= hi; sd++) {
        const recs = g.map(newRec); let ri = 0, cur = null;
        /* tbStudy runs the rows in order for the seed; each traced run advances ri at its last year */
        E.setRepHook(function (agents, yr, T, lf) { if (!S.full) return; if (yr === 0) cur = hookFor(E, recs[ri], part); cur(agents, yr, T, lf); if (yr === T - 1) ri++; });
        S.runs = [];
        let R; try { R = E.tbStudy(g.map(r => r.c), sd, P, SO(E), sd); } finally { E.setRepHook(null); }
        if (ri !== g.length || S.runs.length !== g.length) throw new Error('traced ' + ri + ' runs and ' + S.runs.length + ' paths for ' + g.length + ' rows');
        g.forEach((r, i) => { const o = out[r.nm] = out[r.nm] || {seeds: [], keys: {}}; const rec = recs[i];
          rec.path = S.runs[i]; ['pov', 'endoAnn', 'medWealthReal', 'cost', 'fgt0PY', 'bOAPy'].forEach(q => { (o.keys[q] = o.keys[q] || []).push(R[i]._s[q] ? R[i]._s[q][0] : null); });
          o.seeds.push(compact(rec)); });
      }
    });
  } finally { S.on = false; setK(E, null); E.resetNR6(svN); E.tbSetG(svG); }
  return out;
}
function r4(x) { return typeof x === 'number' && isFinite(x) ? +x.toPrecision(7) : x; }
function compact(rec) {  /* year arrays per measure */
  const o = {}, ks = Object.keys(rec.y[0]);
  ks.forEach(k => { o[k] = rec.y.map(d => d && d[k] !== undefined ? (Array.isArray(d[k]) ? d[k].map(r4) : r4(d[k])) : null); });
  o.U = rec.path.map(q => r4(q.U/(q.idx || 1)/500)); o.UY = rec.path.map(q => r4(q.Y > 0 ? q.U/q.Y*100 : 0));
  if (rec.adults) { o.adults = rec.adults.map((a, j) => [a.id, r4(rec.w0[j]), r4(a.wEnd), a.lf, r4(a.wage), r4(a.conv), r4(a.disp), r4(a.cost)]); o.lfEnd = r4(rec.y[rec.y.length - 1].lf); }
  return o;
}

/* ---- check 1: the copy reproduces the harness exactly (seeds 1-5, every Part A row at 20 years in Reference); check 2: K2 = main in Reference ---- */
function check() {
  const E = engineCopy(), P = Object.assign({}, H.FULL_INTEGRATION, {years: 20, nAgents: 500}), bad = [];
  const rowsE = rowsFor(E, P, 'A').filter(r => !r.k), rowsH = rowsFor(H, P, 'A').filter(r => !r.k);
  const run = (M, rows, probe) => { const svN = M.applyNR6(), svG = M.tbSetG(M.TB_PROFILE_G); if (probe) { M._s66.S66.on = true; M.setRepHook(function () {}); }
    try { return M.tbStudy(rows.map(r => r.c), 5, P, SO(M)); } finally { if (probe) { M._s66.S66.on = false; M.setRepHook(null); } M.resetNR6(svN); M.tbSetG(svG); } };
  const a = run(H, rowsH, false), b = run(E, rowsE, true);
  let nk = 0; rowsH.forEach((r, i) => Object.keys(a[i]._s).forEach(k => { nk++; const x = Array.from(a[i]._s[k]), y = b[i]._s[k] ? Array.from(b[i]._s[k]) : null;
    if (!y || x.some((v, j) => !(v === y[j] || (isNaN(v) && isNaN(y[j]))))) bad.push(r.nm + ' ' + k); }));
  console.log('check 1: ' + nk + ' row-keys compared, seeds 1-5, Reference, 20 years: ' + (bad.length ? bad.length + ' DIFFER: ' + bad.slice(0, 20).join(', ') : 'all identical'));
  const k2 = rowsFor(E, P, 'A').filter(r => r.k === 'K2'), m = rowsFor(E, P, 'A').filter(r => !r.k && /^fix(10|20|30|40)$/.test(r.nm)); setK(E, 'K2');
  let c; try { c = run(E, k2, true); } finally { setK(E, null); }
  const d = run(E, m, true), bad2 = []; k2.forEach((r, i) => Object.keys(d[i]._s).forEach(k => { if (JSON.stringify(Array.from(d[i]._s[k])) !== JSON.stringify(Array.from(c[i]._s[k]))) bad2.push(r.nm + ' ' + k); }));
  console.log('check 2: K2 against the main reading in Reference: ' + (bad2.length ? bad2.length + ' DIFFER: ' + bad2.slice(0, 10).join(', ') : 'identical on every key'));
  return bad.length + bad2.length;
}

if (require.main === module) {
  if (process.argv.includes('--check')) process.exit(check() ? 1 : 0);
  const part = process.argv[2], env = process.argv[3], sd = arg('seeds', '1-100').split('-').map(Number);
  if (!['A', 'A40', 'B', 'C'].includes(part) || !ENVN[env]) { console.error('usage: s66_trace.js A|A40|B|C ref|adv|st [--seeds=1-100]'); process.exit(1); }
  const t0 = Date.now(), E = engineCopy(), rows = runPart(E, part, env, sd[0], sd[1]);
  const out = {_meta: {what: 'S66 trace (research-update prereg/2026-11-s66-low-share-trace.md)', part, env, seeds: sd, manifest: H.runManifest(), patches: PATCH.map(p => p[0]),
    command: 'node dev/tools/s66_trace.js ' + process.argv.slice(2).join(' '), seconds: Math.round((Date.now() - t0)/1000)}, rows};
  const file = arg('out', path.join(ROOT, 'dev', 'runs', 's66-trace', 's66-' + part + '-' + env + '-' + sd.join('-') + '.json.gz'));
  fs.mkdirSync(path.dirname(file), {recursive: true}); fs.writeFileSync(file, zlib.gzipSync(JSON.stringify(out)));
  console.log('wrote ' + file + ' (' + out._meta.seconds + ' s)');
}
module.exports = {engineCopy, rowsFor, runPart};
