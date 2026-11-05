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

## Stage 3: confirmation on fresh seeds 51-100 (decision rule 5)

Each cell: the change against no programme, seed mean and 95% interval. Confirmed: basket poverty's interval below zero, each no-harm measure's upper end at or below +0.5 points, and inflation's upper end under 5 points a year (required for the chosen setting, reported for Pareto points), in every environment.

### release row, wages 100%

| Setting | Role | Environment | basket poverty, % of adult-years | non-participants' basket poverty, % | non-participants' wealth poverty, % | non-participants' income drops of 25%+ with no buffer, per 100 | non-participants under 3 months of basics covered, % | wealth poverty at year 20, % | programme inflation, points a year | participation, mean of years 1-19, % | Passes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| t0 | Pareto point | Reference | -31.74 (-32.19, -31.29) | -15.53 (-16.52, -14.56) | +26.80 (+25.19, +28.37) | +0.53 (+0.46, +0.60) | +23.03 (+21.95, +24.09) | +9.02 (+8.40, +9.64) | +52.65 (+52.27, +53.03) | +83.61 (+82.93, +84.26) | no (inflation) |
| t0 | Pareto point | Adverse | -38.13 (-38.65, -37.58) | -18.64 (-19.64, -17.62) | +44.29 (+42.98, +45.57) | +0.46 (+0.36, +0.56) | +27.04 (+26.23, +27.86) | +33.64 (+33.08, +34.15) | +62.88 (+62.36, +63.38) | +83.61 (+82.93, +84.27) | no (inflation) |
| t0 | Pareto point | Stress | -14.89 (-15.33, -14.44) | -5.09 (-5.52, -4.65) | +40.34 (+39.42, +41.28) | +0.78 (+0.72, +0.85) | +24.43 (+23.90, +24.96) | +31.90 (+31.23, +32.56) | +30.81 (+30.21, +31.40) | +43.10 (+42.22, +44.00) | no (inflation) |
| bt0 | Pareto point | Reference | -31.29 (-31.76, -30.83) | -14.65 (-15.64, -13.66) | +28.54 (+26.93, +30.16) | +0.64 (+0.56, +0.73) | +24.16 (+23.10, +25.16) | +10.06 (+9.41, +10.71) | +52.37 (+51.95, +52.76) | +83.00 (+82.32, +83.68) | no (inflation) |
| bt0 | Pareto point | Adverse | -37.53 (-38.08, -36.95) | -17.54 (-18.63, -16.51) | +44.58 (+43.28, +45.85) | +0.56 (+0.45, +0.67) | +27.79 (+27.04, +28.57) | +33.94 (+33.38, +34.44) | +62.67 (+62.12, +63.21) | +83.07 (+82.39, +83.75) | no (inflation) |
| bt0 | Pareto point | Stress | -14.76 (-15.21, -14.32) | -5.00 (-5.43, -4.55) | +40.24 (+39.31, +41.19) | +0.78 (+0.72, +0.84) | +24.35 (+23.82, +24.88) | +31.93 (+31.27, +32.56) | +30.51 (+29.91, +31.10) | +43.00 (+42.13, +43.89) | no (inflation) |
| t4 | Pareto point | Reference | -31.05 (-31.49, -30.59) | -14.97 (-15.96, -13.99) | +27.61 (+26.02, +29.17) | +0.52 (+0.45, +0.59) | +23.61 (+22.53, +24.66) | +10.08 (+9.47, +10.68) | +51.99 (+51.60, +52.37) | +83.48 (+82.81, +84.15) | no (inflation) |
| t4 | Pareto point | Adverse | -37.03 (-37.58, -36.48) | -17.69 (-18.71, -16.69) | +44.70 (+43.47, +45.94) | +0.44 (+0.33, +0.54) | +27.54 (+26.76, +28.33) | +34.45 (+33.88, +34.99) | +62.17 (+61.65, +62.68) | +83.48 (+82.81, +84.13) | no (inflation) |
| t4 | Pareto point | Stress | -14.47 (-14.91, -14.03) | -4.90 (-5.32, -4.47) | +40.00 (+39.07, +40.95) | +0.77 (+0.71, +0.83) | +24.20 (+23.67, +24.74) | +31.78 (+31.12, +32.44) | +30.06 (+29.46, +30.63) | +43.07 (+42.20, +43.97) | no (inflation) |
| ixn | Pareto point | Reference | -30.78 (-31.23, -30.34) | -16.23 (-17.20, -15.27) | +27.37 (+25.84, +28.87) | +0.62 (+0.54, +0.69) | +22.56 (+21.52, +23.66) | +11.24 (+10.63, +11.85) | +51.92 (+51.53, +52.29) | +84.84 (+84.20, +85.49) | no (inflation) |
| ixn | Pareto point | Adverse | -36.62 (-37.16, -36.06) | -19.41 (-20.41, -18.42) | +45.01 (+43.69, +46.33) | +0.51 (+0.40, +0.62) | +26.57 (+25.75, +27.39) | +35.87 (+35.31, +36.40) | +62.49 (+61.99, +62.99) | +85.08 (+84.44, +85.71) | no (inflation) |
| ixn | Pareto point | Stress | -13.19 (-13.60, -12.77) | -4.42 (-4.81, -4.01) | +38.88 (+37.94, +39.83) | +0.75 (+0.69, +0.81) | +23.27 (+22.77, +23.80) | +31.27 (+30.57, +31.98) | +27.38 (+26.82, +27.93) | +43.23 (+42.35, +44.13) | no (inflation) |
| t8 | Pareto point | Reference | -30.25 (-30.72, -29.79) | -14.17 (-15.16, -13.18) | +28.41 (+26.82, +29.95) | +0.54 (+0.47, +0.62) | +24.28 (+23.21, +25.30) | +11.01 (+10.40, +11.61) | +51.22 (+50.81, +51.60) | +83.22 (+82.53, +83.88) | no (inflation) |
| t8 | Pareto point | Adverse | -35.90 (-36.44, -35.32) | -16.74 (-17.79, -15.71) | +45.21 (+43.98, +46.41) | +0.45 (+0.36, +0.55) | +28.00 (+27.24, +28.79) | +35.18 (+34.60, +35.72) | +61.37 (+60.84, +61.89) | +83.25 (+82.57, +83.91) | no (inflation) |
| t8 | Pareto point | Stress | -14.09 (-14.52, -13.66) | -4.73 (-5.15, -4.30) | +39.71 (+38.81, +40.64) | +0.75 (+0.68, +0.82) | +23.93 (+23.40, +24.46) | +31.58 (+30.93, +32.22) | +29.26 (+28.68, +29.83) | +43.06 (+42.18, +43.96) | no (inflation) |
| rcap | Pareto point | Reference | -30.03 (-30.50, -29.55) | -13.79 (-14.80, -12.80) | +28.70 (+27.17, +30.25) | +0.54 (+0.46, +0.62) | +24.44 (+23.41, +25.43) | +11.20 (+10.60, +11.81) | +50.23 (+49.83, +50.61) | +83.06 (+82.38, +83.73) | no (inflation) |
| rcap | Pareto point | Adverse | -35.59 (-36.12, -35.02) | -16.32 (-17.37, -15.29) | +45.61 (+44.34, +46.84) | +0.45 (+0.35, +0.55) | +28.07 (+27.34, +28.82) | +35.76 (+35.16, +36.33) | +60.30 (+59.76, +60.82) | +83.13 (+82.45, +83.80) | no (inflation) |
| rcap | Pareto point | Stress | -13.17 (-13.58, -12.75) | -4.36 (-4.77, -3.94) | +38.73 (+37.80, +39.69) | +0.72 (+0.65, +0.78) | +23.12 (+22.60, +23.65) | +31.14 (+30.44, +31.84) | +27.17 (+26.61, +27.71) | +43.04 (+42.16, +43.93) | no (inflation) |
| pr0c75 | Pareto point | Reference | -29.78 (-30.24, -29.32) | -13.91 (-14.90, -12.96) | +28.07 (+26.57, +29.54) | +0.44 (+0.37, +0.51) | +24.28 (+23.24, +25.28) | +10.97 (+10.35, +11.58) | +50.63 (+50.24, +51.00) | +83.37 (+82.69, +84.02) | no (inflation) |
| pr0c75 | Pareto point | Adverse | -35.16 (-35.70, -34.61) | -16.37 (-17.40, -15.37) | +45.42 (+44.15, +46.65) | +0.38 (+0.28, +0.47) | +28.01 (+27.25, +28.77) | +35.63 (+35.02, +36.19) | +60.65 (+60.12, +61.15) | +83.38 (+82.70, +84.03) | no (inflation) |
| pr0c75 | Pareto point | Stress | -13.16 (-13.57, -12.74) | -4.38 (-4.78, -3.97) | +38.80 (+37.90, +39.74) | +0.72 (+0.66, +0.79) | +23.16 (+22.63, +23.69) | +31.17 (+30.48, +31.87) | +27.30 (+26.74, +27.83) | +43.05 (+42.17, +43.94) | no (inflation) |
| kp50 | Pareto point | Reference | -29.59 (-30.06, -29.12) | -13.60 (-14.60, -12.65) | +28.28 (+26.74, +29.83) | +0.54 (+0.46, +0.62) | +24.24 (+23.21, +25.23) | +10.91 (+10.32, +11.49) | +49.27 (+48.86, +49.65) | +83.08 (+82.40, +83.75) | no (inflation) |
| kp50 | Pareto point | Adverse | -34.96 (-35.51, -34.39) | -16.09 (-17.12, -15.08) | +45.42 (+44.17, +46.65) | +0.44 (+0.34, +0.54) | +27.99 (+27.27, +28.73) | +35.47 (+34.81, +36.05) | +59.40 (+58.86, +59.92) | +83.16 (+82.47, +83.82) | no (inflation) |
| kp50 | Pareto point | Stress | -13.12 (-13.53, -12.70) | -4.36 (-4.76, -3.94) | +38.69 (+37.75, +39.65) | +0.71 (+0.65, +0.78) | +23.05 (+22.54, +23.59) | +31.09 (+30.36, +31.80) | +27.10 (+26.55, +27.64) | +43.04 (+42.16, +43.93) | no (inflation) |
| mm9 | Pareto point | Reference | -29.48 (-29.95, -29.01) | -13.53 (-14.52, -12.57) | +28.93 (+27.38, +30.45) | +0.53 (+0.45, +0.60) | +24.73 (+23.69, +25.72) | +11.80 (+11.18, +12.41) | +50.47 (+50.06, +50.84) | +83.09 (+82.40, +83.76) | no (inflation) |
| mm9 | Pareto point | Adverse | -34.79 (-35.34, -34.22) | -15.95 (-16.98, -14.94) | +45.74 (+44.46, +46.96) | +0.44 (+0.34, +0.54) | +28.33 (+27.61, +29.07) | +36.13 (+35.56, +36.66) | +60.58 (+60.04, +61.11) | +83.16 (+82.47, +83.82) | no (inflation) |
| mm9 | Pareto point | Stress | -13.26 (-13.68, -12.84) | -4.40 (-4.81, -3.98) | +38.81 (+37.91, +39.75) | +0.73 (+0.66, +0.79) | +23.28 (+22.77, +23.81) | +30.98 (+30.30, +31.65) | +27.50 (+26.94, +28.05) | +43.04 (+42.16, +43.93) | no (inflation) |
| kp25 | Pareto point | Reference | -29.53 (-30.00, -29.07) | -13.57 (-14.56, -12.61) | +28.69 (+27.18, +30.19) | +0.53 (+0.45, +0.61) | +24.50 (+23.46, +25.49) | +11.32 (+10.72, +11.90) | +49.87 (+49.47, +50.25) | +83.09 (+82.40, +83.76) | no (inflation) |
| kp25 | Pareto point | Adverse | -34.87 (-35.42, -34.30) | -16.03 (-17.06, -15.02) | +45.61 (+44.34, +46.83) | +0.44 (+0.34, +0.54) | +28.16 (+27.44, +28.90) | +35.85 (+35.24, +36.42) | +60.00 (+59.46, +60.52) | +83.16 (+82.47, +83.82) | no (inflation) |
| kp25 | Pareto point | Stress | -13.11 (-13.52, -12.69) | -4.35 (-4.75, -3.93) | +38.73 (+37.79, +39.69) | +0.72 (+0.65, +0.78) | +23.09 (+22.57, +23.63) | +31.13 (+30.42, +31.84) | +27.13 (+26.58, +27.67) | +43.04 (+42.16, +43.93) | no (inflation) |
| kp10 | Pareto point | Reference | -29.50 (-29.97, -29.03) | -13.54 (-14.54, -12.59) | +28.89 (+27.36, +30.43) | +0.53 (+0.45, +0.60) | +24.65 (+23.61, +25.63) | +11.62 (+11.02, +12.21) | +50.23 (+49.83, +50.61) | +83.09 (+82.40, +83.76) | no (inflation) |
| kp10 | Pareto point | Adverse | -34.82 (-35.37, -34.25) | -15.99 (-17.02, -14.98) | +45.67 (+44.40, +46.88) | +0.44 (+0.34, +0.54) | +28.26 (+27.55, +29.00) | +36.01 (+35.42, +36.55) | +60.35 (+59.81, +60.88) | +83.16 (+82.47, +83.82) | no (inflation) |
| kp10 | Pareto point | Stress | -13.11 (-13.52, -12.69) | -4.35 (-4.75, -3.93) | +38.73 (+37.80, +39.69) | +0.72 (+0.65, +0.78) | +23.11 (+22.60, +23.65) | +31.14 (+30.44, +31.84) | +27.15 (+26.59, +27.69) | +43.04 (+42.16, +43.93) | no (inflation) |
| phi0 | Pareto point | Reference | -29.41 (-29.87, -28.94) | -13.50 (-14.50, -12.56) | +29.02 (+27.52, +30.54) | +0.52 (+0.44, +0.59) | +24.77 (+23.74, +25.76) | +11.94 (+11.33, +12.55) | +50.51 (+50.11, +50.89) | +83.10 (+82.42, +83.77) | no (inflation) |
| phi0 | Pareto point | Adverse | -34.70 (-35.24, -34.14) | -15.93 (-16.97, -14.92) | +45.80 (+44.53, +47.02) | +0.44 (+0.34, +0.53) | +28.38 (+27.66, +29.12) | +36.20 (+35.64, +36.72) | +60.65 (+60.11, +61.17) | +83.17 (+82.49, +83.83) | no (inflation) |
| phi0 | Pareto point | Stress | -13.07 (-13.48, -12.64) | -4.32 (-4.72, -3.91) | +38.76 (+37.82, +39.73) | +0.71 (+0.65, +0.78) | +23.12 (+22.60, +23.65) | +31.17 (+30.46, +31.87) | +27.09 (+26.53, +27.63) | +43.04 (+42.16, +43.93) | no (inflation) |
| mm6 | Pareto point | Reference | -29.09 (-29.57, -28.62) | -13.39 (-14.38, -12.43) | +29.32 (+27.79, +30.83) | +0.49 (+0.41, +0.55) | +24.95 (+23.95, +25.93) | +12.73 (+12.11, +13.38) | +50.29 (+49.89, +50.69) | +83.15 (+82.46, +83.81) | no (inflation) |
| mm6 | Pareto point | Adverse | -34.27 (-34.83, -33.70) | -15.71 (-16.73, -14.69) | +45.99 (+44.72, +47.19) | +0.43 (+0.33, +0.52) | +28.58 (+27.87, +29.30) | +36.52 (+36.00, +37.00) | +60.58 (+60.03, +61.11) | +83.20 (+82.51, +83.86) | no (inflation) |
| mm6 | Pareto point | Stress | -13.11 (-13.52, -12.69) | -4.34 (-4.75, -3.93) | +38.73 (+37.80, +39.69) | +0.72 (+0.65, +0.78) | +23.13 (+22.61, +23.66) | +31.14 (+30.44, +31.84) | +27.16 (+26.61, +27.70) | +43.04 (+42.16, +43.93) | no (inflation) |
| mm3 | Pareto point | Reference | -28.55 (-29.02, -28.09) | -13.15 (-14.14, -12.16) | +29.96 (+28.46, +31.42) | +0.45 (+0.38, +0.51) | +25.32 (+24.32, +26.29) | +14.04 (+13.37, +14.68) | +50.12 (+49.71, +50.52) | +83.23 (+82.56, +83.89) | no (inflation) |
| mm3 | Pareto point | Adverse | -33.54 (-34.09, -32.97) | -15.38 (-16.39, -14.36) | +46.18 (+44.95, +47.41) | +0.37 (+0.28, +0.46) | +28.94 (+28.24, +29.67) | +37.08 (+36.54, +37.59) | +60.65 (+60.09, +61.19) | +83.29 (+82.61, +83.95) | no (inflation) |
| mm3 | Pareto point | Stress | -12.87 (-13.28, -12.45) | -4.23 (-4.63, -3.83) | +38.69 (+37.78, +39.66) | +0.71 (+0.65, +0.77) | +22.98 (+22.47, +23.50) | +31.45 (+30.70, +32.19) | +26.68 (+26.12, +27.22) | +43.04 (+42.16, +43.93) | no (inflation) |
| ex0 | Pareto point | Reference | -28.34 (-28.80, -27.89) | -13.41 (-14.38, -12.48) | +30.70 (+29.18, +32.21) | +0.38 (+0.30, +0.45) | +25.47 (+24.43, +26.49) | +15.49 (+14.86, +16.12) | +51.81 (+51.41, +52.20) | +83.43 (+82.74, +84.09) | no (inflation) |
| ex0 | Pareto point | Adverse | -33.35 (-33.90, -32.77) | -15.61 (-16.59, -14.65) | +46.52 (+45.31, +47.77) | +0.31 (+0.21, +0.41) | +28.96 (+28.25, +29.69) | +37.90 (+37.38, +38.42) | +62.12 (+61.57, +62.65) | +83.43 (+82.74, +84.09) | no (inflation) |
| ex0 | Pareto point | Stress | -13.10 (-13.51, -12.68) | -4.34 (-4.75, -3.93) | +38.76 (+37.84, +39.72) | +0.72 (+0.65, +0.78) | +23.14 (+22.62, +23.67) | +31.18 (+30.46, +31.88) | +27.17 (+26.61, +27.71) | +43.04 (+42.16, +43.94) | no (inflation) |
| ph5 | Pareto point | Reference | -28.11 (-28.56, -27.65) | -12.90 (-13.83, -11.98) | +28.56 (+27.03, +30.08) | +0.43 (+0.36, +0.51) | +23.93 (+22.96, +24.87) | +11.42 (+10.80, +12.05) | +48.55 (+48.16, +48.93) | +83.11 (+82.43, +83.78) | no (inflation) |
| ph5 | Pareto point | Adverse | -33.41 (-33.96, -32.85) | -15.34 (-16.35, -14.35) | +45.82 (+44.55, +47.02) | +0.33 (+0.23, +0.42) | +27.65 (+26.96, +28.35) | +36.19 (+35.59, +36.74) | +58.51 (+57.99, +59.02) | +83.18 (+82.50, +83.85) | no (inflation) |
| ph5 | Pareto point | Stress | -12.69 (-13.09, -12.28) | -4.34 (-4.74, -3.93) | +37.75 (+36.86, +38.65) | +0.66 (+0.59, +0.72) | +21.54 (+21.06, +22.05) | +30.18 (+29.51, +30.86) | +25.78 (+25.25, +26.30) | +43.04 (+42.16, +43.94) | no (inflation) |
| svc | Pareto point | Reference | -28.59 (-29.07, -28.13) | -12.79 (-13.79, -11.82) | +11.76 (+10.25, +13.23) | +0.51 (+0.43, +0.58) | +18.17 (+16.99, +19.35) | -5.88 (-6.41, -5.32) | +59.55 (+59.04, +60.04) | +83.13 (+82.44, +83.80) | no (inflation) |
| svc | Pareto point | Adverse | -32.87 (-33.41, -32.32) | -14.62 (-15.59, -13.63) | +25.67 (+24.28, +27.06) | +0.45 (+0.35, +0.55) | +20.92 (+19.95, +21.93) | +6.63 (+5.86, +7.42) | +74.72 (+73.99, +75.43) | +83.20 (+82.52, +83.86) | no (inflation) |
| svc | Pareto point | Stress | -12.49 (-12.91, -12.08) | -3.85 (-4.24, -3.44) | +32.61 (+31.85, +33.39) | +0.75 (+0.69, +0.82) | +22.06 (+21.58, +22.54) | +23.28 (+22.69, +23.87) | +32.71 (+32.03, +33.37) | +43.04 (+42.16, +43.93) | no (inflation) |
| bt25 | Pareto point | Reference | -27.12 (-27.58, -26.67) | -12.16 (-13.13, -11.23) | +29.84 (+28.45, +31.25) | +0.45 (+0.38, +0.52) | +25.37 (+24.36, +26.35) | +14.23 (+13.66, +14.83) | +48.28 (+47.90, +48.66) | +83.24 (+82.56, +83.89) | no (inflation) |
| bt25 | Pareto point | Adverse | -31.50 (-32.05, -30.94) | -14.13 (-15.10, -13.18) | +46.85 (+45.67, +47.99) | +0.40 (+0.31, +0.49) | +28.89 (+28.19, +29.63) | +38.26 (+37.74, +38.78) | +58.22 (+57.70, +58.72) | +83.30 (+82.62, +83.96) | no (inflation) |
| bt25 | Pareto point | Stress | -12.50 (-12.89, -12.10) | -4.12 (-4.50, -3.72) | +37.83 (+36.93, +38.74) | +0.70 (+0.63, +0.76) | +22.55 (+22.05, +23.08) | +30.64 (+29.92, +31.36) | +25.74 (+25.20, +26.26) | +43.04 (+42.16, +43.94) | no (inflation) |
| t25 | Pareto point | Reference | -26.77 (-27.22, -26.31) | -11.88 (-12.83, -10.96) | +30.23 (+28.81, +31.68) | +0.55 (+0.47, +0.62) | +25.53 (+24.51, +26.52) | +14.80 (+14.20, +15.40) | +47.79 (+47.40, +48.17) | +82.73 (+82.06, +83.40) | no (inflation) |
| t25 | Pareto point | Adverse | -31.09 (-31.62, -30.53) | -13.78 (-14.73, -12.83) | +47.05 (+45.88, +48.21) | +0.47 (+0.38, +0.57) | +29.05 (+28.36, +29.77) | +38.42 (+37.88, +38.96) | +57.84 (+57.30, +58.35) | +82.95 (+82.28, +83.62) | no (inflation) |
| t25 | Pareto point | Stress | -12.44 (-12.83, -12.04) | -4.09 (-4.47, -3.70) | +37.80 (+36.89, +38.72) | +0.69 (+0.63, +0.76) | +22.50 (+22.00, +23.02) | +30.64 (+29.92, +31.36) | +25.60 (+25.07, +26.12) | +43.01 (+42.14, +43.91) | no (inflation) |
| ph10 | Pareto point | Reference | -26.35 (-26.77, -25.93) | -12.04 (-12.93, -11.18) | +28.23 (+26.75, +29.72) | +0.40 (+0.33, +0.47) | +23.39 (+22.42, +24.34) | +10.90 (+10.28, +11.51) | +45.99 (+45.62, +46.36) | +83.20 (+82.51, +83.87) | no (inflation) |
| ph10 | Pareto point | Adverse | -31.47 (-32.02, -30.92) | -14.32 (-15.31, -13.37) | +45.77 (+44.48, +46.96) | +0.31 (+0.21, +0.41) | +27.24 (+26.55, +27.91) | +35.95 (+35.30, +36.55) | +55.71 (+55.21, +56.20) | +83.25 (+82.57, +83.92) | no (inflation) |
| ph10 | Pareto point | Stress | -12.02 (-12.39, -11.64) | -4.19 (-4.57, -3.80) | +36.45 (+35.54, +37.35) | +0.59 (+0.52, +0.66) | +19.69 (+19.24, +20.17) | +28.80 (+28.08, +29.48) | +23.86 (+23.35, +24.35) | +43.04 (+42.16, +43.94) | no (inflation) |
| h100 | Pareto point | Reference | -25.13 (-25.56, -24.72) | -10.96 (-11.88, -10.09) | +13.86 (+12.32, +15.34) | +0.46 (+0.39, +0.53) | +18.61 (+17.49, +19.72) | -2.32 (-2.84, -1.80) | +53.69 (+53.20, +54.18) | +82.72 (+82.05, +83.38) | no (inflation) |
| h100 | Pareto point | Adverse | -28.71 (-29.25, -28.16) | -12.35 (-13.27, -11.43) | +28.39 (+27.15, +29.64) | +0.35 (+0.26, +0.44) | +21.80 (+20.90, +22.67) | +11.08 (+10.39, +11.78) | +68.55 (+67.84, +69.25) | +82.99 (+82.31, +83.66) | no (inflation) |
| h100 | Pareto point | Stress | -11.56 (-11.95, -11.18) | -3.67 (-4.04, -3.29) | +31.43 (+30.64, +32.29) | +0.67 (+0.61, +0.74) | +19.84 (+19.40, +20.29) | +22.54 (+21.93, +23.16) | +29.37 (+28.74, +29.98) | +43.00 (+42.12, +43.90) | no (inflation) |
| bu80 | Pareto point | Reference | -23.70 (-24.16, -23.28) | -10.46 (-11.37, -9.59) | +28.85 (+27.41, +30.33) | +0.41 (+0.34, +0.48) | +25.19 (+24.23, +26.15) | +14.90 (+14.23, +15.58) | +43.81 (+43.47, +44.14) | +83.40 (+82.72, +84.07) | no (inflation) |
| bu80 | Pareto point | Adverse | -27.58 (-28.12, -27.00) | -12.22 (-13.08, -11.30) | +46.08 (+44.87, +47.29) | +0.35 (+0.25, +0.45) | +28.92 (+28.24, +29.62) | +37.58 (+37.04, +38.10) | +52.30 (+51.85, +52.74) | +83.42 (+82.73, +84.08) | no (inflation) |
| bu80 | Pareto point | Stress | -11.15 (-11.54, -10.76) | -3.75 (-4.10, -3.39) | +35.06 (+34.15, +35.99) | +0.63 (+0.56, +0.69) | +20.55 (+20.08, +21.04) | +28.26 (+27.52, +28.94) | +22.20 (+21.74, +22.65) | +43.04 (+42.16, +43.94) | no (inflation) |
| h10 | Pareto point | Reference | -23.42 (-23.88, -22.99) | -11.83 (-12.65, -11.00) | +27.95 (+26.54, +29.43) | +0.39 (+0.32, +0.46) | +23.56 (+22.62, +24.53) | +16.13 (+15.47, +16.83) | +43.16 (+42.82, +43.48) | +85.20 (+84.57, +85.81) | no (inflation) |
| h10 | Pareto point | Adverse | -27.04 (-27.56, -26.50) | -13.52 (-14.30, -12.70) | +46.52 (+45.33, +47.78) | +0.41 (+0.32, +0.50) | +27.99 (+27.30, +28.68) | +38.98 (+38.42, +39.52) | +51.90 (+51.46, +52.33) | +85.07 (+84.42, +85.70) | no (inflation) |
| h10 | Pareto point | Stress | -11.24 (-11.64, -10.84) | -3.87 (-4.24, -3.50) | +34.96 (+34.05, +35.89) | +0.63 (+0.57, +0.70) | +20.36 (+19.90, +20.84) | +28.15 (+27.42, +28.86) | +22.18 (+21.71, +22.63) | +43.18 (+42.31, +44.08) | no (inflation) |
| h192 | Pareto point | Reference | -23.32 (-23.74, -22.92) | -10.25 (-11.11, -9.42) | +13.51 (+12.02, +14.99) | +0.37 (+0.31, +0.44) | +18.57 (+17.48, +19.61) | -2.02 (-2.59, -1.48) | +51.61 (+51.15, +52.05) | +83.27 (+82.59, +83.92) | no (inflation) |
| h192 | Pareto point | Adverse | -26.65 (-27.17, -26.12) | -11.57 (-12.47, -10.67) | +28.17 (+26.93, +29.44) | +0.28 (+0.19, +0.37) | +22.18 (+21.36, +22.98) | +11.36 (+10.70, +12.03) | +65.37 (+64.71, +66.02) | +83.33 (+82.65, +83.99) | no (inflation) |
| h192 | Pareto point | Stress | -11.19 (-11.58, -10.81) | -3.64 (-4.00, -3.26) | +30.65 (+29.84, +31.49) | +0.63 (+0.56, +0.70) | +18.92 (+18.50, +19.35) | +21.92 (+21.34, +22.51) | +28.05 (+27.45, +28.64) | +43.00 (+42.13, +43.90) | no (inflation) |
| br2 | Pareto point | Reference | -23.43 (-23.91, -23.00) | -10.05 (-10.94, -9.16) | +29.74 (+28.31, +31.23) | +0.41 (+0.34, +0.48) | +25.67 (+24.72, +26.61) | +16.44 (+15.76, +17.17) | +43.49 (+43.14, +43.83) | +83.42 (+82.73, +84.07) | no (inflation) |
| br2 | Pareto point | Adverse | -27.09 (-27.62, -26.53) | -11.78 (-12.63, -10.88) | +47.54 (+46.33, +48.79) | +0.35 (+0.26, +0.45) | +29.42 (+28.74, +30.12) | +40.27 (+39.72, +40.85) | +52.41 (+51.93, +52.88) | +83.42 (+82.74, +84.08) | no (inflation) |
| br2 | Pareto point | Stress | -10.53 (-10.90, -10.14) | -3.47 (-3.81, -3.11) | +34.09 (+33.22, +34.98) | +0.62 (+0.55, +0.68) | +19.83 (+19.36, +20.33) | +28.03 (+27.26, +28.75) | +20.86 (+20.41, +21.32) | +43.04 (+42.16, +43.94) | no (inflation) |
| h23 | Pareto point | Reference | -23.05 (-23.52, -22.62) | -9.74 (-10.60, -8.87) | +14.39 (+12.90, +15.81) | +0.39 (+0.32, +0.45) | +19.97 (+18.90, +21.01) | -0.57 (-1.11, -0.06) | +52.31 (+51.87, +52.75) | +83.39 (+82.70, +84.04) | no (inflation) |
| h23 | Pareto point | Adverse | -26.30 (-26.81, -25.76) | -11.16 (-12.02, -10.27) | +30.13 (+28.82, +31.45) | +0.33 (+0.24, +0.42) | +23.62 (+22.80, +24.45) | +14.54 (+13.92, +15.18) | +65.76 (+65.11, +66.40) | +83.39 (+82.71, +84.05) | no (inflation) |
| h23 | Pareto point | Stress | -11.02 (-11.42, -10.61) | -3.43 (-3.80, -3.06) | +31.26 (+30.46, +32.13) | +0.69 (+0.63, +0.76) | +20.40 (+19.96, +20.85) | +23.15 (+22.54, +23.77) | +28.25 (+27.66, +28.83) | +43.03 (+42.15, +43.92) | no (inflation) |
| bt50 | Pareto point | Reference | -22.77 (-23.25, -22.35) | -9.73 (-10.63, -8.85) | +29.61 (+28.17, +31.10) | +0.41 (+0.34, +0.48) | +25.62 (+24.67, +26.59) | +16.69 (+16.00, +17.40) | +42.31 (+41.97, +42.65) | +83.43 (+82.74, +84.08) | no (inflation) |
| bt50 | Pareto point | Adverse | -26.08 (-26.58, -25.57) | -11.14 (-11.98, -10.29) | +48.03 (+46.86, +49.25) | +0.38 (+0.29, +0.47) | +29.54 (+28.87, +30.24) | +40.98 (+40.36, +41.61) | +51.12 (+50.64, +51.59) | +83.43 (+82.74, +84.09) | no (inflation) |
| bt50 | Pareto point | Stress | -9.63 (-9.97, -9.28) | -2.75 (-3.04, -2.45) | +34.09 (+33.19, +34.98) | +0.71 (+0.64, +0.78) | +19.74 (+19.27, +20.25) | +28.27 (+27.48, +29.01) | +20.40 (+19.93, +20.84) | +43.04 (+42.16, +43.94) | no (inflation) |
| h119 | Pareto point | Reference | -21.01 (-21.43, -20.62) | -10.23 (-11.00, -9.45) | +27.01 (+25.59, +28.53) | +0.35 (+0.28, +0.42) | +22.37 (+21.47, +23.29) | +16.31 (+15.64, +16.99) | +37.79 (+37.47, +38.09) | +85.10 (+84.47, +85.72) | no (inflation) |
| h119 | Pareto point | Adverse | -23.94 (-24.42, -23.44) | -11.49 (-12.21, -10.73) | +47.32 (+46.11, +48.50) | +0.41 (+0.30, +0.50) | +27.38 (+26.73, +28.05) | +40.36 (+39.80, +40.95) | +46.31 (+45.89, +46.74) | +84.97 (+84.32, +85.60) | no (inflation) |
| h119 | Pareto point | Stress | -9.44 (-9.77, -9.09) | -3.25 (-3.55, -2.93) | +31.22 (+30.36, +32.08) | +0.53 (+0.48, +0.59) | +16.97 (+16.53, +17.43) | +25.54 (+24.80, +26.27) | +18.23 (+17.81, +18.64) | +43.15 (+42.28, +44.05) | no (inflation) |
| h4 | Pareto point | Reference | -21.08 (-21.54, -20.67) | -8.51 (-9.36, -7.67) | +15.61 (+14.18, +16.95) | +0.39 (+0.32, +0.46) | +20.30 (+19.31, +21.30) | +2.54 (+2.02, +3.06) | +47.76 (+47.32, +48.20) | +83.37 (+82.70, +84.03) | no (inflation) |
| h4 | Pareto point | Adverse | -23.80 (-24.28, -23.30) | -9.85 (-10.64, -9.03) | +32.81 (+31.61, +34.05) | +0.33 (+0.24, +0.42) | +24.30 (+23.50, +25.12) | +19.49 (+18.86, +20.14) | +60.80 (+60.16, +61.44) | +83.38 (+82.70, +84.03) | no (inflation) |
| h4 | Pareto point | Stress | -9.02 (-9.33, -8.70) | -2.46 (-2.75, -2.17) | +30.50 (+29.60, +31.39) | +0.70 (+0.63, +0.76) | +18.89 (+18.46, +19.34) | +23.99 (+23.23, +24.70) | +24.20 (+23.66, +24.71) | +43.02 (+42.14, +43.91) | no (inflation) |
| h141 | Pareto point | Reference | -19.92 (-20.32, -19.55) | -8.21 (-9.01, -7.43) | +14.94 (+13.53, +16.24) | +0.37 (+0.30, +0.44) | +19.43 (+18.46, +20.41) | +2.12 (+1.64, +2.58) | +44.30 (+43.90, +44.69) | +83.41 (+82.73, +84.07) | no (inflation) |
| h141 | Pareto point | Adverse | -22.50 (-23.00, -22.00) | -9.37 (-10.13, -8.57) | +32.43 (+31.22, +33.66) | +0.31 (+0.21, +0.40) | +23.72 (+22.98, +24.48) | +19.24 (+18.62, +19.88) | +56.17 (+55.59, +56.75) | +83.41 (+82.73, +84.07) | no (inflation) |
| h141 | Pareto point | Stress | -9.44 (-9.78, -9.09) | -3.00 (-3.33, -2.65) | +28.87 (+27.99, +29.80) | +0.59 (+0.53, +0.65) | +17.52 (+17.11, +17.95) | +21.87 (+21.17, +22.54) | +23.36 (+22.84, +23.86) | +43.04 (+42.17, +43.94) | no (inflation) |
| h126 | Pareto point | Reference | -19.50 (-19.88, -19.13) | -8.32 (-9.06, -7.59) | +13.86 (+12.48, +15.18) | +0.37 (+0.30, +0.44) | +18.43 (+17.51, +19.35) | +0.80 (+0.28, +1.26) | +42.06 (+41.71, +42.40) | +83.41 (+82.73, +84.06) | no (inflation) |
| h126 | Pareto point | Adverse | -22.19 (-22.68, -21.70) | -9.48 (-10.21, -8.72) | +31.65 (+30.44, +32.90) | +0.32 (+0.22, +0.41) | +23.04 (+22.31, +23.78) | +18.18 (+17.56, +18.79) | +52.66 (+52.16, +53.17) | +83.41 (+82.72, +84.07) | no (inflation) |
| h126 | Pareto point | Stress | -9.38 (-9.70, -9.04) | -3.06 (-3.37, -2.73) | +27.94 (+27.05, +28.85) | +0.58 (+0.52, +0.64) | +16.92 (+16.52, +17.33) | +20.64 (+20.02, +21.23) | +22.82 (+22.34, +23.29) | +43.04 (+42.17, +43.94) | no (inflation) |
| bu60 | Pareto point | Reference | -19.50 (-19.89, -19.13) | -8.65 (-9.41, -7.90) | +25.50 (+24.06, +26.94) | +0.39 (+0.33, +0.46) | +23.21 (+22.30, +24.14) | +13.73 (+13.08, +14.37) | +34.42 (+34.15, +34.69) | +83.43 (+82.74, +84.09) | no (inflation) |
| bu60 | Pareto point | Adverse | -22.56 (-23.04, -22.06) | -10.11 (-10.83, -9.34) | +44.14 (+42.86, +45.41) | +0.39 (+0.30, +0.49) | +27.74 (+27.07, +28.43) | +35.44 (+34.84, +36.01) | +40.95 (+40.59, +41.30) | +83.43 (+82.74, +84.09) | no (inflation) |
| bu60 | Pareto point | Stress | -8.89 (-9.19, -8.56) | -3.02 (-3.30, -2.71) | +29.29 (+28.52, +30.04) | +0.52 (+0.46, +0.58) | +16.83 (+16.42, +17.25) | +23.76 (+23.10, +24.44) | +17.04 (+16.68, +17.40) | +43.04 (+42.16, +43.94) | no (inflation) |
| m9.6 | Pareto point | Reference | -18.99 (-19.36, -18.64) | -9.19 (-9.89, -8.52) | +12.59 (+11.22, +13.92) | +0.34 (+0.27, +0.40) | +16.79 (+15.93, +17.68) | +1.04 (+0.52, +1.49) | +40.53 (+40.20, +40.85) | +85.01 (+84.37, +85.63) | no (inflation) |
| m9.6 | Pareto point | Adverse | -21.34 (-21.81, -20.86) | -10.08 (-10.74, -9.37) | +31.21 (+29.98, +32.47) | +0.38 (+0.28, +0.48) | +21.89 (+21.15, +22.64) | +18.52 (+17.89, +19.17) | +50.95 (+50.50, +51.41) | +84.80 (+84.15, +85.44) | no (inflation) |
| m9.6 | Pareto point | Stress | -8.79 (-9.09, -8.48) | -2.89 (-3.17, -2.60) | +26.77 (+25.90, +27.62) | +0.54 (+0.48, +0.60) | +15.71 (+15.33, +16.11) | +19.94 (+19.28, +20.59) | +21.18 (+20.73, +21.62) | +43.20 (+42.33, +44.10) | no (inflation) |
| br1 | Pareto point | Reference | -19.08 (-19.48, -18.71) | -7.93 (-8.70, -7.16) | +26.56 (+25.07, +28.08) | +0.43 (+0.36, +0.50) | +24.17 (+23.23, +25.12) | +15.67 (+14.99, +16.35) | +34.28 (+33.98, +34.57) | +83.43 (+82.74, +84.09) | no (inflation) |
| br1 | Pareto point | Adverse | -21.35 (-21.82, -20.85) | -8.87 (-9.57, -8.13) | +47.04 (+45.81, +48.32) | +0.47 (+0.37, +0.57) | +28.94 (+28.28, +29.59) | +40.79 (+40.26, +41.35) | +41.33 (+40.94, +41.72) | +83.43 (+82.74, +84.09) | no (inflation) |
| br1 | Pareto point | Stress | -7.78 (-8.09, -7.46) | -2.57 (-2.84, -2.28) | +27.30 (+26.46, +28.11) | +0.49 (+0.43, +0.55) | +15.50 (+15.06, +15.96) | +23.02 (+22.28, +23.76) | +15.14 (+14.78, +15.51) | +43.04 (+42.16, +43.94) | no (inflation) |
| h50 | Pareto point | Reference | -18.73 (-19.11, -18.38) | -7.86 (-8.60, -7.13) | +26.29 (+24.83, +27.80) | +0.38 (+0.31, +0.44) | +22.41 (+21.52, +23.32) | +15.05 (+14.43, +15.68) | +33.13 (+32.83, +33.42) | +83.35 (+82.67, +84.01) | no (inflation) |
| h50 | Pareto point | Adverse | -21.32 (-21.83, -20.83) | -9.01 (-9.69, -8.29) | +46.52 (+45.29, +47.80) | +0.34 (+0.25, +0.43) | +27.45 (+26.81, +28.09) | +39.37 (+38.79, +39.96) | +40.61 (+40.20, +41.01) | +83.35 (+82.67, +84.01) | no (inflation) |
| h50 | Pareto point | Stress | -7.83 (-8.12, -7.54) | -2.46 (-2.71, -2.20) | +28.40 (+27.63, +29.17) | +0.50 (+0.45, +0.56) | +15.35 (+14.92, +15.78) | +23.68 (+22.96, +24.38) | +15.73 (+15.36, +16.09) | +42.99 (+42.11, +43.88) | no (inflation) |
| h89 | Pareto point | Reference | -18.30 (-18.66, -17.95) | -7.75 (-8.46, -7.02) | +25.72 (+24.34, +27.15) | +0.36 (+0.29, +0.42) | +22.18 (+21.29, +23.10) | +15.91 (+15.32, +16.51) | +31.86 (+31.58, +32.13) | +83.32 (+82.64, +83.98) | no (inflation) |
| h89 | Pareto point | Adverse | -20.61 (-21.11, -20.11) | -8.86 (-9.55, -8.12) | +45.84 (+44.53, +47.16) | +0.34 (+0.25, +0.43) | +27.39 (+26.76, +28.05) | +38.94 (+38.34, +39.58) | +39.01 (+38.62, +39.38) | +83.33 (+82.65, +83.98) | no (inflation) |
| h89 | Pareto point | Stress | -8.43 (-8.74, -8.11) | -2.90 (-3.18, -2.60) | +28.27 (+27.43, +29.08) | +0.47 (+0.42, +0.53) | +15.68 (+15.27, +16.10) | +23.44 (+22.68, +24.18) | +16.02 (+15.66, +16.37) | +42.97 (+42.10, +43.87) | no (inflation) |
| h132 | Pareto point | Reference | -17.38 (-17.76, -17.05) | -8.18 (-8.89, -7.49) | +26.07 (+24.64, +27.55) | +1.23 (+1.13, +1.33) | +22.80 (+21.86, +23.75) | +18.04 (+17.45, +18.68) | +31.74 (+31.46, +32.01) | +84.90 (+84.26, +85.52) | no (inflation) |
| h132 | Pareto point | Adverse | -18.88 (-19.32, -18.45) | -8.47 (-9.09, -7.79) | +46.80 (+45.47, +48.13) | +1.52 (+1.40, +1.65) | +28.64 (+27.99, +29.31) | +41.55 (+40.93, +42.19) | +39.17 (+38.79, +39.55) | +84.57 (+83.91, +85.21) | no (inflation) |
| h132 | Pareto point | Stress | -7.35 (-7.63, -7.05) | -2.41 (-2.66, -2.14) | +26.85 (+26.01, +27.68) | +0.80 (+0.73, +0.87) | +15.17 (+14.74, +15.63) | +22.92 (+22.18, +23.66) | +14.65 (+14.30, +15.00) | +43.15 (+42.28, +44.04) | no (inflation) |
| h41 | Pareto point | Reference | -17.10 (-17.48, -16.76) | -6.92 (-7.67, -6.16) | +26.02 (+24.59, +27.44) | +0.42 (+0.36, +0.49) | +23.17 (+22.26, +24.11) | +17.28 (+16.69, +17.87) | +31.11 (+30.82, +31.39) | +83.41 (+82.73, +84.07) | no (inflation) |
| h41 | Pareto point | Adverse | -18.93 (-19.39, -18.46) | -7.73 (-8.38, -7.04) | +46.67 (+45.36, +48.00) | +0.45 (+0.35, +0.55) | +28.55 (+27.91, +29.22) | +41.07 (+40.49, +41.69) | +38.46 (+38.06, +38.85) | +83.41 (+82.73, +84.07) | no (inflation) |
| h41 | Pareto point | Stress | -7.13 (-7.41, -6.84) | -2.23 (-2.47, -1.98) | +26.57 (+25.72, +27.41) | +0.48 (+0.43, +0.54) | +14.92 (+14.49, +15.36) | +22.74 (+22.00, +23.48) | +14.41 (+14.06, +14.76) | +43.04 (+42.17, +43.94) | no (inflation) |
| m3.4 | Pareto point | Reference | -17.08 (-17.44, -16.75) | -6.75 (-7.47, -6.01) | +16.30 (+15.00, +17.60) | +0.42 (+0.36, +0.49) | +19.92 (+19.00, +20.85) | +6.46 (+5.93, +6.98) | +37.30 (+36.97, +37.64) | +83.43 (+82.74, +84.08) | no (inflation) |
| m3.4 | Pareto point | Adverse | -18.70 (-19.16, -18.23) | -7.48 (-8.13, -6.80) | +36.02 (+34.77, +37.27) | +0.43 (+0.33, +0.54) | +25.05 (+24.32, +25.77) | +26.98 (+26.38, +27.60) | +47.32 (+46.83, +47.81) | +83.43 (+82.74, +84.08) | no (inflation) |
| m3.4 | Pareto point | Stress | -7.32 (-7.62, -7.01) | -2.12 (-2.37, -1.85) | +25.89 (+25.16, +26.67) | +0.57 (+0.51, +0.63) | +15.90 (+15.49, +16.34) | +20.79 (+20.11, +21.48) | +18.92 (+18.48, +19.34) | +43.05 (+42.18, +43.95) | no (inflation) |
| h154 | Pareto point | Reference | -17.26 (-17.62, -16.93) | -8.29 (-8.99, -7.61) | +23.64 (+22.34, +24.98) | +0.35 (+0.29, +0.41) | +20.48 (+19.58, +21.39) | +15.55 (+15.04, +16.09) | +29.69 (+29.44, +29.93) | +84.71 (+84.07, +85.34) | no (inflation) |
| h154 | Pareto point | Adverse | -18.84 (-19.31, -18.39) | -8.66 (-9.26, -8.02) | +45.31 (+43.99, +46.65) | +0.50 (+0.41, +0.60) | +26.55 (+25.92, +27.20) | +38.80 (+38.20, +39.43) | +36.40 (+36.06, +36.74) | +84.37 (+83.71, +85.01) | no (inflation) |
| h154 | Pareto point | Stress | -6.84 (-7.13, -6.57) | -2.06 (-2.28, -1.84) | +25.95 (+25.20, +26.69) | +0.50 (+0.44, +0.55) | +14.23 (+13.84, +14.63) | +21.90 (+21.23, +22.58) | +14.02 (+13.70, +14.33) | +43.02 (+42.15, +43.92) | no (inflation) |
| m0.0 | Pareto point | Reference | -16.76 (-17.11, -16.43) | -6.94 (-7.65, -6.25) | +15.37 (+14.06, +16.69) | +0.42 (+0.35, +0.48) | +18.88 (+17.98, +19.78) | +5.61 (+5.08, +6.12) | +35.52 (+35.20, +35.82) | +83.47 (+82.79, +84.13) | no (inflation) |
| m0.0 | Pareto point | Adverse | -18.40 (-18.87, -17.92) | -7.63 (-8.26, -6.95) | +34.84 (+33.67, +36.07) | +0.42 (+0.32, +0.52) | +24.20 (+23.51, +24.87) | +25.40 (+24.79, +26.00) | +44.78 (+44.34, +45.22) | +83.47 (+82.78, +84.13) | no (inflation) |
| m0.0 | Pareto point | Stress | -7.66 (-7.97, -7.35) | -2.41 (-2.67, -2.11) | +25.43 (+24.70, +26.17) | +0.54 (+0.47, +0.60) | +15.47 (+15.07, +15.86) | +19.92 (+19.29, +20.56) | +18.89 (+18.48, +19.29) | +43.11 (+42.23, +44.01) | no (inflation) |
| h138 | Pareto point | Reference | -16.51 (-16.83, -16.20) | -7.13 (-7.78, -6.47) | +13.64 (+12.41, +14.83) | +0.36 (+0.29, +0.42) | +17.17 (+16.31, +18.02) | +2.74 (+2.28, +3.17) | +33.41 (+33.13, +33.69) | +83.36 (+82.68, +84.01) | no (inflation) |
| h138 | Pareto point | Adverse | -18.49 (-18.97, -17.99) | -7.93 (-8.56, -7.24) | +32.51 (+31.31, +33.75) | +0.35 (+0.26, +0.44) | +22.69 (+22.06, +23.33) | +20.88 (+20.28, +21.50) | +41.88 (+41.48, +42.28) | +83.36 (+82.68, +84.01) | no (inflation) |
| h138 | Pareto point | Stress | -7.55 (-7.85, -7.25) | -2.46 (-2.73, -2.18) | +24.55 (+23.87, +25.25) | +0.48 (+0.42, +0.54) | +14.43 (+14.05, +14.81) | +18.92 (+18.32, +19.51) | +18.25 (+17.85, +18.62) | +43.00 (+42.13, +43.89) | no (inflation) |
| h130 | Pareto point | Reference | -17.10 (-17.49, -16.76) | -7.78 (-8.52, -7.08) | +16.08 (+14.80, +17.37) | +0.92 (+0.83, +1.00) | +19.51 (+18.59, +20.45) | +7.51 (+7.02, +8.03) | +38.33 (+37.97, +38.68) | +84.92 (+84.29, +85.54) | no (inflation) |
| h130 | Pareto point | Adverse | -18.41 (-18.83, -17.99) | -7.93 (-8.55, -7.28) | +37.03 (+35.82, +38.28) | +1.15 (+1.05, +1.26) | +24.88 (+24.10, +25.65) | +28.74 (+28.17, +29.32) | +49.38 (+48.87, +49.90) | +84.66 (+84.00, +85.29) | no (inflation) |
| h130 | Pareto point | Stress | -6.82 (-7.09, -6.55) | -1.91 (-2.14, -1.66) | +25.79 (+25.04, +26.56) | +0.76 (+0.69, +0.83) | +15.65 (+15.23, +16.09) | +21.45 (+20.74, +22.13) | +18.24 (+17.81, +18.66) | +43.15 (+42.28, +44.04) | no (inflation) |
| h164 | Pareto point | Reference | -16.38 (-16.78, -16.04) | -7.58 (-8.30, -6.88) | +25.19 (+23.73, +26.65) | +0.48 (+0.42, +0.54) | +22.04 (+21.12, +23.00) | +17.56 (+16.96, +18.20) | +30.13 (+29.84, +30.41) | +84.86 (+84.22, +85.49) | no (inflation) |
| h164 | Pareto point | Adverse | -17.88 (-18.31, -17.45) | -7.87 (-8.49, -7.21) | +46.54 (+45.20, +47.88) | +0.65 (+0.55, +0.75) | +28.16 (+27.51, +28.82) | +41.28 (+40.65, +41.91) | +37.68 (+37.28, +38.07) | +84.54 (+83.87, +85.18) | no (inflation) |
| h164 | Pareto point | Stress | -7.42 (-7.70, -7.14) | -2.44 (-2.69, -2.18) | +26.61 (+25.76, +27.47) | +0.77 (+0.70, +0.83) | +15.06 (+14.63, +15.51) | +22.78 (+22.01, +23.56) | +14.51 (+14.17, +14.85) | +43.18 (+42.30, +44.08) | no (inflation) |
| h46 | Pareto point | Reference | -16.60 (-16.97, -16.26) | -7.42 (-8.14, -6.72) | +16.27 (+14.95, +17.60) | +0.46 (+0.39, +0.53) | +19.66 (+18.72, +20.62) | +8.03 (+7.55, +8.53) | +37.69 (+37.33, +38.03) | +84.81 (+84.17, +85.44) | no (inflation) |
| h46 | Pareto point | Adverse | -17.95 (-18.36, -17.54) | -7.68 (-8.29, -7.04) | +37.05 (+35.85, +38.28) | +0.59 (+0.48, +0.69) | +25.04 (+24.28, +25.80) | +28.89 (+28.32, +29.46) | +48.33 (+47.84, +48.84) | +84.54 (+83.88, +85.18) | no (inflation) |
| h46 | Pareto point | Stress | -6.86 (-7.13, -6.56) | -1.95 (-2.20, -1.70) | +25.52 (+24.77, +26.29) | +0.55 (+0.49, +0.62) | +15.46 (+15.03, +15.90) | +21.11 (+20.41, +21.80) | +18.01 (+17.59, +18.43) | +43.11 (+42.23, +44.00) | no (inflation) |
| h20 | Pareto point | Reference | -16.30 (-16.63, -16.00) | -6.83 (-7.51, -6.16) | +14.65 (+13.41, +15.93) | +0.37 (+0.31, +0.43) | +18.02 (+17.13, +18.91) | +4.64 (+4.16, +5.10) | +33.44 (+33.15, +33.73) | +83.28 (+82.59, +83.94) | no (inflation) |
| h20 | Pareto point | Adverse | -17.87 (-18.35, -17.38) | -7.50 (-8.13, -6.83) | +34.31 (+33.11, +35.55) | +0.40 (+0.31, +0.48) | +23.62 (+22.95, +24.26) | +24.68 (+24.07, +25.30) | +42.09 (+41.67, +42.51) | +83.28 (+82.60, +83.94) | no (inflation) |
| h20 | Pareto point | Stress | -7.10 (-7.38, -6.81) | -2.17 (-2.42, -1.90) | +24.38 (+23.71, +25.07) | +0.51 (+0.44, +0.57) | +14.67 (+14.28, +15.06) | +19.35 (+18.75, +19.95) | +17.69 (+17.30, +18.07) | +42.96 (+42.08, +43.85) | no (inflation) |
| h61 | Pareto point | Reference | -16.14 (-16.46, -15.83) | -6.94 (-7.60, -6.31) | +23.02 (+21.70, +24.37) | +0.35 (+0.29, +0.41) | +19.91 (+19.07, +20.80) | +14.09 (+13.52, +14.67) | +27.72 (+27.47, +27.96) | +83.25 (+82.57, +83.91) | no (inflation) |
| h61 | Pareto point | Adverse | -18.05 (-18.53, -17.56) | -7.81 (-8.44, -7.15) | +44.47 (+43.13, +45.79) | +0.34 (+0.26, +0.42) | +25.56 (+24.95, +26.17) | +37.52 (+36.98, +38.08) | +34.09 (+33.75, +34.43) | +83.26 (+82.58, +83.92) | no (inflation) |
| h61 | Pareto point | Stress | -6.92 (-7.19, -6.63) | -2.31 (-2.55, -2.08) | +24.36 (+23.61, +25.07) | +0.41 (+0.36, +0.45) | +13.08 (+12.71, +13.46) | +20.26 (+19.56, +20.93) | +13.45 (+13.13, +13.75) | +42.92 (+42.04, +43.82) | no (inflation) |
| m7.12 | Pareto point | Reference | -16.74 (-17.14, -16.40) | -7.56 (-8.29, -6.85) | +15.99 (+14.72, +17.30) | +0.57 (+0.49, +0.64) | +19.46 (+18.51, +20.40) | +7.38 (+6.87, +7.93) | +38.09 (+37.72, +38.45) | +84.92 (+84.29, +85.55) | no (inflation) |
| m7.12 | Pareto point | Adverse | -17.82 (-18.22, -17.43) | -7.50 (-8.11, -6.87) | +37.35 (+36.14, +38.60) | +0.86 (+0.75, +0.97) | +24.97 (+24.22, +25.73) | +28.98 (+28.36, +29.59) | +49.44 (+48.91, +49.99) | +84.66 (+84.00, +85.29) | no (inflation) |
| m7.12 | Pareto point | Stress | -6.42 (-6.69, -6.15) | -1.67 (-1.91, -1.43) | +25.69 (+24.94, +26.49) | +0.70 (+0.62, +0.77) | +15.50 (+15.06, +15.94) | +21.54 (+20.82, +22.23) | +17.96 (+17.52, +18.37) | +43.16 (+42.29, +44.06) | no (inflation) |
| m1.4 | Pareto point | Reference | -16.33 (-16.72, -16.00) | -7.32 (-8.05, -6.63) | +16.18 (+14.91, +17.47) | +0.47 (+0.40, +0.54) | +19.82 (+18.88, +20.78) | +7.96 (+7.48, +8.45) | +37.96 (+37.60, +38.32) | +84.91 (+84.27, +85.53) | no (inflation) |
| m1.4 | Pareto point | Adverse | -17.72 (-18.14, -17.30) | -7.53 (-8.13, -6.88) | +37.01 (+35.79, +38.26) | +0.62 (+0.51, +0.72) | +25.14 (+24.38, +25.90) | +28.76 (+28.19, +29.35) | +49.08 (+48.57, +49.60) | +84.64 (+83.99, +85.28) | no (inflation) |
| m1.4 | Pareto point | Stress | -6.77 (-7.05, -6.47) | -1.93 (-2.19, -1.66) | +25.89 (+25.13, +26.64) | +0.57 (+0.51, +0.63) | +15.70 (+15.26, +16.14) | +21.86 (+21.16, +22.55) | +18.11 (+17.70, +18.52) | +43.20 (+42.32, +44.10) | no (inflation) |
| h178 | Pareto point | Reference | -16.38 (-16.75, -16.07) | -7.42 (-8.11, -6.75) | +16.13 (+14.84, +17.45) | +0.93 (+0.84, +1.03) | +19.40 (+18.46, +20.35) | +7.79 (+7.28, +8.32) | +37.10 (+36.75, +37.44) | +84.81 (+84.17, +85.44) | no (inflation) |
| h178 | Pareto point | Adverse | -17.64 (-18.06, -17.21) | -7.57 (-8.18, -6.93) | +36.96 (+35.76, +38.19) | +1.16 (+1.04, +1.28) | +24.92 (+24.17, +25.66) | +28.81 (+28.26, +29.37) | +47.60 (+47.12, +48.10) | +84.51 (+83.85, +85.15) | no (inflation) |
| h178 | Pareto point | Stress | -6.64 (-6.91, -6.36) | -1.91 (-2.16, -1.65) | +25.00 (+24.26, +25.77) | +0.69 (+0.62, +0.75) | +15.12 (+14.69, +15.55) | +20.83 (+20.13, +21.51) | +17.56 (+17.15, +17.97) | +43.09 (+42.22, +43.98) | no (inflation) |
| m1.7 | Pareto point | Reference | -16.17 (-16.56, -15.83) | -7.24 (-7.97, -6.57) | +16.18 (+14.91, +17.47) | +0.46 (+0.39, +0.52) | +19.79 (+18.84, +20.75) | +7.92 (+7.44, +8.42) | +37.82 (+37.45, +38.17) | +84.91 (+84.26, +85.53) | no (inflation) |
| m1.7 | Pareto point | Adverse | -17.56 (-17.98, -17.14) | -7.46 (-8.07, -6.81) | +37.00 (+35.78, +38.26) | +0.60 (+0.50, +0.70) | +25.12 (+24.37, +25.87) | +28.74 (+28.17, +29.32) | +48.92 (+48.41, +49.45) | +84.63 (+83.97, +85.27) | no (inflation) |
| m1.7 | Pareto point | Stress | -6.71 (-7.00, -6.42) | -1.93 (-2.18, -1.66) | +25.76 (+24.99, +26.54) | +0.56 (+0.50, +0.62) | +15.59 (+15.16, +16.04) | +21.76 (+21.05, +22.47) | +18.03 (+17.62, +18.44) | +43.19 (+42.32, +44.09) | no (inflation) |
| m7.11 | Pareto point | Reference | -16.11 (-16.53, -15.77) | -7.19 (-7.91, -6.48) | +16.09 (+14.81, +17.36) | +0.44 (+0.38, +0.51) | +19.57 (+18.62, +20.54) | +7.77 (+7.29, +8.28) | +37.64 (+37.27, +38.01) | +84.89 (+84.25, +85.52) | no (inflation) |
| m7.11 | Pareto point | Adverse | -17.57 (-17.99, -17.16) | -7.43 (-8.05, -6.80) | +36.98 (+35.75, +38.24) | +0.59 (+0.49, +0.69) | +24.99 (+24.23, +25.74) | +28.69 (+28.11, +29.29) | +48.89 (+48.37, +49.43) | +84.63 (+83.97, +85.26) | no (inflation) |
| m7.11 | Pareto point | Stress | -6.29 (-6.55, -6.02) | -1.76 (-2.00, -1.51) | +25.13 (+24.37, +25.90) | +0.55 (+0.48, +0.61) | +15.26 (+14.83, +15.71) | +21.40 (+20.66, +22.11) | +17.45 (+17.04, +17.85) | +43.17 (+42.29, +44.06) | no (inflation) |
| h32 | Pareto point | Reference | -16.51 (-16.86, -16.19) | -6.90 (-7.58, -6.22) | +23.93 (+22.57, +25.29) | +0.37 (+0.31, +0.44) | +21.07 (+20.21, +21.99) | +15.37 (+14.84, +15.92) | +28.36 (+28.11, +28.61) | +83.43 (+82.74, +84.08) | no (inflation) |
| h32 | Pareto point | Adverse | -17.35 (-17.81, -16.90) | -6.82 (-7.41, -6.19) | +46.00 (+44.62, +47.39) | +0.50 (+0.40, +0.60) | +27.12 (+26.49, +27.75) | +40.20 (+39.50, +40.93) | +35.32 (+34.94, +35.71) | +83.43 (+82.74, +84.08) | no (inflation) |
| h32 | Pareto point | Stress | -6.17 (-6.44, -5.92) | -1.67 (-1.88, -1.46) | +24.64 (+23.84, +25.40) | +0.53 (+0.47, +0.60) | +13.61 (+13.21, +14.01) | +20.99 (+20.29, +21.70) | +13.16 (+12.83, +13.47) | +43.06 (+42.18, +43.95) | no (inflation) |
| h131 | Pareto point | Reference | -15.54 (-15.92, -15.21) | -6.34 (-7.06, -5.64) | +25.38 (+24.01, +26.76) | +0.42 (+0.35, +0.49) | +22.62 (+21.71, +23.58) | +17.48 (+16.90, +18.10) | +29.30 (+29.02, +29.58) | +83.46 (+82.77, +84.11) | no (inflation) |
| h131 | Pareto point | Adverse | -17.18 (-17.62, -16.75) | -6.90 (-7.53, -6.24) | +46.37 (+45.04, +47.71) | +0.45 (+0.35, +0.54) | +28.43 (+27.78, +29.10) | +41.07 (+40.43, +41.72) | +36.89 (+36.48, +37.29) | +83.46 (+82.77, +84.12) | no (inflation) |
| h131 | Pareto point | Stress | -6.58 (-6.85, -6.31) | -2.15 (-2.39, -1.89) | +25.21 (+24.35, +26.05) | +0.45 (+0.39, +0.50) | +14.32 (+13.91, +14.74) | +21.95 (+21.19, +22.68) | +13.57 (+13.24, +13.89) | +43.08 (+42.21, +43.98) | no (inflation) |
| h166 | Pareto point | Reference | -15.56 (-15.94, -15.22) | -6.36 (-7.08, -5.65) | +25.34 (+23.95, +26.71) | +0.43 (+0.36, +0.50) | +22.48 (+21.57, +23.42) | +17.39 (+16.80, +18.00) | +29.17 (+28.88, +29.45) | +83.46 (+82.78, +84.12) | no (inflation) |
| h166 | Pareto point | Adverse | -17.19 (-17.62, -16.76) | -6.92 (-7.55, -6.25) | +46.30 (+44.97, +47.64) | +0.45 (+0.35, +0.55) | +28.29 (+27.64, +28.97) | +41.00 (+40.36, +41.66) | +36.70 (+36.30, +37.10) | +83.46 (+82.77, +84.11) | no (inflation) |
| h166 | Pareto point | Stress | -6.57 (-6.84, -6.30) | -2.15 (-2.39, -1.89) | +25.10 (+24.23, +25.96) | +0.45 (+0.39, +0.50) | +14.17 (+13.76, +14.59) | +21.84 (+21.06, +22.62) | +13.48 (+13.15, +13.79) | +43.08 (+42.21, +43.98) | no (inflation) |
| h66 | Pareto point | Reference | -15.93 (-16.29, -15.61) | -7.10 (-7.79, -6.42) | +15.50 (+14.22, +16.81) | +0.44 (+0.38, +0.51) | +18.39 (+17.47, +19.35) | +7.20 (+6.68, +7.73) | +34.10 (+33.79, +34.39) | +84.66 (+84.02, +85.29) | no (inflation) |
| h66 | Pareto point | Adverse | -16.93 (-17.36, -16.49) | -7.22 (-7.81, -6.60) | +36.78 (+35.61, +38.05) | +0.61 (+0.51, +0.71) | +24.35 (+23.65, +25.05) | +29.05 (+28.48, +29.62) | +43.09 (+42.67, +43.52) | +84.36 (+83.70, +84.99) | no (inflation) |
| h66 | Pareto point | Stress | -6.45 (-6.74, -6.14) | -1.90 (-2.14, -1.65) | +23.51 (+22.74, +24.27) | +0.50 (+0.45, +0.56) | +14.10 (+13.68, +14.52) | +19.08 (+18.39, +19.76) | +16.52 (+16.12, +16.90) | +43.05 (+42.18, +43.95) | no (inflation) |
| h102 | Pareto point | Reference | -15.71 (-16.08, -15.38) | -7.27 (-7.96, -6.61) | +23.92 (+22.54, +25.30) | +0.59 (+0.52, +0.66) | +21.06 (+20.17, +22.00) | +16.58 (+16.03, +17.18) | +27.91 (+27.65, +28.16) | +84.69 (+84.04, +85.32) | no (inflation) |
| h102 | Pareto point | Adverse | -16.84 (-17.26, -16.43) | -7.42 (-8.01, -6.79) | +45.19 (+43.85, +46.56) | +0.78 (+0.68, +0.89) | +27.30 (+26.65, +27.97) | +39.94 (+39.34, +40.56) | +34.60 (+34.25, +34.95) | +84.34 (+83.68, +84.98) | no (inflation) |
| h102 | Pareto point | Stress | -6.58 (-6.85, -6.31) | -2.19 (-2.43, -1.94) | +24.09 (+23.31, +24.87) | +0.55 (+0.50, +0.61) | +13.64 (+13.24, +14.04) | +20.78 (+20.10, +21.46) | +12.94 (+12.63, +13.23) | +43.07 (+42.19, +43.96) | no (inflation) |
| h153 | Pareto point | Reference | -15.74 (-16.13, -15.41) | -7.26 (-7.94, -6.59) | +24.87 (+23.46, +26.31) | +0.42 (+0.35, +0.48) | +21.84 (+20.92, +22.81) | +17.37 (+16.76, +18.02) | +29.02 (+28.74, +29.29) | +84.81 (+84.16, +85.43) | no (inflation) |
| h153 | Pareto point | Adverse | -17.08 (-17.50, -16.67) | -7.49 (-8.12, -6.87) | +45.90 (+44.56, +47.28) | +0.59 (+0.49, +0.68) | +28.07 (+27.41, +28.74) | +40.72 (+40.10, +41.36) | +36.15 (+35.78, +36.52) | +84.46 (+83.80, +85.10) | no (inflation) |
| h153 | Pareto point | Stress | -6.38 (-6.64, -6.12) | -2.09 (-2.32, -1.84) | +24.42 (+23.60, +25.22) | +0.45 (+0.39, +0.50) | +14.04 (+13.63, +14.45) | +21.31 (+20.60, +22.03) | +13.08 (+12.77, +13.39) | +43.16 (+42.29, +44.06) | no (inflation) |
| h146 | Pareto point | Reference | -15.68 (-16.07, -15.34) | -7.26 (-7.95, -6.58) | +24.40 (+23.00, +25.82) | +0.48 (+0.41, +0.56) | +21.39 (+20.48, +22.33) | +17.00 (+16.41, +17.66) | +28.52 (+28.25, +28.78) | +84.75 (+84.10, +85.38) | no (inflation) |
| h146 | Pareto point | Adverse | -16.92 (-17.35, -16.51) | -7.40 (-7.97, -6.78) | +45.66 (+44.31, +47.05) | +0.67 (+0.57, +0.77) | +27.74 (+27.08, +28.39) | +40.44 (+39.83, +41.07) | +35.57 (+35.20, +35.95) | +84.40 (+83.74, +85.04) | no (inflation) |
| h146 | Pareto point | Stress | -6.48 (-6.75, -6.22) | -1.99 (-2.21, -1.77) | +24.89 (+24.08, +25.68) | +0.66 (+0.60, +0.73) | +14.04 (+13.64, +14.46) | +21.44 (+20.74, +22.15) | +13.38 (+13.05, +13.69) | +43.11 (+42.24, +44.00) | no (inflation) |
| h105 | Pareto point | Reference | -15.80 (-16.19, -15.47) | -7.07 (-7.78, -6.41) | +16.23 (+14.95, +17.46) | +0.49 (+0.42, +0.56) | +19.54 (+18.58, +20.51) | +8.20 (+7.73, +8.67) | +36.22 (+35.87, +36.57) | +84.86 (+84.22, +85.49) | no (inflation) |
| h105 | Pareto point | Adverse | -17.05 (-17.46, -16.65) | -7.18 (-7.78, -6.57) | +37.06 (+35.91, +38.29) | +0.67 (+0.56, +0.77) | +25.25 (+24.53, +25.99) | +29.10 (+28.53, +29.68) | +46.74 (+46.24, +47.24) | +84.57 (+83.92, +85.21) | no (inflation) |
| h105 | Pareto point | Stress | -6.13 (-6.39, -5.87) | -1.70 (-1.94, -1.45) | +24.59 (+23.79, +25.36) | +0.55 (+0.49, +0.61) | +15.12 (+14.69, +15.56) | +21.10 (+20.36, +21.79) | +16.91 (+16.51, +17.29) | +43.18 (+42.31, +44.08) | no (inflation) |
| fland | Pareto point | Reference | -16.70 (-17.18, -16.24) | +0.81 (-0.44, +2.13) | +0.22 (-1.14, +1.52) | +0.82 (+0.73, +0.90) | +1.22 (+0.25, +2.20) | -16.46 (-17.06, -15.86) | +5.25 (+5.17, +5.32) | +80.72 (+80.10, +81.35) | no (inflation) |
| fland | Pareto point | Adverse | -18.11 (-18.90, -17.36) | -0.40 (-1.55, +0.71) | +37.00 (+35.19, +38.73) | +1.10 (+0.96, +1.23) | +13.18 (+12.21, +14.16) | +20.40 (+18.72, +22.02) | +13.09 (+12.44, +13.74) | +82.80 (+82.11, +83.49) | no (inflation) |
| fland | Pareto point | Stress | -2.77 (-3.16, -2.40) | +4.91 (+4.51, +5.33) | +3.54 (+3.06, +4.03) | +0.15 (+0.11, +0.19) | +1.74 (+1.45, +2.03) | -3.12 (-3.58, -2.66) | +1.34 (+1.28, +1.40) | +36.98 (+36.15, +37.84) | no |
| h21 | Pareto point | Reference | -15.70 (-16.07, -15.37) | -7.04 (-7.73, -6.37) | +15.92 (+14.66, +17.13) | +0.64 (+0.56, +0.72) | +19.10 (+18.17, +20.05) | +8.09 (+7.62, +8.55) | +35.36 (+35.02, +35.70) | +84.81 (+84.17, +85.43) | no (inflation) |
| h21 | Pareto point | Adverse | -16.89 (-17.30, -16.47) | -7.14 (-7.72, -6.53) | +36.95 (+35.80, +38.19) | +0.83 (+0.72, +0.94) | +24.91 (+24.17, +25.65) | +29.07 (+28.52, +29.63) | +45.67 (+45.19, +46.17) | +84.53 (+83.87, +85.17) | no (inflation) |
| h21 | Pareto point | Stress | -6.01 (-6.25, -5.76) | -1.65 (-1.89, -1.41) | +24.24 (+23.44, +25.05) | +0.58 (+0.52, +0.64) | +14.72 (+14.29, +15.15) | +20.74 (+19.99, +21.46) | +16.63 (+16.23, +17.01) | +43.15 (+42.27, +44.04) | no (inflation) |
| h168 | Pareto point | Reference | -15.41 (-15.80, -15.08) | -6.84 (-7.54, -6.15) | +15.95 (+14.67, +17.18) | +0.45 (+0.38, +0.51) | +19.16 (+18.23, +20.14) | +8.01 (+7.54, +8.48) | +35.55 (+35.20, +35.89) | +84.78 (+84.14, +85.41) | no (inflation) |
| h168 | Pareto point | Adverse | -16.70 (-17.11, -16.28) | -7.01 (-7.62, -6.38) | +36.88 (+35.72, +38.13) | +0.60 (+0.50, +0.70) | +24.92 (+24.19, +25.65) | +28.86 (+28.32, +29.42) | +46.10 (+45.61, +46.61) | +84.51 (+83.85, +85.15) | no (inflation) |
| h168 | Pareto point | Stress | -6.01 (-6.26, -5.74) | -1.69 (-1.93, -1.44) | +24.16 (+23.37, +24.96) | +0.51 (+0.45, +0.58) | +14.57 (+14.15, +15.00) | +20.61 (+19.89, +21.29) | +16.58 (+16.19, +16.96) | +43.11 (+42.24, +44.00) | no (inflation) |
| m3.9 | Pareto point | Reference | -15.40 (-15.75, -15.10) | -6.93 (-7.58, -6.29) | +15.64 (+14.35, +16.93) | +1.52 (+1.39, +1.64) | +18.50 (+17.55, +19.45) | +7.78 (+7.26, +8.28) | +33.63 (+33.33, +33.93) | +84.74 (+84.10, +85.37) | no (inflation) |
| m3.9 | Pareto point | Adverse | -16.29 (-16.71, -15.87) | -6.89 (-7.45, -6.31) | +36.88 (+35.73, +38.09) | +1.74 (+1.60, +1.87) | +24.53 (+23.83, +25.23) | +29.28 (+28.72, +29.86) | +42.66 (+42.24, +43.09) | +84.42 (+83.76, +85.07) | no (inflation) |
| m3.9 | Pareto point | Stress | -6.22 (-6.48, -5.94) | -1.79 (-2.01, -1.55) | +23.44 (+22.66, +24.19) | +0.88 (+0.80, +0.95) | +14.12 (+13.72, +14.54) | +19.29 (+18.62, +19.96) | +16.31 (+15.92, +16.69) | +43.15 (+42.28, +44.05) | no (inflation) |
| h47 | Pareto point | Reference | -15.07 (-15.43, -14.73) | -6.19 (-6.89, -5.49) | +24.02 (+22.68, +25.35) | +0.42 (+0.36, +0.48) | +21.35 (+20.46, +22.27) | +16.48 (+15.90, +17.05) | +27.26 (+26.99, +27.52) | +83.30 (+82.62, +83.96) | no (inflation) |
| h47 | Pareto point | Adverse | -16.37 (-16.81, -15.95) | -6.54 (-7.12, -5.92) | +45.23 (+43.90, +46.60) | +0.46 (+0.37, +0.56) | +27.45 (+26.80, +28.10) | +39.90 (+39.29, +40.53) | +34.28 (+33.89, +34.66) | +83.31 (+82.63, +83.97) | no (inflation) |
| h47 | Pareto point | Stress | -6.14 (-6.39, -5.89) | -1.99 (-2.21, -1.75) | +23.71 (+22.92, +24.49) | +0.43 (+0.37, +0.49) | +13.39 (+12.99, +13.78) | +20.66 (+19.96, +21.37) | +12.60 (+12.29, +12.90) | +42.95 (+42.07, +43.85) | no (inflation) |
| m3.5 | Pareto point | Reference | -15.15 (-15.50, -14.85) | -5.95 (-6.65, -5.25) | +16.09 (+14.86, +17.32) | +0.44 (+0.38, +0.51) | +19.12 (+18.21, +20.05) | +7.76 (+7.24, +8.29) | +32.89 (+32.59, +33.18) | +83.43 (+82.74, +84.08) | no (inflation) |
| m3.5 | Pareto point | Adverse | -16.09 (-16.52, -15.67) | -6.14 (-6.71, -5.55) | +36.90 (+35.74, +38.13) | +0.51 (+0.40, +0.60) | +24.92 (+24.22, +25.60) | +29.28 (+28.68, +29.90) | +41.91 (+41.47, +42.36) | +83.43 (+82.74, +84.08) | no (inflation) |
| m3.5 | Pareto point | Stress | -6.09 (-6.38, -5.80) | -1.58 (-1.81, -1.34) | +23.81 (+23.03, +24.56) | +0.54 (+0.49, +0.59) | +14.32 (+13.90, +14.74) | +19.61 (+18.96, +20.27) | +16.44 (+16.05, +16.83) | +43.05 (+42.18, +43.95) | no (inflation) |
| h108 | Pareto point | Reference | -14.86 (-15.17, -14.58) | -7.04 (-7.66, -6.43) | +13.70 (+12.48, +14.97) | +0.35 (+0.29, +0.41) | +16.04 (+15.20, +16.92) | +5.30 (+4.80, +5.78) | +30.70 (+30.43, +30.96) | +84.66 (+84.00, +85.30) | no (inflation) |
| h108 | Pareto point | Adverse | -16.14 (-16.60, -15.67) | -7.23 (-7.79, -6.61) | +33.98 (+32.80, +35.22) | +0.45 (+0.36, +0.54) | +22.30 (+21.64, +22.94) | +25.07 (+24.50, +25.64) | +38.85 (+38.49, +39.22) | +84.32 (+83.66, +84.97) | no (inflation) |
| h108 | Pareto point | Stress | -6.29 (-6.57, -6.02) | -1.98 (-2.20, -1.75) | +22.28 (+21.55, +23.00) | +0.42 (+0.37, +0.47) | +12.79 (+12.42, +13.17) | +17.72 (+17.08, +18.34) | +15.70 (+15.35, +16.03) | +43.12 (+42.25, +44.03) | no (inflation) |
| h86 | Pareto point | Reference | -15.02 (-15.35, -14.73) | -6.30 (-6.93, -5.66) | +22.04 (+20.67, +23.42) | +1.02 (+0.92, +1.12) | +20.12 (+19.27, +21.01) | +14.30 (+13.73, +14.86) | +25.70 (+25.45, +25.94) | +83.44 (+82.75, +84.09) | no (inflation) |
| h86 | Pareto point | Adverse | -16.19 (-16.63, -15.75) | -6.65 (-7.23, -6.05) | +43.53 (+42.19, +44.91) | +1.42 (+1.27, +1.56) | +26.20 (+25.57, +26.83) | +37.85 (+37.26, +38.44) | +31.70 (+31.38, +32.03) | +83.44 (+82.75, +84.09) | no (inflation) |
| h86 | Pareto point | Stress | -6.06 (-6.31, -5.80) | -1.98 (-2.20, -1.76) | +22.17 (+21.42, +22.90) | +0.50 (+0.45, +0.55) | +12.53 (+12.15, +12.91) | +18.96 (+18.32, +19.60) | +11.87 (+11.58, +12.15) | +43.07 (+42.19, +43.96) | no (inflation) |
| m9.5 | Pareto point | Reference | -14.65 (-14.97, -14.37) | -6.71 (-7.36, -6.09) | +14.59 (+13.39, +15.84) | +0.39 (+0.34, +0.45) | +16.90 (+16.04, +17.79) | +7.05 (+6.52, +7.57) | +30.59 (+30.32, +30.84) | +84.69 (+84.04, +85.33) | no (inflation) |
| m9.5 | Pareto point | Adverse | -15.53 (-15.96, -15.09) | -6.72 (-7.27, -6.13) | +35.38 (+34.17, +36.66) | +0.52 (+0.43, +0.62) | +23.23 (+22.56, +23.88) | +27.54 (+26.93, +28.16) | +38.70 (+38.33, +39.08) | +84.34 (+83.67, +84.99) | no (inflation) |
| m9.5 | Pareto point | Stress | -6.29 (-6.57, -6.01) | -1.93 (-2.16, -1.70) | +22.32 (+21.60, +23.02) | +0.45 (+0.40, +0.51) | +13.07 (+12.69, +13.47) | +17.79 (+17.15, +18.42) | +15.64 (+15.30, +15.98) | +43.18 (+42.30, +44.08) | no (inflation) |
| m9.1 | Pareto point | Reference | -14.69 (-15.02, -14.40) | -6.74 (-7.40, -6.11) | +14.93 (+13.75, +16.15) | +0.40 (+0.34, +0.46) | +17.29 (+16.41, +18.19) | +7.37 (+6.86, +7.87) | +31.23 (+30.95, +31.50) | +84.70 (+84.05, +85.33) | no (inflation) |
| m9.1 | Pareto point | Adverse | -15.67 (-16.10, -15.23) | -6.80 (-7.36, -6.21) | +35.54 (+34.30, +36.83) | +0.54 (+0.44, +0.63) | +23.53 (+22.86, +24.20) | +27.80 (+27.20, +28.40) | +39.57 (+39.19, +39.96) | +84.36 (+83.70, +85.01) | no (inflation) |
| m9.1 | Pareto point | Stress | -6.01 (-6.28, -5.74) | -1.77 (-1.99, -1.55) | +22.64 (+21.89, +23.34) | +0.48 (+0.42, +0.53) | +13.33 (+12.96, +13.73) | +18.58 (+17.94, +19.22) | +15.52 (+15.17, +15.86) | +43.19 (+42.31, +44.09) | no (inflation) |
| h71 | Pareto point | Reference | -14.60 (-14.97, -14.29) | -6.74 (-7.39, -6.10) | +23.45 (+22.09, +24.81) | +0.43 (+0.37, +0.49) | +20.65 (+19.76, +21.59) | +16.57 (+16.01, +17.16) | +26.74 (+26.49, +26.99) | +84.62 (+83.97, +85.26) | no (inflation) |
| h71 | Pareto point | Adverse | -15.75 (-16.15, -15.35) | -6.80 (-7.35, -6.22) | +44.70 (+43.28, +46.16) | +0.57 (+0.47, +0.66) | +27.04 (+26.39, +27.70) | +39.45 (+38.82, +40.10) | +33.28 (+32.94, +33.63) | +84.27 (+83.60, +84.91) | no (inflation) |
| h71 | Pareto point | Stress | -5.93 (-6.17, -5.70) | -1.96 (-2.18, -1.73) | +22.84 (+22.07, +23.59) | +0.41 (+0.35, +0.46) | +12.95 (+12.58, +13.34) | +19.94 (+19.25, +20.60) | +12.09 (+11.80, +12.37) | +43.08 (+42.21, +43.98) | no (inflation) |
| m4.16 | Pareto point | Reference | -14.60 (-14.97, -14.29) | -6.76 (-7.42, -6.12) | +22.92 (+21.58, +24.27) | +0.40 (+0.34, +0.46) | +20.12 (+19.22, +21.06) | +16.08 (+15.54, +16.65) | +26.23 (+25.98, +26.47) | +84.57 (+83.91, +85.21) | no (inflation) |
| m4.16 | Pareto point | Adverse | -15.65 (-16.06, -15.25) | -6.77 (-7.31, -6.20) | +44.42 (+43.04, +45.90) | +0.54 (+0.45, +0.64) | +26.61 (+25.96, +27.26) | +39.19 (+38.56, +39.84) | +32.68 (+32.34, +33.03) | +84.21 (+83.55, +84.86) | no (inflation) |
| m4.16 | Pareto point | Stress | -5.81 (-6.05, -5.57) | -1.89 (-2.11, -1.68) | +22.56 (+21.76, +23.32) | +0.40 (+0.35, +0.46) | +12.73 (+12.34, +13.12) | +19.69 (+19.00, +20.38) | +11.92 (+11.63, +12.20) | +43.03 (+42.15, +43.93) | no (inflation) |
| m9.0 | Pareto point | Reference | -14.36 (-14.67, -14.07) | -5.92 (-6.58, -5.27) | +15.38 (+14.20, +16.57) | +0.41 (+0.35, +0.48) | +17.61 (+16.75, +18.48) | +7.42 (+6.90, +7.94) | +30.35 (+30.07, +30.62) | +83.47 (+82.79, +84.13) | no (inflation) |
| m9.0 | Pareto point | Adverse | -15.42 (-15.86, -14.97) | -6.21 (-6.79, -5.62) | +35.45 (+34.21, +36.76) | +0.44 (+0.34, +0.53) | +23.70 (+23.05, +24.35) | +27.61 (+27.00, +28.22) | +38.72 (+38.31, +39.11) | +83.47 (+82.79, +84.13) | no (inflation) |
| m9.0 | Pareto point | Stress | -6.00 (-6.27, -5.73) | -1.76 (-1.98, -1.53) | +22.54 (+21.78, +23.28) | +0.47 (+0.42, +0.52) | +13.28 (+12.90, +13.68) | +18.50 (+17.86, +19.14) | +15.47 (+15.12, +15.81) | +43.11 (+42.24, +44.01) | no (inflation) |
| h162 | Pareto point | Reference | -14.47 (-14.83, -14.16) | -6.70 (-7.36, -6.07) | +22.74 (+21.43, +24.03) | +0.39 (+0.34, +0.45) | +20.04 (+19.15, +20.97) | +15.96 (+15.42, +16.51) | +25.90 (+25.65, +26.13) | +84.67 (+84.01, +85.29) | no (inflation) |
| h162 | Pareto point | Adverse | -15.50 (-15.90, -15.11) | -6.73 (-7.29, -6.16) | +44.10 (+42.71, +45.50) | +0.54 (+0.44, +0.63) | +26.51 (+25.85, +27.17) | +38.95 (+38.33, +39.57) | +32.22 (+31.89, +32.55) | +84.31 (+83.65, +84.96) | no (inflation) |
| h162 | Pareto point | Stress | -5.80 (-6.04, -5.56) | -1.94 (-2.16, -1.71) | +22.24 (+21.46, +23.00) | +0.39 (+0.33, +0.44) | +12.57 (+12.19, +12.95) | +19.38 (+18.72, +20.05) | +11.72 (+11.44, +12.00) | +43.14 (+42.28, +44.04) | no (inflation) |
| h40 | Pareto point | Reference | -14.82 (-15.11, -14.55) | -6.20 (-6.82, -5.57) | +13.95 (+12.81, +15.13) | +0.40 (+0.35, +0.47) | +16.77 (+15.90, +17.65) | +4.42 (+3.92, +4.88) | +29.60 (+29.33, +29.86) | +83.34 (+82.66, +84.00) | no (inflation) |
| h40 | Pareto point | Adverse | -15.36 (-15.82, -14.92) | -5.98 (-6.53, -5.39) | +35.56 (+34.23, +36.93) | +0.53 (+0.43, +0.63) | +23.27 (+22.63, +23.90) | +27.13 (+26.39, +27.89) | +37.42 (+37.02, +37.82) | +83.35 (+82.67, +84.00) | no (inflation) |
| h40 | Pareto point | Stress | -5.18 (-5.44, -4.94) | -1.17 (-1.36, -0.97) | +21.55 (+20.85, +22.21) | +0.53 (+0.46, +0.59) | +12.57 (+12.19, +12.95) | +17.46 (+16.85, +18.07) | +14.52 (+14.16, +14.85) | +43.01 (+42.13, +43.90) | no (inflation) |
| h30 | Pareto point | Reference | -14.23 (-14.58, -13.91) | -5.91 (-6.56, -5.27) | +22.71 (+21.29, +24.03) | +0.39 (+0.33, +0.44) | +20.18 (+19.32, +21.06) | +15.72 (+15.14, +16.28) | +25.22 (+24.98, +25.46) | +83.42 (+82.73, +84.07) | no (inflation) |
| h30 | Pareto point | Adverse | -15.32 (-15.73, -14.91) | -6.19 (-6.77, -5.60) | +43.86 (+42.46, +45.24) | +0.44 (+0.34, +0.53) | +26.51 (+25.86, +27.17) | +38.71 (+38.10, +39.35) | +31.63 (+31.28, +31.97) | +83.42 (+82.73, +84.07) | no (inflation) |
| h30 | Pareto point | Stress | -5.88 (-6.11, -5.64) | -1.96 (-2.19, -1.73) | +22.18 (+21.41, +22.91) | +0.38 (+0.33, +0.43) | +12.54 (+12.16, +12.92) | +19.31 (+18.64, +19.98) | +11.72 (+11.44, +12.00) | +43.05 (+42.17, +43.94) | no (inflation) |
| h176 | Pareto point | Reference | -14.18 (-14.53, -13.86) | -5.90 (-6.55, -5.27) | +22.67 (+21.24, +24.02) | +0.39 (+0.34, +0.46) | +19.96 (+19.11, +20.84) | +15.61 (+15.04, +16.15) | +25.13 (+24.89, +25.37) | +83.46 (+82.78, +84.12) | no (inflation) |
| h176 | Pareto point | Adverse | -15.29 (-15.71, -14.88) | -6.19 (-6.76, -5.59) | +43.81 (+42.40, +45.18) | +0.45 (+0.35, +0.54) | +26.30 (+25.66, +26.95) | +38.65 (+38.05, +39.28) | +31.54 (+31.20, +31.88) | +83.46 (+82.77, +84.12) | no (inflation) |
| h176 | Pareto point | Stress | -5.85 (-6.09, -5.60) | -1.96 (-2.18, -1.73) | +22.17 (+21.40, +22.92) | +0.39 (+0.33, +0.44) | +12.50 (+12.12, +12.88) | +19.29 (+18.62, +19.96) | +11.72 (+11.44, +11.99) | +43.09 (+42.21, +43.99) | no (inflation) |
| m9.2 | Pareto point | Reference | -14.16 (-14.48, -13.87) | -6.49 (-7.13, -5.88) | +14.41 (+13.22, +15.64) | +0.38 (+0.33, +0.44) | +16.64 (+15.77, +17.54) | +6.96 (+6.44, +7.47) | +29.96 (+29.69, +30.22) | +84.68 (+84.02, +85.31) | no (inflation) |
| m9.2 | Pareto point | Adverse | -15.07 (-15.50, -14.63) | -6.48 (-7.03, -5.91) | +35.29 (+34.07, +36.57) | +0.51 (+0.42, +0.61) | +23.09 (+22.44, +23.74) | +27.43 (+26.80, +28.07) | +38.13 (+37.76, +38.51) | +84.33 (+83.66, +84.98) | no (inflation) |
| m9.2 | Pareto point | Stress | -5.76 (-6.02, -5.50) | -1.73 (-1.94, -1.52) | +21.67 (+20.98, +22.36) | +0.43 (+0.38, +0.49) | +12.52 (+12.16, +12.90) | +17.74 (+17.14, +18.35) | +14.86 (+14.52, +15.18) | +43.18 (+42.30, +44.08) | no (inflation) |
| h193 | Pareto point | Reference | -14.05 (-14.39, -13.75) | -6.41 (-7.04, -5.79) | +22.82 (+21.52, +24.13) | +0.42 (+0.37, +0.48) | +20.42 (+19.53, +21.36) | +16.28 (+15.74, +16.85) | +25.70 (+25.46, +25.93) | +84.57 (+83.91, +85.20) | no (inflation) |
| h193 | Pareto point | Adverse | -15.03 (-15.44, -14.62) | -6.47 (-7.02, -5.89) | +43.85 (+42.46, +45.26) | +0.59 (+0.48, +0.69) | +26.91 (+26.25, +27.57) | +38.79 (+38.19, +39.42) | +31.88 (+31.55, +32.21) | +84.23 (+83.57, +84.88) | no (inflation) |
| h193 | Pareto point | Stress | -5.74 (-5.97, -5.50) | -1.89 (-2.11, -1.66) | +22.25 (+21.45, +22.98) | +0.40 (+0.34, +0.45) | +12.82 (+12.44, +13.20) | +19.44 (+18.78, +20.11) | +11.71 (+11.43, +11.98) | +43.09 (+42.21, +43.99) | no (inflation) |
| m9.3 | Pareto point | Reference | -14.00 (-14.33, -13.71) | -6.42 (-7.04, -5.82) | +14.33 (+13.16, +15.53) | +0.38 (+0.32, +0.43) | +16.61 (+15.75, +17.50) | +7.08 (+6.59, +7.59) | +29.77 (+29.50, +30.04) | +84.67 (+84.01, +85.31) | no (inflation) |
| m9.3 | Pareto point | Adverse | -14.89 (-15.32, -14.45) | -6.38 (-6.93, -5.81) | +35.24 (+34.01, +36.55) | +0.50 (+0.41, +0.60) | +23.07 (+22.41, +23.71) | +27.46 (+26.84, +28.09) | +37.97 (+37.60, +38.35) | +84.32 (+83.65, +84.97) | no (inflation) |
| m9.3 | Pareto point | Stress | -5.72 (-5.97, -5.46) | -1.71 (-1.93, -1.50) | +21.68 (+20.99, +22.35) | +0.43 (+0.38, +0.49) | +12.51 (+12.14, +12.89) | +17.86 (+17.23, +18.48) | +14.80 (+14.46, +15.12) | +43.18 (+42.30, +44.08) | no (inflation) |
| h113 | Pareto point | Reference | -14.11 (-14.41, -13.82) | -6.28 (-6.90, -5.66) | +14.48 (+13.34, +15.67) | +0.43 (+0.37, +0.49) | +17.16 (+16.29, +18.06) | +7.00 (+6.47, +7.51) | +29.44 (+29.18, +29.69) | +84.53 (+83.88, +85.17) | no (inflation) |
| h113 | Pareto point | Adverse | -14.65 (-15.04, -14.26) | -6.11 (-6.62, -5.57) | +36.28 (+35.09, +37.59) | +0.61 (+0.51, +0.71) | +23.61 (+22.96, +24.27) | +29.22 (+28.60, +29.84) | +36.88 (+36.52, +37.25) | +84.21 (+83.54, +84.85) | no (inflation) |
| h113 | Pareto point | Stress | -5.28 (-5.54, -5.04) | -1.38 (-1.58, -1.18) | +20.99 (+20.30, +21.64) | +0.47 (+0.41, +0.52) | +12.48 (+12.11, +12.87) | +17.23 (+16.60, +17.82) | +14.22 (+13.88, +14.55) | +43.10 (+42.23, +44.00) | no (inflation) |
| h14 | Pareto point | Reference | -13.91 (-14.26, -13.60) | -6.16 (-6.80, -5.53) | +15.52 (+14.34, +16.68) | +0.42 (+0.36, +0.48) | +17.88 (+16.97, +18.84) | +8.46 (+7.99, +8.93) | +30.91 (+30.61, +31.20) | +84.68 (+84.03, +85.31) | no (inflation) |
| h14 | Pareto point | Adverse | -14.76 (-15.17, -14.35) | -6.12 (-6.68, -5.55) | +36.36 (+35.15, +37.64) | +0.59 (+0.49, +0.68) | +24.27 (+23.57, +24.95) | +29.17 (+28.60, +29.75) | +39.87 (+39.45, +40.30) | +84.37 (+83.71, +85.01) | no (inflation) |
| h14 | Pareto point | Stress | -5.35 (-5.59, -5.11) | -1.55 (-1.77, -1.32) | +21.95 (+21.20, +22.68) | +0.45 (+0.39, +0.50) | +13.04 (+12.65, +13.44) | +18.76 (+18.10, +19.40) | +14.68 (+14.33, +15.01) | +43.18 (+42.30, +44.08) | no (inflation) |
| h129 | Pareto point | Reference | -13.64 (-13.96, -13.36) | -5.58 (-6.21, -4.97) | +22.66 (+21.33, +23.92) | +0.48 (+0.42, +0.54) | +20.76 (+19.87, +21.68) | +16.06 (+15.49, +16.62) | +24.75 (+24.52, +24.99) | +83.42 (+82.74, +84.08) | no (inflation) |
| h129 | Pareto point | Adverse | -14.62 (-15.02, -14.22) | -5.83 (-6.40, -5.25) | +43.33 (+41.94, +44.75) | +0.57 (+0.48, +0.67) | +27.06 (+26.39, +27.74) | +38.34 (+37.72, +38.98) | +30.80 (+30.47, +31.13) | +83.42 (+82.74, +84.08) | no (inflation) |
| h129 | Pareto point | Stress | -5.64 (-5.87, -5.40) | -1.79 (-2.00, -1.57) | +22.14 (+21.35, +22.87) | +0.43 (+0.37, +0.48) | +13.07 (+12.68, +13.45) | +19.37 (+18.70, +20.03) | +11.62 (+11.34, +11.89) | +43.05 (+42.17, +43.94) | no (inflation) |
| h182 | Pareto point | Reference | -13.56 (-13.86, -13.28) | -5.74 (-6.36, -5.14) | +20.03 (+18.70, +21.33) | +0.37 (+0.32, +0.43) | +18.03 (+17.22, +18.88) | +13.34 (+12.79, +13.90) | +22.38 (+22.17, +22.58) | +83.42 (+82.74, +84.08) | no (inflation) |
| h182 | Pareto point | Adverse | -14.28 (-14.70, -13.86) | -5.89 (-6.44, -5.34) | +40.91 (+39.64, +42.23) | +0.43 (+0.35, +0.52) | +24.32 (+23.69, +24.95) | +35.74 (+35.12, +36.36) | +27.42 (+27.14, +27.69) | +83.42 (+82.74, +84.08) | no (inflation) |
| h182 | Pareto point | Stress | -5.39 (-5.63, -5.15) | -1.79 (-1.98, -1.58) | +19.82 (+19.06, +20.57) | +0.33 (+0.28, +0.38) | +11.03 (+10.68, +11.40) | +16.87 (+16.26, +17.48) | +10.43 (+10.17, +10.68) | +43.06 (+42.19, +43.96) | no (inflation) |
| h25 | Pareto point | Reference | -13.67 (-13.96, -13.38) | -6.11 (-6.71, -5.48) | +13.54 (+12.41, +14.69) | +0.41 (+0.36, +0.47) | +16.39 (+15.51, +17.30) | +5.68 (+5.22, +6.15) | +28.00 (+27.73, +28.26) | +84.46 (+83.80, +85.10) | no (inflation) |
| h25 | Pareto point | Adverse | -14.39 (-14.80, -13.97) | -5.96 (-6.46, -5.40) | +35.26 (+33.98, +36.61) | +0.59 (+0.49, +0.69) | +23.05 (+22.42, +23.69) | +27.41 (+26.78, +28.08) | +35.26 (+34.91, +35.61) | +84.13 (+83.47, +84.78) | no (inflation) |
| h25 | Pareto point | Stress | -4.82 (-5.05, -4.60) | -1.19 (-1.37, -1.01) | +19.98 (+19.32, +20.64) | +0.45 (+0.39, +0.50) | +11.79 (+11.42, +12.17) | +16.53 (+15.93, +17.11) | +13.31 (+12.99, +13.62) | +43.09 (+42.21, +43.99) | no (inflation) |
| h26 | Pareto point | Reference | -13.14 (-13.46, -12.86) | -6.05 (-6.63, -5.50) | +20.64 (+19.37, +21.87) | +0.41 (+0.35, +0.46) | +17.95 (+17.11, +18.83) | +14.43 (+13.88, +14.99) | +22.65 (+22.44, +22.86) | +84.56 (+83.90, +85.20) | no (inflation) |
| h26 | Pareto point | Adverse | -13.83 (-14.22, -13.45) | -5.98 (-6.49, -5.45) | +41.66 (+40.35, +43.01) | +0.52 (+0.43, +0.62) | +24.62 (+23.99, +25.25) | +36.77 (+36.16, +37.40) | +28.13 (+27.84, +28.42) | +84.21 (+83.54, +84.85) | no (inflation) |
| h26 | Pareto point | Stress | -5.85 (-6.10, -5.61) | -2.00 (-2.21, -1.78) | +20.80 (+20.06, +21.50) | +0.49 (+0.44, +0.54) | +11.75 (+11.38, +12.12) | +17.73 (+17.12, +18.34) | +11.11 (+10.84, +11.38) | +43.16 (+42.28, +44.06) | no (inflation) |
| m3.2 | Pareto point | Reference | -13.13 (-13.42, -12.88) | -5.50 (-6.08, -4.91) | +13.93 (+12.89, +15.02) | +0.38 (+0.33, +0.44) | +15.93 (+15.07, +16.78) | +5.75 (+5.25, +6.24) | +26.45 (+26.20, +26.69) | +83.42 (+82.74, +84.08) | no (inflation) |
| m3.2 | Pareto point | Adverse | -14.27 (-14.72, -13.81) | -5.90 (-6.46, -5.31) | +33.22 (+31.96, +34.52) | +0.44 (+0.35, +0.53) | +22.33 (+21.73, +22.95) | +24.56 (+23.95, +25.17) | +33.35 (+33.01, +33.68) | +83.43 (+82.74, +84.08) | no (inflation) |
| m3.2 | Pareto point | Stress | -5.25 (-5.51, -5.00) | -1.54 (-1.75, -1.33) | +19.59 (+18.92, +20.27) | +0.40 (+0.35, +0.45) | +11.64 (+11.28, +12.00) | +15.97 (+15.42, +16.52) | +13.35 (+13.04, +13.64) | +43.06 (+42.18, +43.95) | no (inflation) |
| h123 | Pareto point | Reference | -13.28 (-13.61, -12.99) | -5.88 (-6.49, -5.27) | +15.01 (+13.84, +16.21) | +0.41 (+0.35, +0.47) | +17.50 (+16.63, +18.41) | +8.51 (+8.03, +9.00) | +29.35 (+29.07, +29.63) | +84.59 (+83.93, +85.22) | no (inflation) |
| h123 | Pareto point | Adverse | -13.98 (-14.36, -13.59) | -5.75 (-6.28, -5.21) | +36.25 (+35.09, +37.50) | +0.56 (+0.45, +0.66) | +24.07 (+23.38, +24.75) | +29.21 (+28.65, +29.77) | +37.83 (+37.43, +38.24) | +84.27 (+83.60, +84.92) | no (inflation) |
| h123 | Pareto point | Stress | -5.08 (-5.30, -4.85) | -1.44 (-1.64, -1.23) | +21.12 (+20.38, +21.83) | +0.43 (+0.37, +0.48) | +12.59 (+12.21, +12.98) | +18.08 (+17.44, +18.71) | +14.04 (+13.71, +14.36) | +43.13 (+42.26, +44.04) | no (inflation) |
| m3.3 | Pareto point | Reference | -13.07 (-13.35, -12.82) | -5.44 (-6.02, -4.86) | +14.19 (+13.14, +15.28) | +0.39 (+0.33, +0.45) | +15.91 (+15.06, +16.76) | +6.01 (+5.52, +6.52) | +26.26 (+26.02, +26.49) | +83.42 (+82.74, +84.08) | no (inflation) |
| m3.3 | Pareto point | Adverse | -13.86 (-14.29, -13.43) | -5.64 (-6.18, -5.08) | +34.16 (+32.97, +35.41) | +0.44 (+0.36, +0.54) | +22.40 (+21.79, +23.01) | +26.83 (+26.21, +27.45) | +32.99 (+32.66, +33.32) | +83.43 (+82.74, +84.08) | no (inflation) |
| m3.3 | Pareto point | Stress | -5.25 (-5.51, -5.00) | -1.54 (-1.75, -1.33) | +19.59 (+18.92, +20.27) | +0.40 (+0.35, +0.45) | +11.64 (+11.28, +12.00) | +15.97 (+15.42, +16.52) | +13.35 (+13.04, +13.64) | +43.06 (+42.18, +43.95) | no (inflation) |
| m3.0 | Pareto point | Reference | -13.01 (-13.30, -12.76) | -5.40 (-5.99, -4.82) | +14.45 (+13.39, +15.56) | +0.38 (+0.33, +0.44) | +15.99 (+15.16, +16.84) | +6.74 (+6.27, +7.23) | +26.15 (+25.91, +26.37) | +83.42 (+82.74, +84.08) | no (inflation) |
| m3.0 | Pareto point | Adverse | -13.70 (-14.11, -13.27) | -5.54 (-6.06, -4.99) | +34.35 (+33.14, +35.61) | +0.45 (+0.37, +0.54) | +22.52 (+21.91, +23.13) | +27.22 (+26.62, +27.84) | +32.89 (+32.56, +33.22) | +83.43 (+82.74, +84.08) | no (inflation) |
| m3.0 | Pareto point | Stress | -5.27 (-5.54, -5.02) | -1.54 (-1.75, -1.33) | +19.69 (+19.00, +20.37) | +0.40 (+0.35, +0.45) | +11.71 (+11.35, +12.08) | +16.05 (+15.49, +16.61) | +13.40 (+13.09, +13.71) | +43.06 (+42.18, +43.96) | no (inflation) |
| m1.1 | Pareto point | Reference | -12.89 (-13.20, -12.61) | -5.74 (-6.33, -5.16) | +14.75 (+13.61, +15.91) | +0.43 (+0.38, +0.49) | +16.73 (+15.84, +17.65) | +8.56 (+8.10, +9.08) | +27.47 (+27.22, +27.72) | +84.54 (+83.88, +85.18) | no (inflation) |
| m1.1 | Pareto point | Adverse | -13.41 (-13.79, -13.02) | -5.54 (-6.05, -5.01) | +35.46 (+34.27, +36.75) | +0.56 (+0.46, +0.66) | +23.44 (+22.79, +24.09) | +28.96 (+28.40, +29.52) | +34.91 (+34.56, +35.26) | +84.22 (+83.55, +84.86) | no (inflation) |
| m1.1 | Pareto point | Stress | -5.25 (-5.49, -5.00) | -1.59 (-1.80, -1.36) | +20.20 (+19.49, +20.91) | +0.40 (+0.35, +0.46) | +11.98 (+11.61, +12.36) | +16.91 (+16.29, +17.48) | +13.57 (+13.25, +13.87) | +43.18 (+42.30, +44.08) | no (inflation) |
| m1.2 | Pareto point | Reference | -12.88 (-13.19, -12.60) | -5.73 (-6.32, -5.16) | +14.77 (+13.63, +15.92) | +0.43 (+0.38, +0.49) | +16.72 (+15.84, +17.64) | +8.57 (+8.10, +9.09) | +27.46 (+27.20, +27.70) | +84.54 (+83.88, +85.18) | no (inflation) |
| m1.2 | Pareto point | Adverse | -13.41 (-13.78, -13.02) | -5.53 (-6.04, -5.00) | +35.46 (+34.27, +36.75) | +0.56 (+0.46, +0.66) | +23.43 (+22.77, +24.09) | +28.96 (+28.40, +29.54) | +34.89 (+34.55, +35.24) | +84.22 (+83.55, +84.86) | no (inflation) |
| m1.2 | Pareto point | Stress | -5.23 (-5.47, -4.98) | -1.58 (-1.79, -1.36) | +20.18 (+19.47, +20.88) | +0.41 (+0.35, +0.46) | +11.97 (+11.59, +12.35) | +16.90 (+16.29, +17.48) | +13.54 (+13.22, +13.84) | +43.18 (+42.30, +44.08) | no (inflation) |
| h53 | Pareto point | Reference | -12.66 (-12.95, -12.40) | -5.42 (-6.00, -4.86) | +19.61 (+18.39, +20.79) | +0.59 (+0.52, +0.66) | +17.50 (+16.71, +18.31) | +13.42 (+12.91, +13.93) | +21.42 (+21.22, +21.61) | +83.37 (+82.69, +84.02) | no (inflation) |
| h53 | Pareto point | Adverse | -13.39 (-13.79, -12.99) | -5.53 (-6.05, -5.00) | +40.34 (+39.03, +41.67) | +0.76 (+0.66, +0.87) | +23.92 (+23.31, +24.53) | +35.32 (+34.71, +35.92) | +26.48 (+26.20, +26.75) | +83.37 (+82.69, +84.03) | no (inflation) |
| h53 | Pareto point | Stress | -5.30 (-5.55, -5.06) | -1.85 (-2.05, -1.64) | +19.30 (+18.55, +20.01) | +0.36 (+0.30, +0.41) | +10.67 (+10.32, +11.02) | +16.53 (+15.95, +17.10) | +10.10 (+9.85, +10.33) | +43.01 (+42.14, +43.91) | no (inflation) |
| h34 | Pareto point | Reference | -12.64 (-12.95, -12.37) | -5.58 (-6.16, -5.01) | +14.80 (+13.63, +15.97) | +0.42 (+0.36, +0.47) | +17.17 (+16.29, +18.07) | +8.63 (+8.16, +9.14) | +28.31 (+28.03, +28.58) | +84.56 (+83.90, +85.19) | no (inflation) |
| h34 | Pareto point | Adverse | -13.37 (-13.76, -12.98) | -5.47 (-5.99, -4.94) | +35.86 (+34.66, +37.14) | +0.55 (+0.44, +0.65) | +23.78 (+23.10, +24.44) | +29.03 (+28.45, +29.61) | +36.49 (+36.11, +36.88) | +84.23 (+83.57, +84.88) | no (inflation) |
| h34 | Pareto point | Stress | -5.40 (-5.64, -5.16) | -1.46 (-1.67, -1.25) | +21.79 (+21.08, +22.49) | +0.74 (+0.68, +0.81) | +12.92 (+12.53, +13.32) | +18.16 (+17.53, +18.79) | +14.70 (+14.35, +15.03) | +43.15 (+42.28, +44.05) | no (inflation) |
| m1.0 | Pareto point | Reference | -12.65 (-12.96, -12.38) | -5.14 (-5.73, -4.56) | +15.05 (+13.97, +16.20) | +0.43 (+0.37, +0.49) | +16.87 (+16.03, +17.75) | +8.50 (+8.04, +9.00) | +26.78 (+26.53, +27.03) | +83.47 (+82.78, +84.13) | no (inflation) |
| m1.0 | Pareto point | Adverse | -13.25 (-13.63, -12.84) | -5.13 (-5.65, -4.59) | +35.37 (+34.20, +36.61) | +0.49 (+0.40, +0.59) | +23.42 (+22.79, +24.05) | +28.80 (+28.22, +29.38) | +34.27 (+33.91, +34.63) | +83.47 (+82.78, +84.13) | no (inflation) |
| m1.0 | Pareto point | Stress | -5.23 (-5.47, -4.98) | -1.57 (-1.78, -1.34) | +20.15 (+19.45, +20.84) | +0.40 (+0.35, +0.46) | +11.93 (+11.55, +12.31) | +16.86 (+16.25, +17.44) | +13.53 (+13.21, +13.83) | +43.11 (+42.23, +44.01) | no (inflation) |
| h8 | Pareto point | Reference | -12.64 (-12.94, -12.37) | -5.35 (-5.93, -4.79) | +20.25 (+18.97, +21.47) | +0.37 (+0.32, +0.42) | +17.80 (+17.01, +18.61) | +14.02 (+13.46, +14.60) | +21.75 (+21.54, +21.96) | +83.44 (+82.75, +84.09) | no (inflation) |
| h8 | Pareto point | Adverse | -13.36 (-13.75, -12.97) | -5.39 (-5.92, -4.86) | +41.28 (+39.96, +42.63) | +0.42 (+0.33, +0.52) | +24.37 (+23.74, +25.01) | +36.28 (+35.63, +36.94) | +27.27 (+26.97, +27.56) | +83.44 (+82.75, +84.09) | no (inflation) |
| h8 | Pareto point | Stress | -5.11 (-5.33, -4.88) | -1.73 (-1.91, -1.53) | +19.63 (+18.88, +20.34) | +0.33 (+0.28, +0.38) | +10.90 (+10.55, +11.26) | +17.04 (+16.42, +17.66) | +10.18 (+9.94, +10.42) | +43.07 (+42.19, +43.97) | no (inflation) |
| m1.3 | Pareto point | Reference | -12.65 (-12.96, -12.37) | -5.62 (-6.19, -5.05) | +14.78 (+13.65, +15.92) | +0.42 (+0.37, +0.48) | +16.67 (+15.80, +17.58) | +8.72 (+8.25, +9.21) | +27.10 (+26.85, +27.34) | +84.53 (+83.87, +85.17) | no (inflation) |
| m1.3 | Pareto point | Adverse | -13.18 (-13.55, -12.79) | -5.44 (-5.95, -4.91) | +35.46 (+34.26, +36.75) | +0.56 (+0.46, +0.66) | +23.38 (+22.73, +24.04) | +28.94 (+28.36, +29.52) | +34.57 (+34.22, +34.92) | +84.21 (+83.55, +84.85) | no (inflation) |
| m1.3 | Pareto point | Stress | -5.17 (-5.41, -4.94) | -1.56 (-1.77, -1.34) | +20.17 (+19.45, +20.88) | +0.41 (+0.35, +0.46) | +11.96 (+11.58, +12.34) | +16.97 (+16.36, +17.55) | +13.46 (+13.16, +13.76) | +43.18 (+42.30, +44.08) | no (inflation) |
| h74 | Pareto point | Reference | -12.75 (-13.03, -12.49) | -5.46 (-6.01, -4.90) | +19.32 (+18.10, +20.56) | +0.86 (+0.77, +0.95) | +17.39 (+16.59, +18.19) | +13.11 (+12.60, +13.62) | +21.31 (+21.12, +21.50) | +83.43 (+82.74, +84.09) | no (inflation) |
| h74 | Pareto point | Adverse | -13.12 (-13.50, -12.74) | -5.22 (-5.70, -4.71) | +40.42 (+39.14, +41.75) | +1.26 (+1.13, +1.39) | +23.92 (+23.31, +24.53) | +35.35 (+34.74, +35.98) | +26.31 (+26.04, +26.58) | +83.43 (+82.74, +84.09) | no (inflation) |
| h74 | Pareto point | Stress | -5.14 (-5.36, -4.93) | -1.65 (-1.83, -1.47) | +19.49 (+18.76, +20.20) | +0.51 (+0.46, +0.56) | +10.76 (+10.41, +11.12) | +16.55 (+15.97, +17.13) | +10.14 (+9.89, +10.38) | +43.06 (+42.19, +43.96) | no (inflation) |
| h114 | Pareto point | Reference | -12.52 (-12.82, -12.25) | -5.35 (-5.91, -4.80) | +19.74 (+18.53, +20.94) | +0.38 (+0.33, +0.43) | +17.56 (+16.76, +18.38) | +13.75 (+13.21, +14.30) | +21.40 (+21.20, +21.60) | +83.48 (+82.79, +84.14) | no (inflation) |
| h114 | Pareto point | Adverse | -13.23 (-13.62, -12.84) | -5.41 (-5.93, -4.88) | +40.92 (+39.62, +42.26) | +0.43 (+0.34, +0.53) | +24.07 (+23.44, +24.70) | +35.76 (+35.12, +36.41) | +26.74 (+26.46, +27.02) | +83.48 (+82.79, +84.14) | no (inflation) |
| h114 | Pareto point | Stress | -5.08 (-5.31, -4.85) | -1.77 (-1.96, -1.56) | +19.37 (+18.66, +20.03) | +0.31 (+0.26, +0.36) | +10.74 (+10.40, +11.09) | +16.84 (+16.24, +17.44) | +10.00 (+9.77, +10.24) | +43.11 (+42.24, +44.01) | no (inflation) |
| m7.5 | Pareto point | Reference | -12.65 (-12.96, -12.37) | -5.62 (-6.20, -5.06) | +14.47 (+13.35, +15.64) | +0.50 (+0.44, +0.57) | +16.34 (+15.48, +17.25) | +8.40 (+7.93, +8.89) | +26.76 (+26.51, +27.00) | +84.52 (+83.85, +85.15) | no (inflation) |
| m7.5 | Pareto point | Adverse | -13.11 (-13.48, -12.73) | -5.39 (-5.90, -4.88) | +35.26 (+34.07, +36.50) | +0.66 (+0.56, +0.76) | +23.13 (+22.48, +23.78) | +28.80 (+28.20, +29.41) | +34.26 (+33.91, +34.61) | +84.19 (+83.52, +84.83) | no (inflation) |
| m7.5 | Pareto point | Stress | -4.99 (-5.22, -4.76) | -1.49 (-1.69, -1.28) | +19.83 (+19.14, +20.52) | +0.43 (+0.38, +0.49) | +11.69 (+11.32, +12.07) | +16.81 (+16.21, +17.40) | +13.16 (+12.86, +13.46) | +43.13 (+42.25, +44.02) | no (inflation) |
| h167 | Pareto point | Reference | -12.56 (-12.86, -12.29) | -5.86 (-6.41, -5.31) | +19.47 (+18.20, +20.72) | +0.43 (+0.37, +0.49) | +17.23 (+16.42, +18.08) | +13.59 (+13.10, +14.10) | +21.67 (+21.47, +21.87) | +84.32 (+83.66, +84.96) | no (inflation) |
| h167 | Pareto point | Adverse | -13.03 (-13.40, -12.66) | -5.52 (-6.00, -5.02) | +40.81 (+39.47, +42.15) | +0.66 (+0.55, +0.77) | +23.93 (+23.31, +24.55) | +35.82 (+35.21, +36.44) | +26.86 (+26.59, +27.14) | +83.98 (+83.31, +84.63) | no (inflation) |
| h167 | Pareto point | Stress | -4.88 (-5.09, -4.66) | -1.59 (-1.77, -1.40) | +19.29 (+18.59, +19.96) | +0.37 (+0.33, +0.42) | +10.62 (+10.28, +10.97) | +16.72 (+16.13, +17.30) | +9.95 (+9.71, +10.18) | +42.99 (+42.12, +43.89) | no (inflation) |
| sva | Pareto point | Reference | -13.43 (-13.78, -13.09) | -1.52 (-2.41, -0.63) | -2.51 (-3.31, -1.76) | -0.22 (-0.26, -0.18) | -5.55 (-6.16, -4.94) | -10.41 (-10.82, -10.03) | +1128.16 (+1103.31, +1154.81) | +83.41 (+82.73, +84.07) | yes (inflation) |
| sva | Pareto point | Adverse | -15.23 (-15.62, -14.83) | -2.88 (-3.56, -2.20) | -8.22 (-9.01, -7.43) | -0.76 (-0.83, -0.69) | -8.69 (-9.30, -8.05) | -16.39 (-16.98, -15.80) | +1405.05 (+1371.07, +1440.67) | +83.42 (+82.73, +84.07) | yes (inflation) |
| sva | Pareto point | Stress | -1.34 (-1.62, -1.06) | +3.91 (+3.58, +4.25) | -3.62 (-4.15, -3.11) | -0.48 (-0.53, -0.43) | -4.10 (-4.39, -3.80) | -7.20 (-7.68, -6.75) | +1235.17 (+1203.75, +1267.86) | +43.04 (+42.16, +43.94) | no (inflation) |
| m2.0 | Pareto point | Reference | -12.24 (-12.54, -11.97) | -5.26 (-5.81, -4.72) | +19.69 (+18.44, +20.89) | +0.38 (+0.33, +0.43) | +17.47 (+16.67, +18.27) | +13.85 (+13.31, +14.42) | +21.28 (+21.08, +21.48) | +83.48 (+82.79, +84.14) | no (inflation) |
| m2.0 | Pareto point | Adverse | -13.02 (-13.42, -12.63) | -5.35 (-5.87, -4.82) | +40.78 (+39.46, +42.14) | +0.44 (+0.35, +0.53) | +23.96 (+23.35, +24.58) | +35.75 (+35.13, +36.38) | +26.62 (+26.34, +26.91) | +83.47 (+82.78, +84.13) | no (inflation) |
| m2.0 | Pareto point | Stress | -5.08 (-5.31, -4.85) | -1.78 (-1.98, -1.58) | +19.30 (+18.59, +19.97) | +0.32 (+0.26, +0.37) | +10.63 (+10.30, +10.98) | +16.76 (+16.16, +17.36) | +9.97 (+9.73, +10.20) | +43.11 (+42.23, +44.01) | no (inflation) |
| m2.1 | Pareto point | Reference | -12.22 (-12.52, -11.96) | -5.25 (-5.81, -4.71) | +19.67 (+18.41, +20.88) | +0.37 (+0.32, +0.43) | +17.47 (+16.68, +18.28) | +13.84 (+13.30, +14.41) | +21.28 (+21.08, +21.48) | +83.48 (+82.79, +84.13) | no (inflation) |
| m2.1 | Pareto point | Adverse | -13.01 (-13.41, -12.61) | -5.34 (-5.86, -4.81) | +40.80 (+39.49, +42.15) | +0.43 (+0.34, +0.52) | +23.98 (+23.36, +24.59) | +35.76 (+35.13, +36.38) | +26.63 (+26.34, +26.91) | +83.47 (+82.79, +84.13) | no (inflation) |
| m2.1 | Pareto point | Stress | -5.07 (-5.29, -4.83) | -1.77 (-1.97, -1.57) | +19.31 (+18.60, +19.97) | +0.31 (+0.26, +0.36) | +10.64 (+10.30, +10.98) | +16.76 (+16.16, +17.36) | +9.97 (+9.73, +10.20) | +43.11 (+42.24, +44.01) | no (inflation) |
| m2.4 | Pareto point | Reference | -12.22 (-12.52, -11.96) | -5.25 (-5.81, -4.71) | +19.67 (+18.41, +20.88) | +0.37 (+0.32, +0.43) | +17.47 (+16.68, +18.28) | +13.84 (+13.30, +14.41) | +21.28 (+21.08, +21.48) | +83.48 (+82.79, +84.13) | no (inflation) |
| m2.4 | Pareto point | Adverse | -13.01 (-13.41, -12.61) | -5.34 (-5.86, -4.81) | +40.80 (+39.49, +42.15) | +0.43 (+0.34, +0.52) | +23.98 (+23.36, +24.59) | +35.76 (+35.13, +36.38) | +26.63 (+26.34, +26.91) | +83.47 (+82.79, +84.13) | no (inflation) |
| m2.4 | Pareto point | Stress | -5.07 (-5.29, -4.84) | -1.77 (-1.97, -1.57) | +19.31 (+18.60, +19.97) | +0.31 (+0.26, +0.36) | +10.64 (+10.30, +10.98) | +16.76 (+16.16, +17.36) | +9.97 (+9.73, +10.20) | +43.11 (+42.24, +44.01) | no (inflation) |
| m2.5 | Pareto point | Reference | -12.19 (-12.48, -11.91) | -5.24 (-5.79, -4.70) | +19.59 (+18.31, +20.82) | +0.37 (+0.32, +0.42) | +17.45 (+16.65, +18.26) | +13.82 (+13.27, +14.40) | +21.26 (+21.06, +21.46) | +83.47 (+82.79, +84.13) | no (inflation) |
| m2.5 | Pareto point | Adverse | -12.96 (-13.36, -12.57) | -5.31 (-5.84, -4.79) | +40.78 (+39.46, +42.14) | +0.42 (+0.33, +0.51) | +23.96 (+23.34, +24.57) | +35.74 (+35.12, +36.36) | +26.61 (+26.33, +26.89) | +83.48 (+82.79, +84.13) | no (inflation) |
| m2.5 | Pareto point | Stress | -5.05 (-5.27, -4.82) | -1.77 (-1.97, -1.56) | +19.29 (+18.58, +19.95) | +0.31 (+0.26, +0.36) | +10.64 (+10.30, +10.98) | +16.74 (+16.14, +17.34) | +9.96 (+9.73, +10.20) | +43.11 (+42.23, +44.00) | no (inflation) |
| h177 | Pareto point | Reference | -12.20 (-12.50, -11.93) | -5.27 (-5.82, -4.73) | +18.97 (+17.68, +20.19) | +0.37 (+0.32, +0.42) | +16.98 (+16.20, +17.80) | +13.27 (+12.70, +13.83) | +20.71 (+20.51, +20.90) | +83.29 (+82.61, +83.95) | no (inflation) |
| h177 | Pareto point | Adverse | -12.88 (-13.28, -12.48) | -5.29 (-5.81, -4.79) | +40.09 (+38.80, +41.43) | +0.44 (+0.35, +0.53) | +23.55 (+22.93, +24.16) | +35.03 (+34.42, +35.63) | +25.90 (+25.62, +26.17) | +83.30 (+82.62, +83.95) | no (inflation) |
| h177 | Pareto point | Stress | -4.91 (-5.13, -4.69) | -1.71 (-1.89, -1.51) | +18.79 (+18.07, +19.44) | +0.32 (+0.27, +0.36) | +10.39 (+10.05, +10.73) | +16.34 (+15.76, +16.92) | +9.69 (+9.46, +9.92) | +42.95 (+42.07, +43.84) | no (inflation) |
| h83 | Pareto point | Reference | -12.24 (-12.52, -11.98) | -5.04 (-5.59, -4.48) | +13.81 (+12.72, +14.94) | +0.37 (+0.32, +0.43) | +15.39 (+14.57, +16.23) | +6.20 (+5.73, +6.67) | +24.93 (+24.69, +25.16) | +83.33 (+82.65, +83.98) | no (inflation) |
| h83 | Pareto point | Adverse | -12.94 (-13.35, -12.54) | -5.09 (-5.61, -4.56) | +34.17 (+32.90, +35.47) | +0.47 (+0.39, +0.56) | +22.06 (+21.47, +22.64) | +27.02 (+26.40, +27.67) | +31.67 (+31.34, +32.00) | +83.33 (+82.66, +83.99) | no (inflation) |
| h83 | Pareto point | Stress | -4.57 (-4.78, -4.36) | -1.26 (-1.44, -1.08) | +18.56 (+17.91, +19.19) | +0.38 (+0.33, +0.43) | +10.75 (+10.40, +11.10) | +15.43 (+14.87, +15.99) | +12.25 (+11.96, +12.53) | +42.99 (+42.11, +43.89) | no (inflation) |
| m7.6 | Pareto point | Reference | -12.25 (-12.55, -11.96) | -5.43 (-5.99, -4.89) | +14.61 (+13.48, +15.75) | +0.40 (+0.35, +0.46) | +16.39 (+15.53, +17.29) | +8.62 (+8.13, +9.12) | +26.49 (+26.24, +26.74) | +84.48 (+83.82, +85.12) | no (inflation) |
| m7.6 | Pareto point | Adverse | -12.78 (-13.15, -12.41) | -5.24 (-5.74, -4.72) | +35.24 (+34.05, +36.48) | +0.55 (+0.45, +0.65) | +23.24 (+22.58, +23.88) | +28.84 (+28.23, +29.45) | +34.08 (+33.73, +34.45) | +84.17 (+83.51, +84.82) | no (inflation) |
| m7.6 | Pareto point | Stress | -4.68 (-4.89, -4.46) | -1.37 (-1.57, -1.17) | +19.70 (+18.97, +20.43) | +0.39 (+0.34, +0.44) | +11.58 (+11.22, +11.95) | +16.89 (+16.26, +17.50) | +12.84 (+12.54, +13.13) | +43.12 (+42.25, +44.02) | no (inflation) |
| m7.9 | Pareto point | Reference | -12.22 (-12.52, -11.94) | -5.43 (-5.98, -4.89) | +14.59 (+13.49, +15.74) | +0.40 (+0.34, +0.46) | +16.21 (+15.35, +17.09) | +8.55 (+8.08, +9.05) | +26.36 (+26.10, +26.61) | +84.48 (+83.82, +85.11) | no (inflation) |
| m7.9 | Pareto point | Adverse | -12.78 (-13.15, -12.41) | -5.25 (-5.76, -4.74) | +35.19 (+34.00, +36.43) | +0.54 (+0.44, +0.64) | +23.05 (+22.39, +23.68) | +28.75 (+28.13, +29.36) | +33.94 (+33.59, +34.30) | +84.17 (+83.51, +84.82) | no (inflation) |
| m7.9 | Pareto point | Stress | -4.66 (-4.88, -4.45) | -1.38 (-1.57, -1.18) | +19.59 (+18.87, +20.33) | +0.39 (+0.34, +0.45) | +11.46 (+11.11, +11.84) | +16.78 (+16.17, +17.40) | +12.79 (+12.49, +13.07) | +43.13 (+42.26, +44.02) | no (inflation) |
| m7.8 | Pareto point | Reference | -12.21 (-12.51, -11.93) | -5.42 (-5.97, -4.88) | +14.59 (+13.49, +15.74) | +0.40 (+0.35, +0.46) | +16.26 (+15.40, +17.15) | +8.56 (+8.09, +9.06) | +26.40 (+26.15, +26.65) | +84.48 (+83.82, +85.11) | no (inflation) |
| m7.8 | Pareto point | Adverse | -12.77 (-13.14, -12.40) | -5.24 (-5.75, -4.73) | +35.19 (+34.00, +36.43) | +0.54 (+0.44, +0.64) | +23.11 (+22.45, +23.74) | +28.77 (+28.15, +29.39) | +33.99 (+33.63, +34.34) | +84.17 (+83.51, +84.82) | no (inflation) |
| m7.8 | Pareto point | Stress | -4.66 (-4.87, -4.44) | -1.37 (-1.56, -1.17) | +19.65 (+18.92, +20.39) | +0.40 (+0.34, +0.45) | +11.51 (+11.15, +11.88) | +16.82 (+16.20, +17.44) | +12.81 (+12.51, +13.09) | +43.13 (+42.25, +44.02) | no (inflation) |
| m7.10 | Pareto point | Reference | -12.21 (-12.51, -11.93) | -5.43 (-5.98, -4.89) | +14.61 (+13.50, +15.74) | +0.40 (+0.35, +0.46) | +16.17 (+15.32, +17.06) | +8.56 (+8.09, +9.06) | +26.34 (+26.09, +26.59) | +84.48 (+83.82, +85.12) | no (inflation) |
| m7.10 | Pareto point | Adverse | -12.77 (-13.13, -12.39) | -5.25 (-5.76, -4.74) | +35.19 (+34.00, +36.43) | +0.54 (+0.44, +0.64) | +23.04 (+22.39, +23.67) | +28.74 (+28.13, +29.36) | +33.93 (+33.57, +34.28) | +84.17 (+83.51, +84.82) | no (inflation) |
| m7.10 | Pareto point | Stress | -4.66 (-4.88, -4.45) | -1.38 (-1.57, -1.18) | +19.57 (+18.84, +20.30) | +0.39 (+0.33, +0.45) | +11.45 (+11.09, +11.82) | +16.76 (+16.16, +17.38) | +12.78 (+12.48, +13.06) | +43.12 (+42.25, +44.02) | no (inflation) |
| h142 | Pareto point | Reference | -11.95 (-12.23, -11.69) | -5.15 (-5.67, -4.62) | +18.38 (+17.21, +19.54) | +0.48 (+0.42, +0.55) | +16.45 (+15.68, +17.26) | +12.74 (+12.19, +13.27) | +20.04 (+19.86, +20.22) | +83.30 (+82.62, +83.96) | no (inflation) |
| h142 | Pareto point | Adverse | -12.55 (-12.94, -12.15) | -5.16 (-5.66, -4.65) | +39.23 (+37.97, +40.54) | +0.61 (+0.51, +0.71) | +22.85 (+22.25, +23.45) | +34.12 (+33.48, +34.78) | +24.83 (+24.57, +25.08) | +83.31 (+82.63, +83.97) | no (inflation) |
| h142 | Pareto point | Stress | -5.02 (-5.27, -4.79) | -1.76 (-1.96, -1.57) | +18.25 (+17.53, +18.93) | +0.35 (+0.29, +0.40) | +10.07 (+9.73, +10.42) | +15.67 (+15.09, +16.24) | +9.52 (+9.28, +9.76) | +42.96 (+42.08, +43.86) | no (inflation) |
| h101 | Pareto point | Reference | -12.16 (-12.45, -11.90) | -5.69 (-6.23, -5.15) | +17.51 (+16.29, +18.69) | +0.52 (+0.45, +0.59) | +15.87 (+15.09, +16.69) | +12.04 (+11.52, +12.54) | +19.90 (+19.72, +20.08) | +84.32 (+83.66, +84.96) | no (inflation) |
| h101 | Pareto point | Adverse | -12.41 (-12.78, -12.04) | -5.28 (-5.74, -4.79) | +38.87 (+37.57, +40.18) | +0.87 (+0.76, +0.97) | +22.54 (+21.94, +23.13) | +33.78 (+33.16, +34.42) | +24.46 (+24.21, +24.70) | +83.98 (+83.31, +84.63) | no (inflation) |
| h101 | Pareto point | Stress | -4.60 (-4.79, -4.40) | -1.50 (-1.67, -1.33) | +17.57 (+16.88, +18.23) | +0.35 (+0.31, +0.40) | +9.73 (+9.41, +10.06) | +15.10 (+14.56, +15.68) | +9.10 (+8.87, +9.31) | +43.03 (+42.15, +43.93) | no (inflation) |
| m8.0 | Pareto point | Reference | -11.75 (-12.04, -11.48) | -4.78 (-5.33, -4.25) | +14.94 (+13.84, +16.11) | +0.42 (+0.36, +0.48) | +16.35 (+15.54, +17.22) | +8.70 (+8.24, +9.20) | +25.64 (+25.39, +25.89) | +83.47 (+82.79, +84.13) | no (inflation) |
| m8.0 | Pareto point | Adverse | -12.44 (-12.82, -12.05) | -4.80 (-5.31, -4.28) | +35.05 (+33.83, +36.32) | +0.48 (+0.39, +0.58) | +23.10 (+22.47, +23.72) | +28.48 (+27.87, +29.10) | +33.24 (+32.87, +33.61) | +83.47 (+82.78, +84.13) | no (inflation) |
| m8.0 | Pareto point | Stress | -4.66 (-4.87, -4.44) | -1.38 (-1.58, -1.18) | +19.50 (+18.77, +20.22) | +0.38 (+0.33, +0.44) | +11.38 (+11.02, +11.75) | +16.70 (+16.08, +17.32) | +12.73 (+12.43, +13.02) | +43.11 (+42.23, +44.01) | no (inflation) |
| h122 | Pareto point | Reference | -11.75 (-12.02, -11.49) | -4.78 (-5.30, -4.26) | +14.33 (+13.19, +15.50) | +0.65 (+0.58, +0.73) | +15.54 (+14.75, +16.38) | +8.12 (+7.68, +8.60) | +24.42 (+24.19, +24.64) | +83.43 (+82.75, +84.09) | no (inflation) |
| h122 | Pareto point | Adverse | -12.20 (-12.57, -11.82) | -4.73 (-5.23, -4.22) | +34.32 (+33.10, +35.59) | +0.81 (+0.70, +0.92) | +22.28 (+21.66, +22.87) | +28.09 (+27.47, +28.70) | +31.22 (+30.90, +31.55) | +83.43 (+82.75, +84.09) | no (inflation) |
| h122 | Pareto point | Stress | -4.78 (-5.00, -4.56) | -1.44 (-1.63, -1.24) | +18.71 (+18.05, +19.37) | +0.46 (+0.41, +0.51) | +10.87 (+10.51, +11.23) | +15.67 (+15.10, +16.25) | +12.36 (+12.07, +12.64) | +43.07 (+42.19, +43.97) | no (inflation) |
| h67 | Pareto point | Reference | -11.71 (-12.00, -11.46) | -5.39 (-5.92, -4.88) | +17.91 (+16.67, +19.12) | +0.41 (+0.36, +0.46) | +16.47 (+15.67, +17.33) | +12.97 (+12.45, +13.50) | +19.70 (+19.52, +19.88) | +84.31 (+83.66, +84.95) | no (inflation) |
| h67 | Pareto point | Adverse | -12.10 (-12.45, -11.75) | -5.24 (-5.72, -4.75) | +38.69 (+37.45, +39.97) | +0.58 (+0.49, +0.67) | +23.12 (+22.50, +23.73) | +33.81 (+33.18, +34.46) | +24.28 (+24.03, +24.52) | +84.00 (+83.33, +84.66) | no (inflation) |
| h67 | Pareto point | Stress | -4.72 (-4.93, -4.52) | -1.64 (-1.82, -1.44) | +17.84 (+17.11, +18.54) | +0.33 (+0.28, +0.38) | +10.23 (+9.90, +10.57) | +15.58 (+14.99, +16.19) | +9.15 (+8.93, +9.36) | +43.08 (+42.20, +43.98) | no (inflation) |
| h92 | Pareto point | Reference | -11.84 (-12.12, -11.59) | -5.26 (-5.78, -4.72) | +13.24 (+12.07, +14.43) | +0.36 (+0.31, +0.41) | +14.54 (+13.72, +15.38) | +6.83 (+6.35, +7.32) | +23.78 (+23.56, +23.99) | +84.40 (+83.73, +85.04) | no (inflation) |
| h92 | Pareto point | Adverse | -12.15 (-12.52, -11.76) | -5.04 (-5.52, -4.54) | +33.91 (+32.71, +35.18) | +0.51 (+0.43, +0.60) | +21.50 (+20.91, +22.11) | +27.43 (+26.81, +28.06) | +30.08 (+29.79, +30.38) | +84.08 (+83.41, +84.73) | no (inflation) |
| h92 | Pareto point | Stress | -4.41 (-4.62, -4.20) | -1.33 (-1.50, -1.14) | +17.67 (+17.01, +18.30) | +0.34 (+0.29, +0.39) | +10.17 (+9.84, +10.52) | +14.82 (+14.25, +15.40) | +11.55 (+11.28, +11.81) | +43.14 (+42.26, +44.04) | no (inflation) |
| h137 | Pareto point | Reference | -11.86 (-12.13, -11.61) | -5.31 (-5.84, -4.77) | +13.19 (+11.97, +14.37) | +0.37 (+0.32, +0.42) | +14.42 (+13.59, +15.27) | +7.18 (+6.70, +7.68) | +23.40 (+23.20, +23.61) | +84.28 (+83.62, +84.92) | no (inflation) |
| h137 | Pareto point | Adverse | -11.88 (-12.23, -11.53) | -4.85 (-5.31, -4.38) | +33.96 (+32.75, +35.29) | +0.55 (+0.46, +0.63) | +21.40 (+20.80, +22.01) | +27.88 (+27.24, +28.56) | +29.41 (+29.12, +29.70) | +83.97 (+83.30, +84.62) | no (inflation) |
| h137 | Pareto point | Stress | -4.51 (-4.72, -4.30) | -1.28 (-1.46, -1.10) | +17.73 (+17.13, +18.31) | +0.36 (+0.31, +0.41) | +10.24 (+9.92, +10.58) | +14.59 (+14.06, +15.12) | +11.73 (+11.45, +12.00) | +43.05 (+42.17, +43.95) | no (inflation) |
| h98 | Pareto point | Reference | -11.41 (-11.69, -11.15) | -4.93 (-5.44, -4.42) | +17.82 (+16.55, +19.03) | +0.36 (+0.31, +0.42) | +16.24 (+15.49, +17.03) | +12.70 (+12.16, +13.21) | +19.50 (+19.31, +19.68) | +83.41 (+82.72, +84.06) | no (inflation) |
| h98 | Pareto point | Adverse | -12.05 (-12.43, -11.67) | -4.96 (-5.46, -4.46) | +38.81 (+37.55, +40.08) | +0.45 (+0.36, +0.55) | +22.73 (+22.12, +23.33) | +33.81 (+33.18, +34.45) | +24.36 (+24.10, +24.61) | +83.41 (+82.72, +84.06) | no (inflation) |
| h98 | Pareto point | Stress | -4.72 (-4.93, -4.51) | -1.67 (-1.86, -1.48) | +17.71 (+17.00, +18.39) | +0.30 (+0.24, +0.35) | +9.87 (+9.55, +10.19) | +15.40 (+14.80, +16.00) | +9.17 (+8.95, +9.38) | +43.04 (+42.17, +43.94) | no (inflation) |
| h28 | Pareto point | Reference | -11.36 (-11.62, -11.12) | -4.96 (-5.46, -4.46) | +16.86 (+15.63, +18.05) | +0.30 (+0.25, +0.35) | +15.18 (+14.45, +15.94) | +11.51 (+10.97, +12.00) | +18.73 (+18.56, +18.91) | +83.34 (+82.65, +83.99) | no (inflation) |
| h28 | Pareto point | Adverse | -11.59 (-11.97, -11.20) | -4.55 (-5.03, -4.07) | +38.26 (+36.94, +39.60) | +0.47 (+0.38, +0.55) | +21.85 (+21.27, +22.41) | +32.71 (+32.06, +33.39) | +23.48 (+23.22, +23.74) | +83.34 (+82.65, +84.00) | no (inflation) |
| h28 | Pareto point | Stress | -4.19 (-4.38, -4.00) | -1.23 (-1.40, -1.07) | +17.11 (+16.44, +17.77) | +0.35 (+0.29, +0.41) | +9.41 (+9.10, +9.74) | +14.69 (+14.14, +15.27) | +8.83 (+8.62, +9.04) | +43.00 (+42.12, +43.89) | no (inflation) |
| h160 | Pareto point | Reference | -10.97 (-11.24, -10.72) | -4.73 (-5.21, -4.25) | +17.25 (+16.02, +18.44) | +0.31 (+0.26, +0.36) | +15.60 (+14.85, +16.37) | +12.31 (+11.80, +12.80) | +18.75 (+18.57, +18.92) | +83.28 (+82.60, +83.93) | no (inflation) |
| h160 | Pareto point | Adverse | -11.52 (-11.90, -11.15) | -4.79 (-5.27, -4.30) | +38.29 (+37.05, +39.60) | +0.40 (+0.31, +0.48) | +22.13 (+21.53, +22.71) | +33.22 (+32.57, +33.88) | +23.46 (+23.21, +23.71) | +83.28 (+82.60, +83.94) | no (inflation) |
| h160 | Pareto point | Stress | -4.54 (-4.73, -4.34) | -1.56 (-1.73, -1.38) | +17.51 (+16.91, +18.10) | +0.29 (+0.24, +0.34) | +9.78 (+9.51, +10.07) | +15.26 (+14.76, +15.78) | +9.04 (+8.88, +9.20) | +42.93 (+42.05, +43.82) | no (inflation) |
| m4.2 | Pareto point | Reference | -10.96 (-11.23, -10.72) | -4.80 (-5.26, -4.32) | +16.16 (+15.05, +17.29) | +0.37 (+0.31, +0.43) | +14.53 (+13.78, +15.28) | +11.03 (+10.52, +11.49) | +17.71 (+17.54, +17.87) | +83.42 (+82.74, +84.08) | no (inflation) |
| m4.2 | Pareto point | Adverse | -11.45 (-11.84, -11.06) | -4.85 (-5.34, -4.37) | +36.50 (+35.28, +37.76) | +0.50 (+0.41, +0.59) | +20.95 (+20.38, +21.51) | +31.37 (+30.76, +31.98) | +21.96 (+21.73, +22.19) | +83.42 (+82.74, +84.08) | no (inflation) |
| m4.2 | Pareto point | Stress | -4.43 (-4.63, -4.24) | -1.61 (-1.78, -1.43) | +15.74 (+15.11, +16.33) | +0.25 (+0.21, +0.30) | +8.83 (+8.53, +9.14) | +13.60 (+13.09, +14.12) | +8.32 (+8.12, +8.52) | +43.07 (+42.19, +43.97) | no (inflation) |
| m4.4 | Pareto point | Reference | -10.92 (-11.19, -10.68) | -4.78 (-5.24, -4.30) | +16.15 (+15.05, +17.26) | +0.34 (+0.29, +0.40) | +14.49 (+13.74, +15.25) | +11.08 (+10.57, +11.55) | +17.65 (+17.48, +17.81) | +83.42 (+82.74, +84.08) | no (inflation) |
| m4.4 | Pareto point | Adverse | -11.40 (-11.79, -11.02) | -4.82 (-5.31, -4.34) | +36.45 (+35.28, +37.66) | +0.46 (+0.37, +0.54) | +20.92 (+20.34, +21.48) | +31.36 (+30.76, +31.98) | +21.91 (+21.68, +22.13) | +83.42 (+82.74, +84.08) | no (inflation) |
| m4.4 | Pareto point | Stress | -4.39 (-4.59, -4.20) | -1.59 (-1.76, -1.41) | +15.64 (+15.02, +16.24) | +0.24 (+0.19, +0.28) | +8.80 (+8.50, +9.10) | +13.52 (+13.01, +14.06) | +8.28 (+8.08, +8.47) | +43.06 (+42.19, +43.96) | no (inflation) |
| h147 | Pareto point | Reference | -10.62 (-10.88, -10.39) | -4.97 (-5.43, -4.50) | +16.36 (+15.21, +17.51) | +0.30 (+0.25, +0.36) | +14.65 (+13.88, +15.43) | +11.74 (+11.25, +12.23) | +17.95 (+17.79, +18.11) | +84.30 (+83.65, +84.94) | no (inflation) |
| h147 | Pareto point | Adverse | -11.10 (-11.47, -10.73) | -4.88 (-5.35, -4.42) | +36.82 (+35.59, +38.07) | +0.42 (+0.34, +0.50) | +21.24 (+20.66, +21.81) | +31.95 (+31.34, +32.59) | +22.27 (+22.05, +22.50) | +83.99 (+83.32, +84.64) | no (inflation) |
| h147 | Pareto point | Stress | -4.76 (-4.98, -4.55) | -1.69 (-1.87, -1.50) | +16.94 (+16.25, +17.58) | +0.36 (+0.32, +0.41) | +9.41 (+9.09, +9.74) | +14.46 (+13.91, +15.02) | +8.89 (+8.68, +9.10) | +43.14 (+42.26, +44.04) | no (inflation) |
| h81 | Pareto point | Reference | -10.89 (-11.16, -10.64) | -5.07 (-5.53, -4.59) | +16.35 (+15.19, +17.48) | +0.30 (+0.25, +0.35) | +14.55 (+13.78, +15.34) | +11.57 (+11.08, +12.04) | +17.93 (+17.77, +18.09) | +84.29 (+83.63, +84.93) | no (inflation) |
| h81 | Pareto point | Adverse | -11.16 (-11.50, -10.82) | -4.83 (-5.27, -4.37) | +36.78 (+35.56, +38.03) | +0.44 (+0.36, +0.53) | +21.27 (+20.68, +21.84) | +31.91 (+31.28, +32.56) | +22.26 (+22.03, +22.50) | +83.97 (+83.30, +84.62) | no (inflation) |
| h81 | Pareto point | Stress | -4.29 (-4.47, -4.10) | -1.52 (-1.68, -1.36) | +15.83 (+15.19, +16.45) | +0.26 (+0.22, +0.31) | +8.91 (+8.61, +9.22) | +13.80 (+13.27, +14.36) | +8.30 (+8.11, +8.50) | +43.10 (+42.22, +44.00) | no (inflation) |
| m9.12 | Pareto point | Reference | -11.94 (-12.30, -11.61) | -1.81 (-2.64, -0.99) | -2.66 (-3.38, -1.99) | -0.29 (-0.34, -0.25) | -5.30 (-5.82, -4.81) | -9.40 (-9.80, -9.00) | +1133.98 (+1108.60, +1161.21) | +84.79 (+84.15, +85.43) | yes (inflation) |
| m9.12 | Pareto point | Adverse | -13.68 (-14.05, -13.29) | -2.95 (-3.58, -2.33) | -8.27 (-9.10, -7.45) | -0.81 (-0.90, -0.72) | -8.52 (-9.17, -7.89) | -15.03 (-15.57, -14.50) | +1414.39 (+1379.93, +1450.91) | +84.64 (+83.97, +85.28) | yes (inflation) |
| m9.12 | Pareto point | Stress | -0.40 (-0.67, -0.14) | +4.29 (+3.99, +4.61) | -3.26 (-3.75, -2.81) | -0.49 (-0.55, -0.44) | -3.72 (-3.97, -3.45) | -6.36 (-6.80, -5.94) | +1232.17 (+1200.18, +1265.27) | +43.15 (+42.27, +44.05) | no (inflation) |
| m5.6 | Pareto point | Reference | -10.79 (-11.05, -10.54) | -5.05 (-5.51, -4.57) | +16.19 (+15.01, +17.31) | +0.31 (+0.25, +0.36) | +14.42 (+13.64, +15.21) | +11.43 (+10.94, +11.90) | +17.70 (+17.54, +17.86) | +84.27 (+83.61, +84.91) | no (inflation) |
| m5.6 | Pareto point | Adverse | -11.14 (-11.50, -10.78) | -4.89 (-5.35, -4.43) | +36.59 (+35.39, +37.81) | +0.44 (+0.35, +0.53) | +21.02 (+20.45, +21.58) | +31.62 (+31.01, +32.26) | +21.92 (+21.69, +22.14) | +83.97 (+83.30, +84.62) | no (inflation) |
| m5.6 | Pareto point | Stress | -4.37 (-4.55, -4.19) | -1.56 (-1.72, -1.38) | +15.95 (+15.40, +16.49) | +0.25 (+0.21, +0.30) | +9.00 (+8.73, +9.28) | +13.87 (+13.38, +14.38) | +8.38 (+8.24, +8.53) | +43.11 (+42.23, +44.02) | no (inflation) |
| m5.7 | Pareto point | Reference | -10.78 (-11.05, -10.54) | -5.05 (-5.51, -4.58) | +16.19 (+15.01, +17.31) | +0.30 (+0.25, +0.36) | +14.42 (+13.63, +15.21) | +11.43 (+10.94, +11.90) | +17.69 (+17.53, +17.85) | +84.27 (+83.61, +84.91) | no (inflation) |
| m5.7 | Pareto point | Adverse | -11.14 (-11.50, -10.78) | -4.89 (-5.35, -4.43) | +36.59 (+35.39, +37.81) | +0.43 (+0.35, +0.52) | +21.02 (+20.44, +21.58) | +31.62 (+31.01, +32.26) | +21.91 (+21.69, +22.14) | +83.97 (+83.30, +84.62) | no (inflation) |
| m5.7 | Pareto point | Stress | -4.37 (-4.55, -4.19) | -1.55 (-1.72, -1.38) | +15.91 (+15.37, +16.46) | +0.25 (+0.20, +0.30) | +9.00 (+8.73, +9.27) | +13.84 (+13.37, +14.34) | +8.38 (+8.24, +8.53) | +43.11 (+42.23, +44.02) | no (inflation) |
| m5.4 | Pareto point | Reference | -10.67 (-10.93, -10.43) | -5.02 (-5.47, -4.55) | +16.11 (+14.94, +17.26) | +0.28 (+0.24, +0.34) | +14.26 (+13.48, +15.04) | +11.35 (+10.86, +11.83) | +17.55 (+17.38, +17.70) | +84.27 (+83.60, +84.91) | no (inflation) |
| m5.4 | Pareto point | Adverse | -11.00 (-11.36, -10.64) | -4.83 (-5.28, -4.38) | +36.43 (+35.21, +37.62) | +0.39 (+0.31, +0.48) | +20.84 (+20.26, +21.40) | +31.51 (+30.86, +32.17) | +21.75 (+21.53, +21.97) | +83.96 (+83.29, +84.61) | no (inflation) |
| m5.4 | Pareto point | Stress | -4.32 (-4.50, -4.14) | -1.54 (-1.70, -1.36) | +15.86 (+15.30, +16.39) | +0.25 (+0.20, +0.30) | +8.95 (+8.68, +9.23) | +13.84 (+13.33, +14.36) | +8.35 (+8.20, +8.49) | +43.11 (+42.23, +44.01) | no (inflation) |
| m5.3 | Pareto point | Reference | -10.60 (-10.86, -10.36) | -4.97 (-5.42, -4.52) | +16.01 (+14.84, +17.14) | +0.28 (+0.23, +0.33) | +14.15 (+13.38, +14.92) | +11.28 (+10.76, +11.76) | +17.44 (+17.28, +17.60) | +84.26 (+83.60, +84.91) | no (inflation) |
| m5.3 | Pareto point | Adverse | -10.94 (-11.30, -10.58) | -4.82 (-5.28, -4.36) | +36.28 (+35.06, +37.48) | +0.39 (+0.31, +0.47) | +20.74 (+20.16, +21.30) | +31.44 (+30.80, +32.08) | +21.64 (+21.42, +21.86) | +83.95 (+83.29, +84.61) | no (inflation) |
| m5.3 | Pareto point | Stress | -4.37 (-4.55, -4.19) | -1.53 (-1.70, -1.36) | +16.25 (+15.73, +16.76) | +0.26 (+0.21, +0.31) | +9.17 (+8.92, +9.42) | +14.16 (+13.68, +14.65) | +8.49 (+8.37, +8.61) | +43.12 (+42.24, +44.02) | no (inflation) |
| m4.6 | Pareto point | Reference | -10.58 (-10.84, -10.35) | -4.67 (-5.12, -4.21) | +16.03 (+14.89, +17.16) | +0.30 (+0.25, +0.35) | +14.19 (+13.45, +14.95) | +11.05 (+10.53, +11.54) | +17.24 (+17.08, +17.40) | +83.21 (+82.52, +83.86) | no (inflation) |
| m4.6 | Pareto point | Adverse | -11.07 (-11.45, -10.69) | -4.69 (-5.17, -4.21) | +36.00 (+34.75, +37.23) | +0.38 (+0.31, +0.46) | +20.62 (+20.06, +21.18) | +31.02 (+30.38, +31.67) | +21.54 (+21.31, +21.76) | +83.22 (+82.53, +83.87) | no (inflation) |
| m4.6 | Pareto point | Stress | -4.25 (-4.44, -4.06) | -1.56 (-1.73, -1.38) | +15.36 (+14.77, +15.94) | +0.23 (+0.18, +0.27) | +8.61 (+8.32, +8.91) | +13.37 (+12.86, +13.89) | +8.12 (+7.93, +8.31) | +42.89 (+42.01, +43.79) | no (inflation) |
| m4.5 | Pareto point | Reference | -10.59 (-10.85, -10.35) | -4.67 (-5.13, -4.21) | +16.03 (+14.89, +17.16) | +0.31 (+0.26, +0.36) | +14.20 (+13.47, +14.97) | +11.06 (+10.53, +11.56) | +17.25 (+17.08, +17.41) | +83.20 (+82.52, +83.85) | no (inflation) |
| m4.5 | Pareto point | Adverse | -11.03 (-11.40, -10.65) | -4.66 (-5.14, -4.18) | +36.08 (+34.87, +37.28) | +0.37 (+0.30, +0.45) | +20.64 (+20.08, +21.19) | +31.13 (+30.51, +31.78) | +21.51 (+21.28, +21.73) | +83.20 (+82.52, +83.86) | no (inflation) |
| m4.5 | Pareto point | Stress | -4.25 (-4.44, -4.06) | -1.56 (-1.72, -1.38) | +15.33 (+14.74, +15.90) | +0.23 (+0.18, +0.27) | +8.62 (+8.32, +8.92) | +13.35 (+12.85, +13.87) | +8.13 (+7.93, +8.31) | +42.88 (+42.00, +43.77) | no (inflation) |
| m5.2 | Pareto point | Reference | -10.38 (-10.63, -10.15) | -4.86 (-5.29, -4.41) | +16.05 (+14.88, +17.18) | +0.28 (+0.23, +0.33) | +14.24 (+13.47, +15.02) | +11.41 (+10.90, +11.89) | +17.42 (+17.26, +17.58) | +84.24 (+83.58, +84.88) | no (inflation) |
| m5.2 | Pareto point | Adverse | -10.80 (-11.17, -10.44) | -4.76 (-5.22, -4.30) | +36.26 (+35.04, +37.45) | +0.39 (+0.31, +0.47) | +20.77 (+20.20, +21.34) | +31.41 (+30.77, +32.05) | +21.62 (+21.40, +21.84) | +83.94 (+83.27, +84.60) | no (inflation) |
| m5.2 | Pareto point | Stress | -4.36 (-4.55, -4.18) | -1.53 (-1.70, -1.35) | +16.27 (+15.74, +16.79) | +0.26 (+0.21, +0.31) | +9.17 (+8.92, +9.43) | +14.19 (+13.70, +14.67) | +8.49 (+8.37, +8.60) | +43.11 (+42.24, +44.02) | no (inflation) |
| h158 | Pareto point | Reference | -10.60 (-10.87, -10.35) | -4.71 (-5.19, -4.23) | +13.10 (+11.90, +14.29) | +0.33 (+0.28, +0.39) | +14.08 (+13.28, +14.90) | +8.14 (+7.66, +8.62) | +22.06 (+21.85, +22.27) | +84.20 (+83.54, +84.84) | no (inflation) |
| h158 | Pareto point | Adverse | -10.80 (-11.13, -10.46) | -4.40 (-4.85, -3.92) | +33.28 (+31.98, +34.65) | +0.50 (+0.41, +0.59) | +21.23 (+20.61, +21.86) | +27.55 (+26.90, +28.20) | +28.42 (+28.12, +28.72) | +83.90 (+83.23, +84.55) | no (inflation) |
| h158 | Pareto point | Stress | -4.01 (-4.20, -3.83) | -1.20 (-1.36, -1.03) | +16.82 (+16.20, +17.43) | +0.33 (+0.28, +0.38) | +9.85 (+9.54, +10.19) | +14.60 (+14.06, +15.16) | +10.94 (+10.68, +11.18) | +43.01 (+42.13, +43.92) | no (inflation) |
| m4.12 | Pareto point | Reference | -10.47 (-10.74, -10.23) | -4.62 (-5.07, -4.17) | +16.06 (+14.94, +17.15) | +0.29 (+0.25, +0.34) | +14.25 (+13.52, +15.01) | +11.15 (+10.63, +11.64) | +17.18 (+17.02, +17.34) | +83.21 (+82.52, +83.86) | no (inflation) |
| m4.12 | Pareto point | Adverse | -10.79 (-11.14, -10.44) | -4.52 (-4.98, -4.05) | +36.13 (+34.93, +37.33) | +0.37 (+0.29, +0.44) | +20.77 (+20.19, +21.32) | +31.28 (+30.65, +31.91) | +21.50 (+21.27, +21.73) | +83.22 (+82.53, +83.87) | no (inflation) |
| m4.12 | Pareto point | Stress | -4.15 (-4.34, -3.97) | -1.48 (-1.64, -1.31) | +15.38 (+14.81, +15.96) | +0.24 (+0.20, +0.28) | +8.66 (+8.36, +8.97) | +13.40 (+12.90, +13.95) | +8.10 (+7.91, +8.29) | +42.89 (+42.01, +43.79) | no (inflation) |
| m5.0 | Pareto point | Reference | -10.22 (-10.47, -9.99) | -4.50 (-4.93, -4.07) | +16.01 (+14.90, +17.11) | +0.29 (+0.24, +0.34) | +14.19 (+13.46, +14.95) | +11.18 (+10.65, +11.66) | +17.07 (+16.91, +17.23) | +83.42 (+82.73, +84.08) | no (inflation) |
| m5.0 | Pareto point | Adverse | -10.72 (-11.10, -10.35) | -4.55 (-5.02, -4.08) | +36.02 (+34.82, +37.22) | +0.35 (+0.27, +0.43) | +20.61 (+20.04, +21.17) | +31.12 (+30.48, +31.77) | +21.34 (+21.11, +21.57) | +83.42 (+82.74, +84.08) | no (inflation) |
| m5.0 | Pareto point | Stress | -4.36 (-4.54, -4.17) | -1.52 (-1.70, -1.35) | +16.24 (+15.70, +16.76) | +0.26 (+0.21, +0.31) | +9.16 (+8.91, +9.42) | +14.15 (+13.66, +14.65) | +8.48 (+8.36, +8.60) | +43.07 (+42.19, +43.97) | no (inflation) |
| h170 | Pareto point | Reference | -11.49 (-11.83, -11.18) | -1.47 (-2.27, -0.68) | -2.32 (-3.01, -1.67) | -0.27 (-0.32, -0.22) | -5.41 (-5.93, -4.92) | -9.08 (-9.48, -8.70) | +1126.86 (+1101.77, +1153.86) | +84.74 (+84.09, +85.37) | yes (inflation) |
| h170 | Pareto point | Adverse | -13.04 (-13.41, -12.66) | -2.59 (-3.19, -1.97) | -7.89 (-8.65, -7.13) | -0.77 (-0.87, -0.68) | -8.62 (-9.25, -8.00) | -14.62 (-15.16, -14.10) | +1405.66 (+1371.58, +1441.74) | +84.57 (+83.91, +85.21) | yes (inflation) |
| h170 | Pareto point | Stress | -0.38 (-0.65, -0.12) | +4.20 (+3.88, +4.54) | -3.31 (-3.81, -2.82) | -0.49 (-0.55, -0.43) | -3.83 (-4.10, -3.56) | -6.42 (-6.88, -5.99) | +1225.14 (+1194.00, +1257.92) | +43.16 (+42.29, +44.06) | no (inflation) |
| h55 | Pareto point | Reference | -10.34 (-10.59, -10.10) | -4.59 (-5.06, -4.13) | +13.18 (+12.02, +14.35) | +0.35 (+0.30, +0.41) | +14.18 (+13.38, +14.98) | +8.28 (+7.83, +8.76) | +21.97 (+21.76, +22.16) | +84.32 (+83.66, +84.96) | no (inflation) |
| h55 | Pareto point | Adverse | -10.68 (-11.03, -10.33) | -4.36 (-4.82, -3.90) | +33.21 (+31.94, +34.50) | +0.50 (+0.41, +0.60) | +21.24 (+20.63, +21.84) | +27.49 (+26.85, +28.13) | +28.24 (+27.95, +28.53) | +84.03 (+83.36, +84.68) | no (inflation) |
| h55 | Pareto point | Stress | -4.04 (-4.23, -3.85) | -1.25 (-1.42, -1.07) | +16.76 (+16.14, +17.37) | +0.32 (+0.27, +0.37) | +9.84 (+9.52, +10.17) | +14.54 (+14.02, +15.10) | +10.90 (+10.64, +11.13) | +43.16 (+42.28, +44.06) | no (inflation) |
| h77 | Pareto point | Reference | -10.24 (-10.51, -10.00) | -4.22 (-4.68, -3.77) | +13.35 (+12.26, +14.43) | +0.35 (+0.30, +0.40) | +14.27 (+13.50, +15.06) | +8.16 (+7.71, +8.61) | +21.69 (+21.48, +21.91) | +83.38 (+82.70, +84.04) | no (inflation) |
| h77 | Pareto point | Adverse | -10.67 (-11.04, -10.32) | -4.16 (-4.63, -3.69) | +33.06 (+31.80, +34.42) | +0.44 (+0.35, +0.53) | +21.16 (+20.54, +21.76) | +27.32 (+26.68, +27.95) | +28.17 (+27.86, +28.48) | +83.38 (+82.71, +84.04) | no (inflation) |
| h77 | Pareto point | Stress | -4.07 (-4.26, -3.88) | -1.24 (-1.41, -1.06) | +16.84 (+16.22, +17.44) | +0.32 (+0.27, +0.37) | +9.82 (+9.50, +10.16) | +14.60 (+14.07, +15.16) | +10.98 (+10.72, +11.22) | +43.03 (+42.15, +43.92) | no (inflation) |
| h93 | Pareto point | Reference | -10.27 (-10.53, -10.03) | -4.56 (-5.02, -4.10) | +12.95 (+11.78, +14.11) | +0.36 (+0.31, +0.42) | +14.02 (+13.21, +14.82) | +8.21 (+7.74, +8.70) | +21.59 (+21.39, +21.79) | +84.27 (+83.61, +84.91) | no (inflation) |
| h93 | Pareto point | Adverse | -10.56 (-10.90, -10.22) | -4.29 (-4.73, -3.84) | +32.95 (+31.69, +34.23) | +0.51 (+0.42, +0.60) | +21.09 (+20.49, +21.70) | +27.35 (+26.70, +28.01) | +27.78 (+27.49, +28.08) | +83.98 (+83.31, +84.63) | no (inflation) |
| h93 | Pareto point | Stress | -3.96 (-4.14, -3.77) | -1.19 (-1.35, -1.03) | +16.56 (+15.91, +17.17) | +0.33 (+0.28, +0.38) | +9.72 (+9.40, +10.06) | +14.41 (+13.87, +14.98) | +10.73 (+10.48, +10.96) | +43.12 (+42.23, +44.02) | no (inflation) |
| m6.0 | Pareto point | Reference | -10.20 (-10.46, -9.97) | -4.26 (-4.70, -3.82) | +12.71 (+11.61, +13.81) | +0.39 (+0.34, +0.46) | +13.78 (+13.03, +14.54) | +7.65 (+7.20, +8.11) | +21.01 (+20.81, +21.21) | +83.42 (+82.74, +84.08) | no (inflation) |
| m6.0 | Pareto point | Adverse | -10.55 (-10.90, -10.20) | -4.13 (-4.60, -3.67) | +32.63 (+31.39, +33.97) | +0.51 (+0.42, +0.61) | +20.60 (+20.02, +21.16) | +26.94 (+26.28, +27.59) | +27.09 (+26.80, +27.37) | +83.42 (+82.74, +84.08) | no (inflation) |
| m6.0 | Pareto point | Stress | -4.09 (-4.28, -3.90) | -1.28 (-1.45, -1.11) | +16.40 (+15.77, +17.00) | +0.32 (+0.27, +0.36) | +9.48 (+9.17, +9.81) | +14.03 (+13.50, +14.57) | +10.69 (+10.44, +10.92) | +43.07 (+42.19, +43.97) | no (inflation) |
| h184 | Pareto point | Reference | -10.21 (-10.46, -9.97) | -4.55 (-5.01, -4.10) | +12.74 (+11.57, +13.91) | +0.34 (+0.29, +0.40) | +13.81 (+13.02, +14.60) | +8.02 (+7.58, +8.50) | +21.44 (+21.23, +21.63) | +84.32 (+83.66, +84.96) | no (inflation) |
| h184 | Pareto point | Adverse | -10.54 (-10.89, -10.18) | -4.31 (-4.76, -3.85) | +32.80 (+31.55, +34.13) | +0.50 (+0.41, +0.59) | +20.82 (+20.21, +21.41) | +27.22 (+26.58, +27.88) | +27.58 (+27.30, +27.87) | +84.02 (+83.36, +84.68) | no (inflation) |
| h184 | Pareto point | Stress | -3.99 (-4.18, -3.80) | -1.25 (-1.42, -1.07) | +16.46 (+15.84, +17.04) | +0.31 (+0.26, +0.36) | +9.56 (+9.25, +9.89) | +14.27 (+13.74, +14.82) | +10.65 (+10.41, +10.88) | +43.17 (+42.29, +44.07) | no (inflation) |
| m6.1 | Pareto point | Reference | -10.11 (-10.37, -9.89) | -4.21 (-4.65, -3.78) | +12.63 (+11.57, +13.72) | +0.37 (+0.32, +0.43) | +13.67 (+12.91, +14.44) | +7.61 (+7.17, +8.07) | +20.89 (+20.69, +21.09) | +83.42 (+82.73, +84.08) | no (inflation) |
| m6.1 | Pareto point | Adverse | -10.45 (-10.80, -10.09) | -4.10 (-4.56, -3.63) | +32.60 (+31.36, +33.94) | +0.48 (+0.39, +0.57) | +20.50 (+19.91, +21.07) | +26.91 (+26.24, +27.56) | +26.96 (+26.67, +27.25) | +83.42 (+82.74, +84.08) | no (inflation) |
| m6.1 | Pareto point | Stress | -4.06 (-4.25, -3.87) | -1.28 (-1.45, -1.10) | +16.30 (+15.68, +16.89) | +0.31 (+0.26, +0.35) | +9.43 (+9.12, +9.76) | +13.95 (+13.43, +14.48) | +10.65 (+10.40, +10.88) | +43.06 (+42.19, +43.96) | no (inflation) |
| m6.4 | Pareto point | Reference | -9.84 (-10.09, -9.61) | -4.04 (-4.46, -3.62) | +12.77 (+11.72, +13.85) | +0.33 (+0.27, +0.38) | +13.77 (+13.00, +14.54) | +7.93 (+7.50, +8.38) | +20.71 (+20.50, +20.91) | +83.42 (+82.73, +84.07) | no (inflation) |
| m6.4 | Pareto point | Adverse | -10.22 (-10.57, -9.86) | -3.98 (-4.44, -3.51) | +32.55 (+31.34, +33.86) | +0.43 (+0.34, +0.52) | +20.65 (+20.06, +21.21) | +27.00 (+26.34, +27.66) | +26.85 (+26.56, +27.14) | +83.42 (+82.74, +84.08) | no (inflation) |
| m6.4 | Pareto point | Stress | -3.92 (-4.12, -3.73) | -1.22 (-1.39, -1.04) | +16.29 (+15.67, +16.87) | +0.30 (+0.25, +0.35) | +9.53 (+9.22, +9.86) | +14.14 (+13.62, +14.69) | +10.55 (+10.30, +10.77) | +43.06 (+42.19, +43.96) | no (inflation) |
| h197 | Pareto point | Reference | -8.68 (-8.99, -8.39) | +0.13 (-0.62, +0.86) | -1.50 (-2.14, -0.89) | -0.27 (-0.32, -0.22) | -4.39 (-4.86, -3.94) | -7.21 (-7.57, -6.86) | +1108.46 (+1083.45, +1135.32) | +84.50 (+83.84, +85.14) | no (inflation) |
| h197 | Pareto point | Adverse | -9.95 (-10.28, -9.59) | -0.86 (-1.42, -0.27) | -6.75 (-7.48, -6.04) | -0.79 (-0.88, -0.71) | -7.45 (-8.03, -6.90) | -12.58 (-13.10, -12.11) | +1384.10 (+1350.21, +1420.33) | +84.31 (+83.64, +84.96) | yes (inflation) |
| h197 | Pareto point | Stress | +0.76 (+0.52, +1.00) | +4.67 (+4.36, +4.98) | -2.90 (-3.36, -2.44) | -0.48 (-0.54, -0.43) | -3.49 (-3.72, -3.26) | -5.55 (-5.96, -5.17) | +1216.89 (+1185.72, +1249.72) | +43.14 (+42.26, +44.04) | no (inflation) |
| h189 | Pareto point | Reference | -8.11 (-8.43, -7.81) | +0.96 (+0.24, +1.66) | -0.65 (-1.24, -0.05) | -0.28 (-0.32, -0.23) | -3.71 (-4.20, -3.23) | -6.75 (-7.16, -6.34) | +1080.89 (+1056.38, +1107.15) | +83.28 (+82.60, +83.94) | no (inflation) |
| h189 | Pareto point | Adverse | -9.35 (-9.69, -8.99) | -0.15 (-0.71, +0.43) | -6.36 (-7.09, -5.66) | -0.84 (-0.92, -0.76) | -6.73 (-7.27, -6.19) | -12.18 (-12.70, -11.70) | +1345.90 (+1312.64, +1381.10) | +83.28 (+82.60, +83.94) | yes (inflation) |
| h189 | Pareto point | Stress | +0.91 (+0.67, +1.15) | +4.78 (+4.48, +5.07) | -2.83 (-3.29, -2.37) | -0.48 (-0.54, -0.43) | -3.39 (-3.62, -3.17) | -5.44 (-5.86, -5.04) | +1204.10 (+1172.89, +1236.74) | +42.94 (+42.06, +43.83) | no (inflation) |
| h62 | Pareto point | Reference | -7.27 (-7.56, -6.99) | +0.95 (+0.25, +1.64) | -0.91 (-1.47, -0.35) | -0.26 (-0.30, -0.21) | -3.73 (-4.18, -3.29) | -6.23 (-6.62, -5.85) | +1084.46 (+1059.72, +1111.07) | +84.37 (+83.71, +85.02) | no (inflation) |
| h62 | Pareto point | Adverse | -8.38 (-8.70, -8.03) | -0.01 (-0.55, +0.54) | -6.02 (-6.70, -5.35) | -0.79 (-0.88, -0.70) | -6.71 (-7.26, -6.17) | -11.31 (-11.81, -10.85) | +1351.83 (+1318.27, +1387.38) | +84.18 (+83.51, +84.83) | no (inflation) |
| h62 | Pareto point | Stress | +1.53 (+1.28, +1.76) | +5.02 (+4.73, +5.31) | -2.69 (-3.15, -2.23) | -0.47 (-0.52, -0.42) | -3.20 (-3.41, -3.00) | -5.09 (-5.47, -4.70) | +1203.40 (+1172.11, +1236.25) | +43.12 (+42.25, +44.02) | no (inflation) |
| m9.9 | Pareto point | Reference | -6.53 (-6.80, -6.25) | +1.30 (+0.64, +1.94) | -0.77 (-1.30, -0.26) | -0.25 (-0.30, -0.21) | -3.42 (-3.87, -3.00) | -5.84 (-6.21, -5.48) | +1068.46 (+1044.10, +1094.83) | +84.31 (+83.64, +84.96) | no (inflation) |
| m9.9 | Pareto point | Adverse | -7.56 (-7.87, -7.25) | +0.42 (-0.10, +0.95) | -5.59 (-6.28, -4.93) | -0.77 (-0.85, -0.68) | -6.37 (-6.89, -5.87) | -10.72 (-11.24, -10.25) | +1332.50 (+1299.00, +1367.81) | +84.12 (+83.45, +84.78) | no (inflation) |
| m9.9 | Pareto point | Stress | +1.89 (+1.67, +2.10) | +5.23 (+4.95, +5.51) | -2.58 (-3.02, -2.13) | -0.46 (-0.51, -0.41) | -3.09 (-3.29, -2.90) | -4.83 (-5.22, -4.45) | +1198.75 (+1167.08, +1231.76) | +43.13 (+42.25, +44.03) | no (inflation) |
| h13 | Pareto point | Reference | -4.11 (-4.33, -3.89) | +2.84 (+2.27, +3.40) | +0.24 (-0.33, +0.81) | -0.20 (-0.24, -0.15) | -2.98 (-3.42, -2.56) | -4.39 (-4.77, -4.03) | +1064.16 (+1039.78, +1090.25) | +84.01 (+83.35, +84.66) | no (inflation) |
| h13 | Pareto point | Adverse | -5.04 (-5.33, -4.73) | +1.75 (+1.30, +2.23) | -4.68 (-5.31, -4.05) | -0.71 (-0.79, -0.63) | -5.90 (-6.39, -5.43) | -9.22 (-9.74, -8.77) | +1330.90 (+1297.61, +1366.18) | +83.91 (+83.24, +84.57) | no (inflation) |
| h13 | Pareto point | Stress | +2.60 (+2.38, +2.82) | +5.41 (+5.13, +5.71) | -2.45 (-2.88, -2.02) | -0.44 (-0.48, -0.38) | -3.06 (-3.26, -2.88) | -4.43 (-4.78, -4.10) | +1194.24 (+1163.15, +1226.68) | +43.06 (+42.18, +43.95) | no (inflation) |
| h112 | Pareto point | Reference | -4.07 (-4.32, -3.83) | +2.95 (+2.40, +3.48) | +0.41 (-0.19, +1.00) | -0.25 (-0.29, -0.21) | -2.60 (-3.02, -2.20) | -4.34 (-4.68, -4.01) | +1034.82 (+1011.02, +1060.28) | +83.41 (+82.73, +84.07) | no (inflation) |
| h112 | Pareto point | Adverse | -5.04 (-5.34, -4.74) | +1.87 (+1.41, +2.37) | -4.64 (-5.27, -4.06) | -0.77 (-0.84, -0.69) | -5.51 (-5.97, -5.09) | -9.08 (-9.59, -8.59) | +1291.23 (+1258.75, +1325.67) | +83.41 (+82.73, +84.07) | no (inflation) |
| h112 | Pareto point | Stress | +2.59 (+2.37, +2.81) | +5.44 (+5.16, +5.72) | -2.43 (-2.86, -2.01) | -0.45 (-0.50, -0.40) | -2.97 (-3.16, -2.79) | -4.44 (-4.81, -4.08) | +1179.25 (+1148.18, +1211.57) | +43.04 (+42.17, +43.94) | no (inflation) |
| h37 | Pareto point | Reference | -3.68 (-3.91, -3.45) | +3.00 (+2.43, +3.55) | +0.38 (-0.19, +0.97) | -0.23 (-0.28, -0.19) | -2.60 (-3.01, -2.20) | -4.05 (-4.40, -3.71) | +1060.43 (+1035.93, +1086.72) | +84.02 (+83.36, +84.68) | no (inflation) |
| h37 | Pareto point | Adverse | -4.61 (-4.92, -4.30) | +1.96 (+1.50, +2.43) | -4.43 (-5.05, -3.82) | -0.76 (-0.84, -0.68) | -5.52 (-5.99, -5.08) | -8.84 (-9.35, -8.38) | +1326.95 (+1293.45, +1362.43) | +83.93 (+83.26, +84.59) | no (inflation) |
| h37 | Pareto point | Stress | +2.88 (+2.66, +3.10) | +5.53 (+5.25, +5.81) | -2.35 (-2.77, -1.93) | -0.45 (-0.51, -0.40) | -2.89 (-3.08, -2.72) | -4.21 (-4.55, -3.88) | +1190.93 (+1159.64, +1223.60) | +43.08 (+42.20, +43.97) | no (inflation) |
| h90 | Pareto point | Reference | -3.52 (-3.76, -3.30) | +3.33 (+2.78, +3.86) | +0.52 (-0.06, +1.09) | -0.24 (-0.29, -0.20) | -2.47 (-2.90, -2.08) | -4.00 (-4.38, -3.66) | +1057.56 (+1033.13, +1083.73) | +83.42 (+82.73, +84.07) | no (inflation) |
| h90 | Pareto point | Adverse | -4.52 (-4.82, -4.21) | +2.18 (+1.73, +2.68) | -4.37 (-4.98, -3.79) | -0.77 (-0.85, -0.69) | -5.41 (-5.87, -4.98) | -8.83 (-9.36, -8.38) | +1323.77 (+1290.40, +1359.26) | +83.42 (+82.73, +84.07) | no (inflation) |
| h90 | Pareto point | Stress | +2.82 (+2.59, +3.04) | +5.51 (+5.22, +5.79) | -2.38 (-2.80, -1.96) | -0.45 (-0.50, -0.40) | -2.92 (-3.11, -2.75) | -4.29 (-4.65, -3.94) | +1190.89 (+1159.64, +1223.61) | +43.06 (+42.18, +43.95) | no (inflation) |
| h143 | Pareto point | Reference | -3.57 (-3.80, -3.33) | +3.21 (+2.67, +3.74) | +0.55 (-0.03, +1.10) | -0.25 (-0.30, -0.21) | -2.38 (-2.80, -2.00) | -4.00 (-4.35, -3.66) | +1040.98 (+1016.96, +1066.72) | +83.45 (+82.76, +84.11) | no (inflation) |
| h143 | Pareto point | Adverse | -4.49 (-4.77, -4.19) | +2.15 (+1.70, +2.64) | -4.28 (-4.89, -3.68) | -0.77 (-0.85, -0.70) | -5.27 (-5.70, -4.86) | -8.66 (-9.20, -8.18) | +1301.26 (+1268.06, +1336.48) | +83.45 (+82.76, +84.11) | no (inflation) |
| h143 | Pareto point | Stress | +2.93 (+2.73, +3.14) | +5.62 (+5.35, +5.89) | -2.31 (-2.72, -1.89) | -0.44 (-0.49, -0.39) | -2.85 (-3.03, -2.68) | -4.15 (-4.52, -3.81) | +1184.41 (+1152.88, +1217.26) | +43.07 (+42.20, +43.97) | no (inflation) |
| h64 | Pareto point | Reference | -3.12 (-3.33, -2.91) | +3.50 (+2.97, +4.03) | +0.55 (-0.01, +1.08) | -0.24 (-0.29, -0.20) | -2.28 (-2.68, -1.91) | -3.72 (-4.07, -3.39) | +1054.03 (+1029.59, +1080.14) | +83.46 (+82.78, +84.12) | no (inflation) |
| h64 | Pareto point | Adverse | -4.07 (-4.37, -3.76) | +2.37 (+1.93, +2.85) | -4.21 (-4.83, -3.64) | -0.77 (-0.85, -0.70) | -5.22 (-5.65, -4.80) | -8.42 (-8.94, -7.97) | +1319.40 (+1285.94, +1354.94) | +83.46 (+82.78, +84.12) | no (inflation) |
| h64 | Pareto point | Stress | +3.05 (+2.83, +3.26) | +5.60 (+5.32, +5.88) | -2.30 (-2.71, -1.88) | -0.45 (-0.50, -0.40) | -2.84 (-3.02, -2.67) | -4.06 (-4.41, -3.72) | +1188.48 (+1157.14, +1221.21) | +43.08 (+42.21, +43.97) | no (inflation) |
| h87 | Pareto point | Reference | -2.96 (-3.17, -2.75) | +3.60 (+3.06, +4.11) | +0.78 (+0.22, +1.32) | -0.24 (-0.29, -0.20) | -2.24 (-2.64, -1.87) | -3.53 (-3.88, -3.19) | +1051.84 (+1027.43, +1077.89) | +83.46 (+82.77, +84.11) | no (inflation) |
| h87 | Pareto point | Adverse | -3.91 (-4.21, -3.60) | +2.45 (+2.01, +2.92) | -4.16 (-4.79, -3.57) | -0.76 (-0.84, -0.69) | -5.17 (-5.61, -4.76) | -8.34 (-8.87, -7.87) | +1316.84 (+1283.52, +1352.21) | +83.46 (+82.77, +84.11) | no (inflation) |
| h87 | Pareto point | Stress | +3.04 (+2.82, +3.26) | +5.59 (+5.31, +5.87) | -2.31 (-2.73, -1.89) | -0.45 (-0.50, -0.40) | -2.86 (-3.04, -2.69) | -4.08 (-4.43, -3.74) | +1187.60 (+1156.34, +1220.24) | +43.08 (+42.20, +43.97) | no (inflation) |
| h103 | Pareto point | Reference | -2.93 (-3.14, -2.73) | +3.40 (+2.88, +3.92) | +0.57 (-0.01, +1.11) | -0.23 (-0.28, -0.19) | -2.41 (-2.80, -2.04) | -3.52 (-3.85, -3.20) | +1050.07 (+1025.81, +1076.14) | +83.94 (+83.28, +84.60) | no (inflation) |
| h103 | Pareto point | Adverse | -3.85 (-4.14, -3.55) | +2.32 (+1.90, +2.78) | -4.10 (-4.70, -3.55) | -0.75 (-0.84, -0.67) | -5.28 (-5.71, -4.86) | -8.30 (-8.82, -7.84) | +1314.70 (+1281.33, +1350.18) | +83.87 (+83.20, +84.53) | no (inflation) |
| h103 | Pareto point | Stress | +3.12 (+2.90, +3.33) | +5.63 (+5.36, +5.91) | -2.26 (-2.68, -1.83) | -0.44 (-0.49, -0.39) | -2.84 (-3.02, -2.67) | -4.01 (-4.38, -3.67) | +1186.12 (+1154.76, +1218.86) | +43.08 (+42.20, +43.98) | no (inflation) |
| h36 | Pareto point | Reference | -2.49 (-2.69, -2.29) | +3.63 (+3.11, +4.14) | +0.77 (+0.22, +1.31) | -0.23 (-0.28, -0.19) | -2.21 (-2.59, -1.85) | -3.17 (-3.48, -2.86) | +1044.96 (+1020.68, +1070.96) | +83.88 (+83.21, +84.54) | no (inflation) |
| h36 | Pareto point | Adverse | -3.40 (-3.68, -3.10) | +2.54 (+2.13, +2.99) | -4.05 (-4.66, -3.49) | -0.76 (-0.84, -0.68) | -5.11 (-5.53, -4.71) | -8.06 (-8.60, -7.57) | +1308.63 (+1275.32, +1344.04) | +83.81 (+83.14, +84.47) | no (inflation) |
| h36 | Pareto point | Stress | +3.30 (+3.09, +3.52) | +5.71 (+5.43, +5.99) | -2.20 (-2.61, -1.78) | -0.44 (-0.49, -0.39) | -2.78 (-2.95, -2.61) | -3.85 (-4.22, -3.51) | +1183.44 (+1152.08, +1216.14) | +43.05 (+42.17, +43.95) | no (inflation) |
| m5.8 | Pareto point | Reference | -2.51 (-2.72, -2.31) | +3.61 (+3.09, +4.12) | +0.79 (+0.25, +1.31) | -0.23 (-0.27, -0.19) | -2.21 (-2.60, -1.85) | -3.17 (-3.50, -2.85) | +1044.12 (+1019.81, +1070.13) | +83.90 (+83.24, +84.56) | no (inflation) |
| m5.8 | Pareto point | Adverse | -3.39 (-3.67, -3.09) | +2.53 (+2.13, +2.97) | -4.01 (-4.62, -3.44) | -0.76 (-0.84, -0.68) | -5.10 (-5.53, -4.71) | -8.07 (-8.60, -7.59) | +1307.36 (+1274.05, +1342.65) | +83.84 (+83.17, +84.50) | no (inflation) |
| m5.8 | Pareto point | Stress | +3.34 (+3.12, +3.55) | +5.72 (+5.44, +5.99) | -2.18 (-2.59, -1.77) | -0.44 (-0.49, -0.39) | -2.78 (-2.95, -2.61) | -3.79 (-4.16, -3.45) | +1182.55 (+1151.23, +1215.04) | +43.09 (+42.21, +43.99) | no (inflation) |
| m5.11 | Pareto point | Reference | -2.49 (-2.70, -2.29) | +3.62 (+3.10, +4.13) | +0.79 (+0.25, +1.31) | -0.23 (-0.27, -0.19) | -2.20 (-2.59, -1.84) | -3.15 (-3.47, -2.84) | +1044.05 (+1019.74, +1070.06) | +83.90 (+83.24, +84.56) | no (inflation) |
| m5.11 | Pareto point | Adverse | -3.37 (-3.65, -3.07) | +2.54 (+2.14, +2.99) | -4.01 (-4.62, -3.44) | -0.76 (-0.84, -0.68) | -5.10 (-5.52, -4.70) | -8.04 (-8.56, -7.56) | +1307.34 (+1274.02, +1342.66) | +83.84 (+83.17, +84.50) | no (inflation) |
| m5.11 | Pareto point | Stress | +3.34 (+3.12, +3.55) | +5.72 (+5.44, +5.99) | -2.18 (-2.59, -1.77) | -0.44 (-0.49, -0.39) | -2.78 (-2.95, -2.61) | -3.79 (-4.16, -3.45) | +1182.32 (+1151.00, +1214.81) | +43.09 (+42.21, +43.99) | no (inflation) |
| m6.12 | Pareto point | Reference | -2.28 (-2.48, -2.08) | +3.73 (+3.21, +4.24) | +0.91 (+0.37, +1.44) | -0.23 (-0.28, -0.19) | -2.12 (-2.51, -1.77) | -2.99 (-3.29, -2.69) | +1042.86 (+1018.59, +1068.87) | +83.76 (+83.10, +84.42) | no (inflation) |
| m6.12 | Pareto point | Adverse | -3.17 (-3.44, -2.88) | +2.66 (+2.26, +3.10) | -3.99 (-4.61, -3.41) | -0.76 (-0.84, -0.68) | -5.02 (-5.44, -4.63) | -7.86 (-8.38, -7.40) | +1306.69 (+1273.14, +1342.27) | +83.72 (+83.05, +84.38) | no (inflation) |
| m6.12 | Pareto point | Stress | +3.43 (+3.22, +3.64) | +5.78 (+5.51, +6.05) | -2.16 (-2.57, -1.75) | -0.43 (-0.48, -0.39) | -2.74 (-2.91, -2.57) | -3.74 (-4.12, -3.40) | +1183.16 (+1151.68, +1215.82) | +42.97 (+42.09, +43.86) | no (inflation) |
| fflat | Pareto point | Reference | +19.42 (+18.78, +20.05) | +35.51 (+34.27, +36.78) | +32.24 (+30.87, +33.67) | +3.91 (+3.66, +4.16) | +16.66 (+15.72, +17.63) | +14.79 (+14.14, +15.46) | -0.03 (-0.04, -0.03) | +83.11 (+82.47, +83.76) | no |
| fflat | Pareto point | Adverse | +13.15 (+12.49, +13.83) | +25.45 (+24.49, +26.43) | +32.29 (+31.14, +33.43) | +3.52 (+3.34, +3.69) | +17.04 (+16.32, +17.76) | +18.48 (+17.82, +19.16) | +0.00 (+0.00, +0.00) | +70.63 (+69.88, +71.36) | no |
| fflat | Pareto point | Stress | +5.77 (+5.32, +6.23) | +13.74 (+13.11, +14.36) | +14.86 (+14.24, +15.53) | +0.81 (+0.74, +0.89) | +8.33 (+7.90, +8.75) | +8.42 (+7.88, +8.97) | +0.00 (+0.00, +0.00) | +35.60 (+34.84, +36.40) | no |

