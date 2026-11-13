# Bargaining power: does a Basic Unit let workers bargain higher wages? (S60)

Nov 13, 2026. Pilot: seeds 1-100, 500 adults, 20 years, three environments, engine `69f69f5`. A pilot is a mechanism check, not a result; the frozen 500-seed batch decides. Preregistered before the build and before any run (research-update `prereg/2026-11-s60-bargaining-power.md`, with one dated amendment before the pilot). Tables: `dev/runs/s60-bargain/tables.md`. Per-seed files: compassionism-sim-results `s60-bargain-69f69f5`.

## In short
1. **The question.** A Basic Unit (BU) changes what a worker could fall back on if they walked away from a job. In bargaining theory a better fallback (an "outside option") lets workers demand more, as long as employers pay less than workers add (a "markdown"). The model had no such channel. This step builds one, in reduced form, behind a switch, and asks how much it is worth.
2. **What the evidence says: almost nothing.** The largest natural experiment on the value of not working (four Austrian unemployment-benefit reforms) finds wages move by less than a cent per dollar of benefit, and rules out more than 3 cents. The one US experiment that gave people $1,000 a month and asked found no rise in the lowest wage they said they would accept (−$0.27 an hour, standard error $0.50) and no rise in hourly pay (−$0.14; more than +$0.58 ruled out). No study of unconditional cash (Finland, Alaska, Stockton, Kenya) finds wages rising through workers' fallback; in Kenya wages rose because the cash created demand.
3. **So the main reading is no bargained raise (pass-through 0), identical to the switch off.** That is a finding, not a default: the model's figures do not need a bargaining gain, and the evidence gives none.
4. **At the largest pass-through the evidence allows (3 cents per dollar)** the bargained raise is about $650 per worker a year in the release design in Reference and Adverse ($280 under Stress, where fewer adults take part) and about $910 in the C2.2 design, 5-9% of all the programme's raises to the wage rate. It lowers wealth poverty by a further 0.1-0.3 points and basket poverty by 0.2-0.6 points. Small, and bounded.
5. **At the US experiment's own upper bound (10 cents)** the raise is about $2,150 in the release design ($920 under Stress) and $3,000 in C2.2, 15-24% of the programme's raises; wealth poverty falls a further 0.4-0.9 points and basket poverty 0.5-1.9. This is the outer edge of the evidence.
6. **The Nash bargaining readings (24 and 48 cents), which the evidence rejects,** would make bargaining 28-59% of the programme's wage gains: $2,100-$14,000 per worker a year, wealth poverty 0.6-3.4 points lower and basket poverty 0.7-6.1 points lower. They are shown as the theory case only. Even the theory cannot produce the evidence's figures: with the measured markdown, a pass-through of 3 or 10 cents would need a negative reservation wage (the puzzle the Austrian study reports).
7. **The markdown matters only for those theory readings.** At 3 cents almost no worker reaches the cap (0.1% of worker-years at most); at 10 cents 1-6% of worker-years do; at 48 cents 19-65%. With no markdown there is no room and the switch does nothing.
8. **The outside option the programme adds is large.** A worker in the release design gains about $22,400 a year of what they would keep without working ($31,400 in C2.2; $9,600 in the release design under Stress, where fewer adults take part): a median of 33% of their full-year earnings (P10 3%, P90 98%) in Reference. A large fallback that moves wages little is what the evidence describes.
9. **Who pays a bargained raise is not modelled,** and it matters: at 10 cents the raises are 7-23% of all the capital income the model's adults receive, at 48 cents 28-83%, and more than all of it with the manufacturing markdown in C2.2. The raise also lowers the programme's inflation (by 0.1-0.7 points a year at 3 cents, 0.3-2.2 at 10 cents) because it adds to the income the price rule divides by while nobody's income falls to pay for it. A payer is needed before any reading above 3 cents is used for a wealth or price result.
10. **The hours and participation check against the US experiment.** The engine loses 12.9 cents of earnings per dollar of a $12,000 transfer per adult (15.6 cents per worker; the study: 16 cents): it passes. But nobody in the engine stops working (0.0 points; the study: −4.2 points). The engine puts the whole response on hours. Listed for the specification screen (S70) and the freeze (S63).
11. **For the design freeze (S63), fixed before the results:** the switch at pass-through 0 in the main row (the same as off), with 3 cents beside every wage, income and poverty result and 10 cents as the outer evidence reading. The Nash readings go to S70's screen as the theory case.

