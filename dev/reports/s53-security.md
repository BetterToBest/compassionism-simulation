# Security beyond wealth: income shocks, months of cover, hours, moves and exposure (pilot)

Nov 2, 2026 · research-update plan step S53 · study P · Claude

**PILOT.** Seeds 1-50 on GitHub Actions. These numbers decide only what the full study (seeds 1-500, after the design freeze) must contain. They are not figures of the model and should not be quoted as findings.

- Preregistration: research-update `prereg/2026-11-security-addendum.md` (written before any run), with its Amendment 1 (Nov 2, after this pilot: table presentation and two descriptive measures for the full study).
- What each measure counts, and which are true by construction: `dev/reports/s53-security-reading.md`.
- Every table: `dev/reports/s53-security-tables.md`, written by `dev/tools/s53_security.py` (paired bootstrap over seeds, 2,000 replicates, resampler seed 53).
- Per-seed results: compassionism-sim-results `s53-security-f15eaf6/` (engine f15eaf6; run.txt; SHA256SUMS, all 20 files verified Nov 2). Both consumer scripts load it: `s53_security.py --check` (30 rows, 229 keys, 50 seeds) and `s19_series.py` (the yearly poverty series add up to the run's person-year figures to 1e-14).

## The question

The model already reports poverty and wealth. This study asks about security as people live it. Compared with no programme, on the same simulated adults:
- Are big falls in income that savings cannot cover rarer? (primary)
- Could more households cover the basics for three months without wages? (primary)
- How many hours of work do the basics cost, how often are people pushed out by price, and how much of the budget is exposed to market prices for essentials? (mostly the design's accounting)
- Do the answers hold under the outside supply shock (S52), and how much of the savings result is savings losing value to inflation?

Two designs: **the release row** as released, and **the C2.2 design** (the BU indexed to the price of food, housing and medical care, distributed to everyone automatically). Three environments: Reference, Adverse, Stress. Three groups: all adults; the adults who take part; the adults who choose not to. The two groups are fixed at the start from each adult's drawn willingness to join, so they are the same people in every design and in the no-programme run. Under C2.2 everyone receives the BU automatically, so there the two groups differ little; under the release row some of those who chose not to still belong to PTF or PTH, which are drawn separately.

The release row and C2.2 rows measure need against different cost-of-living lines (C2.2 uses the CPS yardstick), so their no-programme levels differ; each design is compared only with its own no-programme run.

## What the pilot shows

Every cell named below has a 95% interval that excludes zero unless it says otherwise.

### 1. Big income falls with no buffer: fewer for participants under both designs; more for those outside the release row

A "big fall with no buffer" is a year in which a household's resources (money plus the help it gets in kind) fall 25% or more and its liquid savings cannot cover the fall. Without the programme it happens about 1 to 2 times per 100 adult-years.

| Change per 100 adult-years (no outside shock) | All adults | Took part | Chose not to |
|---|---|---|---|
| Release row, Reference (no programme: 0.99) | -0.17 | -0.31 | **+0.35** |
| Release row, Adverse (2.04) | -0.75 | -1.05 | **+0.28** |
| Release row, Stress (2.04) | **+0.25** | -0.60 | **+0.82** |
| C2.2, Reference (0.89) | **+0.11** | **+0.10** | **+0.16** |
| C2.2, Adverse (1.79) | -0.49 | -0.51 | -0.42 |
| C2.2, Stress (1.79) | -0.63 | -0.65 | -0.62 |

Bold: worse with the programme.

- **Falls of any size become much rarer** under both designs, for every group, in every environment (0.7 to 3.1 fewer per 100 adult-years). The BU does not stop when wages do, so resources hold up. That is the mechanism working.
- **Under the release row, the adults who chose not to take part have more uncovered falls** in all three environments. They get almost none of the BU's cushion, and their savings lose value to the programme's inflation (section 3 shows this is the channel). This is harm to non-participants on this measure (decision rule 2).
- **Under C2.2 in Reference**, uncovered falls rise slightly (+0.10 to +0.16) even though falls of any size halve. The falls that remain are mostly falls in conversion pay (section 4), which are large in dollars against liquid savings. A fall in conversion pay does not touch the basics, which the BU still covers; the measure cannot see that (see Limits and Amendment 1). In Adverse and Stress, C2.2 makes uncovered falls rarer for every group.

### 2. Months of the basics covered without wages: much better under C2.2; worse under the release row except for those with almost nothing

"Under 3 months" is the share of adult-years in which liquid savings would cover less than three months of the basics if wages stopped (conversion pay left out, the cautious reading).

| Change in % of adult-years under 3 months (no shock) | All adults | Took part | Chose not to |
|---|---|---|---|
| Release row, Reference (no programme: 37.0%) | **+6.9** | **+2.1** | **+23.7** |
| Release row, Adverse (43.1%) | **+14.3** | **+10.5** | **+27.7** |
| Release row, Stress (43.1%) | **+16.7** | **+6.4** | **+23.5** |
| C2.2, Reference (26.2%) | -21.0 | -21.1 | -20.6 |
| C2.2, Adverse (31.3%) | -24.0 | -24.1 | -23.6 |
| C2.2, Stress (31.3%) | -20.7 | -20.8 | -20.6 |

- **C2.2** almost removes the problem as measured: under 3 months falls from about a quarter or a third of adult-years to 5-11%, for participants and non-participants alike, and the median months covered rises by 1 to 5 months. **But this comes from lower need, not from larger savings.** Prices rise strongly under C2.2 too (the price level at year 20 is about 440 times its start in Reference, roughly 36% a year), and the median adult's savings in real terms fall by about two thirds (Reference: $403,000 to $133,000; Adverse $205,000 to $68,000; recorded beside the measures, not a preregistered outcome). C2.2's BU is indexed to the price of food, housing and medical care and covers nearly all of them, so what is left to cover without wages is small, and a small balance covers many months. That part is by construction. Whether C2.2's households could also weather a loss the BU does not cover is not tested by this study; Amendment 1 adds C2.2 rows with savings that keep up with prices to the full study, so the inflation share can be measured for C2.2 as it is here for the release row.
- **The release row** cuts the share with **under one month** for participants (by 1.8-9.5 points), because the BU lowers what a month of the basics costs them. But more households fall **under three months**, the median months covered falls (by 3-4 months overall: participants 2-3, non-participants 4-6), and non-participants are much worse off on every savings measure (under 1 month +10 to +18 points). Again the channel is inflation (section 3).

### 3. How much of the savings result is inflation's (decision rule 3): nearly all of the unfavourable part

The release row was run a second time with savings that keep up with prices (S51's sensitivity). Every unfavourable savings result turns favourable:

| Release row, Reference | Plain savings | Savings that keep up with prices | Difference |
|---|---|---|---|
| Under 3 months, all adults | +6.9 | -19.7 | -26.6 (-27.3, -25.9) |
| Under 3 months, chose not to | +23.7 | -10.1 | -33.8 (-34.8, -32.8) |
| Uncovered big falls, chose not to | +0.35 | -0.36 | -0.71 (-0.76, -0.65) |
| Displaced by price, chose not to | +1.21 | -0.31 | -1.52 (-1.61, -1.43) |
| Wealth poverty at year 20, chose not to | +27.2 | -9.7 | -36.9 (-38.2, -35.6) |

Adverse and Stress show the same (tables, "Difference in differences"). Under the release row the price level at year 20 is about 2,600 times its start in Reference (roughly 48% a year; S51 traced this to conversion pay that almost no output backs), and savings that do not keep up lose their value; that, not the BU itself, is what makes households less able to ride out a loss of wages. The difference in basket poverty is under 0.1 point: protecting savings changes the buffer, not who can afford the basics this year.

This is the same finding as S51 and S52, now on security measures: under the release row the programme's inflation is the main source of harm, and it falls hardest on the adults who chose not to take part.

### 4. Money income against resources (decision rule 4): the two readings disagree, and the reason differs by design

On money income alone (leaving out the help in kind), uncovered 25% falls are **more** frequent with the programme in every cell: +1.0 to +1.5 per 100 adult-years under both designs, for every group. On resources the release row makes them rarer for participants. So both readings are given here.

The BU replaces the part of income that pays for the essentials (food, housing and utilities, medical care, and transport where it covers it), and pays it in kind. Money income still pays for everything else, and the BU does not cushion a fall in it.

Why money-income falls are less often covered, from a 10-seed exploratory check on the session machine (not preregistered, not a result; a scratch copy of the engine with extra counters, Reference and Stress):
- **Release row:** money-income falls of 25% or more happen about as often as without the programme (2.29 against 2.28 per 100 adult-years for participants in Reference). What changes is the buffer: savings lose value to inflation. With savings that keep up with prices, uncovered money-income falls are fewer than with no programme (section 3 tables: -0.25 in Reference).
- **C2.2:** falls driven by wages become rarer (1.04 against 1.73), but falls in conversion pay appear (0.94; zero without the programme), because conversion pay moves from year to year. These are large in dollars against liquid savings.

Amendment 1 adds the counts behind this check to the full study, so it is measured on 500 seeds rather than inferred.

### 5. Hours, exposure and PTH moves: the design's accounting (by construction)

These follow from the design as written and are not evidence that it works.
- **Hours a week the basics cost** at the adult's usual wage: without the programme, a median of 41 (release row's line) or 27 (CPS line) in Reference, and 50 and 34 in Adverse. The programme cuts this by 17-22 hours (Reference, Adverse) and 9-21 hours (Stress). Under C2.2, counting conversion pay, the median adult needs no hours at all in Reference and Adverse (2 in Stress).
- **Essentials paid in money at market prices:** 100% of essentials without the programme (by definition). Under C2.2 about 2% remain; under the release row 19-22% for participants and 54-56% for non-participants (Reference, Adverse), more in Stress. **One exception to note:** in Stress, under the release row, non-participants' essentials take a larger share of their whole budget (+9.7 points), because the programme's inflation raises the market prices they pay.
- **PTH tenancies ended:** 4.4-4.5 per 100 member-years with the programme. No rule in the model ends a tenancy against the member's will; these are the drawn ordinary moves (6.2% a year with the PTH books on). Forced PTH moves are zero by construction.

### 6. Displacement by price (a proxy): worse under the release row, better under C2.2

Adults outside PTH who could pay their costs last year and cannot this year (the engine's housing-distress test; the model has no moving decision).
- **Release row:** more displacement, for every group, in every environment: +0.3 to +1.4 per 100 adult-years overall, +1.2 to +2.0 for non-participants (no programme: 1.1 to 1.5). With savings that keep up with prices it turns favourable (-0.3 to -0.7 overall), so the channel is again inflation.
- **C2.2:** displacement falls by 0.6-0.9 per 100 adult-years, for every group, in every environment.

### 7. Under the outside supply shock (S52): the answers hold

Every result above points the same way under S52's main supply shock (one borderline cell, uncovered 50% falls for non-participants under the release row in Adverse, loses its interval). The shock moves the programme's effect on the security measures by less than one point (under 3 months +0.3 to +0.7 points worse under the release row; uncovered falls by under 0.05). As S52 found, the shock adds to wealth poverty with the programme in five of six cells (+0.7 to +3.0 points against the change without the shock; C2.2 in Reference -0.3) and lowers basket poverty slightly (0.1-0.7 points).

### 8. Beside them (guardrail 6)

Basket poverty falls under both designs everywhere (release row 13-36 points; C2.2 26-37 points). Wealth poverty at year 20 rises under the release row (+11 to +37 points; non-participants +27 to +45) and falls under C2.2 (-8 to -24 points). Median real savings fall under both designs (section 2). Every security finding above should be read beside these.

## What is by construction and what emerges

- **Emergent:** income falls and whether savings cover them; displacement by price (a proxy).
- **Mixed:** months covered (need is lowered by construction; savings are emergent). Under C2.2 the lower need dominates; under the release row the savings erosion does.
- **By construction, given prices and wages:** hours, exposure, PTH moves. A lower own cost means fewer hours and less exposure; the size of the change follows from the BU amount and the price cuts. The price level that enters them is emergent, which is why Stress shows non-participants more exposed.

## Limits

- 500 adults, 20 years, 50 seeds (a pilot).
- The model has no moving decision, no rent arrears process and no eviction court; displacement is a proxy.
- Liquid savings are a fixed 20% of savings, not a separate account.
- A big fall in resources counts the same whether or not the household can still pay for the basics. Under C2.2 most remaining falls are falls in conversion pay while the BU still covers the essentials; Amendment 1 adds a reading that counts only falls that leave the household below its own cost of living.
- The hours measure uses the adult's usual wage; in a recession year the wage on offer may be lower.
- The money-income explanation in section 4 rests on a 10-seed exploratory check, not on the preregistered outputs.
- The policy comparison stays frozen (ledger d94): no comparator rows were run.

## What S47 must carry

1. **Study P as preregistered:** `runner/jobs/security.js --env=all --procs=4`, 10 rows per environment, seeds 1-500. The pilot ran at about 5 seconds per seed per shard on a 4-process Actions runner (17-21 seconds per seed per process), so 500 seeds take about 0.7 runner-hours. That fits Actions.
2. **The security measures and the S19 series on every batch job that S54 or S19 reads** (already in S47's list): study option `sec: true`, `SEC_KEYS`, and `S19_KEYS` to the run's horizon, at least on the release panel, study O and study N. Dry-run check: `python3 dev/tools/s53_security.py FOLDER --check` and `python3 dev/tools/s19_series.py FOLDER`.
3. **Two more rows per environment (Amendment 1):** C2.2 and its no-programme run with savings that keep up with prices (`c22.off.none.sv`, `c22.off.prog.sv`), so study P has 12 rows per environment (`runner/jobs/security.js`, `PREREG_ROWS` 12; about 0.85 runner-hours at 500 seeds).
4. **Two descriptive measures (Amendment 1)**, reporting keys only under the same study option (the guard test must stay identical; an engine change before the dry run):
   - any 25% fall in money income, and its main cause (wages, conversion pay, or other: taxes and transfers), per group, so decision rule 4's channel is measured;
   - uncovered 25% falls in resources that leave the adult below their own cost of living that year, so a fall that leaves the basics covered is told apart from one that does not.
5. **For S54 (policy levers), whose own addendum decides:** report the primary security measures (`secU25`, `secM3`) for every lever row on both savings readings, since section 3 shows the savings reading decides their sign under the release row; and include them in stage 3's no-harm test for non-participants beside basket and wealth poverty.
6. No change to the design or to any released figure follows from this pilot. Any design change Duke makes from it is a ledger decision, a new row and a dated amendment before the freeze.

## For Duke

The pilot gives a two-sided answer. The BU does what it is meant to: income falls become much rarer, the basics cost far fewer hours of work, and far less of the budget is exposed to market prices. Under the C2.2 design this carries through to security as a household lives it: more months of cover, fewer people pushed out by price, for participants and non-participants alike. One caution: C2.2 also has strong inflation, and real savings fall under it too; its households are secure mainly because the BU covers nearly all of the basics, so they need little savings to fall back on. Under the release row as released it does not: the programme's inflation eats savings, so more households would run out within three months if wages stopped, more are pushed out by price, and the adults who chose not to take part are less secure than with no programme on almost every savings measure. Protecting savings from inflation reverses all of this, which is why S54's value-protecting levers matter. If "security" in your writing means something these measures miss, say so and I will add it.
