# The measures study and the visual suite's second pass

Oct 14, 2026. Plain-words report for Duke. The plans behind this work are `dev/plans/suite-v2-plan.md` and `dev/plans/next-study-plan.md`; the choices are in `dev/DECISIONS.md`, Session 12.

## What was done

1. **A new study is running.** It measures, for every simulated adult in every year, the things the visual suite page could not show yet: how far each person's money goes with the program compared with the same person without it (EPPM), the money left each month above basic living for everyone in both runs (FBS), the equity community-housing members build (Acre Equity, for the CSI), the wealth Gini net of rent and interest, how people move between the six BLEI steps, and breakdowns by income fifth, household type, age and membership. It runs on one Runpod pod (16 cores, $0.48 an hour, a 4-hour limit) over 500 paired runs in each of the three environments, at 20 and 40 years. It changes no rule of the model: it reads quantities the model already keeps. The pod checks this itself: every published figure of the v5.6 release must come out the same, or it saves nothing.
2. **The visual suite page has a second pass** (not yet linked from anywhere, as before). Each of the paper's six measures now has its own card: the question in plain words, the answer for no program and Compassionism, how it is computed here, how that differs from your paper, what it does not show, and a status badge: *Measured*, *Measured differently from the paper*, *Partly modelled* or *Not modelled*. A new section, "Who gains, and how people move", fills in when the study's data is added. Until then, the cards that need the study say so.
3. **IPBI now shows what the model does have:** the public costs avoided (prisons, hospital and psychiatric stays, homelessness), the same figures as the main page's cost section, beside the program's cost. In the Stress Test the homelessness figure is negative (more people unhoused), and the card says so in words.

## Things to check against your vision

These are flagged, not asked: you delegated the math, but each touches a claim in your BLEI paper. Please say if any misrepresents what you meant.

- **EPPM is measured in the model's own terms, not with the paper's formula.** The paper counts the allowance at about twice its face value ($2,502 of market purchasing power for $1,200 of allowance), because community prices make it go further. The model already applies those community price cuts separately, so using the paper's multiplier as well would count the same gain twice. The model counts the allowance at face value and adds the price cuts as their own part. So the model's figures will be well below the paper's worked example (5.80× for one near-poverty household). That is a difference in method, not a defect in either.
- **Each person is compared with themselves.** EPPM sets each adult with the program against the same adult in the no-program run of the same simulation (the same starting wage, savings and luck). This avoids the usual problem that people who join may differ from those who do not. It includes the program's effects on prices and wages.
- **The program's price rise is inside the result.** In the main reading the Source's payout is new money, and the model's prices rise about 50% a year (the release's own figure is 50.8% a year at Reference over 20 years; the price level ends about 2,440 times where it started). The page's sentence about this was checked and is accurate. Every figure on the page is in today's prices, so the rise is taken out; but it is why savings lose their worth and why the top of the ladder falls in that reading. In the reading where every dollar is backed by new output, prices do not rise.
- **IPBI is "partly modelled".** The model's avoided costs are savings to public budgets across the whole population. They are not the dollars your paper estimates for a non-participant household ($22,800 to $59,900 a year across five channels). The page cites the paper's range but does not put it beside simulated results. Market growth, productivity and property values are marked "not modelled", each with what it would need.
- **CSI is answered by simulation.** The model runs the years instead of projecting them with your closed formula, and adds Acre Equity in full (it is kept apart from savings and never counted twice). It is labelled "simulated reading".
- **Your paper's own discrepancies are not copied.** Where the page cites a paper figure that the paper gives two ways, it says so (the near-poverty household's EDC is 0.625 in the paper's tables and 0.744 in its appendix). The paper's Month-0 BLEI (71.3 in its table, 70.7 from its own arithmetic) is not cited.

## What the study does not include

- **New mechanisms.** None of the planned new mechanisms (more public costs avoided, a cost-of-living line weighted by population, spending that raises other people's incomes, a wider safety net, financing) is in this run. Each needs sourced numbers and a proof that switching it off changes nothing, which did not fit before the launch.
- **Children.** The ladder stays adults only, and the page says so.
- **The outside audit.** The audit prompt (`dev/plans/next-study-audit-prompt.md`) had no replies back by the launch. The definitions can still change when the results are ingested, because the study saves each person-year's parts, not one finished number.

## How it was checked

- A two-seed trial in all six settings passed every self-check: no accounting identity failed, each adult's below-30-days status adds up to the model's own figure, the ordinary wealth Gini equals the model's, every adult has a twin, and the parts of EPPM add up to the whole.
- With the study's switches on, all 4,696 results of a three-seed comparison in two settings were identical to the published model's.
- The page checks: validate, unit (222), domtest (142), the glossary check, the figure check (every number on the suite page equals the data, 3,888 numbers in 12 views, and 1,311 study numbers on a two-seed test file that is never shown on the page), and the no-figure-change comparison (no figure, engine or data file moved).

## What happens next

When the pod finishes, its six files are copied into the release data, the page fills in, and this report gains the results. Linking the page from the findings explorer waits for your approval, in a separate pull request.
