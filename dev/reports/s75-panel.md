# US policy eras and their stability: the descriptive panel

> **Note (Nov 28, 2026).** The results repository named in this document, `BetterToBest/compassionism-sim-results`, is offline: GitHub disabled it. Every figure can be reproduced from the engine commit named beside it, with the commands in `REPRODUCE.md`. The results folders are deposited in an archive with a permanent identifier, DOI 10.5281/zenodo.24615619 (copied on OSF at osf.io/7v5ur); folders not in the archive are listed in `data/results-manifest.json`.

Nov 16, 2026. The first part of the policy-eras study: published data only, no engine. Preregistration: research-update `prereg/2026-11-s75-deep-history.md` (committed before any figure here was computed), with Amendment 1 (written after the files were downloaded and before any figure was computed). Script: `sources/s75_eras.py`, from the files in `sources/s75_eras/raw/`, `sources/s74_history/raw/` and `sources/s59_shiller/`. Output: `sources/s75_eras.json`. Every cell: `dev/runs/s75-panel/tables.md`. Results copy: compassionism-sim-results `s75-panel-<commit>`. The engine readings (part 2) and the full report come next.

The eras were fixed before any figure: 1947-1972, 1973-1983, 1984-2007 and 2008-2025, with 1913-1946 as a reading only. The central-bank study's window, 2005-2025, is shown beside them. "Less stable" or "more stable" is said only where the difference between two eras passes the preregistered test: a block-bootstrap interval, with Holm's correction across the 14 measures compared for each pair of eras. Eras are short (11 to 26 years), so most differences do not pass.

## In short
- **On no measure was 2005-2025 clearly less stable than all three earlier postwar eras.** That was the preregistered test of Duke's view that 2005-2025 was less stable than the decades before it. On 5 of the 14 measures the record goes against it: 2005-2025 was steadier than 1973-1983 on inflation and on food, shelter and medical prices, and medical prices rose more slowly than in 1984-2007 too. On the other 9, no comparison passes the test either way (the preregistered label for this is "mixed").
- **Three measures lean Duke's way but do not pass the test.** Unemployment swung more from year to year in 2005-2025 (standard deviation 2.0 points) than in 1947-1972 (1.1) or 1984-2007 (1.0). Real home prices swung more (6.3 points a year) than in 1947-1972 (3.0). Food prices swung more (3.3) than in 1984-2007 (1.7). Each of these intervals excludes zero before the correction, but none does after it. Growth per person was also lower (1.4% a year against 2.5% in 1947-1972 and 2.2% in 1984-2007), again without passing the test.
- **1973-1983 was the unstable era.** Against both 1947-1972 and 1984-2007 it had higher inflation (8.3% a year), higher food, shelter and medical inflation, and higher unemployment. Against 1984-2007 its prices also swung more. Each of these passes the test.
- **Distribution moved the other way from stability.** The top 1%'s share of pre-tax income fell in 1947-1972 (14.9% to 11.0%), was flat in 1973-1983, rose in 1984-2007 (12.2% to 18.4%), and stayed high after (19.1% in 2019). Its share of wealth followed the same path (29.8% in 1947, 24.0% in 1983, 34.9% in 2019).
- **Tax rates actually paid were far more progressive in the 1950s.** In Piketty, Saez and Zucman's accounts, the top 0.1% paid 57.3% of pre-tax income in all taxes over 1950-1959, the top 1% 45.5%, and the bottom half about 20%. By 2008-2019 the top 0.1% paid 34.8%, the top 1% 32.9%, and the bottom half 25.2%. The 91-92% top statutory rate of the 1950s applied to few incomes; these are the rates actually paid.
- **How the central bank set its rate changed between eras.** In a simple fitted rule, the rate rose 0.45-0.65 points per point of inflation in 1947-1972 and 1973-1983 (less than one for one, which would lower the real rate as inflation rose), 1.3 points in 1984-2007, and not at all in 2008-2025, when the rate sat at zero for years and then rose late in 2022. These are descriptive fits, not the rules the Federal Reserve followed.

## Stability by era (yearly figures; the tables hold every cell)

