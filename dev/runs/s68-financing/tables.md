# S68 pilot: the financing identity and costs at the within-year price level (tables)

Seeds 1-N per environment as in each file; 500 adults, 20 years; the frozen row (today's safety net, CPS earnings), round-2 switches off. Paired differences with 95% intervals, unadjusted. Money in year-0 dollars per adult-year; inflation `endoAnn` in % a year; poverty in % (basket: adult-years below the cost of living; wealth: adults below the line at year 20, all-cash wealth).

## Reference (seeds 1-100; engine e03aa73)

### (A) Who pays the programme

| Row | Payout | Contribution raised | New money | Matched output | Unpaid (before fx.fin) | Unpaid, % of payout | Mean rate | Years at the cap (of 20) | Inflation | Basket poverty | Wealth poverty | Hours |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 0 | 0 | 0 | 0 | 0 | 0.00 | 0.0% | 0.0 | 0.00 | 26.8 | 21.9 | -1.4% |
| rel source | 32639 | 1227 | 28710 | 2698 | 10 | 0.03 | 1.5% | 0.0 | 31.52 | 10.1 | 43.4 | -5.3% |
| c22 source | 60401 | 1219 | 40123 | 19056 | 10 | 0.02 | 1.5% | 0.0 | 37.44 | 2.2 | 22.6 | 1.1% |
| c22 tax report | 79601 | 49284 | 0 | 0 | 30317 | 38.07 | 83.7% | 17.0 | 0.08 | 9.8 | 6.7 | -20.6% |
| c22 tax money | 67036 | 46877 | 20158 | 0 | 20158 | 0.00 | 83.6% | 17.0 | 21.42 | 13.8 | 58.6 | -25.8% |
| c22 hybrid report | 66469 | 19500 | 25429 | 21949 | 2378 | 3.58 | 25.3% | 0.0 | 22.36 | 3.7 | 16.0 | -1.5% |
| c22 hybrid money | 65960 | 19605 | 26539 | 21752 | 1540 | 0.00 | 25.5% | 0.0 | 23.71 | 3.6 | 16.5 | -1.6% |
| rel tax report | 39108 | 38109 | 0 | 0 | 2250 | 5.76 | 50.0% | 0.0 | 0.04 | 24.9 | 19.5 | -15.3% |
| rel tax money | 37745 | 36770 | 1925 | 0 | 1925 | 0.00 | 48.6% | 0.0 | 2.27 | 25.4 | 22.3 | -15.0% |

Against the no-programme run (paired):

| Row | Basket poverty | Wealth poverty | Hours, % |
|---|---|---|---|
| rel source | -16.7 (-17.0 to -16.4) | 21.5 (21.0 to 22.1) | -3.9 (-4.0 to -3.8) |
| c22 source | -24.6 (-25.0 to -24.3) | 0.7 (0.2 to 1.1) | 2.5 (2.0 to 2.9) |
| c22 tax report | -17.1 (-17.4 to -16.7) | -15.2 (-15.6 to -14.9) | -19.2 (-19.9 to -18.5) |
| c22 tax money | -13.0 (-13.3 to -12.7) | 36.7 (35.6 to 37.7) | -24.4 (-25.0 to -23.9) |
| c22 hybrid report | -23.2 (-23.5 to -22.9) | -5.9 (-6.3 to -5.5) | -0.1 (-0.5 to 0.3) |
| c22 hybrid money | -23.2 (-23.5 to -22.9) | -5.4 (-5.8 to -4.9) | -0.3 (-0.7 to 0.2) |
| rel tax report | -2.0 (-2.4 to -1.6) | -2.4 (-2.7 to -2.0) | -13.9 (-14.2 to -13.7) |
| rel tax money | -1.4 (-1.8 to -1.0) | 0.4 (0.0 to 0.7) | -13.6 (-13.9 to -13.4) |

The gap as new money against the gap unpaid (fx.fin 'money' less 'report', paired):

| Design and reading | Inflation, points a year | Basket poverty | Wealth poverty |
|---|---|---|---|
| C2.2, flat contribution | 21.33 (20.98 to 21.68) | 4.0 (3.8 to 4.2) | 51.9 (50.8 to 53.0) |
| C2.2, hybrid | 1.35 (1.33 to 1.36) | -0.1 (-0.1 to -0.0) | 0.5 (0.4 to 0.6) |
| Release design, flat contribution | 2.23 (2.21 to 2.25) | 0.6 (0.5 to 0.6) | 2.7 (2.5 to 2.9) |

### (B) Costs at the within-year price level (quarterly count of today's rule)

| Row | Within-year level over opening | Basket poverty, published | At within-year prices | Depth (FGT1), published | At within-year prices |
|---|---|---|---|---|---|
| none q4 | 1.0000 | 26.8 | 26.8 | 8.98 | 8.98 |
| rel q4 | 1.1079 | 10.1 | 12.3 | 2.18 | 2.72 |
| c22 q4 | 1.1256 | 2.2 | 2.9 | 0.29 | 0.39 |

The programme's effect on basket poverty (against the no-programme run, paired), published and at within-year prices, and how far the reading moves it:

| Design | Effect, published | Effect at within-year prices | Moved by |
|---|---|---|---|
| Release design | -16.7 (-17.0 to -16.4) | -14.5 (-14.8 to -14.2) | 2.2 (2.1 to 2.3) |
| C2.2 (Source) | -24.6 (-25.0 to -24.3) | -23.9 (-24.2 to -23.6) | 0.7 (0.7 to 0.7) |

## Adverse (seeds 1-100; engine e03aa73)

### (A) Who pays the programme

| Row | Payout | Contribution raised | New money | Matched output | Unpaid (before fx.fin) | Unpaid, % of payout | Mean rate | Years at the cap (of 20) | Inflation | Basket poverty | Wealth poverty | Hours |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 0 | 0 | 0 | 0 | 0 | 0.00 | 0.0% | 0.0 | 0.00 | 38.3 | 31.9 | -1.9% |
| rel source | 31227 | 1202 | 27588 | 2404 | 34 | 0.11 | 1.9% | 0.0 | 37.59 | 15.8 | 76.9 | -7.3% |
| c22 source | 57535 | 1194 | 39194 | 17115 | 33 | 0.06 | 1.9% | 0.0 | 43.98 | 3.1 | 62.0 | -1.5% |
| c22 tax report | 77959 | 37904 | 0 | 0 | 40055 | 51.38 | 83.8% | 17.0 | 0.11 | 10.3 | 9.0 | -21.5% |
| c22 tax money | 60676 | 35729 | 24947 | 0 | 24947 | 0.00 | 83.7% | 17.0 | 33.24 | 20.7 | 93.2 | -29.2% |
| c22 hybrid report | 63547 | 19173 | 23942 | 20353 | 2386 | 3.76 | 32.6% | 0.0 | 25.88 | 5.2 | 50.3 | -5.3% |
| c22 hybrid money | 63039 | 19258 | 25050 | 20236 | 1612 | 0.00 | 32.8% | 0.0 | 27.43 | 5.0 | 51.7 | -5.4% |
| rel tax report | 27415 | 26742 | 0 | 0 | 1897 | 6.92 | 43.9% | 0.0 | 0.00 | 41.6 | 32.4 | -15.0% |
| rel tax money | 34069 | 32322 | 2555 | 0 | 2555 | 0.00 | 59.4% | 1.4 | 3.43 | 48.0 | 43.0 | -21.4% |

Against the no-programme run (paired):

| Row | Basket poverty | Wealth poverty | Hours, % |
|---|---|---|---|
| rel source | -22.6 (-23.0 to -22.2) | 45.0 (44.4 to 45.6) | -5.3 (-5.4 to -5.2) |
| c22 source | -35.3 (-35.7 to -34.8) | 30.2 (29.5 to 30.9) | 0.5 (-0.2 to 1.2) |
| c22 tax report | -28.0 (-28.4 to -27.5) | -22.9 (-23.3 to -22.5) | -19.6 (-20.7 to -18.4) |
| c22 tax money | -17.6 (-18.0 to -17.2) | 61.3 (60.9 to 61.8) | -27.2 (-28.1 to -26.3) |
| c22 hybrid report | -33.1 (-33.5 to -32.7) | 18.4 (17.5 to 19.3) | -3.3 (-3.9 to -2.7) |
| c22 hybrid money | -33.3 (-33.7 to -32.9) | 19.9 (18.9 to 20.8) | -3.4 (-4.2 to -2.7) |
| rel tax report | 3.3 (2.8 to 3.7) | 0.5 (0.1 to 0.9) | -13.0 (-13.3 to -12.8) |
| rel tax money | 9.7 (8.7 to 10.7) | 11.2 (10.1 to 12.2) | -19.4 (-20.2 to -18.6) |

The gap as new money against the gap unpaid (fx.fin 'money' less 'report', paired):

| Design and reading | Inflation, points a year | Basket poverty | Wealth poverty |
|---|---|---|---|
| C2.2, flat contribution | 33.13 (32.63 to 33.64) | 10.3 (10.0 to 10.7) | 84.3 (83.8 to 84.8) |
| C2.2, hybrid | 1.55 (1.52 to 1.57) | -0.2 (-0.2 to -0.2) | 1.4 (1.2 to 1.7) |
| Release design, flat contribution | 3.43 (3.16 to 3.70) | 6.4 (5.8 to 7.1) | 10.6 (9.7 to 11.6) |

### (B) Costs at the within-year price level (quarterly count of today's rule)

| Row | Within-year level over opening | Basket poverty, published | At within-year prices | Depth (FGT1), published | At within-year prices |
|---|---|---|---|---|---|
| none q4 | 1.0000 | 38.3 | 38.3 | 14.02 | 14.02 |
| rel q4 | 1.1281 | 15.8 | 19.5 | 3.53 | 4.48 |
| c22 q4 | 1.1465 | 3.1 | 4.2 | 0.40 | 0.55 |

The programme's effect on basket poverty (against the no-programme run, paired), published and at within-year prices, and how far the reading moves it:

| Design | Effect, published | Effect at within-year prices | Moved by |
|---|---|---|---|
| Release design | -22.6 (-23.0 to -22.2) | -18.8 (-19.2 to -18.4) | 3.7 (3.6 to 3.8) |
| C2.2 (Source) | -35.3 (-35.7 to -34.8) | -34.2 (-34.6 to -33.7) | 1.1 (1.0 to 1.1) |

## Stress (seeds 1-100; engine e03aa73)

### (A) Who pays the programme

| Row | Payout | Contribution raised | New money | Matched output | Unpaid (before fx.fin) | Unpaid, % of payout | Mean rate | Years at the cap (of 20) | Inflation | Basket poverty | Wealth poverty | Hours |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 0 | 0 | 0 | 0 | 0 | 0.00 | 0.0% | 0.0 | 0.00 | 38.3 | 31.9 | -1.9% |
| rel source | 12247 | 601 | 11326 | 299 | 23 | 0.18 | 0.9% | 0.0 | 16.47 | 29.6 | 56.7 | -4.8% |
| c22 source | 50193 | 587 | 37039 | 12546 | 22 | 0.04 | 1.0% | 0.0 | 45.89 | 3.8 | 73.5 | -3.6% |
| c22 tax report | 66449 | 36665 | 0 | 0 | 29784 | 44.82 | 83.4% | 17.0 | 0.10 | 14.5 | 14.5 | -24.1% |
| c22 tax money | 54200 | 34789 | 19411 | 0 | 19411 | 0.00 | 83.3% | 17.0 | 28.93 | 29.7 | 94.0 | -30.4% |
| c22 hybrid report | 55657 | 18941 | 20438 | 16118 | 1773 | 3.19 | 33.1% | 0.0 | 24.58 | 5.9 | 57.6 | -7.2% |
| c22 hybrid money | 55305 | 18991 | 21395 | 16010 | 1279 | 0.00 | 33.3% | 0.0 | 25.98 | 5.8 | 60.3 | -7.3% |
| rel tax report | 9590 | 9381 | 0 | 0 | 469 | 4.89 | 14.2% | 0.0 | 0.00 | 38.2 | 31.1 | -6.4% |
| rel tax money | 9995 | 9763 | 521 | 0 | 521 | 0.00 | 14.9% | 0.0 | 0.71 | 38.5 | 32.5 | -6.8% |

Against the no-programme run (paired):

| Row | Basket poverty | Wealth poverty | Hours, % |
|---|---|---|---|
| rel source | -8.7 (-9.0 to -8.4) | 24.8 (24.1 to 25.5) | -2.9 (-2.9 to -2.8) |
| c22 source | -34.5 (-35.0 to -34.1) | 41.6 (40.9 to 42.4) | -1.6 (-2.2 to -1.0) |
| c22 tax report | -23.8 (-24.3 to -23.4) | -17.4 (-17.8 to -17.0) | -22.1 (-23.2 to -21.0) |
| c22 tax money | -8.6 (-9.1 to -8.1) | 62.1 (61.7 to 62.6) | -28.4 (-29.2 to -27.7) |
| c22 hybrid report | -32.5 (-32.9 to -32.1) | 25.7 (24.7 to 26.8) | -5.3 (-5.9 to -4.7) |
| c22 hybrid money | -32.6 (-32.9 to -32.2) | 28.5 (27.3 to 29.6) | -5.4 (-6.1 to -4.7) |
| rel tax report | -0.1 (-0.4 to 0.2) | -0.7 (-1.0 to -0.5) | -4.5 (-4.7 to -4.2) |
| rel tax money | 0.2 (-0.0 to 0.5) | 0.6 (0.3 to 0.9) | -4.8 (-4.9 to -4.7) |

The gap as new money against the gap unpaid (fx.fin 'money' less 'report', paired):

| Design and reading | Inflation, points a year | Basket poverty | Wealth poverty |
|---|---|---|---|
| C2.2, flat contribution | 28.82 (28.30 to 29.34) | 15.2 (14.8 to 15.7) | 79.5 (79.0 to 80.0) |
| C2.2, hybrid | 1.40 (1.37 to 1.43) | -0.1 (-0.1 to -0.1) | 2.7 (2.5 to 3.0) |
| Release design, flat contribution | 0.71 (0.68 to 0.74) | 0.3 (0.3 to 0.4) | 1.4 (1.2 to 1.5) |

### (B) Costs at the within-year price level (quarterly count of today's rule)

| Row | Within-year level over opening | Basket poverty, published | At within-year prices | Depth (FGT1), published | At within-year prices |
|---|---|---|---|---|---|
| none q4 | 1.0000 | 38.3 | 38.3 | 14.02 | 14.02 |
| rel q4 | 1.0594 | 29.6 | 32.1 | 9.24 | 10.26 |
| c22 q4 | 1.1527 | 3.8 | 5.2 | 0.49 | 0.68 |

The programme's effect on basket poverty (against the no-programme run, paired), published and at within-year prices, and how far the reading moves it:

| Design | Effect, published | Effect at within-year prices | Moved by |
|---|---|---|---|
| Release design | -8.7 (-9.0 to -8.4) | -6.2 (-6.5 to -5.9) | 2.5 (2.4 to 2.6) |
| C2.2 (Source) | -34.5 (-35.0 to -34.1) | -33.1 (-33.6 to -32.7) | 1.4 (1.3 to 1.5) |

