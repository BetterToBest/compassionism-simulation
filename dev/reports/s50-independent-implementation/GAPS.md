# S50: gaps and contradictions in the written description of the release row

Found while writing the second implementation (`s50_release.py`) from the S50 packet. I wrote from `MODEL_SPEC.md` and `ODD.md` first. Wherever they did not settle a question exactly enough to reproduce the engine's numbers, I opened the packet's code excerpt. Each entry below is one such question: what the description says, what the code does, and the line of `code/release-row-code-full.js` (the unfolded excerpt) that settled it. Line numbers are that file's.

The list has two parts. **Contradictions** are places where the description says one thing and the code does another; these are findings, and each one should be corrected in the description or in the engine. **Gaps** are places where the description is silent or too loose to reproduce the result; the code settled them, and the description should say what the code does.

Phase 1 (this list) was written without opening the engine itself (`index.html`, `harness.js`) or any other part of the repository's `dev/` folder.

## Contradictions

1. **A recession can start in the last year.** Section 4, item 3 (and Appendix A, gap 22) says no recession starts in year 0 or in the last year. The code draws a possible start in every year from year 1 to year 19 of a 20-year run, the last year included (`for(var y=0;y<years;y++){if(y>0)updateRecession(st);`, line 250). The description should say "from year 1 to the last year".

2. **The essentials' supply path is not the reported no-programme run.** Section 4, item 5 says the no-programme run of the same seed sets each essential's capacity. The capacity in fact comes from a separate price-only run (`priceRun`, line 3000, called through `s3BaseS`, lines 3067-3071), and that run differs from the reported no-programme run in four ways:
   - it has no job loss (its job-loss stream is never set up);
   - it has no safety net, no flat contribution and none of the testbed's accounts;
   - it has no labour response;
   - its wages are not indexed to prices (`PM_DEFAULTS.wIdx` 0).

   It runs in the switch context of whichever run of the seed asks first; the study runs the no-programme row first and caches the path, line 3357. Because the reported no-programme economy differs from the one that sets capacity, the no-programme run's own price level drifts: in Reference, seed 1, it ends at 0.993, although no programme exists. The description should describe the supply run as it is, or the engine should take capacity from the reported no-programme run.

3. **The flat contribution does not pay for the surplus split's price cuts.** Section 12.5 says the year's need includes "PTF and PTH cuts and the split's". In the code the need is the PTF and PTH cuts (`tbPT`, line 2695, summed in `C.cutPT`, line 2313), less the part funded from forgone profit, plus the cash part of PTH appreciation (line 3177). The split's price cuts go into `C.conv` (line 2313), which the Source pays and which the contribution's need leaves out when the Source finances the row.

4. **Octave advancement measures the basic monthly cost at the BLEI paper's daily cost, not the cost of living.** Section 6.8 says the basic monthly cost is "the adult's yearly cost of living at this year's prices (in a household, their share of its needs) times their cost factor". The code uses `dcA × cfPreCCO / 12` (line 2776). Here `dcA` is the BLEI daily cost ($68.33 × 365 = $24,940 a year at year-0 prices) times the price level and the household's BLEI share (lines 2394, 2603), not the MIT basket ($49,370). Appendix B says that the validation path does this, which suggests the release row does not; it does.

5. **Zone induction into PTF is for participants only, in the release row too.** Appendix B lists "SZH induction only for participants" as a difference of the validation path, which implies the release row inducts every adult. In the code the induction test (line 2782) sits inside the participants' block that starts at line 2754, so only participants are inducted.

