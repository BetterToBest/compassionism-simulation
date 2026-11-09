# A price rule that answers demand and capacity (S58)

Nov 9, 2026 · Claude · preregistration: research-update `prereg/2026-11-s58-price-rule.md` (Amendment 1 before the pilot; Amendment 2 after a failed check, before any report) · engine `74ca1a8` (switch `PRICE_RULE`, row option `pr`; study option `mf`; both off by default) · pilot: seeds 1-100, 500 adults, 20 years, Reference, Adverse and Stress · tables `dev/runs/s58-price/tables.md`, every estimate `dev/runs/s58-price/estimates.csv` (tool `dev/tools/s58_table.py`), runs `dev/tools/s58_price.js`, results compassionism-sim-results `s58-price-74ca1a8`.

## In plain words

Every wealth result of the programme rests on the engine's price rule. Until now it was a placeholder: each year, every dollar of new money that no new output backs raises prices one for one the next year. Under the C2.2 design that money is about 37% of household cash income a year, and prices end about 420 times their start after 19 years. Two outside reviews asked for a rule in which prices answer demand relative to what the economy can produce, output answers first where there is slack, wages pass into costs and expectations carry inflation forward. This step built that rule beside the old one and tried it on 100 paired seeds.

1. **No study covers new money on this scale.** The cash-transfer experiments (Kenya, Mexico, the Philippines) were one-time, local and met by slack capacity; the pandemic estimates cover one episode of about 11% of GDP. Nothing measures new money of 30-50% of household income every year. The long-run evidence across 110 countries is that inflation follows money growth about one for one (McCandless and Weber 1995).
2. **The new rule agrees with that evidence, and so the programme's inflation hardly changes.** Its parameters come from US data in the rule's own form (1960-2024). Over 19 years the general price level follows the money with a pass-through between 0.96 and 1.04 in every reading. The programme's inflation stays within about 2 points a year of the old rule: C2.2 in Reference 37.4 → 38.2 points a year at the main values, the release row 31.5 → 32.2. The placeholder's long-run answer was not the weak point.
3. **The path changes, in cycles.** Prices lag at first (14% in the first year instead of 33%), then overshoot and swing in waves of about 9 years (C2.2 in Reference: 72% in year 4, 25% in year 9, 45% in year 13), because wages and last year's inflation carry prices forward and the gap closes only partly each year. The old rule has no such waves.
4. **Basket poverty and the cost of living do not move** (every difference under 0.1 point at the main values, under 0.25 anywhere in the sweep). **Wealth poverty does, and with the waves.** The C2.2 design's effect on wealth poverty in Reference is +0.7 points under the old rule and −1.8 under the new one; across the sweep it runs from −17.8 to +1.6, mostly because year 20 falls at a different point of the wave. A wealth result read at one year from this rule needs its yearly path beside it.
5. **Both rules hide a shortage.** Under the old rule, the year's new money is spent at last year's prices, so about 22.5% of demand each year (C2.2, Reference) is more than any output could supply; under the new rule 11.3%. Read at prices that would clear demand ("shadow prices"), the C2.2 design's effect on wealth poverty is +11.7 points under the old rule and +2.5 under the new one.
6. **The conversion tax was never in the new money.** The engine pays every conversion net of the tax, so the tax (about $12,300 per adult-year in C2.2 Reference, 23% of gross conversion) is already outside the money count, and the Source spends none of it. S39's sentence saying otherwise gets a dated correction note. No engine change was needed for it.
7. **For S63 (fixed before the pilot):** the new rule at its main values as the main-row candidate, the old rule beside it, the sweep as readings; and, from this pilot, wealth outcomes read over the yearly path (or as yearly averages), not only at year 20.

## 1. The evidence (item 1)

