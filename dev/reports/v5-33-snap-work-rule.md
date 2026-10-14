# SNAP's work rule, built behind a switch that stays off

Oct 14, 2026 (ledger step s166, decision d209, issue i23). This adds no figure to any page and changes no published number. The switch is off by default, and with it off every output is identical, as tested. The rule will run beside the main results in the next study (ledger step s165). Whether it becomes part of the main results is a separate decision for a v5.6 release, after Duke has seen both sets of figures side by side.

## 1. What the rule is (checked against the law and USDA)

SNAP (food stamps) has a time limit for "able-bodied adults without dependents". Public Law 119-21 (July 4, 2025) widened it, and USDA put the change into effect on November 1, 2025. Each element below was checked against the statute as amended (7 U.S.C. 2015(o)) and USDA's October 2025 implementation memos. The quotations and links are in `sources/snap_work_rule.md`.

| Element | The law and USDA | In the model |
|---|---|---|
| Who it covers | Ages 18 to 64 (USDA's reading of the law's "over 65"), with no child under 14 in the household | Adults aged 18 to 64 in a household with no child under 14. Adults with no age recorded (runs without aging) count as covered. |
| The test | Working 20 hours or more a week, averaged monthly, or a work or training program | The model's pay is for a full-time job (2,080 hours a year, the hours MIT's living wage assumes). A month counts against the adult when they are out of work, or when their hours at work have fallen below half of full time. |
| The limit | SNAP for 3 months in any 36 months in which the test is not met | Each adult has a clock with the countable months used in the last three years. Months beyond 3 get no SNAP for that adult. |
| Who is exempt | People receiving unemployment insurance, people medically unfit for work, pregnant women, students, people in treatment, caregivers of an incapacitated person, and some Native Americans | Weeks on unemployment insurance do not count. The model has no medical, pregnancy, student, treatment or caregiver states, so those exemptions cannot apply. |
| State exemptions | A State may exempt up to 8% of covered people each year | Applied as an expected share: the benefit cut is 92% of what the rule alone would cut. No one is picked at random. |
| Area waivers | Now only where unemployment is over 10% | Not modelled. The model's economy stays well below 10% unemployment. |
| What the household loses | The adult is not counted as a household member; their income still counts | In each lost month the household's SNAP is worked out with one member fewer and all income still counted. |

## 2. Choices where the law had to be fitted to a yearly model (modelling assumptions)

- **Timing.** SNAP is set at the start of each year from last year's income, and the work test reads last year's work as well.
- **Retirees** are treated as exempt. Some retire before 65, and the real rule would cover them. This is the cautious reading: it does not overstate the rule's bite.
- **Regaining eligibility.** The law lets an adult regain SNAP by working 80 hours in 30 days. A year with enough work counts no months against the clock anyway, so this is not modelled separately.
- **No new random draw.** The rule reads things the model already has: each adult's weeks out of work, their unemployment insurance, their hours, their age and their household's children. The CRN guarantee of eight draws per adult-year holds.

## 3. What it does to today's safety net alone

This is a first look: 20 seeds, the v5.4 main row and its no-program run, both with today's safety net, rule off against rule on. The study (s165) will give the 500-seed figures.

| | Reference, no program | Reference, with Compassionism | Adverse, no program | Adverse, with Compassionism |
|---|---|---|---|---|
| Adult-years losing some SNAP months | 0.71% | 0.75% | 1.64% | 1.79% |
| SNAP months lost per adult-year | 0.03 | 0.04 | 0.07 | 0.09 |
| SNAP cut per adult-year (today's dollars) | $5.75 | $6.89 | $13.52 | $17.45 |
| SNAP received per adult-year, before, then after | $703, then $697 | $720, then $713 | $1,082, then $1,067 | $1,047, then $1,028 |
| Below the cost of living (% of adult-years), before, then after | 50.20, then 50.20 | 20.06, then 20.08 | 67.56, then 67.56 | 32.00, then 32.04 |

## 4. Claude's reading of how big an effect to expect

Small, in the model, and smaller than in the real world:

- **Who the rule reaches.** In the model every working-age adult has a job or is between jobs. Most spells out of work are short (the average is about 15 weeks in normal years), and some are covered by unemployment insurance. So few adults ever pass 3 countable months. In the US, many of the people the rule removes have not worked for a long time, or work irregular hours, and the model has neither group. The model's effect is best read as a **lower bound** on the rule's real effect.
- **In both arms.** The rule cuts today's safety net with and without Compassionism. In this first look the cut is slightly larger with Compassionism (its adults work a little less, so a few more fall under 20 hours a week). That nudges basket poverty with the program up by about 0.02 to 0.04 points.
- **Expected change to Compassionism's measured gain:** a few hundredths of a percentage point, within the run-to-run spread. The 500-seed study will say whether it is distinguishable from zero.

## 5. Something found while preparing the study: the published results leave out today's safety net

The note on decision d209 said today's safety net (SNAP, the earned income tax credit and the refundable Child Tax Credit) is in both arms of every comparison. That is true of the 500-seed study's safety-net rows (published on the study page). It is **not** true of the main results on the front page and the findings page (v5.4 and v5.5): their runs, with and without Compassionism, have no SNAP, EITC or CTC. The work rule only exists inside SNAP, so a v5.6 panel "with the SNAP rule" must also add today's safety net to both arms.

The safety net moves figures on its own. On 20 seeds, comparing the guard test's runs with the same runs plus the safety net, basket poverty with Compassionism changes by +0.11 points (Reference), −0.20 (Adverse) and +0.54 (Stress). The no-program run changes by +0.04, +0.03 and +0.03. These are 20-seed figures. That the safety net raises basket poverty slightly is itself surprising, and should be explained before release. The likely cause is people working a little less as benefits phase out (the safety net's own work response).

So the study job (ledger s165) runs three things on the same engine:
1. the full panel with today's safety net **and** the rule (`--snab`);
2. the rule's own effect: the main row and its no-program run, with the safety net, rule off and on, 500 seeds;
3. the v5.5 panel already published, which has neither.

Together these let the v5.6 report separate what the safety net does from what the rule does. Whether v5.6's main results include the safety net is part of the decision in issue i23. This note flags it for Duke rather than settling it.

## 6. Tests

- **Switch off is bit-identical.** `node dev/tools/guard_test.js` passes: 25 v5.4 panel rows, seeds 1 to 20, three environments, every output. The guard test runs no row with today's safety net, so a second guard was added, `dev/tools/snap_rule_check.js`. Its reference was made on the engine *before* the rule was added. It shows the main row and its no-program run with today's safety net identical in all 483 outputs, for 20 seeds in each environment.
- **Engine lineage.** `node dev/tools/engine_lineage.js prove "SNAP work rule behind a switch"` links the new engine to the published panels: the six 12-seed release panels have the same fingerprints.
- **Unit test (by hand):** the 3-months-in-36 clock over seven years, and the household cut for a single adult and a couple with the 8% State exemptions.
- `harness.js validate`, `unit`, `domtest.js`, `check_figures.js` and `no_figure_change.py compare`: see HANDOFF.md for the results on the final commit.

## 7. For Duke

- Nothing on the pages changes with this pull request.
- Issue i23 is the decision that matters: whether, after seeing the 500-seed figures, the rule should be part of the main results (a v5.6 release). Section 5 adds one thing to it: the rule brings today's safety net into the main results too.
