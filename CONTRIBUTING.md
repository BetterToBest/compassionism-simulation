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

## v4.4 Release Notes

v4.4 is a mechanics-changing release, and the first shipped only after putting the prior release through two independent adversarial code audits rather than trusting internal validation alone — this document's own account of the v4.0-v4.3 history is a record of real bugs slipping through multiple prior passes, so an audit step is now the default before further mechanics changes to a published research artifact, not a formality.

**The audit process.** First pass: an open-weight model (Qwen3-Coder-30B-A3B-Instruct) orchestrated via RunPod Serverless, given an explicitly skeptical prompt instructing it not to assume anything was correct. It returned seven structured, plausible-looking findings. Every one was independently re-verified against the actual code and **rejected as a false positive** — a self-contradicting RNG-stream claim that named no actual conditional draw, a misread of an existing `Math.max` guard, a misunderstanding of the documented PTH-equity accounting, among others. None were applied. Second pass: a more rigorous review returned twelve findings; most held up under the same direct-code verification this time. Four were judged substantive and consequential enough to implement as a real mechanics-changing release rather than a quiet patch — the four items below.

- **Wage/income scale unified across BLEI, FBS, and Gini.** v4.0 fixed unit-mixing inside these formulas using `SIU_TO_USD` (≈16.63) — a cost-side-derived approximation, invented because no real wage-side dollar anchor existed at the time. v4.3's `WAGE_TO_USD` (≈100.52, Census/BLS-sourced) was scoped to the main wealth loop only, leaving the same agent's wage worth roughly $3,518/month for wealth accumulation and roughly $582/month for welfare measurement simultaneously — a ~6× divergence the second audit correctly identified as no longer defensible once one anchor is empirically grounded and the other isn't. `SIU_TO_USD` is **retired**. `agentBLEI()`'s income-buffer term, `calcBLEIComponents()`, the FBS gate's `Yusd`, and the EDC-adjusted-Gini calculation now all use `WAGE_TO_USD`. `agentEDC()` was and remains unaffected — it's a dimensionless SIU/SIU ratio that never touched either constant.

- **`FBS_LAMBDA` recalibrated — a necessary consequence of the above, not a separate judgment call.** `λ`'s units are literally 1/USD by its own original code comment; once its dominant input (`Yusd`) grew ~6× under the wage-scale fix, `λ` left unscaled pushed octave-advancement probability toward saturation regardless of BU level, measurably weakening the BU-monotonicity `VAL_TEST` (one seed dropped from a clean win to an exact tie at n=200). Rescaled ÷6.0456 — the precise `WAGE_TO_USD`/legacy-`SIU_TO_USD` ratio, not a fitted number — from 0.001/0.008 to 0.0001654/0.0013233, preserving the 8× HI/LO heterogeneity shape. All six `VAL_TESTS` pass 5/5 post-change.

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