| | 1947-1972 | 1973-1983 | 1984-2007 | 2008-2025 | 2005-2025 | 1913-1946 (reading) |
|---|---|---|---|---|---|---|
| Inflation (CPI-U), mean / spread | 2.7 / 2.4 | 8.3 / 3.4 | 3.1 / 1.2 | 2.5 / 1.8 | 2.6 / 1.7 | 2.6 / 7.6 |
| Worst inflation year | 8.8 (1947) | 13.3 (1979) | 6.1 (1990) | 7.0 (2021) | 7.0 (2021) | 20.4 (1918) |
| Food, mean / spread | 1.9 / 3.3 | 8.0 / 6.5 | 3.1 / 1.7 | 2.5 / 3.5 | 2.6 / 3.3 | |
| Shelter, mean / spread (from 1954) | 3.1 / 2.5 | 9.1 / 4.6 | 3.7 / 1.0 | 3.1 / 1.8 | 3.1 / 1.7 | |
| Medical care, mean / spread | 4.1 / 1.7 | 9.6 / 2.2 | 5.3 / 1.8 | 2.8 / 1.0 | 3.0 / 1.1 | |
| Unemployment, mean / spread (from 1948) | 4.8 / 1.1 | 7.3 / 1.6 | 5.7 / 1.0 | 5.9 / 2.1 | 5.7 / 2.0 | 8.8 / 7.2 |
| Months in recession | 16% | 29% | 6% | 9% | 8% | 34% |
| Growth per person, mean / spread | 2.5 / 3.1 | 1.7 / 3.2 | 2.2 / 1.4 | 1.3 / 1.9 | 1.4 / 1.7 | 2.5 / 8.2 |
| Real share prices: spread of the yearly change | 15.3 | 18.8 | 14.3 | 17.0 | 15.8 | 23.7 |
| Real share prices: largest fall (months to regain the peak) | 35% (258) | 60% (61) | 47% (141) | 46% (48) | 52% (56) | 81% (317) |
| Real home prices: spread of the yearly change | 3.0 | 4.2 | 4.9 | 6.0 | 6.3 | 7.3 |
| Real home prices: largest fall (years to regain the peak) | 9% (10) | 11% (4) | 13% (4) | 18% (4) | 35% (10) | 32% (25) |

Spread is the standard deviation of the yearly values, in points. Price changes are December over December. Drawdowns count only falls whose peak and trough are both inside the era. That is why 2008-2025's home price fall (18%, from its 2008 level) is smaller than 2005-2025's (35%, from the 2005 peak).

## Was 2005-2025 less stable than the decades before it? (decision rule, per measure)

| measure | vs 1947-1972 | vs 1973-1983 | vs 1984-2007 | reading |
|---|---|---|---|---|
| Inflation, mean | no clear difference | more stable | no clear difference | against it |
| Inflation, spread | no clear difference | no clear difference | no clear difference | mixed |
| Food prices, mean | no clear difference | more stable | no clear difference | against it |
| Food prices, spread | no clear difference | no clear difference | no clear difference (unadjusted: less stable; Holm p 0.052) | mixed |
| Shelter prices, mean | no clear difference | more stable | no clear difference | against it |
| Shelter prices, spread | no clear difference | more stable | no clear difference | against it |
| Medical prices, mean | no clear difference | more stable | more stable | against it |
| Medical prices, spread | no clear difference | no clear difference | no clear difference | mixed |
| Unemployment, mean | no clear difference | no clear difference | no clear difference | mixed |
| Unemployment, spread | no clear difference (unadjusted: less stable) | no clear difference | no clear difference (unadjusted: less stable) | mixed |
| Growth, mean | no clear difference | no clear difference | no clear difference | mixed |
| Growth, spread | no clear difference (unadjusted: more stable) | no clear difference | no clear difference | mixed |
| Share prices, spread | no clear difference | no clear difference | no clear difference | mixed |
| Home prices, spread | no clear difference (unadjusted: less stable) | no clear difference | no clear difference | mixed |

The tally: supported on 0 measures, against it on 5, mixed on 9. 2008-2025 alone gives the same picture, and it was also steadier than 1947-1972 on medical prices (see the tables). "Unadjusted" marks where the 95% interval excludes zero before Holm's correction. Those differences are worth noting but did not pass the preregistered test.

## Policy settings and distribution by era

