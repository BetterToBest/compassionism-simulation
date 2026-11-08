# Synergy report (S36): what each part of the design contributes, and whether the parts work together

**Full study batch.** Every figure here comes from the preregistered batch: seeds 1-500, run once as frozen. These are not pilot figures.

- Preregistration: research-update `prereg/2026-11-study-program.md` (question Q2, the Analysis section, decision rules 2, 3, 6 and 7), with Amendments 4 (the C2.2 design is the headline design), 9 (the design freeze; materiality for inflation read on the yearly rate) and 10 (the frozen spending share). How the rows are built: research-update `prereg/run-manifest.md`, section 3 (B and B10).
- Engine: `ce8d030b8d16a752706c4ea2db71196e11e73831`, the frozen engine (the outside audit's three corrections, the second implementation's four fixes, the re-derived spending share) on every row, the no-programme rows included.
- Results: BetterToBest/compassionism-sim-results, folders `prog-b-ce8d030` (study B, 500 adults, 20 and 40 years) and `prog-b10-ce8d030` (study B10, 10,000 adults, 20 years). Each has `run.txt` (the exact command and its workflow run), `SHA256SUMS` and `DONE`.
- Every table behind this report: `dev/runs/s36-synergy/tables.md`. Every estimate with its interval and flags (about 25,600): `dev/runs/s36-synergy/estimates.csv`. Both are written by `python3 dev/tools/s36_synergy.py <compassionism-sim-results checkout> dev/runs/s36-synergy` (about 30 seconds).
- Checks the script makes before any table (all pass, `tables.md` section 0): the cells without the CCO are identical under the two designs; the first 20 years of every 40-year row equal the 20-year row; study B's full-design and no-programme rows equal study A's at 500 adults, every key and seed; the Shapley values add up to the full design's effect on every seed.

## The words used here

