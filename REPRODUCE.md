# Reproduce every published table and figure

Every number on the simulation page (`index.html`), the findings explorer (`findings.html`) and the replication page comes from one data file per release (`data/releases/v<version>.json`), which `dev/tools/release_data.py` writes from the run files in `dev/runs/`. This page lists, for each group of published tables and figures, the command that makes the run file, the file, and a fingerprint to compare with. The model is described in [MODEL_SPEC.md](MODEL_SPEC.md); the switches in [TESTBED_SPEC.md](TESTBED_SPEC.md).

## Set-up

- Node 22 (the v5.2 and v5.3 runs used v22.22.0; each run file records its own in `_meta.manifest.node`) and Python 3 (standard library only).
- `npm ci` installs the one dev dependency (jsdom, for the page tests) at the versions in `package-lock.json`. The simulation itself needs no install: open `index.html`.
- The three checks: `npm test` (`node harness.js validate`, `node harness.js unit`, `node domtest.js`; about 7 minutes).
- Run each 500-seed command from a clean checkout of the release commit. One process per environment; they can run side by side (the runs are independent and seeded, so splitting changes no figure). A v5.3 20-year release panel takes about 2 hours per environment on one core and a 40-year one about 3½ hours (v5.2's took 55 and 95 minutes: v5.3's panel has more rows, and households cost more to simulate); the backing sweep and the attribution study take about an hour each.

**Fingerprints.** A run file holds its results and, under `_meta`, how and when it was made (commit, date, seconds). A rerun gives the same results but a new `_meta`, so compare `python3 dev/tools/panel_hash.py FILE` (SHA-256 of everything except `_meta`, written canonically; first 16 hex digits below). The v5.2 files were made at commit `42cd8b9` (v5.2); the engine is unchanged in v5.2.1 and v5.2.2, so the same commands at a later release commit give the same fingerprints. Checked on Oct 6, 2026: `node harness.js testbed 500 release ref` at commit `f8427e1` (the v5.2.2 work, clean tree; 53 minutes) gave `1799e859c5e90b1e`, the published Reference fingerprint, with the same engine-block hash.

## The release data (v5.3)

