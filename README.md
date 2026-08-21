# Compassionism Framework Simulation

A research-oriented, browser-based agent-based simulation exploring all five [Compassionism](https://bettertobest.github.io/research-hub/) architectures for comparative policy analysis — no installation required. BLEI-calibrated against 2023 US Consumer Expenditure Survey data.

**[▶ Open the simulation](https://bettertobest.github.io/compassionism-simulation/)** · DOI: [10.17605/OSF.IO/QWTE2](https://doi.org/10.17605/OSF.IO/QWTE2)

---

## What's new since v3.3 (now v4.2)

- **FBS-gated octave advancement** — advancement probability is now driven by each agent's Financial Bandwidth Score, `P(advance) = 1 − exp(−λ·FBS)` with `λ ~ U(0.001, 0.008)` per agent, replacing a fixed BLEI-based probability; an agent at FBS = 0 can no longer advance regardless of quality. Octave itself now also governs CCO conversion-rate *capacity* — previously it played no role in conversion at all (v4.0)
- **Common-random-numbers population pairing** — the main run and its "CCO Only"/baseline comparisons now share one canonically-drawn latent population instead of three independent samples, closing a comparability gap external review flagged. Also fixed an independently-found bug where short-circuit eligibility draws made same-seed runs silently diverge once toggle states differed. Reconfirmed with a fresh N=5,000 large-N study (see Output metrics) — changes the RNG sequence, so v4.2 seeds don't reproduce v4.1 numeric output (v4.2)
- **Structural System Stability metric** — replaces the earlier trend-plus-noise heuristic (`improving ? 0.88 : 0.60` + random noise) with the inverse coefficient of variation of median wealth and BLEI over the run's final quarter — an endogenous, non-random measurement (v4.2)
- **6-check validation suite, multi-seed** — the original four checks now run across five seeds and require unanimous agreement; two checks added (a non-participant-poverty isolation check, a structural-invariants regression check); renamed "Internal Consistency & Behavioral Test Suite" and scoped explicitly to ODD validation Levels 1–3 (v4.2)
- **PTH Acre Equity now has three distinct benefits** — housing-cost reduction (35%), a 25% share of that saving routed into Acre Equity (the "payments build equity" mechanism, previously appreciation-only), and appreciation itself (~4%/yr, 50% liquidity haircut at exit) (v4.0)
- **SZH synergy gated by zone coherence** — the θ synergy coefficient is now 0 below 55% Zone Coherence Index, scaling linearly to 0.25 at 90%+, instead of applying linearly at every coherence level (v4.0)
- **Unit-consistent BLEI, FBS & Gini** — wage (SIU) is now converted to real USD via a derived constant (`SIU_TO_USD ≈ 16.6`) before mixing with dollar-valued terms in BLEI, the new FBS gate, and the Gini calculation, which is now computed on EDC-adjusted net wealth. The main wealth-accumulation loop deliberately keeps its pre-v4.0 unit convention — a full fix proved dangerously sensitive to the conversion constant over multi-decade runs; see Known Limitations in-app (v4.0)
- **Independently-isolated baseline & CCO-only comparisons** — comparison populations are generated from their own parameters rather than copied from the tested scenario; baseline shocks/inflation are now anchored to documented reference values instead of the user's own sliders (v4.0)
- **Recession severity mode corrected** — beta(5,2) recession severity's mode is 0.90 (10% income loss), not 0.86/14% as earlier documentation stated; the distribution itself, its mean (~12% loss), and its NBER calibration are unchanged (v4.0 correction)
- **Monte Carlo, ablation & OAT statistics fixed** — 3×/10×/50× Monte Carlo runs were silently executing once with zero results collected; now fully functional and relabeled "Stochastic CI" (a re-run-at-fixed-parameters error range, not a full outcome-uncertainty interval). Ablation/attribution now uses paired populations and RNG streams with signed deltas. OAT sensitivity perturbs all five parameters by a uniform ±20% of each one's own slider range (v4.0)
- **Framing corrected to "exploratory," not "policy-grade"** — title, meta tags, and copy now consistently describe this as a research-oriented exploratory ABM for comparative policy analysis, matching the caveats already in Known Limitations (v4.2)
- **In-app glossary & accessible charts** — a collapsible CCO/PTF/PTH/SZH/CIP/BLEI/EDC/FBS/AE glossary panel, plus ARIA labels on all 11 Chart.js canvases for screen readers (v3.7)
- **DOI + citation consolidation, Cancel control** — archival DOI ([10.17605/OSF.IO/QWTE2](https://doi.org/10.17605/OSF.IO/QWTE2)) added; a single metadata object drives version/citation strings across the UI and both export formats; single runs and chained Monte Carlo batches can now be cancelled mid-run (v3.5–v3.6)
- **New policy-benchmark KPIs, attribution chart & conversion ledger** — Break-even Year, wealth p90/p10 ratio, and bottom-decile wealth join the KPI set; a BLEI gain-attribution (ablation) chart shows each system's marginal contribution; JSON/CSV export now includes cumulative CCO conversion proceeds (v4.0)

Full line-by-line changelog (v3.1 → v4.2) is in the simulation's own source and in the [Replication Framework's Version History](https://bettertobest.github.io/research-hub/cco-ptf-simulation-replication.html).

---

## What this simulates

The simulation models all five integrated Compassionism architectures and their interactions:

| System | Layer | Role in the model |
|--------|-------|-------------------|
| **CCO** (Creative Currency Octaves) | Economic | Distributes flat Basic Units (BU) monthly ($1,200 face value); BU food-purchasing-power premium ε_food = 2.64× ($990/adult/month effective). Conversion rate is capacity-gated by octave (scales linearly from 1× toward the quality ceiling as octave rises) and modulated by quality (1×–9×), plus a Φ 1.618× golden-ratio bonus above 70% of the quality ceiling (v4.0) |
| **PTF** (Public Trust Foundations) | Asset | Community-owned essential goods/services that accept BU; modeled purely as a **cost-reduction mechanism** (12–16% lower living costs), not a wealth-addition channel — eliminates the ex-nihilo money creation present in earlier versions |
| **PTH** (Public Trust Housing) | Asset | Community-owned housing; reduces housing-linked living costs 35%, routes 25% of that saving into Acre Equity (appreciating ~4%/yr, 50% liquidity haircut at exit) alongside separate appreciation on the initial endowment; PTH payments carry EDC = 0 (v4.0) |
| **SZH** (Social Zone Harmonization) | Spatial | Zone Coherence Index (0.30–0.95) gives all residents a flat coherence-linked benefit, plus gates a separate PTF-network synergy bonus (θ): 0 below 55% coherence, scaling linearly to 0.25 at 90%+ (v4.0) |
| **CIP** (Citizens Internet Portal) | Democratic | Digital platform administering CCO currency operations and democratic voting on PTF/PTH decisions; raises effective octave-advancement capability (+20% to λ at full participation, replacing the old flat advancement bump), improves quality accuracy, and reduces conversion-tax leakage |

Welfare outcomes are measured against the **Basic Living Economic Index (BLEI)** — a temporal stability metric calibrated to US baseline conditions. See the [BLEI paper](https://bettertobest.github.io/research-hub/basic-living-economic-index.html).

---

## How to use

**No Python. No installation. Just open `index.html` in any browser.**

### Option A — Open locally
1. Download `index.html`
2. Double-click — opens in Chrome, Firefox, Safari, or Edge
3. Adjust controls and click **Run Simulation**

### Option B — Host on GitHub Pages
1. Upload `index.html` to your repository root
2. Go to **Settings → Pages → Source → main branch / root**
3. Live at `https://yourusername.github.io/compassionism-simulation/`

---

## Controls reference

### Scenario presets

| Preset | Systems active | Purpose |
|--------|---------------|---------|
| **Traditional Welfare** | None (BU = $0) | US baseline — no CCO; 3% CPI inflation and recession shocks on by default |
| **CCO Only** | CCO (75% participation) | Basic Units active; no community infrastructure |
| **Full Integration** | All five | Reference calibration (78% CCO / 18% initial PTF / 20% PTH / 0.72 SZH / 65% CIP) from Monte Carlo research |
| **Stress Test** | All five (degraded) + AI automation | Low participation (40%) + shocks + AI displacement — tests fragility |
| **High Automation** | Full Integration params + AI wave | Full Integration parameters with AI displacement over a 25-year horizon |

### CCO parameters

| Parameter | Range | Reference |
|-----------|-------|-----------|
| Monthly BU allocation | $0–$1,800 | $1,200 |
| Max octave level | 1–9 | 6 — sets the CCO conversion-rate *capacity* ceiling; capacity scales linearly from 1× toward the quality ceiling as octave rises (v4.0) |
| BU expiry | 1–6 months | 1 month |
| Phi Φ rate | On / Off | On — 1.618× bonus once quality exceeds 70% of the quality ceiling |
| Conversion tax | 0–30% | 12% (progressive taper above a conversion rate of 3.0×) |
| Quality multiplier ceiling | 1×–9× | 9× (effective max with Phi: 14.56×) |

### SZH parameters
- **Zone coherence index** (0.30–0.95, default 0.72): a flat coherence-linked benefit for all residents, plus the gate for the θ PTF-network synergy bonus described above

### CIP parameters
- **Democratic participation rate** (20–95%, default 65%): raises effective octave-advancement capability, improves quality accuracy, and reduces conversion-tax leakage

### Population, environment & run parameters
- **Agent population** (default 500)
- **Simulation years** (default 20; the High Automation preset runs 25)
- **Initial PTF share** (0–35%, reference ~18%; renamed from "PTF market share" in v3.6): sets only the *initial* adoption probability — organic Bass-diffusion growth means the realized final share can exceed this. Distortion threshold: >30%
- **PTH uptake rate** (default 20%)
- **Inflation rate** (0–?%/yr, default 0%): 3% = US CPI baseline; PTF/PTH dampen effective inflation
- **Stochastic recession events**: population-level, 10% annual probability, 1–3 year duration, beta(5,2)-distributed 70–95% income multiplier (mode ≈ 0.90 → 10% loss)
- **AI labor automation**: heterogeneous per-agent risk; assumes a 2025 simulation start, with displacement beginning year 5+ (~2030) and accelerating from year 15+ (~2040)
- **Random seed**: optional — same seed + same parameters reproduces an identical run; blank uses natural Monte Carlo variance

### Participation thresholds
- **Minimum viable:** 55% (below this, network effects collapse)
- **Reference:** 78%

### Run options
- **Run Simulation** — single run (deterministic with a seed, or naturally variable without one)
- **Cancel Run** — stop a long run cleanly, no page reload needed (v3.6)
- **Run 3×** — variance range (min/max/mean)
- **Run 10× / 50×** — "Stochastic CI" (mean ± 1.96·SD/√n): a re-run-at-fixed-parameters error range, relabeled from "Publication/95% CI" for accuracy — it is not a full outcome-uncertainty interval (v4.0)
- **One-at-a-Time Sensitivity** — 5 parameters, each perturbed by a uniform ±20% of its own slider range, from real mini-runs at seed 7777 (v4.0)
- **Validation Suite** — the "Internal Consistency & Behavioral Test Suite": 6 checks across 5 seeds requiring unanimous agreement; covers ODD validation Levels 1–3 only (v4.2)

---

## Output metrics

**v4.2 large-N study** — 5,000 independent seeded runs per scenario (seeds 1–5,000, 500 agents, 20 years each; Full Integration reference configuration). Figures below are the mean across runs; 95% CIs (typically ±0.05–0.1 percentage points at this sample size) are in the [Replication Framework's Performance Comparison](https://bettertobest.github.io/research-hub/cco-ptf-simulation-replication.html). These are internally calibrated simulation outcomes under a reference parameter set — a design reference point, not a prediction for any specific real-world deployment.

| Metric | Full Integration | CCO Only | Traditional Welfare Baseline |
|--------|------------------|----------|-------------------------------|
| Median wealth, year 20 | $81,597 | $73,001 | $7,316 |
| Gini (EDC-adjusted net wealth) | 0.484 | 0.516 | 0.800 |
| BLEI poverty rate (Crisis+Precarious, <30 days — primary poverty indicator) | 7.9% | 9.7% | 52.2% |
| BLEI Threshold rate (≥30 days) | 92.1% | 90.3% | 47.8% |
| BLEI Stable rate (≥120 days) | 80.8% | — | — |
| BLEI Secure rate (≥365 days) | 39.7% | — | — |
| BLEI Flourishing rate (≥730 days) | 15.2% | — | — |
| Median BLEI, final year | 294 days | — | — |
| Participant vs. non-participant poverty | 4.3% vs. 52.0% | — | — |
| System stability (structural metric, v4.2) | 94.7% | 95.3% | 80.6% |

*Daily basic cost (calibration constant, unchanged): $31.67/day under CCO+PTH vs. $68.33/day baseline (BLS CES 2023).*

**Design targets vs. measured output:** pre-existing internal calibration targets (BLEI Threshold ≥95%, EDC-adjusted Gini ≤0.25, System Stability ≥90%, BLEI Poverty <5%) were aspirational goals never checked against shipped code — EDC-adjusted Gini specifically couldn't have been, since v4.0 is the first release that actually computes it. Measured v4.2 output meets or exceeds the Stability and Threshold-Rate targets and lands within 0.5% of the wealth target, but falls short on Poverty Rate (7.9% vs. <5%) and further short on Gini (0.484 vs. ≤0.25). The likely driver: the wealth-initialization distribution itself, `lognormal(10.5, 1.2)`, carries an inherent Gini of ≈0.60 before any simulation dynamics or EDC adjustment — suggesting the old 0.22 target was a theoretical projection never checked against the actual initialization, not a value the model regressed on. Nordic post-redistribution Gini (0.27–0.29, external reference) remains the more realistic real-world comparison point than either the design targets or this simulation's reference-configuration output. Full discussion in the Replication Framework's "On calibration versus validation."

### BLEI tier definitions

| Tier | Days covered | Economic condition |
|------|-------------|-------------------|
| Crisis | <7 | Immediate survival risk |
| Precarious | 7–29 | Acute economic vulnerability |
| Threshold | 30–119 | Basic needs met, no buffer |
| Stable | 120–364 | Modest planning horizon |
| Secure | 365–729 | One-year investment horizon |
| **Flourishing** | **730+** | **Two-year entrepreneurial horizon unlocked** |

The top tier is labeled **Flourishing** when both CCO and PTF are active, or **Comfortable** for baseline/CCO-only configurations — both refer to the same 730-day threshold; "Flourishing" reflects that the label is structurally attainable once PTF's cost reductions are in play.

**BLEI poverty** (% Crisis + Precarious, i.e. < 30 days) is the framework's primary poverty indicator — it captures temporal vulnerability rather than wealth stock, and correctly classifies income-stable households who happen to hold low assets.

---

## Stress-test scenarios

1. **No CCO (BU = $0)** — Traditional Welfare preset; observe the pure welfare-state baseline (3% CPI, shocks on) — BLEI drops to Precarious/Threshold for most agents
2. **Participation collapse** — Set participation to 40%; network effects fail; Gini and poverty stagnate
3. **SZH disabled** — Compare outcomes with and without spatial zone coherence; disabling SZH also zeroes the θ PTF-network synergy bonus entirely
4. **CIP disabled** — Observe quality noise increase, stability drop, and reduced octave-advancement capability (CIP's +20% λ boost no longer applies)
5. **Phi-only economy** — Set max multiplier 9×, enable Φ, participation 95%; the asymptotic conversion ceiling (14.56×) is unchanged from earlier versions even though the path to it is now linear-in-octave rather than exponential — what is the ceiling in practice?
6. **PTF saturation** — Push Initial PTF share above 30%; observe the distortion warning and Gini effects
7. **Shock resilience** — Enable shocks (beta(5,2) severity, mode 0.90/10% loss, 1–3 year duration) with reference vs. stress-test parameters
8. **High automation wave** — Use the High Automation preset (25-year horizon); observe heterogeneous wage displacement by `automationRisk` tier, starting year 5+ and accelerating year 15+
9. **Non-participant equity** — Enable CCO at 78%, examine participant vs. non-participant stratification charts; the v4.2 validation suite confirms non-participants run measurably *better* under CCO, not worse (≈2.6 percentage points lower poverty in testing)

---

## Replication & validation

This simulation implements the mathematical framework from:

> Johnson, D. & Claude (Anthropic). (2026). *CCO-PTF-PTH-CIP-SZH Simulation Replication Framework*. Better To Best Research Hub. <https://bettertobest.github.io/research-hub/cco-ptf-simulation-replication.html>

BLEI calibration from:

> Johnson, D. & Claude (Anthropic). (2026). *Basic Living Economic Index: A temporal stability framework for welfare measurement under Compassionism*. Better To Best Research Hub. <https://bettertobest.github.io/research-hub/basic-living-economic-index.html>

### Core formulas

**Octave conversion-rate capacity (v4.0, replaces the earlier exponential form):**
```
C_ceiling(O) = 1 + (O / O_max) × (M_max − 1)          [linear in octave, not 2^O]
Q_factor     = min(1, Quality / M_max)
BaseRate     = 1 + Q_factor × (C_ceiling − 1)
Rate         = min(BaseRate × φ_beauty × M_PTF, M_max × φ_beauty)
```
where φ_beauty = 1.618 once Quality exceeds 70% of M_max, else 1.0. The asymptotic ceiling (M_max × φ_beauty, e.g. 14.56× at defaults) is unchanged from earlier versions.

**Octave advancement probability (v4.0, new):**
```
P(advance) = 1 − exp(−λ × FBS)
```
`λ ~ Uniform(0.001, 0.008)` per agent; CIP support raises effective λ by up to +20% at full participation. An agent at FBS = 0 cannot advance regardless of quality or BLEI.

**Financial Bandwidth Score (FBS):**
```
FBS = max(0, Y_USD + BU_monthly − C_basic_cash_monthly − EDC_residual × Y_USD)
```
`EDC_residual` uses consumer-debt-only values (0.12 baseline, 0.025 for CCO+PTH participants) to avoid double-counting housing costs already in `C_basic`.

**SZH synergy coefficient θ (v4.0, zone-coherence-gated):**
```
θ(coh) = 0                                            if coh < 0.55
θ(coh) = min(0.25, (coh − 0.55) / (0.90 − 0.55) × 0.25) if coh ≥ 0.55
```
replacing a flat linear treatment at every coherence level; magnitudes are scaled so θ at full coherence matches the pre-v4.0 ceiling.

**SIU → USD conversion (v4.0, used only in BLEI/FBS/Gini — not the main wealth loop):**
```
SIU_TO_USD = (BASE_DAILY_COST × 365) / SIM_COST_SCALE ≈ 16.6
```
The main wealth-accumulation step deliberately keeps wage (SIU) and cost (SIM_COST_SCALE) combined directly, unchanged since before v4.0 — a full USD conversion there proved extremely sensitive to the conversion constant over multi-decade runs (candidate constants spanning a ~3.5× range swung 20-year outcomes from universal wealth-floor collapse to implausible multi-million-dollar median wealth) and would need a joint recalibration against real income data to do safely.

**Gini coefficient (v4.0, computed on EDC-adjusted net wealth):**
```
W_net,i = max(0, W_nominal,i − EDC_i × Y_USD,i × 12)
Gini    = (2 × Σ rank_i × W_net,i) / (n × Σ W_net) − (n + 1) / n
```
computed over agents sorted ascending by `W_net`. Previously the engine only computed nominal-wealth Gini.

**Structural System Stability (v4.2, new — replaces a trend-plus-noise heuristic):**
```
CV(x)      = σ(x) / |mean(x)|                          [over the run's final quarter]
Stability  = clamp(0, 0.99, (1/(1+CV_wealth) + 1/(1+CV_BLEI)) / 2)
```
No RNG call and no manual per-mechanism bonus — a genuinely stabilizing mechanism now shows up endogenously as lower volatility.

**Recession severity (v3.3; mode figure corrected v4.0):**
```
incomeMultiplier = 0.70 + Beta(5, 2) × 0.25   ∈ [0.70, 0.95]
```
Mode = 0.90 (10% income loss) — Beta(5,2)'s mode is (5−1)/(5+2−2) = 0.80, so 0.70 + 0.80×0.25 = 0.90. (Earlier documentation stated the mode as ≈0.86/14% loss, which was arithmetically wrong; the formula itself was never wrong.) Mean ≈0.88 (~12% loss), unaffected by the correction, and close to the cited NBER target. Calibrated against NBER post-WWII recession data. Source: [NBER Business Cycle Dating Committee](https://www.nber.org/research/business-cycle-dating).

**Dual wealth accumulation (paper-level formalization; θ behavior updated per above):**
```
W_total(t) = W_CCO(t) + W_PTF(t) + θ × W_CCO(t) × W_PTF(t)
```

---

## License & attribution

Released under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

**Cite as:**
> Johnson, D. & Claude (Anthropic). (2026). *Compassionism Framework Simulation* (v4.2). Better To Best Research Hub. CC BY 4.0. <https://doi.org/10.17605/OSF.IO/QWTE2>

**Research Hub:** [bettertobest.github.io/research-hub](https://bettertobest.github.io/research-hub/)
**Wiki:** [bettertobest.github.io/research-hub/wiki](https://bettertobest.github.io/research-hub/wiki/)
**BLEI Paper:** [basic-living-economic-index.html](https://bettertobest.github.io/research-hub/basic-living-economic-index.html)
**Replication Framework:** [cco-ptf-simulation-replication.html](https://bettertobest.github.io/research-hub/cco-ptf-simulation-replication.html)
**Contributors' Guide:** [CONTRIBUTING.md](https://github.com/BetterToBest/compassionism-simulation/blob/main/CONTRIBUTING.md)
**DOI:** [10.17605/OSF.IO/QWTE2](https://doi.org/10.17605/OSF.IO/QWTE2)
**Contact:** BetterToBestResearch@gmail.com
**Discussions:** [GitHub Discussions](https://github.com/BetterToBest/research-hub/discussions)
