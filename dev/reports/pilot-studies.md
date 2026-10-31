# Pilot studies (S35): what the full study batch needs

**PILOT.** Every figure in this report comes from pilot runs: 50 seeds, 500 to 10,000 adults. None of them is a headline figure. The pilots were run to find out what the full batch (S48, 500 seeds) must contain, and how long it will take. The full batch, run once as frozen in S47, is where findings come from.

- Preregistration: research-update `prereg/2026-11-study-program.md`, with amendment 1 (engine commit, job script, choices made before any run).
- Engine: `70d23beff2065b554b687a2a4843c1433b19498b` (pull request 50). Job script: compassionism-sim-results `runner/jobs/program.js`.
- Results: BetterToBest/compassionism-sim-results, folders `pilot-a-70d23be`, `pilot-b-70d23be`, `pilot-b10-70d23be`, `pilot-c-70d23be`, `pilot-d-70d23be`, `pilot-d10-70d23be`, `pilot-f-70d23be`. Each folder has `run.txt` (the exact command and its workflow run), `SHA256SUMS` (every file checked: all match) and `DONE`.
- Every table behind this report: `dev/runs/pilot-studies/tables.md`. Every estimate with its interval: `dev/runs/pilot-studies/estimates.csv`. Both are written by `python3 dev/tools/pilot_studies.py <compassionism-sim-results checkout> dev/runs/pilot-studies`.
- Method, as preregistered: each figure is a mean over seeds of the release row (or a cell) minus the no-programme row of the same seed. Intervals are 95% paired-bootstrap intervals over seeds (10,000 replicates, random seed 20261101). The comparisons between population sizes treat the sizes as independent runs. For the poverty shares, a reduction is a positive number of percentage points ("points").
- Outcomes named below: *basic living*: the share of adult-years with fewer than 30 days of basic living (the BLEI), read on the design-neutral definition unless stated; *cost of living*: the share of adult-years with income below the MIT living-wage budget; *wealth*: the share of adults with wealth below $25,000 in year-0 prices; *cost*: programme cost per adult-year; *inflation*: the model's cumulative price rise.

## The short answers

1. **Population size changes nothing that matters.** Across 504 comparisons (three environments, two horizons, two yardsticks, the release row with the raise off and on, the no-programme levels; 2,000 and 10,000 adults against 500), 11 differ from the 500-adult figure beyond Monte Carlo error. That is 2.2%, fewer than the 5% expected by chance alone. Only one share outcome passes the preregistered scale rule (wealth, Adverse, released wages, raise on: 1.0 points [0.1, 1.9], at the threshold). The others are cumulative inflation over 40 years in Stress, explained in section 2: the typical price path does not change with size, but the spread between seeds narrows. The synergy table and the participation curve at 10,000 adults match 500 adults on every share outcome. **In this engine, a larger population narrows the intervals and changes no conclusion.**
2. **Synergy is small, and the design's effect is almost all the CCO.** In the Reference environment at 20 years, the CCO accounts for 97% of the release row's effect on basic living and 93% of its effect on the cost of living. The PTF, PTH and SZH each move every share outcome by less than 1.2 points in every setting (their Shapley values). The interactions that clear the materiality bar are nearly all between the CCO and CIP: they overlap on the cost of living (together they do 1 to 3 points less than the sum of their separate effects) and reinforce each other on wealth (up to 5 points more).
3. **Age at joining and ageing matter.** With ageing on (people grow older and retire), the release row raises the share with low wealth instead of lowering it (Reference, year 40: 16.7 points worse, against 8.1 points better without ageing). Adults who never join are worse off in the release row than in the no-programme run on basic living and wealth.
4. **The participation curve is close to a straight line for basic living, bowed for the cost of living, and flat then rising for wealth.** The Reference row's gain on all three outcomes is detected already at the lowest grid level (10%), so the grid's floor decides S5's figure there. In Adverse and Stress no level qualifies, because the release row's wealth effect goes the wrong way.
5. **The debt reading roughly halves the share of families in debt but stays above the SCF's 9.3% without the programme** (Reference, year 20: 21.4% with the released spending rule, 14.9% with the debt reading). It changes no decision about the release row.
6. **A community layer is needed (S37), on the pilots' evidence.** The parts whose case rests on local density (SZH, PTF, PTH) are close to inert in this engine, and nothing in it depends on population size. A synergy report built on the engine as it stands would find "no synergy among them" only because no mechanism for it exists. Section 8 gives the reasoning.
7. **The full batch fits on Actions:** about 101 runner-hours for every preregistered study except the 50,000-adult rows, plus an estimated 130 runner-hours for those (section 1). Section 9 lists what the batch still needs.

