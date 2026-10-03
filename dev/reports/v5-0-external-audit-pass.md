# External audit pass on v5.0: clarity, rigor and technical issues

**Date:** Oct 2, 2026. **Target:** `main` at `9596af3`, which is nine commits after the `v5.0` tag (`b43750b`); the 40-year panel and the walk-through rebuild exist only on `main`, so the live page is not the tagged artifact.
**Method:** cloned the repository; ran `validate`, `unit` and `domtest` (all passed); executed the page in jsdom (live runs, with and without Chart.js); ran paired harness studies; compared page and harness top-level bindings with a parser; ran ESLint bug-class rules; checked the two attached audits' claims against the code.
**Scope:** items already tracked in CONTRIBUTING.md are not restated.

## 1. The two attached audits, checked against the code

| Claim | Verdict |
|---|---|
| ChatGPT V5-01: the tag carries two version identities | **Confirmed, and wider than reported.** 13 static fields said 4.22 (see section 2). The README has no version string, so that part does not apply. |
| V5-02: the framework BLEI gate reads last year's `_fwBUm` | **Confirmed.** Smaller than rated: poverty, wealth, prices and cost move by 0.1 point or less; the design-neutral BLEI reading moves 0.2-1.8 points. Proposed, not applied (`dev/proposals/`). |
| V5-03: the gate should use the BU spent, not the budget | **Does not hold.** `fwB0` is already capped at essentials and DECISIONS records the choice. Only a comment is loose. |
| V5-04: source parity is not dependency parity | **Partly outdated.** A behavioural parity check exists, but only seeds 1-2, 3 of 11 rows, 20 years. Top-level bindings shared by page and harness: 83 of 85 identical; the two differences (`CFG` has two extra display-only poverty-line keys on the page; `TIERS` carries colours and CSS classes on the page) do not enter the engine. All 46 function bodies compare correctly under a real parser. A coverage gap, not a current divergence. |
| V5-05: optional framework modules are exercised thinly | Plausible, **not tested** in this pass. |
| V5-06: `META` is called the single source of truth but static fields are hard-coded | **Confirmed**; now enforced by CI (section 2). The static copies are needed for crawlers, so the fix is a check, not runtime generation. |
| V5-07: `runYear()` reads ambient state | True, and architectural. It conflicts with the single-file constraint the project has reaffirmed; not pursued. |
| V5-08: no machine-readable provenance manifest | **Valid.** `_meta` has no commit, no file hashes, no Node version. |
| xAI: maintainability, size, no external review | General and already disclosed in README and CONTRIBUTING; nothing new that I could verify. |

## 2. New findings

| # | Severity | Finding | Status |
|---|---|---|---|
| F1 | High | **A live run's text says "No group is worse off than with no programme on any test" whatever its numbers show.** `relLiveRows` hard-codes `worse:'none'`. Reference, seeds 1-6: adults who did not take part lose $415-$1,441 in every seed. Adverse and Stress, seeds 1-6: wealth poverty rises (+2.2 to +8.8 points) in all 12. | **Fixed** (`relLiveWorse`) |
| V5-01 | High | **13 static fields said 4.22 in a 5.0 release:** page `<title>`; JSON-LD `softwareVersion`; two static `.meta-ver` labels; the script banner; the CONTRIBUTING signature line; on the replication page the JSON-LD name, the seal tooltip, three "now at v4.22" caveats, and both meta descriptions. `domtest` only checked labels filled in at run time. | **Fixed**, plus `dev/tools/check_versions.js` (run by `domtest` Phase 13) and an extended `set_version.py` |
| F2 | Medium | **The earlier-engine explorer stalls without Chart.js.** `finish()` throws in `drawThresholdCharts` and the status bar stays at "Simulating year 20 of 20…100%". `domtest` stubs `Chart`, so it never saw this. The front door survives. | **Fixed** (guard plus a visible note) |
| F3 | Low-Medium | **Price level.** The front door shows the mean over seeds of a compounding quantity, stored under the key `pLev20` even in the 40-year panel. Measured per seed: at 20 years mean and median agree within 1% in all three environments (so the mean is fine there). At 40 years: Reference mean/median 1.03; **Adverse 1.24** (mean 8.5x10^8, median 6.9x10^8, 40 seeds). The 40-year Adverse page text reads "821,679,717 times today's", which a reader will take as a forecast. | Not applied. Show the median with a range, rename the key, and cap or reword the display above 1,000x |
| F4 | Medium | **The Hub's own targets are invisible at the front door.** The release engine computes Gini (`giniD`, `giniX`) but the panel rows do not carry it. The Gini target (<=0.25) and poverty target (<2%) are never shown against achieved values; extreme poverty appears only as homelessness avoided. | Not applied (enhancement E1) |
| F5 | Low | Check counts disagree across documents (95, 97; actual now 102). | Code Contributions count fixed; the historical v5.0 note left as history |
| F6 | Low | The "mixed result" sentence named inflation as the cause even for runs with none; a dead `+(...?'':'')` expression; result panels had no `aria-live`; front-door state (environment, years) is not URL-addressable. | First three **fixed**; deep link is E4 |

