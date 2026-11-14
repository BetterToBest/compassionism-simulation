# Who stops working, and who comes back: yearly movement in and out of the labour force, and the programme's participation margin (S73)

Nov 14, 2026. Preregistered in BetterToBest/research-update `prereg/2026-11-s73-participation.md` (with Amendment 1, before the pilot). Engine commit `d12fd0f` (pull request 103). Results: BetterToBest/compassionism-sim-results `s73-participation-d12fd0f`. Tables: `dev/runs/s73-participation/tables.md`.

## In short
1. **People now move in and out of work each year.** Until now, S61's adults outside the labour force stayed out for the whole run and everyone else stayed in. Now, each year, about 3.6 in 100 working-age adults in the labour force stop working all year (for care, illness, school or early retirement) and about 18 in 100 of those out come back. The rates come from 18,937 adults the Census Bureau's survey interviewed in both March 2025 and March 2026. Today's out-of-work share (17%) holds, but over 20 years about 65% of adults spend at least one year out.
2. **Counting that movement makes both designs cut basket poverty by 1 to 2 points more** (release design: 1.1 to 1.4 points; C2.2: 1.0 to 1.9 points). Programme inflation is also 0.6 to 3.4 points a year lower. A spell out of work now falls on more people for shorter times, and the programme's floor catches them.
3. **Some people now stop working because of the programme**, as in the US guaranteed-income experiment. The same income effect as before (16 cents less earnings per unconditional dollar) is now split: 43% of it falls on people who stop working for the year, and the rest falls on hours. On the $12,000-a-year check, participation falls 1.3 points (the experiment: −4.2, interval −7.5 to −0.9). This passes the test S60 failed (0.0). It is still a third of the experiment's estimate, and the report says why below.
4. **Under the programme, 1.3 to 4.4% of adult-years are spent out of work because of it.** That is 3.5 to 4.3 points fewer adults with earnings under C2.2, and 1.3 to 3.0 points fewer under the release design. Basket poverty is 0.1 to 1.0 point higher than with the flows alone. Wealth poverty moves by at most 0.14 points. The C2.2 Stress figure is 1.005 points, just over the preregistered 1 point, so the margin goes to the specification screen (S70) as headline-moving. So do the flows.
5. **Neither the price rule nor the contribution moves much.** Under C2.2 paid by the flat contribution on wages, the rate stays at 85.1% of wages and inflation changes by less than 0.1 points a year. The margin keeps expected earnings unchanged, so the wage base hardly moves.
6. **Unpaid work.** People who leave paid work may care for children and family, do community work, or build something new. The model counts none of that as income or output. It counts only what leaving paid work does to earnings, prices and the contribution. The survey's own leavers give care as the most common reason (37%; women 45%). Claude's reading of the design is in section 6.

## 1. What was built (MODEL_SPEC 14.15)
- **`lf.fl`, yearly flows.** Each year from year 1, an adult under 67 in the labour force stops working for a reason with the chance for their group. Groups are household type, and age band and sex where adults have them, which is only with ageing. An adult who is out comes back with the chance for their reason. The draws come from the flows' own random stream, two per adult-year in any state, so paired runs stay paired. Main reading `'stock'`: exits are set from the survey's returns and today's shares (`exit = return × share out / share in`), so today's shares hold. The survey's own exits are higher because they include ageing: people leave more than they return as they get older. At fixed ages those exits would lift the out share to 28%, so they are a second reading (`'panel'`) for runs with ageing. A leaver takes S61's own income for the reason. A returner's wage is the wage at exit moved with prices. Real wages do not grow while out (a simplification; the evidence shows a pay penalty after time out, which is not modelled).
- **`lf.pm`, the participation margin.** One income effect per unconditional dollar (guardrail 7), split between two margins. `L` is the earnings a worker gives up to the programme's dollars this year. The worker leaves for the year when a personal draw, fixed for the run, is below `q = pm × L / E`, where `E` is the year's earnings. A worker who stays cuts `(1 − pm) × L / (1 − q)`. Expected earnings are exactly today's (unit test, exact over the draw). The same people tend to stay out while the programme's dollars stay large next to their earnings, and those with the most programme dollars per dollar earned leave first. A leaver gets no unemployment insurance (a quit), and SNAP's work rule reads the year as not worked. `pm` = 0.43 is the extensive margin's share of Chetty's (2012) compensated elasticities, 0.25 / (0.25 + 0.33). That source is already in the engine. Using it assumes income effects split between the two margins as wage effects do, a modelling assumption. Swept 0, 0.25, 0.7, 1.
- With both options off, every figure is identical (guard test; unit test against S61's reading). There are 8 unit tests. The candidate main row gains `lf: {fl: 'stock', pm: 0.43}`. In the on-together tests, 154 rows × 3 environments pass, including the new row (the survey's flows with the whole income effect on leaving).

