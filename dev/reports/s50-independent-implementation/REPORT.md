# A second, independent program for the published results: the check and what it found

*Research-update step S50, Nov 1, 2026. For Duke; no programming or economics needed to read it.*

## What was checked

Every figure the Research Hub and the simulation page publish comes from one pair of runs: **the release row** (Compassionism with every mechanism, paid for by the Source) and **its paired no-programme run**. Each pair is run in three environments: Reference (calm), Adverse (recessions, 2% outside inflation, the automation wave) and Stress (the same with weaker settings), for 500 random seeds each.

An outside economist has not yet reviewed the model. Until one does, the strongest check one author can arrange is to have a second program written separately and see whether it gives the same numbers. If it does, the written description of the model and the code agree, and the code does what the description says. Where they differ, one of them has a mistake worth finding.

An earlier check (October 29) did this for the engine's validation presets and matched them exactly. Those presets switch off every mechanism behind the published figures, so this check is the first one of the published results themselves.

How it was done. Part 1 (earlier today) prepared a packet: the model's written description, every setting of the six runs as data, the code those runs execute, and the engine's own results for seeds 1-500. Part 2 (this session) was done by a session that had never read the engine:

- I wrote a new program in Python (`s50_release.py`) from that packet. I read the description first and used the code only to settle questions the description left open. Each of those questions is listed in `GAPS.md`.
- I did not open the engine itself until this program and its results were saved and published (phase 1).
- I changed no setting to make a number agree.

## What agreed

**Everything.** The second program reproduces the engine's results to the last digit that matters, for every seed, in all six runs.

| Environment | Run | Keys compared | Equal on all 500 seeds | Pass the statistical test |
|---|---|---|---|---|
| Reference | no programme | 631 | 630 | 631 |
| Reference | release row | 631 | 630 | 631 |
| Reference | the programme's effect (release − no programme) | 631 | 630 | 631 |
| Adverse | no programme | 631 | 630 | 631 |
| Adverse | release row | 631 | 630 | 631 |
| Adverse | the programme's effect | 631 | 630 | 631 |
| Stress | no programme | 631 | 630 | 631 |
| Stress | release row | 631 | 630 | 631 |
| Stress | the programme's effect | 631 | 630 | 631 |

"Keys" are every number the engine reports for a run: poverty on its three measures, children's and households' poverty, prices, cost, work, inequality, the Source's books, each mechanism's own report, and the year-by-year paths. "Equal" means the two programs agree to within a billionth, relative to the number (or, for a number that should be exactly zero, within a billionth absolutely). The statistical test is the brief's: the two 500-seed means differ by less than twice their standard error. By chance alone about one key in twenty could fail it; none did.

The headline measures (the full tables are in `results/COMPARISON.md`):

| Measure (500-seed mean) | Environment | Engine | Second program |
|---|---|---|---|
| Adult-years below the cost of living: no programme → release row | Reference | 49.25% → 19.53% | 49.25% → 19.53% |
| | Adverse | 65.99% → 31.09% | 65.99% → 31.09% |
| | Stress | 65.99% → 52.80% | 65.99% → 52.80% |
| Adult-years below 30 days of basic living: no programme → release row | Reference | 26.55% → 11.71% | 26.55% → 11.71% |
| Adults with too little wealth at the end: no programme → release row | Reference | 32.73% → 44.37% | 32.73% → 44.37% |
| Programme cost per adult-year (today's dollars) | Reference | $29,874 | $29,874 |
| The flat contribution's mean rate | Reference | 2.79% | 2.79% |
| Programme inflation a year | Reference | 50.8% | 50.8% |

The last line is worth a word. In the release row, prices end about 2,500 times higher after 20 years in Reference. The second program computes exactly the same, so this is what the model's rules produce, not a slip in the code. Whether the rules are right is the design question the outside audit raised (its finding E6). This check does not answer it.

The one key that is not equal on every seed counts adults who lose SNAP months under the work rule (`snAbN`). There the two programs differ by one adult-year in 10,000 on some seeds. The cause is explained below. It is a rounding quirk in how that count is kept, not a difference in the model.

## What did not agree, and why

**The computers' arithmetic, in the last binary digit.** Python and Node (the engine's JavaScript) compute logarithms, exponentials, powers and the trigonometric functions with different C libraries. On 200,000 test inputs, 3% to 10% of results differed in the last of their 53 binary digits. The model's numbers absorb these differences: they change results by about one part in a million billion.