- **The five parts:** the CCO (the Basic Unit paid by the Source, with its octaves), PTF (the merchant network), PTH (the housing arm), SZH (the zones), CIP (the community investment programme).
- **The C2.2 design** (headline, Duke's answer to ledger decision D8): a Basic Unit that covers food, housing with utilities and medical care for one adult ($1,788.43 a month), indexed to those prices, paid automatically to every resident. **The release design** ($1,200 a month, opt-in, as published in v5.6) is shown beside it.
- **Outcomes:** *basic living*: the share of adult-years with fewer than 30 days of basic living, on the design-neutral reading (the design's own reading credits SZH with days no one can spend; it is shown in the tables and never claimed); *cost of living*: the share of adult-years with income below the MIT living-wage budget; *wealth*: the share of adults with wealth below $25,000 in year-0 prices, at year 20 or year 40; *cost*: programme cost per adult-year; *inflation*: the model's yearly price rise implied by the price level at year 20 or 40 (cumulative inflation is in the tables too, as preregistered).
- **Effects** are each row against the no-programme run of the same seed. For the three shares, a reduction is a positive number of percentage points ("points").
- **Shapley value:** a part's average added effect over every order in which the five parts could be switched on. The five values add up exactly to the full design's effect.
- **Interaction contrast:** how far the parts' joint effect differs from the sum of their separate effects. The *whole-design contrast* is the full design's effect minus the five single-part effects. A *pair contrast* (for example CCO × CIP) is how much more one part adds when the other is there, with the remaining three on. For the shares, a positive contrast is **synergy** (together they cut the share by more than the sum); a negative one is **overlap** (together they do less than the sum). For cost and inflation, a positive contrast means more cost or more inflation together, so negative is the favourable direction.
- **The rule for a synergy claim** (research rule 4, decision rule 2): the contrast's 95% interval excludes zero. It is called **material** only if it is also at least 1 point (shares), 5% of the full design's cost, or 1 point of the yearly inflation rate. Holm's correction over each outcome's 11 contrasts is stated beside it (in this batch every material contrast also survives Holm).
- Intervals are 95% paired-bootstrap intervals over seeds (10,000 replicates, bootstrap seed 20261101).

## The short answers

1. **The CCO is almost the whole effect.** In the headline cell (C2.2 design, Reference, 500 adults, 20 years, CPS yardstick, raise off), the CCO accounts for 98% of the gain in basic living (17.23 of 17.55 points) and 96% of the gain on the cost of living (23.56 of 24.52 points). Under the C2.2 design its share is 97-100% for basic living and 93-99% for the cost of living in every one of the 24 settings of study B. CIP is the second part (0-3% and 1-6%). Under the C2.2 design PTF, PTH and SZH each move basic living and the cost of living by at most 0.15 and 0.33 points in any setting (0.52 and 0.97 under the release design).
2. **On basic living and the cost of living, the parts overlap; they do not reinforce each other.** The whole-design contrast is negative in every one of the 24 C2.2 settings: basic living −0.25 to −0.63 points at 20 years (never material) and −0.36 to −1.53 at 40 years (material in 7 of 12, all in Reference and Adverse); the cost of living −0.84 to −2.18 points at 20 years (material in 8 of 12) and −1.03 to −3.93 at 40 years (material in all 12). Nearly all of it is CCO × CIP: both raise the same low incomes, so once the Basic Unit has lifted someone over the line, CIP's income lifts fewer people over it. Under the C2.2 design no setting shows a material synergy on basic living. The only material synergies on basic living or the cost of living anywhere in the batch are in one corner: Adverse, 40 years, released-wage yardstick (CCO × PTH on the cost of living, +1.1 to +1.6 points; under the release design also CCO × CIP on basic living, +1.1 to +1.3). None is in the headline yardstick.
3. **Wealth: the largest interactions, and none robust.** The programme raises the share with low wealth in most cells, because its inflation erodes savings (C2.2, Reference, year 20: −0.33 points [−0.56, −0.11], that is, slightly more adults with low wealth; release design −21.3 points). The pair contrasts on wealth are the largest in the batch. At 20 years with the CPS yardstick and the raise off, in Reference and Adverse: under the C2.2 design CCO × PTH +2.3 and +2.7 points (PTH's housing offsets part of the CCO's wealth loss), PTF × CIP +1.1 and +1.7, and CCO × CIP −1.5 and −1.1; under the release design CCO × CIP +2.7 and +1.6. But their sign and materiality change with the octave raise, the yardstick, the design and the horizon (section 4 below). No wealth synergy holds across settings, so none is stated as a finding.
4. **Inflation: the parts together inflate a little less than the CCO alone.** The whole-design contrast on the yearly rate is −0.85 to −4.28 points a year under the C2.2 design (material in 18 of 24 settings) and −0.41 to −3.82 under the release design (material in 19 of 24). Under the C2.2 design it is mostly CCO × PTH (−0.65 to −4.56 points, material in 19 of 24; a likely reading, not tested here: PTH holds down housing costs, and the C2.2 Basic Unit is indexed to them); under the release design, CCO × CIP. This is small beside the full design's own effect: 26 to 89 points a year of inflation under the C2.2 design and 15 to 73 under the release design, across study B's settings.
5. **Cost:** the whole-design contrast is never material (under 5% of the full design's cost). One pair is, in 3 of 24 C2.2 settings: CCO × CIP lowers the cost by about 5% ($3,165 per adult-year [3,133, 3,197] in the headline cell).
6. **SZH never matters.** No contrast involving SZH is material on any claimable outcome in any setting, and its Shapley value on design-neutral basic living is 0.00 in the headline cell. It counts only in the design's own BLEI reading (0.24 points there), which is not claimed.
7. **Population size changes nothing.** At 10,000 adults (study B10) against 500, none of 510 comparisons (every contrast, Shapley value and full effect on the claimable outcomes, both designs, three environments) passes the preregistered scale rule. The intervals narrow; the table does not change. The headline figures can therefore be read at 500 adults.
8. **What replaces the Hub's "0.42 / 0.28 / 0.18 / 0.12".** That split (direct transfers, work incentive, social recognition, community effects) named no welfare measure and no method (audit A08; it survives only in an old PDF). Its four categories are not separate mechanisms in this engine, so it cannot be recomputed in its own terms. What the engine can compute is the split by the design's five parts, which is the table in the next section. A one-line replacement for the Hub, if one is wanted: *"In the simulation, the CCO accounts for about 98% of the design's effect on basic living and 96% of its effect on the cost of living; CIP 1-3%; PTF, PTH and SZH under 1% each (C2.2 design, Reference environment, 20 years, Shapley values, 500 seeds). The parts overlap rather than reinforce each other on these outcomes."* It lands through the corrections package (S24) and the paper bodies (S25).

## 1. The headline table

C2.2 design, Reference, 500 adults, 20 years, CPS yardstick, octave raise off. Shapley values in points ($ for cost), with the share of the full effect.

| Outcome | Full design | CCO | PTF | PTH | SZH | CIP |
|---|---|---|---|---|---|---|
| Basic living (points) | 17.55 [17.44, 17.66] | 17.23 (98%) | 0.03 (0%) | 0.04 (0%) | 0.00 (0%) | 0.25 (1%) |
| Cost of living (points) | 24.52 [24.36, 24.69] | 23.56 (96%) | 0.05 (0%) | 0.13 (1%) | 0.01 (0%) | 0.78 (3%) |
| Wealth at year 20 (points) | −0.33 [−0.56, −0.11] | −1.20 | −0.66 | +1.26 | +0.10 | +0.17 |
| Cost ($ per adult-year) | 60,494 [60,431, 60,555] | 60,384 (100%) | 487 (1%) | 1,204 (2%) | 81 (0%) | −1,662 (−3%) |
| Inflation, yearly rate (points) | 35.08 [34.99, 35.18] | 35.58 (101%) | 0.20 | −0.54 | −0.03 | −0.12 |

Interaction contrasts, same cell (points; $ for cost). Material ones in bold.

| Outcome | Whole design | CCO × PTF | CCO × PTH | CCO × CIP | PTF × CIP | PTH × CIP |
|---|---|---|---|---|---|---|
| Basic living | −0.55 [−0.58, −0.52] | −0.09 | −0.02 | −0.46 | 0.00 | 0.00 |
| Cost of living | **−1.66 [−1.69, −1.63]** | −0.18 | 0.03 | **−1.55 [−1.57, −1.53]** | 0.02 | −0.01 |
| Wealth at year 20 | **−1.04 [−1.15, −0.93]** | −0.97 | **+2.28 [2.19, 2.36]** | **−1.46 [−1.55, −1.37]** | **+1.10 [1.02, 1.17]** | −0.48 |
| Cost ($) | −2,184 | 593 | 829 | **−3,165 [−3,197, −3,133]** | 826 | −306 |
| Inflation, yearly rate | −0.95 [−0.96, −0.94] | 0.30 | **−1.07 [−1.08, −1.06]** | −0.29 | −0.17 | 0.07 |

The four contrasts with SZH and PTF × PTH are within ±0.3 points on every share outcome and are in `tables.md`. The wealth row's Shapley values have no shares: the full effect is close to zero, so shares of it would run to several hundred percent.

**The release design, same cell:** basic living 9.06 points (CCO 93%, CIP 6%, PTH 2%); cost of living 16.58 (CCO 92%, CIP 6%); wealth −21.29 (the CCO alone −25.11; CIP +2.37 offsets a little); cost $32,755; inflation 29.65 points a year. The whole-design contrast is +0.06 on basic living (not material), −1.07 on the cost of living (material overlap), +2.65 on wealth (material, from CCO × CIP +2.74), and −1.44 on inflation (material).

## 2. Across environments and horizons (C2.2 design, CPS yardstick, raise off)

| Environment, horizon | Basic living: full effect; CCO share; whole-design contrast | Cost of living: full; CCO share; whole design | Wealth: full; whole design | Inflation a year: full; whole design |
|---|---|---|---|---|
| Reference, 20 years | 17.55; 98%; −0.55 | 24.52; 96%; −1.66 | −0.33; −1.04 | 35.08; −0.95 |
| Adverse, 20 years | 21.05; 98%; −0.63 | 35.18; 97%; −1.98 | −29.48; +0.11 (not detected) | 41.92; −1.07 |
| Stress, 20 years | 20.81; 99%; −0.32 | 34.46; 98%; −0.96 | −41.09; +0.54 | 43.73; −0.90 |
| Reference, 40 years | 18.52; 97%; −1.15 | 21.85; 93%; −2.56 | +9.32 (year 40); +1.85 | 32.51; −1.32 |
| Adverse, 40 years | 27.07; 97%; −1.45 | 42.16; 95%; −3.65 | −42.08; +1.09 | 47.38; −2.22 |
| Stress, 40 years | 25.83; 98%; −0.66 | 40.12; 97%; −1.64 | −49.53; +0.02 (not detected) | 52.59; −1.50 |

All full effects and all whole-design contrasts not marked otherwise have 95% intervals that exclude zero. In Adverse and Stress the programme raises the share of adults with low wealth by 29 to 50 points: the wealth "synergies" there are the other parts softening that loss slightly. The 40-year statements hold without ageing only (study B has no ageing; decision rule 4 asks for a 40-year statement to hold with ageing too, and the ageing study C has no factorial).

**How often each interaction is material** (24 settings of study B per design: 3 environments × 2 horizons × 2 yardsticks × raise off and on; + synergy, − overlap or, for inflation, less inflation together):

| Design | Contrast | Basic living | Cost of living | Wealth | Cost | Inflation a year |
|---|---|---|---|---|---|---|
| C2.2 | whole design | 0+ / 7− | 0+ / 20− | 6+ / 5− | 0 | 0+ / 18− |
| C2.2 | CCO × PTH | 0 | 2+ / 0− | 15+ / 0− | 0 | 0+ / 19− |
| C2.2 | CCO × CIP | 0+ / 8− | 0+ / 22− | 3+ / 13− | 0+ / 3− | 2+ / 0− |
| C2.2 | PTF × CIP | 0 | 0 | 7+ / 0− | 0 | 0+ / 1− |
| release | whole design | 1+ / 0− | 0+ / 15− | 13+ / 4− | 0 | 0+ / 19− |
| release | CCO × CIP | 2+ / 0− | 0+ / 15− | 11+ / 6− | 0 | 0+ / 10− |

(Also material, rarely: CCO × PTF on wealth (1 C2.2 setting, 3 release), on the cost of living and on inflation (1 release setting each); CCO × PTH on the cost of living under the release design (1); PTH × CIP on wealth under C2.2 (1). Every other pair, and every pair with SZH, is never material.)

## 3. Scale: 10,000 adults against 500 (Q1)

Study B10 ran the 32-cell factorial at 10,000 adults (20 years, CPS yardstick, raise off). Contrast by contrast, Shapley value by Shapley value, none of 510 differences from 500 adults passes the scale rule (it must exceed both its Monte Carlo error and the materiality threshold). Example, the C2.2 design in Reference: the whole-design contrast on the cost of living is −1.66 [−1.69, −1.63] at 500 adults and −1.64 [−1.65, −1.63] at 10,000. **In this engine, a larger population narrows the intervals and changes no conclusion of the synergy table.** This engine has no mechanism that depends on population size or local density; the community and zone layer (S37), which adds one, is tested in its own studies and reported separately (S38).

## 4. How robust the decisions are (Q5, Q6, the design, the horizon)

Each preregistered rule asks whether a decision changes with a setting. Counted over the 11 contrasts of every claimable outcome (`tables.md` sections 4-8 list each one):

| Comparison | Contrasts compared | Decision changes | Of which a material synergy is gained, lost or changes sign |
|---|---|---|---|
| Octave raise on against off (decision rule 6) | 1,320 | 164 | 42 |
| Released wages against CPS earnings (rule 7) | 1,320 | 237 | 71 |
| Release design against C2.2 design | 1,485 | 359 | 133 |
| Year 40 against year 20, same 40-year runs (rule 4: change of at least 1 point, interval excluding zero) | 528 | 49 pass | |

- The material changes are almost all on **wealth** and on **inflation**. On basic living and the cost of living the conclusion (overlap, mostly CCO × CIP; no synergy in the headline yardstick) holds in every comparison.
- On wealth, the whole-design contrast changes sign with the raise in 40-year cells and with the design in 20-year cells (for example, Reference at 20 years: −1.04 under C2.2, +2.65 under the release design). This is why no wealth synergy is stated.
- On inflation, CCO × PTH is material under the C2.2 design (the Basic Unit is indexed to the housing price that PTH lowers) and not under the release design ($1,200, not indexed).
- Over the horizon, 39 of the 49 changes that pass are wealth contrasts, growing or shrinking by more than a point in both directions. The other 10 are on inflation, all more negative at 40 years (the whole-design contrast in 6 settings).

The headline statements above already carry these qualifications (decision rules 6 and 7 ask the headline sentence to say where a decision differs).

## 5. Pilot to batch

The pilots (S35, 50 seeds, the published engine) found the same pattern: the CCO about 93-97% of the effect, PTF, PTH and SZH near inert, the material interactions mostly CCO × CIP. The batch differs from the pilots in two ways at once: new seeds (1-500 against 1-50) and the frozen engine's corrections (the audit's, the second implementation's, and the spending share of 0.877 in place of 0.593). The largest change is on wealth: with the re-derived spending share, households save less, so the programme's inflation leaves more of them with low wealth, and the release design's wealth effect turns from a gain (pilot: 3.95 points) to a loss (−21.3). A pilot-to-batch difference cannot be split between the two causes from these folders; study R measures the corrections on their own.

## 6. What this does and does not show

- The synergy argument for the framework rests partly on local density (PTF merchant networks, SZH zones, PTH communities). Without the community layer, the engine has no mechanism through which PTF, PTH or SZH could reinforce the CCO on basic living or the cost of living, so the null on those three parts is a finding about this engine, not a test of that argument. The layer's own factorial (studies G and G10) is the test, reported in S38.
- The overlap between the CCO and CIP is a direct consequence of how both are modelled: both add income, and a share below a line can fall only once per person. The engine does not model the non-income channels the Hub attributes to CIP.
- 40-year results are without ageing (nobody grows older, retires or dies).
- Everyone in the model works; there is no part-time work; the engine has no child and dependent care credit (limits carried from S34).
- Every cell is published: all 54 settings (both designs, three environments, both horizons, both yardsticks, raise off and on, and 10,000 adults) are in `tables.md`, and every estimate, the secondary terms (the 26 Harsanyi dividends and the averaged two-way contrasts) included, is in `estimates.csv`.