### release row, wages 90%

| Setting | Role | Environment | basket poverty, % of adult-years | non-participants' basket poverty, % | non-participants' wealth poverty, % | non-participants' income drops of 25%+ with no buffer, per 100 | non-participants under 3 months of basics covered, % | wealth poverty at year 20, % | programme inflation, points a year | participation, mean of years 1-19, % | Passes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| t0 | Pareto point | Reference | -13.55 (-13.98, -13.14) | +6.95 (+5.79, +8.22) | +63.72 (+62.40, +64.99) | +0.78 (+0.68, +0.86) | +35.72 (+34.86, +36.63) | +57.97 (+57.44, +58.46) | +70.67 (+70.03, +71.27) | +83.62 (+82.94, +84.28) | no (inflation) |
| t0 | Pareto point | Adverse | -15.61 (-16.06, -15.13) | +2.07 (+1.20, +2.92) | +55.63 (+54.48, +56.80) | +0.81 (+0.68, +0.94) | +35.04 (+34.34, +35.74) | +52.98 (+52.43, +53.51) | +88.28 (+87.38, +89.14) | +83.62 (+82.94, +84.27) | no (inflation) |
| t0 | Pareto point | Stress | -2.42 (-2.82, -2.01) | +7.17 (+6.67, +7.69) | +51.91 (+51.04, +52.79) | +1.03 (+0.96, +1.09) | +29.12 (+28.62, +29.66) | +47.90 (+47.22, +48.58) | +38.15 (+37.28, +38.99) | +43.11 (+42.22, +44.00) | no (inflation) |
| bt0 | Pareto point | Reference | -12.94 (-13.36, -12.54) | +7.98 (+6.82, +9.25) | +63.89 (+62.59, +65.17) | +0.83 (+0.73, +0.92) | +36.30 (+35.47, +37.18) | +58.10 (+57.54, +58.61) | +70.47 (+69.77, +71.11) | +83.09 (+82.40, +83.77) | no (inflation) |
| bt0 | Pareto point | Adverse | -15.06 (-15.50, -14.57) | +2.88 (+2.05, +3.72) | +55.62 (+54.47, +56.77) | +0.84 (+0.71, +0.98) | +35.42 (+34.74, +36.12) | +53.02 (+52.48, +53.55) | +88.19 (+87.26, +89.09) | +83.17 (+82.48, +83.83) | no (inflation) |
| bt0 | Pareto point | Stress | -2.33 (-2.72, -1.92) | +7.22 (+6.72, +7.76) | +51.97 (+51.11, +52.84) | +1.02 (+0.95, +1.08) | +29.06 (+28.57, +29.61) | +48.02 (+47.37, +48.70) | +37.80 (+36.92, +38.66) | +43.01 (+42.13, +43.90) | no (inflation) |
| t4 | Pareto point | Reference | -12.45 (-12.86, -12.04) | +7.73 (+6.57, +8.97) | +64.03 (+62.72, +65.32) | +0.75 (+0.67, +0.84) | +36.01 (+35.16, +36.91) | +58.58 (+57.99, +59.11) | +69.84 (+69.19, +70.45) | +83.49 (+82.82, +84.15) | no (inflation) |
| t4 | Pareto point | Adverse | -14.53 (-14.97, -14.06) | +2.81 (+1.96, +3.65) | +55.75 (+54.57, +56.92) | +0.81 (+0.68, +0.94) | +35.29 (+34.60, +35.97) | +53.36 (+52.80, +53.93) | +87.50 (+86.60, +88.37) | +83.49 (+82.81, +84.15) | no (inflation) |
| t4 | Pareto point | Stress | -2.20 (-2.59, -1.79) | +7.18 (+6.68, +7.72) | +51.82 (+50.94, +52.71) | +1.01 (+0.94, +1.08) | +28.91 (+28.41, +29.45) | +47.81 (+47.13, +48.50) | +37.09 (+36.24, +37.93) | +43.08 (+42.20, +43.98) | no (inflation) |
| t8 | Pareto point | Reference | -11.35 (-11.75, -10.95) | +8.66 (+7.52, +9.90) | +64.42 (+63.14, +65.66) | +0.73 (+0.65, +0.81) | +36.37 (+35.54, +37.24) | +59.14 (+58.58, +59.67) | +68.86 (+68.20, +69.48) | +83.27 (+82.59, +83.92) | no (inflation) |
| t8 | Pareto point | Adverse | -13.53 (-13.96, -13.08) | +3.53 (+2.73, +4.34) | +55.83 (+54.66, +56.99) | +0.79 (+0.67, +0.92) | +35.53 (+34.87, +36.23) | +53.70 (+53.17, +54.23) | +86.63 (+85.71, +87.51) | +83.33 (+82.66, +83.99) | no (inflation) |
| t8 | Pareto point | Stress | -1.98 (-2.38, -1.57) | +7.18 (+6.67, +7.71) | +51.76 (+50.88, +52.67) | +0.98 (+0.91, +1.05) | +28.71 (+28.21, +29.25) | +47.80 (+47.11, +48.50) | +36.01 (+35.18, +36.84) | +43.06 (+42.19, +43.96) | no (inflation) |
| fland | Pareto point | Reference | -11.70 (-12.19, -11.22) | +6.62 (+5.37, +7.96) | +8.37 (+6.77, +9.89) | +1.05 (+0.95, +1.15) | +5.08 (+4.05, +6.18) | -10.60 (-11.30, -9.89) | +5.89 (+5.74, +6.04) | +80.25 (+79.50, +81.03) | no (inflation) |
| fland | Pareto point | Adverse | -13.15 (-13.74, -12.60) | +4.97 (+3.92, +6.04) | +49.11 (+47.78, +50.45) | +0.97 (+0.83, +1.10) | +18.53 (+17.66, +19.41) | +40.20 (+39.28, +41.08) | +20.94 (+19.93, +21.91) | +82.89 (+82.20, +83.58) | no (inflation) |
| fland | Pareto point | Stress | -1.50 (-1.88, -1.12) | +6.20 (+5.76, +6.65) | +4.43 (+3.94, +4.91) | +0.17 (+0.13, +0.22) | +2.26 (+1.96, +2.57) | -2.25 (-2.72, -1.80) | +1.37 (+1.31, +1.43) | +37.04 (+36.22, +37.92) | no |
| kp50 | Pareto point | Reference | -10.81 (-11.21, -10.42) | +8.96 (+7.86, +10.14) | +64.36 (+63.10, +65.64) | +0.70 (+0.62, +0.79) | +36.16 (+35.35, +37.01) | +59.10 (+58.54, +59.63) | +66.32 (+65.65, +66.95) | +83.16 (+82.47, +83.82) | no (inflation) |
| kp50 | Pareto point | Adverse | -12.92 (-13.35, -12.46) | +3.91 (+3.11, +4.73) | +55.87 (+54.68, +57.02) | +0.77 (+0.64, +0.89) | +35.43 (+34.76, +36.12) | +53.87 (+53.32, +54.43) | +84.25 (+83.30, +85.16) | +83.25 (+82.57, +83.91) | no (inflation) |
| kp50 | Pareto point | Stress | -1.61 (-1.98, -1.21) | +6.99 (+6.49, +7.50) | +51.04 (+50.14, +51.98) | +0.92 (+0.85, +0.98) | +27.77 (+27.26, +28.33) | +47.23 (+46.53, +47.96) | +33.07 (+32.28, +33.84) | +43.04 (+42.16, +43.93) | no (inflation) |
| ixn | Pareto point | Reference | -10.72 (-11.12, -10.32) | +8.04 (+6.95, +9.24) | +64.86 (+63.60, +66.11) | +1.09 (+1.00, +1.17) | +36.03 (+35.20, +36.91) | +59.99 (+59.43, +60.53) | +69.14 (+68.48, +69.77) | +83.99 (+83.32, +84.65) | no (inflation) |
| ixn | Pareto point | Adverse | -13.12 (-13.53, -12.68) | +2.71 (+1.94, +3.52) | +55.89 (+54.70, +57.06) | +1.09 (+0.96, +1.23) | +35.16 (+34.46, +35.86) | +53.96 (+53.41, +54.51) | +87.40 (+86.50, +88.28) | +84.17 (+83.51, +84.83) | no (inflation) |
| ixn | Pareto point | Stress | -1.52 (-1.90, -1.12) | +7.07 (+6.57, +7.58) | +51.20 (+50.30, +52.12) | +0.94 (+0.88, +1.01) | +27.98 (+27.48, +28.54) | +47.39 (+46.70, +48.12) | +33.33 (+32.54, +34.11) | +43.15 (+42.28, +44.05) | no (inflation) |
| pr0c75 | Pareto point | Reference | -10.72 (-11.13, -10.31) | +8.95 (+7.85, +10.15) | +64.53 (+63.21, +65.85) | +0.66 (+0.58, +0.74) | +36.35 (+35.53, +37.21) | +59.50 (+58.92, +60.05) | +67.93 (+67.29, +68.54) | +83.39 (+82.70, +84.04) | no (inflation) |
| pr0c75 | Pareto point | Adverse | -12.90 (-13.33, -12.46) | +3.80 (+3.00, +4.62) | +55.89 (+54.70, +57.06) | +0.73 (+0.60, +0.87) | +35.56 (+34.89, +36.25) | +53.90 (+53.36, +54.47) | +85.70 (+84.79, +86.58) | +83.42 (+82.74, +84.07) | no (inflation) |
| pr0c75 | Pareto point | Stress | -1.58 (-1.96, -1.17) | +7.03 (+6.53, +7.55) | +51.12 (+50.21, +52.06) | +0.93 (+0.86, +0.99) | +27.90 (+27.38, +28.45) | +47.24 (+46.51, +48.00) | +33.30 (+32.51, +34.07) | +43.04 (+42.17, +43.94) | no (inflation) |
| kp25 | Pareto point | Reference | -10.55 (-10.95, -10.15) | +9.18 (+8.08, +10.37) | +64.51 (+63.22, +65.78) | +0.70 (+0.62, +0.79) | +36.42 (+35.60, +37.27) | +59.38 (+58.81, +59.91) | +67.12 (+66.45, +67.76) | +83.16 (+82.48, +83.82) | no (inflation) |
| kp25 | Pareto point | Adverse | -12.74 (-13.17, -12.29) | +4.02 (+3.21, +4.84) | +55.89 (+54.70, +57.06) | +0.77 (+0.64, +0.90) | +35.59 (+34.92, +36.28) | +53.90 (+53.35, +54.46) | +85.02 (+84.08, +85.93) | +83.25 (+82.57, +83.91) | no (inflation) |
| kp25 | Pareto point | Stress | -1.58 (-1.96, -1.18) | +7.01 (+6.51, +7.52) | +51.06 (+50.15, +51.99) | +0.91 (+0.85, +0.98) | +27.82 (+27.30, +28.38) | +47.24 (+46.55, +47.98) | +33.11 (+32.32, +33.88) | +43.04 (+42.16, +43.93) | no (inflation) |
| kp10 | Pareto point | Reference | -10.39 (-10.79, -9.99) | +9.32 (+8.22, +10.49) | +64.65 (+63.35, +65.93) | +0.71 (+0.62, +0.79) | +36.56 (+35.75, +37.42) | +59.60 (+59.05, +60.14) | +67.59 (+66.93, +68.23) | +83.16 (+82.48, +83.82) | no (inflation) |
| kp10 | Pareto point | Adverse | -12.64 (-13.07, -12.19) | +4.09 (+3.29, +4.91) | +55.89 (+54.70, +57.06) | +0.78 (+0.64, +0.91) | +35.68 (+35.01, +36.36) | +53.91 (+53.36, +54.48) | +85.48 (+84.54, +86.38) | +83.25 (+82.57, +83.91) | no (inflation) |
| kp10 | Pareto point | Stress | -1.57 (-1.95, -1.17) | +7.03 (+6.52, +7.54) | +51.06 (+50.15, +51.99) | +0.92 (+0.85, +0.98) | +27.85 (+27.33, +28.41) | +47.24 (+46.55, +47.98) | +33.13 (+32.34, +33.90) | +43.04 (+42.16, +43.93) | no (inflation) |
| no6 | Pareto point | Reference | -10.28 (-10.69, -9.90) | +9.41 (+8.31, +10.58) | +64.72 (+63.43, +66.00) | +0.71 (+0.62, +0.80) | +36.67 (+35.87, +37.52) | +59.73 (+59.18, +60.26) | +67.91 (+67.24, +68.55) | +83.16 (+82.48, +83.82) | no (inflation) |
| no6 | Pareto point | Adverse | -12.56 (-12.99, -12.11) | +4.15 (+3.35, +4.96) | +55.89 (+54.70, +57.06) | +0.77 (+0.64, +0.91) | +35.73 (+35.05, +36.42) | +53.92 (+53.38, +54.48) | +85.78 (+84.84, +86.68) | +83.25 (+82.57, +83.91) | no (inflation) |
| no6 | Pareto point | Stress | -1.60 (-1.98, -1.20) | +7.01 (+6.51, +7.52) | +50.77 (+49.86, +51.69) | +0.91 (+0.85, +0.98) | +27.83 (+27.31, +28.39) | +46.60 (+45.89, +47.33) | +33.06 (+32.28, +33.82) | +43.04 (+42.16, +43.93) | no (inflation) |
| phi0 | Pareto point | Reference | -10.16 (-10.55, -9.77) | +9.47 (+8.37, +10.63) | +64.78 (+63.50, +66.05) | +0.70 (+0.61, +0.79) | +36.71 (+35.90, +37.55) | +59.78 (+59.24, +60.30) | +68.00 (+67.34, +68.64) | +83.17 (+82.49, +83.84) | no (inflation) |
| phi0 | Pareto point | Adverse | -12.47 (-12.89, -12.01) | +4.19 (+3.39, +5.00) | +55.89 (+54.70, +57.06) | +0.77 (+0.64, +0.90) | +35.76 (+35.08, +36.45) | +53.94 (+53.40, +54.50) | +85.90 (+84.96, +86.80) | +83.26 (+82.58, +83.92) | no (inflation) |
| phi0 | Pareto point | Stress | -1.52 (-1.90, -1.13) | +7.05 (+6.56, +7.56) | +51.08 (+50.19, +52.01) | +0.91 (+0.84, +0.98) | +27.84 (+27.33, +28.41) | +47.27 (+46.56, +48.01) | +33.07 (+32.28, +33.84) | +43.04 (+42.16, +43.93) | no (inflation) |
| ph5 | Pareto point | Reference | -9.88 (-10.27, -9.50) | +9.00 (+7.89, +10.17) | +64.37 (+63.08, +65.65) | +0.61 (+0.53, +0.69) | +35.46 (+34.68, +36.28) | +59.17 (+58.56, +59.76) | +64.75 (+64.12, +65.37) | +83.18 (+82.50, +83.84) | no (inflation) |
| ph5 | Pareto point | Adverse | -11.98 (-12.41, -11.52) | +4.12 (+3.36, +4.90) | +55.87 (+54.70, +57.02) | +0.68 (+0.55, +0.81) | +34.83 (+34.19, +35.48) | +53.90 (+53.37, +54.44) | +82.00 (+81.11, +82.86) | +83.27 (+82.59, +83.93) | no (inflation) |
| ph5 | Pareto point | Stress | -1.98 (-2.33, -1.61) | +6.29 (+5.84, +6.75) | +50.17 (+49.22, +51.15) | +0.85 (+0.78, +0.91) | +25.95 (+25.45, +26.49) | +46.03 (+45.27, +46.82) | +31.14 (+30.40, +31.87) | +43.04 (+42.16, +43.94) | no (inflation) |
| ph10 | Pareto point | Reference | -9.11 (-9.49, -8.74) | +8.79 (+7.73, +9.91) | +63.88 (+62.62, +65.11) | +0.58 (+0.50, +0.66) | +34.46 (+33.68, +35.28) | +58.19 (+57.62, +58.76) | +60.71 (+60.10, +61.30) | +83.26 (+82.58, +83.92) | no (inflation) |
| ph10 | Pareto point | Adverse | -10.95 (-11.37, -10.51) | +4.39 (+3.66, +5.17) | +55.79 (+54.62, +56.95) | +0.62 (+0.50, +0.75) | +34.23 (+33.59, +34.88) | +53.75 (+53.22, +54.29) | +77.10 (+76.25, +77.92) | +83.33 (+82.64, +83.99) | no (inflation) |
| ph10 | Pareto point | Stress | -2.28 (-2.60, -1.92) | +5.54 (+5.13, +6.00) | +48.80 (+47.83, +49.81) | +0.76 (+0.69, +0.83) | +23.74 (+23.25, +24.25) | +44.11 (+43.33, +44.92) | +28.44 (+27.74, +29.11) | +43.04 (+42.16, +43.94) | no (inflation) |
| bt25 | Pareto point | Reference | -7.43 (-7.83, -7.06) | +10.77 (+9.74, +11.85) | +65.40 (+64.21, +66.61) | +0.64 (+0.56, +0.71) | +36.91 (+36.11, +37.74) | +61.23 (+60.68, +61.74) | +64.99 (+64.35, +65.63) | +83.31 (+82.63, +83.97) | no (inflation) |
| bt25 | Pareto point | Adverse | -10.00 (-10.40, -9.57) | +5.40 (+4.64, +6.20) | +56.09 (+54.91, +57.25) | +0.70 (+0.58, +0.83) | +35.94 (+35.26, +36.62) | +54.44 (+53.85, +55.02) | +82.67 (+81.78, +83.54) | +83.37 (+82.69, +84.04) | no (inflation) |
| bt25 | Pareto point | Stress | -1.32 (-1.66, -0.94) | +6.91 (+6.44, +7.41) | +50.46 (+49.52, +51.44) | +0.88 (+0.81, +0.94) | +27.18 (+26.66, +27.75) | +46.71 (+45.96, +47.50) | +31.19 (+30.44, +31.93) | +43.04 (+42.16, +43.94) | no (inflation) |
| bu80 | Pareto point | Reference | -5.26 (-5.65, -4.89) | +10.82 (+9.85, +11.87) | +63.81 (+62.53, +65.09) | +0.57 (+0.49, +0.65) | +36.13 (+35.34, +36.94) | +58.79 (+58.24, +59.35) | +56.92 (+56.38, +57.44) | +83.42 (+82.73, +84.08) | no (inflation) |
| bu80 | Pareto point | Adverse | -8.21 (-8.61, -7.80) | +5.78 (+5.07, +6.53) | +55.93 (+54.70, +57.10) | +0.66 (+0.53, +0.78) | +35.48 (+34.81, +36.14) | +53.99 (+53.44, +54.54) | +71.09 (+70.36, +71.81) | +83.43 (+82.74, +84.08) | no (inflation) |
| bu80 | Pareto point | Stress | -0.96 (-1.28, -0.61) | +6.32 (+5.88, +6.78) | +47.71 (+46.74, +48.73) | +0.78 (+0.72, +0.85) | +24.93 (+24.42, +25.48) | +43.16 (+42.38, +43.96) | +26.28 (+25.66, +26.89) | +43.04 (+42.16, +43.94) | no (inflation) |
| h10 | Pareto point | Reference | -4.40 (-4.79, -4.04) | +10.40 (+9.44, +11.39) | +64.37 (+63.07, +65.64) | +0.86 (+0.79, +0.94) | +35.64 (+34.85, +36.45) | +59.74 (+59.20, +60.26) | +55.20 (+54.67, +55.71) | +83.99 (+83.34, +84.64) | no (inflation) |
| h10 | Pareto point | Adverse | -7.13 (-7.49, -6.74) | +5.55 (+4.87, +6.24) | +56.00 (+54.81, +57.17) | +0.90 (+0.78, +1.02) | +35.15 (+34.50, +35.79) | +54.30 (+53.72, +54.88) | +69.96 (+69.24, +70.67) | +84.17 (+83.50, +84.81) | no (inflation) |
| h10 | Pareto point | Stress | -1.13 (-1.47, -0.78) | +6.15 (+5.71, +6.61) | +47.55 (+46.57, +48.56) | +0.78 (+0.71, +0.85) | +24.66 (+24.15, +25.21) | +42.87 (+42.10, +43.65) | +26.19 (+25.55, +26.80) | +43.13 (+42.26, +44.03) | no (inflation) |
| svc | Pareto point | Reference | -4.83 (-5.22, -4.46) | +13.59 (+12.59, +14.67) | +50.18 (+48.89, +51.55) | +0.78 (+0.69, +0.86) | +29.64 (+28.62, +30.62) | +33.57 (+32.88, +34.25) | +89.14 (+88.16, +90.12) | +83.25 (+82.56, +83.91) | no (inflation) |
| svc | Pareto point | Adverse | -7.49 (-7.89, -7.08) | +7.28 (+6.53, +8.05) | +45.27 (+44.03, +46.49) | +0.80 (+0.67, +0.94) | +27.23 (+26.38, +28.08) | +32.38 (+31.79, +33.01) | +119.75 (+118.27, +121.25) | +83.35 (+82.66, +84.01) | no (inflation) |
| svc | Pareto point | Stress | +0.83 (+0.48, +1.21) | +8.98 (+8.48, +9.49) | +49.18 (+48.27, +50.16) | +1.02 (+0.95, +1.09) | +27.56 (+27.06, +28.06) | +43.20 (+42.57, +43.85) | +41.99 (+40.97, +43.00) | +43.04 (+42.16, +43.93) | no (inflation) |
| bu60 | Pareto point | Reference | -3.48 (-3.83, -3.16) | +9.59 (+8.71, +10.53) | +59.03 (+57.68, +60.37) | +0.52 (+0.45, +0.59) | +33.38 (+32.56, +34.17) | +51.41 (+50.73, +52.08) | +42.58 (+42.18, +42.96) | +83.43 (+82.74, +84.09) | no (inflation) |
| bu60 | Pareto point | Adverse | -5.50 (-5.87, -5.10) | +6.10 (+5.46, +6.76) | +55.68 (+54.49, +56.85) | +0.61 (+0.48, +0.73) | +33.68 (+33.04, +34.34) | +53.30 (+52.77, +53.84) | +52.90 (+52.37, +53.43) | +83.43 (+82.74, +84.09) | no (inflation) |
| bu60 | Pareto point | Stress | -0.45 (-0.75, -0.15) | +5.32 (+4.94, +5.71) | +41.07 (+40.03, +42.21) | +0.65 (+0.58, +0.71) | +20.65 (+20.16, +21.18) | +36.41 (+35.50, +37.33) | +19.50 (+19.04, +19.95) | +43.04 (+42.16, +43.94) | no (inflation) |
| h119 | Pareto point | Reference | -3.08 (-3.47, -2.74) | +10.36 (+9.47, +11.28) | +63.40 (+62.20, +64.63) | +0.76 (+0.68, +0.83) | +34.02 (+33.23, +34.81) | +59.10 (+58.48, +59.69) | +47.94 (+47.44, +48.44) | +83.99 (+83.33, +84.63) | no (inflation) |
| h119 | Pareto point | Adverse | -4.81 (-5.15, -4.45) | +6.61 (+5.98, +7.24) | +56.17 (+54.96, +57.33) | +0.80 (+0.69, +0.92) | +34.22 (+33.60, +34.84) | +54.58 (+54.00, +55.18) | +62.60 (+61.87, +63.34) | +84.11 (+83.45, +84.75) | no (inflation) |
| h119 | Pareto point | Stress | -0.92 (-1.22, -0.59) | +5.18 (+4.81, +5.57) | +43.27 (+42.22, +44.43) | +0.66 (+0.60, +0.72) | +20.72 (+20.21, +21.26) | +38.98 (+38.03, +39.97) | +21.07 (+20.53, +21.60) | +43.10 (+42.23, +44.00) | no (inflation) |
| h100 | Pareto point | Reference | -2.39 (-2.76, -2.05) | +14.06 (+13.11, +15.02) | +52.19 (+51.01, +53.43) | +0.68 (+0.60, +0.76) | +30.07 (+29.17, +30.94) | +37.13 (+36.46, +37.78) | +79.69 (+78.77, +80.62) | +83.10 (+82.43, +83.76) | no (inflation) |
| h100 | Pareto point | Adverse | -4.87 (-5.24, -4.48) | +8.30 (+7.65, +8.99) | +46.65 (+45.38, +47.83) | +0.69 (+0.56, +0.82) | +28.03 (+27.25, +28.81) | +35.26 (+34.66, +35.90) | +107.92 (+106.54, +109.33) | +83.25 (+82.57, +83.91) | no (inflation) |
| h100 | Pareto point | Stress | +0.43 (+0.09, +0.78) | +7.91 (+7.44, +8.40) | +48.16 (+47.27, +49.10) | +0.90 (+0.84, +0.97) | +25.02 (+24.55, +25.53) | +42.08 (+41.44, +42.73) | +37.00 (+36.08, +37.91) | +43.00 (+42.13, +43.90) | no (inflation) |
| h50 | Pareto point | Reference | -2.65 (-3.02, -2.32) | +10.17 (+9.32, +11.03) | +61.26 (+59.90, +62.68) | +0.51 (+0.44, +0.58) | +32.72 (+31.93, +33.49) | +55.66 (+54.97, +56.37) | +41.88 (+41.42, +42.33) | +83.35 (+82.67, +84.01) | no (inflation) |
| h50 | Pareto point | Adverse | -3.78 (-4.13, -3.43) | +7.20 (+6.63, +7.79) | +56.12 (+54.92, +57.28) | +0.58 (+0.47, +0.69) | +33.53 (+32.91, +34.14) | +54.54 (+53.97, +55.14) | +54.62 (+53.93, +55.30) | +83.35 (+82.67, +84.01) | no (inflation) |
| h50 | Pareto point | Stress | -0.16 (-0.42, +0.10) | +5.10 (+4.77, +5.44) | +39.67 (+38.58, +40.86) | +0.62 (+0.56, +0.68) | +18.82 (+18.32, +19.36) | +35.87 (+34.91, +36.88) | +17.98 (+17.50, +18.44) | +42.99 (+42.11, +43.88) | no (inflation) |
| h192 | Pareto point | Reference | -1.82 (-2.17, -1.49) | +13.65 (+12.77, +14.59) | +51.52 (+50.31, +52.77) | +0.58 (+0.50, +0.66) | +29.98 (+29.11, +30.82) | +36.77 (+36.15, +37.40) | +74.26 (+73.43, +75.09) | +83.34 (+82.66, +84.00) | no (inflation) |
| h192 | Pareto point | Adverse | -4.22 (-4.58, -3.84) | +8.32 (+7.67, +8.99) | +46.24 (+44.97, +47.47) | +0.66 (+0.53, +0.79) | +28.41 (+27.64, +29.17) | +34.81 (+34.22, +35.43) | +99.04 (+97.81, +100.29) | +83.36 (+82.68, +84.02) | no (inflation) |
| h192 | Pareto point | Stress | +0.22 (-0.11, +0.57) | +7.46 (+7.02, +7.92) | +47.34 (+46.44, +48.31) | +0.84 (+0.78, +0.91) | +23.91 (+23.44, +24.41) | +40.94 (+40.30, +41.58) | +35.00 (+34.13, +35.85) | +43.01 (+42.13, +43.90) | no (inflation) |
| h89 | Pareto point | Reference | -2.12 (-2.46, -1.81) | +10.09 (+9.29, +10.93) | +60.10 (+58.70, +61.52) | +0.50 (+0.43, +0.58) | +32.61 (+31.80, +33.37) | +54.64 (+53.96, +55.28) | +40.11 (+39.69, +40.53) | +83.32 (+82.65, +83.98) | no (inflation) |
| h89 | Pareto point | Adverse | -3.24 (-3.57, -2.90) | +7.26 (+6.69, +7.87) | +55.99 (+54.77, +57.17) | +0.56 (+0.44, +0.67) | +33.42 (+32.81, +34.05) | +54.33 (+53.75, +54.92) | +51.99 (+51.37, +52.60) | +83.33 (+82.65, +83.98) | no (inflation) |
| h89 | Pareto point | Stress | -0.44 (-0.73, -0.14) | +4.96 (+4.60, +5.33) | +40.13 (+39.03, +41.31) | +0.57 (+0.51, +0.63) | +19.30 (+18.79, +19.82) | +36.27 (+35.26, +37.33) | +18.29 (+17.83, +18.75) | +42.97 (+42.10, +43.87) | no (inflation) |
| h61 | Pareto point | Reference | -1.98 (-2.32, -1.67) | +8.79 (+8.04, +9.56) | +55.39 (+53.80, +56.93) | +0.46 (+0.40, +0.53) | +29.29 (+28.47, +30.07) | +48.93 (+48.10, +49.75) | +33.93 (+33.56, +34.28) | +83.26 (+82.57, +83.91) | no (inflation) |
| h61 | Pareto point | Adverse | -2.52 (-2.85, -2.19) | +6.89 (+6.38, +7.44) | +55.71 (+54.53, +56.86) | +0.57 (+0.46, +0.67) | +31.25 (+30.66, +31.83) | +53.90 (+53.37, +54.45) | +44.10 (+43.57, +44.64) | +83.26 (+82.58, +83.92) | no (inflation) |
| h61 | Pareto point | Stress | -0.19 (-0.44, +0.06) | +4.31 (+4.00, +4.62) | +34.80 (+33.76, +35.88) | +0.49 (+0.44, +0.55) | +16.08 (+15.64, +16.56) | +30.94 (+30.07, +31.84) | +15.08 (+14.69, +15.46) | +42.92 (+42.04, +43.82) | no (inflation) |
| h154 | Pareto point | Reference | -1.42 (-1.75, -1.13) | +9.38 (+8.58, +10.20) | +57.38 (+55.91, +58.90) | +0.69 (+0.61, +0.76) | +31.02 (+30.20, +31.82) | +51.87 (+51.13, +52.60) | +36.12 (+35.75, +36.49) | +83.68 (+83.03, +84.33) | no (inflation) |
| h154 | Pareto point | Adverse | -2.08 (-2.37, -1.78) | +7.27 (+6.74, +7.80) | +55.93 (+54.72, +57.11) | +0.76 (+0.64, +0.87) | +32.50 (+31.89, +33.10) | +54.21 (+53.63, +54.80) | +47.29 (+46.73, +47.85) | +83.86 (+83.20, +84.51) | no (inflation) |
| h154 | Pareto point | Stress | +0.34 (+0.10, +0.58) | +4.97 (+4.66, +5.28) | +36.53 (+35.47, +37.61) | +0.60 (+0.55, +0.66) | +17.44 (+16.95, +17.94) | +32.97 (+32.06, +33.92) | +15.79 (+15.38, +16.18) | +42.99 (+42.11, +43.89) | no (inflation) |
| h23 | Pareto point | Reference | -0.49 (-0.84, -0.17) | +15.02 (+14.14, +15.97) | +54.53 (+53.27, +55.84) | +0.61 (+0.52, +0.69) | +31.76 (+30.90, +32.61) | +41.29 (+40.66, +41.93) | +75.90 (+75.06, +76.74) | +83.39 (+82.71, +84.05) | no (inflation) |
| h23 | Pareto point | Adverse | -3.44 (-3.79, -3.06) | +9.00 (+8.34, +9.66) | +48.22 (+47.04, +49.35) | +0.70 (+0.58, +0.83) | +29.93 (+29.17, +30.67) | +38.51 (+37.91, +39.15) | +101.58 (+100.30, +102.88) | +83.39 (+82.71, +84.05) | no (inflation) |
| h23 | Pareto point | Stress | +1.18 (+0.83, +1.54) | +8.39 (+7.90, +8.89) | +48.00 (+47.15, +48.95) | +0.90 (+0.83, +0.96) | +25.92 (+25.43, +26.44) | +42.19 (+41.57, +42.84) | +35.44 (+34.57, +36.29) | +43.03 (+42.15, +43.92) | no (inflation) |
| h126 | Pareto point | Reference | -0.56 (-0.90, -0.23) | +12.70 (+11.84, +13.61) | +53.00 (+51.57, +54.46) | +0.53 (+0.46, +0.61) | +29.86 (+29.07, +30.64) | +41.15 (+40.48, +41.82) | +56.67 (+56.07, +57.27) | +83.41 (+82.72, +84.06) | no (inflation) |
| h126 | Pareto point | Adverse | -2.52 (-2.85, -2.15) | +8.40 (+7.81, +9.01) | +49.93 (+48.74, +51.05) | +0.61 (+0.50, +0.72) | +29.69 (+29.09, +30.33) | +41.88 (+41.27, +42.51) | +75.00 (+74.11, +75.90) | +83.41 (+82.72, +84.06) | no (inflation) |
| h126 | Pareto point | Stress | +0.67 (+0.37, +0.99) | +6.77 (+6.37, +7.19) | +43.76 (+42.82, +44.72) | +0.73 (+0.67, +0.80) | +21.55 (+21.08, +22.04) | +37.60 (+36.89, +38.36) | +27.48 (+26.82, +28.14) | +43.04 (+42.17, +43.94) | no (inflation) |
| h32 | Pareto point | Reference | -1.07 (-1.39, -0.77) | +9.95 (+9.18, +10.74) | +57.30 (+55.81, +58.79) | +0.50 (+0.43, +0.56) | +31.07 (+30.23, +31.85) | +51.90 (+51.11, +52.66) | +35.20 (+34.81, +35.58) | +83.43 (+82.74, +84.08) | no (inflation) |
| h32 | Pareto point | Adverse | -0.94 (-1.23, -0.65) | +8.34 (+7.81, +8.88) | +56.00 (+54.80, +57.17) | +0.77 (+0.63, +0.91) | +32.81 (+32.21, +33.42) | +54.44 (+53.88, +55.02) | +47.00 (+46.36, +47.66) | +83.43 (+82.74, +84.08) | no (inflation) |
| h32 | Pareto point | Stress | +0.72 (+0.49, +0.95) | +5.02 (+4.71, +5.33) | +34.89 (+33.84, +35.98) | +0.66 (+0.59, +0.74) | +16.75 (+16.26, +17.25) | +31.58 (+30.68, +32.53) | +14.78 (+14.38, +15.16) | +43.06 (+42.18, +43.96) | no (inflation) |
| h174 | Pareto point | Reference | -0.72 (-1.02, -0.44) | +9.37 (+8.64, +10.11) | +54.21 (+52.52, +55.88) | +0.47 (+0.41, +0.53) | +29.46 (+28.63, +30.24) | +48.34 (+47.54, +49.18) | +32.18 (+31.82, +32.52) | +83.32 (+82.64, +83.97) | no (inflation) |
| h174 | Pareto point | Adverse | -0.64 (-0.92, -0.38) | +7.97 (+7.47, +8.46) | +55.68 (+54.48, +56.81) | +0.65 (+0.54, +0.76) | +31.77 (+31.17, +32.37) | +54.04 (+53.48, +54.62) | +42.69 (+42.12, +43.25) | +83.32 (+82.65, +83.98) | no (inflation) |
| h174 | Pareto point | Stress | +0.81 (+0.59, +1.03) | +4.76 (+4.46, +5.05) | +33.09 (+32.05, +34.15) | +0.58 (+0.51, +0.65) | +15.74 (+15.28, +16.22) | +30.09 (+29.19, +31.01) | +13.77 (+13.40, +14.11) | +42.96 (+42.09, +43.86) | no (inflation) |
| h86 | Pareto point | Reference | -0.14 (-0.43, +0.13) | +9.81 (+9.05, +10.59) | +53.65 (+52.02, +55.28) | +1.60 (+1.45, +1.75) | +29.96 (+29.12, +30.74) | +47.83 (+46.98, +48.68) | +31.45 (+31.09, +31.79) | +83.44 (+82.75, +84.09) | no (inflation) |
| h86 | Pareto point | Adverse | -0.31 (-0.61, +0.01) | +8.11 (+7.60, +8.64) | +55.69 (+54.50, +56.82) | +1.83 (+1.68, +1.98) | +32.11 (+31.51, +32.72) | +54.06 (+53.50, +54.62) | +41.48 (+40.94, +42.02) | +83.44 (+82.75, +84.09) | no (inflation) |
| h86 | Pareto point | Stress | +0.49 (+0.24, +0.74) | +4.39 (+4.08, +4.70) | +31.48 (+30.43, +32.55) | +0.63 (+0.57, +0.69) | +15.50 (+15.03, +15.98) | +28.56 (+27.68, +29.46) | +13.21 (+12.86, +13.57) | +43.07 (+42.19, +43.96) | no (inflation) |
| h141 | Pareto point | Reference | +0.50 (+0.15, +0.81) | +14.12 (+13.27, +15.01) | +55.13 (+53.83, +56.47) | +0.55 (+0.47, +0.63) | +31.02 (+30.20, +31.84) | +44.56 (+43.93, +45.20) | +62.01 (+61.30, +62.73) | +83.41 (+82.73, +84.07) | no (inflation) |
| h141 | Pareto point | Adverse | -1.42 (-1.74, -1.08) | +9.46 (+8.86, +10.06) | +50.55 (+49.39, +51.66) | +0.62 (+0.50, +0.74) | +30.30 (+29.65, +30.98) | +42.96 (+42.28, +43.62) | +83.68 (+82.60, +84.78) | +83.41 (+82.73, +84.07) | no (inflation) |
| h141 | Pareto point | Stress | +1.15 (+0.84, +1.46) | +7.25 (+6.83, +7.69) | +45.44 (+44.48, +46.44) | +0.76 (+0.68, +0.82) | +22.49 (+22.00, +23.02) | +40.49 (+39.73, +41.30) | +28.50 (+27.78, +29.22) | +43.04 (+42.17, +43.94) | no (inflation) |
| h132 | Pareto point | Reference | +0.54 (+0.23, +0.83) | +11.62 (+10.76, +12.49) | +61.07 (+59.78, +62.36) | +1.77 (+1.63, +1.90) | +34.30 (+33.49, +35.09) | +57.22 (+56.58, +57.86) | +39.88 (+39.43, +40.33) | +83.77 (+83.11, +84.42) | no (inflation) |
| h132 | Pareto point | Adverse | -0.47 (-0.78, -0.14) | +8.59 (+8.02, +9.16) | +56.18 (+54.97, +57.33) | +1.81 (+1.66, +1.97) | +34.71 (+34.07, +35.33) | +54.67 (+54.09, +55.26) | +54.11 (+53.39, +54.84) | +84.03 (+83.36, +84.67) | no (inflation) |
| h132 | Pareto point | Stress | +0.38 (+0.10, +0.66) | +5.14 (+4.80, +5.51) | +37.91 (+36.76, +39.13) | +1.00 (+0.92, +1.08) | +18.73 (+18.21, +19.29) | +34.67 (+33.67, +35.70) | +16.66 (+16.21, +17.10) | +43.11 (+42.24, +44.01) | no (inflation) |
| h138 | Pareto point | Reference | +0.26 (-0.08, +0.57) | +11.25 (+10.44, +12.08) | +49.17 (+47.63, +50.74) | +0.51 (+0.45, +0.58) | +28.08 (+27.31, +28.82) | +38.00 (+37.21, +38.79) | +42.80 (+42.35, +43.24) | +83.36 (+82.68, +84.01) | no (inflation) |
| h138 | Pareto point | Adverse | -0.81 (-1.14, -0.47) | +8.44 (+7.88, +9.01) | +52.03 (+50.86, +53.23) | +0.58 (+0.47, +0.69) | +29.71 (+29.13, +30.31) | +46.13 (+45.50, +46.77) | +56.59 (+55.93, +57.25) | +83.36 (+82.68, +84.01) | no (inflation) |
| h138 | Pareto point | Stress | +1.18 (+0.90, +1.47) | +6.08 (+5.72, +6.47) | +38.80 (+37.82, +39.90) | +0.62 (+0.55, +0.68) | +18.69 (+18.23, +19.17) | +33.66 (+32.81, +34.53) | +21.39 (+20.87, +21.90) | +43.00 (+42.12, +43.89) | no (inflation) |
| h182 | Pareto point | Reference | -0.01 (-0.29, +0.25) | +8.77 (+8.09, +9.47) | +47.87 (+46.13, +49.54) | +0.48 (+0.41, +0.55) | +26.97 (+26.16, +27.76) | +41.95 (+41.04, +42.86) | +26.61 (+26.32, +26.89) | +83.42 (+82.74, +84.08) | no (inflation) |
| h182 | Pareto point | Adverse | +0.10 (-0.21, +0.41) | +7.64 (+7.14, +8.15) | +54.63 (+53.45, +55.77) | +0.54 (+0.44, +0.64) | +30.11 (+29.52, +30.71) | +52.69 (+52.10, +53.29) | +34.70 (+34.27, +35.14) | +83.42 (+82.74, +84.08) | no (inflation) |
| h182 | Pareto point | Stress | +0.45 (+0.23, +0.67) | +3.88 (+3.59, +4.16) | +27.54 (+26.57, +28.54) | +0.40 (+0.34, +0.46) | +13.55 (+13.14, +13.98) | +24.81 (+24.03, +25.59) | +11.45 (+11.15, +11.75) | +43.06 (+42.19, +43.96) | no (inflation) |
| h53 | Pareto point | Reference | +0.42 (+0.16, +0.67) | +8.68 (+8.00, +9.37) | +46.61 (+44.94, +48.23) | +0.85 (+0.76, +0.94) | +26.22 (+25.42, +26.99) | +40.68 (+39.84, +41.49) | +25.47 (+25.19, +25.75) | +83.37 (+82.69, +84.02) | no (inflation) |
| h53 | Pareto point | Adverse | +0.61 (+0.31, +0.91) | +7.68 (+7.20, +8.15) | +54.39 (+53.27, +55.48) | +0.91 (+0.79, +1.03) | +29.67 (+29.09, +30.26) | +52.36 (+51.79, +52.90) | +33.53 (+33.10, +33.96) | +83.37 (+82.69, +84.02) | no (inflation) |
| h53 | Pareto point | Stress | +0.42 (+0.20, +0.65) | +3.69 (+3.40, +3.99) | +26.48 (+25.57, +27.38) | +0.43 (+0.37, +0.50) | +13.09 (+12.68, +13.50) | +24.02 (+23.26, +24.81) | +11.05 (+10.76, +11.34) | +43.01 (+42.14, +43.91) | no (inflation) |
| h74 | Pareto point | Reference | +0.23 (-0.03, +0.48) | +8.50 (+7.82, +9.20) | +45.96 (+44.28, +47.62) | +1.21 (+1.09, +1.33) | +25.96 (+25.17, +26.73) | +40.00 (+39.13, +40.81) | +25.21 (+24.94, +25.47) | +83.43 (+82.74, +84.09) | no (inflation) |
| h74 | Pareto point | Adverse | +0.71 (+0.43, +0.99) | +7.79 (+7.33, +8.26) | +54.34 (+53.18, +55.45) | +1.50 (+1.36, +1.64) | +29.56 (+28.97, +30.14) | +52.29 (+51.74, +52.82) | +33.14 (+32.71, +33.57) | +83.43 (+82.74, +84.09) | no (inflation) |
| h74 | Pareto point | Stress | +0.55 (+0.35, +0.77) | +3.90 (+3.62, +4.18) | +26.76 (+25.89, +27.64) | +0.65 (+0.58, +0.72) | +13.19 (+12.79, +13.61) | +24.13 (+23.42, +24.85) | +11.11 (+10.81, +11.40) | +43.06 (+42.19, +43.96) | no (inflation) |
| h28 | Pareto point | Reference | -0.04 (-0.30, +0.21) | +7.20 (+6.57, +7.81) | +39.52 (+37.98, +41.00) | +0.42 (+0.36, +0.49) | +22.57 (+21.80, +23.36) | +33.67 (+32.90, +34.43) | +21.81 (+21.57, +22.04) | +83.34 (+82.65, +83.99) | no (inflation) |
| h28 | Pareto point | Adverse | +0.64 (+0.39, +0.89) | +7.14 (+6.64, +7.60) | +52.43 (+51.24, +53.57) | +0.61 (+0.51, +0.72) | +27.19 (+26.62, +27.75) | +49.95 (+49.34, +50.52) | +28.81 (+28.43, +29.19) | +83.34 (+82.66, +83.99) | no (inflation) |
| h28 | Pareto point | Stress | +0.80 (+0.62, +0.98) | +3.60 (+3.37, +3.85) | +23.20 (+22.38, +24.03) | +0.42 (+0.36, +0.48) | +11.47 (+11.11, +11.83) | +21.12 (+20.42, +21.83) | +9.58 (+9.33, +9.82) | +43.00 (+42.12, +43.89) | no (inflation) |
| h101 | Pareto point | Reference | +0.25 (-0.01, +0.49) | +7.75 (+7.12, +8.40) | +41.80 (+40.23, +43.42) | +0.83 (+0.74, +0.92) | +23.99 (+23.19, +24.77) | +36.14 (+35.24, +37.02) | +22.87 (+22.63, +23.10) | +83.50 (+82.83, +84.14) | no (inflation) |
| h101 | Pareto point | Adverse | +0.75 (+0.48, +1.03) | +7.29 (+6.83, +7.75) | +53.11 (+51.96, +54.22) | +1.02 (+0.91, +1.14) | +28.18 (+27.59, +28.77) | +50.82 (+50.23, +51.40) | +30.11 (+29.73, +30.48) | +83.71 (+83.05, +84.37) | no (inflation) |
| h101 | Pareto point | Stress | +0.60 (+0.40, +0.82) | +3.53 (+3.27, +3.80) | +23.80 (+22.95, +24.66) | +0.42 (+0.37, +0.47) | +11.86 (+11.48, +12.22) | +21.65 (+20.93, +22.38) | +9.88 (+9.62, +10.13) | +43.02 (+42.14, +43.92) | no (inflation) |
| h164 | Pareto point | Reference | +1.06 (+0.76, +1.35) | +11.58 (+10.77, +12.40) | +60.01 (+58.66, +61.40) | +0.81 (+0.73, +0.89) | +33.43 (+32.61, +34.23) | +55.73 (+55.04, +56.43) | +37.84 (+37.39, +38.28) | +83.77 (+83.11, +84.41) | no (inflation) |
| h164 | Pareto point | Adverse | +0.27 (-0.04, +0.58) | +8.89 (+8.37, +9.43) | +56.16 (+54.97, +57.31) | +0.90 (+0.79, +1.01) | +34.36 (+33.73, +34.99) | +54.65 (+54.07, +55.23) | +52.00 (+51.28, +52.73) | +84.02 (+83.36, +84.67) | no (inflation) |
| h164 | Pareto point | Stress | +0.36 (+0.08, +0.64) | +5.12 (+4.77, +5.48) | +37.77 (+36.61, +39.00) | +0.95 (+0.87, +1.03) | +18.65 (+18.12, +19.20) | +34.72 (+33.70, +35.81) | +16.47 (+16.03, +16.91) | +43.14 (+42.26, +44.03) | no (inflation) |
| h102 | Pareto point | Reference | +0.88 (+0.60, +1.15) | +10.83 (+10.03, +11.63) | +56.80 (+55.31, +58.33) | +0.93 (+0.85, +1.02) | +31.91 (+31.07, +32.70) | +52.30 (+51.51, +53.08) | +34.29 (+33.90, +34.67) | +83.64 (+82.98, +84.28) | no (inflation) |
| h102 | Pareto point | Adverse | +0.33 (+0.03, +0.64) | +8.59 (+8.07, +9.12) | +56.02 (+54.80, +57.17) | +1.01 (+0.88, +1.13) | +33.42 (+32.81, +34.04) | +54.48 (+53.93, +55.05) | +46.51 (+45.88, +47.13) | +83.90 (+83.23, +84.55) | no (inflation) |
| h102 | Pareto point | Stress | +0.53 (+0.26, +0.82) | +4.70 (+4.36, +5.06) | +34.40 (+33.37, +35.51) | +0.67 (+0.61, +0.73) | +16.85 (+16.35, +17.37) | +31.58 (+30.61, +32.56) | +14.51 (+14.12, +14.88) | +43.04 (+42.17, +43.93) | no (inflation) |
| h144 | Pareto point | Reference | +0.57 (+0.35, +0.79) | +7.35 (+6.77, +7.93) | +37.96 (+36.42, +39.55) | +0.42 (+0.36, +0.49) | +22.03 (+21.26, +22.82) | +33.13 (+32.26, +33.98) | +20.83 (+20.60, +21.05) | +83.48 (+82.80, +84.14) | no (inflation) |
| h144 | Pareto point | Adverse | +1.05 (+0.77, +1.33) | +6.99 (+6.54, +7.44) | +51.81 (+50.63, +52.95) | +0.49 (+0.40, +0.59) | +26.74 (+26.16, +27.32) | +49.35 (+48.76, +49.92) | +27.51 (+27.15, +27.86) | +83.48 (+82.80, +84.14) | no (inflation) |
| h144 | Pareto point | Stress | +0.53 (+0.34, +0.74) | +3.22 (+2.97, +3.47) | +22.17 (+21.40, +22.92) | +0.32 (+0.28, +0.37) | +11.15 (+10.81, +11.48) | +20.25 (+19.61, +20.89) | +9.22 (+9.01, +9.43) | +43.12 (+42.25, +44.02) | no (inflation) |
| h26 | Pareto point | Reference | +0.99 (+0.74, +1.23) | +9.21 (+8.49, +9.95) | +48.62 (+46.90, +50.31) | +0.62 (+0.55, +0.68) | +27.32 (+26.49, +28.12) | +43.10 (+42.22, +44.00) | +26.80 (+26.50, +27.10) | +83.66 (+83.00, +84.30) | no (inflation) |
| h26 | Pareto point | Adverse | +1.00 (+0.71, +1.30) | +8.00 (+7.51, +8.49) | +55.01 (+53.82, +56.17) | +0.70 (+0.60, +0.81) | +30.58 (+29.97, +31.18) | +53.19 (+52.58, +53.80) | +36.05 (+35.58, +36.52) | +83.89 (+83.22, +84.56) | no (inflation) |
| h26 | Pareto point | Stress | +0.34 (+0.10, +0.60) | +4.02 (+3.72, +4.33) | +29.33 (+28.38, +30.32) | +0.60 (+0.54, +0.66) | +14.48 (+14.05, +14.94) | +26.42 (+25.61, +27.26) | +12.26 (+11.94, +12.59) | +43.14 (+42.26, +44.04) | no (inflation) |
| h147 | Pareto point | Reference | +0.77 (+0.56, +0.99) | +7.31 (+6.71, +7.91) | +37.24 (+35.77, +38.73) | +0.46 (+0.40, +0.52) | +21.90 (+21.14, +22.69) | +32.72 (+31.89, +33.54) | +20.50 (+20.28, +20.71) | +83.56 (+82.90, +84.21) | no (inflation) |
| h147 | Pareto point | Adverse | +1.21 (+0.93, +1.50) | +6.98 (+6.52, +7.44) | +51.58 (+50.40, +52.74) | +0.53 (+0.44, +0.63) | +26.68 (+26.10, +27.26) | +49.08 (+48.50, +49.64) | +27.20 (+26.86, +27.54) | +83.78 (+83.11, +84.43) | no (inflation) |
| h147 | Pareto point | Stress | +0.32 (+0.13, +0.54) | +3.23 (+2.97, +3.49) | +22.94 (+22.10, +23.78) | +0.46 (+0.40, +0.51) | +11.49 (+11.12, +11.84) | +20.68 (+20.00, +21.39) | +9.63 (+9.38, +9.88) | +43.12 (+42.24, +44.03) | no (inflation) |
| h81 | Pareto point | Reference | +0.64 (+0.42, +0.86) | +7.25 (+6.65, +7.85) | +37.20 (+35.69, +38.72) | +0.46 (+0.40, +0.52) | +21.87 (+21.10, +22.66) | +32.65 (+31.83, +33.47) | +20.45 (+20.23, +20.67) | +83.54 (+82.88, +84.19) | no (inflation) |
| h81 | Pareto point | Adverse | +1.22 (+0.97, +1.48) | +7.03 (+6.59, +7.45) | +51.42 (+50.28, +52.58) | +0.55 (+0.45, +0.64) | +26.73 (+26.15, +27.31) | +49.05 (+48.46, +49.62) | +27.18 (+26.83, +27.53) | +83.75 (+83.09, +84.41) | no (inflation) |
| h81 | Pareto point | Stress | +0.57 (+0.38, +0.78) | +3.17 (+2.92, +3.43) | +21.49 (+20.66, +22.28) | +0.33 (+0.28, +0.37) | +10.86 (+10.51, +11.22) | +19.66 (+18.99, +20.35) | +8.96 (+8.73, +9.18) | +43.09 (+42.21, +43.99) | no (inflation) |
| h146 | Pareto point | Reference | +1.16 (+0.87, +1.44) | +11.17 (+10.38, +11.98) | +57.85 (+56.37, +59.37) | +0.80 (+0.73, +0.88) | +32.42 (+31.59, +33.22) | +53.40 (+52.60, +54.18) | +35.33 (+34.91, +35.73) | +83.69 (+83.04, +84.33) | no (inflation) |
| h146 | Pareto point | Adverse | +0.52 (+0.22, +0.82) | +8.83 (+8.31, +9.34) | +56.07 (+54.87, +57.23) | +0.93 (+0.80, +1.05) | +33.81 (+33.19, +34.43) | +54.55 (+53.98, +55.13) | +48.31 (+47.64, +48.99) | +83.95 (+83.29, +84.60) | no (inflation) |
| h146 | Pareto point | Stress | +0.72 (+0.47, +0.99) | +5.01 (+4.69, +5.35) | +35.53 (+34.45, +36.69) | +0.82 (+0.75, +0.90) | +17.33 (+16.83, +17.85) | +32.48 (+31.50, +33.48) | +15.08 (+14.66, +15.48) | +43.08 (+42.20, +43.97) | no (inflation) |
| h162 | Pareto point | Reference | +1.23 (+0.96, +1.49) | +10.43 (+9.67, +11.19) | +54.32 (+52.69, +55.95) | +0.66 (+0.59, +0.73) | +30.46 (+29.61, +31.24) | +49.22 (+48.35, +50.08) | +31.44 (+31.08, +31.80) | +83.67 (+83.01, +84.32) | no (inflation) |
| h162 | Pareto point | Adverse | +0.89 (+0.60, +1.18) | +8.58 (+8.06, +9.09) | +55.74 (+54.52, +56.88) | +0.75 (+0.64, +0.86) | +32.61 (+32.01, +33.23) | +54.17 (+53.61, +54.75) | +42.68 (+42.11, +43.25) | +83.93 (+83.26, +84.58) | no (inflation) |
| h162 | Pareto point | Stress | +0.80 (+0.55, +1.07) | +4.44 (+4.12, +4.76) | +31.29 (+30.29, +32.33) | +0.44 (+0.39, +0.50) | +15.53 (+15.07, +16.00) | +28.79 (+27.90, +29.70) | +13.05 (+12.70, +13.39) | +43.12 (+42.25, +44.01) | no (inflation) |
| h153 | Pareto point | Reference | +1.42 (+1.13, +1.70) | +11.49 (+10.69, +12.30) | +58.62 (+57.21, +60.05) | +0.71 (+0.64, +0.79) | +33.09 (+32.26, +33.90) | +54.24 (+53.52, +54.96) | +36.12 (+35.69, +36.54) | +83.73 (+83.07, +84.38) | no (inflation) |
| h153 | Pareto point | Adverse | +0.71 (+0.41, +1.02) | +9.01 (+8.48, +9.55) | +56.11 (+54.91, +57.26) | +0.83 (+0.71, +0.94) | +34.24 (+33.61, +34.88) | +54.59 (+54.02, +55.17) | +49.40 (+48.72, +50.09) | +84.00 (+83.34, +84.65) | no (inflation) |
| h153 | Pareto point | Stress | +0.95 (+0.68, +1.24) | +4.99 (+4.64, +5.35) | +34.98 (+33.97, +36.06) | +0.52 (+0.46, +0.59) | +17.40 (+16.90, +17.92) | +32.40 (+31.48, +33.35) | +14.74 (+14.35, +15.14) | +43.13 (+42.26, +44.02) | no (inflation) |
| h108 | Pareto point | Reference | +1.69 (+1.39, +1.97) | +11.23 (+10.48, +12.00) | +48.93 (+47.32, +50.53) | +0.62 (+0.56, +0.69) | +27.10 (+26.30, +27.86) | +40.20 (+39.41, +41.01) | +38.38 (+37.96, +38.80) | +83.63 (+82.97, +84.29) | no (inflation) |
| h108 | Pareto point | Adverse | +1.04 (+0.75, +1.35) | +8.92 (+8.39, +9.44) | +53.77 (+52.64, +54.91) | +0.70 (+0.59, +0.81) | +29.65 (+29.07, +30.23) | +49.66 (+49.10, +50.21) | +51.97 (+51.35, +52.59) | +83.85 (+83.18, +84.51) | no (inflation) |
| h108 | Pareto point | Stress | +1.54 (+1.28, +1.80) | +5.65 (+5.33, +5.97) | +35.10 (+33.99, +36.20) | +0.54 (+0.48, +0.60) | +16.53 (+16.09, +17.00) | +30.82 (+29.90, +31.76) | +18.13 (+17.67, +18.57) | +43.11 (+42.23, +44.00) | no (inflation) |
| h21 | Pareto point | Reference | +4.85 (+4.53, +5.15) | +14.95 (+14.09, +15.80) | +56.14 (+54.74, +57.66) | +1.05 (+0.96, +1.14) | +32.15 (+31.37, +32.92) | +50.16 (+49.44, +50.92) | +47.39 (+46.79, +48.00) | +83.66 (+83.00, +84.31) | no (inflation) |
| h21 | Pareto point | Adverse | +3.36 (+3.02, +3.70) | +11.19 (+10.63, +11.77) | +55.08 (+53.92, +56.20) | +1.15 (+1.02, +1.27) | +32.87 (+32.24, +33.49) | +53.01 (+52.44, +53.59) | +67.28 (+66.30, +68.27) | +83.99 (+83.32, +84.64) | no (inflation) |
| h21 | Pareto point | Stress | +2.97 (+2.69, +3.26) | +6.93 (+6.57, +7.31) | +38.40 (+37.18, +39.68) | +0.70 (+0.63, +0.77) | +19.20 (+18.68, +19.77) | +35.74 (+34.67, +36.85) | +19.60 (+19.05, +20.12) | +43.11 (+42.23, +44.01) | no (inflation) |
| h105 | Pareto point | Reference | +5.33 (+5.01, +5.64) | +15.49 (+14.66, +16.34) | +57.03 (+55.67, +58.48) | +0.87 (+0.79, +0.96) | +32.84 (+32.05, +33.62) | +51.08 (+50.40, +51.78) | +48.95 (+48.32, +49.59) | +83.70 (+83.04, +84.34) | no (inflation) |
| h105 | Pareto point | Adverse | +3.66 (+3.33, +4.01) | +11.48 (+10.92, +12.07) | +55.12 (+53.94, +56.26) | +1.00 (+0.88, +1.13) | +33.45 (+32.81, +34.08) | +53.00 (+52.44, +53.58) | +69.52 (+68.50, +70.54) | +84.03 (+83.37, +84.67) | no (inflation) |
| h105 | Pareto point | Stress | +3.11 (+2.80, +3.42) | +7.13 (+6.74, +7.53) | +39.04 (+37.87, +40.30) | +0.66 (+0.60, +0.73) | +19.75 (+19.24, +20.32) | +36.33 (+35.28, +37.42) | +19.99 (+19.44, +20.53) | +43.15 (+42.27, +44.05) | no (inflation) |
| fflat | Pareto point | Reference | +19.42 (+18.78, +20.05) | +35.51 (+34.27, +36.78) | +32.24 (+30.87, +33.67) | +3.91 (+3.66, +4.16) | +16.66 (+15.72, +17.63) | +14.79 (+14.14, +15.46) | -0.03 (-0.04, -0.03) | +83.11 (+82.47, +83.76) | no |
| fflat | Pareto point | Adverse | +13.15 (+12.49, +13.83) | +25.45 (+24.49, +26.43) | +32.29 (+31.14, +33.43) | +3.52 (+3.34, +3.69) | +17.04 (+16.32, +17.76) | +18.48 (+17.82, +19.16) | +0.00 (+0.00, +0.00) | +70.63 (+69.88, +71.36) | no |
| fflat | Pareto point | Stress | +5.77 (+5.32, +6.23) | +13.74 (+13.11, +14.36) | +14.86 (+14.24, +15.53) | +0.81 (+0.74, +0.89) | +8.33 (+7.90, +8.75) | +8.42 (+7.88, +8.97) | +0.00 (+0.00, +0.00) | +35.60 (+34.84, +36.40) | no |
| sva | Pareto point | Reference | +27.86 (+27.49, +28.23) | +35.30 (+34.44, +36.20) | +12.95 (+11.80, +14.09) | +0.01 (-0.05, +0.06) | +1.45 (+0.83, +2.06) | +6.25 (+5.80, +6.67) | +2757.09 (+2688.73, +2829.87) | +83.41 (+82.73, +84.07) | no (inflation) |
| sva | Pareto point | Adverse | +14.67 (+14.21, +15.15) | +21.02 (+20.29, +21.75) | +2.22 (+1.13, +3.30) | -0.47 (-0.59, -0.35) | -3.33 (-3.87, -2.81) | -4.86 (-5.39, -4.34) | +3657.55 (+3556.60, +3764.01) | +83.42 (+82.73, +84.07) | no (inflation) |
| sva | Pareto point | Stress | +20.53 (+20.03, +21.03) | +22.75 (+22.13, +23.40) | +6.15 (+5.43, +6.83) | -0.33 (-0.40, -0.25) | +0.77 (+0.40, +1.12) | +3.16 (+2.62, +3.67) | +2910.56 (+2830.90, +2995.28) | +43.04 (+42.16, +43.94) | no (inflation) |
| h170 | Pareto point | Reference | +29.81 (+29.46, +30.18) | +35.92 (+35.08, +36.77) | +13.93 (+12.74, +15.13) | -0.01 (-0.08, +0.05) | +2.16 (+1.56, +2.73) | +8.22 (+7.77, +8.65) | +2745.12 (+2676.45, +2818.67) | +83.27 (+82.61, +83.93) | no (inflation) |
| h170 | Pareto point | Adverse | +16.23 (+15.75, +16.70) | +21.38 (+20.64, +22.11) | +2.87 (+1.77, +3.97) | -0.57 (-0.69, -0.44) | -2.68 (-3.19, -2.19) | -3.20 (-3.77, -2.64) | +3652.72 (+3551.42, +3759.56) | +83.83 (+83.15, +84.48) | no (inflation) |
| h170 | Pareto point | Stress | +21.07 (+20.58, +21.58) | +22.91 (+22.29, +23.56) | +6.43 (+5.71, +7.14) | -0.35 (-0.43, -0.28) | +1.05 (+0.69, +1.40) | +3.88 (+3.36, +4.37) | +2884.81 (+2805.56, +2968.66) | +43.12 (+42.25, +44.02) | no (inflation) |
| h197 | Pareto point | Reference | +31.46 (+31.12, +31.82) | +36.78 (+35.93, +37.64) | +14.64 (+13.42, +15.85) | -0.03 (-0.10, +0.04) | +3.06 (+2.49, +3.60) | +9.77 (+9.34, +10.20) | +2703.69 (+2635.07, +2777.13) | +83.18 (+82.52, +83.85) | no (inflation) |
| h197 | Pareto point | Adverse | +17.69 (+17.21, +18.17) | +22.18 (+21.44, +22.93) | +3.58 (+2.52, +4.60) | -0.62 (-0.74, -0.50) | -1.82 (-2.27, -1.37) | -1.82 (-2.36, -1.31) | +3594.04 (+3493.19, +3700.36) | +83.75 (+83.07, +84.40) | no (inflation) |
| h197 | Pareto point | Stress | +21.61 (+21.10, +22.11) | +23.11 (+22.48, +23.74) | +6.66 (+5.95, +7.35) | -0.36 (-0.43, -0.28) | +1.30 (+0.96, +1.63) | +4.51 (+3.99, +5.00) | +2858.60 (+2779.16, +2942.81) | +43.11 (+42.23, +44.01) | no (inflation) |
| h189 | Pareto point | Reference | +31.68 (+31.33, +32.04) | +37.00 (+36.17, +37.87) | +14.85 (+13.64, +16.10) | -0.14 (-0.20, -0.09) | +3.47 (+2.91, +4.02) | +10.18 (+9.72, +10.64) | +2596.77 (+2531.06, +2667.58) | +83.28 (+82.60, +83.94) | no (inflation) |
| h189 | Pareto point | Adverse | +18.04 (+17.56, +18.52) | +22.47 (+21.74, +23.21) | +3.99 (+2.94, +5.00) | -0.70 (-0.81, -0.59) | -1.29 (-1.72, -0.87) | -1.03 (-1.56, -0.51) | +3416.80 (+3321.02, +3517.85) | +83.28 (+82.61, +83.94) | no (inflation) |
| h189 | Pareto point | Stress | +21.68 (+21.20, +22.17) | +23.14 (+22.52, +23.76) | +6.74 (+6.03, +7.42) | -0.36 (-0.44, -0.29) | +1.41 (+1.07, +1.72) | +4.74 (+4.23, +5.20) | +2800.64 (+2722.20, +2883.70) | +42.94 (+42.06, +43.83) | no (inflation) |
| h118 | Pareto point | Reference | +32.55 (+32.20, +32.92) | +37.42 (+36.58, +38.29) | +15.09 (+13.85, +16.32) | -0.14 (-0.20, -0.08) | +3.67 (+3.11, +4.23) | +10.64 (+10.18, +11.09) | +2713.00 (+2643.66, +2787.16) | +83.44 (+82.76, +84.10) | no (inflation) |
| h118 | Pareto point | Adverse | +18.68 (+18.18, +19.17) | +22.79 (+22.05, +23.55) | +4.04 (+3.05, +5.04) | -0.67 (-0.79, -0.56) | -1.12 (-1.55, -0.70) | -0.84 (-1.34, -0.34) | +3613.48 (+3511.23, +3722.18) | +83.44 (+82.76, +84.10) | no (inflation) |
| h118 | Pareto point | Stress | +21.99 (+21.49, +22.49) | +23.25 (+22.62, +23.89) | +6.85 (+6.14, +7.53) | -0.36 (-0.44, -0.29) | +1.48 (+1.15, +1.79) | +4.97 (+4.44, +5.45) | +2854.73 (+2774.77, +2939.46) | +43.07 (+42.19, +43.97) | no (inflation) |
| h62 | Pareto point | Reference | +32.56 (+32.20, +32.95) | +37.28 (+36.44, +38.16) | +15.14 (+13.93, +16.37) | -0.04 (-0.11, +0.03) | +3.75 (+3.19, +4.27) | +10.98 (+10.51, +11.42) | +2602.35 (+2536.03, +2673.45) | +83.12 (+82.45, +83.78) | no (inflation) |
| h62 | Pareto point | Adverse | +18.75 (+18.26, +19.24) | +22.71 (+21.96, +23.46) | +4.36 (+3.40, +5.32) | -0.65 (-0.77, -0.52) | -1.09 (-1.50, -0.67) | -0.32 (-0.84, +0.16) | +3435.21 (+3337.93, +3537.78) | +83.69 (+83.00, +84.34) | no (inflation) |
| h62 | Pareto point | Stress | +22.05 (+21.56, +22.54) | +23.28 (+22.66, +23.91) | +6.91 (+6.21, +7.57) | -0.35 (-0.43, -0.27) | +1.54 (+1.21, +1.85) | +5.13 (+4.63, +5.60) | +2800.90 (+2721.72, +2884.81) | +43.09 (+42.22, +43.99) | no (inflation) |
| h190 | Pareto point | Reference | +32.66 (+32.30, +33.03) | +37.45 (+36.60, +38.33) | +15.07 (+13.84, +16.30) | -0.13 (-0.19, -0.08) | +3.69 (+3.13, +4.25) | +10.69 (+10.23, +11.13) | +2724.52 (+2654.82, +2799.12) | +83.46 (+82.77, +84.12) | no (inflation) |
| h190 | Pareto point | Adverse | +18.81 (+18.31, +19.30) | +22.83 (+22.08, +23.59) | +4.03 (+3.02, +5.08) | -0.66 (-0.78, -0.55) | -1.11 (-1.53, -0.69) | -0.79 (-1.30, -0.32) | +3630.90 (+3528.26, +3740.15) | +83.46 (+82.77, +84.12) | no (inflation) |
| h190 | Pareto point | Stress | +22.03 (+21.53, +22.54) | +23.28 (+22.65, +23.91) | +6.86 (+6.15, +7.54) | -0.36 (-0.44, -0.28) | +1.49 (+1.15, +1.80) | +5.00 (+4.48, +5.49) | +2860.96 (+2780.85, +2946.01) | +43.07 (+42.20, +43.97) | no (inflation) |
| h42 | Pareto point | Reference | +32.94 (+32.58, +33.32) | +37.59 (+36.74, +38.47) | +15.33 (+14.09, +16.53) | -0.15 (-0.20, -0.09) | +3.89 (+3.33, +4.43) | +11.09 (+10.63, +11.56) | +2699.04 (+2629.88, +2773.02) | +83.44 (+82.75, +84.09) | no (inflation) |
| h42 | Pareto point | Adverse | +19.05 (+18.56, +19.55) | +22.98 (+22.24, +23.74) | +4.46 (+3.46, +5.45) | -0.69 (-0.81, -0.57) | -0.93 (-1.34, -0.52) | -0.31 (-0.86, +0.21) | +3591.45 (+3489.64, +3699.76) | +83.44 (+82.75, +84.09) | no (inflation) |
| h42 | Pareto point | Stress | +22.13 (+21.63, +22.64) | +23.31 (+22.68, +23.95) | +6.92 (+6.20, +7.58) | -0.36 (-0.43, -0.28) | +1.55 (+1.21, +1.86) | +5.16 (+4.64, +5.65) | +2847.62 (+2767.48, +2932.40) | +43.06 (+42.18, +43.95) | no (inflation) |
| h159 | Pareto point | Reference | +33.13 (+32.77, +33.52) | +37.65 (+36.81, +38.53) | +15.41 (+14.17, +16.61) | -0.13 (-0.18, -0.07) | +3.97 (+3.41, +4.51) | +11.28 (+10.82, +11.74) | +2673.00 (+2604.51, +2746.35) | +83.46 (+82.78, +84.12) | no (inflation) |
| h159 | Pareto point | Adverse | +19.20 (+18.71, +19.69) | +23.04 (+22.30, +23.80) | +4.61 (+3.64, +5.56) | -0.67 (-0.78, -0.55) | -0.83 (-1.24, -0.41) | -0.02 (-0.55, +0.48) | +3551.58 (+3450.96, +3658.66) | +83.46 (+82.78, +84.12) | no (inflation) |
| h159 | Pareto point | Stress | +22.17 (+21.68, +22.68) | +23.32 (+22.69, +23.95) | +6.96 (+6.26, +7.63) | -0.35 (-0.43, -0.27) | +1.57 (+1.24, +1.88) | +5.27 (+4.76, +5.75) | +2831.84 (+2752.11, +2916.50) | +43.08 (+42.20, +43.98) | no (inflation) |
| h13 | Pareto point | Reference | +33.59 (+33.22, +33.99) | +37.68 (+36.83, +38.57) | +15.88 (+14.69, +17.03) | +0.05 (-0.02, +0.12) | +4.20 (+3.66, +4.73) | +12.35 (+11.88, +12.81) | +2560.20 (+2494.93, +2630.31) | +83.02 (+82.35, +83.68) | no (inflation) |
| h13 | Pareto point | Adverse | +19.45 (+18.96, +19.97) | +23.00 (+22.26, +23.75) | +5.21 (+4.30, +6.15) | -0.51 (-0.62, -0.39) | -0.62 (-1.00, -0.23) | +0.99 (+0.48, +1.48) | +3387.47 (+3292.08, +3488.19) | +83.60 (+82.91, +84.26) | no (inflation) |
| h13 | Pareto point | Stress | +22.12 (+21.63, +22.63) | +23.24 (+22.63, +23.88) | +7.00 (+6.31, +7.68) | -0.30 (-0.38, -0.23) | +1.59 (+1.26, +1.90) | +5.48 (+4.98, +5.95) | +2774.15 (+2696.41, +2856.72) | +43.03 (+42.16, +43.93) | no (inflation) |
| h165 | Pareto point | Reference | +33.44 (+33.08, +33.83) | +37.77 (+36.93, +38.65) | +15.53 (+14.33, +16.72) | -0.14 (-0.20, -0.09) | +4.15 (+3.60, +4.69) | +11.58 (+11.11, +12.03) | +2646.60 (+2578.68, +2719.28) | +83.41 (+82.72, +84.07) | no (inflation) |
| h165 | Pareto point | Adverse | +19.51 (+19.02, +20.01) | +23.19 (+22.46, +23.93) | +4.98 (+4.05, +5.93) | -0.68 (-0.80, -0.57) | -0.61 (-1.00, -0.21) | +0.50 (-0.05, +1.02) | +3511.68 (+3412.28, +3617.55) | +83.41 (+82.72, +84.07) | no (inflation) |
| h165 | Pareto point | Stress | +22.26 (+21.77, +22.77) | +23.36 (+22.73, +23.99) | +6.98 (+6.28, +7.65) | -0.36 (-0.43, -0.28) | +1.63 (+1.30, +1.94) | +5.36 (+4.85, +5.84) | +2818.81 (+2738.98, +2903.72) | +43.04 (+42.16, +43.93) | no (inflation) |
| h171 | Pareto point | Reference | +33.46 (+33.10, +33.85) | +37.77 (+36.92, +38.66) | +15.57 (+14.37, +16.74) | -0.13 (-0.19, -0.07) | +4.18 (+3.63, +4.73) | +11.66 (+11.19, +12.11) | +2638.26 (+2570.54, +2710.76) | +83.39 (+82.71, +84.04) | no (inflation) |
| h171 | Pareto point | Adverse | +19.52 (+19.02, +20.01) | +23.19 (+22.45, +23.94) | +4.95 (+4.00, +5.88) | -0.67 (-0.79, -0.56) | -0.59 (-0.98, -0.19) | +0.53 (-0.02, +1.05) | +3498.87 (+3399.54, +3604.30) | +83.39 (+82.71, +84.05) | no (inflation) |
| h171 | Pareto point | Stress | +22.27 (+21.77, +22.77) | +23.35 (+22.73, +23.98) | +6.95 (+6.25, +7.62) | -0.36 (-0.44, -0.28) | +1.63 (+1.29, +1.93) | +5.37 (+4.87, +5.83) | +2812.46 (+2732.87, +2896.78) | +43.03 (+42.15, +43.92) | no (inflation) |
| h112 | Pareto point | Reference | +33.60 (+33.24, +33.99) | +37.74 (+36.89, +38.63) | +15.96 (+14.76, +17.16) | -0.13 (-0.18, -0.07) | +4.47 (+3.93, +5.01) | +12.56 (+12.08, +13.04) | +2441.09 (+2378.59, +2508.79) | +83.41 (+82.73, +84.07) | no (inflation) |
| h112 | Pareto point | Adverse | +19.65 (+19.16, +20.15) | +23.15 (+22.42, +23.89) | +5.49 (+4.56, +6.48) | -0.68 (-0.79, -0.57) | -0.25 (-0.62, +0.12) | +1.46 (+1.00, +1.92) | +3191.86 (+3101.41, +3287.39) | +83.41 (+82.73, +84.07) | no (inflation) |
| h112 | Pareto point | Stress | +22.18 (+21.69, +22.67) | +23.25 (+22.63, +23.87) | +7.09 (+6.38, +7.73) | -0.33 (-0.41, -0.26) | +1.66 (+1.34, +1.96) | +5.60 (+5.12, +6.07) | +2706.62 (+2629.70, +2788.06) | +43.04 (+42.17, +43.94) | no (inflation) |
| h181 | Pareto point | Reference | +33.65 (+33.29, +34.04) | +37.83 (+36.97, +38.72) | +15.80 (+14.58, +16.96) | -0.12 (-0.17, -0.06) | +4.28 (+3.74, +4.83) | +12.05 (+11.59, +12.48) | +2599.34 (+2532.76, +2670.64) | +83.38 (+82.71, +84.04) | no (inflation) |
| h181 | Pareto point | Adverse | +19.64 (+19.14, +20.14) | +23.22 (+22.49, +23.97) | +5.19 (+4.25, +6.14) | -0.66 (-0.77, -0.55) | -0.48 (-0.86, -0.08) | +0.96 (+0.42, +1.48) | +3439.44 (+3342.40, +3542.52) | +83.39 (+82.71, +84.04) | no (inflation) |
| h181 | Pareto point | Stress | +22.25 (+21.76, +22.75) | +23.32 (+22.70, +23.94) | +7.03 (+6.33, +7.70) | -0.35 (-0.43, -0.27) | +1.64 (+1.31, +1.95) | +5.49 (+4.98, +5.96) | +2791.04 (+2712.33, +2874.58) | +43.02 (+42.15, +43.92) | no (inflation) |
| h116 | Pareto point | Reference | +33.68 (+33.32, +34.07) | +37.86 (+37.02, +38.74) | +15.66 (+14.46, +16.80) | -0.13 (-0.18, -0.07) | +4.29 (+3.73, +4.83) | +11.89 (+11.44, +12.35) | +2623.69 (+2556.26, +2695.81) | +83.45 (+82.77, +84.11) | no (inflation) |
| h116 | Pareto point | Adverse | +19.70 (+19.20, +20.20) | +23.25 (+22.51, +24.00) | +5.13 (+4.16, +6.08) | -0.67 (-0.79, -0.56) | -0.48 (-0.87, -0.08) | +0.80 (+0.27, +1.32) | +3477.11 (+3378.53, +3582.03) | +83.45 (+82.76, +84.11) | no (inflation) |
| h116 | Pareto point | Stress | +22.31 (+21.82, +22.82) | +23.35 (+22.73, +23.98) | +6.99 (+6.30, +7.66) | -0.35 (-0.43, -0.27) | +1.66 (+1.33, +1.96) | +5.47 (+4.98, +5.93) | +2804.40 (+2725.06, +2888.63) | +43.07 (+42.19, +43.96) | no (inflation) |
| h48 | Pareto point | Reference | +33.77 (+33.41, +34.16) | +37.91 (+37.06, +38.79) | +15.68 (+14.51, +16.82) | -0.13 (-0.18, -0.07) | +4.31 (+3.76, +4.87) | +11.99 (+11.53, +12.43) | +2618.67 (+2551.38, +2690.71) | +83.46 (+82.77, +84.12) | no (inflation) |
| h48 | Pareto point | Adverse | +19.76 (+19.26, +20.26) | +23.27 (+22.52, +24.02) | +5.20 (+4.26, +6.13) | -0.67 (-0.79, -0.56) | -0.45 (-0.84, -0.05) | +0.87 (+0.34, +1.39) | +3469.05 (+3370.55, +3573.64) | +83.46 (+82.77, +84.11) | no (inflation) |
| h48 | Pareto point | Stress | +22.33 (+21.84, +22.83) | +23.36 (+22.74, +23.99) | +6.99 (+6.29, +7.65) | -0.35 (-0.43, -0.28) | +1.67 (+1.33, +1.97) | +5.47 (+4.98, +5.93) | +2801.74 (+2722.39, +2885.91) | +43.07 (+42.20, +43.97) | no (inflation) |
| h187 | Pareto point | Reference | +33.75 (+33.39, +34.15) | +37.91 (+37.07, +38.79) | +15.73 (+14.55, +16.88) | -0.13 (-0.18, -0.07) | +4.34 (+3.78, +4.89) | +12.01 (+11.55, +12.46) | +2616.52 (+2549.23, +2688.57) | +83.39 (+82.71, +84.05) | no (inflation) |
| h187 | Pareto point | Adverse | +19.78 (+19.28, +20.27) | +23.29 (+22.56, +24.05) | +5.20 (+4.25, +6.12) | -0.66 (-0.78, -0.55) | -0.41 (-0.80, -0.02) | +0.93 (+0.40, +1.46) | +3467.33 (+3368.07, +3572.30) | +83.39 (+82.71, +84.05) | no (inflation) |
| h187 | Pareto point | Stress | +22.38 (+21.90, +22.87) | +23.41 (+22.80, +24.03) | +7.00 (+6.31, +7.66) | -0.34 (-0.42, -0.27) | +1.70 (+1.37, +2.01) | +5.52 (+5.03, +5.98) | +2802.81 (+2722.85, +2887.41) | +43.02 (+42.15, +43.92) | no (inflation) |
| h24 | Pareto point | Reference | +34.00 (+33.64, +34.38) | +37.92 (+37.08, +38.80) | +15.86 (+14.69, +17.00) | -0.06 (-0.12, +0.00) | +4.44 (+3.91, +4.97) | +12.54 (+12.06, +13.01) | +2582.37 (+2515.69, +2653.85) | +83.02 (+82.36, +83.68) | no (inflation) |
| h24 | Pareto point | Adverse | +19.92 (+19.42, +20.41) | +23.27 (+22.53, +24.01) | +5.28 (+4.33, +6.21) | -0.65 (-0.77, -0.53) | -0.39 (-0.77, +0.00) | +1.24 (+0.72, +1.74) | +3423.37 (+3326.48, +3526.49) | +83.60 (+82.92, +84.26) | no (inflation) |
| h24 | Pareto point | Stress | +22.40 (+21.91, +22.90) | +23.38 (+22.76, +24.01) | +7.07 (+6.37, +7.72) | -0.34 (-0.42, -0.27) | +1.72 (+1.39, +2.03) | +5.65 (+5.18, +6.09) | +2783.50 (+2704.47, +2867.46) | +43.04 (+42.17, +43.94) | no (inflation) |
| h90 | Pareto point | Reference | +34.07 (+33.71, +34.46) | +37.99 (+37.14, +38.87) | +15.90 (+14.72, +17.06) | -0.11 (-0.17, -0.05) | +4.53 (+3.98, +5.07) | +12.53 (+12.04, +13.02) | +2555.96 (+2490.28, +2626.37) | +83.42 (+82.73, +84.07) | no (inflation) |
| h90 | Pareto point | Adverse | +20.01 (+19.51, +20.50) | +23.34 (+22.61, +24.10) | +5.42 (+4.48, +6.37) | -0.64 (-0.76, -0.52) | -0.24 (-0.63, +0.15) | +1.46 (+0.96, +1.95) | +3375.99 (+3280.29, +3477.34) | +83.42 (+82.73, +84.07) | no (inflation) |
| h90 | Pareto point | Stress | +22.38 (+21.90, +22.89) | +23.35 (+22.73, +23.97) | +7.07 (+6.38, +7.72) | -0.33 (-0.41, -0.26) | +1.71 (+1.38, +2.01) | +5.66 (+5.18, +6.10) | +2766.83 (+2688.21, +2850.34) | +43.06 (+42.18, +43.95) | no (inflation) |
| h143 | Pareto point | Reference | +34.14 (+33.78, +34.53) | +38.00 (+37.15, +38.89) | +16.13 (+14.94, +17.30) | -0.13 (-0.19, -0.07) | +4.68 (+4.13, +5.22) | +12.90 (+12.41, +13.37) | +2472.37 (+2408.19, +2541.00) | +83.45 (+82.76, +84.11) | no (inflation) |
| h143 | Pareto point | Adverse | +20.16 (+19.67, +20.66) | +23.40 (+22.66, +24.14) | +5.68 (+4.72, +6.63) | -0.68 (-0.80, -0.56) | -0.04 (-0.41, +0.34) | +1.84 (+1.38, +2.30) | +3240.09 (+3147.49, +3337.84) | +83.45 (+82.76, +84.11) | no (inflation) |
| h143 | Pareto point | Stress | +22.46 (+21.98, +22.96) | +23.39 (+22.78, +24.01) | +7.12 (+6.43, +7.77) | -0.32 (-0.40, -0.25) | +1.77 (+1.44, +2.07) | +5.73 (+5.24, +6.17) | +2726.08 (+2647.81, +2808.60) | +43.07 (+42.20, +43.97) | no (inflation) |
| h64 | Pareto point | Reference | +34.40 (+34.04, +34.79) | +38.12 (+37.26, +39.01) | +16.15 (+14.94, +17.31) | -0.13 (-0.18, -0.07) | +4.73 (+4.19, +5.28) | +13.03 (+12.53, +13.53) | +2540.53 (+2475.03, +2610.80) | +83.46 (+82.78, +84.12) | no (inflation) |
| h64 | Pareto point | Adverse | +20.32 (+19.82, +20.82) | +23.48 (+22.74, +24.23) | +5.62 (+4.71, +6.58) | -0.65 (-0.77, -0.53) | -0.04 (-0.42, +0.35) | +1.81 (+1.31, +2.30) | +3352.85 (+3257.25, +3454.04) | +83.46 (+82.78, +84.12) | no (inflation) |
| h64 | Pareto point | Stress | +22.53 (+22.04, +23.03) | +23.41 (+22.79, +24.03) | +7.13 (+6.44, +7.78) | -0.33 (-0.40, -0.25) | +1.78 (+1.45, +2.08) | +5.77 (+5.29, +6.20) | +2757.56 (+2678.85, +2841.31) | +43.08 (+42.21, +43.97) | no (inflation) |
| h87 | Pareto point | Reference | +34.43 (+34.07, +34.83) | +38.15 (+37.29, +39.03) | +16.13 (+14.93, +17.29) | -0.12 (-0.18, -0.07) | +4.74 (+4.19, +5.29) | +13.06 (+12.56, +13.56) | +2536.11 (+2470.70, +2606.19) | +83.46 (+82.77, +84.11) | no (inflation) |
| h87 | Pareto point | Adverse | +20.33 (+19.83, +20.83) | +23.48 (+22.75, +24.24) | +5.64 (+4.73, +6.61) | -0.65 (-0.77, -0.53) | -0.03 (-0.41, +0.35) | +1.83 (+1.34, +2.32) | +3346.10 (+3250.89, +3446.74) | +83.46 (+82.77, +84.11) | no (inflation) |
| h87 | Pareto point | Stress | +22.49 (+22.00, +22.99) | +23.38 (+22.77, +24.00) | +7.13 (+6.44, +7.78) | -0.33 (-0.41, -0.26) | +1.76 (+1.44, +2.06) | +5.74 (+5.26, +6.19) | +2754.42 (+2676.09, +2837.65) | +43.08 (+42.20, +43.97) | no (inflation) |

