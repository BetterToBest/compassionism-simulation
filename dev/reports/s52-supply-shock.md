# When prices jump from outside: do PTF and PTH protect the basics? (pilot)

Nov 2, 2026 · research-update plan step S52 · study O · Claude

**PILOT.** Seeds 1-50 on GitHub Actions. These numbers decide only what the full study (seeds 1-500, after the design freeze) must contain. They are not figures of the model and should not be quoted as findings.

- Preregistration: research-update `prereg/2026-11-supply-shock-addendum.md` (written before any run).
- How the shock is modelled: `dev/reports/s52-supply-shock-reading.md` (Claude's reading of the design, readings X1-X9).
- Every table: `dev/reports/s52-supply-shock-tables.md`, written by `dev/tools/s52_shock.py`.
- Per-seed results: compassionism-sim-results `s52-shock-98b6100/` (engine 98b6100; run.txt; SHA256SUMS, all 40 files verified Nov 2).

## The question

The Hub says PTF and PTH give people stable, affordable access to the basics, and that PTF communities hold up against shocks such as "energy price manipulation". The model had never faced a sudden jump in the price of the basics from outside. This study adds one. The real price of energy rises 32.8% over two years from year 5, and 88% of the rise stays. That is the middle of the three largest US episodes since 1967. Food, transport and household energy follow the rise in the proportions seen in US data. A household's whole market basket rises about 2-3% at the peak.

For each group, the study measures **the share of the shock that reaches what its members pay in money**: the rise in their own money costs over the rise in the same basket at market prices, on the same seed, against the same run without the shock. 100% means they pay the whole rise; 0% means none of it. The groups are:
- PTF members;
- PTH members not in PTF;
- other CCO participants;
- adults in none of the three;
- adults who chose not to take part at the start. These are the same people in every design and in the no-programme run. Some of them join later under the release row.

Two designs are tested: the release row as released, and the C2.2 design (automatic distribution, the BU indexed to the cost of needs). Each runs in three environments. The Stress environment shares the Adverse economy and differs in the programme's own conditions, so its no-programme figures equal Adverse's.

## What the pilot shows

**1. The BU, not PTF or PTH, is what protects people from this shock.** With no programme, everyone pays 100% of the shock. The figures below are for the main shock with the main reading (a quarter of the rise is markup; no local sourcing), during the shock, with 95% intervals in the tables.

| Share of the shock paid in money | Reference, release row | Reference, C2.2 | Adverse, release row | Adverse, C2.2 | Stress, release row | Stress, C2.2 |
|---|---|---|---|---|---|---|
| all adults | 52% | 21% | 53% | 22% | 80% | 22% |
| PTF members | 56% | 29% | 57% | 31% | 79% | 34% |
| PTH members (not PTF) | 48% | 17% | 49% | 19% | 79% | 19% |
| other CCO participants | 44% | 19% | 45% | 20% | 58% | 21% |
| in none of the three | 100% | (no one) | 100% | (no one) | 100% | (no one) |
| chose not to take part | 71% | 21% | 72% | 22% | 91% | 22% |

While the BU covers a household's food, housing and medical care, a price rise in those is paid in BU, not money (reading X9). Under the release row, adults outside all three parts pay the whole rise. The gap between them and other participants (42-56 points) is the BU's protection. Under C2.2 everyone receives the BU, so about a fifth of the shock reaches anyone's money costs. After the shock (years 9-19) the shares are similar under the release row. Under C2.2 they rise to about 30%: the BU absorbs most of the rise only while it is new.

**2. PTF protects its members, but only a little (decision rule 1: met in all six cells).** PTF removes the markup part of the rise in food and utilities. Under the release row in Reference, members pay 56% of the shock; without markup removal they would pay 60%, a difference of 4.2 points. Across the six cells the difference is 2.2-4.8 points, every interval above zero. It is small for three reasons, all by construction:
- the rise is mostly real cost, which PTF pays in dollars like everyone else (reading X5);
- transport, the shock's biggest channel, is outside PTF;
- the BU already absorbs much of the food rise.

PTF members pay a **larger** share than other participants (56% against 44% in Reference, release row). That is true even with no markup removal (60%), so it is not PTF's doing. It comes from who PTF members are and how their BU meets their costs. The pilot's outputs cannot separate the two; the full batch needs a breakdown of costs by payer (S47 list, item 2).

**3. Local sourcing helps only as an upper bound (decision rule 2).** The main reading has local supply half as exposed to the shock. In Reference, release row:
- PTF members' share at a quarter markup falls from 56% with no local supply to 53% with half and 50% with all local supply;
- if local supply were fully sheltered from the shock (labelled optimistic), it falls to 44% with all local supply.
- Across the six cells, all-local supply at half exposure lowers members' share by 3-7 points.

These are upper bounds: the model gives local food no normal-times price premium. A three-year price reserve (pooling) lowers members' share during the shock by 1-3 points and moves the cost later, as designed.

**4. PTH does not protect against this shock on its own (decision rule 3).** PTH removes the rent markup, and an energy shock does not move rents (reading X7).
- **Release row:** PTH members pay more of the shock than other participants (4-21 points more), so the rule is not met.
- **C2.2:** they pay 1.2-1.7 points less, interval above zero in all three environments, so the rule as written is met.

PTH's own cut does not touch utilities, so the C2.2 difference must come through something else. The most likely channel is the BU: with cheaper housing, the BU stretches further across food and utilities. The groups also differ in who they are. Read it as PTH working through the BU, by a small amount, and not as protection from the shock by PTH itself.

**5. No harm to non-participants' basket poverty (decision rule 4: not triggered).**
- The shock raises basket poverty in every cell. With the programme it rises less than without it, for all adults (0.2-0.9 points less during the shock) and for those who chose not to take part. The one exception is Stress under the release row, where the difference for non-participants is -0.08 points with an interval from -0.26 to +0.11, so no difference either way.
- The shock does push some PTF members into basket poverty (0.2-1.2 points during the shock).

**6. An unfavourable result: under the programme, the shock adds to the programme's own inflation, and wealth poverty rises.** This is the pilot's most important finding for the design.
- Without the programme, the shock raises the price level at year 20 by 2.7%. With the programme it raises it by 11-25%: the programme's yearly inflation rises 0.6-1.6 points and compounds.
- The pilot's outputs point to the channel. The output that backs the payouts falls (backed payout 1-8% lower), and the BU, which follows prices, costs more ($1-34 a person-year under the release row, $148-158 under C2.2). So more of each year's payout is new money with nothing behind it.
- As in the backing study (S51), savings lose value. Too little wealth at year 20 rises 0.7-3.0 points more with the programme than without it in five of six cells, for non-participants as much as participants (2.2 points each in Reference, release row). The exception is Reference under C2.2, where it rises 0.3 points less.
- The shock does not change participation: the joining rule does not see prices.
- A shock that the basics absorb once can therefore, through the programme's money, become lasting inflation. The full batch should measure this directly (S47 list, items 3 and 5).

**7. Volatility.** The shock makes costs jump more from year to year in every cell.
- The programme reduces this extra volatility in Reference (both designs) and in Stress under the release row.
- It increases it in Adverse (both designs) and in Stress under C2.2, by 0.1-0.3 points.
- The measure is the percentage change in a group's mean money cost. Participants' money costs are smaller (the BU pays part), so the same dollar change is a larger percentage. The full batch needs a dollar-based reading beside it (S47 list, item 4).

**8. Shock size.** The shares above barely move with the size of the shock (24.6% to 65.5%) or with how much of it stays: the rules are proportional to the rise. The effect on basket poverty grows with size: in Reference, release row, the programme's advantage during the shock is 0.6 points at the smallest shock and 1.3 at the largest (beyond history, labelled so).

## What is by construction and what emerges

**By construction** (they follow from the rules):
- adults outside all three pay 100%;
- the no-programme run passes on 100%;
- a larger markup share lowers PTF members' share;
- PTH's cut does not touch utilities;
- local sourcing lowers members' share in proportion.

**Emergent:**
- the size of the BU's protection;
- PTF members' share relative to others;
- PTH's small effect under C2.2;
- the poverty effects;
- the programme's extra inflation, and the wealth poverty that follows from it;
- the volatility effects;
- participation's lack of response.

## Limits

- 500 adults, 20 years, 50 seeds (a pilot).
- One kind of shock (energy). It is the environment's, so wages follow the general price level, not this rise (reading X1).
- The markup share, local sourcing, the local supply's exposure and pooling are design parameters, swept.
- Local food's normal-times price is not modelled.
- Transport is outside PTF.
- The collective electricity purchasing described in the PTH governance paper is not credited (it buys at market prices).
- The policy comparison stays frozen (ledger d94): no comparator rows face the shock.

## What S47 must carry

1. **Study O as preregistered:** `runner/jobs/shock.js --env=all --procs=4`, 70 rows per environment, seeds 1-500. The pilot ran at about 31.5 seconds per seed per shard on a 4-process Actions runner, so 500 seeds take about 4.4 runner-hours. That fits Actions.
2. **A breakdown of essential costs by payer** (reporting keys only, behind the existing switch; the guard test must stay identical): for each group and window, the BU spent, PTF's cut, PTH's cut and the money paid, by category (food, housing and utilities, transport, medical). This explains why PTF members pay a larger share than other participants (finding 2) and where PTH's small C2.2 effect comes from (finding 4).
3. **A yearly series of the Source's backed and unbacked payout and of the BU's cost**, so the programme's extra inflation under the shock (finding 6) can be split into its parts: less backing output, a costlier BU, and a smaller real economy.
4. **A dollar-based volatility reading** beside the percentage one: the standard deviation of the year-to-year change in a group's mean money cost, over the group's market basket.
5. **For S54 (policy levers), whose own addendum decides:** run its confirmed settings (stage 3) on the main shock path too, especially the levers that protect value (BU indexation rules, inflation-protected savings), since the shock's harm runs through the programme's inflation and savings. Also check S54's joining reading (joining that sees what joining pays) under the shock, since today's joining rule ignores prices.
6. No change to the design or to any released figure follows from this pilot. Any design change Duke makes from it is a ledger decision, a new row and a dated amendment before the freeze.

## For Duke

The pilot gives a plain answer to the question this step asked. In the model, PTF removes the markup part of a price rise and so protects members a little: 2-5 points of the shock. Local sourcing could add a few more. PTH protects only through the BU. Most of the protection comes from the BU itself. Against that, the programme's own money turns part of the one-time jump into lasting inflation, and that raises wealth poverty, for non-participants too. The full study will measure all of this at 500 seeds. If you read the design differently on any of these points (for example, if PTF should hold a price reserve, or PTH should buy energy for its residents), say so and I will add it as a row.
