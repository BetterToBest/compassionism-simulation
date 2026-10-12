#!/usr/bin/env node
/* v5.2.1 (Oct 6, 2026; ledger s90 and s93): the extra fields the pages' "explore" sections draw, read from the same runs as the v5.2 release panel.
 * Presentation only: harness.js is not changed and nothing here feeds back into a published figure.
 *
 * Runs four rows of the release panel on paired seeds 1..N, exactly as `node harness.js testbed N release ENV [--years=40]` builds them
 * (releaseRows; study options fin 'tax', aT 0, a 0, X 0, the sourced spending share and REL_V52_STUDY): no programme, the main row (release), H1
 * (every Source dollar backed) and the middle backing reading (mid). Each row is independent of the others on the same seed (the feature-matrix
 * test checks it), so running four rows gives those rows' figures exactly. It writes dev/runs/explore-ENV-YRS.json with:
 *  - bands: for each row, each year and each measure of the published year-by-year path (below the cost of living, too little wealth, below 30 days of
 *    basic living, median savings in today's dollars), the 10th, 50th and 90th percentile across the seeds and the mean;
 *  - deciles: the 10th..90th percentile of savings in today's dollars at Year 7 and the last year, each seed's, averaged over the seeds;
 *  - lives: the adults of one seed (default seed 1) with and without the programme: each year's flags (1 below 30 days of basic living, the BLEI
 *    paper's reading; 2 below the cost of living; 4 too little wealth; 8 taking part in the programme) as one hex digit, and savings in today's
 *    dollars (hundreds). The status the pages show is the most severe flag.
 * Self-checks (nothing is written if either fails): (1) every row's yearly means, rounded as the panel rounds them, equal the published year-by-year
 * path in dev/runs/release-panel[-40].json; (2) for the life seed, the adults' flags add up to the engine's own yearly shares for that seed.
 *
 * Usage: node dev/tools/explore_export.js ENV [YEARS] [SEEDS] [LIFESEED] [--v53]   (ENV ref, adv or st; YEARS 20 or 40; default 500 seeds, life seed 1)
 * v5.3 B10: --v53 runs the v5.3 rows (releaseRowsV53; the no-programme run of relMainCfgs) and checks them against dev/runs/v53/release-panel[-40]-ENV.json.
 * v5.4 step 9: --v54 runs the v5.4 rows (releaseRowsV54; both runs with REL_V54) and checks them against the merged v5.4 panel. */
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const ARG = process.argv.slice(2).filter(a => !/^--/.test(a)), V54 = process.argv.indexOf('--v54') >= 0, V53 = V54 || process.argv.indexOf('--v53') >= 0;
const env = ARG[0] || 'ref', YRS = +(ARG[1] || 20), N = +(ARG[2] || 500), LS = +(ARG[3] || 1);
const NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
if (!NAME || (YRS !== 20 && YRS !== 40) || !(LS >= 1 && LS <= N)) { console.error('usage: explore_export.js ref|adv|st [20|40] [SEEDS] [LIFESEED]'); process.exit(1); }
const ROOT = path.join(__dirname, '..', '..'), PANEL = path.join(ROOT, 'dev', 'runs', 'release-panel' + (YRS === 40 ? '-40' : '') + '.json');  /* the merged panel (with --v53, the v5.3 panel once it is merged) */
const C = H.CFG, SC = H.SPEND_SOURCED, M = ['f0', 'pov', 'bO', 'medW'], Q = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9];
const t0 = Date.now(), wf0 = C.WEALTH_FLOOR; C.WEALTH_FLOOR = -10000;  /* as the testbed command sets it */
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G);
const ROWS = ['base', 'release', 'h1', 'mid'];
const out = {_meta: {what: 'year-by-year spread across seeds, savings deciles and one seed\'s adults, for the pages\' explore sections (presentation only)', env, years: YRS, seeds: N, lifeSeed: LS,
  rows: ROWS, manifest: H.runManifest(), command: 'node dev/tools/explore_export.js ' + env + ' ' + YRS + ' ' + N + ' ' + LS + (V54 ? ' --v54' : V53 ? ' --v53' : ''),
  flags: {1: 'below 30 days of basic living (BLEI paper)', 2: 'below the cost of living', 4: 'too little wealth', 8: 'taking part in the programme'}}, bands: {}, deciles: {}, lives: {}};
