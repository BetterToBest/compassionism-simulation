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
| `SIM_COST_SCALE` | 1,500 (SIU) | ABM calibration | **v4.0 scope note:** this now drives *only* the main wealth-accumulation loop, kept at its pre-v4.0 value deliberately (see "Main wealth-accumulation loop" under Model Architecture Feedback, below). BLEI/FBS/Gini use `SIU_TO_USD` instead (next row). Pilot data on real PTF pricing relative to market would still improve it. |
| `SIU_TO_USD` | ≈16.63 (derived: `BASE_DAILY_COST×365 / SIM_COST_SCALE`) | Derived, v4.0 | **New in v4.0.** Converts wage (SIU) to USD for BLEI, FBS, and EDC-adjusted-Gini only — not the main wealth loop. Derived so it reproduces the pre-v4.0 operative ratio at those call sites; not independently validated against real income data. A joint recalibration (see below) would supersede it. |
| `WAGE_MEDIAN_SIU` | 35 SIU | Framework spec | Cross-scenario calibration; also now the anchor point for `agentEDC()`'s rescaled saturation constants (v4.0) |
| `FBS_LAMBDA_LO/HI` | 0.001 / 0.008 | BLEI paper §Index IV (λ ~ Uniform) | **New in v4.0** (formula was previously unimplemented). Direct from framework spec — empirical grounding for the range itself is still open. |
| `FBS_EDC_RESIDUAL_BASE/PTH` | 0.12 / 0.025 | BLEI paper Table 1b worked values | **New in v4.0.** Used as a fixed proxy for "consumer debt interest only" — a separately-modelled consumer-debt submodel would be more accurate. |
| `PTH_EQUITY_CONTRIB_SHARE` | 25% | **Internal design choice, not externally sourced** | **New in v4.0.** Share of PTH's annual housing-cost saving that routes to Acre Equity vs. staying as direct liquid relief. Loosely modelled on typical CLT shared-equity resale formulas but not fit to a specific one — a priority calibration item. |
| `SZH_THETA_THRESHOLD/MAX_COH/MAX` | 0.55 / 0.90 / 0.25 | BLEI paper Table 6 (synergy coefficient θ) | **New in v4.0** (was previously unimplemented — see Model Architecture Feedback). Direct from framework spec. |
| `PTF_BASS_Q` | 0.05 | **Internal design choice, not externally sourced** | **New in v4.0.** Bass (1969) imitation coefficient for PTF adoption. The ODD protocol has always described diffusion-driven adoption; this is a first implementation, not a validated estimate — classic Bass-model literature estimates are often higher (q≈0.3–0.5), chosen conservatively here to avoid destabilizing existing calibration. Worth revisiting with real cooperative-sector adoption-curve data. |
| `BASELINE_CPI_RATE` | 3% | Historic US CPI | **New in v4.0.** Baseline scenario's inflation is now anchored to this fixed rate instead of copying the user's inflation slider — see Model Architecture Feedback. |
| `automationRisk` distribution | uniform[0.2,1.0] | Simplifying assumption | **Priority item (flagged since v3.4, still open in v4.0):** Real exposure is bimodal/occupation-dependent (Frey & Osborne, 2013; Autor, 2015). Contributions implementing occupation-stratified risk distributions are especially welcome. |

To propose a calibration update, open an issue with prefix `calibration:`, your proposed value, full citation, and a before/after output comparison.

### 3. Reproducibility Testing

The simulation supports seeded runs (Mulberry32 PRNG). To verify a result:

1. Note the **Random seed** and all parameter values from the exported CSV or JSON
2. Enter the same seed and parameters in the simulation
3. Confirm the output matches

If results diverge under identical seed + parameters, open a bug report with both exports. This should not happen — if it does, it indicates a browser environment difference worth documenting.