Opened in S56 and checked there (triage `audits/2026-11-s39-s55-review-triage.md`, B2): Egger, Haushofer, Miguel, Niehaus and Walker, *Econometrica* 2022 (Kenya; one-time transfers over 15% of local GDP: average price inflation 0.1%, upper 95% bound 0.22%, under 1% at the peak; the authors attribute it to slack capacity); Cunha, De Giorgi and Jayachandran, *Review of Economic Studies* 2019 (Mexico; about +0.2%, not significant; larger in remote villages); Filmer, Friedman, Kandpal and Onishi, *Review of Economics and Statistics* 2023 (Philippines; perishable protein prices up in remote and saturated markets); Allen and Gentilini, IFPRI 2025 (review: minimal average effects, larger where supply is inelastic); de Soyres, Santacreu and Young 2022 (about 2.5-2.6 points of US inflation from pandemic fiscal support); Arias, Rubio-Ramírez and Shin, Philadelphia Fed WP 26-23, 2026 (transfers about 11% of 2019 GDP; the GDP deflator roughly 5% higher by end-2021); Comin, Johnson and Jones (binding capacity constraints explain about half of the 2021-22 rise).

Opened for this step:
- McCandless and Weber, "Some Monetary Facts", Federal Reserve Bank of Minneapolis *Quarterly Review* 19(3), 1995 (PDF sha256 `839622fb76083029b024133701bbb16199c106b17ca7b3e8cad0c63f3ea4ee7b`; text read): over 30 years (1960-1990) in 110 countries the correlation between money growth and inflation is 0.925 (M0), 0.958 (M1) and 0.950 (M2), "very close to linear" with "a slope very close to unity"; money growth and real output growth are not correlated. In the 14 Latin American countries, 0.973-0.993; in the 21 OECD countries, 0.894-0.958.
- FRED series, downloaded Nov 9, 2026 and kept in `sources/s58_fred/` (sha256 of each in `sources/s58_price_rule.json`): real GDP (GDPC1) and CBO's potential GDP (GDPPOT); capacity utilisation for total industry (TCU) and food manufacturing (CAPUTLG311S), Federal Reserve G.17; rental vacancy (RRVRUSQ156N), Census HVS; CPI-U (CPIAUCSL).

What it can and cannot say: none of the studies covers new money of 30-50% of household income a year. The transfer experiments are local, one-time and met by slack; the pandemic is one episode at about 11% of GDP. They are order-of-magnitude checks for small or temporary injections, never targets, and they bound nothing at the programme's scale. The long-run monetary evidence is the only one that speaks to sustained large money growth, and it says prices follow it.

## 2. Claude's reading: the rule

