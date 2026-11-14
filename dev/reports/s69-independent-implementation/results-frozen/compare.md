## Summary

| Environment | Run | Keys | Keys exact in all 500 seeds | Keys failing the 2-SE test | Keys missing | Seconds | Seeds that failed to run |
|---|---|---|---|---|---|---|---|
| ref | base | 958 | 958 | 0 | 0 | 325.3 | 0 |
| ref | main | 990 | 990 | 0 | 0 | 383.5 | 0 |
| adv | base | 958 | 958 | 0 | 0 | 293.5 | 0 |
| adv | main | 990 | 990 | 0 | 0 | 396.1 | 0 |
| st | base | 958 | 958 | 0 | 0 | 302.2 | 0 |
| st | main | 990 | 990 | 0 | 0 | 383.4 | 0 |

| Environment | Effect keys compared (main row minus no programme) | Failing the 2-SE test |
|---|---|---|
| ref | 958 | 0 |
| adv | 958 | 0 |
| st | 958 | 0 |

## Keys not exact in every seed

Why: "zero earnings" = every such seed has an adult-year whose earnings are zero in exact arithmetic, so rounding decides whether it was worked (GAPS.md item 22); "ties" = a weighted distribution measure whose order of near-tied adults at the borrowing limit is set by rounding (item 24); "not explained" = neither.

| Environment | Run | Key | Seeds not exact | Of them, seeds with a zero-earnings adult-year | Why | First seeds |
|---|---|---|---|---|---|---|

## Headline keys

