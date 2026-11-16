# BLS research CPI by income quintile (R-CPI-I): raw files

Downloaded by Duke from bls.gov on Nov 15, 2026 (bls.gov refused the build machine, HTTP 403, so these were supplied by hand). Kept unchanged, as downloaded.

| File | What it holds | Coverage |
|---|---|---|
| `R-CPI-I.xlsx` | Table 1, R-CPI-I index by income quintile I1 (lowest) to I5 (highest), December 2005 = 100, monthly | Dec 2005 - Dec 2025; October 2025 is "-" (not published, 2025 lapse in appropriations) |
| `R-C-CPI-I.xlsx` | Table 2, the chained version (R-C-CPI-I), December 2005 = 100, monthly | Dec 2005 - Dec 2024 |
| `R-CPI-I-relative-importance.xlsx` | Relative importance of 8 major groups and 75 item components by quintile, one sheet per December | 2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021, 2022, 2023, 2024; row 3 of each sheet is each quintile's share of CPI-U expenditure |
| `BLS-CPI-calculation-methodology.txt` | Text of BLS's "Consumer Price Index: Calculation" methodology page (last modified Jan 30, 2025), pasted. Its equations did not copy (they read "formula"); the text is the general CPI method, not an R-CPI-I-specific page | |

SHA-256:
- R-CPI-I.xlsx d3a7ae2554b4e059a3e9f9420483ec6fc8fabc29e5ec4387cd57a0cd0b02e3bc
- R-C-CPI-I.xlsx 4752f7c7c4573549c2772e39df0768963d080a09aa86079d010f683999cf72ad
- R-CPI-I-relative-importance.xlsx ea5c845490b3ea4584dcf9fba17336b51471b75c23a5a9a5e6eaf095a9c5190b
- BLS-CPI-calculation-methodology.txt 763107b961047d2c55f63fe6cd4a8e6c66e928970a7a940ed45f8a647df991de

Checks made on receipt: months are continuous from Dec 2005; no gaps other than October 2025; each relative-importance sheet's eight major groups sum to 100 (within rounding) for every quintile.
