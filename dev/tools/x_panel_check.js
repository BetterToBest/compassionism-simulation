#!/usr/bin/env node
/* S48 (Nov 8, 2026; research-update prereg/run-manifest.md, job X): explore_export.js self-check (1) for the batch's X folder, without rerunning it.
 * Each X shard (compassionism-sim-results runner/jobs/series.js) stores, per row (base, c22, release) and measure (f0, pov, bO, medW), the yearly means
 * rounded exactly as explore_export.js rounds them for its check. This compares them with the merged frozen panel's paths, as --panel=FILE would.
 *   node dev/tools/x_panel_check.js X_FOLDER PANEL_20.json PANEL_40.json      (exits 1 on any difference) */
const fs = require('fs'), [X, P20, P40] = process.argv.slice(2); let bad = [], n = 0;
for (let i = 0; i < 6; i++) {
  const x = JSON.parse(fs.readFileSync(X + '/shard-000' + i + '.json')), env = x._meta.env, yrs = x._meta.years;
  const PJ = JSON.parse(fs.readFileSync(yrs === 40 ? P40 : P20)), panel = PJ.envs[env];
  if (x._meta.seriesSeeds !== PJ._meta.seeds) bad.push('seeds differ ' + x._meta.seriesSeeds + ' vs ' + PJ._meta.seeds);
  for (const j of Object.keys(x.bands)) { const pub = j === 'base' ? panel.base.path : panel.rows[j].path;
    for (const m of Object.keys(x.bands[j])) x.bands[j][m].mean.forEach((v, t) => { n++; if (v !== pub[m][t]) bad.push(env + ' ' + yrs + ' ' + j + ' ' + m + ' year ' + (t + 1) + ': ' + v + ' vs ' + pub[m][t]); }); }
}
console.log(bad.length ? 'FAIL ' + bad.length + '\n' + bad.slice(0, 20).join('\n') : 'PASS: ' + n + ' yearly means (6 environment-horizons x 3 rows x 4 measures) equal the merged frozen panel');
process.exit(bad.length ? 1 : 0);
