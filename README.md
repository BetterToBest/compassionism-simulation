# Walk-through: the Compassionism Framework Simulation (v4.22)

<!-- Written by walkthrough/make_walkthrough.py. Edit the captions there and rebuild; edits here are overwritten. -->

[![The walk-through video](img/poster.jpg)](https://bettertobest.github.io/compassionism-simulation/walkthrough/walkthrough.mp4)

**[Watch the walk-through](https://bettertobest.github.io/compassionism-simulation/walkthrough/walkthrough.mp4)** (6:22, narrated by a synthetic voice, with captions; [caption file](captions.vtt)). The same tour follows as text, one screenshot per step.

It covers what the page shows, how Compassionism works, what the model finds so far, how to run a scenario, how to check the work, and how to help. Every figure below is read from the page's own comparison data when the tour is built (`python3 walkthrough/make_walkthrough.py`), so it matches the page it was built from. The figures are results of the model under its stated assumptions, not forecasts.

## 1. What the page is for

![The page's opening sentence, highlighted](img/01-headline.png)

The first screen says what the tool is for: set Compassionism beside five other anti-poverty designs and see how each does on poverty and work.

![The subtitle: the rules every design shares, highlighted](img/02-rules.png)

Every design runs on the same 500 simulated adults for 20 years, is paid for the same way, and faces the same rules for how people respond.

![The "Read this first" caveats box, highlighted](img/03-caveats.png)

Read this first: it is an exploratory model, not a forecast. Its results show what its assumptions imply, not that the assumptions are true.

## 2. How Compassionism works

![The design panel's description of Compassionism, highlighted](img/04-design.png)

Each participant receives a monthly allowance of Basic Units (BU): a restricted currency for essentials that expires if it is not used. BU can be converted to dollars at elevated rates, set by market demand and by the quality of work the community validates through creative collectives. A participant's octave is their conversion capacity: a safeguard against exploitation, and an open ceiling for creators whose work draws demand. Wage work is still paid in dollars. Community-owned businesses and housing (PTF, PTH) lower living costs, zone coordination (SZH) adds a cooperative benefit, and a civic portal (CIP) runs the currency and the votes. Taking part is open to every adult. In the model, 78% do at the reference settings, and each adult's choice holds for all 20 years.

## 3. Reading the comparison

![The comparison table at reference settings and equal cost, with Compassionism's row marked](img/05-table.png)

Each row is a design. Cost is per adult per year, shown with the wage contribution that pays for it and the change in poverty per $1,000.

![The comparison table with the poverty-severity tooltip open](img/06-measure.png)

The main measure is poverty severity: each adult's shortfall below a living-wage basket, squared so the deepest count most, averaged over 20 years. Beside it: the final year alone, the share of adults in poverty, hours worked, and any group left worse off than with no program.

![The table's controls, highlighted](img/07-controls.png)

The controls switch the environment, compare the designs at equal cost or at the size their proponents propose, and model Compassionism as coded or as specified on the Hub.

![The proposed-size view, with the basic income and negative income tax rows marked](img/08-proposed.png)

At proposed size, the basic income pays $12,000 a year and the negative income tax guarantees the 2026 poverty guideline for one adult, $15,960.

## 4. What the model finds so far

![Compassionism, basic income and negative income tax rows marked, reference settings](img/09-headline-result.png)

At the reference settings and equal cost, Compassionism as coded cuts poverty severity by 3.21 points, against 1.60 for a basic income and 2.30 for a negative income tax.

![Compassionism's row and the shaded row without its two theoretical mechanisms, marked](img/10-mechanisms.png)

The shaded row switches off two mechanisms that are theoretical, yet to be empirically tested, and cost nothing in the model: a yearly wage raise per octave, and slower inflation. At reference, with no inflation, only the wage raise acts. Without it the cut falls from 3.21 to 1.78, about 45% less.

![The same two rows in the Adverse Environment](img/11-adverse.png)

In the Adverse Environment, with recessions and 2% inflation, the two carry about 79% of the cut: 7.67 falls to 1.62. The next round replaces them or switches them off.

![The mechanisms-off row and the basic income row, marked](img/12-without.png)

Without them, Compassionism still does better than a basic income of equal cost, in all three environments.

![The mechanisms-off row and the negative income tax row, marked](img/13-nit.png)

The negative income tax cuts severity more at reference, 2.30, by focusing on the deepest shortfalls, but it raises the share in poverty from 55% to 81% and cuts hours by 22%.

![Compassionism's row and the needs-based top-up row, marked](img/14-topup.png)

A variant that moves a tenth of the flat allowance into a top-up for low earners cuts a little more: 3.38.

![The worse-off cells for Compassionism and the basic income, marked](img/15-who-pays.png)

Someone always pays. Each design is funded by a contribution on wages; under Compassionism the cost falls mainly on adults who chose not to take part, about $5,800 a year.

![Compassionism as specified on the Hub, marked](img/16-hub-scale.png)

At the scale specified on the Hub, Compassionism costs about $32,000 per adult a year, which would take a contribution of 61% of wages.

![The caveats box, highlighted](img/17-limits.png)

What the model cannot test: whether conversion rewards pay for new output (it has no production side), households and children, or savings from poverty removed.

## 5. Run a scenario yourself

![The live tab's scenario presets, highlighted](img/18-live.png)

Compassionism's own scenarios run live in your browser: pick a preset, or change any control and press Run Simulation.

![The live simulation: controls on the left, results on the right](img/19-results.png)

Each run follows 500 adults year by year and reports poverty, wealth and the BLEI: how many days of basic living each adult's resources cover.

![The Poverty by five measures panel](img/20-panels.png)

Panels below show poverty by five measures, BLEI tiers over time, participants beside non-participants, and what each system contributes. These live runs use the engine's own settings, not the comparison's testbed profile, so their figures differ from the table's.

![The Assumptions, ODD Protocol and Known Limitations panel, highlighted](img/21-assumptions.png)

At the foot of the page: the assumptions, the ODD protocol, known limitations and references.

## 6. Check the work

![The Replication framework page](img/22-replication.png)

The Replication framework page holds the formulas, the calibration and the full version history.

```
git clone https://github.com/BetterToBest/compassionism-simulation
cd compassionism-simulation && npm install
npm test                              # validate, unit and domtest
node harness.js testbed 500 a5 ref    # the comparison table, reference environment
```

The simulation is one HTML file. harness.js runs the same engine from the command line; the comparison table comes from node harness.js testbed 500 a5 ref. npm test runs the three checks, validate, unit and domtest, and GitHub runs them on every push.

## 7. Help improve it

Ways to contribute, from [CONTRIBUTING.md](../CONTRIBUTING.md#how-to-contribute): scenario testing (the highest-value contribution), calibration with cited sources, reproducibility testing, model architecture feedback, code, and peer review.

Contributions most wanted: sources for the untested constants, scenario tests from places you know, reproductions, and critiques of the design. Changes follow the project rules: the old behaviour stays behind a switch, results are compared on 500 paired seeds, and no constant is tuned to hit a target. Open an issue or a pull request on GitHub. CONTRIBUTING.md explains how.

## Links

- Simulation: https://bettertobest.github.io/compassionism-simulation/
- Code and checks: https://github.com/BetterToBest/compassionism-simulation
- Replication framework: https://bettertobest.github.io/compassionism-simulation/replication.html
- Archive: https://doi.org/10.17605/OSF.IO/QWTE2
