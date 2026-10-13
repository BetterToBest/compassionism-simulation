#!/usr/bin/env node
/* Session 2a (Oct 13, 2026; dev/reports/v5-25-health-today.md): the health settings' paired check. For each variant, the v5.4 release row and its no-programme
 * run, both with the variant's health setting, paired by seed. Reports both runs' levels, the programme's paired effect, and, against the variant's reference
 * (no health setting for setting A rows; setting A for setting B and C rows), how far the variant moves that effect (the difference of the paired effects,
 * seed by seed, with a 95% interval): for B and C rows, the health and Compassionism interaction (how much the programme's effect changes when that setting
 * replaces today's system). Each row also gives the paired difference of its levels from the reference's, in the no-programme run (baseVsRef) and the
 * programme run (progVsRef).
 * Session 2b (dev/reports/v5-27-health-financing.md): setting C (single payer with a private layer and Medicaid kept), the benefit-cliff variants (countBU),
 * PTF's health-sector cut at 0.25 (ptf), today's safety net (sn), the share of setting B's savings each setting C row erodes, the public costs avoided with
 * the emergency-room part counted once, and the time per run.
 * Session 2c (dev/reports/v5-28-safety-net-grid.md): the six-cell grid with today's safety net on in every cell (ledger decision d192; --grid runs off, A, ASN,
 * BSN, CSN: settings A, B and C, each without and with the programme, plus the no-programme, no-safety-net reference line), government's share under B and C
 * fixed at its no-programme level (d194; HEALTH.gov 'fixed', the default) with the floating share as sensitivity rows (*fl), the prevention link (prev), and
 * each cell's costs beside its results (costs: programme cost, health tax, household health bill, safety-net outlays, government's share, private-layer overpayment).
 * Usage: node dev/tools/health_check.js ref|adv|st [SEEDS] [--rows=off,A,Anx,B,...] [--grid] [--out=NAME] [--theta=X] [--thetaX=K] [--flat] [--lo=FIRST] [--dump]
 *        node dev/tools/health_check.js ref|adv|st SEEDS --merge=PIECE1,PIECE2,... [--out=NAME]
 * Outside audit (Oct 13, 2026; dev/reports/v5-29-outside-audit.md): --lo=FIRST runs seeds FIRST..SEEDS (the Runpod pieces); --dump also writes each run's
 * per-seed values (NAME-ENV.seeds.json); --merge joins such pieces (same environment, rows and price options; together seeds 1..SEEDS, each once) and
 * writes the same summary one process would have (seeds are paired, so splitting changes no figure). --thetaX=K multiplies every essentials' price response.
 * --theta=X sets the medical price response to extra demand (PM_DEFAULTS.theta.medical, 0.5 as released) in every row; --flat holds prices flat (pass-through 0,
 * every essentials' response 0): the difference between a run with prices free and one with --flat is the part that comes through prices.
 * Output: dev/runs/health/NAME-ENV.json (NAME defaults to 'check'). */
'use strict';
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const arg = k => { const a = process.argv.find(x => x.startsWith('--' + k + '=')); return a ? a.split('=')[1] : null; };
const pos = process.argv.slice(2).filter(x => !x.startsWith('--'));
const env = pos[0] || 'ref', N = +(pos[1] || 20), LO = +(arg('lo') || 1), NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
if (!NAME || !(LO >= 1 && N - LO >= 1)) { console.error('usage: health_check.js ref|adv|st [SEEDS >= 2] [--rows=off,A,...]'); process.exit(1); }
/* The variants: hl, the row option hl (undefined = the health setting off); sn, today's safety net (row option sn); ptf, PTF's rate for health care, transport and
 * childcare (v54 ptfs.other; 0 as released); ref, the row its programme effect is compared with (default: A for setting B and C rows, off otherwise). */