**v4.0 regression baseline:** use seed `42`, Full Integration preset, 20 years. **v4.0 does *not* produce the same numerical output as v3.9 or earlier — this is expected.** v4.0 changes core mechanics (FBS-gated advancement, octave-governed conversion capacity, PTH equity contributions, network-density-gated SZH synergy, Bass-diffusion PTF adoption, EDC-adjusted Gini) by design, per an external technical review ([Refine.ink, Aug 2026](https://www.refine.ink/app/session/4e84aa99-44ff-438f-9382-719bf9714344)). Prior versions' regression baselines (v3.3 through v3.9) remain valid *among themselves* but are not comparable to v4.0 output. Exact v4.0 seed-42 values, for your own reproducibility check:

| Metric | Value |
|---|---|
| Median BLEI (final year) | 284 days |
| BLEI Poverty (% Crisis+Precarious) | 9.0% |
| BLEI Threshold Rate (≥30d) | 91.0% |
| BLEI Stable Rate (≥120d) | 78.2% |
| BLEI Secure Rate (≥365d) | 35.4% |
| BLEI Flourishing Rate (≥730d) | 13.0% |
| Gini, EDC-adjusted | 0.482 |
| Gini, nominal wealth | 0.470 |
| Median Wealth (final year) | $78,813 |
| Wealth Poverty Rate (<$25,000) | 16.2% |

These are for the exact seed that auto-loads on page open — a single run, not an average, so expect it to sit within (not exactly at) the large-N study's confidence intervals below. If you're tracking a regression baseline across versions, start a fresh one from v4.0 using this table.

**v4.0 large-N study (new).** The companion replication document's headline statistics (BLEI Threshold/Stable/Secure/Flourishing rates, Gini, System Stability, wealth, and milestone-crossing times) were refreshed under v4.0 mechanics via 5,000 independent seeded runs each of Full Integration, CCO-Only, and Traditional Welfare Baseline (seeds 1–5,000, 500 agents, 20 years). Full methodology and results are in the replication document's Performance Comparison section. One finding worth flagging here specifically: the near-poverty cohort's *median* member does not reach the Flourishing tier (≥730 days) within the 20-year reference horizon in any of the 5,000 runs, now that advancement is genuinely FBS-gated — this superseded the pre-v4.0 "~33 months to Flourishing" figure, which was generated under the old fixed-probability advancement heuristic. If you re-run this study (e.g. to extend the horizon past 20 years and see whether/when the median near-poverty agent eventually crosses Flourishing), we'd welcome the data as a `data:`-labeled issue.

### 4. Model Architecture Feedback

Areas currently open for discussion:

- **Main wealth-accumulation loop keeps its pre-v4.0 unit simplification (highest-priority open item).** v4.0 fixed a wage(SIU)/wealth(USD) unit mismatch in BLEI, FBS, and Gini, but deliberately left the core annual wealth update unchanged: wage and living cost are still combined in native SIU-scale terms via `SIM_COST_SCALE`, not real USD. We built and tested a version that also converts this loop to USD; because wage compounds against cost over up to 30 years, it turned out to be extremely sensitive to the conversion constant — a ~3.5× range of candidate values swung 20-year outcomes from universal wealth-floor collapse (68%+ poverty in every scenario) to implausible multi-million-dollar median wealth. A defensible fix needs a **joint recalibration** of the wage distribution (`lognormal(3.5, 0.5)`), the cost scale, and every `TARGET_*` constant against real income data — not a single conversion constant chosen in isolation. This is likely the single most valuable contribution area for anyone with income-distribution modeling experience.
- **EDC-adjusted Gini vs. wealth-initialization spread (new in v4.0).** Now that EDC-adjusted Gini is actually computed (previously specified but unimplemented), measured output at the reference configuration (≈0.45–0.48 full deployment, ≈0.73–0.77 baseline) is meaningfully higher than the framework's earlier aspirational target (0.22 full / 0.44–0.46 baseline). The likely cause: `wealth ~ lognormal(10.5, 1.2)` alone has an inherent Gini coefficient of ≈0.60 *before any simulation dynamics or EDC adjustment* — already above the old baseline target. Two possible resolutions: narrow the wealth-initialization spread (lower σ), or revise the target. Either requires deciding what population the initialization is meant to represent and grounding σ in that choice — not just picking a number that hits the target.
- **PTH liquidity haircut is flat, not tenure-cohort-varying.** v4.0 added the "payments build equity" contribution mechanism to Acre Equity, but the *withdrawal haircut* is still a flat 50%, not the tenure-varying schedule (~10–20% at 6 months rising to ~80–90% at 5+ years) sketched in the BLEI paper's Table 1a. Implementing a real tenure-tracking mechanism (agents don't currently record how long they've held PTH residency) would close this gap.
- **PTH_EQUITY_CONTRIB_SHARE (25%) and PTF_BASS_Q (0.05) are internal design choices, not fitted values.** See the Calibration Validation table above — both are new in v4.0 and were chosen conservatively to implement the documented mechanism without over-tuning; neither is validated against real shared-equity-housing or cooperative-adoption data.
- **CCO conversion proceeds are tracked but not production-constrained.** BU→wealth conversion credits agents without debiting a modelled treasury, PTF balance sheet, or production account — an external review correctly flagged this as an open stock-flow accounting gap. v4.0 adds transparency only (cumulative conversion proceeds are tracked and exported in CSV/JSON). Designing a genuine aggregate production constraint — a production function, capacity limits, and rationing behaviour when exhausted — is a substantial economic-modelling contribution we'd welcome help scoping, not just implementing.
- **System Stability is still a trend heuristic, not a structural metric.** Flagged since v3.6, scoped for v4.0, not implemented in v4.0 (that release prioritised the external review's findings instead). The displayed value (`stabBase` by poverty-trend direction + CIP bonus + bounded noise) is not derived from wealth variance, BLEI volatility, or agent-state transitions. A structural replacement — e.g. coefficient of variation of median wealth over the final years, or share of agents remaining in the same BLEI tier for 3+ consecutive years — remains open.
- **Initial PTF share is not a hard cap.** The PTF slider sets the `t=0` adoption probability only; per-agent adoption checks each year (now including the v4.0 Bass-diffusion imitation term) mean the realised final share can exceed the slider value with no aggregate feedback loop constraining it. A quota-based or feedback-clamped adoption model remains open.
- **EDC baseline** — Rent is the dominant extraction channel. Does this adequately represent consumer debt, healthcare, and other extraction vectors?
- **PTF distortion threshold** — 30% market share. What empirical evidence exists for cooperative sector concentration limits?
- **automationRisk distribution** — Currently uniform[0.2,1.0]. Real automation exposure is bimodal: routine-manual workers at high risk, cognitive workers at low risk (Frey & Osborne, 2013; Autor, 2015). Contributions implementing occupation-stratified or bimodal distributions would significantly improve High Automation scenario plausibility.
- **Sobol/LHC sensitivity** — the simulation computes OAT sensitivity from mini-simulations (v4.0: uniformly ±20% of each parameter's own slider range). Contributions implementing Sobol indices or Latin hypercube sampling via CSV export are especially welcome.
- **BLEI external validation** — Phase 4 roadmap: validate against Fed SCF, CPS, ACS, BLS CES, and OECD inequality trajectories.
- **Participant stratification** — tracks CCO participant vs. non-participant welfare. Contributions testing whether non-participant poverty worsens under specific parameter combinations would strengthen the equity argument.
- **Large-N study now v4.0-native (done, Aug 2026) — but only at a 20-year horizon.** The companion replication document's headline statistics were refreshed via 5,000 seeded runs under v4.0 mechanics (see the Reproducibility Testing section above). One open follow-up: the near-poverty cohort's median member doesn't reach Flourishing within that 20-year window — extending the study to a longer horizon (30–40 years) to see whether/when it eventually does, and whether that's a reasonable timeframe to expect in the first place, is a well-scoped, concrete contribution.

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
- Extend the validation suite: fifth check — non-participant poverty does not worsen when CCO is enabled
- Implement occupation-stratified automationRisk distribution (see architecture discussion above)
- Add per-agent PTH tenure tracking as a first step toward the tenure-cohort liquidity haircut (see architecture discussion above)
- Implement a structural System Stability metric to replace the current trend-plus-noise heuristic (see architecture discussion above)

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

The page loads automatically with seed 42 / Full Integration as an **illustrative reference run** — clearly labeled as such. All published comparisons should specify the seed used and, given the v4.0 mechanics changes, the simulation version.

---

## Contact

- **Email**: BetterToBestResearch@gmail.com
- **Hub**: [BetterToBest.github.io/research-hub](https://BetterToBest.github.io/research-hub/)
- **Bluesky**: [@authordukejohnson.bsky.social](https://bsky.app/profile/authordukejohnson.bsky.social)

---

## License

All contributions are released under **CC BY 4.0**. Attribution to the Better To Best Research Hub is required. By submitting a contribution, you agree to these terms.

---

*Better To Best Research Hub · Compassionism Framework Simulation v4.0*  
*Principal Investigator: Duke Johnson (pseudonymous)*
