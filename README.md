# Compassionism Framework Simulation

An interactive, browser-based agent-based simulation of the [Compassionism economic framework](https://bettertobest.github.io/research-hub/) — no installation required.

**[▶ Open the simulation](https://bettertobest.github.io/research-hub/compassionism-sim/)** *(once uploaded to GitHub Pages)*

---

## What this simulates

The simulation models the five integrated Compassionism architectures:

| System | Role | What it does in the model |
|--------|------|--------------------------|
| **CCO** (Creative Currency Octaves) | Economic layer | Distributes Basic Units monthly; agents convert them at quality-based multipliers (1×–9×, plus Φ 1.618× bonus) |
| **PTF** (Public Trust Foundations) | Asset layer | Community-owned essential goods; reduces agent overhead 40–60%; raises conversion rates for participating agents |
| **PTH** (Public Trust Housing) | Asset layer | Builds Acre Equity for resident agents; housing costs partially settled in Basic Units |
| **SZH** (Social Zone Harmonization) | Spatial layer | Shapes PTF service zones (modelled via PTF participation rates) |
| **CIP** (Citizens Internet Portal) | Democratic layer | Governs conversion, merit assessment, and Octave advancement (modelled as quality score updates) |

---

## How to use

**No Python. No installation. Just open `index.html` in any web browser.**

### Option A — Open locally
1. Download `index.html` to your computer
2. Double-click the file — it opens in Chrome, Firefox, Safari, or Edge
3. Adjust sliders and toggles, then click **Run Simulation**

### Option B — Host on GitHub Pages (recommended for sharing)
1. Create a new repository on GitHub (e.g. `compassionism-sim`)
2. Upload `index.html` to the repository root
3. Go to **Settings → Pages → Source → main branch / root**
4. Your simulation will be live at `https://yourusername.github.io/compassionism-sim/`

---

## Controls reference

### Scenario presets
Click any preset to auto-fill all parameters:

| Preset | Purpose |
|--------|---------|
| Traditional welfare | Baseline — no CCO/PTF, minimal welfare transfer |
| CCO only | Basic Units active; no PTF or PTH infrastructure |
| Full integration | Optimal parameters per 10,000-iteration Monte Carlo research |
| Stress test | Low participation, shocks enabled — tests system fragility |

### Key parameters

**CCO — Basic Units**
- *Monthly BU allocation* — amount each CCO participant receives per month ($400–$1,800; optimal: $1,200)
- *Max octave level* — conversion capacity ceiling; each octave doubles the previous (C_n = C_base × 2ⁿ)
- *BU expiry* — months before unused Basic Units expire; 1 month = standard monthly circulation cycle
- *Phi rate (Φ)* — enables the 1.618× golden ratio bonus for work assessed as productive AND beautiful

**Quality & Conversion**
- *Base multiplier ceiling* — maximum conversion rate from 1× (minimal quality) to 9× (exquisite)
- *Conversion tax rate* — % levied on BU→primary currency conversions; balances system revenue with participation incentive

**Population & Participation**
- *CCO participation rate* — share of agents who opt into the CCO system; **minimum viable: 55%** (network effects threshold)
- *Simulation years* — projection horizon (5–30 years)

**Systems to enable**
- Toggle PTF, PTH, and economic shock events on/off to observe isolated vs. integrated outcomes

---

## Output metrics

| Metric | Target | Baseline |
|--------|--------|---------|
| Poverty rate | < 2% | ~77% |
| Gini coefficient | ≤ 0.25 | ~0.48 |
| Median wealth | $82,000 | ~$18,500 |
| System stability | ≥ 90% | ~65% |

The **system comparison table** shows your current parameters vs. CCO-only vs. traditional welfare baseline simultaneously.

The **sensitivity chart** shows which parameters have the highest impact on poverty reduction (fixed from research — not run-dependent).

---

## Replication & validation

This simulation implements the mathematical framework from:

> Johnson, D. & Claude (Anthropic). (2025). *CCO-PTF-PTH-CIP-SZH Simulation Replication Framework*. Better To Best Research Hub. [https://bettertobest.github.io/research-hub/cco-ptf-simulation-replication.html](https://bettertobest.github.io/research-hub/cco-ptf-simulation-replication.html)

Core formulas implemented:

**Dual wealth accumulation:**  
`W_total(t) = W_CCO(t) + W_PTF(t) + θ × W_CCO(t) × W_PTF(t)`  
where θ = 0.15–0.25 (synergy coefficient)

**Phi-enhanced conversion:**  
`CCO_enhanced = B₀ × 2^O × R_base × φ_beauty × M_PTF`

**Gini evolution:**  
`Gini(t) = Gini₀ × (1 - ρ_CCO - ρ_PTF - ρ_synergy)^t`

---

## Stress-test ideas

Try these scenarios to probe system behaviour:

1. **Participation collapse** — Set participation to 40%. Observe Gini and poverty stagnating; note the stability warning.
2. **BU floor** — Set BU to $400 with 78% participation. Does high participation compensate for low allocation?
3. **Phi-only economy** — Set max multiplier to 9×, enable Φ, set participation to 95%. What is the ceiling outcome?
4. **PTF saturation** — Increase PTF market share above 30%. Observe the distortion warning.
5. **Shock resilience** — Enable economic shocks with optimal vs. stress-test parameters. Compare stability scores.

---

## License & attribution

This simulation is released under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to share, adapt, and build on this work with attribution.

**Cite as:**  
Johnson, D. & Claude (Anthropic). (2025–2026). *Compassionism Framework Interactive Simulation*. Better To Best Research Hub. https://bettertobest.github.io/research-hub/

**Research Hub:** [bettertobest.github.io/research-hub](https://bettertobest.github.io/research-hub/)  
**Contact:** BetterToBestResearch@gmail.com  
**Discussions:** [GitHub Discussions](https://github.com/BetterToBest/research-hub/discussions)
