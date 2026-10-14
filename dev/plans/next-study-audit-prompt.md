# Audit prompt: definitions for the next Compassionism simulation study

Paste everything below the line into an AI system with web access. It needs no access to the code. Use it with two different systems and bring both replies back. Expected time to answer: 15 to 30 minutes.

---

You are auditing the **definitions** of a planned computer study, before it is run. You are not asked to run anything or to read code. Please be direct: say what is wrong, not only what is good.

## What the model is

An open, in-browser agent-based simulation of an economic design called Compassionism (author: Duke Johnson). 500 simulated US adults are followed for 20 or 40 years in three environments (Reference, Adverse, Stress Test), once with no program and once with Compassionism, using the **same** simulated adults in both runs (so each person has a "twin" without the program). Results are averaged over 500 paired random seeds. Today's US safety net (SNAP with its work rule, the earned income tax credit, the refundable child tax credit) is in both runs. Households and children are modelled. The model has not been reviewed by an independent economist; the code is public at https://github.com/BetterToBest/compassionism-simulation and the main measure comes from the Basic Living Economic Index paper at https://bettertobest.github.io/research-hub/basic-living-economic-index.html.

Key terms: **BLEI** = days of basic living a person's accessible resources cover (savings, a share of monthly pay, one month of the allowance), in six tiers: Crisis (under 7 days), Precarious (7 to 30), Threshold (30 to 120), Stable (120 to 365), Secure (365 to 730), Flourishing (over 730). **Allowance (BU)** = a monthly payment valued at $1 per unit, spendable on essentials at community prices. **Acre Equity** = equity that community-housing residents build, kept separate from savings and not counted in BLEI. **Community prices** = lower prices at community businesses and housing (about 12% to 16% off the basket for business members, 35% off housing for community-housing members). **EDC** = share of income paid out as rent and interest.

## What the study would add

A. **EPPM (how far a person's money goes).** For each person-year, with that person's twin: real resources = (cash income + allowance spent + safety-net receipts − rent − interest − fees) ÷ the person's own basket price index (relative to year 0). EPPM = real resources with the program ÷ real resources of the twin without it. Reported as three parts: the allowance (a transfer, at face value), lower rent and interest, and prices (community discounts net of any program-driven rise in the general price level). The source paper defines EPPM with an extra multiplier on the allowance (about 2.1 times face value, from community prices); the study does not use it, because the community price cuts are already modelled separately and applying both would count the same gain twice. Statistic: ratio of group totals or median of person ratios, with a stated floor for near-zero denominators; also the share of participants above 1. Shown for all participants, the poorest fifth (by the twin's no-program income), and non-participants.
B. **Financial bandwidth** = monthly income plus allowance minus basic cost minus drain, floored at zero, for **all** adults in **both** runs (today it is reported for participants only).
C. **Compound stability, by simulation.** BLEI days plus Acre Equity ÷ daily basic cost, not the paper's closed-form formula.
D. **Movement between tiers.** Each person's tier every year; the share starting in Crisis who are in each tier 5 and 10 years later; years spent in Crisis; time to first exit; re-entry.
E. **Wealth Gini net of drain** (wealth minus rent-and-interest drain times income) beside the ordinary wealth Gini.
F. **Breakdowns** of tiers, EPPM and surplus by: the twin's no-program income fifth, household type, age band, community-housing membership, community-business membership.
G. **Net fiscal position by income fifth:** what each fifth pays (conversion tax, flat contribution, taxes) against what it receives (allowance, price cuts, safety net).
H. **A ladder for children** in households.
I. **Planned new mechanisms** (each would be a separately labelled extra reading, never the headline): public costs avoided beyond prison, hospital and homelessness (emergency services, child welfare); a population-weighted cost-of-living line; a demand multiplier from participants' spending to other people's incomes; labour-force entrants; a wider safety net (Medicaid, housing aid, Social Security, standard unemployment insurance); reconciling tax revenue with outlays.

## What I want from you

Reply with numbered findings. Tag each **[Correction]** (something is wrong or misleading), **[Polish]** (optional improvement) or **[Question]** (I could not judge without more information). One or two sentences each; say what you would change.

1. **EPPM.** Is the definition well-formed? Does comparing each person with their own twin make sense when prices, wages and the safety net are all affected by the program? Is the three-part split sound (what is double-counted or missing)? Which statistic (ratio of totals, median of ratios, something else) would you use, and how should near-zero denominators be handled? Is showing the poorest fifth by the **twin's** no-program income the right way to avoid selecting on the outcome?
2. **Other measures (B to H).** For each, any definitional flaw, selection problem, or way a reader could be misled. Especially: the Gini net of drain (does it make sense for people with negative wealth?), the child ladder (are adult BLEI thresholds appropriate for children?), and net fiscal position (what is missing for it to be called incidence?).
3. **Group breakdowns.** Fixing group membership by the twin's no-program status: is that fair to both runs, and what would you do instead?
4. **Mechanisms (I).** For each, the **primary sources** (with URLs and the number you would use) for a defensible central value and range: public cost of child welfare and emergency services avoided per unit of poverty reduction; a fiscal or local-income multiplier for cash transfers (with the evidence on whether it applies to non-participants); the effect of a wider safety net on how much of a recession's rise in poverty it absorbs (the model's current safety net absorbs about 0.5% of it, against about 73% in the data). Say plainly where you could not find or verify a source; do not invent citations.
5. **What would a skeptical economist or reporter attack first**, and what one sentence on the page would defuse it?
6. **What this list leaves out** that a study of "what standard poverty and inequality measures miss" should include.

Please also list anything you **could not check** and why. Do not rewrite the whole plan; do not suggest a rebuild of the model.