## Claude's reading of the design
The Hub's papers expect the programme to remove the economic desperation that makes people accept bad terms: the Citizens Internet Portal paper (section 6.2.1, "Corruption exploits desperation": workers threatened with job loss, whistleblowers who "choose silence over unemployment"), and the Corporate Transformation paper scores "labor exploitation (poverty wages, poor conditions)" as an extraction category. The BLEI paper cites the Alaska dividend's negligible employment effects. No paper gives a figure for how much wages rise, or says that the BU raises wages one for one. Where the papers are silent the model takes the most cautious reading: a BU raises a worker's outside option by what it buys, and that moves the wage only by the pass-through the evidence supports. This models the design; it does not change it.

## What was built
A switch, `BARGAIN` (row option `bg`), off by default. Off, nothing in it is read and every figure is unchanged (guard test: 25 rows, 20 seeds, 483 outputs, three environments, identical). It is a reduced form: there are no firms, vacancies or hiring in the model, and this step does not add them (a full employer layer is later work, as the review triage decided).

- **The markdown.** Each worker is paid a share `m` of what they add to their employer's revenue (the marginal revenue product). The main value is 1/1.21 = 0.826: workers add 21% more than they are paid (Azar, Berry and Marinescu 2022, the median across US occupations in online job applications). Swept: 1/1.53 = 0.654 (Yeh, Macaluso and Hershbein 2022, US manufacturing plants) and 1 (no markdown). What a worker adds is read on the year's wage, including the programme's own raises (the engine treats those as matched by output). So the room for a bargained raise is 21% of the wage (53% with the manufacturing markdown, none without a markdown).
- **The outside option.** What the programme adds to what a worker would keep if they stopped working: the same unconditional dollars the engine's income effect already counts, at the same weights. A Basic Unit counts at the value of what it buys (BU spent at the worker's own prices); expired BU buy the holder nothing and count for nothing. Cash in the comparison designs, price-cut dollars, last year's liquid PTH appreciation, owners' dollars and conversion proceeds (as far as the income effect treats them as unearned) count too. Today's safety net does not: the model's wages were measured with it in place. With no programme the rise is zero, so a no-programme run is identical to off.
- **The bargained raise.** For the year, `g = min(π × O / E, 1/m − 1)`: π cents of yearly wage per dollar of yearly outside option `O`, against the worker's full-year earnings `E`, capped at what the worker adds. The raise lasts as long as the outside option; it is not added to the wage path.
- **One wage elasticity (guardrail 7).** A bargained raise is a change in the return to work, so it gets the elasticity every raise gets: earnings are multiplied by `(1 + g)^(1 + ε − ρ)` (the higher wage, and the hours response to it). The income effect is unchanged: the same dollars, the same 16 cents per dollar. The hours measure and project hours are valued at the bargained wage, so hours stay hours.
- **No random draw.** Adults outside the labour force, retirees and anyone with no earnings in the year get no raise.
- **Tests.** Seven unit tests (`bgUnitSuite`): off, π 0 and no markdown give results identical to the switch absent on every key (632) in all three rows, and any π leaves a no-programme row identical; the raise by hand; one elasticity (year-0 earnings with the raise equal those without it times `(1 + g)^1.33` with no income effect, and times `(1 + g)` with no response, for every worker); the cap (no raise above `1/m − 1` in any year, the cap binds for some workers at π 1); monotone in π and in the room; the outside option's dollars (zero with no programme, unchanged with the safety net off, smaller without the BU, larger with the BU counted twice); and no random draw (the main stream at the same place at the end of every year).
- **Files.** `index.html` (the switch, after `LABOR_DEFAULTS`; the labour block in `runYear`; the outside-option tally in `tbLab`), `harness.js` (`bgUnitSuite`), `sources/s60_bargain.py` (every source figure as read, the readings derived from them), `dev/tools/s60_bargain.js` (the pilot and the validation), `dev/tools/s60_table.py` (the tables).

