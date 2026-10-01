# N1 Design: The ESP Surplus Split, in Place of the Pay-Everyone-by-Wage Stand-in

Sep 30, 2026 · Compassionism Simulation · session 25 (dashboard s40) · design only: no code changed · engine v4.22, repo at `dc1ef62`

Read with: `N1-s34-restudy-500.md` (the main rows this changes), `session-25-handoff.md`. Background: `N1-design-esp-payroll.md` (d70–d76), `N1-design-project-hiring.md` (d58–d66).

## Purpose

Session 19 found that the ESP's own premium carries the Hub-spec result. That premium is what an ESP earns converting the BU it keeps: about $15,900 per adult-year at reference. Today it is paid the next year to every adult in proportion to wages, a stand-in with no mechanism behind it (d75, d77). Sending it to the ESP's own workers instead moved the main row by 17–19 points.

Your Sep 30 answer supplies the design. This document turns it into rules the model can run, sources the one constant it needs, sizes it from the current main row, and raises the choices as decisions d97–d106 before any code. Each decision shows the default applied and its alternatives.

## 1. The design, as rules

| # | Rule | Source |
|---|---|---|
| S1 | An ESP converts the BU it keeps as soon as it takes them; it does not hold them for higher rates. | Your input, session 22 |
| S2 | The converted dollars go one-third each to lower prices, reinvestment in capacity and profit-sharing with the ESP's workers, until PTF capacity is reached. | Your answer, Sep 30 |
| S3 | PTF capacity is reached when there are enough ESPs per town or region to serve demand. After that, 60% goes to lower prices and 40% to worker profit-share. | Your answer, Sep 30 |
| S4 | Charters and contracts can adjust the shares by location, for example prime against less desirable locations. | Your answer, Sep 30 |
| E1 | ESPs accept BU as well as cash, check, card and wire. | R7; `N1-design-esp-payroll.md` |
| R2 | Expired BU are directed to projects and convert at the holder's earned rate. | `N1-design-project-hiring.md` |

## 2. What the model can represent