### C2.2 design, wages 100%

| Setting | Role | Environment | basket poverty, % of adult-years | non-participants' basket poverty, % | non-participants' wealth poverty, % | non-participants' income drops of 25%+ with no buffer, per 100 | non-participants under 3 months of basics covered, % | wealth poverty at year 20, % | programme inflation, points a year | participation, mean of years 1-19, % | Passes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| t0 | Pareto point | Reference | -25.54 (-25.95, -25.12) | -24.89 (-25.88, -23.91) | -19.97 (-20.83, -19.13) | +1.53 (+1.34, +1.71) | -21.54 (-22.21, -20.80) | -20.20 (-20.62, -19.81) | +36.35 (+36.08, +36.61) | +100.00 (+100.00, +100.00) | no (inflation) |
| t0 | Pareto point | Adverse | -36.50 (-37.16, -35.81) | -35.49 (-36.68, -34.31) | -27.22 (-28.26, -26.20) | +0.87 (+0.69, +1.06) | -25.59 (-26.40, -24.79) | -27.98 (-28.52, -27.45) | +42.17 (+41.81, +42.53) | +100.00 (+100.00, +100.00) | no (inflation) |
| t0 | Pareto point | Stress | -36.15 (-36.80, -35.46) | -36.19 (-37.05, -35.32) | -24.26 (-24.95, -23.54) | +4.12 (+3.68, +4.56) | -26.10 (-26.60, -25.61) | -24.03 (-24.62, -23.49) | +42.90 (+42.49, +43.31) | +100.00 (+100.00, +100.00) | no (inflation) |
| kp50 | Pareto point | Reference | -25.35 (-25.76, -24.94) | -24.73 (-25.72, -23.75) | -19.94 (-20.81, -19.10) | +0.20 (+0.10, +0.30) | -21.29 (-21.96, -20.54) | -20.20 (-20.61, -19.80) | +28.74 (+28.49, +28.98) | +100.00 (+100.00, +100.00) | yes (inflation) |
| kp50 | Pareto point | Adverse | -36.19 (-36.86, -35.50) | -35.17 (-36.39, -33.96) | -27.74 (-28.82, -26.73) | -0.33 (-0.47, -0.21) | -25.36 (-26.17, -24.55) | -28.59 (-29.16, -28.05) | +33.39 (+33.06, +33.71) | +100.00 (+100.00, +100.00) | yes (inflation) |
| kp50 | Pareto point | Stress | -35.43 (-36.08, -34.75) | -35.52 (-36.39, -34.67) | -21.20 (-21.87, -20.50) | -0.71 (-0.81, -0.61) | -24.12 (-24.56, -23.66) | -21.10 (-21.72, -20.48) | +37.14 (+36.71, +37.58) | +100.00 (+100.00, +100.00) | yes (inflation) |
| svc | Pareto point | Reference | -25.18 (-25.59, -24.76) | -24.57 (-25.58, -23.59) | -19.99 (-20.86, -19.13) | +0.09 (+0.00, +0.18) | -21.74 (-22.41, -21.01) | -20.24 (-20.65, -19.84) | +41.43 (+41.07, +41.79) | +100.00 (+100.00, +100.00) | yes (inflation) |
| svc | Pareto point | Adverse | -35.69 (-36.36, -34.99) | -34.66 (-35.90, -33.46) | -28.04 (-29.11, -27.03) | -0.40 (-0.52, -0.28) | -26.19 (-27.03, -25.38) | -28.97 (-29.51, -28.43) | +50.56 (+50.02, +51.09) | +100.00 (+100.00, +100.00) | yes (inflation) |
| svc | Pareto point | Stress | -34.62 (-35.25, -33.96) | -34.74 (-35.59, -33.94) | -27.41 (-28.09, -26.73) | -0.62 (-0.72, -0.52) | -26.37 (-26.89, -25.87) | -27.24 (-27.80, -26.70) | +53.82 (+53.18, +54.46) | +100.00 (+100.00, +100.00) | yes (inflation) |
| fflat | Pareto point | Reference | -18.29 (-18.73, -17.85) | -18.04 (-18.98, -17.11) | -18.54 (-19.41, -17.69) | +5.17 (+4.95, +5.39) | -18.94 (-19.64, -18.21) | -18.50 (-18.96, -18.03) | +0.08 (+0.08, +0.08) | +100.00 (+100.00, +100.00) | no |
| fflat | Pareto point | Adverse | -29.28 (-29.87, -28.65) | -28.59 (-29.67, -27.48) | -26.83 (-27.86, -25.84) | +3.68 (+3.44, +3.93) | -23.69 (-24.49, -22.86) | -27.53 (-28.10, -26.95) | +0.16 (+0.15, +0.16) | +100.00 (+100.00, +100.00) | no |
| fflat | Pareto point | Stress | -25.62 (-26.22, -25.03) | -25.64 (-26.49, -24.86) | -24.97 (-25.66, -24.21) | +1.43 (+1.26, +1.59) | -23.12 (-23.62, -22.61) | -24.78 (-25.30, -24.20) | +0.15 (+0.15, +0.16) | +100.00 (+100.00, +100.00) | no |
| fland | Pareto point | Reference | -18.99 (-19.40, -18.59) | -18.41 (-19.44, -17.39) | -19.99 (-20.85, -19.16) | +2.65 (+2.49, +2.81) | -22.33 (-23.06, -21.60) | -20.25 (-20.67, -19.85) | +5.03 (+4.95, +5.10) | +100.00 (+100.00, +100.00) | no (inflation) |
| fland | Pareto point | Adverse | -26.43 (-27.02, -25.84) | -25.42 (-26.67, -24.09) | -28.21 (-29.31, -27.17) | +3.45 (+3.15, +3.76) | -26.83 (-27.68, -25.98) | -29.16 (-29.72, -28.60) | +6.23 (+6.07, +6.39) | +100.00 (+100.00, +100.00) | no (inflation) |
| fland | Pareto point | Stress | -24.29 (-24.88, -23.71) | -24.37 (-25.22, -23.52) | -28.99 (-29.69, -28.29) | +1.04 (+0.89, +1.20) | -27.51 (-28.03, -27.00) | -28.85 (-29.40, -28.31) | +5.21 (+5.07, +5.37) | +100.00 (+100.00, +100.00) | no (inflation) |