## 2. The source (`sources/s73_lf_flows.py`)
Census Bureau, CPS ASEC 2025 and 2026 public-use files. About half of one March's sample is interviewed again the next March. 39,927 identifier matches; 18,937 adults aged 25-63 pass the check (same sex, age up 0-2 years). "Out" uses S61's definition: did not work at all in the year, because of illness or disability, retirement, care of home or family, or school.

| | survey (linked adults) | engine, no ageing, no programme |
|---|---|---|
| out of the labour force all year | 17.0% (full sample 17.2%) | 17.3% at year 0; 17.1% mean; 16.9% at year 20 |
| stopping work in a year, per 100 in | 4.7 (survey's own); 3.6 (stock-holding) | 3.6 |
| coming back in a year, per 100 out | disability 12, retirement 11, care 22, school 44 | 17.6 overall |
| reasons of those who stop | care 37%, retirement 31%, disability 24%, school 8% | care 47%, retirement 15%, disability 23%, school 16% |

The engine's reason mix differs from the survey's leavers because, at fixed ages, the stock-holding exits replace the life cycle's retirements with the churn of shorter spells. With ageing and the stock-holding exits, the share falls from 18.5% to 16.9% over 20 years. With the survey's own exits it rises from 18.5% to 24.7%. Today's 17-19% lies between these. The survey's exits seem to run above its age profile, possibly because movers are lost to the link, so `'panel'` overstates leaving. With ageing, `'stock'` is the closer reading and `'panel'` is printed beside it.

## 3. The check against the US experiment (S60's check, rule A)
$12,000 a year to every adult and no programme otherwise, 100 seeds. Adverse and Stress give the same figures to the dollar.

| margin | adults with earnings | inside the study's interval (−7.5 to −0.9) | earnings per transfer dollar |
|---|---|---|---|
| 0 (today) | 0.00 points | no | −11.2 cents |
| **0.43 (main)** | **−1.26 to −1.30 points** | **yes** | −10.2 cents |
| 1 | −3.0 to −3.1 points | yes | −9.5 cents |

**Rule A passes.** Participation lies inside the interval, and earnings per dollar are within 2 cents of the run without the margin (1.0 cent). The rule keeps each worker's expected loss exactly. Where the remaining cent comes from in a whole run is not traced. Why only a third of −4.2? The experiment gave $1,000 a month to low-income adults aged 21-40, for whom it was a large share of earnings. The engine gives it to every adult, most of whom earn far more, and under the one-rule margin the chance of leaving is proportional to the transfer over earnings. Even with the whole income effect on leaving (`pm` 1), the change is −3.1 points. The check is passed by the main value, not matched: no value was chosen from it.

## 4. Results (paired over 100 seeds; full tables in `dev/runs/s73-participation/tables.md`)
Effects of each design against its own no-programme run, in points. Intervals are 95%.

**The flows (rule D: flows alone minus today's main row):**

| | Reference | Adverse | Stress |
|---|---|---|---|
| release: basket poverty | −1.06 (−1.30, −0.83) | −1.44 (−1.70, −1.18) | −1.22 (−1.41, −1.03) |
| release: wealth poverty, yearly average | −0.37 | −0.42 | −0.23 |
| C2.2: basket poverty | −1.92 (−2.20, −1.64) | −1.33 (−1.60, −1.06) | −0.98 (−1.24, −0.71) |
| C2.2: wealth poverty, yearly average | −0.35 | −0.36 | −0.42 |
| programme inflation (release / C2.2), points a year | −1.1 / −1.4 | −2.4 / −2.7 | −0.6 / −3.4 |

**The margin (rule C: margin 0.43 minus flows alone):**

| | Reference | Adverse | Stress |
|---|---|---|---|
| release: adults with earnings | −2.45 | −3.02 | −1.25 |
| release: basket poverty | +0.44 (+0.36, +0.53) | +0.42 (+0.32, +0.51) | +0.11 (+0.04, +0.19) |
| release: wealth poverty, yearly average | −0.01 | −0.04 | −0.03 |
| C2.2: adults with earnings | −3.47 | −4.23 | −4.25 |
| C2.2: basket poverty | +0.53 (+0.48, +0.59) | +0.67 (+0.60, +0.73) | +1.00 (+0.92, +1.09) |
| C2.2: wealth poverty, yearly average | +0.13 | +0.14 | +0.14 |
| programme leavers, % of adult-years (release / C2.2) | 2.5 / 3.5 | 3.1 / 4.4 | 1.3 / 4.4 |
| earnings forgone by leavers, per adult-year (release / C2.2) | $1,145 / $1,693 | $1,154 / $1,682 | $471 / $1,657 |

The C2.2 design still cuts basket poverty by 31 to 39 points with the margin on (38 to 46 with ageing), and the release design by 9 to 23. At `pm` 1 the margin costs up to 2.5 points of C2.2's cut (Stress). Leavers keep the programme's floor, but they lose earnings, unemployment insurance and SNAP's work-rule months. Their expected earnings are unchanged, but who bears the loss changes: a few lose everything for a year rather than many losing a little. That is why basket poverty rises while expected earnings do not.

**Through the price rule and the contribution (rule E):** with the margin, programme inflation changes by −0.03 to −0.08 points a year (Source rows). Under the flat contribution on wages (C2.2, S72's D21 row), the rate stays at 85.1% (change −0.01 points) and inflation changes by −0.03 to −0.10 points a year. Because the margin keeps expected earnings, the wage base the contribution is charged on and the income the price rule divides new money by hardly move. The margin changes who has earnings, not how much is earned in all.

## 5. The preregistered rules
- (A) Validation: **passed** (section 3).
- (B) Recommendation to S63, fixed before the results: `lf {fl: 'stock', pm: 0.43}` in the main row; `pm` 0 and 1 beside every poverty and work result; `fl 'panel'` with ageing as the ageing rows' reading (printed beside `'stock'`, which holds today's shares better; section 2). The extra `pm 1` row of the rule's second sentence is not needed, since rule A passed. It is printed anyway, as the upper reading.
- (C) The margin moves C2.2's basket poverty by 1.005 points in Stress, over 1 point: **headline-moving; to S70's screen.**
- (D) The flows move basket poverty by more than 1 point in five of six design-environment cells: **headline-moving; to S70's screen.**
- (E) Reported above, with intervals in the tables.

## 6. Unpaid work: Claude's reading of the design (research rule 6)
Duke's note (ledger, Nov 13): people who leave paid work may do work of value the market does not pay for: care of children and family, community work, inventions and new businesses.

**What the Hub says.** In the Creative Currency Octaves, Basic Units can be converted into primary currency for "essential services, creative work, skill development, community building, cultural contribution, and PTF business operations" (glossary). The research summary ties the Flourishing threshold to "the capital commitment horizon required for entrepreneurial ventures to become viable". So the design means to reward some work the market does not pay for, and to make starting something new safer. The pages read do not name care of one's own children or family as a converting activity.

**Claude's reading (a modelling assumption where the text is silent):** the model counts unpaid work only where the design pays for it. That means conversion through projects, which the engine already models and which an adult outside the labour force keeps under `lf conv 'keep'`. It does not give care of one's own family any converted income or market value, because the Hub does not say it converts. It does not model a business started by a leaver. This is the cautious reading. It understates the programme's value to the extent that leavers' care, community work and ventures have value, and it does not count them as poverty-reducing.

**What the model counts beside the participation result:** the adult-years out because of the programme (1.3-4.4%), their earnings forgone ($470-1,690 per adult-year averaged over all adults), and the survey's reasons for today's leavers (care 37%; women 45%). **What it leaves out:** the value of the care, community work and new ventures done in that time; any effect on children's outcomes; and the programme's leavers' own reasons (the model gives them none). A valuation of unpaid time, for example at a replacement wage, would be an illustrative projection. It is not computed here and would never enter poverty or a headline. If Duke means family care to convert under the CCO, that is a change to the design, not the model: a ledger decision.

## 7. Limits
- The linked sample loses people who move house; its out share (17.0%) is close to the full sample's (17.2%).
- Returners keep their real wage from exit; the pay penalty after time out is not modelled.
- The margin splits the income effect only; the response to the programme's raises stays on hours.
- A spell keeps its reason; a person out for care who later is out for illness is not followed.
- The margin's share (0.43) assumes income effects split as wage effects do; the check against the experiment is passed by it, not used to set it.
- Without ageing, adults have no age or sex, so flows differ by household type only.
- Hours depend on population size in the frozen engine (S68 part 2).

## 8. For S63 and S70
- **S63:** carry `lf {fl: 'stock', pm: 0.43}` in the main row, with `pm` 0 and 1 beside every poverty and work result. With ageing, carry `fl 'stock'` and print `'panel'` beside it. Report programme leavers and their earnings forgone beside every participation figure, and the section 6 statement of what the model leaves out.
- **S70:** screen `lf.pm` (0-1) and `lf.fl` ('stock', 'panel', and off). Both moved a headline by over 1 point here.

## Reproduce
In a clean worktree at `d12fd0f`: `node dev/tools/s73_pilot.js ENV 100 DIR` (ENV ref, adv, st), then `node dev/tools/s73_table.js DIR`. The source: `python3 sources/s73_lf_flows.py DIR25 DIR26 --json=sources/s73_lf_flows.json`, with the two Census files unzipped (hashes in the script).
