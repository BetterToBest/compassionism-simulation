#!/usr/bin/env node
/* S92 (Nov 19, 2026): check 3 of research-update prereg/2026-11-s90-private-price-at-sale.md. The engine's accounting checks (ACCT, MODEL_SPEC section 11)
 * on the at-sale rows (the full-coverage and opt-in main rows with sp.vAt 'sale'), seeds 1-5, 500 adults, 20 years, in Reference, Adverse and Stress,
 * by the unit suite's method (privUnitSuite, "S90 at-sale: the books balance"): the check on, the row run, its failure counts read. The check passes if
 * no identity fails in any row and environment and the premium identity was checked.
 * S93 (Nov 21, 2026; prereg Amendment 2 section C2): --a=X runs the programme rows at backed share X (0 and 0.5 there); absent, full backing.
 * Usage: node dev/tools/s90_acct.js [--seeds=5] [--years=20] [--a=X] [--out=FILE] */
'use strict';
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const arg = (k, d) => { const a = process.argv.find(x => x.startsWith('--' + k + '=')); return a ? a.slice(k.length + 3) : d; };
const N = +arg('seeds', 5), years = +arg('years', 20), out = arg('out', ''), BA = arg('a', '');
const ENVS = [['ref', 'FULL_INTEGRATION'], ['adv', 'ADVERSE_REFERENCE'], ['st', 'STRESS_TEST']];
const S = H.startRelease(), res = {what: 'S92 check 3: accounting identities on the at-sale rows', seeds: [1, N], years, adults: 500, backedShare: BA !== '' ? +BA : 1, cells: []};
let ok = true;
try {
  ENVS.forEach(([e, k]) => { const P = Object.assign({}, H[k], {years, nAgents: 500});
    ['c22', 'rel'].forEach(d => { const c = H.r2FreezePair(P, d)[1]; c.sp = Object.assign({}, c.sp, {vAt: 'sale'}); if (BA !== '') c.o = Object.assign({}, c.o, {a: +BA});
      H.setAcct(H.acctNew()); try { H.tbStudy([c], N, P, H.r2MainStudy()); } finally { var A = H.getAcct(); H.setAcct(null); }
      const fails = Object.keys(A.nFail || {}).filter(x => A.nFail[x] > 0), checks = Object.assign({}, A.n);
      const pass = fails.length === 0 && (checks.premium || 0) > 0; if (!pass) ok = false;
      res.cells.push({env: e, row: d + '.sale', pass, checks, fails: fails.map(x => x + ' ' + A.nFail[x])});
      console.log(e.padEnd(4) + d.padEnd(4) + '.sale  ' + (pass ? 'pass' : 'FAIL') + '  checks: ' + Object.keys(checks).map(x => x + ' ' + checks[x]).join(', ') + (fails.length ? '  failing: ' + fails.join(', ') : '')); }); });
} finally { S.restore(); }
res.pass = ok; console.log('check 3: ' + (ok ? 'passes' : 'FAILS'));
if (out) fs.writeFileSync(out, JSON.stringify(res, null, 1));
process.exit(ok ? 0 : 1);
