# S54 policy levers: tables (pilot, seeds 1-50; labelled pilot, not figures of the model)

Engine e6da050. Written by `dev/tools/s54_levers.py` from compassionism-sim-results (stage 1: ../compassionism-sim-results/s54-levers1-e6da050; stage 2: ../compassionism-sim-results/s54-levers2-e6da050). Paired bootstrap over seeds, 2000 replicates, resampler seed 54, the same resample for every cell. research-update `prereg/2026-11-levers-addendum.md` defines every cell.

## Stage 1: each lever on its own (Q20, decision rule 1)

Lever effect: the lever row minus its comparison row on the same seeds (the design under the test reading, `base`; for today's rule's tax sweep, `asis`; for `asis` itself, `base`, so that row is the effect of the joining reading). A lever **works** on an outcome where the interval excludes zero in the favourable direction in all three environments, **harms** where it excludes zero in the unfavourable direction in any environment, and otherwise does not move it. Each cell of the matrices: the verdict and the lever effect's mean over the three environments (points; inflation in points a year). Participation (higher is favourable) is in % of adults.

### The designs against no programme (programme effect, seed mean and 95% interval)

| Design | Wages | Row | Environment | basket poverty, % of adult-years | wealth poverty at year 20, % | non-participants' basket poverty, % | programme inflation, points a year | participation, mean of years 1-19, % | non-participants' wealth poverty, % | non-participants' income drops of 25%+ with no buffer, per 100 | non-participants under 3 months of basics covered, % | below 30 days of basic living, design-neutral, % |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| release row | 100% | base | Reference | -29.79 (-30.40, -29.24) | +11.38 (+10.62, +12.18) | -14.61 (-15.36, -13.81) | +50.78 (+50.34, +51.26) | +83.61 (+83.08, +84.12) | +27.92 (+26.56, +29.31) | +0.56 (+0.49, +0.63) | +24.10 (+22.87, +25.36) | -12.42 (-12.86, -11.97) |
| release row | 100% | base | Adverse | -35.11 (-35.84, -34.39) | +36.18 (+35.56, +36.83) | -17.27 (-18.26, -16.20) | +60.87 (+60.29, +61.49) | +83.70 (+83.18, +84.21) | +44.90 (+43.50, +46.30) | +0.46 (+0.36, +0.56) | +27.84 (+26.85, +28.84) | -7.94 (-8.43, -7.45) |
| release row | 100% | base | Stress | -13.42 (-13.96, -12.85) | +31.47 (+30.72, +32.18) | -4.54 (-5.00, -4.06) | +27.68 (+27.14, +28.21) | +44.06 (+43.29, +44.84) | +39.05 (+38.10, +40.04) | +0.82 (+0.75, +0.88) | +23.50 (+22.93, +24.08) | +5.80 (+5.45, +6.14) |
| release row | 100% | asis | Reference | -29.97 (-30.59, -29.41) | +11.30 (+10.51, +12.12) | -15.23 (-16.02, -14.39) | +51.00 (+50.56, +51.47) | +83.99 (+83.47, +84.49) | +27.20 (+25.81, +28.60) | +0.35 (+0.28, +0.41) | +23.73 (+22.49, +24.99) | -12.57 (-13.01, -12.11) |
| release row | 100% | asis | Adverse | -35.23 (-35.96, -34.52) | +36.30 (+35.66, +36.97) | -17.74 (-18.80, -16.65) | +61.08 (+60.50, +61.70) | +83.99 (+83.47, +84.49) | +44.81 (+43.40, +46.19) | +0.28 (+0.18, +0.38) | +27.68 (+26.67, +28.70) | -8.05 (-8.54, -7.55) |
| release row | 100% | asis | Stress | -13.42 (-13.97, -12.85) | +31.47 (+30.72, +32.18) | -4.54 (-5.00, -4.06) | +27.68 (+27.14, +28.21) | +44.06 (+43.30, +44.84) | +39.05 (+38.10, +40.04) | +0.82 (+0.75, +0.88) | +23.50 (+22.93, +24.08) | +5.80 (+5.45, +6.14) |
| release row | 100% | base.sv | Reference | -29.75 (-30.37, -29.21) | -19.90 (-20.52, -19.29) | -14.60 (-15.36, -13.80) | +50.82 (+50.38, +51.29) | +83.62 (+83.09, +84.13) | -9.25 (-10.09, -8.48) | -0.23 (-0.28, -0.17) | -9.75 (-10.52, -9.00) | -17.41 (-17.82, -17.02) |
| release row | 100% | base.sv | Adverse | -35.03 (-35.77, -34.32) | -22.84 (-23.47, -22.17) | -17.20 (-18.21, -16.13) | +61.00 (+60.42, +61.62) | +83.71 (+83.18, +84.21) | -10.89 (-11.82, -9.96) | -0.67 (-0.76, -0.59) | -10.67 (-11.48, -9.90) | -18.22 (-18.63, -17.79) |
| release row | 100% | base.sv | Stress | -13.37 (-13.92, -12.80) | -8.95 (-9.37, -8.54) | -4.49 (-4.95, -4.02) | +27.69 (+27.16, +28.22) | +44.06 (+43.29, +44.84) | -2.77 (-3.15, -2.39) | -0.39 (-0.45, -0.33) | -3.19 (-3.48, -2.90) | -7.08 (-7.38, -6.78) |
| release row | 90% | base | Reference | -10.61 (-11.08, -10.16) | +60.00 (+59.42, +60.58) | +8.13 (+7.00, +9.26) | +68.47 (+67.72, +69.28) | +83.72 (+83.19, +84.22) | +64.81 (+63.46, +66.04) | +0.75 (+0.68, +0.81) | +36.55 (+35.58, +37.54) | +2.85 (+2.36, +3.39) |
| release row | 90% | base | Adverse | -12.73 (-13.23, -12.23) | +54.01 (+53.41, +54.63) | +3.43 (+2.38, +4.51) | +86.34 (+85.29, +87.45) | +83.79 (+83.26, +84.29) | +55.53 (+54.14, +56.94) | +0.74 (+0.62, +0.87) | +35.47 (+34.52, +36.45) | +10.04 (+9.60, +10.51) |
| release row | 90% | base | Stress | -1.66 (-2.15, -1.17) | +47.49 (+46.86, +48.10) | +6.85 (+6.33, +7.40) | +33.89 (+33.12, +34.64) | +44.06 (+43.29, +44.84) | +51.55 (+50.92, +52.24) | +1.01 (+0.94, +1.08) | +28.24 (+27.74, +28.74) | +14.03 (+13.61, +14.44) |
| release row | 90% | asis | Reference | -10.65 (-11.11, -10.18) | +60.08 (+59.50, +60.67) | +7.76 (+6.63, +8.94) | +68.73 (+68.00, +69.54) | +83.99 (+83.47, +84.49) | +64.81 (+63.49, +66.05) | +0.57 (+0.50, +0.64) | +36.47 (+35.49, +37.47) | +2.81 (+2.32, +3.35) |
| release row | 90% | asis | Adverse | -12.74 (-13.24, -12.24) | +54.02 (+53.43, +54.63) | +3.23 (+2.20, +4.30) | +86.60 (+85.57, +87.69) | +83.99 (+83.47, +84.49) | +55.53 (+54.14, +56.94) | +0.59 (+0.47, +0.70) | +35.41 (+34.46, +36.39) | +10.03 (+9.59, +10.50) |
| release row | 90% | asis | Stress | -1.66 (-2.15, -1.17) | +47.49 (+46.86, +48.10) | +6.85 (+6.33, +7.40) | +33.89 (+33.13, +34.64) | +44.06 (+43.30, +44.84) | +51.55 (+50.92, +52.24) | +1.01 (+0.94, +1.09) | +28.24 (+27.74, +28.74) | +14.04 (+13.61, +14.44) |
| release row | 90% | base.sv | Reference | -10.43 (-10.89, -9.97) | -11.84 (-12.44, -11.24) | +8.27 (+7.15, +9.40) | +68.72 (+67.97, +69.54) | +83.72 (+83.19, +84.23) | -0.01 (-1.02, +0.99) | -0.12 (-0.17, -0.06) | -5.92 (-6.70, -5.15) | -13.66 (-14.08, -13.25) |
| release row | 90% | base.sv | Adverse | -12.63 (-13.13, -12.14) | -14.80 (-15.38, -14.19) | +3.50 (+2.45, +4.59) | +86.53 (+85.48, +87.65) | +83.79 (+83.26, +84.29) | -2.88 (-4.08, -1.61) | -0.54 (-0.64, -0.45) | -7.38 (-8.21, -6.57) | -14.82 (-15.25, -14.39) |
| release row | 90% | base.sv | Stress | -1.66 (-2.14, -1.16) | -4.02 (-4.54, -3.53) | +6.86 (+6.35, +7.41) | +33.88 (+33.11, +34.63) | +44.06 (+43.29, +44.84) | +2.22 (+1.64, +2.79) | -0.36 (-0.42, -0.30) | -1.25 (-1.59, -0.90) | -4.92 (-5.17, -4.65) |
| C2.2 design | 100% | base | Reference | -25.51 (-26.03, -25.01) | -19.86 (-20.35, -19.35) | -24.99 (-26.13, -23.89) | +37.66 (+37.33, +38.00) | +100.00 (+100.00, +100.00) | -19.38 (-20.44, -18.34) | +0.16 (+0.07, +0.24) | -20.60 (-21.53, -19.71) | -17.29 (-17.68, -16.89) |
| C2.2 design | 100% | base | Adverse | -36.14 (-36.82, -35.50) | -23.50 (-24.07, -22.95) | -35.58 (-36.80, -34.33) | +44.27 (+43.85, +44.72) | +100.00 (+100.00, +100.00) | -23.28 (-24.58, -22.07) | -0.42 (-0.55, -0.29) | -23.58 (-24.59, -22.64) | -20.93 (-21.34, -20.50) |
| C2.2 design | 100% | base | Stress | -35.28 (-35.95, -34.66) | -11.25 (-11.96, -10.51) | -35.27 (-36.02, -34.53) | +46.32 (+45.83, +46.84) | +100.00 (+100.00, +100.00) | -10.94 (-11.84, -9.97) | -0.62 (-0.71, -0.55) | -20.62 (-21.14, -20.08) | -20.94 (-21.35, -20.51) |
| C2.2 design | 100% | asis | Reference | -25.51 (-26.03, -25.01) | -19.86 (-20.35, -19.35) | -24.99 (-26.13, -23.89) | +37.66 (+37.33, +38.00) | +100.00 (+100.00, +100.00) | -19.38 (-20.44, -18.34) | +0.16 (+0.07, +0.24) | -20.60 (-21.53, -19.71) | -17.29 (-17.68, -16.89) |
| C2.2 design | 100% | asis | Adverse | -36.14 (-36.82, -35.50) | -23.50 (-24.07, -22.95) | -35.58 (-36.80, -34.33) | +44.27 (+43.85, +44.72) | +100.00 (+100.00, +100.00) | -23.28 (-24.58, -22.07) | -0.42 (-0.55, -0.29) | -23.58 (-24.59, -22.64) | -20.93 (-21.34, -20.50) |
| C2.2 design | 100% | asis | Stress | -35.28 (-35.95, -34.66) | -11.25 (-11.96, -10.51) | -35.27 (-36.02, -34.53) | +46.32 (+45.83, +46.84) | +100.00 (+100.00, +100.00) | -10.94 (-11.84, -9.97) | -0.62 (-0.71, -0.55) | -20.62 (-21.14, -20.08) | -20.94 (-21.35, -20.51) |
| C2.2 design | 100% | base.sv | Reference | -25.49 (-26.02, -25.00) | -19.83 (-20.32, -19.32) | -24.97 (-26.11, -23.87) | +37.66 (+37.33, +38.00) | +100.00 (+100.00, +100.00) | -19.37 (-20.40, -18.35) | -0.44 (-0.51, -0.37) | -21.98 (-22.92, -21.10) | -17.03 (-17.42, -16.64) |
| C2.2 design | 100% | base.sv | Adverse | -36.13 (-36.80, -35.49) | -26.15 (-26.69, -25.64) | -35.56 (-36.79, -34.32) | +44.27 (+43.85, +44.72) | +100.00 (+100.00, +100.00) | -25.52 (-26.71, -24.40) | -1.13 (-1.24, -1.01) | -24.93 (-25.97, -23.97) | -19.83 (-20.23, -19.43) |
| C2.2 design | 100% | base.sv | Stress | -35.27 (-35.93, -34.65) | -25.86 (-26.39, -25.35) | -35.26 (-36.01, -34.52) | +46.32 (+45.83, +46.84) | +100.00 (+100.00, +100.00) | -25.83 (-26.56, -25.12) | -1.34 (-1.42, -1.26) | -25.06 (-25.63, -24.48) | -19.84 (-20.24, -19.43) |
| C2.2 design | 90% | base | Reference | -24.61 (-25.11, -24.14) | -10.83 (-11.67, -9.91) | -24.22 (-25.37, -23.16) | +46.49 (+46.00, +47.00) | +100.00 (+100.00, +100.00) | -11.14 (-12.22, -10.11) | +0.18 (+0.09, +0.27) | -18.26 (-19.09, -17.47) | -17.26 (-17.66, -16.86) |
| C2.2 design | 90% | base | Adverse | -33.87 (-34.46, -33.29) | +19.77 (+18.02, +21.55) | -33.42 (-34.59, -32.26) | +56.38 (+55.71, +57.10) | +100.00 (+100.00, +100.00) | +19.97 (+17.90, +22.02) | -0.47 (-0.59, -0.34) | -15.55 (-16.50, -14.65) | -20.89 (-21.30, -20.46) |
| C2.2 design | 90% | base | Stress | -30.85 (-31.37, -30.33) | +43.46 (+42.02, +44.92) | -30.80 (-31.44, -30.15) | +61.54 (+60.72, +62.42) | +100.00 (+100.00, +100.00) | +43.58 (+42.08, +45.12) | -0.75 (-0.84, -0.68) | -5.72 (-6.49, -4.99) | -20.85 (-21.26, -20.43) |
| C2.2 design | 90% | asis | Reference | -24.61 (-25.11, -24.14) | -10.83 (-11.67, -9.91) | -24.22 (-25.37, -23.16) | +46.49 (+46.00, +47.00) | +100.00 (+100.00, +100.00) | -11.14 (-12.22, -10.11) | +0.18 (+0.09, +0.27) | -18.26 (-19.09, -17.47) | -17.26 (-17.66, -16.86) |
| C2.2 design | 90% | asis | Adverse | -33.87 (-34.46, -33.29) | +19.77 (+18.02, +21.55) | -33.42 (-34.59, -32.26) | +56.38 (+55.71, +57.10) | +100.00 (+100.00, +100.00) | +19.97 (+17.90, +22.02) | -0.47 (-0.59, -0.34) | -15.55 (-16.50, -14.65) | -20.89 (-21.30, -20.46) |
| C2.2 design | 90% | asis | Stress | -30.85 (-31.37, -30.33) | +43.46 (+42.02, +44.92) | -30.80 (-31.44, -30.15) | +61.54 (+60.72, +62.42) | +100.00 (+100.00, +100.00) | +43.58 (+42.08, +45.12) | -0.75 (-0.84, -0.68) | -5.72 (-6.49, -4.99) | -20.85 (-21.26, -20.43) |
| C2.2 design | 90% | base.sv | Reference | -24.60 (-25.09, -24.12) | -19.69 (-20.19, -19.17) | -24.20 (-25.36, -23.14) | +46.49 (+46.00, +47.00) | +100.00 (+100.00, +100.00) | -19.26 (-20.27, -18.29) | -0.39 (-0.47, -0.31) | -21.79 (-22.73, -20.91) | -17.01 (-17.39, -16.62) |
| C2.2 design | 90% | base.sv | Adverse | -33.86 (-34.45, -33.28) | -25.90 (-26.41, -25.40) | -33.40 (-34.56, -32.24) | +56.38 (+55.71, +57.10) | +100.00 (+100.00, +100.00) | -25.38 (-26.53, -24.26) | -1.09 (-1.20, -0.97) | -24.72 (-25.74, -23.74) | -19.80 (-20.20, -19.40) |
| C2.2 design | 90% | base.sv | Stress | -30.84 (-31.36, -30.32) | -25.36 (-25.88, -24.84) | -30.79 (-31.43, -30.14) | +61.54 (+60.72, +62.42) | +100.00 (+100.00, +100.00) | -25.36 (-26.08, -24.66) | -1.32 (-1.40, -1.24) | -24.72 (-25.31, -24.14) | -19.81 (-20.22, -19.41) |

### Verdicts: release row, wages 100%

| Row | What it sets | vs | basket poverty, % of adult-years | wealth poverty at year 20, % | non-participants' basket poverty, % | programme inflation, points a year | participation, mean of years 1-19, % | non-participants' wealth poverty, % | non-participants' income drops of 25%+ with no buffer, per 100 | non-participants under 3 months of basics covered, % | below 30 days of basic living, design-neutral, % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| asis | today's joining rule | base | no move -0.10 | **harms** +0.01 | no move -0.36 | **harms** +0.14 | no move +0.22 | no move -0.27 | no move -0.13 | no move -0.18 | no move -0.09 |
| t0 | tax 0% | base | **works** -2.55 | **harms** -1.43 | **works** -2.07 | **harms** +2.76 | **works** +0.46 | **harms** -0.84 | **harms** -0.01 | **harms** -0.86 | no move -1.53 |
| t4 | tax 4% | base | **works** -1.77 | **harms** -0.86 | **works** -1.36 | **harms** +2.02 | **works** +0.29 | **harms** -0.46 | **harms** -0.00 | **harms** -0.49 | no move -0.99 |
| t8 | tax 8% | base | **works** -1.00 | **harms** -0.33 | **works** -0.77 | **harms** +1.24 | **works** +0.14 | **harms** -0.07 | **harms** -0.00 | **harms** -0.13 | **harms** -0.48 |
| t12 | tax 12% | base | no move -0.20 | **harms** +0.13 | no move -0.08 | **harms** +0.43 | no move +0.01 | **harms** +0.21 | **harms** +0.01 | **harms** +0.17 | **harms** +0.02 |
| t16 | tax 16% | base | **harms** +0.59 | **harms** +0.59 | **harms** +0.40 | **harms** -0.41 | **harms** -0.13 | **harms** +0.43 | **harms** +0.02 | **harms** +0.30 | **harms** +0.48 |
| t20 | tax 20% | base | **harms** +1.38 | **harms** +1.13 | **harms** +0.85 | **works** -1.27 | **harms** -0.21 | **harms** +0.63 | **harms** +0.03 | **harms** +0.36 | **harms** +0.90 |
| t25 | tax 25% | base | **harms** +2.35 | **harms** +1.68 | **harms** +1.36 | **works** -2.33 | **harms** -0.23 | **harms** +0.75 | **harms** +0.03 | **harms** +0.37 | **harms** +1.40 |
| t30 | tax 30% | base | **harms** +3.33 | **harms** +2.13 | **harms** +1.90 | **works** -3.47 | **harms** -0.17 | **harms** +0.71 | **harms** +0.01 | **harms** +0.35 | **harms** +1.84 |
| t40 | tax 40% | base | **harms** +5.26 | **harms** +2.58 | **harms** +2.93 | **works** -6.26 | **harms** -0.10 | **harms** +0.26 | no move -0.03 | **harms** +0.08 | **harms** +2.58 |
| asis.t0 | tax 0%, today's rule | asis | **works** -2.37 | **harms** -1.39 | **works** -1.42 | **harms** +2.53 | no move +0.00 | **harms** -0.33 | **harms** +0.01 | **harms** -0.38 | no move -1.37 |
| asis.t4 | tax 4%, today's rule | asis | **works** -1.66 | **harms** -0.85 | **works** -0.97 | **harms** +1.88 | no move +0.00 | **harms** -0.12 | **harms** +0.01 | **harms** -0.18 | **harms** -0.89 |
| asis.t8 | tax 8%, today's rule | asis | **works** -0.94 | **harms** -0.32 | **works** -0.54 | **harms** +1.18 | no move +0.00 | **harms** +0.15 | **harms** +0.01 | **harms** +0.00 | **harms** -0.43 |
| asis.t12 | tax 12%, today's rule | asis | no move -0.20 | **harms** +0.13 | no move -0.08 | **harms** +0.43 | no move +0.00 | **harms** +0.21 | **harms** +0.01 | **harms** +0.16 | **harms** +0.02 |
| asis.t16 | tax 16%, today's rule | asis | **harms** +0.56 | **harms** +0.60 | **harms** +0.39 | **harms** -0.36 | no move +0.00 | **harms** +0.46 | **harms** +0.01 | **harms** +0.30 | **harms** +0.45 |
| asis.t20 | tax 20%, today's rule | asis | **harms** +1.33 | **harms** +1.11 | **harms** +0.87 | **works** -1.17 | no move +0.00 | **harms** +0.67 | **harms** +0.02 | **harms** +0.38 | **harms** +0.86 |
| asis.t25 | tax 25%, today's rule | asis | **harms** +2.32 | **harms** +1.65 | **harms** +1.45 | **works** -2.24 | no move +0.00 | **harms** +0.78 | **harms** +0.02 | **harms** +0.44 | **harms** +1.38 |
| asis.t30 | tax 30%, today's rule | asis | **harms** +3.32 | **harms** +2.10 | **harms** +2.07 | **works** -3.41 | no move +0.00 | **harms** +0.80 | **harms** +0.03 | **harms** +0.45 | **harms** +1.85 |
| asis.t40 | tax 40%, today's rule | asis | **harms** +5.29 | **harms** +2.58 | **harms** +3.21 | **works** -6.25 | no move +0.00 | **harms** +0.53 | **harms** +0.04 | **harms** +0.29 | **harms** +2.64 |
| pr0c75 | progression 0 pts, cap 75% | base | **works** -0.29 | no move -0.36 | **works** -0.44 | **harms** +0.14 | **works** +0.20 | no move -0.40 | **harms** -0.05 | **harms** -0.31 | no move -0.31 |
| pr8c75 | progression 8 pts, cap 75% | base | **harms** +0.38 | **harms** +0.41 | **harms** +0.38 | **works** -0.32 | **harms** -0.58 | **harms** +0.29 | **harms** +0.12 | **harms** +0.21 | **harms** +0.36 |
| pr0c50 | progression 0 pts, cap 50% | base | **works** -0.29 | no move -0.36 | **works** -0.44 | **harms** +0.14 | **works** +0.20 | no move -0.40 | **harms** -0.05 | **harms** -0.31 | no move -0.31 |
| pr4c50 | progression 4 pts, cap 50% | base | no move -0.00 | no move -0.03 | no move -0.00 | no move -0.00 | no move +0.00 | no move -0.02 | no move -0.00 | no move -0.01 | no move -0.01 |
| pr8c50 | progression 8 pts, cap 50% | base | **harms** +0.27 | **harms** +0.28 | **harms** +0.29 | **works** -0.24 | **harms** -0.44 | **harms** +0.18 | **harms** +0.09 | **harms** +0.16 | **harms** +0.25 |
| bt0 | business tax 0% | base | **works** -2.09 | **harms** -0.95 | **works** -1.11 | **harms** +2.43 | **harms** -0.09 | **harms** -0.04 | **harms** +0.11 | **harms** -0.13 | no move -1.08 |
| bt25 | business tax 25% | base | **harms** +2.06 | **harms** +1.39 | **harms** +1.14 | **works** -1.98 | no move +0.10 | **harms** +0.51 | no move -0.03 | **harms** +0.28 | **harms** +1.22 |
| bt50 | business tax 50% | base | **harms** +6.40 | **harms** +2.52 | **harms** +3.53 | **works** -8.14 | no move +0.22 | **harms** -0.08 | no move -0.05 | **harms** -0.23 | **harms** +2.84 |
| bt75 | business tax 75% | base | **harms** +10.46 | **harms** +1.24 | **harms** +5.64 | **works** -15.51 | no move +0.22 | **harms** -2.74 | **harms** +0.01 | **harms** -1.90 | **harms** +3.99 |
| kp10 | Source keeps 10% of project sales | base | **works** -0.02 | no move -0.10 | **works** -0.02 | **works** -0.16 | no move +0.00 | no move -0.08 | no move +0.00 | **works** -0.07 | **works** -0.03 |
| kp25 | Source keeps 25% of project sales | base | **works** -0.05 | no move -0.24 | **works** -0.04 | **works** -0.41 | no move -0.00 | no move -0.18 | no move +0.01 | **works** -0.17 | **works** -0.08 |
| kp50 | Source keeps 50% of project sales | base | **works** -0.10 | **works** -0.52 | **works** -0.09 | **works** -0.82 | no move -0.00 | **works** -0.43 | **harms** +0.01 | **works** -0.33 | **works** -0.15 |
| ex50 | 50% of expired BU recycled | base | **harms** +0.45 | **harms** +1.01 | **harms** +0.09 | **harms** +0.48 | no move +0.09 | **harms** +0.55 | no move -0.04 | **harms** +0.25 | **harms** +0.55 |
| ex0 | 0% of expired BU recycled | base | **harms** +0.88 | **harms** +1.98 | **harms** +0.13 | **harms** +0.98 | no move +0.22 | **harms** +1.04 | no move -0.12 | **harms** +0.46 | **harms** +1.02 |
| fprog | outside finance: progressive income tax | base | **harms** +42.37 | **harms** +16.95 | **harms** +40.05 | **works** -14.65 | **harms** -1.09 | **harms** +12.53 | **harms** +1.38 | **harms** +7.78 | **harms** +20.00 |
| fland | outside finance: land-value tax | base | **harms** +13.13 | **works** -25.66 | **harms** +12.72 | **works** -39.71 | **harms** -3.08 | **works** -24.08 | **harms** +0.13 | **works** -20.20 | **works** -7.90 |
| fflat | outside finance: flat wage contribution | base | **harms** +38.76 | **harms** -12.50 | **harms** +36.31 | **works** -46.46 | **harms** -6.92 | **harms** -11.20 | **harms** +2.13 | **works** -11.37 | **harms** +10.51 |
| br1 | business rate 1x | base | **harms** +9.93 | **harms** +0.52 | **harms** +5.10 | **works** -15.87 | no move +0.22 | **harms** -3.45 | **harms** -0.09 | **harms** -2.26 | **harms** +3.62 |
| br15 | business rate 1.5x | base | **harms** +8.05 | **harms** +1.59 | **harms** +4.22 | **works** -12.04 | no move +0.22 | **harms** -1.69 | no move -0.10 | **harms** -1.21 | **harms** +3.13 |
| br2 | business rate 2x | base | **harms** +5.55 | **harms** +2.21 | **harms** +2.97 | **works** -7.16 | no move +0.21 | **harms** -0.17 | no move -0.08 | **harms** -0.25 | **harms** +2.48 |
| bu60 | 60% of the BU | base | **harms** +8.96 | **harms** -1.90 | **harms** +4.21 | **works** -15.35 | no move +0.22 | **works** -4.34 | no move -0.12 | no move -2.58 | **harms** +5.75 |
| bu80 | 80% of the BU | base | **harms** +5.05 | **harms** +0.75 | **harms** +2.53 | **works** -6.66 | no move +0.20 | **harms** -0.87 | no move -0.08 | **harms** -0.37 | **harms** +4.18 |
| mm3 | top multiplier 3 | base | **harms** +0.81 | **harms** +1.23 | **harms** +0.31 | **harms** -0.25 | no move +0.09 | **harms** +0.57 | **works** -0.05 | **harms** +0.38 | **harms** +0.64 |
| mm6 | top multiplier 6 | base | **harms** +0.29 | **harms** +0.49 | **harms** +0.10 | no move -0.05 | no move +0.04 | **harms** +0.22 | no move -0.03 | **harms** +0.17 | **harms** +0.26 |
| mm9 | top multiplier 9 | base | no move -0.06 | no move -0.02 | no move -0.03 | **harms** +0.12 | no move +0.00 | no move +0.03 | **harms** +0.00 | **harms** +0.04 | no move +0.01 |
| oc25 | octave capacity 25% | base | **harms** +0.05 | **harms** +1.51 | **harms** +0.02 | **harms** +0.16 | **harms** -0.02 | **harms** +0.89 | **harms** +0.01 | **harms** +0.11 | **harms** +0.03 |
| oc50 | octave capacity 50% | base | **harms** +0.08 | **harms** +1.03 | **harms** +0.05 | **harms** +0.09 | **harms** -0.01 | **harms** +0.62 | no move +0.00 | **harms** +0.05 | **harms** +0.05 |
| oc100 | octave capacity 100% | base | **harms** +0.09 | **harms** +0.47 | **harms** +0.05 | **harms** +0.05 | no move +0.00 | **harms** +0.24 | **harms** +0.00 | **harms** +0.02 | **harms** +0.09 |
| no2 | 2 octaves | base | no move -0.42 | **harms** +0.27 | no move -0.22 | **harms** -0.00 | **harms** -0.05 | **harms** +0.12 | **harms** +0.02 | **harms** -0.02 | **works** -0.47 |
| no4 | 4 octaves | base | no move -0.21 | **harms** +0.08 | no move -0.13 | **harms** -0.01 | **harms** -0.03 | no move +0.00 | **harms** +0.01 | no move -0.01 | no move -0.24 |
| no6 | 6 octaves | base | **harms** +0.01 | no move -0.02 | **harms** +0.00 | no move -0.01 | no move +0.00 | no move -0.03 | no move +0.00 | no move -0.01 | **harms** +0.01 |
| phi0 | Phi tier off | base | **harms** +0.06 | **harms** +0.09 | **harms** +0.01 | **harms** +0.01 | no move +0.01 | no move +0.02 | no move -0.01 | **harms** +0.01 | **harms** +0.06 |
| ph5 | phase-in over 5 years | base | **harms** +1.06 | no move -0.45 | **harms** +0.39 | **works** -1.79 | no move +0.02 | no move -0.47 | **works** -0.07 | **works** -0.98 | **harms** +0.02 |
| ph10 | phase-in over 10 years | base | **harms** +2.54 | **works** -1.08 | **harms** +1.10 | **works** -4.22 | no move +0.08 | **works** -1.04 | **works** -0.12 | **works** -1.88 | **harms** +0.27 |
| cap2 | issuance cap 2% | base | **harms** +11.97 | **harms** +2.39 | **harms** +6.37 | **works** -17.34 | no move +0.21 | **harms** -2.96 | **harms** +0.24 | **harms** -1.22 | **harms** +6.44 |
| cap4 | issuance cap 4% | base | **harms** +11.97 | **harms** +2.39 | **harms** +6.37 | **works** -17.34 | no move +0.21 | **harms** -2.96 | **harms** +0.24 | **harms** -1.22 | **harms** +6.44 |
| cap8 | issuance cap 8% | base | **harms** +11.97 | **harms** +2.39 | **harms** +6.37 | **works** -17.34 | no move +0.21 | **harms** -2.96 | **harms** +0.24 | **harms** -1.22 | **harms** +6.44 |
| ixs | indexation: surge protocol (5%) | base | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 |
| ixy | indexation: every year, price level | base | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 |
| ixn | indexation: every year, basic needs | base | **works** -1.05 | **harms** -0.26 | **works** -2.01 | **harms** +1.15 | **works** +1.24 | **harms** -0.88 | **harms** -0.00 | **harms** -1.38 | **harms** -1.11 |
| sva | protected account, all savings | base | **harms** +15.97 | **works** -37.36 | **harms** +11.37 | **harms** +1196.67 | no move +0.21 | **works** -42.48 | **works** -1.09 | **works** -31.71 | no move -5.66 |
| svc | protected account, first $10,000 | base | **harms** +1.12 | **works** -18.36 | **harms** +0.82 | **harms** +9.67 | no move +0.04 | **works** -14.55 | **harms** +0.01 | **works** -5.19 | **works** -4.73 |
| rcap | rent cap for BU tenants | base | **works** -0.46 | no move -0.32 | **works** -0.23 | **harms** -0.18 | **harms** -0.02 | no move -0.18 | **harms** +0.01 | **works** -0.26 | **works** -0.38 |
| hc | rent risk ($1.41 a BU dollar) | base | **harms** +6.02 | **harms** +4.34 | **harms** +5.51 | **harms** +0.94 | no move +0.12 | **harms** +3.21 | **harms** +0.86 | **harms** +3.45 | **harms** +4.05 |
| hcrc | rent risk and rent cap | base | **harms** +2.48 | **harms** +0.54 | **harms** +7.46 | **works** -0.79 | **harms** -0.02 | **harms** +2.59 | **harms** +4.31 | **harms** +2.32 | **harms** +1.50 |

### Verdicts: release row, wages 90%

| Row | What it sets | vs | basket poverty, % of adult-years | wealth poverty at year 20, % | non-participants' basket poverty, % | programme inflation, points a year | participation, mean of years 1-19, % | non-participants' wealth poverty, % | non-participants' income drops of 25%+ with no buffer, per 100 | non-participants under 3 months of basics covered, % | below 30 days of basic living, design-neutral, % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| asis | today's joining rule | base | no move -0.02 | **harms** +0.03 | no move -0.19 | **harms** +0.17 | no move +0.16 | no move +0.00 | no move -0.11 | no move -0.05 | no move -0.02 |
| t0 | tax 0% | base | **works** -2.45 | **harms** -0.59 | **harms** -1.71 | **harms** +3.46 | **works** +0.38 | **harms** -0.28 | **harms** +0.04 | **harms** -0.25 | **harms** -1.37 |
| t4 | tax 4% | base | **works** -1.63 | **harms** -0.30 | **harms** -1.08 | **harms** +2.55 | **works** +0.24 | **harms** -0.12 | **harms** +0.03 | **harms** -0.07 | **harms** -0.83 |
| t8 | tax 8% | base | **works** -0.85 | **harms** -0.05 | **harms** -0.52 | **harms** +1.59 | **works** +0.11 | **harms** +0.03 | **harms** +0.02 | **harms** +0.08 | **harms** -0.33 |
| t12 | tax 12% | base | no move -0.08 | **harms** +0.11 | **harms** +0.02 | **harms** +0.59 | no move +0.01 | **harms** +0.12 | **harms** +0.01 | **harms** +0.18 | **harms** +0.12 |
| t16 | tax 16% | base | **harms** +0.62 | **harms** +0.27 | **harms** +0.35 | **harms** -0.45 | **harms** -0.07 | **harms** +0.20 | **harms** +0.02 | **harms** +0.16 | **harms** +0.51 |
| t20 | tax 20% | base | **harms** +1.33 | **harms** +0.39 | **harms** +0.66 | **works** -1.53 | **harms** -0.12 | **harms** +0.21 | **harms** +0.02 | **harms** +0.10 | **harms** +0.86 |
| t25 | tax 25% | base | **harms** +2.17 | **harms** +0.47 | **harms** +1.00 | **works** -2.99 | **harms** -0.12 | **harms** +0.13 | no move -0.00 | **harms** -0.00 | **harms** +1.24 |
| t30 | tax 30% | base | **harms** +2.90 | **harms** +0.44 | **harms** +1.27 | **works** -4.73 | **harms** -0.11 | **harms** +0.01 | no move -0.03 | **harms** -0.15 | **harms** +1.50 |
| t40 | tax 40% | base | **harms** +4.28 | **harms** +0.19 | **harms** +1.70 | **works** -8.74 | **harms** -0.10 | **harms** -0.42 | no move -0.06 | **harms** -0.57 | **harms** +1.89 |
| asis.t0 | tax 0%, today's rule | asis | **works** -2.36 | **harms** -0.65 | **harms** -1.21 | **harms** +3.15 | no move +0.00 | **harms** -0.24 | **harms** +0.04 | **harms** -0.04 | **harms** -1.29 |
| asis.t4 | tax 4%, today's rule | asis | **works** -1.57 | **harms** -0.31 | **harms** -0.77 | **harms** +2.35 | no move +0.00 | **harms** -0.07 | **harms** +0.02 | **harms** +0.06 | **harms** -0.77 |
| asis.t8 | tax 8%, today's rule | asis | **works** -0.82 | **harms** -0.07 | **harms** -0.35 | **harms** +1.50 | no move +0.00 | **harms** +0.03 | **harms** +0.01 | **harms** +0.13 | **harms** -0.30 |
| asis.t12 | tax 12%, today's rule | asis | no move -0.09 | **harms** +0.10 | **harms** +0.02 | **harms** +0.59 | no move +0.00 | **harms** +0.12 | no move +0.00 | **harms** +0.18 | **harms** +0.12 |
| asis.t16 | tax 16%, today's rule | asis | **harms** +0.61 | **harms** +0.27 | **harms** +0.36 | **harms** -0.39 | no move +0.00 | **harms** +0.21 | no move +0.00 | **harms** +0.17 | **harms** +0.50 |
| asis.t20 | tax 20%, today's rule | asis | **harms** +1.31 | **harms** +0.41 | **harms** +0.71 | **works** -1.44 | no move +0.00 | **harms** +0.21 | no move +0.00 | **harms** +0.13 | **harms** +0.85 |
| asis.t25 | tax 25%, today's rule | asis | **harms** +2.15 | **harms** +0.49 | **harms** +1.09 | **works** -2.91 | no move +0.00 | **harms** +0.16 | **harms** -0.00 | **harms** +0.05 | **harms** +1.25 |
| asis.t30 | tax 30%, today's rule | asis | **harms** +2.89 | **harms** +0.45 | **harms** +1.40 | **works** -4.67 | no move +0.00 | **harms** +0.04 | no move -0.00 | **harms** -0.08 | **harms** +1.52 |
| asis.t40 | tax 40%, today's rule | asis | **harms** +4.28 | **harms** +0.21 | **harms** +1.89 | **works** -8.70 | no move +0.00 | **harms** -0.39 | no move -0.01 | **harms** -0.46 | **harms** +1.94 |
| pr0c75 | progression 0 pts, cap 75% | base | no move -0.27 | no move -0.05 | no move -0.33 | **harms** +0.06 | **works** +0.17 | no move -0.07 | no move -0.03 | **harms** -0.15 | **harms** -0.32 |
| pr8c75 | progression 8 pts, cap 75% | base | **harms** +0.30 | no move +0.02 | **harms** +0.21 | **works** -0.26 | **harms** -0.39 | no move -0.01 | **harms** +0.11 | **harms** +0.08 | **harms** +0.28 |
| pr0c50 | progression 0 pts, cap 50% | base | no move -0.27 | no move -0.05 | no move -0.33 | **harms** +0.06 | **works** +0.17 | no move -0.07 | no move -0.03 | **harms** -0.15 | **harms** -0.32 |
| pr4c50 | progression 4 pts, cap 50% | base | no move -0.01 | no move -0.00 | no move -0.01 | no move -0.01 | no move +0.00 | no move +0.00 | no move -0.00 | no move -0.00 | no move -0.01 |
| pr8c50 | progression 8 pts, cap 50% | base | **harms** +0.22 | no move +0.02 | **harms** +0.15 | **works** -0.20 | **harms** -0.30 | no move -0.01 | **harms** +0.08 | **harms** +0.06 | **harms** +0.18 |
| bt0 | business tax 0% | base | **works** -2.01 | **harms** -0.53 | **harms** -0.94 | **harms** +3.19 | **harms** -0.06 | **harms** -0.19 | **harms** +0.11 | **harms** +0.15 | **harms** -0.92 |
| bt25 | business tax 25% | base | **harms** +1.93 | **harms** +0.45 | **harms** +0.86 | **works** -2.65 | no move +0.09 | **harms** +0.12 | **works** -0.05 | **harms** -0.04 | **harms** +1.10 |
| bt50 | business tax 50% | base | **harms** +4.88 | **harms** -0.32 | **harms** +1.75 | **works** -11.83 | no move +0.16 | **harms** -0.93 | no move -0.10 | **harms** -1.10 | **harms** +1.73 |
| bt75 | business tax 75% | base | **harms** +7.31 | **harms** -3.51 | **harms** +2.03 | **works** -22.62 | no move +0.16 | **harms** -4.15 | **harms** -0.04 | **works** -3.41 | **harms** +1.54 |
| kp10 | Source keeps 10% of project sales | base | **works** -0.06 | no move -0.03 | **works** -0.05 | **works** -0.21 | no move -0.00 | no move -0.02 | no move +0.00 | **works** -0.06 | **works** -0.07 |
| kp25 | Source keeps 25% of project sales | base | **works** -0.16 | no move -0.07 | **works** -0.14 | **works** -0.53 | **harms** -0.00 | no move -0.05 | no move +0.00 | **works** -0.16 | **works** -0.17 |
| kp50 | Source keeps 50% of project sales | base | **works** -0.31 | **works** -0.17 | **works** -0.26 | **works** -1.08 | **harms** -0.00 | no move -0.10 | no move +0.00 | **works** -0.31 | **works** -0.34 |
| ex50 | 50% of expired BU recycled | base | **harms** +0.62 | **harms** +0.27 | **harms** +0.28 | **harms** +0.78 | no move +0.07 | **harms** +0.18 | no move -0.03 | **harms** +0.21 | **harms** +0.69 |
| ex0 | 0% of expired BU recycled | base | **harms** +1.18 | **harms** +0.47 | **harms** +0.51 | **harms** +1.55 | no move +0.16 | **harms** +0.30 | no move -0.09 | **harms** +0.40 | **harms** +1.29 |
| fprog | outside finance: progressive income tax | base | **harms** +31.44 | **harms** -4.12 | **harms** +25.53 | **harms** -11.42 | **harms** -0.95 | **harms** -4.37 | **harms** +1.50 | **harms** +1.92 | **harms** +14.76 |
| fland | outside finance: land-value tax | base | no move -0.59 | **works** -44.44 | no move -1.26 | **works** -53.34 | **harms** -3.23 | **works** -36.85 | **harms** -0.04 | **works** -25.17 | **works** -19.16 |
| fflat | outside finance: flat wage contribution | base | **harms** +21.00 | **works** -39.99 | **harms** +18.03 | **works** -62.91 | **harms** -6.98 | **works** -31.20 | **harms** +1.91 | **works** -19.65 | **works** -3.32 |
| br1 | business rate 1x | base | **harms** +6.76 | **harms** -3.93 | **harms** +1.52 | **works** -23.26 | no move +0.16 | **harms** -4.49 | no move -0.16 | **works** -3.68 | **harms** +1.07 |
| br15 | business rate 1.5x | base | **harms** +5.76 | **harms** -1.92 | **harms** +1.57 | **works** -17.56 | no move +0.16 | **harms** -2.54 | **works** -0.16 | no move -2.35 | **harms** +1.39 |
| br2 | business rate 2x | base | **harms** +4.27 | **harms** -0.27 | **harms** +1.49 | **works** -10.35 | no move +0.15 | **harms** -0.80 | **works** -0.12 | **harms** -1.00 | **harms** +1.52 |
| bu60 | 60% of the BU | base | **harms** +5.09 | **works** -6.24 | **harms** +0.29 | **works** -24.17 | no move +0.16 | **works** -5.07 | **works** -0.20 | **works** -4.04 | **harms** +1.67 |
| bu80 | 80% of the BU | base | **harms** +3.41 | no move -1.55 | **harms** +0.84 | **works** -10.96 | no move +0.15 | no move -1.30 | **works** -0.11 | **works** -1.14 | **harms** +2.48 |
| mm3 | top multiplier 3 | base | **harms** +1.10 | **harms** +0.25 | **harms** +0.53 | **harms** +0.21 | no move +0.08 | **harms** +0.11 | no move -0.03 | **harms** +0.39 | **harms** +0.91 |
| mm6 | top multiplier 6 | base | **harms** +0.42 | **harms** +0.06 | **harms** +0.20 | **harms** +0.13 | no move +0.03 | no move +0.02 | no move -0.02 | **harms** +0.19 | **harms** +0.36 |
| mm9 | top multiplier 9 | base | no move -0.04 | no move -0.04 | no move -0.00 | **harms** +0.13 | no move +0.00 | no move +0.00 | no move +0.00 | **harms** +0.05 | **harms** +0.01 |
| oc25 | octave capacity 25% | base | **harms** +0.24 | **harms** +0.41 | **harms** +0.13 | **harms** +0.60 | **harms** -0.01 | **harms** +0.25 | **harms** +0.01 | **harms** +0.14 | **harms** +0.25 |
| oc50 | octave capacity 50% | base | **harms** +0.19 | **harms** +0.30 | **harms** +0.10 | **harms** +0.37 | **harms** -0.00 | **harms** +0.19 | **harms** +0.01 | **harms** +0.08 | **harms** +0.19 |
| oc100 | octave capacity 100% | base | **harms** +0.13 | **harms** +0.16 | **harms** +0.06 | **harms** +0.15 | no move +0.00 | **harms** +0.10 | no move +0.00 | **harms** +0.02 | **harms** +0.13 |
| no2 | 2 octaves | base | **harms** -0.16 | **harms** +0.11 | **harms** -0.05 | **harms** +0.43 | **harms** -0.03 | **harms** +0.05 | **harms** +0.02 | **harms** +0.14 | **harms** -0.22 |
| no4 | 4 octaves | base | no move -0.05 | no move +0.00 | no move -0.01 | **harms** +0.23 | **harms** -0.02 | no move +0.01 | **harms** +0.01 | **harms** +0.08 | no move -0.09 |
| no6 | 6 octaves | base | no move -0.01 | no move -0.21 | no move -0.01 | no move -0.03 | no move +0.00 | no move -0.09 | no move +0.00 | no move -0.02 | no move -0.01 |
| phi0 | Phi tier off | base | **harms** +0.07 | **harms** +0.02 | **harms** +0.02 | **harms** +0.04 | no move +0.01 | no move +0.00 | no move -0.01 | **harms** +0.02 | **harms** +0.07 |
| ph5 | phase-in over 5 years | base | **harms** +0.19 | no move -0.52 | **works** -0.43 | **works** -3.00 | no move +0.02 | no move -0.33 | **works** -0.08 | **works** -1.33 | **works** -0.82 |
| ph10 | phase-in over 10 years | base | **harms** +0.74 | **works** -1.46 | **harms** -0.55 | **works** -6.91 | no move +0.06 | no move -1.00 | **works** -0.14 | **works** -2.53 | **works** -1.53 |
| cap2 | issuance cap 2% | base | **harms** +9.51 | **harms** -3.30 | **harms** +3.25 | **works** -23.86 | no move +0.15 | **harms** -4.39 | **harms** +0.22 | **harms** -2.11 | **harms** +5.08 |
| cap4 | issuance cap 4% | base | **harms** +9.51 | **harms** -3.30 | **harms** +3.25 | **works** -23.86 | no move +0.15 | **harms** -4.39 | **harms** +0.22 | **harms** -2.11 | **harms** +5.08 |
| cap8 | issuance cap 8% | base | **harms** +9.51 | **harms** -3.30 | **harms** +3.25 | **works** -23.86 | no move +0.15 | **harms** -4.39 | **harms** +0.22 | **harms** -2.11 | **harms** +5.08 |
| ixs | indexation: surge protocol (5%) | base | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 |
| ixy | indexation: every year, price level | base | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 |
| ixn | indexation: every year, basic needs | base | **harms** -0.31 | **harms** +0.12 | **harms** -0.84 | **harms** +0.96 | **works** +0.57 | **harms** +0.09 | **harms** +0.20 | **harms** -0.37 | **harms** -0.24 |
| sva | protected account, all savings | base | **harms** +29.19 | **works** -52.09 | **harms** +19.86 | **harms** +3012.14 | no move +0.15 | **works** -50.01 | **works** -1.08 | **works** -33.98 | **works** -12.80 |
| svc | protected account, first $10,000 | base | **harms** +4.34 | **works** -17.53 | **harms** +3.18 | **harms** +21.68 | no move +0.05 | **works** -9.50 | **harms** +0.07 | **works** -5.61 | **works** -8.57 |
| rcap | rent cap for BU tenants | base | **works** -0.30 | no move -0.01 | **works** -0.16 | **harms** -0.15 | **harms** -0.01 | no move -0.01 | **harms** +0.01 | **works** -0.13 | **works** -0.23 |
| hc | rent risk ($1.41 a BU dollar) | base | **harms** +5.91 | **harms** +0.87 | **harms** +4.55 | **harms** +1.30 | no move +0.09 | **harms** +0.48 | **harms** +1.81 | **harms** +2.28 | **harms** +4.05 |
| hcrc | rent risk and rent cap | base | **harms** +1.43 | **harms** -0.09 | **harms** +4.41 | **works** -1.07 | **harms** -0.01 | **harms** +0.05 | **harms** +6.52 | **harms** +1.24 | **harms** +0.73 |

### Verdicts: C2.2 design, wages 100%

| Row | What it sets | vs | basket poverty, % of adult-years | wealth poverty at year 20, % | non-participants' basket poverty, % | programme inflation, points a year | participation, mean of years 1-19, % | non-participants' wealth poverty, % | non-participants' income drops of 25%+ with no buffer, per 100 | non-participants under 3 months of basics covered, % | below 30 days of basic living, design-neutral, % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| asis | today's joining rule | base | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 |
| t0 | tax 0% | base | **works** -0.66 | **works** -6.07 | **works** -0.65 | **works** -2.31 | no move +0.00 | **works** -5.92 | **harms** +2.59 | **works** -2.70 | **works** -0.04 |
| t4 | tax 4% | base | **works** -0.60 | **works** -5.29 | **works** -0.60 | **works** -1.70 | no move +0.00 | **works** -5.22 | **harms** +0.72 | **works** -2.22 | **works** -0.03 |
| t8 | tax 8% | base | **works** -0.43 | **works** -3.83 | **works** -0.43 | **works** -1.04 | no move +0.00 | **works** -3.76 | **harms** +0.26 | **works** -1.57 | **works** -0.02 |
| t12 | tax 12% | base | no move -0.20 | no move -1.84 | no move -0.21 | no move -0.39 | no move +0.00 | no move -1.92 | **harms** +0.04 | no move -0.77 | no move -0.01 |
| t16 | tax 16% | base | **harms** +0.09 | **harms** +0.57 | **harms** +0.07 | **harms** +0.23 | no move +0.00 | **harms** +0.43 | **harms** -0.08 | **harms** +0.24 | **harms** +0.00 |
| t20 | tax 20% | base | **harms** +0.42 | **harms** +3.37 | **harms** +0.40 | **harms** +0.81 | no move +0.00 | **harms** +3.31 | no move -0.12 | **harms** +1.45 | **harms** +0.02 |
| t25 | tax 25% | base | **harms** +0.92 | **harms** +7.00 | **harms** +0.92 | **harms** +1.46 | no move +0.00 | **harms** +6.93 | no move -0.16 | **harms** +3.20 | **harms** +0.04 |
| t30 | tax 30% | base | **harms** +1.50 | **harms** +10.79 | **harms** +1.49 | **harms** +1.96 | no move +0.00 | **harms** +10.76 | no move -0.14 | **harms** +5.21 | **harms** +0.08 |
| t40 | tax 40% | base | **harms** +3.02 | **harms** +17.48 | **harms** +3.02 | **harms** +1.93 | no move +0.00 | **harms** +17.34 | **harms** -0.07 | **harms** +9.32 | **harms** +0.25 |
| asis.t0 | tax 0%, today's rule | asis | **works** -0.66 | **works** -6.07 | **works** -0.65 | **works** -2.31 | no move +0.00 | **works** -5.92 | **harms** +2.59 | **works** -2.70 | **works** -0.04 |
| asis.t4 | tax 4%, today's rule | asis | **works** -0.60 | **works** -5.29 | **works** -0.60 | **works** -1.70 | no move +0.00 | **works** -5.22 | **harms** +0.72 | **works** -2.22 | **works** -0.03 |
| asis.t8 | tax 8%, today's rule | asis | **works** -0.43 | **works** -3.83 | **works** -0.43 | **works** -1.04 | no move +0.00 | **works** -3.76 | **harms** +0.26 | **works** -1.57 | **works** -0.02 |
| asis.t12 | tax 12%, today's rule | asis | no move -0.20 | no move -1.84 | no move -0.21 | no move -0.39 | no move +0.00 | no move -1.92 | **harms** +0.04 | no move -0.77 | no move -0.01 |
| asis.t16 | tax 16%, today's rule | asis | **harms** +0.09 | **harms** +0.57 | **harms** +0.07 | **harms** +0.23 | no move +0.00 | **harms** +0.43 | **harms** -0.08 | **harms** +0.24 | **harms** +0.00 |
| asis.t20 | tax 20%, today's rule | asis | **harms** +0.42 | **harms** +3.37 | **harms** +0.40 | **harms** +0.81 | no move +0.00 | **harms** +3.31 | no move -0.12 | **harms** +1.45 | **harms** +0.02 |
| asis.t25 | tax 25%, today's rule | asis | **harms** +0.92 | **harms** +7.00 | **harms** +0.92 | **harms** +1.46 | no move +0.00 | **harms** +6.93 | no move -0.16 | **harms** +3.20 | **harms** +0.04 |
| asis.t30 | tax 30%, today's rule | asis | **harms** +1.50 | **harms** +10.79 | **harms** +1.49 | **harms** +1.96 | no move +0.00 | **harms** +10.76 | no move -0.14 | **harms** +5.21 | **harms** +0.08 |
| asis.t40 | tax 40%, today's rule | asis | **harms** +3.02 | **harms** +17.48 | **harms** +3.02 | **harms** +1.93 | no move +0.00 | **harms** +17.34 | **harms** -0.07 | **harms** +9.32 | **harms** +0.25 |
| pr0c75 | progression 0 pts, cap 75% | base | **works** -0.18 | **works** -2.02 | **works** -0.17 | **works** -1.13 | no move +0.00 | **works** -1.89 | **harms** +0.01 | **works** -0.74 | **works** -0.01 |
| pr8c75 | progression 8 pts, cap 75% | base | **harms** +0.22 | **harms** +3.00 | **harms** +0.22 | **harms** +1.07 | no move +0.00 | **harms** +2.88 | **harms** -0.00 | **harms** +0.95 | **harms** +0.01 |
| pr0c50 | progression 0 pts, cap 50% | base | **works** -0.18 | **works** -2.02 | **works** -0.17 | **works** -1.13 | no move +0.00 | **works** -1.89 | **harms** +0.01 | **works** -0.74 | **works** -0.01 |
| pr4c50 | progression 4 pts, cap 50% | base | no move -0.00 | no move -0.02 | no move -0.00 | no move -0.03 | no move +0.00 | no move -0.01 | no move +0.00 | no move -0.00 | no move +0.00 |
| pr8c50 | progression 8 pts, cap 50% | base | **harms** +0.19 | **harms** +2.33 | **harms** +0.19 | **harms** +0.69 | no move +0.00 | **harms** +2.26 | no move -0.00 | **harms** +0.78 | **harms** +0.01 |
| bt0 | business tax 0% | base | **works** -0.48 | **works** -3.72 | **works** -0.46 | **works** -1.13 | no move +0.00 | **works** -3.59 | **harms** +1.29 | **works** -1.84 | **works** -0.02 |
| bt25 | business tax 25% | base | **harms** +0.64 | **harms** +4.33 | **harms** +0.63 | **harms** +0.92 | no move +0.00 | **harms** +4.26 | **works** -0.16 | **harms** +2.13 | **harms** +0.03 |
| bt50 | business tax 50% | base | **harms** +3.75 | **harms** +17.10 | **harms** +3.75 | **harms** +0.34 | no move +0.00 | **harms** +16.91 | **harms** -0.04 | **harms** +10.52 | **harms** +0.33 |
| bt75 | business tax 75% | base | **harms** +9.84 | **harms** +27.33 | **harms** +9.63 | **works** -3.41 | no move +0.00 | **harms** +27.11 | **harms** +0.30 | **harms** +19.02 | **harms** +1.79 |
| kp10 | Source keeps 10% of project sales | base | **works** -0.06 | **works** -1.08 | **works** -0.05 | **works** -1.82 | no move +0.00 | **works** -0.99 | no move -0.00 | **works** -0.43 | no move -0.00 |
| kp25 | Source keeps 25% of project sales | base | **works** -0.14 | **works** -2.76 | **works** -0.13 | **works** -4.65 | no move +0.00 | **works** -2.61 | **harms** +0.01 | **works** -1.03 | no move -0.00 |
| kp50 | Source keeps 50% of project sales | base | **works** -0.26 | **works** -5.28 | **works** -0.25 | **works** -9.68 | no move +0.00 | **works** -5.15 | **harms** +0.06 | **works** -1.92 | no move -0.00 |
| ex50 | 50% of expired BU recycled | base | **harms** +1.43 | **harms** +12.87 | **harms** +1.44 | **harms** +4.27 | no move +0.00 | **harms** +12.83 | **harms** -0.08 | **harms** +5.58 | **harms** +0.10 |
| ex0 | 0% of expired BU recycled | base | **harms** +4.23 | **harms** +26.32 | **harms** +4.24 | **harms** +9.02 | no move +0.00 | **harms** +26.22 | **harms** +0.04 | **harms** +12.17 | **harms** +1.72 |
| fprog | outside finance: progressive income tax | base | **harms** +7.80 | **harms** +41.65 | **harms** +7.52 | **works** -4.19 | no move +0.00 | **harms** +41.56 | **harms** +1.27 | **harms** +19.39 | **harms** +0.03 |
| fland | outside finance: land-value tax | base | **harms** +8.84 | **works** -7.97 | **harms** +8.84 | **works** -37.32 | no move +0.00 | **works** -7.74 | **harms** +2.69 | **works** -3.69 | **harms** +0.01 |
| fflat | outside finance: flat wage contribution | base | **harms** +7.75 | **harms** -5.48 | **harms** +7.54 | **works** -42.62 | no move +0.00 | **harms** -5.47 | **harms** +3.75 | **harms** -0.40 | **harms** +0.20 |
| br1 | business rate 1x | base | **harms** +9.62 | **harms** +26.61 | **harms** +9.43 | **works** -3.83 | no move +0.00 | **harms** +26.32 | **harms** +0.26 | **harms** +18.62 | **harms** +1.77 |
| br15 | business rate 1.5x | base | **harms** +6.22 | **harms** +21.85 | **harms** +6.16 | **works** -1.70 | no move +0.00 | **harms** +21.77 | **harms** +0.09 | **harms** +14.67 | **harms** +1.00 |
| br2 | business rate 2x | base | **harms** +3.14 | **harms** +15.43 | **harms** +3.14 | **harms** +0.72 | no move +0.00 | **harms** +15.33 | **harms** -0.07 | **harms** +9.16 | **harms** +0.24 |
| bu60 | 60% of the BU | base | **harms** +10.67 | **harms** +25.63 | **harms** +10.51 | **works** -3.05 | no move +0.00 | **harms** +25.60 | **harms** +0.19 | **harms** +19.68 | **harms** +9.19 |
| bu80 | 80% of the BU | base | **harms** +3.81 | **harms** +17.00 | **harms** +3.82 | **harms** +2.24 | no move +0.00 | **harms** +16.88 | **harms** -0.01 | **harms** +10.55 | **harms** +1.55 |
| mm3 | top multiplier 3 | base | **harms** +1.21 | **harms** +11.04 | **harms** +1.22 | **harms** +2.80 | no move +0.00 | **harms** +10.93 | **harms** -0.05 | **harms** +4.73 | **harms** +0.08 |
| mm6 | top multiplier 6 | base | **harms** +0.27 | **harms** +2.88 | **harms** +0.25 | **harms** +0.74 | no move +0.00 | **harms** +2.84 | no move -0.05 | **harms** +1.03 | **harms** +0.02 |
| mm9 | top multiplier 9 | base | no move -0.20 | no move -2.42 | no move -0.20 | no move -0.46 | no move +0.00 | no move -2.49 | **harms** +0.01 | no move -0.86 | no move -0.01 |
| oc25 | octave capacity 25% | base | **harms** +1.93 | **harms** +23.15 | **harms** +1.94 | **harms** +3.00 | no move +0.00 | **harms** +23.06 | **harms** +0.44 | **harms** +4.80 | **harms** +0.46 |
| oc50 | octave capacity 50% | base | **harms** +1.58 | **harms** +21.04 | **harms** +1.58 | **harms** +2.62 | no move +0.00 | **harms** +20.95 | **harms** +0.31 | **harms** +3.83 | **harms** +0.31 |
| oc100 | octave capacity 100% | base | **harms** +1.23 | **harms** +18.03 | **harms** +1.25 | **harms** +2.24 | no move +0.00 | **harms** +18.08 | **harms** +0.18 | **harms** +3.00 | **harms** +0.19 |
| no2 | 2 octaves | base | **works** -0.39 | **works** -0.28 | **works** -0.39 | **works** -1.75 | no move +0.00 | **works** -0.22 | **harms** +0.07 | **works** -1.24 | **works** -0.08 |
| no4 | 4 octaves | base | no move -0.17 | no move -0.18 | no move -0.17 | no move -0.75 | no move +0.00 | no move -0.12 | no move -0.04 | no move -0.51 | no move -0.03 |
| no6 | 6 octaves | base | **harms** +0.10 | **harms** +0.11 | **harms** +0.11 | **harms** +0.27 | no move +0.00 | **harms** +0.12 | **harms** +0.02 | **harms** +0.36 | **harms** +0.02 |
| phi0 | Phi tier off | base | **harms** +0.17 | **harms** +1.82 | **harms** +0.16 | **harms** +0.59 | no move +0.00 | **harms** +1.82 | no move -0.01 | **harms** +0.67 | **harms** +0.01 |
| ph5 | phase-in over 5 years | base | **harms** +0.63 | no move -0.03 | **harms** +0.61 | **works** -0.29 | no move +0.00 | no move -0.04 | **works** -0.32 | **harms** +1.37 | **harms** +0.10 |
| ph10 | phase-in over 10 years | base | **harms** +1.65 | **harms** +0.06 | **harms** +1.62 | **works** -0.71 | no move +0.00 | **harms** +0.06 | **works** -0.30 | **harms** +3.83 | **harms** +0.23 |
| cap2 | issuance cap 2% | base | **harms** +10.95 | **harms** +29.68 | **harms** +10.69 | **works** -5.42 | no move +0.00 | **harms** +29.30 | **harms** +0.98 | **harms** +19.81 | **harms** +2.17 |
| cap4 | issuance cap 4% | base | **harms** +10.95 | **harms** +29.68 | **harms** +10.69 | **works** -5.42 | no move +0.00 | **harms** +29.30 | **harms** +0.98 | **harms** +19.81 | **harms** +2.17 |
| cap8 | issuance cap 8% | base | **harms** +10.95 | **harms** +29.68 | **harms** +10.69 | **works** -5.42 | no move +0.00 | **harms** +29.30 | **harms** +0.98 | **harms** +19.81 | **harms** +2.17 |
| ixs | indexation: surge protocol (5%) | base | **harms** +0.46 | **harms** +3.17 | **harms** +0.45 | **harms** +0.95 | no move +0.00 | **harms** +3.05 | **harms** +0.07 | **harms** +1.54 | **harms** +0.10 |
| ixy | indexation: every year, price level | base | **harms** +0.46 | **harms** +3.17 | **harms** +0.45 | **harms** +0.95 | no move +0.00 | **harms** +3.05 | **harms** +0.07 | **harms** +1.54 | **harms** +0.10 |
| ixn | indexation: every year, basic needs | base | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 |
| sva | protected account, all savings | base | **harms** +11.30 | **harms** +0.56 | **harms** +11.06 | **harms** +885.71 | no move +0.00 | **harms** +0.66 | **works** -0.70 | **harms** +1.89 | **harms** +1.59 |
| svc | protected account, first $10,000 | base | **harms** +0.21 | **works** -7.40 | **harms** +0.20 | **harms** +5.79 | no move +0.00 | **works** -7.19 | **harms** +0.03 | **works** -3.07 | **works** -0.01 |
| rcap | rent cap for BU tenants | base | **works** -0.26 | **works** -1.91 | **works** -0.26 | **works** -1.49 | no move +0.00 | **works** -1.83 | no move -0.01 | **works** -0.93 | **works** -0.02 |
| hc | rent risk ($1.41 a BU dollar) | base | **harms** +4.71 | **harms** +19.50 | **harms** +4.67 | **harms** +9.91 | no move +0.00 | **harms** +19.45 | **harms** -0.01 | **harms** +13.39 | **harms** +0.57 |
| hcrc | rent risk and rent cap | base | **works** -0.26 | **works** -1.91 | **works** -0.26 | **works** -1.49 | no move +0.00 | **works** -1.83 | no move -0.01 | **works** -0.93 | **works** -0.02 |

### Verdicts: C2.2 design, wages 90%

| Row | What it sets | vs | basket poverty, % of adult-years | wealth poverty at year 20, % | non-participants' basket poverty, % | programme inflation, points a year | participation, mean of years 1-19, % | non-participants' wealth poverty, % | non-participants' income drops of 25%+ with no buffer, per 100 | non-participants under 3 months of basics covered, % | below 30 days of basic living, design-neutral, % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| asis | today's joining rule | base | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 |
| t0 | tax 0% | base | **works** -1.95 | **works** -22.66 | **works** -1.92 | **works** -4.96 | no move +0.00 | **works** -22.57 | **harms** +2.80 | **works** -8.09 | **works** -0.07 |
| t4 | tax 4% | base | **works** -1.74 | **works** -17.05 | **works** -1.72 | **works** -3.68 | no move +0.00 | **works** -16.73 | **harms** +0.89 | **works** -6.51 | **works** -0.06 |
| t8 | tax 8% | base | **works** -1.25 | **works** -10.25 | **works** -1.24 | **works** -2.29 | no move +0.00 | **works** -10.14 | **harms** +0.34 | **works** -4.36 | **works** -0.04 |
| t12 | tax 12% | base | no move -0.57 | no move -3.15 | no move -0.57 | no move -0.88 | no move +0.00 | no move -3.16 | **harms** +0.06 | no move -1.81 | no move -0.03 |
| t16 | tax 16% | base | **harms** +0.22 | **harms** +3.71 | **harms** +0.22 | **harms** +0.52 | no move +0.00 | **harms** +3.77 | **harms** -0.09 | **harms** +1.02 | **harms** -0.00 |
| t20 | tax 20% | base | **harms** +1.13 | **harms** +9.53 | **harms** +1.11 | **harms** +1.89 | no move +0.00 | **harms** +9.74 | **works** -0.18 | **harms** +4.01 | **harms** +0.04 |
| t25 | tax 25% | base | **harms** +2.46 | **harms** +16.01 | **harms** +2.46 | **harms** +3.47 | no move +0.00 | **harms** +16.12 | **works** -0.21 | **harms** +7.75 | **harms** +0.15 |
| t30 | tax 30% | base | **harms** +3.96 | **harms** +20.83 | **harms** +3.93 | **harms** +4.68 | no move +0.00 | **harms** +20.86 | no move -0.21 | **harms** +11.21 | **harms** +0.39 |
| t40 | tax 40% | base | **harms** +7.23 | **harms** +26.88 | **harms** +7.15 | **harms** +5.07 | no move +0.00 | **harms** +27.04 | no move -0.16 | **harms** +16.45 | **harms** +1.50 |
| asis.t0 | tax 0%, today's rule | asis | **works** -1.95 | **works** -22.66 | **works** -1.92 | **works** -4.96 | no move +0.00 | **works** -22.57 | **harms** +2.80 | **works** -8.09 | **works** -0.07 |
| asis.t4 | tax 4%, today's rule | asis | **works** -1.74 | **works** -17.05 | **works** -1.72 | **works** -3.68 | no move +0.00 | **works** -16.73 | **harms** +0.89 | **works** -6.51 | **works** -0.06 |
| asis.t8 | tax 8%, today's rule | asis | **works** -1.25 | **works** -10.25 | **works** -1.24 | **works** -2.29 | no move +0.00 | **works** -10.14 | **harms** +0.34 | **works** -4.36 | **works** -0.04 |
| asis.t12 | tax 12%, today's rule | asis | no move -0.57 | no move -3.15 | no move -0.57 | no move -0.88 | no move +0.00 | no move -3.16 | **harms** +0.06 | no move -1.81 | no move -0.03 |
| asis.t16 | tax 16%, today's rule | asis | **harms** +0.22 | **harms** +3.71 | **harms** +0.22 | **harms** +0.52 | no move +0.00 | **harms** +3.77 | **harms** -0.09 | **harms** +1.02 | **harms** -0.00 |
| asis.t20 | tax 20%, today's rule | asis | **harms** +1.13 | **harms** +9.53 | **harms** +1.11 | **harms** +1.89 | no move +0.00 | **harms** +9.74 | **works** -0.18 | **harms** +4.01 | **harms** +0.04 |
| asis.t25 | tax 25%, today's rule | asis | **harms** +2.46 | **harms** +16.01 | **harms** +2.46 | **harms** +3.47 | no move +0.00 | **harms** +16.12 | **works** -0.21 | **harms** +7.75 | **harms** +0.15 |
| asis.t30 | tax 30%, today's rule | asis | **harms** +3.96 | **harms** +20.83 | **harms** +3.93 | **harms** +4.68 | no move +0.00 | **harms** +20.86 | no move -0.21 | **harms** +11.21 | **harms** +0.39 |
| asis.t40 | tax 40%, today's rule | asis | **harms** +7.23 | **harms** +26.88 | **harms** +7.15 | **harms** +5.07 | no move +0.00 | **harms** +27.04 | no move -0.16 | **harms** +16.45 | **harms** +1.50 |
| pr0c75 | progression 0 pts, cap 75% | base | **works** -0.63 | **works** -8.83 | **works** -0.63 | **works** -2.26 | no move +0.00 | **works** -8.73 | **harms** +0.04 | **works** -2.56 | **works** -0.02 |
| pr8c75 | progression 8 pts, cap 75% | base | **harms** +0.80 | **harms** +8.49 | **harms** +0.82 | **harms** +2.18 | no move +0.00 | **harms** +8.52 | **harms** -0.02 | **harms** +3.18 | **harms** +0.03 |
| pr0c50 | progression 0 pts, cap 50% | base | **works** -0.63 | **works** -8.83 | **works** -0.63 | **works** -2.26 | no move +0.00 | **works** -8.73 | **harms** +0.04 | **works** -2.56 | **works** -0.02 |
| pr4c50 | progression 4 pts, cap 50% | base | no move -0.01 | no move -0.16 | no move -0.01 | no move -0.05 | no move +0.00 | no move -0.16 | no move +0.00 | no move -0.03 | no move +0.00 |
| pr8c50 | progression 8 pts, cap 50% | base | **harms** +0.62 | **harms** +6.00 | **harms** +0.64 | **harms** +1.40 | no move +0.00 | **harms** +6.05 | no move -0.02 | **harms** +2.33 | **harms** +0.02 |
| bt0 | business tax 0% | base | **works** -1.38 | **works** -12.52 | **works** -1.36 | **works** -2.63 | no move +0.00 | **works** -12.29 | **harms** +1.44 | **works** -5.18 | **works** -0.05 |
| bt25 | business tax 25% | base | **harms** +1.64 | **harms** +11.03 | **harms** +1.62 | **harms** +2.19 | no move +0.00 | **harms** +11.28 | **works** -0.22 | **harms** +5.24 | **harms** +0.08 |
| bt50 | business tax 50% | base | **harms** +8.04 | **harms** +25.34 | **harms** +7.96 | **harms** +2.09 | no move +0.00 | **harms** +25.60 | **harms** -0.13 | **harms** +16.62 | **harms** +1.53 |
| bt75 | business tax 75% | base | **harms** +17.79 | **harms** +31.91 | **harms** +17.55 | **harms** -2.26 | no move +0.00 | **harms** +32.19 | **harms** +0.23 | **harms** +24.55 | **harms** +5.33 |
| kp10 | Source keeps 10% of project sales | base | **works** -0.27 | **works** -4.40 | **works** -0.27 | **works** -2.56 | no move +0.00 | **works** -4.37 | no move +0.00 | **works** -1.40 | no move -0.01 |
| kp25 | Source keeps 25% of project sales | base | **works** -0.66 | **works** -11.32 | **works** -0.65 | **works** -6.57 | no move +0.00 | **works** -11.23 | **harms** +0.02 | **works** -3.53 | no move -0.01 |
| kp50 | Source keeps 50% of project sales | base | **works** -1.29 | **works** -23.28 | **works** -1.25 | **works** -13.69 | no move +0.00 | **works** -22.96 | **harms** +0.10 | **works** -6.70 | **works** -0.03 |
| ex50 | 50% of expired BU recycled | base | **harms** +4.11 | **harms** +22.37 | **harms** +4.11 | **harms** +8.13 | no move +0.00 | **harms** +22.37 | no move -0.16 | **harms** +11.80 | **harms** +0.66 |
| ex0 | 0% of expired BU recycled | base | **harms** +10.56 | **harms** +34.97 | **harms** +10.50 | **harms** +17.23 | no move +0.00 | **harms** +35.32 | **harms** -0.07 | **harms** +21.24 | **harms** +5.91 |
| fprog | outside finance: progressive income tax | base | **harms** +19.31 | **harms** +41.53 | **harms** +19.04 | **harms** +2.09 | no move +0.00 | **harms** +42.09 | **harms** +1.44 | **harms** +27.96 | **harms** +1.17 |
| fland | outside finance: land-value tax | base | **harms** +8.07 | **works** -43.40 | **harms** +8.12 | **works** -48.95 | no move +0.00 | **works** -42.86 | **harms** +3.27 | **works** -11.93 | no move -0.03 |
| fflat | outside finance: flat wage contribution | base | **harms** +5.21 | **works** -41.15 | **harms** +5.08 | **works** -54.67 | no move +0.00 | **works** -40.81 | **harms** +3.80 | **works** -8.82 | **harms** +0.15 |
| br1 | business rate 1x | base | **harms** +17.39 | **harms** +31.41 | **harms** +17.15 | **works** -3.02 | no move +0.00 | **harms** +31.70 | **harms** +0.19 | **harms** +24.07 | **harms** +5.22 |
| br15 | business rate 1.5x | base | **harms** +12.37 | **harms** +28.67 | **harms** +12.17 | **harms** -0.38 | no move +0.00 | **harms** +28.94 | **harms** +0.01 | **harms** +20.57 | **harms** +3.31 |
| br2 | business rate 2x | base | **harms** +6.90 | **harms** +23.93 | **harms** +6.84 | **harms** +2.50 | no move +0.00 | **harms** +24.13 | **harms** -0.16 | **harms** +15.18 | **harms** +1.15 |
| bu60 | 60% of the BU | base | **harms** +18.31 | **harms** +26.57 | **harms** +18.12 | **works** -4.05 | no move +0.00 | **harms** +26.78 | **harms** +0.16 | **harms** +24.33 | **harms** +16.99 |
| bu80 | 80% of the BU | base | **harms** +8.44 | **harms** +24.09 | **harms** +8.35 | **harms** +4.08 | no move +0.00 | **harms** +24.24 | **harms** -0.07 | **harms** +16.88 | **harms** +4.48 |
| mm3 | top multiplier 3 | base | **harms** +3.59 | **harms** +20.89 | **harms** +3.58 | **harms** +6.19 | no move +0.00 | **harms** +20.83 | no move -0.12 | **harms** +10.74 | **harms** +0.41 |
| mm6 | top multiplier 6 | base | **harms** +0.82 | **harms** +8.41 | **harms** +0.80 | **harms** +1.68 | no move +0.00 | **harms** +8.58 | no move -0.08 | **harms** +3.23 | **harms** +0.03 |
| mm9 | top multiplier 9 | base | no move -0.61 | no move -2.82 | no move -0.61 | no move -0.97 | no move +0.00 | no move -2.82 | **harms** +0.01 | no move -1.97 | no move -0.03 |
| oc25 | octave capacity 25% | base | **harms** +5.99 | **harms** +29.71 | **harms** +5.94 | **harms** +7.31 | no move +0.00 | **harms** +30.09 | **harms** +0.46 | **harms** +10.06 | **harms** +2.85 |
| oc50 | octave capacity 50% | base | **harms** +5.27 | **harms** +28.34 | **harms** +5.24 | **harms** +6.49 | no move +0.00 | **harms** +28.70 | **harms** +0.32 | **harms** +8.59 | **harms** +2.36 |
| oc100 | octave capacity 100% | base | **harms** +4.50 | **harms** +26.18 | **harms** +4.50 | **harms** +5.60 | no move +0.00 | **harms** +26.41 | **harms** +0.18 | **harms** +7.16 | **harms** +1.88 |
| no2 | 2 octaves | base | **works** -0.63 | **works** -1.86 | **works** -0.62 | **works** -2.30 | no move +0.00 | **works** -1.83 | **harms** +0.12 | **works** -2.33 | **works** -0.11 |
| no4 | 4 octaves | base | no move -0.27 | no move -0.95 | no move -0.28 | no move -0.92 | no move +0.00 | no move -0.99 | no move -0.05 | no move -1.06 | no move -0.04 |
| no6 | 6 octaves | base | **harms** +0.17 | **harms** +0.24 | **harms** +0.17 | **harms** +0.35 | no move +0.00 | **harms** +0.23 | **harms** +0.02 | **harms** +0.50 | **harms** +0.03 |
| phi0 | Phi tier off | base | **harms** +0.51 | **harms** +3.58 | **harms** +0.51 | **harms** +1.15 | no move +0.00 | **harms** +3.49 | no move -0.02 | **harms** +1.69 | **harms** +0.04 |
| ph5 | phase-in over 5 years | base | **harms** +0.66 | no move -0.13 | **harms** +0.65 | **works** -0.39 | no move +0.00 | no move -0.14 | **works** -0.40 | **harms** +1.53 | **harms** +0.12 |
| ph10 | phase-in over 10 years | base | **harms** +1.96 | **harms** -0.08 | **harms** +1.92 | **works** -0.78 | no move +0.00 | **harms** -0.15 | **works** -0.37 | **harms** +4.64 | **harms** +0.31 |
| cap2 | issuance cap 2% | base | **harms** +19.63 | **harms** +32.97 | **harms** +19.32 | **works** -3.54 | no move +0.00 | **harms** +33.28 | **harms** +1.10 | **harms** +25.83 | **harms** +6.48 |
| cap4 | issuance cap 4% | base | **harms** +19.63 | **harms** +32.97 | **harms** +19.32 | **works** -3.54 | no move +0.00 | **harms** +33.28 | **harms** +1.10 | **harms** +25.83 | **harms** +6.48 |
| cap8 | issuance cap 8% | base | **harms** +19.63 | **harms** +32.97 | **harms** +19.32 | **works** -3.54 | no move +0.00 | **harms** +33.28 | **harms** +1.10 | **harms** +25.83 | **harms** +6.48 |
| ixs | indexation: surge protocol (5%) | base | **harms** +1.12 | **harms** +6.63 | **harms** +1.11 | **harms** +1.85 | no move +0.00 | **harms** +6.70 | **harms** +0.06 | **harms** +3.48 | **harms** +0.16 |
| ixy | indexation: every year, price level | base | **harms** +1.12 | **harms** +6.63 | **harms** +1.11 | **harms** +1.85 | no move +0.00 | **harms** +6.70 | **harms** +0.06 | **harms** +3.48 | **harms** +0.16 |
| ixn | indexation: every year, basic needs | base | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 |
| sva | protected account, all savings | base | **harms** +45.03 | **harms** -25.62 | **harms** +44.85 | **harms** +2101.21 | no move +0.00 | **harms** -25.46 | **works** -0.51 | **harms** -2.10 | **harms** +3.95 |
| svc | protected account, first $10,000 | base | **harms** +2.10 | **works** -39.30 | **harms** +2.08 | **harms** +14.54 | no move +0.00 | **works** -38.91 | **harms** +0.05 | **works** -10.34 | **works** -0.03 |
| rcap | rent cap for BU tenants | base | **works** -0.70 | **works** -5.79 | **works** -0.69 | **works** -2.43 | no move +0.00 | **works** -5.82 | **harms** +0.00 | **works** -2.53 | **works** -0.03 |
| hc | rent risk ($1.41 a BU dollar) | base | **harms** +11.64 | **harms** +30.06 | **harms** +11.48 | **harms** +16.36 | no move +0.00 | **harms** +30.57 | **harms** -0.02 | **harms** +22.42 | **harms** +2.97 |
| hcrc | rent risk and rent cap | base | **works** -0.70 | **works** -5.79 | **works** -0.69 | **works** -2.43 | no move +0.00 | **works** -5.82 | **harms** +0.00 | **works** -2.53 | **works** -0.03 |

### Verdicts: release row, wages 100%, savings that keep up with prices (`.sv` twins, against `base.sv`)

| Row | What it sets | vs | basket poverty, % of adult-years | wealth poverty at year 20, % | non-participants' basket poverty, % | programme inflation, points a year | participation, mean of years 1-19, % | non-participants' wealth poverty, % | non-participants' income drops of 25%+ with no buffer, per 100 | non-participants under 3 months of basics covered, % | below 30 days of basic living, design-neutral, % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| asis.sv | today's joining rule | base.sv | no move -0.10 | no move -0.08 | no move -0.35 | **harms** +0.14 | no move +0.22 | no move -0.29 | no move -0.08 | no move -0.22 | no move -0.04 |
| t0.sv | tax 0% | base.sv | **works** -2.55 | **works** -1.69 | **works** -2.06 | **harms** +2.76 | **works** +0.46 | **works** -1.34 | no move -0.02 | **works** -1.05 | **works** -1.11 |
| t4.sv | tax 4% | base.sv | **works** -1.77 | **works** -1.11 | **works** -1.37 | **harms** +2.02 | **works** +0.28 | **works** -0.85 | no move -0.01 | **works** -0.68 | **works** -0.76 |
| t8.sv | tax 8% | base.sv | **works** -1.00 | **works** -0.63 | **works** -0.78 | **harms** +1.24 | **works** +0.14 | **works** -0.45 | no move -0.01 | **works** -0.39 | **works** -0.43 |
| t12.sv | tax 12% | base.sv | no move -0.20 | no move -0.12 | no move -0.08 | **harms** +0.43 | no move +0.01 | no move -0.04 | no move +0.00 | no move -0.05 | no move -0.09 |
| t16.sv | tax 16% | base.sv | **harms** +0.60 | **harms** +0.43 | **harms** +0.41 | **harms** -0.41 | **harms** -0.13 | **harms** +0.28 | no move +0.01 | **harms** +0.16 | **harms** +0.24 |
| t20.sv | tax 20% | base.sv | **harms** +1.38 | **harms** +0.94 | **harms** +0.85 | **works** -1.26 | **harms** -0.20 | **harms** +0.47 | **harms** +0.01 | **harms** +0.38 | **harms** +0.55 |
| t25.sv | tax 25% | base.sv | **harms** +2.36 | **harms** +1.55 | **harms** +1.39 | **works** -2.32 | **harms** -0.22 | **harms** +0.72 | **harms** +0.02 | **harms** +0.61 | **harms** +0.95 |
| t30.sv | tax 30% | base.sv | **harms** +3.34 | **harms** +2.17 | **harms** +1.91 | **works** -3.46 | **harms** -0.17 | **harms** +0.91 | **harms** +0.01 | **harms** +0.84 | **harms** +1.33 |
| t40.sv | tax 40% | base.sv | **harms** +5.27 | **harms** +3.37 | **harms** +2.95 | **works** -6.26 | **harms** -0.10 | **harms** +1.57 | **harms** -0.00 | **harms** +1.31 | **harms** +2.11 |
| asis.t0.sv | tax 0%, today's rule | asis.sv | **works** -2.38 | **works** -1.56 | **works** -1.42 | **harms** +2.53 | no move +0.00 | **works** -0.81 | no move -0.00 | **works** -0.66 | **works** -1.00 |
| asis.t4.sv | tax 4%, today's rule | asis.sv | **works** -1.67 | **works** -1.05 | **works** -0.98 | **harms** +1.88 | no move +0.00 | **works** -0.59 | no move -0.00 | **works** -0.46 | **works** -0.70 |
| asis.t8.sv | tax 8%, today's rule | asis.sv | **works** -0.94 | **works** -0.61 | **works** -0.55 | **harms** +1.17 | no move +0.00 | **works** -0.32 | no move -0.01 | **works** -0.26 | **works** -0.38 |
| asis.t12.sv | tax 12%, today's rule | asis.sv | no move -0.20 | no move -0.11 | no move -0.08 | **harms** +0.43 | no move +0.00 | no move -0.04 | no move -0.00 | no move -0.05 | no move -0.09 |
| asis.t16.sv | tax 16%, today's rule | asis.sv | **harms** +0.56 | **harms** +0.40 | **harms** +0.38 | **harms** -0.36 | no move +0.00 | **harms** +0.26 | no move +0.00 | **harms** +0.17 | **harms** +0.23 |
| asis.t20.sv | tax 20%, today's rule | asis.sv | **harms** +1.34 | **harms** +0.91 | **harms** +0.86 | **works** -1.17 | no move +0.00 | **harms** +0.49 | **harms** +0.01 | **harms** +0.40 | **harms** +0.54 |
| asis.t25.sv | tax 25%, today's rule | asis.sv | **harms** +2.32 | **harms** +1.52 | **harms** +1.46 | **works** -2.23 | no move +0.00 | **harms** +0.75 | **harms** +0.02 | **harms** +0.67 | **harms** +0.94 |
| asis.t30.sv | tax 30%, today's rule | asis.sv | **harms** +3.33 | **harms** +2.18 | **harms** +2.07 | **works** -3.41 | no move +0.00 | **harms** +1.06 | **harms** +0.02 | **harms** +0.95 | **harms** +1.34 |
| asis.t40.sv | tax 40%, today's rule | asis.sv | **harms** +5.30 | **harms** +3.42 | **harms** +3.22 | **works** -6.24 | no move +0.00 | **harms** +1.76 | **harms** +0.04 | **harms** +1.47 | **harms** +2.12 |
| pr0c75.sv | progression 0 pts, cap 75% | base.sv | **works** -0.28 | no move -0.27 | **works** -0.43 | **harms** +0.14 | **works** +0.20 | no move -0.38 | no move -0.03 | **works** -0.24 | **works** -0.16 |
| pr8c75.sv | progression 8 pts, cap 75% | base.sv | **harms** +0.38 | **harms** +0.28 | **harms** +0.39 | **works** -0.32 | **harms** -0.58 | **harms** +0.26 | **harms** +0.06 | **harms** +0.14 | **harms** +0.14 |
| pr0c50.sv | progression 0 pts, cap 50% | base.sv | **works** -0.28 | no move -0.27 | **works** -0.43 | **harms** +0.14 | **works** +0.20 | no move -0.38 | no move -0.03 | **works** -0.24 | **works** -0.16 |
| pr4c50.sv | progression 4 pts, cap 50% | base.sv | no move -0.01 | no move -0.00 | no move -0.00 | no move -0.00 | no move +0.00 | no move +0.00 | no move -0.00 | no move -0.00 | no move -0.00 |
| pr8c50.sv | progression 8 pts, cap 50% | base.sv | **harms** +0.27 | **harms** +0.21 | **harms** +0.29 | **works** -0.24 | **harms** -0.44 | **harms** +0.21 | **harms** +0.04 | **harms** +0.11 | **harms** +0.11 |
| bt0.sv | business tax 0% | base.sv | **works** -2.09 | **works** -1.27 | **works** -1.10 | **harms** +2.43 | **harms** -0.09 | **works** -0.60 | **harms** +0.05 | **works** -0.49 | **works** -0.85 |
| bt25.sv | business tax 25% | base.sv | **harms** +2.07 | **harms** +1.33 | **harms** +1.16 | **works** -1.97 | no move +0.10 | **harms** +0.53 | **harms** -0.02 | **harms** +0.47 | **harms** +0.82 |
| bt50.sv | business tax 50% | base.sv | **harms** +6.42 | **harms** +3.97 | **harms** +3.55 | **works** -8.13 | no move +0.22 | **harms** +1.79 | **harms** -0.01 | **harms** +1.52 | **harms** +2.51 |
| bt75.sv | business tax 75% | base.sv | **harms** +10.49 | **harms** +6.63 | **harms** +5.66 | **works** -15.51 | no move +0.22 | **harms** +3.31 | **harms** +0.06 | **harms** +2.92 | **harms** +4.21 |
| kp10.sv | Source keeps 10% of project sales | base.sv | no move -0.02 | no move -0.00 | no move -0.02 | **works** -0.16 | no move -0.00 | no move +0.00 | no move +0.00 | no move -0.01 | no move -0.01 |
| kp25.sv | Source keeps 25% of project sales | base.sv | **works** -0.05 | no move -0.02 | **works** -0.04 | **works** -0.41 | **harms** -0.00 | no move -0.01 | no move +0.00 | **works** -0.02 | no move -0.02 |
| kp50.sv | Source keeps 50% of project sales | base.sv | **works** -0.10 | no move -0.04 | **works** -0.09 | **works** -0.82 | **harms** -0.00 | no move -0.01 | **harms** +0.00 | **works** -0.03 | no move -0.03 |
| ex50.sv | 50% of expired BU recycled | base.sv | **harms** +0.45 | **harms** +0.46 | **harms** +0.10 | **harms** +0.48 | no move +0.09 | no move +0.10 | no move -0.03 | no move +0.03 | **harms** +0.27 |
| ex0.sv | 0% of expired BU recycled | base.sv | **harms** +0.88 | **harms** +0.91 | **harms** +0.14 | **harms** +0.99 | no move +0.22 | **harms** +0.10 | no move -0.08 | **harms** +0.05 | **harms** +0.53 |
| fprog.sv | outside finance: progressive income tax | base.sv | **harms** +42.37 | **harms** +26.85 | **harms** +40.04 | **works** -14.63 | **harms** -1.09 | **harms** +30.86 | **harms** +1.91 | **harms** +19.58 | **harms** +16.62 |
| fland.sv | outside finance: land-value tax | base.sv | **harms** +14.11 | **harms** -0.24 | **harms** +14.38 | **works** -43.48 | **harms** -3.62 | **harms** +1.89 | **harms** +0.57 | **harms** +1.48 | **harms** -0.96 |
| fflat.sv | outside finance: flat wage contribution | base.sv | **harms** +38.72 | **harms** +30.41 | **harms** +36.26 | **works** -46.51 | **harms** -6.92 | **harms** +33.12 | **harms** +3.11 | **harms** +21.51 | **harms** +19.44 |
| br1.sv | business rate 1x | base.sv | **harms** +9.95 | **harms** +6.36 | **harms** +5.12 | **works** -15.87 | no move +0.22 | **harms** +2.97 | **harms** +0.01 | **harms** +2.79 | **harms** +4.10 |
| br15.sv | business rate 1.5x | base.sv | **harms** +8.07 | **harms** +5.14 | **harms** +4.24 | **works** -12.04 | no move +0.22 | **harms** +2.30 | **harms** -0.02 | **harms** +2.11 | **harms** +3.25 |
| br2.sv | business rate 2x | base.sv | **harms** +5.57 | **harms** +3.49 | **harms** +3.00 | **works** -7.16 | no move +0.21 | **harms** +1.51 | **harms** -0.04 | **harms** +1.30 | **harms** +2.19 |
| bu60.sv | 60% of the BU | base.sv | **harms** +8.98 | **harms** +5.76 | **harms** +4.22 | **works** -15.36 | no move +0.22 | **harms** +2.44 | **harms** -0.01 | **harms** +2.44 | **harms** +5.20 |
| bu80.sv | 80% of the BU | base.sv | **harms** +5.06 | **harms** +3.25 | **harms** +2.55 | **works** -6.66 | no move +0.20 | **harms** +1.25 | **harms** -0.03 | **harms** +1.18 | **harms** +2.97 |
| mm3.sv | top multiplier 3 | base.sv | **harms** +0.82 | **harms** +0.74 | **harms** +0.32 | **harms** -0.25 | no move +0.09 | **harms** +0.27 | no move -0.03 | **harms** +0.24 | **harms** +0.43 |
| mm6.sv | top multiplier 6 | base.sv | **harms** +0.29 | **harms** +0.30 | **harms** +0.10 | no move -0.05 | no move +0.04 | **harms** +0.12 | no move -0.02 | **harms** +0.09 | **harms** +0.17 |
| mm9.sv | top multiplier 9 | base.sv | no move -0.06 | no move -0.03 | no move -0.03 | **harms** +0.12 | no move +0.00 | no move -0.01 | no move +0.00 | no move -0.02 | no move -0.03 |
| oc25.sv | octave capacity 25% | base.sv | **harms** +0.04 | **harms** +0.06 | **harms** +0.02 | **harms** +0.16 | **harms** -0.02 | **harms** +0.06 | no move +0.00 | **works** -0.06 | **works** -0.09 |
| oc50.sv | octave capacity 50% | base.sv | **harms** +0.08 | **harms** +0.08 | **harms** +0.05 | **harms** +0.09 | **harms** -0.01 | **harms** +0.05 | no move +0.00 | no move -0.02 | **works** -0.03 |
| oc100.sv | octave capacity 100% | base.sv | **harms** +0.09 | **harms** +0.09 | **harms** +0.06 | **harms** +0.05 | no move +0.00 | **harms** +0.05 | no move +0.00 | **harms** +0.00 | **harms** +0.01 |
| no2.sv | 2 octaves | base.sv | no move -0.42 | **works** -0.37 | no move -0.22 | **harms** -0.00 | **harms** -0.05 | no move -0.16 | no move +0.00 | **works** -0.17 | **works** -0.29 |
| no4.sv | 4 octaves | base.sv | no move -0.20 | no move -0.18 | no move -0.12 | **harms** -0.01 | **harms** -0.03 | no move -0.10 | no move +0.01 | no move -0.06 | no move -0.12 |
| no6.sv | 6 octaves | base.sv | **harms** +0.01 | **harms** +0.02 | no move +0.00 | no move -0.01 | no move +0.00 | no move +0.01 | no move +0.00 | **harms** +0.00 | no move +0.00 |
| phi0.sv | Phi tier off | base.sv | **harms** +0.06 | **harms** +0.08 | **harms** +0.01 | **harms** +0.01 | no move +0.01 | **harms** +0.03 | no move -0.01 | **harms** +0.01 | **harms** +0.05 |
| ph5.sv | phase-in over 5 years | base.sv | **harms** +1.06 | **harms** +0.58 | **harms** +0.38 | **works** -1.79 | no move +0.02 | **harms** +0.18 | no move -0.04 | **harms** +0.51 | **harms** +0.81 |
| ph10.sv | phase-in over 10 years | base.sv | **harms** +2.54 | **harms** +1.30 | **harms** +1.10 | **works** -4.23 | no move +0.08 | **harms** +0.42 | no move -0.04 | **harms** +1.13 | **harms** +1.63 |
| cap2.sv | issuance cap 2% | base.sv | **harms** +12.02 | **harms** +8.81 | **harms** +6.42 | **works** -17.32 | no move +0.21 | **harms** +4.43 | **harms** +0.19 | **harms** +3.15 | **harms** +4.74 |
| cap4.sv | issuance cap 4% | base.sv | **harms** +12.02 | **harms** +8.81 | **harms** +6.42 | **works** -17.32 | no move +0.21 | **harms** +4.43 | **harms** +0.19 | **harms** +3.15 | **harms** +4.74 |
| cap8.sv | issuance cap 8% | base.sv | **harms** +12.02 | **harms** +8.81 | **harms** +6.42 | **works** -17.32 | no move +0.21 | **harms** +4.43 | **harms** +0.19 | **harms** +3.15 | **harms** +4.74 |
| ixs.sv | indexation: surge protocol (5%) | base.sv | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 |
| ixy.sv | indexation: every year, price level | base.sv | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 |
| ixn.sv | indexation: every year, basic needs | base.sv | **works** -1.12 | **works** -0.75 | **works** -2.11 | **harms** +1.22 | **works** +1.31 | **works** -1.40 | **harms** -0.05 | **works** -1.23 | **works** -0.64 |
| rcap.sv | rent cap for BU tenants | base.sv | **works** -0.49 | no move -0.32 | **works** -0.25 | **harms** -0.19 | **harms** -0.02 | no move -0.10 | **harms** +0.01 | **works** -0.11 | **works** -0.21 |
| hc.sv | rent risk ($1.41 a BU dollar) | base.sv | **harms** +6.06 | **harms** +3.71 | **harms** +5.54 | **harms** +0.96 | no move +0.12 | **harms** +3.17 | **harms** +0.65 | **harms** +2.55 | **harms** +2.31 |
| hcrc.sv | rent risk and rent cap | base.sv | **harms** +2.44 | **harms** +1.60 | **harms** +7.46 | **works** -0.79 | **harms** -0.02 | **harms** +5.28 | **harms** +3.15 | **harms** +4.16 | **harms** +1.08 |

### Verdicts: release row, wages 90%, savings that keep up with prices (`.sv` twins, against `base.sv`)

| Row | What it sets | vs | basket poverty, % of adult-years | wealth poverty at year 20, % | non-participants' basket poverty, % | programme inflation, points a year | participation, mean of years 1-19, % | non-participants' wealth poverty, % | non-participants' income drops of 25%+ with no buffer, per 100 | non-participants under 3 months of basics covered, % | below 30 days of basic living, design-neutral, % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| asis.sv | today's joining rule | base.sv | no move -0.02 | no move -0.05 | no move -0.18 | **harms** +0.17 | no move +0.16 | no move -0.21 | no move -0.08 | no move -0.16 | no move -0.03 |
| t0.sv | tax 0% | base.sv | **works** -2.46 | **works** -1.73 | **harms** -1.70 | **harms** +3.46 | **works** +0.38 | no move -1.14 | no move -0.01 | **works** -0.94 | **works** -1.13 |
| t4.sv | tax 4% | base.sv | **works** -1.63 | **works** -1.16 | **harms** -1.08 | **harms** +2.55 | **works** +0.24 | no move -0.72 | no move -0.00 | **works** -0.62 | **works** -0.77 |
| t8.sv | tax 8% | base.sv | **works** -0.85 | **works** -0.63 | **harms** -0.52 | **harms** +1.59 | **works** +0.11 | no move -0.36 | no move +0.01 | **works** -0.33 | **works** -0.43 |
| t12.sv | tax 12% | base.sv | no move -0.08 | no move -0.09 | **harms** +0.02 | **harms** +0.59 | no move +0.01 | no move -0.02 | no move -0.00 | no move -0.03 | no move -0.07 |
| t16.sv | tax 16% | base.sv | **harms** +0.63 | **harms** +0.47 | **harms** +0.36 | **harms** -0.45 | **harms** -0.07 | **harms** +0.25 | no move +0.00 | **harms** +0.15 | **harms** +0.25 |
| t20.sv | tax 20% | base.sv | **harms** +1.33 | **harms** +0.91 | **harms** +0.67 | **works** -1.52 | **harms** -0.11 | **harms** +0.36 | no move -0.00 | **harms** +0.33 | **harms** +0.57 |
| t25.sv | tax 25% | base.sv | **harms** +2.17 | **harms** +1.47 | **harms** +1.01 | **works** -2.99 | **harms** -0.12 | **harms** +0.61 | no move -0.00 | **harms** +0.53 | **harms** +0.96 |
| t30.sv | tax 30% | base.sv | **harms** +2.90 | **harms** +2.02 | **harms** +1.27 | **works** -4.74 | **harms** -0.11 | **harms** +0.78 | no move -0.02 | **harms** +0.71 | **harms** +1.34 |
| t40.sv | tax 40% | base.sv | **harms** +4.27 | **harms** +3.08 | **harms** +1.70 | **works** -8.77 | **harms** -0.10 | **harms** +1.31 | **harms** -0.02 | **harms** +1.12 | **harms** +2.09 |
| asis.t0.sv | tax 0%, today's rule | asis.sv | **works** -2.36 | **works** -1.62 | **harms** -1.22 | **harms** +3.14 | no move +0.00 | no move -0.72 | **harms** +0.01 | **works** -0.60 | **works** -1.05 |
| asis.t4.sv | tax 4%, today's rule | asis.sv | **works** -1.57 | **works** -1.11 | **harms** -0.77 | **harms** +2.35 | no move +0.00 | no move -0.48 | no move +0.00 | **works** -0.42 | **works** -0.71 |
| asis.t8.sv | tax 8%, today's rule | asis.sv | **works** -0.82 | **works** -0.61 | **harms** -0.36 | **harms** +1.50 | no move +0.00 | no move -0.22 | **harms** +0.00 | **works** -0.23 | **works** -0.39 |
| asis.t12.sv | tax 12%, today's rule | asis.sv | no move -0.08 | no move -0.09 | **harms** +0.02 | **harms** +0.59 | no move +0.00 | no move -0.01 | no move -0.00 | no move -0.03 | no move -0.07 |
| asis.t16.sv | tax 16%, today's rule | asis.sv | **harms** +0.62 | **harms** +0.45 | **harms** +0.38 | **harms** -0.39 | no move +0.00 | **harms** +0.27 | no move -0.00 | **harms** +0.16 | **harms** +0.25 |
| asis.t20.sv | tax 20%, today's rule | asis.sv | **harms** +1.31 | **harms** +0.89 | **harms** +0.71 | **works** -1.44 | no move +0.00 | **harms** +0.39 | no move -0.00 | **harms** +0.36 | **harms** +0.57 |
| asis.t25.sv | tax 25%, today's rule | asis.sv | **harms** +2.15 | **harms** +1.46 | **harms** +1.10 | **works** -2.92 | no move +0.00 | **harms** +0.67 | no move +0.01 | **harms** +0.58 | **harms** +0.96 |
| asis.t30.sv | tax 30%, today's rule | asis.sv | **harms** +2.89 | **harms** +2.04 | **harms** +1.40 | **works** -4.69 | no move +0.00 | **harms** +0.93 | no move +0.00 | **harms** +0.79 | **harms** +1.35 |
| asis.t40.sv | tax 40%, today's rule | asis.sv | **harms** +4.28 | **harms** +3.09 | **harms** +1.89 | **works** -8.73 | no move +0.00 | **harms** +1.46 | **harms** +0.01 | **harms** +1.23 | **harms** +2.11 |
| pr0c75.sv | progression 0 pts, cap 75% | base.sv | no move -0.26 | no move -0.24 | no move -0.32 | **harms** +0.06 | **works** +0.17 | no move -0.31 | no move -0.02 | **works** -0.21 | **works** -0.15 |
| pr8c75.sv | progression 8 pts, cap 75% | base.sv | **harms** +0.30 | **harms** +0.26 | **harms** +0.21 | **works** -0.25 | **harms** -0.38 | **harms** +0.19 | **harms** +0.05 | **harms** +0.12 | **harms** +0.12 |
| pr0c50.sv | progression 0 pts, cap 50% | base.sv | no move -0.26 | no move -0.24 | no move -0.32 | **harms** +0.06 | **works** +0.17 | no move -0.31 | no move -0.02 | **works** -0.21 | **works** -0.15 |
| pr4c50.sv | progression 4 pts, cap 50% | base.sv | no move -0.01 | no move -0.00 | no move -0.01 | no move -0.01 | no move +0.00 | no move +0.00 | no move -0.00 | no move -0.00 | no move -0.00 |
| pr8c50.sv | progression 8 pts, cap 50% | base.sv | **harms** +0.21 | **harms** +0.17 | **harms** +0.15 | **works** -0.19 | **harms** -0.29 | **harms** +0.14 | **harms** +0.04 | **harms** +0.08 | **harms** +0.09 |
| bt0.sv | business tax 0% | base.sv | **works** -2.02 | **works** -1.31 | **harms** -0.94 | **harms** +3.19 | **harms** -0.06 | no move -0.43 | **harms** +0.04 | **works** -0.42 | **works** -0.87 |
| bt25.sv | business tax 25% | base.sv | **harms** +1.93 | **harms** +1.25 | **harms** +0.87 | **works** -2.66 | no move +0.09 | **harms** +0.45 | no move -0.03 | **harms** +0.40 | **harms** +0.83 |
| bt50.sv | business tax 50% | base.sv | **harms** +4.88 | **harms** +3.40 | **harms** +1.77 | **works** -11.88 | no move +0.16 | **harms** +1.38 | **harms** -0.04 | **harms** +1.31 | **harms** +2.38 |
| bt75.sv | business tax 75% | base.sv | **harms** +7.29 | **harms** +5.80 | **harms** +2.02 | **works** -22.70 | no move +0.16 | **harms** +2.41 | **harms** +0.03 | **harms** +2.50 | **harms** +3.95 |
| kp10.sv | Source keeps 10% of project sales | base.sv | **works** -0.06 | no move -0.02 | **works** -0.05 | **works** -0.21 | no move -0.00 | no move -0.01 | no move +0.00 | **works** -0.01 | **works** -0.01 |
| kp25.sv | Source keeps 25% of project sales | base.sv | **works** -0.15 | no move -0.04 | **works** -0.12 | **works** -0.53 | **harms** -0.00 | no move -0.04 | no move +0.00 | **works** -0.03 | **works** -0.03 |
| kp50.sv | Source keeps 50% of project sales | base.sv | **works** -0.31 | no move -0.09 | **works** -0.26 | **works** -1.07 | **harms** -0.00 | no move -0.09 | no move +0.00 | **works** -0.05 | **works** -0.06 |
| ex50.sv | 50% of expired BU recycled | base.sv | **harms** +0.61 | **harms** +0.52 | **harms** +0.28 | **harms** +0.78 | no move +0.07 | **harms** +0.15 | no move -0.02 | **harms** +0.06 | **harms** +0.29 |
| ex0.sv | 0% of expired BU recycled | base.sv | **harms** +1.17 | **harms** +1.00 | **harms** +0.50 | **harms** +1.55 | no move +0.16 | **harms** +0.29 | no move -0.07 | **harms** +0.12 | **harms** +0.59 |
| fprog.sv | outside finance: progressive income tax | base.sv | **harms** +31.36 | **harms** +22.57 | **harms** +25.47 | **harms** -11.57 | **harms** -0.97 | **harms** +24.64 | **harms** +2.05 | **harms** +17.04 | **harms** +15.94 |
| fland.sv | outside finance: land-value tax | base.sv | **works** -1.59 | **works** -6.30 | no move -1.59 | **works** -59.89 | **harms** -3.60 | **works** -3.93 | **harms** +0.50 | no move -0.85 | **works** -3.68 |
| fflat.sv | outside finance: flat wage contribution | base.sv | **harms** +20.90 | **harms** +23.40 | **harms** +17.95 | **works** -63.05 | **harms** -6.98 | **harms** +25.70 | **harms** +3.02 | **harms** +18.49 | **harms** +16.33 |
| br1.sv | business rate 1x | base.sv | **harms** +6.74 | **harms** +5.53 | **harms** +1.52 | **works** -23.35 | no move +0.16 | **harms** +2.13 | **harms** -0.03 | **harms** +2.38 | **harms** +3.82 |
| br15.sv | business rate 1.5x | base.sv | **harms** +5.75 | **harms** +4.45 | **harms** +1.58 | **works** -17.63 | no move +0.16 | **harms** +1.81 | **harms** -0.05 | **harms** +1.81 | **harms** +3.04 |
| br2.sv | business rate 2x | base.sv | **harms** +4.27 | **harms** +2.99 | **harms** +1.49 | **works** -10.40 | no move +0.15 | **harms** +1.11 | **harms** -0.06 | **harms** +1.10 | **harms** +2.09 |
| bu60.sv | 60% of the BU | base.sv | **harms** +5.06 | **harms** +4.57 | **harms** +0.29 | **works** -24.27 | no move +0.16 | **harms** +1.18 | **harms** -0.06 | **harms** +1.92 | **harms** +4.55 |
| bu80.sv | 80% of the BU | base.sv | **harms** +3.41 | **harms** +2.72 | **harms** +0.86 | **works** -11.01 | no move +0.15 | **harms** +0.87 | **harms** -0.05 | **harms** +0.92 | **harms** +2.70 |
| mm3.sv | top multiplier 3 | base.sv | **harms** +1.09 | **harms** +0.88 | **harms** +0.54 | **harms** +0.21 | no move +0.08 | **harms** +0.35 | no move -0.03 | **harms** +0.32 | **harms** +0.52 |
| mm6.sv | top multiplier 6 | base.sv | **harms** +0.42 | **harms** +0.35 | **harms** +0.21 | **harms** +0.14 | no move +0.03 | **harms** +0.16 | no move -0.02 | **harms** +0.13 | **harms** +0.19 |
| mm9.sv | top multiplier 9 | base.sv | no move -0.04 | no move -0.02 | no move -0.00 | **harms** +0.13 | no move +0.00 | no move +0.01 | no move -0.00 | no move -0.01 | no move -0.02 |
| oc25.sv | octave capacity 25% | base.sv | **harms** +0.23 | **harms** +0.13 | **harms** +0.13 | **harms** +0.60 | **harms** -0.01 | **harms** +0.09 | no move +0.00 | no move -0.02 | **works** -0.08 |
| oc50.sv | octave capacity 50% | base.sv | **harms** +0.19 | **harms** +0.13 | **harms** +0.11 | **harms** +0.37 | **harms** -0.00 | **harms** +0.06 | no move +0.00 | no move +0.00 | no move -0.02 |
| oc100.sv | octave capacity 100% | base.sv | **harms** +0.12 | **harms** +0.10 | **harms** +0.06 | **harms** +0.15 | no move +0.00 | **harms** +0.04 | no move +0.00 | **harms** +0.01 | **harms** +0.01 |
| no2.sv | 2 octaves | base.sv | **harms** -0.16 | no move -0.28 | **harms** -0.05 | **harms** +0.43 | **harms** -0.03 | no move -0.02 | no move +0.01 | no move -0.10 | **works** -0.30 |
| no4.sv | 4 octaves | base.sv | no move -0.06 | no move -0.10 | no move -0.01 | **harms** +0.23 | **harms** -0.02 | no move +0.02 | **harms** +0.01 | no move -0.03 | no move -0.11 |
| no6.sv | 6 octaves | base.sv | no move -0.01 | **harms** +0.01 | no move -0.01 | no move -0.03 | no move +0.00 | no move +0.00 | no move +0.00 | **harms** +0.00 | no move +0.00 |
| phi0.sv | Phi tier off | base.sv | **harms** +0.07 | **harms** +0.07 | **harms** +0.03 | **harms** +0.04 | no move +0.01 | no move -0.01 | no move -0.01 | **harms** +0.02 | **harms** +0.05 |
| ph5.sv | phase-in over 5 years | base.sv | **harms** +0.18 | **harms** +0.37 | **works** -0.43 | **works** -3.01 | no move +0.02 | no move -0.16 | no move -0.04 | **harms** +0.35 | **harms** +0.83 |
| ph10.sv | phase-in over 10 years | base.sv | **harms** +0.73 | **harms** +0.97 | **harms** -0.55 | **works** -6.93 | no move +0.06 | no move -0.04 | **harms** -0.04 | **harms** +0.82 | **harms** +1.69 |
| cap2.sv | issuance cap 2% | base.sv | **harms** +9.51 | **harms** +8.45 | **harms** +3.26 | **works** -23.92 | no move +0.15 | **harms** +3.85 | **harms** +0.19 | **harms** +3.00 | **harms** +4.80 |
| cap4.sv | issuance cap 4% | base.sv | **harms** +9.51 | **harms** +8.45 | **harms** +3.26 | **works** -23.92 | no move +0.15 | **harms** +3.85 | **harms** +0.19 | **harms** +3.00 | **harms** +4.80 |
| cap8.sv | issuance cap 8% | base.sv | **harms** +9.51 | **harms** +8.45 | **harms** +3.26 | **works** -23.92 | no move +0.15 | **harms** +3.85 | **harms** +0.19 | **harms** +3.00 | **harms** +4.80 |
| ixs.sv | indexation: surge protocol (5%) | base.sv | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 |
| ixy.sv | indexation: every year, price level | base.sv | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 |
| ixn.sv | indexation: every year, basic needs | base.sv | **harms** -0.43 | no move -0.45 | **harms** -1.03 | **harms** +1.16 | **works** +0.72 | no move -0.93 | **harms** +0.03 | **works** -0.90 | **works** -0.48 |
| rcap.sv | rent cap for BU tenants | base.sv | **works** -0.35 | **works** -0.20 | **works** -0.18 | **harms** -0.18 | **harms** -0.01 | no move -0.08 | **harms** +0.00 | **works** -0.09 | **works** -0.19 |
| hc.sv | rent risk ($1.41 a BU dollar) | base.sv | **harms** +5.90 | **harms** +3.57 | **harms** +4.55 | **harms** +1.23 | no move +0.09 | **harms** +3.19 | **harms** +1.21 | **harms** +2.55 | **harms** +2.49 |
| hcrc.sv | rent risk and rent cap | base.sv | **harms** +1.38 | **harms** +1.36 | **harms** +4.37 | **works** -1.13 | **harms** -0.01 | **harms** +4.43 | **harms** +4.10 | **harms** +3.92 | **harms** +1.02 |

### Verdicts: C2.2 design, wages 100%, savings that keep up with prices (`.sv` twins, against `base.sv`)

| Row | What it sets | vs | basket poverty, % of adult-years | wealth poverty at year 20, % | non-participants' basket poverty, % | programme inflation, points a year | participation, mean of years 1-19, % | non-participants' wealth poverty, % | non-participants' income drops of 25%+ with no buffer, per 100 | non-participants under 3 months of basics covered, % | below 30 days of basic living, design-neutral, % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| asis.sv | today's joining rule | base.sv | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 |
| t0.sv | tax 0% | base.sv | **works** -0.66 | **works** -0.16 | **works** -0.65 | **works** -2.31 | no move +0.00 | no move -0.17 | **harms** +0.83 | **works** -0.53 | **works** -0.03 |
| t4.sv | tax 4% | base.sv | **works** -0.60 | **works** -0.15 | **works** -0.59 | **works** -1.70 | no move +0.00 | no move -0.16 | **harms** +0.42 | **works** -0.41 | **works** -0.03 |
| t8.sv | tax 8% | base.sv | **works** -0.43 | **works** -0.12 | **works** -0.43 | **works** -1.04 | no move +0.00 | no move -0.13 | **harms** +0.18 | **works** -0.27 | **works** -0.02 |
| t12.sv | tax 12% | base.sv | no move -0.20 | no move -0.07 | no move -0.21 | no move -0.39 | no move +0.00 | no move -0.08 | **harms** +0.04 | no move -0.11 | no move -0.01 |
| t16.sv | tax 16% | base.sv | **harms** +0.09 | **harms** +0.01 | **harms** +0.07 | **harms** +0.23 | no move +0.00 | **harms** +0.01 | **harms** -0.06 | **harms** +0.06 | **harms** +0.00 |
| t20.sv | tax 20% | base.sv | **harms** +0.42 | **harms** +0.14 | **harms** +0.40 | **harms** +0.81 | no move +0.00 | **harms** +0.14 | **works** -0.12 | **harms** +0.27 | **harms** +0.02 |
| t25.sv | tax 25% | base.sv | **harms** +0.92 | **harms** +0.31 | **harms** +0.92 | **harms** +1.46 | no move +0.00 | **harms** +0.27 | **works** -0.16 | **harms** +0.58 | **harms** +0.04 |
| t30.sv | tax 30% | base.sv | **harms** +1.50 | **harms** +0.58 | **harms** +1.49 | **harms** +1.96 | no move +0.00 | **harms** +0.51 | **works** -0.18 | **harms** +0.99 | **harms** +0.06 |
| t40.sv | tax 40% | base.sv | **harms** +3.02 | **harms** +1.64 | **harms** +3.02 | **harms** +1.93 | no move +0.00 | **harms** +1.56 | **works** -0.17 | **harms** +2.11 | **harms** +0.18 |
| asis.t0.sv | tax 0%, today's rule | asis.sv | **works** -0.66 | **works** -0.16 | **works** -0.65 | **works** -2.31 | no move +0.00 | no move -0.17 | **harms** +0.83 | **works** -0.53 | **works** -0.03 |
| asis.t4.sv | tax 4%, today's rule | asis.sv | **works** -0.60 | **works** -0.15 | **works** -0.59 | **works** -1.70 | no move +0.00 | no move -0.16 | **harms** +0.42 | **works** -0.41 | **works** -0.03 |
| asis.t8.sv | tax 8%, today's rule | asis.sv | **works** -0.43 | **works** -0.12 | **works** -0.43 | **works** -1.04 | no move +0.00 | no move -0.13 | **harms** +0.18 | **works** -0.27 | **works** -0.02 |
| asis.t12.sv | tax 12%, today's rule | asis.sv | no move -0.20 | no move -0.07 | no move -0.21 | no move -0.39 | no move +0.00 | no move -0.08 | **harms** +0.04 | no move -0.11 | no move -0.01 |
| asis.t16.sv | tax 16%, today's rule | asis.sv | **harms** +0.09 | **harms** +0.01 | **harms** +0.07 | **harms** +0.23 | no move +0.00 | **harms** +0.01 | **harms** -0.06 | **harms** +0.06 | **harms** +0.00 |
| asis.t20.sv | tax 20%, today's rule | asis.sv | **harms** +0.42 | **harms** +0.14 | **harms** +0.40 | **harms** +0.81 | no move +0.00 | **harms** +0.14 | **works** -0.12 | **harms** +0.27 | **harms** +0.02 |
| asis.t25.sv | tax 25%, today's rule | asis.sv | **harms** +0.92 | **harms** +0.31 | **harms** +0.92 | **harms** +1.46 | no move +0.00 | **harms** +0.27 | **works** -0.16 | **harms** +0.58 | **harms** +0.04 |
| asis.t30.sv | tax 30%, today's rule | asis.sv | **harms** +1.50 | **harms** +0.58 | **harms** +1.49 | **harms** +1.96 | no move +0.00 | **harms** +0.51 | **works** -0.18 | **harms** +0.99 | **harms** +0.06 |
| asis.t40.sv | tax 40%, today's rule | asis.sv | **harms** +3.02 | **harms** +1.64 | **harms** +3.02 | **harms** +1.93 | no move +0.00 | **harms** +1.56 | **works** -0.17 | **harms** +2.11 | **harms** +0.18 |
| pr0c75.sv | progression 0 pts, cap 75% | base.sv | **works** -0.18 | no move -0.04 | **works** -0.17 | **works** -1.13 | no move +0.00 | no move -0.05 | **harms** +0.03 | **works** -0.08 | **works** -0.01 |
| pr8c75.sv | progression 8 pts, cap 75% | base.sv | **harms** +0.22 | **harms** +0.06 | **harms** +0.22 | **harms** +1.07 | no move +0.00 | **harms** +0.07 | **works** -0.03 | **harms** +0.09 | **harms** +0.00 |
| pr0c50.sv | progression 0 pts, cap 50% | base.sv | **works** -0.18 | no move -0.04 | **works** -0.17 | **works** -1.13 | no move +0.00 | no move -0.05 | **harms** +0.03 | **works** -0.08 | **works** -0.01 |
| pr4c50.sv | progression 4 pts, cap 50% | base.sv | no move -0.00 | no move +0.00 | no move +0.00 | no move -0.03 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 |
| pr8c50.sv | progression 8 pts, cap 50% | base.sv | **harms** +0.19 | **harms** +0.05 | **harms** +0.19 | **harms** +0.69 | no move +0.00 | **harms** +0.05 | **works** -0.02 | **harms** +0.08 | **harms** +0.00 |
| bt0.sv | business tax 0% | base.sv | **works** -0.48 | **works** -0.14 | **works** -0.46 | **works** -1.13 | no move +0.00 | no move -0.15 | **harms** +0.59 | **works** -0.37 | **works** -0.02 |
| bt25.sv | business tax 25% | base.sv | **harms** +0.64 | **harms** +0.21 | **harms** +0.63 | **harms** +0.92 | no move +0.00 | **harms** +0.19 | **works** -0.15 | **harms** +0.40 | **harms** +0.02 |
| bt50.sv | business tax 50% | base.sv | **harms** +3.75 | **harms** +1.87 | **harms** +3.75 | **harms** +0.35 | no move +0.00 | **harms** +1.81 | **works** -0.17 | **harms** +2.58 | **harms** +0.23 |
| bt75.sv | business tax 75% | base.sv | **harms** +9.83 | **harms** +7.06 | **harms** +9.63 | **works** -3.39 | no move +0.00 | **harms** +7.04 | **harms** -0.07 | **harms** +6.70 | **harms** +1.21 |
| kp10.sv | Source keeps 10% of project sales | base.sv | **works** -0.06 | no move -0.02 | **works** -0.05 | **works** -1.82 | no move +0.00 | no move -0.03 | **harms** +0.00 | **works** -0.02 | no move -0.00 |
| kp25.sv | Source keeps 25% of project sales | base.sv | **works** -0.14 | no move -0.04 | **works** -0.13 | **works** -4.65 | no move +0.00 | no move -0.05 | no move +0.01 | **works** -0.06 | no move -0.00 |
| kp50.sv | Source keeps 50% of project sales | base.sv | **works** -0.26 | no move -0.07 | **works** -0.25 | **works** -9.68 | no move +0.00 | no move -0.08 | **harms** +0.03 | **works** -0.12 | no move -0.00 |
| ex50.sv | 50% of expired BU recycled | base.sv | **harms** +1.43 | **harms** +0.67 | **harms** +1.44 | **harms** +4.27 | no move +0.00 | **harms** +0.59 | **works** -0.14 | **harms** +0.91 | **harms** +0.08 |
| ex0.sv | 0% of expired BU recycled | base.sv | **harms** +4.23 | **harms** +4.59 | **harms** +4.24 | **harms** +9.03 | no move +0.00 | **harms** +4.70 | **works** -0.14 | **harms** +3.34 | **harms** +1.06 |
| fprog.sv | outside finance: progressive income tax | base.sv | **harms** +7.79 | **harms** +2.45 | **harms** +7.52 | **works** -4.16 | no move +0.00 | **harms** +2.16 | **harms** +1.25 | **harms** +3.36 | **harms** +0.02 |
| fland.sv | outside finance: land-value tax | base.sv | **harms** +13.19 | no move -0.11 | **harms** +13.24 | **works** -37.93 | no move +0.00 | no move -0.10 | **harms** +2.10 | **works** -0.30 | **harms** +0.01 |
| fflat.sv | outside finance: flat wage contribution | base.sv | **harms** +7.75 | **harms** +2.11 | **harms** +7.54 | **works** -42.62 | no move +0.00 | **harms** +1.85 | **harms** +4.23 | **harms** +3.40 | **harms** +0.21 |
| br1.sv | business rate 1x | base.sv | **harms** +9.62 | **harms** +7.01 | **harms** +9.43 | **works** -3.81 | no move +0.00 | **harms** +7.02 | **harms** -0.08 | **harms** +6.65 | **harms** +1.21 |
| br15.sv | business rate 1.5x | base.sv | **harms** +6.22 | **harms** +3.95 | **harms** +6.16 | **works** -1.69 | no move +0.00 | **harms** +3.97 | no move -0.13 | **harms** +4.39 | **harms** +0.67 |
| br2.sv | business rate 2x | base.sv | **harms** +3.14 | **harms** +1.46 | **harms** +3.15 | **harms** +0.72 | no move +0.00 | **harms** +1.38 | **works** -0.17 | **harms** +2.12 | **harms** +0.17 |
| bu60.sv | 60% of the BU | base.sv | **harms** +10.67 | **harms** +8.39 | **harms** +10.51 | **works** -3.03 | no move +0.00 | **harms** +8.40 | **harms** -0.06 | **harms** +8.15 | **harms** +5.90 |
| bu80.sv | 80% of the BU | base.sv | **harms** +3.81 | **harms** +2.21 | **harms** +3.82 | **harms** +2.24 | no move +0.00 | **harms** +2.14 | **works** -0.12 | **harms** +3.02 | **harms** +1.15 |
| mm3.sv | top multiplier 3 | base.sv | **harms** +1.21 | **harms** +0.47 | **harms** +1.22 | **harms** +2.80 | no move +0.00 | **harms** +0.41 | **works** -0.11 | **harms** +0.77 | **harms** +0.06 |
| mm6.sv | top multiplier 6 | base.sv | **harms** +0.27 | **harms** +0.08 | **harms** +0.25 | **harms** +0.74 | no move +0.00 | **harms** +0.08 | no move -0.06 | **harms** +0.19 | **harms** +0.02 |
| mm9.sv | top multiplier 9 | base.sv | no move -0.20 | no move -0.07 | no move -0.20 | no move -0.46 | no move +0.00 | no move -0.08 | **harms** +0.01 | no move -0.12 | no move -0.01 |
| oc25.sv | octave capacity 25% | base.sv | **harms** +1.93 | **harms** +0.76 | **harms** +1.95 | **harms** +3.01 | no move +0.00 | **harms** +0.73 | **harms** +0.13 | **harms** +0.05 | **harms** +0.01 |
| oc50.sv | octave capacity 50% | base.sv | **harms** +1.58 | **harms** +0.48 | **harms** +1.58 | **harms** +2.63 | no move +0.00 | **harms** +0.44 | **harms** +0.06 | **harms** +0.04 | no move +0.00 |
| oc100.sv | octave capacity 100% | base.sv | **harms** +1.24 | **harms** +0.29 | **harms** +1.25 | **harms** +2.24 | no move +0.00 | **harms** +0.29 | **harms** +0.00 | **harms** +0.05 | **harms** +0.00 |
| no2.sv | 2 octaves | base.sv | **works** -0.39 | **works** -0.05 | **works** -0.39 | **works** -1.75 | no move +0.00 | no move -0.05 | **harms** +0.04 | **works** -0.48 | **works** -0.07 |
| no4.sv | 4 octaves | base.sv | no move -0.16 | no move -0.02 | no move -0.17 | no move -0.75 | no move +0.00 | no move -0.01 | no move -0.03 | no move -0.17 | no move -0.02 |
| no6.sv | 6 octaves | base.sv | **harms** +0.10 | **harms** +0.03 | **harms** +0.11 | **harms** +0.27 | no move +0.00 | **harms** +0.03 | **harms** +0.01 | **harms** +0.09 | **harms** +0.02 |
| phi0.sv | Phi tier off | base.sv | **harms** +0.17 | **harms** +0.05 | **harms** +0.16 | **harms** +0.59 | no move +0.00 | **harms** +0.06 | **works** -0.02 | **harms** +0.09 | **harms** +0.01 |
| ph5.sv | phase-in over 5 years | base.sv | **harms** +0.63 | **harms** +0.02 | **harms** +0.61 | **works** -0.29 | no move +0.00 | **harms** +0.01 | **works** -0.21 | **harms** +1.06 | **harms** +0.10 |
| ph10.sv | phase-in over 10 years | base.sv | **harms** +1.65 | **harms** +0.05 | **harms** +1.63 | **works** -0.71 | no move +0.00 | **harms** +0.04 | **works** -0.17 | **harms** +2.33 | **harms** +0.21 |
| cap2.sv | issuance cap 2% | base.sv | **harms** +10.94 | **harms** +8.73 | **harms** +10.68 | **works** -5.38 | no move +0.00 | **harms** +8.56 | **harms** +0.41 | **harms** +6.51 | **harms** +1.40 |
| cap4.sv | issuance cap 4% | base.sv | **harms** +10.94 | **harms** +8.73 | **harms** +10.68 | **works** -5.38 | no move +0.00 | **harms** +8.56 | **harms** +0.41 | **harms** +6.51 | **harms** +1.40 |
| cap8.sv | issuance cap 8% | base.sv | **harms** +10.94 | **harms** +8.73 | **harms** +10.68 | **works** -5.38 | no move +0.00 | **harms** +8.56 | **harms** +0.41 | **harms** +6.51 | **harms** +1.40 |
| ixs.sv | indexation: surge protocol (5%) | base.sv | **harms** +0.46 | **harms** +0.15 | **harms** +0.45 | **harms** +0.95 | no move +0.00 | **harms** +0.14 | **harms** +0.02 | **harms** +0.26 | **harms** +0.09 |
| ixy.sv | indexation: every year, price level | base.sv | **harms** +0.46 | **harms** +0.15 | **harms** +0.45 | **harms** +0.95 | no move +0.00 | **harms** +0.14 | **harms** +0.02 | **harms** +0.26 | **harms** +0.09 |
| ixn.sv | indexation: every year, basic needs | base.sv | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 |
| rcap.sv | rent cap for BU tenants | base.sv | **works** -0.26 | no move -0.07 | **works** -0.26 | **works** -1.49 | no move +0.00 | no move -0.07 | **harms** +0.01 | **works** -0.15 | **works** -0.01 |
| hc.sv | rent risk ($1.41 a BU dollar) | base.sv | **harms** +4.71 | **harms** +2.17 | **harms** +4.67 | **harms** +9.92 | no move +0.00 | **harms** +2.09 | no move -0.13 | **harms** +3.13 | **harms** +0.36 |
| hcrc.sv | rent risk and rent cap | base.sv | **works** -0.26 | no move -0.07 | **works** -0.26 | **works** -1.49 | no move +0.00 | no move -0.07 | **harms** +0.01 | **works** -0.15 | **works** -0.01 |

### Verdicts: C2.2 design, wages 90%, savings that keep up with prices (`.sv` twins, against `base.sv`)

| Row | What it sets | vs | basket poverty, % of adult-years | wealth poverty at year 20, % | non-participants' basket poverty, % | programme inflation, points a year | participation, mean of years 1-19, % | non-participants' wealth poverty, % | non-participants' income drops of 25%+ with no buffer, per 100 | non-participants under 3 months of basics covered, % | below 30 days of basic living, design-neutral, % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| asis.sv | today's joining rule | base.sv | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 |
| t0.sv | tax 0% | base.sv | **works** -1.95 | **works** -0.40 | **works** -1.92 | **works** -4.96 | no move +0.00 | **works** -0.35 | **harms** +0.94 | **works** -0.64 | **works** -0.04 |
| t4.sv | tax 4% | base.sv | **works** -1.74 | **works** -0.35 | **works** -1.72 | **works** -3.68 | no move +0.00 | **works** -0.32 | **harms** +0.48 | **works** -0.50 | **works** -0.03 |
| t8.sv | tax 8% | base.sv | **works** -1.25 | **works** -0.26 | **works** -1.24 | **works** -2.29 | no move +0.00 | **works** -0.24 | **harms** +0.21 | **works** -0.33 | **works** -0.02 |
| t12.sv | tax 12% | base.sv | no move -0.57 | no move -0.12 | no move -0.57 | no move -0.88 | no move +0.00 | no move -0.11 | **harms** +0.05 | no move -0.14 | no move -0.01 |
| t16.sv | tax 16% | base.sv | **harms** +0.22 | **harms** +0.04 | **harms** +0.22 | **harms** +0.52 | no move +0.00 | **harms** +0.04 | **harms** -0.07 | **harms** +0.07 | **harms** +0.01 |
| t20.sv | tax 20% | base.sv | **harms** +1.13 | **harms** +0.27 | **harms** +1.11 | **harms** +1.90 | no move +0.00 | **harms** +0.22 | **works** -0.14 | **harms** +0.34 | **harms** +0.02 |
| t25.sv | tax 25% | base.sv | **harms** +2.46 | **harms** +0.69 | **harms** +2.46 | **harms** +3.47 | no move +0.00 | **harms** +0.65 | **works** -0.19 | **harms** +0.79 | **harms** +0.06 |
| t30.sv | tax 30% | base.sv | **harms** +3.96 | **harms** +1.35 | **harms** +3.93 | **harms** +4.69 | no move +0.00 | **harms** +1.32 | **works** -0.22 | **harms** +1.36 | **harms** +0.12 |
| t40.sv | tax 40% | base.sv | **harms** +7.23 | **harms** +3.40 | **harms** +7.14 | **harms** +5.09 | no move +0.00 | **harms** +3.38 | **works** -0.22 | **harms** +2.79 | **harms** +0.43 |
| asis.t0.sv | tax 0%, today's rule | asis.sv | **works** -1.95 | **works** -0.40 | **works** -1.92 | **works** -4.96 | no move +0.00 | **works** -0.35 | **harms** +0.94 | **works** -0.64 | **works** -0.04 |
| asis.t4.sv | tax 4%, today's rule | asis.sv | **works** -1.74 | **works** -0.35 | **works** -1.72 | **works** -3.68 | no move +0.00 | **works** -0.32 | **harms** +0.48 | **works** -0.50 | **works** -0.03 |
| asis.t8.sv | tax 8%, today's rule | asis.sv | **works** -1.25 | **works** -0.26 | **works** -1.24 | **works** -2.29 | no move +0.00 | **works** -0.24 | **harms** +0.21 | **works** -0.33 | **works** -0.02 |
| asis.t12.sv | tax 12%, today's rule | asis.sv | no move -0.57 | no move -0.12 | no move -0.57 | no move -0.88 | no move +0.00 | no move -0.11 | **harms** +0.05 | no move -0.14 | no move -0.01 |
| asis.t16.sv | tax 16%, today's rule | asis.sv | **harms** +0.22 | **harms** +0.04 | **harms** +0.22 | **harms** +0.52 | no move +0.00 | **harms** +0.04 | **harms** -0.07 | **harms** +0.07 | **harms** +0.01 |
| asis.t20.sv | tax 20%, today's rule | asis.sv | **harms** +1.13 | **harms** +0.27 | **harms** +1.11 | **harms** +1.90 | no move +0.00 | **harms** +0.22 | **works** -0.14 | **harms** +0.34 | **harms** +0.02 |
| asis.t25.sv | tax 25%, today's rule | asis.sv | **harms** +2.46 | **harms** +0.69 | **harms** +2.46 | **harms** +3.47 | no move +0.00 | **harms** +0.65 | **works** -0.19 | **harms** +0.79 | **harms** +0.06 |
| asis.t30.sv | tax 30%, today's rule | asis.sv | **harms** +3.96 | **harms** +1.35 | **harms** +3.93 | **harms** +4.69 | no move +0.00 | **harms** +1.32 | **works** -0.22 | **harms** +1.36 | **harms** +0.12 |
| asis.t40.sv | tax 40%, today's rule | asis.sv | **harms** +7.23 | **harms** +3.40 | **harms** +7.14 | **harms** +5.09 | no move +0.00 | **harms** +3.38 | **works** -0.22 | **harms** +2.79 | **harms** +0.43 |
| pr0c75.sv | progression 0 pts, cap 75% | base.sv | **works** -0.63 | **works** -0.12 | **works** -0.63 | **works** -2.26 | no move +0.00 | **works** -0.10 | **harms** +0.03 | **works** -0.12 | **works** -0.01 |
| pr8c75.sv | progression 8 pts, cap 75% | base.sv | **harms** +0.80 | **harms** +0.13 | **harms** +0.82 | **harms** +2.18 | no move +0.00 | **harms** +0.13 | **works** -0.04 | **harms** +0.12 | **harms** +0.01 |
| pr0c50.sv | progression 0 pts, cap 50% | base.sv | **works** -0.63 | **works** -0.12 | **works** -0.63 | **works** -2.26 | no move +0.00 | **works** -0.10 | **harms** +0.03 | **works** -0.12 | **works** -0.01 |
| pr4c50.sv | progression 4 pts, cap 50% | base.sv | no move -0.01 | no move +0.00 | no move -0.01 | no move -0.05 | no move +0.00 | no move +0.00 | no move +0.00 | no move -0.00 | no move +0.00 |
| pr8c50.sv | progression 8 pts, cap 50% | base.sv | **harms** +0.61 | **harms** +0.11 | **harms** +0.64 | **harms** +1.41 | no move +0.00 | **harms** +0.11 | **works** -0.03 | **harms** +0.11 | **harms** +0.01 |
| bt0.sv | business tax 0% | base.sv | **works** -1.38 | **works** -0.32 | **works** -1.37 | **works** -2.63 | no move +0.00 | **works** -0.29 | **harms** +0.66 | **works** -0.44 | **works** -0.03 |
| bt25.sv | business tax 25% | base.sv | **harms** +1.64 | **harms** +0.45 | **harms** +1.62 | **harms** +2.19 | no move +0.00 | **harms** +0.40 | **works** -0.18 | **harms** +0.53 | **harms** +0.04 |
| bt50.sv | business tax 50% | base.sv | **harms** +8.03 | **harms** +3.47 | **harms** +7.95 | **harms** +2.11 | no move +0.00 | **harms** +3.42 | **works** -0.22 | **harms** +3.19 | **harms** +0.51 |
| bt75.sv | business tax 75% | base.sv | **harms** +17.77 | **harms** +10.43 | **harms** +17.53 | **harms** -2.13 | no move +0.00 | **harms** +10.29 | no move -0.14 | **harms** +7.92 | **harms** +2.26 |
| kp10.sv | Source keeps 10% of project sales | base.sv | **works** -0.27 | **works** -0.05 | **works** -0.27 | **works** -2.56 | no move +0.00 | no move -0.05 | no move -0.00 | **works** -0.03 | no move -0.00 |
| kp25.sv | Source keeps 25% of project sales | base.sv | **works** -0.66 | **works** -0.11 | **works** -0.65 | **works** -6.57 | no move +0.00 | **works** -0.10 | no move +0.00 | **works** -0.09 | no move -0.00 |
| kp50.sv | Source keeps 50% of project sales | base.sv | **works** -1.29 | **works** -0.20 | **works** -1.25 | **works** -13.69 | no move +0.00 | **works** -0.17 | **harms** +0.02 | **works** -0.18 | **works** -0.01 |
| ex50.sv | 50% of expired BU recycled | base.sv | **harms** +4.11 | **harms** +1.66 | **harms** +4.11 | **harms** +8.13 | no move +0.00 | **harms** +1.64 | **works** -0.17 | **harms** +1.33 | **harms** +0.16 |
| ex0.sv | 0% of expired BU recycled | base.sv | **harms** +10.56 | **harms** +7.78 | **harms** +10.50 | **harms** +17.32 | no move +0.00 | **harms** +7.91 | **works** -0.19 | **harms** +4.56 | **harms** +1.96 |
| fprog.sv | outside finance: progressive income tax | base.sv | **harms** +19.20 | **harms** +5.24 | **harms** +18.91 | **harms** +2.27 | no move +0.00 | **harms** +4.96 | **harms** +1.27 | **harms** +4.33 | **harms** +0.16 |
| fland.sv | outside finance: land-value tax | base.sv | **harms** +12.25 | **works** -0.40 | **harms** +12.36 | **works** -49.76 | no move +0.00 | no move -0.34 | **harms** +2.22 | **works** -0.49 | no move -0.00 |
| fflat.sv | outside finance: flat wage contribution | base.sv | **harms** +5.21 | **harms** +1.82 | **harms** +5.07 | **works** -54.67 | no move +0.00 | **harms** +1.61 | **harms** +4.20 | **harms** +3.16 | **harms** +0.18 |
| br1.sv | business rate 1x | base.sv | **harms** +17.37 | **harms** +10.34 | **harms** +17.13 | **works** -2.90 | no move +0.00 | **harms** +10.20 | no move -0.15 | **harms** +7.89 | **harms** +2.25 |
| br15.sv | business rate 1.5x | base.sv | **harms** +12.36 | **harms** +6.33 | **harms** +12.15 | **harms** -0.33 | no move +0.00 | **harms** +6.24 | **works** -0.19 | **harms** +5.30 | **harms** +1.27 |
| br2.sv | business rate 2x | base.sv | **harms** +6.90 | **harms** +2.82 | **harms** +6.83 | **harms** +2.51 | no move +0.00 | **harms** +2.77 | **works** -0.23 | **harms** +2.68 | **harms** +0.37 |
| bu60.sv | 60% of the BU | base.sv | **harms** +18.32 | **harms** +12.16 | **harms** +18.13 | **works** -3.92 | no move +0.00 | **harms** +12.18 | no move -0.13 | **harms** +9.63 | **harms** +7.66 |
| bu80.sv | 80% of the BU | base.sv | **harms** +8.43 | **harms** +4.43 | **harms** +8.35 | **harms** +4.10 | no move +0.00 | **harms** +4.49 | **works** -0.17 | **harms** +3.88 | **harms** +1.88 |
| mm3.sv | top multiplier 3 | base.sv | **harms** +3.59 | **harms** +1.28 | **harms** +3.58 | **harms** +6.19 | no move +0.00 | **harms** +1.25 | **works** -0.14 | **harms** +1.17 | **harms** +0.12 |
| mm6.sv | top multiplier 6 | base.sv | **harms** +0.82 | **harms** +0.18 | **harms** +0.80 | **harms** +1.68 | no move +0.00 | **harms** +0.15 | no move -0.07 | **harms** +0.24 | **harms** +0.02 |
| mm9.sv | top multiplier 9 | base.sv | no move -0.61 | no move -0.13 | no move -0.61 | no move -0.97 | no move +0.00 | no move -0.12 | **harms** +0.02 | no move -0.15 | no move -0.01 |
| oc25.sv | octave capacity 25% | base.sv | **harms** +5.99 | **harms** +1.64 | **harms** +5.93 | **harms** +7.37 | no move +0.00 | **harms** +1.62 | **harms** +0.14 | **harms** +0.24 | **harms** +0.04 |
| oc50.sv | octave capacity 50% | base.sv | **harms** +5.26 | **harms** +1.21 | **harms** +5.24 | **harms** +6.54 | no move +0.00 | **harms** +1.16 | **harms** +0.08 | **harms** +0.18 | **harms** +0.01 |
| oc100.sv | octave capacity 100% | base.sv | **harms** +4.50 | **harms** +0.90 | **harms** +4.49 | **harms** +5.63 | no move +0.00 | **harms** +0.88 | **harms** +0.00 | **harms** +0.15 | **harms** +0.01 |
| no2.sv | 2 octaves | base.sv | **works** -0.63 | **works** -0.15 | **works** -0.62 | **works** -2.30 | no move +0.00 | **works** -0.12 | **harms** +0.07 | **works** -0.57 | **works** -0.09 |
| no4.sv | 4 octaves | base.sv | no move -0.27 | no move -0.05 | no move -0.28 | no move -0.92 | no move +0.00 | no move -0.03 | no move -0.03 | no move -0.20 | no move -0.03 |
| no6.sv | 6 octaves | base.sv | **harms** +0.17 | **harms** +0.05 | **harms** +0.17 | **harms** +0.35 | no move +0.00 | **harms** +0.04 | no move +0.00 | **harms** +0.13 | **harms** +0.02 |
| phi0.sv | Phi tier off | base.sv | **harms** +0.51 | **harms** +0.10 | **harms** +0.51 | **harms** +1.15 | no move +0.00 | **harms** +0.09 | **works** -0.03 | **harms** +0.13 | **harms** +0.01 |
| ph5.sv | phase-in over 5 years | base.sv | **harms** +0.66 | **harms** +0.09 | **harms** +0.65 | **works** -0.39 | no move +0.00 | **harms** +0.08 | **works** -0.26 | **harms** +1.17 | **harms** +0.12 |
| ph10.sv | phase-in over 10 years | base.sv | **harms** +1.96 | **harms** +0.31 | **harms** +1.92 | **works** -0.78 | no move +0.00 | **harms** +0.29 | **works** -0.22 | **harms** +2.64 | **harms** +0.28 |
| cap2.sv | issuance cap 2% | base.sv | **harms** +19.62 | **harms** +12.65 | **harms** +19.32 | **works** -3.31 | no move +0.00 | **harms** +12.33 | **harms** +0.47 | **harms** +8.01 | **harms** +2.66 |
| cap4.sv | issuance cap 4% | base.sv | **harms** +19.62 | **harms** +12.65 | **harms** +19.32 | **works** -3.31 | no move +0.00 | **harms** +12.33 | **harms** +0.47 | **harms** +8.01 | **harms** +2.66 |
| cap8.sv | issuance cap 8% | base.sv | **harms** +19.62 | **harms** +12.65 | **harms** +19.32 | **works** -3.31 | no move +0.00 | **harms** +12.33 | **harms** +0.47 | **harms** +8.01 | **harms** +2.66 |
| ixs.sv | indexation: surge protocol (5%) | base.sv | **harms** +1.12 | **harms** +0.33 | **harms** +1.12 | **harms** +1.85 | no move +0.00 | **harms** +0.31 | **harms** +0.02 | **harms** +0.36 | **harms** +0.10 |
| ixy.sv | indexation: every year, price level | base.sv | **harms** +1.12 | **harms** +0.33 | **harms** +1.12 | **harms** +1.85 | no move +0.00 | **harms** +0.31 | **harms** +0.02 | **harms** +0.36 | **harms** +0.10 |
| ixn.sv | indexation: every year, basic needs | base.sv | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 | no move +0.00 |
| rcap.sv | rent cap for BU tenants | base.sv | **works** -0.70 | **works** -0.14 | **works** -0.69 | **works** -2.43 | no move +0.00 | **works** -0.14 | **harms** +0.01 | **works** -0.20 | **works** -0.02 |
| hc.sv | rent risk ($1.41 a BU dollar) | base.sv | **harms** +11.64 | **harms** +4.71 | **harms** +11.49 | **harms** +16.41 | no move +0.00 | **harms** +4.66 | **works** -0.16 | **harms** +4.19 | **harms** +0.92 |
| hcrc.sv | rent risk and rent cap | base.sv | **works** -0.70 | **works** -0.14 | **works** -0.69 | **works** -2.43 | no move +0.00 | **works** -0.14 | **harms** +0.01 | **works** -0.20 | **works** -0.02 |

### basket poverty, % of adult-years: release row, wages 100% (lever effect, seed mean and 95% interval)

| Row | What it sets | Reference | Adverse | Stress | Verdict |
|---|---|---|---|---|---|
| asis | today's joining rule | -0.18 (-0.23, -0.14) | -0.12 (-0.16, -0.08) | -0.00 (-0.00, +0.00) | does not move |
| t0 | tax 0% | -2.36 (-2.49, -2.24) | -3.42 (-3.54, -3.30) | -1.87 (-2.00, -1.75) | works |
| t4 | tax 4% | -1.60 (-1.69, -1.51) | -2.28 (-2.38, -2.19) | -1.43 (-1.55, -1.33) | works |
| t8 | tax 8% | -0.84 (-0.90, -0.78) | -1.15 (-1.21, -1.10) | -1.01 (-1.09, -0.93) | works |
| t12 | tax 12% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -0.60 (-0.66, -0.54) | does not move |
| t16 | tax 16% | +0.84 (+0.79, +0.89) | +1.12 (+1.06, +1.17) | -0.20 (-0.23, -0.17) | harms |
| t20 | tax 20% | +1.69 (+1.61, +1.77) | +2.24 (+2.16, +2.33) | +0.19 (+0.16, +0.21) | harms |
| t25 | tax 25% | +2.77 (+2.65, +2.89) | +3.63 (+3.51, +3.76) | +0.65 (+0.60, +0.71) | harms |
| t30 | tax 30% | +3.79 (+3.63, +3.94) | +4.97 (+4.80, +5.16) | +1.22 (+1.13, +1.32) | harms |
| t40 | tax 40% | +5.85 (+5.65, +6.06) | +7.39 (+7.15, +7.66) | +2.54 (+2.36, +2.73) | harms |
| asis.t0 | tax 0%, today's rule | -2.09 (-2.20, -1.99) | -3.19 (-3.30, -3.08) | -1.84 (-1.98, -1.72) | works |
| asis.t4 | tax 4%, today's rule | -1.43 (-1.51, -1.36) | -2.13 (-2.22, -2.05) | -1.41 (-1.53, -1.30) | works |
| asis.t8 | tax 8%, today's rule | -0.73 (-0.77, -0.68) | -1.08 (-1.13, -1.03) | -1.00 (-1.08, -0.92) | works |
| asis.t12 | tax 12%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -0.59 (-0.65, -0.53) | does not move |
| asis.t16 | tax 16%, today's rule | +0.80 (+0.75, +0.84) | +1.07 (+1.02, +1.12) | -0.20 (-0.22, -0.17) | harms |
| asis.t20 | tax 20%, today's rule | +1.62 (+1.55, +1.70) | +2.19 (+2.11, +2.27) | +0.19 (+0.16, +0.21) | harms |
| asis.t25 | tax 25%, today's rule | +2.73 (+2.61, +2.84) | +3.57 (+3.45, +3.71) | +0.65 (+0.59, +0.71) | harms |
| asis.t30 | tax 30%, today's rule | +3.80 (+3.65, +3.95) | +4.94 (+4.78, +5.13) | +1.22 (+1.12, +1.31) | harms |
| asis.t40 | tax 40%, today's rule | +5.93 (+5.72, +6.13) | +7.41 (+7.16, +7.67) | +2.54 (+2.35, +2.73) | harms |
| pr0c75 | progression 0 pts, cap 75% | -0.39 (-0.44, -0.34) | -0.42 (-0.47, -0.38) | -0.05 (-0.07, -0.03) | works |
| pr8c75 | progression 8 pts, cap 75% | +0.49 (+0.43, +0.56) | +0.58 (+0.50, +0.66) | +0.06 (+0.04, +0.08) | harms |
| pr0c50 | progression 0 pts, cap 50% | -0.39 (-0.44, -0.34) | -0.42 (-0.47, -0.38) | -0.05 (-0.07, -0.03) | works |
| pr4c50 | progression 4 pts, cap 50% | -0.01 (-0.01, -0.00) | -0.01 (-0.01, -0.00) | +0.00 (+0.00, +0.00) | does not move |
| pr8c50 | progression 8 pts, cap 50% | +0.35 (+0.30, +0.40) | +0.42 (+0.36, +0.50) | +0.03 (+0.02, +0.05) | harms |
| bt0 | business tax 0% | -1.79 (-1.88, -1.70) | -2.76 (-2.86, -2.67) | -1.72 (-1.85, -1.60) | works |
| bt25 | business tax 25% | +2.39 (+2.28, +2.50) | +3.21 (+3.10, +3.33) | +0.58 (+0.53, +0.64) | harms |
| bt50 | business tax 50% | +6.88 (+6.63, +7.14) | +8.76 (+8.45, +9.07) | +3.57 (+3.35, +3.81) | harms |
| bt75 | business tax 75% | +10.59 (+10.24, +10.94) | +14.47 (+14.07, +14.91) | +6.32 (+5.98, +6.68) | harms |
| kp10 | Source keeps 10% of project sales | -0.03 (-0.04, -0.03) | -0.03 (-0.04, -0.02) | -0.00 (-0.00, -0.00) | works |
| kp25 | Source keeps 25% of project sales | -0.07 (-0.08, -0.06) | -0.08 (-0.09, -0.07) | -0.01 (-0.01, -0.00) | works |
| kp50 | Source keeps 50% of project sales | -0.13 (-0.15, -0.12) | -0.17 (-0.19, -0.15) | -0.01 (-0.01, -0.01) | works |
| ex50 | 50% of expired BU recycled | +0.58 (+0.52, +0.63) | +0.76 (+0.71, +0.82) | +0.00 (-0.00, +0.01) | harms |
| ex0 | 0% of expired BU recycled | +1.13 (+1.04, +1.21) | +1.50 (+1.41, +1.60) | +0.01 (+0.00, +0.01) | harms |
| fprog | outside finance: progressive income tax | +46.03 (+45.41, +46.70) | +46.96 (+46.39, +47.53) | +34.13 (+33.55, +34.70) | harms |
| fland | outside finance: land-value tax | +12.85 (+12.47, +13.25) | +16.27 (+15.64, +16.88) | +10.26 (+9.85, +10.67) | harms |
| fflat | outside finance: flat wage contribution | +48.92 (+48.44, +49.42) | +48.27 (+47.61, +48.89) | +19.10 (+18.56, +19.62) | harms |
| br1 | business rate 1x | +10.66 (+10.32, +11.02) | +13.61 (+13.25, +14.01) | +5.51 (+5.21, +5.82) | harms |
| br15 | business rate 1.5x | +8.78 (+8.48, +9.09) | +10.94 (+10.61, +11.29) | +4.43 (+4.17, +4.70) | harms |
| br2 | business rate 2x | +6.19 (+5.97, +6.44) | +7.76 (+7.49, +8.05) | +2.71 (+2.54, +2.88) | harms |
| bu60 | 60% of the BU | +10.22 (+9.88, +10.56) | +12.30 (+11.90, +12.72) | +4.37 (+4.12, +4.62) | harms |
| bu80 | 80% of the BU | +5.93 (+5.70, +6.16) | +7.18 (+6.92, +7.46) | +2.03 (+1.89, +2.16) | harms |
| mm3 | top multiplier 3 | +0.89 (+0.82, +0.95) | +1.31 (+1.22, +1.40) | +0.25 (+0.21, +0.29) | harms |
| mm6 | top multiplier 6 | +0.33 (+0.30, +0.37) | +0.53 (+0.48, +0.58) | +0.00 (+0.00, +0.00) | harms |
| mm9 | top multiplier 9 | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -0.18 (-0.21, -0.14) | does not move |
| oc25 | octave capacity 25% | -0.10 (-0.14, -0.07) | +0.26 (+0.21, +0.30) | -0.02 (-0.04, +0.01) | harms |
| oc50 | octave capacity 50% | -0.03 (-0.06, -0.00) | +0.29 (+0.25, +0.32) | -0.02 (-0.03, -0.00) | harms |
| oc100 | octave capacity 100% | +0.04 (+0.03, +0.05) | +0.24 (+0.22, +0.26) | +0.00 (+0.00, +0.00) | harms |
| no2 | 2 octaves | -0.66 (-0.72, -0.61) | -0.57 (-0.63, -0.51) | -0.02 (-0.05, +0.01) | does not move |
| no4 | 4 octaves | -0.35 (-0.38, -0.31) | -0.27 (-0.32, -0.23) | +0.00 (+0.00, +0.00) | does not move |
| no6 | 6 octaves | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.04 (+0.02, +0.06) | harms |
| phi0 | Phi tier off | +0.05 (+0.04, +0.07) | +0.07 (+0.05, +0.09) | +0.04 (+0.03, +0.06) | harms |
| ph5 | phase-in over 5 years | +1.35 (+1.29, +1.40) | +1.38 (+1.32, +1.45) | +0.44 (+0.38, +0.50) | harms |
| ph10 | phase-in over 10 years | +3.15 (+3.05, +3.25) | +3.33 (+3.21, +3.45) | +1.15 (+1.04, +1.25) | harms |
| cap2 | issuance cap 2% | +13.03 (+12.67, +13.43) | +16.52 (+16.11, +16.98) | +6.36 (+6.06, +6.68) | harms |
| cap4 | issuance cap 4% | +13.03 (+12.67, +13.43) | +16.52 (+16.11, +16.98) | +6.36 (+6.06, +6.68) | harms |
| cap8 | issuance cap 8% | +13.03 (+12.67, +13.43) | +16.52 (+16.11, +16.98) | +6.36 (+6.06, +6.68) | harms |
| ixs | indexation: surge protocol (5%) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ixy | indexation: every year, price level | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ixn | indexation: every year, basic needs | -1.33 (-1.41, -1.23) | -1.74 (-1.84, -1.63) | -0.08 (-0.10, -0.06) | works |
| sva | protected account, all savings | +16.22 (+15.80, +16.65) | +19.75 (+19.32, +20.23) | +11.94 (+11.63, +12.25) | harms |
| svc | protected account, first $10,000 | +0.88 (+0.83, +0.93) | +1.89 (+1.79, +1.98) | +0.60 (+0.57, +0.64) | harms |
| rcap | rent cap for BU tenants | -0.55 (-0.59, -0.51) | -0.79 (-0.85, -0.73) | -0.05 (-0.06, -0.04) | works |
| hc | rent risk ($1.41 a BU dollar) | +7.03 (+6.80, +7.28) | +8.13 (+7.90, +8.37) | +2.91 (+2.80, +3.02) | harms |
| hcrc | rent risk and rent cap | +2.88 (+2.72, +3.04) | +2.31 (+2.16, +2.46) | +2.24 (+2.14, +2.33) | harms |

### wealth poverty at year 20, %: release row, wages 100% (lever effect, seed mean and 95% interval)

| Row | What it sets | Reference | Adverse | Stress | Verdict |
|---|---|---|---|---|---|
| asis | today's joining rule | -0.08 (-0.17, +0.02) | +0.12 (+0.05, +0.20) | +0.00 (+0.00, +0.00) | harms |
| t0 | tax 0% | -2.66 (-2.95, -2.40) | -2.41 (-2.66, -2.18) | +0.80 (+0.53, +1.08) | harms |
| t4 | tax 4% | -1.77 (-2.00, -1.54) | -1.48 (-1.69, -1.30) | +0.68 (+0.43, +0.93) | harms |
| t8 | tax 8% | -0.90 (-1.06, -0.74) | -0.66 (-0.80, -0.53) | +0.57 (+0.37, +0.77) | harms |
| t12 | tax 12% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.40 (+0.24, +0.55) | harms |
| t16 | tax 16% | +1.00 (+0.82, +1.20) | +0.68 (+0.55, +0.80) | +0.09 (-0.02, +0.21) | harms |
| t20 | tax 20% | +2.02 (+1.76, +2.29) | +1.51 (+1.26, +1.76) | -0.15 (-0.26, -0.04) | harms |
| t25 | tax 25% | +3.05 (+2.78, +3.32) | +2.34 (+2.05, +2.63) | -0.34 (-0.52, -0.15) | harms |
| t30 | tax 30% | +4.11 (+3.78, +4.44) | +3.00 (+2.72, +3.28) | -0.73 (-1.00, -0.46) | harms |
| t40 | tax 40% | +5.13 (+4.71, +5.55) | +3.95 (+3.67, +4.24) | -1.34 (-1.71, -0.96) | harms |
| asis.t0 | tax 0%, today's rule | -2.43 (-2.74, -2.14) | -2.49 (-2.72, -2.28) | +0.76 (+0.48, +1.05) | harms |
| asis.t4 | tax 4%, today's rule | -1.57 (-1.81, -1.35) | -1.64 (-1.85, -1.43) | +0.67 (+0.41, +0.93) | harms |
| asis.t8 | tax 8%, today's rule | -0.78 (-0.94, -0.62) | -0.75 (-0.89, -0.63) | +0.57 (+0.37, +0.77) | harms |
| asis.t12 | tax 12%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.40 (+0.24, +0.55) | harms |
| asis.t16 | tax 16%, today's rule | +1.04 (+0.84, +1.24) | +0.68 (+0.57, +0.81) | +0.09 (-0.02, +0.21) | harms |
| asis.t20 | tax 20%, today's rule | +2.00 (+1.76, +2.24) | +1.48 (+1.26, +1.71) | -0.15 (-0.26, -0.04) | harms |
| asis.t25 | tax 25%, today's rule | +3.05 (+2.78, +3.30) | +2.25 (+1.98, +2.52) | -0.34 (-0.52, -0.16) | harms |
| asis.t30 | tax 30%, today's rule | +4.04 (+3.74, +4.34) | +2.99 (+2.70, +3.27) | -0.73 (-1.00, -0.46) | harms |
| asis.t40 | tax 40%, today's rule | +5.21 (+4.83, +5.57) | +3.86 (+3.56, +4.14) | -1.32 (-1.70, -0.94) | harms |
| pr0c75 | progression 0 pts, cap 75% | -0.86 (-1.03, -0.70) | -0.29 (-0.36, -0.23) | +0.08 (-0.03, +0.17) | does not move |
| pr8c75 | progression 8 pts, cap 75% | +0.90 (+0.75, +1.05) | +0.30 (+0.20, +0.40) | +0.02 (-0.08, +0.12) | harms |
| pr0c50 | progression 0 pts, cap 50% | -0.86 (-1.03, -0.70) | -0.29 (-0.36, -0.23) | +0.08 (-0.03, +0.17) | does not move |
| pr4c50 | progression 4 pts, cap 50% | -0.06 (-0.10, -0.03) | -0.04 (-0.07, -0.01) | +0.00 (+0.00, +0.00) | does not move |
| pr8c50 | progression 8 pts, cap 50% | +0.60 (+0.46, +0.74) | +0.19 (+0.11, +0.28) | +0.04 (-0.04, +0.11) | harms |
| bt0 | business tax 0% | -1.69 (-1.97, -1.43) | -2.02 (-2.26, -1.79) | +0.84 (+0.60, +1.08) | harms |
| bt25 | business tax 25% | +2.44 (+2.17, +2.71) | +2.16 (+1.87, +2.45) | -0.43 (-0.64, -0.24) | harms |
| bt50 | business tax 50% | +5.26 (+4.81, +5.73) | +4.67 (+4.34, +4.99) | -2.37 (-2.77, -1.98) | harms |
| bt75 | business tax 75% | +4.66 (+4.16, +5.20) | +5.87 (+5.42, +6.35) | -6.82 (-7.40, -6.23) | harms |
| kp10 | Source keeps 10% of project sales | -0.21 (-0.28, -0.14) | -0.08 (-0.12, -0.04) | -0.00 (-0.01, +0.00) | does not move |
| kp25 | Source keeps 25% of project sales | -0.45 (-0.57, -0.34) | -0.25 (-0.34, -0.18) | -0.02 (-0.04, +0.00) | does not move |
| kp50 | Source keeps 50% of project sales | -1.00 (-1.16, -0.84) | -0.50 (-0.62, -0.39) | -0.06 (-0.10, -0.02) | works |
| ex50 | 50% of expired BU recycled | +1.99 (+1.75, +2.23) | +1.02 (+0.86, +1.19) | +0.00 (+0.00, +0.01) | harms |
| ex0 | 0% of expired BU recycled | +4.02 (+3.66, +4.38) | +1.92 (+1.70, +2.14) | +0.01 (+0.00, +0.03) | harms |
| fprog | outside finance: progressive income tax | +39.59 (+38.77, +40.38) | +16.61 (+15.96, +17.24) | -5.35 (-6.30, -4.40) | harms |
| fland | outside finance: land-value tax | -27.26 (-28.13, -26.40) | -15.27 (-16.84, -13.70) | -34.46 (-35.17, -33.76) | works |
| fflat | outside finance: flat wage contribution | +3.10 (+2.10, +4.07) | -17.77 (-18.73, -16.86) | -22.82 (-23.36, -22.29) | harms |
| br1 | business rate 1x | +4.60 (+4.10, +5.13) | +4.82 (+4.41, +5.24) | -7.88 (-8.39, -7.36) | harms |
| br15 | business rate 1.5x | +5.28 (+4.82, +5.77) | +4.92 (+4.54, +5.30) | -5.42 (-5.90, -4.95) | harms |
| br2 | business rate 2x | +5.02 (+4.58, +5.44) | +4.26 (+3.98, +4.55) | -2.66 (-3.02, -2.31) | harms |
| bu60 | 60% of the BU | +2.01 (+1.53, +2.50) | -0.66 (-1.00, -0.34) | -7.04 (-7.52, -6.58) | harms |
| bu80 | 80% of the BU | +3.40 (+3.00, +3.79) | +1.47 (+1.20, +1.76) | -2.63 (-2.89, -2.36) | harms |
| mm3 | top multiplier 3 | +2.37 (+2.13, +2.63) | +1.04 (+0.88, +1.19) | +0.28 (+0.10, +0.46) | harms |
| mm6 | top multiplier 6 | +0.96 (+0.78, +1.14) | +0.52 (+0.40, +0.62) | +0.00 (+0.00, +0.00) | harms |
| mm9 | top multiplier 9 | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -0.05 (-0.17, +0.08) | does not move |
| oc25 | octave capacity 25% | +2.56 (+2.29, +2.82) | +1.46 (+1.25, +1.67) | +0.52 (+0.33, +0.71) | harms |
| oc50 | octave capacity 50% | +1.56 (+1.34, +1.76) | +1.29 (+1.12, +1.47) | +0.26 (+0.13, +0.40) | harms |
| oc100 | octave capacity 100% | +0.56 (+0.45, +0.67) | +0.87 (+0.72, +1.02) | +0.00 (+0.00, +0.00) | harms |
| no2 | 2 octaves | +0.28 (+0.11, +0.45) | +0.00 (-0.11, +0.11) | +0.54 (+0.34, +0.74) | harms |
| no4 | 4 octaves | +0.22 (+0.10, +0.33) | +0.01 (-0.08, +0.10) | +0.00 (+0.00, +0.00) | harms |
| no6 | 6 octaves | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -0.05 (-0.14, +0.04) | does not move |
| phi0 | Phi tier off | +0.17 (+0.10, +0.24) | +0.11 (+0.06, +0.16) | +0.01 (-0.06, +0.08) | harms |
| ph5 | phase-in over 5 years | -0.39 (-0.52, -0.26) | -0.05 (-0.18, +0.09) | -0.92 (-1.10, -0.76) | does not move |
| ph10 | phase-in over 10 years | -0.82 (-1.00, -0.66) | -0.21 (-0.37, -0.05) | -2.22 (-2.46, -1.98) | works |
| cap2 | issuance cap 2% | +8.17 (+7.58, +8.83) | +5.92 (+5.49, +6.33) | -6.90 (-7.49, -6.30) | harms |
| cap4 | issuance cap 4% | +8.17 (+7.58, +8.83) | +5.92 (+5.49, +6.33) | -6.90 (-7.49, -6.30) | harms |
| cap8 | issuance cap 8% | +8.17 (+7.58, +8.83) | +5.92 (+5.49, +6.33) | -6.90 (-7.49, -6.30) | harms |
| ixs | indexation: surge protocol (5%) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ixy | indexation: every year, price level | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ixn | indexation: every year, basic needs | -0.76 (-0.94, -0.57) | -0.19 (-0.33, -0.06) | +0.17 (+0.10, +0.23) | harms |
| sva | protected account, all savings | -21.64 (-22.53, -20.86) | -52.18 (-52.98, -51.42) | -38.27 (-39.11, -37.35) | works |
| svc | protected account, first $10,000 | -17.18 (-17.98, -16.48) | -30.08 (-30.88, -29.21) | -7.82 (-8.37, -7.31) | works |
| rcap | rent cap for BU tenants | -0.64 (-0.76, -0.52) | -0.30 (-0.39, -0.23) | -0.02 (-0.04, +0.00) | does not move |
| hc | rent risk ($1.41 a BU dollar) | +7.85 (+7.39, +8.33) | +3.50 (+3.20, +3.79) | +1.68 (+1.48, +1.89) | harms |
| hcrc | rent risk and rent cap | +1.14 (+0.91, +1.38) | -0.48 (-0.64, -0.34) | +0.96 (+0.80, +1.13) | harms |

### non-participants' basket poverty, %: release row, wages 100% (lever effect, seed mean and 95% interval)

| Row | What it sets | Reference | Adverse | Stress | Verdict |
|---|---|---|---|---|---|
| asis | today's joining rule | -0.61 (-0.76, -0.48) | -0.48 (-0.62, -0.35) | -0.00 (-0.00, +0.00) | does not move |
| t0 | tax 0% | -2.32 (-2.58, -2.05) | -3.09 (-3.31, -2.87) | -0.79 (-0.88, -0.70) | works |
| t4 | tax 4% | -1.51 (-1.68, -1.34) | -2.00 (-2.16, -1.85) | -0.57 (-0.66, -0.49) | works |
| t8 | tax 8% | -0.86 (-1.02, -0.73) | -1.06 (-1.19, -0.94) | -0.40 (-0.46, -0.33) | works |
| t12 | tax 12% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -0.24 (-0.29, -0.19) | does not move |
| t16 | tax 16% | +0.56 (+0.49, +0.63) | +0.71 (+0.62, +0.80) | -0.07 (-0.10, -0.05) | harms |
| t20 | tax 20% | +1.05 (+0.94, +1.16) | +1.43 (+1.28, +1.57) | +0.06 (+0.04, +0.09) | harms |
| t25 | tax 25% | +1.64 (+1.48, +1.80) | +2.19 (+1.99, +2.39) | +0.25 (+0.20, +0.30) | harms |
| t30 | tax 30% | +2.17 (+1.95, +2.40) | +3.03 (+2.74, +3.30) | +0.50 (+0.42, +0.58) | harms |
| t40 | tax 40% | +3.36 (+3.00, +3.74) | +4.34 (+3.97, +4.68) | +1.10 (+0.94, +1.25) | harms |
| asis.t0 | tax 0%, today's rule | -1.31 (-1.48, -1.15) | -2.19 (-2.36, -2.03) | -0.75 (-0.84, -0.65) | works |
| asis.t4 | tax 4%, today's rule | -0.89 (-1.00, -0.79) | -1.47 (-1.59, -1.35) | -0.54 (-0.63, -0.46) | works |
| asis.t8 | tax 8%, today's rule | -0.48 (-0.55, -0.41) | -0.75 (-0.83, -0.68) | -0.38 (-0.45, -0.31) | works |
| asis.t12 | tax 12%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -0.23 (-0.28, -0.19) | does not move |
| asis.t16 | tax 16%, today's rule | +0.54 (+0.47, +0.60) | +0.70 (+0.62, +0.78) | -0.07 (-0.10, -0.05) | harms |
| asis.t20 | tax 20%, today's rule | +1.05 (+0.94, +1.17) | +1.48 (+1.34, +1.61) | +0.07 (+0.04, +0.09) | harms |
| asis.t25 | tax 25%, today's rule | +1.77 (+1.61, +1.94) | +2.33 (+2.12, +2.53) | +0.26 (+0.21, +0.30) | harms |
| asis.t30 | tax 30%, today's rule | +2.44 (+2.23, +2.66) | +3.25 (+2.98, +3.52) | +0.50 (+0.42, +0.58) | harms |
| asis.t40 | tax 40%, today's rule | +3.81 (+3.48, +4.15) | +4.71 (+4.37, +5.04) | +1.11 (+0.95, +1.26) | harms |
| pr0c75 | progression 0 pts, cap 75% | -0.68 (-0.85, -0.54) | -0.60 (-0.74, -0.48) | -0.03 (-0.05, -0.02) | works |
| pr8c75 | progression 8 pts, cap 75% | +0.53 (+0.42, +0.67) | +0.57 (+0.45, +0.70) | +0.04 (+0.02, +0.06) | harms |
| pr0c50 | progression 0 pts, cap 50% | -0.68 (-0.85, -0.54) | -0.60 (-0.74, -0.48) | -0.03 (-0.05, -0.02) | works |
| pr4c50 | progression 4 pts, cap 50% | -0.00 (-0.01, +0.00) | +0.00 (-0.00, +0.01) | +0.00 (+0.00, +0.00) | does not move |
| pr8c50 | progression 8 pts, cap 50% | +0.39 (+0.31, +0.48) | +0.45 (+0.35, +0.56) | +0.02 (+0.01, +0.03) | harms |
| bt0 | business tax 0% | -0.96 (-1.10, -0.82) | -1.70 (-1.87, -1.54) | -0.66 (-0.75, -0.57) | works |
| bt25 | business tax 25% | +1.29 (+1.11, +1.48) | +1.90 (+1.70, +2.09) | +0.22 (+0.18, +0.27) | harms |
| bt50 | business tax 50% | +3.82 (+3.38, +4.29) | +5.18 (+4.78, +5.56) | +1.58 (+1.39, +1.76) | harms |
| bt75 | business tax 75% | +5.84 (+5.29, +6.43) | +8.48 (+7.96, +8.97) | +2.60 (+2.30, +2.89) | harms |
| kp10 | Source keeps 10% of project sales | -0.03 (-0.04, -0.01) | -0.02 (-0.03, -0.00) | -0.00 (-0.00, -0.00) | works |
| kp25 | Source keeps 25% of project sales | -0.05 (-0.08, -0.03) | -0.06 (-0.08, -0.04) | -0.00 (-0.01, -0.00) | works |
| kp50 | Source keeps 50% of project sales | -0.11 (-0.14, -0.07) | -0.15 (-0.18, -0.12) | -0.01 (-0.01, -0.01) | works |
| ex50 | 50% of expired BU recycled | +0.03 (-0.08, +0.13) | +0.25 (+0.17, +0.34) | +0.00 (-0.00, +0.00) | harms |
| ex0 | 0% of expired BU recycled | -0.01 (-0.16, +0.14) | +0.41 (+0.25, +0.57) | +0.00 (-0.00, +0.01) | harms |
| fprog | outside finance: progressive income tax | +48.12 (+46.83, +49.39) | +40.95 (+39.88, +41.95) | +31.08 (+30.46, +31.72) | harms |
| fland | outside finance: land-value tax | +14.06 (+13.45, +14.66) | +15.12 (+14.32, +15.91) | +8.98 (+8.50, +9.43) | harms |
| fflat | outside finance: flat wage contribution | +48.65 (+47.44, +49.85) | +42.15 (+41.06, +43.19) | +18.12 (+17.55, +18.65) | harms |
| br1 | business rate 1x | +5.88 (+5.32, +6.47) | +7.59 (+7.12, +8.05) | +1.82 (+1.57, +2.06) | harms |
| br15 | business rate 1.5x | +4.92 (+4.41, +5.44) | +6.22 (+5.79, +6.63) | +1.52 (+1.31, +1.71) | harms |
| br2 | business rate 2x | +3.46 (+3.05, +3.88) | +4.52 (+4.15, +4.88) | +0.94 (+0.80, +1.06) | harms |
| bu60 | 60% of the BU | +5.00 (+4.47, +5.58) | +6.27 (+5.80, +6.74) | +1.35 (+1.14, +1.55) | harms |
| bu80 | 80% of the BU | +3.02 (+2.65, +3.41) | +3.93 (+3.56, +4.26) | +0.65 (+0.55, +0.75) | harms |
| mm3 | top multiplier 3 | +0.23 (+0.10, +0.35) | +0.62 (+0.48, +0.75) | +0.10 (+0.07, +0.13) | harms |
| mm6 | top multiplier 6 | +0.06 (-0.01, +0.12) | +0.24 (+0.17, +0.32) | +0.00 (+0.00, +0.00) | harms |
| mm9 | top multiplier 9 | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -0.08 (-0.11, -0.05) | does not move |
| oc25 | octave capacity 25% | -0.06 (-0.12, -0.01) | +0.12 (+0.04, +0.19) | -0.00 (-0.02, +0.02) | harms |
| oc50 | octave capacity 50% | -0.03 (-0.06, +0.01) | +0.18 (+0.12, +0.25) | -0.00 (-0.01, +0.01) | harms |
| oc100 | octave capacity 100% | +0.02 (+0.01, +0.04) | +0.13 (+0.11, +0.16) | +0.00 (+0.00, +0.00) | harms |
| no2 | 2 octaves | -0.31 (-0.39, -0.24) | -0.34 (-0.44, -0.24) | +0.00 (-0.02, +0.02) | does not move |
| no4 | 4 octaves | -0.18 (-0.23, -0.12) | -0.20 (-0.26, -0.13) | +0.00 (+0.00, +0.00) | does not move |
| no6 | 6 octaves | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.01 (+0.00, +0.03) | harms |
| phi0 | Phi tier off | -0.02 (-0.05, +0.01) | +0.01 (-0.03, +0.04) | +0.02 (+0.01, +0.04) | harms |
| ph5 | phase-in over 5 years | +0.55 (+0.46, +0.65) | +0.58 (+0.49, +0.66) | +0.03 (-0.01, +0.08) | harms |
| ph10 | phase-in over 10 years | +1.51 (+1.33, +1.68) | +1.57 (+1.39, +1.75) | +0.21 (+0.12, +0.30) | harms |
| cap2 | issuance cap 2% | +7.38 (+6.81, +7.98) | +9.37 (+8.84, +9.92) | +2.37 (+2.09, +2.64) | harms |
| cap4 | issuance cap 4% | +7.38 (+6.81, +7.98) | +9.37 (+8.84, +9.92) | +2.37 (+2.09, +2.64) | harms |
| cap8 | issuance cap 8% | +7.38 (+6.81, +7.98) | +9.37 (+8.84, +9.92) | +2.37 (+2.09, +2.64) | harms |
| ixs | indexation: surge protocol (5%) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ixy | indexation: every year, price level | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ixn | indexation: every year, basic needs | -2.69 (-2.96, -2.41) | -3.25 (-3.52, -2.95) | -0.08 (-0.11, -0.05) | works |
| sva | protected account, all savings | +12.19 (+11.60, +12.77) | +13.72 (+13.17, +14.26) | +8.21 (+7.91, +8.51) | harms |
| svc | protected account, first $10,000 | +0.65 (+0.57, +0.72) | +1.34 (+1.22, +1.47) | +0.48 (+0.44, +0.52) | harms |
| rcap | rent cap for BU tenants | -0.26 (-0.32, -0.21) | -0.43 (-0.50, -0.36) | -0.01 (-0.02, -0.00) | works |
| hc | rent risk ($1.41 a BU dollar) | +6.71 (+6.28, +7.16) | +7.10 (+6.65, +7.58) | +2.72 (+2.59, +2.85) | harms |
| hcrc | rent risk and rent cap | +10.49 (+9.91, +11.10) | +8.60 (+8.14, +9.08) | +3.29 (+3.13, +3.44) | harms |

### programme inflation, points a year: release row, wages 100% (lever effect, seed mean and 95% interval)

| Row | What it sets | Reference | Adverse | Stress | Verdict |
|---|---|---|---|---|---|
| asis | today's joining rule | +0.21 (+0.18, +0.25) | +0.21 (+0.16, +0.25) | +0.00 (+0.00, +0.00) | harms |
| t0 | tax 0% | +2.25 (+2.20, +2.30) | +2.33 (+2.27, +2.39) | +3.70 (+3.65, +3.76) | harms |
| t4 | tax 4% | +1.53 (+1.49, +1.57) | +1.59 (+1.54, +1.64) | +2.94 (+2.90, +2.98) | harms |
| t8 | tax 8% | +0.79 (+0.76, +0.82) | +0.80 (+0.78, +0.83) | +2.13 (+2.10, +2.16) | harms |
| t12 | tax 12% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +1.30 (+1.28, +1.31) | harms |
| t16 | tax 16% | -0.83 (-0.85, -0.81) | -0.85 (-0.88, -0.82) | +0.44 (+0.43, +0.44) | harms |
| t20 | tax 20% | -1.65 (-1.68, -1.62) | -1.70 (-1.74, -1.66) | -0.44 (-0.45, -0.44) | works |
| t25 | tax 25% | -2.67 (-2.70, -2.63) | -2.75 (-2.80, -2.70) | -1.58 (-1.60, -1.55) | works |
| t30 | tax 30% | -3.71 (-3.76, -3.66) | -3.97 (-4.02, -3.90) | -2.74 (-2.78, -2.70) | works |
| t40 | tax 40% | -6.48 (-6.55, -6.42) | -7.20 (-7.27, -7.11) | -5.11 (-5.18, -5.03) | works |
| asis.t0 | tax 0%, today's rule | +1.94 (+1.91, +1.97) | +2.01 (+1.97, +2.04) | +3.66 (+3.60, +3.71) | harms |
| asis.t4 | tax 4%, today's rule | +1.34 (+1.32, +1.36) | +1.40 (+1.37, +1.43) | +2.91 (+2.87, +2.95) | harms |
| asis.t8 | tax 8%, today's rule | +0.70 (+0.68, +0.71) | +0.72 (+0.70, +0.73) | +2.11 (+2.08, +2.14) | harms |
| asis.t12 | tax 12%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +1.28 (+1.27, +1.30) | harms |
| asis.t16 | tax 16%, today's rule | -0.74 (-0.75, -0.72) | -0.77 (-0.78, -0.75) | +0.43 (+0.43, +0.44) | harms |
| asis.t20 | tax 20%, today's rule | -1.51 (-1.53, -1.48) | -1.57 (-1.60, -1.55) | -0.44 (-0.45, -0.43) | works |
| asis.t25 | tax 25%, today's rule | -2.52 (-2.55, -2.48) | -2.63 (-2.66, -2.59) | -1.57 (-1.59, -1.54) | works |
| asis.t30 | tax 30%, today's rule | -3.62 (-3.66, -3.58) | -3.91 (-3.96, -3.86) | -2.71 (-2.75, -2.68) | works |
| asis.t40 | tax 40%, today's rule | -6.48 (-6.54, -6.43) | -7.19 (-7.26, -7.12) | -5.07 (-5.14, -4.99) | works |
| pr0c75 | progression 0 pts, cap 75% | +0.19 (+0.15, +0.23) | +0.09 (+0.05, +0.13) | +0.14 (+0.12, +0.15) | harms |
| pr8c75 | progression 8 pts, cap 75% | -0.46 (-0.52, -0.39) | -0.38 (-0.46, -0.30) | -0.14 (-0.15, -0.12) | works |
| pr0c50 | progression 0 pts, cap 50% | +0.19 (+0.15, +0.23) | +0.09 (+0.05, +0.13) | +0.14 (+0.12, +0.15) | harms |
| pr4c50 | progression 4 pts, cap 50% | -0.00 (-0.00, +0.00) | -0.00 (-0.01, -0.00) | +0.00 (+0.00, +0.00) | does not move |
| pr8c50 | progression 8 pts, cap 50% | -0.34 (-0.39, -0.29) | -0.29 (-0.35, -0.23) | -0.08 (-0.09, -0.07) | works |
| bt0 | business tax 0% | +1.87 (+1.83, +1.90) | +2.04 (+1.99, +2.08) | +3.39 (+3.33, +3.45) | harms |
| bt25 | business tax 25% | -2.15 (-2.19, -2.11) | -2.34 (-2.39, -2.30) | -1.44 (-1.47, -1.42) | works |
| bt50 | business tax 50% | -8.13 (-8.24, -8.03) | -9.44 (-9.56, -9.32) | -6.84 (-6.95, -6.73) | works |
| bt75 | business tax 75% | -16.02 (-16.20, -15.87) | -18.52 (-18.72, -18.34) | -11.98 (-12.16, -11.79) | works |
| kp10 | Source keeps 10% of project sales | -0.24 (-0.24, -0.23) | -0.24 (-0.24, -0.23) | -0.01 (-0.01, -0.01) | works |
| kp25 | Source keeps 25% of project sales | -0.60 (-0.61, -0.59) | -0.59 (-0.60, -0.58) | -0.03 (-0.03, -0.03) | works |
| kp50 | Source keeps 50% of project sales | -1.21 (-1.23, -1.19) | -1.20 (-1.22, -1.17) | -0.06 (-0.06, -0.06) | works |
| ex50 | 50% of expired BU recycled | +0.68 (+0.65, +0.71) | +0.76 (+0.74, +0.79) | +0.00 (+0.00, +0.00) | harms |
| ex0 | 0% of expired BU recycled | +1.38 (+1.34, +1.43) | +1.56 (+1.52, +1.61) | +0.00 (+0.00, +0.01) | harms |
| fprog | outside finance: progressive income tax | -12.08 (-12.43, -11.70) | -7.25 (-7.78, -6.71) | -24.62 (-25.06, -24.19) | works |
| fland | outside finance: land-value tax | -45.48 (-45.85, -45.12) | -47.38 (-47.80, -46.88) | -26.28 (-26.77, -25.79) | works |
| fflat | outside finance: flat wage contribution | -50.82 (-51.29, -50.37) | -60.87 (-61.49, -60.29) | -27.68 (-28.21, -27.14) | works |
| br1 | business rate 1x | -16.19 (-16.37, -16.04) | -19.25 (-19.46, -19.06) | -12.17 (-12.36, -11.98) | works |
| br15 | business rate 1.5x | -12.00 (-12.14, -11.88) | -14.19 (-14.35, -14.05) | -9.92 (-10.08, -9.77) | works |
| br2 | business rate 2x | -6.95 (-7.04, -6.86) | -8.15 (-8.26, -8.06) | -6.38 (-6.48, -6.28) | works |
| bu60 | 60% of the BU | -16.09 (-16.27, -15.92) | -19.68 (-19.92, -19.45) | -10.29 (-10.48, -10.10) | works |
| bu80 | 80% of the BU | -6.64 (-6.74, -6.55) | -8.29 (-8.42, -8.17) | -5.05 (-5.14, -4.95) | works |
| mm3 | top multiplier 3 | -0.32 (-0.36, -0.28) | +0.06 (+0.02, +0.10) | -0.49 (-0.51, -0.47) | harms |
| mm6 | top multiplier 6 | -0.15 (-0.17, -0.13) | -0.00 (-0.02, +0.02) | +0.00 (+0.00, +0.00) | does not move |
| mm9 | top multiplier 9 | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.35 (+0.33, +0.36) | harms |
| oc25 | octave capacity 25% | +0.06 (+0.04, +0.09) | +0.42 (+0.40, +0.45) | -0.00 (-0.01, +0.00) | harms |
| oc50 | octave capacity 50% | +0.01 (-0.01, +0.02) | +0.26 (+0.24, +0.27) | -0.00 (-0.01, +0.00) | harms |
| oc100 | octave capacity 100% | +0.02 (+0.01, +0.02) | +0.12 (+0.11, +0.13) | +0.00 (+0.00, +0.00) | harms |
| no2 | 2 octaves | -0.15 (-0.19, -0.12) | +0.12 (+0.09, +0.15) | +0.03 (+0.03, +0.04) | harms |
| no4 | 4 octaves | -0.09 (-0.12, -0.07) | +0.08 (+0.06, +0.10) | +0.00 (+0.00, +0.00) | harms |
| no6 | 6 octaves | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -0.03 (-0.04, -0.03) | does not move |
| phi0 | Phi tier off | +0.05 (+0.04, +0.05) | +0.06 (+0.06, +0.07) | -0.07 (-0.08, -0.06) | harms |
| ph5 | phase-in over 5 years | -1.90 (-1.93, -1.87) | -2.06 (-2.09, -2.04) | -1.40 (-1.43, -1.37) | works |
| ph10 | phase-in over 10 years | -4.45 (-4.50, -4.40) | -4.85 (-4.90, -4.81) | -3.35 (-3.41, -3.29) | works |
| cap2 | issuance cap 2% | -18.69 (-18.82, -18.58) | -20.90 (-21.04, -20.77) | -12.43 (-12.63, -12.23) | works |
| cap4 | issuance cap 4% | -18.69 (-18.82, -18.58) | -20.90 (-21.04, -20.77) | -12.43 (-12.63, -12.23) | works |
| cap8 | issuance cap 8% | -18.69 (-18.82, -18.58) | -20.90 (-21.04, -20.77) | -12.43 (-12.63, -12.23) | works |
| ixs | indexation: surge protocol (5%) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ixy | indexation: every year, price level | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ixn | indexation: every year, basic needs | +1.43 (+1.34, +1.52) | +1.80 (+1.69, +1.90) | +0.22 (+0.19, +0.24) | harms |
| sva | protected account, all savings | +1067.51 (+1041.35, +1095.64) | +1328.71 (+1295.38, +1363.82) | +1193.79 (+1161.93, +1227.31) | harms |
| svc | protected account, first $10,000 | +9.17 (+9.02, +9.34) | +14.19 (+13.94, +14.46) | +5.64 (+5.53, +5.76) | harms |
| rcap | rent cap for BU tenants | -0.25 (-0.26, -0.24) | -0.29 (-0.31, -0.28) | +0.01 (+0.00, +0.01) | harms |
| hc | rent risk ($1.41 a BU dollar) | +1.51 (+1.46, +1.56) | +1.35 (+1.29, +1.41) | -0.04 (-0.04, -0.04) | harms |
| hcrc | rent risk and rent cap | -1.00 (-1.03, -0.97) | -1.31 (-1.35, -1.28) | -0.06 (-0.07, -0.06) | works |

### participation, mean of years 1-19, %: release row, wages 100% (lever effect, seed mean and 95% interval)

| Row | What it sets | Reference | Adverse | Stress | Verdict |
|---|---|---|---|---|---|
| asis | today's joining rule | +0.37 (+0.31, +0.44) | +0.28 (+0.22, +0.34) | +0.00 (+0.00, +0.00) | does not move |
| t0 | tax 0% | +0.69 (+0.58, +0.80) | +0.59 (+0.48, +0.70) | +0.09 (+0.07, +0.12) | works |
| t4 | tax 4% | +0.44 (+0.35, +0.52) | +0.36 (+0.28, +0.44) | +0.06 (+0.04, +0.09) | works |
| t8 | tax 8% | +0.22 (+0.16, +0.29) | +0.16 (+0.12, +0.21) | +0.04 (+0.03, +0.06) | works |
| t12 | tax 12% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.02 (+0.01, +0.03) | does not move |
| t16 | tax 16% | -0.23 (-0.28, -0.17) | -0.16 (-0.21, -0.12) | +0.01 (+0.00, +0.01) | harms |
| t20 | tax 20% | -0.36 (-0.44, -0.28) | -0.25 (-0.32, -0.19) | -0.01 (-0.01, -0.00) | harms |
| t25 | tax 25% | -0.40 (-0.48, -0.32) | -0.26 (-0.33, -0.20) | -0.03 (-0.03, -0.02) | harms |
| t30 | tax 30% | -0.30 (-0.37, -0.22) | -0.18 (-0.26, -0.11) | -0.05 (-0.06, -0.04) | harms |
| t40 | tax 40% | -0.10 (-0.19, -0.02) | -0.11 (-0.19, -0.03) | -0.10 (-0.11, -0.09) | harms |
| asis.t0 | tax 0%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t4 | tax 4%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t8 | tax 8%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t12 | tax 12%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t16 | tax 16%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t20 | tax 20%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t25 | tax 25%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t30 | tax 30%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t40 | tax 40%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| pr0c75 | progression 0 pts, cap 75% | +0.33 (+0.26, +0.41) | +0.26 (+0.20, +0.33) | +0.01 (+0.00, +0.02) | works |
| pr8c75 | progression 8 pts, cap 75% | -0.96 (-1.10, -0.83) | -0.76 (-0.89, -0.63) | -0.02 (-0.02, -0.01) | harms |
| pr0c50 | progression 0 pts, cap 50% | +0.33 (+0.26, +0.41) | +0.26 (+0.20, +0.33) | +0.01 (+0.00, +0.02) | works |
| pr4c50 | progression 4 pts, cap 50% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| pr8c50 | progression 8 pts, cap 50% | -0.73 (-0.85, -0.62) | -0.58 (-0.69, -0.48) | -0.01 (-0.02, -0.01) | harms |
| bt0 | business tax 0% | -0.12 (-0.15, -0.09) | -0.12 (-0.14, -0.09) | -0.04 (-0.05, -0.02) | harms |
| bt25 | business tax 25% | +0.16 (+0.12, +0.20) | +0.13 (+0.10, +0.16) | +0.00 (+0.00, +0.00) | does not move |
| bt50 | business tax 50% | +0.37 (+0.30, +0.43) | +0.28 (+0.22, +0.34) | +0.00 (+0.00, +0.00) | does not move |
| bt75 | business tax 75% | +0.37 (+0.31, +0.44) | +0.28 (+0.22, +0.34) | +0.00 (+0.00, +0.00) | does not move |
| kp10 | Source keeps 10% of project sales | +0.00 (-0.00, +0.00) | +0.00 (-0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| kp25 | Source keeps 25% of project sales | -0.00 (-0.01, +0.00) | -0.00 (-0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| kp50 | Source keeps 50% of project sales | -0.00 (-0.01, +0.00) | -0.00 (-0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ex50 | 50% of expired BU recycled | +0.16 (+0.12, +0.21) | +0.11 (+0.08, +0.14) | +0.00 (+0.00, +0.00) | does not move |
| ex0 | 0% of expired BU recycled | +0.37 (+0.31, +0.44) | +0.28 (+0.22, +0.34) | +0.00 (+0.00, +0.00) | does not move |
| fprog | outside finance: progressive income tax | -0.10 (-0.13, -0.08) | -0.04 (-0.05, -0.03) | -3.13 (-3.66, -2.61) | harms |
| fland | outside finance: land-value tax | -2.71 (-2.89, -2.54) | -0.41 (-0.47, -0.35) | -6.13 (-6.51, -5.75) | harms |
| fflat | outside finance: flat wage contribution | -0.01 (-0.09, +0.07) | -13.02 (-13.43, -12.58) | -7.73 (-8.09, -7.37) | harms |
| br1 | business rate 1x | +0.37 (+0.31, +0.44) | +0.28 (+0.22, +0.34) | +0.00 (+0.00, +0.00) | does not move |
| br15 | business rate 1.5x | +0.37 (+0.31, +0.44) | +0.28 (+0.22, +0.34) | +0.00 (+0.00, +0.00) | does not move |
| br2 | business rate 2x | +0.35 (+0.29, +0.41) | +0.27 (+0.21, +0.32) | +0.00 (+0.00, +0.00) | does not move |
| bu60 | 60% of the BU | +0.37 (+0.31, +0.44) | +0.28 (+0.22, +0.34) | +0.00 (+0.00, +0.00) | does not move |
| bu80 | 80% of the BU | +0.34 (+0.28, +0.40) | +0.26 (+0.21, +0.32) | +0.00 (+0.00, +0.00) | does not move |
| mm3 | top multiplier 3 | +0.17 (+0.13, +0.21) | +0.12 (+0.08, +0.15) | +0.00 (+0.00, +0.00) | does not move |
| mm6 | top multiplier 6 | +0.08 (+0.06, +0.11) | +0.05 (+0.03, +0.07) | +0.00 (+0.00, +0.00) | does not move |
| mm9 | top multiplier 9 | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| oc25 | octave capacity 25% | -0.04 (-0.05, -0.03) | -0.02 (-0.03, -0.01) | +0.00 (+0.00, +0.00) | harms |
| oc50 | octave capacity 50% | -0.02 (-0.03, -0.01) | -0.01 (-0.01, -0.00) | +0.00 (+0.00, +0.00) | harms |
| oc100 | octave capacity 100% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| no2 | 2 octaves | -0.08 (-0.11, -0.06) | -0.06 (-0.07, -0.04) | +0.00 (-0.00, +0.00) | harms |
| no4 | 4 octaves | -0.05 (-0.07, -0.04) | -0.03 (-0.04, -0.02) | +0.00 (+0.00, +0.00) | harms |
| no6 | 6 octaves | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| phi0 | Phi tier off | +0.02 (+0.01, +0.03) | +0.01 (+0.01, +0.02) | +0.00 (+0.00, +0.00) | does not move |
| ph5 | phase-in over 5 years | +0.04 (+0.03, +0.05) | +0.03 (+0.02, +0.04) | +0.00 (+0.00, +0.00) | does not move |
| ph10 | phase-in over 10 years | +0.13 (+0.10, +0.15) | +0.10 (+0.08, +0.13) | +0.00 (+0.00, +0.00) | does not move |
| cap2 | issuance cap 2% | +0.36 (+0.30, +0.43) | +0.27 (+0.21, +0.32) | +0.00 (+0.00, +0.00) | does not move |
| cap4 | issuance cap 4% | +0.36 (+0.30, +0.43) | +0.27 (+0.21, +0.32) | +0.00 (+0.00, +0.00) | does not move |
| cap8 | issuance cap 8% | +0.36 (+0.30, +0.43) | +0.27 (+0.21, +0.32) | +0.00 (+0.00, +0.00) | does not move |
| ixs | indexation: surge protocol (5%) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ixy | indexation: every year, price level | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ixn | indexation: every year, basic needs | +1.72 (+1.55, +1.90) | +1.79 (+1.61, +1.96) | +0.19 (+0.15, +0.24) | works |
| sva | protected account, all savings | +0.36 (+0.29, +0.42) | +0.27 (+0.21, +0.32) | +0.00 (+0.00, +0.00) | does not move |
| svc | protected account, first $10,000 | +0.06 (+0.04, +0.08) | +0.05 (+0.03, +0.07) | +0.00 (+0.00, +0.00) | does not move |
| rcap | rent cap for BU tenants | -0.04 (-0.05, -0.03) | -0.03 (-0.04, -0.02) | +0.00 (+0.00, +0.00) | harms |
| hc | rent risk ($1.41 a BU dollar) | +0.21 (+0.16, +0.26) | +0.15 (+0.10, +0.20) | +0.00 (+0.00, +0.00) | does not move |
| hcrc | rent risk and rent cap | -0.04 (-0.05, -0.03) | -0.03 (-0.04, -0.02) | +0.00 (+0.00, +0.00) | harms |

### basket poverty, % of adult-years: release row, wages 90% (lever effect, seed mean and 95% interval)

| Row | What it sets | Reference | Adverse | Stress | Verdict |
|---|---|---|---|---|---|
| asis | today's joining rule | -0.03 (-0.06, -0.01) | -0.01 (-0.03, +0.01) | +0.00 (+0.00, +0.00) | does not move |
| t0 | tax 0% | -3.30 (-3.41, -3.20) | -3.16 (-3.25, -3.07) | -0.89 (-0.96, -0.83) | works |
| t4 | tax 4% | -2.17 (-2.24, -2.09) | -2.06 (-2.13, -1.99) | -0.65 (-0.71, -0.59) | works |
| t8 | tax 8% | -1.06 (-1.11, -1.01) | -1.04 (-1.08, -0.99) | -0.45 (-0.51, -0.40) | works |
| t12 | tax 12% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -0.25 (-0.30, -0.21) | does not move |
| t16 | tax 16% | +1.04 (+0.99, +1.09) | +0.92 (+0.89, +0.97) | -0.09 (-0.11, -0.07) | harms |
| t20 | tax 20% | +2.08 (+2.00, +2.16) | +1.84 (+1.78, +1.88) | +0.08 (+0.06, +0.10) | harms |
| t25 | tax 25% | +3.31 (+3.20, +3.42) | +2.90 (+2.81, +2.97) | +0.31 (+0.26, +0.36) | harms |
| t30 | tax 30% | +4.33 (+4.20, +4.48) | +3.81 (+3.70, +3.91) | +0.57 (+0.48, +0.67) | harms |
| t40 | tax 40% | +5.98 (+5.80, +6.17) | +5.61 (+5.48, +5.73) | +1.25 (+1.09, +1.43) | harms |
| asis.t0 | tax 0%, today's rule | -3.16 (-3.26, -3.07) | -3.03 (-3.11, -2.96) | -0.89 (-0.96, -0.81) | works |
| asis.t4 | tax 4%, today's rule | -2.08 (-2.15, -2.01) | -1.99 (-2.05, -1.94) | -0.65 (-0.71, -0.58) | works |
| asis.t8 | tax 8%, today's rule | -1.01 (-1.05, -0.97) | -1.00 (-1.04, -0.97) | -0.46 (-0.51, -0.40) | works |
| asis.t12 | tax 12%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -0.26 (-0.30, -0.21) | does not move |
| asis.t16 | tax 16%, today's rule | +1.01 (+0.96, +1.06) | +0.91 (+0.88, +0.95) | -0.09 (-0.11, -0.07) | harms |
| asis.t20 | tax 20%, today's rule | +2.03 (+1.95, +2.11) | +1.81 (+1.75, +1.86) | +0.08 (+0.06, +0.10) | harms |
| asis.t25 | tax 25%, today's rule | +3.25 (+3.13, +3.37) | +2.87 (+2.79, +2.94) | +0.32 (+0.27, +0.37) | harms |
| asis.t30 | tax 30%, today's rule | +4.31 (+4.17, +4.45) | +3.78 (+3.68, +3.88) | +0.57 (+0.49, +0.67) | harms |
| asis.t40 | tax 40%, today's rule | +5.99 (+5.80, +6.18) | +5.59 (+5.46, +5.71) | +1.26 (+1.11, +1.44) | harms |
| pr0c75 | progression 0 pts, cap 75% | -0.44 (-0.49, -0.39) | -0.37 (-0.40, -0.33) | -0.01 (-0.03, +0.01) | does not move |
| pr8c75 | progression 8 pts, cap 75% | +0.51 (+0.46, +0.57) | +0.36 (+0.32, +0.40) | +0.03 (+0.01, +0.04) | harms |
| pr0c50 | progression 0 pts, cap 50% | -0.44 (-0.49, -0.39) | -0.37 (-0.40, -0.33) | -0.01 (-0.03, +0.01) | does not move |
| pr4c50 | progression 4 pts, cap 50% | -0.01 (-0.02, -0.01) | -0.01 (-0.01, -0.00) | +0.00 (+0.00, +0.00) | does not move |
| pr8c50 | progression 8 pts, cap 50% | +0.37 (+0.32, +0.43) | +0.26 (+0.23, +0.30) | +0.01 (+0.00, +0.03) | harms |
| bt0 | business tax 0% | -2.66 (-2.75, -2.58) | -2.56 (-2.63, -2.49) | -0.82 (-0.88, -0.75) | works |
| bt25 | business tax 25% | +2.94 (+2.84, +3.04) | +2.57 (+2.49, +2.65) | +0.26 (+0.22, +0.31) | harms |
| bt50 | business tax 50% | +6.59 (+6.40, +6.80) | +6.36 (+6.21, +6.53) | +1.67 (+1.46, +1.91) | harms |
| bt75 | business tax 75% | +8.91 (+8.65, +9.19) | +10.40 (+10.13, +10.70) | +2.61 (+2.28, +2.94) | harms |
| kp10 | Source keeps 10% of project sales | -0.10 (-0.11, -0.09) | -0.07 (-0.08, -0.06) | -0.01 (-0.01, -0.01) | works |
| kp25 | Source keeps 25% of project sales | -0.26 (-0.28, -0.24) | -0.19 (-0.21, -0.17) | -0.03 (-0.03, -0.02) | works |
| kp50 | Source keeps 50% of project sales | -0.50 (-0.53, -0.47) | -0.39 (-0.42, -0.37) | -0.05 (-0.06, -0.04) | works |
| ex50 | 50% of expired BU recycled | +1.09 (+1.04, +1.15) | +0.76 (+0.72, +0.80) | +0.00 (+0.00, +0.01) | harms |
| ex0 | 0% of expired BU recycled | +2.11 (+2.02, +2.21) | +1.43 (+1.37, +1.49) | +0.01 (+0.00, +0.01) | harms |
| fprog | outside finance: progressive income tax | +40.48 (+39.91, +41.02) | +30.93 (+30.44, +31.39) | +22.92 (+22.49, +23.35) | harms |
| fland | outside finance: land-value tax | -1.14 (-1.63, -0.68) | -0.46 (-0.94, -0.02) | -0.18 (-0.55, +0.19) | does not move |
| fflat | outside finance: flat wage contribution | +29.75 (+29.17, +30.32) | +25.90 (+25.30, +26.43) | +7.35 (+6.98, +7.70) | harms |
| br1 | business rate 1x | +8.95 (+8.69, +9.24) | +9.54 (+9.38, +9.71) | +1.77 (+1.54, +2.02) | harms |
| br15 | business rate 1.5x | +7.81 (+7.59, +8.04) | +7.89 (+7.75, +8.03) | +1.57 (+1.36, +1.78) | harms |
| br2 | business rate 2x | +6.14 (+5.96, +6.33) | +5.64 (+5.51, +5.76) | +1.03 (+0.89, +1.17) | harms |
| bu60 | 60% of the BU | +6.96 (+6.70, +7.23) | +7.11 (+6.93, +7.29) | +1.19 (+1.00, +1.38) | harms |
| bu80 | 80% of the BU | +5.11 (+4.93, +5.30) | +4.41 (+4.29, +4.52) | +0.70 (+0.60, +0.80) | harms |
| mm3 | top multiplier 3 | +1.57 (+1.48, +1.66) | +1.52 (+1.47, +1.57) | +0.21 (+0.18, +0.24) | harms |
| mm6 | top multiplier 6 | +0.64 (+0.59, +0.69) | +0.62 (+0.58, +0.65) | +0.00 (+0.00, +0.00) | harms |
| mm9 | top multiplier 9 | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -0.12 (-0.15, -0.08) | does not move |
| oc25 | octave capacity 25% | +0.43 (+0.38, +0.48) | +0.22 (+0.18, +0.26) | +0.07 (+0.06, +0.09) | harms |
| oc50 | octave capacity 50% | +0.36 (+0.32, +0.40) | +0.18 (+0.14, +0.21) | +0.04 (+0.03, +0.05) | harms |
| oc100 | octave capacity 100% | +0.27 (+0.25, +0.29) | +0.11 (+0.09, +0.12) | +0.00 (+0.00, +0.00) | harms |
| no2 | 2 octaves | -0.43 (-0.48, -0.38) | -0.13 (-0.19, -0.08) | +0.07 (+0.04, +0.09) | harms |
| no4 | 4 octaves | -0.15 (-0.18, -0.11) | -0.00 (-0.04, +0.03) | +0.00 (+0.00, +0.00) | does not move |
| no6 | 6 octaves | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -0.03 (-0.05, -0.01) | does not move |
| phi0 | Phi tier off | +0.12 (+0.09, +0.14) | +0.09 (+0.07, +0.11) | +0.02 (+0.00, +0.03) | harms |
| ph5 | phase-in over 5 years | +0.45 (+0.37, +0.52) | +0.55 (+0.48, +0.62) | -0.42 (-0.49, -0.36) | harms |
| ph10 | phase-in over 10 years | +1.27 (+1.14, +1.41) | +1.59 (+1.47, +1.71) | -0.65 (-0.77, -0.53) | harms |
| cap2 | issuance cap 2% | +12.33 (+11.95, +12.73) | +13.04 (+12.76, +13.31) | +3.16 (+2.90, +3.41) | harms |
| cap4 | issuance cap 4% | +12.33 (+11.95, +12.73) | +13.04 (+12.76, +13.31) | +3.16 (+2.90, +3.41) | harms |
| cap8 | issuance cap 8% | +12.33 (+11.95, +12.73) | +13.04 (+12.76, +13.31) | +3.16 (+2.90, +3.41) | harms |
| ixs | indexation: surge protocol (5%) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ixy | indexation: every year, price level | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ixn | indexation: every year, basic needs | -0.40 (-0.46, -0.35) | -0.56 (-0.61, -0.51) | +0.03 (+0.01, +0.05) | harms |
| sva | protected account, all savings | +38.25 (+37.78, +38.69) | +27.27 (+26.84, +27.65) | +22.04 (+21.64, +22.43) | harms |
| svc | protected account, first $10,000 | +5.52 (+5.36, +5.70) | +5.12 (+4.99, +5.25) | +2.39 (+2.32, +2.45) | harms |
| rcap | rent cap for BU tenants | -0.44 (-0.47, -0.41) | -0.43 (-0.46, -0.40) | -0.03 (-0.03, -0.02) | works |
| hc | rent risk ($1.41 a BU dollar) | +8.36 (+8.16, +8.56) | +6.77 (+6.63, +6.91) | +2.61 (+2.54, +2.68) | harms |
| hcrc | rent risk and rent cap | +1.71 (+1.58, +1.84) | +0.96 (+0.87, +1.06) | +1.62 (+1.56, +1.68) | harms |

### wealth poverty at year 20, %: release row, wages 90% (lever effect, seed mean and 95% interval)

| Row | What it sets | Reference | Adverse | Stress | Verdict |
|---|---|---|---|---|---|
| asis | today's joining rule | +0.08 (+0.02, +0.15) | +0.01 (+0.00, +0.02) | +0.00 (+0.00, +0.00) | harms |
| t0 | tax 0% | -1.59 (-1.80, -1.41) | -0.75 (-0.90, -0.60) | +0.56 (+0.32, +0.82) | harms |
| t4 | tax 4% | -0.94 (-1.10, -0.80) | -0.44 (-0.58, -0.31) | +0.47 (+0.24, +0.70) | harms |
| t8 | tax 8% | -0.30 (-0.40, -0.20) | -0.23 (-0.33, -0.14) | +0.37 (+0.20, +0.55) | harms |
| t12 | tax 12% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.32 (+0.17, +0.46) | harms |
| t16 | tax 16% | +0.52 (+0.38, +0.66) | +0.19 (+0.12, +0.26) | +0.10 (+0.02, +0.18) | harms |
| t20 | tax 20% | +1.00 (+0.78, +1.22) | +0.31 (+0.22, +0.39) | -0.14 (-0.22, -0.08) | harms |
| t25 | tax 25% | +1.48 (+1.22, +1.75) | +0.42 (+0.32, +0.51) | -0.48 (-0.65, -0.32) | harms |
| t30 | tax 30% | +1.75 (+1.46, +2.03) | +0.50 (+0.39, +0.60) | -0.92 (-1.19, -0.65) | harms |
| t40 | tax 40% | +1.88 (+1.56, +2.20) | +0.64 (+0.53, +0.74) | -1.95 (-2.41, -1.50) | harms |
| asis.t0 | tax 0%, today's rule | -1.70 (-1.90, -1.50) | -0.75 (-0.90, -0.60) | +0.51 (+0.28, +0.75) | harms |
| asis.t4 | tax 4%, today's rule | -0.95 (-1.12, -0.79) | -0.44 (-0.57, -0.31) | +0.46 (+0.24, +0.69) | harms |
| asis.t8 | tax 8%, today's rule | -0.35 (-0.47, -0.23) | -0.22 (-0.31, -0.14) | +0.36 (+0.18, +0.53) | harms |
| asis.t12 | tax 12%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.30 (+0.15, +0.44) | harms |
| asis.t16 | tax 16%, today's rule | +0.54 (+0.39, +0.68) | +0.18 (+0.12, +0.25) | +0.10 (+0.02, +0.18) | harms |
| asis.t20 | tax 20%, today's rule | +1.08 (+0.84, +1.30) | +0.31 (+0.22, +0.40) | -0.14 (-0.21, -0.08) | harms |
| asis.t25 | tax 25%, today's rule | +1.52 (+1.24, +1.80) | +0.42 (+0.32, +0.52) | -0.47 (-0.64, -0.31) | harms |
| asis.t30 | tax 30%, today's rule | +1.76 (+1.48, +2.03) | +0.50 (+0.39, +0.60) | -0.90 (-1.17, -0.63) | harms |
| asis.t40 | tax 40%, today's rule | +1.90 (+1.60, +2.20) | +0.63 (+0.52, +0.74) | -1.91 (-2.36, -1.46) | harms |
| pr0c75 | progression 0 pts, cap 75% | -0.15 (-0.23, -0.09) | -0.01 (-0.02, +0.00) | +0.00 (-0.06, +0.07) | does not move |
| pr8c75 | progression 8 pts, cap 75% | +0.03 (-0.05, +0.10) | -0.00 (-0.03, +0.02) | +0.04 (-0.03, +0.10) | does not move |
| pr0c50 | progression 0 pts, cap 50% | -0.15 (-0.23, -0.09) | -0.01 (-0.02, +0.00) | +0.00 (-0.06, +0.07) | does not move |
| pr4c50 | progression 4 pts, cap 50% | -0.01 (-0.02, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| pr8c50 | progression 8 pts, cap 50% | +0.01 (-0.06, +0.08) | -0.01 (-0.04, +0.00) | +0.05 (-0.01, +0.10) | does not move |
| bt0 | business tax 0% | -1.44 (-1.64, -1.27) | -0.70 (-0.85, -0.54) | +0.56 (+0.31, +0.80) | harms |
| bt25 | business tax 25% | +1.47 (+1.19, +1.75) | +0.43 (+0.32, +0.53) | -0.55 (-0.70, -0.40) | harms |
| bt50 | business tax 50% | +1.90 (+1.59, +2.24) | +0.76 (+0.64, +0.88) | -3.64 (-4.21, -3.08) | harms |
| bt75 | business tax 75% | -1.25 (-1.81, -0.68) | +0.87 (+0.73, +1.01) | -10.16 (-11.01, -9.34) | harms |
| kp10 | Source keeps 10% of project sales | -0.08 (-0.13, -0.03) | -0.01 (-0.02, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| kp25 | Source keeps 25% of project sales | -0.15 (-0.22, -0.09) | -0.03 (-0.06, -0.01) | -0.02 (-0.04, +0.00) | does not move |
| kp50 | Source keeps 50% of project sales | -0.41 (-0.50, -0.31) | -0.07 (-0.11, -0.03) | -0.04 (-0.07, -0.01) | works |
| ex50 | 50% of expired BU recycled | +0.72 (+0.56, +0.90) | +0.10 (+0.05, +0.17) | +0.00 (+0.00, +0.00) | harms |
| ex0 | 0% of expired BU recycled | +1.22 (+1.02, +1.43) | +0.19 (+0.12, +0.26) | +0.00 (+0.00, +0.00) | harms |
| fprog | outside finance: progressive income tax | +6.40 (+5.96, +6.83) | +0.89 (+0.76, +1.02) | -19.63 (-20.74, -18.41) | harms |
| fland | outside finance: land-value tax | -69.96 (-70.81, -69.14) | -14.06 (-15.51, -12.65) | -49.32 (-50.02, -48.65) | works |
| fflat | outside finance: flat wage contribution | -45.52 (-46.31, -44.74) | -35.60 (-36.17, -35.01) | -38.84 (-39.48, -38.20) | works |
| br1 | business rate 1x | -1.40 (-1.98, -0.81) | +0.86 (+0.72, +1.00) | -11.26 (-12.05, -10.48) | harms |
| br15 | business rate 1.5x | +0.98 (+0.54, +1.42) | +0.84 (+0.71, +0.97) | -7.59 (-8.28, -6.89) | harms |
| br2 | business rate 2x | +1.98 (+1.64, +2.34) | +0.69 (+0.58, +0.80) | -3.49 (-4.00, -3.00) | harms |
| bu60 | 60% of the BU | -8.10 (-8.63, -7.54) | -0.53 (-0.67, -0.40) | -10.10 (-10.63, -9.56) | works |
| bu80 | 80% of the BU | -0.96 (-1.23, -0.68) | -0.01 (-0.08, +0.05) | -3.66 (-4.04, -3.32) | does not move |
| mm3 | top multiplier 3 | +0.54 (+0.40, +0.69) | +0.09 (+0.04, +0.14) | +0.12 (+0.00, +0.23) | harms |
| mm6 | top multiplier 6 | +0.17 (+0.08, +0.26) | +0.02 (+0.00, +0.06) | +0.00 (+0.00, +0.00) | harms |
| mm9 | top multiplier 9 | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -0.11 (-0.19, -0.02) | does not move |
| oc25 | octave capacity 25% | +0.74 (+0.60, +0.89) | +0.09 (+0.02, +0.16) | +0.42 (+0.32, +0.52) | harms |
| oc50 | octave capacity 50% | +0.62 (+0.48, +0.76) | +0.07 (+0.01, +0.14) | +0.22 (+0.15, +0.31) | harms |
| oc100 | octave capacity 100% | +0.41 (+0.30, +0.53) | +0.08 (+0.03, +0.13) | +0.00 (+0.00, +0.00) | harms |
| no2 | 2 octaves | -0.04 (-0.12, +0.03) | -0.07 (-0.13, -0.02) | +0.43 (+0.33, +0.54) | harms |
| no4 | 4 octaves | +0.04 (-0.00, +0.08) | -0.03 (-0.07, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| no6 | 6 octaves | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -0.64 (-0.78, -0.51) | does not move |
| phi0 | Phi tier off | +0.04 (+0.02, +0.08) | +0.00 (+0.00, +0.00) | +0.00 (-0.04, +0.05) | harms |
| ph5 | phase-in over 5 years | -0.38 (-0.53, -0.22) | -0.04 (-0.10, +0.01) | -1.14 (-1.32, -0.96) | does not move |
| ph10 | phase-in over 10 years | -1.38 (-1.64, -1.11) | -0.18 (-0.25, -0.12) | -2.82 (-3.11, -2.52) | works |
| cap2 | issuance cap 2% | -1.02 (-1.55, -0.47) | +0.86 (+0.72, +1.00) | -9.74 (-10.51, -8.97) | harms |
| cap4 | issuance cap 4% | -1.02 (-1.55, -0.47) | +0.86 (+0.72, +1.00) | -9.74 (-10.51, -8.97) | harms |
| cap8 | issuance cap 8% | -1.02 (-1.55, -0.47) | +0.86 (+0.72, +1.00) | -9.74 (-10.51, -8.97) | harms |
| ixs | indexation: surge protocol (5%) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ixy | indexation: every year, price level | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ixn | indexation: every year, basic needs | +0.25 (+0.18, +0.33) | +0.02 (-0.02, +0.07) | +0.08 (+0.03, +0.15) | harms |
| sva | protected account, all savings | -53.61 (-54.28, -52.99) | -58.58 (-59.14, -58.02) | -44.08 (-44.82, -43.37) | works |
| svc | protected account, first $10,000 | -27.18 (-27.93, -26.38) | -21.44 (-21.94, -20.91) | -3.97 (-4.37, -3.53) | works |
| rcap | rent cap for BU tenants | -0.04 (-0.09, -0.01) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| hc | rent risk ($1.41 a BU dollar) | +1.91 (+1.67, +2.14) | +0.22 (+0.14, +0.31) | +0.49 (+0.37, +0.63) | harms |
| hcrc | rent risk and rent cap | -0.31 (-0.40, -0.22) | -0.08 (-0.15, -0.04) | +0.12 (+0.05, +0.18) | harms |

### non-participants' basket poverty, %: release row, wages 90% (lever effect, seed mean and 95% interval)

| Row | What it sets | Reference | Adverse | Stress | Verdict |
|---|---|---|---|---|---|
| asis | today's joining rule | -0.38 (-0.52, -0.25) | -0.19 (-0.27, -0.13) | -0.00 (-0.00, +0.00) | does not move |
| t0 | tax 0% | -2.81 (-3.04, -2.60) | -2.40 (-2.60, -2.22) | +0.07 (+0.01, +0.14) | harms |
| t4 | tax 4% | -1.79 (-1.96, -1.62) | -1.56 (-1.70, -1.42) | +0.10 (+0.04, +0.16) | harms |
| t8 | tax 8% | -0.86 (-0.99, -0.74) | -0.79 (-0.91, -0.68) | +0.10 (+0.05, +0.15) | harms |
| t12 | tax 12% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.06 (+0.02, +0.10) | harms |
| t16 | tax 16% | +0.54 (+0.47, +0.61) | +0.48 (+0.43, +0.54) | +0.02 (-0.00, +0.04) | harms |
| t20 | tax 20% | +1.09 (+0.97, +1.21) | +0.94 (+0.86, +1.03) | -0.04 (-0.07, -0.02) | harms |
| t25 | tax 25% | +1.64 (+1.46, +1.81) | +1.50 (+1.40, +1.62) | -0.14 (-0.18, -0.09) | harms |
| t30 | tax 30% | +2.07 (+1.86, +2.28) | +1.95 (+1.80, +2.11) | -0.21 (-0.29, -0.12) | harms |
| t40 | tax 40% | +2.57 (+2.29, +2.86) | +2.77 (+2.58, +2.99) | -0.25 (-0.40, -0.08) | harms |
| asis.t0 | tax 0%, today's rule | -1.96 (-2.10, -1.82) | -1.77 (-1.87, -1.66) | +0.09 (+0.02, +0.16) | harms |
| asis.t4 | tax 4%, today's rule | -1.25 (-1.36, -1.14) | -1.16 (-1.25, -1.08) | +0.11 (+0.05, +0.17) | harms |
| asis.t8 | tax 8%, today's rule | -0.58 (-0.65, -0.52) | -0.58 (-0.64, -0.52) | +0.10 (+0.05, +0.15) | harms |
| asis.t12 | tax 12%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.06 (+0.02, +0.10) | harms |
| asis.t16 | tax 16%, today's rule | +0.56 (+0.50, +0.63) | +0.50 (+0.45, +0.56) | +0.02 (+0.00, +0.04) | harms |
| asis.t20 | tax 20%, today's rule | +1.17 (+1.05, +1.29) | +1.00 (+0.93, +1.08) | -0.04 (-0.06, -0.02) | harms |
| asis.t25 | tax 25%, today's rule | +1.80 (+1.63, +1.97) | +1.60 (+1.49, +1.72) | -0.13 (-0.17, -0.08) | harms |
| asis.t30 | tax 30%, today's rule | +2.29 (+2.08, +2.49) | +2.10 (+1.95, +2.25) | -0.19 (-0.27, -0.10) | harms |
| asis.t40 | tax 40%, today's rule | +2.92 (+2.65, +3.22) | +2.96 (+2.77, +3.18) | -0.22 (-0.38, -0.05) | harms |
| pr0c75 | progression 0 pts, cap 75% | -0.60 (-0.75, -0.46) | -0.40 (-0.52, -0.30) | +0.00 (-0.01, +0.02) | does not move |
| pr8c75 | progression 8 pts, cap 75% | +0.40 (+0.31, +0.50) | +0.22 (+0.16, +0.31) | +0.00 (-0.02, +0.02) | harms |
| pr0c50 | progression 0 pts, cap 50% | -0.60 (-0.75, -0.46) | -0.40 (-0.52, -0.30) | +0.00 (-0.01, +0.02) | does not move |
| pr4c50 | progression 4 pts, cap 50% | -0.01 (-0.02, -0.00) | -0.01 (-0.01, -0.00) | +0.00 (+0.00, +0.00) | does not move |
| pr8c50 | progression 8 pts, cap 50% | +0.31 (+0.24, +0.39) | +0.16 (+0.09, +0.23) | -0.01 (-0.02, +0.01) | harms |
| bt0 | business tax 0% | -1.52 (-1.66, -1.38) | -1.40 (-1.49, -1.30) | +0.11 (+0.05, +0.18) | harms |
| bt25 | business tax 25% | +1.42 (+1.25, +1.57) | +1.30 (+1.18, +1.41) | -0.14 (-0.18, -0.09) | harms |
| bt50 | business tax 50% | +2.56 (+2.26, +2.88) | +3.03 (+2.81, +3.27) | -0.33 (-0.53, -0.10) | harms |
| bt75 | business tax 75% | +2.36 (+1.96, +2.78) | +4.79 (+4.42, +5.21) | -1.06 (-1.39, -0.74) | harms |
| kp10 | Source keeps 10% of project sales | -0.09 (-0.11, -0.08) | -0.06 (-0.08, -0.04) | -0.01 (-0.02, -0.01) | works |
| kp25 | Source keeps 25% of project sales | -0.25 (-0.29, -0.21) | -0.13 (-0.17, -0.10) | -0.03 (-0.04, -0.02) | works |
| kp50 | Source keeps 50% of project sales | -0.45 (-0.51, -0.41) | -0.26 (-0.30, -0.23) | -0.05 (-0.06, -0.04) | works |
| ex50 | 50% of expired BU recycled | +0.50 (+0.40, +0.58) | +0.34 (+0.27, +0.41) | +0.00 (-0.00, +0.00) | harms |
| ex0 | 0% of expired BU recycled | +0.91 (+0.78, +1.03) | +0.61 (+0.52, +0.70) | +0.00 (+0.00, +0.01) | harms |
| fprog | outside finance: progressive income tax | +33.00 (+32.13, +33.87) | +23.65 (+22.93, +24.35) | +19.95 (+19.41, +20.49) | harms |
| fland | outside finance: land-value tax | -3.02 (-3.98, -2.10) | +0.34 (-0.24, +0.88) | -1.11 (-1.52, -0.68) | does not move |
| fflat | outside finance: flat wage contribution | +25.90 (+25.08, +26.75) | +21.46 (+20.72, +22.17) | +6.73 (+6.35, +7.09) | harms |
| br1 | business rate 1x | +2.34 (+1.94, +2.78) | +4.03 (+3.74, +4.33) | -1.81 (-2.07, -1.56) | harms |
| br15 | business rate 1.5x | +2.52 (+2.18, +2.87) | +3.50 (+3.27, +3.73) | -1.31 (-1.52, -1.10) | harms |
| br2 | business rate 2x | +2.51 (+2.23, +2.79) | +2.70 (+2.53, +2.89) | -0.74 (-0.87, -0.61) | harms |
| bu60 | 60% of the BU | +0.43 (+0.03, +0.84) | +2.14 (+1.88, +2.41) | -1.70 (-1.90, -1.51) | harms |
| bu80 | 80% of the BU | +1.47 (+1.19, +1.75) | +1.72 (+1.54, +1.89) | -0.67 (-0.76, -0.57) | harms |
| mm3 | top multiplier 3 | +0.77 (+0.65, +0.89) | +0.81 (+0.71, +0.90) | +0.02 (-0.01, +0.04) | harms |
| mm6 | top multiplier 6 | +0.29 (+0.21, +0.36) | +0.31 (+0.26, +0.36) | +0.00 (+0.00, +0.00) | harms |
| mm9 | top multiplier 9 | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -0.00 (-0.03, +0.02) | does not move |
| oc25 | octave capacity 25% | +0.24 (+0.17, +0.31) | +0.12 (+0.05, +0.19) | +0.04 (+0.02, +0.05) | harms |
| oc50 | octave capacity 50% | +0.19 (+0.14, +0.23) | +0.11 (+0.06, +0.16) | +0.01 (+0.01, +0.02) | harms |
| oc100 | octave capacity 100% | +0.13 (+0.10, +0.15) | +0.06 (+0.04, +0.07) | +0.00 (+0.00, +0.00) | harms |
| no2 | 2 octaves | -0.19 (-0.27, -0.10) | -0.02 (-0.10, +0.07) | +0.05 (+0.02, +0.07) | harms |
| no4 | 4 octaves | -0.03 (-0.09, +0.04) | +0.01 (-0.05, +0.07) | +0.00 (+0.00, +0.00) | does not move |
| no6 | 6 octaves | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -0.03 (-0.05, -0.02) | does not move |
| phi0 | Phi tier off | +0.04 (-0.01, +0.07) | +0.04 (+0.02, +0.06) | -0.00 (-0.02, +0.01) | harms |
| ph5 | phase-in over 5 years | -0.41 (-0.52, -0.31) | -0.11 (-0.20, -0.01) | -0.77 (-0.83, -0.71) | works |
| ph10 | phase-in over 10 years | -0.51 (-0.72, -0.31) | +0.28 (+0.12, +0.44) | -1.44 (-1.54, -1.32) | harms |
| cap2 | issuance cap 2% | +4.41 (+3.86, +5.01) | +6.18 (+5.70, +6.68) | -0.84 (-1.10, -0.57) | harms |
| cap4 | issuance cap 4% | +4.41 (+3.86, +5.01) | +6.18 (+5.70, +6.68) | -0.84 (-1.10, -0.57) | harms |
| cap8 | issuance cap 8% | +4.41 (+3.86, +5.01) | +6.18 (+5.70, +6.68) | -0.84 (-1.10, -0.57) | harms |
| ixs | indexation: surge protocol (5%) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ixy | indexation: every year, price level | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ixn | indexation: every year, basic needs | -1.22 (-1.40, -1.05) | -1.33 (-1.49, -1.17) | +0.03 (+0.01, +0.05) | harms |
| sva | protected account, all savings | +26.56 (+25.74, +27.43) | +17.25 (+16.60, +17.93) | +15.76 (+15.28, +16.23) | harms |
| svc | protected account, first $10,000 | +4.33 (+4.14, +4.52) | +3.32 (+3.16, +3.49) | +1.90 (+1.83, +1.97) | harms |
| rcap | rent cap for BU tenants | -0.24 (-0.29, -0.21) | -0.24 (-0.28, -0.19) | -0.01 (-0.01, -0.00) | works |
| hc | rent risk ($1.41 a BU dollar) | +6.59 (+6.33, +6.84) | +4.91 (+4.69, +5.11) | +2.15 (+2.08, +2.22) | harms |
| hcrc | rent risk and rent cap | +6.64 (+6.31, +6.97) | +4.19 (+3.95, +4.43) | +2.38 (+2.29, +2.47) | harms |

### programme inflation, points a year: release row, wages 90% (lever effect, seed mean and 95% interval)

| Row | What it sets | Reference | Adverse | Stress | Verdict |
|---|---|---|---|---|---|
| asis | today's joining rule | +0.26 (+0.21, +0.32) | +0.26 (+0.20, +0.32) | +0.00 (+0.00, +0.00) | harms |
| t0 | tax 0% | +2.80 (+2.72, +2.88) | +2.51 (+2.41, +2.61) | +5.08 (+4.99, +5.17) | harms |
| t4 | tax 4% | +1.92 (+1.86, +1.99) | +1.71 (+1.63, +1.78) | +4.02 (+3.95, +4.08) | harms |
| t8 | tax 8% | +0.99 (+0.95, +1.03) | +0.87 (+0.82, +0.92) | +2.92 (+2.87, +2.97) | harms |
| t12 | tax 12% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +1.78 (+1.75, +1.81) | harms |
| t16 | tax 16% | -1.04 (-1.07, -1.01) | -0.91 (-0.94, -0.87) | +0.60 (+0.59, +0.61) | harms |
| t20 | tax 20% | -2.07 (-2.12, -2.03) | -1.90 (-1.95, -1.85) | -0.61 (-0.62, -0.60) | works |
| t25 | tax 25% | -3.37 (-3.43, -3.31) | -3.44 (-3.52, -3.36) | -2.15 (-2.19, -2.11) | works |
| t30 | tax 30% | -4.93 (-5.01, -4.84) | -5.53 (-5.63, -5.43) | -3.72 (-3.79, -3.66) | works |
| t40 | tax 40% | -9.16 (-9.27, -9.05) | -10.15 (-10.29, -10.02) | -6.89 (-7.01, -6.77) | works |
| asis.t0 | tax 0%, today's rule | +2.38 (+2.34, +2.42) | +2.05 (+2.00, +2.10) | +5.01 (+4.92, +5.10) | harms |
| asis.t4 | tax 4%, today's rule | +1.66 (+1.63, +1.69) | +1.43 (+1.39, +1.46) | +3.97 (+3.90, +4.04) | harms |
| asis.t8 | tax 8%, today's rule | +0.87 (+0.85, +0.88) | +0.74 (+0.72, +0.76) | +2.89 (+2.84, +2.94) | harms |
| asis.t12 | tax 12%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +1.76 (+1.73, +1.79) | harms |
| asis.t16 | tax 16%, today's rule | -0.93 (-0.95, -0.92) | -0.83 (-0.85, -0.81) | +0.59 (+0.58, +0.61) | harms |
| asis.t20 | tax 20%, today's rule | -1.91 (-1.94, -1.88) | -1.80 (-1.83, -1.76) | -0.60 (-0.62, -0.59) | works |
| asis.t25 | tax 25%, today's rule | -3.21 (-3.26, -3.17) | -3.37 (-3.43, -3.31) | -2.13 (-2.18, -2.09) | works |
| asis.t30 | tax 30%, today's rule | -4.84 (-4.91, -4.78) | -5.47 (-5.55, -5.39) | -3.69 (-3.76, -3.62) | works |
| asis.t40 | tax 40%, today's rule | -9.13 (-9.23, -9.05) | -10.13 (-10.25, -10.00) | -6.83 (-6.95, -6.71) | works |
| pr0c75 | progression 0 pts, cap 75% | +0.05 (-0.00, +0.10) | -0.03 (-0.09, +0.03) | +0.16 (+0.14, +0.17) | harms |
| pr8c75 | progression 8 pts, cap 75% | -0.40 (-0.51, -0.30) | -0.21 (-0.29, -0.13) | -0.16 (-0.18, -0.14) | works |
| pr0c50 | progression 0 pts, cap 50% | +0.05 (-0.00, +0.10) | -0.03 (-0.09, +0.03) | +0.16 (+0.14, +0.17) | harms |
| pr4c50 | progression 4 pts, cap 50% | -0.01 (-0.01, -0.00) | -0.01 (-0.01, -0.01) | +0.00 (+0.00, +0.00) | does not move |
| pr8c50 | progression 8 pts, cap 50% | -0.33 (-0.40, -0.24) | -0.17 (-0.24, -0.11) | -0.10 (-0.11, -0.09) | works |
| bt0 | business tax 0% | +2.51 (+2.46, +2.56) | +2.35 (+2.30, +2.40) | +4.72 (+4.62, +4.81) | harms |
| bt25 | business tax 25% | -2.89 (-2.95, -2.84) | -3.08 (-3.17, -2.99) | -1.99 (-2.03, -1.95) | works |
| bt50 | business tax 50% | -12.22 (-12.40, -12.07) | -14.02 (-14.23, -13.83) | -9.24 (-9.41, -9.06) | works |
| bt75 | business tax 75% | -24.32 (-24.63, -24.04) | -27.67 (-28.02, -27.34) | -15.85 (-16.15, -15.56) | works |
| kp10 | Source keeps 10% of project sales | -0.32 (-0.32, -0.31) | -0.30 (-0.31, -0.30) | -0.02 (-0.02, -0.02) | works |
| kp25 | Source keeps 25% of project sales | -0.80 (-0.81, -0.78) | -0.76 (-0.78, -0.75) | -0.04 (-0.04, -0.04) | works |
| kp50 | Source keeps 50% of project sales | -1.61 (-1.64, -1.58) | -1.54 (-1.58, -1.51) | -0.08 (-0.09, -0.08) | works |
| ex50 | 50% of expired BU recycled | +1.10 (+1.06, +1.14) | +1.23 (+1.19, +1.28) | +0.00 (+0.00, +0.00) | harms |
| ex0 | 0% of expired BU recycled | +2.24 (+2.17, +2.30) | +2.41 (+2.33, +2.49) | +0.00 (+0.00, +0.01) | harms |
| fprog | outside finance: progressive income tax | -7.02 (-7.67, -6.38) | +2.56 (+1.47, +3.68) | -29.79 (-30.41, -29.19) | harms |
| fland | outside finance: land-value tax | -62.51 (-63.16, -61.90) | -65.06 (-65.67, -64.39) | -32.46 (-33.16, -31.76) | works |
| fflat | outside finance: flat wage contribution | -68.50 (-69.32, -67.75) | -86.34 (-87.45, -85.29) | -33.89 (-34.64, -33.12) | works |
| br1 | business rate 1x | -24.57 (-24.89, -24.29) | -29.09 (-29.42, -28.80) | -16.13 (-16.44, -15.82) | works |
| br15 | business rate 1.5x | -18.18 (-18.42, -17.97) | -21.24 (-21.50, -21.02) | -13.27 (-13.52, -13.01) | works |
| br2 | business rate 2x | -10.40 (-10.56, -10.27) | -12.01 (-12.19, -11.86) | -8.64 (-8.81, -8.47) | works |
| bu60 | 60% of the BU | -25.50 (-25.88, -25.16) | -33.06 (-33.58, -32.58) | -13.95 (-14.27, -13.64) | works |
| bu80 | 80% of the BU | -11.06 (-11.26, -10.87) | -14.78 (-15.07, -14.51) | -7.03 (-7.19, -6.87) | works |
| mm3 | top multiplier 3 | +0.32 (+0.27, +0.38) | +0.86 (+0.81, +0.93) | -0.56 (-0.58, -0.54) | harms |
| mm6 | top multiplier 6 | +0.09 (+0.07, +0.12) | +0.31 (+0.28, +0.34) | +0.00 (+0.00, +0.00) | harms |
| mm9 | top multiplier 9 | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.40 (+0.39, +0.42) | harms |
| oc25 | octave capacity 25% | +0.70 (+0.67, +0.73) | +1.06 (+1.03, +1.09) | +0.06 (+0.04, +0.07) | harms |
| oc50 | octave capacity 50% | +0.43 (+0.41, +0.45) | +0.65 (+0.63, +0.67) | +0.03 (+0.02, +0.03) | harms |
| oc100 | octave capacity 100% | +0.18 (+0.17, +0.20) | +0.26 (+0.24, +0.27) | +0.00 (+0.00, +0.00) | harms |
| no2 | 2 octaves | +0.36 (+0.33, +0.40) | +0.80 (+0.76, +0.85) | +0.11 (+0.10, +0.12) | harms |
| no4 | 4 octaves | +0.22 (+0.20, +0.24) | +0.47 (+0.45, +0.50) | +0.00 (+0.00, +0.00) | harms |
| no6 | 6 octaves | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -0.09 (-0.10, -0.08) | does not move |
| phi0 | Phi tier off | +0.09 (+0.08, +0.10) | +0.11 (+0.10, +0.12) | -0.08 (-0.10, -0.07) | harms |
| ph5 | phase-in over 5 years | -3.14 (-3.19, -3.10) | -3.80 (-3.86, -3.74) | -2.06 (-2.11, -2.01) | works |
| ph10 | phase-in over 10 years | -7.20 (-7.28, -7.11) | -8.71 (-8.83, -8.59) | -4.82 (-4.93, -4.71) | works |
| cap2 | issuance cap 2% | -26.24 (-26.45, -26.04) | -29.01 (-29.22, -28.83) | -16.34 (-16.65, -16.02) | works |
| cap4 | issuance cap 4% | -26.24 (-26.45, -26.04) | -29.01 (-29.22, -28.83) | -16.34 (-16.65, -16.02) | works |
| cap8 | issuance cap 8% | -26.24 (-26.45, -26.04) | -29.01 (-29.22, -28.83) | -16.34 (-16.65, -16.02) | works |
| ixs | indexation: surge protocol (5%) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ixy | indexation: every year, price level | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ixn | indexation: every year, basic needs | +1.19 (+1.09, +1.29) | +1.50 (+1.41, +1.59) | +0.19 (+0.17, +0.21) | harms |
| sva | protected account, all savings | +2663.51 (+2592.47, +2740.20) | +3528.40 (+3432.48, +3630.50) | +2844.51 (+2763.12, +2930.59) | harms |
| svc | protected account, first $10,000 | +21.53 (+21.09, +22.01) | +34.46 (+33.77, +35.16) | +9.05 (+8.81, +9.29) | harms |
| rcap | rent cap for BU tenants | -0.21 (-0.22, -0.20) | -0.24 (-0.25, -0.23) | +0.00 (+0.00, +0.00) | harms |
| hc | rent risk ($1.41 a BU dollar) | +2.01 (+1.92, +2.09) | +1.92 (+1.82, +2.02) | -0.03 (-0.04, -0.03) | harms |
| hcrc | rent risk and rent cap | -1.53 (-1.58, -1.48) | -1.60 (-1.66, -1.54) | -0.06 (-0.07, -0.06) | works |

### participation, mean of years 1-19, %: release row, wages 90% (lever effect, seed mean and 95% interval)

| Row | What it sets | Reference | Adverse | Stress | Verdict |
|---|---|---|---|---|---|
| asis | today's joining rule | +0.27 (+0.21, +0.33) | +0.20 (+0.15, +0.25) | +0.00 (+0.00, +0.00) | does not move |
| t0 | tax 0% | +0.58 (+0.47, +0.69) | +0.49 (+0.39, +0.58) | +0.09 (+0.06, +0.11) | works |
| t4 | tax 4% | +0.36 (+0.28, +0.44) | +0.31 (+0.24, +0.39) | +0.06 (+0.04, +0.08) | works |
| t8 | tax 8% | +0.17 (+0.11, +0.23) | +0.14 (+0.09, +0.19) | +0.04 (+0.02, +0.05) | works |
| t12 | tax 12% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.02 (+0.01, +0.03) | does not move |
| t16 | tax 16% | -0.15 (-0.19, -0.10) | -0.08 (-0.11, -0.05) | +0.01 (+0.00, +0.01) | harms |
| t20 | tax 20% | -0.23 (-0.29, -0.17) | -0.11 (-0.15, -0.07) | -0.01 (-0.01, -0.00) | harms |
| t25 | tax 25% | -0.24 (-0.30, -0.17) | -0.10 (-0.16, -0.05) | -0.03 (-0.03, -0.02) | harms |
| t30 | tax 30% | -0.17 (-0.24, -0.10) | -0.11 (-0.17, -0.06) | -0.05 (-0.06, -0.04) | harms |
| t40 | tax 40% | -0.11 (-0.19, -0.03) | -0.08 (-0.14, -0.03) | -0.10 (-0.11, -0.08) | harms |
| asis.t0 | tax 0%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t4 | tax 4%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t8 | tax 8%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t12 | tax 12%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t16 | tax 16%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t20 | tax 20%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t25 | tax 25%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t30 | tax 30%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t40 | tax 40%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| pr0c75 | progression 0 pts, cap 75% | +0.26 (+0.20, +0.33) | +0.23 (+0.17, +0.30) | +0.00 (+0.00, +0.01) | works |
| pr8c75 | progression 8 pts, cap 75% | -0.70 (-0.83, -0.58) | -0.44 (-0.52, -0.37) | -0.02 (-0.02, -0.01) | harms |
| pr0c50 | progression 0 pts, cap 50% | +0.26 (+0.20, +0.33) | +0.23 (+0.17, +0.30) | +0.00 (+0.00, +0.01) | works |
| pr4c50 | progression 4 pts, cap 50% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| pr8c50 | progression 8 pts, cap 50% | -0.54 (-0.65, -0.44) | -0.33 (-0.40, -0.26) | -0.01 (-0.02, -0.01) | harms |
| bt0 | business tax 0% | -0.09 (-0.11, -0.07) | -0.08 (-0.09, -0.06) | -0.03 (-0.04, -0.02) | harms |
| bt25 | business tax 25% | +0.13 (+0.09, +0.16) | +0.14 (+0.10, +0.18) | +0.00 (+0.00, +0.00) | does not move |
| bt50 | business tax 50% | +0.27 (+0.21, +0.32) | +0.20 (+0.15, +0.25) | +0.00 (+0.00, +0.00) | does not move |
| bt75 | business tax 75% | +0.27 (+0.21, +0.33) | +0.20 (+0.15, +0.25) | +0.00 (+0.00, +0.00) | does not move |
| kp10 | Source keeps 10% of project sales | -0.00 (-0.00, +0.00) | -0.00 (-0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| kp25 | Source keeps 25% of project sales | -0.00 (-0.00, -0.00) | -0.00 (-0.00, +0.00) | +0.00 (+0.00, +0.00) | harms |
| kp50 | Source keeps 50% of project sales | -0.00 (-0.01, -0.00) | -0.00 (-0.01, -0.00) | +0.00 (+0.00, +0.00) | harms |
| ex50 | 50% of expired BU recycled | +0.11 (+0.07, +0.14) | +0.10 (+0.08, +0.13) | +0.00 (+0.00, +0.00) | does not move |
| ex0 | 0% of expired BU recycled | +0.27 (+0.21, +0.33) | +0.20 (+0.15, +0.25) | +0.00 (+0.00, +0.00) | does not move |
| fprog | outside finance: progressive income tax | -0.03 (-0.04, -0.03) | +0.00 (-0.01, +0.01) | -2.81 (-3.40, -2.28) | harms |
| fland | outside finance: land-value tax | -3.20 (-3.49, -2.92) | -0.40 (-0.47, -0.34) | -6.07 (-6.40, -5.73) | harms |
| fflat | outside finance: flat wage contribution | -0.11 (-0.20, -0.02) | -13.10 (-13.52, -12.65) | -7.73 (-8.09, -7.37) | harms |
| br1 | business rate 1x | +0.27 (+0.21, +0.33) | +0.20 (+0.15, +0.25) | +0.00 (+0.00, +0.00) | does not move |
| br15 | business rate 1.5x | +0.27 (+0.21, +0.33) | +0.20 (+0.15, +0.25) | +0.00 (+0.00, +0.00) | does not move |
| br2 | business rate 2x | +0.26 (+0.21, +0.31) | +0.20 (+0.15, +0.24) | +0.00 (+0.00, +0.00) | does not move |
| bu60 | 60% of the BU | +0.27 (+0.21, +0.33) | +0.20 (+0.15, +0.25) | +0.00 (+0.00, +0.00) | does not move |
| bu80 | 80% of the BU | +0.25 (+0.20, +0.31) | +0.19 (+0.15, +0.24) | +0.00 (+0.00, +0.00) | does not move |
| mm3 | top multiplier 3 | +0.11 (+0.08, +0.15) | +0.11 (+0.08, +0.14) | +0.00 (+0.00, +0.00) | does not move |
| mm6 | top multiplier 6 | +0.04 (+0.02, +0.06) | +0.04 (+0.03, +0.05) | +0.00 (+0.00, +0.00) | does not move |
| mm9 | top multiplier 9 | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| oc25 | octave capacity 25% | -0.02 (-0.03, -0.01) | -0.01 (-0.02, -0.01) | +0.00 (+0.00, +0.00) | harms |
| oc50 | octave capacity 50% | -0.01 (-0.01, -0.00) | -0.00 (-0.01, -0.00) | +0.00 (+0.00, +0.00) | harms |
| oc100 | octave capacity 100% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| no2 | 2 octaves | -0.05 (-0.07, -0.04) | -0.04 (-0.05, -0.03) | +0.00 (-0.00, +0.00) | harms |
| no4 | 4 octaves | -0.03 (-0.04, -0.02) | -0.02 (-0.03, -0.02) | +0.00 (+0.00, +0.00) | harms |
| no6 | 6 octaves | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| phi0 | Phi tier off | +0.01 (+0.00, +0.02) | +0.01 (+0.00, +0.01) | +0.00 (+0.00, +0.00) | does not move |
| ph5 | phase-in over 5 years | +0.03 (+0.02, +0.04) | +0.02 (+0.01, +0.03) | +0.00 (+0.00, +0.00) | does not move |
| ph10 | phase-in over 10 years | +0.10 (+0.08, +0.12) | +0.08 (+0.07, +0.10) | +0.00 (+0.00, +0.00) | does not move |
| cap2 | issuance cap 2% | +0.26 (+0.20, +0.31) | +0.19 (+0.14, +0.23) | +0.00 (+0.00, +0.00) | does not move |
| cap4 | issuance cap 4% | +0.26 (+0.20, +0.31) | +0.19 (+0.14, +0.23) | +0.00 (+0.00, +0.00) | does not move |
| cap8 | issuance cap 8% | +0.26 (+0.20, +0.31) | +0.19 (+0.14, +0.23) | +0.00 (+0.00, +0.00) | does not move |
| ixs | indexation: surge protocol (5%) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ixy | indexation: every year, price level | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ixn | indexation: every year, basic needs | +0.76 (+0.64, +0.89) | +0.84 (+0.75, +0.93) | +0.12 (+0.09, +0.14) | works |
| sva | protected account, all savings | +0.25 (+0.20, +0.31) | +0.19 (+0.14, +0.23) | +0.00 (+0.00, +0.00) | does not move |
| svc | protected account, first $10,000 | +0.06 (+0.04, +0.09) | +0.10 (+0.07, +0.13) | +0.00 (+0.00, +0.00) | does not move |
| rcap | rent cap for BU tenants | -0.01 (-0.02, -0.01) | -0.01 (-0.01, -0.01) | +0.00 (+0.00, +0.00) | harms |
| hc | rent risk ($1.41 a BU dollar) | +0.15 (+0.10, +0.19) | +0.11 (+0.08, +0.15) | +0.00 (+0.00, +0.00) | does not move |
| hcrc | rent risk and rent cap | -0.02 (-0.03, -0.01) | -0.01 (-0.02, -0.01) | +0.00 (+0.00, +0.00) | harms |

### basket poverty, % of adult-years: C2.2 design, wages 100% (lever effect, seed mean and 95% interval)

| Row | What it sets | Reference | Adverse | Stress | Verdict |
|---|---|---|---|---|---|
| asis | today's joining rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| t0 | tax 0% | -0.30 (-0.32, -0.28) | -0.59 (-0.64, -0.55) | -1.11 (-1.18, -1.04) | works |
| t4 | tax 4% | -0.24 (-0.26, -0.22) | -0.45 (-0.49, -0.42) | -1.11 (-1.17, -1.05) | works |
| t8 | tax 8% | -0.14 (-0.15, -0.13) | -0.25 (-0.28, -0.23) | -0.91 (-0.97, -0.86) | works |
| t12 | tax 12% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -0.60 (-0.65, -0.56) | does not move |
| t16 | tax 16% | +0.18 (+0.16, +0.20) | +0.30 (+0.28, +0.33) | -0.22 (-0.24, -0.20) | harms |
| t20 | tax 20% | +0.38 (+0.35, +0.41) | +0.65 (+0.60, +0.69) | +0.23 (+0.22, +0.25) | harms |
| t25 | tax 25% | +0.67 (+0.62, +0.72) | +1.20 (+1.12, +1.27) | +0.90 (+0.85, +0.96) | harms |
| t30 | tax 30% | +1.01 (+0.95, +1.08) | +1.83 (+1.73, +1.95) | +1.65 (+1.56, +1.75) | harms |
| t40 | tax 40% | +1.93 (+1.84, +2.03) | +3.48 (+3.30, +3.68) | +3.65 (+3.46, +3.85) | harms |
| asis.t0 | tax 0%, today's rule | -0.30 (-0.32, -0.28) | -0.59 (-0.64, -0.55) | -1.11 (-1.18, -1.04) | works |
| asis.t4 | tax 4%, today's rule | -0.24 (-0.26, -0.22) | -0.45 (-0.49, -0.42) | -1.11 (-1.17, -1.05) | works |
| asis.t8 | tax 8%, today's rule | -0.14 (-0.15, -0.13) | -0.25 (-0.28, -0.23) | -0.91 (-0.97, -0.86) | works |
| asis.t12 | tax 12%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -0.60 (-0.65, -0.56) | does not move |
| asis.t16 | tax 16%, today's rule | +0.18 (+0.16, +0.20) | +0.30 (+0.28, +0.33) | -0.22 (-0.24, -0.20) | harms |
| asis.t20 | tax 20%, today's rule | +0.38 (+0.35, +0.41) | +0.65 (+0.60, +0.69) | +0.23 (+0.22, +0.25) | harms |
| asis.t25 | tax 25%, today's rule | +0.67 (+0.62, +0.72) | +1.20 (+1.12, +1.27) | +0.90 (+0.85, +0.96) | harms |
| asis.t30 | tax 30%, today's rule | +1.01 (+0.95, +1.08) | +1.83 (+1.73, +1.95) | +1.65 (+1.56, +1.75) | harms |
| asis.t40 | tax 40%, today's rule | +1.93 (+1.84, +2.03) | +3.48 (+3.30, +3.68) | +3.65 (+3.46, +3.85) | harms |
| pr0c75 | progression 0 pts, cap 75% | -0.10 (-0.11, -0.09) | -0.20 (-0.22, -0.18) | -0.24 (-0.26, -0.22) | works |
| pr8c75 | progression 8 pts, cap 75% | +0.12 (+0.10, +0.13) | +0.26 (+0.24, +0.29) | +0.29 (+0.26, +0.32) | harms |
| pr0c50 | progression 0 pts, cap 50% | -0.10 (-0.11, -0.09) | -0.20 (-0.22, -0.18) | -0.24 (-0.26, -0.22) | works |
| pr4c50 | progression 4 pts, cap 50% | -0.00 (-0.00, +0.00) | -0.00 (-0.00, -0.00) | +0.00 (+0.00, +0.00) | does not move |
| pr8c50 | progression 8 pts, cap 50% | +0.11 (+0.09, +0.12) | +0.23 (+0.21, +0.25) | +0.23 (+0.21, +0.25) | harms |
| bt0 | business tax 0% | -0.21 (-0.23, -0.19) | -0.40 (-0.44, -0.37) | -0.82 (-0.88, -0.76) | works |
| bt25 | business tax 25% | +0.48 (+0.45, +0.51) | +0.80 (+0.75, +0.86) | +0.64 (+0.60, +0.68) | harms |
| bt50 | business tax 50% | +2.33 (+2.21, +2.45) | +4.00 (+3.80, +4.22) | +4.94 (+4.70, +5.19) | harms |
| bt75 | business tax 75% | +6.14 (+5.86, +6.43) | +10.99 (+10.60, +11.38) | +12.38 (+12.00, +12.76) | harms |
| kp10 | Source keeps 10% of project sales | -0.02 (-0.03, -0.02) | -0.06 (-0.07, -0.05) | -0.09 (-0.10, -0.08) | works |
| kp25 | Source keeps 25% of project sales | -0.06 (-0.07, -0.05) | -0.14 (-0.16, -0.13) | -0.21 (-0.23, -0.19) | works |
| kp50 | Source keeps 50% of project sales | -0.10 (-0.11, -0.09) | -0.27 (-0.30, -0.25) | -0.40 (-0.44, -0.37) | works |
| ex50 | 50% of expired BU recycled | +0.81 (+0.75, +0.87) | +1.66 (+1.55, +1.77) | +1.83 (+1.72, +1.95) | harms |
| ex0 | 0% of expired BU recycled | +2.79 (+2.64, +2.95) | +5.12 (+4.90, +5.36) | +4.79 (+4.58, +5.02) | harms |
| fprog | outside finance: progressive income tax | +4.43 (+4.30, +4.56) | +7.49 (+7.12, +7.86) | +11.47 (+10.83, +12.08) | harms |
| fland | outside finance: land-value tax | +6.28 (+6.16, +6.40) | +9.49 (+9.18, +9.80) | +10.75 (+10.41, +11.09) | harms |
| fflat | outside finance: flat wage contribution | +7.00 (+6.84, +7.16) | +6.69 (+6.52, +6.86) | +9.56 (+9.29, +9.82) | harms |
| br1 | business rate 1x | +6.25 (+5.97, +6.54) | +10.73 (+10.39, +11.08) | +11.89 (+11.54, +12.23) | harms |
| br15 | business rate 1.5x | +3.83 (+3.64, +4.04) | +6.57 (+6.29, +6.86) | +8.25 (+7.95, +8.56) | harms |
| br2 | business rate 2x | +1.92 (+1.83, +2.01) | +3.30 (+3.13, +3.49) | +4.20 (+3.99, +4.42) | harms |
| bu60 | 60% of the BU | +7.19 (+6.89, +7.49) | +11.95 (+11.56, +12.36) | +12.87 (+12.47, +13.27) | harms |
| bu80 | 80% of the BU | +2.41 (+2.30, +2.54) | +4.14 (+3.94, +4.37) | +4.86 (+4.62, +5.11) | harms |
| mm3 | top multiplier 3 | +0.74 (+0.69, +0.80) | +1.65 (+1.54, +1.77) | +1.24 (+1.16, +1.33) | harms |
| mm6 | top multiplier 6 | +0.28 (+0.25, +0.31) | +0.54 (+0.49, +0.58) | +0.00 (+0.00, +0.00) | harms |
| mm9 | top multiplier 9 | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -0.60 (-0.65, -0.55) | does not move |
| oc25 | octave capacity 25% | +0.55 (+0.50, +0.60) | +2.17 (+2.07, +2.28) | +3.07 (+2.94, +3.23) | harms |
| oc50 | octave capacity 50% | +0.33 (+0.30, +0.37) | +1.71 (+1.62, +1.80) | +2.71 (+2.59, +2.83) | harms |
| oc100 | octave capacity 100% | +0.16 (+0.14, +0.18) | +1.23 (+1.17, +1.31) | +2.31 (+2.21, +2.42) | harms |
| no2 | 2 octaves | -0.40 (-0.43, -0.37) | -0.51 (-0.54, -0.47) | -0.25 (-0.28, -0.23) | works |
| no4 | 4 octaves | -0.21 (-0.23, -0.19) | -0.28 (-0.31, -0.26) | +0.00 (+0.00, +0.00) | does not move |
| no6 | 6 octaves | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.30 (+0.28, +0.33) | harms |
| phi0 | Phi tier off | +0.06 (+0.05, +0.07) | +0.11 (+0.10, +0.12) | +0.33 (+0.31, +0.36) | harms |
| ph5 | phase-in over 5 years | +0.55 (+0.51, +0.58) | +0.62 (+0.59, +0.66) | +0.72 (+0.68, +0.77) | harms |
| ph10 | phase-in over 10 years | +1.41 (+1.34, +1.48) | +1.65 (+1.57, +1.73) | +1.90 (+1.81, +2.00) | harms |
| cap2 | issuance cap 2% | +7.25 (+6.95, +7.54) | +12.70 (+12.34, +13.07) | +12.90 (+12.55, +13.24) | harms |
| cap4 | issuance cap 4% | +7.25 (+6.95, +7.54) | +12.70 (+12.34, +13.07) | +12.90 (+12.55, +13.24) | harms |
| cap8 | issuance cap 8% | +7.25 (+6.95, +7.54) | +12.70 (+12.34, +13.07) | +12.90 (+12.55, +13.24) | harms |
| ixs | indexation: surge protocol (5%) | +0.24 (+0.22, +0.27) | +0.49 (+0.45, +0.53) | +0.64 (+0.60, +0.69) | harms |
| ixy | indexation: every year, price level | +0.24 (+0.22, +0.27) | +0.49 (+0.45, +0.53) | +0.64 (+0.60, +0.69) | harms |
| ixn | indexation: every year, basic needs | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| sva | protected account, all savings | +7.43 (+7.13, +7.74) | +13.24 (+12.86, +13.60) | +13.22 (+12.86, +13.58) | harms |
| svc | protected account, first $10,000 | +0.06 (+0.05, +0.07) | +0.19 (+0.17, +0.21) | +0.36 (+0.34, +0.39) | harms |
| rcap | rent cap for BU tenants | -0.12 (-0.14, -0.11) | -0.25 (-0.28, -0.23) | -0.41 (-0.45, -0.38) | works |
| hc | rent risk ($1.41 a BU dollar) | +2.70 (+2.56, +2.84) | +4.72 (+4.51, +4.96) | +6.70 (+6.45, +6.99) | harms |
| hcrc | rent risk and rent cap | -0.12 (-0.14, -0.11) | -0.25 (-0.28, -0.23) | -0.41 (-0.45, -0.38) | works |

### wealth poverty at year 20, %: C2.2 design, wages 100% (lever effect, seed mean and 95% interval)

| Row | What it sets | Reference | Adverse | Stress | Verdict |
|---|---|---|---|---|---|
| asis | today's joining rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| t0 | tax 0% | -0.44 (-0.54, -0.34) | -4.64 (-4.99, -4.26) | -13.15 (-13.87, -12.46) | works |
| t4 | tax 4% | -0.37 (-0.47, -0.29) | -3.73 (-4.03, -3.44) | -11.77 (-12.44, -11.16) | works |
| t8 | tax 8% | -0.26 (-0.33, -0.20) | -2.27 (-2.46, -2.07) | -8.98 (-9.51, -8.47) | works |
| t12 | tax 12% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -5.52 (-5.94, -5.16) | does not move |
| t16 | tax 16% | +0.31 (+0.24, +0.38) | +3.16 (+2.90, +3.42) | -1.76 (-1.97, -1.56) | harms |
| t20 | tax 20% | +1.06 (+0.90, +1.22) | +6.97 (+6.52, +7.44) | +2.07 (+1.89, +2.25) | harms |
| t25 | tax 25% | +2.37 (+2.13, +2.60) | +12.04 (+11.48, +12.66) | +6.58 (+6.22, +6.98) | harms |
| t30 | tax 30% | +4.08 (+3.78, +4.42) | +17.01 (+16.36, +17.70) | +11.29 (+10.89, +11.74) | harms |
| t40 | tax 40% | +7.78 (+7.38, +8.23) | +25.55 (+24.86, +26.29) | +19.10 (+18.54, +19.65) | harms |
| asis.t0 | tax 0%, today's rule | -0.44 (-0.54, -0.34) | -4.64 (-4.99, -4.26) | -13.15 (-13.87, -12.46) | works |
| asis.t4 | tax 4%, today's rule | -0.37 (-0.47, -0.29) | -3.73 (-4.03, -3.44) | -11.77 (-12.44, -11.16) | works |
| asis.t8 | tax 8%, today's rule | -0.26 (-0.33, -0.20) | -2.27 (-2.46, -2.07) | -8.98 (-9.51, -8.47) | works |
| asis.t12 | tax 12%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -5.52 (-5.94, -5.16) | does not move |
| asis.t16 | tax 16%, today's rule | +0.31 (+0.24, +0.38) | +3.16 (+2.90, +3.42) | -1.76 (-1.97, -1.56) | harms |
| asis.t20 | tax 20%, today's rule | +1.06 (+0.90, +1.22) | +6.97 (+6.52, +7.44) | +2.07 (+1.89, +2.25) | harms |
| asis.t25 | tax 25%, today's rule | +2.37 (+2.13, +2.60) | +12.04 (+11.48, +12.66) | +6.58 (+6.22, +6.98) | harms |
| asis.t30 | tax 30%, today's rule | +4.08 (+3.78, +4.42) | +17.01 (+16.36, +17.70) | +11.29 (+10.89, +11.74) | harms |
| asis.t40 | tax 40%, today's rule | +7.78 (+7.38, +8.23) | +25.55 (+24.86, +26.29) | +19.10 (+18.54, +19.65) | harms |
| pr0c75 | progression 0 pts, cap 75% | -0.28 (-0.37, -0.21) | -2.87 (-3.11, -2.63) | -2.91 (-3.18, -2.65) | works |
| pr8c75 | progression 8 pts, cap 75% | +0.41 (+0.32, +0.50) | +4.20 (+3.86, +4.56) | +4.38 (+4.05, +4.77) | harms |
| pr0c50 | progression 0 pts, cap 50% | -0.28 (-0.37, -0.21) | -2.87 (-3.11, -2.63) | -2.91 (-3.18, -2.65) | works |
| pr4c50 | progression 4 pts, cap 50% | -0.00 (-0.01, +0.00) | -0.06 (-0.09, -0.03) | +0.00 (+0.00, +0.00) | does not move |
| pr8c50 | progression 8 pts, cap 50% | +0.37 (+0.29, +0.45) | +3.63 (+3.34, +3.94) | +3.00 (+2.76, +3.26) | harms |
| bt0 | business tax 0% | -0.30 (-0.39, -0.22) | -3.13 (-3.37, -2.88) | -7.73 (-8.26, -7.22) | works |
| bt25 | business tax 25% | +1.15 (+0.97, +1.33) | +7.29 (+6.86, +7.75) | +4.55 (+4.25, +4.87) | harms |
| bt50 | business tax 50% | +7.67 (+7.28, +8.10) | +24.15 (+23.46, +24.90) | +19.49 (+18.94, +20.06) | harms |
| bt75 | business tax 75% | +14.86 (+14.32, +15.40) | +37.44 (+36.52, +38.38) | +29.70 (+28.97, +30.42) | harms |
| kp10 | Source keeps 10% of project sales | -0.14 (-0.19, -0.10) | -1.52 (-1.68, -1.35) | -1.58 (-1.80, -1.38) | works |
| kp25 | Source keeps 25% of project sales | -0.30 (-0.40, -0.23) | -3.38 (-3.65, -3.10) | -4.60 (-4.93, -4.29) | works |
| kp50 | Source keeps 50% of project sales | -0.43 (-0.53, -0.34) | -5.23 (-5.66, -4.80) | -10.18 (-10.72, -9.66) | works |
| ex50 | 50% of expired BU recycled | +5.20 (+4.88, +5.56) | +18.66 (+18.02, +19.31) | +14.76 (+14.30, +15.24) | harms |
| ex0 | 0% of expired BU recycled | +15.09 (+14.54, +15.64) | +36.74 (+35.92, +37.64) | +27.13 (+26.48, +27.82) | harms |
| fprog | outside finance: progressive income tax | +11.10 (+10.15, +12.10) | +55.91 (+54.60, +57.19) | +57.95 (+56.76, +59.06) | harms |
| fland | outside finance: land-value tax | -0.47 (-0.59, -0.36) | -5.77 (-6.24, -5.30) | -17.66 (-18.54, -16.84) | works |
| fflat | outside finance: flat wage contribution | +1.45 (+1.30, +1.61) | -4.16 (-4.60, -3.72) | -13.74 (-14.64, -12.89) | harms |
| br1 | business rate 1x | +15.01 (+14.47, +15.55) | +36.33 (+35.56, +37.16) | +28.50 (+27.88, +29.08) | harms |
| br15 | business rate 1.5x | +10.99 (+10.59, +11.40) | +30.34 (+29.61, +31.14) | +24.22 (+23.60, +24.83) | harms |
| br2 | business rate 2x | +6.44 (+6.08, +6.82) | +21.83 (+21.12, +22.54) | +18.02 (+17.52, +18.51) | harms |
| bu60 | 60% of the BU | +15.47 (+14.94, +16.02) | +35.06 (+34.29, +35.87) | +26.38 (+25.76, +27.02) | harms |
| bu80 | 80% of the BU | +7.85 (+7.48, +8.26) | +23.79 (+23.17, +24.45) | +19.37 (+18.78, +19.94) | harms |
| mm3 | top multiplier 3 | +4.58 (+4.27, +4.94) | +18.24 (+17.64, +18.87) | +10.30 (+9.92, +10.68) | harms |
| mm6 | top multiplier 6 | +1.09 (+0.92, +1.28) | +7.55 (+7.10, +8.02) | +0.00 (+0.00, +0.00) | harms |
| mm9 | top multiplier 9 | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -7.26 (-7.72, -6.82) | does not move |
| oc25 | octave capacity 25% | +9.78 (+9.28, +10.31) | +33.39 (+32.52, +34.35) | +26.27 (+25.60, +26.96) | harms |
| oc50 | octave capacity 50% | +6.74 (+6.26, +7.27) | +30.62 (+29.76, +31.58) | +25.75 (+25.08, +26.42) | harms |
| oc100 | octave capacity 100% | +2.86 (+2.44, +3.31) | +26.34 (+25.46, +27.32) | +24.88 (+24.23, +25.55) | harms |
| no2 | 2 octaves | -0.15 (-0.19, -0.11) | -0.55 (-0.66, -0.43) | -0.13 (-0.19, -0.08) | works |
| no4 | 4 octaves | -0.12 (-0.16, -0.08) | -0.42 (-0.51, -0.32) | +0.00 (+0.00, +0.00) | does not move |
| no6 | 6 octaves | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.34 (+0.25, +0.43) | harms |
| phi0 | Phi tier off | +0.16 (+0.12, +0.22) | +1.48 (+1.30, +1.67) | +3.81 (+3.52, +4.13) | harms |
| ph5 | phase-in over 5 years | -0.00 (-0.02, +0.01) | +0.03 (-0.02, +0.08) | -0.10 (-0.15, -0.06) | does not move |
| ph10 | phase-in over 10 years | +0.02 (-0.00, +0.04) | +0.24 (+0.15, +0.34) | -0.08 (-0.14, -0.03) | harms |
| cap2 | issuance cap 2% | +18.03 (+17.47, +18.64) | +40.45 (+39.68, +41.28) | +30.56 (+29.91, +31.20) | harms |
| cap4 | issuance cap 4% | +18.03 (+17.47, +18.64) | +40.45 (+39.68, +41.28) | +30.56 (+29.91, +31.20) | harms |
| cap8 | issuance cap 8% | +18.03 (+17.47, +18.64) | +40.45 (+39.68, +41.28) | +30.56 (+29.91, +31.20) | harms |
| ixs | indexation: surge protocol (5%) | +0.37 (+0.29, +0.45) | +4.54 (+4.16, +4.94) | +4.62 (+4.31, +4.97) | harms |
| ixy | indexation: every year, price level | +0.37 (+0.29, +0.45) | +4.54 (+4.16, +4.94) | +4.62 (+4.31, +4.97) | harms |
| ixn | indexation: every year, basic needs | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| sva | protected account, all savings | +6.10 (+5.78, +6.41) | +3.44 (+2.92, +3.98) | -7.87 (-8.68, -7.08) | harms |
| svc | protected account, first $10,000 | -0.46 (-0.56, -0.37) | -5.59 (-6.04, -5.13) | -16.16 (-16.94, -15.39) | works |
| rcap | rent cap for BU tenants | -0.18 (-0.24, -0.13) | -2.06 (-2.26, -1.86) | -3.48 (-3.81, -3.18) | works |
| hc | rent risk ($1.41 a BU dollar) | +7.71 (+7.31, +8.14) | +25.40 (+24.66, +26.16) | +25.38 (+24.72, +26.01) | harms |
| hcrc | rent risk and rent cap | -0.18 (-0.24, -0.13) | -2.06 (-2.26, -1.86) | -3.48 (-3.81, -3.18) | works |

### non-participants' basket poverty, %: C2.2 design, wages 100% (lever effect, seed mean and 95% interval)

| Row | What it sets | Reference | Adverse | Stress | Verdict |
|---|---|---|---|---|---|
| asis | today's joining rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| t0 | tax 0% | -0.29 (-0.36, -0.24) | -0.52 (-0.60, -0.44) | -1.15 (-1.24, -1.06) | works |
| t4 | tax 4% | -0.23 (-0.29, -0.19) | -0.41 (-0.47, -0.34) | -1.15 (-1.23, -1.06) | works |
| t8 | tax 8% | -0.14 (-0.17, -0.11) | -0.24 (-0.28, -0.20) | -0.93 (-1.00, -0.85) | works |
| t12 | tax 12% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -0.62 (-0.68, -0.56) | does not move |
| t16 | tax 16% | +0.17 (+0.14, +0.21) | +0.27 (+0.23, +0.32) | -0.22 (-0.25, -0.20) | harms |
| t20 | tax 20% | +0.35 (+0.29, +0.40) | +0.61 (+0.53, +0.70) | +0.24 (+0.22, +0.26) | harms |
| t25 | tax 25% | +0.61 (+0.52, +0.70) | +1.22 (+1.07, +1.39) | +0.94 (+0.87, +1.02) | harms |
| t30 | tax 30% | +0.92 (+0.80, +1.05) | +1.85 (+1.63, +2.11) | +1.69 (+1.56, +1.83) | harms |
| t40 | tax 40% | +1.85 (+1.65, +2.06) | +3.50 (+3.14, +3.89) | +3.72 (+3.50, +3.95) | harms |
| asis.t0 | tax 0%, today's rule | -0.29 (-0.36, -0.24) | -0.52 (-0.60, -0.44) | -1.15 (-1.24, -1.06) | works |
| asis.t4 | tax 4%, today's rule | -0.23 (-0.29, -0.19) | -0.41 (-0.47, -0.34) | -1.15 (-1.23, -1.06) | works |
| asis.t8 | tax 8%, today's rule | -0.14 (-0.17, -0.11) | -0.24 (-0.28, -0.20) | -0.93 (-1.00, -0.85) | works |
| asis.t12 | tax 12%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -0.62 (-0.68, -0.56) | does not move |
| asis.t16 | tax 16%, today's rule | +0.17 (+0.14, +0.21) | +0.27 (+0.23, +0.32) | -0.22 (-0.25, -0.20) | harms |
| asis.t20 | tax 20%, today's rule | +0.35 (+0.29, +0.40) | +0.61 (+0.53, +0.70) | +0.24 (+0.22, +0.26) | harms |
| asis.t25 | tax 25%, today's rule | +0.61 (+0.52, +0.70) | +1.22 (+1.07, +1.39) | +0.94 (+0.87, +1.02) | harms |
| asis.t30 | tax 30%, today's rule | +0.92 (+0.80, +1.05) | +1.85 (+1.63, +2.11) | +1.69 (+1.56, +1.83) | harms |
| asis.t40 | tax 40%, today's rule | +1.85 (+1.65, +2.06) | +3.50 (+3.14, +3.89) | +3.72 (+3.50, +3.95) | harms |
| pr0c75 | progression 0 pts, cap 75% | -0.10 (-0.12, -0.07) | -0.19 (-0.22, -0.15) | -0.24 (-0.27, -0.21) | works |
| pr8c75 | progression 8 pts, cap 75% | +0.11 (+0.09, +0.15) | +0.24 (+0.19, +0.29) | +0.30 (+0.27, +0.34) | harms |
| pr0c50 | progression 0 pts, cap 50% | -0.10 (-0.12, -0.07) | -0.19 (-0.22, -0.15) | -0.24 (-0.27, -0.21) | works |
| pr4c50 | progression 4 pts, cap 50% | +0.00 (+0.00, +0.00) | -0.00 (-0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| pr8c50 | progression 8 pts, cap 50% | +0.12 (+0.09, +0.14) | +0.21 (+0.17, +0.26) | +0.24 (+0.22, +0.27) | harms |
| bt0 | business tax 0% | -0.19 (-0.24, -0.15) | -0.35 (-0.42, -0.29) | -0.84 (-0.92, -0.77) | works |
| bt25 | business tax 25% | +0.43 (+0.36, +0.51) | +0.78 (+0.68, +0.89) | +0.67 (+0.61, +0.73) | harms |
| bt50 | business tax 50% | +2.24 (+2.02, +2.47) | +4.00 (+3.61, +4.44) | +5.02 (+4.75, +5.29) | harms |
| bt75 | business tax 75% | +5.97 (+5.43, +6.54) | +10.57 (+9.83, +11.32) | +12.36 (+11.92, +12.81) | harms |
| kp10 | Source keeps 10% of project sales | -0.02 (-0.03, -0.01) | -0.05 (-0.07, -0.04) | -0.09 (-0.10, -0.08) | works |
| kp25 | Source keeps 25% of project sales | -0.06 (-0.08, -0.04) | -0.13 (-0.16, -0.10) | -0.21 (-0.24, -0.19) | works |
| kp50 | Source keeps 50% of project sales | -0.11 (-0.13, -0.08) | -0.24 (-0.29, -0.19) | -0.41 (-0.46, -0.37) | works |
| ex50 | 50% of expired BU recycled | +0.76 (+0.65, +0.88) | +1.67 (+1.45, +1.91) | +1.88 (+1.74, +2.02) | harms |
| ex0 | 0% of expired BU recycled | +2.81 (+2.48, +3.15) | +5.11 (+4.65, +5.60) | +4.80 (+4.56, +5.06) | harms |
| fprog | outside finance: progressive income tax | +4.00 (+3.71, +4.28) | +7.00 (+6.44, +7.57) | +11.58 (+10.88, +12.25) | harms |
| fland | outside finance: land-value tax | +6.22 (+5.89, +6.56) | +9.42 (+8.97, +9.87) | +10.89 (+10.54, +11.23) | harms |
| fflat | outside finance: flat wage contribution | +6.67 (+6.37, +6.99) | +6.41 (+6.04, +6.76) | +9.55 (+9.22, +9.85) | harms |
| br1 | business rate 1x | +6.08 (+5.54, +6.64) | +10.34 (+9.64, +11.06) | +11.87 (+11.46, +12.29) | harms |
| br15 | business rate 1.5x | +3.78 (+3.43, +4.17) | +6.42 (+5.87, +6.98) | +8.28 (+7.93, +8.66) | harms |
| br2 | business rate 2x | +1.83 (+1.64, +2.04) | +3.31 (+2.98, +3.69) | +4.28 (+4.04, +4.53) | harms |
| bu60 | 60% of the BU | +7.08 (+6.48, +7.71) | +11.61 (+10.77, +12.43) | +12.83 (+12.35, +13.31) | harms |
| bu80 | 80% of the BU | +2.36 (+2.14, +2.60) | +4.18 (+3.78, +4.63) | +4.93 (+4.66, +5.21) | harms |
| mm3 | top multiplier 3 | +0.68 (+0.59, +0.79) | +1.70 (+1.47, +1.94) | +1.29 (+1.18, +1.40) | harms |
| mm6 | top multiplier 6 | +0.26 (+0.22, +0.31) | +0.50 (+0.43, +0.58) | +0.00 (+0.00, +0.00) | harms |
| mm9 | top multiplier 9 | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -0.61 (-0.68, -0.55) | does not move |
| oc25 | octave capacity 25% | +0.53 (+0.44, +0.63) | +2.22 (+1.98, +2.47) | +3.08 (+2.91, +3.25) | harms |
| oc50 | octave capacity 50% | +0.32 (+0.26, +0.38) | +1.72 (+1.55, +1.90) | +2.71 (+2.57, +2.86) | harms |
| oc100 | octave capacity 100% | +0.15 (+0.13, +0.19) | +1.28 (+1.15, +1.42) | +2.31 (+2.19, +2.44) | harms |
| no2 | 2 octaves | -0.40 (-0.47, -0.33) | -0.50 (-0.59, -0.42) | -0.26 (-0.29, -0.22) | works |
| no4 | 4 octaves | -0.22 (-0.27, -0.18) | -0.29 (-0.34, -0.24) | +0.00 (+0.00, +0.00) | does not move |
| no6 | 6 octaves | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.32 (+0.29, +0.36) | harms |
| phi0 | Phi tier off | +0.06 (+0.04, +0.07) | +0.08 (+0.06, +0.11) | +0.35 (+0.32, +0.39) | harms |
| ph5 | phase-in over 5 years | +0.51 (+0.45, +0.57) | +0.59 (+0.52, +0.66) | +0.73 (+0.68, +0.78) | harms |
| ph10 | phase-in over 10 years | +1.36 (+1.23, +1.48) | +1.59 (+1.44, +1.75) | +1.93 (+1.82, +2.04) | harms |
| cap2 | issuance cap 2% | +6.96 (+6.39, +7.56) | +12.25 (+11.55, +12.97) | +12.85 (+12.47, +13.25) | harms |
| cap4 | issuance cap 4% | +6.96 (+6.39, +7.56) | +12.25 (+11.55, +12.97) | +12.85 (+12.47, +13.25) | harms |
| cap8 | issuance cap 8% | +6.96 (+6.39, +7.56) | +12.25 (+11.55, +12.97) | +12.85 (+12.47, +13.25) | harms |
| ixs | indexation: surge protocol (5%) | +0.24 (+0.19, +0.28) | +0.44 (+0.38, +0.51) | +0.67 (+0.62, +0.74) | harms |
| ixy | indexation: every year, price level | +0.24 (+0.19, +0.28) | +0.44 (+0.38, +0.51) | +0.67 (+0.62, +0.74) | harms |
| ixn | indexation: every year, basic needs | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| sva | protected account, all savings | +7.16 (+6.55, +7.80) | +12.85 (+12.15, +13.60) | +13.17 (+12.77, +13.58) | harms |
| svc | protected account, first $10,000 | +0.06 (+0.04, +0.09) | +0.17 (+0.14, +0.20) | +0.38 (+0.34, +0.41) | harms |
| rcap | rent cap for BU tenants | -0.14 (-0.17, -0.11) | -0.23 (-0.28, -0.19) | -0.42 (-0.46, -0.37) | works |
| hc | rent risk ($1.41 a BU dollar) | +2.66 (+2.42, +2.92) | +4.61 (+4.19, +5.06) | +6.74 (+6.43, +7.05) | harms |
| hcrc | rent risk and rent cap | -0.14 (-0.17, -0.11) | -0.23 (-0.28, -0.19) | -0.42 (-0.46, -0.37) | works |

### programme inflation, points a year: C2.2 design, wages 100% (lever effect, seed mean and 95% interval)

| Row | What it sets | Reference | Adverse | Stress | Verdict |
|---|---|---|---|---|---|
| asis | today's joining rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| t0 | tax 0% | -1.30 (-1.34, -1.26) | -2.14 (-2.20, -2.09) | -3.50 (-3.59, -3.41) | works |
| t4 | tax 4% | -0.87 (-0.89, -0.84) | -1.43 (-1.47, -1.40) | -2.79 (-2.87, -2.72) | works |
| t8 | tax 8% | -0.43 (-0.44, -0.42) | -0.71 (-0.73, -0.69) | -1.99 (-2.04, -1.94) | works |
| t12 | tax 12% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -1.17 (-1.21, -1.14) | does not move |
| t16 | tax 16% | +0.39 (+0.38, +0.41) | +0.68 (+0.66, +0.70) | -0.38 (-0.39, -0.37) | harms |
| t20 | tax 20% | +0.75 (+0.73, +0.78) | +1.32 (+1.28, +1.36) | +0.37 (+0.36, +0.38) | harms |
| t25 | tax 25% | +1.14 (+1.10, +1.18) | +2.05 (+1.99, +2.11) | +1.21 (+1.18, +1.24) | harms |
| t30 | tax 30% | +1.39 (+1.34, +1.44) | +2.61 (+2.54, +2.69) | +1.88 (+1.83, +1.93) | harms |
| t40 | tax 40% | +1.18 (+1.12, +1.25) | +2.76 (+2.66, +2.88) | +1.84 (+1.76, +1.94) | harms |
| asis.t0 | tax 0%, today's rule | -1.30 (-1.34, -1.26) | -2.14 (-2.20, -2.09) | -3.50 (-3.59, -3.41) | works |
| asis.t4 | tax 4%, today's rule | -0.87 (-0.89, -0.84) | -1.43 (-1.47, -1.40) | -2.79 (-2.87, -2.72) | works |
| asis.t8 | tax 8%, today's rule | -0.43 (-0.44, -0.42) | -0.71 (-0.73, -0.69) | -1.99 (-2.04, -1.94) | works |
| asis.t12 | tax 12%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -1.17 (-1.21, -1.14) | does not move |
| asis.t16 | tax 16%, today's rule | +0.39 (+0.38, +0.41) | +0.68 (+0.66, +0.70) | -0.38 (-0.39, -0.37) | harms |
| asis.t20 | tax 20%, today's rule | +0.75 (+0.73, +0.78) | +1.32 (+1.28, +1.36) | +0.37 (+0.36, +0.38) | harms |
| asis.t25 | tax 25%, today's rule | +1.14 (+1.10, +1.18) | +2.05 (+1.99, +2.11) | +1.21 (+1.18, +1.24) | harms |
| asis.t30 | tax 30%, today's rule | +1.39 (+1.34, +1.44) | +2.61 (+2.54, +2.69) | +1.88 (+1.83, +1.93) | harms |
| asis.t40 | tax 40%, today's rule | +1.18 (+1.12, +1.25) | +2.76 (+2.66, +2.88) | +1.84 (+1.76, +1.94) | harms |
| pr0c75 | progression 0 pts, cap 75% | -0.86 (-0.91, -0.83) | -1.42 (-1.48, -1.36) | -1.10 (-1.14, -1.06) | works |
| pr8c75 | progression 8 pts, cap 75% | +0.78 (+0.75, +0.82) | +1.27 (+1.23, +1.33) | +1.15 (+1.11, +1.20) | harms |
| pr0c50 | progression 0 pts, cap 50% | -0.86 (-0.91, -0.83) | -1.42 (-1.48, -1.36) | -1.10 (-1.14, -1.06) | works |
| pr4c50 | progression 4 pts, cap 50% | -0.03 (-0.04, -0.03) | -0.05 (-0.06, -0.04) | +0.00 (+0.00, +0.00) | does not move |
| pr8c50 | progression 8 pts, cap 50% | +0.50 (+0.49, +0.52) | +0.83 (+0.81, +0.85) | +0.73 (+0.71, +0.76) | harms |
| bt0 | business tax 0% | -0.69 (-0.70, -0.67) | -1.09 (-1.12, -1.06) | -1.63 (-1.68, -1.57) | works |
| bt25 | business tax 25% | +0.78 (+0.76, +0.80) | +1.27 (+1.24, +1.31) | +0.70 (+0.68, +0.72) | harms |
| bt50 | business tax 50% | +0.33 (+0.27, +0.39) | +1.18 (+1.09, +1.28) | -0.48 (-0.58, -0.37) | harms |
| bt75 | business tax 75% | -3.11 (-3.21, -3.01) | -2.15 (-2.31, -1.97) | -4.96 (-5.13, -4.79) | works |
| kp10 | Source keeps 10% of project sales | -1.72 (-1.74, -1.70) | -2.04 (-2.06, -2.02) | -1.69 (-1.71, -1.67) | works |
| kp25 | Source keeps 25% of project sales | -4.37 (-4.42, -4.33) | -5.23 (-5.29, -5.18) | -4.36 (-4.41, -4.31) | works |
| kp50 | Source keeps 50% of project sales | -8.91 (-9.01, -8.81) | -10.91 (-11.04, -10.79) | -9.24 (-9.35, -9.13) | works |
| ex50 | 50% of expired BU recycled | +3.55 (+3.50, +3.61) | +5.00 (+4.92, +5.09) | +4.24 (+4.18, +4.31) | harms |
| ex0 | 0% of expired BU recycled | +7.62 (+7.51, +7.75) | +10.65 (+10.48, +10.84) | +8.78 (+8.64, +8.93) | harms |
| fprog | outside finance: progressive income tax | -5.91 (-6.22, -5.55) | -0.60 (-1.03, -0.11) | -6.05 (-6.46, -5.60) | works |
| fland | outside finance: land-value tax | -32.63 (-32.94, -32.35) | -38.15 (-38.50, -37.80) | -41.19 (-41.59, -40.79) | works |
| fflat | outside finance: flat wage contribution | -37.58 (-37.92, -37.25) | -44.12 (-44.57, -43.70) | -46.17 (-46.68, -45.68) | works |
| br1 | business rate 1x | -3.19 (-3.29, -3.09) | -2.75 (-2.88, -2.63) | -5.55 (-5.68, -5.42) | works |
| br15 | business rate 1.5x | -1.22 (-1.30, -1.14) | -0.56 (-0.66, -0.45) | -3.31 (-3.42, -3.20) | works |
| br2 | business rate 2x | +0.72 (+0.66, +0.77) | +1.56 (+1.49, +1.64) | -0.13 (-0.21, -0.06) | harms |
| bu60 | 60% of the BU | -2.40 (-2.50, -2.30) | -1.98 (-2.12, -1.85) | -4.78 (-4.93, -4.64) | works |
| bu80 | 80% of the BU | +2.09 (+2.03, +2.15) | +3.20 (+3.12, +3.29) | +1.41 (+1.33, +1.50) | harms |
| mm3 | top multiplier 3 | +2.05 (+1.98, +2.13) | +3.76 (+3.66, +3.87) | +2.57 (+2.52, +2.63) | harms |
| mm6 | top multiplier 6 | +0.78 (+0.75, +0.81) | +1.45 (+1.42, +1.50) | +0.00 (+0.00, +0.00) | harms |
| mm9 | top multiplier 9 | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -1.39 (-1.42, -1.36) | does not move |
| oc25 | octave capacity 25% | +0.97 (+0.90, +1.05) | +3.41 (+3.30, +3.54) | +4.62 (+4.52, +4.75) | harms |
| oc50 | octave capacity 50% | +0.79 (+0.74, +0.86) | +2.91 (+2.81, +3.03) | +4.16 (+4.06, +4.27) | harms |
| oc100 | octave capacity 100% | +0.68 (+0.64, +0.73) | +2.35 (+2.26, +2.46) | +3.69 (+3.60, +3.79) | harms |
| no2 | 2 octaves | -2.27 (-2.30, -2.25) | -2.17 (-2.20, -2.15) | -0.80 (-0.81, -0.79) | works |
| no4 | 4 octaves | -1.16 (-1.18, -1.15) | -1.10 (-1.11, -1.08) | +0.00 (+0.00, +0.00) | does not move |
| no6 | 6 octaves | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.80 (+0.79, +0.81) | harms |
| phi0 | Phi tier off | +0.29 (+0.27, +0.31) | +0.43 (+0.40, +0.46) | +1.03 (+1.00, +1.08) | harms |
| ph5 | phase-in over 5 years | -0.21 (-0.22, -0.19) | -0.20 (-0.22, -0.18) | -0.47 (-0.49, -0.46) | works |
| ph10 | phase-in over 10 years | -0.58 (-0.61, -0.55) | -0.47 (-0.50, -0.43) | -1.09 (-1.12, -1.06) | works |
| cap2 | issuance cap 2% | -6.11 (-6.19, -6.02) | -4.51 (-4.63, -4.36) | -5.64 (-5.76, -5.53) | works |
| cap4 | issuance cap 4% | -6.11 (-6.19, -6.02) | -4.51 (-4.63, -4.36) | -5.64 (-5.76, -5.53) | works |
| cap8 | issuance cap 8% | -6.11 (-6.19, -6.02) | -4.51 (-4.63, -4.36) | -5.64 (-5.76, -5.53) | works |
| ixs | indexation: surge protocol (5%) | +0.67 (+0.65, +0.69) | +1.17 (+1.14, +1.21) | +1.02 (+0.99, +1.05) | harms |
| ixy | indexation: every year, price level | +0.67 (+0.65, +0.69) | +1.17 (+1.14, +1.21) | +1.02 (+0.99, +1.05) | harms |
| ixn | indexation: every year, basic needs | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| sva | protected account, all savings | +763.06 (+747.57, +780.14) | +944.13 (+924.48, +965.64) | +949.95 (+930.22, +971.58) | harms |
| svc | protected account, first $10,000 | +3.78 (+3.70, +3.86) | +6.21 (+6.07, +6.36) | +7.38 (+7.22, +7.57) | harms |
| rcap | rent cap for BU tenants | -1.03 (-1.06, -0.99) | -1.59 (-1.64, -1.55) | -1.86 (-1.91, -1.81) | works |
| hc | rent risk ($1.41 a BU dollar) | +8.25 (+8.14, +8.37) | +10.59 (+10.45, +10.73) | +10.91 (+10.78, +11.04) | harms |
| hcrc | rent risk and rent cap | -1.03 (-1.06, -0.99) | -1.59 (-1.64, -1.55) | -1.86 (-1.91, -1.81) | works |

### participation, mean of years 1-19, %: C2.2 design, wages 100% (lever effect, seed mean and 95% interval)

| Row | What it sets | Reference | Adverse | Stress | Verdict |
|---|---|---|---|---|---|
| asis | today's joining rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| t0 | tax 0% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| t4 | tax 4% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| t8 | tax 8% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| t12 | tax 12% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| t16 | tax 16% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| t20 | tax 20% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| t25 | tax 25% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| t30 | tax 30% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| t40 | tax 40% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t0 | tax 0%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t4 | tax 4%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t8 | tax 8%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t12 | tax 12%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t16 | tax 16%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t20 | tax 20%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t25 | tax 25%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t30 | tax 30%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t40 | tax 40%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| pr0c75 | progression 0 pts, cap 75% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| pr8c75 | progression 8 pts, cap 75% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| pr0c50 | progression 0 pts, cap 50% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| pr4c50 | progression 4 pts, cap 50% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| pr8c50 | progression 8 pts, cap 50% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| bt0 | business tax 0% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| bt25 | business tax 25% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| bt50 | business tax 50% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| bt75 | business tax 75% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| kp10 | Source keeps 10% of project sales | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| kp25 | Source keeps 25% of project sales | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| kp50 | Source keeps 50% of project sales | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ex50 | 50% of expired BU recycled | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ex0 | 0% of expired BU recycled | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| fprog | outside finance: progressive income tax | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| fland | outside finance: land-value tax | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| fflat | outside finance: flat wage contribution | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| br1 | business rate 1x | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| br15 | business rate 1.5x | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| br2 | business rate 2x | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| bu60 | 60% of the BU | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| bu80 | 80% of the BU | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| mm3 | top multiplier 3 | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| mm6 | top multiplier 6 | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| mm9 | top multiplier 9 | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| oc25 | octave capacity 25% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| oc50 | octave capacity 50% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| oc100 | octave capacity 100% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| no2 | 2 octaves | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| no4 | 4 octaves | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| no6 | 6 octaves | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| phi0 | Phi tier off | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ph5 | phase-in over 5 years | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ph10 | phase-in over 10 years | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| cap2 | issuance cap 2% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| cap4 | issuance cap 4% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| cap8 | issuance cap 8% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ixs | indexation: surge protocol (5%) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ixy | indexation: every year, price level | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ixn | indexation: every year, basic needs | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| sva | protected account, all savings | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| svc | protected account, first $10,000 | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| rcap | rent cap for BU tenants | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| hc | rent risk ($1.41 a BU dollar) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| hcrc | rent risk and rent cap | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |

### basket poverty, % of adult-years: C2.2 design, wages 90% (lever effect, seed mean and 95% interval)

| Row | What it sets | Reference | Adverse | Stress | Verdict |
|---|---|---|---|---|---|
| asis | today's joining rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| t0 | tax 0% | -0.66 (-0.71, -0.61) | -1.72 (-1.81, -1.63) | -3.49 (-3.66, -3.33) | works |
| t4 | tax 4% | -0.51 (-0.55, -0.48) | -1.32 (-1.39, -1.25) | -3.39 (-3.54, -3.26) | works |
| t8 | tax 8% | -0.29 (-0.31, -0.27) | -0.75 (-0.80, -0.71) | -2.70 (-2.82, -2.59) | works |
| t12 | tax 12% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -1.72 (-1.80, -1.64) | does not move |
| t16 | tax 16% | +0.37 (+0.34, +0.40) | +0.90 (+0.85, +0.95) | -0.61 (-0.65, -0.57) | harms |
| t20 | tax 20% | +0.82 (+0.76, +0.88) | +1.94 (+1.85, +2.03) | +0.63 (+0.59, +0.66) | harms |
| t25 | tax 25% | +1.50 (+1.41, +1.59) | +3.51 (+3.35, +3.67) | +2.39 (+2.30, +2.48) | harms |
| t30 | tax 30% | +2.28 (+2.16, +2.42) | +5.24 (+5.03, +5.46) | +4.35 (+4.21, +4.50) | harms |
| t40 | tax 40% | +4.27 (+4.06, +4.49) | +8.99 (+8.68, +9.32) | +8.42 (+8.19, +8.67) | harms |
| asis.t0 | tax 0%, today's rule | -0.66 (-0.71, -0.61) | -1.72 (-1.81, -1.63) | -3.49 (-3.66, -3.33) | works |
| asis.t4 | tax 4%, today's rule | -0.51 (-0.55, -0.48) | -1.32 (-1.39, -1.25) | -3.39 (-3.54, -3.26) | works |
| asis.t8 | tax 8%, today's rule | -0.29 (-0.31, -0.27) | -0.75 (-0.80, -0.71) | -2.70 (-2.82, -2.59) | works |
| asis.t12 | tax 12%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -1.72 (-1.80, -1.64) | does not move |
| asis.t16 | tax 16%, today's rule | +0.37 (+0.34, +0.40) | +0.90 (+0.85, +0.95) | -0.61 (-0.65, -0.57) | harms |
| asis.t20 | tax 20%, today's rule | +0.82 (+0.76, +0.88) | +1.94 (+1.85, +2.03) | +0.63 (+0.59, +0.66) | harms |
| asis.t25 | tax 25%, today's rule | +1.50 (+1.41, +1.59) | +3.51 (+3.35, +3.67) | +2.39 (+2.30, +2.48) | harms |
| asis.t30 | tax 30%, today's rule | +2.28 (+2.16, +2.42) | +5.24 (+5.03, +5.46) | +4.35 (+4.21, +4.50) | harms |
| asis.t40 | tax 40%, today's rule | +4.27 (+4.06, +4.49) | +8.99 (+8.68, +9.32) | +8.42 (+8.19, +8.67) | harms |
| pr0c75 | progression 0 pts, cap 75% | -0.26 (-0.28, -0.23) | -0.80 (-0.86, -0.75) | -0.84 (-0.90, -0.79) | works |
| pr8c75 | progression 8 pts, cap 75% | +0.34 (+0.31, +0.37) | +0.99 (+0.93, +1.05) | +1.09 (+1.03, +1.16) | harms |
| pr0c50 | progression 0 pts, cap 50% | -0.26 (-0.28, -0.23) | -0.80 (-0.86, -0.75) | -0.84 (-0.90, -0.79) | works |
| pr4c50 | progression 4 pts, cap 50% | -0.00 (-0.01, -0.00) | -0.01 (-0.02, -0.01) | +0.00 (+0.00, +0.00) | does not move |
| pr8c50 | progression 8 pts, cap 50% | +0.29 (+0.26, +0.32) | +0.81 (+0.76, +0.85) | +0.75 (+0.70, +0.80) | harms |
| bt0 | business tax 0% | -0.45 (-0.48, -0.41) | -1.15 (-1.22, -1.09) | -2.54 (-2.67, -2.41) | works |
| bt25 | business tax 25% | +0.98 (+0.92, +1.05) | +2.27 (+2.16, +2.37) | +1.67 (+1.60, +1.74) | harms |
| bt50 | business tax 50% | +4.71 (+4.49, +4.95) | +9.36 (+9.04, +9.70) | +10.04 (+9.75, +10.33) | harms |
| bt75 | business tax 75% | +11.72 (+11.35, +12.09) | +20.83 (+20.29, +21.38) | +20.80 (+20.37, +21.25) | harms |
| kp10 | Source keeps 10% of project sales | -0.11 (-0.12, -0.10) | -0.33 (-0.35, -0.31) | -0.38 (-0.41, -0.36) | works |
| kp25 | Source keeps 25% of project sales | -0.25 (-0.28, -0.23) | -0.76 (-0.81, -0.72) | -0.97 (-1.03, -0.93) | works |
| kp50 | Source keeps 50% of project sales | -0.45 (-0.48, -0.41) | -1.40 (-1.48, -1.33) | -2.02 (-2.11, -1.94) | works |
| ex50 | 50% of expired BU recycled | +2.18 (+2.05, +2.31) | +5.12 (+4.93, +5.31) | +5.05 (+4.91, +5.20) | harms |
| ex0 | 0% of expired BU recycled | +6.96 (+6.72, +7.22) | +13.28 (+12.96, +13.65) | +11.43 (+11.19, +11.70) | harms |
| fprog | outside finance: progressive income tax | +7.93 (+7.53, +8.33) | +21.66 (+20.65, +22.69) | +28.35 (+27.32, +29.41) | harms |
| fland | outside finance: land-value tax | +6.21 (+6.06, +6.35) | +9.37 (+8.99, +9.76) | +8.64 (+8.26, +9.03) | harms |
| fflat | outside finance: flat wage contribution | +6.10 (+5.94, +6.27) | +4.42 (+4.26, +4.57) | +5.12 (+4.86, +5.37) | harms |
| br1 | business rate 1x | +11.90 (+11.52, +12.28) | +20.27 (+19.83, +20.74) | +19.99 (+19.63, +20.37) | harms |
| br15 | business rate 1.5x | +7.61 (+7.32, +7.92) | +14.17 (+13.78, +14.59) | +15.33 (+15.00, +15.67) | harms |
| br2 | business rate 2x | +3.95 (+3.75, +4.17) | +8.00 (+7.72, +8.29) | +8.76 (+8.52, +9.01) | harms |
| bu60 | 60% of the BU | +12.98 (+12.60, +13.38) | +21.39 (+20.91, +21.91) | +20.57 (+20.18, +20.98) | harms |
| bu80 | 80% of the BU | +4.97 (+4.75, +5.22) | +9.99 (+9.65, +10.35) | +10.36 (+10.08, +10.66) | harms |
| mm3 | top multiplier 3 | +2.13 (+2.00, +2.27) | +5.10 (+4.91, +5.32) | +3.52 (+3.41, +3.64) | harms |
| mm6 | top multiplier 6 | +0.70 (+0.65, +0.76) | +1.76 (+1.67, +1.85) | +0.00 (+0.00, +0.00) | harms |
| mm9 | top multiplier 9 | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -1.83 (-1.92, -1.76) | does not move |
| oc25 | octave capacity 25% | +2.59 (+2.48, +2.72) | +7.34 (+7.13, +7.59) | +8.03 (+7.86, +8.24) | harms |
| oc50 | octave capacity 50% | +2.03 (+1.93, +2.14) | +6.41 (+6.21, +6.66) | +7.36 (+7.20, +7.56) | harms |
| oc100 | octave capacity 100% | +1.42 (+1.34, +1.51) | +5.41 (+5.22, +5.62) | +6.68 (+6.52, +6.87) | harms |
| no2 | 2 octaves | -0.58 (-0.62, -0.55) | -0.86 (-0.92, -0.81) | -0.43 (-0.47, -0.40) | works |
| no4 | 4 octaves | -0.33 (-0.35, -0.30) | -0.50 (-0.53, -0.46) | +0.00 (+0.00, +0.00) | does not move |
| no6 | 6 octaves | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.51 (+0.48, +0.54) | harms |
| phi0 | Phi tier off | +0.14 (+0.12, +0.15) | +0.36 (+0.33, +0.40) | +1.03 (+0.98, +1.09) | harms |
| ph5 | phase-in over 5 years | +0.61 (+0.58, +0.64) | +0.68 (+0.64, +0.72) | +0.70 (+0.66, +0.73) | harms |
| ph10 | phase-in over 10 years | +1.67 (+1.59, +1.74) | +2.05 (+1.96, +2.15) | +2.15 (+2.06, +2.25) | harms |
| cap2 | issuance cap 2% | +13.87 (+13.49, +14.27) | +23.34 (+22.86, +23.86) | +21.68 (+21.31, +22.09) | harms |
| cap4 | issuance cap 4% | +13.87 (+13.49, +14.27) | +23.34 (+22.86, +23.86) | +21.68 (+21.31, +22.09) | harms |
| cap8 | issuance cap 8% | +13.87 (+13.49, +14.27) | +23.34 (+22.86, +23.86) | +21.68 (+21.31, +22.09) | harms |
| ixs | indexation: surge protocol (5%) | +0.47 (+0.43, +0.51) | +1.28 (+1.21, +1.35) | +1.61 (+1.52, +1.70) | harms |
| ixy | indexation: every year, price level | +0.47 (+0.43, +0.51) | +1.28 (+1.21, +1.35) | +1.61 (+1.52, +1.70) | harms |
| ixn | indexation: every year, basic needs | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| sva | protected account, all savings | +41.40 (+40.93, +41.89) | +48.22 (+47.87, +48.60) | +45.46 (+45.19, +45.75) | harms |
| svc | protected account, first $10,000 | +0.41 (+0.38, +0.45) | +2.20 (+2.05, +2.36) | +3.69 (+3.50, +3.90) | harms |
| rcap | rent cap for BU tenants | -0.25 (-0.27, -0.23) | -0.70 (-0.75, -0.65) | -1.15 (-1.23, -1.08) | works |
| hc | rent risk ($1.41 a BU dollar) | +6.27 (+6.03, +6.53) | +12.64 (+12.23, +13.04) | +16.01 (+15.65, +16.39) | harms |
| hcrc | rent risk and rent cap | -0.25 (-0.27, -0.23) | -0.70 (-0.75, -0.65) | -1.15 (-1.23, -1.08) | works |

### wealth poverty at year 20, %: C2.2 design, wages 90% (lever effect, seed mean and 95% interval)

| Row | What it sets | Reference | Adverse | Stress | Verdict |
|---|---|---|---|---|---|
| asis | today's joining rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| t0 | tax 0% | -7.62 (-8.31, -6.96) | -28.58 (-29.50, -27.77) | -31.78 (-32.58, -31.06) | works |
| t4 | tax 4% | -6.19 (-6.80, -5.66) | -19.74 (-20.40, -19.16) | -25.21 (-25.96, -24.52) | works |
| t8 | tax 8% | -3.80 (-4.24, -3.42) | -9.91 (-10.49, -9.34) | -17.03 (-17.63, -16.42) | works |
| t12 | tax 12% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -9.46 (-9.90, -9.00) | does not move |
| t16 | tax 16% | +4.71 (+4.36, +5.06) | +9.15 (+8.64, +9.66) | -2.73 (-2.99, -2.47) | harms |
| t20 | tax 20% | +10.11 (+9.56, +10.68) | +16.12 (+15.45, +16.82) | +2.36 (+2.08, +2.64) | harms |
| t25 | tax 25% | +17.04 (+16.36, +17.76) | +23.63 (+22.86, +24.40) | +7.34 (+6.77, +7.91) | harms |
| t30 | tax 30% | +23.77 (+22.99, +24.59) | +28.39 (+27.52, +29.29) | +10.32 (+9.58, +11.05) | harms |
| t40 | tax 40% | +33.03 (+32.20, +33.87) | +33.98 (+32.86, +35.04) | +13.62 (+12.68, +14.60) | harms |
| asis.t0 | tax 0%, today's rule | -7.62 (-8.31, -6.96) | -28.58 (-29.50, -27.77) | -31.78 (-32.58, -31.06) | works |
| asis.t4 | tax 4%, today's rule | -6.19 (-6.80, -5.66) | -19.74 (-20.40, -19.16) | -25.21 (-25.96, -24.52) | works |
| asis.t8 | tax 8%, today's rule | -3.80 (-4.24, -3.42) | -9.91 (-10.49, -9.34) | -17.03 (-17.63, -16.42) | works |
| asis.t12 | tax 12%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -9.46 (-9.90, -9.00) | does not move |
| asis.t16 | tax 16%, today's rule | +4.71 (+4.36, +5.06) | +9.15 (+8.64, +9.66) | -2.73 (-2.99, -2.47) | harms |
| asis.t20 | tax 20%, today's rule | +10.11 (+9.56, +10.68) | +16.12 (+15.45, +16.82) | +2.36 (+2.08, +2.64) | harms |
| asis.t25 | tax 25%, today's rule | +17.04 (+16.36, +17.76) | +23.63 (+22.86, +24.40) | +7.34 (+6.77, +7.91) | harms |
| asis.t30 | tax 30%, today's rule | +23.77 (+22.99, +24.59) | +28.39 (+27.52, +29.29) | +10.32 (+9.58, +11.05) | harms |
| asis.t40 | tax 40%, today's rule | +33.03 (+32.20, +33.87) | +33.98 (+32.86, +35.04) | +13.62 (+12.68, +14.60) | harms |
| pr0c75 | progression 0 pts, cap 75% | -4.86 (-5.34, -4.44) | -14.36 (-15.08, -13.68) | -7.28 (-7.68, -6.88) | works |
| pr8c75 | progression 8 pts, cap 75% | +6.56 (+6.09, +7.09) | +13.42 (+12.64, +14.24) | +5.50 (+5.00, +6.00) | harms |
| pr0c50 | progression 0 pts, cap 50% | -4.86 (-5.34, -4.44) | -14.36 (-15.08, -13.68) | -7.28 (-7.68, -6.88) | works |
| pr4c50 | progression 4 pts, cap 50% | -0.08 (-0.14, -0.04) | -0.41 (-0.54, -0.29) | +0.00 (+0.00, +0.00) | does not move |
| pr8c50 | progression 8 pts, cap 50% | +5.23 (+4.86, +5.62) | +9.36 (+8.82, +9.97) | +3.41 (+3.04, +3.80) | harms |
| bt0 | business tax 0% | -5.32 (-5.81, -4.86) | -15.82 (-16.37, -15.31) | -16.41 (-16.88, -15.91) | works |
| bt25 | business tax 25% | +10.65 (+10.12, +11.20) | +17.10 (+16.41, +17.80) | +5.34 (+4.89, +5.80) | harms |
| bt50 | business tax 50% | +30.12 (+29.38, +30.92) | +32.64 (+31.62, +33.65) | +13.26 (+12.44, +14.10) | harms |
| bt75 | business tax 75% | +39.41 (+38.62, +40.23) | +39.35 (+38.18, +40.46) | +16.96 (+16.05, +17.84) | harms |
| kp10 | Source keeps 10% of project sales | -3.04 (-3.38, -2.71) | -7.09 (-7.53, -6.66) | -3.08 (-3.39, -2.79) | works |
| kp25 | Source keeps 25% of project sales | -6.28 (-6.88, -5.74) | -18.91 (-19.62, -18.24) | -8.79 (-9.34, -8.22) | works |
| kp50 | Source keeps 50% of project sales | -8.76 (-9.57, -8.00) | -38.72 (-39.82, -37.63) | -22.36 (-23.40, -21.28) | works |
| ex50 | 50% of expired BU recycled | +27.01 (+26.24, +27.82) | +28.40 (+27.41, +29.38) | +11.71 (+10.80, +12.61) | harms |
| ex0 | 0% of expired BU recycled | +49.44 (+48.53, +50.44) | +38.45 (+36.92, +39.91) | +17.02 (+15.80, +18.27) | harms |
| fprog | outside finance: progressive income tax | +57.19 (+55.85, +58.46) | +43.46 (+41.91, +44.95) | +23.94 (+22.58, +25.29) | harms |
| fland | outside finance: land-value tax | -9.50 (-10.39, -8.68) | -48.88 (-50.80, -47.00) | -71.83 (-73.28, -70.36) | works |
| fflat | outside finance: flat wage contribution | -7.58 (-8.41, -6.80) | -47.44 (-49.38, -45.56) | -68.44 (-70.01, -66.85) | works |
| br1 | business rate 1x | +39.61 (+38.81, +40.42) | +38.49 (+37.38, +39.58) | +16.13 (+15.26, +17.02) | harms |
| br15 | business rate 1.5x | +35.02 (+34.26, +35.83) | +35.91 (+34.83, +36.95) | +15.09 (+14.28, +15.94) | harms |
| br2 | business rate 2x | +28.05 (+27.27, +28.87) | +31.27 (+30.25, +32.26) | +12.47 (+11.64, +13.31) | harms |
| bu60 | 60% of the BU | +36.89 (+36.14, +37.71) | +32.17 (+30.96, +33.40) | +10.63 (+9.74, +11.53) | harms |
| bu80 | 80% of the BU | +30.87 (+30.11, +31.69) | +30.00 (+28.84, +31.15) | +11.40 (+10.53, +12.28) | harms |
| mm3 | top multiplier 3 | +25.70 (+24.97, +26.52) | +27.55 (+26.63, +28.46) | +9.41 (+8.65, +10.16) | harms |
| mm6 | top multiplier 6 | +10.55 (+10.03, +11.08) | +14.68 (+14.07, +15.32) | +0.00 (+0.00, +0.00) | harms |
| mm9 | top multiplier 9 | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -8.46 (-8.97, -7.93) | does not move |
| oc25 | octave capacity 25% | +38.89 (+38.00, +39.88) | +34.94 (+33.56, +36.25) | +15.31 (+14.16, +16.45) | harms |
| oc50 | octave capacity 50% | +35.55 (+34.58, +36.61) | +34.29 (+32.96, +35.55) | +15.18 (+14.06, +16.30) | harms |
| oc100 | octave capacity 100% | +30.57 (+29.56, +31.74) | +33.07 (+31.88, +34.22) | +14.89 (+13.77, +15.99) | harms |
| no2 | 2 octaves | -1.96 (-2.21, -1.71) | -3.00 (-3.30, -2.71) | -0.63 (-0.76, -0.52) | works |
| no4 | 4 octaves | -1.17 (-1.38, -0.97) | -1.69 (-1.90, -1.49) | +0.00 (+0.00, +0.00) | does not move |
| no6 | 6 octaves | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.72 (+0.57, +0.88) | harms |
| phi0 | Phi tier off | +2.29 (+2.01, +2.61) | +3.86 (+3.42, +4.34) | +4.59 (+4.11, +5.08) | harms |
| ph5 | phase-in over 5 years | +0.00 (-0.05, +0.07) | -0.01 (-0.13, +0.10) | -0.40 (-0.50, -0.30) | does not move |
| ph10 | phase-in over 10 years | +0.19 (+0.11, +0.28) | +0.51 (+0.33, +0.70) | -0.93 (-1.09, -0.78) | harms |
| cap2 | issuance cap 2% | +41.85 (+41.05, +42.73) | +39.84 (+38.68, +40.98) | +17.22 (+16.27, +18.17) | harms |
| cap4 | issuance cap 4% | +41.85 (+41.05, +42.73) | +39.84 (+38.68, +40.98) | +17.22 (+16.27, +18.17) | harms |
| cap8 | issuance cap 8% | +41.85 (+41.05, +42.73) | +39.84 (+38.68, +40.98) | +17.22 (+16.27, +18.17) | harms |
| ixs | indexation: surge protocol (5%) | +4.79 (+4.41, +5.17) | +10.58 (+10.00, +11.17) | +4.52 (+4.14, +4.92) | harms |
| ixy | indexation: every year, price level | +4.79 (+4.41, +5.17) | +10.58 (+10.00, +11.17) | +4.52 (+4.14, +4.92) | harms |
| ixn | indexation: every year, basic needs | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| sva | protected account, all savings | +7.05 (+6.20, +7.86) | -30.72 (-32.64, -28.83) | -53.20 (-54.75, -51.60) | harms |
| svc | protected account, first $10,000 | -8.78 (-9.60, -8.01) | -45.85 (-47.69, -44.07) | -63.28 (-64.68, -61.88) | works |
| rcap | rent cap for BU tenants | -2.88 (-3.28, -2.51) | -8.80 (-9.34, -8.28) | -5.70 (-6.07, -5.37) | works |
| hc | rent risk ($1.41 a BU dollar) | +38.63 (+37.74, +39.56) | +34.34 (+33.00, +35.62) | +17.21 (+16.00, +18.44) | harms |
| hcrc | rent risk and rent cap | -2.88 (-3.28, -2.51) | -8.80 (-9.34, -8.28) | -5.70 (-6.07, -5.37) | works |

### non-participants' basket poverty, %: C2.2 design, wages 90% (lever effect, seed mean and 95% interval)

| Row | What it sets | Reference | Adverse | Stress | Verdict |
|---|---|---|---|---|---|
| asis | today's joining rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| t0 | tax 0% | -0.58 (-0.67, -0.49) | -1.65 (-1.83, -1.48) | -3.52 (-3.71, -3.33) | works |
| t4 | tax 4% | -0.47 (-0.55, -0.39) | -1.28 (-1.44, -1.14) | -3.41 (-3.57, -3.26) | works |
| t8 | tax 8% | -0.27 (-0.33, -0.22) | -0.73 (-0.84, -0.64) | -2.70 (-2.83, -2.58) | works |
| t12 | tax 12% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -1.72 (-1.81, -1.64) | does not move |
| t16 | tax 16% | +0.36 (+0.31, +0.42) | +0.90 (+0.81, +1.01) | -0.60 (-0.64, -0.56) | harms |
| t20 | tax 20% | +0.85 (+0.74, +0.97) | +1.86 (+1.71, +2.03) | +0.63 (+0.59, +0.67) | harms |
| t25 | tax 25% | +1.57 (+1.38, +1.80) | +3.38 (+3.16, +3.62) | +2.42 (+2.31, +2.53) | harms |
| t30 | tax 30% | +2.33 (+2.07, +2.61) | +5.09 (+4.77, +5.41) | +4.36 (+4.19, +4.54) | harms |
| t40 | tax 40% | +4.25 (+3.85, +4.66) | +8.79 (+8.34, +9.23) | +8.40 (+8.10, +8.71) | harms |
| asis.t0 | tax 0%, today's rule | -0.58 (-0.67, -0.49) | -1.65 (-1.83, -1.48) | -3.52 (-3.71, -3.33) | works |
| asis.t4 | tax 4%, today's rule | -0.47 (-0.55, -0.39) | -1.28 (-1.44, -1.14) | -3.41 (-3.57, -3.26) | works |
| asis.t8 | tax 8%, today's rule | -0.27 (-0.33, -0.22) | -0.73 (-0.84, -0.64) | -2.70 (-2.83, -2.58) | works |
| asis.t12 | tax 12%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -1.72 (-1.81, -1.64) | does not move |
| asis.t16 | tax 16%, today's rule | +0.36 (+0.31, +0.42) | +0.90 (+0.81, +1.01) | -0.60 (-0.64, -0.56) | harms |
| asis.t20 | tax 20%, today's rule | +0.85 (+0.74, +0.97) | +1.86 (+1.71, +2.03) | +0.63 (+0.59, +0.67) | harms |
| asis.t25 | tax 25%, today's rule | +1.57 (+1.38, +1.80) | +3.38 (+3.16, +3.62) | +2.42 (+2.31, +2.53) | harms |
| asis.t30 | tax 30%, today's rule | +2.33 (+2.07, +2.61) | +5.09 (+4.77, +5.41) | +4.36 (+4.19, +4.54) | harms |
| asis.t40 | tax 40%, today's rule | +4.25 (+3.85, +4.66) | +8.79 (+8.34, +9.23) | +8.40 (+8.10, +8.71) | harms |
| pr0c75 | progression 0 pts, cap 75% | -0.24 (-0.29, -0.19) | -0.80 (-0.93, -0.69) | -0.85 (-0.91, -0.79) | works |
| pr8c75 | progression 8 pts, cap 75% | +0.36 (+0.30, +0.43) | +1.00 (+0.90, +1.13) | +1.10 (+1.03, +1.18) | harms |
| pr0c50 | progression 0 pts, cap 50% | -0.24 (-0.29, -0.19) | -0.80 (-0.93, -0.69) | -0.85 (-0.91, -0.79) | works |
| pr4c50 | progression 4 pts, cap 50% | -0.00 (-0.01, -0.00) | -0.01 (-0.02, -0.00) | +0.00 (+0.00, +0.00) | does not move |
| pr8c50 | progression 8 pts, cap 50% | +0.31 (+0.26, +0.37) | +0.83 (+0.75, +0.94) | +0.76 (+0.71, +0.82) | harms |
| bt0 | business tax 0% | -0.42 (-0.49, -0.35) | -1.12 (-1.27, -1.00) | -2.55 (-2.69, -2.41) | works |
| bt25 | business tax 25% | +1.02 (+0.89, +1.17) | +2.16 (+2.00, +2.34) | +1.68 (+1.61, +1.77) | harms |
| bt50 | business tax 50% | +4.68 (+4.26, +5.15) | +9.14 (+8.66, +9.61) | +10.05 (+9.70, +10.41) | harms |
| bt75 | business tax 75% | +11.38 (+10.65, +12.12) | +20.44 (+19.60, +21.25) | +20.82 (+20.28, +21.39) | harms |
| kp10 | Source keeps 10% of project sales | -0.10 (-0.12, -0.08) | -0.32 (-0.37, -0.28) | -0.38 (-0.41, -0.35) | works |
| kp25 | Source keeps 25% of project sales | -0.25 (-0.30, -0.20) | -0.73 (-0.83, -0.65) | -0.96 (-1.02, -0.91) | works |
| kp50 | Source keeps 50% of project sales | -0.39 (-0.46, -0.32) | -1.34 (-1.50, -1.20) | -2.01 (-2.10, -1.93) | works |
| ex50 | 50% of expired BU recycled | +2.24 (+1.98, +2.53) | +5.04 (+4.72, +5.35) | +5.06 (+4.88, +5.24) | harms |
| ex0 | 0% of expired BU recycled | +6.91 (+6.40, +7.43) | +13.17 (+12.59, +13.78) | +11.40 (+11.07, +11.76) | harms |
| fprog | outside finance: progressive income tax | +7.48 (+6.93, +8.05) | +21.26 (+20.13, +22.40) | +28.38 (+27.29, +29.47) | harms |
| fland | outside finance: land-value tax | +6.27 (+5.89, +6.65) | +9.36 (+8.81, +9.87) | +8.73 (+8.31, +9.14) | harms |
| fflat | outside finance: flat wage contribution | +5.90 (+5.59, +6.22) | +4.25 (+3.87, +4.59) | +5.08 (+4.74, +5.37) | harms |
| br1 | business rate 1x | +11.55 (+10.81, +12.29) | +19.91 (+19.16, +20.64) | +20.01 (+19.55, +20.48) | harms |
| br15 | business rate 1.5x | +7.34 (+6.78, +7.93) | +13.84 (+13.21, +14.45) | +15.32 (+14.91, +15.73) | harms |
| br2 | business rate 2x | +3.94 (+3.56, +4.37) | +7.81 (+7.40, +8.22) | +8.76 (+8.47, +9.06) | harms |
| bu60 | 60% of the BU | +12.72 (+11.87, +13.56) | +21.06 (+20.21, +21.91) | +20.59 (+20.05, +21.13) | harms |
| bu80 | 80% of the BU | +4.94 (+4.49, +5.42) | +9.78 (+9.26, +10.28) | +10.33 (+9.97, +10.69) | harms |
| mm3 | top multiplier 3 | +2.21 (+1.94, +2.50) | +5.00 (+4.67, +5.32) | +3.53 (+3.40, +3.67) | harms |
| mm6 | top multiplier 6 | +0.72 (+0.62, +0.84) | +1.69 (+1.53, +1.85) | +0.00 (+0.00, +0.00) | harms |
| mm9 | top multiplier 9 | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -1.83 (-1.92, -1.75) | does not move |
| oc25 | octave capacity 25% | +2.59 (+2.36, +2.82) | +7.24 (+6.91, +7.57) | +7.98 (+7.75, +8.24) | harms |
| oc50 | octave capacity 50% | +2.06 (+1.88, +2.25) | +6.34 (+6.05, +6.65) | +7.33 (+7.12, +7.57) | harms |
| oc100 | octave capacity 100% | +1.49 (+1.35, +1.64) | +5.34 (+5.07, +5.62) | +6.65 (+6.46, +6.88) | harms |
| no2 | 2 octaves | -0.58 (-0.69, -0.48) | -0.83 (-0.97, -0.71) | -0.45 (-0.49, -0.41) | works |
| no4 | 4 octaves | -0.34 (-0.41, -0.27) | -0.49 (-0.58, -0.41) | +0.00 (+0.00, +0.00) | does not move |
| no6 | 6 octaves | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.50 (+0.46, +0.54) | harms |
| phi0 | Phi tier off | +0.12 (+0.09, +0.15) | +0.37 (+0.31, +0.43) | +1.04 (+0.98, +1.12) | harms |
| ph5 | phase-in over 5 years | +0.59 (+0.52, +0.65) | +0.68 (+0.61, +0.76) | +0.68 (+0.64, +0.73) | harms |
| ph10 | phase-in over 10 years | +1.62 (+1.47, +1.78) | +2.00 (+1.83, +2.18) | +2.14 (+2.03, +2.25) | harms |
| cap2 | issuance cap 2% | +13.41 (+12.72, +14.13) | +22.93 (+22.11, +23.72) | +21.63 (+21.17, +22.11) | harms |
| cap4 | issuance cap 4% | +13.41 (+12.72, +14.13) | +22.93 (+22.11, +23.72) | +21.63 (+21.17, +22.11) | harms |
| cap8 | issuance cap 8% | +13.41 (+12.72, +14.13) | +22.93 (+22.11, +23.72) | +21.63 (+21.17, +22.11) | harms |
| ixs | indexation: surge protocol (5%) | +0.48 (+0.41, +0.56) | +1.24 (+1.13, +1.38) | +1.62 (+1.53, +1.72) | harms |
| ixy | indexation: every year, price level | +0.48 (+0.41, +0.56) | +1.24 (+1.13, +1.38) | +1.62 (+1.53, +1.72) | harms |
| ixn | indexation: every year, basic needs | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| sva | protected account, all savings | +41.01 (+40.23, +41.76) | +48.09 (+47.50, +48.68) | +45.45 (+45.11, +45.82) | harms |
| svc | protected account, first $10,000 | +0.42 (+0.36, +0.49) | +2.11 (+1.95, +2.29) | +3.70 (+3.50, +3.92) | harms |
| rcap | rent cap for BU tenants | -0.24 (-0.29, -0.20) | -0.68 (-0.77, -0.60) | -1.15 (-1.23, -1.08) | works |
| hc | rent risk ($1.41 a BU dollar) | +6.12 (+5.66, +6.60) | +12.33 (+11.76, +12.90) | +16.00 (+15.57, +16.44) | harms |
| hcrc | rent risk and rent cap | -0.24 (-0.29, -0.20) | -0.68 (-0.77, -0.60) | -1.15 (-1.23, -1.08) | works |

### programme inflation, points a year: C2.2 design, wages 90% (lever effect, seed mean and 95% interval)

| Row | What it sets | Reference | Adverse | Stress | Verdict |
|---|---|---|---|---|---|
| asis | today's joining rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| t0 | tax 0% | -2.70 (-2.77, -2.62) | -4.53 (-4.66, -4.41) | -7.65 (-7.88, -7.44) | works |
| t4 | tax 4% | -1.82 (-1.88, -1.77) | -3.07 (-3.16, -2.99) | -6.15 (-6.32, -5.98) | works |
| t8 | tax 8% | -0.91 (-0.93, -0.88) | -1.54 (-1.59, -1.50) | -4.42 (-4.55, -4.30) | works |
| t12 | tax 12% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -2.64 (-2.72, -2.57) | does not move |
| t16 | tax 16% | +0.88 (+0.85, +0.91) | +1.55 (+1.51, +1.60) | -0.88 (-0.90, -0.85) | harms |
| t20 | tax 20% | +1.73 (+1.68, +1.79) | +3.08 (+2.99, +3.17) | +0.87 (+0.85, +0.90) | harms |
| t25 | tax 25% | +2.71 (+2.63, +2.80) | +4.83 (+4.70, +4.98) | +2.88 (+2.81, +2.95) | harms |
| t30 | tax 30% | +3.48 (+3.38, +3.59) | +6.24 (+6.08, +6.44) | +4.33 (+4.23, +4.44) | harms |
| t40 | tax 40% | +3.67 (+3.54, +3.81) | +7.07 (+6.85, +7.33) | +4.49 (+4.33, +4.67) | harms |
| asis.t0 | tax 0%, today's rule | -2.70 (-2.77, -2.62) | -4.53 (-4.66, -4.41) | -7.65 (-7.88, -7.44) | works |
| asis.t4 | tax 4%, today's rule | -1.82 (-1.88, -1.77) | -3.07 (-3.16, -2.99) | -6.15 (-6.32, -5.98) | works |
| asis.t8 | tax 8%, today's rule | -0.91 (-0.93, -0.88) | -1.54 (-1.59, -1.50) | -4.42 (-4.55, -4.30) | works |
| asis.t12 | tax 12%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -2.64 (-2.72, -2.57) | does not move |
| asis.t16 | tax 16%, today's rule | +0.88 (+0.85, +0.91) | +1.55 (+1.51, +1.60) | -0.88 (-0.90, -0.85) | harms |
| asis.t20 | tax 20%, today's rule | +1.73 (+1.68, +1.79) | +3.08 (+2.99, +3.17) | +0.87 (+0.85, +0.90) | harms |
| asis.t25 | tax 25%, today's rule | +2.71 (+2.63, +2.80) | +4.83 (+4.70, +4.98) | +2.88 (+2.81, +2.95) | harms |
| asis.t30 | tax 30%, today's rule | +3.48 (+3.38, +3.59) | +6.24 (+6.08, +6.44) | +4.33 (+4.23, +4.44) | harms |
| asis.t40 | tax 40%, today's rule | +3.67 (+3.54, +3.81) | +7.07 (+6.85, +7.33) | +4.49 (+4.33, +4.67) | harms |
| pr0c75 | progression 0 pts, cap 75% | -1.73 (-1.81, -1.66) | -2.84 (-2.96, -2.73) | -2.20 (-2.29, -2.12) | works |
| pr8c75 | progression 8 pts, cap 75% | +1.59 (+1.53, +1.66) | +2.61 (+2.51, +2.72) | +2.33 (+2.25, +2.43) | harms |
| pr0c50 | progression 0 pts, cap 50% | -1.73 (-1.81, -1.66) | -2.84 (-2.96, -2.73) | -2.20 (-2.29, -2.12) | works |
| pr4c50 | progression 4 pts, cap 50% | -0.06 (-0.07, -0.05) | -0.10 (-0.11, -0.09) | +0.00 (+0.00, +0.00) | does not move |
| pr8c50 | progression 8 pts, cap 50% | +1.03 (+1.01, +1.07) | +1.69 (+1.65, +1.75) | +1.49 (+1.44, +1.54) | harms |
| bt0 | business tax 0% | -1.43 (-1.47, -1.39) | -2.44 (-2.52, -2.37) | -4.03 (-4.16, -3.90) | works |
| bt25 | business tax 25% | +1.73 (+1.68, +1.78) | +3.03 (+2.95, +3.12) | +1.80 (+1.75, +1.85) | harms |
| bt50 | business tax 50% | +1.69 (+1.59, +1.80) | +3.90 (+3.72, +4.10) | +0.68 (+0.50, +0.88) | harms |
| bt75 | business tax 75% | -2.83 (-2.98, -2.67) | +0.51 (+0.18, +0.87) | -4.45 (-4.78, -4.11) | harms |
| kp10 | Source keeps 10% of project sales | -2.41 (-2.44, -2.38) | -2.88 (-2.92, -2.85) | -2.40 (-2.43, -2.37) | works |
| kp25 | Source keeps 25% of project sales | -6.12 (-6.20, -6.06) | -7.40 (-7.49, -7.32) | -6.19 (-6.27, -6.12) | works |
| kp50 | Source keeps 50% of project sales | -12.51 (-12.67, -12.37) | -15.46 (-15.66, -15.28) | -13.11 (-13.28, -12.95) | works |
| ex50 | 50% of expired BU recycled | +6.46 (+6.34, +6.59) | +9.61 (+9.42, +9.82) | +8.32 (+8.16, +8.49) | harms |
| ex0 | 0% of expired BU recycled | +14.13 (+13.87, +14.41) | +20.54 (+20.17, +20.97) | +17.04 (+16.75, +17.37) | harms |
| fprog | outside finance: progressive income tax | -0.57 (-1.04, -0.02) | +7.45 (+6.71, +8.30) | -0.62 (-1.34, +0.19) | harms |
| fland | outside finance: land-value tax | -41.23 (-41.71, -40.79) | -49.71 (-50.30, -49.13) | -55.92 (-56.64, -55.21) | works |
| fflat | outside finance: flat wage contribution | -46.40 (-46.92, -45.92) | -56.22 (-56.94, -55.56) | -61.39 (-62.27, -60.57) | works |
| br1 | business rate 1x | -2.93 (-3.09, -2.78) | -0.58 (-0.81, -0.34) | -5.54 (-5.77, -5.29) | works |
| br15 | business rate 1.5x | -0.34 (-0.46, -0.20) | +1.96 (+1.77, +2.18) | -2.76 (-2.97, -2.54) | harms |
| br2 | business rate 2x | +2.20 (+2.10, +2.30) | +4.31 (+4.16, +4.46) | +1.00 (+0.86, +1.16) | harms |
| bu60 | 60% of the BU | -2.54 (-2.70, -2.37) | -1.95 (-2.20, -1.70) | -7.66 (-7.97, -7.35) | works |
| bu80 | 80% of the BU | +3.98 (+3.87, +4.09) | +6.03 (+5.86, +6.21) | +2.24 (+2.07, +2.42) | harms |
| mm3 | top multiplier 3 | +4.85 (+4.71, +5.01) | +8.29 (+8.07, +8.53) | +5.42 (+5.30, +5.56) | harms |
| mm6 | top multiplier 6 | +1.84 (+1.78, +1.90) | +3.20 (+3.11, +3.29) | +0.00 (+0.00, +0.00) | harms |
| mm9 | top multiplier 9 | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | -2.92 (-2.99, -2.85) | does not move |
| oc25 | octave capacity 25% | +3.72 (+3.57, +3.89) | +8.44 (+8.19, +8.71) | +9.77 (+9.55, +10.02) | harms |
| oc50 | octave capacity 50% | +3.13 (+3.00, +3.29) | +7.43 (+7.20, +7.68) | +8.91 (+8.70, +9.14) | harms |
| oc100 | octave capacity 100% | +2.48 (+2.37, +2.61) | +6.26 (+6.05, +6.49) | +8.05 (+7.86, +8.26) | harms |
| no2 | 2 octaves | -2.82 (-2.85, -2.79) | -2.90 (-2.93, -2.86) | -1.18 (-1.20, -1.17) | works |
| no4 | 4 octaves | -1.37 (-1.39, -1.35) | -1.39 (-1.41, -1.37) | +0.00 (+0.00, +0.00) | does not move |
| no6 | 6 octaves | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +1.05 (+1.03, +1.07) | harms |
| phi0 | Phi tier off | +0.54 (+0.51, +0.58) | +0.83 (+0.78, +0.89) | +2.07 (+1.99, +2.16) | harms |
| ph5 | phase-in over 5 years | -0.22 (-0.25, -0.20) | -0.20 (-0.22, -0.17) | -0.74 (-0.77, -0.71) | works |
| ph10 | phase-in over 10 years | -0.55 (-0.59, -0.50) | -0.29 (-0.35, -0.22) | -1.50 (-1.56, -1.44) | works |
| cap2 | issuance cap 2% | -5.20 (-5.36, -5.02) | -0.90 (-1.19, -0.55) | -4.51 (-4.75, -4.24) | works |
| cap4 | issuance cap 4% | -5.20 (-5.36, -5.02) | -0.90 (-1.19, -0.55) | -4.51 (-4.75, -4.24) | works |
| cap8 | issuance cap 8% | -5.20 (-5.36, -5.02) | -0.90 (-1.19, -0.55) | -4.51 (-4.75, -4.24) | works |
| ixs | indexation: surge protocol (5%) | +1.22 (+1.17, +1.26) | +2.27 (+2.19, +2.35) | +2.07 (+2.00, +2.14) | harms |
| ixy | indexation: every year, price level | +1.22 (+1.17, +1.26) | +2.27 (+2.19, +2.35) | +2.07 (+2.00, +2.14) | harms |
| ixn | indexation: every year, basic needs | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| sva | protected account, all savings | +1751.17 (+1710.28, +1796.32) | +2273.04 (+2218.62, +2332.80) | +2279.42 (+2225.26, +2339.12) | harms |
| svc | protected account, first $10,000 | +7.88 (+7.67, +8.12) | +15.36 (+14.86, +15.93) | +20.38 (+19.70, +21.12) | harms |
| rcap | rent cap for BU tenants | -1.59 (-1.64, -1.54) | -2.57 (-2.66, -2.49) | -3.13 (-3.23, -3.03) | works |
| hc | rent risk ($1.41 a BU dollar) | +13.35 (+13.15, +13.57) | +17.64 (+17.37, +17.94) | +18.07 (+17.82, +18.34) | harms |
| hcrc | rent risk and rent cap | -1.59 (-1.64, -1.54) | -2.57 (-2.66, -2.49) | -3.13 (-3.23, -3.03) | works |

### participation, mean of years 1-19, %: C2.2 design, wages 90% (lever effect, seed mean and 95% interval)

| Row | What it sets | Reference | Adverse | Stress | Verdict |
|---|---|---|---|---|---|
| asis | today's joining rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| t0 | tax 0% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| t4 | tax 4% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| t8 | tax 8% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| t12 | tax 12% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| t16 | tax 16% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| t20 | tax 20% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| t25 | tax 25% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| t30 | tax 30% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| t40 | tax 40% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t0 | tax 0%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t4 | tax 4%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t8 | tax 8%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t12 | tax 12%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t16 | tax 16%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t20 | tax 20%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t25 | tax 25%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t30 | tax 30%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| asis.t40 | tax 40%, today's rule | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| pr0c75 | progression 0 pts, cap 75% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| pr8c75 | progression 8 pts, cap 75% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| pr0c50 | progression 0 pts, cap 50% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| pr4c50 | progression 4 pts, cap 50% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| pr8c50 | progression 8 pts, cap 50% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| bt0 | business tax 0% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| bt25 | business tax 25% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| bt50 | business tax 50% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| bt75 | business tax 75% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| kp10 | Source keeps 10% of project sales | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| kp25 | Source keeps 25% of project sales | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| kp50 | Source keeps 50% of project sales | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ex50 | 50% of expired BU recycled | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ex0 | 0% of expired BU recycled | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| fprog | outside finance: progressive income tax | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| fland | outside finance: land-value tax | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| fflat | outside finance: flat wage contribution | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| br1 | business rate 1x | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| br15 | business rate 1.5x | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| br2 | business rate 2x | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| bu60 | 60% of the BU | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| bu80 | 80% of the BU | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| mm3 | top multiplier 3 | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| mm6 | top multiplier 6 | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| mm9 | top multiplier 9 | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| oc25 | octave capacity 25% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| oc50 | octave capacity 50% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| oc100 | octave capacity 100% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| no2 | 2 octaves | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| no4 | 4 octaves | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| no6 | 6 octaves | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| phi0 | Phi tier off | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ph5 | phase-in over 5 years | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ph10 | phase-in over 10 years | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| cap2 | issuance cap 2% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| cap4 | issuance cap 4% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| cap8 | issuance cap 8% | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ixs | indexation: surge protocol (5%) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ixy | indexation: every year, price level | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| ixn | indexation: every year, basic needs | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| sva | protected account, all savings | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| svc | protected account, first $10,000 | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| rcap | rent cap for BU tenants | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| hc | rent risk ($1.41 a BU dollar) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |
| hcrc | rent risk and rent cap | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | +0.00 (+0.00, +0.00) | does not move |

## The conversion tax: three break-even rates (Q21, decision rules 2 and 3)

Test reading: joining that sees what joining pays (`tNN`, released rate `base`); today's rule: `asis.tNN`, released rate `asis`. Intervals: 2.5th-97.5th percentiles over the bootstrap replicates; "beyond 40%" where fewer than 2.5% (or 97.5%) of replicates reach it; "reached" is the share of replicates that do.

| Design | Wages | Environment | Joining | Self-funding rate | Net new money at 0% / released / 40% (% of earned income) | Lowest basket poverty at | Deterrence rate (participation 5 points below its level at the released rate) | Participation at released / 40% |
|---|---|---|---|---|---|---|---|---|
| release row | 100% | Reference | test | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 64.6 / 59.7 / 48.3 | 0% (0%, 0%) | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 83.6 / 83.5 |
| release row | 100% | Reference | today's | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 64.5 / 59.9 / 48.5 | 0% (0%, 0%) | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 84.0 / 84.0 |
| release row | 100% | Adverse | test | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 78.5 / 72.7 / 59.2 | 0% (0%, 0%) | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 83.7 / 83.6 |
| release row | 100% | Adverse | today's | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 78.3 / 72.9 / 59.5 | 0% (0%, 0%) | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 84.0 / 84.0 |
| release row | 100% | Stress | test | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 34.1 / 29.5 / 23.4 | 0% (0%, 0%) | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 44.1 / 44.0 |
| release row | 100% | Stress | today's | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 34.1 / 29.5 / 23.5 | 0% (0%, 0%) | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 44.1 / 44.1 |
| release row | 90% | Reference | test | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 89.5 / 82.3 / 65.5 | 0% (0%, 0%) | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 83.7 / 83.6 |
| release row | 90% | Reference | today's | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 89.2 / 82.6 / 65.8 | 0% (0%, 0%) | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 84.0 / 84.0 |
| release row | 90% | Adverse | test | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 106.8 / 98.8 / 79.8 | 0% (0%, 0%) | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 83.8 / 83.7 |
| release row | 90% | Adverse | today's | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 106.5 / 99.1 / 80.2 | 0% (0%, 0%) | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 84.0 / 84.0 |
| release row | 90% | Stress | test | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 41.4 / 35.3 / 27.5 | 0% (0%, 0%) | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 44.1 / 44.0 |
| release row | 90% | Stress | today's | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 41.3 / 35.3 / 27.6 | 0% (0%, 0%) | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 44.1 / 44.1 |
| C2.2 design | 100% | Reference | test | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 53.2 / 51.3 / 45.1 | 0% (0%, 0%) | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 100.0 / 100.0 |
| C2.2 design | 100% | Reference | today's | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 53.2 / 51.3 / 45.1 | 0% (0%, 0%) | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 100.0 / 100.0 |
| C2.2 design | 100% | Adverse | test | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 65.7 / 63.4 / 55.9 | 0% (0%, 0%) | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 100.0 / 100.0 |
| C2.2 design | 100% | Adverse | today's | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 65.7 / 63.4 / 55.9 | 0% (0%, 0%) | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 100.0 / 100.0 |
| C2.2 design | 100% | Stress | test | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 64.5 / 61.2 / 55.3 | 0% (0%, 4%) | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 100.0 / 100.0 |
| C2.2 design | 100% | Stress | today's | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 64.5 / 61.2 / 55.3 | 0% (0%, 4%) | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 100.0 / 100.0 |
| C2.2 design | 90% | Reference | test | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 70.1 / 68.0 / 60.2 | 0% (0%, 0%) | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 100.0 / 100.0 |
| C2.2 design | 90% | Reference | today's | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 70.1 / 68.0 / 60.2 | 0% (0%, 0%) | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 100.0 / 100.0 |
| C2.2 design | 90% | Adverse | test | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 86.2 / 83.8 / 74.2 | 0% (0%, 0%) | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 100.0 / 100.0 |
| C2.2 design | 90% | Adverse | today's | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 86.2 / 83.8 / 74.2 | 0% (0%, 0%) | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 100.0 / 100.0 |
| C2.2 design | 90% | Stress | test | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 85.0 / 81.9 / 73.7 | 0% (0%, 0%) | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 100.0 / 100.0 |
| C2.2 design | 90% | Stress | today's | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 85.0 / 81.9 / 73.7 | 0% (0%, 0%) | not reached by 40% (beyond 40%, beyond 40%; reached 0%) | 100.0 / 100.0 |

### The tax sweep (seed means; basket poverty as the change against no programme)

#### release row, wages 100%

| Rate | Reference test: basket / new money / participation | Reference today's: basket / new money / participation | Adverse test: basket / new money / participation | Adverse today's: basket / new money / participation | Stress test: basket / new money / participation | Stress today's: basket / new money / participation |
|---|---|---|---|---|---|---|
| 0% | -32.15 / 64.6 / 84.3 | -32.06 / 64.5 / 84.0 | -38.52 / 78.5 / 84.3 | -38.41 / 78.3 / 84.0 | -15.29 / 34.1 / 44.2 | -15.26 / 34.1 / 44.1 |
| 4% | -31.38 / 63.0 / 84.0 | -31.40 / 63.0 / 84.0 | -37.38 / 76.6 / 84.1 | -37.36 / 76.6 / 84.0 | -14.85 / 33.2 / 44.1 | -14.83 / 33.1 / 44.1 |
| 8% | -30.62 / 61.3 / 83.8 | -30.70 / 61.5 / 84.0 | -36.26 / 74.6 / 83.9 | -36.30 / 74.8 / 84.0 | -14.43 / 32.1 / 44.1 | -14.42 / 32.1 / 44.1 |
| 12% | -29.79 / 59.7 / 83.6 | -29.97 / 59.9 / 84.0 | -35.11 / 72.7 / 83.7 | -35.23 / 72.9 / 84.0 | -14.02 / 31.1 / 44.1 | -14.01 / 31.1 / 44.1 |
| 16% | -28.94 / 58.0 / 83.4 | -29.17 / 58.4 / 84.0 | -33.99 / 70.7 / 83.5 | -34.16 / 71.1 / 84.0 | -13.62 / 30.0 / 44.1 | -13.61 / 30.0 / 44.1 |
| 20% | -28.09 / 56.3 / 83.3 | -28.34 / 56.8 / 84.0 | -32.86 / 68.9 / 83.5 | -33.04 / 69.3 / 84.0 | -13.23 / 29.0 / 44.1 | -13.23 / 29.0 / 44.1 |
| 25% | -27.01 / 54.4 / 83.2 | -27.24 / 54.8 / 84.0 | -31.48 / 66.6 / 83.4 | -31.65 / 67.0 / 84.0 | -12.76 / 27.6 / 44.0 | -12.77 / 27.6 / 44.1 |
| 30% | -26.00 / 52.5 / 83.3 | -26.17 / 52.9 / 84.0 | -30.13 / 64.3 / 83.5 | -30.28 / 64.6 / 84.0 | -12.20 / 26.2 / 44.0 | -12.20 / 26.3 / 44.1 |
| 40% | -23.94 / 48.3 / 83.5 | -24.04 / 48.5 / 84.0 | -27.71 / 59.2 / 83.6 | -27.82 / 59.5 / 84.0 | -10.88 / 23.4 / 44.0 | -10.88 / 23.5 / 44.1 |

#### release row, wages 90%

| Rate | Reference test: basket / new money / participation | Reference today's: basket / new money / participation | Adverse test: basket / new money / participation | Adverse today's: basket / new money / participation | Stress test: basket / new money / participation | Stress today's: basket / new money / participation |
|---|---|---|---|---|---|---|
| 0% | -13.92 / 89.5 / 84.3 | -13.81 / 89.2 / 84.0 | -15.90 / 106.8 / 84.3 | -15.78 / 106.5 / 84.0 | -2.56 / 41.4 / 44.2 | -2.55 / 41.3 / 44.1 |
| 4% | -12.78 / 87.1 / 84.1 | -12.72 / 87.1 / 84.0 | -14.79 / 104.1 / 84.1 | -14.74 / 104.1 / 84.0 | -2.31 / 40.1 / 44.1 | -2.31 / 40.1 / 44.1 |
| 8% | -11.67 / 84.7 / 83.9 | -11.65 / 84.8 / 84.0 | -13.77 / 101.5 / 83.9 | -13.75 / 101.6 / 84.0 | -2.12 / 38.8 / 44.1 | -2.12 / 38.8 / 44.1 |
| 12% | -10.61 / 82.3 / 83.7 | -10.65 / 82.6 / 84.0 | -12.73 / 98.8 / 83.8 | -12.74 / 99.1 / 84.0 | -1.92 / 37.4 / 44.1 | -1.92 / 37.4 / 44.1 |
| 16% | -9.57 / 79.9 / 83.6 | -9.64 / 80.4 / 84.0 | -11.81 / 96.3 / 83.7 | -11.83 / 96.7 / 84.0 | -1.75 / 36.0 / 44.1 | -1.75 / 36.0 / 44.1 |
| 20% | -8.53 / 77.6 / 83.5 | -8.62 / 78.1 / 84.0 | -10.90 / 93.8 / 83.7 | -10.93 / 94.2 / 84.0 | -1.58 / 34.6 / 44.1 | -1.58 / 34.6 / 44.1 |
| 25% | -7.31 / 74.8 / 83.5 | -7.39 / 75.3 / 84.0 | -9.84 / 90.5 / 83.7 | -9.88 / 90.9 / 84.0 | -1.35 / 32.9 / 44.0 | -1.35 / 32.9 / 44.1 |
| 30% | -6.28 / 71.9 / 83.5 | -6.34 / 72.3 / 84.0 | -8.93 / 87.0 / 83.7 | -8.96 / 87.4 / 84.0 | -1.10 / 31.1 / 44.0 | -1.09 / 31.1 / 44.1 |
| 40% | -4.63 / 65.5 / 83.6 | -4.66 / 65.8 / 84.0 | -7.13 / 79.8 / 83.7 | -7.16 / 80.2 / 84.0 | -0.41 / 27.5 / 44.0 | -0.40 / 27.6 / 44.1 |

#### C2.2 design, wages 100%

| Rate | Reference test: basket / new money / participation | Reference today's: basket / new money / participation | Adverse test: basket / new money / participation | Adverse today's: basket / new money / participation | Stress test: basket / new money / participation | Stress today's: basket / new money / participation |
|---|---|---|---|---|---|---|
| 0% | -25.80 / 53.2 / 100.0 | -25.80 / 53.2 / 100.0 | -36.73 / 65.7 / 100.0 | -36.73 / 65.7 / 100.0 | -36.39 / 64.5 / 100.0 | -36.39 / 64.5 / 100.0 |
| 4% | -25.74 / 52.6 / 100.0 | -25.74 / 52.6 / 100.0 | -36.60 / 65.0 / 100.0 | -36.60 / 65.0 / 100.0 | -36.39 / 63.7 / 100.0 | -36.39 / 63.7 / 100.0 |
| 8% | -25.64 / 51.9 / 100.0 | -25.64 / 51.9 / 100.0 | -36.40 / 64.2 / 100.0 | -36.40 / 64.2 / 100.0 | -36.19 / 63.0 / 100.0 | -36.19 / 63.0 / 100.0 |
| 12% | -25.51 / 51.3 / 100.0 | -25.51 / 51.3 / 100.0 | -36.14 / 63.4 / 100.0 | -36.14 / 63.4 / 100.0 | -35.89 / 62.3 / 100.0 | -35.89 / 62.3 / 100.0 |
| 16% | -25.33 / 50.6 / 100.0 | -25.33 / 50.6 / 100.0 | -35.84 / 62.6 / 100.0 | -35.84 / 62.6 / 100.0 | -35.50 / 61.6 / 100.0 | -35.50 / 61.6 / 100.0 |
| 20% | -25.12 / 49.8 / 100.0 | -25.12 / 49.8 / 100.0 | -35.50 / 61.7 / 100.0 | -35.50 / 61.7 / 100.0 | -35.05 / 60.8 / 100.0 | -35.05 / 60.8 / 100.0 |
| 25% | -24.84 / 48.9 / 100.0 | -24.84 / 48.9 / 100.0 | -34.95 / 60.5 / 100.0 | -34.95 / 60.5 / 100.0 | -34.38 / 59.8 / 100.0 | -34.38 / 59.8 / 100.0 |
| 30% | -24.49 / 47.8 / 100.0 | -24.49 / 47.8 / 100.0 | -34.31 / 59.2 / 100.0 | -34.31 / 59.2 / 100.0 | -33.63 / 58.6 / 100.0 | -33.63 / 58.6 / 100.0 |
| 40% | -23.58 / 45.1 / 100.0 | -23.58 / 45.1 / 100.0 | -32.66 / 55.9 / 100.0 | -32.66 / 55.9 / 100.0 | -31.63 / 55.3 / 100.0 | -31.63 / 55.3 / 100.0 |

#### C2.2 design, wages 90%

| Rate | Reference test: basket / new money / participation | Reference today's: basket / new money / participation | Adverse test: basket / new money / participation | Adverse today's: basket / new money / participation | Stress test: basket / new money / participation | Stress today's: basket / new money / participation |
|---|---|---|---|---|---|---|
| 0% | -25.27 / 70.1 / 100.0 | -25.27 / 70.1 / 100.0 | -35.59 / 86.2 / 100.0 | -35.59 / 86.2 / 100.0 | -34.34 / 85.0 / 100.0 | -34.34 / 85.0 / 100.0 |
| 4% | -25.12 / 69.4 / 100.0 | -25.12 / 69.4 / 100.0 | -35.19 / 85.5 / 100.0 | -35.19 / 85.5 / 100.0 | -34.24 / 84.3 / 100.0 | -34.24 / 84.3 / 100.0 |
| 8% | -24.90 / 68.8 / 100.0 | -24.90 / 68.8 / 100.0 | -34.63 / 84.7 / 100.0 | -34.63 / 84.7 / 100.0 | -33.55 / 83.7 / 100.0 | -33.55 / 83.7 / 100.0 |
| 12% | -24.61 / 68.0 / 100.0 | -24.61 / 68.0 / 100.0 | -33.87 / 83.8 / 100.0 | -33.87 / 83.8 / 100.0 | -32.57 / 83.0 / 100.0 | -32.57 / 83.0 / 100.0 |
| 16% | -24.24 / 67.3 / 100.0 | -24.24 / 67.3 / 100.0 | -32.98 / 82.9 / 100.0 | -32.98 / 82.9 / 100.0 | -31.46 / 82.3 / 100.0 | -31.46 / 82.3 / 100.0 |
| 20% | -23.79 / 66.4 / 100.0 | -23.79 / 66.4 / 100.0 | -31.93 / 81.9 / 100.0 | -31.93 / 81.9 / 100.0 | -30.22 / 81.5 / 100.0 | -30.22 / 81.5 / 100.0 |
| 25% | -23.11 / 65.3 / 100.0 | -23.11 / 65.3 / 100.0 | -30.37 / 80.5 / 100.0 | -30.37 / 80.5 / 100.0 | -28.46 / 80.3 / 100.0 | -28.46 / 80.3 / 100.0 |
| 30% | -22.33 / 63.9 / 100.0 | -22.33 / 63.9 / 100.0 | -28.63 / 78.8 / 100.0 | -28.63 / 78.8 / 100.0 | -26.49 / 78.7 / 100.0 | -26.49 / 78.7 / 100.0 |
| 40% | -20.34 / 60.2 / 100.0 | -20.34 / 60.2 / 100.0 | -24.88 / 74.2 / 100.0 | -24.88 / 74.2 / 100.0 | -22.43 / 73.7 / 100.0 | -22.43 / 73.7 / 100.0 |

## Stage 2: Morris screening (Q22; descriptive, no claim rests on it)

Elementary effects on the [0, 1] factor scale (the change over the full range, in points; inflation in points a year), 10 trajectories, wages 100%: mu* the mean absolute effect, sd its spread (a large sd beside mu* means the factor's effect depends on the others). Sorted by mu* on basket poverty, mean over environments.

### release row, Reference

| Factor | basket poverty mu* (mu; sd) | wealth poverty mu* (mu; sd) | participation mu* (mu; sd) | inflation mu* (mu; sd) |
|---|---|---|---|---|
| protected account (none, capped, all) | 11.40 (+11.40; 2.62) | 22.02 (-22.02; 6.56) | 0.25 (-0.25; 0.27) | 1578.89 (+1578.89; 51.38) |
| BU amount (60-100%) | 6.88 (-6.88; 1.01) | 3.99 (-2.36; 4.07) | 0.44 (+0.44; 0.29) | 69.07 (+69.07; 46.09) |
| issuance cap (none, 8, 4, 2%) | 0.85 (+0.85; 2.22) | 0.55 (+0.55; 1.52) | 0.00 (+0.00; 0.01) | 1.74 (-1.36; 4.43) |
| business rate (1-3x) | 0.77 (-0.54; 2.05) | 1.12 (-0.72; 2.97) | 0.04 (+0.04; 0.12) | 1.86 (+1.69; 4.69) |
| business base rate (0-75%) | 0.74 (+0.54; 1.28) | 0.53 (+0.25; 0.90) | 0.02 (-0.01; 0.04) | 3.42 (+1.08; 7.56) |
| rent cap (off, on) | 0.43 (-0.43; 0.09) | 0.30 (-0.30; 0.08) | 0.02 (+0.02; 0.01) | 2.89 (+2.89; 2.05) |
| indexation (surge, yearly, needs) | 0.45 (-0.45; 0.17) | 0.24 (+0.02; 0.32) | 1.40 (+1.40; 0.36) | 2.46 (+2.46; 2.35) |
| top multiplier (3-9) | 0.26 (-0.26; 0.37) | 0.15 (-0.07; 0.22) | 0.01 (+0.01; 0.01) | 0.68 (-0.07; 0.84) |
| base conversion tax (0-40%) | 0.17 (+0.17; 0.19) | 0.06 (+0.06; 0.04) | 0.16 (-0.16; 0.10) | 0.38 (+0.09; 0.45) |
| phase-in (1-10 years) | 0.19 (+0.17; 0.24) | 0.14 (-0.07; 0.21) | 0.02 (+0.00; 0.03) | 0.58 (+0.02; 0.88) |
| octave capacity (none, 100, 50, 25%) | 0.12 (+0.12; 0.18) | 0.14 (+0.14; 0.20) | 0.00 (-0.00; 0.00) | 0.24 (-0.14; 0.31) |
| number of octaves (2-6) | 0.03 (-0.02; 0.06) | 0.19 (-0.16; 0.54) | 0.00 (+0.00; 0.01) | 0.09 (+0.04; 0.17) |
| Phi tier (on, off) | 0.01 (+0.01; 0.01) | 0.01 (+0.01; 0.01) | 0.00 (-0.00; 0.00) | 0.08 (+0.06; 0.06) |
| progression (0-8 points) | 0.00 (+0.00; 0.01) | 0.01 (+0.00; 0.01) | 0.00 (-0.00; 0.00) | 0.02 (-0.00; 0.04) |
| project sales kept (0-50%) | 0.01 (-0.01; 0.01) | 0.01 (-0.01; 0.02) | 0.00 (+0.00; 0.00) | 0.19 (-0.19; 0.12) |
| progression cap (50-75%) | 0.01 (+0.01; 0.02) | 0.01 (+0.01; 0.03) | 0.00 (-0.00; 0.00) | 0.02 (+0.02; 0.06) |
| expired BU recycled (0-100%) | 0.00 (+0.00; 0.00) | 0.00 (+0.00; 0.00) | 0.00 (+0.00; 0.00) | 0.00 (+0.00; 0.00) |

### release row, Adverse

| Factor | basket poverty mu* (mu; sd) | wealth poverty mu* (mu; sd) | participation mu* (mu; sd) | inflation mu* (mu; sd) |
|---|---|---|---|---|
| protected account (none, capped, all) | 11.35 (+11.35; 3.50) | 60.83 (-60.83; 8.65) | 0.17 (-0.17; 0.27) | 1971.77 (+1971.77; 66.87) |
| BU amount (60-100%) | 7.94 (-7.94; 0.76) | 4.55 (-2.31; 5.31) | 0.42 (+0.42; 0.27) | 86.97 (+86.97; 57.41) |
| issuance cap (none, 8, 4, 2%) | 1.20 (+0.78; 2.86) | 0.60 (+0.43; 1.67) | 0.01 (+0.01; 0.02) | 6.99 (-6.99; 11.22) |
| business rate (1-3x) | 1.13 (-0.67; 2.93) | 1.56 (-1.17; 4.38) | 0.07 (+0.05; 0.19) | 5.19 (+4.89; 9.70) |
| business base rate (0-75%) | 0.95 (+0.90; 1.70) | 0.73 (+0.58; 1.23) | 0.03 (-0.02; 0.07) | 7.99 (+5.78; 20.75) |
| rent cap (off, on) | 0.35 (-0.35; 0.10) | 0.21 (-0.20; 0.16) | 0.02 (+0.02; 0.01) | 3.45 (+3.45; 2.52) |
| indexation (surge, yearly, needs) | 0.31 (-0.31; 0.16) | 0.32 (+0.13; 0.33) | 0.99 (+0.99; 0.28) | 2.59 (+2.59; 2.85) |
| top multiplier (3-9) | 0.27 (-0.27; 0.38) | 0.08 (-0.01; 0.11) | 0.01 (+0.01; 0.01) | 0.72 (-0.17; 0.85) |
| base conversion tax (0-40%) | 0.27 (+0.27; 0.23) | 0.17 (+0.07; 0.21) | 0.16 (-0.16; 0.09) | 2.42 (+2.15; 4.42) |
| phase-in (1-10 years) | 0.24 (+0.22; 0.27) | 0.17 (-0.02; 0.22) | 0.01 (+0.00; 0.03) | 1.19 (+0.58; 2.01) |
| octave capacity (none, 100, 50, 25%) | 0.18 (+0.18; 0.25) | 0.35 (+0.35; 1.06) | 0.00 (-0.00; 0.00) | 0.27 (-0.13; 0.34) |
| number of octaves (2-6) | 0.11 (-0.10; 0.30) | 0.42 (-0.41; 1.29) | 0.00 (+0.00; 0.01) | 0.14 (+0.03; 0.26) |
| Phi tier (on, off) | 0.02 (+0.02; 0.02) | 0.01 (-0.00; 0.01) | 0.00 (+0.00; 0.00) | 0.09 (+0.07; 0.07) |
| progression (0-8 points) | 0.01 (+0.01; 0.01) | 0.00 (-0.00; 0.01) | 0.00 (-0.00; 0.00) | 0.03 (+0.00; 0.05) |
| project sales kept (0-50%) | 0.01 (-0.01; 0.01) | 0.01 (-0.01; 0.02) | 0.00 (+0.00; 0.00) | 0.21 (-0.21; 0.13) |
| progression cap (50-75%) | 0.01 (+0.01; 0.02) | 0.01 (+0.01; 0.02) | 0.00 (-0.00; 0.00) | 0.03 (+0.03; 0.11) |
| expired BU recycled (0-100%) | 0.00 (+0.00; 0.00) | 0.00 (+0.00; 0.00) | 0.00 (+0.00; 0.00) | 0.00 (+0.00; 0.00) |

### release row, Stress

| Factor | basket poverty mu* (mu; sd) | wealth poverty mu* (mu; sd) | participation mu* (mu; sd) | inflation mu* (mu; sd) |
|---|---|---|---|---|
| protected account (none, capped, all) | 11.18 (+11.18; 1.76) | 34.74 (-34.74; 5.44) | 0.04 (-0.03; 0.04) | 1770.79 (+1770.79; 27.90) |
| BU amount (60-100%) | 2.99 (-2.99; 0.36) | 4.35 (+1.79; 5.10) | 0.05 (+0.04; 0.04) | 35.30 (+35.30; 24.30) |
| issuance cap (none, 8, 4, 2%) | 0.64 (+0.29; 1.42) | 0.55 (-0.55; 1.43) | 0.00 (-0.00; 0.00) | 5.28 (-5.28; 8.95) |
| business rate (1-3x) | 0.62 (-0.23; 1.33) | 0.50 (+0.47; 0.99) | 0.01 (+0.01; 0.01) | 4.56 (+3.15; 7.67) |
| business base rate (0-75%) | 0.48 (+0.46; 0.76) | 0.39 (-0.14; 0.70) | 0.00 (-0.00; 0.00) | 4.22 (+3.38; 8.77) |
| rent cap (off, on) | 0.03 (-0.03; 0.02) | 0.02 (-0.02; 0.02) | 0.00 (+0.00; 0.00) | 0.42 (+0.28; 0.62) |
| indexation (surge, yearly, needs) | 0.02 (-0.02; 0.01) | 0.07 (+0.05; 0.08) | 0.11 (+0.11; 0.03) | 0.19 (+0.19; 0.20) |
| top multiplier (3-9) | 0.18 (-0.18; 0.31) | 0.07 (+0.00; 0.09) | 0.01 (+0.01; 0.02) | 0.35 (+0.12; 0.56) |
| base conversion tax (0-40%) | 0.19 (+0.19; 0.16) | 0.10 (+0.05; 0.13) | 0.15 (-0.15; 0.08) | 2.08 (+1.90; 3.71) |
| phase-in (1-10 years) | 0.10 (+0.10; 0.09) | 0.21 (-0.17; 0.40) | 0.01 (+0.00; 0.02) | 0.87 (+0.59; 1.77) |
| octave capacity (none, 100, 50, 25%) | 0.02 (+0.02; 0.04) | 0.05 (+0.05; 0.09) | 0.00 (+0.00; 0.00) | 0.04 (-0.02; 0.06) |
| number of octaves (2-6) | 0.01 (+0.01; 0.02) | 0.02 (-0.00; 0.03) | 0.00 (+0.00; 0.01) | 0.05 (+0.02; 0.09) |
| Phi tier (on, off) | 0.02 (+0.02; 0.02) | 0.02 (+0.02; 0.02) | 0.00 (+0.00; 0.00) | 0.21 (+0.19; 0.33) |
| progression (0-8 points) | 0.01 (+0.01; 0.02) | 0.01 (-0.01; 0.03) | 0.00 (-0.00; 0.00) | 0.04 (+0.01; 0.08) |
| project sales kept (0-50%) | 0.01 (-0.01; 0.01) | 0.02 (-0.02; 0.03) | 0.00 (+0.00; 0.00) | 0.22 (-0.22; 0.16) |
| progression cap (50-75%) | 0.01 (+0.01; 0.03) | 0.00 (+0.00; 0.02) | 0.00 (-0.00; 0.00) | 0.10 (+0.10; 0.32) |
| expired BU recycled (0-100%) | 0.00 (+0.00; 0.00) | 0.00 (+0.00; 0.00) | 0.00 (+0.00; 0.00) | 0.00 (+0.00; 0.00) |

### C2.2 design, Reference

| Factor | basket poverty mu* (mu; sd) | wealth poverty mu* (mu; sd) | participation mu* (mu; sd) | inflation mu* (mu; sd) |
|---|---|---|---|---|
| BU amount (60-100%) | 6.88 (-6.88; 0.78) | 4.10 (-4.10; 1.51) | 0.00 (+0.00; 0.00) | 53.88 (+53.88; 35.04) |
| protected account (none, capped, all) | 5.24 (+5.24; 2.14) | 6.68 (-6.22; 4.00) | 0.00 (+0.00; 0.00) | 1114.99 (+1114.99; 39.39) |
| business rate (1-3x) | 0.69 (-0.56; 1.91) | 0.81 (-0.60; 2.25) | 0.00 (+0.00; 0.00) | 1.40 (+1.32; 3.50) |
| rent cap (off, on) | 0.65 (-0.65; 0.10) | 0.52 (-0.52; 0.08) | 0.00 (+0.00; 0.00) | 2.71 (+2.71; 1.89) |
| issuance cap (none, 8, 4, 2%) | 0.60 (+0.60; 1.67) | 0.53 (+0.53; 1.46) | 0.00 (+0.00; 0.00) | 1.59 (-1.31; 4.13) |
| business base rate (0-75%) | 0.60 (+0.50; 1.05) | 0.58 (+0.25; 1.01) | 0.00 (+0.00; 0.00) | 2.67 (+0.36; 5.51) |
| indexation (surge, yearly, needs) | 0.49 (-0.49; 0.17) | 0.22 (-0.22; 0.15) | 0.00 (+0.00; 0.00) | 2.46 (+2.46; 1.86) |
| top multiplier (3-9) | 0.14 (-0.14; 0.20) | 0.11 (-0.09; 0.18) | 0.00 (+0.00; 0.00) | 0.43 (+0.11; 0.59) |
| base conversion tax (0-40%) | 0.07 (+0.07; 0.10) | 0.06 (+0.06; 0.07) | 0.00 (+0.00; 0.00) | 0.24 (-0.03; 0.34) |
| phase-in (1-10 years) | 0.13 (+0.12; 0.18) | 0.04 (-0.00; 0.06) | 0.00 (+0.00; 0.00) | 0.36 (-0.22; 0.61) |
| octave capacity (none, 100, 50, 25%) | 0.06 (+0.05; 0.09) | 0.08 (+0.04; 0.11) | 0.00 (+0.00; 0.00) | 0.31 (-0.18; 0.42) |
| expired BU recycled (0-100%) | 0.09 (-0.09; 0.19) | 0.12 (-0.12; 0.23) | 0.00 (+0.00; 0.00) | 0.16 (-0.16; 0.22) |
| number of octaves (2-6) | 0.01 (+0.01; 0.02) | 0.04 (-0.03; 0.08) | 0.00 (+0.00; 0.00) | 0.17 (+0.05; 0.34) |
| Phi tier (on, off) | 0.01 (+0.01; 0.01) | 0.01 (+0.00; 0.01) | 0.00 (+0.00; 0.00) | 0.04 (+0.02; 0.04) |
| progression (0-8 points) | 0.00 (+0.00; 0.01) | 0.01 (+0.01; 0.02) | 0.00 (+0.00; 0.00) | 0.02 (-0.00; 0.04) |
| progression cap (50-75%) | 0.01 (+0.01; 0.02) | 0.01 (+0.01; 0.02) | 0.00 (+0.00; 0.00) | 0.02 (-0.02; 0.05) |
| project sales kept (0-50%) | 0.00 (-0.00; 0.00) | 0.01 (-0.01; 0.01) | 0.00 (+0.00; 0.00) | 0.15 (-0.15; 0.09) |

### C2.2 design, Adverse

| Factor | basket poverty mu* (mu; sd) | wealth poverty mu* (mu; sd) | participation mu* (mu; sd) | inflation mu* (mu; sd) |
|---|---|---|---|---|
| BU amount (60-100%) | 9.43 (-9.43; 0.99) | 6.13 (-5.21; 3.50) | 0.00 (+0.00; 0.00) | 70.71 (+70.71; 45.76) |
| protected account (none, capped, all) | 7.13 (+7.13; 3.23) | 30.12 (-30.12; 8.74) | 0.00 (+0.00; 0.00) | 1379.71 (+1379.71; 54.81) |
| business rate (1-3x) | 1.08 (-0.79; 2.95) | 1.29 (-0.93; 3.56) | 0.00 (+0.00; 0.00) | 3.55 (+3.46; 6.75) |
| rent cap (off, on) | 0.98 (-0.98; 0.17) | 0.71 (-0.71; 0.10) | 0.00 (+0.00; 0.00) | 4.36 (+4.36; 3.00) |
| issuance cap (none, 8, 4, 2%) | 0.92 (+0.66; 2.33) | 0.74 (+0.67; 2.20) | 0.00 (+0.00; 0.00) | 5.13 (-5.13; 7.96) |
| business base rate (0-75%) | 0.87 (+0.78; 1.56) | 0.72 (+0.55; 1.41) | 0.00 (+0.00; 0.00) | 5.78 (+3.45; 14.54) |
| indexation (surge, yearly, needs) | 0.76 (-0.76; 0.23) | 0.47 (-0.30; 0.41) | 0.00 (+0.00; 0.00) | 3.68 (+3.68; 2.79) |
| top multiplier (3-9) | 0.16 (-0.16; 0.23) | 0.07 (-0.03; 0.09) | 0.00 (+0.00; 0.00) | 0.44 (+0.04; 0.56) |
| base conversion tax (0-40%) | 0.18 (+0.18; 0.23) | 0.07 (+0.07; 0.06) | 0.00 (+0.00; 0.00) | 2.40 (+2.17; 5.18) |
| phase-in (1-10 years) | 0.17 (+0.15; 0.22) | 0.11 (-0.00; 0.16) | 0.00 (+0.00; 0.00) | 0.98 (+0.34; 1.82) |
| octave capacity (none, 100, 50, 25%) | 0.10 (+0.10; 0.13) | 0.23 (+0.23; 0.65) | 0.00 (+0.00; 0.00) | 0.32 (-0.15; 0.44) |
| expired BU recycled (0-100%) | 0.09 (-0.09; 0.20) | 0.08 (-0.08; 0.14) | 0.00 (+0.00; 0.00) | 0.19 (-0.19; 0.26) |
| number of octaves (2-6) | 0.06 (-0.05; 0.13) | 0.29 (-0.27; 0.81) | 0.00 (+0.00; 0.00) | 0.20 (+0.04; 0.37) |
| Phi tier (on, off) | 0.01 (+0.01; 0.01) | 0.02 (+0.02; 0.02) | 0.00 (+0.00; 0.00) | 0.04 (+0.03; 0.04) |
| progression (0-8 points) | 0.00 (+0.00; 0.01) | 0.00 (-0.00; 0.01) | 0.00 (+0.00; 0.00) | 0.03 (+0.00; 0.05) |
| progression cap (50-75%) | 0.00 (+0.00; 0.01) | 0.00 (+0.00; 0.02) | 0.00 (+0.00; 0.00) | 0.02 (-0.02; 0.06) |
| project sales kept (0-50%) | 0.00 (-0.00; 0.00) | 0.01 (-0.01; 0.02) | 0.00 (+0.00; 0.00) | 0.17 (-0.17; 0.10) |

### C2.2 design, Stress

| Factor | basket poverty mu* (mu; sd) | wealth poverty mu* (mu; sd) | participation mu* (mu; sd) | inflation mu* (mu; sd) |
|---|---|---|---|---|
| BU amount (60-100%) | 9.29 (-9.29; 0.97) | 6.08 (-5.13; 3.53) | 0.00 (+0.00; 0.00) | 72.60 (+72.60; 46.92) |
| protected account (none, capped, all) | 6.51 (+6.51; 3.33) | 32.17 (-32.17; 9.07) | 0.00 (+0.00; 0.00) | 1381.76 (+1381.76; 55.17) |
| business rate (1-3x) | 1.19 (-0.75; 3.09) | 1.29 (-1.01; 3.67) | 0.00 (+0.00; 0.00) | 5.31 (+5.20; 7.73) |
| rent cap (off, on) | 1.09 (-1.09; 0.19) | 0.79 (-0.79; 0.13) | 0.00 (+0.00; 0.00) | 4.82 (+4.82; 3.34) |
| issuance cap (none, 8, 4, 2%) | 0.94 (+0.69; 2.40) | 0.80 (+0.74; 2.42) | 0.00 (+0.00; 0.00) | 5.25 (-5.25; 8.10) |
| business base rate (0-75%) | 0.85 (+0.75; 1.51) | 0.70 (+0.54; 1.32) | 0.00 (+0.00; 0.00) | 5.72 (+3.37; 14.32) |
| indexation (surge, yearly, needs) | 0.73 (-0.73; 0.24) | 0.43 (-0.28; 0.38) | 0.00 (+0.00; 0.00) | 3.65 (+3.65; 2.74) |
| top multiplier (3-9) | 0.19 (-0.19; 0.26) | 0.07 (-0.01; 0.08) | 0.00 (+0.00; 0.00) | 0.48 (+0.15; 0.62) |
| base conversion tax (0-40%) | 0.21 (+0.21; 0.22) | 0.09 (+0.09; 0.07) | 0.00 (+0.00; 0.00) | 3.13 (+2.88; 5.64) |
| phase-in (1-10 years) | 0.15 (+0.14; 0.21) | 0.10 (-0.02; 0.17) | 0.00 (+0.00; 0.00) | 0.79 (+0.23; 1.58) |
| octave capacity (none, 100, 50, 25%) | 0.12 (+0.12; 0.15) | 0.27 (+0.26; 0.77) | 0.00 (+0.00; 0.00) | 0.34 (-0.20; 0.46) |
| expired BU recycled (0-100%) | 0.08 (-0.08; 0.18) | 0.05 (-0.05; 0.09) | 0.00 (+0.00; 0.00) | 0.27 (-0.27; 0.50) |
| number of octaves (2-6) | 0.06 (-0.05; 0.16) | 0.34 (-0.31; 1.02) | 0.00 (+0.00; 0.00) | 0.22 (+0.06; 0.44) |
| Phi tier (on, off) | 0.02 (+0.02; 0.03) | 0.02 (+0.00; 0.03) | 0.00 (+0.00; 0.00) | 0.12 (+0.01; 0.15) |
| progression (0-8 points) | 0.02 (+0.02; 0.04) | 0.01 (+0.01; 0.03) | 0.00 (+0.00; 0.00) | 0.34 (+0.29; 0.98) |
| progression cap (50-75%) | 0.01 (+0.01; 0.04) | 0.01 (+0.01; 0.03) | 0.00 (+0.00; 0.00) | 0.11 (+0.11; 0.34) |
| project sales kept (0-50%) | 0.00 (-0.00; 0.00) | 0.01 (-0.01; 0.02) | 0.00 (+0.00; 0.00) | 0.17 (-0.17; 0.11) |

## The trade-off front and the best setting (Q22, Q23, decision rule 4)

Candidates: every stage-1 row under the test reading on ordinary savings and every stage-2 row. Objectives: the mean over the three environments of the change against no programme in basket poverty and wealth poverty (lower is better), participation (higher) and programme inflation (lower, points a year). No harm: gNonF0, gNonW, secU25X, secM3X and wealth poverty at or below zero in every environment; inflation under 5 points a year in every environment.

### release row, wages 100%

435 candidates; 0 pass no harm in every environment; 0 of those keep inflation under 5 points a year. **No setting tested meets the rule.** Closest (by the summed excess of what fails): `fland` (outside finance: land-value tax: gNonW +0.74 in Reference, secU25X +0.86 in Reference, secM3X +0.94 in Reference, inflation 5.30 in Reference ...); `m6.1` (base tax 13%; progression 0.0 pts; cap 58%; business tax 0%; sales kept 17%; recycled 0%; business rate 1.0x; BU 60%; top multiplier 3.0; octave capacity not enforced; octaves 2; Phi tier on; phase-in 10 y; issuance cap 8%; indexation every year; protected account first $10,000; rent cap off: gNonW +13.15 in Reference, secU25X +0.43 in Reference, secM3X +14.09 in Reference, pov +7.92 in Reference ...); `m6.4` (base tax 13%; progression 0.0 pts; cap 58%; business tax 0%; sales kept 50%; recycled 0%; business rate 2.3x; BU 60%; top multiplier 3.0; octave capacity 50%; octaves 2; Phi tier on; phase-in 10 y; issuance cap 8%; indexation every year; protected account first $10,000; rent cap off: gNonW +13.26 in Reference, secU25X +0.40 in Reference, secM3X +14.19 in Reference, pov +8.25 in Reference ...); `m6.2` (base tax 13%; progression 0.0 pts; cap 58%; business tax 0%; sales kept 17%; recycled 0%; business rate 2.3x; BU 60%; top multiplier 3.0; octave capacity not enforced; octaves 2; Phi tier on; phase-in 10 y; issuance cap 8%; indexation every year; protected account first $10,000; rent cap off: gNonW +13.30 in Reference, secU25X +0.40 in Reference, secM3X +14.24 in Reference, pov +8.27 in Reference ...); `m6.3` (base tax 13%; progression 0.0 pts; cap 58%; business tax 0%; sales kept 17%; recycled 0%; business rate 2.3x; BU 60%; top multiplier 3.0; octave capacity 50%; octaves 2; Phi tier on; phase-in 10 y; issuance cap 8%; indexation every year; protected account first $10,000; rent cap off: gNonW +13.30 in Reference, secU25X +0.40 in Reference, secM3X +14.24 in Reference, pov +8.27 in Reference ...).

| Point | What it sets | Basket poverty | Wealth poverty | Participation | Inflation | On the front in | Fails |
|---|---|---|---|---|---|---|---|
| t0 | tax 0% | -28.65 | +24.92 | 70.9 | 49.20 | Reference, Adverse, Stress | 15: gNonW +25.42 in Reference; secU25X +0.51 in Reference; secM3X +22.00 in Reference ... |
| bt0 | business tax 0% | -28.19 | +25.39 | 70.4 | 48.88 | Reference, Adverse, Stress | 15: gNonW +27.34 in Reference; secU25X +0.70 in Reference; secM3X +23.32 in Reference ... |
| t4 | tax 4% | -27.87 | +25.49 | 70.7 | 48.47 | Reference, Adverse, Stress | 15: gNonW +26.20 in Reference; secU25X +0.53 in Reference; secM3X +22.72 in Reference ... |
| ixn | indexation: every year, basic needs | -27.15 | +26.08 | 71.7 | 47.59 | Reference, Adverse, Stress | 15: gNonW +26.04 in Reference; secU25X +0.56 in Reference; secM3X +21.75 in Reference ... |
| t8 | tax 8% | -27.10 | +26.01 | 70.6 | 47.69 | Reference, Adverse, Stress | 15: gNonW +27.01 in Reference; secU25X +0.53 in Reference; secM3X +23.43 in Reference ... |
| rcap | rent cap for BU tenants | -26.57 | +26.02 | 70.4 | 46.27 | Reference, Adverse, Stress | 15: gNonW +27.57 in Reference; secU25X +0.58 in Reference; secM3X +23.72 in Reference ... |
| pr0c75 (= pr0c50) | progression 0 pts, cap 75% | -26.39 | +25.98 | 70.7 | 46.58 | Reference, Adverse, Stress | 15: gNonW +26.87 in Reference; secU25X +0.46 in Reference; secM3X +23.52 in Reference ... |
| kp50 | Source keeps 50% of project sales | -26.21 | +25.83 | 70.5 | 45.62 | Reference, Adverse, Stress | 15: gNonW +27.04 in Reference; secU25X +0.57 in Reference; secM3X +23.59 in Reference ... |
| mm9 | top multiplier 9 | -26.16 | +26.33 | 70.5 | 46.56 | Stress | 15: gNonW +27.92 in Reference; secU25X +0.56 in Reference; secM3X +24.10 in Reference ... |
| kp25 | Source keeps 25% of project sales | -26.15 | +26.10 | 70.5 | 46.04 | Reference | 15: gNonW +27.53 in Reference; secU25X +0.56 in Reference; secM3X +23.84 in Reference ... |
| kp10 | Source keeps 10% of project sales | -26.12 | +26.25 | 70.5 | 46.28 | Reference, Adverse | 15: gNonW +27.75 in Reference; secU25X +0.56 in Reference; secM3X +23.98 in Reference ... |
| phi0 | Phi tier off | -26.05 | +26.44 | 70.5 | 46.46 | Reference, Adverse, Stress | 15: gNonW +27.94 in Reference; secU25X +0.53 in Reference; secM3X +24.12 in Reference ... |
| mm6 | top multiplier 6 | -25.82 | +26.83 | 70.5 | 46.39 | Reference, Adverse | 15: gNonW +28.34 in Reference; secU25X +0.50 in Reference; secM3X +24.33 in Reference ... |
| mm3 | top multiplier 3 | -25.29 | +27.57 | 70.6 | 46.19 | Reference, Adverse, Stress | 15: gNonW +29.13 in Reference; secU25X +0.46 in Reference; secM3X +24.71 in Reference ... |
| ex0 | 0% of expired BU recycled | -25.22 | +28.33 | 70.7 | 47.43 | Reference, Adverse | 15: gNonW +29.91 in Reference; secU25X +0.36 in Reference; secM3X +24.80 in Reference ... |
| ph5 | phase-in over 5 years | -25.05 | +25.89 | 70.5 | 44.66 | Reference, Adverse, Stress | 15: gNonW +27.38 in Reference; secU25X +0.47 in Reference; secM3X +23.39 in Reference ... |
| svc | protected account, first $10,000 | -24.98 | +7.98 | 70.5 | 56.11 | Reference, Adverse, Stress | 14: gNonW +11.00 in Reference; secU25X +0.54 in Reference; secM3X +17.46 in Reference ... |
| bt25 | business tax 25% | -24.04 | +27.73 | 70.6 | 44.47 | Reference, Adverse, Stress | 15: gNonW +28.91 in Reference; secU25X +0.50 in Reference; secM3X +24.94 in Reference ... |
| t25 | tax 25% | -23.75 | +28.03 | 70.2 | 44.11 | Reference, Stress | 15: gNonW +29.48 in Reference; secU25X +0.59 in Reference; secM3X +25.11 in Reference ... |
| ph10 | phase-in over 10 years | -23.56 | +25.26 | 70.5 | 42.23 | Reference, Adverse, Stress | 15: gNonW +27.20 in Reference; secU25X +0.42 in Reference; secM3X +22.95 in Reference ... |
| h100 | base tax 29%; progression 4.4 pts; cap 66%; business tax 19%; sales kept 25%; recycled 93%; business rate 2.9x; BU 99%; top multiplier 6.9; octave capacity 25%; octaves 5; Phi tier on; phase-in 6 y; issuance cap none; indexation surge; protected account first $10,000; rent cap on | -22.07 | +10.65 | 70.2 | 50.96 | Reference, Adverse, Stress | 14: gNonW +13.24 in Reference; secU25X +0.50 in Reference; secM3X +18.14 in Reference ... |
| bu80 | 80% of the BU | -21.06 | +27.09 | 70.7 | 39.79 | Reference, Adverse | 15: gNonW +28.28 in Reference; secU25X +0.44 in Reference; secM3X +24.82 in Reference ... |
| h10 | base tax 20%; progression 5.0 pts; cap 64%; business tax 2%; sales kept 27%; recycled 2%; business rate 2.4x; BU 84%; top multiplier 7.8; octave capacity 50%; octaves 6; Phi tier off; phase-in 2 y; issuance cap none; indexation basic needs; protected account none; rent cap off | -20.76 | +27.98 | 71.7 | 39.34 | Reference, Adverse, Stress | 15: gNonW +27.72 in Reference; secU25X +0.38 in Reference; secM3X +23.40 in Reference ... |
| h192 | base tax 27%; progression 4.8 pts; cap 60%; business tax 0%; sales kept 8%; recycled 26%; business rate 2.6x; BU 92%; top multiplier 5.2; octave capacity 25%; octaves 4; Phi tier on; phase-in 9 y; issuance cap none; indexation surge; protected account first $10,000; rent cap off | -20.64 | +10.58 | 70.6 | 48.78 | Reference, Adverse, Stress | 14: gNonW +12.50 in Reference; secU25X +0.38 in Reference; secM3X +18.16 in Reference ... |
| br2 | business rate 2x | -20.55 | +28.55 | 70.7 | 39.28 | Reference, Adverse, Stress | 15: gNonW +29.25 in Reference; secU25X +0.43 in Reference; secM3X +25.40 in Reference ... |
| h23 | base tax 23%; progression 0.5 pts; cap 69%; business tax 8%; sales kept 3%; recycled 16%; business rate 2.4x; BU 93%; top multiplier 4.3; octave capacity 100%; octaves 6; Phi tier on; phase-in 2 y; issuance cap none; indexation surge; protected account first $10,000; rent cap off | -20.33 | +12.54 | 70.6 | 49.22 | Reference, Adverse, Stress | 14: gNonW +13.45 in Reference; secU25X +0.41 in Reference; secM3X +19.66 in Reference ... |
| bt50 | business tax 50% | -19.70 | +28.86 | 70.7 | 38.31 | Reference, Adverse, Stress | 15: gNonW +29.30 in Reference; secU25X +0.42 in Reference; secM3X +25.38 in Reference ... |
| h119 | base tax 20%; progression 2.4 pts; cap 67%; business tax 20%; sales kept 7%; recycled 2%; business rate 2.0x; BU 95%; top multiplier 6.1; octave capacity 100%; octaves 4; Phi tier on; phase-in 9 y; issuance cap none; indexation basic needs; protected account none; rent cap on | -18.23 | +27.72 | 71.6 | 34.36 | Reference, Adverse, Stress | 15: gNonW +27.64 in Reference; secU25X +0.35 in Reference; secM3X +22.45 in Reference ... |
| h4 | base tax 25%; progression 3.4 pts; cap 63%; business tax 42%; sales kept 10%; recycled 67%; business rate 2.8x; BU 95%; top multiplier 3.7; octave capacity 25%; octaves 3; Phi tier on; phase-in 2 y; issuance cap none; indexation every year; protected account first $10,000; rent cap on | -18.12 | +15.51 | 70.6 | 44.65 | Reference, Adverse | 15: gNonW +14.68 in Reference; secU25X +0.41 in Reference; secM3X +20.02 in Reference ... |
| h141 | base tax 17%; progression 7.5 pts; cap 53%; business tax 0%; sales kept 37%; recycled 79%; business rate 1.9x; BU 89%; top multiplier 7.8; octave capacity 50%; octaves 2; Phi tier off; phase-in 8 y; issuance cap none; indexation surge; protected account first $10,000; rent cap off | -17.43 | +14.67 | 70.7 | 41.65 | Reference, Adverse, Stress | 15: gNonW +14.08 in Reference; secU25X +0.39 in Reference; secM3X +19.19 in Reference ... |
| h126 | base tax 17%; progression 0.4 pts; cap 55%; business tax 17%; sales kept 16%; recycled 97%; business rate 2.8x; BU 75%; top multiplier 7.9; octave capacity not enforced; octaves 4; Phi tier off; phase-in 7 y; issuance cap none; indexation every year; protected account first $10,000; rent cap off | -17.17 | +13.30 | 70.7 | 39.54 | Reference, Adverse, Stress | 15: gNonW +12.94 in Reference; secU25X +0.38 in Reference; secM3X +18.20 in Reference ... |
| bu60 | 60% of the BU | -17.14 | +24.45 | 70.7 | 31.09 | Reference, Adverse, Stress | 15: gNonW +25.66 in Reference; secU25X +0.42 in Reference; secM3X +22.98 in Reference ... |
| m9.6 | base tax 0%; progression 2.7 pts; cap 50%; business tax 25%; sales kept 17%; recycled 100%; business rate 3.0x; BU 73%; top multiplier 7.0; octave capacity 50%; octaves 2; Phi tier on; phase-in 10 y; issuance cap none; indexation basic needs; protected account first $10,000; rent cap off | -16.50 | +13.43 | 71.6 | 37.82 | Reference, Adverse, Stress | 15: gNonW +12.08 in Reference; secU25X +0.35 in Reference; secM3X +16.74 in Reference ... |
| br1 | business rate 1x | -16.18 | +26.86 | 70.7 | 30.57 | Reference, Stress | 15: gNonW +27.11 in Reference; secU25X +0.45 in Reference; secM3X +24.17 in Reference ... |
| h50 | base tax 30%; progression 4.7 pts; cap 50%; business tax 42%; sales kept 24%; recycled 96%; business rate 2.3x; BU 91%; top multiplier 7.2; octave capacity 100%; octaves 6; Phi tier off; phase-in 8 y; issuance cap none; indexation every year; protected account none; rent cap on | -16.07 | +26.38 | 70.6 | 30.13 | Reference, Adverse, Stress | 15: gNonW +26.46 in Reference; secU25X +0.38 in Reference; secM3X +22.44 in Reference ... |
| h89 | base tax 32%; progression 5.0 pts; cap 68%; business tax 2%; sales kept 17%; recycled 69%; business rate 1.7x; BU 79%; top multiplier 6.5; octave capacity 50%; octaves 3; Phi tier off; phase-in 5 y; issuance cap none; indexation surge; protected account none; rent cap on | -15.89 | +26.55 | 70.6 | 29.24 | Reference, Adverse, Stress | 15: gNonW +26.31 in Reference; secU25X +0.39 in Reference; secM3X +22.03 in Reference ... |
| h132 | base tax 16%; progression 1.3 pts; cap 53%; business tax 50%; sales kept 50%; recycled 18%; business rate 1.5x; BU 99%; top multiplier 8.3; octave capacity not enforced; octaves 3; Phi tier on; phase-in 4 y; issuance cap 2%; indexation basic needs; protected account none; rent cap off | -14.61 | +27.79 | 71.5 | 28.76 | Reference, Adverse | 15: gNonW +26.87 in Reference; secU25X +1.35 in Reference; secM3X +22.93 in Reference ... |
| h41 | base tax 18%; progression 7.3 pts; cap 65%; business tax 29%; sales kept 19%; recycled 78%; business rate 1.4x; BU 98%; top multiplier 4.6; octave capacity 25%; octaves 6; Phi tier off; phase-in 3 y; issuance cap none; indexation every year; protected account none; rent cap off | -14.48 | +27.31 | 70.7 | 28.28 | Stress | 15: gNonW +27.06 in Reference; secU25X +0.45 in Reference; secM3X +23.21 in Reference ... |
| m3.4 | base tax 13%; progression 0.0 pts; cap 75%; business tax 25%; sales kept 0%; recycled 33%; business rate 1.7x; BU 87%; top multiplier 5.0; octave capacity 25%; octaves 6; Phi tier on; phase-in 1 y; issuance cap none; indexation surge; protected account first $10,000; rent cap off | -14.46 | +18.41 | 70.7 | 34.86 | Reference, Adverse | 15: gNonW +16.20 in Reference; secU25X +0.47 in Reference; secM3X +19.71 in Reference ... |
| h154 | base tax 37%; progression 2.6 pts; cap 65%; business tax 45%; sales kept 41%; recycled 42%; business rate 2.7x; BU 75%; top multiplier 4.4; octave capacity not enforced; octaves 2; Phi tier on; phase-in 4 y; issuance cap none; indexation basic needs; protected account none; rent cap on | -14.41 | +25.77 | 71.3 | 26.92 | Reference, Adverse, Stress | 15: gNonW +24.73 in Reference; secU25X +0.38 in Reference; secM3X +20.50 in Reference ... |
| m0.0 | base tax 0%; progression 2.7 pts; cap 50%; business tax 0%; sales kept 0%; recycled 33%; business rate 1.7x; BU 73%; top multiplier 5.0; octave capacity not enforced; octaves 2; Phi tier on; phase-in 4 y; issuance cap none; indexation surge; protected account first $10,000; rent cap off | -14.39 | +17.30 | 70.7 | 33.38 | Reference, Adverse, Stress | 15: gNonW +15.18 in Reference; secU25X +0.45 in Reference; secM3X +18.68 in Reference ... |
| h138 | base tax 24%; progression 7.4 pts; cap 72%; business tax 1%; sales kept 43%; recycled 19%; business rate 2.3x; BU 60%; top multiplier 5.7; octave capacity 100%; octaves 6; Phi tier off; phase-in 6 y; issuance cap none; indexation every year; protected account first $10,000; rent cap on | -14.30 | +14.42 | 70.6 | 31.47 | Reference, Adverse, Stress | 15: gNonW +13.01 in Reference; secU25X +0.39 in Reference; secM3X +17.04 in Reference ... |
| h130 | base tax 18%; progression 4.5 pts; cap 70%; business tax 60%; sales kept 38%; recycled 44%; business rate 1.6x; BU 99%; top multiplier 8.8; octave capacity 50%; octaves 4; Phi tier on; phase-in 3 y; issuance cap 2%; indexation basic needs; protected account first $10,000; rent cap on | -14.19 | +19.63 | 71.5 | 35.58 | Reference, Adverse, Stress | 15: gNonW +16.52 in Reference; secU25X +1.02 in Reference; secM3X +19.40 in Reference ... |
| h164 | base tax 8%; progression 3.6 pts; cap 58%; business tax 28%; sales kept 36%; recycled 56%; business rate 1.3x; BU 98%; top multiplier 9.0; octave capacity 100%; octaves 2; Phi tier off; phase-in 2 y; issuance cap 4%; indexation basic needs; protected account none; rent cap on | -13.94 | +27.57 | 71.5 | 27.66 | Reference, Adverse, Stress | 15: gNonW +26.52 in Reference; secU25X +0.48 in Reference; secM3X +22.24 in Reference ... |
| h46 | base tax 27%; progression 6.8 pts; cap 70%; business tax 73%; sales kept 21%; recycled 50%; business rate 1.1x; BU 98%; top multiplier 6.0; octave capacity not enforced; octaves 3; Phi tier off; phase-in 2 y; issuance cap none; indexation basic needs; protected account first $10,000; rent cap off | -13.87 | +19.73 | 71.4 | 34.95 | Reference, Adverse, Stress | 15: gNonW +16.67 in Reference; secU25X +0.49 in Reference; secM3X +19.57 in Reference ... |
| h20 | base tax 35%; progression 2.0 pts; cap 65%; business tax 12%; sales kept 17%; recycled 58%; business rate 2.0x; BU 67%; top multiplier 6.1; octave capacity 100%; octaves 4; Phi tier on; phase-in 3 y; issuance cap none; indexation every year; protected account first $10,000; rent cap on | -13.86 | +16.50 | 70.6 | 31.38 | Stress | 15: gNonW +14.27 in Reference; secU25X +0.43 in Reference; secM3X +17.87 in Reference ... |
| h61 | base tax 39%; progression 4.0 pts; cap 70%; business tax 34%; sales kept 34%; recycled 1%; business rate 2.3x; BU 75%; top multiplier 6.9; octave capacity 50%; octaves 5; Phi tier off; phase-in 9 y; issuance cap none; indexation surge; protected account none; rent cap off | -13.78 | +24.43 | 70.5 | 25.34 | Reference, Adverse, Stress | 15: gNonW +23.97 in Reference; secU25X +0.38 in Reference; secM3X +19.97 in Reference ... |
| m7.12 | base tax 13%; progression 8.0 pts; cap 58%; business tax 75%; sales kept 50%; recycled 100%; business rate 2.3x; BU 100%; top multiplier 5.0; octave capacity 25%; octaves 6; Phi tier on; phase-in 10 y; issuance cap 2%; indexation basic needs; protected account first $10,000; rent cap on | -13.68 | +19.73 | 71.5 | 35.45 | Reference, Stress | 15: gNonW +16.39 in Reference; secU25X +0.63 in Reference; secM3X +19.37 in Reference ... |
| m1.4 (= m1.5, m1.6) | base tax 0%; progression 8.0 pts; cap 58%; business tax 25%; sales kept 0%; recycled 0%; business rate 1.0x; BU 100%; top multiplier 3.0; octave capacity 50%; octaves 2; Phi tier on; phase-in 1 y; issuance cap none; indexation basic needs; protected account first $10,000; rent cap off | -13.66 | +19.91 | 71.5 | 35.31 | Reference, Adverse, Stress | 15: gNonW +16.73 in Reference; secU25X +0.48 in Reference; secM3X +19.73 in Reference ... |
| h178 | base tax 33%; progression 0.1 pts; cap 73%; business tax 39%; sales kept 49%; recycled 99%; business rate 1.2x; BU 97%; top multiplier 8.5; octave capacity 50%; octaves 5; Phi tier off; phase-in 1 y; issuance cap 2%; indexation basic needs; protected account first $10,000; rent cap off | -13.64 | +19.49 | 71.4 | 34.36 | Reference, Adverse, Stress | 15: gNonW +16.30 in Reference; secU25X +1.04 in Reference; secM3X +19.33 in Reference ... |
| m1.7 | base tax 0%; progression 8.0 pts; cap 58%; business tax 75%; sales kept 0%; recycled 67%; business rate 1.0x; BU 100%; top multiplier 3.0; octave capacity 50%; octaves 2; Phi tier on; phase-in 7 y; issuance cap none; indexation basic needs; protected account first $10,000; rent cap off | -13.54 | +19.87 | 71.5 | 35.18 | Reference, Adverse, Stress | 15: gNonW +16.64 in Reference; secU25X +0.47 in Reference; secM3X +19.68 in Reference ... |
| m7.11 | base tax 13%; progression 8.0 pts; cap 58%; business tax 25%; sales kept 50%; recycled 100%; business rate 2.3x; BU 100%; top multiplier 5.0; octave capacity 25%; octaves 6; Phi tier on; phase-in 10 y; issuance cap 2%; indexation basic needs; protected account first $10,000; rent cap on | -13.38 | +19.75 | 71.5 | 34.91 | Reference, Adverse | 15: gNonW +16.57 in Reference; secU25X +0.45 in Reference; secM3X +19.51 in Reference ... |
| h32 | base tax 13%; progression 1.2 pts; cap 67%; business tax 63%; sales kept 20%; recycled 80%; business rate 2.8x; BU 84%; top multiplier 4.7; octave capacity 50%; octaves 4; Phi tier off; phase-in 7 y; issuance cap none; indexation every year; protected account none; rent cap on | -13.37 | +25.95 | 70.7 | 25.90 | Reference, Adverse | 15: gNonW +24.99 in Reference; secU25X +0.41 in Reference; secM3X +21.09 in Reference ... |
| h131 | base tax 3%; progression 2.0 pts; cap 50%; business tax 25%; sales kept 0%; recycled 53%; business rate 1.9x; BU 99%; top multiplier 5.5; octave capacity not enforced; octaves 2; Phi tier on; phase-in 8 y; issuance cap 4%; indexation every year; protected account none; rent cap off | -13.16 | +27.29 | 70.7 | 26.85 | Stress | 15: gNonW +26.65 in Reference; secU25X +0.46 in Reference; secM3X +22.69 in Reference ... |
| h166 | base tax 2%; progression 5.4 pts; cap 57%; business tax 60%; sales kept 40%; recycled 95%; business rate 2.0x; BU 98%; top multiplier 5.5; octave capacity 100%; octaves 4; Phi tier on; phase-in 5 y; issuance cap 4%; indexation surge; protected account none; rent cap off | -13.15 | +27.20 | 70.7 | 26.71 | Stress | 15: gNonW +26.56 in Reference; secU25X +0.46 in Reference; secM3X +22.59 in Reference ... |
| h66 | base tax 35%; progression 0.5 pts; cap 58%; business tax 13%; sales kept 47%; recycled 61%; business rate 1.2x; BU 86%; top multiplier 8.0; octave capacity not enforced; octaves 4; Phi tier on; phase-in 7 y; issuance cap none; indexation basic needs; protected account first $10,000; rent cap on | -13.15 | +18.77 | 71.3 | 31.52 | Reference, Adverse, Stress | 15: gNonW +15.61 in Reference; secU25X +0.47 in Reference; secM3X +18.43 in Reference ... |
| h102 | base tax 36%; progression 0.8 pts; cap 63%; business tax 74%; sales kept 25%; recycled 68%; business rate 1.0x; BU 90%; top multiplier 8.2; octave capacity 25%; octaves 3; Phi tier on; phase-in 4 y; issuance cap 4%; indexation basic needs; protected account none; rent cap on | -13.09 | +26.24 | 71.3 | 25.36 | Reference, Adverse, Stress | 15: gNonW +25.09 in Reference; secU25X +0.62 in Reference; secM3X +21.26 in Reference ... |
| h153 | base tax 8%; progression 5.1 pts; cap 58%; business tax 6%; sales kept 22%; recycled 48%; business rate 2.8x; BU 94%; top multiplier 3.2; octave capacity 100%; octaves 5; Phi tier off; phase-in 8 y; issuance cap 2%; indexation basic needs; protected account none; rent cap on | -13.09 | +26.90 | 71.4 | 26.29 | Reference, Adverse, Stress | 15: gNonW +25.80 in Reference; secU25X +0.45 in Reference; secM3X +22.04 in Reference ... |
| h146 | base tax 25%; progression 1.3 pts; cap 71%; business tax 62%; sales kept 49%; recycled 57%; business rate 2.4x; BU 93%; top multiplier 6.6; octave capacity 25%; octaves 5; Phi tier on; phase-in 6 y; issuance cap 2%; indexation basic needs; protected account none; rent cap on | -13.05 | +26.80 | 71.4 | 26.06 | Reference, Adverse, Stress | 15: gNonW +25.45 in Reference; secU25X +0.52 in Reference; secM3X +21.60 in Reference ... |
| h105 | base tax 1%; progression 7.9 pts; cap 65%; business tax 5%; sales kept 37%; recycled 94%; business rate 2.3x; BU 95%; top multiplier 8.5; octave capacity not enforced; octaves 6; Phi tier on; phase-in 4 y; issuance cap 8%; indexation basic needs; protected account first $10,000; rent cap on | -13.03 | +19.88 | 71.5 | 33.53 | Reference, Adverse, Stress | 15: gNonW +16.54 in Reference; secU25X +0.52 in Reference; secM3X +19.50 in Reference ... |
| fland | outside finance: land-value tax | -12.97 | +0.68 | 67.4 | 6.73 | Reference, Adverse, Stress | 13: gNonW +0.74 in Reference; secU25X +0.86 in Reference; secM3X +0.94 in Reference ... |
| h21 | base tax 16%; progression 1.4 pts; cap 51%; business tax 65%; sales kept 30%; recycled 17%; business rate 2.2x; BU 94%; top multiplier 8.0; octave capacity not enforced; octaves 2; Phi tier on; phase-in 8 y; issuance cap 4%; indexation basic needs; protected account first $10,000; rent cap on | -12.91 | +19.76 | 71.4 | 32.81 | Reference, Adverse | 15: gNonW +16.32 in Reference; secU25X +0.70 in Reference; secM3X +19.02 in Reference ... |
| h168 | base tax 27%; progression 3.1 pts; cap 75%; business tax 18%; sales kept 43%; recycled 70%; business rate 1.8x; BU 96%; top multiplier 6.5; octave capacity 25%; octaves 5; Phi tier off; phase-in 5 y; issuance cap 8%; indexation basic needs; protected account first $10,000; rent cap on | -12.75 | +19.59 | 71.4 | 32.98 | Reference, Adverse | 15: gNonW +16.24 in Reference; secU25X +0.47 in Reference; secM3X +19.13 in Reference ... |
| m3.9 (= m3.10) | base tax 13%; progression 0.0 pts; cap 75%; business tax 75%; sales kept 33%; recycled 33%; business rate 1.7x; BU 87%; top multiplier 9.0; octave capacity 25%; octaves 6; Phi tier on; phase-in 1 y; issuance cap 4%; indexation basic needs; protected account first $10,000; rent cap off | -12.69 | +19.11 | 71.4 | 31.14 | Reference, Adverse | 15: gNonW +15.68 in Reference; secU25X +1.65 in Reference; secM3X +18.56 in Reference ... |
| h47 | base tax 39%; progression 7.3 pts; cap 56%; business tax 58%; sales kept 47%; recycled 28%; business rate 2.8x; BU 92%; top multiplier 8.1; octave capacity 100%; octaves 4; Phi tier on; phase-in 8 y; issuance cap 2%; indexation surge; protected account none; rent cap on | -12.56 | +26.21 | 70.6 | 24.97 | Adverse, Stress | 15: gNonW +25.08 in Reference; secU25X +0.45 in Reference; secM3X +21.51 in Reference ... |
| m3.5 | base tax 13%; progression 0.0 pts; cap 75%; business tax 75%; sales kept 0%; recycled 33%; business rate 1.7x; BU 87%; top multiplier 5.0; octave capacity 25%; octaves 6; Phi tier on; phase-in 1 y; issuance cap none; indexation surge; protected account first $10,000; rent cap off | -12.51 | +19.15 | 70.7 | 30.74 | Reference | 15: gNonW +16.21 in Reference; secU25X +0.48 in Reference; secM3X +19.11 in Reference ... |
| h108 | base tax 12%; progression 5.3 pts; cap 72%; business tax 22%; sales kept 24%; recycled 35%; business rate 2.2x; BU 64%; top multiplier 3.1; octave capacity not enforced; octaves 2; Phi tier on; phase-in 8 y; issuance cap none; indexation basic needs; protected account first $10,000; rent cap off | -12.51 | +16.42 | 71.3 | 28.65 | Reference, Adverse, Stress | 15: gNonW +13.22 in Reference; secU25X +0.37 in Reference; secM3X +16.14 in Reference ... |
| h86 | base tax 10%; progression 0.9 pts; cap 69%; business tax 70%; sales kept 9%; recycled 50%; business rate 1.6x; BU 82%; top multiplier 6.4; octave capacity not enforced; octaves 5; Phi tier off; phase-in 2 y; issuance cap 2%; indexation surge; protected account none; rent cap on | -12.48 | +24.15 | 70.7 | 23.33 | Reference, Adverse, Stress | 15: gNonW +23.18 in Reference; secU25X +1.15 in Reference; secM3X +20.26 in Reference ... |
| m9.5 | base tax 0%; progression 2.7 pts; cap 50%; business tax 25%; sales kept 17%; recycled 100%; business rate 1.7x; BU 73%; top multiplier 7.0; octave capacity 50%; octaves 2; Phi tier on; phase-in 10 y; issuance cap none; indexation basic needs; protected account first $10,000; rent cap off | -12.23 | +17.77 | 71.4 | 28.55 | Reference, Adverse, Stress | 15: gNonW +14.60 in Reference; secU25X +0.43 in Reference; secM3X +17.05 in Reference ... |
| m9.1 | base tax 0%; progression 2.7 pts; cap 50%; business tax 25%; sales kept 17%; recycled 33%; business rate 1.7x; BU 73%; top multiplier 3.0; octave capacity not enforced; octaves 2; Phi tier on; phase-in 4 y; issuance cap none; indexation basic needs; protected account first $10,000; rent cap off | -12.18 | +18.22 | 71.4 | 29.01 | Reference, Adverse, Stress | 15: gNonW +14.99 in Reference; secU25X +0.44 in Reference; secM3X +17.38 in Reference ... |
| h71 | base tax 29%; progression 6.4 pts; cap 64%; business tax 40%; sales kept 10%; recycled 85%; business rate 1.8x; BU 87%; top multiplier 8.8; octave capacity 100%; octaves 4; Phi tier on; phase-in 3 y; issuance cap 2%; indexation basic needs; protected account none; rent cap off | -12.13 | +25.83 | 71.3 | 24.24 | Reference, Adverse, Stress | 15: gNonW +24.40 in Reference; secU25X +0.48 in Reference; secM3X +20.97 in Reference ... |
| m4.16 | base tax 40%; progression 5.3 pts; cap 75%; business tax 50%; sales kept 33%; recycled 67%; business rate 2.3x; BU 87%; top multiplier 7.0; octave capacity 50%; octaves 6; Phi tier off; phase-in 10 y; issuance cap 2%; indexation basic needs; protected account none; rent cap on | -12.04 | +25.42 | 71.2 | 23.82 | Reference, Adverse | 15: gNonW +23.75 in Reference; secU25X +0.44 in Reference; secM3X +20.43 in Reference ... |
| m9.0 | base tax 0%; progression 2.7 pts; cap 50%; business tax 25%; sales kept 17%; recycled 33%; business rate 1.7x; BU 73%; top multiplier 3.0; octave capacity not enforced; octaves 2; Phi tier on; phase-in 4 y; issuance cap none; indexation surge; protected account first $10,000; rent cap off | -11.99 | +18.13 | 70.7 | 28.45 | Reference, Stress | 15: gNonW +15.29 in Reference; secU25X +0.45 in Reference; secM3X +17.71 in Reference ... |
| h162 | base tax 12%; progression 5.6 pts; cap 62%; business tax 36%; sales kept 30%; recycled 81%; business rate 2.1x; BU 85%; top multiplier 5.7; octave capacity 100%; octaves 5; Phi tier off; phase-in 6 y; issuance cap 8%; indexation basic needs; protected account none; rent cap on | -11.95 | +25.20 | 71.3 | 23.47 | Reference, Adverse | 15: gNonW +23.68 in Reference; secU25X +0.44 in Reference; secM3X +20.31 in Reference ... |
| h40 | base tax 25%; progression 1.8 pts; cap 60%; business tax 56%; sales kept 34%; recycled 91%; business rate 2.6x; BU 67%; top multiplier 8.0; octave capacity not enforced; octaves 5; Phi tier off; phase-in 4 y; issuance cap none; indexation every year; protected account first $10,000; rent cap on | -11.83 | +16.74 | 70.6 | 27.48 | Reference, Adverse | 15: gNonW +13.44 in Reference; secU25X +0.43 in Reference; secM3X +16.98 in Reference ... |
| h30 | base tax 16%; progression 2.9 pts; cap 61%; business tax 33%; sales kept 46%; recycled 72%; business rate 1.9x; BU 85%; top multiplier 5.4; octave capacity 25%; octaves 4; Phi tier on; phase-in 2 y; issuance cap 4%; indexation surge; protected account none; rent cap on | -11.82 | +25.03 | 70.7 | 23.08 | Reference, Adverse, Stress | 15: gNonW +23.61 in Reference; secU25X +0.44 in Reference; secM3X +20.41 in Reference ... |
| h176 | base tax 3%; progression 2.8 pts; cap 52%; business tax 39%; sales kept 44%; recycled 19%; business rate 2.0x; BU 86%; top multiplier 7.7; octave capacity not enforced; octaves 3; Phi tier off; phase-in 5 y; issuance cap 4%; indexation every year; protected account none; rent cap on | -11.80 | +24.93 | 70.7 | 23.03 | Reference, Adverse, Stress | 15: gNonW +23.56 in Reference; secU25X +0.45 in Reference; secM3X +20.22 in Reference ... |
| m9.2 | base tax 0%; progression 2.7 pts; cap 50%; business tax 25%; sales kept 17%; recycled 33%; business rate 1.7x; BU 73%; top multiplier 3.0; octave capacity not enforced; octaves 2; Phi tier on; phase-in 10 y; issuance cap none; indexation basic needs; protected account first $10,000; rent cap off | -11.73 | +17.70 | 71.4 | 27.87 | Reference, Adverse, Stress | 15: gNonW +14.46 in Reference; secU25X +0.42 in Reference; secM3X +16.84 in Reference ... |
| h193 | base tax 28%; progression 5.2 pts; cap 60%; business tax 17%; sales kept 21%; recycled 28%; business rate 3.0x; BU 83%; top multiplier 3.5; octave capacity 25%; octaves 6; Phi tier off; phase-in 4 y; issuance cap 2%; indexation basic needs; protected account none; rent cap off | -11.61 | +25.32 | 71.3 | 23.29 | Reference, Adverse | 15: gNonW +23.85 in Reference; secU25X +0.46 in Reference; secM3X +20.71 in Reference ... |
| m9.3 (= m9.4) | base tax 0%; progression 2.7 pts; cap 50%; business tax 25%; sales kept 17%; recycled 33%; business rate 1.7x; BU 73%; top multiplier 3.0; octave capacity 50%; octaves 2; Phi tier on; phase-in 10 y; issuance cap none; indexation basic needs; protected account first $10,000; rent cap off | -11.60 | +17.77 | 71.4 | 27.73 | Reference, Adverse, Stress | 15: gNonW +14.44 in Reference; secU25X +0.41 in Reference; secM3X +16.75 in Reference ... |
| h113 | base tax 18%; progression 5.5 pts; cap 66%; business tax 46%; sales kept 3%; recycled 55%; business rate 1.7x; BU 74%; top multiplier 7.2; octave capacity 100%; octaves 4; Phi tier on; phase-in 6 y; issuance cap none; indexation basic needs; protected account first $10,000; rent cap off | -11.40 | +18.19 | 71.3 | 27.10 | Reference, Adverse, Stress | 15: gNonW +14.75 in Reference; secU25X +0.46 in Reference; secM3X +17.33 in Reference ... |
| h14 | base tax 1%; progression 1.6 pts; cap 60%; business tax 7%; sales kept 28%; recycled 73%; business rate 1.5x; BU 85%; top multiplier 7.6; octave capacity 100%; octaves 2; Phi tier off; phase-in 9 y; issuance cap 2%; indexation basic needs; protected account first $10,000; rent cap on | -11.35 | +19.22 | 71.4 | 28.71 | Reference, Stress | 15: gNonW +15.78 in Reference; secU25X +0.47 in Reference; secM3X +17.95 in Reference ... |
| h129 | base tax 15%; progression 4.5 pts; cap 70%; business tax 30%; sales kept 16%; recycled 8%; business rate 2.9x; BU 80%; top multiplier 4.5; octave capacity 25%; octaves 5; Phi tier on; phase-in 1 y; issuance cap 2%; indexation every year; protected account none; rent cap off | -11.30 | +25.04 | 70.7 | 22.61 | Adverse | 15: gNonW +23.56 in Reference; secU25X +0.55 in Reference; secM3X +20.94 in Reference ... |
| h182 | base tax 14%; progression 1.0 pts; cap 63%; business tax 44%; sales kept 5%; recycled 20%; business rate 1.3x; BU 71%; top multiplier 4.2; octave capacity not enforced; octaves 3; Phi tier off; phase-in 3 y; issuance cap none; indexation surge; protected account none; rent cap on | -11.12 | +22.40 | 70.7 | 20.29 | Reference, Adverse, Stress | 15: gNonW +20.64 in Reference; secU25X +0.41 in Reference; secM3X +18.27 in Reference ... |
| h25 | base tax 19%; progression 6.2 pts; cap 68%; business tax 56%; sales kept 39%; recycled 89%; business rate 1.8x; BU 70%; top multiplier 6.5; octave capacity 100%; octaves 6; Phi tier off; phase-in 3 y; issuance cap none; indexation basic needs; protected account first $10,000; rent cap off | -11.04 | +16.83 | 71.2 | 25.77 | Reference, Adverse | 15: gNonW +13.31 in Reference; secU25X +0.44 in Reference; secM3X +16.61 in Reference ... |
| h26 | base tax 4%; progression 7.6 pts; cap 67%; business tax 34%; sales kept 14%; recycled 31%; business rate 1.4x; BU 76%; top multiplier 8.3; octave capacity 50%; octaves 3; Phi tier off; phase-in 1 y; issuance cap 2%; indexation basic needs; protected account none; rent cap on | -10.96 | +23.35 | 71.3 | 20.81 | Reference, Adverse, Stress | 15: gNonW +20.94 in Reference; secU25X +0.43 in Reference; secM3X +18.23 in Reference ... |
| m3.2 | base tax 13%; progression 0.0 pts; cap 75%; business tax 25%; sales kept 0%; recycled 33%; business rate 1.7x; BU 60%; top multiplier 5.0; octave capacity 100%; octaves 6; Phi tier on; phase-in 1 y; issuance cap none; indexation surge; protected account first $10,000; rent cap off | -10.92 | +15.77 | 70.7 | 24.65 | Reference, Adverse | 15: gNonW +13.38 in Reference; secU25X +0.45 in Reference; secM3X +16.24 in Reference ... |
| h123 | base tax 13%; progression 7.9 pts; cap 66%; business tax 44%; sales kept 6%; recycled 45%; business rate 2.5x; BU 81%; top multiplier 3.4; octave capacity 25%; octaves 2; Phi tier on; phase-in 3 y; issuance cap 8%; indexation basic needs; protected account first $10,000; rent cap on | -10.79 | +19.03 | 71.3 | 27.29 | Reference, Adverse | 15: gNonW +15.61 in Reference; secU25X +0.45 in Reference; secM3X +17.64 in Reference ... |
| m3.3 | base tax 13%; progression 0.0 pts; cap 75%; business tax 25%; sales kept 0%; recycled 33%; business rate 1.7x; BU 60%; top multiplier 5.0; octave capacity 25%; octaves 6; Phi tier on; phase-in 1 y; issuance cap none; indexation surge; protected account first $10,000; rent cap off | -10.76 | +16.65 | 70.7 | 24.45 | Reference, Adverse, Stress | 15: gNonW +13.64 in Reference; secU25X +0.45 in Reference; secM3X +16.23 in Reference ... |
| m3.0 (= m3.1) | base tax 13%; progression 0.0 pts; cap 58%; business tax 25%; sales kept 0%; recycled 33%; business rate 1.7x; BU 60%; top multiplier 5.0; octave capacity 100%; octaves 3; Phi tier on; phase-in 1 y; issuance cap none; indexation surge; protected account first $10,000; rent cap off | -10.68 | +17.07 | 70.7 | 24.40 | Reference, Adverse, Stress | 15: gNonW +14.08 in Reference; secU25X +0.45 in Reference; secM3X +16.30 in Reference ... |
| m1.1 | base tax 0%; progression 2.7 pts; cap 58%; business tax 25%; sales kept 0%; recycled 0%; business rate 1.0x; BU 73%; top multiplier 3.0; octave capacity not enforced; octaves 2; Phi tier on; phase-in 1 y; issuance cap none; indexation basic needs; protected account first $10,000; rent cap off | -10.55 | +18.53 | 71.3 | 25.54 | Reference, Adverse, Stress | 15: gNonW +15.07 in Reference; secU25X +0.46 in Reference; secM3X +17.03 in Reference ... |
| m1.2 | base tax 0%; progression 8.0 pts; cap 58%; business tax 25%; sales kept 0%; recycled 0%; business rate 1.0x; BU 73%; top multiplier 3.0; octave capacity not enforced; octaves 2; Phi tier on; phase-in 1 y; issuance cap none; indexation basic needs; protected account first $10,000; rent cap off | -10.54 | +18.53 | 71.3 | 25.52 | Reference, Adverse, Stress | 15: gNonW +15.07 in Reference; secU25X +0.46 in Reference; secM3X +17.02 in Reference ... |
| h53 | base tax 24%; progression 2.2 pts; cap 67%; business tax 70%; sales kept 25%; recycled 43%; business rate 1.1x; BU 71%; top multiplier 6.7; octave capacity 100%; octaves 2; Phi tier off; phase-in 3 y; issuance cap 8%; indexation every year; protected account none; rent cap off | -10.47 | +22.16 | 70.6 | 19.53 | Adverse, Stress | 15: gNonW +20.15 in Reference; secU25X +0.64 in Reference; secM3X +17.78 in Reference ... |
| h34 | base tax 7%; progression 1.5 pts; cap 66%; business tax 68%; sales kept 2%; recycled 42%; business rate 2.3x; BU 79%; top multiplier 8.0; octave capacity 25%; octaves 5; Phi tier on; phase-in 9 y; issuance cap 2%; indexation basic needs; protected account first $10,000; rent cap off | -10.46 | +19.06 | 71.3 | 26.73 | Reference, Adverse | 15: gNonW +15.58 in Reference; secU25X +0.46 in Reference; secM3X +17.34 in Reference ... |
| m1.0 | base tax 0%; progression 2.7 pts; cap 58%; business tax 25%; sales kept 0%; recycled 0%; business rate 1.0x; BU 73%; top multiplier 3.0; octave capacity not enforced; octaves 2; Phi tier on; phase-in 1 y; issuance cap none; indexation surge; protected account first $10,000; rent cap off | -10.40 | +18.40 | 70.7 | 25.11 | Reference, Adverse, Stress | 15: gNonW +15.32 in Reference; secU25X +0.47 in Reference; secM3X +17.12 in Reference ... |
| h8 | base tax 10%; progression 0.6 pts; cap 58%; business tax 54%; sales kept 26%; recycled 59%; business rate 2.8x; BU 75%; top multiplier 5.1; octave capacity 25%; octaves 3; Phi tier on; phase-in 3 y; issuance cap 4%; indexation every year; protected account none; rent cap on | -10.39 | +22.79 | 70.7 | 19.92 | Reference, Adverse, Stress | 15: gNonW +20.66 in Reference; secU25X +0.41 in Reference; secM3X +18.02 in Reference ... |
| m1.3 | base tax 0%; progression 8.0 pts; cap 58%; business tax 25%; sales kept 0%; recycled 0%; business rate 1.0x; BU 73%; top multiplier 3.0; octave capacity 50%; octaves 2; Phi tier on; phase-in 1 y; issuance cap none; indexation basic needs; protected account first $10,000; rent cap off | -10.36 | +18.61 | 71.3 | 25.26 | Reference, Adverse, Stress | 15: gNonW +15.22 in Reference; secU25X +0.46 in Reference; secM3X +16.93 in Reference ... |
| h74 | base tax 12%; progression 1.5 pts; cap 62%; business tax 69%; sales kept 18%; recycled 12%; business rate 2.3x; BU 69%; top multiplier 8.4; octave capacity 25%; octaves 4; Phi tier off; phase-in 3 y; issuance cap 4%; indexation surge; protected account none; rent cap off | -10.33 | +22.11 | 70.7 | 19.47 | Reference, Adverse, Stress | 15: gNonW +19.99 in Reference; secU25X +0.97 in Reference; secM3X +17.66 in Reference ... |
| h114 | base tax 0%; progression 2.1 pts; cap 55%; business tax 12%; sales kept 35%; recycled 17%; business rate 2.4x; BU 73%; top multiplier 7.9; octave capacity 100%; octaves 3; Phi tier off; phase-in 8 y; issuance cap 2%; indexation surge; protected account none; rent cap on | -10.29 | +22.47 | 70.7 | 19.57 | Reference, Adverse, Stress | 15: gNonW +20.26 in Reference; secU25X +0.41 in Reference; secM3X +17.82 in Reference ... |
| m7.5 | base tax 13%; progression 8.0 pts; cap 58%; business tax 25%; sales kept 17%; recycled 33%; business rate 1.0x; BU 73%; top multiplier 5.0; octave capacity 25%; octaves 3; Phi tier on; phase-in 4 y; issuance cap 2%; indexation basic needs; protected account first $10,000; rent cap on | -10.26 | +18.45 | 71.3 | 24.93 | Reference, Adverse, Stress | 15: gNonW +15.04 in Reference; secU25X +0.52 in Reference; secM3X +16.60 in Reference ... |
| h167 | base tax 38%; progression 0.5 pts; cap 59%; business tax 74%; sales kept 35%; recycled 81%; business rate 2.0x; BU 72%; top multiplier 4.2; octave capacity 50%; octaves 5; Phi tier on; phase-in 7 y; issuance cap 8%; indexation basic needs; protected account none; rent cap off | -10.15 | +22.38 | 71.1 | 19.69 | Reference, Adverse | 15: gNonW +19.91 in Reference; secU25X +0.48 in Reference; secM3X +17.55 in Reference ... |
| sva | protected account, all savings | -10.13 | -11.02 | 70.7 | 1243.11 | Reference, Adverse, Stress | 4: inflation 1118.30 in Reference; inflation 1389.58 in Adverse; gNonF0 +3.67 in Stress ... |
| m2.0 | base tax 0%; progression 0.0 pts; cap 58%; business tax 0%; sales kept 17%; recycled 33%; business rate 1.0x; BU 73%; top multiplier 3.0; octave capacity not enforced; octaves 2; Phi tier on; phase-in 1 y; issuance cap 8%; indexation every year; protected account none; rent cap off | -10.12 | +22.45 | 70.7 | 19.48 | Adverse, Stress | 15: gNonW +20.26 in Reference; secU25X +0.42 in Reference; secM3X +17.75 in Reference ... |
| m2.1 (= m2.2, m2.3) | base tax 0%; progression 0.0 pts; cap 58%; business tax 0%; sales kept 17%; recycled 33%; business rate 1.0x; BU 73%; top multiplier 3.0; octave capacity not enforced; octaves 2; Phi tier off; phase-in 1 y; issuance cap 8%; indexation every year; protected account none; rent cap off | -10.11 | +22.45 | 70.7 | 19.48 | Adverse, Stress | 15: gNonW +20.26 in Reference; secU25X +0.41 in Reference; secM3X +17.77 in Reference ... |
| m2.4 | base tax 0%; progression 5.3 pts; cap 75%; business tax 0%; sales kept 17%; recycled 33%; business rate 1.0x; BU 73%; top multiplier 3.0; octave capacity not enforced; octaves 2; Phi tier off; phase-in 1 y; issuance cap 2%; indexation every year; protected account none; rent cap off | -10.11 | +22.45 | 70.7 | 19.48 | Stress | 15: gNonW +20.26 in Reference; secU25X +0.41 in Reference; secM3X +17.77 in Reference ... |
| m2.5 | base tax 0%; progression 5.3 pts; cap 75%; business tax 0%; sales kept 17%; recycled 33%; business rate 1.0x; BU 73%; top multiplier 3.0; octave capacity not enforced; octaves 2; Phi tier off; phase-in 7 y; issuance cap 2%; indexation every year; protected account none; rent cap off | -10.07 | +22.45 | 70.7 | 19.47 | Adverse, Stress | 15: gNonW +20.27 in Reference; secU25X +0.41 in Reference; secM3X +17.76 in Reference ... |
| h177 | base tax 35%; progression 1.1 pts; cap 63%; business tax 31%; sales kept 23%; recycled 6%; business rate 1.5x; BU 71%; top multiplier 5.3; octave capacity 100%; octaves 2; Phi tier off; phase-in 8 y; issuance cap 2%; indexation every year; protected account none; rent cap on | -10.00 | +21.97 | 70.6 | 18.96 | Adverse | 15: gNonW +19.58 in Reference; secU25X +0.40 in Reference; secM3X +17.29 in Reference ... |
| h83 | base tax 28%; progression 2.8 pts; cap 62%; business tax 49%; sales kept 30%; recycled 21%; business rate 1.5x; BU 66%; top multiplier 6.3; octave capacity 100%; octaves 5; Phi tier off; phase-in 7 y; issuance cap none; indexation surge; protected account first $10,000; rent cap off | -9.95 | +16.46 | 70.6 | 23.20 | Reference, Adverse | 15: gNonW +13.53 in Reference; secU25X +0.43 in Reference; secM3X +15.77 in Reference ... |
| m7.6 (= m7.7) | base tax 13%; progression 8.0 pts; cap 58%; business tax 25%; sales kept 17%; recycled 33%; business rate 2.3x; BU 73%; top multiplier 5.0; octave capacity 25%; octaves 3; Phi tier on; phase-in 4 y; issuance cap 2%; indexation basic needs; protected account first $10,000; rent cap on | -9.91 | +18.51 | 71.3 | 24.67 | Reference, Adverse | 15: gNonW +15.07 in Reference; secU25X +0.44 in Reference; secM3X +16.62 in Reference ... |
| m7.9 | base tax 13%; progression 8.0 pts; cap 58%; business tax 25%; sales kept 50%; recycled 100%; business rate 2.3x; BU 73%; top multiplier 5.0; octave capacity 25%; octaves 3; Phi tier on; phase-in 10 y; issuance cap 2%; indexation basic needs; protected account first $10,000; rent cap on | -9.89 | +18.43 | 71.3 | 24.56 | Reference, Adverse | 15: gNonW +15.01 in Reference; secU25X +0.43 in Reference; secM3X +16.44 in Reference ... |
| m7.8 | base tax 13%; progression 8.0 pts; cap 58%; business tax 25%; sales kept 17%; recycled 100%; business rate 2.3x; BU 73%; top multiplier 5.0; octave capacity 25%; octaves 3; Phi tier on; phase-in 10 y; issuance cap 2%; indexation basic needs; protected account first $10,000; rent cap on | -9.88 | +18.45 | 71.3 | 24.60 | none | 15: gNonW +15.06 in Reference; secU25X +0.43 in Reference; secM3X +16.49 in Reference ... |
| m7.10 | base tax 13%; progression 8.0 pts; cap 58%; business tax 25%; sales kept 50%; recycled 100%; business rate 2.3x; BU 73%; top multiplier 5.0; octave capacity 25%; octaves 6; Phi tier on; phase-in 10 y; issuance cap 2%; indexation basic needs; protected account first $10,000; rent cap on | -9.88 | +18.44 | 71.3 | 24.55 | Reference, Adverse | 15: gNonW +15.01 in Reference; secU25X +0.44 in Reference; secM3X +16.42 in Reference ... |
| h142 | base tax 33%; progression 3.0 pts; cap 59%; business tax 39%; sales kept 31%; recycled 55%; business rate 1.0x; BU 68%; top multiplier 8.9; octave capacity 50%; octaves 2; Phi tier on; phase-in 9 y; issuance cap 8%; indexation every year; protected account none; rent cap off | -9.87 | +21.25 | 70.6 | 18.34 | Adverse, Stress | 15: gNonW +19.12 in Reference; secU25X +0.53 in Reference; secM3X +16.78 in Reference ... |
| h101 | base tax 29%; progression 6.8 pts; cap 71%; business tax 72%; sales kept 1%; recycled 30%; business rate 1.9x; BU 64%; top multiplier 6.8; octave capacity not enforced; octaves 3; Phi tier on; phase-in 4 y; issuance cap 2%; indexation basic needs; protected account none; rent cap on | -9.73 | +20.83 | 71.1 | 18.00 | Reference, Adverse | 15: gNonW +18.31 in Reference; secU25X +0.59 in Reference; secM3X +16.20 in Reference ... |
| m8.0 | base tax 0%; progression 0.0 pts; cap 50%; business tax 25%; sales kept 0%; recycled 33%; business rate 1.7x; BU 73%; top multiplier 5.0; octave capacity 100%; octaves 2; Phi tier on; phase-in 4 y; issuance cap 8%; indexation every year; protected account first $10,000; rent cap off | -9.62 | +18.35 | 70.7 | 24.10 | Adverse | 15: gNonW +15.30 in Reference; secU25X +0.46 in Reference; secM3X +16.62 in Reference ... |
| h122 | base tax 11%; progression 7.5 pts; cap 50%; business tax 51%; sales kept 31%; recycled 82%; business rate 1.1x; BU 67%; top multiplier 7.7; octave capacity 25%; octaves 4; Phi tier on; phase-in 6 y; issuance cap 4%; indexation every year; protected account first $10,000; rent cap off | -9.58 | +17.65 | 70.7 | 22.89 | Adverse | 15: gNonW +14.47 in Reference; secU25X +0.73 in Reference; secM3X +15.92 in Reference ... |
| h67 | base tax 24%; progression 2.4 pts; cap 55%; business tax 3%; sales kept 15%; recycled 37%; business rate 2.2x; BU 64%; top multiplier 9.0; octave capacity not enforced; octaves 6; Phi tier on; phase-in 2 y; issuance cap 4%; indexation basic needs; protected account none; rent cap on | -9.52 | +21.19 | 71.1 | 17.87 | Reference, Adverse | 15: gNonW +18.77 in Reference; secU25X +0.48 in Reference; secM3X +16.82 in Reference ... |
| h92 | base tax 7%; progression 5.5 pts; cap 62%; business tax 47%; sales kept 23%; recycled 10%; business rate 1.2x; BU 63%; top multiplier 3.4; octave capacity 50%; octaves 5; Phi tier off; phase-in 9 y; issuance cap none; indexation basic needs; protected account first $10,000; rent cap on | -9.49 | +16.64 | 71.2 | 22.00 | Reference, Adverse, Stress | 15: gNonW +13.13 in Reference; secU25X +0.42 in Reference; secM3X +14.94 in Reference ... |
| h137 | base tax 26%; progression 3.4 pts; cap 52%; business tax 69%; sales kept 27%; recycled 75%; business rate 1.5x; BU 61%; top multiplier 8.1; octave capacity not enforced; octaves 2; Phi tier off; phase-in 9 y; issuance cap none; indexation basic needs; protected account first $10,000; rent cap on | -9.44 | +16.88 | 71.1 | 21.72 | Reference, Adverse | 15: gNonW +13.22 in Reference; secU25X +0.42 in Reference; secM3X +14.82 in Reference ... |
| h98 | base tax 17%; progression 1.4 pts; cap 68%; business tax 23%; sales kept 21%; recycled 40%; business rate 1.5x; BU 67%; top multiplier 8.2; octave capacity 50%; octaves 4; Phi tier on; phase-in 4 y; issuance cap 2%; indexation every year; protected account none; rent cap off | -9.38 | +21.12 | 70.7 | 17.85 | Reference | 15: gNonW +18.76 in Reference; secU25X +0.44 in Reference; secM3X +16.63 in Reference ... |
| h28 | base tax 26%; progression 7.2 pts; cap 52%; business tax 62%; sales kept 14%; recycled 52%; business rate 2.2x; BU 62%; top multiplier 3.1; octave capacity 100%; octaves 6; Phi tier on; phase-in 7 y; issuance cap none; indexation surge; protected account none; rent cap off | -9.02 | +20.19 | 70.6 | 17.22 | Reference, Adverse | 15: gNonW +17.55 in Reference; secU25X +0.36 in Reference; secM3X +15.55 in Reference ... |
| h160 | base tax 34%; progression 4.2 pts; cap 74%; business tax 38%; sales kept 23%; recycled 88%; business rate 2.7x; BU 65%; top multiplier 3.1; octave capacity 50%; octaves 3; Phi tier off; phase-in 7 y; issuance cap 8%; indexation surge; protected account none; rent cap off | -9.01 | +20.63 | 70.5 | 17.21 | Reference, Adverse | 15: gNonW +18.00 in Reference; secU25X +0.37 in Reference; secM3X +15.97 in Reference ... |
| m4.2 (= m4.3) | base tax 13%; progression 0.0 pts; cap 58%; business tax 0%; sales kept 0%; recycled 0%; business rate 1.0x; BU 60%; top multiplier 3.0; octave capacity not enforced; octaves 3; Phi tier on; phase-in 4 y; issuance cap 2%; indexation surge; protected account none; rent cap on | -8.94 | +19.16 | 70.7 | 16.16 | Reference, Adverse, Stress | 15: gNonW +16.54 in Reference; secU25X +0.41 in Reference; secM3X +14.92 in Reference ... |
| m4.4 | base tax 13%; progression 0.0 pts; cap 75%; business tax 0%; sales kept 0%; recycled 0%; business rate 1.0x; BU 60%; top multiplier 3.0; octave capacity not enforced; octaves 3; Phi tier off; phase-in 4 y; issuance cap 2%; indexation surge; protected account none; rent cap on | -8.90 | +19.17 | 70.7 | 16.11 | Reference, Adverse, Stress | 15: gNonW +16.46 in Reference; secU25X +0.38 in Reference; secM3X +14.91 in Reference ... |
| h147 | base tax 7%; progression 1.0 pts; cap 51%; business tax 75%; sales kept 7%; recycled 73%; business rate 1.4x; BU 62%; top multiplier 5.8; octave capacity not enforced; octaves 4; Phi tier on; phase-in 5 y; issuance cap 2%; indexation basic needs; protected account none; rent cap off | -8.82 | +19.92 | 71.2 | 16.52 | Reference, Adverse, Stress | 15: gNonW +17.00 in Reference; secU25X +0.36 in Reference; secM3X +15.07 in Reference ... |
| h81 | base tax 14%; progression 3.9 pts; cap 59%; business tax 66%; sales kept 35%; recycled 38%; business rate 2.6x; BU 61%; top multiplier 5.3; octave capacity 50%; octaves 6; Phi tier off; phase-in 3 y; issuance cap 4%; indexation basic needs; protected account none; rent cap on | -8.81 | +19.66 | 71.1 | 16.31 | Reference, Adverse, Stress | 15: gNonW +16.94 in Reference; secU25X +0.36 in Reference; secM3X +14.97 in Reference ... |
| m9.12 | base tax 0%; progression 8.0 pts; cap 67%; business tax 25%; sales kept 50%; recycled 100%; business rate 3.0x; BU 100%; top multiplier 7.0; octave capacity 50%; octaves 2; Phi tier off; phase-in 10 y; issuance cap none; indexation basic needs; protected account all savings; rent cap off | -8.77 | -9.97 | 71.5 | 1246.70 | Reference, Adverse, Stress | 4: inflation 1123.64 in Reference; inflation 1397.95 in Adverse; gNonF0 +4.06 in Stress ... |
| m5.6 | base tax 13%; progression 2.7 pts; cap 67%; business tax 25%; sales kept 17%; recycled 67%; business rate 1.7x; BU 60%; top multiplier 7.0; octave capacity 100%; octaves 2; Phi tier on; phase-in 10 y; issuance cap 8%; indexation basic needs; protected account none; rent cap on | -8.74 | +19.52 | 71.1 | 16.12 | Reference, Adverse | 15: gNonW +16.56 in Reference; secU25X +0.37 in Reference; secM3X +14.86 in Reference ... |
| m5.7 | base tax 13%; progression 8.0 pts; cap 67%; business tax 25%; sales kept 17%; recycled 67%; business rate 1.7x; BU 60%; top multiplier 7.0; octave capacity 100%; octaves 2; Phi tier on; phase-in 10 y; issuance cap 8%; indexation basic needs; protected account none; rent cap on | -8.74 | +19.51 | 71.1 | 16.12 | Reference, Adverse, Stress | 15: gNonW +16.56 in Reference; secU25X +0.36 in Reference; secM3X +14.85 in Reference ... |
| m5.4 (= m5.5) | base tax 13%; progression 2.7 pts; cap 50%; business tax 25%; sales kept 17%; recycled 67%; business rate 1.7x; BU 60%; top multiplier 3.0; octave capacity 100%; octaves 2; Phi tier on; phase-in 10 y; issuance cap 8%; indexation basic needs; protected account none; rent cap on | -8.64 | +19.38 | 71.1 | 16.01 | Reference, Adverse, Stress | 15: gNonW +16.38 in Reference; secU25X +0.33 in Reference; secM3X +14.71 in Reference ... |
| m5.3 | base tax 13%; progression 2.7 pts; cap 50%; business tax 25%; sales kept 17%; recycled 67%; business rate 1.7x; BU 60%; top multiplier 3.0; octave capacity 100%; octaves 2; Phi tier on; phase-in 4 y; issuance cap 8%; indexation basic needs; protected account none; rent cap on | -8.62 | +19.39 | 71.1 | 15.96 | Reference, Adverse, Stress | 15: gNonW +16.31 in Reference; secU25X +0.32 in Reference; secM3X +14.62 in Reference ... |
| m4.6 | base tax 40%; progression 0.0 pts; cap 75%; business tax 0%; sales kept 0%; recycled 0%; business rate 1.0x; BU 60%; top multiplier 3.0; octave capacity not enforced; octaves 6; Phi tier off; phase-in 4 y; issuance cap 2%; indexation surge; protected account none; rent cap on | -8.62 | +19.00 | 70.5 | 15.79 | Reference, Adverse, Stress | 15: gNonW +16.23 in Reference; secU25X +0.34 in Reference; secM3X +14.61 in Reference ... |
| m4.5 | base tax 40%; progression 0.0 pts; cap 75%; business tax 0%; sales kept 0%; recycled 0%; business rate 1.0x; BU 60%; top multiplier 3.0; octave capacity not enforced; octaves 3; Phi tier off; phase-in 4 y; issuance cap 2%; indexation surge; protected account none; rent cap on | -8.60 | +19.01 | 70.5 | 15.78 | Reference, Adverse, Stress | 15: gNonW +16.20 in Reference; secU25X +0.34 in Reference; secM3X +14.62 in Reference ... |
| m5.2 | base tax 13%; progression 2.7 pts; cap 50%; business tax 25%; sales kept 17%; recycled 67%; business rate 1.7x; BU 60%; top multiplier 3.0; octave capacity 100%; octaves 2; Phi tier on; phase-in 4 y; issuance cap 8%; indexation basic needs; protected account none; rent cap off | -8.49 | +19.45 | 71.1 | 15.95 | Reference, Adverse | 15: gNonW +16.36 in Reference; secU25X +0.33 in Reference; secM3X +14.69 in Reference ... |
| h158 | base tax 32%; progression 0.1 pts; cap 58%; business tax 46%; sales kept 41%; recycled 66%; business rate 2.3x; BU 62%; top multiplier 3.0; octave capacity 100%; octaves 2; Phi tier on; phase-in 4 y; issuance cap 2%; indexation basic needs; protected account first $10,000; rent cap on | -8.48 | +17.09 | 71.1 | 20.64 | Reference, Adverse | 15: gNonW +13.46 in Reference; secU25X +0.40 in Reference; secM3X +14.48 in Reference ... |
| m4.12 | base tax 40%; progression 5.3 pts; cap 75%; business tax 50%; sales kept 33%; recycled 67%; business rate 2.3x; BU 60%; top multiplier 3.0; octave capacity 50%; octaves 6; Phi tier off; phase-in 4 y; issuance cap 2%; indexation surge; protected account none; rent cap on | -8.47 | +19.08 | 70.5 | 15.72 | Reference, Adverse, Stress | 15: gNonW +16.19 in Reference; secU25X +0.33 in Reference; secM3X +14.60 in Reference ... |
| m5.0 (= m5.1) | base tax 13%; progression 2.7 pts; cap 50%; business tax 25%; sales kept 17%; recycled 0%; business rate 1.7x; BU 60%; top multiplier 3.0; octave capacity 100%; octaves 2; Phi tier on; phase-in 4 y; issuance cap 8%; indexation surge; protected account none; rent cap off | -8.41 | +19.25 | 70.7 | 15.75 | Reference, Adverse | 15: gNonW +16.12 in Reference; secU25X +0.33 in Reference; secM3X +14.65 in Reference ... |
| h170 | base tax 2%; progression 5.0 pts; cap 70%; business tax 9%; sales kept 16%; recycled 33%; business rate 2.1x; BU 94%; top multiplier 6.8; octave capacity 50%; octaves 6; Phi tier off; phase-in 2 y; issuance cap none; indexation basic needs; protected account all savings; rent cap on | -8.39 | -9.83 | 71.4 | 1239.05 | Reference, Adverse, Stress | 4: inflation 1116.50 in Reference; inflation 1389.22 in Adverse; gNonF0 +4.00 in Stress ... |
| h55 | base tax 4%; progression 4.7 pts; cap 53%; business tax 7%; sales kept 45%; recycled 25%; business rate 2.9x; BU 62%; top multiplier 4.7; octave capacity 100%; octaves 4; Phi tier on; phase-in 10 y; issuance cap 8%; indexation basic needs; protected account first $10,000; rent cap off | -8.36 | +17.09 | 71.2 | 20.54 | Reference, Adverse, Stress | 15: gNonW +13.46 in Reference; secU25X +0.41 in Reference; secM3X +14.61 in Reference ... |
| h77 | base tax 20%; progression 4.1 pts; cap 72%; business tax 31%; sales kept 7%; recycled 54%; business rate 1.9x; BU 63%; top multiplier 7.1; octave capacity 50%; octaves 4; Phi tier off; phase-in 4 y; issuance cap 8%; indexation surge; protected account first $10,000; rent cap off | -8.31 | +17.02 | 70.6 | 20.47 | Adverse | 15: gNonW +13.69 in Reference; secU25X +0.41 in Reference; secM3X +14.64 in Reference ... |
| h93 | base tax 13%; progression 6.3 pts; cap 70%; business tax 51%; sales kept 28%; recycled 86%; business rate 2.9x; BU 61%; top multiplier 8.8; octave capacity not enforced; octaves 3; Phi tier on; phase-in 5 y; issuance cap 2%; indexation basic needs; protected account first $10,000; rent cap off | -8.28 | +16.98 | 71.1 | 20.20 | Reference, Adverse | 15: gNonW +13.48 in Reference; secU25X +0.41 in Reference; secM3X +14.44 in Reference ... |
| m6.0 | base tax 13%; progression 0.0 pts; cap 58%; business tax 0%; sales kept 17%; recycled 0%; business rate 1.0x; BU 60%; top multiplier 3.0; octave capacity not enforced; octaves 2; Phi tier on; phase-in 4 y; issuance cap 8%; indexation every year; protected account first $10,000; rent cap off | -8.28 | +16.52 | 70.7 | 19.78 | Reference, Adverse | 15: gNonW +13.28 in Reference; secU25X +0.45 in Reference; secM3X +14.19 in Reference ... |
| h184 | base tax 2%; progression 6.1 pts; cap 75%; business tax 23%; sales kept 41%; recycled 52%; business rate 2.7x; BU 61%; top multiplier 7.8; octave capacity 50%; octaves 4; Phi tier on; phase-in 7 y; issuance cap 8%; indexation basic needs; protected account first $10,000; rent cap off | -8.25 | +16.84 | 71.2 | 20.05 | Reference, Adverse, Stress | 15: gNonW +13.23 in Reference; secU25X +0.41 in Reference; secM3X +14.23 in Reference ... |
| m6.1 | base tax 13%; progression 0.0 pts; cap 58%; business tax 0%; sales kept 17%; recycled 0%; business rate 1.0x; BU 60%; top multiplier 3.0; octave capacity not enforced; octaves 2; Phi tier on; phase-in 10 y; issuance cap 8%; indexation every year; protected account first $10,000; rent cap off | -8.21 | +16.44 | 70.7 | 19.68 | Reference, Adverse | 15: gNonW +13.15 in Reference; secU25X +0.43 in Reference; secM3X +14.09 in Reference ... |
| m6.4 | base tax 13%; progression 0.0 pts; cap 58%; business tax 0%; sales kept 50%; recycled 0%; business rate 2.3x; BU 60%; top multiplier 3.0; octave capacity 50%; octaves 2; Phi tier on; phase-in 10 y; issuance cap 8%; indexation every year; protected account first $10,000; rent cap off | -7.99 | +16.70 | 70.7 | 19.55 | Reference, Adverse | 15: gNonW +13.26 in Reference; secU25X +0.40 in Reference; secM3X +14.19 in Reference ... |
| h197 | base tax 4%; progression 6.8 pts; cap 70%; business tax 9%; sales kept 11%; recycled 90%; business rate 1.6x; BU 87%; top multiplier 4.9; octave capacity not enforced; octaves 2; Phi tier off; phase-in 2 y; issuance cap none; indexation basic needs; protected account all savings; rent cap off | -6.05 | -8.20 | 71.3 | 1223.03 | Reference, Adverse, Stress | 4: inflation 1098.11 in Reference; inflation 1367.92 in Adverse; gNonF0 +4.49 in Stress ... |
| h189 | base tax 38%; progression 4.0 pts; cap 73%; business tax 12%; sales kept 42%; recycled 35%; business rate 2.7x; BU 80%; top multiplier 7.1; octave capacity 100%; octaves 2; Phi tier off; phase-in 4 y; issuance cap none; indexation surge; protected account all savings; rent cap off | -5.64 | -7.91 | 70.5 | 1197.06 | Reference, Adverse, Stress | 5: gNonF0 +0.28 in Reference; inflation 1070.82 in Reference; inflation 1330.33 in Adverse ... |
| h62 | base tax 5%; progression 4.7 pts; cap 56%; business tax 14%; sales kept 47%; recycled 36%; business rate 2.2x; BU 78%; top multiplier 3.6; octave capacity 50%; octaves 5; Phi tier on; phase-in 8 y; issuance cap none; indexation basic needs; protected account all savings; rent cap on | -4.82 | -7.33 | 71.2 | 1199.82 | Reference, Adverse, Stress | 5: gNonF0 +0.34 in Reference; inflation 1074.27 in Reference; inflation 1335.86 in Adverse ... |
| m9.9 | base tax 0%; progression 2.7 pts; cap 67%; business tax 25%; sales kept 50%; recycled 100%; business rate 3.0x; BU 73%; top multiplier 7.0; octave capacity 50%; octaves 2; Phi tier on; phase-in 10 y; issuance cap none; indexation basic needs; protected account all savings; rent cap off | -4.16 | -6.95 | 71.2 | 1186.59 | Reference, Adverse, Stress | 6: gNonF0 +0.77 in Reference; inflation 1058.27 in Reference; gNonF0 +0.07 in Adverse ... |
| h13 | base tax 25%; progression 6.2 pts; cap 58%; business tax 21%; sales kept 13%; recycled 15%; business rate 2.9x; BU 65%; top multiplier 6.2; octave capacity 100%; octaves 5; Phi tier on; phase-in 1 y; issuance cap 2%; indexation basic needs; protected account all savings; rent cap on | -2.30 | -5.86 | 71.0 | 1183.13 | Reference, Adverse, Stress | 6: gNonF0 +2.26 in Reference; inflation 1054.01 in Reference; gNonF0 +1.40 in Adverse ... |
| h112 | base tax 16%; progression 2.1 pts; cap 72%; business tax 11%; sales kept 46%; recycled 14%; business rate 2.4x; BU 60%; top multiplier 8.4; octave capacity 25%; octaves 3; Phi tier off; phase-in 3 y; issuance cap none; indexation every year; protected account all savings; rent cap off | -2.29 | -5.77 | 70.7 | 1155.20 | Reference, Adverse, Stress | 6: gNonF0 +2.42 in Reference; inflation 1024.62 in Reference; gNonF0 +1.51 in Adverse ... |
| h37 | base tax 17%; progression 0.6 pts; cap 74%; business tax 40%; sales kept 29%; recycled 39%; business rate 1.2x; BU 66%; top multiplier 8.5; octave capacity 100%; octaves 5; Phi tier on; phase-in 7 y; issuance cap 8%; indexation basic needs; protected account all savings; rent cap on | -1.91 | -5.50 | 71.0 | 1179.38 | Reference, Adverse, Stress | 7: gNonF0 +2.47 in Reference; gNonW +0.11 in Reference; inflation 1050.12 in Reference ... |
| h90 | base tax 14%; progression 4.9 pts; cap 56%; business tax 24%; sales kept 14%; recycled 29%; business rate 1.6x; BU 66%; top multiplier 8.3; octave capacity 50%; octaves 4; Phi tier off; phase-in 2 y; issuance cap 8%; indexation surge; protected account all savings; rent cap off | -1.85 | -5.50 | 70.7 | 1177.46 | Adverse, Stress | 7: gNonF0 +2.81 in Reference; gNonW +0.20 in Reference; inflation 1047.38 in Reference ... |
| h143 | base tax 8%; progression 4.8 pts; cap 55%; business tax 22%; sales kept 3%; recycled 12%; business rate 2.2x; BU 62%; top multiplier 6.0; octave capacity 100%; octaves 2; Phi tier on; phase-in 7 y; issuance cap none; indexation surge; protected account all savings; rent cap off | -1.82 | -5.42 | 70.7 | 1162.26 | Reference, Adverse, Stress | 7: gNonF0 +2.72 in Reference; gNonW +0.22 in Reference; inflation 1030.72 in Reference ... |
| h64 | base tax 3%; progression 7.4 pts; cap 68%; business tax 42%; sales kept 9%; recycled 48%; business rate 2.2x; BU 64%; top multiplier 4.1; octave capacity 25%; octaves 6; Phi tier off; phase-in 7 y; issuance cap 8%; indexation surge; protected account all savings; rent cap on | -1.47 | -5.19 | 70.7 | 1173.97 | Reference, Adverse, Stress | 7: gNonF0 +3.02 in Reference; gNonW +0.41 in Reference; inflation 1043.79 in Reference ... |
| h87 | base tax 5%; progression 5.7 pts; cap 51%; business tax 4%; sales kept 42%; recycled 90%; business rate 1.8x; BU 64%; top multiplier 6.1; octave capacity 25%; octaves 5; Phi tier on; phase-in 9 y; issuance cap 8%; indexation surge; protected account all savings; rent cap off | -1.38 | -5.14 | 70.7 | 1172.15 | Reference, Adverse, Stress | 7: gNonF0 +3.08 in Reference; gNonW +0.43 in Reference; inflation 1041.66 in Reference ... |
| h103 | base tax 15%; progression 4.3 pts; cap 64%; business tax 38%; sales kept 28%; recycled 98%; business rate 2.1x; BU 63%; top multiplier 6.9; octave capacity not enforced; octaves 5; Phi tier on; phase-in 3 y; issuance cap 8%; indexation basic needs; protected account all savings; rent cap off | -1.33 | -5.14 | 71.0 | 1170.20 | Reference, Adverse, Stress | 7: gNonF0 +2.90 in Reference; gNonW +0.29 in Reference; inflation 1039.81 in Reference ... |
| h36 | base tax 23%; progression 7.2 pts; cap 69%; business tax 32%; sales kept 49%; recycled 8%; business rate 2.7x; BU 61%; top multiplier 8.1; octave capacity 25%; octaves 5; Phi tier off; phase-in 6 y; issuance cap 8%; indexation basic needs; protected account all savings; rent cap off | -0.96 | -4.84 | 71.0 | 1165.60 | Adverse, Stress | 7: gNonF0 +3.15 in Reference; gNonW +0.47 in Reference; inflation 1034.74 in Reference ... |
| m5.8 (= m5.9) | base tax 13%; progression 8.0 pts; cap 67%; business tax 25%; sales kept 17%; recycled 67%; business rate 1.7x; BU 60%; top multiplier 7.0; octave capacity 100%; octaves 2; Phi tier on; phase-in 10 y; issuance cap 8%; indexation basic needs; protected account all savings; rent cap on | -0.94 | -4.84 | 71.0 | 1164.68 | Reference, Adverse, Stress | 7: gNonF0 +3.16 in Reference; gNonW +0.50 in Reference; inflation 1033.88 in Reference ... |
| m5.11 | base tax 13%; progression 8.0 pts; cap 67%; business tax 25%; sales kept 50%; recycled 67%; business rate 1.7x; BU 60%; top multiplier 7.0; octave capacity 25%; octaves 2; Phi tier on; phase-in 10 y; issuance cap 2%; indexation basic needs; protected account all savings; rent cap on | -0.93 | -4.82 | 71.0 | 1164.57 | Reference, Adverse, Stress | 7: gNonF0 +3.16 in Reference; gNonW +0.50 in Reference; inflation 1033.80 in Reference ... |
| m6.12 (= m6.13) | base tax 40%; progression 5.3 pts; cap 58%; business tax 50%; sales kept 50%; recycled 0%; business rate 2.3x; BU 60%; top multiplier 7.0; octave capacity 50%; octaves 2; Phi tier off; phase-in 10 y; issuance cap 2%; indexation basic needs; protected account all savings; rent cap off | -0.77 | -4.73 | 70.9 | 1164.21 | Reference, Adverse | 7: gNonF0 +3.27 in Reference; gNonW +0.49 in Reference; inflation 1032.64 in Reference ... |
| fflat | outside finance: flat wage contribution | +12.66 | +13.85 | 63.5 | -0.01 | Reference, Adverse, Stress | 15: gNonF0 +34.03 in Reference; gNonW +31.40 in Reference; secU25X +3.90 in Reference ... |

### release row, wages 90%

255 candidates; 0 pass no harm in every environment; 0 of those keep inflation under 5 points a year. **No setting tested meets the rule.** Closest (by the summed excess of what fails): `fland` (outside finance: land-value tax: gNonF0 +5.11 in Reference, gNonW +8.38 in Reference, secU25X +1.04 in Reference, secM3X +4.65 in Reference ...); `fflat` (outside finance: flat wage contribution: gNonF0 +34.03 in Reference, gNonW +31.40 in Reference, secU25X +3.90 in Reference, secM3X +16.06 in Reference ...); `h81` (base tax 14%; progression 3.9 pts; cap 59%; business tax 66%; sales kept 35%; recycled 38%; business rate 2.6x; BU 61%; top multiplier 5.3; octave capacity 50%; octaves 6; Phi tier off; phase-in 3 y; issuance cap 4%; indexation basic needs; protected account none; rent cap on: gNonF0 +6.87 in Reference, gNonW +37.59 in Reference, secU25X +0.57 in Reference, secM3X +22.22 in Reference ...); `h147` (base tax 7%; progression 1.0 pts; cap 51%; business tax 75%; sales kept 7%; recycled 73%; business rate 1.4x; BU 62%; top multiplier 5.8; octave capacity not enforced; octaves 4; Phi tier on; phase-in 5 y; issuance cap 2%; indexation basic needs; protected account none; rent cap off: gNonF0 +6.93 in Reference, gNonW +37.64 in Reference, secU25X +0.56 in Reference, secM3X +22.24 in Reference ...); `h144` (base tax 1%; progression 3.7 pts; cap 71%; business tax 68%; sales kept 38%; recycled 80%; business rate 1.9x; BU 62%; top multiplier 7.6; octave capacity 100%; octaves 3; Phi tier off; phase-in 8 y; issuance cap 8%; indexation surge; protected account none; rent cap off: gNonF0 +6.95 in Reference, gNonW +38.30 in Reference, secU25X +0.52 in Reference, secM3X +22.39 in Reference ...).

| Point | What it sets | Basket poverty | Wealth poverty | Participation | Inflation | On the front in | Fails |
|---|---|---|---|---|---|---|---|
| t0 | tax 0% | -10.79 | +53.24 | 70.9 | 66.36 | Reference, Adverse, Stress | 18: gNonF0 +5.32 in Reference; gNonW +63.63 in Reference; secU25X +0.73 in Reference ... |
| bt0 | business tax 0% | -10.35 | +53.31 | 70.5 | 66.09 | Reference, Adverse, Stress | 18: gNonF0 +6.61 in Reference; gNonW +63.92 in Reference; secU25X +0.89 in Reference ... |
| t4 | tax 4% | -9.96 | +53.53 | 70.8 | 65.45 | Reference, Adverse, Stress | 18: gNonF0 +6.34 in Reference; gNonW +64.06 in Reference; secU25X +0.75 in Reference ... |
| t8 | tax 8% | -9.19 | +53.78 | 70.6 | 64.49 | Reference, Adverse, Stress | 18: gNonF0 +7.27 in Reference; gNonW +64.56 in Reference; secU25X +0.75 in Reference ... |
| fland | outside finance: land-value tax | -8.93 | +9.39 | 67.3 | 9.56 | Reference, Adverse, Stress | 15: gNonF0 +5.11 in Reference; gNonW +8.38 in Reference; secU25X +1.04 in Reference ... |
| kp50 | Source keeps 50% of project sales | -8.65 | +53.66 | 70.5 | 61.82 | Reference, Adverse | 18: gNonF0 +7.68 in Reference; gNonW +64.56 in Reference; secU25X +0.75 in Reference ... |
| ixn | indexation: every year, basic needs | -8.65 | +53.95 | 71.1 | 63.86 | Reference, Adverse, Stress | 18: gNonF0 +6.91 in Reference; gNonW +65.00 in Reference; secU25X +1.06 in Reference ... |
| pr0c75 (= pr0c50) | progression 0 pts, cap 75% | -8.61 | +53.78 | 70.7 | 62.96 | Reference, Adverse, Stress | 18: gNonF0 +7.53 in Reference; gNonW +64.60 in Reference; secU25X +0.68 in Reference ... |
| kp25 | Source keeps 25% of project sales | -8.49 | +53.77 | 70.5 | 62.37 | Reference, Adverse | 18: gNonF0 +7.88 in Reference; gNonW +64.68 in Reference; secU25X +0.75 in Reference ... |
| kp10 | Source keeps 10% of project sales | -8.40 | +53.81 | 70.5 | 62.69 | Reference, Adverse | 18: gNonF0 +8.04 in Reference; gNonW +64.75 in Reference; secU25X +0.75 in Reference ... |
| no6 | 6 octaves | -8.35 | +53.62 | 70.5 | 62.87 | none | 18: gNonF0 +8.13 in Reference; gNonW +64.81 in Reference; secU25X +0.75 in Reference ... |
| phi0 | Phi tier off | -8.26 | +53.85 | 70.5 | 62.94 | none | 18: gNonF0 +8.17 in Reference; gNonW +64.84 in Reference; secU25X +0.73 in Reference ... |
| ph5 | phase-in over 5 years | -8.15 | +53.32 | 70.5 | 59.90 | Reference, Adverse | 18: gNonF0 +7.72 in Reference; gNonW +64.64 in Reference; secU25X +0.63 in Reference ... |
| ph10 | phase-in over 10 years | -7.60 | +52.38 | 70.6 | 55.99 | Reference, Adverse, Stress | 18: gNonF0 +7.62 in Reference; gNonW +64.01 in Reference; secU25X +0.59 in Reference ... |
| bt25 | business tax 25% | -6.41 | +54.29 | 70.6 | 60.25 | Reference, Adverse | 18: gNonF0 +9.55 in Reference; gNonW +65.54 in Reference; secU25X +0.68 in Reference ... |
| bu80 | 80% of the BU | -4.93 | +52.29 | 70.7 | 51.94 | Reference, Adverse | 18: gNonF0 +9.60 in Reference; gNonW +64.07 in Reference; secU25X +0.60 in Reference ... |
| h10 | base tax 20%; progression 5.0 pts; cap 64%; business tax 2%; sales kept 27%; recycled 2%; business rate 2.4x; BU 84%; top multiplier 7.8; octave capacity 50%; octaves 6; Phi tier off; phase-in 2 y; issuance cap none; indexation basic needs; protected account none; rent cap off | -4.31 | +52.62 | 71.1 | 50.90 | Reference, Adverse, Stress | 18: gNonF0 +9.41 in Reference; gNonW +64.64 in Reference; secU25X +0.83 in Reference ... |
| svc | protected account, first $10,000 | -3.99 | +36.31 | 70.6 | 84.58 | Reference, Adverse | 18: gNonF0 +12.46 in Reference; gNonW +49.40 in Reference; secU25X +0.80 in Reference ... |
| bu60 | 60% of the BU | -3.25 | +47.59 | 70.7 | 38.73 | Reference, Adverse, Stress | 18: gNonF0 +8.57 in Reference; gNonW +59.23 in Reference; secU25X +0.58 in Reference ... |
| h119 | base tax 20%; progression 2.4 pts; cap 67%; business tax 20%; sales kept 7%; recycled 2%; business rate 2.0x; BU 95%; top multiplier 6.1; octave capacity 100%; octaves 4; Phi tier on; phase-in 9 y; issuance cap none; indexation basic needs; protected account none; rent cap on | -2.97 | +51.37 | 71.1 | 44.32 | Reference, Adverse, Stress | 18: gNonF0 +9.44 in Reference; gNonW +63.83 in Reference; secU25X +0.76 in Reference ... |
| h100 | base tax 29%; progression 4.4 pts; cap 66%; business tax 19%; sales kept 25%; recycled 93%; business rate 2.9x; BU 99%; top multiplier 6.9; octave capacity 25%; octaves 5; Phi tier on; phase-in 6 y; issuance cap none; indexation surge; protected account first $10,000; rent cap on | -2.38 | +38.36 | 70.5 | 75.72 | Reference, Adverse | 18: gNonF0 +12.92 in Reference; gNonW +51.63 in Reference; secU25X +0.69 in Reference ... |
| h50 | base tax 30%; progression 4.7 pts; cap 50%; business tax 42%; sales kept 24%; recycled 96%; business rate 2.3x; BU 91%; top multiplier 7.2; octave capacity 100%; octaves 6; Phi tier off; phase-in 8 y; issuance cap none; indexation every year; protected account none; rent cap on | -2.23 | +49.16 | 70.6 | 38.61 | Reference, Stress | 18: gNonF0 +9.28 in Reference; gNonW +61.67 in Reference; secU25X +0.54 in Reference ... |
| h192 | base tax 27%; progression 4.8 pts; cap 60%; business tax 0%; sales kept 8%; recycled 26%; business rate 2.6x; BU 92%; top multiplier 5.2; octave capacity 25%; octaves 4; Phi tier on; phase-in 9 y; issuance cap none; indexation surge; protected account first $10,000; rent cap off | -2.02 | +37.67 | 70.6 | 70.22 | Reference, Adverse | 18: gNonF0 +12.68 in Reference; gNonW +51.36 in Reference; secU25X +0.61 in Reference ... |
| h89 | base tax 32%; progression 5.0 pts; cap 68%; business tax 2%; sales kept 17%; recycled 69%; business rate 1.7x; BU 79%; top multiplier 6.5; octave capacity 50%; octaves 3; Phi tier off; phase-in 5 y; issuance cap none; indexation surge; protected account none; rent cap on | -1.97 | +48.89 | 70.6 | 37.20 | Reference, Adverse, Stress | 18: gNonF0 +9.18 in Reference; gNonW +60.65 in Reference; secU25X +0.55 in Reference ... |
| h61 | base tax 39%; progression 4.0 pts; cap 70%; business tax 34%; sales kept 34%; recycled 1%; business rate 2.3x; BU 75%; top multiplier 6.9; octave capacity 50%; octaves 5; Phi tier off; phase-in 9 y; issuance cap none; indexation surge; protected account none; rent cap off | -1.61 | +45.09 | 70.5 | 31.40 | Reference, Adverse, Stress | 18: gNonF0 +8.15 in Reference; gNonW +55.90 in Reference; secU25X +0.53 in Reference ... |
| h154 | base tax 37%; progression 2.6 pts; cap 65%; business tax 45%; sales kept 41%; recycled 42%; business rate 2.7x; BU 75%; top multiplier 4.4; octave capacity not enforced; octaves 2; Phi tier on; phase-in 4 y; issuance cap none; indexation basic needs; protected account none; rent cap on | -1.09 | +46.77 | 70.8 | 33.41 | Reference, Adverse | 18: gNonF0 +8.68 in Reference; gNonW +57.95 in Reference; secU25X +0.73 in Reference ... |
| h23 | base tax 23%; progression 0.5 pts; cap 69%; business tax 8%; sales kept 3%; recycled 16%; business rate 2.4x; BU 93%; top multiplier 4.3; octave capacity 100%; octaves 6; Phi tier on; phase-in 2 y; issuance cap none; indexation surge; protected account first $10,000; rent cap off | -0.98 | +40.96 | 70.6 | 71.77 | Reference, Adverse | 18: gNonF0 +13.96 in Reference; gNonW +54.14 in Reference; secU25X +0.63 in Reference ... |
| h126 | base tax 17%; progression 0.4 pts; cap 55%; business tax 17%; sales kept 16%; recycled 97%; business rate 2.8x; BU 75%; top multiplier 7.9; octave capacity not enforced; octaves 4; Phi tier off; phase-in 7 y; issuance cap none; indexation every year; protected account first $10,000; rent cap off | -0.85 | +40.76 | 70.7 | 53.63 | Reference, Adverse | 18: gNonF0 +11.68 in Reference; gNonW +53.12 in Reference; secU25X +0.56 in Reference ... |
| h32 | base tax 13%; progression 1.2 pts; cap 67%; business tax 63%; sales kept 20%; recycled 80%; business rate 2.8x; BU 84%; top multiplier 4.7; octave capacity 50%; octaves 4; Phi tier off; phase-in 7 y; issuance cap none; indexation every year; protected account none; rent cap on | -0.39 | +46.37 | 70.7 | 32.76 | Reference, Adverse | 18: gNonF0 +9.26 in Reference; gNonW +57.66 in Reference; secU25X +0.56 in Reference ... |
| h174 | base tax 32%; progression 7.4 pts; cap 57%; business tax 53%; sales kept 17%; recycled 56%; business rate 2.5x; BU 76%; top multiplier 3.6; octave capacity 100%; octaves 3; Phi tier off; phase-in 5 y; issuance cap none; indexation surge; protected account none; rent cap off | -0.17 | +44.71 | 70.6 | 29.91 | Reference, Adverse | 18: gNonF0 +8.78 in Reference; gNonW +55.18 in Reference; secU25X +0.56 in Reference ... |
| h86 | base tax 10%; progression 0.9 pts; cap 69%; business tax 70%; sales kept 9%; recycled 50%; business rate 1.6x; BU 82%; top multiplier 6.4; octave capacity not enforced; octaves 5; Phi tier off; phase-in 2 y; issuance cap 2%; indexation surge; protected account none; rent cap on | -0.01 | +44.02 | 70.7 | 29.07 | Reference, Adverse | 18: gNonF0 +9.22 in Reference; gNonW +54.41 in Reference; secU25X +1.79 in Reference ... |
| h141 | base tax 17%; progression 7.5 pts; cap 53%; business tax 0%; sales kept 37%; recycled 79%; business rate 1.9x; BU 89%; top multiplier 7.8; octave capacity 50%; octaves 2; Phi tier off; phase-in 8 y; issuance cap none; indexation surge; protected account first $10,000; rent cap off | +0.04 | +43.12 | 70.7 | 58.71 | Adverse | 18: gNonF0 +13.20 in Reference; gNonW +55.38 in Reference; secU25X +0.58 in Reference ... |
| h132 | base tax 16%; progression 1.3 pts; cap 53%; business tax 50%; sales kept 50%; recycled 18%; business rate 1.5x; BU 99%; top multiplier 8.3; octave capacity not enforced; octaves 3; Phi tier on; phase-in 4 y; issuance cap 2%; indexation basic needs; protected account none; rent cap off | +0.14 | +49.35 | 71.0 | 37.30 | Reference, Adverse | 18: gNonF0 +10.94 in Reference; gNonW +61.50 in Reference; secU25X +1.90 in Reference ... |
| h138 | base tax 24%; progression 7.4 pts; cap 72%; business tax 1%; sales kept 43%; recycled 19%; business rate 2.3x; BU 60%; top multiplier 5.7; octave capacity 100%; octaves 6; Phi tier off; phase-in 6 y; issuance cap none; indexation every year; protected account first $10,000; rent cap on | +0.15 | +39.89 | 70.6 | 40.70 | Reference, Adverse | 18: gNonF0 +10.34 in Reference; gNonW +49.33 in Reference; secU25X +0.57 in Reference ... |
| h182 | base tax 14%; progression 1.0 pts; cap 63%; business tax 44%; sales kept 5%; recycled 20%; business rate 1.3x; BU 71%; top multiplier 4.2; octave capacity not enforced; octaves 3; Phi tier off; phase-in 3 y; issuance cap none; indexation surge; protected account none; rent cap on | +0.16 | +40.34 | 70.7 | 24.55 | Reference, Adverse | 18: gNonF0 +8.33 in Reference; gNonW +48.25 in Reference; secU25X +0.56 in Reference ... |
| h53 | base tax 24%; progression 2.2 pts; cap 67%; business tax 70%; sales kept 25%; recycled 43%; business rate 1.1x; BU 71%; top multiplier 6.7; octave capacity 100%; octaves 2; Phi tier off; phase-in 3 y; issuance cap 8%; indexation every year; protected account none; rent cap off | +0.46 | +39.45 | 70.6 | 23.64 | Adverse | 18: gNonF0 +8.28 in Reference; gNonW +46.52 in Reference; secU25X +0.90 in Reference ... |
| h74 | base tax 12%; progression 1.5 pts; cap 62%; business tax 69%; sales kept 18%; recycled 12%; business rate 2.3x; BU 69%; top multiplier 8.4; octave capacity 25%; octaves 4; Phi tier off; phase-in 3 y; issuance cap 4%; indexation surge; protected account none; rent cap off | +0.49 | +39.27 | 70.7 | 23.45 | Reference, Adverse | 18: gNonF0 +8.06 in Reference; gNonW +46.09 in Reference; secU25X +1.36 in Reference ... |
| h28 | base tax 26%; progression 7.2 pts; cap 52%; business tax 62%; sales kept 14%; recycled 52%; business rate 2.2x; BU 62%; top multiplier 3.1; octave capacity 100%; octaves 6; Phi tier on; phase-in 7 y; issuance cap none; indexation surge; protected account none; rent cap off | +0.52 | +35.21 | 70.6 | 20.34 | Reference, Adverse | 18: gNonF0 +6.80 in Reference; gNonW +39.50 in Reference; secU25X +0.52 in Reference ... |
| h101 | base tax 29%; progression 6.8 pts; cap 71%; business tax 72%; sales kept 1%; recycled 30%; business rate 1.9x; BU 64%; top multiplier 6.8; octave capacity not enforced; octaves 3; Phi tier on; phase-in 4 y; issuance cap 2%; indexation basic needs; protected account none; rent cap on | +0.54 | +36.49 | 70.8 | 21.19 | Reference, Adverse | 18: gNonF0 +7.31 in Reference; gNonW +41.67 in Reference; secU25X +0.91 in Reference ... |
| h164 | base tax 8%; progression 3.6 pts; cap 58%; business tax 28%; sales kept 36%; recycled 56%; business rate 1.3x; BU 98%; top multiplier 9.0; octave capacity 100%; octaves 2; Phi tier off; phase-in 2 y; issuance cap 4%; indexation basic needs; protected account none; rent cap on | +0.55 | +48.82 | 71.0 | 35.82 | Reference, Adverse | 18: gNonF0 +10.97 in Reference; gNonW +60.40 in Reference; secU25X +0.83 in Reference ... |
| h102 | base tax 36%; progression 0.8 pts; cap 63%; business tax 74%; sales kept 25%; recycled 68%; business rate 1.0x; BU 90%; top multiplier 8.2; octave capacity 25%; octaves 3; Phi tier on; phase-in 4 y; issuance cap 4%; indexation basic needs; protected account none; rent cap on | +0.56 | +46.52 | 70.9 | 32.12 | Reference, Adverse | 18: gNonF0 +10.20 in Reference; gNonW +57.28 in Reference; secU25X +0.99 in Reference ... |
| h144 | base tax 1%; progression 3.7 pts; cap 71%; business tax 68%; sales kept 38%; recycled 80%; business rate 1.9x; BU 62%; top multiplier 7.6; octave capacity 100%; octaves 3; Phi tier off; phase-in 8 y; issuance cap 8%; indexation surge; protected account none; rent cap off | +0.71 | +34.48 | 70.7 | 19.39 | Reference, Adverse, Stress | 18: gNonF0 +6.95 in Reference; gNonW +38.30 in Reference; secU25X +0.52 in Reference ... |
| h26 | base tax 4%; progression 7.6 pts; cap 67%; business tax 34%; sales kept 14%; recycled 31%; business rate 1.4x; BU 76%; top multiplier 8.3; octave capacity 50%; octaves 3; Phi tier off; phase-in 1 y; issuance cap 2%; indexation basic needs; protected account none; rent cap on | +0.75 | +41.45 | 70.9 | 25.31 | Reference, Adverse, Stress | 18: gNonF0 +8.73 in Reference; gNonW +48.85 in Reference; secU25X +0.67 in Reference ... |
| h147 | base tax 7%; progression 1.0 pts; cap 51%; business tax 75%; sales kept 7%; recycled 73%; business rate 1.4x; BU 62%; top multiplier 5.8; octave capacity not enforced; octaves 4; Phi tier on; phase-in 5 y; issuance cap 2%; indexation basic needs; protected account none; rent cap off | +0.77 | +34.40 | 70.8 | 19.31 | Reference, Adverse, Stress | 18: gNonF0 +6.93 in Reference; gNonW +37.64 in Reference; secU25X +0.56 in Reference ... |
| h81 | base tax 14%; progression 3.9 pts; cap 59%; business tax 66%; sales kept 35%; recycled 38%; business rate 2.6x; BU 61%; top multiplier 5.3; octave capacity 50%; octaves 6; Phi tier off; phase-in 3 y; issuance cap 4%; indexation basic needs; protected account none; rent cap on | +0.79 | +34.01 | 70.8 | 19.05 | Reference, Adverse, Stress | 18: gNonF0 +6.87 in Reference; gNonW +37.59 in Reference; secU25X +0.57 in Reference ... |
| h146 | base tax 25%; progression 1.3 pts; cap 71%; business tax 62%; sales kept 49%; recycled 57%; business rate 2.4x; BU 93%; top multiplier 6.6; octave capacity 25%; octaves 5; Phi tier on; phase-in 6 y; issuance cap 2%; indexation basic needs; protected account none; rent cap on | +0.81 | +47.24 | 70.9 | 33.29 | Reference, Adverse | 18: gNonF0 +10.55 in Reference; gNonW +58.09 in Reference; secU25X +0.87 in Reference ... |
| h162 | base tax 12%; progression 5.6 pts; cap 62%; business tax 36%; sales kept 30%; recycled 81%; business rate 2.1x; BU 85%; top multiplier 5.7; octave capacity 100%; octaves 5; Phi tier off; phase-in 6 y; issuance cap 8%; indexation basic needs; protected account none; rent cap on | +0.95 | +44.51 | 70.9 | 29.37 | Reference, Adverse | 18: gNonF0 +9.87 in Reference; gNonW +54.61 in Reference; secU25X +0.71 in Reference ... |
| h153 | base tax 8%; progression 5.1 pts; cap 58%; business tax 6%; sales kept 22%; recycled 48%; business rate 2.8x; BU 94%; top multiplier 3.2; octave capacity 100%; octaves 5; Phi tier off; phase-in 8 y; issuance cap 2%; indexation basic needs; protected account none; rent cap on | +1.01 | +47.41 | 70.9 | 33.77 | Reference, Adverse | 18: gNonF0 +10.94 in Reference; gNonW +58.81 in Reference; secU25X +0.77 in Reference ... |
| h108 | base tax 12%; progression 5.3 pts; cap 72%; business tax 22%; sales kept 24%; recycled 35%; business rate 2.2x; BU 64%; top multiplier 3.1; octave capacity not enforced; octaves 2; Phi tier on; phase-in 8 y; issuance cap none; indexation basic needs; protected account first $10,000; rent cap off | +1.42 | +40.60 | 70.9 | 36.53 | Reference, Adverse | 18: gNonF0 +10.53 in Reference; gNonW +48.72 in Reference; secU25X +0.71 in Reference ... |
| h21 | base tax 16%; progression 1.4 pts; cap 51%; business tax 65%; sales kept 30%; recycled 17%; business rate 2.2x; BU 94%; top multiplier 8.0; octave capacity not enforced; octaves 2; Phi tier on; phase-in 8 y; issuance cap 4%; indexation basic needs; protected account first $10,000; rent cap on | +3.70 | +46.80 | 70.9 | 45.23 | Adverse | 18: gNonF0 +14.39 in Reference; gNonW +56.54 in Reference; secU25X +1.12 in Reference ... |
| h105 | base tax 1%; progression 7.9 pts; cap 65%; business tax 5%; sales kept 37%; recycled 94%; business rate 2.3x; BU 95%; top multiplier 8.5; octave capacity not enforced; octaves 6; Phi tier on; phase-in 4 y; issuance cap 8%; indexation basic needs; protected account first $10,000; rent cap on | +4.01 | +47.23 | 70.9 | 46.61 | Adverse, Stress | 18: gNonF0 +15.03 in Reference; gNonW +57.15 in Reference; secU25X +0.86 in Reference ... |
| fflat | outside finance: flat wage contribution | +12.66 | +13.85 | 63.5 | -0.01 | Reference, Adverse, Stress | 15: gNonF0 +34.03 in Reference; gNonW +31.40 in Reference; secU25X +3.90 in Reference ... |
| sva | protected account, all savings | +20.85 | +1.74 | 70.7 | 3075.04 | Reference, Adverse, Stress | 14: gNonF0 +34.70 in Reference; gNonW +13.37 in Reference; secU25X +0.02 in Reference ... |
| h170 | base tax 2%; progression 5.0 pts; cap 70%; business tax 9%; sales kept 16%; recycled 33%; business rate 2.1x; BU 94%; top multiplier 6.8; octave capacity 50%; octaves 6; Phi tier off; phase-in 2 y; issuance cap none; indexation basic needs; protected account all savings; rent cap on | +22.23 | +3.25 | 70.7 | 3060.09 | Reference, Adverse, Stress | 13: gNonF0 +35.38 in Reference; gNonW +14.42 in Reference; secM3X +2.21 in Reference ... |
| h197 | base tax 4%; progression 6.8 pts; cap 70%; business tax 9%; sales kept 11%; recycled 90%; business rate 1.6x; BU 87%; top multiplier 4.9; octave capacity not enforced; octaves 2; Phi tier off; phase-in 2 y; issuance cap none; indexation basic needs; protected account all savings; rent cap off | +23.44 | +4.51 | 70.7 | 3017.64 | Reference, Adverse, Stress | 13: gNonF0 +36.26 in Reference; gNonW +15.25 in Reference; secM3X +3.21 in Reference ... |
| h189 | base tax 38%; progression 4.0 pts; cap 73%; business tax 12%; sales kept 42%; recycled 35%; business rate 2.7x; BU 80%; top multiplier 7.1; octave capacity 100%; octaves 2; Phi tier off; phase-in 4 y; issuance cap none; indexation surge; protected account all savings; rent cap off | +23.66 | +4.93 | 70.5 | 2904.64 | Reference, Adverse, Stress | 13: gNonF0 +36.48 in Reference; gNonW +15.35 in Reference; secM3X +3.58 in Reference ... |
| h118 | base tax 8%; progression 1.5 pts; cap 64%; business tax 32%; sales kept 12%; recycled 65%; business rate 1.0x; BU 82%; top multiplier 5.6; octave capacity not enforced; octaves 2; Phi tier on; phase-in 4 y; issuance cap none; indexation surge; protected account all savings; rent cap on | +24.26 | +5.23 | 70.7 | 3025.96 | Reference, Stress | 13: gNonF0 +36.94 in Reference; gNonW +15.67 in Reference; secM3X +3.87 in Reference ... |
| h62 | base tax 5%; progression 4.7 pts; cap 56%; business tax 14%; sales kept 47%; recycled 36%; business rate 2.2x; BU 78%; top multiplier 3.6; octave capacity 50%; octaves 5; Phi tier on; phase-in 8 y; issuance cap none; indexation basic needs; protected account all savings; rent cap on | +24.31 | +5.54 | 70.6 | 2911.79 | Adverse, Stress | 13: gNonF0 +36.81 in Reference; gNonW +15.76 in Reference; secM3X +3.98 in Reference ... |
| h190 | base tax 2%; progression 6.0 pts; cap 51%; business tax 49%; sales kept 48%; recycled 22%; business rate 1.3x; BU 83%; top multiplier 8.4; octave capacity 50%; octaves 6; Phi tier off; phase-in 6 y; issuance cap 8%; indexation every year; protected account all savings; rent cap off | +24.36 | +5.29 | 70.7 | 3037.70 | Reference | 13: gNonF0 +37.00 in Reference; gNonW +15.67 in Reference; secM3X +3.90 in Reference ... |
| h42 | base tax 10%; progression 3.5 pts; cap 65%; business tax 29%; sales kept 47%; recycled 87%; business rate 1.7x; BU 81%; top multiplier 6.8; octave capacity not enforced; octaves 4; Phi tier on; phase-in 10 y; issuance cap 2%; indexation every year; protected account all savings; rent cap off | +24.58 | +5.52 | 70.7 | 3011.75 | Reference, Adverse | 13: gNonF0 +37.14 in Reference; gNonW +15.77 in Reference; secM3X +4.08 in Reference ... |
| h159 | base tax 0%; progression 0.3 pts; cap 57%; business tax 36%; sales kept 45%; recycled 49%; business rate 1.6x; BU 78%; top multiplier 7.7; octave capacity not enforced; octaves 2; Phi tier off; phase-in 7 y; issuance cap 4%; indexation surge; protected account all savings; rent cap on | +24.70 | +5.73 | 70.7 | 2984.46 | Reference | 14: gNonF0 +37.20 in Reference; gNonW +15.82 in Reference; secM3X +4.17 in Reference ... |
| h13 | base tax 25%; progression 6.2 pts; cap 58%; business tax 21%; sales kept 13%; recycled 15%; business rate 2.9x; BU 65%; top multiplier 6.2; octave capacity 100%; octaves 5; Phi tier on; phase-in 1 y; issuance cap 2%; indexation basic needs; protected account all savings; rent cap on | +24.92 | +6.51 | 70.6 | 2872.93 | Reference, Adverse, Stress | 15: gNonF0 +37.21 in Reference; gNonW +16.54 in Reference; secU25X +0.06 in Reference ... |
| h165 | base tax 18%; progression 7.8 pts; cap 51%; business tax 28%; sales kept 5%; recycled 18%; business rate 2.6x; BU 75%; top multiplier 5.6; octave capacity 50%; octaves 3; Phi tier off; phase-in 5 y; issuance cap 4%; indexation every year; protected account all savings; rent cap off | +24.94 | +6.10 | 70.7 | 2957.88 | Reference | 14: gNonF0 +37.32 in Reference; gNonW +16.06 in Reference; secM3X +4.39 in Reference ... |
| h171 | base tax 22%; progression 3.7 pts; cap 51%; business tax 8%; sales kept 18%; recycled 77%; business rate 1.1x; BU 74%; top multiplier 7.5; octave capacity not enforced; octaves 4; Phi tier on; phase-in 6 y; issuance cap 8%; indexation surge; protected account all savings; rent cap on | +24.95 | +6.16 | 70.6 | 2948.94 | Reference | 14: gNonF0 +37.31 in Reference; gNonW +16.10 in Reference; secM3X +4.41 in Reference ... |
| h112 | base tax 16%; progression 2.1 pts; cap 72%; business tax 11%; sales kept 46%; recycled 14%; business rate 2.4x; BU 60%; top multiplier 8.4; octave capacity 25%; octaves 3; Phi tier off; phase-in 3 y; issuance cap none; indexation every year; protected account all savings; rent cap off | +25.03 | +6.75 | 70.7 | 2746.52 | Reference, Adverse, Stress | 14: gNonF0 +37.27 in Reference; gNonW +16.29 in Reference; secM3X +4.65 in Reference ... |
| h181 | base tax 23%; progression 4.6 pts; cap 62%; business tax 10%; sales kept 9%; recycled 84%; business rate 2.9x; BU 70%; top multiplier 8.8; octave capacity 25%; octaves 2; Phi tier off; phase-in 5 y; issuance cap 2%; indexation every year; protected account all savings; rent cap on | +25.05 | +6.40 | 70.6 | 2909.18 | Reference | 14: gNonF0 +37.34 in Reference; gNonW +16.29 in Reference; secM3X +4.49 in Reference ... |
| h116 | base tax 5%; progression 1.7 pts; cap 71%; business tax 3%; sales kept 48%; recycled 7%; business rate 1.2x; BU 73%; top multiplier 5.3; octave capacity 25%; octaves 5; Phi tier off; phase-in 6 y; issuance cap 2%; indexation every year; protected account all savings; rent cap off | +25.10 | +6.33 | 70.7 | 2934.14 | Reference | 14: gNonF0 +37.40 in Reference; gNonW +16.26 in Reference; secM3X +4.53 in Reference ... |
| h48 | base tax 4%; progression 5.5 pts; cap 61%; business tax 66%; sales kept 1%; recycled 1%; business rate 1.1x; BU 72%; top multiplier 3.9; octave capacity 100%; octaves 4; Phi tier on; phase-in 9 y; issuance cap 4%; indexation every year; protected account all savings; rent cap off | +25.16 | +6.40 | 70.7 | 2928.94 | Reference | 14: gNonF0 +37.44 in Reference; gNonW +16.29 in Reference; secM3X +4.57 in Reference ... |
| h187 | base tax 23%; progression 5.1 pts; cap 73%; business tax 51%; sales kept 34%; recycled 44%; business rate 2.4x; BU 72%; top multiplier 4.8; octave capacity 25%; octaves 5; Phi tier on; phase-in 7 y; issuance cap 2%; indexation surge; protected account all savings; rent cap on | +25.17 | +6.43 | 70.6 | 2927.73 | Reference | 14: gNonF0 +37.43 in Reference; gNonW +16.31 in Reference; secM3X +4.57 in Reference ... |
| h24 | base tax 21%; progression 1.3 pts; cap 72%; business tax 15%; sales kept 2%; recycled 64%; business rate 1.9x; BU 69%; top multiplier 3.9; octave capacity 50%; octaves 3; Phi tier off; phase-in 5 y; issuance cap 8%; indexation basic needs; protected account all savings; rent cap on | +25.31 | +6.70 | 70.6 | 2895.38 | Adverse, Stress | 14: gNonF0 +37.45 in Reference; gNonW +16.59 in Reference; secM3X +4.72 in Reference ... |
| h90 | base tax 14%; progression 4.9 pts; cap 56%; business tax 24%; sales kept 14%; recycled 29%; business rate 1.6x; BU 66%; top multiplier 8.3; octave capacity 50%; octaves 4; Phi tier off; phase-in 2 y; issuance cap 8%; indexation surge; protected account all savings; rent cap off | +25.36 | +6.79 | 70.7 | 2865.51 | Reference, Adverse, Stress | 14: gNonF0 +37.53 in Reference; gNonW +16.52 in Reference; secM3X +4.74 in Reference ... |
| h143 | base tax 8%; progression 4.8 pts; cap 55%; business tax 22%; sales kept 3%; recycled 12%; business rate 2.2x; BU 62%; top multiplier 6.0; octave capacity 100%; octaves 2; Phi tier on; phase-in 7 y; issuance cap none; indexation surge; protected account all savings; rent cap off | +25.46 | +7.05 | 70.7 | 2778.57 | Reference, Adverse, Stress | 14: gNonF0 +37.56 in Reference; gNonW +16.56 in Reference; secM3X +4.95 in Reference ... |
| h64 | base tax 3%; progression 7.4 pts; cap 68%; business tax 42%; sales kept 9%; recycled 48%; business rate 2.2x; BU 64%; top multiplier 4.1; octave capacity 25%; octaves 6; Phi tier off; phase-in 7 y; issuance cap 8%; indexation surge; protected account all savings; rent cap on | +25.63 | +7.11 | 70.7 | 2849.43 | Reference, Adverse, Stress | 14: gNonF0 +37.70 in Reference; gNonW +16.62 in Reference; secM3X +4.99 in Reference ... |
| h87 | base tax 5%; progression 5.7 pts; cap 51%; business tax 4%; sales kept 42%; recycled 90%; business rate 1.8x; BU 64%; top multiplier 6.1; octave capacity 25%; octaves 5; Phi tier on; phase-in 9 y; issuance cap 8%; indexation surge; protected account all savings; rent cap off | +25.63 | +7.11 | 70.7 | 2844.73 | Reference, Adverse, Stress | 14: gNonF0 +37.71 in Reference; gNonW +16.62 in Reference; secM3X +5.00 in Reference ... |

### C2.2 design, wages 100%

435 candidates; 175 pass no harm in every environment; 0 of those keep inflation under 5 points a year. **No setting tested meets the rule.** Closest (by the summed excess of what fails): `fland` (outside finance: land-value tax: secU25X +2.81 in Reference, inflation 5.03 in Reference, secU25X +3.31 in Adverse, inflation 6.12 in Adverse ...); `fflat` (outside finance: flat wage contribution: secU25X +5.24 in Reference, secU25X +3.70 in Adverse, secU25X +1.43 in Stress); `kp50` (Source keeps 50% of project sales: secU25X +0.27 in Reference, inflation 28.75 in Reference, inflation 33.37 in Adverse, inflation 37.08 in Stress); `m6.1` (base tax 13%; progression 0.0 pts; cap 58%; business tax 0%; sales kept 17%; recycled 0%; business rate 1.0x; BU 60%; top multiplier 3.0; octave capacity not enforced; octaves 2; Phi tier on; phase-in 10 y; issuance cap 8%; indexation every year; protected account first $10,000; rent cap off: secU25X +0.27 in Reference, inflation 20.16 in Reference, gNonW +7.22 in Adverse, secU25X +0.30 in Adverse ...); `m6.4` (base tax 13%; progression 0.0 pts; cap 58%; business tax 0%; sales kept 50%; recycled 0%; business rate 2.3x; BU 60%; top multiplier 3.0; octave capacity 50%; octaves 2; Phi tier on; phase-in 10 y; issuance cap 8%; indexation every year; protected account first $10,000; rent cap off: secU25X +0.22 in Reference, inflation 20.03 in Reference, gNonW +7.43 in Adverse, secU25X +0.25 in Adverse ...).

| Point | What it sets | Basket poverty | Wealth poverty | Participation | Inflation | On the front in | Fails |
|---|---|---|---|---|---|---|---|
| t0 | tax 0% | -32.98 | -24.28 | 100.0 | 40.44 | Reference, Adverse, Stress | 6: secU25X +1.69 in Reference; inflation 36.36 in Reference; secU25X +0.92 in Adverse ... |
| kp50 | Source keeps 50% of project sales | -32.57 | -23.48 | 100.0 | 33.07 | Reference, Adverse, Stress | 4: secU25X +0.27 in Reference; inflation 28.75 in Reference; inflation 33.37 in Adverse ... |
| svc | protected account, first $10,000 | -32.10 | -25.61 | 100.0 | 48.54 | Reference, Adverse, Stress | 4: secU25X +0.16 in Reference; inflation 41.43 in Reference; inflation 50.48 in Adverse ... |
| fflat | outside finance: flat wage contribution | -24.56 | -23.69 | 100.0 | 0.13 | Reference, Adverse, Stress | 3: secU25X +5.24 in Reference; secU25X +3.70 in Adverse; secU25X +1.43 in Stress |
| fland | outside finance: land-value tax | -23.47 | -26.17 | 100.0 | 5.43 | Reference, Adverse, Stress | 6: secU25X +2.81 in Reference; inflation 5.03 in Reference; secU25X +3.31 in Adverse ... |

### C2.2 design, wages 90%

255 candidates; 0 pass no harm in every environment; 0 of those keep inflation under 5 points a year. **No setting tested meets the rule.** Closest (by the summed excess of what fails): `fflat` (outside finance: flat wage contribution: secU25X +5.24 in Reference, secU25X +3.70 in Adverse, secU25X +1.43 in Stress); `fland` (outside finance: land-value tax: secU25X +3.21 in Reference, inflation 5.25 in Reference, secU25X +4.15 in Adverse, inflation 6.67 in Adverse ...); `kp50` (Source keeps 50% of project sales: secU25X +0.33 in Reference, inflation 33.97 in Reference, inflation 40.92 in Adverse, gNonW +21.46 in Stress ...); `t0` (tax 0%: secU25X +2.04 in Reference, inflation 43.79 in Reference, secU25X +1.20 in Adverse, inflation 51.85 in Adverse ...); `t4` (tax 4%: secU25X +0.92 in Reference, inflation 44.66 in Reference, gNonW +0.26 in Adverse, secU25X +0.26 in Adverse ...).

| Point | What it sets | Basket poverty | Wealth poverty | Participation | Inflation | On the front in | Fails |
|---|---|---|---|---|---|---|---|
| t0 | tax 0% | -31.73 | -5.19 | 100.0 | 49.84 | Reference, Adverse, Stress | 8: secU25X +2.04 in Reference; inflation 43.79 in Reference; secU25X +1.20 in Adverse ... |
| kp50 | Source keeps 50% of project sales | -31.06 | -5.81 | 100.0 | 41.11 | Reference, Adverse, Stress | 6: secU25X +0.33 in Reference; inflation 33.97 in Reference; inflation 40.92 in Adverse ... |
| svc | protected account, first $10,000 | -27.68 | -21.84 | 100.0 | 69.34 | Reference, Adverse, Stress | 4: secU25X +0.19 in Reference; inflation 54.37 in Reference; inflation 71.74 in Adverse ... |
| fflat | outside finance: flat wage contribution | -24.56 | -23.69 | 100.0 | 0.13 | Reference, Adverse, Stress | 3: secU25X +5.24 in Reference; secU25X +3.70 in Adverse; secU25X +1.43 in Stress |
| fland | outside finance: land-value tax | -21.70 | -25.93 | 100.0 | 5.85 | Reference, Adverse, Stress | 6: secU25X +3.21 in Reference; inflation 5.25 in Reference; secU25X +4.15 in Adverse ... |

