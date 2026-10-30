#!/usr/bin/env node
/* S34 (Oct 30, 2026; preregistration research-update prereg/s34-baseline-realism.md, Q5): the engine's yearly SNAP, EITC and refundable Child Tax Credit
 * for six representative households, to set beside PolicyEngine-US's (dev/tools/pe_households.py). Each household's rent is the engine's housing line for
 * its type (MIT's HUD rent with utilities, CFG.HH_RATIO) and its childcare the engine's (CFG.HH_CHILDCARE, children under 13), in year-0 (2025) dollars;
 * the safety net as in the v5.6 release (SNAP's work rule on, the slope reading on); take-up set to "takes up" (the check is of the benefit rules, not of
 * take-up); adults of working age (30 and 32), no Social Security or other income. The work rule needs a year's work history; these adults work all year,
 * so it does not bite. Writes JSON to stdout (or --out=FILE). */
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js')), C = H.CFG;
const OUTA = process.argv.filter(a => /^--out=/.test(a))[0];
const HH = [
  {id: 1, label: 'Single adult, earning $15,000', nA: 1, kids: [], earn: 15000},
  {id: 2, label: 'Single adult, earning $30,000', nA: 1, kids: [], earn: 30000},
  {id: 3, label: 'Single parent, one child aged 3, earning $22,000', nA: 1, kids: [3], earn: 22000},
  {id: 4, label: 'Single parent, children aged 4 and 9, earning $35,000', nA: 1, kids: [4, 9], earn: 35000},
  {id: 5, label: 'Couple, children aged 7 and 12, one earner at $40,000', nA: 2, kids: [7, 12], earn: 40000},
  {id: 6, label: 'Couple without children, earning $25,000 together', nA: 2, kids: [], earn: 25000}];
const SN = {abawd: true, slope: true};
const out = {_meta: {what: 'S34 Q5: the engine\'s safety-net amounts for six households', sn: Object.assign({}, H.SNET_DEFAULTS, SN), manifest: H.runManifest(),
  command: 'node dev/tools/sn_households.js', dollars: 'year-0 (2025) dollars; SNAP at FY2026 allotments as the engine holds them'}, households: []};
HH.forEach(function (x) {
  const nK = x.kids.length, R = C.HH_RATIO[x.nA + 'a' + Math.min(3, nK) + 'k'], house = C.LIVING_WAGE_ANNUAL*C.BASKET.housing*R.housing;
  let care = 0, nc = 0; x.kids.slice().sort((a, b) => a - b).forEach(function (age) { if (age < C.HH_CARE_AGE) { care += C.HH_CHILDCARE[Math.min(nc, C.HH_CHILDCARE.length - 1)]; nc++; } });
  const h = {nA: x.nA, nK: nK, k17: x.kids.filter(a => a < C.SN_CTC.age).length, other: 0, house: house, care: care, old: false, okAge: true, takeS: true, takeT: true};
  const b = H.snBenAt(SN, h, x.earn), it = H.incomeTest(x.nA, nK, x.earn);
  out.households.push(Object.assign({}, x, {rent: house, childcare: care, povertyRatio: it.ratio, engine: {snap: b[0], eitc: b[1], ctc: b[2]}}));
});
const js = JSON.stringify(out, null, 1);
if (OUTA) fs.writeFileSync(OUTA.slice(6), js); else console.log(js);