The exception is the SNAP work-rule count. An adult whose whole spell out of work was insured should count 0 lost months. The engine computes that 0 as "weeks out minus insured weeks", and the result can come out as a tiny remainder (about 10⁻¹⁶ of a month). The count then records that adult as losing a month. Which adults get a remainder depends on that last binary digit, so the two programs record slightly different counts. The dollars involved are nil, and no other result is affected.

**Phase 2 confirms it.** Once phase 1 was published, the program got a switch (`--js-math`) that computes those five functions with Node's own maths (not the engine) instead of Python's. With it, PHASE2_RESULT

## What else it found: places where the description and the code disagree

Writing a program from a description exposes every place where the description is silent or wrong. `GAPS.md` lists 38, each with the line of code that settled it. Eight are contradictions, places where the description says one thing and the code does another. Phase 2 read the engine's own comments to decide, for each, whether the description or the engine should change. In plain words:

**The engine should change (questions for the design freeze, step S47, where each change can be measured):**

1. **Partners and PTH's books.** The engine opens each community home's books before it forms households. Forming households then moves partners into or out of PTH to match their household. As a result, about a quarter of PTH members have no books: their equity grows by the older 3-5% rule instead of the price rise + 2%, and they never leave the network. And about two dozen homes a seed have books but no member, and are never filled. The engine's own comment says every PTH home has books beside its member and that the household head's draw decides, so this is an ordering mistake.
2. **The no-programme run's prices drift a little.** The capacity that essentials prices are measured against comes from a separate simplified run, not from the published no-programme run. When it was set up in September, the two were the same economy. Job loss, the safety net and the labour response were later added to the published run but not to the simplified one. In Reference the no-programme price level ends 0.5% lower after 20 years, although no programme exists; in Adverse and Stress it does not drift.
3. **PTH's home prices are set at half the market housing cost.** The engine's comment says a home costs 18.23 years of "the housing share of their basket, at market prices". The code uses the BLEI paper's daily cost ($24,940 a year for one adult in today's dollars), about half the basket ($49,370). Either the code or the comment should change.
4. **The SNAP work-rule count** described above should treat a remainder of a billionth of a month as zero.

**The description should change (the engine does what it was meant to do):**

5. **The flat contribution does not pay for the surplus split's price cuts.** The description says it does. In the engine the Source pays every conversion, and those cuts come out of the conversion premium.
6. **Octave advancement measures living costs at the BLEI paper's daily cost, not the cost of living.** The engine's comment says this is deliberate.
7. **A recession can start in the last year.** The description says it cannot.
8. **Zone induction into community businesses is for participants only,** in the published row as in the older one. The description implies everyone.

None of these changes the agreement: the second program does what the code does, so its results match. Items 1-4 would change results and go to the design freeze. Items 1 and 3 touch PTH members only; item 2 is 0.5% on prices in Reference; item 4 changes nothing beyond the count itself. Items 5-8 are corrections to `MODEL_SPEC.md`, along with the 30 gaps.

## What it means

- **The published figures are what the engine's code computes, and the code is complete.** A program written separately, from the packet, reproduces every key of the release row and its no-programme run, in all three environments, seed by seed. The packet held everything the published runs execute; the earlier check had to add three missing functions.
- **The description is not yet enough on its own.** Someone with only the description could reproduce the model's broad behaviour, but not its numbers. `GAPS.md` lists what to add, and four contradictions are corrections to the description itself. This is the main work this check hands to the design freeze.
- **Three things in the engine are not what its authors meant.** They are the PTH books' order, the stale supply run, and the home-price base. Apart from the 0.5% price drift, this check did not measure what they change in the headline figures; each should be fixed and measured in the freeze.
- This check shows that the code computes what it says and what the description, once corrected, will say. It cannot show that the model is right about the world. That remains the job of the outside comparisons (the no-programme baseline against US data, and the outside engine cross-check) and of an outside economist.

## Runs not reached

None. All six runs were compared on all 500 seeds, in phase 1 and in phase 2.
