# The visual suite page: a report for Duke

October 14, 2026 · Claude · ledger step s161 · draft pull request from `claude/magical-einstein-umkin2` into `main`

## In one paragraph

A new page, `suite.html` ("Beyond one poverty line"), shows what the other pages do not: the whole six-step ladder of your BLEI paper year by year, what each adult's days of security are made of, what happens to people who take part and to people who do not, how four different poverty lines tell four different stories, and how far one run can land from another. It reads the newest release through `data/manifest.json` (today v5.6) and prints every number from the data; nothing is typed in. It is not linked from any other page yet, so you can look at it before anyone else does. No figure, and nothing in the engine, has changed.

**This branch carries the v5.6 release draft (pull request 32) underneath it.** Please merge pull request 32 first; this one then adds only the page.

## What to look at first

1. **"The BLEI ladder, year by year."** Two charts side by side, no program and Compassionism: each column is a year, each band a step from Crisis (under a week of basic living) to Flourishing (two years and more). The buttons above switch between all adults, adults taking part and adults not taking part.
2. **"The bottom and the top of the ladder."** At Reference over 20 years, in the main reading, Compassionism cuts the share in Crisis from 23.4% to 4.4%, but the share Flourishing falls from 48.0% to 3.4%, and the median adult's days fall from 654 to 163. The second chart shows why: change only how much new output backs the Source's payout, and Flourishing goes from 3.4% (main reading) to 5.6% (middle reading) to 76.2% (every dollar backed). In the main reading prices rise 50.8% a year faster than without the program, so savings in dollars lose their worth.
3. **"The six measures of the BLEI paper."** One card per measure: what it asks, and what this model can say about it (see the next section).

The strip under the section menu sets the environment (Reference, Adverse, Stress Test), 20 or 40 years, and the backing reading (main, middle, every dollar backed). The address carries the choice, so any view can be shared.

## The six measures: Claude's reading of the design

Your BLEI paper (https://bettertobest.github.io/research-hub/basic-living-economic-index.html) defines six measures. I read it before mapping them onto the model; this is my reading, and the page labels it so.

| Measure | What the paper asks | What the model can show today |
|---|---|---|
| BLEI | How many days of basic living a household's resources cover | Measured for every adult every year, on the paper's own reading, with its six tiers. This is most of the page. |
| EDC | How much income drains away to rent and interest | Measured from each year's payments since v5.3 (Reference, 20 years: 26.0% of income with no program, 15.9% with Compassionism). |
| EPPM | How far a participant's money goes against the same income without the program | Not computed as one number. Its parts are in the model; combining them as the paper does could be a next measure. |
| FBS | Money left each month above basic living | Measured for participants only (93.8% of participant-years have even or better odds of advancing). No one takes part without the program, so there is nothing to compare it with. |
| CSI | How security compounds over time | Not computed as the paper's formula: the model simulates the years directly instead, and the ladder over time is its answer to the same question. |
| IPBI | What people who do not take part gain indirectly (less crime, better health, property values, productivity, larger markets) | Not measured: the model has none of these channels. The page shows the direct effect on non-participants through prices and wages, and says the comparison is not the paper's. |

Where your writing is silent on how a measure maps to the model, I chose the cautious option: show "not computed" rather than build a stand-in number.

## What the page shows that is easy to miss

- **The floor and the top move in opposite directions in the main reading.** Fewer people in Crisis, far fewer at the top. A poverty count alone would call this a clear gain; the ladder shows the price of it.
- **The backing assumption decides the top, not the bottom.** Crisis is low in all three readings at Reference (4.4%, 4.3%, 2.9%); Flourishing is 3.4%, 5.6% or 76.2%.
- **What the days are made of.** Savings are owned and stay through a bad year; the allowance lasts as long as the program does. With no program the average adult's days come almost wholly from savings (2,237 days at Year 20); with Compassionism savings give 177 days, the allowance 26 and pay 18. Two adults with the same total can be in very different positions.
- **People who do not take part.** In the main reading the median non-participant ends with 41 days, against 654 for the median adult with no program. The page warns that the two groups choose and differ before the program does anything, and that the fair comparison is the whole population.
- **Four lines, four answers.** At Reference, Year 20: under 30 days, 12.7% on the paper's reading and 14.0% on the same-rules reading (30.7% with no program on both); relative income poverty barely moves (20.5% against 19.8%) because it counts cash only and the allowance is not cash; unhoused 0.19% against 0.31%.
- **The environment matters as much as the program.** In the Stress Test, the main reading leaves 56.0% under 30 days against 42.1% with no program (10th to 90th percentile across the runs: 53.0% to 59.4%, against 39.4% to 44.6%).

## Choices made (each recorded in `dev/DECISIONS.md`, Session 11)

1. **Where the page's extra data lives.** The suite series were already in the study's explore files; `release_data.py` now copies them into `data/releases/v5.6/suite-20.json` and `suite-40.json` and lists them in the release file, so the page needs nothing but the manifest. Alternative: read `dev/runs/` directly (the live site would then depend on development files).
2. **The page stands alone and asks search engines not to index it** until you decide to link it. Alternative: link it from the findings explorer now.
3. **Colours for the ladder.** Two colour ramps split at the 30-day line, warm below and blue above, each checked for colour-blind readers in light and dark. One ramp cannot show six steps distinctly.
4. **"Flourishing" for both runs.** Your paper keeps "Flourishing" for configurations where community prices make the tier durable, and the earlier engine said "Comfortable" otherwise. The data file names the tier Flourishing in both runs; the page says so in its limits. Alternative: relabel the no-program tier "Comfortable" (would add a word the data does not carry).

## How it was checked

- `validate`, `unit` and `domtest` pass; `domtest` gains Phase 15 (six checks on how the page behaves: it opens the newest release, the address carries the view both ways, every chart and table draws with one column a year, the charts answer the keyboard, every table has downloads, no other page links to it, and a release without the suite gets a plain note).
- `check_figures.js` gains three checks: the suite series agree with the release (the share under 30 days equals the published path to its rounding; the six tiers add up to all adults every year; no one takes part without the program), every number on the page equals the data in 12 views (3,804 numbers), and nothing is typed in.
- `guard_test.js` passes (no engine change). `no_figure_change.py compare` passes: no engine hash and no number in any existing data file moved; the new files and the new words are listed.
- Looked at in a browser at desktop and phone widths, light and dark, with no sideways scrolling.

## Limits

- It is not a forecast; the model has not been reviewed by an independent economist.
- Three of the paper's six measures are not computed, so the page cannot test the indirect gains your paper expects.
- The suite series cover the four main rows (no program, main, middle and every dollar backed), not the other readings.
- Participants and non-participants choose, so differences between them are not effects of the program alone.

## Reproduce

The series: `node dev/tools/explore_export.js ENV YEARS 500 1 --v54 --suite --snab --slope --panel=…` for ENV ref, adv, st and YEARS 20, 40 (the s165 study, engine commit 5bf5bcc; the exact commands are in each suite file's `_meta.commands`). Then `python3 dev/tools/release_data.py`, and open `suite.html` through a web server.
