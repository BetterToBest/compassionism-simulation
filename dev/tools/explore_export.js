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
 * Extra self-checks with --suite: the hook's bO equals the published path's measure year by year, and the mean over years of ep equals each run's epPY.
 * Session 12 (Oct 14, 2026; dev/plans/next-study-plan.md Tier A, dev/DECISIONS.md Session 12): --study adds the next study's per-person fields
 * (dev/tools/study_fields.js: EPPM and its parts against each adult's no-programme twin, the monthly surplus in both runs, Acre Equity in days and
 * the simulated CSI reading, the wealth Gini net of drain, breakdowns by the twin's income fifth, household type, age band and membership, what each
 * fifth receives and pays, movement between the six tiers) and writes dev/runs/explore-study-ENV-YRS[-sn|-snab].json without the bands, deciles
 * and lives. It runs every row with the measured EDC (row option em) and the accounting check (ACCT) on; both are reporting only, and the bands'
 * self-check against the published panel proves the figures unchanged. Extra self-checks: no accounting identity fails; the per-adult below-30-days
 * count equals the engine's bO; the ordinary wealth Gini equals the engine's at Year 7 and the last year; every adult of a programme run has a twin;
 * EPPM's parts add up (study_fields.js throws otherwise).
 * S47 (Nov 6, 2026; research-update prereg/run-manifest.md, job X): --frozen runs the frozen model (harness.js frozenRow: the audit's corrections and the second
 * implementation's fixes on every row, the no-programme run included, so each row's supply path is its own no-programme testbed run) on three rows: no programme
 * ('base'), the headline C2.2 design ('c22', harness.js c22Design) and the release design ('release'). Self-check (1) then needs a panel made the same way
 * (harness.js testbed N release ENV ... --frozen, merged) given with --panel=FILE; without one the bands are not compared, and the file says so. With --suite it
 * writes the visual suite's series (BLEI tiers, the median BLEI and its parts, relative income poverty, extreme poverty) for the three rows.
 * S11 (Nov 16, 2026; research-update prereg/2026-11-x2-series-addendum.md, job X2, ledger D30): --r2 runs release 2's main row (harness.js r2FreezePair, as
 * compassionism-sim-results runner/jobs/r2.js part M runs it: 500 adults, study options harness.js r2MainStudy, each row in its own study call, no
 * change to CFG.WEALTH_FLOOR) on three rows: no programme ('base'), the C2.2 design ('c22') and the release design ('release'). The rows carry today's
 * safety net with SNAP's work rule and its slope already (R2_MAIN.sn), so --r2 refuses --sn, --snab, --slope, --frozen, --v53, --v54 and --study.
 * Self-check (1) under --r2 compares every engine output key of every row and seed 1..N with release 2's stored part M shard, given with
 * --panel=FILE (r2-m-ENV-YEARS-104691f/shard-0000.json[.gz]; ENV str for st): equal values (non-finite stored as null) prove the run is release 2's
 * main row on this engine; without --panel the file says it was not compared. Check (2) and the --suite checks are unchanged.
 * S79 (Nov 16, 2026; research-update prereg/2026-11-x3-measures-addendum.md, job X3): --r2 --study adds the measures study and the BLEI paper's other
 * measures to release 2's main row. Every row gets two reporting switches release 2 did not carry: em (the measured EDC: rent and interest paid) and fb
 * {dist 'lambda', scale 1} (FBS50's tally with each adult's own lambda: the advancement rule as it is); the accounting check (ACCT) runs as under --study.
 * Each seed's three rows run one after another, each its own study call on that seed (part M ran each row over all seeds in one call; a seed's run does
 * not read the seeds before it), so the no-programme twin of every adult is at hand. Check (1) still compares every engine key of every row and seed with
 * part M; the only keys allowed beyond part M's are the two switches' own (EDC_KEYS, FBS_KEYS). It writes out.study and out.studyRun as --study does,
 * and out.measures: per row the mean and 10th-90th percentile over seeds of the EDC and FBS keys, cost, epPY, fgt0PY and fgt1PY; for the two designs the
 * public costs avoided (IPBI's modelled part, computed from the means as release 1's panel does) and paired differences against no programme with 95%
 * intervals (tbDiff). --r2 --study refuses --suite (job X2 has the suite series). */
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const ARG = process.argv.slice(2).filter(a => !/^--/.test(a)), V54 = process.argv.indexOf('--v54') >= 0, V53 = V54 || process.argv.indexOf('--v53') >= 0;
const STUDY = process.argv.indexOf('--study') >= 0, SF = STUDY ? require('./study_fields.js') : null, SUITE = process.argv.indexOf('--suite') >= 0, SNAB = process.argv.indexOf('--snab') >= 0, SN = SNAB || process.argv.indexOf('--sn') >= 0, SLOPE = SN && process.argv.indexOf('--slope') >= 0, PANEL_ARG = (process.argv.find(a => a.startsWith('--panel=')) || '').slice(8);
const R2 = process.argv.indexOf('--r2') >= 0;  /* S11: release 2's main row */
if (R2 && ['--sn', '--snab', '--slope', '--frozen', '--v53', '--v54'].some(f => process.argv.indexOf(f) >= 0)) { console.error('--r2 runs release 2\'s main row as it is: no --sn, --snab, --slope, --frozen, --v53 or --v54'); process.exit(1); }
const R2S = R2 && STUDY;  /* S79: release 2's main row with the measures study, each seed's rows run one after another (seed outer) so every adult has its twin */
if (R2S && SUITE) { console.error('--r2 --study does not take --suite (job X2 recorded the suite series)'); process.exit(1); }
const R2_ADDED = R2S ? H.EDC_KEYS.concat(H.FBS_KEYS) : [];  /* S79: the keys the two reporting switches add (em, fb); every other key must equal release 2's */
const env = ARG[0] || 'ref', YRS = +(ARG[1] || 20), N = +(ARG[2] || 500), LS = +(ARG[3] || 1);
const NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
if (!NAME || (YRS !== 20 && YRS !== 40) || !(LS >= 1 && LS <= N)) { console.error('usage: explore_export.js ref|adv|st [20|40] [SEEDS] [LIFESEED]'); process.exit(1); }
const ROOT = path.join(__dirname, '..', '..'), PANEL = PANEL_ARG ? path.resolve(PANEL_ARG) : path.join(ROOT, 'dev', 'runs', 'release-panel' + (YRS === 40 ? '-40' : '') + '.json');  /* the merged panel (with --v53, the v5.3 panel once it is merged) */
const C = H.CFG, SC = H.SPEND_SOURCED, M = ['f0', 'pov', 'bO', 'medW'], Q = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9];
const t0 = Date.now(), wf0 = C.WEALTH_FLOOR; if (!R2) C.WEALTH_FLOOR = -10000;  /* as the testbed command sets it (S11: the r2 job leaves it as it is) */
const svS = H.startRelease(), svN = svS.svN, svG = svS.svG;
const FRZ = process.argv.indexOf('--frozen') >= 0;  /* S47 */
const ROWS = FRZ || R2 ? ['base', 'c22', 'release'] : ['base', 'release', 'h1', 'mid'];
const out = {_meta: {what: 'year-by-year spread across seeds, savings deciles and one seed\'s adults, for the pages\' explore sections (presentation only)', env, years: YRS, seeds: N, lifeSeed: LS,
  rows: ROWS, manifest: H.runManifest(), command: 'node dev/tools/explore_export.js ' + env + ' ' + YRS + ' ' + N + ' ' + LS + (V54 ? ' --v54' : V53 ? ' --v53' : '') + (SUITE ? ' --suite' : '') + (STUDY ? ' --study' : '') + (SNAB ? ' --snab' : SN ? ' --sn' : '') + (SLOPE ? ' --slope' : '') + (FRZ ? ' --frozen' : '') + (R2 ? ' --r2' : '') + (PANEL_ARG ? ' --panel=' + PANEL_ARG : ''),
  flags: {1: 'below 30 days of basic living (BLEI paper)', 2: 'below the cost of living', 4: 'too little wealth', 8: 'taking part in the programme'}}, bands: {}, deciles: {}, lives: {}};
