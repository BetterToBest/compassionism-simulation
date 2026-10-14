/* Session 12 (Oct 14, 2026; dev/plans/next-study-plan.md, Tier A; dev/DECISIONS.md Session 12): the next study's per-person fields, for
 * dev/tools/explore_export.js --study. Reporting only: it reads quantities the engine already keeps at the end of each simulated year
 * (the yearly records the poverty measures read, and the per-adult flows of the accounting check, ACCT, which is proven bit-identical
 * on or off by the unit suite); it changes no state and draws no random number.
 *
 * Per adult and year (dollars of the year; divided by the run's price level lf for today's dollars):
 *   D  cash income after the contribution: wages + conversion income + cash transfers (the comparator's UBI, unemployment insurance,
 *      Social Security, the programme's cash and today's safety net, SNAP and tax credits) - the contribution (yrTax)
 *   I  interest paid on debt (the accounting check's interest when it is negative); interest earned on savings is not counted
 *   B  allowance (BU) spent on essentials, at face value (the accounting check's BU spent)
 *   K  the basic basket at the run's general prices less what this adult paid for it (yrBasketUSD - yrCostUSD): the BU spent plus the
 *      community price cuts (business and housing members' cuts, the public grocery cut), less any medical bill above the basket line
 *      and any rent mark-up; P = K - B is everything but the allowance (called "community prices" on the page, with that caveat)
 *   N  resources = D - I + K; real resources R = N / lf (today's dollars). Rent is inside the basket: lower rent for community-housing
 *      members shows as their housing cut, inside P.
 *   surplus (monthly, the BLEI paper's financial bandwidth in the model's terms) = (D - I - yrCostUSD) / 12, floored at 0 when reported.
 *   EPPM for a group = sum of R with the programme / sum of R of the same adults in the no-programme run of the same seed (their twins).
 *   Its exact parts, in real terms (they add up to EPPM - 1): cash income D/lf, interest -I/lf, the allowance B/lf and the other basket
 *   changes P/lf, each with the programme less the twin's, divided by the twins' total R. Each run is deflated by its own price level,
 *   so the programme's effect on the general price level sits inside every part (chiefly the cash part); the price levels themselves
 *   are reported beside it (lf). A split with a separate price-level part was tried and rejected (dev/DECISIONS.md Session 12).
 */
'use strict';
const TIER_N = 6;

function quant(x, q) { if (!x.length) return null; const v = x.slice().sort((a, b) => a - b), h = (v.length - 1)*q, i = Math.floor(h); return i + 1 < v.length ? v[i] + (h - i)*(v[i + 1] - v[i]) : v[i]; }
function giniPos(x) { const v = x.map(z => Math.max(0, +z || 0)).sort((a, b) => a - b), n = v.length; let t = 0, w = 0; for (let i = 0; i < n; i++) { t += v[i]; w += (i + 1)*v[i]; } return n > 0 && t > 0 ? 2*w/(n*t) - (n + 1)/n : 0; }
function giniNeg(x) { const v = x.map(z => +z || 0).sort((a, b) => a - b), n = v.length; let t = 0, w = 0; for (let i = 0; i < n; i++) { t += v[i]; w += (i + 1)*v[i]; } return n > 0 && t > 0 ? 2*w/(n*t) - (n + 1)/n : 0; }

/* One adult at the end of one year. H: harness exports; p: the row's preset; tierOf: days -> tier index; idx: the adult's position. */
function adult(H, a, p, lf, tierOf, idx) {
  const C = H.CFG, E = +a.yrWageUSD || 0, D = E + (+a.yrConvUSD || 0) + (+a.yrUbiUSD || 0) + (+a.yrSSUSD || 0) + (+a.yrTbCash || 0) - (+a.yrTax || 0);
  const I = Math.max(0, -(+a._acI || 0)), B = +a._acBs || 0, mlc = +a.yrBasketUSD || 0, cost = +a.yrCostUSD || 0, K = mlc - cost, N = D - I + K;
  const bo = H.agentBLEI(a, p.bu, p.ccoOn, p.pth, p.szh, p.szhCoh, p.ptf)/lf, w = Math.max(0, +a.wealth || 0), eq = Math.max(0, +a.acreEquity || 0);
  const eqd = eq > 0 ? (H.agentBLEI(Object.assign({}, a, {wealth: w + eq/0.20}), p.bu, p.ccoOn, p.pth, p.szh, p.szhCoh, p.ptf) - H.agentBLEI(Object.assign({}, a, {wealth: w}), p.bu, p.ccoOn, p.pth, p.szh, p.szhCoh, p.ptf))/lf : 0;
  const hh = a._hh, ht = !hh || hh.single || hh.a.length < 2 ? (hh && hh.kids && hh.kids.length ? 'k' : 's') : (hh.kids && hh.kids.length ? 'k' : 'c');
  const age = typeof a.age === 'number' ? a.age : null, ab = age === null ? null : age < 35 ? 1 : age < 55 ? 2 : age < 65 ? 3 : 4;
  return {id: a._id === undefined ? 'i' + idx : a._id + ':' + (a._born || 0),  /* without ageing no adult leaves or joins: the position is the person */
    D, I, B, P: K - B, N, lf, R: N/lf, sur: (D - I - cost)/12/lf, bo, tier: tierOf(bo), eqd,
    wnet: ((+a.wealth || 0) - (+a._edcR || 0) - (+a._edcInt || 0))/lf, w: (+a.wealth || 0)/lf, part: !!a.inCCO, pth: !!a.inPTH, ptf: !!a.inPTF, ht, ab,
    recv: (B + (K - B) + (+a.yrConvUSD || 0) + (+a.yrTbCash || 0) - (+a._snB || 0))/lf, paid: (+a.yrTax || 0)/lf, sn: (+a._snB || 0)/lf, wage: E/12/lf, emp: E > 0 && !a._ret};
}

