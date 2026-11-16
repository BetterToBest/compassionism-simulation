#!/usr/bin/env node
/* S75 part 2 tables (research-update prereg/2026-11-s75-deep-history.md, Part B "Analysis" and "Decision rules", and Amendment 4, item 6).
 * Reads DIR/s75-eras-e1..e4.json (dev/tools/s75_eras.js) and writes DIR/tables.md and DIR/tables.json:
 *  levels   each era, arm and row: the mean over seeds of P1-P5, P3 over years 0-11, basket poverty and wealth poverty;
 *  Q3       the no-programme row, era X minus 2008-2025 (E4), same arm and seeds, Holm across P1-P5 within each era pair, arm and design;
 *  settings the no-programme row, each arm minus arm P within an era (which setting moves it, inside the model), Holm as Q3;
 *  Q4       the programme's effect (programme minus no programme) by era, arm and design, Holm across P1-P5, its direction against S74's History
 *           arm with the rule; T's charges and neutrality gap; the rule's stance against the actual one (arms R, S, A).
 * Paired t intervals; a paired bootstrap (2,000 replicates, seed 20261115) beside them for P3 and P5. Usage: node dev/tools/s75_table.js [DIR] */
'use strict';
const fs = require('fs'), path = require('path');
const dir = process.argv[2] || path.join(__dirname, '..', 'runs', 's75-eras');
const ERAS = ['e1', 'e2', 'e3', 'e4'], NAME = {e1: '1947-1972', e2: '1973-1983', e3: '1984-2007', e4: '2008-2025'}, ARMS = ['P', 'R', 'S', 'T', 'H', 'A'], DES = ['c22', 'rel'];
const DNAME = {c22: 'C2.2', rel: 'release design'};
const ANAME = {P: 'P the era\'s path (actual rates)', R: 'R + the era\'s rule', S: 'S + S74\'s rule', T: 'T + the era\'s tax schedule', H: 'H + the era\'s health cost growth', A: 'A all (R, T, H)', Tn: 'Tn T with nothing returned'};
const PRIM = [['stP1', 'P1 spread of the basket price level\'s yearly change (points)'], ['stP2', 'P2 spread of yearly changes in real cash income ($)'],
  ['stP3', 'P3 largest fall in real wealth ($, median; whole run)'], ['rkRecM', 'P4 years to recover from an income shock (mean)'], ['stP5', 'P5 % pushed below the basket line in a recession year']];
const SEC = [['stP3e', 'P3 over years 0-11 ($, median)'], ['fgt0PY', 'basket poverty (% of person-years)'], ['pov', 'wealth poverty, last year (%)'], ['ppovA', 'wealth poverty, yearly average (%)']];
const S74 = {c22: {stP1: 1, stP2: 1, stP3: -1, rkRecM: -1, stP5: -1}, rel: {stP1: 1, stP2: 1, stP3: -1, rkRecM: 1, stP5: -1}};  /* S74's History arm with the rule (report, the stability test) */
/* Student t (as dev/tools/s74_table.js) */
function lgam(x){ const c = [76.18009172947146, -86.50532032941677, 24.01409824083091, -1.231739572450155, 0.1208650973866179e-2, -0.5395239384953e-5]; let y = x, t = x + 5.5; t -= (x + 0.5)*Math.log(t); let s = 1.000000000190015; for (const k of c) s += k/++y; return -t + Math.log(2.5066282746310005*s/x); }
function betacf(a, b, x){ let qab = a + b, qap = a + 1, qam = a - 1, c = 1, d = 1 - qab*x/qap; d = 1/(Math.abs(d) < 1e-300 ? 1e-300 : d); let h = d;
  for (let m = 1; m <= 300; m++){ const m2 = 2*m; let aa = m*(b - m)*x/((qam + m2)*(a + m2)); d = 1 + aa*d; d = 1/(Math.abs(d) < 1e-300 ? 1e-300 : d); c = 1 + aa/c; c = Math.abs(c) < 1e-300 ? 1e-300 : c; h *= d*c;
    aa = -(a + m)*(qab + m)*x/((a + m2)*(qap + m2)); d = 1 + aa*d; d = 1/(Math.abs(d) < 1e-300 ? 1e-300 : d); c = 1 + aa/c; c = Math.abs(c) < 1e-300 ? 1e-300 : c; const del = d*c; h *= del; if (Math.abs(del - 1) < 3e-16) break; } return h; }