| Published tables and figures | Command | File | Fingerprint |
|---|---|---|---|
| Main result, 20 years: headline cards (with children), main table (`rel-t20`), run by run (`rel-paired`), households and children (`rel-hh`), Hub-target table, the readings table (`rel-v53`), who gains, cost and how it is paid, year-by-year charts, prices | `node harness.js testbed 500 release ref --v53 --json=dev/runs/release-panel-ref.json` (and `adv`, `st`), commit `c5e96f9` | `dev/runs/release-panel-ref.json` / `-adv` / `-st` | `691b1c65af92edc9` / `83ceec24c2e1c25a` / `2d54d56182143300` |
| The same, merged | `python3 dev/tools/merge_panel.py` | `dev/runs/release-panel.json` (embedded in `index.html` as `#rel-data`) | `ac9f9245b8b86dce` |
| Main result, 40 years (`rel-t40` and every 40-year view) | `node harness.js testbed 500 release ref --v53 --years=40 --json=dev/runs/release-panel-40-ref.json` (and `adv`, `st`), commit `c5e96f9` | `dev/runs/release-panel-40-ref.json` / `-adv` / `-st` | `a20a6138deabd5a0` / `2268b7f481b2282b` / `a624ff71ea4f4d28` |
| The same, merged | `python3 dev/tools/merge_panel.py 40` | `dev/runs/release-panel-40.json` (`#rel-data-40`) | `2c7678bab1ac2cbb` |
| Backing-share chart and table (`bs`) | `node harness.js testbed 500 backing ref --v53 --json=dev/runs/backing-share-ref.json` (and `adv`, `st`), commit `289e723`, then `python3 dev/tools/backing_chart.py` | `dev/runs/backing-share-ref.json` / `-adv` / `-st`; merged `backing-share.json` | `90c459e3122289a9` / `7a9d006d788c736a` / `edbb09283f9cbbf0`; `ccf454fdfe6464b5` |
| What each part does (`rel-attrib`, the simulation page’s "What each part does") | `node dev/tools/attrib_check.js ref 500 20` (and `adv`, `st`), commit `289e723` | `dev/runs/attrib-check-ref.json` / `-adv` / `-st` | `9fad7cb56355ed31` / `49cec38a0c08923e` / `feb0e17254048373` |
| The no-programme run against US data (`rel-us`, `rel-us3`, `rel-us2`) | `node dev/tools/us_check.js ref 500 20 --v53` and `adv`, commit `289e723` | `dev/runs/us-check-ref.json` / `-adv` | `0e65d71aef08c477` / `ed00bc8df34285e6` |
| Spread across the runs, savings deciles, one run’s 500 adults (the simulation page’s explore sections) | `node dev/tools/explore_export.js ENV YRS 500 1 --v53` for ENV `ref`, `adv`, `st` and YRS `20`, `40`, commit `c1f8b8e` (after the merges) | `dev/runs/explore-ENV-YRS.json` | EXPLORE_FP |
| The release file, the list of releases and the pages’ static figures | `python3 dev/tools/release_data.py` (`--check` confirms they are current; domtest Phase 14 runs it) | `data/releases/v5.3.json`, `data/releases/v5.3/*` (including `attrib.json`), `data/manifest.json` | — (generated; checked by `--check`) |
| The constants the release file quotes (wealth line, poverty line, BLEI days) | `node harness.js constants` | `dev/runs/constants.json` | — (Phase 14 checks it equals the harness’s CFG) |
| Earlier releases in the version switcher (v5.0, v5.0.1, v5.1, v5.2) | v5.2’s file is the one published with v5.2.2 (its status now “earlier”); the older ones: `python3 dev/tools/release_data.py --backfill v5.1` (and `v5.0.1`, `v5.0`), from the files committed at each tag | `data/releases/v5.2.json`, `v5.1.json` etc. | v5.2’s commands and fingerprints are in this file at tag `v5.2.2` |

### Headline values to compare (main row against no programme, 500 paired seeds)

Below the cost of living (share of adult-years); children below the cost of living (share of child-years); too little wealth at the last year (share of adults); below 30 days of basic living (BLEI, share of adult-years); the change in too little wealth with its 95% interval (percentage points, paired by seed); programme inflation a year; cost per adult a year (today’s dollars).

| Environment, years | Below the cost of living | Children below the cost of living | Too little wealth | Below 30 days (BLEI) | Change in too little wealth | Inflation | Cost |
|---|---|---|---|---|---|---|---|
| Reference, 20 | 16.7% vs 45.1% | 29.4% vs 72.6% | 36.0% vs 30.5% | 10.4% vs 25.4% | +5.51 (+5.29 to +5.73) | 47.9% | $31,366 |
| Adverse, 20 | 33.7% vs 72.1% | 51.2% vs 91.3% | 89.4% vs 48.8% | 18.6% vs 32.1% | +40.57 (+40.39 to +40.76) | 61.5% | $29,567 |
| Stress Test, 20 | 56.6% vs 72.1% | 76.5% vs 91.3% | 86.3% vs 48.8% | 37.6% vs 32.1% | +37.50 (+37.29 to +37.71) | 28.5% | $12,177 |
| Reference, 40 | 12.1% vs 36.5% | 22.5% vs 62.2% | 18.4% vs 27.3% | 8.8% vs 26.5% | −8.91 (−9.09 to −8.72) | 44.7% | $32,854 |
| Adverse, 40 | 54.5% vs 83.8% | 69.5% vs 95.3% | 98.8% vs 70.2% | 30.0% vs 45.2% | +28.62 (+28.45 to +28.78) | 89.1% | $28,555 |
| Stress Test, 40 | 73.4% vs 83.8% | 86.4% vs 95.3% | 98.5% vs 70.2% | 59.8% vs 45.2% | +28.35 (+28.19 to +28.52) | 43.0% | $12,336 |

## Diagnostics and step studies (not on the pages; behind decisions and reports)