## 1. Timings, for S47

The pilot runners were GitHub-hosted, with 4 vCPUs and 15 GB each. Studies A, B and B10 ran 2 processes per runner; C, D, D10 and F ran 4. A 4-vCPU runner does about two cores' worth of work. With 4 processes, each process ran at about half the speed it did with 2: at 500 adults and 20 years, a row cost 0.82 core-seconds a seed in study C against 0.47 in study A, and 0.65 in D against 0.28 in B. So per-process core-seconds overstate the work. Plan with **runner-hours**: the summed wall time of the pilot's shards, times 10 for 500 seeds.

| Study | Pilot shards | Processes per runner | Wall time per shard, s (min / median / max) | Peak memory per process | Full batch at 500 seeds, runner-hours |
|---|---|---|---|---|---|
| A (scale, 500 to 10,000) | 25 | 2 | 267 / 435 / 478 | 499 MB | 28.5 |
| B (synergy, 500) | 25 | 2 | 130 / 219 / 251 | 351 MB | 14.4 |
| B10 (synergy, 10,000) | 25 | 2 | 328 / 494 / 571 | 469 MB | 32.8 |
| C (ageing) | 5 | 4 | 61 / 74 / 107 | 386 MB | 1.1 |
| D (participation, 500) | 10 | 4 | 176 / 278 / 419 | 310 MB | 7.9 |
| D10 (participation, 10,000) | 10 | 4 | 372 / 604 / 653 | 448 MB | 15.4 |
| F (debt reading) | 5 | 4 | 64 / 84 / 89 | 263 MB | 1.1 |
| **All, without 50,000 adults** | | | | | **101** |

Per-block figures (core-seconds per seed and per row, every environment, size and horizon) are in table 1 of `tables.md`. The measured cost of a row (2 processes per runner, core-seconds per seed) is:

| Adults | 20 years | 40 years | 40 years over 20 years |
|---|---|---|---|
| 500 | 0.22-0.47 | 0.41-0.66 | 1.4-1.9 |
| 2,000 | 1.0-1.3 | 2.0-2.4 | 1.75-2.0 |
| 10,000 | 4.5-6.6 | 11.0-13.0 | 1.95-1.97 |

From 2,000 to 10,000 adults the cost grows 4.9 to 5.6 times for 5 times the people (about in proportion, slightly faster at 40 years). Extending that to 50,000 adults gives about 70 core-seconds per seed for a 40-year row and 35 for a 20-year row. The preregistration's own estimate was 80 seconds. Study A's 50,000-adult block is 6 rows × 2 horizons × 3 environments × 500 seeds: about 260 core-hours, or about 130 runner-hours at 2 processes per runner. Memory grows roughly in proportion (about 500 MB per process at 10,000 adults, so about 2.5 GB at 50,000), which fits 2 processes on a 15 GB runner. One 50,000-adult seed of one row takes under 2 minutes for both horizons, so a shard of 2 seeds × 6 rows (about 25 minutes per process) stays well under the 6-hour job limit. **Whole batch: about 230 runner-hours, about 12 hours on 20 parallel runners, all on Actions.** No study needs Runpod. In core-hours the batch comes to about 490 (228 measured plus about 260 for 50,000 adults), in line with the preregistration's 463.