function ibeta(a, b, x){ if (x <= 0) return 0; if (x >= 1) return 1; const bt = Math.exp(lgam(a + b) - lgam(a) - lgam(b) + a*Math.log(x) + b*Math.log(1 - x)); return x < (a + 1)/(a + b + 2) ? bt*betacf(a, b, x)/a : 1 - bt*betacf(b, a, 1 - x)/b; }
function tP2(t, df){ return ibeta(df/2, 0.5, df/(df + t*t)); }
function tQ(p2, df){ let lo = 0, hi = 1000; for (let i = 0; i < 200; i++){ const m = (lo + hi)/2; if (tP2(m, df) > p2) lo = m; else hi = m; } return (lo + hi)/2; }
function mulberry32(a){ return function(){ a |= 0; a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0)/4294967296; }; }
function pair(d){ const n = d.length, m = d.reduce((u, v) => u + v, 0)/n, sd = Math.sqrt(d.reduce((u, v) => u + (v - m)*(v - m), 0)/(n - 1)), se = sd/Math.sqrt(n), t = se > 0 ? m/se : (m === 0 ? 0 : Infinity);
  return {n, m, se, p: se > 0 ? tP2(Math.abs(t), n - 1) : (m === 0 ? 1 : 0), lo: m - tQ(0.05, n - 1)*se, hi: m + tQ(0.05, n - 1)*se}; }
function boot(d){ const r = mulberry32(20261115), n = d.length, B = []; for (let b = 0; b < 2000; b++){ let s = 0; for (let i = 0; i < n; i++) s += d[Math.floor(r()*n)]; B.push(s/n); } B.sort((x, y) => x - y); return [B[49], B[1949]]; }
function holm(rows){ const o = rows.map((r, i) => i).sort((i, j) => rows[i].p - rows[j].p), m = rows.length; let run = 0;
  o.forEach((i, k) => { const r = rows[i], a = 0.05/(m - k); run = Math.max(run, Math.min(1, r.p*(m - k))); r.pH = run; const q = r.se > 0 ? tQ(a, r.n - 1)*r.se : 0; r.loH = r.m - q; r.hiH = r.m + q; }); return rows; }
const J = {}; ERAS.forEach(e => { const f = path.join(dir, 's75-eras-' + e + '.json'); if (fs.existsSync(f)) J[e] = JSON.parse(fs.readFileSync(f, 'utf8')); });
function vals(e, d, arm, row, k){ const R = J[e] && J[e][d] && J[e][d][arm] && J[e][d][arm][row]; if (!R) return null;
  if (k === 'ppovA'){ const n = J[e]._meta.years, ks = []; for (let t = 0; t < n; t++) if (R['ppov_' + t]) ks.push(R['ppov_' + t]); if (!ks.length) return null; return ks[0].map((_, i) => ks.reduce((u, v) => u + v[i], 0)/ks.length); }
  return R[k] || null; }
const mean = x => x.reduce((u, v) => u + v, 0)/x.length;
const f = (v, k) => v === null || v === undefined || !isFinite(v) ? 'n/a' : Math.abs(v) >= 1000 ? Math.round(v).toLocaleString('en-US') : Math.abs(v) >= 10 ? v.toFixed(1) : v.toFixed(2);
const sgn = v => (v > 0 ? '+' : '') + f(v);
function verdict(r){ if (!r) return 'n/a'; if (r.none) return 'no recessions'; return r.hiH < 0 ? 'steadier (' + sgn(r.m) + ')' : r.loH > 0 ? 'less steady (' + sgn(r.m) + ')' : 'no clear difference (' + sgn(r.m) + ')'; }
function family(mk){ const rows = PRIM.map(([k, l]) => { const x = mk(k); if (!x) return null; const r = pair(x); r.k = k; r.l = l; if (k === 'stP3' || k === 'stP5') r.boot = boot(x); return r; });
  const ok = rows.filter(r => r && !(r.k === 'stP5' && r.none)); holm(ok); return rows; }
const md = [], out = {meta: {}, levels: {}, q3: {}, settings: {}, q4: {}, tax: {}, stance: {}};
ERAS.forEach(e => { if (J[e]) out.meta[e] = {command: J[e]._meta.command, commit: J[e]._meta.manifest && J[e]._meta.manifest.commit, dirty: J[e]._meta.manifest && J[e]._meta.manifest.dirty, seeds: J[e]._meta.seeds, secs: J[e]._meta.secs}; });
md.push('# S75 engine readings: today\'s households under each era\'s settings', '', 'A model counterfactual (research-update prereg/2026-11-s75-deep-history.md, Part B and Amendment 4): the frozen round-2 main pair, 500 adults, seeds 1-' + (J.e1 ? J.e1._meta.seeds : '?') + ', each era\'s length plus its starting year. Engine commit ' + (out.meta.e1 ? out.meta.e1.commit : '?') + '. Generated by `node dev/tools/s75_eras.js ERA` (each era) and `node dev/tools/s75_table.js`.', '');
const noRec = (e, d, arm) => { const n = vals(e, d, arm, 0, 'stP5n'); return n && n.every(v => v === 0); };
/* levels */
md.push('## Levels (means over seeds)', '');
DES.forEach(d => { md.push('### ' + DNAME[d], '', '| era | arm | row | ' + PRIM.concat(SEC).map(x => x[1]).join(' | ') + ' |', '|' + '---|'.repeat(3 + PRIM.length + SEC.length));
  ERAS.forEach(e => ARMS.concat(['Tn']).forEach(arm => [0, 1].forEach(row => { const c = PRIM.concat(SEC).map(([k]) => { const v = vals(e, d, arm, row, k); return v ? mean(v) : null; });
    if (c.every(v => v === null)) return; (out.levels[d] = out.levels[d] || {})[e + ' ' + arm + ' ' + row] = c; md.push('| ' + NAME[e] + ' | ' + arm + ' | ' + (row ? 'programme' : 'none') + ' | ' + c.map(v => f(v)).join(' | ') + ' |'); }))); md.push(''); });