### C2.2 design, wages 90%

| Setting | Role | Environment | basket poverty, % of adult-years | non-participants' basket poverty, % | non-participants' wealth poverty, % | non-participants' income drops of 25%+ with no buffer, per 100 | non-participants under 3 months of basics covered, % | wealth poverty at year 20, % | programme inflation, points a year | participation, mean of years 1-19, % | Passes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| t0 | Pareto point | Reference | -24.99 (-25.40, -24.56) | -24.37 (-25.36, -23.39) | -18.42 (-19.35, -17.48) | +1.90 (+1.70, +2.10) | -20.49 (-21.17, -19.76) | -18.29 (-18.78, -17.85) | +43.79 (+43.41, +44.17) | +100.00 (+100.00, +100.00) | no (inflation) |
| t0 | Pareto point | Adverse | -35.27 (-35.91, -34.60) | -34.31 (-35.55, -33.12) | -6.85 (-8.56, -5.19) | +1.10 (+0.90, +1.29) | -22.46 (-23.26, -21.68) | -8.27 (-9.59, -7.00) | +51.93 (+51.41, +52.45) | +100.00 (+100.00, +100.00) | no (inflation) |
| t0 | Pareto point | Stress | -34.03 (-34.64, -33.40) | -34.08 (-34.89, -33.31) | +12.34 (+10.81, +13.92) | +4.02 (+3.55, +4.49) | -20.60 (-21.07, -20.11) | +11.97 (+10.51, +13.48) | +54.01 (+53.40, +54.62) | +100.00 (+100.00, +100.00) | no (inflation) |
| kp50 | Pareto point | Reference | -24.78 (-25.19, -24.35) | -24.18 (-25.21, -23.16) | -19.47 (-20.38, -18.60) | +0.26 (+0.15, +0.37) | -20.49 (-21.18, -19.76) | -19.48 (-19.92, -19.06) | +33.97 (+33.62, +34.31) | +100.00 (+100.00, +100.00) | yes (inflation) |
| kp50 | Pareto point | Adverse | -34.95 (-35.60, -34.27) | -34.01 (-35.26, -32.79) | -17.87 (-19.19, -16.54) | -0.36 (-0.49, -0.24) | -23.21 (-24.03, -22.42) | -19.11 (-20.14, -18.11) | +40.97 (+40.46, +41.47) | +100.00 (+100.00, +100.00) | yes (inflation) |
| kp50 | Pareto point | Stress | -32.53 (-33.12, -31.95) | -32.63 (-33.41, -31.89) | +21.32 (+19.40, +23.25) | -0.81 (-0.91, -0.71) | -15.82 (-16.43, -15.24) | +21.13 (+19.22, +23.08) | +48.53 (+47.82, +49.24) | +100.00 (+100.00, +100.00) | no (inflation) |
| svc | Pareto point | Reference | -23.85 (-24.26, -23.42) | -23.26 (-24.27, -22.28) | -19.38 (-20.25, -18.52) | +0.12 (+0.02, +0.22) | -20.98 (-21.68, -20.27) | -19.56 (-19.96, -19.17) | +54.40 (+53.77, +55.01) | +100.00 (+100.00, +100.00) | yes (inflation) |
| svc | Pareto point | Adverse | -31.35 (-31.89, -30.81) | -30.61 (-31.68, -29.50) | -25.09 (-26.16, -24.04) | -0.39 (-0.52, -0.27) | -25.07 (-25.88, -24.25) | -25.84 (-26.44, -25.27) | +71.93 (+70.81, +73.05) | +100.00 (+100.00, +100.00) | yes (inflation) |
| svc | Pareto point | Stress | -26.93 (-27.40, -26.46) | -26.99 (-27.61, -26.40) | -20.00 (-20.64, -19.28) | -0.71 (-0.81, -0.60) | -24.68 (-25.16, -24.21) | -19.76 (-20.34, -19.19) | +82.18 (+80.70, +83.66) | +100.00 (+100.00, +100.00) | yes (inflation) |
| fflat | Pareto point | Reference | -18.29 (-18.73, -17.85) | -18.04 (-18.98, -17.11) | -18.54 (-19.41, -17.69) | +5.17 (+4.95, +5.39) | -18.94 (-19.64, -18.21) | -18.50 (-18.96, -18.03) | +0.08 (+0.08, +0.08) | +100.00 (+100.00, +100.00) | no |
| fflat | Pareto point | Adverse | -29.28 (-29.87, -28.65) | -28.59 (-29.67, -27.48) | -26.83 (-27.86, -25.84) | +3.68 (+3.44, +3.93) | -23.69 (-24.49, -22.86) | -27.53 (-28.10, -26.95) | +0.16 (+0.15, +0.16) | +100.00 (+100.00, +100.00) | no |
| fflat | Pareto point | Stress | -25.62 (-26.22, -25.03) | -25.64 (-26.49, -24.86) | -24.97 (-25.66, -24.21) | +1.43 (+1.26, +1.59) | -23.12 (-23.62, -22.61) | -24.78 (-25.30, -24.20) | +0.15 (+0.15, +0.16) | +100.00 (+100.00, +100.00) | no |
| fland | Pareto point | Reference | -18.12 (-18.51, -17.73) | -17.53 (-18.53, -16.52) | -19.99 (-20.85, -19.16) | +3.02 (+2.85, +3.20) | -22.25 (-22.97, -21.52) | -20.24 (-20.66, -19.84) | +5.25 (+5.18, +5.33) | +100.00 (+100.00, +100.00) | no (inflation) |
| fland | Pareto point | Adverse | -24.21 (-24.81, -23.63) | -23.25 (-24.53, -21.89) | -28.10 (-29.19, -27.08) | +4.33 (+3.95, +4.74) | -26.59 (-27.42, -25.75) | -28.97 (-29.52, -28.42) | +6.78 (+6.60, +6.98) | +100.00 (+100.00, +100.00) | no (inflation) |
| fland | Pareto point | Stress | -21.96 (-22.54, -21.39) | -22.02 (-22.84, -21.22) | -28.62 (-29.29, -27.96) | +1.41 (+1.25, +1.59) | -27.25 (-27.77, -26.75) | -28.45 (-28.99, -27.93) | +5.69 (+5.51, +5.87) | +100.00 (+100.00, +100.00) | no (inflation) |