**What S47 should fix about dispatch:** use 2 processes per runner (4 gains little and makes timings misleading), and shard so each job runs under about 2 hours.

**A free saving S47 may take:** the first 20 years of every 40-year run equal the 20-year run of the same seed, byte for byte. Every one of the 50,350 year-20 values in studies A, B, C, D and F matched. Only the whole-run averages (basic living, cost of living, cost) and the design-neutral basic-living share at a year differ, because a 40-year run reports them over 40 years or for the last year only. If the engine also reported those over years 1 to 20 (reporting only, guard test identical), the separate 20-year rows could be dropped, saving about a third of studies A, B, C, D and F. This is optional; section 9 lists it.

## 2. Does any outcome move with population size? (Q1)

**No, beyond Monte Carlo error.** Study A ran the release row (raise off and on) and the no-programme row at 500, 2,000 and 10,000 adults. For every primary outcome, the difference from 500 adults was computed with its interval (table 3 of `tables.md`):

- Of 504 differences, 11 have an interval that excludes zero (2.2%, below the 5% that chance alone gives).
- Two of those 11 are share outcomes. Both are the same figure, wealth at year 20 in Adverse with released wages and the raise on, read twice (from the 20-year and the 40-year run). It is 1.0 points [0.1, 1.9] at 10,000 adults, exactly at the rule's 1-point bar, and with its interval just clear of zero it is unlikely to survive Holm's correction over the three sizes the full batch runs.
- The other nine are cumulative inflation to year 40, mostly in Stress. The yearly rate barely moves with size: in Stress with the CPS yardstick, the release row's price level grows 21.4% a year at 500 adults and 21.2% at 10,000. Compounded over 40 years, though, the mean over seeds of the cumulative rise is pulled up by the seeds with the fastest rise, and those spreads narrow as the population grows. The median price level falls only from 2,400 to 2,126 times its start; the standard deviation over seeds falls from 1,330 to 317. This passes the scale rule as written (more than 1 point of cumulative inflation), so the rule's consequence applies: cumulative inflation at year 40 is to be headlined from the largest population run (50,000 adults). It is a property of averaging a compounding quantity, not a population mechanism.
- The synergy table at 10,000 adults (study B10) matches 500 adults (study B) on every whole-design and pair contrast for the share outcomes and cost. One contrast differs under the rule: inflation to year 20, Stress, CCO × PTH, 6.5 at 500 against 4.4 at 10,000 points of cumulative inflation.
- The participation curve at 10,000 adults (study D10) matches 500 adults (study D) at every level, for all three share outcomes, in every environment.

So, as S35's step text asks to be said plainly: **in this engine no mechanism depends on population size; a bigger population only narrows the intervals.** At 10,000 adults the intervals of the share outcomes' effects are about a quarter as wide as at 500 (median ratio 0.27). That is itself a robustness result, and it is also a limit: anything in the framework that is meant to work through numbers or density (a network, a local market, a zone) is not in the engine.

## 3. Synergy: the table, its size and its noise (Q2)

Study B ran all 31 combinations of the five parts (CCO, PTF, PTH, SZH, CIP) at 500 adults; study B10 ran them at 10,000 adults (20 years, CPS yardstick, raise off). For each outcome, the tables give each part's Shapley value (its average added effect over every order of adding the parts), the whole-design contrast (the full design minus the sum of each part alone), and the 10 pair contrasts within the full design (section 4 of `tables.md`, all 27 settings).

**Size.** Reference, 500 adults, 20 years, CPS yardstick, raise off (the cell that heads the preregistered report):

