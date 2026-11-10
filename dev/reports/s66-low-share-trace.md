# Why wealth looks better at a 10% PTF share, how much of every wealth result is the erosion of opening savings, and the wealth harm with adults outside the labour force (S66, Nov 10, 2026)

A trace, not a study of the programme. Preregistered before any run (research-update `prereg/2026-11-s66-low-share-trace.md`). No engine change: the engine is main at `78e1dd7`. The tool `dev/tools/s66_trace.js` runs its own copy of the engine with a read-only probe, and its preregistered check proves the copy gives the harness's outputs exactly (7,080 row-keys, seeds 1-5). Seeds 1-100, 500 adults, on the session machine. Tables: `dev/runs/s66-trace/tables.md` (from `dev/tools/s66_table.py`). Per-seed, per-year files: compassionism-sim-results `s66-trace-4e9d841`. Intervals are 95% paired-bootstrap intervals over seeds, unadjusted. No published figure changes here.

## In plain words
1. **The dip at the low end of the fixed-share curve is real in the model, but it is not a reason to prefer a small PTF network.** At 20 years, holding the PTFs' share of essential sales at 10% leaves 1.57 points fewer adults under $25,000 than holding it at 20% (Reference [1.41, 1.73]; Adverse 1.50; Stress 0.31). The cause is a timing threshold in the ESP surplus split:
   - The split routes part of the PTFs' business premium into reinvestment, which counts as output that matches new money.
   - Once the PTFs' capital account reaches the capital needed to serve all of the population's essentials ($18,862 per adult), reinvestment stops.
   - At 5-10% it never gets there within 20 years. At 20% it gets there in year 15.
   - After that, less of the new money is matched, so inflation runs 0.37 points a year higher at 20% than at 10%. By year 20 prices are 5% higher, and every nominal balance is worth 5% less.

   At 40 years every share has made the switch (10% in year 26), and the dip is gone: 10% is then 0.33 points worse than 20%. So no low-share optimum is claimed (preregistered rule 4).
2. **PTF damping of inflation plays no part, anywhere.** The release rows are built with PTF and PTH damping of outside inflation switched off (decision d86). Switching the damping line off changed no output in Reference or Adverse. S55's "likely reading" of why open access helps wealth named damping. It now carries a dated correction note.
3. **Nearly all of the programme's effect on year-20 real wealth is the erosion of the savings adults held at the start.** The model holds every dollar of wealth as cash with no return. Under the programme's inflation, prices are about 400 times their start after 19 years in Reference, so a balance held from year 0 keeps a quarter of one percent of its real value. That erosion term is 90-96% of the mean gap in year-20 real wealth between the programme and no programme, in every design and environment.
   - If opening balances had kept their real value, the release design's wealth-poverty harm in Reference (+21.5 points) would be a reduction (−6.8).
   - The C2.2 design's +0.7 would be −12.1.
   - In Adverse and Stress the harms of +25 to +45 points would all be reductions of 9 to 14 points.

   This is an accounting reading, not a run (section 2 says what it leaves out). It measures how much of each published wealth result is the all-wealth-is-cash assumption: almost all of it. S59 (asset classes and returns) replaces that assumption.
