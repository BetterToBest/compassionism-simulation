/* s118 packet: reference outputs of the real engine for an independent re-implementation to match.
 * Runs the six presets (all new mechanisms off, as in `node harness.js validate`) for seeds 1-30 and 42, 500 adults, and writes the result of runScenario for each.
 * Usage: node dev/packets/make_s118_reference.js > s118-reference.json */
const H = require('../../harness.js');
const presets = {full_integration: H.FULL_INTEGRATION, cco_only: H.CCO_ONLY, baseline_3pct: H.BASELINE, adverse: H.ADVERSE_REFERENCE, stress: H.STRESS_TEST};
H.CFG.WEALTH_FLOOR = -10000;
const out = {about: 'Real engine (index.html read by harness.js), runScenario(preset, seed), 500 adults. Keys as in node harness.js validate. Seeds 1-30 and 42.', presets: {}};
for (const [name, p] of Object.entries(presets)) {
  const q = Object.assign({}, p, {nAgents: 500});
  out.presets[name] = {params: q, seeds: {}};
  for (const s of (process.env.S118_SEEDS ? Array.from({length: +process.env.S118_SEEDS}, (_, i) => i + 1) : Array.from({length: 30}, (_, i) => i + 1).concat([42]))) out.presets[name].seeds[s] = H.runScenario(q, s);
}
console.log(JSON.stringify(out));