| Outcome | Full design's effect | CCO | PTF | PTH | SZH | CIP | Whole-design contrast |
|---|---|---|---|---|---|---|---|
| Basic living, design-neutral (points) | 10.66 [10.30, 11.02] | 10.32 (97%) | -0.11 | 0.02 | 0.00 | 0.43 (4%) | -0.08 [-0.19, 0.02] |
| Basic living, the design's own reading | 11.41 | 10.59 (93%) | -0.05 | 0.31 | 0.15 | 0.41 | 0.76 [0.64, 0.88] |
| Cost of living (points) | 17.33 | 16.06 (93%) | -0.05 | 0.23 | 0.02 | 1.07 (6%) | -1.03 [-1.14, -0.92] |
| Wealth at year 20 (points) | 3.95 | 2.58 (65%) | -0.20 | 0.09 | 0.00 | 1.47 (37%) | 0.75 [0.40, 1.10] |
| Cost ($ per adult-year) | 32,733 | 31,620 (97%) | 478 | 832 | 54 | -253 | -26 [-61, 6] |

- On design-neutral basic living, the parts add up: the whole-design contrast is indistinguishable from zero. The design's own reading shows 0.76 points of synergy, which is mostly SZH and PTH credit for days that no one can spend (preregistration check 3); it is not claimed.
- On the cost of living, the parts overlap: together they do 1.03 points less than separately, almost all from CCO and CIP both raising the same incomes (CCO × CIP: -1.02).
- On wealth, CCO and CIP reinforce each other (+0.77) but below the 1-point materiality bar in this cell.
- Across all 24 settings of study B (three environments, two horizons, two yardsticks, raise off and on), the material synergies (interval excluding zero and at least 1 point) on share outcomes are: wealth, 30 positive and 3 negative, nearly all the whole-design contrast and CCO × CIP, largest in Adverse and with released wages (up to 4.9 points); cost of living, 1 positive and 32 negative (CCO × CIP overlap, up to 3.2 points); design-neutral basic living, 2 positive and 3 negative (all at 40 years in Adverse, CCO × PTF and CCO × PTH, about 1.0 to 1.4 points). No contrast involving SZH is material on any share outcome. On cost, no contrast reaches 5% of the full design's cost.
- Shapley values of PTF, PTH and SZH over every setting, on every share outcome, lie between -1.2 and +0.3 points; PTF and PTH are slightly unfavourable more often than favourable, while costing $220-$480 (PTF) and $360-$860 (PTH) per adult-year. CIP's range is +0.3 to +6.5 points.
- Cumulative inflation compounds (the price level multiplies year by year), so its additive contrasts are large by construction (thousands to millions of points). They are in the tables but are not synergy in any useful sense; section 9 proposes reading them on the yearly rate.

**Noise.** At 50 seeds and 500 adults, the median interval half-width of a synergy contrast on a share outcome is 0.05 points; for the release row's main effects it is about 0.3 to 0.5 points. At 500 seeds both shrink by about the square root of 10 (to about 0.015 and 0.1 points). At 10,000 adults the median half-width is already 0.01 points at 50 seeds. So the full batch will resolve every contrast to well within the 1-point materiality bar: which interactions are material will be decided by their size, not by noise. With 1,151 of 1,584 contrasts already excluding zero in the pilot, "statistically detectable" will cover almost every contrast in the full batch; the materiality bar and Holm's correction are what separate findings from noise.

## 4. Horizon and age at joining (Q3)

**Year 40 against year 20** (same 40-year run, Reference, CPS yardstick, raise off; table 5 of `tables.md`). Without ageing (study A), the release row's effect on the year's cost-of-living share shrinks by 3.1 points [2.7, 3.6], and its effect on wealth grows by 4.1 points [3.7, 4.6]. With ageing on (study C), the cost-of-living effect grows by 5.2 points, the effect on the design's own basic-living reading shrinks by 4.4 points, and wealth gets worse by 12.0 points. Under decision rule 4, these 40-year statements depend on whether people age, and the full batch must report them as such.

