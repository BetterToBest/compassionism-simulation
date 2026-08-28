# Compassionism Framework Simulation

A research-oriented, browser-based agent-based simulation exploring all five [Compassionism](https://bettertobest.github.io/research-hub/) architectures for comparative policy analysis — no installation required. BLEI-calibrated against US Consumer Expenditure Survey data.

**[▶ Open the simulation](https://bettertobest.github.io/compassionism-simulation/)** · DOI: [10.17605/OSF.IO/QWTE2](https://doi.org/10.17605/OSF.IO/QWTE2)

This file covers what the project is and how to run it. For everything version-specific — the full changelog, current output metrics, methodology, and formulas — see the **[Replication Framework](https://bettertobest.github.io/research-hub/cco-ptf-simulation-replication.html)**, which is kept current with each release. For open questions, known limitations, and how to contribute, see **[CONTRIBUTING.md](https://github.com/BetterToBest/compassionism-simulation/blob/main/CONTRIBUTING.md)**.

---

## What this simulates

The simulation models all five integrated Compassionism architectures and their interactions:

| System | Layer | Role in the model |
|--------|-------|-------------------|
| **CCO** (Creative Currency Octaves) | Economic | Distributes flat Basic Units (BU) monthly to participants, redeemable at PTF businesses and convertible to primary currency at merit-scaled rates that improve with an agent's octave level and quality |
| **PTF** (Public Trust Foundations) | Asset | Community-owned essential goods/services that accept BU; modeled as a **cost-reduction mechanism**, not a wealth-addition channel |
| **PTH** (Public Trust Housing) | Asset | Community-owned housing; reduces housing-linked living costs and routes a share of that saving into Acre Equity, which appreciates over time and is accessible at exit subject to a liquidity haircut |
| **SZH** (Social Zone Harmonization) | Spatial | Zone-level coherence gives residents a coherence-linked benefit and gates a separate cooperative-synergy bonus once PTF merchant density crosses a threshold |
| **CIP** (Citizens Internet Portal) | Democratic | Digital platform administering CCO currency operations and democratic voting on PTF/PTH decisions; participation improves octave-advancement capability, quality accuracy, and reduces conversion-tax leakage |

Welfare outcomes are measured against the **Basic Living Economic Index (BLEI)** — a temporal-stability metric expressing how many days of basic living an agent's accessible resources cover, rather than a raw income or wealth snapshot. See the [BLEI paper](https://bettertobest.github.io/research-hub/basic-living-economic-index.html) for the full framework, and the Replication Framework for the current formulas as implemented.

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

The simulation itself documents its own current controls, presets, calibration constants, and known limitations in-app — see the collapsible **Assumptions, ODD Protocol & Known Limitations** and **References & Citations** panels at the bottom of the page, which are kept in sync with the shipped code.

---

## Where to find version-specific information

This README intentionally stays stable across releases. For anything tied to a specific version:

- **What changed, and when** — the [Replication Framework's Version History](https://bettertobest.github.io/research-hub/cco-ptf-simulation-replication.html) has the full line-by-line changelog, in chronological order, for every release.
- **Current output metrics and large-N study results** — the Replication Framework's Performance Comparison section, refreshed after any mechanics-changing release.
- **Formulas as currently implemented** — the Replication Framework's Mathematical Framework section, and the simulation's own source comments.
- **Open questions, known limitations, and how to contribute** — [CONTRIBUTING.md](https://github.com/BetterToBest/compassionism-simulation/blob/main/CONTRIBUTING.md), which tracks unresolved calibration items, model-architecture feedback, and good-first-issues.

---

## License & attribution

Released under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

**Cite as:**
> Johnson, D. & Claude (Anthropic). *Compassionism Framework Simulation*. Better To Best Research Hub. CC BY 4.0. <https://doi.org/10.17605/OSF.IO/QWTE2>

The DOI resolves to the archived record; cite the specific version and date you used alongside it if that matters for your purposes (the simulation's own footer and export files record the version and timestamp of any given run).

**Research Hub:** [bettertobest.github.io/research-hub](https://bettertobest.github.io/research-hub/)
**Wiki:** [bettertobest.github.io/research-hub/wiki](https://bettertobest.github.io/research-hub/wiki/)
**BLEI Paper:** [basic-living-economic-index.html](https://bettertobest.github.io/research-hub/basic-living-economic-index.html)
**Replication Framework:** [cco-ptf-simulation-replication.html](https://bettertobest.github.io/research-hub/cco-ptf-simulation-replication.html)
**Contributors' Guide:** [CONTRIBUTING.md](https://github.com/BetterToBest/compassionism-simulation/blob/main/CONTRIBUTING.md)
**DOI:** [10.17605/OSF.IO/QWTE2](https://doi.org/10.17605/OSF.IO/QWTE2)
**Contact:** BetterToBestResearch@gmail.com
