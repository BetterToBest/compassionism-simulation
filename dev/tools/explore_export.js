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
 * v5.4 step 9: --v54 runs the v5.4 rows (releaseRowsV54; both runs with REL_V54) and checks them against the merged v5.4 panel.
 * Session 7 (Oct 14, 2026; ledger s164, decision d208): --suite adds the visual suite's series and writes dev/runs/explore-suite-ENV-YRS[-sn|-snab].json.
 * For each row and year, the mean over seeds and the 10th and 90th percentile across seeds of:
 *  - tiers: the share of adults in each BLEI tier, on the BLEI paper's reading in today's prices (Crisis under 7 days, Precarious 7-30, Threshold 30-120,
 *    Stable 120-365, Secure 365-730, Flourishing 730 and over; CFG.BLEI_*_MAX), for all adults, participants and non-participants;
 *  - medBlei: the median BLEI (days), all, participants, non-participants; and its parts: savings (20% of wealth), income (a share of a month's wage) and
 *    BU (a month of the BU spent on essentials), each in days, as medians (which do not add up) and as means (which do);
 *  - bO and bN: the share below 30 days on the BLEI paper's reading and on the same-rules reading (earlier called design-neutral);
 *  - relPov: relative income poverty, cash income below 60% of the same run's median (the definition the page's Five Measures card used);
 *  - ep: extreme poverty (unhoused), the engine's own yearly figure; part: the share taking part in the programme.
 *  A group with no adults (participants, with no programme) is null, not 0; a seed with none is left out of that year's mean and percentiles.
 * --out=FILE writes the file there instead. --sn runs every row with today's safety net (row option sn); --snab with SNAP's work rule on as well (SNET.abawd). --panel=FILE compares the yearly
 * means with that merged panel instead of the default one (a panel made with the same options; the v5.6 study makes its own).
 * Extra self-checks with --suite: the hook's bO equals the published path's measure year by year, and the mean over years of ep equals each run's epPY. */
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const ARG = process.argv.slice(2).filter(a => !/^--/.test(a)), V54 = process.argv.indexOf('--v54') >= 0, V53 = V54 || process.argv.indexOf('--v53') >= 0;
const SUITE = process.argv.indexOf('--suite') >= 0, SNAB = process.argv.indexOf('--snab') >= 0, SN = SNAB || process.argv.indexOf('--sn') >= 0, SLOPE = SN && process.argv.indexOf('--slope') >= 0, PANEL_ARG = (process.argv.find(a => a.startsWith('--panel=')) || '').slice(8);
const env = ARG[0] || 'ref', YRS = +(ARG[1] || 20), N = +(ARG[2] || 500), LS = +(ARG[3] || 1);
const NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
if (!NAME || (YRS !== 20 && YRS !== 40) || !(LS >= 1 && LS <= N)) { console.error('usage: explore_export.js ref|adv|st [20|40] [SEEDS] [LIFESEED]'); process.exit(1); }
const ROOT = path.join(__dirname, '..', '..'), PANEL = PANEL_ARG ? path.resolve(PANEL_ARG) : path.join(ROOT, 'dev', 'runs', 'release-panel' + (YRS === 40 ? '-40' : '') + '.json');  /* the merged panel (with --v53, the v5.3 panel once it is merged) */
const C = H.CFG, SC = H.SPEND_SOURCED, M = ['f0', 'pov', 'bO', 'medW'], Q = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9];
const t0 = Date.now(), wf0 = C.WEALTH_FLOOR; C.WEALTH_FLOOR = -10000;  /* as the testbed command sets it */
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G);
const ROWS = ['base', 'release', 'h1', 'mid'];
const out = {_meta: {what: 'year-by-year spread across seeds, savings deciles and one seed\'s adults, for the pages\' explore sections (presentation only)', env, years: YRS, seeds: N, lifeSeed: LS,
  rows: ROWS, manifest: H.runManifest(), command: 'node dev/tools/explore_export.js ' + env + ' ' + YRS + ' ' + N + ' ' + LS + (V54 ? ' --v54' : V53 ? ' --v53' : '') + (SUITE ? ' --suite' : '') + (SNAB ? ' --snab' : SN ? ' --sn' : '') + (SLOPE ? ' --slope' : '') + (PANEL_ARG ? ' --panel=' + PANEL_ARG : ''),
  flags: {1: 'below 30 days of basic living (BLEI paper)', 2: 'below the cost of living', 4: 'too little wealth', 8: 'taking part in the programme'}}, bands: {}, deciles: {}, lives: {}};
