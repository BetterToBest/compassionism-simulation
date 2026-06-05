# Contributing to the Compassionism Framework Simulation

**Better To Best Research Hub** · [bettertobest.github.io/research-hub](https://bettertobest.github.io/research-hub/)  
CC BY 4.0 · Contact: BetterToBestResearch@gmail.com

---

## Research Objective

These simulations are designed to identify parameter configurations where **optimal-for-all** conditions align with **ideal-for-each** — analogous to a structural model that must meet a specified load capacity across all points simultaneously. The five Compassionism architectures (CCO, PTF, PTH, SZH, CIP) are the design variables; BLEI-calibrated welfare metrics are the load criteria.

The goal is not to find a single "correct" answer but to map the solution space: where do welfare improvements compound, where do trade-offs appear, and where do the six BLEI tiers distribute under different real-world conditions? Community input is essential to refining and validating this map.

---

## How to Contribute

### 1. Parameter Feedback & Scenario Testing

Run the simulation with parameter configurations that model real-world conditions you know well — a specific region, income cohort, housing market, or policy environment. Export your results via the **Download CSV** button and open a GitHub issue with:

- Your exported CSV attached
- A brief description of the real-world scenario you were modeling
- Any discrepancies between the simulation output and observed or expected outcomes

This is the highest-value contribution. The model's calibration constants (daily basic cost, EDC ranges, PTF distortion threshold) were set from US CES 2023 data and benefit greatly from being tested against other contexts.

### 2. Calibration Validation

The simulation uses several empirically grounded constants defined in the `CFG` object at the top of `index.html`. Contributions that improve these with cited sources are especially welcome:

| Constant | Current value | Source | What would improve it |
|---|---|---|---|
| `BASE_DAILY_COST` | $68.33/day | US CES 2023 | Regional breakdowns; non-US benchmarks |
| `CCO_PTH_DAILY_COST` | $31.67/day | BLEI §3.2 estimate | Empirical housing cost studies |
| `EDC_BASELINE_LO/HI` | 0.62–0.72 | US CES 2023, near-poverty | Income quintile breakdowns; international data |
| `PTF_OPTIMAL_SHARE` | 18% | Framework spec | Cooperative sector empirical studies |
| `NORDIC_GINI` | 0.28 | OECD | Year-specific updates; regional variants |
| `PROG_PIVOT` / `PROG_RATE` | 3.0 / 0.040 | Theoretical | Creative economy income distribution data |

To propose a calibration update, open an issue with the prefix `calibration:`, your proposed value, the source with full citation, and if possible a comparison of output before and after the change.

### 3. Reproducibility Testing

The simulation supports seeded runs (Mulberry32 PRNG). To verify a result:

1. Note the **Random seed** and all parameter values from the exported CSV
2. Enter the same seed and parameters in the simulation
3. Confirm the output matches byte-for-byte

If results diverge under identical seed + parameters, open a bug report with both CSVs. This should not happen — if it does, it indicates a browser environment difference worth documenting.

### 4. Model Architecture Feedback

The BLEI framework (Johnson & Claude, 2026) defines six welfare tiers using days of basic living covered as the unit. If you have academic or practitioner expertise in welfare measurement, poverty metrics, or mechanism design and see gaps between the model's architecture and real-world welfare dynamics, open an issue with the prefix `architecture:`.

Areas currently open for discussion:

- **FBS gating** — Octave advancement is currently gated on BLEI > 30 days (Precarious threshold). Is this threshold appropriately set?
- **EDC baseline** — The extractive drain coefficient currently models rent as the dominant extraction channel. Does this adequately represent consumer debt, healthcare, and other extraction vectors?
- **PTF distortion threshold** — The 30% market share distortion threshold is a framework specification. What empirical evidence exists for cooperative sector distortion thresholds?
- **θ synergy coefficient** — Inter-system synergy effects (SZH amplifying PTF, CIP improving CCO quality accuracy) are currently hardcoded. Should these be exposed as parameters with empirically derived defaults?

### 5. Code Contributions

The simulation is intentionally a single HTML file with no build tooling — it runs directly from any browser, is easily auditable, and can be archived. Please maintain this constraint.

**Before submitting a pull request:**

- Test in Chrome, Firefox, and Safari
- Ensure the seeded RNG produces identical output before and after your change (use seed `42`, Full Integration preset, 20 years — record the Median BLEI score and Gini as a regression check)
- Do not introduce external dependencies beyond the existing Chart.js CDN import
- Follow the existing code style: vanilla JS, CSS variables, inline documentation, `CFG` object for all calibration constants

**Good first issues:**

- Add a "Copy parameters as URL" feature so scenarios can be shared as links
- Add an i-button next to each BLEI tier in the distribution chart that shows its definition
- Export the year-by-year time series (poverty, Gini, wealth, BLEI) as additional CSV rows

### 6. Academic Peer Review

Researchers are invited to review the primary papers and submit formal comments:

- **BLEI Paper**: [bettertobest.github.io/research-hub/basic-living-economic-index.html](https://bettertobest.github.io/research-hub/basic-living-economic-index.html)
- **Replication Framework**: [bettertobest.github.io/research-hub/cco-ptf-simulation-replication.html](https://bettertobest.github.io/research-hub/cco-ptf-simulation-replication.html)
- **Academia.edu**: [independentresearcher.academia.edu/DukeJohnson](https://independentresearcher.academia.edu/DukeJohnson)

Submit review comments as GitHub issues with the prefix `review:`.

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

Each simulation run without a fixed seed produces slightly different results — this is correct behaviour, not a bug. It reflects genuine Monte Carlo variance across the agent population. When reporting results for comparative purposes, either:

1. Use a fixed seed (record it in your CSV export), or
2. Run multiple unseeded trials and report the mean ± standard deviation across runs

Neither approach is more "correct" — they answer different questions. Fixed seeds ask *"given this exact stochastic realization, what happens?"*; unseeded multiple trials ask *"on average across realizations, what happens?"*

---

## Contact

- **Email**: BetterToBestResearch@gmail.com
- **Hub**: [bettertobest.github.io/research-hub](https://bettertobest.github.io/research-hub/)
- **Bluesky**: [@better-to-best.bsky.social](https://bsky.app/profile/better-to-best.bsky.social)
- **Medium**: [medium.com/@duke.t.james](https://medium.com/@duke.t.james)

---

## License

All contributions are released under **CC BY 4.0**. Attribution to the Better To Best Research Hub is required. By submitting a contribution, you agree to these terms.

---

*Better To Best Research Hub · Compassionism Framework Simulation v2.2*  
*Principal Investigator: Duke Johnson (pseudonymous)*  