| | 1947-1972 | 1973-1983 | 1984-2007 | 2008-2025 |
|---|---|---|---|---|
| Top 1% share of pre-tax income: start to end | 14.9 to 11.0 | 10.8 to 11.5 | 12.2 to 18.4 | 17.9 to 19.1 (2019) |
| Top 10% share of pre-tax income: start to end | 36.5 to 34.4 | 34.3 to 35.3 | 36.5 to 44.0 | 43.6 to 45.7 (2019) |
| Top 1% share of wealth: start to end | 29.8 to 26.2 | 25.3 to 24.0 | 24.2 to 33.3 | 33.9 to 34.9 (2019) |
| Bottom half's share of wealth: start to end | 1.3 to 1.1 (from 1962) | 1.0 to 1.8 | 1.4 to -0.4 | -1.2 to 0.2 (2019) |
| SCF+ (survey data): top 10% share of wealth, first to last survey year | 72.3 (1950) to 70.7 (1971) | 64.1 (1977) to 66.5 (1983) | 67.6 (1989) to 71.5 (2007) | 74.6 (2010) to 77.4 (2016) |
| SCF+: bottom half's share of wealth | 3.0 to 3.0 (mean 3.6) | 4.0 to 3.9 | 2.9 to 2.5 | 1.2 to 1.2 |
| SCF+: wealth Gini (x100) | 81 to 80 | 76 to 78 | 79 to 82 | 85 to 86 |
| Average tax rate, all taxes (era mean): bottom 50% | 21.6 | 25.4 | 28.0 | 25.2 (to 2019) |
| middle 40% | 26.1 (from 1962) | 30.3 | 30.7 | 28.4 |
| top 1% | 44.3 | 39.0 | 34.7 | 32.9 |
| top 0.1% | 54.9 | 44.1 | 37.3 | 34.8 |
| Top statutory income tax rate (era mean; context only) | 83.5 | 65.6 | 39.1 | 37.3 (to 2018) |
| Official poverty rate: start to end | 22.4 (1959) to 11.9 | 11.1 to 15.2 | 14.4 to 12.5 | 13.2 to 10.2 |
| Anchored SPM poverty: start to end | 25.8 (1967) to 20.4 | 19.1 to 21.4 | 20.5 to 14.8 | 14.6 to 10.1 (2024) |
| Health spending, % of GDP: start to end | 5.0 (1960) to 7.2 | 7.2 to 10.0 | 10.0 to 15.9 | 16.3 to 18.0 (2024) |
| Real health spending per person, yearly growth | 6.3 (from 1961) | 3.8 | 3.7 | 1.7 |
| Out-of-pocket share of health spending: start to end | 47.1 (1960) to 30.1 | 29.9 to 20.5 | 20.5 to 12.8 | 12.5 to 10.5 |
| Medical prices' yearly rise above CPI-U (mean) | 1.7 | 1.3 | 2.3 | 0.3 |

Poverty fell in three of the four eras and rose in 1973-1983. Health spending's share of GDP rose in every era, most in points in 1984-2007. The share households paid out of pocket fell in every era. The household survey data (SCF+, Kuhn, Schularick and Steins) tell the same story as PSZ's accounts in direction: wealth was least concentrated around 1977 (top 10% 64.1%, Gini 76) and most concentrated in 2016 (77.4%, Gini 86). The bottom half's share stayed between 2.5% and 4.2% from 1950 to 2007, then fell to 1.1-1.2% after the 2008 crisis. (PSZ's levels for the bottom half are lower, around 1%, and the two sources measure wealth differently; each is shown as published.)

## Who owned the hospitals

Supplied by Duke after the first version of this note (prereg Amendments 2 and 3): the Historical Statistics of the United States (all hospitals, 1946-1993), Health, United States 2017 (community hospitals, 1975-2015), and the Social Security Bulletin of November 1973 (private community hospitals, 1961-1971). They measure different things and are not joined.

| all US hospitals (HSUS) | 1946 | 1947-1972: first to last | 1973-1983 | 1984-1993 |
|---|---|---|---|---|
| for-profit share of hospitals | 21.2% | 21.0% to 12.0% | 12.4% to 13.8% | 14.6% to 17.1% |
| for-profit share of beds | 3.7% | 3.6% to 4.2% | 4.8% to 8.2% | 8.9% to 11.3% |
| non-profit share of beds | 23.3% | 24.4% to 41.3% | 42.5% to 54.7% | 55.1% to 57.4% |
| government share of beds | 73.0% | 71.9% to 54.5% | 52.7% to 37.1% | 36.0% to 31.3% |

| community hospitals: share of admissions (Health, United States 2017) | 1975 | 1980 | 1990 | 2000 | 2010 | 2015 |
|---|---|---|---|---|---|---|
| non-profit | 70.9% | 70.7% | 73.4% | 73.9% | 72.6% | 71.8% |
| for-profit | 7.9% | 8.8% | 9.8% | 12.5% | 14.0% | 15.6% |
| state and local government | 21.1% | 20.5% | 16.8% | 13.6% | 13.4% | 12.6% |

- **For-profit hospitals were common before 1973, but small.** In 1946-1950 about one US hospital in five was proprietary, but these were small: they held under 4% of beds. Their share of hospitals fell through the 1950s and 1960s (to 12% in 1972), as many small proprietary hospitals closed.
- **For-profit care grew after 1973.** The for-profit share of beds roughly doubled in 1973-1983 (4.8% to 8.2%) and kept rising (11.3% in 1993). The for-profit share of community hospital admissions doubled from 7.9% in 1975 to 15.6% in 2015. The rise follows the HMO Act (1973), but the panel does not test what caused it.
- **Non-profits carry most hospital care throughout.** They held about 71-74% of community hospital admissions in every year shown, 1975-2015. Their share of all beds rose from 23% (1946) to 57% (1993), mostly because government beds fell (from 73% to 31%; state hospitals alone held 711,000 beds in 1953 and 558,000 in 1970).
- **For-profit hospitals earned more on each dollar, before Medicare and after.** Among private community hospitals in 1961-1971, net income was 4.3-8.4% of revenue for for-profit hospitals and -0.1-3.7% for non-profits. The for-profit share of their revenue stayed between 6.5% and 7.7%. (The source estimated 1968's split from 1969's.)