### Summary

| Design | Wages | Setting | Role | Confirmed | Inflation under 5 points everywhere |
|---|---|---|---|---|---|
| release row | 100% | t0 | Pareto point | not confirmed | no |
| release row | 100% | bt0 | Pareto point | not confirmed | no |
| release row | 100% | t4 | Pareto point | not confirmed | no |
| release row | 100% | ixn | Pareto point | not confirmed | no |
| release row | 100% | t8 | Pareto point | not confirmed | no |
| release row | 100% | rcap | Pareto point | not confirmed | no |
| release row | 100% | pr0c75 | Pareto point | not confirmed | no |
| release row | 100% | kp50 | Pareto point | not confirmed | no |
| release row | 100% | mm9 | Pareto point | not confirmed | no |
| release row | 100% | kp25 | Pareto point | not confirmed | no |
| release row | 100% | kp10 | Pareto point | not confirmed | no |
| release row | 100% | phi0 | Pareto point | not confirmed | no |
| release row | 100% | mm6 | Pareto point | not confirmed | no |
| release row | 100% | mm3 | Pareto point | not confirmed | no |
| release row | 100% | ex0 | Pareto point | not confirmed | no |
| release row | 100% | ph5 | Pareto point | not confirmed | no |
| release row | 100% | svc | Pareto point | not confirmed | no |
| release row | 100% | bt25 | Pareto point | not confirmed | no |
| release row | 100% | t25 | Pareto point | not confirmed | no |
| release row | 100% | ph10 | Pareto point | not confirmed | no |
| release row | 100% | h100 | Pareto point | not confirmed | no |
| release row | 100% | bu80 | Pareto point | not confirmed | no |
| release row | 100% | h10 | Pareto point | not confirmed | no |
| release row | 100% | h192 | Pareto point | not confirmed | no |
| release row | 100% | br2 | Pareto point | not confirmed | no |
| release row | 100% | h23 | Pareto point | not confirmed | no |
| release row | 100% | bt50 | Pareto point | not confirmed | no |
| release row | 100% | h119 | Pareto point | not confirmed | no |
| release row | 100% | h4 | Pareto point | not confirmed | no |
| release row | 100% | h141 | Pareto point | not confirmed | no |
| release row | 100% | h126 | Pareto point | not confirmed | no |
| release row | 100% | bu60 | Pareto point | not confirmed | no |
| release row | 100% | m9.6 | Pareto point | not confirmed | no |
| release row | 100% | br1 | Pareto point | not confirmed | no |
| release row | 100% | h50 | Pareto point | not confirmed | no |
| release row | 100% | h89 | Pareto point | not confirmed | no |
| release row | 100% | h132 | Pareto point | not confirmed | no |
| release row | 100% | h41 | Pareto point | not confirmed | no |
| release row | 100% | m3.4 | Pareto point | not confirmed | no |
| release row | 100% | h154 | Pareto point | not confirmed | no |
| release row | 100% | m0.0 | Pareto point | not confirmed | no |
| release row | 100% | h138 | Pareto point | not confirmed | no |
| release row | 100% | h130 | Pareto point | not confirmed | no |
| release row | 100% | h164 | Pareto point | not confirmed | no |
| release row | 100% | h46 | Pareto point | not confirmed | no |
| release row | 100% | h20 | Pareto point | not confirmed | no |
| release row | 100% | h61 | Pareto point | not confirmed | no |
| release row | 100% | m7.12 | Pareto point | not confirmed | no |
| release row | 100% | m1.4 | Pareto point | not confirmed | no |
| release row | 100% | h178 | Pareto point | not confirmed | no |
| release row | 100% | m1.7 | Pareto point | not confirmed | no |
| release row | 100% | m7.11 | Pareto point | not confirmed | no |
| release row | 100% | h32 | Pareto point | not confirmed | no |
| release row | 100% | h131 | Pareto point | not confirmed | no |
| release row | 100% | h166 | Pareto point | not confirmed | no |
| release row | 100% | h66 | Pareto point | not confirmed | no |
| release row | 100% | h102 | Pareto point | not confirmed | no |
| release row | 100% | h153 | Pareto point | not confirmed | no |
| release row | 100% | h146 | Pareto point | not confirmed | no |
| release row | 100% | h105 | Pareto point | not confirmed | no |
| release row | 100% | fland | Pareto point | not confirmed | no |
| release row | 100% | h21 | Pareto point | not confirmed | no |
| release row | 100% | h168 | Pareto point | not confirmed | no |
| release row | 100% | m3.9 | Pareto point | not confirmed | no |
| release row | 100% | h47 | Pareto point | not confirmed | no |
| release row | 100% | m3.5 | Pareto point | not confirmed | no |
| release row | 100% | h108 | Pareto point | not confirmed | no |
| release row | 100% | h86 | Pareto point | not confirmed | no |
| release row | 100% | m9.5 | Pareto point | not confirmed | no |
| release row | 100% | m9.1 | Pareto point | not confirmed | no |
| release row | 100% | h71 | Pareto point | not confirmed | no |
| release row | 100% | m4.16 | Pareto point | not confirmed | no |
| release row | 100% | m9.0 | Pareto point | not confirmed | no |
| release row | 100% | h162 | Pareto point | not confirmed | no |
| release row | 100% | h40 | Pareto point | not confirmed | no |
| release row | 100% | h30 | Pareto point | not confirmed | no |
| release row | 100% | h176 | Pareto point | not confirmed | no |
| release row | 100% | m9.2 | Pareto point | not confirmed | no |
| release row | 100% | h193 | Pareto point | not confirmed | no |
| release row | 100% | m9.3 | Pareto point | not confirmed | no |
| release row | 100% | h113 | Pareto point | not confirmed | no |
| release row | 100% | h14 | Pareto point | not confirmed | no |
| release row | 100% | h129 | Pareto point | not confirmed | no |
| release row | 100% | h182 | Pareto point | not confirmed | no |
| release row | 100% | h25 | Pareto point | not confirmed | no |
| release row | 100% | h26 | Pareto point | not confirmed | no |
| release row | 100% | m3.2 | Pareto point | not confirmed | no |
| release row | 100% | h123 | Pareto point | not confirmed | no |
| release row | 100% | m3.3 | Pareto point | not confirmed | no |
| release row | 100% | m3.0 | Pareto point | not confirmed | no |
| release row | 100% | m1.1 | Pareto point | not confirmed | no |
| release row | 100% | m1.2 | Pareto point | not confirmed | no |
| release row | 100% | h53 | Pareto point | not confirmed | no |
| release row | 100% | h34 | Pareto point | not confirmed | no |
| release row | 100% | m1.0 | Pareto point | not confirmed | no |
| release row | 100% | h8 | Pareto point | not confirmed | no |
| release row | 100% | m1.3 | Pareto point | not confirmed | no |
| release row | 100% | h74 | Pareto point | not confirmed | no |
| release row | 100% | h114 | Pareto point | not confirmed | no |
| release row | 100% | m7.5 | Pareto point | not confirmed | no |
| release row | 100% | h167 | Pareto point | not confirmed | no |
| release row | 100% | sva | Pareto point | not confirmed | no |
| release row | 100% | m2.0 | Pareto point | not confirmed | no |
| release row | 100% | m2.1 | Pareto point | not confirmed | no |
| release row | 100% | m2.4 | Pareto point | not confirmed | no |
| release row | 100% | m2.5 | Pareto point | not confirmed | no |
| release row | 100% | h177 | Pareto point | not confirmed | no |
| release row | 100% | h83 | Pareto point | not confirmed | no |
| release row | 100% | m7.6 | Pareto point | not confirmed | no |
| release row | 100% | m7.9 | Pareto point | not confirmed | no |
| release row | 100% | m7.8 | Pareto point | not confirmed | no |
| release row | 100% | m7.10 | Pareto point | not confirmed | no |
| release row | 100% | h142 | Pareto point | not confirmed | no |
| release row | 100% | h101 | Pareto point | not confirmed | no |
| release row | 100% | m8.0 | Pareto point | not confirmed | no |
| release row | 100% | h122 | Pareto point | not confirmed | no |
| release row | 100% | h67 | Pareto point | not confirmed | no |
| release row | 100% | h92 | Pareto point | not confirmed | no |
| release row | 100% | h137 | Pareto point | not confirmed | no |
| release row | 100% | h98 | Pareto point | not confirmed | no |
| release row | 100% | h28 | Pareto point | not confirmed | no |
| release row | 100% | h160 | Pareto point | not confirmed | no |
| release row | 100% | m4.2 | Pareto point | not confirmed | no |
| release row | 100% | m4.4 | Pareto point | not confirmed | no |
| release row | 100% | h147 | Pareto point | not confirmed | no |
| release row | 100% | h81 | Pareto point | not confirmed | no |
| release row | 100% | m9.12 | Pareto point | not confirmed | no |
| release row | 100% | m5.6 | Pareto point | not confirmed | no |
| release row | 100% | m5.7 | Pareto point | not confirmed | no |
| release row | 100% | m5.4 | Pareto point | not confirmed | no |
| release row | 100% | m5.3 | Pareto point | not confirmed | no |
| release row | 100% | m4.6 | Pareto point | not confirmed | no |
| release row | 100% | m4.5 | Pareto point | not confirmed | no |
| release row | 100% | m5.2 | Pareto point | not confirmed | no |
| release row | 100% | h158 | Pareto point | not confirmed | no |
| release row | 100% | m4.12 | Pareto point | not confirmed | no |
| release row | 100% | m5.0 | Pareto point | not confirmed | no |
| release row | 100% | h170 | Pareto point | not confirmed | no |
| release row | 100% | h55 | Pareto point | not confirmed | no |
| release row | 100% | h77 | Pareto point | not confirmed | no |
| release row | 100% | h93 | Pareto point | not confirmed | no |
| release row | 100% | m6.0 | Pareto point | not confirmed | no |
| release row | 100% | h184 | Pareto point | not confirmed | no |
| release row | 100% | m6.1 | Pareto point | not confirmed | no |
| release row | 100% | m6.4 | Pareto point | not confirmed | no |
| release row | 100% | h197 | Pareto point | not confirmed | no |
| release row | 100% | h189 | Pareto point | not confirmed | no |
| release row | 100% | h62 | Pareto point | not confirmed | no |
| release row | 100% | m9.9 | Pareto point | not confirmed | no |
| release row | 100% | h13 | Pareto point | not confirmed | no |
| release row | 100% | h112 | Pareto point | not confirmed | no |
| release row | 100% | h37 | Pareto point | not confirmed | no |
| release row | 100% | h90 | Pareto point | not confirmed | no |
| release row | 100% | h143 | Pareto point | not confirmed | no |
| release row | 100% | h64 | Pareto point | not confirmed | no |
| release row | 100% | h87 | Pareto point | not confirmed | no |
| release row | 100% | h103 | Pareto point | not confirmed | no |
| release row | 100% | h36 | Pareto point | not confirmed | no |
| release row | 100% | m5.8 | Pareto point | not confirmed | no |
| release row | 100% | m5.11 | Pareto point | not confirmed | no |
| release row | 100% | m6.12 | Pareto point | not confirmed | no |
| release row | 100% | fflat | Pareto point | not confirmed | yes |
| release row | 90% | t0 | Pareto point | not confirmed | no |
| release row | 90% | bt0 | Pareto point | not confirmed | no |
| release row | 90% | t4 | Pareto point | not confirmed | no |
| release row | 90% | t8 | Pareto point | not confirmed | no |
| release row | 90% | fland | Pareto point | not confirmed | no |
| release row | 90% | kp50 | Pareto point | not confirmed | no |
| release row | 90% | ixn | Pareto point | not confirmed | no |
| release row | 90% | pr0c75 | Pareto point | not confirmed | no |
| release row | 90% | kp25 | Pareto point | not confirmed | no |
| release row | 90% | kp10 | Pareto point | not confirmed | no |
| release row | 90% | no6 | Pareto point | not confirmed | no |
| release row | 90% | phi0 | Pareto point | not confirmed | no |
| release row | 90% | ph5 | Pareto point | not confirmed | no |
| release row | 90% | ph10 | Pareto point | not confirmed | no |
| release row | 90% | bt25 | Pareto point | not confirmed | no |
| release row | 90% | bu80 | Pareto point | not confirmed | no |
| release row | 90% | h10 | Pareto point | not confirmed | no |
| release row | 90% | svc | Pareto point | not confirmed | no |
| release row | 90% | bu60 | Pareto point | not confirmed | no |
| release row | 90% | h119 | Pareto point | not confirmed | no |
| release row | 90% | h100 | Pareto point | not confirmed | no |
| release row | 90% | h50 | Pareto point | not confirmed | no |
| release row | 90% | h192 | Pareto point | not confirmed | no |
| release row | 90% | h89 | Pareto point | not confirmed | no |
| release row | 90% | h61 | Pareto point | not confirmed | no |
| release row | 90% | h154 | Pareto point | not confirmed | no |
| release row | 90% | h23 | Pareto point | not confirmed | no |
| release row | 90% | h126 | Pareto point | not confirmed | no |
| release row | 90% | h32 | Pareto point | not confirmed | no |
| release row | 90% | h174 | Pareto point | not confirmed | no |
| release row | 90% | h86 | Pareto point | not confirmed | no |
| release row | 90% | h141 | Pareto point | not confirmed | no |
| release row | 90% | h132 | Pareto point | not confirmed | no |
| release row | 90% | h138 | Pareto point | not confirmed | no |
| release row | 90% | h182 | Pareto point | not confirmed | no |
| release row | 90% | h53 | Pareto point | not confirmed | no |
| release row | 90% | h74 | Pareto point | not confirmed | no |
| release row | 90% | h28 | Pareto point | not confirmed | no |
| release row | 90% | h101 | Pareto point | not confirmed | no |
| release row | 90% | h164 | Pareto point | not confirmed | no |
| release row | 90% | h102 | Pareto point | not confirmed | no |
| release row | 90% | h144 | Pareto point | not confirmed | no |
| release row | 90% | h26 | Pareto point | not confirmed | no |
| release row | 90% | h147 | Pareto point | not confirmed | no |
| release row | 90% | h81 | Pareto point | not confirmed | no |
| release row | 90% | h146 | Pareto point | not confirmed | no |
| release row | 90% | h162 | Pareto point | not confirmed | no |
| release row | 90% | h153 | Pareto point | not confirmed | no |
| release row | 90% | h108 | Pareto point | not confirmed | no |
| release row | 90% | h21 | Pareto point | not confirmed | no |
| release row | 90% | h105 | Pareto point | not confirmed | no |
| release row | 90% | fflat | Pareto point | not confirmed | yes |
| release row | 90% | sva | Pareto point | not confirmed | no |
| release row | 90% | h170 | Pareto point | not confirmed | no |
| release row | 90% | h197 | Pareto point | not confirmed | no |
| release row | 90% | h189 | Pareto point | not confirmed | no |
| release row | 90% | h118 | Pareto point | not confirmed | no |
| release row | 90% | h62 | Pareto point | not confirmed | no |
| release row | 90% | h190 | Pareto point | not confirmed | no |
| release row | 90% | h42 | Pareto point | not confirmed | no |
| release row | 90% | h159 | Pareto point | not confirmed | no |
| release row | 90% | h13 | Pareto point | not confirmed | no |
| release row | 90% | h165 | Pareto point | not confirmed | no |
| release row | 90% | h171 | Pareto point | not confirmed | no |
| release row | 90% | h112 | Pareto point | not confirmed | no |
| release row | 90% | h181 | Pareto point | not confirmed | no |
| release row | 90% | h116 | Pareto point | not confirmed | no |
| release row | 90% | h48 | Pareto point | not confirmed | no |
| release row | 90% | h187 | Pareto point | not confirmed | no |
| release row | 90% | h24 | Pareto point | not confirmed | no |
| release row | 90% | h90 | Pareto point | not confirmed | no |
| release row | 90% | h143 | Pareto point | not confirmed | no |
| release row | 90% | h64 | Pareto point | not confirmed | no |
| release row | 90% | h87 | Pareto point | not confirmed | no |
| C2.2 design | 100% | t0 | Pareto point | not confirmed | no |
| C2.2 design | 100% | kp50 | Pareto point | confirmed | no |
| C2.2 design | 100% | svc | Pareto point | confirmed | no |
| C2.2 design | 100% | fflat | Pareto point | not confirmed | yes |
| C2.2 design | 100% | fland | Pareto point | not confirmed | no |
| C2.2 design | 90% | t0 | Pareto point | not confirmed | no |
| C2.2 design | 90% | kp50 | Pareto point | not confirmed | no |
| C2.2 design | 90% | svc | Pareto point | confirmed | no |
| C2.2 design | 90% | fflat | Pareto point | not confirmed | yes |
| C2.2 design | 90% | fland | Pareto point | not confirmed | no |

