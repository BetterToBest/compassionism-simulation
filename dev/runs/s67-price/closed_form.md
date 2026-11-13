# The capacity price rule in closed form (S67)

Made by `dev/tools/s67_closed_form.py` (research-update `prereg/2026-11-s67-price-rule-derivation.md`, A1). φ = α + ρ (+ κ × bv).

## 1. Roots of the yearly rule, π(t) = (1 + φ − κ)π(t−1) − φπ(t−2) + κm

| Reading | φ | κ | Roots | Modulus | Period (years) | Steady gap per unit of money growth (1 − φ)/κ | Stable |
|---|---|---|---|---|---|---|---|
| main | 0.783 | 0.445 | 0.669 ± 0.579i | 0.885 | 8.8 | 0.488 | yes |
| k 0.25 | 0.783 | 0.250 | 0.766 ± 0.442i | 0.885 | 12.0 | 0.869 | yes |
| k 1 | 0.783 | 1.000 | 0.391 ± 0.793i | 0.885 | 5.6 | 0.217 | yes |
| r 0 | 0.508 | 0.445 | 0.531 ± 0.475i | 0.713 | 8.6 | 1.106 | yes |
| r 0.45 | 0.958 | 0.445 | 0.756 ± 0.621i | 0.979 | 9.1 | 0.095 | yes |
| a 0 | 0.275 | 0.445 | 0.415 ± 0.321i | 0.524 | 9.6 | 1.629 | yes |
| k2 0 | 0.783 | 0.445 | 0.669 ± 0.579i | 0.885 | 8.8 | 0.488 | yes |
| k2 0.657 | 0.783 | 0.445 | 0.669 ± 0.579i | 0.885 | 8.8 | 0.488 | yes |
| slack 0.0446 | 0.783 | 0.445 | 0.669 ± 0.579i | 0.885 | 8.8 | 0.488 | yes |
| today's rule (k 1, a 0, r 0) | 0.000 | 1.000 | 0.000, 0.000 | 0.000 | no wave | 1.000 | yes |
| vel (bv 0.0043) | 0.785 | 0.445 | 0.670 ± 0.580i | 0.886 | 8.8 | 0.484 | yes |
| velh (bv 0.0022) | 0.784 | 0.445 | 0.669 ± 0.579i | 0.885 | 8.8 | 0.486 | yes |
| drift (bd 0.132) | 0.783 | 0.445 | 0.669 ± 0.579i | 0.885 | 8.8 | 0.488 | yes |
| qtvel (today's rule, bv 0.0043) | 0.004 | 1.000 | 0.002 ± 0.066i | 0.066 | 4.1 | 0.996 | yes |
| qtdrift (today's rule, bd 0.132) | 0.000 | 1.000 | 0.000, 0.000 | 0.000 | no wave | 1.000 | yes |
| US 1960-1983 (k 0.282, k2 0.657, persistence 0.922) | 0.922 | 0.282 | 0.820 ± 0.500i | 0.960 | 11.5 | 0.277 | yes |
| US 1984-2024 (k 0.615, k2 0, persistence 0.488) | 0.488 | 0.615 | 0.436 ± 0.545i | 0.699 | 7.0 | 0.833 | yes |
| high-inflation panel, pooled (k 0.085, persistence 0.663) | 0.663 | 0.085 | 0.789 ± 0.201i | 0.814 | 25.1 | 3.959 | yes |
| high-inflation panel, episode effects (k 0.178, persistence 0.544) | 0.544 | 0.178 | 0.683 ± 0.279i | 0.737 | 16.2 | 2.560 | yes |

## 2. The rule alone on a step of money (0.32 log a year, 40 years; wage indexation 1; general basket)

| Reading | Wave, years 5-19 (points) | Period on the path | Damping a year on the path | Pass-through, year 3 | Year 19 | Year 40 | Rationed share, mean of 20 years (%) | Within-year average level over opening, mean | Gap turns negative |
|---|---|---|---|---|---|---|---|---|---|
| main | 35.8 | 8.8 | 0.882 | 0.991 | 1.021 | 1.013 | 12.2 | 1.000 | yes, year 6 |
| k 0.25 | 32.6 | 12.0 | 0.885 | 0.636 | 1.012 | 1.003 | 22.9 | 1.000 | no |
| k 1 | 35.3 | 6.2 | 0.891 | 1.465 | 1.039 | 1.020 | 4.3 | 1.000 | yes, year 4 |
| r 0 | 10.0 | 8.5 | 0.709 | 0.853 | 0.994 | 0.997 | 26.6 | 1.000 | no |
| r 0.45 | 73.4 | 16.5 | 0.980 | 1.091 | 1.005 | 1.055 | 9.0 | 1.000 | yes, year 5 |
| a 0 | 2.0 | 9.7 | 0.530 | 0.753 | 0.967 | 0.984 | 36.5 | 1.000 | no |
| k2 0 | 35.9 | 8.9 | 0.885 | 0.991 | 1.021 | 1.013 | 12.1 | 1.000 | yes, year 6 |
| k2 0.657 | 36.4 | 8.8 | 0.884 | 0.991 | 1.020 | 1.013 | 12.5 | 1.000 | yes, year 6 |
| slack 0.0446 | 36.7 | 8.9 | 0.884 | 0.922 | 1.014 | 1.009 | 12.0 | 1.000 | yes, year 7 |
| today's rule (k 1, a 0, r 0) | 0.0 | - | - | 1.000 | 1.000 | 1.000 | 22.9 | 1.000 | no |
| wy (4 sub-steps; k 0.0788, k2 0, r 0.2333 a quarter) | 15.2 | 10.3 | 0.770 | 0.597 | 0.970 | 0.986 | 19.9 | 1.123 | no |
| wyroot (4 sub-steps; a 0, r 0.9406, k 0.0317, k2 0.0036) | 40.3 | 8.9 | 0.886 | 0.638 | 0.984 | 0.995 | 11.3 | 1.125 | yes, year 7 |
| today's rule in 4 sub-steps (k 1, a 0, r 0) | 0.0 | 10.0 | 1.000 | 1.000 | 1.000 | 1.000 | 2.0 | 1.127 | no |
| vel (bv 0.0043) | 36.1 | 8.9 | 0.886 | 0.992 | 1.021 | 1.013 | 12.2 | 1.000 | yes, year 6 |
| velh (bv 0.0022) | 36.0 | 8.9 | 0.886 | 0.992 | 1.021 | 1.013 | 12.2 | 1.000 | yes, year 6 |
| drift (bd 0.132) | 42.4 | 8.8 | 0.882 | 1.122 | 1.155 | 1.147 | 14.1 | 1.000 | yes, year 6 |
| qtvel (today's rule, bv 0.0043) | 0.0 | 4.0 | 0.065 | 1.001 | 1.000 | 1.000 | 23.0 | 1.000 | no |
| qtdrift (today's rule, bd 0.132) | 0.0 | - | - | 1.132 | 1.132 | 1.132 | 26.1 | 1.000 | no |
| US 1960-1983 (k 0.282, k2 0.657, persistence 0.922) | 67.7 | 10.3 | 0.959 | 0.756 | 1.043 | 1.021 | 14.9 | 1.000 | yes, year 7 |
| US 1984-2024 (k 0.615, k2 0, persistence 0.488) | 4.7 | 7.0 | 0.698 | 1.029 | 1.009 | 1.004 | 19.8 | 1.000 | no |
| high-inflation panel, pooled (k 0.085, persistence 0.663) | 17.0 | 25.0 | 0.813 | 0.226 | 0.846 | 0.926 | 66.7 | 1.000 | no |
| high-inflation panel, episode effects (k 0.178, persistence 0.544) | 4.9 | 16.0 | 0.735 | 0.419 | 0.918 | 0.961 | 52.0 | 1.000 | no |

## 3. The closed form against the engine (S58 pilot, Reference, seeds 1-100)

Each seed's closed-form path is driven by the money of the same design under today's rule on that seed (its yearly log price change), then compared with the capacity row's yearly inflation in the engine. Differences in points of yearly inflation; wave = largest less smallest yearly inflation over years 5-19 on the mean path.

| S58 row | Mean absolute difference | Largest (mean path) | In year | Wave, engine | Wave, closed form | Period on the engine path | Closed-form period |
|---|---|---|---|---|---|---|---|
| c22-cap | 1.01 | -2.55 | 4 | 39.1 | 41.4 | 9.3 | 8.8 |
| c22-k25 | 1.21 | -2.13 | 16 | 35.5 | 38.0 | 11.0 | 12.0 |
| c22-k1 | 1.37 | -3.20 | 10 | 31.8 | 36.4 | 7.0 | 5.6 |
| c22-r0 | 0.42 | -1.74 | 3 | 16.3 | 16.5 | 8.0 | 8.6 |
| c22-r45 | 2.02 | -11.76 | 19 | 81.8 | 83.8 | - | 9.1 |
| c22-a0 | 0.42 | -1.41 | 3 | 8.6 | 9.3 | 2.0 | 9.6 |
| c22-h | 1.11 | +1.96 | 9 | 40.8 | 42.6 | 9.3 | 8.8 |
| c22-k2z | 0.99 | -2.55 | 4 | 39.1 | 41.4 | 9.3 | 8.8 |
| c22-k2h | 1.57 | -3.39 | 12 | 38.3 | 41.5 | 9.3 | 8.8 |
| c22-nest | 0.00 | -0.00 | 14 | 9.9 | 9.9 | 2.0 | no wave |
| rel-cap | 1.34 | +2.80 | 11 | 32.0 | 34.3 | 8.7 | 8.8 |
| rel-k25 | 0.87 | -1.91 | 8 | 28.1 | 29.2 | 11.0 | 12.0 |