let segs = [], cur = null;
try {
  const P = Object.assign({}, H[NAME], {years: YRS}, R2 ? {nAgents: 500} : {}), PR = H.tbPresets(P), rel = V54 ? H.releaseRowsV54(SC) : V53 ? H.releaseRowsV53(SC) : H.releaseRows(SC), byJ = {};
  rel.forEach(r => { byJ[r.j] = r; });
  const cfg = [Object.assign({p: PR.baseline(), sc: SC}, V53 ? {hh: H.REL_V53.hh, sg: H.REL_V53.sg, g: H.REL_V53.g} : {}, V54 ? H.REL_V54 : {})].concat(ROWS.slice(1).map(j => { const r = byJ[j === 'c22' ? 'release' : j], c = H.n1Row(PR, 'framework', r.v); if (r.v.o) Object.assign(c.o || (c.o = {}), r.v.o); return j === 'c22' ? H.c22Design(c) : c; }));
  if (FRZ) cfg.forEach(H.frozenRow);  /* S47: the frozen model, every row */
  if (R2) { const pc = H.r2FreezePair(P, 'c22'); cfg.splice(0, cfg.length, pc[0], pc[1], H.r2FreezePair(P, 'rel')[1]); }  /* S11: as r2.js mainRows builds none, c22, rel */
  if (STUDY) cfg.forEach(c => { c.em = true; });  /* session 12: the measured EDC's rent and interest (reporting only) */
  if (R2S) cfg.forEach(c => { c.fb = {dist: 'lambda', scale: 1}; });  /* S79: FBS50's tally with each adult's own lambda, the rule unchanged (index.html FBS50; reporting only) */
  if (SN) cfg.forEach(c => { c.sn = Object.assign(SNAB ? {abawd: true} : {}, SLOPE ? {slope: true} : {}); });  /* session 7: today's safety net, and SNAP's work rule; session 9: --slope, SNET.slope (i24-1) */
  const T = YRS, L30 = C.BLEI_PRECARIOUS_MAX, TB = [C.BLEI_CRISIS_MAX, C.BLEI_PRECARIOUS_MAX, C.BLEI_THRESHOLD_MAX, C.BLEI_STABLE_MAX, C.BLEI_SECURE_MAX];
  const tierOf = d => { let k = 0; while (k < TB.length && d >= TB[k]) k++; return k; }, med = x => x.length ? H.quantileOf(x, 0.5) : null, mean = x => x.length ? x.reduce((s, v) => s + v, 0)/x.length : 0;
  /* session 7 (--suite): one year of one run, the visual suite's series */
  /* S81 (Nov 17, 2026): the same year with each adult counted at its weight a._w (1 where the run has none, so v5.6's weighted keys equal its plain ones).
   * v5.9's runs give 18 top-tail adults the place of very rich families, so a plain mean, share or median over the simulated adults counts those 18 once
   * each; the w-keys count them at their share of the population. The plain keys are unchanged (they equal the stored suite files). */
  const wMean = (x, w) => { let s = 0, t = 0; for (let i = 0; i < x.length; i++) { s += x[i]*w[i]; t += w[i]; } return t > 0 ? s/t : 0; };
  const wMed = (x, w) => { if (!x.length) return null; const ix = x.map((_, i) => i).sort((i, j) => x[i] - x[j]); let t = 0; ix.forEach(i => { t += w[i]; }); if (!(t > 0)) return null;
    let c = 0; const pos = ix.map(i => { const q = (c + w[i]/2)/t; c += w[i]; return q; }); if (0.5 <= pos[0]) return x[ix[0]]; if (0.5 >= pos[pos.length - 1]) return x[ix[ix.length - 1]];
    let k = 0; while (pos[k + 1] < 0.5) k++; const f = (0.5 - pos[k])/(pos[k + 1] - pos[k]); return x[ix[k]] + f*(x[ix[k + 1]] - x[ix[k]]); };
  function suiteYear(agents, p, lf, ep) {
    const g = {all: [], part: [], non: []}, gw = {all: [], part: [], non: []}, sav = [], inc = [], bu = [], cash = [], wt = [], n = agents.length; let bO = 0, bN = 0, wO = 0, wN = 0, W = 0;
    agents.forEach(a => { const bo = H.agentBLEI(a, p.bu, p.ccoOn, p.pth, p.szh, p.szhCoh, p.ptf)/lf, bn = (H.agentBLEI(a, 0, false, false, false, 0, false) + (a._tbM || 0)/C.BASE_DAILY_COST)/lf, w = a._w === undefined ? 1 : +a._w;
      const s0 = H.agentBLEI(Object.assign({}, a, {wealth: 0}), p.bu, p.ccoOn, p.pth, p.szh, p.szhCoh, p.ptf)/lf, b0 = H.agentBLEI(a, 0, p.ccoOn, p.pth, p.szh, p.szhCoh, p.ptf)/lf;
      g.all.push(bo); g[a.inCCO ? 'part' : 'non'].push(bo); gw.all.push(w); gw[a.inCCO ? 'part' : 'non'].push(w); sav.push(bo - s0); bu.push(bo - b0); inc.push(bo - (bo - s0) - (bo - b0)); wt.push(w); W += w;
      if (bo < L30) { bO++; wO += w; } if (bn < L30) { bN++; wN += w; } cash.push(H.tbCashIncome(a)); });
    const cm = med(cash), r = {bO: bO/n*100, bN: bN/n*100, relPov: cash.filter(c => c < 0.6*cm).length/n*100, ep: ep, part: g.part.length/n*100,
      medSav: med(sav), medInc: med(inc), medBu: med(bu), meanSav: mean(sav), meanInc: mean(inc), meanBu: mean(bu)};
    ['all', 'part', 'non'].forEach(k => { const t = [0, 0, 0, 0, 0, 0]; g[k].forEach(d => { t[tierOf(d)]++; }); const m = g[k].length;
      r['med_' + k] = med(g[k]); t.forEach((c, i) => { r['tier' + i + '_' + k] = m ? c/m*100 : null; }); });
    /* S81: the weighted keys */
    const wcm = wMed(cash, wt); let wrp = 0; cash.forEach((c, i) => { if (c < 0.6*wcm) wrp += wt[i]; });
    Object.assign(r, {wbO: wO/W*100, wbN: wN/W*100, wrelPov: wrp/W*100, wpart: gw.part.reduce((s, v) => s + v, 0)/W*100,
      wmedSav: wMed(sav, wt), wmedInc: wMed(inc, wt), wmedBu: wMed(bu, wt), wmeanSav: wMean(sav, wt), wmeanInc: wMean(inc, wt), wmeanBu: wMean(bu, wt)});
    ['all', 'part', 'non'].forEach(k => { const t = [0, 0, 0, 0, 0, 0]; let m = 0; g[k].forEach((d, i) => { t[tierOf(d)] += gw[k][i]; m += gw[k][i]; });
      r['wmed_' + k] = wMed(g[k], gw[k]); t.forEach((c, i) => { r['wtier' + i + '_' + k] = m > 0 ? c/m*100 : null; }); });
    return r; }
  /* The hook sees every simulated year of every run in tbStudy's order (seed outer, row inner). tbRun may first run one year to set the contribution
   * rate; that short run is recognised (it ends after one year) and dropped. */
  function close() { if (cur && cur.length === T) segs.push(cur); cur = null; }
  let k = 0, twinYr = [], seqMap = null; const stKeys = [];
  H.setRepHook(function (agents, yr, TT, lf, ep) {
    if (yr === 0) close();
    if (yr === 0) cur = [];
    const slot = segs.length, RO = R2 && !R2S, seed = RO ? slot % N + 1 : Math.floor(slot/cfg.length) + 1, row = RO ? Math.floor(slot/N) : slot % cfg.length, rec = {};  /* S11: under --r2 row outer, seed inner (S79: --r2 --study seed outer) */
    if (yr === 6 || yr === T - 1) { const w = agents.map(a => a.wealth/lf); rec.dec = Q.map(q => H.quantileOf(w, q)); }
    if (seed === LS) { const p = cfg[row].p;
      rec.f = agents.map(a => { const bo = H.agentBLEI(a, p.bu, p.ccoOn, p.pth, p.szh, p.szhCoh, p.ptf);
        return (bo/lf < L30 ? 1 : 0) | ((a._tbGap || 0) > 0 ? 2 : 0) | (a.wealth < C.POVERTY_LINE*lf ? 4 : 0) | (a.inCCO ? 8 : 0); });
      rec.w = agents.map(a => Math.round(a.wealth/lf/100)); rec.n = agents.length; }
    if (SUITE) rec.s = suiteYear(agents, cfg[row].p, lf, ep);
    if (STUDY) { const recs = agents.map((a, ix) => SF.adult(H, a, cfg[row].p, lf, tierOf, ix)); if (row === 0) twinYr[yr] = new Map(recs.map(r => [r.id, r]));
      if (yr === 0) seqMap = new Map(); recs.forEach(r => { if (!seqMap.has(r.id)) seqMap.set(r.id, []); seqMap.get(r.id)[yr] = r.tier; });
      const y = SF.yearSummary(recs, row === 0 ? null : twinYr[yr], L30), K = stKeys[row] || (stKeys[row] = Object.keys(y.s));  /* packed: about 1 MB a seed instead of 9 */
      if (K.length !== Object.keys(y.s).length) throw new Error('study keys changed'); rec.st = Float64Array.from(K, x => y.s[x] === null || y.s[x] === undefined ? NaN : y.s[x]); rec.stPaired = y.paired; rec.stN = y.n; rec.stBO = recs.filter(r => r.bo < L30).length/recs.length*100;
      if (yr === T - 1) rec.run = SF.runSummary(seqMap, T); }
    cur.push(rec); k++;
  });
  if (STUDY) H.setAcct(H.acctNew());  /* session 12: the per-adult flows of the accounting check (reporting only) */
  let R; try {
    if (R2S) { R = cfg.map(() => ({_s: {}}));  /* S79: each row its own study call on one seed (part M's call is per row; a seed's run does not depend on the seeds before it, and check (1) proves it) */
      for (let s = 1; s <= N; s++) cfg.forEach((c, i) => { const r = H.tbStudy([c], s, P, H.r2MainStudy(), s)[0]; close();
        Object.keys(r._s).forEach(key => { const A = R[i]._s[key] || (R[i]._s[key] = new Float64Array(N)); A[s - 1] = r._s[key][0]; }); });
      R.forEach(r => { Object.keys(r._s).forEach(key => { r[key] = r._s[key].reduce((a, v) => a + v, 0)/N; }); }); }
    else if (R2) { R = cfg.map(c => { const r = H.tbStudy([c], N, P, H.r2MainStudy())[0]; close(); return r; });  /* S11: each row its own study call, as part M */
      if (segs.length === N*cfg.length) { const o = []; for (let s = 0; s < N; s++) for (let i = 0; i < cfg.length; i++) o.push(segs[i*N + s]); segs = o; } }  /* back to seed outer, row inner */
    else { R = H.tbStudy(cfg, N, P, Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: SC}, H.REL_V52_STUDY)); close(); }
  } finally { H.setRepHook(null); }
  const ACC = STUDY ? H.getAcct() : null; if (STUDY) H.setAcct(null);
  if (segs.length !== N*cfg.length) throw new Error('expected ' + N*cfg.length + ' runs from the hook, saw ' + segs.length);
  const readJ = f => JSON.parse(/\.gz$/.test(f) ? require('zlib').gunzipSync(fs.readFileSync(f)).toString('utf8') : fs.readFileSync(f, 'utf8'));
  const PJ = (FRZ || R2) && !PANEL_ARG ? null : readJ(PANEL), panel = PJ && !R2 ? PJ.envs[env] : null, full = !R2 && !!PJ && N === PJ._meta.seeds, bad = [];
  let r2Cmp = null;  /* S11: every key, row and seed against release 2's part M shard */
  if (R2 && PJ) { const pe = env === 'st' ? 'str' : env, mt = PJ._meta, fin = x => Number.isFinite(x) ? x : null; let nv = 0, nk = 0;
    if (mt.part !== 'M' || mt.env !== pe || mt.years !== YRS || mt.adults !== 500 || mt.seeds[0] !== 1 || mt.seeds[1] < N) throw new Error('--panel is not part M of release 2 for ' + pe + ', ' + YRS + ' years, 500 adults, seeds 1..' + N);
    ['none', 'c22', 'rel'].forEach((nm, i) => { const ref = PJ.rows[pe + '.' + nm], ours = R[i]._s; if (!ref) { bad.push('panel has no row ' + pe + '.' + nm); return; }
      Object.keys(ref).forEach(key => { if (!ours[key]) { bad.push(ROWS[i] + ': key ' + key + ' missing in this run'); return; } nk++;
        for (let s = 0; s < N; s++) { const a = fin(ours[key][s]), b = ref[key][s]; nv++; if (a !== b) bad.push(ROWS[i] + ' ' + key + ' seed ' + (s + 1) + ': ' + a + ' vs release 2 ' + b); } });
      Object.keys(ours).forEach(key => { if (!ref[key] && R2_ADDED.indexOf(key) < 0) bad.push(ROWS[i] + ': key ' + key + ' not in the panel'); }); });
    r2Cmp = {keys: nk, values: nv, engine: mt.manifest && mt.manifest.commit, engineBlockSha256: mt.manifest && mt.manifest.engineBlockSha256}; if (R2S) r2Cmp.added = R2_ADDED; }  /* check (1) needs the panel's own seeds; S47: under --frozen, a frozen panel */
  ROWS.forEach((j, i) => {
    const r = R[i], pub = !full ? null : j === 'base' ? panel.base.path : panel.rows[j].path, b = out.bands[j] = {};
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
  if (STUDY) { out.study = {}; out.studyRun = {}; const SM = function (v) { return v.length ? [+mean(v).toFixed(4), +H.quantileOf(v, 0.1).toFixed(4), +H.quantileOf(v, 0.9).toFixed(4)] : [null, null, null]; };
    out._meta.study = {tiers: ['Crisis', 'Precarious', 'Threshold', 'Stable', 'Secure', 'Flourishing'], definitions: 'dev/tools/study_fields.js', units: 'dollars a month in today\'s prices; shares in %; days of basic living; EPPM a ratio and its parts shares of the twins\' total',
      acct: {checks: ACC.n, failures: ACC.nFail}};
    Object.keys(ACC.nFail).forEach(id => { if (ACC.nFail[id]) bad.push('accounting identity ' + id + ' failed ' + ACC.nFail[id] + ' times'); });
    ROWS.forEach((j, i) => { const S = out.study[j] = {};
      for (let sd = 0; sd < N; sd++) for (let t = 0; t < T; t++) { const y = segs[sd*cfg.length + i][t];
        const eng = R[i]._s['pbO_' + t][sd]; if (Math.abs(y.stBO - eng) > 1e-9) bad.push(j + ' seed ' + (sd + 1) + ' study bO year ' + (t + 1) + ': ' + y.stBO + ' vs ' + eng);
        if (i > 0 && y.stPaired !== y.stN) bad.push(j + ' seed ' + (sd + 1) + ' year ' + (t + 1) + ': ' + (y.stN - y.stPaired) + ' adults without a twin'); }
      stKeys[i].forEach((key, ki) => { const m = [], lo = [], hi = []; for (let t = 0; t < T; t++) { const v = []; for (let sd = 0; sd < N; sd++) { const x = segs[sd*cfg.length + i][t].st[ki]; if (!isNaN(x)) v.push(x); }
        const r = SM(v); m.push(r[0]); lo.push(r[1]); hi.push(r[2]); } S[key] = {mean: m, p10: lo, p90: hi}; });
      const RS = out.studyRun[j] = {}, rk = Object.keys(segs[i][T - 1].run);
      rk.forEach(key => { const v = []; for (let sd = 0; sd < N; sd++) { const x = segs[sd*cfg.length + i][T - 1].run[key]; if (x !== null && x !== undefined) v.push(x); } const r = SM(v); RS[key] = {mean: r[0], p10: r[1], p90: r[2]}; });
      [['y7GiniW', 6], ['eGiniW', T - 1]].forEach(([g, t]) => { const e = R[i]._s[g]; if (!e) return; for (let sd = 0; sd < N; sd++) { const n = segs[sd*cfg.length + i][t].stN, x = segs[sd*cfg.length + i][t].st[stKeys[i].indexOf('giniW')]*n/(n - 1);
        if (Math.abs(x - e[sd]) > 1e-9) bad.push(j + ' seed ' + (sd + 1) + ' ' + g + ': ' + x + ' vs ' + e[sd]); } }); });
    delete out.bands; delete out.deciles; delete out.lives; }
  if (R2S) {  /* S79: the panel's measure keys for release 2's rows (EDC measured, FBS50's tally, the public costs avoided), as release 1's panel builds them */
    const MK = H.EDC_KEYS.concat(H.FBS_KEYS, ['cost', 'epPY', 'fgt0PY', 'fgt1PY']), AH = H.avoidHomelessHl(), B0 = R[0], q = (v, x) => +H.quantileOf(v, x).toFixed(4);
    out.measures = {}; out._meta.measures = {keys: MK, units: 'edc* and fbsAbove* in %; fbs50Med dollars a month; cost dollars per adult a year; epPY, fgt0PY in %; fgt1PY the poverty gap in % of the line',
      ipbi: 'from the means over seeds, as release 1\'s panel (harness.js testbed release): unhoused person-years avoided per 1,000 adults a year, homelessness costs low and high (AVOID_HOMELESS), prisons and hospital and psychiatric stays (avoidWide, main and high), each row against the no-programme row',
      d: 'paired difference row - no programme over the seeds, mean and 95% interval (harness.js tbDiff)'};
    ROWS.forEach((j, i) => { const r = R[i], o = out.measures[j] = {};
      MK.forEach(key => { if (r._s[key]) o[key] = {mean: +r[key].toFixed(4), p10: q(r._s[key], 0.1), p90: q(r._s[key], 0.9)}; });
      if (i === 0) return;
      const av = (B0.epPY - r.epPY)/100, aw = H.avoidWide((B0.fgt1PY - r.fgt1PY)/100*C.LIVING_WAGE_ANNUAL, (B0.fgt0PY - r.fgt0PY)/100);
      o.ipbi = {unhousedAvoided: +(av*1000).toFixed(2), avoidLo: Math.round(av*AH.low), avoidHi: Math.round(av*AH.high), avoidW: Math.round(aw.main), avoidWHi: Math.round(aw.high), avoidJail: Math.round(aw.jail), avoidHealth: Math.round(aw.health)};
      o.d = {}; ['edcM', 'edcMagg', 'cost', 'epPY', 'fgt0PY', 'fgt1PY'].forEach(key => { const x = H.tbDiff(r, B0, key); o.d[key] = [+x.m.toFixed(4), +x.lo.toFixed(4), +x.hi.toFixed(4)]; }); });
    ['edcM', 'fbsAbove'].forEach(key => { ROWS.forEach((j, i) => { if (!R[i]._s[key]) bad.push(j + ': no ' + key + ' (the reporting switch did not run)'); }); }); }
  if (bad.length) { console.error('SELF-CHECK FAILED (' + bad.length + '):\n  ' + bad.slice(0, 20).join('\n  ')); process.exit(1); }
  if (R2) out._meta.r2 = {rows: 'harness.js r2FreezePair: no programme, C2.2 and the release design (release 2\'s main row)', study: 'harness.js r2MainStudy', adults: 500, panelCheck: r2Cmp};
  out._meta.selfCheck = R2 ? (r2Cmp ? 'every engine key of every row equals release 2\'s part M (' + PANEL_ARG + ', engine ' + String(r2Cmp.engine).slice(0, 7) + '): ' + r2Cmp.keys + ' row-keys, ' + r2Cmp.values + ' values, seeds 1..' + N : 'NOT COMPARED WITH RELEASE 2 (--r2 without --panel)') + '; seed ' + LS + '\'s adults add up to the engine\'s yearly shares' + (SUITE ? '; the suite\'s bO equals the engine\'s and the mean yearly ep its epPY' : '') :
    (full ? '' : PJ ? 'NOT COMPARED WITH THE PANEL (seeds differ); ' : 'NOT COMPARED WITH A PANEL (--frozen without --panel); ') + 'yearly means equal the published path (' + PANEL.replace(ROOT + path.sep, '') + '); seed ' + LS + '\'s adults add up to the engine\'s yearly shares' + (STUDY ? '; study: no accounting identity failed, the adults\' below-30-days count equals the engine\'s bO, the wealth Gini equals the engine\'s at Year 7 and the last year, every adult has a twin, EPPM\'s parts add up' : '');
} finally { H.resetNR6(svN); H.tbSetG(svG); C.WEALTH_FLOOR = wf0; }
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const OUTF = (process.argv.find(a => a.startsWith('--out=')) || '').slice(6);  /* session 7: --out=FILE writes there (the s165 job keeps its worktree clean) */
const file = OUTF ? path.resolve(OUTF) : path.join(ROOT, 'dev', 'runs', (STUDY ? 'explore-study-' : SUITE ? 'explore-suite-' : 'explore-') + (R2 ? 'r2-' : '') + env + '-' + YRS + (SNAB ? '-snab' : SN ? '-sn' : '') + '.json');
fs.writeFileSync(file, JSON.stringify(svS.withSettings(out)));
console.log('self-check passed; wrote ' + file + ' (' + out._meta.seconds + ' s)');
