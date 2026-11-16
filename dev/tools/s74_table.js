#!/usr/bin/env node
/* S74 pilot tables (research-update prereg/2026-11-s74-central-bank.md, "Analysis", "Decision rules", Amendment 1). Reads dev/runs/s74-pilot/s74-pilot-ENV.json
 * (dev/tools/s74_pilot.js) and writes tables.md and tables.json beside them. Nothing is run here.
 * Contrasts per environment and design, paired on seeds: E the programme's effect (programme minus no programme) in each arm; X the interaction (E with
 * the central bank on minus E with it off; History: off is 'infl', no central bank); C the central bank's effect (cb minus off) in each run.
 * Intervals: paired t at 95%, and Holm-adjusted across the five primary outcomes within each environment, design and family (E in the cb arm; X);
 * a paired bootstrap (2,000 replicates, fixed seed) beside them for P3 and P5. Usage: node dev/tools/s74_table.js [DIR] */
'use strict';
const fs = require('fs'), path = require('path');
const dir = process.argv[2] || path.join(__dirname, '..', 'runs', 's74-pilot');
const ENVS = ['hx', 'adv', 'st', 'ref'].filter(e => fs.existsSync(path.join(dir, 's74-pilot-' + e + '.json')));
const NAME = {hx: 'History (2005-2025)', adv: 'Adverse', st: 'Stress', ref: 'Reference'}, DNAME = {c22: 'C2.2', rel: 'release design'};
const PRIM = [['stP1', 'P1 spread of the basket price level\'s yearly change (points)'], ['stP2', 'P2 spread of yearly changes in real cash income ($, mean)'],
  ['stP3', 'P3 largest fall in real wealth ($, median)'], ['rkRecM', 'P4 years to recover from an income shock (mean)'], ['stP5', 'P5 % pushed below the basket line in a recession year']];
const SEC = ['fgt0PY', 'pov', 'endoAnn', 'stP1o', 'stP1p', 'stP2q1', 'stP2q3', 'stP2q5', 'stP3q1', 'stP3q3', 'stP3q5', 'stP3t1', 'stP5r', 'rkRec3', 'rkDdB', 'rkDdB30', 'rkDdW'];
const CBK = ['cbI', 'cbIst', 'cbFloor', 'cbQ', 'cbQmax', 'cbM', 'cbRfY', 'cbRfSh', 'cbU', 'cbA', 'cbN', 'cbF', 'cbR', 'fsQ', 'fsN', 'fsRec', 'fsOut', 'fsBuyG', 'fsGap',
  'fsS0', 'fsS1', 'fsS2', 'fsS3', 'fsS4', 'fsS5', 'fsS6', 'fsB0', 'fsB1', 'fsB2', 'fsB3', 'fsB4', 'fsB5', 'fsB6'];
/* Student t: the regularized incomplete beta (continued fraction), its CDF and quantile */
function lgam(x){ const c = [76.18009172947146, -86.50532032941677, 24.01409824083091, -1.231739572450155, 0.1208650973866179e-2, -0.5395239384953e-5]; let y = x, t = x + 5.5; t -= (x + 0.5)*Math.log(t); let s = 1.000000000190015; for (const k of c) s += k/++y; return -t + Math.log(2.5066282746310005*s/x); }
function betacf(a, b, x){ let qab = a + b, qap = a + 1, qam = a - 1, c = 1, d = 1 - qab*x/qap; d = 1/(Math.abs(d) < 1e-300 ? 1e-300 : d); let h = d;
  for (let m = 1; m <= 300; m++){ const m2 = 2*m; let aa = m*(b - m)*x/((qam + m2)*(a + m2)); d = 1 + aa*d; d = 1/(Math.abs(d) < 1e-300 ? 1e-300 : d); c = 1 + aa/c; c = Math.abs(c) < 1e-300 ? 1e-300 : c; h *= d*c;
    aa = -(a + m)*(qab + m)*x/((a + m2)*(qap + m2)); d = 1 + aa*d; d = 1/(Math.abs(d) < 1e-300 ? 1e-300 : d); c = 1 + aa/c; c = Math.abs(c) < 1e-300 ? 1e-300 : c; const del = d*c; h *= del; if (Math.abs(del - 1) < 3e-16) break; } return h; }