let segs = [], cur = null;
try {
  const P = Object.assign({}, H[NAME], {years: YRS}), PR = H.tbPresets(P), rel = V54 ? H.releaseRowsV54(SC) : V53 ? H.releaseRowsV53(SC) : H.releaseRows(SC), byJ = {};
  rel.forEach(r => { byJ[r.j] = r; });
  const cfg = [Object.assign({p: PR.baseline(), sc: SC}, V53 ? {hh: H.REL_V53.hh, sg: H.REL_V53.sg, g: H.REL_V53.g} : {}, V54 ? H.REL_V54 : {})].concat(['release', 'h1', 'mid'].map(j => { const r = byJ[j], c = H.n1Row(PR, 'framework', r.v); if (r.v.o) Object.assign(c.o || (c.o = {}), r.v.o); return c; }));
  if (SN) cfg.forEach(c => { c.sn = Object.assign(SNAB ? {abawd: true} : {}, SLOPE ? {slope: true} : {}); });  /* session 7: today's safety net, and SNAP's work rule; session 9: --slope, SNET.slope (i24-1) */
  const T = YRS, L30 = C.BLEI_PRECARIOUS_MAX, TB = [C.BLEI_CRISIS_MAX, C.BLEI_PRECARIOUS_MAX, C.BLEI_THRESHOLD_MAX, C.BLEI_STABLE_MAX, C.BLEI_SECURE_MAX];
  const tierOf = d => { let k = 0; while (k < TB.length && d >= TB[k]) k++; return k; }, med = x => x.length ? H.quantileOf(x, 0.5) : null, mean = x => x.length ? x.reduce((s, v) => s + v, 0)/x.length : 0;
  /* session 7 (--suite): one year of one run, the visual suite's series */
  function suiteYear(agents, p, lf, ep) {
    const g = {all: [], part: [], non: []}, sav = [], inc = [], bu = [], cash = [], n = agents.length; let bO = 0, bN = 0;
    agents.forEach(a => { const bo = H.agentBLEI(a, p.bu, p.ccoOn, p.pth, p.szh, p.szhCoh, p.ptf)/lf, bn = (H.agentBLEI(a, 0, false, false, false, 0, false) + (a._tbM || 0)/C.BASE_DAILY_COST)/lf;
      const s0 = H.agentBLEI(Object.assign({}, a, {wealth: 0}), p.bu, p.ccoOn, p.pth, p.szh, p.szhCoh, p.ptf)/lf, b0 = H.agentBLEI(a, 0, p.ccoOn, p.pth, p.szh, p.szhCoh, p.ptf)/lf;
      g.all.push(bo); g[a.inCCO ? 'part' : 'non'].push(bo); sav.push(bo - s0); bu.push(bo - b0); inc.push(bo - (bo - s0) - (bo - b0));
      if (bo < L30) bO++; if (bn < L30) bN++; cash.push(H.tbCashIncome(a)); });
    const cm = med(cash), r = {bO: bO/n*100, bN: bN/n*100, relPov: cash.filter(c => c < 0.6*cm).length/n*100, ep: ep, part: g.part.length/n*100,
      medSav: med(sav), medInc: med(inc), medBu: med(bu), meanSav: mean(sav), meanInc: mean(inc), meanBu: mean(bu)};
    ['all', 'part', 'non'].forEach(k => { const t = [0, 0, 0, 0, 0, 0]; g[k].forEach(d => { t[tierOf(d)]++; }); const m = g[k].length;
      r['med_' + k] = med(g[k]); t.forEach((c, i) => { r['tier' + i + '_' + k] = m ? c/m*100 : null; }); });
    return r; }
  /* The hook sees every simulated year of every run in tbStudy's order (seed outer, row inner). tbRun may first run one year to set the contribution
   * rate; that short run is recognised (it ends after one year) and dropped. */
  function close() { if (cur && cur.length === T) segs.push(cur); cur = null; }
  let k = 0;
  H.setRepHook(function (agents, yr, TT, lf, ep) {
    if (yr === 0) close();
    if (yr === 0) cur = [];
    const slot = segs.length, seed = Math.floor(slot/cfg.length) + 1, row = slot % cfg.length, rec = {};
    if (yr === 6 || yr === T - 1) { const w = agents.map(a => a.wealth/lf); rec.dec = Q.map(q => H.quantileOf(w, q)); }
    if (seed === LS) { const p = cfg[row].p;
      rec.f = agents.map(a => { const bo = H.agentBLEI(a, p.bu, p.ccoOn, p.pth, p.szh, p.szhCoh, p.ptf);
        return (bo/lf < L30 ? 1 : 0) | ((a._tbGap || 0) > 0 ? 2 : 0) | (a.wealth < C.POVERTY_LINE*lf ? 4 : 0) | (a.inCCO ? 8 : 0); });
      rec.w = agents.map(a => Math.round(a.wealth/lf/100)); rec.n = agents.length; }
    if (SUITE) rec.s = suiteYear(agents, cfg[row].p, lf, ep);
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
  if (SUITE) { out.suite = {}; out._meta.suite = {tiers: ['Crisis', 'Precarious', 'Threshold', 'Stable', 'Secure', 'Flourishing'], tierDays: TB, units: 'shares in % of adults; BLEI and its parts in days of basic living, today\'s prices; ep in %'};
    ROWS.forEach((j, i) => { const keys = Object.keys(segs[i][0].s), S = out.suite[j] = {};
      keys.forEach(key => { const m = [], lo = [], hi = []; for (let t = 0; t < T; t++) { const v = []; for (let sd = 0; sd < N; sd++) { const x = segs[sd*cfg.length + i][t].s[key]; if (x !== null) v.push(x); }  /* null: no adult in the group (participants with no programme) */
        m.push(v.length ? +mean(v).toFixed(4) : null); lo.push(v.length ? +H.quantileOf(v, 0.1).toFixed(4) : null); hi.push(v.length ? +H.quantileOf(v, 0.9).toFixed(4) : null); } S[key] = {mean: m, p10: lo, p90: hi}; });
      for (let sd = 0; sd < N; sd++) { const seg = segs[sd*cfg.length + i], ep = mean(seg.map(y => y.s.ep)), e = R[i]._s.epPY[sd];
        if (Math.abs(ep - e) > 1e-9) bad.push(j + ' seed ' + (sd + 1) + ': mean yearly ep ' + ep + ' vs epPY ' + e);
        for (let t = 0; t < T; t++) { const b = seg[t].s.bO, eng = R[i]._s['pbO_' + t][sd]; if (Math.abs(b - eng) > 1e-9) bad.push(j + ' seed ' + (sd + 1) + ' bO year ' + (t + 1) + ': ' + b + ' vs ' + eng); } } }); }
  if (bad.length) { console.error('SELF-CHECK FAILED (' + bad.length + '):\n  ' + bad.slice(0, 20).join('\n  ')); process.exit(1); }
  out._meta.selfCheck = (full ? '' : 'NOT COMPARED WITH THE PANEL (seeds differ); ') + 'yearly means equal the published path (' + PANEL.replace(ROOT + path.sep, '') + '); seed ' + LS + '\'s adults add up to the engine\'s yearly shares';
} finally { H.resetNR6(svN); H.tbSetG(svG); C.WEALTH_FLOOR = wf0; }
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const OUTF = (process.argv.find(a => a.startsWith('--out=')) || '').slice(6);  /* session 7: --out=FILE writes there (the s165 job keeps its worktree clean) */
const file = OUTF ? path.resolve(OUTF) : path.join(ROOT, 'dev', 'runs', (SUITE ? 'explore-suite-' : 'explore-') + env + '-' + YRS + (SNAB ? '-snab' : SN ? '-sn' : '') + '.json');
fs.writeFileSync(file, JSON.stringify(out));
console.log('self-check passed; wrote ' + file + ' (' + out._meta.seconds + ' s)');