## Sources (opened for this step)
| source | what it measures | figure used |
|---|---|---|
| Azar, Berry and Marinescu, NBER w30365 (2022) | how many applications a job loses when its wage falls (online job board) | firm-level elasticity 4.8; workers add 21% more than their wage (median): `m` 0.826 |
| Yeh, Macaluso and Hershbein, *AER* 2022 | marginal product over wage, US manufacturing plants | 1.53 on average: `m` 0.654 |
| Jäger, Schoefer, Young and Zweimüller, *QJE* 2020 | wages after four large Austrian unemployment-benefit reforms (a better outside option for every worker) | less than $0.01 of wage per $1.00 of benefit (preferred estimates 0.00 and −0.027); more than $0.03 ruled out; the Nash bargaining model predicts $0.24-$0.48 |
| Vivalt et al., NBER w32719, revised Aug 2026 (*QJE* 2026) | $1,000 a month for three years to 1,000 low-income adults in two US states, against $50 a month | income excluding the transfer −$1,900 a year (16 cents per dollar); participation −4.2 points; hours −1 to −2 a week; hourly pay −$0.14 (more than +$0.58 ruled out); reported reservation wage −$0.27 an hour (standard error $0.50); more job search, longer spells out of work, no change in job quality |
| Egger et al., *Econometrica* 2022 | large cash transfers in rural Kenya | employees' hourly wages +0.04 (s.e. 0.04) in recipient households and +0.19 (s.e. 0.10) in non-recipient households, on a mean of 0.70; the paper attributes the gains to the demand the transfers created |
| Verho, Hämäläinen and Kanninen, *AEJ: Policy* 2022 | Finland's basic income in place of minimum unemployment benefits | no significant change in days employed in the first year; no wage measure |
| Jones and Marinescu, *AEJ: Policy* 2022 | Alaska's permanent dividend | no effect on employment; part-time work +1.8 points; no wage measure |
| West and Castro Baker, Stockton SEED first-year results (2021) | $500 a month for two years, 125 recipients | full-time employment rose faster among recipients; small sample; no wage measure |

What they say together: no study finds that unconditional cash raises wages through a better outside option. The one US experiment that asked finds no rise in the reservation wage people report and no rise in hourly pay. The largest natural experiment on the value of not working finds less than a cent per dollar. The wage gains found in Kenya came from the demand the cash created, which this switch does not model.


## Results
Rows: S71's rows (the frozen release row and the C2.2 design against their own no-programme runs; today's safety net; CPS earnings; wealth by asset class with owners, capital income and the creditor side; the weighted tail) with adults outside the labour force. Every figure below is a paired effect over seeds 1-100; intervals are the 2.5th-97.5th percentiles of 2,000 bootstrap replicates, unadjusted. All tables, with the Adverse and Stress environments, are in `dev/runs/s60-bargain/tables.md`.

**Checks.** The readings that must equal off do: pass-through 0 and pass-through 0.48 with no markdown differ from off on none of 210 series in any environment.

**The mechanism, release design, Reference** (means per worker-year, years 1-19, Year-0 dollars):

