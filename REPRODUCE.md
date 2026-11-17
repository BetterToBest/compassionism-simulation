# Reproduce every published table and figure

This page gives the commands and fingerprints that regenerate every published figure: first for **v5.9**, the current release (rebuilt Nov 17, 2026), then for v5.3, whose data still drive the v5.6 panels of the pages. The model is described in [MODEL_SPEC.md](MODEL_SPEC.md) and [ODD.md](ODD.md); the switches in [TESTBED_SPEC.md](TESTBED_SPEC.md), section 0 for v5.9's main row.

## v5.9

**Where the results are.** v5.9 ran at engine commit `104691f` (frozen Nov 14, 2026, before it ran; registered on OSF, osf.io/msdzk; the frozen model has no central bank: it was first published as v5.8, and the central-bank study came with v5.9 under its own preregistration), on GitHub Actions, through the runner kept in the results repository (BetterToBest/compassionism-sim-results, `runner/jobs/r2.js`). Each results folder there holds the shard files, `run.txt` (the exact command, the engine commit, the runner commit, Node's version, the machine and the date) and `SHA256SUMS` (the SHA-256 of every file in the folder). The page data in this repository are copied from those folders by the scripts below; nothing is typed by hand.

**Set-up.** Clone both repositories side by side; check out the engine at `104691f` in a clean worktree (`git worktree add ../engine-104691f 104691f`); Node 22 (v5.9's runs used v22.22.0); Python 3 with numpy for the tables. A shard of 250-500 seeds takes one to several hours on four cores; seeds are paired and independent, so any split gives the same figures.

**Fingerprints.** For a results folder, the fingerprint is the first 16 hex digits of the SHA-256 of its `SHA256SUMS` file (`sha256sum FOLDER/SHA256SUMS`), so one value covers every file in it. To check a rerun, compare your shard files' SHA-256 with the folder's `SHA256SUMS`; the `.log` and `.timing.json` files differ run to run and are not compared. For a data file in this repository, the fingerprint is the first 16 hex digits of the file's own SHA-256 at release v5.9.12.

### The main row and its readings (500 paired seeds)

Command per shard, run from the engine worktree, `RESULTS` being the results repository: `node RESULTS/runner/jobs/r2.js --part=PART --env=ENV --years=YRS --procs=4 --gzip --seeds=A-B --out=shard-NNNN.json`, for `PART` M, S, F or B, `ENV` ref, adv or str, `YRS` 20 or 40, and seeds 1-500 cut into contiguous ranges (`run.txt` names the ranges). `node RESULTS/runner/jobs/r2.js --check` prints every point of the design against the preregistration; `--selftest` checks that the setters at their main values reproduce the main pair.

| Part | What it holds | Folder | Fingerprints, Reference 20 / 40, Adverse 20 / 40, Stress 20 / 40 |
|---|---|---|---|
| M | the main rows: no programme, the full-coverage design and the opt-in design, every output key; the financed main rows | `r2-m-ENV-YRS-104691f` | `a2e697d02f18df05` / `43995d832ae9b956`, `d8d70966f21ab009` / `85f26facf1c78952`, `4b1221649a1b711c` / `120ffdc22bf5669b` |
| S | the readings paid for by the Source: the 62 preregistered readings, the pairs, the least-favourable bound, the backing curve, the named readings | `r2-s-ENV-YRS-104691f` | `822eb5bbc067edb5` / `963cd508f68c8c4a`, `47ee045246c3795a` / `42384c77623b8c91`, `5ac845023f082461` / `9ffc28ec8380575c` |
| F | the financed rows (a contribution pays; without the weighted top tail) | `r2-f-ENV-YRS-104691f` | `5965a1bdbde18ffb` / `88b4fd8bea5a728f`, `e24d0f584284b8ec` / `83bbd6ce71f3e82a`, `2cd63202298faed4` / `2f0d48cb03d331a9` |
| B | the main pair at 10,000 adults | `r2-b-ENV-YRS-104691f` | `47a61bcf0e028ac6` / `d4b3956959b7bb5d`, `b9a975f396b603c0` / `3309fbf1cb99f620`, `9d1304608bdbb464` / `8171c5aaadf61f6f` |

### From the results to the pages

| Published tables and figures | Command (in this repository) | Output | Fingerprint |
|---|---|---|---|
| Every table of the v5.9 analysis (effects, curves, backing, financed rows, who gains, work) | `python3 dev/tools/s64_tables.py RESULTS_DIR dev/runs/s64-round2` (bootstrap 2,000 resamples, generator seed 6301) | `dev/runs/s64-round2/` (tables, curve files, `s64-summary.json`); published as results folder `r2-tables-104691f` | folder `4fa10c3d6db76b38` |
| The erosion share of each wealth figure, basket poverty by labour-force status | `node dev/tools/s64_erosion.js ENV --years=40 --seeds=A-B` (`run.txt` of the folder) | results folder `r2-erosion-104691f` | `b44b40a8fae9e1b1` |
| The 24 charts | `python3 dev/tools/s64_charts.py` | `dev/runs/s64-round2/charts/`, copied to `data/studies/r2-charts/` | — |
| The findings page's v5.9 sections | `python3 dev/tools/r2_study_files.py` (`--check`: the files are what the script writes) | `data/studies/r2-effects.json`, `r2-curves.json`, `r2-backing.json`, `r2-financed.json`, `r2-distribution.json`, `r2-work.json` | `13c3cf09b3b7b501`, `d00f4c0dcc3fc329`, `5ecf5357aba7103f`, `315092af48960102`, `d506dbb0d8f0ba61`, `9801fc4e17e77734` |
| The suite page's v5.9 series (plain and weighted) | `python3 dev/tools/suite_r2.py RESULTS/x4-a60bd3e RESULTS/x2-5b62481` (`--check`) | `data/releases/r2/suite-20.json`, `suite-40.json`, `index.json` | `99d34961632b71ee`, `d74a5e413f39c231`, `a2b8f6d6a34363cf`; results folder `x4-a60bd3e` `1f575f7985e39bb7` |
| The suite page's measures study | `python3 dev/tools/suite_r2.py --study RESULTS/x3-6d095a1` | `data/releases/r2/study-20.json`, `study-40.json` | `3af82d5ddd052fb9`, `b10427608c5b9034`; results folder `x3-6d095a1` `4709d7d6a29855e9` |

### The central-bank study (100 paired seeds)

| What | Command (in a clean worktree of the commit named) | Results folder | Fingerprint |
|---|---|---|---|
| The study: Reference, Adverse, Stress and History (2005-2025), both designs, with and without the rule | at `3beb5ff`: `node dev/tools/s74_pilot.js ENV 100 --out=DIR` for `ENV` ref, adv, st, hx; `node dev/tools/s74_table.js DIR` | `s74-final-3beb5ff` | `8660e623a255cf8f` |
| The page data | `python3 dev/tools/s76_cb_data.py DIR --check-r2=R2_DIR` (stops unless the no-central-bank arm equals v5.9's main row per seed) | `data/studies/s74-cb.json` | `92e69c0b337b0bf2` |
| The forward sweep (20 seeds) | at `d94b73c`: `node dev/tools/s74_sweep.js ENV 20 --out=DIR`; `node dev/tools/s74_sweep_table.js DIR` | `s74-sweep-d94b73c` | `7c57649d1360f3b3` |
| The source-based forced-sale discounts (20 seeds) | at `e5649ef`: as `run.txt` gives | `s74-fd-e5649ef` | `eb58bc36c1a9f611` |

### The history study (100 paired seeds)

| What | Command | Results folder | Fingerprint |
|---|---|---|---|
| The engine readings: four US policy eras, six arms, both designs | at `e5649ef`: `node dev/tools/s75_eras.js ERA 100 --out=DIR` for `ERA` e1-e4; `node dev/tools/s75_table.js DIR`; checked first by `node dev/tools/s77_check_start.js R2_DIR 2` | `s75-eras-e5649ef` | `913086008cc29d20` |
| The descriptive panel of the eras (no engine) | at `54e88bc`: `python3 sources/s75_eras.py` (`check`: identical) | `s75-panel-54e88bc` | `02d3e6d9afd61f3f` |

### Headline values to compare (main row against no programme, 500 paired seeds)

Programme run against no programme, with the effect in points (dollars for wealth). Basic living, the cost of living and too little wealth count each simulated adult once (unweighted); median real wealth is weighted (each adult at its population weight); programme inflation is the yearly rise in the basket index above no programme. Every row assumes full backing (the design's statement).

| Design, environment, years | Below 30 days of basic living | Below the cost of living | Too little wealth (yearly average) | Median real wealth (year-0 $) | Programme inflation (points a year) |
|---|---|---|---|---|---|
| Full coverage, Reference, 20 | 0.9% vs 19.6% (−18.72) | 3.7% vs 36.1% (−32.39) | 6.0% vs 24.6% (−18.60) | $432,297 vs $223,853 (+208,444) | +0.15 |
| Full coverage, Reference, 40 | 0.5% vs 19.4% (−18.90) | 2.1% vs 32.8% (−30.73) | 3.2% vs 23.3% (−20.05) | $843,651 vs $400,997 (+442,654) | +0.06 |
| Full coverage, Adverse, 20 | 0.8% vs 20.6% (−19.83) | 4.0% vs 44.6% (−40.63) | 5.9% vs 25.5% (−19.63) | $399,515 vs $202,097 (+197,418) | +0.18 |
| Full coverage, Adverse, 40 | 0.5% vs 23.4% (−22.96) | 2.4% vs 48.5% (−46.10) | 3.3% vs 27.0% (−23.79) | $662,354 vs $273,527 (+388,827) | +0.09 |
| Full coverage, Stress, 20 | 0.8% vs 20.6% (−19.83) | 4.5% vs 44.6% (−40.13) | 6.5% vs 25.5% (−19.06) | $371,588 vs $202,097 (+169,491) | +0.18 |
| Full coverage, Stress, 40 | 0.5% vs 23.4% (−22.95) | 3.1% vs 48.5% (−45.37) | 3.8% vs 27.0% (−23.25) | $604,238 vs $273,527 (+330,711) | +0.09 |
| Opt-in, Reference, 20 | 7.3% vs 19.6% (−12.32) | 15.2% vs 36.1% (−20.92) | 13.7% vs 24.6% (−10.90) | $323,278 vs $223,853 (+99,425) | +0.12 |
| Opt-in, Reference, 40 | 5.9% vs 19.4% (−13.53) | 12.9% vs 32.8% (−19.98) | 10.4% vs 23.3% (−12.90) | $613,145 vs $400,997 (+212,147) | +0.05 |
| Opt-in, Adverse, 20 | 10.0% vs 20.6% (−10.60) | 25.7% vs 44.6% (−18.92) | 16.0% vs 25.5% (−9.58) | $274,108 vs $202,097 (+72,011) | +0.08 |
| Opt-in, Adverse, 40 | 12.2% vs 23.4% (−11.18) | 31.8% vs 48.5% (−16.67) | 16.3% vs 27.0% (−10.71) | $386,852 vs $273,527 (+113,325) | +0.01 |
| Opt-in, Stress, 20 | 16.4% vs 20.6% (−4.26) | 37.0% vs 44.6% (−7.67) | 21.7% vs 25.5% (−3.88) | $230,917 vs $202,097 (+28,820) | +0.02 |
| Opt-in, Stress, 40 | 18.9% vs 23.4% (−4.54) | 41.7% vs 48.5% (−6.75) | 22.7% vs 27.0% (−4.35) | $319,879 vs $273,527 (+46,353) | +0.00 |

The earlier corrected runs' first versions (`s74-final-a60ecd1`, `s74-sweep-a60ecd1`, `s74-fd-a60ecd1`, `s74-cb-5f11ceb`, `s75-eras-77a85d6`) left out two global settings, so their main row was not v5.9's; they are superseded and kept as published.

## v5.3 and the v5.6 panels

The rest of this page was written for v5.3 and is kept as it was. Every number on the simulation page (`index.html`), the findings explorer (`findings.html`) and the replication page comes from one data file per release (`data/releases/v<version>.json`), which `dev/tools/release_data.py` writes from the run files in `dev/runs/`. This page lists, for each group of published tables and figures, the command that makes the run file, the file, and a fingerprint to compare with. The model is described in [MODEL_SPEC.md](MODEL_SPEC.md); the switches in [TESTBED_SPEC.md](TESTBED_SPEC.md).

### Set-up (v5.3)

- Node 22 (the v5.2 and v5.3 runs used v22.22.0; each run file records its own in `_meta.manifest.node`) and Python 3 (standard library only).
- `npm ci` installs the one dev dependency (jsdom, for the page tests) at the versions in `package-lock.json`. The simulation itself needs no install: open `index.html`.
- The three checks: `npm test` (`node harness.js validate`, `node harness.js unit`, `node domtest.js`; about 7 minutes).
- Run each 500-seed command from a clean checkout of the release commit. One process per environment; they can run side by side (the runs are independent and seeded, so splitting changes no figure). A v5.3 20-year release panel takes about 2 hours per environment on one core and a 40-year one about 3½ hours (v5.2's took 55 and 95 minutes: v5.3's panel has more rows, and households cost more to simulate); the backing sweep and the attribution study take about an hour each.

**Fingerprints.** A run file holds its results and, under `_meta`, how and when it was made (commit, date, seconds). A rerun gives the same results but a new `_meta`, so compare `python3 dev/tools/panel_hash.py FILE` (SHA-256 of everything except `_meta`, written canonically; first 16 hex digits below). The v5.2 files were made at commit `42cd8b9` (v5.2); the engine is unchanged in v5.2.1 and v5.2.2, so the same commands at a later release commit give the same fingerprints. Checked on Oct 6, 2026: `node harness.js testbed 500 release ref` at commit `f8427e1` (the v5.2.2 work, clean tree; 53 minutes) gave `1799e859c5e90b1e`, the published Reference fingerprint, with the same engine-block hash.

### The release data (v5.3)

| Published tables and figures | Command | File | Fingerprint |
|---|---|---|---|
| Main result, 20 years: headline cards (with children), main table (`rel-t20`), run by run (`rel-paired`), households and children (`rel-hh`), Hub-target table, the readings table (`rel-v53`), who gains, cost and how it is paid, year-by-year charts, prices | `node harness.js testbed 500 release ref --v53 --json=dev/runs/release-panel-ref.json` (and `adv`, `st`), commit `c5e96f9` | `dev/runs/release-panel-ref.json` / `-adv` / `-st` | `691b1c65af92edc9` / `83ceec24c2e1c25a` / `2d54d56182143300` |
| The same, merged | `python3 dev/tools/merge_panel.py` | `dev/runs/release-panel.json` (embedded in `index.html` as `#rel-data`) | `ac9f9245b8b86dce` |
| Main result, 40 years (`rel-t40` and every 40-year view) | `node harness.js testbed 500 release ref --v53 --years=40 --json=dev/runs/release-panel-40-ref.json` (and `adv`, `st`), commit `c5e96f9` | `dev/runs/release-panel-40-ref.json` / `-adv` / `-st` | `a20a6138deabd5a0` / `2268b7f481b2282b` / `a624ff71ea4f4d28` |
| The same, merged | `python3 dev/tools/merge_panel.py 40` | `dev/runs/release-panel-40.json` (`#rel-data-40`) | `2c7678bab1ac2cbb` |
| Backing-share chart and table (`bs`) | `node harness.js testbed 500 backing ref --v53 --json=dev/runs/backing-share-ref.json` (and `adv`, `st`), commit `289e723`, then `python3 dev/tools/backing_chart.py` | `dev/runs/backing-share-ref.json` / `-adv` / `-st`; merged `backing-share.json` | `90c459e3122289a9` / `7a9d006d788c736a` / `edbb09283f9cbbf0`; `ccf454fdfe6464b5` |
| What each part does (`rel-attrib`, the simulation page’s "What each part does") | `node dev/tools/attrib_check.js ref 500 20` (and `adv`, `st`), commit `289e723` | `dev/runs/attrib-check-ref.json` / `-adv` / `-st` | `9fad7cb56355ed31` / `49cec38a0c08923e` / `feb0e17254048373` |
| The no-programme run against US data (`rel-us`, `rel-us3`, `rel-us2`) | `node dev/tools/us_check.js ref 500 20 --v53` and `adv`, commit `289e723` | `dev/runs/us-check-ref.json` / `-adv` | `0e65d71aef08c477` / `ed00bc8df34285e6` |
| Spread across the runs, savings deciles, one run’s 500 adults (the simulation page’s explore sections) | `node dev/tools/explore_export.js ENV YRS 500 1 --v53` for ENV `ref`, `adv`, `st` and YRS `20`, `40`, commit `c1f8b8e` (after the merges) | `dev/runs/explore-ENV-YRS.json` | ref 20 `ed40277e7856ad34`, ref 40 `27dbb0baea6802f5`, adv 20 `42e99ad23b106b87`, adv 40 `4cbd8d36d9ce7a6f`, st 20 `6a08204f22a025f9`, st 40 `c2734846946b78e7` |
| The release file, the list of releases and the pages’ static figures | `python3 dev/tools/release_data.py` (`--check` confirms they are current; domtest Phase 14 runs it) | `data/releases/v5.3.json`, `data/releases/v5.3/*` (including `attrib.json`), `data/manifest.json` | — (generated; checked by `--check`) |
| The constants the release file quotes (wealth line, poverty line, BLEI days) | `node harness.js constants` | `dev/runs/constants.json` | — (Phase 14 checks it equals the harness’s CFG) |
| Earlier releases in the version switcher (v5.0, v5.0.1, v5.1, v5.2) | v5.2’s file is the one published with v5.2.2 (its status now “earlier”); the older ones: `python3 dev/tools/release_data.py --backfill v5.1` (and `v5.0.1`, `v5.0`), from the files committed at each tag | `data/releases/v5.2.json`, `v5.1.json` etc. | v5.2’s commands and fingerprints are in this file at tag `v5.2.2` |

#### Headline values to compare, v5.3

Below the cost of living (share of adult-years); children below the cost of living (share of child-years); too little wealth at the last year (share of adults); below 30 days of basic living (BLEI, share of adult-years); the change in too little wealth with its 95% interval (percentage points, paired by seed); programme inflation a year; cost per adult a year (today’s dollars).

| Environment, years | Below the cost of living | Children below the cost of living | Too little wealth | Below 30 days (BLEI) | Change in too little wealth | Inflation | Cost |
|---|---|---|---|---|---|---|---|
| Reference, 20 | 16.7% vs 45.1% | 29.4% vs 72.6% | 36.0% vs 30.5% | 10.4% vs 25.4% | +5.51 (+5.29 to +5.73) | 47.9% | $31,366 |
| Adverse, 20 | 33.7% vs 72.1% | 51.2% vs 91.3% | 89.4% vs 48.8% | 18.6% vs 32.1% | +40.57 (+40.39 to +40.76) | 61.5% | $29,567 |
| Stress Test, 20 | 56.6% vs 72.1% | 76.5% vs 91.3% | 86.3% vs 48.8% | 37.6% vs 32.1% | +37.50 (+37.29 to +37.71) | 28.5% | $12,177 |
| Reference, 40 | 12.1% vs 36.5% | 22.5% vs 62.2% | 18.4% vs 27.3% | 8.8% vs 26.5% | −8.91 (−9.09 to −8.72) | 44.7% | $32,854 |
| Adverse, 40 | 54.5% vs 83.8% | 69.5% vs 95.3% | 98.8% vs 70.2% | 30.0% vs 45.2% | +28.62 (+28.45 to +28.78) | 89.1% | $28,555 |
| Stress Test, 40 | 73.4% vs 83.8% | 86.4% vs 95.3% | 98.5% vs 70.2% | 59.8% vs 45.2% | +28.35 (+28.19 to +28.52) | 43.0% | $12,336 |

### Diagnostics and step studies (not on the pages; behind decisions and reports)

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

## Checking a reproduction (v5.3; for v5.9, compare against `SHA256SUMS` as above)

1. Run the command at the release commit with a clean tree (the manifest records `dirty: false`).
2. `python3 dev/tools/panel_hash.py` on your file and on the committed one: the 16-digit fingerprints match.
3. For the whole chain: `python3 dev/tools/release_data.py --check` and `node domtest.js` (Phase 14 compares every number on the three pages with the release data).