| Rule | In the model | When |
|---|---|---|
| S1 | The ESP converts the share it keeps in the year it accepts it, and the premium is paid out the next year. | Already |
| S2 | The ESP's own premium (today's `bizNet`, which includes the payroll BU returned to the ESP) is split three ways each year (d97). | This step |
| S2, prices | A uniform discount on essentials for the ESP's customers: every adult (d98), in proportion to essentials spending at their own prices, at one price for BU and cash (d99). | This step |
| S2, reinvestment | An ESP capital account that no household receives (d100). The model gives ESPs unlimited capacity from year 0, so the capital buys nothing it can see yet. It decides when capacity is reached. | This step; its effect on output and prices in N2 (s51) |
| S2, profit share | Paid in dollars to every ESP worker (d72's 23.0% of adults) by last year's wage (d104). | This step |
| S3 | Capacity is reached when cumulative reinvestment per adult equals the capital stock of the Hub's PTF industries per adult (d101). | This step |
| S4 | The model has no places, so the shares are swept, not varied by charter (d103). | Swept |
| PTF and private ESPs | The model cannot tell them apart, so one split applies to every ESP (d102). | This step |

**Engine model.** It has no business conversion, so it is unchanged (d70). Its own-spending conversion waits for the later fidelity pass (d78).

## 3. How big is it?

Sizing is arithmetic on existing runs; no mechanics were changed.

**Method.**
- **Configuration:** the Hub-spec main row as `N1-s34-restudy-500.md` ran it. That is project hiring with your d58–d66 picks, the raise off, the damping off, the gift paid as you go and ESP payroll at the defaults; tax-financed, testbed profile, seeds 1–500, three environments.
- **Record:** a scratch copy of `harness.js` records every agent-year, with the repo untouched. Recomputing each agent-year's poverty gap from the record reproduces the run exactly (no mismatch in 5,000,000 agent-years per environment).
- **One pass.** Each variant re-routes the ESP's own premium year by year, and carries three effects forward:
  - the BU a price cut frees, which expire and go to project hiring the next year (share 1, capacity × quality among willing participants, at the rate project hiring uses, under the conversion tax, CIP bonus and the agent's income shock);
  - the ESP's smaller intake, which shrinks next year's own premium and payroll premium in proportion to the BU no longer accepted;
  - the cost. The **tax reading** moves the flat contribution by the change in cost (capped at 90%). The **hybrid reading** leaves conversion untaxed, so only the BU relief saved moves it.
- **Not included:** labor responses (the payout's raise, the price cuts' income effect, the profit share's raise), the contribution's one-year lag, and any need left unfinanced when the contribution is at its cap.
- **Check.** The method puts the worker-cooperative row at +14.84 / +15.48 / +1.87 against the restudied +19.37 / +17.14 / +2.66 (reference / Adverse / Stress). It captures 70–90% of a full restudy's effect.

Reproduce: `session-25-sizing.zip`, not in the repo. It holds the patch that makes the recording copy, the script and its output. The build session reproduces the split's flows from ledger rows (Section 8); the poverty figures come from the restudy.

**Today's flow** (Hub-spec main row, years 1–19, year-0 dollars)

| Quantity | Reference | Adverse | Stress |
|---|---|---|---|
| ESP's own premium, per adult-year | $15,894 | $13,129 | $4,877 |
| BU accepted by ESPs, per adult-year | $11,207 | $9,353 | $3,592 |
| Share of the premium paid to non-participants | 22.5% | 22.7% | 60.7% |
| PTF members, year 0 → year 19 | 18% → 52% | 18% → 53% | 8% → 43% |

**The capacity trigger (d101).** BEA, Fixed Assets Table 3.1ESI, current-cost net stock of private fixed assets by industry, yearend 2025 (millions of dollars; file created Sep 28, 2026):

| Industry (table line) | Net stock, 2025 |
|---|---|
| Food and beverage stores (45) | $383,164 |
| Food services and drinking places (95) | $454,294 |
| Utilities (9) | $4,250,891 |
| **The Hub's PTF industries** | **$5,088,349** |
| Per adult: ÷ 269,763,509 (Census, age 18+, July 1, 2025) | **$18,862** |
| Adding health care (lines 86–88: $675,592 + $1,632,752 + $186,972) | $28,113 per adult |

Real estate (line 74, $37.8 trillion, mostly housing) is left out: housing is PTH's domain, and the Hub names grocers, counter-serve restaurants and utility providers as PTF businesses.

Phase 1 reinvests about $5,300 per adult a year at reference and somewhat less in Adverse. Capacity is reached at the end of year 4 and the 60/40 split starts in year 5, in every seed at reference and in nearly every seed in Adverse (range 5–6). In Stress it starts in year 12 on average (range 11–15).

**The split at the defaults, and the choices around it.** Change in 20-year average FGT₂ against today's stand-in on the same row, before labor responses; tax reading unless stated. Every 95% interval lies within ±0.09.

| Variant | Reference | Adverse | Stress |
|---|---|---|---|
| **Default** (d97–d104) | **+1.16** | **+3.02** | **+0.20** |
| Default, hybrid reading | −0.03 | +2.95 | +0.20 |
| Capacity: health care included ($28,113) | +2.07 | +3.92 | +1.02 |
| Capacity: half the stock ($9,431) | +0.32 | +2.17 | −0.34 |
| Capacity from year 1 (60/40 throughout) | +0.13 | +1.91 | −0.79 |
| Capacity in year 10 | +3.47 | +5.14 | −0.04 |
| Capacity in year 15 | +5.54 | +6.93 | +0.53 |
| Capacity never reached (thirds throughout) | +6.88 | +8.62 | +1.25 |
| Customers: participants and PTF members (d98) | +2.92 | +3.84 | +0.78 |
| Customers: PTF members only | +2.67 | +1.50 | +0.91 |
| Customers: participants only | +4.13 | +4.17 | +1.15 |
| Cuts on cash purchases only (d99) | +1.97 | +2.53 | +0.06 |
| Reinvestment's third spent as price cuts (d100) | +0.03 | +1.77 | −0.92 |
| Phase-2 worker share 20% (d103) | +0.27 | −0.23 | −0.11 |
| Phase-2 worker share 60% (d103) | +4.72 | +6.59 | +0.56 |
| Worker cooperative (d75's row; the check above) | +14.84 | +15.48 | +1.87 |

**Each part alone**, with the rest of the premium paid as today:

| Part | Reference | Adverse | Stress |
|---|---|---|---|
| A third to price cuts | −1.68 | −1.50 | −0.69 |
| A third to profit share | +2.83 | +3.23 | +0.30 |
| A third to reinvestment | +4.50 | +5.45 | +1.60 |
| 60% to price cuts | −2.34 | −2.50 | −1.21 |
| 40% to profit share | +3.66 | +4.13 | +0.40 |

**Where the money goes at the defaults** (year-0 dollars; per adult-year over the run unless stated)

| Quantity | Reference | Adverse | Stress |
|---|---|---|---|
| Price cut on essentials, phase 1 / phase 2 | 25.8% / 40.2% | 24.7% / 36.9% | 8.4% / 12.7% |
| BU freed by the cuts | $1,394 | $120 | $0 |
| Project income from freed BU | $6,720 | $582 | $0 |
| Change in cost | +$2,555 | +$215 | $0 |
| Change in the contribution, 20-year mean | +1.4 pt | −0.1 pt | 0.0 pt |
| Reinvestment | $1,113 | $1,065 | $1,033 |
| Profit share per ESP worker-year | $23,107 | $21,412 | $7,516 |
| Share of the premium reaching non-participants (today) | 15.4% (22.5%) | 20.9% (22.7%) | 60.1% (60.7%) |

**Groups** (default, tax reading; change in real resources per adult-year against today's stand-in; participants / non-participants / bottom third / top third by year-0 wage):
- Reference: +$2,168 / −$4,048 / +$5,609 / −$5,614.
- Adverse: −$524 / −$1,682 / +$3,046 / −$5,553.
- Stress: −$910 / −$1,030 / +$486 / −$2,780.

## 4. What the sizing says

1. **The split makes the Hub-spec row worse than today's stand-in in every environment, before labor responses:** +1.16 at reference, +3.02 in Adverse and +0.20 in Stress. The levels against no program would be about +5.3, +2.7 and −0.3, from +4.14, −0.34 and −0.54.
2. **The reason is that the stand-in was the generous assumption.** It hands the ESP's whole premium back to every adult in proportion to wages. Your split keeps the premium inside the ESP: its customers, its capital and its workers. Of those, only the price cuts reach the general population.
3. **Price cuts do better than today's payout in every environment.** A third to price cuts lowers FGT₂ by 1.68, 1.50 and 0.69 against paying that third by wage. Essentials spending is spread more evenly than wages, so the cuts reach the bottom third (about +$2,800 a year at reference for that third alone). This is the part of the split the model represents in full.
4. **Reinvestment costs most: +4.50, +5.45 and +1.60 for its third.** It reaches no household. The model already gives ESPs unlimited capacity from year 0 at no cost, so the cost of building capacity shows and its benefit does not. This is the main reason the row worsens, and it lasts until N2 or s44 gives capacity a role.
5. **The profit share concentrates the premium as the cooperative row did**, at +2.83, +3.23 and +0.30 for its third. ESP workers are 23% of adults with average wages, and each receives about $23,100 a year at reference.
6. **When capacity is reached moves the row most:** from +0.13 (year 1) to +6.88 (never) at reference, and from +1.91 to +8.62 in Adverse. The sourced trigger lands in year 5 at reference and in Adverse, close to the favourable end.
7. **Price cuts free BU into project hiring.** BU cover about two-thirds of a participant's essentials, and all of a PTH member's. At reference the 60% price share brings cuts of about 40%, more than many participants pay in cash, so the rest of the cut lowers the BU they need.
   - The BU freed, $1,394 per adult-year over the run, expire and go to project hiring. They convert there at about 4.8× into $6,720 of project income, paid by capacity × quality, so to high-octave, high-quality participants rather than to the poorest.
   - Cost rises $2,555 per adult-year, and the contribution 1.4 points.
   - In Adverse and Stress the BU erode under inflation, cash outlays are larger, and almost nothing is freed ($120 and $0).
   - This loop is why phase 2 does better than phase 1 at reference, and why the hybrid reading is better there (−0.03).
8. **Who gains.** At reference participants and the bottom third gain on average (+$2,168 and +$5,609 a year); non-participants and the top third lose. The share of the premium reaching non-participants falls from 22.5% to 15.4%. FGT₂ rises even though the bottom third gains on average. The sizing does not show which adults carry the deepest gaps; the restudy's FGT₂ by group will.
9. **The customer set is chosen for consistency, not for the result.** Every adult does better than participants and PTF members, or participants alone, in every environment. PTF members only does better in Adverse (+1.50), because cuts of 77–92% free BU into project hiring there too; it does worse at reference and in Stress. The default follows d72 (Section 6).

**Expectation, stated before the restudy.** Adding the labor responses, the main row worsens against today's stand-in by about 1–2 points at reference, 3–4 in Adverse and less than half a point in Stress. Losing today's payout removes a raise from every wage earner, and price cuts carry an income effect; the profit share raises ESP workers' hours. Session 18's expectation for ESP payroll was wrong by 2.7 points, so the restudy decides.

## 5. The mechanism (defaults applied)

Behind a new harness switch `SURP` (null = off, so every run is bit-identical to today), in the Hub-spec model only. It works with ESP payroll on or off. Each year:

1. **Pool.** Last year's ESP premium, `FWS.prev.bizNet` (the BU the ESP kept, plus payroll BU returned to it, converted at the flat 3× under the progressive tax, less face value; d97). The ESP converts in the year it accepts the BU (S1) and the split is paid the next year, as today.
2. **Shares.** Phase 1: one-third each to price cuts, reinvestment and profit share. Phase 2: 60% price cuts, 40% profit share. Phase 2 starts the year after cumulative reinvestment, in year-0 dollars per adult, reaches K = $18,862 (d101).
3. **Price cuts (d98, d99).**
   - Before the agent loop, a pass with no random numbers sums each customer's essentials at own prices: basket × essentials share × the PTF and PTH factors.
   - The cut δ is the price pool ÷ that sum, capped at 1; any pool the cap leaves is added to next year's price pool.
   - Each customer's essentials cost falls by δ. A participant's BU buy the discounted essentials first: BU spent = min(12 × BU, essentials × (1 − δ)). BU no longer needed expire and go to the project pool, as every expired BU does. Non-participants' cash cost falls by δ × their essentials.
4. **Profit share (d104).** Paid in dollars to every ESP worker by last year's wage, as d75's cooperative alternative pays today. It is earned, so it enters the wage elasticity as a raise (1 + share ÷ last year's wage) with no income effect.
5. **Reinvestment (d100).** Added to the ESP capital account. No household receives it.
6. **Labor.** Price cuts are unconditional in-kind dollars, so they carry one income effect, as the PTF, PTH and grocery cuts do (the testbed's `inkindRho`). Today's payout by wage loses its raise treatment, since it no longer exists.
7. **Accounting and financing (d105).** Price cuts used, profit share and reinvestment are parts of the ESP's conversion premium. The testbed counts them as conversion: financed by the flat contribution under tax financing, and created money at additionality *a* under money and hybrid financing. BU relief falls by itself as cuts free BU, and the freed BU's project conversion counts like all project conversion.
8. **Unchanged.** The PTF discount (12% of the basket for PTF members) and the PTH cut (35%) stay as they are (Section 7).

**Random numbers.** No step draws one, so the eight-draws-per-agent-year guarantee (CRN) holds.

## 6. Decisions (defaults applied; override any)

| ID | Question | Default applied | Alternatives | Why |
|---|---|---|---|---|
| d97 | What is split | The ESP's own premium: the dollars from converting the BU it keeps, less their face value | Every converted dollar, face value included | Face value pays for the goods the ESP sold, as a cash sale would; splitting it too would leave the ESP short of what it sold. The premium is the flow today's stand-in pays out. |
| d98 | Who gets the price cuts | Every adult, in proportion to essentials spending at their own prices | Participants and PTF members (+2.92 / +3.84 / +0.78); PTF members only (cuts of 77–95%; better in Adverse, +1.50); participants only (+4.13 / +4.17 / +1.15) | d72 counts every job in grocers, food services, utilities, real estate and health care as an ESP job, so ESP sales are the essentials sector's sales, and every adult buys from it. The result does not decide it (Section 4, item 9). |
| d99 | Price cuts and BU | One price for BU and cash; BU a cut frees expire and go to project hiring | Cuts on cash purchases only (+1.97 / +2.53 / +0.06; no freed BU, cuts near 100% of cash essentials at reference) | An ESP posts one price, and expired BU go to projects under the rules as written (R2, d58–d66). The loop through project hiring is a consequence of the design, reported (Section 4, item 7). |
| d100 | What reinvestment buys | An ESP capital account that no household receives; it decides when capacity is reached (d101). Its effect on output and prices is designed in N2 (s51), next in the round, which takes the account as an input; s44 keeps the PTF and PTH operating costs | Spend it as price cuts until capacity is modeled (+0.03 / +1.77 / −0.92; assumes a full return in the same year, unsourced); wait for s44 as planned (fifth in the round) | d96: effects come from modeled mechanisms, not assumed ones. Added capacity is added output, which is what N2 computes, so the account belongs there. |
| d101 | When PTF capacity is reached | When cumulative reinvestment per adult (year-0 dollars) reaches $18,862, the 2025 net capital stock of the Hub's PTF industries per adult. Phase 2 starts in year 5 at reference and in Adverse, year 12 on average in Stress | Health care included ($28,113: years 7, 7–8, 16–19 or never); a PTF membership threshold; a fixed year (swept 1, 10, 15); never | It is the first rule that gives reinvestment an effect the model can see, and it is sourced (BEA, Census). A capacity able to serve all demand needs at least the capital the existing providers use. **It moves results most**: your estimate of how long building PTF capacity takes would check it. |
| d102 | Private ESPs | The same split for every ESP | Private ESPs pay the profit share of their sales to owners, by wealth (a restudy sensitivity; not sized) | Your answer covers PTFs; the model cannot tell PTFs from private ESPs. |
| d103 | Location and charters | Shares swept, not varied by place: phase-2 worker share 20% and 60%, and reinvestment's third to prices | Vary shares by a stand-in for location (none exists) | The model has no places. The 20% row does better than today in Adverse and Stress (−0.23, −0.11). |
| d104 | Who receives the profit share, and how it counts | Every ESP worker, participant or not, by last year's wage; a return to work (raise, no income effect) | Participating ESP workers only | It is paid in dollars, so it needs no earned rate. The fairness rule gives every change in the return to work one wage elasticity. |
| d105 | How the testbed counts the split | As conversion: taxed under tax financing, created at *a* under money and hybrid. The PTF discount (12%) is unchanged | Count the price cuts as price-cut dollars (taxed under hybrid as well) | All three parts come out of the ESP's conversion premium, so they are conversion rewards. Whether the price share replaces the PTF discount is s44's question. |
| d106 | When it reaches the page | At the development-milestone release (d95), the Hub-spec main row uses the split, and today's stand-in stays one switch away as a sensitivity row. The page changes only after you see the restudy | Add the split as its own row and leave the main row on the stand-in | As d65 and d76 did: the design's mechanism replaces the stand-in, in one reviewed change. |

## 7. Raised here, decided later

- **The BU allowance as prices fall.** Price cuts make the nominal BU allowance buy more; under the rules the excess becomes project money, converted at about 4.8×. Whether the allowance should follow essentials prices down is a financing question for s45. Your stated aim (stabilize basic living costs, then deflation) bears on it.
- **Two PTF price cuts.** The model's PTF discount, 12% of the basket for PTF members, is financed as a price-cut transfer with no mechanism. The price share is a funded price cut for every adult. s44 decides whether the price share replaces the 12%.
- **The capital requirement's scope.** K counts the whole existing stock of the three industries. PTFs that buy or convert existing businesses rather than build would need a different figure; that, and the capital's return, are N2's and s44's questions.
- **Project hiring's allocation.** Freed BU reach participants by capacity × quality, and octave advancement saturates (i9), so they go mostly by quality, not to the poorest.
- **Inflation.** Under hybrid financing at *a* = 0, the freed BU's project conversion adds created money at reference. The restudy reports the price path.

## 8. Build and restudy plan (next session)

**Code.** `SURP` in `harness.js`, Hub-spec model only, null by default. Switches:
- **`p1`:** [1/3, 1/3, 1/3] (prices, reinvestment, profit share); **`p2`:** [0.6, 0, 0.4].
- **`K`:** 18862 (year-0 dollars per adult); `Infinity` for never; a number of years via **`swYear`** for the fixed-year rows.
- **`cust`:** `'all'`; alternatives `'pp'` (participants and PTF members), `'ptf'`, `'part'`.
- **`bu`:** `'one'`; alternative `'cash'`.
- **`rv`:** `'capital'`; alternative `'price'`.
- **`priv`:** `'same'`; alternative `'owners'` (the profit share of non-PTF sales to adults by positive wealth; the PTF share of sales is PTF members' share of customers' essentials).
- **`wk`:** `'esp'`; alternative `'espPart'`.

Ledger rows: the pool; price cuts used, as cash savings and as BU freed; carried excess; profit share; reinvestment; the capital account; δ and the phase each year; the switch year.

The testbed's `esp` section gains the split's rows, and `n1Row` takes a `surp` option, so `projcore`, `esp` and `match` print the split on the Hub-spec main row when the build makes it the default.

**Unit tests**
1. `SURP` null is bit-identical to `dc1ef62` (full-output diffs of `projcore`, `esp`, `match`, `a5`; and a unit check).
2. Shares [0, 0, 1] in both phases reproduce ESP's `rest: 'esp'` exactly on every testbed measure.
3. Conservation each year: pool = price cuts used + profit share + reinvestment + carried excess.
4. Each customer's cut = δ × their essentials; for a participant, cash saving + BU freed = the cut, and the project pool rises by exactly the BU freed.
5. δ ≤ 1, no essentials cost below zero, and non-customers get no cut (`cust: 'pp'`).
6. Phase 2 starts the year after the capital account reaches K; K = Infinity keeps phase 1 for 20 years; K = 0 gives phase 2 from year 1.
7. Eight RNG draws per agent-year; the engine model is unaffected when `SURP` is set.
8. Financing: under tax the pool is in the year's need; under hybrid it is not, and it enters the price module at (1 − *a*).
9. Ledger rows add up, and the profit share's labor raise appears only for ESP workers.

**Restudy.** CRN-paired, 500 seeds, reference, Adverse and Stress, Hub-spec model, tax-financed at each row's own cost, with hybrid (*a* = 0 and 1). Rows:
- Today's Hub-spec main row (the s34 main row, stand-in) and the split at the defaults.
- Sensitivities: K with health care and at half; capacity in year 1, 10 and never; customers `'pp'`, `'ptf'` and `'part'`; cuts on cash only; reinvestment as price cuts; phase-2 worker share 20% and 60%; owners' share; participating ESP workers only; each third alone.
- The page's other rows with the split (d88): the gift over the run, and the shaded row.

Reported: poverty (20-year average and year-20 FGT₂, FGT₀, basket and wealth poverty, FGT₂ and BLEI by group); money (cost, change per $1,000, the contribution, the price path); work (hours); the split's flows (δ by phase, BU freed, project income, profit share per ESP worker-year, reinvestment, capital at year 20, switch year, share reaching non-participants). Run `validate`, `unit` and `domtest`; the repo files go as one `apply-session-NN.zip` (d69).

## 9. Standing guardrails that apply

- Every change sits behind a switch, with the old behaviour kept.
- Before/after comparisons are CRN-paired at 500 seeds.
- `validate`, `unit` and `domtest` run on every change.
- No constant is retuned to hit a target. K is derived from primary sources (BEA, Census) and swept; the shares are yours and swept.
- Every design is tested in the Adverse Environment and the Stress Test, and every gain is confirmed on basket and wealth poverty.
- Fairness rule: one income effect per unconditional dollar (price cuts), one wage elasticity for every change in the return to work (profit share).
- Model limits are reported, not hidden: no places, no firms, no capacity limit, and reinvestment with no visible return until N2.

**Sources, verified in-session on Sep 30**
- **BEA, Fixed Assets Accounts, Table 3.1ESI**, Current-Cost Net Stock of Private Fixed Assets by Industry, yearend, millions of dollars (`Section3All_xls.xlsx`, sheet `FAAt301ESI-A`, file created Sep 28, 2026), 2025 values.
- **Census Bureau, Vintage 2025, SCPRC-EST2025-18+POP**, resident population age 18 and older, July 1, 2025: 269,763,509 (read from a state data center's copy of the Census file).