function ibeta(a, b, x){ if (x <= 0) return 0; if (x >= 1) return 1; const bt = Math.exp(lgam(a + b) - lgam(a) - lgam(b) + a*Math.log(x) + b*Math.log(1 - x)); return x < (a + 1)/(a + b + 2) ? bt*betacf(a, b, x)/a : 1 - bt*betacf(b, a, 1 - x)/b; }
function tP2(t, df){ return ibeta(df/2, 0.5, df/(df + t*t)); }  /* two-sided p */
function tQ(p2, df){ let lo = 0, hi = 1000; for (let i = 0; i < 200; i++){ const m = (lo + hi)/2; if (tP2(m, df) > p2) lo = m; else hi = m; } return (lo + hi)/2; }  /* the t with two-sided p = p2 */
function mulberry32(a){ return function(){ a |= 0; a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0)/4294967296; }; }
function pair(d){ const n = d.length, m = d.reduce((u, v) => u + v, 0)/n, sd = Math.sqrt(d.reduce((u, v) => u + (v - m)*(v - m), 0)/(n - 1)), se = sd/Math.sqrt(n), t = se > 0 ? m/se : (m === 0 ? 0 : Infinity);
  return {n, m, se, p: se > 0 ? tP2(Math.abs(t), n - 1) : (m === 0 ? 1 : 0), lo: m - tQ(0.05, n - 1)*se, hi: m + tQ(0.05, n - 1)*se}; }
function boot(d){ const r = mulberry32(20261115), n = d.length, B = []; for (let b = 0; b < 2000; b++){ let s = 0; for (let i = 0; i < n; i++) s += d[Math.floor(r()*n)]; B.push(s/n); } B.sort((x, y) => x - y); return [B[49], B[1949]]; }
function holm(rows){ const o = rows.map((r, i) => i).sort((i, j) => rows[i].p - rows[j].p), m = rows.length; let run = 0;
  o.forEach((i, k) => { const r = rows[i], a = 0.05/(m - k); run = Math.max(run, Math.min(1, r.p*(m - k))); r.pH = run; const q = r.se > 0 ? tQ(a, r.n - 1)*r.se : 0; r.loH = r.m - q; r.hiH = r.m + q; }); return rows; }
const get = (R, arm, row, k) => R[arm] && R[arm][row] && R[arm][row][k];
const diff = (a, b) => a && b ? a.map((x, i) => x - b[i]) : null;
const f = (x, d) => x === undefined || x === null || !isFinite(x) ? '-' : Math.abs(x) >= 1000 ? x.toFixed(0) : x.toFixed(d === undefined ? 2 : d);
const ci = r => f(r.m) + ' [' + f(r.lo) + ', ' + f(r.hi) + ']';
const word = (r, steadyNeg) => r.loH > 0 ? (steadyNeg ? 'less steady' : 'steadier') : r.hiH < 0 ? (steadyNeg ? 'steadier' : 'less steady') : 'no measurable difference';
const out = {_meta: {dir, envs: ENVS, made: new Date().toISOString()}}, md = ['# S74 pilot tables (100 seeds, frozen round-2 main row)', '',
  'Made by `node dev/tools/s74_table.js` from the pilot files in this folder (`node dev/tools/s74_pilot.js ENV 100`). Programme effect: programme minus no programme, paired on seeds. Interaction: the programme\'s effect with the central bank on minus with it off (History: off is no central bank). Intervals are 95% paired t; Holm-adjusted intervals (H) are across the five primary outcomes within each environment, design and family. For every primary outcome lower is steadier.', ''];