| | 0 (main) | 0.03 | 0.10 | 0.24 (theory) | 0.48 (theory) | 0.48, markdown 1.53 (theory) |
|---|---|---|---|---|---|---|
| outside-option rise | $22,441 | $22,447 | $22,460 | $22,482 | $22,511 | $22,520 |
| bargained raise (wage part) | 0 | $658 | $2,187 | $5,010 | $8,578 | $10,269 |
| earnings it adds after the hours response | 0 | $787 | $2,623 | $6,041 | $10,393 | $12,500 |
| share of the programme's raises to the wage rate | 0% | 5.0% | 14.6% | 27.9% | 39.7% | 43.3% |
| worker-years at the markdown cap | 0% | 0% | 1.3% | 13.0% | 38.5% | 7.9% |
| wage over what the worker adds | 82.6% | 83.3% | 84.8% | 87.6% | 91.2% | 73.4% |
| raise over the capital income adults receive | 0% | 5.0% | 16.7% | 38.3% | 65.4% | 78.3% |

**What bargaining adds to the programme's effects, Reference** (the effect under each reading less the effect with no bargaining, paired by seed; points unless stated):

| | design | 0.03 | 0.10 | 0.24 (theory) | 0.48 (theory) |
|---|---|---|---|---|---|
| wealth poverty, year 20 (weighted) | release | −0.2 (−0.3, −0.2) | −0.7 (−0.8, −0.6) | −1.5 | −1.8 |
| | C2.2 | −0.1 (−0.2, −0.1) | −0.4 (−0.5, −0.3) | −0.6 | −0.7 |
| basket poverty, person-years | release | −0.4 (−0.4, −0.4) | −1.2 (−1.3, −1.2) | −2.3 | −2.6 |
| | C2.2 | −0.2 (−0.2, −0.2) | −0.5 (−0.5, −0.5) | −0.7 | −0.7 |
| real wage earnings per adult-year | release | +$650 | +$2,177 | +$5,031 | +$8,665 |
| inflation a year | release | −0.27 | −0.89 | −1.99 | −3.28 |
| | C2.2 | −0.41 | −1.32 | −2.82 | −4.38 |
| top 1% share of wealth, year 20 (weighted) | release | −0.03 | −0.09 | −0.20 | −0.33 |

With no bargaining the programme's effects are (release, Reference): wealth poverty −14.8 points (−15.1 to −14.4), basket poverty −18.3, real wage earnings −$4,312 per adult-year (the income effect), inflation 36.3% a year, top 1% share −1.35 points; C2.2: −21.7, −29.4, −$5,716, 42.3%, −2.08. Every reading keeps every sign.

**Adverse and Stress.** The same pattern. In Adverse the bargained raises are a little smaller than in Reference but reach the cap more often; the gains on basket poverty are larger (release, 0.10: −1.9 points). Under Stress the release design reaches fewer adults, so its outside option is $9,600 and its raises less than half of Reference's; the C2.2 design's raises are as large as in Reference.

**Reservation wages.** Under the Nash relation (wage = (1 − π) × what the worker adds + π × reservation wage) the starting reservation wage is (1 − (1 − π)/m)/π of the wage: −579% at 0.03 and −89% at 0.10 (impossible: the relation cannot give those pass-throughs with the measured markdown), 34% at 0.24 and 77% at 0.48. With the programme's outside option added, the median worker's reservation wage at 0.48 would be 111% of their wage and the 90th percentile's 175%, above the 121% they add: in a Nash world those jobs would no longer be worth keeping. The engine does not end them (its only exit is the income effect), one more reason the theory readings are not candidates.

**Validation against the US experiment** (no programme; $12,000 a year to every adult, unfinanced, three years, Reference):

| reading | earnings per adult-year | per transfer dollar | adults with earnings | bargained pay per hour | inside the study's pay interval (−$0.87 to +$0.59) |
|---|---|---|---|---|---|
| no bargaining | −$1,544 (−1,552, −1,537) | −0.129 | 0.0 points | 0 | yes |
| 0.03 | −$1,200 | −0.100 | 0.0 | +$0.17 | yes |
| 0.10 | −$401 | −0.033 | 0.0 | +$0.56 | yes (edge) |
| 0.24 | +$1,189 | +0.099 | 0.0 | +$1.33 | no |
| 0.48 | +$3,753 | +0.313 | 0.0 | +$2.56 | no |