The engine has no firms and no goods market, so its "economy" is households' income and a basket of prices. The new rule keeps the old rule's inputs (the year's new money U not matched by output, and the year's cash income Y; S39 confirmed U is the Source's payout less its matched part) and adds what the old rule lacked. Each year, for the general basket and for food, housing and medical care:

- the money-implied demand level grows by ln(1 + U/Y) (the old rule's price level, kept as a state);
- excess demand x is that level over the sector's current price level;
- the price level rises by α × the year's wage indexation (wages pass into costs) + ρ × last year's basket inflation (expectations) + κ × max(0, x − slack) (demand above what output can supply without pressure) + κ₂ × min(0, x) (a weak pull when prices have overshot the money);
- slack is the sector's normal-years slack plus the share of income a recession leaves idle after the spending layer has restored wages (so money up to that slack raises no price: output takes it).

The essentials' own demand rule (θ, a sector's price rising with the gap between its demand and the no-programme supply) stays on top, unchanged. With κ = 1 and α = ρ = slack = 0 the rule is the old rule exactly (checked to 4e-15 in every environment). With no new money every term is 0: the no-programme run is identical under both rules (checked: 0 of 56 outputs differ). Nothing in the rule draws a random number.

Choices (each in `dev/DECISIONS.md`, S58): excess demand is measured against the no-programme economy's output, so the yardstick is untouched; the environment's own outside inflation (Adverse, Stress) stays outside the rule, as before; wages pass into costs through the engine's own indexation rule, not the measured wage (which would also carry programme raises that `aw` already counts as matched by output); demand that no output can meet is reported, not modelled (no queues, no forced saving).

## 3. Parameters

| Parameter | Main value | Basis | Swept in the pilot |
|---|---|---|---|
| α, wages' share of costs, every sector | 0.5078 | Sourced: compensation of employees over gross domestic income, 2025 (BEA, already in the engine). No sector shares opened: one economy-wide share (a simplification) | 0 |
| κ, response to excess demand (a year, on the log gap) | 0.445 | Derived (`sources/s58_price_rule.py`): OLS of annual CPI-U inflation on last year's inflation and last year's CBO output gap split above and below potential, 1960-2024, 65 years: slope above 0.445 (s.e. 0.189) | 0.25; 1 (the old rule's speed) |
| κ₂, pull below normal | 0.051 | Derived, same regression: slope below potential 0.051 (s.e. 0.147; not distinguishable from 0) | 0 (the first preregistered form); 0.657 (1960-1983) |
| ρ, weight of last year's inflation | 0.275 | Derived, same regression: persistence 0.783 (s.e. 0.073) less α × wage indexation (1), since the wage channel already carries that much | 0 (1984-2024: persistence 0.488, below α); 0.45 (just under 1 − α, above which inflation runs on with no money) |
| slack in normal years | 0 in every sector | Sourced, each sector at or past its no-pressure level: CBO output gap 2025 +1.4%; food manufacturing utilisation 84.9% against its 1972-2025 mean 82.2%; rental vacancy 7.1% against its 1956-2025 mean 7.3%; medical care: no capacity series opened | general basket 0.0446 (total-industry utilisation 75.95% in 2025 against its 79.41% mean) |
| recession slack (`rs`) | counted | the engine's recession path, after the spending layer | off (only the nesting point) |
| the most output can stretch (reporting) | 0.0593 | the largest positive CBO gap since 1949, 1966 Q1, +6.1% | none |

Two cautions. The regression is fitted on years whose output gaps lie within about ±9% and whose inflation stayed under about 15%; the programme's excess demand starts above 30% a year, far outside. And the data show prices barely answer slack (κ₂ near 0), so a rule fitted to them corrects an overshoot slowly.

Amendment 1 (before the pilot) added κ₂ and took κ, κ₂ and ρ from one regression of the rule's full form: without κ₂, a unit test showed that after a three-year burst of money the price level ends 2.7 times the money in logs, with nothing in the rule to stop it. With κ₂ = 0.051 it is 1.31; with 0.657, 0.95.

## 4. The conversion tax (item 3; S39 open item b)

Claude's reading, from the code and the Oct 1 reading of the Hub papers (`dev/reports/03a-financing-reading.md`: the BLEI paper, 6.3 and 9, makes the conversion tax the system's revenue for the BU allocation; rule S4 there: the tax "is withheld from each payout, so it lowers the new money directly"): every conversion the engine pays is recorded net of the tax (project, holder and ESP conversions as gross × (1 − tax); the business premium as gross − tax − face value). The tax never reaches anyone's cash, so it is already outside U; netting it again would count it twice. The money-flow table confirms it on every seed (identity gap 0):

| Year-0 dollars per adult-year, Reference | Release, old rule | Release, new rule | C2.2, old rule | C2.2, new rule |
|---|---|---|---|---|
| BU issued | 13,310 | 13,310 | 23,959 | 23,958 |
| BU spent at face value | 12,771 | 12,765 | 18,309 | 18,278 |
| Conversion, gross | 23,832 | 23,749 | 53,185 | 53,155 |
| Conversion tax withheld | 5,195 | 5,172 | 12,314 | 12,301 |
| Conversion paid, net | 18,637 | 18,577 | 40,871 | 40,854 |
| The Source's payout (BU at face + net conversion) | 31,408 | 31,342 | 59,180 | 59,132 |
| Output matched to it | 2,698 | 2,738 | 19,056 | 19,200 |
| New money U (payout − matched) | 28,710 | 28,604 | 40,123 | 39,932 |
| Price cuts paid (PTF, PTH; outside U under Source financing) | 1,216 | 1,217 | 1,207 | 1,207 |
| Tax re-spent by the Source | 0 | 0 | 0 | 0 |
| Cash income Y | 91,082 | 90,942 | 108,514 | 108,429 |
| U/Y, mean of years | 31.5% | 31.4% | 37.1% | 37.0% |
| Tax as a share of gross conversion | 21.8% | 21.8% | 23.1% | 23.1% |

Adverse and Stress are in the tables file. No row's Source spends the tax: what the papers call revenue for the BU allocation is, in the engine's books, exactly this withholding (it offsets part of the dollars paid for the BU's face value). S54's levers keep project proceeds, not the tax, and those already enter U through `lvStep`. No design question for Duke follows. The engine holds no money stock apart from households' wealth, and BU are not carried between years, so the table has no "balances held" line.

## 5. Tests (`prUnitSuite`, 10)

Off is identical (absent or `'qt'`); no new money is identical; nesting (the rule alone over 30 random years to 6e-16; C2.2's year-20 level in Reference, and in Adverse on seed 39, whose recession leaves idle income, to 1e-15, where counting that slack moves it by 0.2%); slack takes money with no price rise; at capacity prices rise by κ × the gap; more capacity, less pressure (and a sector's own slack lowers only that sector); a capacity loss raises prices with no new money and keeps raising them through wages and expectations; the flat contribution moves the general level far less than Source financing (1.01 against 168 by year 20 on seed 1); expectations overshoot after money stops, less with κ₂; `mf` moves no output and its identity holds. Guard test identical (25 rows × 20 seeds × 483 outputs, three environments); lineage linked twice; validate, unit (282) and domtest (153) pass.

Amendment 2: the first pilot run (engine `295dbee`) failed the preregistered nesting check in Adverse and Stress, because the nesting point still counted the recession's idle income as slack. Option `rs` was added (the main reading unchanged), the whole pilot rerun on `74ca1a8`, and only that run is reported.

## 6. The pilot

Rows: no programme under both rules; the release row and the C2.2 design under both rules; the release row with κ = 0.25; C2.2 with κ 0.25 and 1, ρ 0 and 0.45, α 0, general slack 0.0446, κ₂ 0 and 0.657, and the nesting point. Every programme row is paired with the no-programme run on the same seed. Family: exploratory (pilot); 95% paired-bootstrap intervals, not adjusted; of 540 estimates, 500 exclude zero and 482 survive Holm at 5% (with 100 paired seeds almost any difference does; "excludes zero" is not "material").

**Prices (the primary outcomes).** Programme inflation, points a year (old rule → new rule at the main values): release 31.5 → 32.2 (Reference), 37.6 → 38.5 (Adverse), 16.5 → 16.8 (Stress); C2.2 37.4 → 38.2, 44.0 → 45.1, 45.9 → 47.1. The year-20 price level is 6-17% higher (log difference 0.06-0.16). General pass-through after 3 years 0.86-0.995 (prices lag at first), after 19 years 1.019-1.026. Across the sweep the C2.2 inflation rate stays within −2.1 and +2.3 points of the old rule and pass-through after 19 years between 0.96 (α 0) and 1.04 (κ 1). The money share itself barely moves (C2.2 Reference U/Y 35.8-37.5% across all readings).

The yearly path (C2.2, Reference, geometric mean over seeds; inflation in %):

| Year | 1 | 2 | 3 | 4 | 5 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 19 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Old rule | 33 | 47 | 36 | 44 | 37 | 42 | 41 | 40 | 38 | 36 | 34 | 33 | 32 |
| New rule, main | 14 | 41 | 62 | 72 | 64 | 48 | 27 | 29 | 42 | 43 | 33 | 27 | 28 |
| New rule, ρ 0.45 | 14 | 44 | 74 | 92 | 86 | 78 | 60 | 40 | 24 | 12 | 6 | 5 | 17 |
| New rule, α 0 | 14 | 32 | 38 | 42 | 41 | 41 | 40 | 39 | 38 | 37 | 35 | 33 | 33 |

(Year t is the change from year t − 1.) The waves follow from the rule's arithmetic: with persistence α + ρ = 0.78 and κ = 0.445, a step from no new money to 37% a year produces a damped cycle of about 9 years (each year's swing about 0.89 of the last). With ρ = 0.45 the damping is barely 2% a year. Without wage pass-through (α 0) there is almost no wave.

**The programme's effects (secondary).** Basket poverty, the cost-of-living measure and median real wealth: at the main values the rule changes the programme's effect by less than 0.1 point on the first two in every environment (at most 0.25 anywhere in the sweep, ρ 0.45 in Stress), and by at most $2,400 on median real wealth (C2.2 Reference: the programme's effect −$171,474 under the old rule, −$169,081 under the new). Wealth poverty, C2.2 design's effect in points (old rule → new rule): Reference +0.7 → −1.8; Adverse +30.2 → +27.8; Stress +41.7 → +40.7. Across the sweep in Reference: from −17.8 (ρ 0.45) to +1.6 (κ 0.25); κ₂ moves it by under 0.2. The ρ = 0.45 row is the outlier because year 20 falls in its wave's trough (inflation 5% in year 18): wages, indexed to last year's higher inflation, outrun prices, and savings erode least in the last years. That is a property of where the run stops, not of the programme; at 40 years it would differ.

**Shortage and shadow prices.** Excess demand at the year's prices, mean over the run (C2.2 Reference): 37.1% of no-pressure output under the old rule (the whole year's new money, spent at last year's prices), 20.7% under the new one; the share no output could meet (beyond the slack and the 6.1% stretch): 22.5% and 11.3%; output's part 5.3 points. The shadow ratio in the last year (the measured price level against one that would clear demand): 1.25 and 1.11. At shadow prices, the C2.2 design's effect on wealth poverty is +11.7 (old) and +2.5 (new) in Reference; +46.6 and +36.9 in Adverse; +55.1 and +47.9 in Stress. The new rule's lower shortage comes with its higher price level: prices close more of the gap.

## 7. Limits

- The engine has no goods market: demand no output can meet is reported, not modelled as queues, rationing by price or forced saving; real figures at measured prices overstate what money buys by about the rationed share in that year.
- The parameters are estimated on US data with gaps within about ±9%; the programme's starts above 30%. The long-run evidence (McCandless and Weber) supports the rule's long-run behaviour, not its year-by-year path.
- The waves come from adaptive expectations and partial adjustment fitted to US data; there is no central bank in the model and no response of the programme's own issuance to inflation, either of which would damp them. A phase-in (S54's lever) would shrink them.
- After an overshoot, the rule pulls prices back only weakly (κ₂ near 0); a row in which new money falls sharply (a phase-out, the end of a programme) needs this read with care.
- One economy-wide wage share; no sector slack in the main reading (none was found); medical care has no capacity series.
- Testbed runs only: the price-only mode (`priceRun`) keeps the old rule.
- Pilot at 100 seeds and 500 adults; no 500-seed run before S63's freeze.

## 8. What S63 must carry

- The main-row recommendation fixed in the preregistration (decision rule 2): `pr: true` (the main values), with today's rule beside it as the published placeholder, and the sweep (κ 0.25 and 1; ρ 0 and 0.45; α 0; general slack 0.0446; κ₂ 0 and 0.657) as readings. This goes to the ledger decision S63 files before any result.
- From this pilot: every wealth outcome (wealth poverty, median real wealth, S57's measures) read over the yearly path or as yearly averages beside year 20 and year 40, because the rule's waves move the year-20 reading. The yearly price level `plv_*` and S53's yearly series already exist; a yearly wealth-poverty key may be needed.
- The shadow-price readings and the rationed share beside every real-wealth figure (keys `prWsh`, `prPovSh`, `prRat`, `prSh`), under both rules.
- The money-flow table (`mf`) on the main rows, so U, the tax and matched output are printed with each result.
- Hub wording (S25, S40), replacing the placeholder sentence of S39: "The engine's prices now follow a rule fitted to US data, in which prices answer demand relative to capacity and carry inflation forward through wages and expectations. Over 19 years the programme's new money still passes into prices about one for one, as long-run evidence across countries finds; the path comes in waves."