6. **PTH's books are opened before households are formed, so partners and books disagree.** `pthbInit` (line 3130) gives every adult whose own draw put them in PTH a home and books, and puts everyone else on the waiting list. Only afterwards does `hhInit` (line 3133) make each partner follow the head's PTH status (line 1142). The result:
   - partners who joined PTH with their household have no books, so their Acre Equity grows by the old 3-5% rule, not the price rise + 2% cap, and they are never drawn to leave the network;
   - partners whose own draw had them in PTH, but whose household is not in PTH, hold books for a home with no member. Such a home is never refilled, because only a member who leaves passes a home on.

   In seeds 1-5 of Reference, about 27 of the roughly 98 PTH members (28%) have no books, and 21 to 29 sets of books have no member. Sections 12.2 and 6.13 describe neither. It looks like an ordering mistake in the engine.

7. **The PTH home's price and the trust's rent are measured at the BLEI paper's daily cost.** Section 12.2 says each home is bought at "18.23 years of the member's market housing cost". The code prices it at 18.23 × the housing share × `dcA` (line 2852). As in item 4, `dcA` is the BLEI daily cost ($24,940 a year for one adult at year-0 prices), not the basket's housing cost. The trust's housing receipt each year is the same `hSA × dcA` (line 2859). Section 11 mentions this base only for the 25% routed to Acre Equity.

8. **The SNAP work rule counts rounding remainders as lost months.** For an adult whose whole spell out of work was insured, the countable months should be exactly 0. The code computes them as `weeks out − insured weeks`, where the insured weeks come back from a division of the unemployment insurance paid (line 2715). The result can be a remainder of about 10⁻¹⁶ of a month. The work-rule clock (lines 2246-2247) then counts that adult as losing SNAP months (`snAbN`). The dollars involved are nil, but the count depends on the last binary digit of a floating-point result. This is the only key on which my program and the engine differ at seed 1 of Adverse and Stress: 1.94 against 1.95, one adult-year in 10,000.

## Gaps (the description is silent or too loose; the code settled them)

9. The normal distribution's CDF and its inverse (used for occupations and the SCF wealth copula) are particular approximations: an erfc series, and Acklam's rational approximation clamped to [10⁻¹², 1 − 10⁻¹²] (lines 1035, 1039).
10. Quality is computed as `exp(ln(maxMult × 0.5) + 0.4 z)`, not `maxMult × 0.5 × exp(0.4 z)` (line 299). The two are equal in exact arithmetic, but they differ in the last binary digit.
11. How households are formed (lines 1128-1145):
    - the adults are shuffled (Fisher-Yates, on the household stream);
    - the number of couples is round(n × (couples with + without children)/2), and of those round(couples × share with children) have children; the number of single parents is round(n × their share);
    - the first adult of each household is its head;
    - each household with children draws its number of children (1 to 4) from one uniform, then for each child one uniform for an age band (0-5, 6-11, 12-17) and one for the year within it.
12. A household's needs (lines 1118-1125):
    - each basket component is the one-adult amount times MIT's ratio for the household type (children counted up to 3);
    - childcare is charged for each child under 13, the youngest first, at MIT's prices for the first, second and third child;
    - the household's BLEI share per adult is (housing + food + transport at the type's ratios) / (the same for one adult) / adults;
    - the BU multiplier is 1 + childBU × children / adults.