const VAR = {off: {}, A: {hl: {}}, Anx: {hl: {exp: false}}, Askip25: {hl: {skip: 0.25}}, Askip75: {hl: {skip: 0.75}}, Apers80: {hl: {persist: 0.8}}, Apers95: {hl: {persist: 0.95}},
  B: {hl: {set: 'B'}}, Bcau: {hl: {set: 'B', cs: 'cautious'}}, Bhigh: {hl: {set: 'B', cs: 'high'}}, Bnx: {hl: {set: 'B', exp: false}}, Bcap25: {hl: {set: 'B', cap: 0.25}}, Bcap100: {hl: {set: 'B', cap: 1}},
  Badm0: {hl: {set: 'B', adm: 0}}, Badm2: {hl: {set: 'B', adm: 0.02}}, Bind0: {hl: {set: 'B', induce: 0}},
  /* session 2b, setting C: the payment gap (coding intensity: 0, MedPAC 2026's 4%, MedPAC 2025's 8%) and selection (half, MedPAC's 11%, one and a half times) */
  C: {hl: {set: 'C'}}, Cg0: {hl: {set: 'C', gap: 0}}, Cg8: {hl: {set: 'C', gap: 0.08}}, Cs55: {hl: {set: 'C', sel: 0.055}}, Cs165: {hl: {set: 'C', sel: 0.165}},
  Clow: {hl: {set: 'C', gap: 0, sel: 0.055}}, Chigh: {hl: {set: 'C', gap: 0.08, sel: 0.165}}, Cnx: {hl: {set: 'C', exp: false}},
  /* session 2b, the benefit cliff: the BU counted as income in the Medicaid test */
  AbuY: {hl: {countBU: true}}, BbuY: {hl: {set: 'B', countBU: true}, ref: 'AbuY'}, CbuY: {hl: {set: 'C', countBU: true}, ref: 'AbuY'},
  /* session 2b, PTF's health-sector cut at 0.25 (the ptfs25 reading): under B and C it lowers the plan's costs, not the household's */
  Aptf25: {hl: {}, ptf: 0.25}, Bptf25: {hl: {set: 'B'}, ptf: 0.25, ref: 'Aptf25'}, Cptf25: {hl: {set: 'C'}, ptf: 0.25, ref: 'Aptf25'}, ptf25: {ptf: 0.25},
  /* session 2b, today's safety net (SNAP, EITC, the refundable CTC) */
  SN: {sn: {}}, SN130: {sn: {gross: 1.3}},
  /* session 2c, the grid (d192): today's safety net in every cell. ASN's reference is A (the safety net's own effect under today's system; session 2b compared it with
   * no health setting, which folded in setting A's own effect); BSN's and CSN's is ASN (the health and Compassionism interaction, both with the safety net) */
  ASN: {hl: {}, sn: {}, ref: 'A'}, BSN: {hl: {set: 'B'}, sn: {}, ref: 'ASN'}, CSN: {hl: {set: 'C'}, sn: {}, ref: 'ASN'},
  /* session 2c, government's share floating (session 2b's behaviour, d194's sensitivity row) */
  Bfl: {hl: {set: 'B', gov: 'float'}}, Cfl: {hl: {set: 'C', gov: 'float'}}, BSNfl: {hl: {set: 'B', gov: 'float'}, sn: {}, ref: 'ASN'}, CSNfl: {hl: {set: 'C', gov: 'float'}, sn: {}, ref: 'ASN'},
  BbuYfl: {hl: {set: 'B', countBU: true, gov: 'float'}, ref: 'AbuY'}, CbuYfl: {hl: {set: 'C', countBU: true, gov: 'float'}, ref: 'AbuY'},
  /* session 2c, the prevention link (s141) at its central (pv) and high (pvh) cases, in the grid's cells (the zero case is the switch off: ASN, BSN, CSN). ASNpv's
   * reference is ASN (how far the link moves the programme's effect under today's system); BSNpv's and CSNpv's is ASNpv (the interaction, with the link on in both) */
  ASNpv: {hl: {}, sn: {}, pv: H.PREV_CASES.central, ref: 'ASN'}, BSNpv: {hl: {set: 'B'}, sn: {}, pv: H.PREV_CASES.central, ref: 'ASNpv'}, CSNpv: {hl: {set: 'C'}, sn: {}, pv: H.PREV_CASES.central, ref: 'ASNpv'},
  ASNpvh: {hl: {}, sn: {}, pv: H.PREV_CASES.high, ref: 'ASN'}, BSNpvh: {hl: {set: 'B'}, sn: {}, pv: H.PREV_CASES.high, ref: 'ASNpvh'}, CSNpvh: {hl: {set: 'C'}, sn: {}, pv: H.PREV_CASES.high, ref: 'ASNpvh', bref: 'BSNpvh'},
  /* outside audit (Oct 13, 2026; dev/reports/v5-29-outside-audit.md), all with today's safety net: single payer's cautious and high cost cases (the Yale saving is an
   * input, so its range sits beside the central case); setting C's private layer at 25% and 75% enrolment (Medicare Advantage's 55% is an analogue, not an
   * estimate for all ages); its payment factor with no overpayment (diagnostic), coding high with selection central (1.08 x 1.11, 19.9%) and both high
   * (1.08 x 1.165, 25.8%, a stress case); today's safety net at low and high take-up (design values around USDA's 88% and IRS's 80.8%). bref: the setting B
   * row a setting C row's erosion of B's savings is measured against (default B, or BSN for rows with the safety net) */
  BSNcau: {hl: {set: 'B', cs: 'cautious'}, sn: {}, ref: 'ASN'}, BSNhigh: {hl: {set: 'B', cs: 'high'}, sn: {}, ref: 'ASN'},
  CSNcau: {hl: {set: 'C', cs: 'cautious'}, sn: {}, ref: 'ASN', bref: 'BSNcau'}, CSNhigh: {hl: {set: 'C', cs: 'high'}, sn: {}, ref: 'ASN', bref: 'BSNhigh'},
  CSNp25: {hl: {set: 'C', priv: 0.25}, sn: {}, ref: 'ASN'}, CSNp75: {hl: {set: 'C', priv: 0.75}, sn: {}, ref: 'ASN'},
  CSNx0: {hl: {set: 'C', gap: 0, sel: 0}, sn: {}, ref: 'ASN'}, CSNg8: {hl: {set: 'C', gap: 0.08}, sn: {}, ref: 'ASN'}, CSNx26: {hl: {set: 'C', gap: 0.08, sel: 0.165}, sn: {}, ref: 'ASN'},
  ASNtLo: {hl: {}, sn: {snapTake: 0.75, taxTake: 0.70}, ref: 'A'}, ASNtHi: {hl: {}, sn: {snapTake: 0.95, taxTake: 0.90}, ref: 'A'}};