| What | Command | File |
|---|---|---|
| The household reading so far (v5.3, B3; `dev/reports/v5-14-households.md`) | `node dev/tools/hh_check.js ENV 500` (ENV `ref`, `adv`, `st`; commit `36ac97c`) | `dev/runs/hh-check-ENV.json` (fingerprints ref `6c7ca3cde170bcd4`, adv `eb22ae5b4e3d06f2`, st `c9342fcf563cc9ab`) |
| What BU can buy: today's list against the Hub's (v5.3, B3f; `dev/reports/v5-15-bu-scope.md`) | `node dev/tools/scope_check.js ENV 500` (ENV `ref`, `adv`, `st`; commit `aba2841`) | `dev/runs/scope-check-ENV.json` (fingerprints ref `e6db0d498084815d`, adv `09faa9619088e66d`, st `9851d0072ec50b9e`) |
| Children's lives and estates, households with ageing (v5.3, B4 and B5; `dev/reports/v5-16-childrens-lives.md`) | `node dev/tools/life_check.js ENV 500` (ENV `ref`, `adv`, `st`; commit `8b22392`) | `dev/runs/life-check-ENV.json` (fingerprints ref `765306ad0558317d`, adv `d5ee9834fedd29bf`, st `1c80171ca0df0f8a`) |
| Household income shocks and the measured EDC (v5.3, B6; `dev/reports/v5-17-shocks-and-edc.md`) | `node dev/tools/shock_edc_check.js ENV 500` (ENV `ref`, `adv`, `st`; commit `8b22392`) | `dev/runs/shock-edc-check-ENV.json` (fingerprints ref `6c88d60613a76f61`, adv `36bd4ab53ae142c8`, st `3b273a0609c44ee4`) |
| Four calibration readings, and the no-programme run against the SCF at Year 7 (v5.3, B7; `dev/reports/v5-18-calibration.md`) | `node dev/tools/calib_check.js ENV 500` (ENV `ref`, `adv`, `st`; commit `8759752`) | `dev/runs/calib-check-ENV.json` (fingerprints ref `438a096c6297101b`, adv `a08b1a15fa542817`, st `4be3ce12f4754c7d`) |
| The accounting check and its two corrections (v5.3, B2; `dev/reports/v5-13-accounting-check.md`) | `node dev/tools/acct_check.js ENV 500` (ENV `ref`, `adv`, `st`; commit `a316514`) | `dev/runs/acct-check-ENV.json` (fingerprints ref `f26307bdcdff056d`, adv `d8978bbb2b3ad7f5`, st `ff87668797cecb99`) |
| The Phi step (v5.2.2, A7; `dev/reports/v5-11-phi-step.md`) | `node dev/tools/phi_check.js ENV 500` (ENV `ref`, `adv`, `st`) | `dev/runs/phi-check-ENV.json` (fingerprints ref `353830f0bf6e0b50`, adv `eadebbef40935a3e`, st `0415ccac89ed1c6d`) |
| Savings that keep up with prices (v5.2 step 3) | `node dev/tools/save_check.js ENV 200` | `dev/runs/save-check-ENV.json` |
| The middle backing reading (v5.2 step 6) | `node dev/tools/backing_check.js ENV 200` | `dev/runs/backing-check-ENV.json` |
| Robustness readings (v5.2 step 7) | `node dev/tools/robust_check.js ENV 200` | `dev/runs/robust-check-ENV.json` |
| The automation-risk fit (v4.20) | `node harness.js automation` | printed |
| Each v5.0 mechanism's 500-seed restudy (plan steps 1-18) | as recorded beside each result in `dev/PROGRESS.md` | `dev/runs/step*-500-*.txt` |

The commit each study ran at is in its file's `_meta.manifest` and in `dev/DECISIONS.md`.

## Checking a reproduction

1. Run the command at the release commit with a clean tree (the manifest records `dirty: false`).
2. `python3 dev/tools/panel_hash.py` on your file and on the committed one: the 16-digit fingerprints match.
3. For the whole chain: `python3 dev/tools/release_data.py --check` and `node domtest.js` (Phase 14 compares every number on the three pages with the release data).
