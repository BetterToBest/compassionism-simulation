#!/usr/bin/env node
/* S74 part 3: the forward sweep's tables (research-update prereg/2026-11-s74-central-bank.md, item 3, and Amendment 2). Reads DIR/s74-sweep-ENV.json
 * (or .json.gz; dev/tools/s74_sweep.js) and writes sweep-tables.md and sweep-tables.json beside them. Nothing is run here. Descriptive only: means
 * over seeds with the 10th-90th percentile across seeds, and fans (the 10th, 50th and 90th percentile across seeds of each yearly path).
 * E: the programme's effect (programme minus no programme, paired on seeds) in a setting; C: a setting's effect against no central bank (History:
 * hx.rp 'infl'), paired on seeds; X: the interaction on P1 (E in the setting minus E with no central bank).
 * Usage: node dev/tools/s74_sweep_table.js [DIR] */
'use strict';
const fs = require('fs'), path = require('path'), zlib = require('zlib');
const dir = process.argv[2] || path.join(__dirname, '..', 'runs', 's74-sweep');
const rd = env => { const f = path.join(dir, 's74-sweep-' + env + '.json'); if (fs.existsSync(f)) return JSON.parse(fs.readFileSync(f, 'utf8'));
  if (fs.existsSync(f + '.gz')) return JSON.parse(zlib.gunzipSync(fs.readFileSync(f + '.gz')).toString('utf8')); return null; };
const ENVS = ['hx', 'adv', 'st', 'ref'], NAME = {hx: 'History (2005-2025)', adv: 'Adverse', st: 'Stress', ref: 'Reference'}, DNAME = {c22: 'C2.2', rel: 'release design'};
const LABEL = {off: 'no central bank', actual: 'actual rate path', 'actual-sp1.5': 'actual path, spread 1.5', 'actual-sp4.5': 'actual path, spread 4.5', main: 'main rule',
  a1: 'a 1', 'a1.5': 'a 1.5', a2: 'a 2', b0: 'b 0', b1: 'b 1', pt3: 'target 3%', r0: 'neutral rate 0', 'r1.5': 'neutral rate 1.5%', 'bL0.25': 'purchases 0.25', bL1: 'purchases 1', noqe: 'no purchases',
  lag1: 'lag 1 year', lag2: 'lag 2 years', 'th0.25': 'yield response 0.25', th1: 'yield response 1', 'dm0.5': 'spending response 0.5', dm1: 'spending response 1',
  reg2008: '2008-style', reg2020: '2020-style', reg2022: '2022-style', 'sp1.5': 'floating spread 1.5', 'sp4.5': 'floating spread 4.5', 'mm0.75': 'mortgage link 0.75', D4: 'D 4 years', D10: 'D 10 years',
  'k0.25': 'take-up 0.25', k1: 'take-up 1', 'fd0.1': 'sale discount 0.1', 'fd0.27': 'sale discount 0.27', 'fd0.034': 'sale discount 0.034', 'fd0.062': 'sale discount 0.062', 'ok1.5': 'Okun 1.5', nofs: 'no forced sales'};