The study: −$1,900 a year (16 cents per dollar), participation −4.2 points. The engine's 12.9 cents per adult is 15.6 cents per worker-year (17.5% of adult-years have no earnings: adults outside the labour force, who neither earn nor respond, and years out of work). Under the theory readings a cash transfer would raise earnings, the opposite of what the experiment found.

## The preregistered rules
1. **Checks: passed.** Unit tests (7 new, 318 in all) and the guard test pass; the two readings that must equal off do, on every kept series in every environment.
2. **Evidence test.** Within the evidence: 0 and 0.03. The outer edge of the US experiment alone: 0.10 (its pay change, +$0.56 an hour, is just inside the interval). Theory readings the evidence rejects: 0.24 and 0.48.
3. **Share of the wage gain from the outside option:** 0% (main), 5-9% (0.03), 15-24% (0.10), 28-59% (theory readings), by design and environment (tables, section 2).
4. **Hours and participation.** Earnings per dollar: 15.6 cents per worker against the study's 16: passes. Participation: 0.0 points against −4.2: less than half, so reported as a limit and listed for S70 and S63; not fixed here.
5. **Recommendation to S63 (fixed before the results):** `BARGAIN` at pass-through 0 in the main row (identical to off), 0.03 beside every wage, income and poverty result, 0.10 as the outer evidence reading; markdown 1/1.21 main, 1/1.53 and 1 swept; the Nash readings to S70's screen as the theory case. S63 chooses.
6. No synergy is claimed.

## What the sources said, where it differs from the plan
- The plan quoted the January 2026 revision of the US experiment (participation −3.9 points, −$1,800 a year) and the review triage recorded "no QJE version found". The August 2026 revision gives −4.2 points and −$1,900, and the NBER page lists it as *QJE* 141(4), 2026. The triage carries a dated correction; the engine's 16 cents per dollar is unchanged (the paper still gives it).
- The plan asked for "evidence from unconditional cash and basic-income studies on wages, hours and job search". Only the US experiment and Kenya measure wages; Finland, Alaska and Stockton measure employment only. On job search the US experiment found recipients more likely to search (+6 points) but applying to fewer jobs, with longer spells out of work and no better jobs.
- The plan's phrase "a Basic Unit raises reservation wages" is the hypothesis, not the finding: the one experiment that measured reservation wages found no rise.

## Limits
- **Reduced form.** One markdown for every worker; no firms, vacancies or job-to-job moves. The markdown is read on the year's wage including the programme's raises, so those raises never use up the room.
- **Who pays a raise is not modelled.** A bargained raise comes out of the employer's markdown (its owners) or its prices. The tables show its size against the capital income the model's adults receive (`bgK`); under the Nash readings it is most of it. A payer must be built before any reading above 0.03 is used for a wealth result.
- **The benefit evidence is for a dollar paid only when not working.** A BU is paid whether or not one works, so in standard bargaining models it moves the outside option less than an unemployment benefit of the same size. The bound of 0.03 is, if anything, generous for a BU.
- **Demand-driven wage gains** (Kenya) are not this mechanism. In the engine, wages follow the price level (indexation), and the spending layer fills recession slack only.
- **No participation margin.** The engine's labour response puts the whole income effect on earnings within work; nobody stops working because of it (validation, above).
- **A reporting leak found by the tests (older than this step).** The production side's yearly record (`PDS`) is reset only in runs where the production side acts, so a no-programme row reports the PTF-capacity keys (`pdC5`, `pdC10`, `pdC19`, `pdMem19`) the previous programme run left there. Reporting only (no rule reads them in a no-programme run); whether an earlier table quoted them for a no-programme row is for S68 to check. The unit test does not compare them for a no-programme row, and S68's per-run state reset is to fix it.
- **Inflation falls with any bargained raise** because the raise adds to the income the price rule divides new money by, while nobody's income falls to pay for it. Part of the theory readings' poverty gains is this.
- Tested with S71's rows and `lf` only; S68's pairwise tests cover the other round-2 switches.