VAR.CSNfl.bref = 'BSNfl'; VAR.CSNpv.bref = 'BSNpv';
const REF = v => VAR[v].ref || (VAR[v].hl && (VAR[v].hl.set === 'B' || VAR[v].hl.set === 'C') ? (VAR[v].hl.exp === false ? 'Anx' : 'A') : 'off');
const GRID = 'off,A,ASN,BSN,CSN';  /* session 2c: the six cells (A, B, C with the safety net, each without and with the programme) and the reference line (off) */
const rows = (process.argv.includes('--grid') ? GRID + (arg('rows') ? ',' + arg('rows') : '') : arg('rows') || 'off,A,Anx').split(',').filter((v, i, a) => a.indexOf(v) === i);
rows.forEach(v => { if (!(v in VAR)) { console.error('unknown variant ' + v + ' (known: ' + Object.keys(VAR).join(', ') + ')'); process.exit(1); } });
for (let i = 0; i < rows.length; i++) { const r = REF(rows[i]); if (rows.indexOf(r) < 0) { rows.splice(i, 0, r); i = -1; } }  /* every row's reference runs first */
rows.sort((a, b) => (a === 'off' ? -1 : 0) - (b === 'off' ? -1 : 0));
const ROOT = path.join(__dirname, '..', '..'), t0 = Date.now(), SC = H.SPEND_SOURCED, C = H.CFG;
const K = ['fgt0PY', 'fgt1PY', 'fgt2PY', 'pov', 'bOAPy', 'hhCostKidPY', 'hhWlthKidPY', 'cost', 'medWealthReal', 'pLev20', 'giniD', 'hrs'];
/* session 2c: each cell's costs beside its results, per adult-year (year-0 $) unless noted: programme cost (cost), health tax (hlTax), household health bill (hlPaid:
 * under A premiums and out-of-pocket cost; under B and C the tax less the returned employer share), safety-net outlays (snAll), government's share of the plan (hlGovB),
 * the public plan's spending per person-year (hlSB), the private layer's payments above its enrollees' public cost per person-year (hlXtra) */