const PRIM = [['stP1', 'P1'], ['stP2', 'P2'], ['stP3', 'P3'], ['rkRecM', 'P4'], ['stP5', 'P5'], ['fgt0PY', 'basket pov.'], ['pov', 'wealth pov.']];
const mean = a => a.reduce((u, v) => u + v, 0)/a.length;
const q = (a, p) => { const s = a.slice().sort((x, y) => x - y), h = (s.length - 1)*p, i = Math.floor(h); return s[i] + (h - i)*((s[i + 1] === undefined ? s[i] : s[i + 1]) - s[i]); };
const sm = a => a ? {m: mean(a), lo: q(a, 0.1), hi: q(a, 0.9)} : null;
const diff = (a, b) => a && b ? a.map((x, i) => x - b[i]) : null;
const f = (x, d) => x === undefined || x === null || !isFinite(x) ? '-' : Math.abs(x) >= 1000 ? x.toFixed(0) : x.toFixed(d === undefined ? 2 : d);
const rg = r => r ? f(r.m) + ' [' + f(r.lo) + ', ' + f(r.hi) + ']' : '-';
const PATHS = [['cbIy', 'policy rate (%)'], ['cbQy', 'purchases (% of GDP)'], ['cbMy', 'mortgage rate change (points)'], ['cbUy', 'unemployment rise (points)'], ['stLy', 'basket price change (%)'], ['pf0', 'basket poverty (%)'], ['ppov', 'wealth poverty (%)']];
const FANSET = ['main', 'reg2008', 'reg2020', 'reg2022'];
const out = {_meta: {dir, made: new Date().toISOString()}}, md = ['# S74 forward sweep tables (20 seeds, frozen round-2 main row)', '',
  'Made by `node dev/tools/s74_sweep_table.js` from the sweep files in this folder (`node dev/tools/s74_sweep.js ENV 20`). Descriptive only: each cell is the mean over seeds 1-20 with the 10th to 90th percentile across seeds in brackets. E is the programme\'s effect (programme minus no programme, paired on seeds) in each setting; C is the setting\'s effect against no central bank, paired on seeds; X is the interaction on P1 (E in the setting minus E with no central bank). P1 spread of the basket price level\'s yearly change (points); P2 spread of yearly changes in real cash income ($, mean); P3 largest fall in real wealth ($, median); P4 years to recover from an income shock; P5 % pushed below the basket line in a recession year; basket poverty (`fgt0PY`, % of adult-years); wealth poverty (`pov`, % in the last year).', ''];