**With ageing on, the release row harms wealth.** Reference, CPS yardstick: wealth below $25,000 is 4.7 points worse at year 20 and 16.7 points worse at year 40 than with no programme, against 4.0 and 8.1 points better without ageing. Basic living and the cost of living still improve (design-neutral: 9.3 and 25.7 points at 20 years). In Stress with ageing, basic living is worse with the programme over 40 years (7.0 points).

**By age at joining** (study C, the release row against the same adults in the paired no-programme run, over each adult's years from joining; Reference, 20 years):

| Joined the CCO at | Adults per seed | Basic living, design-neutral: reduction | Cost of living: reduction | Wealth: reduction |
|---|---|---|---|---|
| 25-34 | 168 | 13.9 [13.2, 14.7] | 22.5 [21.6, 23.5] | 5.8 [5.1, 6.5] |
| 35-49 | 178 | 13.7 [13.0, 14.4] | 19.3 [18.5, 20.0] | 6.7 [6.2, 7.2] |
| 50-66 | 149 | 12.6 [11.9, 13.3] | 52.7 [51.9, 53.5] | -2.6 [-3.4, -1.8] |
| never joined | 92 | -13.3 [-14.2, -12.5] | 0.0 [-0.2, 0.2] | -20.1 [-21.1, -19.0] |

- Adults joining at 50-66 gain most on the cost of living, because in the no-programme run many of them retire onto Social Security below the cost of living (58% of their years), while retired participants keep the BU. Their wealth is worse.
- **Adults who never join are worse off with the programme**: 13 points more of their years below 30 days of basic living, and 20 points more of them with low wealth. The likeliest channel is the programme's inflation, which raises their prices without raising their income; the full batch reports this group in every cell (it already does, as `gNon*`), and S36 should name it.
- Joining at 67 or over: seen in 1 seed of 50, so this group is effectively empty; it stays in the tables beside the four named groups (amendment 1).
- Every adult in the main row was matched to the same adult in the paired run (100%).
- The Adverse and Stress environments show the same pattern, with larger wealth losses (tables in `tables.md`).

## 5. Participation curve (Q4)

Study D ran the release row from 10% to 90% starting participation (table 6 of `tables.md`). Realised participation by year 20 ends a few points above the starting share (Reference: 21.6% at 20%, 93.5% at 90%). Shape in Reference, 20 years, CPS yardstick, raise off:

- **Basic living** rises almost in proportion: 1.0 points at 10%, 6.2 at 50%, 11.9 at 90%. The departure from a straight line through zero and the 90% point is at most 0.5 points (below the 1-point bar): linear.
- **Cost of living** rises faster at first: 3.3 points at 10%, 11.8 at 50%, 18.8 at 90%; the curve sits 1.2 to 1.7 points above the straight line from 10% to 70%: bowed, non-linear by the rule.
- **Wealth** stays flat until about 50% (0.7 to 0.8 points), then rises to 5.1 points at 90%; up to 2.1 points below the straight line from 40% to 70%: non-linear by the rule. In the engine the wealth gain appears only at high participation.
- At 10,000 adults the curve is the same (no level differs under the scale rule) and much tighter.

**For S5.** The preregistered detection level is the lowest level at which all three outcomes improve with intervals excluding zero. In Reference with the CPS yardstick it is **10%, the lowest level in the grid** (both horizons, raise off and on). The grid's floor therefore decides the figure: the full batch can only say "10% or lower". With released wages it is "none in the grid" (raise off) or 70% (raise on). In Adverse, and in Stress, no level qualifies in most settings, because the release row's wealth effect is unfavourable there at every level. As the preregistration says, this is a detection level, not a viability threshold; the engine has no collapse below a minimum share.

## 6. The debt reading against the SCF's 9.3% (study F)

Share of families (households) with net worth below zero, 500 adults, CPS yardstick:

| Environment | Row | Year 20: released rule / debt reading | Year 40: released rule / debt reading |
|---|---|---|---|
| Reference | no programme | 21.4% / 14.9% | 20.2% / 14.6% |
| Reference | release row | 7.6% / 3.6% | 4.8% / 2.5% |
| Adverse | no programme | 29.4% / 21.0% | 40.0% / 29.1% |
| Adverse | release row | 17.8% / 7.8% | 31.1% / 12.5% |
| Stress | release row | 32.3% / 31.4% | 51.1% / 48.9% |

(Adverse and Stress share one economy, so their no-programme rows are the same run.)

- With no programme, the debt reading moves the Reference figure from 21.4% to 14.9%. That is closer to the SCF 2025 figure of 9.3% but still 5.6 points above it. The remaining debt comes from the engine's other flows (job loss, shocks, the debt floor), which the reading does not touch. With released wages it is 33.5% → 22.7%. As preregistered, 9.3% describes the yardstick and is not a target; no constant was changed.
- In Stress, the release row leaves about half of families in debt at year 40 under either rule; the debt reading barely changes it there (51.1% → 48.9%).
- **It changes no decision about the release row.** On every primary outcome, in every environment, at 20 and 40 years, the release row's effect has the same sign and significance with the debt reading as without (the release row's design-neutral basic-living gain is 0.4 to 1.7 points larger with it). Under decision rule 8, no headline sentence needs to say the result depends on how households below their budget borrow, if the full batch confirms this.

