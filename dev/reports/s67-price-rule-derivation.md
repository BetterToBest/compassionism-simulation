# The price rule: where its numbers come from, its time step and its wording (S67)

Nov 13, 2026 · Claude · preregistration: research-update `prereg/2026-11-s67-price-rule-derivation.md` (committed before any regression or run; Amendment 1 after the data work and before the pilot) · engine `985f0c3` (options `q`, `bv`, `bd` of the capacity price rule; all off by default) · pilot: seeds 1-100, 500 adults, 20 years, Reference, Adverse and Stress · data work `sources/s67_pstar.py`, `sources/s67_panel.py`; closed form `dev/tools/s67_closed_form.py` (`dev/runs/s67-price/closed_form.md`); pilot `dev/tools/s67_price.js`, tables `dev/runs/s67-price/tables.md`, every estimate `dev/runs/s67-price/estimates.csv`; results compassionism-sim-results `s67-price-985f0c3`.

## In plain words

The engine has two price rules. Today's rule (the published one) raises prices each year by exactly the year's new money that no new output backs. The capacity rule, built in S58, lets prices close only part of the gap between money and prices each year and carries inflation forward through wages and expectations; its numbers were fitted to US data. An audit on Nov 9 questioned where those numbers come from and whether the rule's 9-year waves are real. This step checked each point, before S63 decides which rule the main results use.

1. **Both rules assume the same long-run answer; neither finds it.** In both, sustained new money ends up in prices one for one. S58's report said the new rule "agrees with that evidence" as if the pilot had shown it. It could not have shown anything else. Dated correction notes now say so in the S58 report and its proposed Hub sentence; a third note corrects a sentence in the S57 report (for someone holding savings in dollars, inflation does destroy their value). No figure changed.
2. **The waves are the rule's own arithmetic, now written out.** Yearly inflation under the capacity rule obeys a two-term recursion. At the main values it swings in a wave of 8.8 years that shrinks by 11.5% a year. The formula tracks the engine's yearly path within about 1 point of inflation on average.
3. **Estimated on the variable the rule actually uses, the response speed is zero.** S58 took the speed at which prices answer excess demand (0.445 a year) from a regression on the output gap. The rule applies it to a different thing: the gap between the money-implied price level and prices. On that variable, with US data for 1970-2024, the estimate is −0.001 (standard error 0.05). It is large in the 1970s (0.88) and near zero since 1984 (0.04). With the corrected standard errors, S58's own 0.445 is not distinguishable from zero either (standard error 0.24).
4. **Seventy-seven episodes of sustained high inflation give different dynamics again.** In countries with at least three years above 20% (World Bank data, 52 countries, 518 country-years), last year's inflation carries over with a weight of about 0.67 (the US fit: 0.78), and prices close the gap to money at 0.05-0.18 a year, not 0.445, and not distinguishable from zero. Inflation ran ahead of money growth in two thirds of the episodes, by about 4 to 6 percentage points a year.
5. **A shorter time step halves the waves; it does not remove them.** With prices moving four times a year and values fitted to quarterly data, the C2.2 design's wave in Reference is 19.8 points of yearly inflation against 39.1 under the yearly rule (12-14 against 38-42 in Adverse and Stress). With the yearly rule's own values converted to quarters the wave is unchanged (40.7), as the formula says it must be. So the waves come from the values (how much of last period's inflation carries forward), not from the length of the step; and the values are the part that is not pinned down.
6. **The "shortage" under today's rule is mostly the yearly step.** Run in quarters, today's rule gives the same year-end prices and the same results, but the share of demand that no output could meet falls from 22.5% to 1.9%. In its place prices are on average 12.6% above the year's opening level during the year, which the engine's yearly accounts do not charge to households. A velocity response fitted to the episodes changes nothing (pass-through moves by 0.0002). The drift the episodes do show raises the programme's inflation by about 6 points a year (37.4 to 43.4 under today's rule) and its effect on wealth poverty by 5 to 7 points; basket poverty and the cost of living move by 0.3 point or less under every reading.
7. **Recommendation for S63 (set by a rule fixed before the results): today's rule as the main row,** with the capacity rule and its readings beside it, and every wealth outcome given at year 20, at year 40 and as a yearly average under both rules. The preregistered test asked two questions that do not look at any poverty or wealth result: is the response speed identified in the rule's own form (no), and do the waves survive a shorter time step (yes by the preregistered threshold, narrowly: 0.51 of the yearly wave in Reference against a threshold of one half; 0.31-0.32 in Adverse and Stress). Both had to be yes for the capacity rule. Section 9 gives both views in full.