ENVS.forEach(env => { const D = JSON.parse(fs.readFileSync(path.join(dir, 's74-pilot-' + env + '.json'), 'utf8')), OFF = env === 'hx' ? 'infl' : 'off'; out[env] = {meta: D._meta};
  md.push('## ' + NAME[env], '', 'Engine: ' + (D._meta.manifest && (D._meta.manifest.commit || D._meta.manifest.engine || '')) + '; command `' + D._meta.command + '`; ' + D._meta.seeds + ' seeds.', '');
  D._meta.designs.forEach(d => { const R = D[d], o = out[env][d] = {}; md.push('### ' + DNAME[d], '');
    const fam = (label, mk) => { const rows = PRIM.map(([k, l]) => { const x = mk(k); if (!x) return null; const r = pair(x); r.k = k; r.l = l; if (k === 'stP3' || k === 'stP5') r.boot = boot(x); return r; }).filter(Boolean); holm(rows); return rows; };
    const E = fam('E', k => diff(get(R, 'cb', 1, k), get(R, 'cb', 0, k))), X = fam('X', k => { const a = diff(get(R, 'cb', 1, k), get(R, 'cb', 0, k)), b = diff(get(R, OFF, 1, k), get(R, OFF, 0, k)); return a && b ? diff(a, b) : null; });
    const E0 = fam('E0', k => diff(get(R, OFF, 1, k), get(R, OFF, 0, k)));
    o.E = E; o.X = X; o.E0 = E0;
    md.push('**Primary outcomes.** Levels are the no-programme run with the central bank on; E the programme\'s effect with it on (H: Holm-adjusted); X the interaction.', '',
      '| outcome | no programme, cb on | programme, cb on | E (95%) | E (H) | verdict | E with cb off | X (95%) | X (H) |', '|---|---|---|---|---|---|---|---|---|');
    E.forEach((r, i) => { const m = a => a ? a.reduce((u, v) => u + v, 0)/a.length : undefined, x = X[i], e0 = E0[i];
      md.push('| ' + r.l + ' | ' + f(m(get(R, 'cb', 0, r.k))) + ' | ' + f(m(get(R, 'cb', 1, r.k))) + ' | ' + ci(r) + (r.boot ? ' (boot ' + f(r.boot[0]) + ', ' + f(r.boot[1]) + ')' : '') + ' | [' + f(r.loH) + ', ' + f(r.hiH) + '] | ' + word(r, true) +
        ' | ' + (e0 ? ci(e0) : '-') + ' | ' + (x ? ci(x) : '-') + ' | ' + (x ? '[' + f(x.loH) + ', ' + f(x.hiH) + ']' : '-') + ' |'); });
    md.push('');
    const S = SEC.map(k => { const r = {k}; [['E', 'cb', 1, 'cb', 0], ['E0', OFF, 1, OFF, 0], ['Cn', 'cb', 0, OFF, 0], ['Cp', 'cb', 1, OFF, 1]].forEach(([n, a1, r1, a0, r0]) => { const x = diff(get(R, a1, r1, k), get(R, a0, r0, k)); r[n] = x ? pair(x) : null; }); return r; }).filter(r => r.E || r.Cn);
    o.S = S; md.push('**Secondary outcomes** (E, E with cb off; C: the central bank\'s effect, cb minus off, in the no-programme run and in the programme run).', '', '| key | E | E, cb off | C, no programme | C, programme |', '|---|---|---|---|---|');
    S.forEach(r => md.push('| ' + r.k + ' | ' + (r.E ? ci(r.E) : '-') + ' | ' + (r.E0 ? ci(r.E0) : '-') + ' | ' + (r.Cn ? ci(r.Cn) : '-') + ' | ' + (r.Cp ? ci(r.Cp) : '-') + ' |')); md.push('');
    const C = CBK.map(k => { const a = get(R, 'cb', 0, k), b = get(R, 'cb', 1, k), m = x => x ? x.reduce((u, v) => u + v, 0)/x.length : undefined; return {k, none: m(a), prog: m(b)}; }).filter(r => r.none !== undefined);
    o.C = C; md.push('**The rule and forced sales** (means over seeds, central-bank arm).', '', '| key | no programme | programme |', '|---|---|---|'); C.forEach(r => md.push('| ' + r.k + ' | ' + f(r.none) + ' | ' + f(r.prog) + ' |')); md.push('');
    const p1o = get(R, 'cb', 1, 'stP1o'), p1p = get(R, 'cb', 1, 'stP1p'), mm = x => x ? x.reduce((u, v) => u + v, 0)/x.length : NaN;
    o.plain = {outside: mm(p1o), own: mm(p1p)}; md.push('**Plain statement (programme run, central bank on):** the spread of the programme\'s own yearly price change is ' + f(mm(p1p)) + ' points against ' + f(mm(p1o)) + ' for outside inflation: the programme\'s own inflation is ' + (mm(p1p) > mm(p1o) ? '**the larger source of instability**' : 'the smaller source') + ' here.', '');
    if (env === 'hx'){ const A = R.actual && R.actual[0], m = x => x ? x.reduce((u, v) => u + v, 0)/x.length : NaN, chk = [];
      const verdict = (model, data) => (Math.sign(model) === Math.sign(data) && model !== 0) ? (Math.abs(model) >= Math.abs(data)/2 && Math.abs(model) <= 2*Math.abs(data) ? 'matches' : 'same direction, different size') : 'does not match';
      const pov = fs.readFileSync(path.join(__dirname, '..', '..', 'sources', 'history', 'poverty_official.csv'), 'utf8').split('\n').map(l => l.split(',')).filter(c => c[0] === 'official_poverty_rate' && c[2] === 'all');
      const spm = fs.readFileSync(path.join(__dirname, '..', '..', 'sources', 'history', 'poverty_spm_history.csv'), 'utf8').split('\n').map(l => l.split(',')).filter(c => c[0] === 'anchored_SPM_rate' && c[2] === 'all');
      const at = (rows, y) => { const r = rows.find(c => +c[1] === y); return r ? +r[3] : NaN; }, lastY = rows => Math.max.apply(null, rows.map(c => +c[1]));
      const dOff = at(pov, 2025) - at(pov, 2005), sy = lastY(spm), dSpm = at(spm, sy) - at(spm, 2005);
      if (A){ chk.push(['top 1% share of net worth, change (points)', m(A.wtT1E) - m(A.wtT1S), 31.7681 - 27.1703], ['bottom 50% share, change (points)', m(A.wtB50E) - m(A.wtB50S), 2.3981 - 2.5321],
        ['basket poverty, change 2005-2025 (points) vs official poverty', m(A.pf0_20) - m(A.pf0_0), dOff], ['basket poverty vs anchored SPM (2005-' + sy + ')', m(A['pf0_' + (sy - 2005)]) - m(A.pf0_0), dSpm],
        ['wealth poverty, change (points) vs official poverty', m(A.ppov_20) - m(A.ppov_0), dOff]); }
      o.checks = chk.map(c => ({what: c[0], model: c[1], data: c[2], verdict: verdict(c[1], c[2])}));
      md.push('**History checks** (no-programme run, actual rate path; checked, not tuned).', '', '| check | model | data | verdict |', '|---|---|---|---|'); o.checks.forEach(c => md.push('| ' + c.what + ' | ' + f(c.model) + ' | ' + f(c.data) + ' | ' + c.verdict + ' |')); md.push(''); }
    /* Part 3 (Amendment 2): who gains and who pays by group, P2 as a share of income, own inflation (History), the third decision rule. Shown only when the keys exist. */
    if (get(R, 'cb', 0, 'wgWq1')){ const G = [['q1', 'poorest fifth'], ['q2', 'second fifth'], ['q3', 'middle fifth'], ['q4', 'fourth fifth'], ['q5', 'richest fifth'], ['t1', 'top 1%']], CH = ['A', 'N', 'F', 'R', 'J', 'B', 'S'];
      const mean = a => a ? a.reduce((u, v) => u + v, 0)/a.length : undefined; o.W = {};
      [[0, 'no programme'], [1, 'programme']].forEach(([row, rn]) => {
        md.push('**Who gains and who pays: ' + rn + ' run** (by fifth of starting real wealth and the top 1%; Year-0 dollars per adult). C: the central bank\'s effect on the change in real wealth over the run (cb minus ' + (env === 'hx' ? 'no central bank; and cb minus the actual rate path' : 'off') + ', paired, 95%). Channels: first-round tallies in the central-bank arm (asset prices, deposits, floating debt, refinancing, job-loss income, forced-sale buyers\' and sellers\' later gains), means over seeds.', '',
          '| group | C on real wealth (95%) |' + (env === 'hx' ? ' C vs actual path (95%) |' : '') + ' asset prices | deposits | floating debt | refinancing' + (env === 'hx' ? ' (actual path)' : '') + ' | job-loss income | buyers\' gain | sellers\' gain |', '|---|---|' + (env === 'hx' ? '---|' : '') + '---|---|---|---|---|---|---|');
        o.W[rn] = G.map(([g, gn]) => { const c = diff(get(R, 'cb', row, 'wgW' + g), get(R, OFF, row, 'wgW' + g)), ca = env === 'hx' ? diff(get(R, 'cb', row, 'wgW' + g), get(R, 'actual', row, 'wgW' + g)) : null, r = {g, C: c ? pair(c) : null, Ca: ca ? pair(ca) : null};
          CH.forEach(k => { r[k] = mean(get(R, 'cb', row, 'wg' + k + g)); }); if (env === 'hx') r.Ract = mean(get(R, 'actual', row, 'wgR' + g));
          md.push('| ' + gn + ' | ' + (r.C ? ci(r.C) : '-') + ' |' + (env === 'hx' ? ' ' + (r.Ca ? ci(r.Ca) : '-') + ' |' : '') + CH.map(k => ' ' + f(r[k], 0) + (k === 'R' && env === 'hx' ? ' (' + f(r.Ract, 0) + ')' : '') + ' |').join('')); return r; });
        md.push(''); });
      const WS = []; [[0, 'no programme'], [1, 'programme']].forEach(([row, rn]) => (env === 'hx' ? [OFF, 'actual'] : [OFF]).forEach(base => { const r = {run: rn, base};
        ['wtT1E', 'wtT10E', 'wtB50E'].forEach(k => { const x = diff(get(R, 'cb', row, k), get(R, base, row, k)); r[k] = x ? pair(x) : null; }); WS.push(r); })); o.WS = WS;
      md.push('**Wealth shares at the end** (the central bank\'s effect, cb minus ' + (env === 'hx' ? 'no central bank or the actual rate path' : 'off') + ', points of net worth, paired, 95%; weighted tail).', '', '| run | against | top 1% share | top 10% share | bottom 50% share |', '|---|---|---|---|---|');
      WS.forEach(r => md.push('| ' + r.run + ' | ' + (r.base === 'actual' ? 'actual rate path' : r.base === 'infl' ? 'no central bank' : 'off') + ' | ' + (r.wtT1E ? ci(r.wtT1E) : '-') + ' | ' + (r.wtT10E ? ci(r.wtT10E) : '-') + ' | ' + (r.wtB50E ? ci(r.wtB50E) : '-') + ' |')); md.push('');
      const P2S = ['stP2s', 'stP2sq1', 'stP2sq2', 'stP2sq3', 'stP2sq4', 'stP2sq5'].map(k => { const e = diff(get(R, 'cb', 1, k), get(R, 'cb', 0, k)), e0 = diff(get(R, OFF, 1, k), get(R, OFF, 0, k)); return {k, none: mean(get(R, 'cb', 0, k)), prog: mean(get(R, 'cb', 1, k)), E: e ? pair(e) : null, E0: e0 ? pair(e0) : null}; });
      o.P2S = P2S; md.push('**P2 as a share of income** (per adult, the spread of the yearly change in real cash income over its mean, %; weighted median; all adults, then by fifth). E: the programme\'s effect, central bank on; E0 with it off.', '', '| key | no programme, cb on | programme, cb on | E (95%) | E0 (95%) |', '|---|---|---|---|---|');
      P2S.forEach(r => md.push('| ' + r.k + ' | ' + f(r.none) + ' | ' + f(r.prog) + ' | ' + (r.E ? ci(r.E) : '-') + ' | ' + (r.E0 ? ci(r.E0) : '-') + ' |')); md.push('');
      if (env === 'hx'){ const IK = ['stIc', 'stIo', 'stIq1', 'stIq2', 'stIq3', 'stIq4', 'stIq5', 'stIt1', 'stI10', 'stI90'], I = {}; IK.forEach(k => { I[k] = mean(get(R, 'actual', 0, k)); }); o.I = I;
        md.push('**Each household\'s own inflation, 2006-2025** (% a year; its basket by household type, food, housing and medical care at their CPI-U components, the rest at CPI-U; no-programme run, actual rate path). CPI-U ' + f(I.stIc, 3) + '; all households ' + f(I.stIo, 3) + ' (10th-90th percentile ' + f(I.stI10, 3) + ' to ' + f(I.stI90, 3) + '); by fifth ' + ['stIq1', 'stIq2', 'stIq3', 'stIq4', 'stIq5'].map(k => f(I[k], 3)).join(', ') + '; top 1% ' + f(I.stIt1, 3) + '. Not checked against R-CPI-I (not opened).', ''); }
      const pa = (row, arm) => { const T = env === 'hx' ? 21 : 20, x = []; for (let t = 0; t < T; t++){ const v = get(R, arm, row, 'ppov_' + t); if (!v) return null; v.forEach((u, i) => { x[i] = (x[i] || 0) + u/T; }); } return x; };
      const r3 = [['fgt0PY', 'basket poverty'], ['pov', 'wealth poverty, last year'], ['povAvg', 'wealth poverty, yearly average']].map(([k, l]) => { const a = k === 'povAvg' ? pa(1, 'cb') : get(R, 'cb', 1, k), b = k === 'povAvg' ? pa(1, OFF) : get(R, OFF, 1, k), c = diff(a, b); const r = c ? pair(c) : null;
        return {k, l, C: r}; }); holm(r3.map(r => r.C).filter(Boolean)); r3.forEach(r => { r.word = r.C ? (r.C.hiH < 0 ? 'adds to the programme\'s gain' : r.C.loH > 0 ? 'offsets part of the programme\'s gain' : 'no measurable difference') : '-'; });
      o.rule3 = r3; md.push('**Decision rule 3: does the central bank\'s response offset the programme\'s gain?** (programme run, central bank on minus ' + (env === 'hx' ? 'no central bank' : 'off') + ', points; 95% and Holm-adjusted across the three; the reading uses the Holm interval)', '', '| outcome | C (95%) | C (Holm) | reading |', '|---|---|---|---|');
      r3.forEach(r => md.push('| ' + r.l + ' | ' + (r.C ? ci(r.C) : '-') + ' | ' + (r.C ? '[' + f(r.C.loH) + ', ' + f(r.C.hiH) + ']' : '-') + ' | ' + r.word + ' |')); md.push(''); }
  }); });
