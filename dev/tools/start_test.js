#!/usr/bin/env node
/* S84 (Nov 17, 2026; research-update PLAN S84): tests of the one start every study runner uses (harness.js startRelease), run in CI.
 *   1. startRelease applies the release's two global settings (the next-round accounting profile and the testbed profile) and restore() puts both back.
 *   2. The settings it records name every switch and default (version, accounting, testbed profile, labour response, the engine's constants, CFG's hash).
 *   3. The baseline check passes with the start (the frozen no-programme arm equals the release's published rows per seed, seeds 1-2, Reference, Adverse
 *      and Stress) and FAILS without it: a run that started wrongly stops. This is the check S74's first runs would have failed.
 *   4. withSettings adds `_settings` and changes nothing else in an output.
 *   5. No tool in dev/tools applies the two settings by hand: each uses startRelease.
 * Usage: node dev/tools/start_test.js     (exit 1 on any failure) */
'use strict';
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const results = []; const test = (name, fn) => { let r; try { r = fn(); } catch (e) { r = {pass: false, detail: 'threw: ' + e.message}; } results.push(Object.assign({name}, r)); };
const prof = () => H.releaseSettings();

test('startRelease applies the accounting and testbed profiles, and restore() puts both back', () => {
  const before = prof(), S = H.startRelease(), during = prof(); S.restore(); const after = prof();
  const on = during.accounting.THETA_GATE === 'density' && during.accounting.PTH_MODE === 'housing' && during.accounting.DISC_BASE === 'pretax' && during.accounting.SURPLUS_CONSUMPTION_SHARE === 0.9 && during.testbedProfile.N7_BLEI === true;
  const was = before.testbedProfile.N7_BLEI === false && before.accounting.THETA_GATE !== 'density';
  const back = JSON.stringify(before.accounting) === JSON.stringify(after.accounting) && JSON.stringify(before.testbedProfile) === JSON.stringify(after.testbedProfile);
  return {pass: on && was && back, detail: 'on: ' + on + '; the engine\'s own defaults before: ' + was + '; restored: ' + back};
});

test('the recorded settings name the version, every profile, the labour response, the engine\'s constants and CFG\'s hash', () => {
  const S = H.startRelease(), x = S.settings; S.restore();
  const need = ['version', 'engineSwitches', 'accounting', 'testbedProfile', 'tbRun', 'laborDefaults', 'fw', 'pathwayOff', 'pmDefaults', 'spend', 'cfgScalars', 'cfgSha256'], miss = need.filter(k => x[k] === undefined || x[k] === null);
  const manifest = JSON.parse(fs.readFileSync(path.join(__dirname, '..', '..', 'data', 'manifest.json'), 'utf8')), idx = fs.readFileSync(path.join(__dirname, '..', '..', 'index.html'), 'utf8');
  const V = /var META = \{\s*VERSION:'([^']+)'/.exec(idx)[1];
  const ok = !miss.length && x.version === V && /^[0-9a-f]{64}$/.test(x.cfgSha256) && Object.keys(x.engineSwitches).length >= 20 && x.spend.SPEND_FROZEN === manifest.releases[0].docs.spendingShare;
  return {pass: ok, detail: miss.length ? 'missing ' + miss.join(', ') : 'version ' + x.version + ', ' + Object.keys(x.engineSwitches).length + ' engine constants, ' + Object.keys(x.cfgScalars).length + ' CFG scalars, SPEND_FROZEN ' + x.spend.SPEND_FROZEN};
});

test('the baseline check passes with the start, in Reference, Adverse and Stress', () => {
  const S = H.startRelease(); try { const r = ['ref', 'adv', 'st'].map(env => S.checkBaseline({env, seeds: 2})); return {pass: r.every(x => x.checked), detail: r.map(x => x.env + ' ' + x.values + ' values').join(', ') + ' equal the release rows (engine ' + r[0].engine + ')'}; } finally { S.restore(); }
});

test('the baseline check stops a run that started without the release\'s settings', () => {
  let msg = null; try { H.checkBaselineWith({env: 'ref', seeds: 2}); } catch (e) { msg = e.message; }
  return {pass: !!msg && /baseline check FAILED/.test(msg), detail: msg ? msg.split('\n').slice(0, 2).join(' | ') : 'no error: the check let a run without the settings through'};
});

test('the baseline check stops a run whose settings differ from the release in one switch (the accounting share moved from 0.9 to 0.89)', () => {
  const S = H.startRelease(); let msg = null; const sv = H.applyRule({SURPLUS_CONSUMPTION_SHARE: 0.89});
  try { S.checkBaseline({env: 'ref', seeds: 2}); } catch (e) { msg = e.message; } finally { H.applyRule(sv); S.restore(); }
  return {pass: !!msg && /baseline check FAILED/.test(msg), detail: msg ? msg.split('\n')[0] : 'no error: a changed constant went through'};
});

test('withSettings adds _settings and changes nothing else; arrays and non-objects pass through', () => {
  const S = H.startRelease(), o = {a: 1, b: [1, 2]}, w = S.withSettings(o); S.restore();
  return {pass: w._settings && w.a === 1 && w.b === o.b && o._settings === undefined && Array.isArray(S.withSettings([1])) && S.withSettings(null) === null, detail: 'keys ' + Object.keys(w).join(',')};
});

test('no tool in dev/tools applies the two settings by hand (each uses startRelease)', () => {
  const dir = __dirname, bad = fs.readdirSync(dir).filter(f => /\.js$/.test(f) && f !== 'start_test.js').filter(f => /\.applyNR6\(\)/.test(fs.readFileSync(path.join(dir, f), 'utf8')));
  return {pass: !bad.length, detail: bad.length ? 'still call applyNR6 directly: ' + bad.join(', ') : 'none call applyNR6 directly'};
});

let fail = 0; results.forEach(r => { if (!r.pass) fail++; console.log((r.pass ? 'PASS ' : 'FAIL ') + r.name + '\n     ' + r.detail); });
console.log(fail ? '\n' + fail + ' of ' + results.length + ' start tests FAILED' : '\nall ' + results.length + ' start tests passed');
process.exit(fail ? 1 : 0);
