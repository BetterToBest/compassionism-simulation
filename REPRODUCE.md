# Reproduce every published table and figure

Every number on the simulation page (`index.html`), the findings explorer (`findings.html`) and the replication page comes from one data file per release (`data/releases/v<version>.json`), which `dev/tools/release_data.py` writes from the run files in `dev/runs/`. This page lists, for each group of published tables and figures, the command that makes the run file, the file, and a fingerprint to compare with. The model is described in [MODEL_SPEC.md](MODEL_SPEC.md); the switches in [TESTBED_SPEC.md](TESTBED_SPEC.md).

## Set-up

- Node 22 (the v5.2 runs used v22.22.0; each run file records its own in `_meta.manifest.node`) and Python 3 (standard library only).
- `npm ci` installs the one dev dependency (jsdom, for the page tests) at the versions in `package-lock.json`. The simulation itself needs no install: open `index.html`.
- The three checks: `npm test` (`node harness.js validate`, `node harness.js unit`, `node domtest.js`; about 7 minutes).
- Run each 500-seed command from a clean checkout of the release commit. One process per environment; they can run side by side (the runs are independent and seeded, so splitting changes no figure). A 20-year release panel takes about 55 minutes per environment and a 40-year one about 95 minutes on one core.

**Fingerprints.** A run file holds its results and, under `_meta`, how and when it was made (commit, date, seconds). A rerun gives the same results but a new `_meta`, so compare `python3 dev/tools/panel_hash.py FILE` (SHA-256 of everything except `_meta`, written canonically; first 16 hex digits below). The v5.2 files were made at commit `42cd8b9` (v5.2); the engine is unchanged in v5.2.1 and v5.2.2, so the same commands at a later release commit give the same fingerprints. Checked on Oct 6, 2026: `node harness.js testbed 500 release ref` at commit `f8427e1` (the v5.2.2 work, clean tree; 53 minutes) gave `1799e859c5e90b1e`, the published Reference fingerprint, with the same engine-block hash.

## The release data (v5.2 figures, shown in v5.2.2)

| Published tables and figures | Command | File | Fingerprint |
|---|---|---|---|
| Main result, 20 years: headline cards, main table (`rel-t20`), Hub-target table, the readings table, who gains, cost and how it is paid, year-by-year charts, prices | `node harness.js testbed 500 release ref --json=dev/runs/release-panel-ref.json` (and `adv`, `st`) | `dev/runs/release-panel-ref.json` / `-adv` / `-st` | `1799e859c5e90b1e` / `4f0d4dd0aa43e125` / `90c428c2902db7e0` |
| The same, merged | `python3 dev/tools/merge_panel.py` | `dev/runs/release-panel.json` (embedded in `index.html` as `#rel-data`) | `c6052c7e30acbba8` |
| Main result, 40 years (`rel-t40` and every 40-year view) | `node harness.js testbed 500 release ref --years=40 --json=dev/runs/release-panel-40-ref.json` (and `adv`, `st`) | `dev/runs/release-panel-40-ref.json` / `-adv` / `-st` | `2cd3c9a960f168a1` / `3b4fce96ccebffc2` / `94ffe28bf4b8db0c` |
| The same, merged | `python3 dev/tools/merge_panel.py 40` | `dev/runs/release-panel-40.json` (`#rel-data-40`) | `591f8b45968e3941` |
| Backing-share chart and table (`bs`) | `node harness.js testbed 500 backing ref --json=dev/runs/backing-share-ref.json` (and `adv`, `st`), then `python3 dev/tools/backing_chart.py` | `dev/runs/backing-share-ref.json` / `-adv` / `-st`; merged `backing-share.json` | `442022b2f551d7d1` / `ce46dabd3d66b482` / `b4578322561ac8a3`; `c221fce783137801` |
| The no-programme run against US data (`rel-us`, `rel-us2`) | `node dev/tools/us_check.js ref 500 20` and `node dev/tools/us_check.js adv 500 20` | `dev/runs/us-check-ref.json` / `-adv` | `46e53f509403e7e4` / `19fd2109a15ad1d4` |
| The BU indexed every year, at H1 (front-door note) | `node dev/tools/cola_check.js adv` and `st` | `dev/runs/cola-check-adv.json` / `-st` | `9dd011fdd3a751fa` / `4c2566346d69e7a2` |
| Spread across the runs, savings deciles, one run's 500 adults (the simulation page's explore sections) | `node dev/tools/explore_export.js ENV YRS 500 1` for ENV `ref`, `adv`, `st` and YRS `20`, `40` (commit `4e17968`, engine unchanged) | `dev/runs/explore-ENV-YRS.json` | ref 20 `36acfc14ba50e827`, ref 40 `201a6571519d3a5a`, adv 20 `f205a24d19d84712`, adv 40 `4ccfb653c5d2ef30`, st 20 `842d1c10461ba198`, st 40 `6752314fb72fc00a` |
| The release file, the list of releases and the pages' static figures | `python3 dev/tools/release_data.py` (`--check` confirms they are current; domtest Phase 14 runs it) | `data/releases/v5.2.json`, `data/releases/v5.2/*`, `data/manifest.json` | — (generated; checked by `--check`) |
| The constants the release file quotes (wealth line, poverty line, BLEI days) | `node harness.js constants` | `dev/runs/constants.json` | — (Phase 14 checks it equals the harness's CFG) |
| Earlier releases in the version switcher (v5.0, v5.0.1, v5.1) | `python3 dev/tools/release_data.py --backfill v5.1` (and `v5.0.1`, `v5.0`), from the files committed at each tag | `data/releases/v5.1.json` etc. | Regenerated from their tags and identical to their published panels: `dev/runs/v521-backfill-check.txt` |

### Headline values to compare (main row against no programme, 500 paired seeds)

Below the cost of living (share of adult-years); too little wealth at the last year (share of adults); below 30 days of basic living (BLEI, share of adult-years); the change in too little wealth with its 95% interval (percentage points, paired by seed); programme inflation a year; cost per adult a year (year-0 dollars).

| Environment, years | Below the cost of living | Too little wealth | Below 30 days (BLEI) | Change in too little wealth | Inflation | Cost |
|---|---|---|---|---|---|---|
| Reference, 20 | 22.0% vs 55.2% | 35.7% vs 52.0% | 18.7% vs 46.7% | −16.25 (−16.43 to −16.07) | 34.9% | $29,618 |
| Adverse, 20 | 42.1% vs 78.2% | 87.1% vs 82.6% | 33.1% vs 60.0% | +4.42 (+4.27 to +4.57) | 45.5% | $27,677 |
| Stress Test, 20 | 65.6% vs 78.2% | 90.6% vs 82.6% | 54.9% vs 60.0% | +7.94 (+7.80 to +8.09) | 23.8% | $10,494 |
| Reference, 40 | 15.3% vs 47.4% | 15.3% vs 44.2% | 14.8% vs 46.6% | −28.90 (−29.07 to −28.72) | 30.4% | $32,274 |
| Adverse, 40 | 62.1% vs 86.7% | 97.9% vs 94.5% | 51.7% vs 75.1% | +3.41 (+3.32 to +3.49) | 65.4% | $27,013 |
| Stress Test, 40 | 79.3% vs 86.7% | 98.8% vs 94.5% | 72.3% vs 75.1% | +4.34 (+4.25 to +4.43) | 36.4% | $10,685 |

## Diagnostics and step studies (not on the pages; behind decisions and reports)

| What | Command | File |
|---|---|---|
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
