# The Phi step: how big the jump is, and who sits near it

Oct 6, 2026 · v5.2.2, audit item A7 (GPT audit, section 18) · Claude · 500 paired seeds, three environments · diagnostic only, no change to the model or to any figure

## The question

In the model, a participant's conversion rate gets the Phi bonus (×1.618) the moment their quality score passes 70% of the maximum multiplier. Just below that line there is no bonus; just above it there is the full bonus. The GPT audit asked how big this cliff is, how many people sit near it, and whether the Research Hub asks for a threshold like this or for a gradual ramp.

## What the Hub says (Claude's reading of the design)

- The Hub describes the Phi rate as a tier you qualify for, not a slope. *Cultural Value Integration*, section 2.3: "A contribution C qualifies for Phi rate when: F(C) ≥ F_threshold (Functional effectiveness), A(C) ≥ A_threshold (Aesthetic quality)". The glossary: "A special multiplier tier at 1.618× ... applied when a contribution is assessed as both functionally effective and aesthetically beautiful." The FAQ lists it as a rate with its own review step ("Peer review for aesthetic quality dimension").
- The Hub does **not** say where the threshold is. The model's 70% of the maximum (`CFG.PHI_QUALITY_THRESH`) is a modelling choice, not a figure from the papers.
- Two papers also write the Phi payment as proportional to a quality score (*Optimal Transfer Design*: "M(q) = 1.618 × quality_factor"; *CCO-PTF Integrated Framework*: "P_phi = B × 1.618 × Q", with Q from 0.5 to 2.0). That is a second, continuous formula; the model follows the tier reading, where quality already raises the base rate continuously and Phi is a tier on top.

So the threshold itself is what the Hub describes; the place of the threshold is the model's own assumption. I label it that way.

## How big the cliff is

The rate formula: base rate = 1 + (quality ÷ maximum) × (octave ceiling − 1); above the line it is multiplied by 1.618, capped at maximum × 1.618. The conversion tax rises with the rate, which softens the jump in what a person actually keeps.

At the octave of the typical participant near the line (octave 6, the top, in Reference and Adverse; octave 4 in the Stress Test):

| | Reference and Adverse | Stress Test |
|---|---|---|
| Rate just below the line | 6.60× | 4.50× |
| Rate just above the line | 10.69× | 7.29× |
| Jump in the rate | ×1.62 | ×1.62 |
| Dollars kept per BU converted, below → above | $5.34 → $6.76 | $3.59 → $4.97 |
| Jump in dollars kept | ×1.27 | ×1.39 |

The tax on conversion rises with the rate (4 percentage points for every point of rate above 3×, capped at 75%: about 25% just below the line and 41% just above it in Reference), so the person keeps only about a quarter more per BU (Reference) for crossing the line, not 62% more.

In the runs themselves, participants just above the line (quality 70-71% of the maximum) earned on average $27,096 a year from conversion against $23,475 just below it (69-70%), in today's dollars: ×1.15 in Reference, ×1.14 in Adverse ($21,837 against $19,080) and ×1.18 in the Stress Test ($6,961 against $5,914). That is smaller than the jump per BU because not all of their conversion income goes through their own rate (their share of the business premium does not).

## How many people sit near it

Counting every participant in every year of the 500 runs:

| | Reference | Adverse | Stress Test |
|---|---|---|---|
| Participant-years within 1% of the maximum of the line (quality 69-71%) | 0.58% | 0.58% | 1.37% |
| Participant-years above the line (getting Phi) | 3.7% | 3.7% | 11.2% |
| Their share of all conversion income | 8.4% | 8.2% | 15.7% |

(Reference and Adverse have the same participants and the same quality draws, so the counts match; only the incomes differ.)

## What this means, in everyday words

The cliff is real for one person: a tiny gain in quality score, right at the line, raises the rate by 62% and what they keep by about 27%. But very few people are near the line in any year (about 6 in 1,000 participant-years in Reference), and the people above it get under a tenth of all conversion income in Reference and Adverse and about a sixth in the Stress Test. So the cliff matters little for the results the page reports, which are averages over everyone.

## Decision for v5.3 (recorded in dev/DECISIONS.md)

Keep the threshold as designed: the Hub describes the Phi rate as a tier you qualify for, so a step is the faithful reading, and the cliff is too small at population level to justify a new reading on the page. The threshold's place (70% of the maximum) stays labelled a modelling assumption, and it joins the parameters the v5.4 global sensitivity analysis sweeps (Morris screening first), which is where a parameter with no source belongs. A continuous ramp is not added as a row in v5.3.

## How to reproduce

`node dev/tools/phi_check.js ENV 500` for ENV `ref`, `adv` and `st` (about a minute each); output in `dev/runs/phi-check-ENV.json`, logs in `dev/runs/phi-check-500-ENV.txt`. The tool restates the engine's rate formula and checks it against the engine's own at four points before writing anything.
