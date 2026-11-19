#!/usr/bin/env node
/* S90 (Nov 18, 2026): trace of the BU's relief in the main row, year by year. No engine change: index.html is not edited.
 * The tool builds its own copy of the script harness.js runs (as s66_trace.js does), adds read-only probes, and prints, per year, the mean per
 * programme adult of: the BU issued (12 x BU), the essentials bill the BU can buy, the surplus split's price cut (spC), the BU spent (fwB),
 * the BU expired, the relief tbAccount books (buR, = a._slBU), the split's pool, uniform PTF cut (spDelta) and carry, the private ESPs' price
 * cut, the cash paid on essentials, and mean wage and income (all adults).
 * --check   the copy with probes gives the harness's own outputs on every key
 * --sale    the main row with the private ESPs' price at the sale (sp.vAt 'sale'; S90's fix) and its repayment line
 * --patch=  experiments in the tool's copy only (never the engine): nocut (no PTF price cut), fixcut (PTF cut held at 30%),
 *           nov (no private price), none (neither). S90's finding: the cycle goes with nov and none, and stays with nocut.
 * Usage: node dev/tools/s90_trace.js [--env=ref|adv|st] [--seed=1] [--n=500] [--years=20] [--check] [--sale] [--json=FILE] [--patch=NAME] */
const fs = require('fs'), path = require('path'), vm = require('vm');
const ROOT = path.join(__dirname, '..', '..'), H = require(path.join(ROOT, 'harness.js'));
const arg = (k, d) => { const a = process.argv.find(x => x.startsWith('--' + k + '=')); return a ? a.slice(k.length + 3) : d; };
const SALE = process.argv.includes('--sale');
const ENVN = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'};
const PATCH = [
  ['probe: BU spent', 'cf=cfPreCCO+hcX-fwB/mainLoopCostUSD;hcDone=true;', 'cf=cfPreCCO+hcX-fwB/mainLoopCostUSD;hcDone=true;if(S90.on)S90.bu(yr,fwBudget,mainLoopCostUSD*essF,spC,fwB,fwLeft,mainLoopCostUSD);'],
  ['probe: split', 'var spUsed=spDelta*spSum;SPS.carry=spPP-spUsed;', 'var spUsed=spDelta*spSum;SPS.carry=spPP-spUsed;if(S90.on)S90.sp(yr,spPool,spPP,spSum,spDelta,SPS.carry,spPh);'],
  ['probe: private cut', 'if(vC>0){spC+=vC;', 'if(vC>0){if(S90.on)S90.v(yr,vC);spC+=vC;'],
  ['probe: at-sale residual', 'var spRestOn=spRest>0', 'if(S90.on&&spVS)S90.res(yr,spVP,spVW,SPS.vK,SPS.carryV);var spRestOn=spRest>0'],
  ['probe: relief booked', 'if (SLS) a._slBU = buR;', 'if (SLS) a._slBU = buR; if (S90.on) S90.tb(yr, buR, tbG, spCut);'],
  ['probe: income', 'var disp = E + conv', 'if (S90.on) S90.tb2(yr, E, inc); var disp = E + conv']]
const PROBE = `
var S90 = {on:false, Y:{}, y:function(yr){ return this.Y[yr] || (this.Y[yr] = {n:0, iss:0, ess:0, spC:0, fwB:0, left:0, mlc:0, nT:0, buR:0, tbG:0, spCut:0}); },
  bu:function(yr, b, e, c, f, l, m){ var q = this.y(yr); q.n++; q.iss += b; q.ess += e; q.spC += c; q.fwB += f; q.left += l; q.mlc += m; },
  sp:function(yr, pool, pp, sum, d, carry, ph){ var q = this.y(yr); q.pool = pool; q.pp = pp; q.sum = sum; q.d = d; q.carry = carry; q.ph = ph; },
  res:function(yr, r, w, k, c){ var q = this.y(yr); q.res = r; q.wk = w; q.vK = k; q.cv = c; },
  v:function(yr, c){ var q = this.y(yr); q.vC = (q.vC || 0) + c; },
  tb2:function(yr, e, i){ var q = this.y(yr); q.nA = (q.nA || 0) + 1; q.E = (q.E || 0) + e; q.inc = (q.inc || 0) + i; },
  tb:function(yr, r, g, c){ var q = this.y(yr); if (r > 0 || c > 0){ q.nT++; q.buR += r; q.tbG += g; q.spCut += c; } }};
module.exports._s90 = S90;
`;
function engineCopy(extra) {
  let src = H.builtSource();
  PATCH.concat(extra || []).forEach(([w, a, b]) => { const n = src.split(a).length - 1; if (n !== 1) throw new Error('patch "' + w + '" matches ' + n + ' times'); src = src.replace(a, () => b); });
  const mod = {exports: {}};
  vm.runInThisContext('(function (require, module, exports, __dirname, __filename, builtSource, csEngineSource) {' + src + '\n' + PROBE + '\n})', {filename: 's90-engine-copy.js'})
    (require, mod, mod.exports, ROOT, path.join(ROOT, 'harness.js'), H.builtSource, H.csEngineSource);
  return mod.exports;
}
const SPV = 'a._spV=(spVSum>0&&a._spVw>0)?Math.min(spVP*a._spVw/spVSum,a._spVE):0;';
const SPD = 'spDelta=spSum>0?Math.min(1,spPP/spSum):0;';
const ALT = {  /* experiments in the tool's copy only (never the engine), to prove which term carries the cycle */
  nocut: [['no price cut', SPD, 'spDelta=0;']],                                   /* the split's price pool not paid as a cut (it carries) */
  fixcut: [['fixed cut', SPD, 'spDelta=yr>0?0.30:0;']],
  nov: [['no private cut', SPV, 'a._spV=0;']],                                   /* the private ESPs' lower BU price (plan step 14) not paid */
  none: [['no price cut', SPD, 'spDelta=0;'], ['no private cut', SPV, 'a._spV=0;']]};                        /* the uniform cut held at 30% of essentials from year 1 */