| Environment | Run | Key | Reference mean | My mean | Difference | 2 SE | Match (2 SE) | Seeds exact |
|---|---|---|---|---|---|---|---|---|
| ref | base | bNAPy | 19.6161 | 19.6161 | 0 | 0.1639 | yes | 500 |
| ref | base | bOAPy | 19.6161 | 19.6161 | 0 | 0.1639 | yes | 500 |
| ref | base | cost | 0 | 0 | 0 | 0 | yes | 500 |
| ref | base | crRel | 0 | 0 | 0 | 0 | yes | 500 |
| ref | base | drHit | 46.7730 | 46.7730 | 0 | 0.3329 | yes | 500 |
| ref | base | emUrate | 2.3636 | 2.3636 | 0 | 0.01693 | yes | 500 |
| ref | base | endoAnn | 0 | 0 | 0 | 0 | yes | 500 |
| ref | base | epPY | 0.2565 | 0.2565 | 0 | 0.001843 | yes | 500 |
| ref | base | fgt0PY | 36.0977 | 36.0977 | 0 | 0.2258 | yes | 500 |
| ref | base | fgt2PY | 9.4641 | 9.4641 | 0 | 0.07928 | yes | 500 |
| ref | base | finGapSh | 0 | 0 | 0 | 0 | yes | 500 |
| ref | base | giniD | 0.9652 | 0.9652 | 0 | 0.001287 | yes | 500 |
| ref | base | giniX | 0.9652 | 0.9652 | 0 | 0.001287 | yes | 500 |
| ref | base | hrs | -0.01344 | -0.01344 | 0 | 0.0002354 | yes | 500 |
| ref | base | jnP19 | 0 | 0 | 0 | 0 | yes | 500 |
| ref | base | lfShare | 17.3904 | 17.3904 | 0 | 0.2163 | yes | 500 |
| ref | base | medWealthReal | 231268.9 | 231268.9 | 0 | 2342.3 | yes | 500 |
| ref | base | pLev20 | 1.0000 | 1.0000 | 0 | 0 | yes | 500 |
| ref | base | pov | 23.7416 | 23.7416 | 0 | 0.2036 | yes | 500 |
| ref | base | snAll | 989.6247 | 989.6247 | 0 | 13.6473 | yes | 500 |
| ref | base | tauMean | 0 | 0 | 0 | 0 | yes | 500 |
| ref | base | wtF0E | 33.2551 | 33.2551 | 0 | 0.3042 | yes | 500 |
| ref | base | wtGnE | 0.8127 | 0.8127 | 0 | 0.004191 | yes | 500 |
| ref | base | wtPovE | 24.2647 | 24.2647 | 0 | 0.2057 | yes | 500 |
| ref | base | y0BN | 15.9756 | 15.9756 | 0 | 0.1588 | yes | 500 |
| ref | base | y0BO | 15.9756 | 15.9756 | 0 | 0.1588 | yes | 500 |
| ref | base | y0Ep | 0.2245 | 0.2245 | 0 | 0.001216 | yes | 500 |
| ref | base | y0F0 | 39.7592 | 39.7592 | 0 | 0.3082 | yes | 500 |
| ref | base | y0Fpl | 16.3952 | 16.3952 | 0 | 0.2147 | yes | 500 |
| ref | base | y0GiniW | 0.9879 | 0.9879 | 0 | 0.0003521 | yes | 500 |
| ref | base | y0Pov | 25.0232 | 25.0232 | 0 | 0.1735 | yes | 500 |
| ref | main | bNAPy | 0.8921 | 0.8921 | 0 | 0.03633 | yes | 500 |
| ref | main | bOAPy | 0.4887 | 0.4887 | 0 | 0.02665 | yes | 500 |
| ref | main | cost | 80493.3 | 80493.3 | 0 | 133.2204 | yes | 500 |
| ref | main | crRel | 2907.9 | 2907.9 | 0 | 33.6358 | yes | 500 |
| ref | main | drHit | 30.0683 | 30.0683 | 0 | 0.8496 | yes | 500 |
| ref | main | emUrate | 2.3636 | 2.3636 | 0 | 0.01693 | yes | 500 |
| ref | main | endoAnn | 0.001512 | 0.001512 | -4.337e-19 | 1.636e-05 | yes | 500 |
| ref | main | epPY | 0.05874 | 0.05874 | 0 | 0.0004569 | yes | 500 |
| ref | main | fgt0PY | 3.7069 | 3.7069 | 0 | 0.05996 | yes | 500 |
| ref | main | fgt2PY | 0.1803 | 0.1803 | 0 | 0.003679 | yes | 500 |
| ref | main | finGapSh | 0.07162 | 0.07162 | 0 | 0.0006865 | yes | 500 |
| ref | main | giniD | 0.9445 | 0.9445 | 0 | 0.002098 | yes | 500 |
| ref | main | giniX | 0.93 | 0.93 | 0 | 0.002652 | yes | 500 |
| ref | main | hrs | 0.08867 | 0.08867 | -2.776e-17 | 0.02525 | yes | 500 |
| ref | main | jnP19 | 100.0000 | 100.0000 | 0 | 0 | yes | 500 |
| ref | main | lfShare | 17.3904 | 17.3904 | 0 | 0.2163 | yes | 500 |
| ref | main | medWealthReal | 439206.8 | 439206.8 | 5.821e-11 | 2445.4 | yes | 500 |
| ref | main | pLev20 | 1.0291 | 1.0291 | 0 | 0.0003195 | yes | 500 |
| ref | main | paSh | 43.8882 | 43.8882 | 0 | 0.1041 | yes | 500 |
| ref | main | poSub | 1334.9 | 1334.9 | 0 | 3.7608 | yes | 500 |
| ref | main | pov | 1.2452 | 1.2452 | 0 | 0.06083 | yes | 500 |
| ref | main | snAll | 321.9487 | 321.9487 | 0 | 5.9352 | yes | 500 |
| ref | main | tauMean | 0.02993 | 0.02993 | 0 | 0.0002418 | yes | 500 |
| ref | main | wtF0E | 0.8808 | 0.8808 | 0 | 0.055 | yes | 500 |
| ref | main | wtGnE | 0.7019 | 0.7019 | 0 | 0.005982 | yes | 500 |
| ref | main | wtPovE | 1.3138 | 1.3138 | 0 | 0.06402 | yes | 500 |
| ref | main | y0BN | 2.8636 | 2.8636 | 0 | 0.09314 | yes | 500 |
| ref | main | y0BO | 0.9404 | 0.9404 | 0 | 0.0537 | yes | 500 |
| ref | main | y0Ep | 0.1283 | 0.1283 | 0 | 0.001245 | yes | 500 |
| ref | main | y0F0 | 20.8348 | 20.8348 | 0 | 0.2658 | yes | 500 |
| ref | main | y0Fpl | 20.1840 | 20.1840 | 0 | 0.2332 | yes | 500 |
| ref | main | y0GiniW | 0.9878 | 0.9878 | 0 | 0.0003556 | yes | 500 |
| ref | main | y0Pov | 23.5092 | 23.5092 | 0 | 0.1713 | yes | 500 |
| ref | effect | bNAPy | -18.7240 | -18.7240 | 0 | 0.1609 | yes |  |
| ref | effect | bOAPy | -19.1274 | -19.1274 | 0 | 0.1638 | yes |  |
| ref | effect | cost | 80493.3 | 80493.3 | 0 | 133.2204 | yes |  |
| ref | effect | crRel | 2907.9 | 2907.9 | 0 | 33.6358 | yes |  |
| ref | effect | drHit | -16.7047 | -16.7047 | 0 | 0.8492 | yes |  |
| ref | effect | emUrate | 0 | 0 | 0 | 0 | yes |  |
| ref | effect | endoAnn | 0.001512 | 0.001512 | -4.337e-19 | 1.636e-05 | yes |  |
| ref | effect | epPY | -0.1978 | -0.1978 | 0 | 0.001835 | yes |  |
| ref | effect | fgt0PY | -32.3908 | -32.3908 | 0 | 0.217 | yes |  |
| ref | effect | fgt2PY | -9.2838 | -9.2838 | 0 | 0.07782 | yes |  |
| ref | effect | finGapSh | 0.07162 | 0.07162 | 0 | 0.0006865 | yes |  |
| ref | effect | giniD | -0.0207 | -0.0207 | 3.469e-18 | 0.0008189 | yes |  |
| ref | effect | giniX | -0.03526 | -0.03526 | 1.388e-17 | 0.001374 | yes |  |
| ref | effect | hrs | 0.1021 | 0.1021 | -2.776e-17 | 0.02524 | yes |  |
| ref | effect | jnP19 | 100.0000 | 100.0000 | 0 | 0 | yes |  |
| ref | effect | lfShare | 0 | 0 | 0 | 0 | yes |  |
| ref | effect | medWealthReal | 207937.9 | 207937.9 | 0 | 2054.7 | yes |  |
| ref | effect | pLev20 | 0.02912 | 0.02912 | 0 | 0.0003195 | yes |  |
| ref | effect | pov | -22.4964 | -22.4964 | 0 | 0.2043 | yes |  |
| ref | effect | snAll | -667.6760 | -667.6760 | 0 | 10.3699 | yes |  |
| ref | effect | tauMean | 0.02993 | 0.02993 | 0 | 0.0002418 | yes |  |
| ref | effect | wtF0E | -32.3742 | -32.3742 | 0 | 0.3037 | yes |  |
| ref | effect | wtGnE | -0.1108 | -0.1108 | 0 | 0.001888 | yes |  |
| ref | effect | wtPovE | -22.9509 | -22.9509 | 0 | 0.2069 | yes |  |
| ref | effect | y0BN | -13.1120 | -13.1120 | 0 | 0.1574 | yes |  |
| ref | effect | y0BO | -15.0352 | -15.0352 | 0 | 0.1646 | yes |  |
| ref | effect | y0Ep | -0.09619 | -0.09619 | 0 | 0.001486 | yes |  |
| ref | effect | y0F0 | -18.9244 | -18.9244 | 0 | 0.2913 | yes |  |
| ref | effect | y0Fpl | 3.7888 | 3.7888 | 0 | 0.1096 | yes |  |
| ref | effect | y0GiniW | -9.162e-05 | -9.162e-05 | 7.549e-18 | 3.842e-06 | yes |  |
| ref | effect | y0Pov | -1.5140 | -1.5140 | 0 | 0.08216 | yes |  |
| adv | base | bNAPy | 20.6438 | 20.6438 | 0 | 0.1683 | yes | 500 |
| adv | base | bOAPy | 20.6438 | 20.6438 | 0 | 0.1683 | yes | 500 |
| adv | base | cost | 0 | 0 | 0 | 0 | yes | 500 |
| adv | base | crRel | 32235.6 | 32235.6 | -1.819e-11 | 155.4602 | yes | 500 |
| adv | base | drHit | 41.9927 | 41.9927 | 0 | 0.2927 | yes | 500 |
| adv | base | emUrate | 3.5909 | 3.5909 | 0 | 0.05746 | yes | 500 |
| adv | base | endoAnn | 0 | 0 | 0 | 0 | yes | 500 |
| adv | base | epPY | 0.2785 | 0.2785 | 0 | 0.002116 | yes | 500 |
| adv | base | fgt0PY | 44.6290 | 44.6290 | 0 | 0.2591 | yes | 500 |
| adv | base | fgt2PY | 11.7049 | 11.7049 | 0 | 0.09248 | yes | 500 |
| adv | base | finGapSh | 0 | 0 | 0 | 0 | yes | 500 |
| adv | base | giniD | 0.9722 | 0.9722 | 0 | 0.001016 | yes | 500 |
| adv | base | giniX | 0.9722 | 0.9722 | 0 | 0.001016 | yes | 500 |
| adv | base | hrs | -0.01776 | -0.01776 | 3.469e-18 | 0.0002713 | yes | 500 |
| adv | base | jnP19 | 0 | 0 | 0 | 0 | yes | 500 |
| adv | base | lfShare | 17.3904 | 17.3904 | 0 | 0.2163 | yes | 500 |
| adv | base | medWealthReal | 209069.8 | 209069.8 | -5.821e-11 | 2348.1 | yes | 500 |
| adv | base | pLev20 | 1.4568 | 1.4568 | 0 | 2.242e-17 | yes | 500 |
| adv | base | pov | 26.9268 | 26.9268 | 0 | 0.2214 | yes | 500 |
| adv | base | snAll | 1245.6 | 1245.6 | 0 | 15.4517 | yes | 500 |
| adv | base | tauMean | 0 | 0 | 0 | 0 | yes | 500 |
| adv | base | wtF0E | 49.5292 | 49.5292 | 0 | 0.4117 | yes | 500 |
| adv | base | wtGnE | 0.8209 | 0.8209 | 0 | 0.004075 | yes | 500 |
| adv | base | wtPovE | 27.4923 | 27.4923 | 0 | 0.2235 | yes | 500 |
| adv | base | y0BN | 15.9756 | 15.9756 | 0 | 0.1588 | yes | 500 |
| adv | base | y0BO | 15.9756 | 15.9756 | 0 | 0.1588 | yes | 500 |
| adv | base | y0Ep | 0.2245 | 0.2245 | 0 | 0.001216 | yes | 500 |
| adv | base | y0F0 | 39.7592 | 39.7592 | 0 | 0.3082 | yes | 500 |
| adv | base | y0Fpl | 16.3952 | 16.3952 | 0 | 0.2147 | yes | 500 |
| adv | base | y0GiniW | 0.9879 | 0.9879 | 0 | 0.0003521 | yes | 500 |
| adv | base | y0Pov | 25.0232 | 25.0232 | 0 | 0.1735 | yes | 500 |
| adv | main | bNAPy | 0.8134 | 0.8134 | 0 | 0.0343 | yes | 500 |
| adv | main | bOAPy | 0.4703 | 0.4703 | 0 | 0.0268 | yes | 500 |
| adv | main | cost | 79396.2 | 79396.2 | 0 | 131.7185 | yes | 500 |
| adv | main | crRel | 34650.7 | 34650.7 | 0 | 172.1662 | yes | 500 |
| adv | main | drHit | 27.1255 | 27.1255 | 0 | 0.8156 | yes | 500 |
| adv | main | emUrate | 3.5909 | 3.5909 | 0 | 0.05746 | yes | 500 |
| adv | main | endoAnn | 0.001834 | 0.001834 | -4.337e-19 | 1.95e-05 | yes | 500 |
| adv | main | epPY | 0.05908 | 0.05908 | 0 | 0.0004668 | yes | 500 |
| adv | main | fgt0PY | 3.9943 | 3.9943 | 0 | 0.06366 | yes | 500 |
| adv | main | fgt2PY | 0.1871 | 0.1871 | 0 | 0.003855 | yes | 500 |
| adv | main | finGapSh | 0.1049 | 0.1049 | 0 | 0.0009353 | yes | 500 |
| adv | main | giniD | 0.9524 | 0.9524 | 0 | 0.001801 | yes | 500 |
| adv | main | giniX | 0.937 | 0.937 | 0 | 0.0024 | yes | 500 |
| adv | main | hrs | 0.08381 | 0.08381 | 9.714e-17 | 0.02685 | yes | 500 |
| adv | main | jnP19 | 100.0000 | 100.0000 | 0 | 0 | yes | 500 |
| adv | main | lfShare | 17.3904 | 17.3904 | 0 | 0.2163 | yes | 500 |
| adv | main | medWealthReal | 406134.8 | 406134.8 | 0 | 2272.3 | yes | 500 |
| adv | main | pLev20 | 1.5084 | 1.5084 | 0 | 0.0005581 | yes | 500 |
| adv | main | paSh | 43.8504 | 43.8504 | 0 | 0.1055 | yes | 500 |
| adv | main | poSub | 1331.3 | 1331.3 | 0 | 3.8121 | yes | 500 |
| adv | main | pov | 1.3556 | 1.3556 | 0 | 0.06346 | yes | 500 |
| adv | main | snAll | 354.3265 | 354.3265 | 0 | 6.4723 | yes | 500 |
| adv | main | tauMean | 0.03678 | 0.03678 | 0 | 0.0003008 | yes | 500 |
| adv | main | wtF0E | 1.1657 | 1.1657 | 0 | 0.06274 | yes | 500 |
| adv | main | wtGnE | 0.7114 | 0.7114 | 0 | 0.005911 | yes | 500 |
| adv | main | wtPovE | 1.4343 | 1.4343 | 0 | 0.06682 | yes | 500 |
| adv | main | y0BN | 2.8636 | 2.8636 | 0 | 0.09314 | yes | 500 |
| adv | main | y0BO | 0.9404 | 0.9404 | 0 | 0.0537 | yes | 500 |
| adv | main | y0Ep | 0.1283 | 0.1283 | 0 | 0.001245 | yes | 500 |
| adv | main | y0F0 | 20.8348 | 20.8348 | 0 | 0.2658 | yes | 500 |
| adv | main | y0Fpl | 20.1840 | 20.1840 | 0 | 0.2332 | yes | 500 |
| adv | main | y0GiniW | 0.9878 | 0.9878 | 0 | 0.0003556 | yes | 500 |
| adv | main | y0Pov | 23.5092 | 23.5092 | 0 | 0.1713 | yes | 500 |
| adv | effect | bNAPy | -19.8304 | -19.8304 | 0 | 0.1667 | yes |  |
| adv | effect | bOAPy | -20.1736 | -20.1736 | 0 | 0.1691 | yes |  |
| adv | effect | cost | 79396.2 | 79396.2 | 0 | 131.7185 | yes |  |
| adv | effect | crRel | 2415.1 | 2415.1 | 1.819e-11 | 29.1127 | yes |  |
| adv | effect | drHit | -14.8672 | -14.8672 | 0 | 0.8227 | yes |  |
| adv | effect | emUrate | 0 | 0 | 0 | 0 | yes |  |
| adv | effect | endoAnn | 0.001834 | 0.001834 | -4.337e-19 | 1.95e-05 | yes |  |
| adv | effect | epPY | -0.2194 | -0.2194 | 0 | 0.002112 | yes |  |
| adv | effect | fgt0PY | -40.6347 | -40.6347 | 0 | 0.2551 | yes |  |
| adv | effect | fgt2PY | -11.5178 | -11.5178 | 0 | 0.0913 | yes |  |
| adv | effect | finGapSh | 0.1049 | 0.1049 | 0 | 0.0009353 | yes |  |
| adv | effect | giniD | -0.01978 | -0.01978 | 6.939e-18 | 0.000799 | yes |  |
| adv | effect | giniX | -0.03514 | -0.03514 | 0 | 0.001398 | yes |  |
| adv | effect | hrs | 0.1016 | 0.1016 | 8.327e-17 | 0.02685 | yes |  |
| adv | effect | jnP19 | 100.0000 | 100.0000 | 0 | 0 | yes |  |
| adv | effect | lfShare | 0 | 0 | 0 | 0 | yes |  |
| adv | effect | medWealthReal | 197065.0 | 197065.0 | 5.821e-11 | 1877.8 | yes |  |
| adv | effect | pLev20 | 0.05162 | 0.05162 | 0 | 0.0005581 | yes |  |
| adv | effect | pov | -25.5712 | -25.5712 | 0 | 0.2255 | yes |  |
| adv | effect | snAll | -891.2340 | -891.2340 | 0 | 12.2419 | yes |  |
| adv | effect | tauMean | 0.03678 | 0.03678 | 0 | 0.0003008 | yes |  |
| adv | effect | wtF0E | -48.3636 | -48.3636 | 0 | 0.4131 | yes |  |
| adv | effect | wtGnE | -0.1095 | -0.1095 | -1.388e-17 | 0.001944 | yes |  |
| adv | effect | wtPovE | -26.0579 | -26.0579 | 0 | 0.2281 | yes |  |
| adv | effect | y0BN | -13.1120 | -13.1120 | 0 | 0.1574 | yes |  |
| adv | effect | y0BO | -15.0352 | -15.0352 | 0 | 0.1646 | yes |  |
| adv | effect | y0Ep | -0.09619 | -0.09619 | 0 | 0.001486 | yes |  |
| adv | effect | y0F0 | -18.9244 | -18.9244 | 0 | 0.2913 | yes |  |
| adv | effect | y0Fpl | 3.7888 | 3.7888 | 0 | 0.1096 | yes |  |
| adv | effect | y0GiniW | -9.162e-05 | -9.162e-05 | 7.549e-18 | 3.842e-06 | yes |  |
| adv | effect | y0Pov | -1.5140 | -1.5140 | 0 | 0.08216 | yes |  |
| st | base | bNAPy | 20.6438 | 20.6438 | 0 | 0.1683 | yes | 500 |
| st | base | bOAPy | 20.6438 | 20.6438 | 0 | 0.1683 | yes | 500 |
| st | base | cost | 0 | 0 | 0 | 0 | yes | 500 |
| st | base | crRel | 32235.6 | 32235.6 | -1.819e-11 | 155.4602 | yes | 500 |
| st | base | drHit | 41.9927 | 41.9927 | 0 | 0.2927 | yes | 500 |
| st | base | emUrate | 3.5909 | 3.5909 | 0 | 0.05746 | yes | 500 |
| st | base | endoAnn | 0 | 0 | 0 | 0 | yes | 500 |
| st | base | epPY | 0.2785 | 0.2785 | 0 | 0.002116 | yes | 500 |
| st | base | fgt0PY | 44.6290 | 44.6290 | 0 | 0.2591 | yes | 500 |
| st | base | fgt2PY | 11.7049 | 11.7049 | 0 | 0.09248 | yes | 500 |
| st | base | finGapSh | 0 | 0 | 0 | 0 | yes | 500 |
| st | base | giniD | 0.9722 | 0.9722 | 0 | 0.001016 | yes | 500 |
| st | base | giniX | 0.9722 | 0.9722 | 0 | 0.001016 | yes | 500 |
| st | base | hrs | -0.01776 | -0.01776 | 3.469e-18 | 0.0002713 | yes | 500 |
| st | base | jnP19 | 0 | 0 | 0 | 0 | yes | 500 |
| st | base | lfShare | 17.3904 | 17.3904 | 0 | 0.2163 | yes | 500 |
| st | base | medWealthReal | 209069.8 | 209069.8 | -5.821e-11 | 2348.1 | yes | 500 |
| st | base | pLev20 | 1.4568 | 1.4568 | 0 | 2.242e-17 | yes | 500 |
| st | base | pov | 26.9268 | 26.9268 | 0 | 0.2214 | yes | 500 |
| st | base | snAll | 1245.6 | 1245.6 | 0 | 15.4517 | yes | 500 |
| st | base | tauMean | 0 | 0 | 0 | 0 | yes | 500 |
| st | base | wtF0E | 49.5292 | 49.5292 | 0 | 0.4117 | yes | 500 |
| st | base | wtGnE | 0.8209 | 0.8209 | 0 | 0.004075 | yes | 500 |
| st | base | wtPovE | 27.4923 | 27.4923 | 0 | 0.2235 | yes | 500 |
| st | base | y0BN | 15.9756 | 15.9756 | 0 | 0.1588 | yes | 500 |
| st | base | y0BO | 15.9756 | 15.9756 | 0 | 0.1588 | yes | 500 |
| st | base | y0Ep | 0.2245 | 0.2245 | 0 | 0.001216 | yes | 500 |
| st | base | y0F0 | 39.7592 | 39.7592 | 0 | 0.3082 | yes | 500 |
| st | base | y0Fpl | 16.3952 | 16.3952 | 0 | 0.2147 | yes | 500 |
| st | base | y0GiniW | 0.9879 | 0.9879 | 0 | 0.0003521 | yes | 500 |
| st | base | y0Pov | 25.0232 | 25.0232 | 0 | 0.1735 | yes | 500 |
| st | main | bNAPy | 0.8094 | 0.8094 | 0 | 0.0337 | yes | 500 |
| st | main | bOAPy | 0.6669 | 0.6669 | 0 | 0.03297 | yes | 500 |
| st | main | cost | 68177.9 | 68177.9 | 0 | 113.0634 | yes | 500 |
| st | main | crRel | 34644.4 | 34644.4 | 0 | 172.1288 | yes | 500 |
| st | main | drHit | 26.7336 | 26.7336 | 0 | 0.7758 | yes | 500 |
| st | main | emUrate | 3.5909 | 3.5909 | 0 | 0.05746 | yes | 500 |
| st | main | endoAnn | 0.001829 | 0.001829 | 4.337e-19 | 1.953e-05 | yes | 500 |
| st | main | epPY | 0.07105 | 0.07105 | 0 | 0.000515 | yes | 500 |
| st | main | fgt0PY | 4.5014 | 4.5014 | 0 | 0.06649 | yes | 500 |
| st | main | fgt2PY | 0.1975 | 0.1975 | -2.776e-17 | 0.003912 | yes | 500 |
| st | main | finGapSh | 0.1146 | 0.1146 | -1.388e-17 | 0.0007258 | yes | 500 |
| st | main | giniD | 0.9579 | 0.9579 | 0 | 0.001584 | yes | 500 |
| st | main | giniX | 0.9424 | 0.9424 | 0 | 0.002196 | yes | 500 |
| st | main | hrs | 0.05525 | 0.05525 | 8.327e-17 | 0.02359 | yes | 500 |
| st | main | jnP19 | 100.0000 | 100.0000 | 0 | 0 | yes | 500 |
| st | main | lfShare | 17.3904 | 17.3904 | 0 | 0.2163 | yes | 500 |
| st | main | medWealthReal | 378155.1 | 378155.1 | 0 | 2223.1 | yes | 500 |
| st | main | pLev20 | 1.5083 | 1.5083 | 0 | 0.0005588 | yes | 500 |
| st | main | paSh | 37.1914 | 37.1914 | 0 | 0.2084 | yes | 500 |
| st | main | poSub | 983.1400 | 983.1400 | 1.137e-13 | 6.0807 | yes | 500 |
| st | main | pov | 1.9128 | 1.9128 | 0 | 0.07429 | yes | 500 |
| st | main | snAll | 416.4433 | 416.4433 | 0 | 7.6059 | yes | 500 |
| st | main | tauMean | 0.02429 | 0.02429 | -3.469e-18 | 0.000244 | yes | 500 |
| st | main | wtF0E | 2.0569 | 2.0569 | 0 | 0.08325 | yes | 500 |
| st | main | wtGnE | 0.7245 | 0.7245 | 0 | 0.005727 | yes | 500 |
| st | main | wtPovE | 2.0282 | 2.0282 | 0 | 0.0779 | yes | 500 |
| st | main | y0BN | 2.8132 | 2.8132 | 0 | 0.09319 | yes | 500 |
| st | main | y0BO | 1.3460 | 1.3460 | 0 | 0.0629 | yes | 500 |
| st | main | y0Ep | 0.1404 | 0.1404 | 0 | 0.001258 | yes | 500 |
| st | main | y0F0 | 21.0760 | 21.0760 | 0 | 0.2675 | yes | 500 |
| st | main | y0Fpl | 20.1064 | 20.1064 | 0 | 0.2328 | yes | 500 |
| st | main | y0GiniW | 0.9878 | 0.9878 | 0 | 0.0003556 | yes | 500 |
| st | main | y0Pov | 23.5092 | 23.5092 | 0 | 0.1723 | yes | 500 |
| st | effect | bNAPy | -19.8344 | -19.8344 | 0 | 0.1672 | yes |  |
| st | effect | bOAPy | -19.9769 | -19.9769 | 0 | 0.1699 | yes |  |
| st | effect | cost | 68177.9 | 68177.9 | 0 | 113.0634 | yes |  |
| st | effect | crRel | 2408.8 | 2408.8 | 1.728e-11 | 29.1237 | yes |  |
| st | effect | drHit | -15.2591 | -15.2591 | 0 | 0.7896 | yes |  |
| st | effect | emUrate | 0 | 0 | 0 | 0 | yes |  |
| st | effect | endoAnn | 0.001829 | 0.001829 | 4.337e-19 | 1.953e-05 | yes |  |
| st | effect | epPY | -0.2075 | -0.2075 | 0 | 0.00211 | yes |  |
| st | effect | fgt0PY | -40.1276 | -40.1276 | 0 | 0.2527 | yes |  |
| st | effect | fgt2PY | -11.5075 | -11.5075 | 0 | 0.0913 | yes |  |
| st | effect | finGapSh | 0.1146 | 0.1146 | -1.388e-17 | 0.0007258 | yes |  |
| st | effect | giniD | -0.01428 | -0.01428 | 1.735e-17 | 0.0005832 | yes |  |
| st | effect | giniX | -0.02978 | -0.02978 | 1.735e-17 | 0.001193 | yes |  |
| st | effect | hrs | 0.07301 | 0.07301 | 6.939e-17 | 0.02359 | yes |  |
| st | effect | jnP19 | 100.0000 | 100.0000 | 0 | 0 | yes |  |
| st | effect | lfShare | 0 | 0 | 0 | 0 | yes |  |
| st | effect | medWealthReal | 169085.4 | 169085.4 | 2.91e-11 | 1779.1 | yes |  |
| st | effect | pLev20 | 0.05148 | 0.05148 | 0 | 0.0005588 | yes |  |
| st | effect | pov | -25.0140 | -25.0140 | 0 | 0.2293 | yes |  |
| st | effect | snAll | -829.1172 | -829.1172 | -1.137e-13 | 11.5501 | yes |  |
| st | effect | tauMean | 0.02429 | 0.02429 | -3.469e-18 | 0.000244 | yes |  |
| st | effect | wtF0E | -47.4724 | -47.4724 | 0 | 0.4156 | yes |  |
| st | effect | wtGnE | -0.09639 | -0.09639 | -1.388e-17 | 0.001755 | yes |  |
| st | effect | wtPovE | -25.4641 | -25.4641 | 0 | 0.2323 | yes |  |
| st | effect | y0BN | -13.1624 | -13.1624 | 0 | 0.1593 | yes |  |
| st | effect | y0BO | -14.6296 | -14.6296 | 0 | 0.1653 | yes |  |
| st | effect | y0Ep | -0.08413 | -0.08413 | 0 | 0.001469 | yes |  |
| st | effect | y0F0 | -18.6832 | -18.6832 | 0 | 0.2935 | yes |  |
| st | effect | y0Fpl | 3.7112 | 3.7112 | 0 | 0.1082 | yes |  |
| st | effect | y0GiniW | -9.174e-05 | -9.174e-05 | -4.472e-19 | 3.846e-06 | yes |  |
| st | effect | y0Pov | -1.5140 | -1.5140 | 0 | 0.08372 | yes |  |