## 7. What the release row does in the pilots (pilot figures, for orientation only)

These are the cells the full batch will headline, read at 50 seeds. They are not findings.

| Environment, 20 years, CPS yardstick, raise off | Basic living | Cost of living | Wealth | Cost per adult-year | Cumulative inflation |
|---|---|---|---|---|---|
| Reference | 10.7 better | 17.3 better | 4.0 better | $32,733 | prices 199 times higher |
| Adverse | 10.4 better | 23.0 better | 10.2 worse | $31,294 | 702 times |
| Stress | 0.7 better | 8.7 better | 10.9 worse | $12,360 | 29 times |

- The guardrail 6 test (a gain in basic living counts only if cost of living and wealth also improve) passes in Reference only. In Adverse and Stress the wealth measure goes the wrong way.
- **The yardstick changes a decision** (rule 7): with released wages, wealth in Reference is 11.3 points worse instead of 4.0 points better.
- **The octave raise changes decisions** (rule 6): with the raise on, wealth in Reference improves by 9.5 points (against 4.0), Adverse turns from 10.2 worse to 2.0 better, and inflation is lower (prices 132 times higher instead of 199 in Reference).
- **Inflation is extreme**, as the handoff warned. The release row's price level grows about 30% a year in Reference (CPS yardstick), 199 times its start by year 20 and about 31,000 times by year 40; with released wages, about 2,550 times by year 20. Every dollar figure is deflated by this price level, so the full batch's findings page must state it beside every result.

## 8. Is a community layer needed? (the condition for S37)

The plan builds the community and zone layer (S37) only if the pilots show it is needed. Its stated reason is that the framework's synergy argument rests partly on local density: SZH zones, PTF merchant networks, PTH communities. The pilots show:

1. Nothing in the engine depends on population size or density (section 2).
2. The three parts that argument rests on are close to inert: PTF, PTH and SZH each move every share outcome by between -1.2 and +0.3 points in every setting, and no contrast involving SZH is material anywhere (section 3). SZH counts only through the design's own basic-living formula, which credits days no one can spend.
3. The synergy study (Q2) can therefore only find that these parts add nothing and do not interact. That finding would come from the engine having no mechanism for them, not from a test of the framework's claim.

**Claude's reading (a modelling call, not a design change):** the pilots show the layer is needed, if the synergy report (S36) is to test the synergy argument rather than restate a limit of the engine. S37 goes ahead: read the SZH, PTF and PTH papers, write what should depend on local density, build it behind a switch (off = bit-identical), and add a preregistration addendum before any run. Whatever it finds is reported, including no effect. If S37 finds the Hub's papers give no mechanism that can be modelled without invented constants, it says so and stops, and S47 records the layer as ruled out with that reason.