/* Fifth (1..5) of each value by the cut points of the reference list. */
function fifths(ref) { const c = [0.2, 0.4, 0.6, 0.8].map(q => quant(ref, q)); return x => { let k = 1; while (k < 5 && x > c[k - 1]) k++; return k; }; }

/* One year of one run: the summary kept for the seed. twin: Map id -> the no-programme run's adult record for this year (null for the
 * no-programme run itself, which is its own twin). Returns {s: numbers, paired, unpaired}. */
function yearSummary(recs, twin, L30) {
  const s = {}, n = recs.length, isBase = !twin, T = isBase ? new Map(recs.map(r => [r.id, r])) : twin;
  if (T.size !== (isBase ? n : T.size) || new Set(recs.map(r => r.id)).size !== n) throw new Error('adult ids are not unique');
  const tw = [...T.values()], fq = fifths(tw.map(r => r.D));
  const pct = (xs, f) => xs.length ? xs.filter(f).length/xs.length*100 : null, mean = xs => xs.length ? xs.reduce((a, b) => a + b, 0)/xs.length : null;
  const G = {all: recs, part: recs.filter(r => r.part), non: recs.filter(r => !r.part)};
  /* fields in both runs */
  Object.keys(G).forEach(g => { const x = G[g]; if (!x.length) { ['sur', 'sur0', 'cash', 'eqd', 'b730', 'c730'].forEach(k => { s[k + '_' + g] = null; }); return; }
    s['sur_' + g] = quant(x.map(r => Math.max(0, r.sur)), 0.5); s['sur0_' + g] = pct(x, r => r.sur <= 0); s['cash_' + g] = mean(x.map(r => r.D/12/r.lf));
    s['eqd_' + g] = mean(x.map(r => r.eqd)); s['b730_' + g] = pct(x, r => r.bo >= 730); s['c730_' + g] = pct(x, r => r.bo + r.eqd >= 730); });
  const pth = recs.filter(r => r.pth); s.pthShare = pct(recs, r => r.pth); s.eqdMedPth = pth.length ? quant(pth.map(r => r.eqd), 0.5) : null;
  s.giniW = giniPos(recs.map(r => r.w)); s.giniWN = giniNeg(recs.map(r => r.w)); s.giniWnet = giniPos(recs.map(r => r.wnet)); s.giniWnetN = giniNeg(recs.map(r => r.wnet));
  s.lf = recs.length ? recs[0].lf : null; const wk = recs.filter(r => r.emp); s.wageMean = mean(wk.map(r => r.wage));
  s.intMean = mean(recs.map(r => r.I/12/r.lf)); s.buMean = mean(recs.map(r => r.B/12/r.lf)); s.cutMean = mean(recs.map(r => r.P/12/r.lf));
  /* by the twin's cash-income fifth (the same people in both runs) */
  let paired = 0; const Q = [[], [], [], [], [], []];
  recs.forEach(r => { const t = T.get(r.id); if (!t) return; paired++; Q[fq(t.D)].push([r, t]); });
  for (let q = 1; q <= 5; q++) { const x = Q[q].map(z => z[0]); s['bO_q' + q] = pct(x, r => r.bo < L30); s['sur_q' + q] = x.length ? quant(x.map(r => Math.max(0, r.sur)), 0.5) : null;
    if (!isBase) { s['recv_q' + q] = mean(x.map(r => r.recv/12)); s['paid_q' + q] = mean(x.map(r => r.paid/12)); s['snD_q' + q] = mean(Q[q].map(z => (z[0].sn - z[1].sn)/12)); } }
  if (!isBase) {  /* EPPM: this person with the programme against their twin without it */
    const grp = {all: r => true, part: r => r.part, non: r => !r.part, pq1: (r, t) => r.part && fq(t.D) === 1, pth: r => r.pth, ptf: r => r.ptf,
      q1: (r, t) => fq(t.D) === 1, q2: (r, t) => fq(t.D) === 2, q3: (r, t) => fq(t.D) === 3, q4: (r, t) => fq(t.D) === 4, q5: (r, t) => fq(t.D) === 5,
      hs: (r, t) => t.ht === 's', hc: (r, t) => t.ht === 'c', hk: (r, t) => t.ht === 'k', a1: (r, t) => t.ab === 1, a2: (r, t) => t.ab === 2, a3: (r, t) => t.ab === 3, a4: (r, t) => t.ab === 4};
    const PARTS = ['all', 'part', 'pq1', 'non'];
    Object.keys(grp).forEach(g => { let Rt = 0, Rw = 0, cD = 0, cI = 0, cB = 0, cP = 0, m = 0, up = 0;
      recs.forEach(r => { const t = T.get(r.id); if (!t || !grp[g](r, t)) return; m++; Rt += t.R; Rw += r.R; if (r.R > t.R) up++;
        cD += r.D/r.lf - t.D/t.lf; cI -= r.I/r.lf - t.I/t.lf; cB += r.B/r.lf - t.B/t.lf; cP += r.P/r.lf - t.P/t.lf; });
      s['n_' + g] = m; s['eppm_' + g] = m && Rt > 0 ? Rw/Rt : null; s['up_' + g] = m ? up/m*100 : null;
      if (PARTS.indexOf(g) >= 0) { const ok = m && Rt > 0; s['eD_' + g] = ok ? cD/Rt : null; s['eI_' + g] = ok ? cI/Rt : null; s['eB_' + g] = ok ? cB/Rt : null; s['eP_' + g] = ok ? cP/Rt : null;
        if (ok) { const gap = Math.abs(cD + cI + cB + cP - (Rw - Rt))/Math.max(1, Math.abs(Rt)); if (gap > 1e-9) throw new Error('EPPM parts do not add up for ' + g + ': ' + gap); } }
      if (g !== 'all' && PARTS.indexOf(g) < 0) { /* the below-30-days share of the group in both runs */
        let bw = 0, bt = 0; recs.forEach(r => { const t = T.get(r.id); if (!t || !grp[g](r, t)) return; if (r.bo < L30) bw++; if (t.bo < L30) bt++; });
        s['bOw_' + g] = m ? bw/m*100 : null; s['bOt_' + g] = m ? bt/m*100 : null; } });
  }
  return {s, paired, n};
}