- **Per-agent PTH tenure tracking (first step, not the full fix).** Agents now carry `pthTenure` (years held in PTH residency), incremented each year while in PTH and reset on exit. This is tracking data only — the variable tenure-cohort liquidity haircut itself (BLEI paper Table 1a) is not implemented this pass; the flat 50% haircut is unchanged. Tracked as a Good First Issue, below.

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
| `LIVING_WAGE_ANNUAL` | $49,370 | World Population Review's MIT-sourced state living-wage table, single adult/no children, 51-jurisdiction *unweighted* average ($23.735/hr × 2,080 hrs/yr) | **New in v4.3, highest-priority remaining calibration item.** Not population-weighted like MIT's own paid Living Wage Calculator product (large-population states span both directions — CA $30.48/hr and NY $29.89/hr are high, TX $21.77/hr and FL $24.09/hr are more moderate — so a population-weighted figure is unlikely to shift dramatically, but this is unverified). Access to MIT's actual population-weighted figure would settle this. |
| `SS_ANCHOR_SSI_ANNUAL` / `SS_ANCHOR_SSDI_ANNUAL` / `SS_ANCHOR_RETIRE_ANNUAL` | $11,928 / $19,560 / $24,852 | SSA 2026 COLA Fact Sheet (ssa.gov/news/en/cola/factsheets/2026.html) | **New in v4.3.** Reference points for the Social-Security-anchored cohort study (see v4.3 Release Notes). Annual figures; update on each year's COLA Fact Sheet publication to keep current. Cohort tagging now uses `WAGE_TO_USD` for the SIU conversion as of v4.4 (unchanged in practice — the SS-anchor cohorts already used `WAGE_TO_USD` for this purpose since their v4.3 introduction; only BLEI/FBS/Gini's *own* internal formulas changed anchor in v4.4). |
| `WAGE_MEDIAN_SIU` | 35 SIU | Framework spec | Cross-scenario calibration; also the anchor point for `agentEDC()`'s rescaled saturation constants (v4.0) |
| `FBS_LAMBDA_LO/HI` | **0.0001654 / 0.0013233 (v4.4)** — was 0.001 / 0.008 through v4.3 | BLEI paper §Index IV (λ ~ Uniform), rescaled v4.4 | **v4.4: rescaled ÷6.0456 (the exact `WAGE_TO_USD`/legacy-`SIU_TO_USD` ratio), a dimensionally-necessary consequence of λ's own 1/USD units once `Yusd` — one of the FBS gate's dominant inputs — moved onto `WAGE_TO_USD`. Not a re-derivation from the paper spec; the underlying range's empirical grounding is still open, unchanged from pre-v4.4.** |
| `FBS_EDC_RESIDUAL_BASE/PTH` | 0.12 / 0.025 | BLEI paper Table 1b worked values | Used as a fixed proxy for "consumer debt interest only" — a separately-modelled consumer-debt submodel would be more accurate. |
| `PTH_EQUITY_CONTRIB_SHARE` | 25% | Internal design choice, not externally sourced | Matches Champlain Housing Trust's real resale-appreciation share exactly, but that's a coincidental number match, not a mechanistic validation — CHT's 25% is a one-time resale split; the sim's is an ongoing annual savings-to-equity routing. Kept at 25%; code comment reflects this is coincidental, not sourced. |
| `SZH_THETA_THRESHOLD/MAX_COH/MAX` | 0.55 / 0.90 / 0.25 | BLEI paper Table 6 (synergy coefficient θ) | Direct from framework spec. |
| `PTF_BASS_Q` | 0.05 | Internal design choice, not externally sourced | No cooperative-sector-specific citation exists (searched). General product-diffusion q typically 0.3–0.5, real-world q spans 0.05–0.47 across contexts in the literature. 0.05 isn't contradicted, isn't positively sourced either — kept, comment reflects the honest gap rather than implying a citation exists. |
| `BASELINE_CPI_RATE` | 3% | Historic US CPI | Baseline scenario's inflation is anchored to this fixed rate instead of copying the user's inflation slider — see Model Architecture Feedback. |
| `automationRisk` distribution | 47%/53% bimodal Beta(6,1)/Beta(1,6) | Frey & Osborne (2013)/Autor (2015) | **Resolved in v4.3** — was uniform[0.2,1.0], flagged since v3.4. Occupation-stratified (not just bimodal) risk would be a further refinement. **v4.4 note:** the underlying `gamma(a=1)` sampler this distribution's low-risk component depends on had a real bug (silently returned a constant instead of a random draw) — fixed in v4.4, see Release Notes; the *distribution choice itself* (bimodal, these sources) is unaffected and unchanged. |

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
- **Initial PTF share is not a hard cap.** The PTF slider sets the `t=0` adoption probability only; per-agent adoption checks each year (including the Bass-diffusion imitation term) mean the realised final share can exceed the slider value with no aggregate feedback loop constraining it. A quota-based or feedback-clamped adoption model remains open.
- **PTF distortion threshold (30% market share)** — searched, no clean literature citation exists for a cooperative-sector market-concentration threshold specifically. Genuine literature gap, not a research gap on our end — kept at 30%, comment reflects the gap honestly.
- **Sobol/LHC sensitivity** — implementation-ready spec exists (an "LHS Sensitivity Export" button: Latin Hypercube Sample design over the same 5 parameters OAT already varies, reusing the existing `mulberry32` RNG, exporting the design matrix + outcome metrics as CSV). Not yet implemented; a good next PR for someone comfortable with the existing OAT code path.
- **BLEI external validation** — Phase 4 roadmap: validate against Fed SCF, CPS, ACS, BLS CES, and OECD inequality trajectories. Not started.
- **PTH liquidity haircut is flat, not tenure-cohort-varying.** v4.3 added per-agent tenure *tracking* as a first step; the variable haircut formula itself (BLEI paper Table 1a: ~10–20% at 6 months rising to ~80–90% at 5+ years) is not implemented in v4.3 or v4.4. The tracking data is now flowing and exported, so this is closer to shippable than before.

**Resolved in v4.4** (tracked here previously as open items — see v4.4 Release Notes for full detail): the dual wage/income scale across BLEI/FBS/Gini vs. the main wealth loop; the lack of true common-random-numbers pairing across the Baseline/CCO-Only/Main trajectory comparison (population-level pairing only, since v4.2); the baseline scenario's undocumented ×0.85 initial-wealth haircut; the baseline scenario's exemption from automation exposure even when the tested scenario enables it.

### 5. Code Contributions

The simulation is a single HTML file with no build tooling — runs directly from any browser, easily auditable, and archivable. Please maintain this constraint.

**Before submitting a pull request:**

- Test in Chrome, Firefox, and Safari
- Ensure seeded RNG produces identical output before and after your change, for a fixed configuration (seed `42`, Full Integration, 20 years — record Median BLEI, BLEI Poverty, and Gini as regression metrics) — unless your change is intentionally a mechanics fix, in which case say so explicitly in the PR
- Do not introduce external dependencies beyond the existing Chart.js CDN
- Follow existing code style: vanilla JS, CSS variables, inline documentation, `CFG` object for all calibration constants

**Good first issues:**

- Add a "Copy parameters as URL" feature so scenarios can be shared as links
- Add i-buttons next to BLEI tier labels showing tier definitions inline
- Add preset descriptions as tooltips on preset buttons
- Implement the variable tenure-cohort PTH liquidity haircut now that per-agent tenure tracking is in place (v4.3) — see Model Architecture Feedback
- Implement the Sobol/LHC sensitivity export (spec above)
- Surface the Social-Security-anchored cohort study as an in-app stratification (analogous to the existing participant/non-participant charts), rather than harness-only — the constants and methodology are established (v4.3), this would make the finding visible to anyone using the interactive tool, not just readers of this file
- Occupation-*stratified* (not just bimodal) automationRisk would be a further refinement beyond v4.3's fix
- Rebuild the near-poverty cohort's v4.1 40-year extension study under current (v4.4) mechanics — unreconfirmed since v4.1, now three mechanics-changing releases stale, and the 20-year figures have moved enough that the 40-year result is very likely materially different
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

*Better To Best Research Hub · Compassionism Framework Simulation v4.4*  
*Principal Investigator: Duke Johnson (pseudonymous)*