/* Q3 */
md.push('## Q3: without the programme, steadier than 2008-2025? (era minus 2008-2025, same arm; Holm across P1-P5)', '', '"Steadier" means the Holm-adjusted 95% interval of (era minus 2008-2025) is below zero; P3 over the whole run is longer in a longer era, so P3 over years 0-11 is shown beside it (unadjusted interval).', '');
DES.forEach(d => { md.push('### ' + DNAME[d] + ' (its no-programme row)', '', '| arm | outcome | ' + ['e1', 'e2', 'e3'].map(e => NAME[e] + ' vs 2008-2025').join(' | ') + ' |', '|---|---|---|---|---|');
  ARMS.forEach(arm => { const fam = {}; ['e1', 'e2', 'e3'].forEach(e => { fam[e] = family(k => { const a = vals(e, d, arm, 0, k), b = vals('e4', d, arm, 0, k); return a && b ? a.map((v, i) => v - b[i]) : null; });
      fam[e].forEach(r => { if (r && r.k === 'stP5' && (noRec(e, d, arm) || noRec('e4', d, arm))) r.none = true; }); });
    (out.q3[d] = out.q3[d] || {})[arm] = fam;
    PRIM.forEach(([k, l], j) => md.push('| ' + arm + ' | ' + l + ' | ' + ['e1', 'e2', 'e3'].map(e => verdict(fam[e][j]) + (fam[e][j] && fam[e][j].boot ? ' [boot ' + f(fam[e][j].boot[0]) + ', ' + f(fam[e][j].boot[1]) + ']' : '')).join(' | ') + ' |'));
    SEC.forEach(([k, l]) => { const c = ['e1', 'e2', 'e3'].map(e => { const a = vals(e, d, arm, 0, k), b = vals('e4', d, arm, 0, k); if (!a || !b) return 'n/a'; const r = pair(a.map((v, i) => v - b[i])); return sgn(r.m) + ' [' + f(r.lo) + ', ' + f(r.hi) + ']'; }); md.push('| ' + arm + ' | ' + l + ' (secondary) | ' + c.join(' | ') + ' |'); }); });
  md.push(''); });
/* settings */
md.push('## Which setting moves it (no programme, each arm minus arm P in the same era; Holm across P1-P5)', '');
DES.forEach(d => { md.push('### ' + DNAME[d], '', '| era | outcome | ' + ['R', 'S', 'T', 'H', 'A'].map(a => ANAME[a] + ' minus P').join(' | ') + ' |', '|---|---|---|---|---|---|---|');
  ERAS.forEach(e => { const fam = {}; ['R', 'S', 'T', 'H', 'A'].forEach(arm => { fam[arm] = family(k => { const a = vals(e, d, arm, 0, k), b = vals(e, d, 'P', 0, k); return a && b ? a.map((v, i) => v - b[i]) : null; });
      fam[arm].forEach(r => { if (r && r.k === 'stP5' && noRec(e, d, 'P')) r.none = true; }); }); (out.settings[d] = out.settings[d] || {})[e] = fam;
    PRIM.forEach(([k, l], j) => md.push('| ' + NAME[e] + ' | ' + l + ' | ' + ['R', 'S', 'T', 'H', 'A'].map(a => verdict(fam[a][j])).join(' | ') + ' |'));
    ['fgt0PY', 'ppovA'].forEach(k => { const l = SEC.filter(x => x[0] === k)[0][1]; md.push('| ' + NAME[e] + ' | ' + l + ' (secondary) | ' + ['R', 'S', 'T', 'H', 'A'].map(arm => { const a = vals(e, d, arm, 0, k), b = vals(e, d, 'P', 0, k); if (!a || !b) return 'n/a'; const r = pair(a.map((v, i) => v - b[i])); return sgn(r.m) + ' [' + f(r.lo) + ', ' + f(r.hi) + ']'; }).join(' | ') + ' |'); }); });
  md.push(''); });
