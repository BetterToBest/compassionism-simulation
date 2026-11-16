# S74: the R-CPI-I check (Amendment 3)

BLS's research CPI by income quintile (R-CPI-I, December 2005 = 100; I1 lowest income, I5 highest), supplied by Duke on Nov 15, 2026 (bls.gov refuses the build machine). CPI-U is FRED's CPIAUCSL. December to December, % a year. Command: `python3 dev/tools/s74_rcpi.py`. A derived calculation; nothing in the engine uses it.

| | I1 | I2 | I3 | I4 | I5 | I1 - I5 | CPI-U |
|---|---|---|---|---|---|---|---|
| R-CPI-I, Dec 2005 - Dec 2025 | 2.69 | 2.64 | 2.55 | 2.50 | 2.43 | 0.26 | 2.52 |
| R-C-CPI-I (chained), Dec 2005 - Dec 2024 | 2.59 | 2.43 | 2.29 | 2.22 | 2.15 | 0.43 | 2.52 |
| the engine's method on BLS's Dec 2005 shares | 2.83 | 2.83 | 2.82 | 2.82 | 2.82 | 0.01 | 2.52 |

BLS's December 2005 shares (food and beverages / housing / medical care, %): I1 17.0 / 44.0 / 6.2; I2 16.3 / 43.2 / 7.4; I3 15.2 / 41.8 / 7.0; I4 14.4 / 41.8 / 6.1; I5 13.4 / 42.9 / 5.2.
Components, Dec 2005 - Dec 2025 (% a year): all items 2.52, food at home 2.55, shelter 3.13, medical care 2.94.

**The engine** (History, 2006-2025, annual averages; its fifths are by wealth, not income): CPI-U 2.537; all households 2.766 (10th-90th percentile 2.748 to 2.784); by wealth fifth 2.771, 2.767, 2.764, 2.765, 2.764; top 1% 2.775. Spread across fifths 0.007 points.