## The central bank's rule as estimated in each era

| fit | how much the rate rose per point of inflation (phi) | per point of output gap (beta) | quarters |
|---|---|---|---|
| 1947-1972 | 0.45 (se 0.25) | 0.08 (0.11) | 1949Q1-1972Q4 |
| 1947-1972, after the 1951 Accord | 0.55 (0.28) | 0.10 (0.11) | 1951Q2-1972Q4 |
| 1973-1983 | 0.65 (0.20) | -0.18 (0.24) | 1973Q1-1983Q4 |
| 1984-2007 | 1.30 (0.29) | 0.48 (0.23) | 1984Q1-2007Q4 |
| 2008-2025 (shadow rate at the floor) | -0.05 (0.21) | 0.67 (0.25) | 2008Q1-2025Q3 |
| 2008-2025 (effective rate) | -0.05 (0.16) | 0.57 (0.19) | 2008Q1-2025Q3 |

Each row is a regression of the quarterly policy rate on CPI-U's change over four quarters and CBO's output gap (Newey-West standard errors). Before 1984 the fitted response to inflation is below one for one, the pattern Clarida, Galí and Gertler (2000) describe for the pre-Volcker years; it is shown here as found, not from their paper. After 2008 the rate did not follow inflation within the era: it sat at the floor through low inflation and rose only in 2022, after inflation had already climbed. The smoothed version (in the tables) puts heavy weight on last quarter's rate (0.91-0.96) in every era. Part 2 uses these fits as each era's rule in the engine.

## Checks
- **The planning figures for tax rates do not match the opened file.** The planning text gave about 42% (top 1%) and 50.6% (top 0.1%) in the 1950s, against 36.4% and 39.8% in 2014. PSZ's 2022 appendix gives 45.5% and 57.3% (1950-1959 mean), and 33.9% and 36.4% in 2014. The direction and the conclusion are the same: the top paid much more of its income in tax in the 1950s. The file's figures are used. Where the planning figures came from is not known; they may come from an earlier vintage of the accounts.
- CPI-U NSA against the central-bank study's seasonally adjusted series, 2005-2025: mean 2.58 against 2.57, spread 1.69 against 1.72.
- The home price link: Shiller's series and Case-Shiller over CPI-U agree to 0.01 point a year over 2015-2022, so the splice after January 2023 is seamless.
- Jordà, Schularick and Taylor's real returns: each era's mean yearly real change is within 0.5 point of Shiller's for 1913-2007 (homes and shares), though homes in 1913-1946 differ in sign (0.4% against -0.1%). The gaps are larger in 2008-2025 (homes 1.3% against 0.7%, shares 7.9% against 6.0%), where JST ends in 2020.

## Gaps
- **Hospital ownership** comes from the three sources above, supplied by Duke (cdc.gov, ssa.gov and the Historical Statistics' site refuse this machine). The Historical Statistics' ownership split ends in 1993, and Health, United States gives only selected years from 1975. In one Historical Statistics row (1957, beds), the stated total is 30,000 above the sum of the ownership groups. Shares use the sum, and the row is flagged. 1957 enters only the 1947-1972 mean.
- **The Historical SCF (SCF+)** comes from the 2018 working paper's appendix tables (survey years 1950-2016), not the later published dataset.
- PSZ's series end in 2019, so 2008-2025's distribution and tax figures cover 2008-2019. The 2025 unemployment rate uses the 11 months the file holds (October 2025 is missing); the rule's fit ends in 2025Q3 for the same reason.

## Limits
- The panel describes; it does not attribute. Each era differs in many ways at once: the US's postwar position, union membership, demography, fixed exchange rates to 1971, wars, the size of government, the rules of finance. None of the comparisons above says which policy caused which outcome.
- A block bootstrap on 11-26 yearly values gives wide intervals, and it understates spreads a little in short samples. "No clear difference" is often the honest reading.
- The model does not represent war, military spending or corruption, and no figure here is claimed about them.

## Next
The engine readings: today's households under each era's measured settings (the era's macro path, its fitted rule, its tax rates by group, its medical cost growth), without and with the programme, both designs, 100 seeds. Amendment 2 fixes the build's mechanics before any engine run. Then the full report, and a separate Hub page for the findings (Duke's instruction, Nov 16), linked from the simulation and wiki pages once complete.
