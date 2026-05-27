# Compassionism Framework Simulation

An interactive, browser-based agent-based simulation of all five [Compassionism](https://bettertobest.github.io/research-hub/) architectures — no installation required. BLEI-calibrated against 2023 US Consumer Expenditure Survey data.

**[▶ Open the simulation](https://bettertobest.github.io/compassionism-simulation/)**

---

## What this simulates

The simulation models all five integrated Compassionism architectures and their interactions:

| System | Layer | Role in the model |
|--------|-------|-------------------|
| **CCO** (Creative Currency Octaves) | Economic | Distributes Basic Units monthly; agents convert at quality-based multipliers (1×–9×) plus Φ 1.618× golden ratio bonus |
| **PTF** (Public Trust Foundations) | Asset | Community-owned essential goods; reduces agent overhead 40–60%; raises BU food utility at 2.64× premium |
| **PTH** (Public Trust Housing) | Asset | Builds Acre Equity for resident agents; housing costs settled in Basic Units; eliminates rent extraction (EDC drops to &lt;10%) |
| **SZH** (Social Zone Harmonization) | Spatial | Zone coherence index (0.30–0.95) amplifies PTF conversion rates up to 35% and PTH Acre Equity appreciation by up to 1%/yr |
| **CIP** (Citizens Internet Portal) | Democratic | Governs merit assessment and Octave advancement; raises system stability up to 14%; reduces conversion tax leakage |

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
| **Traditional Welfare** | None (BU = $0) | US baseline — no CCO, welfare transfers only |
| **CCO Only** | CCO | Basic Units active; no community infrastructure |
| **Full Integration** | All five | Optimal parameters from Monte Carlo research |
| **Stress Test** | All five (degraded) | Low participation + shocks — tests fragility |

### CCO parameters

| Parameter | Range | Optimal |
|-----------|-------|---------|
| Monthly BU allocation | $0–$1,800 | $1,200 |
| Max octave level | 1–9 | 6 |
| BU expiry | 1–6 months | 1 month |
| Phi Φ rate | On / Off | On (1.618×) |
| Conversion tax | 0–30% | 12% |
| Quality multiplier ceiling | 1×–9× | 9× |

### SZH parameters
- **Zone coherence index** (0.30–0.95, default 0.72): higher coherence amplifies PTF and PTH effectiveness spatially

### CIP parameters
- **Democratic participation rate** (20–95%, default 65%): higher participation improves quality accuracy, octave advancement, and stability

### Participation thresholds
- **Minimum viable:** 55% (below this, network effects collapse)
- **Optimal:** 78%

---

## Output metrics

### Economic outcomes

| Metric | Full integration | US baseline |
|--------|-----------------|-------------|
| Poverty rate | &lt;2% | ~77% |
| Gini coefficient | ≤0.25 | ~0.48 |
| Median wealth | $82,000 | ~$18,500 |
| System stability | ≥90% | ~65% |

### BLEI temporal stability (Johnson & Claude, 2026)

| Metric | Full integration | US baseline |
|--------|-----------------|-------------|
| Median BLEI score | 700–800+ days | ~45 days |
| % at Flourishing tier (730+ days) | >50% | ~2% |
| Avg Extractive Drain (EDC) | &lt;10% | 53–72% |
| Daily basic cost | $31.67 | $68.33 |

### BLEI tier definitions

| Tier | Days covered | Economic condition |
|------|-------------|-------------------|
| Crisis | &lt;7 | Immediate survival risk |
| Precarious | 7–29 | Acute economic vulnerability |
| Threshold | 30–119 | Basic needs met, no buffer |
| Stable | 120–364 | Modest planning horizon |
| Secure | 365–729 | One-year investment horizon |
| **Flourishing** | **730+** | **Two-year entrepreneurial horizon unlocked** |

---

## Stress-test scenarios

1. **No CCO (BU = $0)** — Observe pure welfare-state baseline; BLEI drops to Precarious for most agents
2. **Participation collapse** — Set participation to 40%; network effects fail; Gini and poverty stagnate
3. **SZH disabled** — Compare PTF/PTH outcomes with and without spatial zone coherence
4. **CIP disabled** — Observe quality noise increase; stability drops; octave advancement slows
5. **Phi-only economy** — Set max multiplier 9×, enable Φ, participation 95%; what is the ceiling?
6. **PTF saturation** — Push PTF above 30%; observe distortion warning and Gini effects
7. **Shock resilience** — Enable shocks with optimal vs. stress-test parameters; compare stability scores

---

## Replication & validation

This simulation implements the mathematical framework from:

> Johnson, D. & Claude (Anthropic). (2025). *CCO-PTF-PTH-CIP-SZH Simulation Replication Framework*. Better To Best Research Hub. <https://bettertobest.github.io/research-hub/cco-ptf-simulation-replication.html>

BLEI calibration from:

> Johnson, D. & Claude (Anthropic). (2026). *Basic Living Economic Index: A temporal stability framework for welfare measurement under Compassionism*. Better To Best Research Hub. <https://bettertobest.github.io/research-hub/basic-living-economic-index.html>

### Core formulas

**Dual wealth accumulation:**
```
W_total(t) = W_CCO(t) + W_PTF(t) + θ × W_CCO(t) × W_PTF(t)
```
where θ = 0.15–0.25 (synergy coefficient)

**Phi-enhanced conversion:**
```
CCO_enhanced = B₀ × 2^O × R_base × φ_beauty × M_PTF × M_SZH
```

**SZH PTF amplification:**
```
M_SZH = 1.30 + (ZoneCoherence − 0.50) × 0.35   [range: 1.22–1.48]
```

**BLEI score:**
```
BLEI = (Liquid assets + γ × Monthly income + BU_food_effective) / C_basic_daily
```
where C_basic_daily = $68.33 baseline → $31.67 under CCO + PTH

**Gini evolution:**
```
Gini(t) = Gini₀ × (1 − ρ_CCO − ρ_PTF − ρ_SZH − ρ_CIP)^t
```

---

## License & attribution

Released under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

**Cite as:**
> Johnson, D. & Claude (Anthropic). (2025–2026). *Compassionism Framework Interactive Simulation* (v2.0). Better To Best Research Hub. <https://bettertobest.github.io/compassionism-simulation/>

**Research Hub:** [bettertobest.github.io/research-hub](https://bettertobest.github.io/research-hub/)  
**Wiki:** [bettertobest.github.io/research-hub/wiki](https://bettertobest.github.io/research-hub/wiki/)  
**BLEI Paper:** [basic-living-economic-index.html](https://bettertobest.github.io/research-hub/basic-living-economic-index.html)  
**Contact:** BetterToBestResearch@gmail.com  
**Discussions:** [GitHub Discussions](https://github.com/BetterToBest/research-hub/discussions)
