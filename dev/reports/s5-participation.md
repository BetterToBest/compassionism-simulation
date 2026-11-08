# S5: the participation figure

Nov 8, 2026. Reads the full batch's participation studies (D at 500 adults, D10 at 10,000 adults; engine `ce8d030`, results `prog-d-ce8d030` and `prog-d10-ce8d030`, 500 seeds each, all checks pass). Rule: `prereg/2026-11-study-program.md`, decision rule 5. Tool: `dev/tools/s5_participation.py`. Every estimate: `dev/runs/s5-participation/estimates.csv`; every table: `dev/runs/s5-participation/tables.md`. No engine change.

## What was asked
How do the programme's effects change as the share of adults who join goes from 2% to 90%, and what one participation figure can the Hub state? The grid is for the as-released design (opt-in, $1,200 payout); under the C2.2 design everyone is covered automatically, so the grid does not apply to it (study programme, Amendment 4).

## The one figure
**By the preregistered rule the figure is 2%: the lowest level in the grid, and the lowest level in every environment, horizon and 10,000-adult cell where anything is detected.** At 2% the release row lowers all three of: the share below 30 days of basic living (design-neutral reading), the share below the cost of living, and the share with too little wealth at the last year, with intervals that exclude zero (Reference, 500 adults, 20 years, CPS yardstick, raise off: +0.71, +2.15, +0.95 points).

This is a detection level, not a viability threshold, and it should not be read as "2% is enough". Two reasons:

1. **The gain on wealth does not last.** Under the headline settings, wealth improves only at 2% and 5% (+0.95, +0.58 points). From 10% it gets worse, and worse with every step up: -0.21 at 10%, -3.09 at 20%, -14.19 at 50%, -22.43 at 90% (intervals exclude zero from 10%). The two other measures keep improving all the way: basic living +10.44 and cost of living +18.08 points at 90%. Programme cost rises from $1,963 a person-year at 2% to $35,736 at 90%, and inflation from 0.008 to 0.34 points a year. Under the study's own rule (a gain is stated only if basic living, cost of living and wealth all gain, guardrail 6), the release row shows a gain on all three only up to 5% of adults joining (Reference, headline cell); 10% with the raise on or at 40 years; and 90% only in one cell (Reference, 40 years, raise on, CPS yardstick, where wealth stays favourable at every level). In the other 23 cells the range is 2% to 10% or narrower.
2. **The as-released yardstick often finds nothing.** With the as-released wage scale, no level in the grid improves all three in the Reference, Adverse and Stress environments at 20 years (raise off), because basic living or wealth does not improve; the same holds at 40 years in Adverse and Stress.

Cells (every environment, 20 and 40 years, both yardsticks, raise off and on, and D10) are in `tables.md`. Beside the headline: Reference at 10,000 adults gives the same figure (2%), same range of favourable levels (up to 5%), and the same decisions as 500 adults at every level for all three outcomes (in Stress the basic-living decision differs at one level, 50%, where 500 adults show no stated effect and 10,000 adults a gain). Adverse and Stress give 2% and a range of 2% (raise off) or 5% (raise on).

## Is the curve a straight line?
Not for two of the three outcomes (departure from the straight line through the origin and the 90% effect; stated where the interval excludes zero and the departure is at least 1 point; headline cell): cost of living lies above the line at every level up to 70% (+1.1 to +1.7 points), so most of its gain arrives at low participation; wealth lies above the line up to 20% (+1.5 to +2.3) and below it from 50% to 80% (-1.6 to -2.6), the shape of an effect that reverses. Basic living is within one point of a straight line at every level (largest departure -0.8).

## What this does not tell us
The engine has no network effect and no collapse below a minimum share of participants (its own warning says so). So the Hub's "30% viability", "55% minimum" and "75% minimum viable participation" can be neither confirmed nor refuted by this engine, and no run supports them: none was produced by any code (`audits/early-figures.md`). The 40% and 55% tests the engine does run (S55) are about the PTFs' share of a zone's essential sales, not about how many adults join the programme.

## What the Hub should say (lands through S24/S25)
- Replace every statement of a participation threshold (30%, 55%, 60-65%, 75%) with: *in the simulation, the as-released design lowers poverty on all three measures only while a small share joins, and the wealth result turns negative as participation grows; the model has no minimum-participation threshold, so none is claimed.* Cite this report and the headline row (Reference, CPS, raise off).
- Where a paper needs one number: "2% is the smallest share in the study at which every measure improved; wealth stays improved up to 5%" (Reference, 20 years, CPS yardstick, raise off), plus the decision rule's words that it is a detection level.
- Papers and pages known to state one: CCO-PTF integrated framework (30% viability), economic modelling and simulation paper and BLEI paper section 6.1 (55%; the BLEI text's 40% and 55% density tests are about PTF merchant share and are covered by S55/S25), replication page (75%). "60-65%" was not found in the audits here; S24 greps the Hub corpus for it and every other form.
- Do not carry the grid over to the C2.2 design: there everyone is covered, so participation is not a choice. S25 says so beside any participation figure.

## Checks run
The tool checks: seeds 1-500 contiguous with one engine commit in both folders; the headline cell present; 24 cells for D and 3 for D10; every estimate finite; each mean inside its own interval. Estimates are the preregistered paired differences with a paired bootstrap (10,000 replicates, seed 20261101).
