# Contributing to the Compassionism Framework Simulation

**Better To Best Research Hub** · [BetterToBest.github.io/research-hub](https://BetterToBest.github.io/research-hub/)  
CC BY 4.0 · Contact: BetterToBestResearch@gmail.com

---

## Research Objective

These simulations are designed to identify parameter configurations where **optimal-for-all** conditions align with **ideal-for-each** — analogous to a structural model that must meet a specified load capacity across all points simultaneously. The five Compassionism architectures (CCO, PTF, PTH, SZH, CIP) are the design variables; BLEI-calibrated welfare metrics are the load criteria.

The goal is not to find a single "correct" answer but to map the solution space: where do welfare improvements compound, where do trade-offs appear, and where do the six BLEI tiers distribute under different real-world conditions? Community input is essential to refining and validating this map.

---

## Reference Parameter Configuration

The **Full Integration** preset (seed 42, 20 years) serves as the illustrative reference run and loads automatically when the simulation opens. These are empirically calibrated *reference* values — not asserted optima:

| Parameter | Reference value | Rationale |
|---|---|---|
| Monthly BU allocation | $1,200/month | Approximates US median rent/basic-needs floor |
| CCO participation rate | 78% | Above min-viable 55% network threshold |
| PTF market share | 18% | Below 30% distortion threshold |
| PTH uptake | 20% | Conservative housing transition rate |
| SZH zone coherence | 0.72 | Mid-range cooperative zone coherence |
| CIP democratic rate | 65% | Moderate civic participation |
| Simulation years | 20 | Two decades captures full automation wave |
| Seed | 42 | Fixed for reproducibility; labeled "illustrative reference" |

The label "Reference" (not "Optimal") reflects that these are calibrated starting points for exploration — the solution space around them is what the simulation is designed to map.

---

## v4.6 Release Notes

v4.6 is another good-first-issues pass, not a mechanics-audit release — three items from the Good First Issues list plus one Model Architecture Feedback item, all completable without a framework-author calibration call. Two items touch simulation output only for users who explicitly opt into a new, off-by-default toggle; the third is export-only; the fourth is a re-run of an existing study, not a code change.

- **Latin Hypercube sensitivity export — implements the exact spec from Good First Issues.** A new "🧮 Export LHS Sensitivity Design" button (sidebar, appears alongside the OAT button after a run) builds a stratified Latin Hypercube design over the same five parameters and ranges OAT already perturbs (BU, participation, Initial PTF share, inflation, conversion tax), reusing `mulberry32` for the design draw itself as specified. Each of 100 design points (default `LHS_N`) runs as its own 200-agent/10-year mini-simulation, all at the same fixed seed (7777, matching OAT's own convention of holding the stochastic realization fixed so cross-row variation is attributable to parameters, not RNG noise) — and the design matrix plus outcome metrics (wealth poverty, median BLEI, participant/non-participant poverty) export as CSV for external Sobol/Morris/regression-based analysis in Python or R. This is deliberately **not** a Sobol sampler — genuine Sobol total/first-order indices need paired Saltelli-structured sample sets beyond a single LHS design; what this delivers is well-stratified parameter-space coverage plus real model output, which is the actual gap the CSV-export-for-external-analysis spec was describing. Verified directly against the shipped `latinHypercubeDesign()`/`runMiniSim()` functions: each of the 5 parameter dimensions is confirmed properly stratified (sorted draws fall one-per-stratum into each of the 100 equal-width bins), and a 10-row sample run through the real engine produces poverty/BLEI outputs that track sensibly with the sampled parameters (e.g. a row with 91% participation and $1,231 BU returns 27.0% poverty/705d BLEI; a row with 10% participation and $359 BU returns 44.5%/183d). Export-only — no effect on any existing run.

- **Feedback-clamped PTF adoption — opt-in, off by default.** Model Architecture Feedback flagged that "the PTF slider sets the t=0 adoption probability only... a quota-based or feedback-clamped adoption model remains open," since organic per-agent adoption (Bass diffusion + economic distress, plus a separate SZH→PTF induction pathway) has no ceiling and realised share can run well past the slider. Confirmed directly: an uncapped seed-42/20yr Full Integration run reaches 53.4% realised PTF share against an 18% slider. A new "Cap adoption at slider value" toggle in the PTF section — **off by default** — makes the slider a genuine ceiling when enabled: both adoption pathways now check a shared, continuously-updated live membership count and stop firing once realised share reaches the configured share, agent-by-agent within a year rather than only checked once per year (the same seed/config lands at 19.0% instead of 53.4% when enabled — see the note below on why it isn't exactly 18.0%). Implemented as a use-side gate on RNG draws (`uPtfAdopt`, `uSzhInduce`, `uSzhPtfShare`) `runYear()` already draws unconditionally every year regardless of branch (the v4.3 RNG-coupling discipline) — enabling the cap adds no new RNG call and does not shift stream position, so every existing preset, the seed-42 regression baseline, and every OAT/validation/ablation mini-simulation (none of which set this flag) are byte-identical to v4.5. **A caveat worth stating precisely, caught during testing:** the cap constrains organic *growth* beyond the year-0 random assignment, not the year-0 assignment itself — `instantiateAgent()`'s Bernoulli draw (`uPTF<ptfShare` per agent) already has sampling variance around the slider value independent of anything this cap touches, and a seed whose initial draw happens to land above the slider (confirmed for seed 42: 95/500 agents = 19.0% at year 0, from that pre-existing randomness alone, before any dynamics run) will hold at that level rather than being forced down to the slider's exact value. This is the correct, intended scope — retroactively correcting t=0 sampling noise would require re-drawing agents, a different and larger change not attempted here. Surfaced in run-config, CSV export, and the run-warnings banner when active.

- **FBS₅₀ half-saturation bandwidth exposed as a derived constant.** The "λ Calibration Status" note (below) recommended reporting the FBS gate's λ coefficient via its half-saturation bandwidth, FBS₅₀=ln(2)/λ, and had already hand-computed the resulting range in prose (≈$524–$4,191/month). `CFG.FBS_HALF_SAT_LO/HI` now compute that range directly from `FBS_LAMBDA_HI/LO` and display it in the Assumptions panel, so it can't silently drift out of sync if the λ range is ever revised again. **Reporting change only** — `makeLatentAgent()` still draws λ directly and uniformly from `FBS_LAMBDA_LO/HI` exactly as in v4.5; confirmed the seed-42 regression is unaffected. A genuine reparameterization — sampling FBS₅₀ as uniform and deriving λ from it, rather than the reverse — would change the shape of the λ distribution (a uniform-in-1/x transform isn't uniform in x) and remains a separate, larger open item, not attempted here.

- **Near-poverty cohort's 40-year extension, rebuilt under current (v4.5) mechanics.** Unreconfirmed since v4.1 — flagged in every release since as "now N mechanics-changing releases stale." Rebuilt via the same methodology as v4.1's own extension (N=1,000 seeds, a fresh draw — not a subset of any other study's seed range — Full Integration, 500 agents, run to 40 years instead of 20, cohort median BLEI recorded at every year). Full results and discussion below, under "40-Year Near-Poverty Cohort Extension (v4.6)" — the short version: the original v4.1 question ("does the cohort ever reach Flourishing, and does a 40+-year horizon change the answer?") is now moot, because v4.3's wealth-loop fix already answers it within the existing 20-year table (median 13.0 years to Flourishing, 5,000/5,000 runs) — this rebuild reconfirms that finding at N=1,000 almost exactly (median 13 years, mean 13.4 years to Flourishing; secure/stable milestones both within a percentage point of the existing 20-year figures). The genuinely new information the 40-year window provides is different and arguably more important: **cohort median BLEI shows no sign of plateauing** — it continues climbing at an accelerating pace past year 20 (1,618d → 7,058d by year 40, more than quadrupling), and population-wide median wealth reaches roughly $2.12M by year 40 with no indication of a ceiling. This surfaces a new open question, not resolved here — see Model Architecture Feedback.

### What did NOT get fixed, and why

This was a good-first-issues pass by explicit scope. Occupation-*stratified* automationRisk, `WEALTH_FLOOR`/`TARGET_*` recalibration, the framework-level low-wage-mechanism question, and a genuine production/treasury constraint on BU conversion proceeds all remain open, unchanged from v4.5 — see Model Architecture Feedback and the remaining Good First Issues, below. The new long-horizon wealth-growth question the 40-year cohort rebuild surfaced is also not resolved here — flagged as a new open item, below.

### Regression: seed 42 / Full Integration / 20yr, v4.5 → v4.6

| Metric | v4.5 | v4.6 | Δ |
|---|---|---|---|
| Median BLEI | 1,965d | 1,965d | — |
| Median wealth | $559,223 | $559,223 | — |
| Gini (EDC-adj.) | 0.534 | 0.534 | — |
| Wealth poverty | 16.6% | 16.6% | — |

Zero movement, confirmed directly against the shipped engine rather than assumed from code inspection alone — none of v4.6's three code changes touch default-configuration output: the PTF adoption cap defaults off (and is not set by any preset), the FBS₅₀ constants are a display-only computation over existing values, and the LHS export runs its own isolated mini-simulations without touching the main run. The 40-year cohort study is a fresh large-N study, not a mechanics change, so it has no seed-42/20yr regression entry of its own.

### 40-Year Near-Poverty Cohort Extension (v4.6)

Methodology mirrors v4.1's own extension exactly: N=1,000 seeds (1–1,000, a fresh draw), Full Integration, 500 agents, 40-year horizon instead of 20, cohort tagged by year-0 wealth < $25,000 (37.8% of the population, mean — consistent with every prior version), cohort median BLEI recorded at every year.

**Milestones (cohort median crossing each BLEI tier, per-seed, then aggregated across the 1,000 seeds) — reconfirm the existing 20-year figures almost exactly:**

| Milestone | 20yr table (N=5,000, v4.4/v4.5) | 40yr rebuild (N=1,000, v4.6) |
|---|---|---|
| Threshold (≥30d) | immediate (month 0), 5,000/5,000 | immediate (month 0), 1,000/1,000 |
| Stable (≥120d) | 36.0 months (3.0 yr) [mean 38.6mo] | 36.0 months (3.0 yr) [mean 39.0mo] |
| Secure (≥365d) | 104.9 months (8.7 yr) | 105.2 months (8.8 yr) |
| Flourishing (≥730d) | 156.0 months (13.0 yr) [mean 161.0mo], 5,000/5,000 | 156.0 months (13.0 yr) [mean 161.2mo], 1,000/1,000 |

This close a match across an independent seed range and a 5× smaller N is itself informative: it confirms the 20-year figures are not an artifact of the specific 5,000-seed draw, and that extending the horizon doesn't change *when* the cohort crosses milestones it was already crossing well inside 20 years.

**What extending to 40 years actually adds — no plateau, and a new open question:**

| Year | Cohort median BLEI (days) |
|---|---|
| 5 | 201 |
| 10 | 488 |
| 15 | 951 |
| 20 | 1,618 |
| 25 | 2,522 |
| 30 | 3,706 |
| 35 | 5,190 |
| 40 | 7,058 |

Rather than flattening out after the cohort clears Flourishing (as the pre-v4.3 mechanics did — that study's cohort median climbed only to ≈428d by year 40, still short of the 730d line), the post-v4.3 cohort's median BLEI keeps compounding, quadrupling between year 20 and year 40 alone. Year-40 population-wide headline figures (same N=1,000 runs, whole population not just the cohort) show the same pattern: median wealth ≈$2,115,547 (mean $2,117,807), EDC-adjusted Gini 0.422 (down from 0.518 at year 20 — continued equalization, not a reversal), wealth poverty 3.8%, BLEI poverty 3.2%, Flourishing rate 91.8%, population median BLEI ≈7,252 days.

**This is a genuinely new finding, not a repeat of v4.3's already-documented redistribution story, and it isn't resolved here.** The main wealth-accumulation loop (§2, Mathematical Framework in the replication page) has no explicit long-run ceiling — no retirement, no consumption floor that scales with wealth, no diminishing-returns term beyond the existing wage-growth dampening — so once an agent's annual wage-plus-conversion surplus consistently exceeds cost, wealth compounds essentially without bound over multi-decade horizons. Whether this is a problem depends entirely on what a 40-year run is being used for: as a stress-test of whether the *poverty-elimination* mechanisms keep working at longer horizons, this is arguably a non-issue (nobody is worse off). As a claim about *plausible* absolute wealth levels 40 years out, a median of $2.1M per adult household is well outside any real-world reference point this document uses elsewhere (Fed SCF, Census/BLS) and should not be read as a projection. Tracked as a new open item — see Model Architecture Feedback.

---

v4.5 is a good-first-issues pass, not a mechanics-audit release like v4.3/v4.4 — five items pulled directly from this document's own Good First Issues list (below), all completable without new external data or a framework-author calibration call. Validation scope matches the smaller stakes: a moderate-N sanity check for the one item that changes simulation output, not a fresh N=5,000 study.

- **PTH liquidity haircut implemented — tenure-cohort schedule replaces the flat 50%.** v4.3 added per-agent `pthTenure` tracking as a first step toward this; v4.5 implements the haircut itself via `pthLiquidShare(tenure)` — a linear ramp from 15% at tenure=1 (the closest available point to the BLEI paper Table 1a's "6 months" anchor, given tenure is tracked in whole years) to 85% at tenure≥5 (the paper's "5+ years" anchor), replacing the flat 50% share of annual Acre Equity appreciation counted as liquid wealth used through v4.4. Both anchors are the midpoint of the paper's cited range (10–20% / 80–90%) — the paper gives two qualitative points, not a closed-form curve, so the ramp between them is a documented interpretation choice, not a re-derivation. Since PTH membership doesn't change once assigned, most PTH agents spend the majority of a 20-year run at the mature 85% rate (16 of 20 years) — higher than the old flat 50% for most of the run, lower only in years 1–4.
- **"Copy parameters as URL."** Serializes the current sliders/toggles/seed into a query string, copied via the Clipboard API. Loading a shared link applies its params on top of the Full Integration defaults before the page's own auto-run, so a link only needs to specify what differs from the reference config; the seed-42 "illustrative reference run" banner only fires when no recognized params are present in the URL.
- **Social Security-anchored cohorts surfaced as in-app UI, not harness-only.** The N=5,000 study this document has carried since v4.3 (below) now also appears as a final-year table in the results panel — SSI-level, SSDI-level, and Retirement-level rows, computed from the same final agent state and `calcMetrics()`/`bleiMetrics()` calls the headline KPIs already use. Cross-sectional by design, matching this document's own method: cohort membership is fixed at year 0, not tracked over time. Single-run figures will vary seed-to-seed, especially for the small SSI-level cohort (≈0.8% of a 500-agent population) — this document's own N=5,000 table remains the citable figure.
- **BLEI tier definitions and preset descriptions on hover** — two smaller good first issues, done together. An ⓘ next to the tier-distribution chart's title shows each tier's day-range; each of the five preset buttons shows a one-sentence description of what it actually configures, on hover.
- **Cosmetic, no output effect:** `instantiateAgent()`'s `pthTenure:inPTH?0:0` ternary (identical branches — a copy-paste leftover, previously noted and left alone at v4.4) simplified to `pthTenure:0`.

### Regression: seed 42 / Full Integration / 20yr, v4.4 → v4.5

| Metric | v4.4 | v4.5 | Δ |
|---|---|---|---|
| Median BLEI | 1,951d | 1,965d | +14d |
| BLEI poverty | 13.6% | 13.6% | — |
| Median wealth | $558,001 | $559,223 | +$1,222 |
| Wealth poverty | 16.6% | 16.6% | — |
| Gini (EDC-adj.) | 0.535 | 0.534 | −0.001 |
| System Stability | 88.6% | 88.5% | −0.1pp |
| Avg EDC | 24.9% | 24.9% | — |

All movement traces to the PTH liquidity haircut alone — the only item in this release that touches simulation output — confirmed with an isolated N=300 seed-paired comparison (same population/RNG per seed, only `pthLiquidShare()` toggled between the old flat 0.5 and the new schedule): median wealth $523,958→$526,941 (+0.6%), median BLEI 1,820.6d→1,826.0d (+0.3%), all other headline metrics unchanged to the precision reported. All six `VAL_TESTS` pass 5/5 post-change.

### What did NOT get fixed, and why

This was a good-first-issues pass by explicit scope, not an audit release. `WEALTH_FLOOR` and `TARGET_*` recalibration, the Sobol/LHC sensitivity export, occupation-*stratified* automationRisk, the near-poverty cohort's stale 40-year extension, and the framework-level low-wage-mechanism question all remain open, unchanged from v4.4 — see Model Architecture Feedback and the remaining Good First Issues, below.

---

## v4.4 Release Notes

v4.4 is a mechanics-changing release, and the first shipped only after putting the prior release through two independent adversarial code audits rather than trusting internal validation alone — this document's own account of the v4.0-v4.3 history is a record of real bugs slipping through multiple prior passes, so an audit step is now the default before further mechanics changes to a published research artifact, not a formality.

**The audit process.** First pass: an open-weight model (Qwen3-Coder-30B-A3B-Instruct) orchestrated via RunPod Serverless, given an explicitly skeptical prompt instructing it not to assume anything was correct. It returned seven structured, plausible-looking findings. Every one was independently re-verified against the actual code and **rejected as a false positive** — a self-contradicting RNG-stream claim that named no actual conditional draw, a misread of an existing `Math.max` guard, a misunderstanding of the documented PTH-equity accounting, among others. None were applied. Second pass: a more rigorous review returned twelve findings; most held up under the same direct-code verification this time. Four were judged substantive and consequential enough to implement as a real mechanics-changing release rather than a quiet patch — the four items below.

- **Wage/income scale unified across BLEI, FBS, and Gini.** v4.0 fixed unit-mixing inside these formulas using `SIU_TO_USD` (≈16.63) — a cost-side-derived approximation, invented because no real wage-side dollar anchor existed at the time. v4.3's `WAGE_TO_USD` (≈100.52, Census/BLS-sourced) was scoped to the main wealth loop only, leaving the same agent's wage worth roughly $3,518/month for wealth accumulation and roughly $582/month for welfare measurement simultaneously — a ~6× divergence the second audit correctly identified as no longer defensible once one anchor is empirically grounded and the other isn't. `SIU_TO_USD` is **retired**. `agentBLEI()`'s income-buffer term, `calcBLEIComponents()`, the FBS gate's `Yusd`, and the EDC-adjusted-Gini calculation now all use `WAGE_TO_USD`. `agentEDC()` was and remains unaffected — it's a dimensionless SIU/SIU ratio that never touched either constant.

- **`FBS_LAMBDA` recalibrated — and the reason has since been corrected following post-release review.** `λ`'s units are 1/USD by its own original code comment; once its dominant input (`Yusd`) grew ~6× under the wage-scale fix, `λ` left unscaled pushed octave-advancement probability toward saturation regardless of BU level, measurably weakening the BU-monotonicity `VAL_TEST` (one seed dropped from a clean win to an exact tie at n=200). Rescaled ÷6.0456 — the precise `WAGE_TO_USD`/legacy-`SIU_TO_USD` ratio — from 0.001/0.008 to 0.0001654/0.0013233, preserving the 8× HI/LO heterogeneity shape. **This document originally described that rescale as a "dimensionally-necessary consequence" of λ's units — that overstated the case.** FBS combines the wage-derived term that changed scale with fixed-dollar terms (BU face value, basic cost) that did not, so FBS as a whole does not scale by a single clean factor; dividing λ by exactly 6.0456 is a *chosen behavioral recalibration* to restore useful dynamic range across the model's population, not a unit identity. It is retained because the paper's own original range (λ ~ U(0.001, 0.008)) produces near-saturated advancement probability (89.8–100%) even at the BLEI paper's own worked-example FBS ($2,281/month), leaving little of λ's intended role as an "individual capability coefficient" — see the calibration-status note added to the BLEI paper (Index IV) and to the replication framework (Mathematical Framework §4) for the full account, including the recommendation to eventually reparameterize by half-saturation point (FBS₅₀ = ln(2)/λ) rather than a raw 1/USD coefficient. All six `VAL_TESTS` pass 5/5 post-change — that establishes internal behavioral consistency, not empirical correctness of the absolute λ values; λ's empirical grounding remains open, as it was before v4.4.

- **True common-random-numbers pairing across Baseline / CCO-Only / Main.** v4.2 paired the three scenarios' *populations*; their year-by-year trajectories still ran on three independently-offset RNG streams (`seed+700001`/`seed+700002`/unoffset), decorrelated from each other and from Main — not just from population construction, as v4.2's own note already flagged as a remaining gap. Since v4.3 made `runYear()` draw a fixed count and order of RNG calls per agent per year regardless of policy toggles, three independent same-seed `mulberry32()` closures now necessarily produce identical draw sequences at each (agent, year) position — verified this has zero effect on Main's own trajectory, since `mulberry32()` returns a fresh, independent closure on every call. The ablation engine already used this same same-seed pattern successfully; this brings the main comparison in line with it.

- **Baseline's undocumented ×0.85 initial-wealth haircut removed, and automation exposure now paired.** Baseline agents received an extra ×0.85 wealth adjustment on top of sharing v4.2's paired population, applied before CCO has had any chance to act — no external citation existed for the figure, and it embedded part of the treatment effect into the counterfactual's own starting point. Removed. Separately, Baseline was hardcoded exempt from AI automation exposure even when a user enabled it for the tested scenario, while CCO-Only already mirrored the setting — now paired. Neither fix meaningfully moves the standard reference-configuration figures below (automation defaults off; Baseline's median wealth remains exactly floor-pinned regardless — now confirmed in **100% of N=5,000 runs**, not "more than half" as v4.3 described, since the binding constraint turned out to be the ongoing annual cost/wage gap, not the year-0 starting point).

**A genuine bug, found independently of either audit while building this release's N=5,000 harness.** The general-purpose gamma-distribution sampler divides by `(a−1)` inside a log term; at `a=1` exactly this is `x/0`, making the acceptance test `0×log(∞)=NaN` and therefore always false. Every call exhausted all 5,000 rejection iterations and silently returned the constant `1` — confirmed: 20 of 20 samples identical in testing — not a random Exponential(1) draw. This directly narrows `drawAutomationRisk()`'s `beta(6,1)`/`beta(1,6)` components, used once per agent on every simulation run (browser or harness), and wasted the full 5,000 dead iterations each time. Fixed with the exact closed-form solution — Gamma(shape=1) is exactly Exponential(1), so `-Math.log(RNG())` replaces the rejection loop entirely for this case. Side effect: population construction is now roughly **200× faster**, without which this release's fresh N=5,000 study would not have been practical to run in the time available.

### What the v4.4 fixes actually do

Figures below are N=5,000, same methodology as v4.3's study (seeds 1–5,000, 500 agents, 20 years, shock disabled). Full headline table under Reproducibility Testing.

Full Integration median wealth rose modestly, $495,411→$526,120 (+6.2% — not a repeat of v4.3's much larger jump; this release mostly corrects a measurement formula, not the wealth-accumulation mechanism itself, apart from the FBS-gate feedback described above). BLEI poverty fell 17.1%→12.5%; wealth poverty fell 19.5%→15.4%; EDC-adjusted Gini fell 0.536→0.518 (Full Integration and CCO-Only both became *more* equal, not less). Participant poverty (wealth) fell 15.4%→10.0%; **non-participant poverty is exactly unchanged, 34.3%→34.3%** — a clean mechanistic confirmation the fix behaves as intended, since non-participants never execute the FBS-gated code path this release touches.

The Social-Security-anchored cohorts (v4.3) improved measurably but not qualitatively: SSDI-level median BLEI 16.4d→22.6d, retirement-level 16.6d→a median-of-medians 25.1d. **A methodological correction worth naming, caught before publication:** BLEI is right-skewed for these small (≈4–86 agent) cohorts, and an initial mean-based reading of the retirement-level cohort (mean 32.0d) would have overstated it as crossing the 30-day Threshold. The median-of-medians (25.1d) and the actual per-seed crossing rate (31.1% of 5,000 seeds) both show the typical case still falls short — see the updated table below. The relative-improvement multiplier over Baseline, originally reported as 20–30× under v4.3 mechanics, is now **~7–10×** under v4.4 — not because Full Integration helps this population less, but because Baseline's own BLEI also rose under the corrected wage-buffer term (from near-zero to a few days), narrowing the ratio even as both sides' absolute figures moved in the right direction. The qualitative conclusion is unchanged: Full Integration helps this population enormously in relative terms without lifting the typical case out of poverty by the simulation's own tier definitions, for any of the three anchors.

### What did NOT get fixed, and why

`WEALTH_FLOOR`, and the pre-existing `TARGET_WEALTH`/`TARGET_POVERTY`/`TARGET_GINI` design targets, remain open — both explicitly framework-level decisions requiring the framework's own authors' judgment, not code fixes (see Model Architecture Feedback, below, now considerably more pressing given the wealth figure has moved even further from the original target). This release adds a direct in-app disclosure on the affected KPI badges (the ⓘ icons next to Gini, Median Wealth, System Stability, Flourishing Rate, and EDC in the interactive tool) pointing to this section, without picking new numbers itself. A genuine production/treasury constraint on BU conversion proceeds remains unscoped. The v4.1 40-year cohort-Flourishing extension remains unreconfirmed, now three mechanics-changing releases stale — given how far the 20-year figures have moved, a fresh 40-year run would very likely show materially different results; tracked as an open item rather than assumed either way. The Replication Framework HTML, deliberately unsynced past v4.2 pending this release's audit, is updated alongside this document — its own Version History now covers v4.3 and v4.4 together, since no intermediate v4.3 snapshot of that page was ever published.

---

## v4.3 Release Notes

v4.3 is a mechanics-changing release — **it changes the RNG call sequence and the main wealth-accumulation loop's calibration, so seed-42 output does not reproduce v4.2's** (see the new regression table under Reproducibility Testing, below). Four items:

- **Main wealth-accumulation loop unit fix (resolves the highest-priority open item carried since v4.0).** The wage(SIU)/wealth(USD) mismatch in the main annual wealth update is fixed with two new constants: `WAGE_TO_USD ≈ 100.52` converts wage to real USD (derived from $42,220 median personal income, Census/BLS CPS ASEC 2023, ÷ 35 SIU × 12); `LIVING_WAGE_ANNUAL = $49,370` anchors the cost side (a national living-wage figure for a single adult with no children — $23.735/hr average across 50 states + DC, from World Population Review's MIT-sourced table, × 2,080 hrs/yr; this is an *unweighted* average across jurisdictions, not population-weighted like MIT's own paid Living Wage Calculator product — see the caveat below). This replaces netting WAGE_TO_USD-converted wage against `BASE_DAILY_COST` — a bare-subsistence floor, correct for BLEI's poverty-line use but wrong for a 20-year compounding loop netted against real wage, and which produced an ~11x wealth explosion and broke BU-monotonicity (2/5 seeds) when tested. All six `VAL_TESTS` pass under the shipped anchor, including BU-monotonicity (5/5). `dollarCost`/`BASE_DAILY_COST` is unchanged everywhere else (BLEI, FBS, Gini, and the PTH equity contribution — see the code comment at the PTH block for why that specific choice was tested against the alternative and kept as-is) — only the main loop's cost side changes.

  **This is not a clean win — it redistributes as well as it grows, and it does so along more than one axis. See "What the wage/cost fix actually does," immediately below, for the full picture — this bears directly on the framework's central poverty-elimination claim and should not be read from the headline wealth figure alone.**

- **`runYear()` RNG coupling fixed (resolves the item found in v4.2).** Every conditional quantity inside the per-agent loop (BU spend fraction, CIP quality bump, octave advancement, SZH→PTF induction and share, PTH appreciation noise, PTF Bass adoption) is now drawn unconditionally every year for every agent; only the *use* of the drawn value is gated — mirroring the v4.2 `makeLatentAgent()` eligibility-draw fix. The non-participant-poverty validation check is tightened back to strict per-seed agreement at n=200 (was a mean-across-5-seeds workaround at n=500) and passes 5/5.

- **Per-agent PTH tenure tracking (first step, not the full fix).** Agents now carry `pthTenure` (years held in PTH residency), incremented each year while in PTH and reset on exit. This is tracking data only — the variable tenure-cohort liquidity haircut itself (BLEI paper Table 1a) is not implemented this pass; the flat 50% haircut is unchanged. Tracked as a Good First Issue, below. **v4.5 update: implemented — see Release Notes, above.**

- **Bimodal `automationRisk` distribution.** Replaces uniform[0.2,1.0] with a 47%/53% mixture — high-risk agents ~ Beta(6,1) (mean ≈0.857), low-risk agents ~ Beta(1,6) (mean ≈0.143) — sourced to Frey & Osborne (2013)/Autor (2015): ~47% of US employment sits above a 70% computerization-probability threshold across 702 O\*NET occupations. Verified to have no material effect on aggregate outcomes on its own (isolated in testing before the other three items were combined with it).

### What the wage/cost fix actually does

The single-seed spot-check that first surfaced this (seed 42, reported when the fix was first validated) is now reconfirmed at scale: a 5,000-seed large-N study (seeds 1–5,000, 500 agents, 20 years, same methodology as the v4.0/v4.2 studies below) shows the same pattern holds robustly, and reveals two further effects the single seed didn't have the power to show cleanly. All three are real, and none of them is a reason to revert the fix — `BASE_DAILY_COST` (the pre-v4.3 anchor) is arithmetically wrong for this specific loop, in a way that produced an 11x wealth explosion when tested; `LIVING_WAGE_ANNUAL` is the anchor that passes validation. But "this anchor is more correct" and "this anchor is comfortable" are different claims, and the second one is false in an important way.

1. **Within Compassionism, the fix redistributes as well as grows.** At N=5,000, Full Integration median wealth rises from $80,008 to $495,411 (a ~6.2x increase, consistent with the seed-42 spot-check's $514,502), but EDC-adjusted Gini rises from 0.479 to 0.536 and wealth poverty rises from 14.4% to 19.5%. Mechanism: low-wage-draw, high-`automationRisk`, and non-participating agents don't share proportionally in the wage-side correction the way median-and-above-wage agents do, who now compound a much larger annual surplus.

2. **The Traditional Welfare Baseline collapses far more severely than before.** This is the larger effect, and it wasn't visible in the single-seed check. Baseline agents get no CCO/PTF/PTH cost relief, so their full weight lands on the new $49,370 cost anchor — and a median-wage worker's annual wage income (~$39,800 at year-0 wage, via `WAGE_TO_USD`) doesn't cover that figure even before the baseline's existing 3% CPI compounding widens the gap every year. At N=5,000: median wealth falls from $7,316 to **exactly the wealth floor, −$10,000** — meaning more than half the baseline population is pinned at the debt ceiling by year 20 — wealth poverty rises from 52.2% to 72.3%, and Gini rises from 0.800 to 0.855. This is a legitimate, mechanistically-understood consequence of the new anchor, not a bug — but a median outcome sitting exactly at a hard floor is a blunter result than the pre-v4.3 baseline's, and raises a real question of its own: **is `WEALTH_FLOOR = −$10,000` still the right floor value now that the cost anchor roughly doubled?** Flagged as a new open item below, not resolved here.

3. **The near-poverty (low-*wealth*) cohort now reaches Flourishing — a complete reversal.** The existing near-poverty cohort (year-0 wealth < $25,000, 37.7% of the population) is defined by low starting *wealth*, not low *wage* — and most of its members have ordinary wage draws. Under the new anchor they benefit enormously: cohort-median time to Stable (≥120d) drops from 158.8 months (13.2 years) to 48 months (4 years); a new Secure (≥365d) milestone is reached at 108 months (9 years); and the cohort median reaches **Flourishing (≥730d) in 5,000 of 5,000 runs** within the 20-year horizon — versus 0 of 5,000 runs even after extending to 40 years under pre-v4.3 mechanics (see the v4.1 extension study, below). This is the flip side of finding 1: agents whose *wage* is decent do very well under this fix, regardless of how little wealth they started with.

Findings 1 and 3 together say something more precise than "wealth up, Gini up": **the fix helps agents by wage level, not by starting wealth.** A wealth-poor-but-decent-wage agent now does about as well as anyone; a low-wage agent does not, no matter their wealth. This is exactly the distinction BLEI/EDC-based analysis is supposed to surface over a raw dollar comparison, and it's the reason a wage-anchored cohort — not just the existing wealth-anchored one — is worth tracking directly. See the new Social-Security-anchored cohort study, below, which does exactly that and confirms the concern precisely: even under Full Integration, a cohort whose wage sits at real-world Social Security benefit levels remains deeply impoverished by the simulation's own tier definitions, despite being dramatically better off than under the baseline.

### Social Security-anchored income cohort (new this release)

Prompted by a question raised in review: comparing Compassionism to the US baseline using median-income anchors doesn't show how the framework treats the population most relevant to a poverty-elimination claim — people living on a fixed, sub-median income, not median-wage workers. Real 2026 Social Security figures (SSA's official COLA Fact Sheet, ssa.gov/news/en/cola/factsheets/2026.html) give three anchors:

| Anchor | Monthly / annual | Wage equivalent (SIU, via `WAGE_TO_USD`) | Share of population at or below |
|---|---|---|---|
| SSI federal payment standard, individual | $994/mo, $11,928/yr | 9.89 SIU | 0.8% |
| SSDI average, all disabled workers | $1,630/mo, $19,560/yr | 16.22 SIU | 7.7% |
| Average retired-worker benefit | $2,071/mo, $24,852/yr | 20.60 SIU | 17.1% |

These are reference points, not a simulated Social Security mechanism — the model has no age, disability, or retirement structure (see Known Limitations), so "SSDI cohort" here means *agents whose initial wage happens to sit at this level*, tracked with the same mechanics as everyone else, not agents receiving a modeled benefit with COLA adjustment or recession insulation. That distinction matters and is stated plainly rather than implied away. Tagged from each agent's initial (pre-dynamics) wage, same convention as the existing near-poverty cohort's year-0 wealth tag. `CFG.SS_ANCHOR_SSI_ANNUAL`/`SS_ANCHOR_SSDI_ANNUAL`/`SS_ANCHOR_RETIRE_ANNUAL` hold the dollar figures.

N=5,000 results, Full Integration vs. Traditional Welfare Baseline (same seeds, methodology as above):

| Cohort | Scenario | Wealth poverty | BLEI poverty | Median BLEI | Flourishing rate |
|---|---|---|---|---|---|
| SSI-level (0.8% of pop.†) | Full Integration | 96.5% | 83.0% | 26.3d | 1.6% |
| | Baseline | 99.9% | 99.9% | 1.1d | — |
| SSDI-level (7.7% of pop.) | Full Integration | 84.2% | 80.3% | 16.4d | 7.9% |
| | Baseline | 99.8% | 99.8% | 0.5d | — |
| Retirement-level (17.1% of pop.) | Full Integration | 74.0% | 67.9% | 16.6d | 13.7% |
| | Baseline | 99.7% | 99.7% | 0.6d | — |

† The SSI-level cohort is small (≈4 agents per 500-agent run), so its per-seed median is noisy even at 5,000 seeds — directionally informative, not precision-grade. The SSDI- and retirement-level cohorts (≈38 and ≈85 agents per run) are on firmer statistical ground.

**Read plainly: Compassionism helps this population enormously in relative terms — 20-30x the median BLEI of the baseline, where these agents are functionally at zero — but does not come close to lifting them out of poverty in absolute terms.** Median BLEI in the teens of days is deep in the Precarious tier, nowhere near the 30-day Threshold, let alone the reference configuration's own headline 67.8% population-wide Flourishing rate. The mechanism is direct: even with PTF/PTH cost reductions (~46% combined) and BU support, an agent whose wage sits near or below Social-Security-benefit levels doesn't generate enough annual surplus for the model's other mechanisms (octave advancement, PTF conversion gains, PTH equity building) to compound meaningfully within 20 years. **This is the sharpest test of the framework's poverty-elimination claim run so far, and the framework does not pass it** — a finding that should sit alongside the headline large-N figures in any public-facing summary, not be filed only here.

---

## v4.1 Release Notes

v4.1 is an audit-driven bug-fix release (Claude/Anthropic chat audit, Aug 2026) — unlike v4.0, it does not change simulation mechanics, so the regression baseline and large-N figures below carry over from v4.0 unchanged (confirmed, not assumed — see the v4.1 regression check under Reproducibility Testing). Three fixes:

- **PTF attribution leak in ablation.** `runAblation()`'s paired-population design (v4.0) intentionally builds every removal scenario's agents under the full config for RNG-pairing, but `agentBLEI()`'s SZH+PTF synergy term had no `ptfOn` parameter to gate on — unlike `ccoOn`/`pthOn`, which already gated the equivalent CCO/PTH terms. Result: the "Remove PTF" ablation result could retain a synergy bonus it shouldn't have whenever SZH was also active, understating PTF's contribution on the Attribution chart (~12 BLEI days per affected agent in testing). If you've cited or screenshotted Attribution-chart output from v4.0 or earlier with SZH active, it's worth a re-run under v4.1. Normal (non-ablation) runs are numerically unaffected.
- **Illustrative reference-run label was never shown.** The `IS_REF_RUN` flag (added v3.4) was set but never read, so the "illustrative reference run" banner never actually displayed. Wired up; purely cosmetic.
- **Several UI hint strings had drifted from the formulas they describe** — a recession-duration/severity hint, the Max Octave conversion-capacity hint, a stale default display value, a baseline-chart caption, and one OAT sensitivity range — none of these affect computed results, only what the UI *says* about them. Full detail in `index.html`'s own changelog (search "v4.1").

---

## v4.2 Release Notes

v4.2 is a mechanics-changing release (external audit + internal review, Aug 2026) — **unlike v4.1, it changes the RNG call sequence, so seed-42 output no longer reproduces v4.1's** (see the regression table under Reproducibility Testing, below). This is allowed under this document's own rule that an intentionally mechanics-changing PR should say so explicitly (Code Contributions, below):

- **Common-random-numbers population pairing.** `makeAgent()` is now a thin wrapper over `makeLatentAgent()` (draws pre-policy latent traits, no scenario-specific logic) and `instantiateAgent()` (pure, zero-RNG, scenario-specific mapping). The main run, CCO-Only, and baseline comparisons now share one canonically-drawn latent population instead of three independently-sampled ones — closing the item raised in the Aug 2026 external review ("the baseline and CCO-only populations are not actually the same individuals") and in Model Architecture Feedback, below. Verified with unit tests: agent *i*'s wealth/wage/automationRisk/λ are bit-identical across all three scenario instantiations, differing only in octave/quality (correctly, since those scale by scenario-specific `maxOct`/`maxMult`) and participation flags.
- **Independently found while building the above.** `makeAgent()`'s three eligibility draws used short-circuit `&&`, so the number of RNG calls consumed during agent construction depended on which subsystems were toggled on. Two scenarios built from the "same" seed but different toggle states — e.g. the validation suite's own PTF-on vs PTF-off check — silently diverged in every draw after the first toggle difference, not just membership. Fixed by drawing all three eligibility uniforms unconditionally in `makeLatentAgent()`.
- **Does not extend to full within-run trajectory pairing.** `runYear()` still consumes a variable number of RNG calls per agent depending on which of its *own* conditional branches fire that year, so two scenarios with different participation *composition* still decorrelate agent-level trajectories after year 0, even from an identical starting population. Population-level aggregates (poverty rate, median BLEI) are unaffected. **Fixed in v4.3 — see above.**
- **Structural System Stability metric**, replacing the v3.6-flagged trend-plus-noise heuristic — resolves a good-first-issue below. `structuralStability()` is the inverse coefficient of variation of median wealth and median BLEI over the run's final quarter: no RNG call, no manual per-mechanism bonus. Baseline/CCO-Only comparison rows, previously hardcoded "~65%"/"~88%", now compute the same metric from their own trajectories.
- **Validation suite → 6 checks.** The original four now run across 5 seeds (`VAL_SEEDS`) and require unanimous agreement, instead of one hardcoded seed each (all four are robust 5/5). Added a non-participant-poverty check (resolves a second good-first-issue, below) and a structural-invariants check (population conservation, octave/wealth-floor/participation bounds, Gini bounds). Renamed "Internal Validation Suite" → "Internal Consistency & Behavioral Test Suite," labeled against an ODD Level 1–5 hierarchy (this suite covers Levels 1–3 only).
- **"Policy-grade" language tightened** to "research-oriented exploratory... for comparative policy analysis" throughout title/meta/social tags, matching framing already used elsewhere in the same file (CSV export, Known Limitations).

The replication document was updated in parallel — a new Version History toggle, refreshed Known Limitations, and version numbers throughout — but its headline large-N figures have **not** yet been reconfirmed under v4.2 mechanics (see Reproducibility Testing, below). Full derivation in `index.html`'s own changelog comment (search "v4.1 → v4.2").

---

## How to Contribute

### 1. Parameter Feedback & Scenario Testing

Run the simulation with parameter configurations that model real-world conditions you know well — a specific region, income cohort, housing market, or policy environment. Export your results via **Download CSV** or **Download JSON** and open a GitHub issue with:

- Your exported CSV or JSON attached
- A brief description of the real-world scenario you were modeling
- Any discrepancies between the simulation output and observed or expected outcomes

This is the highest-value contribution. The model's calibration constants (daily basic cost, EDC ranges, PTF distortion threshold) were set from US CES 2023 data and benefit greatly from testing against other contexts.

### 2. Calibration Validation

The simulation uses several empirically grounded constants defined in the `CFG` object at the top of `index.html`. Contributions that improve these with cited sources are especially welcome:

| Constant | Current value | Source | What would improve it |
|---|---|---|---|
| `BASE_DAILY_COST` | $68.33/day | BLS CES 2023 | Regional breakdowns; non-US benchmarks |
| `CCO_PTH_DAILY_COST` | $31.67/day | BLEI §3.2 estimate | Empirical housing cost studies |
| `EDC_BASELINE_LO/HI` | 0.62–0.72 | US CES 2023, near-poverty | Income quintile breakdowns; international data |
| `PTF_OPTIMAL_SHARE` | 18% | Framework spec | Cooperative sector empirical studies |
| `PTF_DISTORTION` | 30% | Framework spec (allocative efficiency threshold) | Empirical evidence on cooperative sector market concentration limits |
| `NORDIC_GINI` | 0.28 | OECD | Year-specific updates; regional variants |
| `PROG_PIVOT` / `PROG_RATE` | 3.0 / 0.040 | Theoretical | Creative economy income distribution data |
| `SIM_COST_SCALE` | 1,500 (SIU) | ABM calibration | **Retired as a wage-conversion input in v4.4** — it only ever fed the now-retired `SIU_TO_USD` derivation (below). No longer load-bearing anywhere in the current codebase; kept in `CFG` as a historical constant. |
| `SIU_TO_USD` | **Retired in v4.4** (was ≈16.63, derived: `BASE_DAILY_COST×365 / SIM_COST_SCALE`) | Derived, v4.0 | Converted wage (SIU) to USD for BLEI, FBS, and EDC-adjusted-Gini only, v4.0–v4.3 — deliberately *not* used by the main wealth loop, which used `WAGE_TO_USD` instead, creating a ~6× divergence at the median wage. v4.4 unified all four formulas onto `WAGE_TO_USD` (below) and removed this constant entirely — see v4.4 Release Notes. |
| `WAGE_TO_USD` | ≈100.52 | Census/BLS CPS ASEC 2023 median personal income ($42,220) ÷ (35 SIU × 12) | **v4.3: main wealth-accumulation loop only. v4.4: expanded to `agentBLEI()`, `calcBLEIComponents()`, the FBS gate, and EDC-adjusted Gini as well — now the single canonical wage-to-USD anchor everywhere in the file.** Sourced and stable throughout; no change to the constant's own value across v4.3→v4.4, only to its scope of use. |
| `LIVING_WAGE_ANNUAL` | $49,370 | World Population Review's MIT-sourced state living-wage table, single adult/no children, 51-jurisdiction *unweighted* average ($23.735/hr × 2,080 hrs/yr) | **New in v4.3, highest-priority remaining calibration item.** Not population-weighted like MIT's own paid Living Wage Calculator product (large-population states span both directions — CA $30.48/hr and NY $29.89/hr are high, TX $21.77/hr and FL $24.09/hr are more moderate — so a population-weighted figure is unlikely to shift dramatically, but this is unverified). **v4.6 note:** searched for a published single population-weighted national figure from MIT's calculator; none exists — the tool is a location-by-location (state/county/metro) lookup with no published national aggregate, weighted or otherwise. Genuinely computing one would mean pulling all ~50 state-level figures and applying Census population weights directly — a real data-assembly task, still open, not attempted here. |
| `SS_ANCHOR_SSI_ANNUAL` / `SS_ANCHOR_SSDI_ANNUAL` / `SS_ANCHOR_RETIRE_ANNUAL` | $11,928 / $19,560 / $24,852 | SSA 2026 COLA Fact Sheet (ssa.gov/news/en/cola/factsheets/2026.html) | **New in v4.3.** Reference points for the Social-Security-anchored cohort study (see v4.3 Release Notes). Annual figures; update on each year's COLA Fact Sheet publication to keep current. Cohort tagging now uses `WAGE_TO_USD` for the SIU conversion as of v4.4 (unchanged in practice — the SS-anchor cohorts already used `WAGE_TO_USD` for this purpose since their v4.3 introduction; only BLEI/FBS/Gini's *own* internal formulas changed anchor in v4.4). |
| `WAGE_MEDIAN_SIU` | 35 SIU | Framework spec | Cross-scenario calibration; also the anchor point for `agentEDC()`'s rescaled saturation constants (v4.0) |
| `FBS_LAMBDA_LO/HI` | **0.0001654 / 0.0013233 (v4.4)** — was 0.001 / 0.008 through v4.3 | BLEI paper §Index IV (λ ~ Uniform), rescaled v4.4 | **Rescaled ÷6.0456 (the `WAGE_TO_USD`/legacy-`SIU_TO_USD` ratio) as a *behavioral recalibration* to restore useful advancement-probability variation — not, as an earlier version of this document claimed, a dimensionally-forced conversion (FBS mixes scaled and unscaled terms, so it doesn't scale by a single clean factor). Open calibration status: the paper's original range already saturates (89.8–100% advancement probability) at the paper's own worked example; the v4.4 range is not itself externally validated. See v4.4 Release Notes for the full account and the recommended FBS₅₀ reparameterization.** |
| `FBS_EDC_RESIDUAL_BASE/PTH` | 0.12 / 0.025 | BLEI paper Table 1b worked values | Used as a fixed proxy for "consumer debt interest only" — a separately-modelled consumer-debt submodel would be more accurate. |
| `PTH_EQUITY_CONTRIB_SHARE` | 25% | Internal design choice, not externally sourced | Matches Champlain Housing Trust's real resale-appreciation share exactly, but that's a coincidental number match, not a mechanistic validation — CHT's 25% is a one-time resale split; the sim's is an ongoing annual savings-to-equity routing. Kept at 25%; code comment reflects this is coincidental, not sourced. |
| `PTH_LIQUID_SHARE_YEAR1/YEAR5PLUS` | 15% / 85% (v4.5) — flat 50% through v4.4 | BLEI paper Table 1a ("~10-20% at 6 months rising to ~80-90% at 5+ years"), midpoints of each cited range | **New in v4.5.** The paper gives two qualitative anchor points, not a closed-form curve — v4.5's linear ramp between them (`pthLiquidShare()`) is a documented interpretation choice, not a re-derivation. Access to the paper's actual underlying curve (if one exists beyond the two cited points) would let this be tightened from an interpolation to a direct implementation. |
| `SZH_THETA_THRESHOLD/MAX_COH/MAX` | 0.55 / 0.90 / 0.25 | BLEI paper Table 6 (synergy coefficient θ) | Direct from framework spec. |
| `PTF_BASS_Q` | 0.05 | Internal design choice, not externally sourced | No cooperative-sector-specific citation exists (searched). General product-diffusion q typically 0.3–0.5, real-world q spans 0.05–0.47 across contexts in the literature. 0.05 isn't contradicted, isn't positively sourced either — kept, comment reflects the honest gap rather than implying a citation exists. |
| `BASELINE_CPI_RATE` | 3% | Historic US CPI | Baseline scenario's inflation is anchored to this fixed rate instead of copying the user's inflation slider — see Model Architecture Feedback. |
| `automationRisk` distribution | 47%/53% bimodal Beta(6,1)/Beta(1,6) | Frey & Osborne (2013)/Autor (2015) | **Resolved in v4.3** — was uniform[0.2,1.0], flagged since v3.4. Occupation-stratified (not just bimodal) risk would be a further refinement. **v4.4 note:** the underlying `gamma(a=1)` sampler this distribution's low-risk component depends on had a real bug (silently returned a constant instead of a random draw) — fixed in v4.4, see Release Notes; the *distribution choice itself* (bimodal, these sources) is unaffected and unchanged. **v4.6 note:** occupation-stratification is now a scoped good-first-issue rather than an open-ended one — Frey & Osborne (2013)'s own appendix (pp. 57–72) publishes per-occupation probabilities for all 702 SOC-2010 codes; what remains is transcribing that table and cross-walking it to current BLS OES employment shares, not sourcing new data. See Good First Issues. |
| `FBS_HALF_SAT_LO/HI` | ≈$524 / $4,191 per month | Derived (v4.6): `ln(2)/FBS_LAMBDA_HI` and `ln(2)/FBS_LAMBDA_LO` respectively | **New in v4.6**, reporting-only. Promotes the half-saturation figure CONTRIBUTING.md's own λ Calibration Status note (below) had already hand-computed in prose into a named constant computed directly from `FBS_LAMBDA_LO/HI`, displayed in the Assumptions panel, so it can't drift out of sync if the λ range is revised again. Does not change per-agent λ sampling — see the λ Calibration Status note and v4.6 Release Notes. |
| PTF adoption cap (`p.ptfCap`, UI toggle) | Off by default | Internal design choice — Model Architecture Feedback's "quota-based or feedback-clamped adoption" item | **New in v4.6, opt-in.** Not a CFG constant (it's a per-run toggle, not a calibration value), listed here for visibility. Off preserves v4.5 behavior exactly (realised PTF share can exceed the slider via organic growth); on enforces the slider as a real, feedback-clamped ceiling. See Model Architecture Feedback and v4.6 Release Notes for the mechanism, and why it defaults off. |

To propose a calibration update, open an issue with prefix `calibration:`, your proposed value, full citation, and a before/after output comparison.

### 3. Reproducibility Testing

The simulation supports seeded runs (Mulberry32 PRNG). To verify a result:

1. Note the **Random seed** and all parameter values from the exported CSV or JSON
2. Enter the same seed and parameters in the simulation
3. Confirm the output matches

If results diverge under identical seed + parameters, open a bug report with both exports. This should not happen — if it does, it indicates a browser environment difference worth documenting.

**v4.4 regression baseline — reproducibility intentionally broken vs. v4.3.** v4.4's wage-scale unification and CRN-pairing changes both change simulation output by design (see v4.4 Release Notes, above) — a given seed no longer reproduces v4.3's numeric output for the comparison scenarios, and the main scenario's own BLEI/Gini/wealth figures shift modestly too (the FBS-gate feedback described in Release Notes). Exact v4.4 seed-42 / Full Integration / 20yr values, alongside v4.3's for comparison:

| Metric | v4.3 | v4.4 |
|---|---|---|
| Median BLEI (final year) | 1,795 days | 1,951 days |
| BLEI Poverty (% Crisis+Precarious) | 18.6% | 13.6% |
| BLEI Threshold Rate (≥30d) | 81.4% | 86.4% |
| BLEI Stable Rate (≥120d) | 79.2% | 82.8% |
| BLEI Secure Rate (≥365d) | 74.6% | 74.8% |
| BLEI Flourishing Rate (≥730d) | 68.2% | 69.8% |
| Gini, EDC-adjusted | 0.521 | 0.535 |
| Median Wealth (final year) | $514,502 | $558,001 |
| Wealth Poverty Rate (<$25,000) | 20.6% | 16.6% |
| System Stability | 88.5% | 88.6% |
| Avg EDC | 25.4% | 24.9% |

If you're tracking a regression baseline across versions, restart it from v4.4 using the right-hand column — same guidance as prior version tables. Full derivation in `index.html`'s own changelog comment (search "v4.4").

**v4.5 update:** good-first-issues pass, not a mechanics-audit release — only one item (the PTH liquidity haircut) touches simulation output, and the movement is small. Seed-42 / Full Integration / 20yr: Median BLEI 1,951d→1,965d, Median wealth $558,001→$559,223, all other headline metrics unchanged to the precision reported — full table and the isolated-effect N=300 comparison in v4.5 Release Notes, above. If you're restarting a regression baseline from v4.5, use those v4.5 figures; the v4.3→v4.4 table above is retained for historical continuity, not as the current baseline.

**v4.4 large-N study — complete (Aug 2026).** Like v4.0, v4.2, and v4.3, this release changes core mechanics, so a full N=5,000 study was run (same methodology as prior large-N studies: a Node.js harness driving `makeLatentPopulation()`/`instantiateAgent()`/`runYear()`/`calcMetrics()`/`bleiMetrics()`/`structuralStability()` directly, seeds 1–5,000, 500 agents, 20 years, shock disabled to match the Full Integration reference preset; script available on request via a GitHub issue). Headline figures, with v4.3's for comparison:

| Metric | Full Integration (v4.4) | Full Integration (v4.3) | CCO Only (v4.4) | CCO Only (v4.3) | Baseline (v4.4) | Baseline (v4.3) |
|---|---|---|---|---|---|---|
| Median wealth, year 20 | $526,120 [CI $525,196–$527,044] | $495,411 | $391,742 [CI $390,856–$392,627] | $323,970 | **−$10,000 (100% of runs pinned)** | −$10,000 (>50% pinned) |
| Gini (EDC-adjusted net wealth) | 0.5183 [CI 0.5179–0.5187] | 0.5359 | 0.5763 [CI 0.5759–0.5768] | 0.6090 | 0.8580 | 0.8554 |
| BLEI poverty rate (Crisis+Precarious) | 12.5% [CI 12.5–12.6%] | 17.1% | 21.0% | 29.5% | 70.6% | 71.5% |
| BLEI Threshold rate (≥30 days) | 87.5% [CI 87.4–87.5%] | 82.9% | 79.0% | 70.5% | 29.4% | 28.5% |
| BLEI Stable rate (≥120 days) | 84.1% [CI 84.1–84.2%] | 79.7% | 75.1% | 67.9% | — | — |
| BLEI Secure rate (≥365 days) | 78.6% [CI 78.5–78.6%] | 74.6% | — | — | — | — |
| BLEI Flourishing rate (≥730 days) | 71.6% [CI 71.5–71.6%] | 67.8% | — | — | — | — |
| Median BLEI, final year | 1,824 days [CI 1,820–1,827] | 1,712 days | 1,175 days | 962 days | 7.5 days | 1.2 days |
| Wealth poverty rate (<$25,000) | 15.4% [CI 15.3–15.4%] | 19.5% | 24.1% | 31.3% | 71.6% | 72.3% |
| Avg EDC | 24.7% | 25.5% | 28.7% | 29.9% | 46.3% | 46.4% |
| Participant vs. non-participant poverty (wealth) | 10.0% vs. **34.3%** | 15.4% vs. 34.3% | — | — | — | — |
| System stability (structural metric) | 88.6% [CI 88.6–88.6%] | 88.6% | 88.4% | 88.7% | 99.0% | 99.0% |

95% CIs are on the *mean of each statistic across the 5,000 runs* (not per-agent spread within one run). **Read this table together with "What the v4.4 fixes actually do" in the Release Notes, above.** Two things worth flagging directly from this table: non-participant poverty is *exactly* unchanged at 34.3% (mechanistically expected — non-participants never execute the FBS-gated code path v4.4 changed, a clean internal-consistency check), and Baseline's median wealth is now confirmed pinned at the wealth floor in literally 100% of runs, up from v4.3's "more than half the population" — removing the ×0.85 haircut (Release Notes) didn't change this, because the binding constraint is the ongoing annual cost/wage gap, not the year-0 starting point.

**Near-poverty cohort tracking (agents with year-0 wealth < $25,000; 37.8% of the population under the v4.4 study, consistent with prior versions) — reconfirmed again under v4.4 mechanics:**

| Milestone | v4.2 (documented) | v4.3 (N=5,000) | v4.4 (N=5,000) |
|---|---|---|---|
| Threshold (≥30d), cohort median | immediate (month 0) | immediate (month 0) | immediate (month 0) — unaffected, as expected (initialization-state fact) |
| Stable (≥120d), cohort median | 158.8 months (13.2 yr) | 48 months (4.0 yr) | **36.0 months (3.0 yr)** [mean 38.6mo] |
| Secure (≥365d), cohort median | not tracked | 108 months (9.0 yr) | **104.9 months (8.7 yr)** [mean, median not materially different at this milestone] |
| Flourishing (≥730d), cohort median | not reached, 0/5,000 (20yr horizon) | reached, 5,000/5,000 (100%), within the 20yr horizon | **156.0 months (13.0 yr)** [mean 161.0mo], reached in 5,000/5,000 runs |

v4.4 continues the direction v4.3 established (this cohort is wealth-poor but not wage-poor, and the wage-scale corrections in both releases reward wage level specifically) — the milestones arrive modestly faster still, not a reversal of v4.3's finding. The v4.1 40-year extension study remains unreconfirmed under current mechanics (see What Did NOT Get Fixed, in v4.4 Release Notes, above) — now three mechanics-changing releases stale.

**Social-Security-anchored cohort study — updated for v4.4 (N=5,000).** Full table, methodology, and the v4.3 figures are under v4.3 Release Notes, above. v4.4's wage-scale unification (Release Notes) directly affects this study, since these cohorts are tagged by wage — updated figures, with a methodological correction:

| Cohort | Scenario | Wealth poverty | BLEI poverty | Median BLEI (median-of-medians) | Flourishing rate |
|---|---|---|---|---|---|
| SSI-level (0.8% of pop.) | Full Integration | 96.8% | 82.7% | 19.8d [mean 26.7d] | 1.4% |
| | Baseline | 99.8% | 99.8% | 1.9d | — |
| SSDI-level (7.7% of pop.) | Full Integration | 83.0% | 75.4% | 22.6d [mean 22.6d] | 8.1% |
| | Baseline | 99.7% | 99.7% | 3.0d | — |
| Retirement-level (17.1% of pop.) | Full Integration | 64.7% | 52.7% | 25.1d [mean 32.0d] | 14.5% |
| | Baseline | 99.6% | 99.6% | 3.7d | — |

**A methodological correction, caught before this table was published anywhere: report median-of-medians for these figures, not the mean.** BLEI is right-skewed (bounded below at 0, long right tail) and these cohorts are small (≈4–86 agents per 500-agent run) — a handful of high-BLEI seeds can pull the mean well above the typical outcome. The retirement-level cohort's mean (32.0d) sits above the 30-day Threshold line; its median-of-medians (25.1d) does not, and only **31.1% of individual seeds** (1,554/5,000) actually cross it — the typical case still falls short, even though it's the closest of the three anchors. Reporting the mean alone here would have overstated this cohort's typical outcome. The v4.3 table above should be read with the same caveat in mind, though the harness at the time did not separately capture median-of-medians for reconstruction here.

**Read plainly, updated for v4.4: Full Integration still helps this population enormously in relative terms, but the multiplier moved.** Originally measured at 20–30× the baseline's BLEI under v4.3 mechanics; recomputed at **~7–10×** under v4.4 (SSI 10.4×, SSDI 7.6×, Retirement 6.8×). This is not because Full Integration became less effective for this population — its absolute BLEI figures all improved — but because Baseline's own BLEI also rose under the corrected wage-buffer term (from ~0.5–1.1d to ~1.9–3.7d), since Baseline agents receive the same wage-derived BLEI correction with no CCO/PTF/PTH mechanism to compound it further. The qualitative finding is unchanged and, if anything, sharpened by the more careful median-of-medians reading: **this remains the sharpest test of the framework's poverty-elimination claim, and the framework does not pass it for the typical case in any of the three cohorts.**

*(Historical: for the v4.0/v4.1/v4.2/v4.3 regression tables and large-N methodology notes, see the version history preserved in this file's git log — trimmed here to keep this section from growing unbounded across releases; the pattern each entry follows is unchanged, so a future contributor extending this table has a template to match.)*

**A reproducibility caveat carried forward from prior sessions.** A single seed-42 run through a fresh harness may not reproduce a documented table bit-for-bit — expect it to land within about 1–3% on every metric, well inside normal seed-to-seed sampling noise at n=500, but not necessarily identical, most likely because `octaveShape`'s `beta(2,5)` draw uses rejection sampling whose last-bit rounding isn't guaranteed identical across JS engine versions. Aggregate statistics from the same harness at N=200+ should match documented large-N figures far more closely than any single seed will. This doesn't affect large-N study validity, which is inherently robust to single-seed variation.

### 4. Model Architecture Feedback

Areas currently open for discussion:

- **`WEALTH_FLOOR = −$10,000` needs reconsideration more urgently than when this was first flagged in v4.3.** The Traditional Welfare Baseline's median wealth now sits exactly at the wealth floor in **100% of N=5,000 runs** (v4.4 study, up from "more than half" at v4.3) — the floor is not an occasional insolvency case, it is the population's typical outcome. v4.4 confirmed removing an unrelated ×0.85 initial-wealth haircut (see v4.4 Release Notes) does not change this — the binding constraint is the ongoing annual cost/wage gap under 20 years of 3% CPI compounding, not the starting point, which rules out "fix the starting conditions" as a solution. Whether −$10,000 is still the right floor for a scenario with no offsetting mechanisms is a design decision for the framework's authors, not a code fix; this document cannot resolve it by further code changes alone.
- **`TARGET_WEALTH` ($82,000), `TARGET_POVERTY` (5%), and `TARGET_GINI` (0.25) are now considerably further from the model's actual output than when v4.3 first flagged them.** Full Integration's measured median wealth ($526,120 under v4.4) is now more than 6× the original target — a widening gap across two consecutive mechanics-changing releases, both legitimate unit-correctness fixes rather than the model drifting. v4.4 added a direct in-app disclosure on the affected KPI badges (Gini, Wealth, Stability, Flourishing, EDC) pointing back to this document, without picking new target values — that remains a framework-level decision for the authors, not something to update silently alongside a mechanics fix.
- **A mechanism specifically targeting low-*wage* (not just low-wealth) populations may be a gap the framework doesn't currently address.** The Social-Security-anchored cohort study (see v4.3/v4.4 Release Notes) found that Full Integration does not lift a low-wage cohort out of poverty by the model's own tier definitions in the typical case, for any of the three anchors, even though every existing mechanism (CCO, PTF, PTH) already applies to them equally — a finding that sharpened, not softened, under v4.4's more careful median-of-medians reading. Whether this points to a genuine mechanism gap (e.g., wage-conditional BU scaling, a floor-topping mechanism) or is an accurate reflection of the framework's actual design scope remains a substantive question for the framework's authors.
- **EDC-adjusted Gini vs. wealth-init spread — needs real Fed SCF *distributional* data** (not just the median already used for wealth init). Unresolved, unrelated to v4.3/v4.4's changes.
- **EDC baseline (rent-only)** — bottom income decile spends ~29% of pre-tax income on healthcare vs. ~3% top decile (BLS CE-based), a real additional extraction channel rent-only accounting misses. Confirmed as a gap; extending `agentEDC()` to a multi-channel model remains its own design task, not attempted in v4.3 or v4.4.
- **CCO conversion proceeds are tracked but not production-constrained.** BU→wealth conversion credits agents without debiting a modelled treasury, PTF balance sheet, or production account. v4.0 added transparency tracking only; v4.4 did not scope this. A genuine aggregate production constraint (production function, capacity limits, rationing behaviour) is a substantial economic-modelling contribution we'd welcome help scoping.
- **Initial PTF share is not a hard cap by default — resolved as an opt-in in v4.6.** The PTF slider sets the `t=0` adoption probability; per-agent adoption checks each year (Bass-diffusion imitation + SZH→PTF induction) previously meant realised final share could run well past the slider (uncapped, seed 42/20yr reaches 53.4% against an 18% slider) with no feedback loop constraining it. v4.6 adds an opt-in, off-by-default "Cap adoption at slider value" toggle that feedback-clamps both growth pathways once realised share reaches the slider value — see v4.6 Release Notes for the mechanism and its one caveat (it constrains organic growth, not t=0 sampling variance in the initial Bernoulli draw itself). Left off by default because making it the default would be a real behavioral change to every PTF-active preset, which is a framework-level calibration decision, not a bug fix — this document's authors have not decided whether the capped or uncapped behavior better reflects the intended "Initial PTF share" semantics for the *reference* configuration specifically.
- **Sobol/LHC sensitivity — implemented in v4.6.** An "LHS Sensitivity Export" button now ships (Latin Hypercube design over the same 5 parameters OAT varies, `mulberry32`-seeded, CSV export of the design matrix + outcome metrics) — see v4.6 Release Notes. This is explicitly an LHS design, not genuine Sobol indices (which need paired Saltelli sampling); external Sobol/Morris analysis in Python/R remains the recommended next step from the exported CSV, as it already was for OAT's own CSV export.
- **Long-horizon wealth growth appears unbounded — a new open question surfaced by the v4.6 40-year cohort rebuild.** Extending the near-poverty cohort study to 40 years (N=1,000, Full Integration — see v4.6 Release Notes for full figures) found no plateau in cohort or population-wide BLEI/wealth: population median wealth reaches roughly $2.12M by year 40, more than 4× its year-20 figure, with cohort median BLEI still climbing at an accelerating pace. The main wealth-accumulation loop has no explicit long-run ceiling — no retirement, no consumption floor that scales with wealth, no diminishing-returns term beyond the existing wage-growth dampening — so once an agent's annual surplus consistently exceeds cost, wealth compounds without an apparent bound over multi-decade horizons. Whether this needs a mechanism (e.g. a diminishing-returns term on conversion gains at high wealth, or simply documenting that the model is not intended for horizons past ~20–30 years) is a framework-level design question, not resolved here.
- **PTF distortion threshold (30% market share)** — searched, no clean literature citation exists for a cooperative-sector market-concentration threshold specifically. Genuine literature gap, not a research gap on our end — kept at 30%, comment reflects the gap honestly.
- **BLEI external validation** — Phase 4 roadmap: validate against Fed SCF, CPS, ACS, BLS CES, and OECD inequality trajectories. Not started.
- **PTH liquidity haircut is flat, not tenure-cohort-varying.** v4.3 added per-agent tenure *tracking* as a first step; the variable haircut formula itself (BLEI paper Table 1a: ~10–20% at 6 months rising to ~80–90% at 5+ years) is not implemented in v4.3 or v4.4. The tracking data is now flowing and exported, so this is closer to shippable than before. **Resolved in v4.5 — see Release Notes, above.**

- **λ Calibration Status — Open.** The BLEI paper's Index IV defines λ ~ U(0.001, 0.008), the FBS advancement-probability coefficient. Simulation v4.4 currently employs λ ~ U(0.0001654, 0.0013233), a behavioral recalibration adopted after the v4.4 wage-scale unification. **A dedicated sensitivity sweep** (N=500 seeds per variant, 500 agents/20 years, Full Integration reference config) tested the paper's original range against v4.4's range and 0.5×/2× variants:

  | λ variant | Median wealth | Gini | BLEI poverty | Secure rate | Flourishing rate | Stability | BU-mono (VAL_SEEDS) | P(advance) mean/median | % saturated (>0.95) |
  |---|---|---|---|---|---|---|---|---|---|
  | Paper (0.001–0.008) | $532,583 | 0.513 | 12.0% | 79.3% | 72.2% | 88.6% | 5/5 | 0.997 / 1.000 | **98.2%** |
  | v4.4 (0.0001654–0.0013233) | $524,282 | 0.518 | 12.6% | 78.6% | 71.5% | 88.6% | 5/5 | 0.883 / 0.946 | **49.0%** |
  | 0.5× v4.4 | $511,010 | 0.525 | 13.4% | 77.7% | 70.7% | 88.6% | 5/5 | 0.727 / 0.764 | **15.5%** |
  | 2× v4.4 | $530,400 | 0.515 | 12.3% | 79.0% | 72.0% | 88.6% | 5/5 | 0.963 / 0.997 | **82.0%** |

  **A correction to how this item was originally motivated.** The rescale was first triggered by a BU-monotonicity `VAL_TEST` regression (one seed, an exact tie at n=200) under the paper's original λ. Re-tested here after the gamma(1) sampler fix (below) — which changes RNG stream positions for every agent draw thereafter — that same tie no longer reproduces: **all four λ variants pass BU-monotonicity 5/5.** The original triggering signal was partly confounded by the separately-discovered gamma(1) bug, not purely a consequence of the wage-scale change alone — worth stating plainly rather than leaving the original (weaker) justification standing. The headline aggregate metrics (wealth, Gini, poverty, BLEI tiers, stability) also move only modestly across all four variants — FBS-gated advancement is one of several mechanisms feeding 20-year wealth outcomes, so even a large swing in advancement probability doesn't dominate the aggregate result.

  **What remains the real, robust justification: the saturation diagnostic itself**, not test pass/fail. The share of CCO participants with P(advance) > 0.95 falls monotonically and substantially across the swept range — 98.2% (paper) → 82.0% (2× v4.4) → 49.0% (v4.4) → 15.5% (0.5× v4.4) — a clean, seed-independent confirmation that the paper's published range leaves λ doing almost no differentiating work for the large majority of the population, regardless of any single regression test's outcome on any given seed set. This is the basis for keeping v4.4's range, not the (now-superseded) monotonicity signal.

  The revised range preserves the original 8× relative heterogeneity but should not itself be interpreted as an empirically estimated parameter — passing `VAL_TESTS` and this sweep demonstrates internal behavioral consistency, not real-world correctness of the absolute values. Empirical calibration of the advancement function against observed entrepreneurial-entry, mobility, or debt-resolution data as a function of residual financial bandwidth remains an open research objective — as does a longer-term reparameterization by half-saturation point (FBS₅₀ = ln(2)/λ, an explicit reference bandwidth at which a median-capability agent has even odds of advancing) rather than a raw 1/USD coefficient, which would make the calibration's behavioral assumptions far easier for a reviewer to interrogate directly. The BLEI paper itself has not been rewritten to match — it retains λ ~ U(0.001, 0.008) as its published theoretical specification, with an added note at Index IV explaining the simulation's current operational divergence and why.

  **v4.6 update:** the FBS₅₀ figure this note describes is now a named, computed constant (`CFG.FBS_HALF_SAT_LO/HI`, ≈$524–$4,191/month) rather than only a hand-computed number in this prose, and is displayed directly in the interactive tool's Assumptions panel — see v4.6 Release Notes. This is a reporting change only; it does not itself perform the "reparameterize by sampling FBS₅₀" idea described above, which remains open, since doing so would change the shape of the λ distribution and need its own validation pass.

**Resolved in v4.4** (tracked here previously as open items — see v4.4 Release Notes for full detail): the dual wage/income scale across BLEI/FBS/Gini vs. the main wealth loop; the lack of true common-random-numbers pairing across the Baseline/CCO-Only/Main trajectory comparison (population-level pairing only, since v4.2); the baseline scenario's undocumented ×0.85 initial-wealth haircut; the baseline scenario's exemption from automation exposure even when the tested scenario enables it.

**Resolved in v4.6** (tracked here previously as open items — see v4.6 Release Notes for full detail): the Sobol/LHC sensitivity export spec, now shipped as an LHS design + CSV export; the near-poverty cohort's stale 40-year extension, rebuilt under current mechanics; "Initial PTF share is not a hard cap," now addressable via an opt-in, off-by-default toggle (the underlying default-off behavior is unchanged — see that item's entry, above, for why it isn't the new default). Occupation-stratified automationRisk and the `LIVING_WAGE_ANNUAL` population-weighting caveat both remain open but are now more precisely scoped after this session's research — see Good First Issues.

### 5. Code Contributions

The simulation is a single HTML file with no build tooling — runs directly from any browser, easily auditable, and archivable. Please maintain this constraint.

**Before submitting a pull request:**

- Test in Chrome, Firefox, and Safari
- Ensure seeded RNG produces identical output before and after your change, for a fixed configuration (seed `42`, Full Integration, 20 years — record Median BLEI, BLEI Poverty, and Gini as regression metrics) — unless your change is intentionally a mechanics fix, in which case say so explicitly in the PR
- Do not introduce external dependencies beyond the existing Chart.js CDN
- Follow existing code style: vanilla JS, CSS variables, inline documentation, `CFG` object for all calibration constants

**Good first issues:**

- Occupation-*stratified* (not just bimodal) automationRisk — **now scoped, not just aspirational.** Searched this session: Frey & Osborne (2013) itself publishes the needed data — a full table of computerisation probability by SOC-2010 occupation code for all 702 occupations, in the paper's own appendix (pp. 57–72, freely available as an Oxford Martin School working paper PDF). What's actually missing is not the probability data but (a) transcribing that ~702-row table into a machine-readable crosswalk (it exists only as a PDF table, not a published CSV), (b) a SOC-2010→current BLS OES crosswalk to get employment-share weights per occupation, and (c) a decision on how agents map to occupations (e.g., draw an occupation per agent weighted by its BLS employment share, then assign that occupation's F&O probability as `automationRisk`, replacing the current Beta(6,1)/Beta(1,6) approximation). This is real data-transcription/crosswalk work, not a modeling judgment call — a good candidate for a contributor with the appendix and BLS OES tables open side by side.
- Implement the Sobol/LHC sensitivity export (spec above) — **done in v4.6, see Release Notes.**
- Rebuild the near-poverty cohort's v4.1 40-year extension study under current mechanics — **done in v4.6, see Release Notes** (the original v4.1 question is moot post-v4.3, but the rebuild surfaced a new open question about unbounded long-horizon wealth growth — see Model Architecture Feedback).
- `LIVING_WAGE_ANNUAL`'s population-weighting caveat — searched this session for a single published population-weighted national figure from MIT's Living Wage Calculator to replace the current unweighted 51-jurisdiction average. None found: MIT's calculator is a location-by-location lookup tool (state/county/metro) with no published single national aggregate, weighted or otherwise — confirmed via web search, not assumed. The unweighted average therefore remains the best available approach; genuinely computing a population-weighted version would mean pulling all ~50 state-level (or finer) figures with Census population weights directly, a bigger data-assembly task than this note anticipated. Still open.
- **Done in v4.6** (see Release Notes, above): Latin Hypercube sensitivity export; opt-in feedback-clamped PTF adoption cap (Model Architecture Feedback item); FBS₅₀ half-saturation bandwidth exposed as a derived, named constant; near-poverty cohort's 40-year extension rebuilt under current mechanics
- **Done in v4.5** (see Release Notes, above): implemented the variable tenure-cohort PTH liquidity haircut; "Copy parameters as URL"; surfaced the Social Security-anchored cohort study as an in-app stratification; i-buttons on BLEI tier labels; preset-button description tooltips
- **Done in v4.4** (see Release Notes, above): unified wage/income scale across BLEI/FBS/Gini onto `WAGE_TO_USD`, with a compensating `FBS_LAMBDA` rescale; true common-random-numbers pairing across the Baseline/CCO-Only/Main trajectory comparison; removed the baseline's undocumented ×0.85 initial-wealth haircut; paired automation exposure across scenarios; fixed a `gamma(a=1)` sampler bug (silently returned a constant, ~200× population-construction speedup as a side effect); renamed the non-participant validation check for accuracy (string-only, logic unchanged); added in-app KPI-badge disclosures for the System Stability flat-outcome reading and the pending `TARGET_*` recalibration
- **Done in v4.3** (see Release Notes, above): occupation-stratified/bimodal automationRisk; `runYear()` RNG-coupling fix, allowing the non-participant validation check to tighten back to strict per-seed agreement at n=200
- **Done in v4.2** (see v4.2 Release Notes, above): a structural System Stability metric, `structuralStability()`, replacing the former trend-plus-noise heuristic

### 6. Academic Peer Review

Researchers are invited to review the primary papers and submit formal comments:

- **BLEI Paper**: [bettertobest.github.io/research-hub/basic-living-economic-index.html](https://bettertobest.github.io/research-hub/basic-living-economic-index.html)
- **Replication Framework**: [bettertobest.github.io/research-hub/cco-ptf-simulation-replication.html](https://bettertobest.github.io/research-hub/cco-ptf-simulation-replication.html)
- **Academia.edu**: [independentresearcher.academia.edu/DukeJohnson](https://independentresearcher.academia.edu/DukeJohnson)

Submit review comments as GitHub issues with prefix `review:`.

---

## Issue Labels

| Label | Use for |
|---|---|
| `calibration:` | Proposing updates to CFG constants with cited sources |
| `architecture:` | Model design questions and mechanism gaps |
| `review:` | Academic peer review comments |
| `bug:` | Reproducibility failures or calculation errors |
| `enhancement:` | New features or UX improvements |
| `data:` | Real-world scenario results and comparisons |

---

## A Note on Stochastic Variance

Each simulation run without a fixed seed produces slightly different results — this is correct behaviour, not a bug. It reflects genuine Monte Carlo variance across the agent population. When reporting results, either:

1. Use a fixed seed (record it in your CSV/JSON export), or
2. Run multiple unseeded trials using **Run 10×** or **Run 50×** (labeled "Stochastic CI" as of v4.0) and report mean ± 95% CI

Note that this CI describes the spread of the simulation's own stochastic output when parameters are held fixed and only the RNG seed varies — it is not a full uncertainty interval, and it does not include calibration, parameter, or structural uncertainty (relabeled from "Publication CI" in v4.0 for exactly this reason).

The page loads automatically with seed 42 / Full Integration as an **illustrative reference run** — clearly labeled as such. All published comparisons should specify the seed used and, given the v4.0/v4.3 mechanics changes, the simulation version.

---

## Contact

- **Email**: BetterToBestResearch@gmail.com
- **Hub**: [BetterToBest.github.io/research-hub](https://BetterToBest.github.io/research-hub/)
- **Bluesky**: [@authordukejohnson.bsky.social](https://bsky.app/profile/authordukejohnson.bsky.social)

---

## License

All contributions are released under **CC BY 4.0**. Attribution to the Better To Best Research Hub is required. By submitting a contribution, you agree to these terms.

---

*Better To Best Research Hub · Compassionism Framework Simulation v4.6*  
*Principal Investigator: Duke Johnson (pseudonymous)*