/* One whole run of one seed: movement between the six tiers. seq: Map id -> array of tiers by year (undefined where absent). */
function runSummary(seq, T) {
  const s = {}, ids = [...seq.keys()], full = ids.filter(id => { const x = seq.get(id); for (let t = 0; t < T; t++) if (x[t] === undefined) return false; return true; });
  const start = ids.filter(id => seq.get(id)[0] === 0);
  [5, 10].forEach(h => { if (h >= T) return; const d = new Array(TIER_N).fill(0); let m = 0;
    start.forEach(id => { const v = seq.get(id)[h]; if (v === undefined) return; d[v]++; m++; });
    for (let k = 0; k < TIER_N; k++) s['trC' + h + '_' + k] = m ? d[k]/m*100 : null; s['trC' + h + '_n'] = m; });
  s.startCrisis = ids.length ? start.length/ids.length*100 : null;
  s.yrsCrisis = full.length ? full.reduce((a, id) => a + seq.get(id).filter(v => v === 0).length, 0)/full.length : null;
  s.everCrisis = full.length ? full.filter(id => seq.get(id).some(v => v === 0)).length/full.length*100 : null;
  let ex = 0, back = 0, st = 0, out = 0, wait = 0;
  ids.forEach(id => { const x = seq.get(id);
    for (let t = 1; t < T; t++) { if (x[t - 1] !== 0 || x[t] === undefined || x[t] === 0) continue; if (t + 2 >= T || x[t + 1] === undefined || x[t + 2] === undefined) continue;
      ex++; if (x[t + 1] === 0 || x[t + 2] === 0) back++; }
    if (x[0] === 0 && full.indexOf(id) >= 0) { st++; let t = 0; while (t < T && x[t] === 0) t++; if (t < T) { out++; wait += t; } } });
  s.reentry2 = ex ? back/ex*100 : null; s.exitN = ex; s.firstExitYrs = out ? wait/out : null; s.neverExit = st ? (st - out)/st*100 : null;
  return s;
}

module.exports = {adult, yearSummary, runSummary, giniPos, giniNeg, quant};