## 9. What the full batch still needs (for S47)

Outputs and choices the pilots show are missing or need fixing before the freeze. Items marked *amendment* change something the preregistration fixed, so each needs a dated amendment before the full batch.

1. **The 50,000-adult rows of study A**, not run in the pilots. Expected cost about 140 runner-hours. Peak memory not yet measured: a 2-seed dry run in S47 must confirm it fits 2 processes per runner.
2. **Missing values must not be written as 0.** In 20-year rows the year-40 keys (`pbO_39`, `pf0_39`, `ppov_39`, `plv_39`, `hhDebt40`) are 0, as are participation (`jnP*`) in no-programme rows and the ageing keys (`agRet`, `agAge`) without ageing. A 0 price level reads as -100% inflation. Either the job script writes `null` for keys past the run (job-script change, no engine change), or every consumer drops them. Recommended: the job script, before S47's dry run.
3. **The design-neutral basic-living share at year 20 in a 40-year run** (today only the last year, `bNA20`, and the design's own `pbO_19`). Needed for Q3 on the design-neutral reading, which is the one claims are made on. A reporting key in the engine (guard test identical), like the price level by year.
4. **Optional: whole-run averages over years 1-20 from a 40-year run** (basic living, cost of living, cost, the group measures). With them, and item 3, the 20-year rows can be dropped (they are the first 20 years of the 40-year rows exactly), saving about a third of studies A, B, C, D and F. Reporting only; amendment (the rows change, not the figures).
5. **Cumulative inflation needs a second reading** (*amendment*). Its mean over seeds is pulled up by the seeds with the fastest rise, its additive synergy contrasts are compounding rather than interaction, and the 1-point rule is meaningless for figures in the millions. Recommended: keep cumulative inflation as preregistered, and add the yearly rate implied by the price level (and the median over seeds) as the reading that the scale, synergy and horizon rules are applied to.
6. **Hours of work** (`hrs`) is mean hours relative to full time, minus 1, not "relative to each adult's own hours with no programme". The no-programme row reads -1.4% (Reference), not 0. The effect (release row minus no programme) is still the average change in hours; the preregistration's wording should match the measure (*amendment*, wording only), or a per-adult paired measure is added to the job script.
7. **The participation grid's floor** (*amendment*). In Reference with the CPS yardstick the detection level is the grid's lowest level, 10%, so S5 can only report "10% or lower". Adding 2% and 5% levels to study D (and D10) would locate it. Cost: 4 rows per environment and horizon at 500 adults, under 1 runner-hour.
8. **Age at joining 67 or over** is seen in 1 seed of 50: kept as a fifth group as amendment 1 says, but S36 and the findings page should say it is too rare to read.
9. **Dispatch**: 2 processes per runner; shards under about 2 hours; 20 parallel runners; about 12 hours in all, every study on Actions (section 1). The per-study runner-hours above go into `prereg/run-manifest.md`.
10. **The community layer (S37)**: rows for it are added by its preregistration addendum before the freeze (section 8).
11. **Measures kept per row**: the 46 measures were enough for every analysis in this report. Items 3, 4 and 6 add to them; nothing else was found missing.

Nothing in the pilots calls for a change to the engine's mechanisms, a constant, or a decision rule.

## Limits

These are pilots: 50 seeds, no 50,000-adult rows, no community layer. Everything the preregistration lists as a limit carried from S34 applies (everyone in the model works; no part-time work; no child and dependent care credit; without ageing nobody grows up, retires or dies). Holm's correction is shown for the synergy contrasts. For the scale comparisons it is discussed but not computed, because the pilots ran two of the three larger sizes. The model has not been reviewed by an independent economist.