function run(E, env, seed, n, years) {
  const P = Object.assign({}, E[ENVN[env]], {years, nAgents: n}), RS = E.startRelease ? E.startRelease() : null;
  try { const c = E.r2FreezePair(P, 'c22'); if (SALE) c[1].sp = Object.assign({}, c[1].sp, {vAt: 'sale'}); E._s90.on = true; E._s90.Y = {}; const R = E.tbStudy([c[1]], seed, P, E.r2MainStudy()); E._s90.on = false; return {R: R[0], Y: E._s90.Y}; }
  finally { if (RS && RS.restore) RS.restore(); }
}
if (require.main === module) {
  const env = arg('env', 'ref'), seed = +arg('seed', 1), n = +arg('n', 500), years = +arg('years', 20);
  const E = engineCopy(ALT[arg('patch', '')] || []), o = run(E, env, seed, n, years);
  if (process.argv.includes('--check')) {
    const P = Object.assign({}, H[ENVN[env]], {years, nAgents: n}), RS = H.startRelease(), c = H.r2FreezePair(P, 'c22'); if (SALE) c[1].sp = Object.assign({}, c[1].sp, {vAt: 'sale'}); const R = H.tbStudy([c[1]], seed, P, H.r2MainStudy())[0]; RS.restore();
    const ks = Object.keys(R).filter(k => k[0] !== '_' && JSON.stringify(R[k]) !== JSON.stringify(o.R[k]));
    console.log('check: the copy with probes gives the harness outputs: ' + (ks.length ? 'FAIL, ' + ks.length + ' keys differ: ' + ks.slice(0, 8) : 'identical (' + Object.keys(R).length + ' keys)'));
  }
  const f = x => Math.round(x).toLocaleString('en-US');
  console.log('yr  adults  basket   issued   ess.bill  cut(spC)  BU spent  expired  booked(buR)  pool       cut share  carry      phase  priv.cut  cash.ess  wage(all)  income(all)');
  Object.keys(o.Y).map(Number).sort((a, b) => a - b).forEach(y => { const q = o.Y[y], m = v => q.n ? v/q.n : 0;
    console.log([String(y).padEnd(3), String(q.n).padStart(6), f(m(q.mlc)).padStart(8), f(m(q.iss)).padStart(8), f(m(q.ess)).padStart(9), f(m(q.spC)).padStart(9), f(m(q.fwB)).padStart(9), f(m(q.left)).padStart(8),
      f(q.nT ? q.buR/q.nT : 0).padStart(11), f(q.pool || 0).padStart(10), (q.d || 0).toFixed(4).padStart(9), f(q.carry || 0).padStart(10), String(q.ph || '').padStart(5), f(m(q.vC || 0)).padStart(9), f(m(q.ess - q.spC - q.fwB)).padStart(9), f(q.nA ? q.E/q.nA : 0).padStart(10), f(q.nA ? q.inc/q.nA : 0).padStart(11)].join(' ')); });
  if (SALE) console.log('at-sale: yr, vK (dollars a private-ESP BU buys beyond face), workers\' share paid, premium left after repaying the advance (shared by last year\'s BU), carry after sharing: ' + Object.keys(o.Y).map(Number).sort((a, b) => a - b).filter(y => o.Y[y].vK !== undefined).map(y => y + ':' + o.Y[y].vK.toFixed(4) + '/' + Math.round(o.Y[y].wk) + '/' + Math.round(o.Y[y].res) + '/' + Math.round(o.Y[y].cv)).join(' '));
  if (arg('json')) fs.writeFileSync(arg('json'), JSON.stringify({env, seed, n, years, Y: o.Y}, null, 1));
}
module.exports = {engineCopy, run};