ENVS.forEach(env => { const D = rd(env); if (!D) return; out[env] = {meta: D._meta}; const OFF = 'off', T = env === 'hx' ? 21 : 20;
  md.push('## ' + NAME[env], '', 'Engine: ' + (D._meta.manifest && D._meta.manifest.commit) + (D._meta.manifest && D._meta.manifest.dirty ? ' (dirty)' : '') + '; command `' + D._meta.command + '`; ' + D._meta.seeds + ' seeds; ' + Object.keys(D._meta.settings).length + ' settings.', '');
  D._meta.designs.forEach(d => { const R = D[d], o = out[env][d] = {rows: {}, fans: {}}, S = Object.keys(R), g = (s, row, k) => R[s] && R[s][row] && R[s][row][k];
    md.push('### ' + DNAME[d], '');
    md.push('**The rule in each setting** (programme run; no-programme run after the slash where it differs in kind).', '', '| setting | policy rate, mean (%) | years at the floor (%) | purchases, peak (% of GDP) | unemployment rise (points) | programme\'s own inflation (%) | forced sales (% of adult-years, no programme / programme) |', '|---|---|---|---|---|---|---|');
    S.forEach(s => { const r = o.rows[s] = {}; ['cbI', 'cbFloor', 'cbQmax', 'cbU', 'endoAnn'].forEach(k => { r[k] = sm(g(s, 1, k)); }); r.fsN0 = sm(g(s, 0, 'fsN')); r.fsN1 = sm(g(s, 1, 'fsN'));
      md.push('| ' + (LABEL[s] || s) + ' | ' + rg(r.cbI) + ' | ' + rg(r.cbFloor) + ' | ' + rg(r.cbQmax) + ' | ' + rg(r.cbU) + ' | ' + rg(r.endoAnn) + ' | ' + (r.fsN0 ? f(r.fsN0.m) + ' / ' + f(r.fsN1.m) : '-') + ' |'); });
    md.push('', '**The programme\'s effect E in each setting**, and the interaction X on P1.', '', '| setting | ' + PRIM.map(p => 'E ' + p[1]).join(' | ') + ' | X P1 |', '|---|' + PRIM.map(() => '---|').join('') + '---|');
    S.forEach(s => { const r = o.rows[s]; r.E = {}; PRIM.forEach(([k]) => { r.E[k] = sm(diff(g(s, 1, k), g(s, 0, k))); });
      const e0 = diff(g(OFF, 1, 'stP1'), g(OFF, 0, 'stP1')), e = diff(g(s, 1, 'stP1'), g(s, 0, 'stP1')); r.X = sm(diff(e, e0));
      md.push('| ' + (LABEL[s] || s) + ' | ' + PRIM.map(([k]) => rg(r.E[k])).join(' | ') + ' | ' + rg(r.X) + ' |'); });
    md.push('', '**The setting\'s effect C on poverty** (against no central bank; points).', '', '| setting | C basket poverty, no programme | C basket poverty, programme | C wealth poverty, no programme | C wealth poverty, programme |', '|---|---|---|---|---|');
    S.filter(s => s !== OFF).forEach(s => { const r = o.rows[s]; r.C = {}; [['fgt0PY', 0], ['fgt0PY', 1], ['pov', 0], ['pov', 1]].forEach(([k, row]) => { r.C[k + row] = sm(diff(g(s, row, k), g(OFF, row, k))); });
      md.push('| ' + (LABEL[s] || s) + ' | ' + rg(r.C.fgt0PY0) + ' | ' + rg(r.C.fgt0PY1) + ' | ' + rg(r.C.pov0) + ' | ' + rg(r.C.pov1) + ' |'); });
    /* ranges across the central-bank settings (every setting but no central bank and History's actual paths) */
    const CBS = S.filter(s => s !== OFF && !/^actual/.test(s)), rng = {}; o.range = rng;
    md.push('', '**Ranges across the ' + CBS.length + ' central-bank settings** (the mean E in each setting: the main rule\'s, the lowest and highest, and how many settings share the main rule\'s sign).', '', '| outcome | main rule | lowest (setting) | highest (setting) | same sign as main |', '|---|---|---|---|---|');
    PRIM.concat([['X', 'X P1']]).forEach(([k, l]) => { const v = CBS.map(s => [s, k === 'X' ? (o.rows[s].X && o.rows[s].X.m) : (o.rows[s].E[k] && o.rows[s].E[k].m)]).filter(x => x[1] !== undefined && x[1] !== null && isFinite(x[1]));
      if (!v.length) return; const mn = v.reduce((a, b) => b[1] < a[1] ? b : a), mx = v.reduce((a, b) => b[1] > a[1] ? b : a), m0 = k === 'X' ? o.rows.main.X.m : o.rows.main.E[k].m, same = v.filter(x => Math.sign(x[1]) === Math.sign(m0)).length;
      rng[k] = {main: m0, min: mn, max: mx, same, n: v.length}; md.push('| ' + (k === 'X' ? 'X P1' : 'E ' + l) + ' | ' + f(m0) + ' | ' + f(mn[1]) + ' (' + (LABEL[mn[0]] || mn[0]) + ') | ' + f(mx[1]) + ' (' + (LABEL[mx[0]] || mx[0]) + ') | ' + same + ' of ' + v.length + ' |'); });
    md.push('');
    /* fans */
    FANSET.concat(env === 'hx' ? ['actual'] : []).filter(s => R[s]).forEach(s => { const F = o.fans[s] = {};
      PATHS.forEach(([p]) => { [0, 1].forEach(row => { const ys = []; for (let t = 0; t < T; t++){ const a = g(s, row, p + (p === 'pf0' || p === 'ppov' ? '_' : '_') + t); ys.push(a ? {p10: q(a, 0.1), p50: q(a, 0.5), p90: q(a, 0.9)} : null); } F[p + row] = ys; }); }); });
    ['main'].concat(FANSET.slice(1)).filter(s => o.fans[s]).forEach(s => { const F = o.fans[s], c = (x) => x ? f(x.p50) + ' (' + f(x.p10) + ' to ' + f(x.p90) + ')' : '-';
      md.push('**Fan: ' + (LABEL[s] || s) + '** (median across seeds, 10th to 90th percentile in brackets).', '', '| year | policy rate, no programme | policy rate, programme | basket price change, programme | basket poverty, no programme | basket poverty, programme |', '|---|---|---|---|---|---|');
      for (let t = 0; t < T; t++) md.push('| ' + (env === 'hx' ? 2005 + t : t) + ' | ' + c(F.cbIy0[t]) + ' | ' + c(F.cbIy1[t]) + ' | ' + (t ? c(F.stLy1[t]) : '-') + ' | ' + c(F.pf00[t]) + ' | ' + c(F.pf01[t]) + ' |');
      md.push(''); });
  }); });
fs.writeFileSync(path.join(dir, 'sweep-tables.json'), JSON.stringify(out)); fs.writeFileSync(path.join(dir, 'sweep-tables.md'), md.join('\n') + '\n');
console.log('wrote ' + path.join(dir, 'sweep-tables.md'));
