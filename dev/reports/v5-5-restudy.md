# The v5.0 restudy: every mechanism, including your four new items

Oct 2, 2026 · Claude, session 31 · 500 paired runs, three environments · **this replaces `11-restudy.md` as the report the release gate asks Duke to read**

## What was run

The same 500 simulated adults for 20 years, 500 times, with Compassionism and with no programme (the same random draws for both), in three environments: Reference (no recessions), Adverse (recessions, 2% outside inflation, an automation wave) and Stress (Adverse with weaker settings: 40% take part, a smaller allowance).

v5.0 is session 30's release candidate plus your four items:

1. **Private essential-service businesses** pass what conversion adds to their BU customers as lower prices, and pay their workers what community-business workers earn (your correction, d140).
2. **Creative projects' output counts at market value**, because they offer it to members below the market price and are paid at their earned rate (Claude's reading of your d138 answer). **Community businesses add capacity within a year**, paying for the capital they borrow (d137). **Only businesses' conversion is capped by their capacity**; individuals and Collectives are not (d139).
3. **The spending layer:** in recessions, the programme's spending fills the idle capacity, at a published multiplier.
4. **Wider public costs avoided:** prisons, hospital stays and psychiatric care, beside homelessness.

## The main result

| Against no programme | Reference | Adverse | Stress |
|---|---|---|---|
| Below 30 days of basic living (your BLEI), share of adult-years | **18.7% vs 46.7%** | **33.1% vs 60.0%** | **54.9% vs 60.0%** |
| Below the cost of living, share of adult-years | **22.0% vs 55.2%** | **42.1% vs 78.2%** | **65.6% vs 78.2%** |
| Too little wealth at year 20 | **35.7% vs 52.0%** | 87.1% vs 82.6% (worse) | 90.6% vs 82.6% (worse) |
| Confirmed gain on all three? | **Yes** | No (wealth worse) | No (wealth worse) |
| Prices: rise a year from the programme | 34.9% | 45.6% | 23.8% |
| Hours worked | −3.1% | −6.8% | −4.3% |
| Cost per adult a year (today's dollars) | $29,619 | $27,678 | $10,495 |
| Public costs avoided per adult a year (homelessness, prisons, hospitals, psychiatric care; main reading) | $834-$1,088 (2.8-3.7% of cost) | $1,526-$1,761 (5.5-6.4%) | $686-$739 (6.5-7.0%) |

Every 95% interval is narrow (within about ±0.2 points), so these differences are not chance.

**Against session 30's release candidate**, v5.0 is better on every poverty measure at Reference (below the cost of living 30.0% → 22.0%; too little wealth 47.5% → 35.7%) and on income and BLEI poverty in Adverse and Stress. Wealth poverty in Adverse and Stress is about the same or slightly worse (Adverse 87.0% → 87.1%; Stress 89.3% → 90.6%).

**In everyday words:**

- **At Reference, Compassionism cuts poverty on every measure, by more than in session 30's build.** Fewer than half as many adult-years fall below the cost of living, and about a third fewer adults end with too little savings.
- **In Adverse and Stress it cuts income poverty and BLEI poverty, but more adults end with too little savings than with no programme**, because prices still rise fast (24-46% a year in the model) and savings are not protected from inflation.
- **Who gains.** At Reference, adults who take part gain about $30,300 a year in real resources, the poorest third $22,500, the richest third $24,300. **Adults who do not take part lose about $800 a year** against no programme, and more of them end with too little wealth. In session 30's build they gained $3,167, because as business owners they received part of the conversion premium; under your correction that premium goes to BU customers instead, while prices still rise. In Adverse and Stress everyone has more real income than with no programme, but every group ends with less wealth.
- **Work** falls less than before (−3.1% at Reference against −6.7%), mainly because the private-business correction gives workers profit shares instead of giving owners unconditional dollars.

## What each new item did (500 runs each; reports `v5-1` to `v5-4`)

| | Reference | Adverse | Stress |
|---|---|---|---|
| 1. Private-business correction: below the cost of living / too little wealth | −7.4 / −7.2 points | −7.2 / +3.4 | −0.9 / +2.1 |
| 2. Creative output at market value (capacity speed makes no difference) | −0.6 / −4.7 | −0.9 / −2.3 | 0 / −0.1 |
| 3. Spending layer (recessions only) | none (no recessions) | −1.5 / −1.0 | −1.0 / −0.6 |
| 4. Wider public costs (reporting only) | +$805 a year avoided | +$1,499 | +$680 |

## The readings shown beside it (Reference; too little wealth at year 20, against 35.7% for v5.0)

- **Every Source dollar backed by new output (H1, the optimistic end):** 15.4%, and no group worse off on any test in any environment.
- **Essentials bought with BU counted as backed:** 25.5%.
- **Creative work counted at the cost of its hours (the cautious reading):** 40.4%.
- **Capacity only as fast as reinvestment pays (the 5-year rule):** 35.7% (the same: the capacity limit rarely binds).
- **Everyone joins:** 27.4%, and nobody is worse off.
- **Paid for by a flat contribution on wages instead of the Source:** 72.8% (much worse).
- **Session 30's build:** 47.5%.

## Model limits that matter for these results

- The price rule is simple: new money not matched by output raises prices; there is no central bank, no interest and no protection of savings.
- Spending creates jobs only in recessions; outside them the model has no idle capacity.
- Single adults only (no children or households); one country; no places.
- Child welfare is not among the public costs avoided (no children in the model); the prison figure is carried over from a study of young people losing disability income, scaled by incarceration rates.
- No independent economist has reviewed the model.

## Release gate status

- **Built:** every mechanism in `dev/PLAN.md` steps 1-9 and your four items (steps 14-17), each behind a switch, with tests; the page carries all of them (step 18).
- **Restudy:** 500 seeds in three environments, done (this report).
- **Checks:** validate, unit (every suite) and domtest (97 of 97) pass.
- **Page and harness agree** on the same seeds (domtest).
- **Gains confirmed on basket and wealth poverty:** at Reference yes; in Adverse and Stress **no** (wealth poverty is worse). This report and the page say so plainly.
- **Former stand-ins off by default:** yes.
- **Duke has read this report:** pending.

## Exact commands and files

- Panel: `node harness.js testbed 500 release ref --json=dev/runs/release-panel-ref.json` (and `adv`, `st`), then `python3 dev/tools/merge_panel.py` and `python3 dev/tools/release_figs.py`. Outputs: `dev/runs/step18-release-500-{ref,adv,st}.txt`, `dev/runs/release-panel.json` (embedded in the page).
- Each item against the one before: `node harness.js testbed 500 v5 ref` (and `adv`, `st`). Outputs: `dev/runs/step14-priv-500-*`, `step15-creative-500-*`, `step16-17-v5-500-*`.
