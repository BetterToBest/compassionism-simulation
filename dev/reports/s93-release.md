# The release v5.9.23: the findings on the release engine

Written Nov 23, 2026. This report says what the release changed, which studies were rerun for it, what was checked before any figure was published, and what stays as the record. Every figure below comes from a results folder in BetterToBest/compassionism-sim-results, named in backticks. Preregistration: BetterToBest/research-update `prereg/2026-11-s90-private-price-at-sale.md`, Amendments 2 to 6.

## What the release is

The release is version **v5.9.23**, engine commit `50bc51d1d551697232fdaa74421325ce66432de6`. Every figure on the findings page and the visual suite now comes from this engine. Its main row differs from the v5.9 main row in three ways, in both runs of each pair (with the programme and without it):

1. **The private businesses' lower BU price is set at the sale.** A privately owned essential-service business takes BU at a lower price, as the design has it. That is Duke Johnson's design (Oct 1, 2026). The engine had shared that premium a year late, which made the BU each adult spends swing from one year to the next. The earlier rule stays available as an option (`sp.vAt: 'lag'`).
2. **Pay differs by household type**, drawn from the survey for single adults, single parents, and couples with and without children.
3. **The child and dependent care credit** is included, under the 2025 rules.

Duke adopted the last two on Nov 21, 2026, after the yardstick study's preregistered rule held. That rule asks whether they bring the no-programme run closer to the US tax-credit data.

Two engine defects were found and fixed before any rerun was read:

- **The stored no-programme economy.** It could be reused across rows whose settings differed. This happened only in studies that run several rows in one process.
- **One payroll pool.** In a collapsed economy, where no worker of the employee-owned businesses had any pay the year before, a payroll pool was lost from the BU accounts.

The CHANGELOG and the release notes describe both defects.

## Which studies were rerun, and which archived pieces were reproduced

Every study whose figures the findings page or the visual suite shows was **rerun in full** on the release engine, with seeds 1-500 unless stated. In all, 60 results folders end in `-50bc51d`. The studies:

- the v5.9 main rows and their readings: the main pairs, the specification curves, the Source-financing bounds and the backing curve;
- the supply study (both batches);
- the automation study (both batches);
- the lending study;
- the yardstick study;
- the central-bank study (seeds 1-100);
- the history study;
- the visual suite's three series jobs;
- the checks below full backing.

Two kinds of check were run **before any figure was read**:

- **Each rerun.** Every folder covers its seeds once, on the release engine, and passes its job's own checks. The main pair that each study carries equals the rerun main rows. The central-bank and history studies start where the main rows do. The supply study's check rows pass. The record of these checks is research-update `audits/2026-11-23-s93-part3.md` and `audits/2026-11-23-s93-part3b.md`.
- **Archived pieces reproduced from scratch.** A sample was drawn before any of it was run. From a clean checkout of each one's recorded engine and runner, eight archived shards were run again: one from each of the four v5.9 parts, the at-sale rerun, the supply study, the automation study and the lending study. So was one era of the history study. Every stored value was equal.

## What changed

**The main rows** (`s93-release-tables-50bc51d`). The change from the published v5.9 main rows to the release main rows is split into two steps. Each step is measured on the same 500 paired seeds, with 95% intervals.

- Across 60 primary effects (two designs, three environments, two horizons, five outcomes), **no effect changes sign**. Its rounded value (two decimals, or whole dollars) changes in 53 of the 60. Overall, 21 changes favour the programme, 25 go against it, and in 14 the interval includes zero.
- **The price at the sale** moved every poverty and wealth effect in the programme's favour.
  - Basket poverty: the full-coverage design's cut grew by 0.28 to 0.59 points, the opt-in design's by 0.04 to 0.26.
  - Median real wealth: the gain grew by $481 to $1,525 (full coverage) and $110 to $605 (opt-in).
  - Programme inflation: it changed by less than 0.0001 points a year. It rose by that much at most in four full-coverage cells (Adverse and Stress); elsewhere it fell slightly or did not change measurably.