**Checked and clean:** the embedded `rel-data` and `rel-data-40` JSON are byte-identical to `dev/runs/release-panel*.json`; ESLint found no undefined globals, unreachable code, duplicate keys or NaN comparisons (only benign `var` redeclarations such as `cfPTF`, `cfPreCCO`, `lbC`); the front door renders when Chart.js is missing; the page has `lang`, one `h1`, labelled table headers and `aria-pressed` toggles.

## 3. What was changed in this pass

Page and text only; **the engine is untouched and every shipped figure is bit-identical** (`validate` reproduces all fixtures). `domtest` goes from 98 to 102 checks. The four new checks were run against the unfixed pages and all four fail there, so they detect the defects they name.

Files: `index.html`, `replication.html`, `CONTRIBUTING.md` (new "Unreleased: external audit pass" section), `domtest.js` (Phase 13), `dev/tools/check_versions.js` (new), `dev/tools/set_version.py`, `dev/proposals/V5-02-*`, this report, `dev/AUDIT-HANDOFF.md`.

## 4. Priority list

**A. Fix or correct**
1. *(done)* F1 live-run sentence. 2. *(done)* V5-01 static versions plus the CI check. 3. *(done)* F2 Chart.js guard.
4. V5-02 gate timing (mechanics release; patch ready; section 1).
5. F3 price-level reporting (median and range; relabel; cap the display).
6. Decide on an immutable corrected citation: the `v5.0` tag still points at the commit with stale fields. Do not move it; bump to 5.0.1 with `python3 dev/tools/set_version.py 5.0.1` and let `release.yml` tag it.

**B. Open items to address** (tracked in CONTRIBUTING; ordered by what this pass touched)
1. V5-08 provenance manifest. 2. Extend behavioural parity (all rows, 40 years, a bindings fingerprint with an allow-list for the two display-only differences). 3. V5-05 feature-matrix smoke tests (framework alone; plus project, ESP, price, labour, all modules).
Already open and worth taking up next: wealth initialisation (about 5.3x below the SCF median), poverty lines under inflation, Gini small-sample bias, PTH appreciation accounting.

**C. Enhancements to the simulation**
- **E1. Hub-target scoreboard.** Export Gini and an extreme-poverty figure in the panel rows; show a small table of achieved against target (Gini <=0.25, poverty <2%) per environment and horizon. High value: it is what a reader of the Hub expects to see.
- **E2. Backing-share curve.** The page's "decisive unknown" is how much new output conversion rewards call forth, shown only as two end points (release and H1). The harness parameter `a` is a fractional share (`(1 - o.a)*A.conv`), so sweep `a` = 0, 0.25, 0.5, 0.75, 1 and draw one static chart of wealth poverty and programme inflation against it. This turns the limitation into a result.
- **E3. Download the front-door figures** (CSV/JSON with `_meta`, version and command), as the earlier-engine explorer already does for its own results.
- **E4. Deep links** (`?env=adv&years=40`) so a specific panel can be cited.
- **E5. Manifest in `_meta`:** commit, SHA-256 of `index.html` and `harness.js`, Node version; `domtest` verifies it.
- **E6. Auto-generated check counts** in README/CONTRIBUTING, so counts cannot drift again.

## 5. Not done in this pass
The V5-05 feature-matrix test; a 500-seed regeneration for V5-02 (the table uses 60 paired seeds); E1-E6; reading the walk-through video or checking the Hub papers against the model. No independent economist has reviewed the model, which the project already says.