let segs = [], cur = null;
try {
  const P = Object.assign({}, H[NAME], {years: YRS}), PR = H.tbPresets(P), rel = V54 ? H.releaseRowsV54(SC) : V53 ? H.releaseRowsV53(SC) : H.releaseRows(SC), byJ = {};
  rel.forEach(r => { byJ[r.j] = r; });
  const cfg = [Object.assign({p: PR.baseline(), sc: SC}, V53 ? {hh: H.REL_V53.hh, sg: H.REL_V53.sg, g: H.REL_V53.g} : {}, V54 ? H.REL_V54 : {})].concat(['release', 'h1', 'mid'].map(j => { const r = byJ[j], c = H.n1Row(PR, 'framework', r.v); if (r.v.o) Object.assign(c.o || (c.o = {}), r.v.o); return c; }));
  const T = YRS, L30 = C.BLEI_PRECARIOUS_MAX;
  /* The hook sees every simulated year of every run in tbStudy's order (seed outer, row inner). tbRun may first run one year to set the contribution
   * rate; that short run is recognised (it ends after one year) and dropped. */
  function close() { if (cur && cur.length === T) segs.push(cur); cur = null; }
  let k = 0;
  H.setRepHook(function (agents, yr, TT, lf) {
    if (yr === 0) close();
    if (yr === 0) cur = [];
    const slot = segs.length, seed = Math.floor(slot/cfg.length) + 1, row = slot % cfg.length, rec = {};
    if (yr === 6 || yr === T - 1) { const w = agents.map(a => a.wealth/lf); rec.dec = Q.map(q => H.quantileOf(w, q)); }
    if (seed === LS) { const p = cfg[row].p;
      rec.f = agents.map(a => { const bo = H.agentBLEI(a, p.bu, p.ccoOn, p.pth, p.szh, p.szhCoh, p.ptf);
        return (bo/lf < L30 ? 1 : 0) | ((a._tbGap || 0) > 0 ? 2 : 0) | (a.wealth < C.POVERTY_LINE*lf ? 4 : 0) | (a.inCCO ? 8 : 0); });
      rec.w = agents.map(a => Math.round(a.wealth/lf/100)); rec.n = agents.length; }
    cur.push(rec); k++;
  });
  let R; try { R = H.tbStudy(cfg, N, P, Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: SC}, H.REL_V52_STUDY)); close(); } finally { H.setRepHook(null); }
  if (segs.length !== N*cfg.length) throw new Error('expected ' + N*cfg.length + ' runs from the hook, saw ' + segs.length);
  const PJ = JSON.parse(fs.readFileSync(PANEL, 'utf8')), panel = PJ.envs[env], full = N === PJ._meta.seeds, bad = [];  /* check (1) needs the panel's own seeds */
  ROWS.forEach((j, i) => {
    const r = R[i], pub = j === 'base' ? panel.base.path : panel.rows[j].path, b = out.bands[j] = {};
    M.forEach(m => { const d = m === 'medW' ? 0 : 1; b[m] = {p10: [], p50: [], p90: [], mean: []};
      for (let t = 0; t < T; t++) { const s = r._s['p' + m + '_' + t]; b[m].p10.push(+H.quantileOf(s, 0.1).toFixed(d)); b[m].p50.push(+H.quantileOf(s, 0.5).toFixed(d)); b[m].p90.push(+H.quantileOf(s, 0.9).toFixed(d));
        const mean = +(+r['p' + m + '_' + t]).toFixed(d); b[m].mean.push(mean); if (full && mean !== pub[m][t]) bad.push(j + ' ' + m + ' year ' + (t + 1) + ': ' + mean + ' vs published ' + pub[m][t]); } });
    const dec = out.deciles[j] = {y7: Q.map(() => 0), end: Q.map(() => 0)};
    for (let s = 0; s < N; s++) { const seg = segs[s*cfg.length + i]; Q.forEach((q, n) => { dec.y7[n] += seg[6].dec[n]/N; dec.end[n] += seg[T - 1].dec[n]/N; }); }
    dec.y7 = dec.y7.map(x => Math.round(x)); dec.end = dec.end.map(x => Math.round(x));
    const life = segs[(LS - 1)*cfg.length + i], n = life[0].n;
    out.lives[j] = {f: [], w: []};
    for (let a = 0; a < n; a++) { out.lives[j].f.push(life.map(y => y.f[a].toString(16)).join('')); out.lives[j].w.push(life.map(y => y.w[a])); }
    for (let t = 0; t < T; t++) [['bO', 1], ['f0', 2], ['pov', 4]].forEach(([m, bit]) => { const cnt = life[t].f.filter(x => x & bit).length, eng = r._s['p' + m + '_' + t][LS - 1];
      if (Math.abs(cnt/n*100 - eng) > 1e-9) bad.push(j + ' seed ' + LS + ' ' + m + ' year ' + (t + 1) + ': adults ' + (cnt/n*100) + '% vs engine ' + eng + '%'); });
  });
  if (bad.length) { console.error('SELF-CHECK FAILED (' + bad.length + '):\n  ' + bad.slice(0, 20).join('\n  ')); process.exit(1); }
  out._meta.selfCheck = (full ? '' : 'NOT COMPARED WITH THE PANEL (seeds differ); ') + 'yearly means equal the published path (' + PANEL.replace(ROOT + path.sep, '') + '); seed ' + LS + '\'s adults add up to the engine\'s yearly shares';
} finally { H.resetNR6(svN); H.tbSetG(svG); C.WEALTH_FLOOR = wf0; }
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const file = path.join(ROOT, 'dev', 'runs', 'explore-' + env + '-' + YRS + '.json');
fs.writeFileSync(file, JSON.stringify(out));
console.log('self-check passed; wrote ' + file + ' (' + out._meta.seconds + ' s)');