- **Pay by household type and the care credit** moved the two designs differently, as expected before the reruns:
  - **Opt-in design:** every poverty cut shrank. Basket poverty by 0.33 to 0.94 points, below 30 days of basic living by 0.13 to 0.39, and too little wealth by 0.19 to 0.42.
  - **Full-coverage design:** its cut below 30 days of basic living grew by 0.42 to 0.75 points, and its other effects moved both ways.

**Every figure the pages print** (`s93-page-check-50bc51d`). The pages were rendered twice, from the published data and from the release data, and every printed figure was paired by its file, row and column. Of 3,262 printed figures, 2,132 change as printed and 37 change sign. Besides the readings below, the sign changes are bounds of intervals near zero and one financed basket-poverty cell (full coverage, Stress, 20 years: +0.6 to −0.6 points). The changes worth stating:

- **Wages that follow half of programme inflation, the rest never made up, with nothing backed** (the supply study). This reading changed the most. At 20 years the programme now lowers basket poverty against no programme: by 8.5 points in Reference, 12.7 in Adverse and 1.2 in Stress. The published figures were rises of 9.6, 5.0 and 9.6. At 40 years it still raises basket poverty in Reference (11.3 points) and Stress (12.1). **The change comes from the price at the sale** (`s93-wage-dec-50bc51d`; seeds 1-20 in each environment and horizon):
  - with only that change undone, the release engine gives the published figures again, within 0.3 points;
  - undoing pay by household type or the care credit moves them by half a point at most;
  - the v5.9 row on the release engine equals the published engine's, so the engine fixes do not move them.
  That run shows which change moves the figure, not the mechanism inside it.
- **The yardstick study's change in programme inflation with both readings** is now a small rise (+0.0044 points a year at 20 years in Adverse and Stress). That study was rerun on the engine with the fix to the stored no-programme economy.
- **Financed rows:** 45 of the 48 poverty and wealth curves are fragile, as before. Two of the full-coverage design's financed curves in Reference at 40 years (wealth poverty and programme inflation) moved from fragile to robust.
- **The automation study's trace** (`s85-trace-50bc51d`):
  - The adults who would take part still carry most of the extra rise in basket poverty with lost jobs: 73-101% of it at 20 years, 62-88% at 40.
  - Enrolment does not fall.
  - No full-coverage cell worsens.

## The two-year swing, and the measure below full backing

The price at the sale was preregistered to remove the swing in the BU each adult spends. The swing is the mean year-to-year change over years 2-12, on seeds 1-20 (`s93-belowfull-50bc51d`). On the release main row at full backing, it is 2.27% with the price at the sale, against 18.30% with the price a year late, in Reference (a ratio of 0.12). The ratio is 0.20 in Adverse and 0.22 in Stress, each below the preregistered half. The earlier at-sale rerun's measure, on the v5.9 row, is printed beside it there.

Below full backing, the preregistered swing measure **failed for a known reason**: it counts the steady growth of the BU price level as swing. After that failure, and before it was computed, a measure of the change in growth was chosen. It holds, with ratios of 0.05-0.11, and a sensitivity measure on the detrended series agrees (0.11-0.29). Both are labelled as chosen after the first measure failed, and the figures below full backing are published with both. Duke may instead hold them back.

## Checks on the pages

- Every printed number on the findings page's v5.9 section is tied to a row of its data file.
- The reader-text check finds no internal label.
- Every headline card carries the full-backing statement and the opt-in design's figure, and the wealth card carries the erosion share.
- Every series the visual suite draws is present in the release data, and every view renders.
- The 24 charts equal what their generator writes from the release tables.
- Each release section's data files carry one engine, which its visible text names (`node dev/tools/s93_checklist.js`).

## What stays as the record

The model registered on OSF (v5.8, engine `104691f`) and the v5.9 figures stay published as the record. Each can be reproduced from its engine commit and the commands in its results folder's `run.txt`. The reports written for the v5.9 studies keep their figures and dated notes as history; where a page figure now differs, the page prints the release figure.