const KC = ['cost', 'hlTax', 'hlPaid', 'snAll', 'hlGovB', 'hlSB', 'hlXtra'];
const KH = H.HL_KEYS, KS = H.SN_KEYS;
const TX = arg('thetaX') !== null ? +arg('thetaX') : null, T0 = H.PM_DEFAULTS.theta;
const FLAT = process.argv.includes('--flat'), PMX = FLAT ? {lamG: 0, theta: {food: 0, housing: 0, medical: 0}} : arg('theta') !== null ? {theta: {medical: +arg('theta')}}
  : TX !== null ? {theta: {food: T0.food*TX, housing: T0.housing*TX, medical: T0.medical*TX}} : {};
const MERGE = arg('merge'), DUMP = process.argv.includes('--dump');
const wf0 = C.WEALTH_FLOOR; C.WEALTH_FLOOR = -10000;
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G);
const cmd = 'node dev/tools/health_check.js ' + env + ' ' + N + ' --rows=' + rows.join(',') + (arg('out') ? ' --out=' + arg('out') : '') + (LO > 1 ? ' --lo=' + LO : '') + (FLAT ? ' --flat' : TX !== null ? ' --thetaX=' + TX : PMX.theta ? ' --theta=' + arg('theta') : '');
const out = {_meta: {prev: H.PREV_CASES, what: 'health settings: the v5.4 release row and its no-programme run under each variant, paired by seed; vsRef: the change in the programme\'s paired effect against the reference row (A against off, B and C against A); baseVsRef, progVsRef: the paired difference of the levels from the reference row, without and with the programme; offProgVsBase (safety-net rows): the release row without the safety net against this row\'s no-programme run, paired; erodeB (setting C rows): the share of setting B\'s savings per person-year that the row loses, no programme; avoided: public costs avoided per adult-year (2025 $), main and high, with the emergency-room part counted once under B and C', env, seeds: N, manifest: H.runManifest(), command: cmd, health: H.HEALTH_DEFAULTS, snet: H.SNET_DEFAULTS}, rows: {}};
const r3 = x => +(+x).toFixed(3);
function pd(a, b, k){ const n = a._s[k].length; let m = 0, v = 0; const d = []; for (let i = 0; i < n; i++) d.push(a._s[k][i] - b._s[k][i]); d.forEach(x => { m += x/n; }); d.forEach(x => { v += (x - m)*(x - m)/(n - 1); }); const h = 1.96*Math.sqrt(v/n); return {m, lo: m - h, hi: m + h, d}; }
function ci(d){ const n = d.length; let m = 0, s = 0; d.forEach(x => { m += x/n; }); d.forEach(x => { s += (x - m)*(x - m)/(n - 1); }); const h = 1.96*Math.sqrt(s/n); return [r3(m), r3(m - h), r3(m + h)]; }
try {
  const P = Object.assign({}, H[NAME]), PR = H.tbPresets(P), cfg = [];
  rows.forEach(v => { const M = H.relMainCfgs(PR), V = VAR[v], x = {};
    if (V.hl) x.hl = V.hl; if (V.sn) x.sn = V.sn; if (V.pv) x.pv = V.pv;
    if (V.ptf !== undefined) M.forEach(m => { m.v54 = Object.assign({}, m.v54, {ptfs: Object.assign({}, m.v54 && m.v54.ptfs, {other: V.ptf})}); });
    cfg.push(Object.assign(M[0], x), Object.assign(M[1], {sc: SC}, x)); });
  const t1 = Date.now(), opt = {flat: FLAT, theta: arg('theta'), thetaX: TX};
  let R;
  if (MERGE){  /* the pieces' per-seed values, joined in seed order; each mean is summed as tbStudy sums it (value/M, seed by seed) */
    const ps = MERGE.split(',').map(f => JSON.parse(fs.readFileSync(f, 'utf8'))).sort((a, b) => a._meta.lo - b._meta.lo);
    let next = 1; ps.forEach(q => { const m = q._meta;
      if (m.env !== env || m.rows.join() !== rows.join() || JSON.stringify(m.opt) !== JSON.stringify(opt) || m.lo !== next) throw new Error('piece ' + m.lo + '-' + m.N + ' does not fit (env, rows, price options or seed range)');
      next = m.N + 1; });
    if (next !== N + 1) throw new Error('the pieces cover seeds 1-' + (next - 1) + ', not 1-' + N);
    R = ps[0].R.map((_, i) => { const r = {_s: {}}; Object.keys(ps[0].R[i]).forEach(k => { const a = [].concat(...ps.map(q => q.R[i][k])); r._s[k] = a; r[k] = 0; a.forEach(x => { r[k] += x/N; }); }); return r; });
    out._meta.pieces = ps.map(q => ({seeds: q._meta.lo + '-' + q._meta.N, command: q._meta.command, manifest: q._meta.manifest, perRun: q._meta.perRun}));
    out._meta.perRun = ps[0]._meta.perRun;
  } else {
    R = H.tbStudy(cfg, N, P, Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: SC}, H.REL_V52_STUDY, PMX), LO);
    out._meta.perRun = +((Date.now() - t1)/1000/(cfg.length*(N - LO + 1))).toFixed(3);
    if (DUMP){ const KD = K.concat(KC, KH, KS).filter((k, i, a) => a.indexOf(k) === i);
      const dump = {_meta: {env, N, lo: LO, rows, opt, command: cmd + (DUMP ? ' --dump' : ''), manifest: H.runManifest(), perRun: out._meta.perRun},
        R: R.map(r => { const o = {}; KD.forEach(k => { if (r._s[k]) o[k] = Array.from(r._s[k]); }); return o; })};
      const dd = path.join(ROOT, 'dev', 'runs', 'health'); fs.mkdirSync(dd, {recursive: true});
      fs.writeFileSync(path.join(dd, (arg('out') || 'check') + '-' + env + '.seeds.json'), JSON.stringify(dump) + '\n'); }
  }  /* seconds per run (one row, one seed, 500 adults, 20 years; each run's one-year pre-pass for the tax rate included), one core */
  const at = {}; rows.forEach((v, i) => { at[v] = {B: R[2*i], M: R[2*i + 1]}; });
  const W = (r, b, hl) => { const g = (b.fgt1PY - r.fgt1PY)/100*C.LIVING_WAGE_ANNUAL, l = (b.fgt0PY - r.fgt0PY)/100, x = H.avoidWide(g, l), y = H.avoidWide(g, l, hl); return {main: r3(x.main), high: r3(x.high), mainOnce: r3(y.main), highOnce: r3(y.high)}; };
  rows.forEach((v, i) => { const B = R[2*i], M = R[2*i + 1], V = VAR[v], ref = v === 'off' ? null : REF(v), o = out.rows[v] = {hl: V.hl || null, sn: V.sn || null, pv: V.pv || null, ptf: V.ptf === undefined ? null : V.ptf, ref, base: {}, prog: {}, d: {}, vsRef: {}, baseVsRef: {}, progVsRef: {}};
    K.concat(V.hl ? KH : [], V.sn ? KS : []).forEach(k => { if (B[k] === undefined) return; const q = pd(M, B, k); o.base[k] = r3(B[k]); o.prog[k] = r3(M[k]); o.d[k] = [r3(q.m), r3(q.lo), r3(q.hi)];
      if (ref && at[ref].B[k] !== undefined){ const q0 = pd(at[ref].M, at[ref].B, k); o.vsRef[k] = ci(q.d.map((x, j) => x - q0.d[j])); o.baseVsRef[k] = ci(pd(B, at[ref].B, k).d); o.progVsRef[k] = ci(pd(M, at[ref].M, k).d); } });
    if (V.sn && !V.hl){ o.offProgVsBase = {}; K.forEach(k => { if (B[k] !== undefined) o.offProgVsBase[k] = ci(pd(at.off.M, B, k).d); }); }  /* Compassionism (the release row, no safety net) against this row's no-programme run */
    o.avoided = W(M, B, V.hl ? V.hl.set || 'A' : null);
    o.costs = {base: {}, prog: {}}; KC.forEach(k => { o.costs.base[k] = B[k] === undefined ? 0 : r3(B[k]); o.costs.prog[k] = M[k] === undefined ? 0 : r3(M[k]); });  /* session 2c */
    const bk = V.bref || (V.sn ? 'BSN' : 'B');  /* outside audit: the matching setting B row (session 2c's rows with the safety net had none) */
    if (V.hl && V.hl.set === 'C' && at[bk] && V.hl.exp !== false){ const b = at[bk].B, n = B._s.hlSB.length, e = []; for (let j = 0; j < n; j++) e.push((B._s.hlSB[j] - b._s.hlSB[j])/(b._s.hlSA[j] - b._s.hlSB[j])*100); o.erodeB = ci(e); } });
} finally { H.resetNR6(svN); H.tbSetG(svG); C.WEALTH_FLOOR = wf0; }
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const dir = path.join(ROOT, 'dev', 'runs', 'health'); fs.mkdirSync(dir, {recursive: true});
const file = path.join(dir, (arg('out') || 'check') + '-' + env + '.json');
fs.writeFileSync(file, JSON.stringify(out, null, 1) + '\n');
const f = x => (x >= 0 ? '+' : '') + (Math.abs(x) >= 100 ? x.toFixed(0) : x.toFixed(2));
console.log('health check, ' + env + ', seeds ' + LO + '-' + N + (MERGE ? ', merged' : '') + ' (' + out._meta.seconds + ' s; ' + out._meta.perRun + ' s per run) -> ' + path.relative(ROOT, file));
rows.forEach(v => { const o = out.rows[v]; console.log('[' + v + ']' + (o.erodeB ? '  erodes setting B\'s savings by ' + o.erodeB[0].toFixed(1) + '% [' + o.erodeB[1].toFixed(1) + ', ' + o.erodeB[2].toFixed(1) + ']' : ''));
  console.log('  costs (no programme / with it): ' + KC.map(k => k + ' ' + Math.round(o.costs.base[k]) + ' / ' + Math.round(o.costs.prog[k])).join(', '));
  Object.keys(o.base).forEach(k => console.log('  ' + k.padEnd(14) + String(o.base[k]).padStart(10) + ' -> ' + String(o.prog[k]).padEnd(10) + ' ' + f(o.d[k][0]) + ' [' + f(o.d[k][1]) + ', ' + f(o.d[k][2]) + ']' + (o.vsRef[k] ? '   vs ' + o.ref + ': ' + f(o.vsRef[k][0]) + ' [' + f(o.vsRef[k][1]) + ', ' + f(o.vsRef[k][2]) + ']; levels ' + f(o.baseVsRef[k][0]) + ' / ' + f(o.progVsRef[k][0]) : ''))); });
