# Community-layer report (S38): does reading the Hub's density tests in each community change the results?

**Full study batch.** Every figure here comes from the preregistered batch: seeds 1-500, run once as frozen. These are not pilot figures, and no pilot of these rows was run.

- Preregistration: research-update `prereg/2026-11-community-layer.md` (questions Q7-Q10, decision rules 1-6), with its Amendment 1 (the frozen engine and both designs). It uses the study programme's outcomes and analysis unchanged (`prereg/2026-11-study-program.md`, with Amendments 2, 4, 9 and 10). How the rows are built: research-update `prereg/run-manifest.md`, section 3 (G, G10, H, I, J).
- Engine: `ce8d030b8d16a752706c4ea2db71196e11e73831`, the frozen engine on every row, the no-programme rows included. The layer itself is the switch `COMM` (row option `cl`), built in S37: `dev/reports/community-layer.md` gives Claude's reading of the design and every choice behind it.
- Results: BetterToBest/compassionism-sim-results, folders `prog-g-ce8d030`, `prog-g10-ce8d030`, `prog-h-ce8d030`, `prog-i-ce8d030` and `prog-j-ce8d030` (the layer's rows), compared with `prog-a-ce8d030`, `prog-b-ce8d030` and `prog-b10-ce8d030` (the same rows without the layer, and the no-programme rows). Each folder has `run.txt` (the exact command and its workflow run), `SHA256SUMS` and `DONE`; per-seed values of every measure are kept there.
- Every table behind this report: `dev/runs/s38-layer/tables.md`. Every estimate with its interval and flags (about 14,000): `dev/runs/s38-layer/estimates.csv`. Both are written by `python3 dev/tools/s38_layer.py <compassionism-sim-results checkout> dev/runs/s38-layer` (about 40 seconds).
- Checks the script makes before any table (all pass, `tables.md` section 0): each study has the preregistered number of rows; the release row with the layer at 10,000 adults is identical in studies G10 and J; study B10's release and no-programme rows are identical to study A's at 10,000 adults; the first 20 years of every 40-year row equal the 20-year row; rows without the CCO are identical under both designs; every row with the layer has adults ÷ k communities on every seed; the Shapley values add up to the full design's effect on every seed; the factorial's full cell is the same row as the release row of Q7.

## The words used here

- **The community layer** (S37): adults live in communities of k adults (100 at the main value). Each year, the PTF's two density tests from the Hub are read in each community instead of across the whole population: the food price cut needs about 40% of the community to be PTF members, and the synergy coefficient θ needs 55%. With SZH on, the PTF's starting members are placed together in zones (communities where a share f of residents are members; f is 0.5 at the main value). Imitation (who joins the PTF next) is local at the main value.
- **The five parts:** the CCO (the Basic Unit, with its octaves), PTF (the merchant network), PTH (the housing arm), SZH (the zones), CIP (the community investment programme). **The C2.2 design** (headline, Duke's answer to ledger decision D8) and **the release design** ($1,200 a month, opt-in) are both shown.
- **Outcomes**, as in the study programme: *basic living* (share of adult-years under 30 days of basic living, design-neutral reading; the design's own reading is in the tables and never claimed), *cost of living* (share of adult-years under the MIT living-wage budget), *wealth* (share of adults with wealth under $25,000 at year 20 or 40), *cost* (programme cost per adult-year), *inflation* (the yearly price rise implied by the price level). For the three shares, a reduction is a positive number of percentage points ("points").
- **The layer's effect:** the release row with the layer minus the same row without it, seed by seed. Positive on the shares means the layer helps.
- **The rule** (addendum rule 1): a layer effect is stated only where its 95% interval excludes zero, and called **material** only at 1 point or more (5% of the release row's cost for cost; 1 point of the yearly inflation rate). Synergy (rule 2) uses the study programme's rule, unchanged.
- Intervals are 95% paired-bootstrap intervals over seeds (10,000 replicates, bootstrap seed 20261101).

## The short answers

1. **The layer changes no result materially, anywhere.** In the headline cell (C2.2 design, Reference, 10,000 adults, 20 years, CPS yardstick, raise off), reading the density tests in each community, with zones placed as SZH places them, improves basic living by 0.01 points [0.01, 0.01], the cost of living by 0.03 points [0.03, 0.03] and wealth by 0.15 points [0.14, 0.15]; it lowers inflation by 0.16 points a year [0.16, 0.16] and adds $209 per adult-year [207, 212] to the cost (0.3%). All are detectable, because the comparison is paired on 500 seeds, and all are far below the materiality thresholds. Across all 60 settings of Q7 (both designs, three environments, 500, 2,000 and 10,000 adults, 20 and 40 years, both yardsticks, the raise off and on), 0 of 300 layer effects on the claimable outcomes is material. The largest are 0.11 points on basic living, 0.12 on the cost of living, 0.22 on wealth, 0.29 points a year on inflation and 0.5% of the cost. **Under the preregistered rule 6, the finding is: reading the Hub's density tests locally, with zones placed as SZH places them, does not change the results in this engine.** That is a finding about the mechanism as modelled, not about real zones.
2. **One decision moves, on a measure that was already near zero.** The C2.2 design's effect on wealth in Reference at 20 years is small and unfavourable without the layer (−0.19 points at 10,000 adults: slightly more adults with low wealth) and not distinguishable from zero with it (−0.04 [−0.09, 0.01]). The same happens at 500 adults. Nothing else in the programme's decisions changes with the layer: every gain on basic living and the cost of living, and every cost and inflation statement, stays as it was.
3. **No synergy appears with the layer.** The pairs the layer was built to test stay tiny. With the layer on, PTF × SZH is at most 0.14 points on basic living, 0.18 on the cost of living and 0.50 on wealth in any setting, and CIP × SZH at most 0.02, 0.02 and 0.23 (in absolute value). No contrast involving SZH or PTF becomes material. 72 of 990 contrast decisions change when the layer is switched on, but almost all move between "not detected" and "detected, below materiality". Six cross the materiality line, and each by a small change (at most 0.16 points or $78) in a contrast that was already close to the threshold: the whole-design contrast on wealth (C2.2, Reference) and on the cost of living (release design, Reference, 10,000 adults) fall just under 1 point, the whole-design contrast on inflation (C2.2, Reference) rises just over 1 point a year, and CCO × CIP on cost (C2.2, Adverse, 500 adults) passes 5% of the cost. All six are overlaps (negative contrasts), none a synergy. S36's answers stand: the CCO is almost the whole effect, and the parts overlap rather than reinforce each other.
4. **The layer's four design parameters move only these tiny effects.** No study H row has a material layer effect. Each swept setting (zone member share f 2/3 or 1; community size k 50 or 250; population-wide imitation; zones that need CIP) changes some decisions between "stated" and "not stated" for effects of a few hundredths of a point (layer rule 1: 3 to 28 outcome-settings per row, most with zones that need CIP). Under rule 3 the headline sentence must name them, so: *the direction of the layer's very small effects depends on the community size k, the zone member share f, how members imitate, and whether zones need CIP; that none is material does not.* In four outcome-settings the programme's own wealth effect, which is close to zero under C2.2, changes between "not stated" and a small statement (k 250, and zones that need CIP); no other programme decision changes. When zones need CIP and CIP is off, no zones form and the layer's small gains disappear; that comes from the design's own rule (rule 2), not a finding.
5. **The PTF's starting size does not change the layer's effect.** At PTF starting shares of 10%, 30% and 50%, the layer's effect stays within half a point of zero on every share and 0.31 points a year on inflation. No difference between two shares reaches 1 point (rule 4: 0 outcome-settings). The Hub's case for beginning in dense zones ("Phase deployment beginning in high-density urban zones") finds no material support in this engine.
6. **Population size changes nothing.** 0 of 720 comparisons (the layer's effect and the release row's effect with the layer at 2,000 and 10,000 adults against 500, and every contrast and Shapley value of the synergy table at 10,000 against 500) pass the scale rule. Zones are coarse at 500 adults (5 communities, about 2 zones) and fine at 10,000 (100 communities, about 36 zones), and the answer is the same at both. So the 500-adult figures lead to no different decision (rule 1's coarseness clause, rule 5).

## Why the layer does so little (Claude's reading; not tested by a separate run)

The layer's own diagnostics (tables section 7) show what it does. At 10,000 adults in Reference, 81% of PTF members live in communities where the member share reaches 40%, so most members get the full food price cut; without the layer, the population-wide share (about 18% at the start) never passed the test. But only 11% of members live where θ is above zero (the 55% test), and members are about 20% of adults. The food price cut reaches about a fifth of adults, and S36 found that the PTF's whole contribution to basic living and the cost of living is a few hundredths of a point beside the CCO's 17 to 24 points. Doubling a small effect leaves a small effect. Stress has fewer members (8% at the start, 11% over the run), fewer zones (about 16 at 10,000 adults) and a smaller layer effect still.

## 1. The headline cell

C2.2 design, Reference, 10,000 adults, 20 years, CPS yardstick, raise off. The release row with and without the layer, against no programme, and the layer's effect (paired). † interval excludes zero; H survives Holm over the five primary outcomes; none is material.

| Outcome | Effect without the layer | Effect with the layer | The layer's effect |
|---|---|---|---|
| Basic living (points) | 17.62 [17.60, 17.65] | 17.63 [17.60, 17.66] | 0.01 [0.01, 0.01] †H |
| Cost of living (points) | 24.40 [24.37, 24.44] | 24.43 [24.40, 24.47] | 0.03 [0.03, 0.03] †H |
| Wealth under $25,000, year 20 (points) | −0.19 [−0.23, −0.14] | −0.04 [−0.09, 0.01] | 0.15 [0.14, 0.15] †H |
| Cost ($ per adult-year) | 60,479 [60,465, 60,492] | 60,688 [60,674, 60,701] | 209 [207, 212] †H |
| Inflation, yearly rate (points) | 35.07 [35.04, 35.09] | 34.91 [34.89, 34.93] | −0.16 [−0.16, −0.16] †H |

Release design, same cell: basic living +0.04 [0.04, 0.05], cost of living +0.07 [0.07, 0.07], wealth +0.14 [0.13, 0.15], cost +$151 [149, 152], inflation −0.02 [−0.02, −0.02] points a year; none material. Secondary outcomes (income and wealth inequality, children below the cost of living, hours, the official poverty line, poverty severity) move by at most 0.4 of a unit (tables section 1).

## 2. The layer's effect in every setting (Q7)

C2.2 design, CPS yardstick, raise off; the layer's effect (with − without), points ($ for cost). Every setting, both designs, both yardsticks and the raise: tables section 2.

| Environment | Adults | Years | Basic living | Cost of living | Wealth | Cost $ | Inflation (yearly) |
|---|---|---|---|---|---|---|---|
| Reference | 500 | 20 | 0.01 [0.01, 0.01] | 0.03 [0.02, 0.03] | 0.15 [0.11, 0.18] | 175 [165, 186] | −0.14 [−0.14, −0.13] |
| Reference | 2,000 | 20 | 0.01 [0.01, 0.01] | 0.03 [0.03, 0.03] | 0.15 [0.14, 0.17] | 200 [196, 205] | −0.15 [−0.16, −0.15] |
| Reference | 10,000 | 20 | 0.01 [0.01, 0.01] | 0.03 [0.03, 0.03] | 0.15 [0.14, 0.15] | 209 [207, 212] | −0.16 [−0.16, −0.16] |
| Reference | 10,000 | 40 | 0.00 [0.00, 0.00] | 0.01 [0.01, 0.01] | −0.05 [−0.06, −0.05] | 81 [78, 84] | −0.10 [−0.10, −0.09] |
| Adverse | 10,000 | 20 | 0.02 [0.01, 0.02] | 0.04 [0.04, 0.04] | 0.17 [0.16, 0.18] | 216 [214, 218] | −0.20 [−0.20, −0.20] |
| Adverse | 10,000 | 40 | 0.01 [0.01, 0.01] | 0.01 [0.01, 0.01] | −0.05 [−0.06, −0.04] | 108 [105, 112] | −0.14 [−0.14, −0.13] |
| Stress | 10,000 | 20 | 0.02 [0.02, 0.02] | 0.04 [0.04, 0.04] | 0.14 [0.13, 0.14] | 67 [66, 68] | −0.05 [−0.05, −0.05] |
| Stress | 10,000 | 40 | 0.01 [0.01, 0.01] | 0.01 [0.01, 0.01] | −0.02 [−0.02, −0.02] | 37 [35, 38] | −0.07 [−0.08, −0.07] |

Over all 60 settings, 283 of the 300 layer effects on claimable outcomes have intervals that exclude zero; 0 is material. Under the release design in Stress (CPS, raise off) the layer's effect on inflation turns slightly positive (+0.02 to +0.06 points a year) and on wealth slightly negative (−0.03 to −0.11 points).

## 3. Synergy with the layer (Q8)

The study programme's Shapley values and 11 interaction contrasts, recomputed on the factorial with the layer on (the 16 cells with PTF from study G or G10; the 15 cells without PTF, and the no-programme row, from B or B10, which the layer cannot change). Headline G10 (10,000 adults, 20 years); G (500 adults, 20 and 40 years) beside it.

- **Shapley values.** With the layer, the PTF's Shapley value on basic living and the cost of living changes by at most 0.04 points, SZH's by at most 0.04. No Shapley value on these two outcomes moves by more than 0.04 points, so S36's split by part stands.
- **The tested pairs.** PTF × SZH and CIP × SZH: listed for every setting in tables section 3b. The largest with the layer are those in short answer 3. None is material.
- **Decisions.** 72 of 990 claimable contrast decisions change (tables section 3a); 6 of them cross the materiality line, all overlaps already near the threshold (short answer 3). 1,111 of 1,530 changes (contrasts, Shapley values and the full effect) have intervals excluding zero: the layer moves every cell with PTF a little, and paired seeds detect it.

## 4. Design parameters (Q9, study H)

Each swept row against the main-value row, 500 adults, paired. Every swept row's difference from the main-value row is below 0.3 points on every share and below 0.3 points a year on inflation; the largest on cost is $278 (f 1, C2.2, Reference). Tables section 4 gives each row in each setting, and the summary by row:

| Swept row | Layer decisions that differ | Programme decisions that differ | Any material |
|---|---|---|---|
| Zone member share f 2/3 | 3 | 0 | no |
| f 1 | 5 | 0 | no |
| Community size k 50 | 3 | 0 | no |
| k 250 | 16 | 1 | no |
| Imitation population-wide | 8 | 0 | no |
| Zones need CIP (four cells with PTF and SZH on, CIP off) | 20 to 28 each | 0 to 2 each | no |

The main values stay the headline (rule 3). No parameter was chosen or re-chosen after a result was seen.

## 5. PTF starting size (Q10, study I)

The layer's effect at a PTF starting share of 10%, 30% and 50%, beside the environment's own (18% in Reference and Adverse, 8% in Stress). C2.2, Reference, 20 years: on the cost of living 0.02, 0.04 and −0.00 points (own share 0.03); on wealth 0.26, 0.34 and −0.06 points (own 0.15); on cost +$111, +$388 and −$37. At a 50% start the layer's small gains vanish or reverse; a likely reading, not tested here, is that most communities then pass the 40% test with or without the layer. No difference between shares reaches 1 point on any claimable outcome in any setting (rule 4).

## 6. The layer's diagnostics

Release row with the layer, C2.2 design (tables section 7 has both designs and every study H and I row):

| | Communities | Zones at the start | Spread of member share (points) | Members where share ≥ 40% | Members where θ > 0 | PTF members (% of adults) | Members' price cut (%) |
|---|---|---|---|---|---|---|---|
| Reference, 500 adults, 20 y | 5 | 2.2 | 19.7 | 68% | 6% | 20.2 | 8.7 |
| Reference, 10,000 adults, 20 y | 100 | 36.2 | 21.1 | 81% | 11% | 19.9 | 9.1 |
| Reference, 10,000 adults, 40 y | 100 | 36.2 | 18.9 | 68% | 13% | 23.1 | 8.7 |
| Stress, 10,000 adults, 20 y | 100 | 16.4 | 16.1 | 66% | 7% | 11.2 | 7.7 |

The batch's placement at 500 adults (68% of members where the share reaches 40%) is a little above the S37 checks' figure at 400 adults (about half), as expected with one more community.

## Limits (stated on the findings page)

As in `dev/reports/community-layer.md`: PTH density is not modelled (the Hub gives only a household count); people do not move between zones; capacity is not limited by zone; members do not shop across zones. The thresholds (40%, 55%, θ up to 0.25 at 90%) and price cuts (2.64, 1.65 below 40%) are the Hub's figures, used as given. The finding is about this mechanism as modelled; a different reading of how density works (for example a network effect on wages, or zones that change prices for non-members) is not tested here.

## How the analysis read the preregistration where it left a detail open

Recorded in `dev/DECISIONS.md` (S38): one bootstrap resample per population size, shared by every study at that size, so every comparison between studies at one size (G against B, J against A, and so on) is paired on one resample, as the addendum's Analysis asks; Holm for Q10 on the three shares' layer effects (as written), with the differences between shares judged by rule 4 alone; materiality of the layer's effect on cost against the release row's cost without the layer (rule 1), and of a contrast against the full design's cost (the programme's rule 2); for a swept row of study H, its layer effect is taken against the same row without the layer (study B), and its programme effect against none.