4. **The wealth harm with adults outside the labour force is the same erosion, falling on people who cannot save it back.** With S61's `lf` rows the C2.2 design's wealth-poverty harm is +9.8 points in Reference (this tool reproduces S61's figure).
   - **Adults outside the labour force:** +27.6 points. Without the erosion it would be −28.6: the programme's flows leave them better off. Their real disposable income rises from $33,700 to $52,500 a year and their own cash cost of essentials falls from $48,100 to $16,900. Every bit of the harm, and more (113% of their real-wealth gap), is the erosion of what they owned at the start.
   - **Adults in the labour force:** +6.1 points, against −13.1 without the erosion.

   The two groups start with about the same savings. The difference is the next 20 years: with no wages, adults outside the labour force rebuild less after their savings lose their value.

## 1. The low end of the fixed-share curve (Part A)
C2.2 design, open access, every zone's share held (no growth), 20 years. Wealth = adults under $25,000 at year-0 prices; no programme minus programme (positive = better).

| Share held | 5% | 10% | 15% | 20% | 25% | 30% | 35% | 40% | 50% | members only |
|---|---|---|---|---|---|---|---|---|---|---|
| Reference | +1.09 | +0.65 | −0.20 | −0.92 | −0.77 | −0.50 | −0.22 | +1.04 | +1.76 | −0.66 |
| Adverse | −28.34 | −29.00 | −29.67 | −30.50 | −30.30 | −29.96 | −29.63 | −27.92 | −26.86 | −30.16 |
| Stress | −40.91 | −41.35 | −41.73 | −41.66 | −41.63 | −41.49 | −41.31 | −40.48 | −39.95 | −41.65 |

Intervals about ±0.45 points against no programme. Share against share on the same seeds they are much tighter: 10% − 20% is +1.57 [1.41, 1.73] in Reference. The curve falls from 5% to 20-25%, then rises, with the step at the 40% test S55 found. S55's 500-seed figures at 10, 20 and 30% (+0.96, −0.55, −0.14) sit within these intervals.

**Not only the count under the line.** 10% against 20%: median real wealth +$1,085 [1,019, 1,150], mean real wealth +$946 (Reference); Adverse +$616 and +$434. The real-wealth distribution at year 20 is shifted, not just pushed across $25,000.

**Which mechanism (preregistered rule 3).** The 10% − 20% difference with each mechanism switched off alone (Reference; Adverse and Stress in the tables):

| Reading | 10% − 20%, wealth | Inflation, 10% − 20% |
|---|---|---|
| Main | +1.57 [1.41, 1.73] | −0.37 |
| 40% price-cut rule off (every share gets the higher food cut) | +1.25 [1.10, 1.39] | −0.24 |
| PTF damping off | +1.57 (identical) | −0.37 |
| Conversion income off | −0.07 [−0.10, −0.04] | +0.03 |
| Surplus split held at 10% | −0.56 [−0.63, −0.49] | +0.30 |
| PTF price cut held at 10% | +2.17 [1.99, 2.35] | −0.68 |

Two switch-offs remove the dip: conversion income off, and the surplus split held at 10%. The surplus split is part of conversion income (the business premium), so they point to the same place. With the split held, the curve rises with the share from the start (Reference +0.65, +1.20, +1.68, +3.11 at 10-40%). The PTF price cut works the other way: it makes higher shares better. Holding it at 10% makes the dip larger and the curve flat above 20%. So the curve is the sum of two forces: the price cut, which helps more as the share rises, and the surplus split, which hurts in the 10-25% range for the reason below. The 40% rule only sets the size of the step at 40%. Damping does nothing.

**How the split does it** (Reference, per adult per year, year-0 dollars, means over years 2-19, 10% → 20%; the code confirms each link):
- The business premium pool is split by the PTFs' share of the BU they accept. The PTFs' part doubles ($1,928 → $3,901). The private ESPs' part, which they pass on as lower BU prices, falls ($11,568 → $10,082). A private ESP's lower BU price frees BU, and freed BU go to projects (plan step 14, d140), whose output counts as matched.
- The PTFs' own part goes a third each to their price pool, reinvestment and worker profit shares until their capital account reaches $18,862 per adult (the capital to serve all of a population's food and utilities, d101). After that it goes 60% to the price pool and 40% to workers, and nothing to reinvestment. Reinvestment is bought capital, counted as matched output. The year that happens: never within 20 years at 5% and 10%, year 19 at 15%, 15 at 20%, 12 at 25%, 11 at 30%, 9 at 40% (every seed). Within 40 years, 10% switches in year 26.
- Together: matched output falls ($20,414 → $19,736), net conversion falls ($43,428 → $42,775), BU spent at face value rises ($17,853 → $18,132), and cash income falls slightly ($110,134 → $109,757). New money not matched by output rises from 37.36% to 37.75% of cash income. The price rule passes it into prices, so inflation is 0.37 points a year higher and the price level at year 20 is 5.0% higher.
- From about 25-30% the PTF price cut every adult gets (the share times the member's cut: $270 a year at 10%, $540 at 20%) outweighs this. At 40% the larger food cut adds the step.

**A model question this exposes (for S62 and S63; nothing changed).** In a fixed-share row, the PTFs reinvest until they could serve all of the population's essentials, although they sell only the held share. The switch reads their capital against the full-capacity figure, not against the share they serve. In the growth rows the share follows capacity, so the two agree. In the fixed-share rows they do not, and the low end of the curve reflects when an unneeded capacity target is reached. Claude's recommendation: S62, which takes up PTF running costs and capacity, should decide whether the switch should read capital against the share served. Until then S63 should report the fixed-share rows at 20 and 40 years with the switch year beside each, and not read the low end at 20 years alone.

**Rule 4: no low-share optimum.** The dip appears in median and mean real wealth at 20 years, but it reverses at 40 years:

| | Reference | Adverse |
|---|---|---|
| 10% − 20%, year 20 | +1.57 | +1.50 |
| 10% − 20%, year 40 | −0.33 [−0.39, −0.28] | −0.23 [−0.28, −0.18] |
| 30% − 20%, year 40 | +0.37 | +0.23 |

Its mechanism is the year a threshold is crossed inside the window, not a rule that favours small networks.

## 2. The erosion of opening balances (Part B)
For each adult in both runs of a seed: the gap in year-20 real wealth (programme minus no programme), and the erosion term. The erosion term is the adult's year-0 balance times the difference of the two runs' price deflators: what that balance loses in real value because the programme's prices are higher. Members-only main rows, 20 years. Wealth poverty here is programme minus no programme (positive = more adults under $25,000).

| Environment | Design | Mean real-wealth gap | Erosion term | Share | Wealth poverty, published | If opening balances kept their value |
|---|---|---|---|---|---|---|
| Reference | release | −$561,600 | −$504,300 | 90% | +21.5 | −6.8 |
| Reference | C2.2 | −$551,700 | −$506,000 | 92% | +0.7 | −12.1 |
| Adverse | release | −$370,900 | −$347,300 | 94% | +45.0 | −8.9 |
| Adverse | C2.2 | −$362,700 | −$347,800 | 96% | +30.2 | −13.8 |
| Stress | release | −$347,700 | −$328,400 | 94% | +24.8 | −8.8 |
| Stress | C2.2 | −$367,900 | −$347,900 | 95% | +41.7 | −11.2 |

Every interval excludes zero (tables, Part B). Means are dominated by the top fifth of opening wealth, which holds most of the dollars. By fifth, the erosion term is 63-114% of the gap in the second to fifth fifths, rising with opening wealth (C2.2, Reference: 76%, 82%, 86%, 95%). In the lowest fifth it is positive (about +$8,000 to +$12,000): those adults start in debt, and inflation erodes debt too.

What this reading leaves out. It treats each opening balance as if it were held untouched for 20 years and keeps every other figure as it is. A model where wealth is held in real assets would also change spending, prices and the programme's flows. An adult who spends a balance early loses less of it to inflation than this counts, and savings built after year 0 also lose value, which this does not count. So it is the share of the gap that the year-0 balance alone accounts for, under the all-wealth-is-cash assumption, not a run of a different model. S59 builds asset classes and returns and runs that model. Until then every published wealth-poverty and real-wealth result under the programme is, to this extent, a result about the assumption.

## 3. The wealth harm with adults outside the labour force (Part C)
S61's row L (the frozen yardstick with `lf`), C2.2 design, 20 years. Wealth poverty is programme minus no programme.

| Environment | Adults | Published | If opening balances kept their value | Erosion share of the real-wealth gap |
|---|---|---|---|---|
| Reference | all, without `lf` | +0.7 | −12.1 | 92% |
| Reference | all, with `lf` | +9.8 | −15.8 | 96% |
| Reference | outside the labour force (86 of 500) | +27.6 | −28.6 | 113% |
| Reference | in the labour force | +6.1 | −13.1 | 93% |
| Adverse | outside / in | +38.2 / +34.9 | −28.8 / −14.7 | 118% / 97% |
| Stress | outside / in | +41.7 / +45.6 | −27.4 / −12.1 | 117% / 96% |

The year-20 flows for adults outside the labour force (Reference, real dollars per year, no programme → programme):
- wages $0 → $0;
- conversion income $0 → $19,200;
- disposable income $33,700 → $52,500;
- own cash cost of essentials $48,100 → $16,900.

So the programme's flows help them more than anyone. The harm is the erosion of what they held at the start (mean opening balance $494,000, against $511,000 for adults in the labour force). Adults in the labour force rebuild more of it from wages and larger conversion income ($36,800). This is the mechanism S61 named as likely; it is now traced. For S63: the `lf` wealth-poverty harm is a consequence of the all-wealth-is-cash assumption, and should not be read as a headline before S59's asset classes.

## 4. What S59 and S63 take from this
- **S59 (asset classes).** Section 2's shares, and section 3's split, are the measure of what the all-cash assumption does to each published wealth result. Re-run the same decomposition on S59's rows so the change can be read against it.
- **S63 (freeze).**
  - The fixed-share rows are reported at 20 and 40 years with the PTFs' switch year beside each.
  - The low end of the curve is not read as an optimum.
  - No sentence attributes anything to PTF damping in the release rows.
  - Every wealth result is read beside section 2's erosion share.
  - The `lf` wealth harm is labelled as section 3 explains.
- **S62 (PTF realism).** Decide whether the surplus split's switch should read capital against the share the PTFs serve (section 1, "a model question").
- **Reproduce.** In a clean checkout of `4e9d841`:
  - `node dev/tools/s66_trace.js --check`
  - `node dev/tools/s66_trace.js PART ENV --seeds=1-100 --out=FILE` (PART A, A40, B, C; ENV ref, adv, st; A was run as seeds 1-50 and 51-100)
  - `python3 dev/tools/s66_table.py DIR`