## 1. Sources

Two papers the step named could not be opened from the session, and nothing is quoted from them:
- Hallman, Porter and Small, "Is the Price Level Tied to the M2 Monetary Aggregate in the Long Run?", *American Economic Review* 81(4), 1991 (JSTOR paywall; the authors' 1989 Federal Reserve staff study was not found online). Its form is taken from Tatom, "The P-Star Model and Austrian Prices", Federal Reserve Bank of St. Louis Working Paper 1992-001A (sha256 `34072dc2…afd69`; read): the equilibrium price level is P* = M V*/Q*, money per unit of potential output at trend velocity, and inflation's change answers last period's gap between P* and P. Tatom also notes that the 1991 paper's constant trend velocity "is doubtful": M2 velocity trended up to 1981 and down after.
- Cagan, "The Monetary Dynamics of Hyperinflation", 1956 (no open copy). Opened instead: Fischer, Sahay and Végh, "Modern Hyper- and High Inflations", NBER Working Paper 8930, 2002 (sha256 `2bfa5049…d011`; read): across 94 market economies the cross-section slope of average inflation on average M2 growth is 1.115, "extremely strong and close to one-to-one", in high- and low-inflation countries alike; inflation inertia matters, and is by and large lower during high-inflation episodes than during low-inflation ones (four exceptions among 16 countries). And Ball, "The Dynamics of High Inflation", NBER Working Paper 4578, 1993 (sha256 `2055a238…576a`; abstract and model read): a high-inflation model with Cagan's money demand and an inertial Phillips curve.

Data, each file hashed in the output JSON:
- FRED, downloaded Nov 13, 2026 (`sources/s67_fred/`): M2 (M2SL), nominal GDP (GDP), real GDP (GDPC1), CBO potential GDP (GDPPOT), the GDP deflator (GDPDEF), CPI-U (CPIAUCSL).
- World Bank, World Development Indicators (database updated Nov 11, 2026; `sources/s67_wdi/panel.csv`, with the hashes of the raw downloads): consumer-price inflation, broad money growth and real GDP growth, 217 countries, 1960-2025; 7,225 country-years have all three.

## 2. The correction notes (item 1)

Three dated notes, no figure changed (`dev/tools/no_figure_change.py`: the engine and every data file are identical; the 14 numbers that moved in the words are the notes' own dates, step labels and a file name):
- S58 report, "In plain words" item 2: the one-for-one long-run pass-through is built into the capacity rule. Its state is a money-implied price level that prices close on, so with steady money growth, any response speed above zero and persistence below one, steady inflation equals money growth. It is an assumption shared with today's rule and supported by McCandless and Weber's cross-country evidence; it is not a result of the pilot.
- S58 report, section 8: the proposed Hub sentence is withdrawn and a replacement is given that says "assumes".
- S57 report: "not because wealth is destroyed" is wrong for the holder of nominal savings; the model treats all wealth as dollars that do not reprice, which is an assumption.

## 3. The closed form (item 2)

Write φ = α + ρ (the share of last year's inflation carried forward by wages and expectations), κ the response speed, m the yearly growth of money in logs. When wages are fully indexed, the basket moves with the general level, there is no slack and prices sit below the money-implied level, the engine's rule is exactly

π(t) = (1 + φ − κ) π(t−1) − φ π(t−2) + κ m.

Three things follow without running anything:
- Steady inflation is m for any κ > 0 and φ < 1. That is the built-in pass-through.
- In the steady state prices sit below the money by (1 − φ) m / κ. At the main values and the C2.2 design's money (m about 0.32) that is 0.156 in logs: a standing shortage of about 14% of demand, the order S58 measured (on average over the run, 11.3% of demand beyond what output could stretch to).
- When (1 + φ − κ)² < 4φ the path is a damped wave with yearly shrink factor √φ and period 2π / arccos((1 + φ − κ) / (2√φ)) years.

| Reading | φ | κ | Shrink factor a year | Period, years | Wave on a step of money (years 5-19, points) |
|---|---|---|---|---|---|
| Main | 0.783 | 0.445 | 0.885 | 8.8 | 35.8 |
| κ 0.25 | 0.783 | 0.25 | 0.885 | 12.0 | 32.6 |
| κ 1 | 0.783 | 1 | 0.885 | 5.6 | 35.3 |
| ρ 0 | 0.508 | 0.445 | 0.713 | 8.6 | 10.0 |
| ρ 0.45 | 0.958 | 0.445 | 0.979 | 9.1 | 73.4 |
| α 0 | 0.275 | 0.445 | 0.524 | 9.6 | 2.0 |
| κ₂ 0, κ₂ 0.657, slack 0.0446 | 0.783 | 0.445 | 0.885 | 8.8 | 35.9, 36.4, 36.7 |
| Today's rule (κ 1, α 0, ρ 0) | 0 | 1 | none | no wave | 0 |
| US fit, 1960-1983 | 0.922 | 0.282 | 0.960 | 11.5 | 67.7 |
| US fit, 1984-2024 | 0.488 | 0.615 | 0.699 | 7.0 | 4.7 |
| High-inflation panel, pooled | 0.663 | 0.085 | 0.814 | 25.1 | 17.0 |
| High-inflation panel, episode effects | 0.544 | 0.178 | 0.737 | 16.2 | 4.9 |

("Wave" is the largest less the smallest yearly inflation in years 5-19 when money starts growing at 0.32 log a year, the rule alone; the full table, with pass-through and the rationed share, is in `closed_form.md`.) The wave's size is set almost entirely by φ: 36 points at the main value, 5 with the 1984-2024 persistence, 68 with the 1960-1983 one. κ sets its length.

**Check against the engine.** For each capacity row of the S58 pilot (Reference, 100 seeds) the formula was driven by that seed's own money and compared with the engine's yearly inflation. Mean absolute difference: 1.0 point at the main values (largest on the mean path −2.6 points, in year 4); 0.4 to 1.6 across the other readings, except ρ 0.45, where it is 2.0 and reaches 11.8 points in year 19 (the nearly undamped case, where small differences build up). The engine's wave at the main values is 39.1 points against the formula's 41.4; its period on the path 9.3 years against 8.8. The formula is an approximation, for three stated reasons: the gap turns negative from about year 6 (prices overshoot, and the weaker pull κ₂ applies), the essentials' own demand rule moves the basket, and the money is not steady.

**For MODEL_SPEC (S68 places it).** "Under the capacity rule yearly inflation follows π(t) = (1 + φ − κ)π(t−1) − φπ(t−2) + κm while prices are below the money-implied level, with φ = α × wage indexation + ρ. Sustained money therefore passes into prices one for one (an assumption of the rule, shared with the quantity rule), with a standing gap of (1 − φ)m/κ. For (1 + φ − κ)² < 4φ the adjustment is a damped wave of period 2π/arccos((1 + φ − κ)/(2√φ)) years and yearly shrink factor √φ: 8.8 years and 0.885 at the main values. With q sub-steps a year the same form holds per sub-step with the sub-step's values."

## 4. The response speed on the rule's own variable (item 3)

The price gap is g = p* − p, with p* = ln M2 + trend velocity − ln potential output. It equals the velocity gap plus the output gap, so S58's regression is the special case that ignores velocity. Annual data, inflation on last year's inflation and last year's gap; Newey-West standard errors in brackets.

| Form | Trend velocity | Sample | Persistence | Slope above (κ) | Slope below (κ₂) | Two-sided slope |
|---|---|---|---|---|---|---|
| S58's: output gap | n/a | 1960-2024 | 0.783 (0.096) | 0.445 (0.240) | 0.051 (0.165) | 0.213 |
| S58's: output gap | n/a | 1970-2024 | 0.749 (0.103) | 0.967 (0.352) | −0.036 (0.170) | |
| **Price gap (main)** | ten years before | 1970-2024 | 0.809 (0.099) | **−0.001 (0.051)** | 0.092 (0.068) | 0.034 (0.022) |
| Price gap | ten years before | 1970-1983 | 1.152 (0.209) | 0.881 (0.347) | 0.485 (0.146) | 0.555 (0.088) |
| Price gap | ten years before | 1984-2024 | 0.519 (0.137) | 0.040 (0.059) | −0.015 (0.048) | 0.020 (0.028) |
| Price gap | constant | 1960-2024 | 0.783 (0.092) | 0.002 (0.024) | 0.054 (0.028) | 0.021 (0.013) |
| Price gap | constant | 1960-1983 | 1.082 (0.127) | 0.165 (0.180) | 0.412 (0.109) | 0.302 (0.072) |
| Price gap | constant | 1984-2024 | 0.456 (0.168) | 0.024 (0.030) | −0.001 (0.032) | 0.015 (0.014) |
| Price gap | two-sided filter | 1960-2024 | 0.846 (0.120) | 0.125 (0.089) | 0.297 (0.121) | 0.194 (0.056) |
| Price gap | two-sided filter | 1960-1983 | 1.056 (0.110) | 0.247 (0.253) | 0.560 (0.137) | 0.425 (0.095) |
| Price gap | two-sided filter | 1984-2024 | 0.219 (0.164) | 0.288 (0.041) | 0.038 (0.092) | 0.203 (0.051) |

(CPI-U inflation. The GDP deflator, the error-correction form, the form with the two gaps apart and the quarterly versions are in `sources/s67_pstar.json`: 164 regressions.)

What it says:
- **In the rule's own form the response speed is not identified.** With a velocity trend that uses no future data, κ is −0.001 over 1970-2024 and its 95% interval runs from −0.10 to +0.10. Only the 1970s carry a response (0.88 in 1970-1983); since 1984 it is 0.04.
- **It depends on how trend velocity is drawn.** With a two-sided filter the two-sided slope is 0.19 and holds in both halves; but that trend uses the years after the one it explains. M2 velocity was near 1.8 from 1960 to 1990, rose to 2.1 by the late 1990s and fell to 1.2 in 2020: there is no fixed level for prices to return to.
- **The asymmetry the rule is built on is not in the data.** Above-against-below never differs by more than about one standard error in the price-gap form, and in the early sample the slope below is the larger one.
- **S58's own regression weakens with proper errors.** 0.445 has a Newey-West standard error of 0.240, so its 95% interval includes zero; and moving the start from 1960 to 1970 doubles it to 0.97.
- **Velocity and output gaps do not carry the same weight** (the form's restriction): entered apart over 1970-2024, the velocity gap's slope is 0.036 (0.021) and the output gap's 0.286 (0.151); the difference is 1.7 standard errors.
- **Persistence is the stable-looking number that is not stable:** 0.78-0.81 over the long samples, above 1 in 1960-1983, 0.46-0.52 since 1984. It is the number that sets the size of the waves (section 3).

By the preregistered rule, the price-gap reading of the engine takes κ = max(0, −0.001) = 0, and a rule whose prices never answer money is not run: the result is the finding. Decision test (a), fixed before the regression, asked for a 95% interval that excludes zero and the same sign in both halves. It fails on the first count.

## 5. High-inflation episodes (item 4)

An episode is at least three years in a row at 20% or more: 77 episodes in 52 countries, 518 country-years, median length 5 years, median inflation 42% a year (the programme's range). Logs throughout; standard errors clustered by country; "without" drops the 23 country-years above 1,000%.

| Question | Estimate | Without the years above 1,000% |
|---|---|---|
| Persistence: this year's inflation on last year's, pooled | 0.670 (0.041) | 0.636 (0.090) |
| … with episode effects (biased down in short panels) | 0.557 (0.069) | 0.453 (0.101) |
| … by last year's inflation: 20-50%, 50-100%, over 100% | 0.53 (0.16), 0.72 (0.41), 0.56 (0.06) | 0.53, 0.44, 0.43 |
| The rule's own form: persistence, and the response to the cumulative gap between money per unit of output and prices, pooled | 0.663 (0.036), κ 0.085 (0.053) | 0.640 (0.086), κ 0.047 (0.030) |
| … with episode effects | 0.544 (0.071), κ 0.178 (0.129) | 0.463 (0.099), κ 0.063 (0.055) |
| Inflation less growth of money per unit of output (velocity growth), mean of episodes, log a year | 0.060 (median 0.043) | 0.039 (median 0.037) |
| Share of episodes where inflation ran ahead of money | 67.5% | 66.7% |
| Cross-section: episode-mean inflation on episode-mean money per unit of output | slope 1.057 (0.071), constant 0.034 | slope 0.838 (0.074), constant 0.101 |
| Velocity's response to a change in inflation (years) | 0.004 (0.032) | 0.050 (0.077) |
| … in levels with episode effects | −0.048 (0.081) | 0.043 (0.171) |

What it says:
- **Inflation is persistent at these rates, a little less than in the US fit:** about two thirds of last year's inflation carries over (0.53 in the 20-50% band where the programme sits). Nothing here supports ρ 0.45 (φ 0.96).
- **Prices close the gap to money slowly:** κ between 0.05 and 0.18 a year and never distinguishable from zero. With those values the rule would leave most of the money unspent on prices for years (a rationed share above half of demand in the closed form), which is not what high-inflation economies look like. The simpler reading of the same numbers is that in these episodes money and prices move together within the year, which is what today's rule assumes, and that the cumulative gap carries little information.
- **Inflation ran ahead of money in two thirds of the episodes,** by 4 to 6 log points a year. Both cross-section fits put inflation at about 0.37 when money per unit of output grows 0.32 (the C2.2 design's rate): about 5 points a year more than either engine rule gives.
- **But velocity does not answer changes in inflation year by year** in these annual data (0.004 years). The rise in velocity is a drift over the episode, not a response the rule can key on. So the preregistered velocity response is run at its estimated value, which is nearly zero, and a second reading was added before the pilot for what the data do show (Amendment 1): a drift, in which the money-implied level grows 13.2% faster than the money (0.060 / 0.457).

Limits: annual data; the database has no consumer-price series for some well-known episodes (Argentina before 2018, for one); broad money definitions differ by country; episodes are selected on inflation itself, which biases persistence within them downward; money is treated as given, while in most of these episodes it accommodated inflation (Fischer, Sahay and Végh find causation running from inflation to money more often than not).

## 6. Three options of the capacity rule (item 5)

Claude's reading of what to build; each is a modelling assumption and off by default (`pr: {q: 1, bv: 0, bd: 0}` gives every output of `pr: true`).

- **Sub-steps within the year (`q`).** The year's new money arrives evenly over q sub-steps. In each, every sector's price moves by the rule, with κ, κ₂ and ρ counted per sub-step; wages are still indexed once a year (as in the engine), spread evenly over the sub-steps to stand for staggered contracts; expectations follow the general level's change in the last sub-step. Next year's prices are the level after the last sub-step. The households still shop at the year's opening prices: the engine's year is not split. So this option changes how fast prices follow money and how the shortage is counted, and reports how far prices rose during the year (`prAvg`); it does not change when households spend.
- **A velocity response (`bv`).** People hold less money when they expect inflation, so the money-implied price level rises by bv times expected inflation (last year's change in the general level). The formula of section 3 then has φ + κ × bv in place of φ. Above 1 the wave never dies out (a unit test holds this; it stays bounded, because the pull back after an overshoot is weak).
- **A velocity drift (`bd`, added by Amendment 1 before the pilot).** The money-implied level grows (1 + bd) times the money. This is the reading in which pass-through exceeds 1 under sustained money. Pass-through is always measured on the money itself.

Values (rules fixed in the preregistration, values recorded in Amendment 1 before the pilot):

| Reading | Values | From |
|---|---|---|
| Within-year, fitted quarterly (`wy`) | q 4; per quarter κ 0.0788, κ₂ 0, ρ 0.2333 | S58's regression form on quarterly data, 1960-2024: persistence 0.741 (0.072), slope above 0.079 (0.035), slope below −0.035 (0.030), floored at 0 |
| Within-year, same roots (`wyroot`) | q 4; α 0, ρ 0.9406, κ 0.0317, κ₂ 0.0036 | the quarterly rule whose roots are the fourth roots of the yearly main rule's |
| Today's rule in four sub-steps (`qt4`) | q 4; κ 1, α 0, ρ 0 | a check: same year-end prices as today's rule |
| Velocity response (`vel`, `velh`; `qtvel` on today's rule) | bv 0.0043, 0.0022 | section 5: 0.004 (0.032), not distinguishable from zero; run as preregistered |
| Velocity drift (`drift`; `qtdrift` on today's rule) | bd 0.132 | section 5: mean velocity growth 0.060 over mean growth of money per unit of output 0.457 |
| Price gap (`pg`) | not run | section 4: κ floors at zero |

Tests (7 added to `prUnitSuite`; 304 unit tests pass): the options off give S58's rule on every output; with no new money the no-programme run is identical under all three (so none draws a random number); four sub-steps with κ = 1 and no persistence give today's rule's year-end levels to 1e-12, with a smaller shortage; with the quarterly-fitted values steady inflation equals money growth and pass-through tends to 1; the same-roots quarterly rule obeys the yearly recursion to 1e-9; the velocity response raises pass-through, keeps steady inflation equal to money growth while stable and gives a standing wave when not; at the nesting point the drift gives pass-through of exactly 1 + bd. Guard test identical (25 rows × 20 seeds × 483 outputs, three environments); lineage linked; validate and domtest (153) pass.

## 7. The pilot (item 6)

Rows: the no-programme run under both rules; the release row and the C2.2 design under both rules (these six also ran in S58 and reproduce its published values exactly: 52,200 of 52,200 per-seed values in each environment); the C2.2 design under each reading above; the release row under `wy`, `vel` and `drift`. Paired seeds 1-100; exploratory; 95% paired-bootstrap intervals, not adjusted; of 712 estimates 660 exclude zero and 629 survive Holm at 5% (with 100 paired seeds almost any difference does). All cells are in `dev/runs/s67-price/tables.md`.

**Prices, C2.2 design (Reference; Adverse; Stress).**

| Rule | Inflation, points a year | Pass-through, year 19 | Wave, points | Demand no output could meet, % | Prices during the year over opening prices |
|---|---|---|---|---|---|
| Today's rule | 37.4; 44.0; 45.9 | 1.000 | 9.9; 6.2; 8.2 | 22.5; 26.3; 27.3 | not counted |
| Today's rule in four sub-steps | 37.4; 44.0; 45.9 | 1.000 | 9.9; 6.2; 8.2 | 1.9; 3.1; 3.5 | 1.126; 1.146; 1.153 |
| Capacity rule, main values | 38.2; 45.1; 47.1 | 1.019; 1.023; 1.026 | 39.1; 38.4; 41.9 | 11.3; 14.1; 15.0 | not counted |
| Within-year, fitted quarterly | 36.3; 42.2; 43.8 | 0.976; 0.968; 0.966 | 19.8; 12.0; 13.5 | 19.3; 23.0; 24.0 | 1.122; 1.141; 1.146 |
| Within-year, same roots (Reference) | 36.9 | 0.989 | 40.7 | 10.5 | 1.123 |
| Capacity + velocity response (Reference) | 38.2 | 1.019 | 39.3 | 11.3 | not counted |
| Capacity + velocity drift (Reference) | 44.2 | 1.154 | 46.4 | 13.2 | not counted |
| Today's rule + velocity drift | 43.4; 51.6; 54.0 | 1.132 | 10.9; 7.8; 10.7 | 25.8; 30.0; 31.1 | not counted |

The wave is the largest less the smallest yearly inflation in years 5-19. Today's rule scores 6 to 10 points on it with no wave at all, because the programme's money is itself uneven (it falls from 44% of income in year 4 to 32% in year 19 in Reference); the excess over that is 29 points for the capacity rule and 10 for the quarterly-fitted reading.

- **The waves (decision test b).** The quarterly-fitted wave is 0.51 of the yearly rule's in Reference (19.8 against 39.1; per seed the within-year wave exceeds half the yearly wave by 0.22 points, interval 0.15 to 0.30), 0.31 in Adverse and 0.32 in Stress. The preregistered test (Reference, at least half) is met by a hair. The release row's ratio is 0.40 (12.8 against 32.0). The same-roots reading reproduces the yearly wave (40.7 against 39.1), which confirms the formula inside the engine: a shorter step by itself changes nothing; different values do.
- **The quarterly-fitted rule is slow.** Its prices have closed only 60% of the way to the money after three years and leave 19% of demand unmet on average, against 11% for the yearly rule. Fitted where the data are (quarters with gaps of a few percent), it says prices take years to absorb money growth of 30-45% a year. The high-inflation episodes say they do not (section 5).
- **The shortage.** Today's rule in four sub-steps gives the same year-20 price level (to 8e-15) and the same results in every key, with 1.9% of demand unmet instead of 22.5%. The yearly count measured the length of the step. What replaces it is a price level that averages 12.6% above the opening level during the year (14.6-15.3% in Adverse and Stress). The engine's real incomes are counted at opening prices, so they overstate what the year's money buys by about that much under either count.
- **Velocity.** The response moves pass-through by 0.0001 (capacity rule) and 0.0002 (today's rule): reported and dropped (decision rule 3). The drift moves it by 0.135 and 0.132 and joins the readings S63 carries. Under today's rule it raises the programme's inflation by 5.9 points a year in Reference (7.6 in Adverse, 8.1 in Stress) and the year-20 price level from 420 to 939 times its start.

**The programme's effects, C2.2 design, Reference (programme minus no programme, points; 95% intervals in the tables).**

| Rule | Basket poverty | Cost of living | Wealth poverty, year 20 | Wealth poverty, average of 20 years | Median real wealth, year 20 | … average of 20 years |
|---|---|---|---|---|---|---|
| Today's rule | −24.64 | −28.24 | +0.66 | +2.67 | −$171,474 | −$111,997 |
| Capacity rule, main values | −24.61 | −28.22 | −1.79 | +3.58 | −$169,081 | −$112,306 |
| Within-year, fitted quarterly | −24.66 | −28.26 | +1.05 | +1.85 | −$171,757 | −$106,149 |
| Within-year, same roots | −24.64 | −28.24 | −0.74 | +2.48 | −$170,166 | −$107,607 |
| Capacity + velocity drift | −24.50 | −28.05 | +4.91 | +8.74 | −$175,005 | −$117,543 |
| Today's rule + velocity drift | −24.54 | −28.08 | +7.95 | +7.90 | −$177,006 | −$117,696 |

- **Basket poverty and the cost of living do not depend on the price rule** (every reading of the C2.2 design within 0.2 point of today's rule; 0.3 for the release row with the drift).
- **The year-20 wealth-poverty reading changes sign with the rule; the yearly average does not.** At year 20 the four rules without drift run from −1.79 to +1.05; averaged over the 20 years they run from +1.85 to +3.58, all above zero. The year-20 figure reads where the wave happens to be; the average reads the programme. The release row shows the same: +21.5, +20.4 and +20.9 at year 20; +12.0, +13.0 and +10.7 on average.
- **Pass-through above 1 matters more than the choice between the two rules.** The drift adds 5 to 7 points to the wealth-poverty effect and takes $5,500 to $5,900 more off median real wealth, under either rule. The two rules differ from each other by about 1 point on the yearly average.
- **Shadow prices.** At prices that would clear demand, the C2.2 design's effect on wealth poverty under today's rule is +11.7 points on the yearly count of the shortage and +1.2 on the quarterly count. S58 reported the first as if it measured the economy; it measures the step.

Adverse and Stress are in the tables. The pattern is the same at higher levels: without the drift the C2.2 design's wealth-poverty effect is +27.7 to +41.7 points at year 20 and +12.8 to +21.1 as a yearly average; with the drift +37.9 to +48.4 and +21.1 to +27.4.

## 8. Limits

- Two of the papers the step named could not be opened (section 1); the forms come from papers that restate them, and no figure of the originals is used.
- The US regressions have 55 to 65 yearly observations and M2 velocity with no stable level; any price-gap estimate depends on how its trend is drawn. The result "not identified" is about this rule and these data, not a claim that money does not move prices.
- The high-inflation panel is annual, selected on inflation, with gaps in coverage; money is treated as given.
- The within-year option does not split the engine's year: households still shop at opening prices. It answers how prices follow money, not how households would respond to prices rising during the year.
- The velocity drift is a ratio of two means over episodes that differ widely (0.132 with every year, 0.101 without the years above 1,000%; the cross-section slope is 1.06 and 0.84). It is a reading to carry, not a main value.
- The wave measure counts the unevenness of the money as well as the rule's cycle; the excess over today's rule is given beside it.
- Pilot: 100 seeds, 500 adults; nothing at 500 seeds before S63's freeze.

## 9. The recommendation for S63's main-row decision, with both views

**The view fixed in S58's preregistration: the capacity rule as the main row,** today's rule beside it. Its reasons: every parameter of the capacity rule is sourced or derived, against today's single placeholder; it has what two outside reviews asked for (capacity, slack, wage costs, expectations); and the choice was fixed before any result so that results could not enter it.

**The audit's view: today's rule as the main row,** the capacity rule beside it, every wealth outcome as a yearly average under both. Its reasons: the two rules give the same long-run answer by construction; the capacity rule adds a cycle that is a property of its yearly lag structure and of parameters that are not stable; its response speed was not estimated on the variable it is applied to; one line explains today's rule.

**What this step found, for each reason.**
- "Every parameter is sourced or derived": the derivation does not hold. In the rule's own form the response speed is zero within error and changes from 0.88 to 0.04 between halves of the sample; S58's own estimate does not exclude zero once its errors allow for serial correlation; the high-inflation episodes give a third set of values. The capacity rule's numbers are no better founded than today's placeholder.
- "Capacity, slack, costs, expectations": the pieces are reasonable, and inflation is persistent in every data set here (0.5 to 0.9). But the size of the wave they produce runs from 5 to 68 points across defensible values of one number, and the data do not choose among them.
- "The cycle is a property of the yearly lag": not quite. A shorter step alone leaves the wave unchanged; values fitted at the shorter step halve it (to 0.51 in Reference, 0.31-0.32 in Adverse and Stress). The cycle is a property of the values.
- "Same long-run answer": yes, by assumption in both, and now said so. The episodes suggest both rules understate inflation by about 5 points a year at the programme's money growth.
- New: the shortage S58 reported under today's rule (22.5% of demand) is the yearly step; in quarters it is 1.9%, with prices 12.6% above opening levels during the year instead.

**Claude's recommendation, by the rule fixed before the results** (preregistration, decision rule 2: the capacity rule only if its response speed is identified in its own form *and* its waves survive a shorter step; the first fails): **today's rule as the main row.** Beside it, as labelled readings: the capacity rule at S58's main values; the quarterly-fitted within-year reading; and today's rule with the velocity drift. Every wealth outcome at year 20, at year 40 and as a yearly average, under each. S70's screening decides which of S58's sweep (κ, ρ, α, slack, κ₂) the 500-seed batch still needs; from this step, ρ (persistence) is the one that matters and κ₂ and the velocity response can be dropped.

This reverses the recommendation fixed in S58's preregistration, for reasons of identification and form; no poverty or wealth result entered the rule. The decision is S63's to file, with both views as written here.

## 10. What later steps must carry

- **S63:** the decision above, both views in its text. Wealth poverty and median real wealth as yearly averages beside years 20 and 40 on every row (keys `ppov_*`, `pmedW_*`; the average is made by the table tool, as `dev/tools/s67_table.py` does). The velocity drift as a reading on the main row. The shortage and shadow-price readings dropped from the headline rows, or given on the quarterly count (`pr: {q: 4, k: 1, a: 0, r: 0, h: 0, rs: false}`) with the within-year price level (`prAvg`) beside them, with the sentence that the engine's real incomes are counted at opening prices.
- **S68:** the closed form of section 3 in MODEL_SPEC; the three options and `prAvg` in the plain-names table; the pairwise tests should include `q` with `rt` and `lf`.
- **S70:** the screening varies persistence (ρ from 0 to 0.45), κ and the drift (0 to 0.132) together; κ₂ and bv can be left out (no effect here).
- **Hub wording (S25, S40):** the replacement sentence in the S58 report's correction note. Any sentence about a shortage or rationing under the programme should be checked against section 7.
- **For an economist reviewer (ECONOMIST-REVIEW.md, row 7):** the open question is no longer which of the two rules, but pass-through: whether sustained money growth of 30-45% a year would raise prices one for one or faster. The episodes say somewhat faster.