/* Decision rule 2: the damping claim, per design */
const dz = {}; ['c22', 'rel'].forEach(d => { const x = e => out[e] && out[e][d] && out[e][d].X ? out[e][d].X.find(r => r.k === 'stP1') : null, eB = e => out[e] && out[e][d] && out[e][d].S ? out[e][d].S.find(r => r.k === 'fgt0PY') : null;
  const neg = e => { const r = x(e); return r && r.hiH < 0; }, okB = e => { const r = eB(e); return r && r.E && r.E.hi <= 0; };
  dz[d] = {hx: neg('hx'), adv: neg('adv'), st: neg('st'), basket: ['hx', 'adv', 'st'].every(e => !out[e] || okB(e))}; dz[d].claim = dz[d].hx && (dz[d].adv || dz[d].st) && dz[d].basket; });
out.damping = dz; md.push('## Decision rule: does the programme\'s share of essentials damp what the central bank and outside shocks do to the cost of basic living?', '');
Object.keys(dz).forEach(d => md.push('- ' + DNAME[d] + ': P1 interaction below zero (Holm) in History ' + dz[d].hx + ', Adverse ' + dz[d].adv + ', Stress ' + dz[d].st + '; basket poverty not worse ' + dz[d].basket + '. **Claim ' + (dz[d].claim ? 'supported' : 'not supported') + '.**'));
fs.writeFileSync(path.join(dir, 'tables.json'), JSON.stringify(out, null, 1)); fs.writeFileSync(path.join(dir, 'tables.md'), md.join('\n') + '\n');
console.log('wrote ' + path.join(dir, 'tables.md') + ' (' + ENVS.join(', ') + ')');
