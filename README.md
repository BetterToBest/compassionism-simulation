# Compassionism Framework Simulation

**Compassionism aspires to enhance cultures by eradicating extreme poverty while incentivizing participation and contribution: see how it does.**

_The math and code of this simulation were engineered by Claude, an AI model made by Anthropic, from the concepts in Duke Johnson's book *Better To Best* and his related vision for eradicating extreme poverty while enriching cultures and supporting human flourishing. The model has not yet been reviewed by an independent economist; the full code is open for anyone to check, and expert collaborators are welcome._

**What it is.** A dynamic microsimulation with a reduced-form price level, open and running in the browser. It follows 500 simulated US adults and their children, in households built from the 2022 Survey of Consumer Finances and the Census's CPS, for 20 or 40 years, once with Compassionism (all five [Research Hub](https://bettertobest.github.io/research-hub/) architectures) and once with no programme, on the same random draws, in three environments (Reference, Adverse, Stress). The programme's institutions, firms and the government are aggregate flows, and prices move by one rule for the whole economy. The current release is **v5.9** (frozen and registered on OSF before it ran, Nov 14, 2026); every figure averages 500 paired runs, with its 95% interval.

**What v5.9 finds, both sides** (Reference, 20 years, the full-coverage design, built to meet NEEC's criterion C2.2, against no programme):
- Adult-years below 30 days of basic living: 0.9% against 19.6%. Below the cost of living: 3.7% against 36.1%. Too little wealth: 6.0% against 24.6%. Median real wealth at year 20: $432,300 against $223,900. Across all 62 preregistered readings, both designs lower all three poverty measures and raise median wealth, in every environment and at both horizons.
- **These results hold only if every dollar the programme pays is matched by new output**, which is the design's statement and not something the model shows: the model's own mechanism reaches about 1% of it, and there prices rise 15 to 53 points a year. Below full backing the model has no limit on what the economy can supply, which is why the poverty effects barely move with backing.
- Fewer adults work (participation falls 1 to 5 points); labour's share of money income falls; fewer adults leave the lowest wealth fifth; the opt-in design loses about two thirds of its effects in Stress; paid for by a contribution instead, 46 of 48 poverty and wealth results are fragile. With a central bank (a study on 100 paired runs), the programme makes the basket's price and dollar incomes swing more, while it cuts the share pushed below the cost of living in a recession year.

**What it is not.** Not a forecast and not a backtest. No limit on supply below full backing, no expectations, no migration, a fixed population (no ageing) in the main row, no value of care or community work. It measures poverty, cost and work, not the cultural effects Compassionism aspires to, and poverty is measured against a living-wage basket, a higher bar than extreme poverty. The one-page [model card](https://bettertobest.github.io/compassionism-simulation/model-card.html) says what the model is and is not; [ODD.md](ODD.md) and [MODEL_SPEC.md](MODEL_SPEC.md) describe it in full; [REPRODUCE.md](REPRODUCE.md) regenerates every figure; [ECONOMIST-REVIEW.md](ECONOMIST-REVIEW.md) is the checklist for an outside reviewer.

**[▶ Open the simulation](https://bettertobest.github.io/compassionism-simulation/)** · **[The findings, chart by chart](https://bettertobest.github.io/compassionism-simulation/findings.html)** · **[The model card](https://bettertobest.github.io/compassionism-simulation/model-card.html)** · DOI: [10.17605/OSF.IO/QWTE2](https://doi.org/10.17605/OSF.IO/QWTE2)

## The pages

The page opens with Compassionism's results. It follows the same 500 simulated adults and their children, living in households, who can lose their jobs and find new ones. It runs them for 20 years (or 40, with the Years switch), once with the program and once with no program, in three environments (Reference, Adverse, Stress). Basic living covered leads: the BLEI measure, the days of basic living that a person's savings, income and Basic Units together cover (a measure of capacity, not cash on hand). One plain sentence each follows on poverty, savings, children, who gains, work, prices, cost and how it is paid, and the public costs of homelessness avoided. Prices are given as the typical run with the range of eight runs in ten (the 10th to 90th percentile). Above 1,000 times today's prices, the page describes the figure as a limit of the model's price rule, not a forecast. A table sets the Research Hub's own Year 7 targets (poverty under 2%, Gini coefficient 0.25 to 0.30) beside what the model reaches. Every figure is an average over 500 paired runs, with its 95% interval, and the page names the command that reproduces it. A button runs the model live in the browser. The model measures poverty, cost and work, not the cultural effects Compassionism aspires to. Poverty is measured against a living-wage basket, a higher bar than extreme poverty.

Since v5.2.1 the results are guided sections under one control strip (environment, 20 or 40 years, with or without Compassionism). The sections are: the answer in ten seconds; one run's 500 adults with their life paths; how poverty moves over time; who gains; families and children; jobs, community homes and shops, and how risky life is (v5.4); what each part does; what it costs and who pays; how sure we are; and run it yourself. Every result, chart by chart and table by table, with every earlier release, is on the **[findings explorer](https://bettertobest.github.io/compassionism-simulation/findings.html)**. Every number on the pages comes from one data file per release (`data/releases/`, listed in `data/manifest.json`); `dev/ADDING-A-RELEASE.md` says how to add the next one.

The narrated walk-through is off the page while the model is still changing (it showed an earlier version); it comes back, re-recorded, once the simulation is settled.


[![checks](https://github.com/BetterToBest/compassionism-simulation/actions/workflows/checks.yml/badge.svg)](https://github.com/BetterToBest/compassionism-simulation/actions/workflows/checks.yml)

This file covers what the project is and how to run it. For everything version-specific — the full changelog, current output metrics, methodology, and formulas — see the **[Replication Framework](https://bettertobest.github.io/compassionism-simulation/replication.html)**, which is kept current with each release. For open questions, known limitations, and how to contribute, see **[CONTRIBUTING.md](https://github.com/BetterToBest/compassionism-simulation/blob/main/CONTRIBUTING.md)**.

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

Welfare outcomes are measured against the **Basic Living Economic Index (BLEI)** — a temporal-stability metric expressing how many days of basic living a person's savings, income and Basic Units together cover (a measure of capacity, not cash on hand), rather than a raw income or wealth snapshot. See the [BLEI paper](https://bettertobest.github.io/research-hub/basic-living-economic-index.html) for the full framework, and the Replication Framework for the current formulas as implemented.

---

## How to use

**No Python. No installation. Just open `index.html` in any browser.** The earlier engine (v4.22, with its own settings, presets and charts) is on its own page, `earlier-engine.html`, linked from the front door as "Explore the earlier engine".

### Option A — Open locally
1. Download the repository (or at least `index.html`, the `site/` and `data/` folders, and `earlier-engine.html` for the earlier engine). `index.html` alone still shows every result and runs the model; the guided sections' charts need `site/`, and the spread across runs and the 500 adults need `data/` served by a web server (browsers do not let a page opened as a file read other files; `python3 -m http.server` in the folder is enough)
2. Double-click — opens in Chrome, Firefox, Safari, or Edge
3. Read the results, or press **Run it yourself**; the earlier engine's controls and **Run Simulation** are on `earlier-engine.html`

### Option B — Host on GitHub Pages
1. Upload `index.html`, `findings.html`, `earlier-engine.html`, `replication.html` and the `site/` and `data/` folders to your repository root
2. Go to **Settings → Pages → Source → main branch / root**
3. Live at `https://yourusername.github.io/compassionism-simulation/`

The simulation itself documents its own current controls, presets, calibration constants, and known limitations in-app — see the collapsible **Assumptions, ODD Protocol & Known Limitations** and **References & Citations** panels at the bottom of the earlier engine's page (`earlier-engine.html`), which are kept in sync with the shipped code.

---

## Where to find version-specific information

This README intentionally stays stable across releases. For anything tied to a specific version:

- **What changed, and when** — the [Replication Framework's Version History](https://bettertobest.github.io/compassionism-simulation/replication.html) has the full line-by-line changelog, newest first, for every release; each release's detailed notes are in [CHANGELOG.md](https://github.com/BetterToBest/compassionism-simulation/blob/main/CHANGELOG.md) (the current release's in CONTRIBUTING.md).
- **Current results** — the [findings explorer](https://bettertobest.github.io/compassionism-simulation/findings.html), every table with CSV and JSON downloads, drawn from one data file per release (`data/releases/`). (The Replication Framework's Performance Comparison section holds the earlier v4.22 engine's large-N figures, as history.)
- **The model as implemented** — [MODEL_SPEC.md](MODEL_SPEC.md) (the release model only: what is simulated, the order of events in a year, every submodel, the random streams, what each headline measures), [TESTBED_SPEC.md](TESTBED_SPEC.md) (every switch and labeled reading, with its status and the decision that set it), [ODD.md](ODD.md) (the ODD protocol, with each parameter's basis) and [REPRODUCE.md](REPRODUCE.md) (the command, file and fingerprint behind every published table). The Replication Framework's Mathematical Framework section describes the earlier v4.22 engine.
- **How to cite** — [CITATION.cff](CITATION.cff) (GitHub's "Cite this repository" reads it).
- **Open questions, known limitations, and how to contribute** — [CONTRIBUTING.md](https://github.com/BetterToBest/compassionism-simulation/blob/main/CONTRIBUTING.md), which tracks unresolved calibration items, model-architecture feedback, and good-first-issues.

---

## Checking a copy

The simulation needs nothing installed. The checks that keep it honest need Node.js (22 or later) and one development dependency:

```
npm ci                   # installs jsdom (pinned in package-lock.json), used only by domtest.js
node harness.js validate # the seed-42 reference run, asserted against the documented figures
node harness.js unit     # pure-function tests
node domtest.js          # drives index.html in a headless DOM (a few minutes)
```

Every `harness.js` study mode also accepts `--agents=N`, the population per run (default 500). For example, `node harness.js largen 500 headline --agents=5000` reruns the headline figures at 5,000 agents per run, in about five minutes on one CPU core.

The same three run automatically on every push (`.github/workflows/checks.yml`). CONTRIBUTING.md explains what each covers and what none of them can see. Today `unit` runs <!-- count:unit -->395<!-- /count --> tests and `domtest` <!-- count:domtest -->162<!-- /count --> checks; each run fails if these numbers are stale, and `--write-counts` (for either) refreshes them.

---

## License & attribution

Split licensing, since v4.8:

- **Source code** (`index.html`, `harness.js`, `domtest.js`) — [Apache License 2.0](LICENSE-CODE.txt).
- **Documentation and papers** (this README, CONTRIBUTING.md, the Replication Framework, and the Research Hub papers) — [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

**Cite as:**
> Johnson, D. & Claude (Anthropic). (2026). *Compassionism Framework Simulation*. Better To Best Research Hub. <https://doi.org/10.17605/OSF.IO/QWTE2> (source code: Apache License 2.0; content and documentation: CC BY 4.0)

The DOI resolves to the archived record; cite the specific version and date you used alongside it if that matters for your purposes (the simulation's own footer and export files record the version and timestamp of any given run).

**Research Hub:** [bettertobest.github.io/research-hub](https://bettertobest.github.io/research-hub/)
**Wiki:** [bettertobest.github.io/research-hub/wiki](https://bettertobest.github.io/research-hub/wiki/)
**BLEI Paper:** [basic-living-economic-index.html](https://bettertobest.github.io/research-hub/basic-living-economic-index.html)
**Replication Framework:** [replication.html](https://bettertobest.github.io/compassionism-simulation/replication.html)
**Contributors' Guide:** [CONTRIBUTING.md](https://github.com/BetterToBest/compassionism-simulation/blob/main/CONTRIBUTING.md)
**DOI:** [10.17605/OSF.IO/QWTE2](https://doi.org/10.17605/OSF.IO/QWTE2)
**Contact:** BetterToBestResearch@gmail.com
