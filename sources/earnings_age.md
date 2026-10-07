# US earnings by age (input for the v5.3 life-cycle earnings reading, plan item B7)

Source: U.S. Bureau of Labor Statistics, Current Population Survey, *Usual Weekly Earnings of Wage and Salary Workers*, Table 3, "Median usual weekly earnings of full-time wage and salary workers by age, race, Hispanic or Latino ethnicity, and sex", second quarter 2026, not seasonally adjusted (https://www.bls.gov/news.release/wkyeng.t03.htm, read Oct 7, 2026; bls.gov refuses scripted downloads from the build environment, so the table was read through a web reader). Both sexes, all races, full-time wage and salary workers.

| Age | 16-19 | 20-24 | 25-34 | 35-44 | 45-54 | 55-64 | 65 and over |
|---|---|---|---|---|---|---|---|
| Median weekly earnings | $678 | $831 | $1,160 | $1,436 | $1,421 | $1,367 | $1,233 |

How v5.3 uses them (`AGE.earn 'cps'`, `CFG.EARN_AGE`): as the shape of earnings over a working life, not their level. Each band's median is placed at the band's middle age (20-24 at 22, 25-34 at 29.5, 35-44 at 39.5, 45-54 at 49.5, 55-64 at 59.5; 65 and over at 67.5, the middle of 65-69, a modelling assumption since the band is open), and earnings at other ages are read off straight lines between those points. Each adult's wage is multiplied by the curve at their age over the curve's average across the population aged 25-66 (`CFG.AGE_WEIGHTS`), so the average wage is unchanged and only who earns what by age changes. A quarter's medians, not an annual average: the shape, which is all the model uses, moves little between quarters.
