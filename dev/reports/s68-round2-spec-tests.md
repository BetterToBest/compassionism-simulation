# Round 2 written down and tested together (S68, part 2)

Plain-words report, Nov 14, 2026. Part 1 (`dev/reports/s68-financing-identity.md`) built the check of who pays the programme. This part does what the step was added for (the Nov 9 audit, findings 3, 4 and 7): it writes every round-2 mechanism down as rules a programmer could follow without the code, tests the round-2 switches switched on together, and builds the packet for a second, independent implementation (step S69). Nothing here is a result about the programme: these are checks of the model.

## In short
- **The candidate main row** now exists as one setting (`harness.js` `r2MainRow`): every round-2 switch at the reading its own report recommends to the design freeze (S63), on the frozen engine, under the C2.2 design. It is Claude's recommendation; S63 decides.
- **Written down.** MODEL_SPEC.md section 14 states each round-2 rule (open PTF access and its growth, PTF running costs, the capacity price rule with its closed form and options, adults outside the labour force, the borrowing limit, wealth by asset class, the creditor side, the top tail, bargaining, the new financing parts, the reporting options), where in the year it acts, its random stream and what refuses what. TESTBED_SPEC.md section 7 gives every row option a plain name, its value when absent, its value in the candidate main row and where it is described. ODD.md section 8 summarises round 2 in the protocol's terms.
- **Tested together.** Each round-2 switch was given one other reading, and each alone and every pair (121 rows) was run on the candidate main row and its no-programme run, at 5 seeds, in the Reference, Adverse and Stress environments. RESULTS_LINE
- **Three defects found and fixed, one limit found.**
  1. *Adults outside the labour force who do not convert* (`lf {conv: 'none'}`) gave non-numbers (NaN) in wealth and 70-odd outputs under a programme: those adults never had a project rate, and zero times an unset rate is not a number. The reading had never been run with a programme. Fixed; no published figure changes.
  2. *PTH's books when a member dies* (ageing with PTH's balance sheet): the heir's Acre Equity rose by the inheritance, but the heir's home's books did not, so that home's accounts were out by the inheritance from then on (about $306 for one home on seed 1). This was also true of the published ageing reading. The correction moves the equity through both homes' books; it sits behind a new switch part (`fx.pe`), so the frozen batch reproduces, and the candidate main row has it on (without ageing it changes nothing).
  3. *A known hazard made a refusal*: a normal-years slack in the price rule together with the spending layer's normal-years slack would count the same idle capacity twice; the engine now refuses the combination.
  4. *A limit*: with no debt relief (fixed-rate debt keeps up with inflation) and the creditor side on, the creditor side hands the debt's indexation to savers and shareholders but caps the shareholders' gain at inflation times their shares (the cap was written for losses). Under high inflation 8-11% of its ledger is then left with no holder. S59 and S71 always ran no debt relief with the creditor side off; the tests do the same, and S63 must too.
- **The 10,000-adult checks** (asked by S59 and S71). BIG_LINE
- **One thing found that is not round 2's:** the labour response's hours change depends on the population size in the frozen engine itself: under the C2.2 design hours rise 11% at 500 adults and 1.8% at 10,000 (Reference, 2 seeds; the candidate main row: 14.0% and 2.0%). An hours figure from 500 adults should not be quoted without the 10,000-adult figure until this is traced (listed for S63 and S70).
- **The packet for S69** (`dev/packets/s69-main-row.zip`): the written description, every setting of both runs as data, the code those runs execute, and the engine's per-seed outputs for seeds 1-500 in three environments. PACKET_LINE

## What the on-together tests check
For every run of every row: every accounting identity of MODEL_SPEC section 11 holds every year (the money per adult, Acre Equity, BU, the ESP premium, the Source's books, the PTH trust's books, who pays the programme); the main random stream gives exactly 8 draws per adult-year, counted on every run including the one-year pre-pass the contribution's rate needs; no output is infinite or not a number; and each switch's own checks hold (the PTF share never falls and stays between 0 and 100%; the creditor ledger balances and leaves under 5% unplaced; under the "new money" reading nothing of the cost is left unpaid; when PTF prices rise to their cost nothing is subsidised; the within-year cost measure equals the published one when the year is not split). The run-order test runs the candidate main pair and the no-programme run alone first and last in one process; the outputs must be identical, so no run reads state a previous run left.

The other readings: the capacity price rule; the price rule counted in quarters; the velocity drift; bargaining pass-through 0.03; the flat contribution with its unpaid part as new money; PTF prices rising to running cost; no demand ceiling on the PTF share; no debt relief (creditor side off); creditors holding the loss; six tail households per type; no conversion outside the labour force; the floor reading of the spending rule; ageing; the community layer; idle labour in normal years. The pairs the plan named (the price rule's quarters with wealth by asset class and with adults outside the labour force; PTF running costs with the price rule, asset classes, the tail, the community layer and bargaining; bargaining with ageing) are among them.

## Choices (each in `dev/DECISIONS.md`, S68 part 2)
- The candidate main row takes each report's own recommendation; where a report left the choice to S63 with a recommendation, the recommendation is used. S72 (the government's budget line) and S73 (movement in and out of the labour force) will add their switches, and the packet is rebuilt then.
- A "pair" means two switches set to their other readings on top of the main row (which already has every switch on), since "on" alone is the main row.
- The `lf` fix is in place, not behind a switch: the reading had never produced a number under a programme. The PTH estate fix is behind a switch because it changes the published ageing reading's PTH accounts.

## Limits
- 5 seeds per row: a test of the rules, not of sizes. The 10,000-adult checks use 2 seeds.
- The tests check what can be checked from outputs and the books; a rule that is wrong but balanced passes. That is what S69's independent implementation is for.
- The deceased member's home is not re-let to someone else after a death (as before the fix).
- Under no debt relief the creditor side is not a valid reading (above).

## Reproduce
```
node dev/tools/s68_pairs.js ENV 5          # ENV ref, adv, st (about 8 minutes each); dev/runs/s68-pairs/s68-pairs-ENV.json
node dev/tools/s68_big.js ENV 2            # the 10,000-adult checks (about 1 minute each)
python3 dev/tools/s68_pairs_table.py       # dev/runs/s68-pairs/tables.md
node dev/packets/make_s69_reference.js run ENV 1 500 > s69-ENV-1-500.json      # and config, coverage 20 DIR; then build_s69_packet.py
```
Unit tests: five added to `s68UnitSuite` (the refusal; `lf` 'none' finite; `fx.pe`; the count of reads of the retiree flag; the on-together check and run order at one seed).