13. Each year, a household's shares are recomputed at that year's component prices; childcare is priced with "other" (line 1167).
14. Starting wealth from the SCF (lines 1148-1159). The copula combines the rank of the household's summed wages with the rank of the household's summed model wealth draw (from section 4), not with an independent draw. The quantile is interpolated linearly between the survey's percentiles. The household's wealth is split equally among its adults.
15. The household income shock (lines 1165, 2608). Each couple draws a shared swing h (uniform 0.90-1.10) each year, before the adults' own draws. Each adult's swing becomes 1 + √|r| × s × (h − 1) + √(1 − |r|) × (own − 1), with r = +0.10 in normal years and −0.10 in recession years. s is −1 for the second partner when r < 0, and +1 otherwise.
16. Order of set-up: occupations are drawn before households are formed (lines 3127, 3133), so the wage ranks are the adults' own drawn wages. The variance of log wages is the population variance, divided by n (lines 1746-1747).
17. The year-0 contribution comes from a complete one-year run with the contribution at 0, with all its draws; its rate is min(0.90, need / base) (lines 3215, 3299).
18. **The demand that moves essentials prices.** Section 6.12 does not define it. It is the mean over adults of 1 − the unmet share, where the unmet share is min(1, (shortfall at the wealth floor + the cut from income-graded spending) / the adult's basket after PTF and PTH cuts) (lines 2874-2875, 1194). The effective demand is S₀ + max(0, d − S₀) − max(0, S_t − S₀), where S is the supply path (line 3026).
19. Borrowed PTF capacity is charged: depreciation and interest (`PROD_CAP_DEP`, `PROD_CAP_INT`) on the borrowed capacity per adult, paid first out of the PTFs' share of the premium. What is not paid is carried as debt. The depreciation part counts as output that backs the Source's payout (lines 2566-2567). Section 5, A5 mentions the borrowing but not the charge.
20. How the labour response's raise R is built (line 2702): max(1, wage / wage without the programme's raises) × (1 + profit share per dollar of last year's earnings) × (1 + the ESP payroll premium as a share of last year's earnings). The flat contribution enters as (1 − τ)^(ε − ρ) plus an income term τX, and the safety net enters as (1 − m)^(ε − ρ) plus the benefits and m × this year's pre-response earnings as unconditional dollars (lines 1492-1502). Sections 6.11 and 12.4 name these effects but not their form. Section 12.4 says the benefits are linearised at "last year's earnings"; the code uses this year's earnings before the response.
21. The "income" of income-graded spending is earnings, unemployment insurance and the safety net; conversion income and payouts are left out (line 2720). For couples it is pooled with the partner's (lines 1188-1191).
22. The safety net's details:
    - SNAP's shelter cost is the household's MIT housing need at year-0 prices, not what the household pays after PTH (line 2267);
    - the gross income test uses the HHS 2025 guideline, $15,650 plus $5,500 a person (line 2152);
    - the EITC phases out on the larger of earnings and income (line 2240);
    - take-up is a hash of (seed + 700001, the head's index, 0, slot 31 for SNAP or 32 for the tax credits) (lines 2145, 2268);
    - the marginal rate is the benefit lost over the next $1,000 of earnings, held between −0.5 and 0.9 (lines 2269, 2273).
23. The SNAP work rule's countable months (line 2715): 12 × (weeks out − insured weeks) / 52, or 12 × (52 − insured weeks) / 52 when this year's earnings after the labour response are under half of what they were before it. The clock allows 3 countable months over the current year and the two before (lines 2246-2247).
24. The pay cut after a permanent job loss is applied as soon as the spell ends. If the spell ends within the year, the cut lowers that whole year's pay rate, including the weeks worked before the spell (line 1775).
25. ESP workers are the adults whose index i gives frac((i + 1) × 0.618…) < 0.23 (line 2518).
26. Private ESPs' lower BU prices go to non-PTF participants in proportion to the BU each spent last year, capped at their essentials after the PTH cut (lines 2584, 2589).
27. The project pool's "mean rate" is the mean of all participants' own rates, weighted by octave capacity × quality (line 2499).
28. The CIP quality step: each year a participant whose draw `uCipQuality` < 0.15 × cipDemo gains 0.1 of quality, up to the cap (line 2759). Section 7 names the step but no section gives the rule.
29. The unhoused overlay (lines 3507-3530):
    - the year's housing distress d is the share of adults whose earnings, conversion and Social Security, plus their wealth at the start of the year (if positive), fall short of their cost;
    - year 0's d₀ uses the wage rate and starting wealth against the living wage;
    - the rate is 0.22% × ((1 − 0.25 − 0.02) × d/d₀ + 0.25 × (1 − wellness-zone reach) + 0.02).
30. The BLEI reading net of the contribution ("X") replaces the wage by this year's earnings less the contribution (line 1535). The groups P and N are set by the adult's own construction draw (uCCO < the environment's participation rate), in the no-programme run too and whatever their household does (line 3126).
31. Spells and the risk measures are defined only in the code (lines 1649-1655, 1674-1697): which spell lengths are counted, how exits and re-entries are dated, drawdowns, and recovery.
32. For couples, the disposable income behind `giniD` and the cost-of-living gap are the household averages (lines 1196-1197, 2344-2351).
33. The cost per adult also includes the split's reinvestment and the capital charges, both paid by the Source as conversion (lines 2313, 2567, 2594-2595).
34. The aggregate income Y in the price step is earnings, conversion income and Social Security. Unemployment insurance and the safety net are left out (line 2875).
35. The PTF leaving stream draws one number per adult in year 0 too, although nobody leaves in year 0 (line 1873). The draw is on its own stream, so this changes no result, but the draw order matters for reproduction.
36. The PTH housing cut is 35% of the housing share times the member's PTF factor, so the two cuts compound (line 2655).
37. θ_SZH reads the PTF density before the year's leavers (line 2361); the leavers come later (line 2375). The food test reads the density after them (section 12.3).
38. `tauMean` averages all 20 years' rates, year 0's pre-pass rate included (line 3240).

## Phase 2: what the engine says about each contradiction

Read after phase 1 was committed and pushed (commit 50a6ffd), with grep and line ranges in `index.html`. The packet's code is the engine's code; what phase 2 adds is the engine's own comments, which say what each piece was meant to do.

| # | Where the fix belongs | What the engine says |
|---|---|---|
| 1 | The description; whether a recession may start in the final year is a small design question | `buildRecessionPath` (index.html line 2835) carries no rule against a start in the last year. Section 4, item 3 states one, and it does not hold. |
| 2 | The engine (for the design freeze) | The comment above `s3BaseS` (index.html lines 6047-6060, September) reasons that the matched baseline "has no conversion, no PTH and no floor money under the adopted rules, so its prices never move". Job loss, the safety net and the labour response were later added to the reported no-programme run but not to this price-only run. The cache key follows households and income-graded spending, but not those three. Size: the no-programme price level ends at 0.995 on average in Reference (−0.5% over 20 years); there is no drift in Adverse and Stress. |
| 3 | The description | The need's formula carries the note "the Source pays every conversion (BU face value included)" (index.html line 6161). The split's price cuts are paid out of the conversion premium, so the Source pays them, not the contribution. Section 12.5 should list only the PTF and PTH cuts (less the part funded by forgone profit) and the cash part of PTH appreciation. |
| 4 | The description | Deliberate. The comment at index.html lines 2046-2052 says FBS's cost side uses the BLEI paper's daily cost (about $2,078 a month), "not leftover staleness". Section 6.8 should say so. |
| 5 | The description | Induction into PTF has always been a participant's draw in the engine; the release row keeps it. Appendix B's contrast should be removed. |
| 6 | The engine (for the design freeze) | The PTH books' header (index.html lines 4712-4733) says every PTH home has the trust's books beside its member's Acre Equity, and that in a household the head's draw decides. The set-up order (`pthbInit` at line 6114, `hhInit` at line 6117) breaks both: about 28% of members have no books, and about 25 homes a seed have books but no member. Opening the books after households are formed (or opening them for the household, on the head's draw) would match the header. It changes the release row's PTH results, so it belongs in the freeze, measured. |
| 7 | The engine or its comment (for the design freeze) | The header calls `hSA × dcA` "the housing share of their basket, at market prices". In fact `dcA` is the BLEI daily cost (about half the MIT basket), so homes are priced, and the trust's rent counted, at about half the market housing cost the header describes. Either the base or the comment should change. |
| 8 | The engine (a small measurement fix) | The work rule's countable months (index.html line 5715) can be a remainder of about 10⁻¹⁶ when a spell was wholly insured. Treating a count under, say, 10⁻⁹ of a month as zero would make `snAbN` independent of rounding; no other key is affected. |