/* Q4 */
md.push('## Q4: the programme\'s effect (programme minus no programme; Holm across P1-P5), and whether it keeps S74\'s direction', '', 'S74\'s History arm with the rule: C2.2 P1 up, P2 up, P3 down, P4 down, P5 down; the release design P1 up, P2 up, P3 down, P4 up, P5 down. "kept" means the Holm interval excludes zero in S74\'s direction.', '');
const tally = {};
DES.forEach(d => { md.push('### ' + DNAME[d], '', '| era | arm | ' + PRIM.map(x => x[1]).join(' | ') + ' | basket poverty, programme minus none (points) |', '|---|---|' + '---|'.repeat(PRIM.length + 1));
  ERAS.forEach(e => ARMS.concat(['Tn']).forEach(arm => { const fam = family(k => { const a = vals(e, d, arm, 1, k), b = vals(e, d, arm, 0, k); return a && b ? a.map((v, i) => v - b[i]) : null; });
    if (fam.every(r => !r)) return; fam.forEach(r => { if (r && r.k === 'stP5' && noRec(e, d, arm)) r.none = true; });
    (out.q4[d] = out.q4[d] || {})[e + ' ' + arm] = fam;
    const cells = fam.map(r => { if (!r) return 'n/a'; if (r.none) return 'no recessions'; const dir = r.hiH < 0 ? -1 : r.loH > 0 ? 1 : 0, w = S74[d][r.k], tag = dir === 0 ? 'no measurable difference' : dir === w ? 'kept' : 'reversed';
      if (ARMS.indexOf(arm) >= 0){ const T = tally[d + ' ' + tag] = (tally[d + ' ' + tag] || 0) + 1; } return tag + ' (' + sgn(r.m) + ')'; });
    const a = vals(e, d, arm, 1, 'fgt0PY'), b = vals(e, d, arm, 0, 'fgt0PY'), bp = a && b ? pair(a.map((v, i) => v - b[i])) : null;
    md.push('| ' + NAME[e] + ' | ' + arm + ' | ' + cells.join(' | ') + ' | ' + (bp ? sgn(bp.m) + ' [' + f(bp.lo) + ', ' + f(bp.hi) + ']' : 'n/a') + ' |'); }));
  md.push('', 'Tally over the four eras and six arms (cells with recessions): ' + ['kept', 'no measurable difference', 'reversed'].map(t => t + ' ' + (tally[d + ' ' + t] || 0)).join(', ') + '.', ''); });
out.q4tally = tally;
/* tax and stance */
md.push('## Arm T: charges and neutrality (no programme and programme; Year-0 dollars per adult-year, means over seeds)', '', '| era | design | arm | row | mean absolute charge | mean rebate | net (charge less rebate) | gap (% of absolute charges) |', '|---|---|---|---|---|---|---|---|');
ERAS.forEach(e => DES.forEach(d => ['T', 'A', 'Tn'].forEach(arm => [0, 1].forEach(row => { const c = ['hxTCh', 'hxTRb', 'hxTNet', 'hxTGap'].map(k => { const v = vals(e, d, arm, row, k); return v ? mean(v) : null; }); if (c[0] === null) return;
  (out.tax[e + ' ' + d + ' ' + arm + ' ' + row] = c); md.push('| ' + NAME[e] + ' | ' + DNAME[d] + ' | ' + arm + ' | ' + (row ? 'programme' : 'none') + ' | ' + c.map(v => f(v)).join(' | ') + ' |'); }))));
md.push('', '## The rule\'s stance against the actual one (arms R, S, A; no programme; the yearly paths are kept for the first 21 engine years)', '', '| era | design | arm | largest tightening (points) | largest easing (points) | mean policy rate (%) | % of years at the floor |', '|---|---|---|---|---|---|---|');
ERAS.forEach(e => DES.forEach(d => ['R', 'S', 'A'].forEach(arm => { const n = Math.min(21, J[e] ? J[e]._meta.years : 0), dy = []; for (let t = 1; t < n; t++){ const v = vals(e, d, arm, 0, 'cbDy_' + t); if (v) dy.push(mean(v)); }
  if (!dy.length) return; const I = vals(e, d, arm, 0, 'cbI'), Fl = vals(e, d, arm, 0, 'cbFloor'), c = [Math.max.apply(null, dy), Math.min.apply(null, dy), I ? mean(I) : null, Fl ? mean(Fl) : null];
  out.stance[e + ' ' + d + ' ' + arm] = c; md.push('| ' + NAME[e] + ' | ' + DNAME[d] + ' | ' + arm + ' | ' + c.map(v => f(v)).join(' | ') + ' |'); })));
md.push('');
fs.writeFileSync(path.join(dir, 'tables.md'), md.join('\n')); fs.writeFileSync(path.join(dir, 'tables.json'), JSON.stringify(out, null, 1));
console.log('wrote ' + path.join(dir, 'tables.md'));
