// S51 explanatory diagnostic (not preregistered; session machine; seeds 1-N, Reference by default). Run in the engine root: node dev/tools/s51_diag.js 10 [ENV]. Two checks:
// (1) does wealth poverty's rise come from savings that do not keep up with prices? (row option sv on both rows of the pair)
// (2) is the dip near full backing the BU surge protocol's 5% threshold? (p.colaThresh = -1: BU follows prices every year)
const path = require('path'), H = require(path.join(process.cwd(), 'harness.js'));
const N = +(process.argv[2] || 10), ENV = process.argv[3] || 'FULL_INTEGRATION';
const P = Object.assign({}, H[ENV], {years: 20, nAgents: 500});
const so = Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: H.SPEND_SOURCED}, H.REL_V52_STUDY);
const pair = () => H.relMainCfgs(H.tbPresets(P)).map(c => Object.assign(c, {sc: H.SPEND_SOURCED, sn: {abawd: true, slope: true}}));
const R = [], add = (n, c, f) => { c.o = Object.assign({}, c.o || {}); f(c); R.push([n, c]); };
console.error('cola on release row:', JSON.stringify({cola: pair()[1].p && pair()[1].p.cola, th: pair()[1].p && pair()[1].p.colaThresh}));
[100, 90].forEach(w => {
  add('none w' + w, pair()[0], c => { c.o.wIdx = w/100; });
  add('a0 w' + w, pair()[1], c => { c.o.wIdx = w/100; });
  add('none w' + w + ' sv', pair()[0], c => { c.o.wIdx = w/100; c.sv = true; });
  add('a0 w' + w + ' sv', pair()[1], c => { c.o.wIdx = w/100; c.sv = true; });
});
[90, 95, 100].forEach(a => {
  add('a' + a + ' w100', pair()[1], c => { c.o.wIdx = 1; c.o.a = a/100; });
  add('a' + a + ' w100 colaAll', pair()[1], c => { c.o.wIdx = 1; c.o.a = a/100; c.p = Object.assign({}, c.p, {colaThresh: -1}); });
});
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G);
try {
  const S = H.tbStudy(R.map(r => r[1]), N, P, so, 1);
  const m = (i, k) => { const a = S[i]._s[k]; return a ? Array.from(a).reduce((s, x) => s + x, 0)/a.length : NaN; };
  R.forEach((r, i) => console.log(r[0].padEnd(20), ['fgt0PY', 'pov', 'jnP19', 'pLev20', 'medWealthReal'].map(k => k + '=' + m(i, k).toPrecision(4)).join(' ')));
} finally { H.resetNR6(svN); H.tbSetG(svG); }
