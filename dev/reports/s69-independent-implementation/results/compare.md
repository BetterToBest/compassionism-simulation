## Summary

| Environment | Run | Keys | Keys exact in all 500 seeds | Keys failing the 2-SE test | Keys missing | Seconds | Seeds that failed to run |
|---|---|---|---|---|---|---|---|
| ref | base | 958 | 948 | 0 | 0 | 217.4 | 0 |
| ref | main | 990 | 687 | 0 | 0 | 281.9 | 0 |
| adv | base | 958 | 948 | 0 | 0 | 212.6 | 0 |
| adv | main | 990 | 677 | 0 | 0 | 281.8 | 0 |
| st | base | 958 | 948 | 0 | 0 | 209.1 | 0 |
| st | main | 990 | 694 | 0 | 0 | 284.4 | 0 |

| Environment | Effect keys compared (main row minus no programme) | Failing the 2-SE test |
|---|---|---|
| ref | 958 | 0 |
| adv | 958 | 0 |
| st | 958 | 0 |

## Keys not exact in every seed

Why: "zero earnings" = every such seed has an adult-year whose earnings are zero in exact arithmetic, so rounding decides whether it was worked (GAPS.md item 22); "ties" = a weighted distribution measure whose order of near-tied adults at the borrowing limit is set by rounding (item 24); "not explained" = neither.

| Environment | Run | Key | Seeds not exact | Of them, seeds with a zero-earnings adult-year | Why | First seeds |
|---|---|---|---|---|---|---|
| ref | base | dmDmS | 4 | 0 | ties | 153, 158, 201, 315 |
| ref | base | dmMob00 | 37 | 0 | ties | 5, 8, 21, 46, 80 |
| ref | base | dmMob01 | 37 | 0 | ties | 5, 8, 21, 46, 80 |
| ref | base | dmMob10 | 37 | 0 | ties | 5, 8, 13, 21, 46 |
| ref | base | dmMob11 | 37 | 0 | ties | 5, 8, 13, 21, 46 |
| ref | base | dmMob20 | 7 | 0 | ties | 13, 207, 271, 313, 337 |
| ref | base | dmMob21 | 7 | 0 | ties | 13, 207, 271, 313, 337 |
| ref | base | dmWp10E | 5 | 0 | ties | 59, 200, 213, 251, 347 |
| ref | base | dmWp10S | 1 | 0 | ties | 12 |
| ref | base | dmWp20E | 1 | 0 | ties | 353 |
| ref | main | E | 1 | 1 | zero earnings | 246 |
| ref | main | E0 | 1 | 1 | zero earnings | 246 |
| ref | main | Er | 1 | 1 | zero earnings | 246 |
| ref | main | bNAMd | 1 | 1 | zero earnings | 246 |
| ref | main | bNNMd | 1 | 1 | zero earnings | 246 |
| ref | main | bNPMd | 1 | 1 | zero earnings | 246 |
| ref | main | bOAMd | 1 | 1 | zero earnings | 246 |
| ref | main | bONMd | 1 | 1 | zero earnings | 246 |
| ref | main | bOPMd | 1 | 1 | zero earnings | 246 |
| ref | main | bXAMd | 1 | 1 | zero earnings | 246 |
| ref | main | bXNMd | 1 | 1 | zero earnings | 246 |
| ref | main | bXPMd | 1 | 1 | zero earnings | 246 |
| ref | main | bgO | 1 | 1 | zero earnings | 246 |
| ref | main | bgOP10 | 1 | 1 | zero earnings | 246 |
| ref | main | bgOP50 | 1 | 1 | zero earnings | 246 |
| ref | main | bgOP90 | 1 | 1 | zero earnings | 246 |
| ref | main | bkPY | 1 | 1 | zero earnings | 246 |
| ref | main | bzPay | 1 | 1 | zero earnings | 246 |
| ref | main | cBU | 1 | 1 | zero earnings | 246 |
| ref | main | cConv | 1 | 1 | zero earnings | 246 |
| ref | main | cPth | 1 | 1 | zero earnings | 246 |
| ref | main | cost | 1 | 1 | zero earnings | 246 |
| ref | main | crBook | 1 | 1 | zero earnings | 246 |
| ref | main | crEq | 1 | 1 | zero earnings | 246 |
| ref | main | crN1 | 1 | 1 | zero earnings | 246 |
| ref | main | crN2 | 1 | 1 | zero earnings | 246 |
| ref | main | crN3 | 1 | 1 | zero earnings | 246 |
| ref | main | crN4 | 1 | 1 | zero earnings | 246 |
| ref | main | crN5 | 1 | 1 | zero earnings | 246 |
| ref | main | crNom | 1 | 1 | zero earnings | 246 |
| ref | main | crOutF | 1 | 1 | zero earnings | 246 |
| ref | main | crOutG | 1 | 1 | zero earnings | 246 |
| ref | main | crOutH | 1 | 1 | zero earnings | 246 |
| ref | main | crR1 | 1 | 1 | zero earnings | 246 |
| ref | main | crR2 | 1 | 1 | zero earnings | 246 |
| ref | main | crR3 | 1 | 1 | zero earnings | 246 |
| ref | main | crR4 | 1 | 1 | zero earnings | 246 |
| ref | main | crR5 | 1 | 1 | zero earnings | 246 |
| ref | main | crRel | 1 | 1 | zero earnings | 246 |
| ref | main | crT1 | 1 | 1 | zero earnings | 246 |
| ref | main | dE | 1 | 1 | zero earnings | 246 |
| ref | main | dmDiE | 1 | 1 | zero earnings | 246 |
| ref | main | dmDmE | 1 | 1 | zero earnings | 246 |
| ref | main | dmLcE | 1 | 1 | zero earnings | 246 |
| ref | main | dmLcPY | 1 | 1 | zero earnings | 246 |
| ref | main | dmLsE | 1 | 1 | zero earnings | 246 |
| ref | main | dmLsPY | 1 | 1 | zero earnings | 246 |
| ref | main | dmWb50E | 1 | 1 | zero earnings | 246 |
| ref | main | dmWp10E | 1 | 1 | zero earnings | 246 |
| ref | main | dmWp15E | 1 | 1 | zero earnings | 246 |
| ref | main | dmWp1E | 1 | 1 | zero earnings | 246 |
| ref | main | dmWp20E | 1 | 1 | zero earnings | 246 |
| ref | main | dmWp25E | 1 | 1 | zero earnings | 246 |
| ref | main | dmWp30E | 1 | 1 | zero earnings | 246 |
| ref | main | dmWp40E | 1 | 1 | zero earnings | 246 |
| ref | main | dmWp45E | 1 | 1 | zero earnings | 246 |
| ref | main | dmWp50E | 1 | 1 | zero earnings | 246 |
| ref | main | dmWp55E | 1 | 1 | zero earnings | 246 |
| ref | main | dmWp5E | 1 | 1 | zero earnings | 246 |
| ref | main | dmWp60E | 1 | 1 | zero earnings | 246 |
| ref | main | dmWp65E | 1 | 1 | zero earnings | 246 |
| ref | main | dmWp70E | 1 | 1 | zero earnings | 246 |
| ref | main | dmWp75E | 1 | 1 | zero earnings | 246 |
| ref | main | dmWp80E | 1 | 1 | zero earnings | 246 |
| ref | main | dmWp85E | 1 | 1 | zero earnings | 246 |
| ref | main | dmWp90E | 1 | 1 | zero earnings | 246 |
| ref | main | dmWp95E | 1 | 1 | zero earnings | 246 |
| ref | main | dmWp99E | 1 | 1 | zero earnings | 246 |
| ref | main | dmWrE | 1 | 1 | zero earnings | 246 |
| ref | main | dmWt10E | 1 | 1 | zero earnings | 246 |
| ref | main | dmWt1E | 1 | 1 | zero earnings | 246 |
| ref | main | dmYb50E | 1 | 1 | zero earnings | 246 |
| ref | main | dmYp10E | 1 | 1 | zero earnings | 246 |
| ref | main | dmYp15E | 1 | 1 | zero earnings | 246 |
| ref | main | dmYp1E | 1 | 1 | zero earnings | 246 |
| ref | main | dmYp20E | 1 | 1 | zero earnings | 246 |
| ref | main | dmYp25E | 1 | 1 | zero earnings | 246 |
| ref | main | dmYp30E | 1 | 1 | zero earnings | 246 |
| ref | main | dmYp35E | 1 | 1 | zero earnings | 246 |
| ref | main | dmYp40E | 1 | 1 | zero earnings | 246 |
| ref | main | dmYp45E | 1 | 1 | zero earnings | 246 |
| ref | main | dmYp50E | 1 | 1 | zero earnings | 246 |
| ref | main | dmYp55E | 1 | 1 | zero earnings | 246 |
| ref | main | dmYp5E | 1 | 1 | zero earnings | 246 |
| ref | main | dmYp60E | 1 | 1 | zero earnings | 246 |
| ref | main | dmYp65E | 1 | 1 | zero earnings | 246 |
| ref | main | dmYp70E | 1 | 1 | zero earnings | 246 |
| ref | main | dmYp75E | 1 | 1 | zero earnings | 246 |
| ref | main | dmYp80E | 1 | 1 | zero earnings | 246 |
| ref | main | dmYp85E | 1 | 1 | zero earnings | 246 |
| ref | main | dmYp90E | 1 | 1 | zero earnings | 246 |
| ref | main | dmYp95E | 1 | 1 | zero earnings | 246 |
| ref | main | dmYp99E | 1 | 1 | zero earnings | 246 |
| ref | main | dmYpE | 1 | 1 | zero earnings | 246 |
| ref | main | dmYt10E | 1 | 1 | zero earnings | 246 |
| ref | main | dmYt1E | 1 | 1 | zero earnings | 246 |
| ref | main | drCut | 1 | 1 | zero earnings | 246 |
| ref | main | eGiniD | 1 | 1 | zero earnings | 246 |
| ref | main | eGiniX | 1 | 1 | zero earnings | 246 |
| ref | main | emUI | 1 | 1 | zero earnings | 246 |
| ref | main | emp | 43 | 43 | zero earnings | 1, 3, 16, 18, 29 |
| ref | main | endoAnn | 1 | 1 | zero earnings | 246 |
| ref | main | esBUW | 1 | 1 | zero earnings | 246 |
| ref | main | esConv | 1 | 1 | zero earnings | 246 |
| ref | main | esPrem | 1 | 1 | zero earnings | 246 |
| ref | main | esPremW | 1 | 1 | zero earnings | 246 |
| ref | main | esRate | 1 | 1 | zero earnings | 246 |
| ref | main | esRet | 1 | 1 | zero earnings | 246 |
| ref | main | esShare | 1 | 1 | zero earnings | 246 |
| ref | main | fgt1 | 1 | 1 | zero earnings | 246 |
| ref | main | fgt1PY | 1 | 1 | zero earnings | 246 |
| ref | main | fgt2 | 1 | 1 | zero earnings | 246 |
| ref | main | fgt2PY | 1 | 1 | zero earnings | 246 |
| ref | main | finGap | 1 | 1 | zero earnings | 246 |
| ref | main | finGapSh | 1 | 1 | zero earnings | 246 |
| ref | main | finMatch | 1 | 1 | zero earnings | 246 |
| ref | main | finMoney | 1 | 1 | zero earnings | 246 |
| ref | main | finPay | 1 | 1 | zero earnings | 246 |
| ref | main | finSur | 1 | 1 | zero earnings | 246 |
| ref | main | finTax | 1 | 1 | zero earnings | 246 |
| ref | main | fplNomPY | 1 | 1 | zero earnings | 246 |
| ref | main | gLowRes | 1 | 1 | zero earnings | 246 |
| ref | main | gNonF2 | 1 | 1 | zero earnings | 246 |
| ref | main | gNonRes | 1 | 1 | zero earnings | 246 |
| ref | main | gPartF2 | 1 | 1 | zero earnings | 246 |
| ref | main | gPartRes | 1 | 1 | zero earnings | 246 |
| ref | main | gPthRes | 1 | 1 | zero earnings | 246 |
| ref | main | gTopRes | 1 | 1 | zero earnings | 246 |
| ref | main | giniD | 1 | 1 | zero earnings | 246 |
| ref | main | giniX | 1 | 1 | zero earnings | 246 |
| ref | main | gvDef | 1 | 1 | zero earnings | 246 |
| ref | main | gvEr | 1 | 1 | zero earnings | 246 |
| ref | main | gvErM | 1 | 1 | zero earnings | 246 |
| ref | main | gvShR | 1 | 1 | zero earnings | 246 |
| ref | main | gvSur | 1 | 1 | zero earnings | 246 |
| ref | main | gvTax | 1 | 1 | zero earnings | 246 |
| ref | main | gvUnp | 1 | 1 | zero earnings | 246 |
| ref | main | hhGiniEq | 1 | 1 | zero earnings | 246 |
| ref | main | hhMedEq | 1 | 1 | zero earnings | 246 |
| ref | main | hrs | 1 | 1 | zero earnings | 246 |
| ref | main | lfPart | 44 | 44 | zero earnings | 1, 3, 16, 18, 29 |
| ref | main | lpE | 1 | 1 | zero earnings | 246 |
| ref | main | medWealthReal | 1 | 1 | zero earnings | 246 |
| ref | main | mfBU | 1 | 1 | zero earnings | 246 |
| ref | main | mfCvG | 1 | 1 | zero earnings | 246 |
| ref | main | mfCvN | 1 | 1 | zero earnings | 246 |
| ref | main | mfM | 1 | 1 | zero earnings | 246 |
| ref | main | mfPay | 1 | 1 | zero earnings | 246 |
| ref | main | mfPth | 1 | 1 | zero earnings | 246 |
| ref | main | mfTax | 1 | 1 | zero earnings | 246 |
| ref | main | mfTaxSh | 1 | 1 | zero earnings | 246 |
| ref | main | mfU | 1 | 1 | zero earnings | 246 |
| ref | main | mfUY | 1 | 1 | zero earnings | 246 |
| ref | main | mfY | 1 | 1 | zero earnings | 246 |
| ref | main | pLev10 | 1 | 1 | zero earnings | 246 |
| ref | main | pLev20 | 1 | 1 | zero earnings | 246 |
| ref | main | payPart | 1 | 1 | zero earnings | 246 |
| ref | main | pbAprC | 1 | 1 | zero earnings | 246 |
| ref | main | pbAprP | 1 | 1 | zero earnings | 246 |
| ref | main | pbCE | 1 | 1 | zero earnings | 246 |
| ref | main | pbCash | 1 | 1 | zero earnings | 246 |
| ref | main | pbD | 1 | 1 | zero earnings | 246 |
| ref | main | pbME | 1 | 1 | zero earnings | 246 |
| ref | main | pbuR_11 | 1 | 1 | zero earnings | 246 |
| ref | main | pbuR_13 | 1 | 1 | zero earnings | 246 |
| ref | main | pbuR_7 | 1 | 1 | zero earnings | 246 |
| ref | main | pbuR_8 | 1 | 1 | zero earnings | 246 |
| ref | main | pbuR_9 | 1 | 1 | zero earnings | 246 |
| ref | main | pdMatch | 1 | 1 | zero earnings | 246 |
| ref | main | pjBU | 1 | 1 | zero earnings | 246 |
| ref | main | pjExp | 1 | 1 | zero earnings | 246 |
| ref | main | pjHrs | 1 | 1 | zero earnings | 246 |
| ref | main | pjNet | 1 | 1 | zero earnings | 246 |
| ref | main | plv_10 | 1 | 1 | zero earnings | 246 |
| ref | main | plv_11 | 1 | 1 | zero earnings | 246 |
| ref | main | plv_12 | 1 | 1 | zero earnings | 246 |
| ref | main | plv_13 | 1 | 1 | zero earnings | 246 |
| ref | main | plv_14 | 1 | 1 | zero earnings | 246 |
| ref | main | plv_15 | 1 | 1 | zero earnings | 246 |
| ref | main | plv_16 | 1 | 1 | zero earnings | 246 |
| ref | main | plv_17 | 1 | 1 | zero earnings | 246 |
| ref | main | plv_18 | 1 | 1 | zero earnings | 246 |
| ref | main | plv_19 | 1 | 1 | zero earnings | 246 |
| ref | main | plv_6 | 1 | 1 | zero earnings | 246 |
| ref | main | plv_7 | 1 | 1 | zero earnings | 246 |
| ref | main | plv_8 | 1 | 1 | zero earnings | 246 |
| ref | main | plv_9 | 1 | 1 | zero earnings | 246 |
| ref | main | pmedW_10 | 1 | 1 | zero earnings | 246 |
| ref | main | pmedW_11 | 1 | 1 | zero earnings | 246 |
| ref | main | pmedW_12 | 1 | 1 | zero earnings | 246 |
| ref | main | pmedW_13 | 1 | 1 | zero earnings | 246 |
| ref | main | pmedW_14 | 1 | 1 | zero earnings | 246 |
| ref | main | pmedW_15 | 1 | 1 | zero earnings | 246 |
| ref | main | pmedW_16 | 1 | 1 | zero earnings | 246 |
| ref | main | pmedW_17 | 1 | 1 | zero earnings | 246 |
| ref | main | pmedW_18 | 1 | 1 | zero earnings | 246 |
| ref | main | pmedW_19 | 1 | 1 | zero earnings | 246 |
| ref | main | pmedW_6 | 1 | 1 | zero earnings | 246 |
| ref | main | pmedW_7 | 1 | 1 | zero earnings | 246 |
| ref | main | pmedW_8 | 1 | 1 | zero earnings | 246 |
| ref | main | pmedW_9 | 1 | 1 | zero earnings | 246 |
| ref | main | poSubSh | 1 | 1 | zero earnings | 246 |
| ref | main | prRat | 1 | 1 | zero earnings | 246 |
| ref | main | prRatE | 1 | 1 | zero earnings | 246 |
| ref | main | prSh | 1 | 1 | zero earnings | 246 |
| ref | main | prWsh | 1 | 1 | zero earnings | 246 |
| ref | main | prX | 1 | 1 | zero earnings | 246 |
| ref | main | prXE | 1 | 1 | zero earnings | 246 |
| ref | main | pwageR_1 | 1 | 1 | zero earnings | 350 |
| ref | main | pwageR_10 | 4 | 4 | zero earnings | 246, 254, 296, 386 |
| ref | main | pwageR_11 | 4 | 4 | zero earnings | 40, 130, 246, 497 |
| ref | main | pwageR_12 | 7 | 7 | zero earnings | 3, 209, 246, 254, 280 |
| ref | main | pwageR_13 | 4 | 4 | zero earnings | 40, 246, 356, 358 |
| ref | main | pwageR_14 | 9 | 9 | zero earnings | 16, 76, 204, 209, 246 |
| ref | main | pwageR_15 | 5 | 5 | zero earnings | 29, 139, 246, 350, 477 |
| ref | main | pwageR_16 | 5 | 5 | zero earnings | 85, 109, 233, 246, 295 |
| ref | main | pwageR_17 | 4 | 4 | zero earnings | 109, 172, 246, 356 |
| ref | main | pwageR_18 | 5 | 5 | zero earnings | 1, 151, 246, 378, 441 |
| ref | main | pwageR_19 | 3 | 3 | zero earnings | 96, 216, 246 |
| ref | main | pwageR_2 | 3 | 3 | zero earnings | 53, 84, 446 |
| ref | main | pwageR_3 | 3 | 3 | zero earnings | 222, 274, 494 |
| ref | main | pwageR_4 | 2 | 2 | zero earnings | 246, 319 |
| ref | main | pwageR_5 | 5 | 5 | zero earnings | 18, 246, 386, 494, 499 |
| ref | main | pwageR_6 | 4 | 4 | zero earnings | 73, 246, 293, 379 |
| ref | main | pwageR_7 | 3 | 3 | zero earnings | 202, 246, 382 |
| ref | main | pwageR_8 | 2 | 2 | zero earnings | 18, 246 |
| ref | main | pwageR_9 | 2 | 2 | zero earnings | 246, 381 |
| ref | main | rkDdB | 1 | 1 | zero earnings | 246 |
| ref | main | rkEv | 1 | 1 | zero earnings | 246 |
| ref | main | rkRec1 | 1 | 1 | zero earnings | 246 |
| ref | main | rkRec3 | 1 | 1 | zero earnings | 246 |
| ref | main | rkRec5 | 1 | 1 | zero earnings | 246 |
| ref | main | rkRecB3 | 1 | 1 | zero earnings | 246 |
| ref | main | rkRecM | 1 | 1 | zero earnings | 246 |
| ref | main | rtDfE | 1 | 1 | zero earnings | 246 |
| ref | main | rtDvE | 1 | 1 | zero earnings | 246 |
| ref | main | rtE | 1 | 1 | zero earnings | 246 |
| ref | main | rtE1 | 1 | 1 | zero earnings | 246 |
| ref | main | rtE2 | 1 | 1 | zero earnings | 246 |
| ref | main | rtE3 | 1 | 1 | zero earnings | 246 |
| ref | main | rtE4 | 1 | 1 | zero earnings | 246 |
| ref | main | rtE5 | 1 | 1 | zero earnings | 246 |
| ref | main | rtGt1E | 1 | 1 | zero earnings | 246 |
| ref | main | rtNE | 1 | 1 | zero earnings | 246 |
| ref | main | rtRE | 1 | 1 | zero earnings | 246 |
| ref | main | rtS | 1 | 1 | zero earnings | 246 |
| ref | main | rtS1 | 1 | 1 | zero earnings | 246 |
| ref | main | rtS2 | 1 | 1 | zero earnings | 246 |
| ref | main | rtS3 | 1 | 1 | zero earnings | 246 |
| ref | main | rtS4 | 1 | 1 | zero earnings | 246 |
| ref | main | rtS5 | 1 | 1 | zero earnings | 246 |
| ref | main | rtV | 1 | 1 | zero earnings | 246 |
| ref | main | rtV1 | 1 | 1 | zero earnings | 246 |
| ref | main | rtV3 | 1 | 1 | zero earnings | 246 |
| ref | main | rtV4 | 1 | 1 | zero earnings | 246 |
| ref | main | rtV5 | 1 | 1 | zero earnings | 246 |
| ref | main | rtYbE | 1 | 1 | zero earnings | 246 |
| ref | main | rtYkE | 1 | 1 | zero earnings | 246 |
| ref | main | rtYkShE | 1 | 1 | zero earnings | 246 |
| ref | main | snAbM | 1 | 1 | zero earnings | 246 |
| ref | main | snAll | 1 | 1 | zero earnings | 246 |
| ref | main | snCtcM | 1 | 1 | zero earnings | 246 |
| ref | main | snEitc | 8 | 8 | zero earnings | 1, 16, 76, 222, 296 |
| ref | main | snEitcM | 1 | 1 | zero earnings | 246 |
| ref | main | snMtr | 1 | 1 | zero earnings | 246 |
| ref | main | snSnapM | 1 | 1 | zero earnings | 246 |
| ref | main | spCap | 1 | 1 | zero earnings | 246 |
| ref | main | spCash | 1 | 1 | zero earnings | 246 |
| ref | main | spCut | 1 | 1 | zero earnings | 246 |
| ref | main | spD1 | 1 | 1 | zero earnings | 246 |
| ref | main | spD2 | 1 | 1 | zero earnings | 246 |
| ref | main | spFreed | 1 | 1 | zero earnings | 246 |
| ref | main | spPool | 1 | 1 | zero earnings | 246 |
| ref | main | spProfW | 1 | 1 | zero earnings | 246 |
| ref | main | spProfit | 1 | 1 | zero earnings | 246 |
| ref | main | spPtfS | 1 | 1 | zero earnings | 246 |
| ref | main | spReinv | 1 | 1 | zero earnings | 246 |
| ref | main | srcCover | 1 | 1 | zero earnings | 246 |
| ref | main | srcM | 1 | 1 | zero earnings | 246 |
| ref | main | srcPay | 1 | 1 | zero earnings | 246 |
| ref | main | srcTax | 1 | 1 | zero earnings | 246 |
| ref | main | tauLast | 1 | 1 | zero earnings | 246 |
| ref | main | tauMean | 1 | 1 | zero earnings | 246 |
| ref | main | tax | 1 | 1 | zero earnings | 246 |
| ref | main | taxAvg | 1 | 1 | zero earnings | 246 |
| ref | main | tgt | 1 | 1 | zero earnings | 246 |
| ref | main | treas | 1 | 1 | zero earnings | 246 |
| ref | main | wtB50E | 1 | 1 | zero earnings | 246 |
| ref | main | wtGnE | 1 | 1 | zero earnings | 246 |
| ref | main | wtGzE | 1 | 1 | zero earnings | 246 |
| ref | main | wtMeanE | 1 | 1 | zero earnings | 246 |
| ref | main | wtMedE | 1 | 1 | zero earnings | 246 |
| ref | main | wtP999E | 1 | 1 | zero earnings | 246 |
| ref | main | wtT01E | 1 | 1 | zero earnings | 246 |
| ref | main | wtT10E | 1 | 1 | zero earnings | 246 |
| ref | main | wtT1E | 1 | 1 | zero earnings | 246 |
| ref | main | wyF1PY | 1 | 1 | zero earnings | 246 |
| ref | main | wyF2PY | 1 | 1 | zero earnings | 246 |
| ref | main | y7GiniD | 1 | 1 | zero earnings | 246 |
| ref | main | y7GiniW | 1 | 1 | zero earnings | 246 |
| ref | main | y7GiniWN | 1 | 1 | zero earnings | 246 |
| ref | main | y7GiniX | 1 | 1 | zero earnings | 246 |
| ref | main | zero | 43 | 43 | zero earnings | 1, 3, 16, 18, 29 |
| adv | base | dmDmS | 4 | 0 | ties | 153, 158, 201, 315 |
| adv | base | dmMob00 | 400 | 0 | ties | 2, 3, 5, 6, 7 |
| adv | base | dmMob01 | 400 | 0 | ties | 2, 3, 5, 6, 7 |
| adv | base | dmMob10 | 380 | 0 | ties | 2, 3, 5, 6, 7 |
| adv | base | dmMob11 | 380 | 0 | ties | 2, 3, 5, 6, 7 |
| adv | base | dmMob20 | 203 | 0 | ties | 2, 7, 9, 13, 16 |
| adv | base | dmMob21 | 203 | 0 | ties | 2, 7, 9, 13, 16 |
| adv | base | dmWp10E | 5 | 0 | ties | 4, 158, 252, 364, 412 |
| adv | base | dmWp10S | 1 | 0 | ties | 12 |
| adv | base | dmWp25E | 1 | 0 | ties | 285 |
| adv | main | E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | E0 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | Er | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | bNAMd | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | bNNMd | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | bNPMd | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | bOAMd | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | bONMd | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | bOPMd | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | bXAMd | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | bXNMd | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | bXPMd | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | bgO | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | bgOP10 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | bgOP50 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | bgOP90 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | bkPY | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | bzPay | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | c22R | 1 | 1 | zero earnings | 109 |
| adv | main | cBU | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | cConv | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | cCut | 2 | 2 | zero earnings | 50, 109 |
| adv | main | cPth | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | cost | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | crBook | 1 | 1 | zero earnings | 211 |
| adv | main | crEq | 1 | 1 | zero earnings | 211 |
| adv | main | crN1 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | crN2 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | crN3 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | crN4 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | crN5 | 2 | 2 | zero earnings | 109, 211 |
| adv | main | crNom | 1 | 1 | zero earnings | 211 |
| adv | main | crOutF | 1 | 1 | zero earnings | 211 |
| adv | main | crOutG | 1 | 1 | zero earnings | 211 |
| adv | main | crOutH | 1 | 1 | zero earnings | 211 |
| adv | main | crR1 | 1 | 1 | zero earnings | 211 |
| adv | main | crR2 | 1 | 1 | zero earnings | 211 |
| adv | main | crR3 | 1 | 1 | zero earnings | 211 |
| adv | main | crR4 | 1 | 1 | zero earnings | 211 |
| adv | main | crR5 | 1 | 1 | zero earnings | 211 |
| adv | main | crRel | 1 | 1 | zero earnings | 211 |
| adv | main | crT1 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | csFree | 2 | 2 | zero earnings | 50, 109 |
| adv | main | dE | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmDiE | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmDmE | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmLcE | 2 | 2 | zero earnings | 50, 211 |
| adv | main | dmLcPY | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmLsE | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmLsPY | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmWb50E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmWp10E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmWp15E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmWp1E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmWp20E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmWp25E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmWp30E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmWp35E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmWp40E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmWp45E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmWp50E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmWp55E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmWp5E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmWp60E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmWp65E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmWp70E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmWp75E | 2 | 2 | zero earnings | 50, 211 |
| adv | main | dmWp80E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmWp85E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmWp90E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmWp95E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmWp99E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmWrE | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmWt10E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmWt1E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmYb50E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmYp10E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmYp15E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmYp1E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmYp20E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmYp25E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmYp30E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmYp35E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmYp40E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmYp45E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmYp50E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmYp55E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmYp5E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmYp60E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmYp65E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmYp70E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmYp75E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmYp80E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmYp85E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmYp90E | 2 | 2 | zero earnings | 109, 211 |
| adv | main | dmYp95E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmYp99E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmYpE | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmYt10E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | dmYt1E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | drCut | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | eGiniD | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | eGiniW | 1 | 1 | zero earnings | 109 |
| adv | main | eGiniWN | 1 | 1 | zero earnings | 109 |
| adv | main | eGiniX | 2 | 2 | zero earnings | 50, 211 |
| adv | main | emUI | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | emp | 127 | 127 | zero earnings | 1, 8, 15, 16, 17 |
| adv | main | endoAnn | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | esBUW | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | esConv | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | esPrem | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | esPremW | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | esRate | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | esRet | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | esShare | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | fgt1 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | fgt1PY | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | fgt2 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | fgt2PY | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | finGap | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | finGapSh | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | finMatch | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | finMoney | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | finPay | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | finSur | 2 | 2 | zero earnings | 50, 109 |
| adv | main | finTax | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | gLowRes | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | gNonF2 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | gNonRes | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | gPartF2 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | gPartRes | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | gPthRes | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | gTopRes | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | giniD | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | giniX | 2 | 2 | zero earnings | 50, 211 |
| adv | main | gvDef | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | gvEr | 1 | 1 | zero earnings | 211 |
| adv | main | gvErM | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | gvPay | 2 | 2 | zero earnings | 50, 109 |
| adv | main | gvShR | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | gvSur | 2 | 2 | zero earnings | 50, 109 |
| adv | main | gvTax | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | gvUnp | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | hhGiniEq | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | hhMedEq | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | hrs | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | lfPart | 135 | 135 | zero earnings | 1, 8, 15, 16, 17 |
| adv | main | lpE | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | medWealthReal | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | mfBU | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | mfCut | 2 | 2 | zero earnings | 50, 109 |
| adv | main | mfCvG | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | mfCvN | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | mfIss | 2 | 2 | zero earnings | 50, 109 |
| adv | main | mfM | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | mfPay | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | mfPth | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | mfTax | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | mfTaxSh | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | mfU | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | mfUY | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | mfY | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | need | 2 | 2 | zero earnings | 50, 109 |
| adv | main | pLev10 | 2 | 2 | zero earnings | 50, 211 |
| adv | main | pLev20 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | payPart | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | pbAprC | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | pbAprP | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | pbCE | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | pbCash | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | pbD | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | pbME | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | pbuR_10 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | pbuR_11 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | pbuR_12 | 2 | 2 | zero earnings | 109, 211 |
| adv | main | pbuR_13 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | pbuR_14 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | pbuR_15 | 2 | 2 | zero earnings | 109, 211 |
| adv | main | pbuR_16 | 2 | 2 | zero earnings | 109, 211 |
| adv | main | pbuR_17 | 1 | 1 | zero earnings | 211 |
| adv | main | pbuR_18 | 2 | 2 | zero earnings | 109, 211 |
| adv | main | pbuR_19 | 1 | 1 | zero earnings | 211 |
| adv | main | pbuR_7 | 1 | 1 | zero earnings | 50 |
| adv | main | pbuR_8 | 1 | 1 | zero earnings | 50 |
| adv | main | pbuR_9 | 1 | 1 | zero earnings | 50 |
| adv | main | pdMatch | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | pfCut | 2 | 2 | zero earnings | 50, 109 |
| adv | main | pjBU | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | pjExp | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | pjHrs | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | pjNet | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | plv_10 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | plv_11 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | plv_12 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | plv_13 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | plv_14 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | plv_15 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | plv_16 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | plv_17 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | plv_18 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | plv_19 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | plv_7 | 1 | 1 | zero earnings | 50 |
| adv | main | plv_8 | 1 | 1 | zero earnings | 50 |
| adv | main | plv_9 | 2 | 2 | zero earnings | 50, 211 |
| adv | main | pmedW_10 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | pmedW_11 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | pmedW_12 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | pmedW_13 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | pmedW_14 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | pmedW_15 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | pmedW_16 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | pmedW_17 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | pmedW_18 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | pmedW_19 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | pmedW_7 | 1 | 1 | zero earnings | 50 |
| adv | main | pmedW_8 | 1 | 1 | zero earnings | 50 |
| adv | main | pmedW_9 | 2 | 2 | zero earnings | 50, 211 |
| adv | main | poFree | 2 | 2 | zero earnings | 50, 109 |
| adv | main | poSub | 2 | 2 | zero earnings | 50, 109 |
| adv | main | poSubSh | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | prRat | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | prRatE | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | prSh | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | prWsh | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | prX | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | prXE | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | pwageR_1 | 1 | 1 | zero earnings | 281 |
| adv | main | pwageR_10 | 11 | 11 | zero earnings | 50, 109, 123, 180, 211 |
| adv | main | pwageR_11 | 18 | 18 | zero earnings | 43, 50, 74, 83, 109 |
| adv | main | pwageR_12 | 15 | 15 | zero earnings | 3, 17, 40, 50, 109 |
| adv | main | pwageR_13 | 17 | 17 | zero earnings | 41, 50, 75, 76, 80 |
| adv | main | pwageR_14 | 24 | 24 | zero earnings | 15, 27, 40, 50, 109 |
| adv | main | pwageR_15 | 22 | 22 | zero earnings | 28, 43, 50, 53, 56 |
| adv | main | pwageR_16 | 15 | 15 | zero earnings | 1, 3, 30, 40, 50 |
| adv | main | pwageR_17 | 31 | 31 | zero earnings | 16, 17, 31, 50, 56 |
| adv | main | pwageR_18 | 27 | 27 | zero earnings | 17, 25, 27, 40, 45 |
| adv | main | pwageR_19 | 25 | 25 | zero earnings | 8, 40, 45, 50, 80 |
| adv | main | pwageR_2 | 2 | 2 | zero earnings | 73, 161 |
| adv | main | pwageR_3 | 4 | 4 | zero earnings | 161, 274, 293, 377 |
| adv | main | pwageR_4 | 3 | 3 | zero earnings | 83, 200, 350 |
| adv | main | pwageR_5 | 3 | 3 | zero earnings | 50, 231, 494 |
| adv | main | pwageR_6 | 11 | 11 | zero earnings | 83, 84, 114, 161, 230 |
| adv | main | pwageR_7 | 5 | 5 | zero earnings | 50, 143, 161, 211, 352 |
| adv | main | pwageR_8 | 5 | 5 | zero earnings | 50, 109, 280, 370, 497 |
| adv | main | pwageR_9 | 12 | 12 | zero earnings | 50, 73, 75, 83, 84 |
| adv | main | rkDdB | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | rkDdW | 1 | 1 | zero earnings | 50 |
| adv | main | rkRec1 | 1 | 1 | zero earnings | 50 |
| adv | main | rkRecM | 1 | 1 | zero earnings | 50 |
| adv | main | rtDfE | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | rtDvE | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | rtE | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | rtE1 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | rtE2 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | rtE3 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | rtE4 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | rtE5 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | rtNE | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | rtS | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | rtS1 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | rtS2 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | rtS3 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | rtS4 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | rtS5 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | rtYbE | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | rtYkE | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | rtYkShE | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | snAbM | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | snAll | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | snCtcM | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | snEitc | 40 | 40 | zero earnings | 16, 64, 74, 75, 76 |
| adv | main | snEitcM | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | snKids | 1 | 1 | zero earnings | 392 |
| adv | main | snMtr | 8 | 8 | zero earnings | 50, 83, 109, 126, 211 |
| adv | main | snSnapM | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | spCap | 1 | 1 | zero earnings | 50 |
| adv | main | spCash | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | spCut | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | spD1 | 1 | 1 | zero earnings | 50 |
| adv | main | spD2 | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | spFreed | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | spPool | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | spProfW | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | spProfit | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | spPtfS | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | spReinv | 1 | 1 | zero earnings | 50 |
| adv | main | srcCover | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | srcIss | 2 | 2 | zero earnings | 50, 109 |
| adv | main | srcM | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | srcPay | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | srcTax | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | tauLast | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | tauMean | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | tax | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | taxAvg | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | tgt | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | treas | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | wtB50E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | wtGnE | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | wtGzE | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | wtMeanE | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | wtMedE | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | wtP999E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | wtT01E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | wtT10E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | wtT1E | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | wyF1PY | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | wyF2PY | 3 | 3 | zero earnings | 50, 109, 211 |
| adv | main | y7GiniD | 1 | 1 | zero earnings | 50 |
| adv | main | y7GiniW | 1 | 1 | zero earnings | 50 |
| adv | main | y7GiniWN | 1 | 1 | zero earnings | 50 |
| adv | main | y7GiniX | 1 | 1 | zero earnings | 50 |
| adv | main | zero | 127 | 127 | zero earnings | 1, 8, 15, 16, 17 |
| st | base | dmDmS | 4 | 0 | ties | 153, 158, 201, 315 |
| st | base | dmMob00 | 400 | 0 | ties | 2, 3, 5, 6, 7 |
| st | base | dmMob01 | 400 | 0 | ties | 2, 3, 5, 6, 7 |
| st | base | dmMob10 | 380 | 0 | ties | 2, 3, 5, 6, 7 |
| st | base | dmMob11 | 380 | 0 | ties | 2, 3, 5, 6, 7 |
| st | base | dmMob20 | 203 | 0 | ties | 2, 7, 9, 13, 16 |
| st | base | dmMob21 | 203 | 0 | ties | 2, 7, 9, 13, 16 |
| st | base | dmWp10E | 5 | 0 | ties | 4, 158, 252, 364, 412 |
| st | base | dmWp10S | 1 | 0 | ties | 12 |
| st | base | dmWp25E | 1 | 0 | ties | 285 |
| st | main | E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | E0 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | Er | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | bNAMd | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | bNNMd | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | bNPMd | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | bOAMd | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | bONMd | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | bOPMd | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | bXAMd | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | bXNMd | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | bXPMd | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | bgO | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | bgOP10 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | bgOP50 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | bgOP90 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | bkPY | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | bzPay | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | cBU | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | cConv | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | cPth | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | cost | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | crBook | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | crEq | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | crN1 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | crN2 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | crN3 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | crN4 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | crN5 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | crNom | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | crOutF | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | crOutG | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | crOutH | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | crR1 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | crR2 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | crR3 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | crR4 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | crR5 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | crRel | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | crT1 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | csFree | 2 | 2 | zero earnings | 211, 486 |
| st | main | dE | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmDiE | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmDmE | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmLcE | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmLcPY | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmLsE | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmLsPY | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmWb50E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmWp10E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmWp15E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmWp1E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmWp20E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmWp25E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmWp30E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmWp35E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmWp40E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmWp45E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmWp50E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmWp55E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmWp5E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmWp60E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmWp65E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmWp70E | 2 | 2 | zero earnings | 306, 486 |
| st | main | dmWp75E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmWp80E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmWp85E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmWp90E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmWp95E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmWp99E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmWrE | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmWt10E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmWt1E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmYb50E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmYp10E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmYp15E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmYp1E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmYp20E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmYp25E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmYp30E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmYp35E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmYp40E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmYp45E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmYp50E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmYp55E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmYp5E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmYp60E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmYp65E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmYp70E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmYp75E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmYp80E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmYp85E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmYp90E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmYp95E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmYp99E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmYpE | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmYt10E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | dmYt1E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | drCut | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | eGiniD | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | eGiniX | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | emUI | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | emp | 131 | 131 | zero earnings | 1, 6, 7, 15, 17 |
| st | main | endoAnn | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | esBUW | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | esConv | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | esPrem | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | esPremW | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | esRate | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | esRet | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | esShare | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | fgt1 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | fgt1PY | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | fgt2 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | fgt2PY | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | finGap | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | finGapSh | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | finMatch | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | finMoney | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | finPay | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | finSur | 2 | 2 | zero earnings | 306, 486 |
| st | main | finTax | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | gLowRes | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | gNonF2 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | gNonRes | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | gPartF2 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | gPartRes | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | gPthRes | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | gTopRes | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | giniD | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | giniX | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | gvDef | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | gvEr | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | gvErM | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | gvPay | 1 | 1 | zero earnings | 486 |
| st | main | gvShR | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | gvSur | 2 | 2 | zero earnings | 306, 486 |
| st | main | gvTax | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | gvUnp | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | hhGiniEq | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | hhMedEq | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | hrs | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | lfPart | 136 | 136 | zero earnings | 1, 6, 7, 15, 17 |
| st | main | lpE | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | medWealthReal | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | mfBU | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | mfCvG | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | mfCvN | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | mfIss | 2 | 2 | zero earnings | 211, 486 |
| st | main | mfM | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | mfPay | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | mfPth | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | mfTax | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | mfTaxSh | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | mfU | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | mfUY | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | mfY | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | need | 1 | 1 | zero earnings | 486 |
| st | main | pLev10 | 1 | 1 | zero earnings | 211 |
| st | main | pLev20 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | paC10 | 1 | 1 | zero earnings | 211 |
| st | main | payPart | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pbAprC | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pbAprP | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pbCE | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pbCash | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pbD | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pbME | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pbuR_10 | 1 | 1 | zero earnings | 211 |
| st | main | pbuR_11 | 2 | 2 | zero earnings | 211, 486 |
| st | main | pbuR_12 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pbuR_13 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pbuR_14 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pbuR_15 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pbuR_16 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pbuR_17 | 2 | 2 | zero earnings | 211, 486 |
| st | main | pbuR_18 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pbuR_19 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pdC10 | 1 | 1 | zero earnings | 211 |
| st | main | pdMatch | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pfCut | 1 | 1 | zero earnings | 211 |
| st | main | pjBU | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pjExp | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pjHrs | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pjNet | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | plv_10 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | plv_11 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | plv_12 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | plv_13 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | plv_14 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | plv_15 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | plv_16 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | plv_17 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | plv_18 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | plv_19 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | plv_9 | 1 | 1 | zero earnings | 211 |
| st | main | pmedW_10 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pmedW_11 | 2 | 2 | zero earnings | 306, 486 |
| st | main | pmedW_12 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pmedW_13 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pmedW_14 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pmedW_15 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pmedW_16 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pmedW_17 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pmedW_18 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pmedW_19 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pmedW_9 | 1 | 1 | zero earnings | 211 |
| st | main | poFree | 2 | 2 | zero earnings | 211, 486 |
| st | main | poSub | 1 | 1 | zero earnings | 211 |
| st | main | poSubSh | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | prRat | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | prRatE | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | prSh | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | prWsh | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | prX | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | prXE | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | pwageR_10 | 9 | 9 | zero earnings | 1, 29, 211, 273, 306 |
| st | main | pwageR_11 | 19 | 19 | zero earnings | 43, 110, 123, 161, 211 |
| st | main | pwageR_12 | 22 | 22 | zero earnings | 40, 46, 56, 80, 110 |
| st | main | pwageR_13 | 18 | 18 | zero earnings | 16, 85, 94, 154, 161 |
| st | main | pwageR_14 | 18 | 18 | zero earnings | 56, 96, 98, 120, 122 |
| st | main | pwageR_15 | 21 | 21 | zero earnings | 1, 36, 53, 114, 122 |
| st | main | pwageR_16 | 23 | 23 | zero earnings | 6, 22, 29, 71, 119 |
| st | main | pwageR_17 | 26 | 26 | zero earnings | 7, 8, 17, 30, 40 |
| st | main | pwageR_18 | 28 | 28 | zero earnings | 6, 61, 71, 89, 192 |
| st | main | pwageR_19 | 26 | 26 | zero earnings | 55, 73, 111, 143, 147 |
| st | main | pwageR_2 | 6 | 6 | zero earnings | 8, 53, 81, 139, 378 |
| st | main | pwageR_3 | 1 | 1 | zero earnings | 420 |
| st | main | pwageR_4 | 3 | 3 | zero earnings | 15, 114, 265 |
| st | main | pwageR_5 | 7 | 7 | zero earnings | 1, 81, 103, 237, 290 |
| st | main | pwageR_6 | 9 | 9 | zero earnings | 16, 41, 189, 261, 356 |
| st | main | pwageR_7 | 6 | 6 | zero earnings | 211, 212, 281, 364, 378 |
| st | main | pwageR_8 | 7 | 7 | zero earnings | 81, 161, 254, 306, 426 |
| st | main | pwageR_9 | 13 | 13 | zero earnings | 28, 38, 73, 76, 84 |
| st | main | rkDdB | 2 | 2 | zero earnings | 211, 486 |
| st | main | rkDdW | 1 | 1 | zero earnings | 211 |
| st | main | rtDfE | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | rtDvE | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | rtE | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | rtE1 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | rtE2 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | rtE3 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | rtE4 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | rtE5 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | rtNE | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | rtS | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | rtS1 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | rtS2 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | rtS3 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | rtS4 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | rtS5 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | rtYbE | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | rtYkE | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | rtYkShE | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | snAbM | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | snAll | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | snCtcM | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | snEitc | 34 | 34 | zero earnings | 1, 7, 38, 43, 76 |
| st | main | snEitcM | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | snKids | 2 | 2 | zero earnings | 119, 481 |
| st | main | snMtr | 10 | 10 | zero earnings | 40, 119, 123, 126, 211 |
| st | main | snSnapM | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | spCap | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | spCash | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | spCut | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | spD1 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | spD2 | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | spFreed | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | spPool | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | spProfW | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | spProfit | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | spPtfS | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | spReinv | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | srcCover | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | srcIss | 2 | 2 | zero earnings | 211, 486 |
| st | main | srcM | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | srcPay | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | srcTax | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | tauLast | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | tauMean | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | tax | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | taxAvg | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | tgt | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | treas | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | wtB50E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | wtGnE | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | wtGzE | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | wtMeanE | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | wtMedE | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | wtP999E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | wtT01E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | wtT10E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | wtT1E | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | wyF1PY | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | wyF2PY | 3 | 3 | zero earnings | 211, 306, 486 |
| st | main | zero | 131 | 131 | zero earnings | 1, 6, 7, 15, 17 |

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
| ref | main | bNAPy | 0.5021 | 0.5021 | 0 | 0.02531 | yes | 500 |
| ref | main | bOAPy | 0.3456 | 0.3456 | 0 | 0.02199 | yes | 500 |
| ref | main | cost | 60425.8 | 60425.8 | 2.496e-06 | 91.0840 | yes | 499 |
| ref | main | crRel | 102635.1 | 102635.1 | 1.545e-06 | 494.7375 | yes | 499 |
| ref | main | drHit | 15.6751 | 15.6751 | 0 | 0.5652 | yes | 500 |
| ref | main | emUrate | 2.3636 | 2.3636 | 0 | 0.01693 | yes | 500 |
| ref | main | endoAnn | 0.4033 | 0.4033 | 7.319e-10 | 0.00162 | yes | 499 |
| ref | main | epPY | 0.05738 | 0.05738 | 0 | 0.0004688 | yes | 500 |
| ref | main | fgt0PY | 5.1355 | 5.1355 | 0 | 0.0729 | yes | 500 |
| ref | main | fgt2PY | 0.2319 | 0.2319 | 1.748e-10 | 0.004633 | yes | 499 |
| ref | main | finGapSh | 0.09887 | 0.09887 | -4.013e-10 | 0.00105 | yes | 499 |
| ref | main | giniD | 0.9468 | 0.9468 | 3.307e-12 | 0.002085 | yes | 499 |
| ref | main | giniX | 0.9293 | 0.9293 | 2.339e-12 | 0.002779 | yes | 499 |
| ref | main | hrs | 0.01662 | 0.01662 | -1.196e-08 | 0.01224 | yes | 499 |
| ref | main | jnP19 | 100.0000 | 100.0000 | 0 | 0 | yes | 500 |
| ref | main | lfShare | 17.3904 | 17.3904 | 0 | 0.2163 | yes | 500 |
| ref | main | medWealthReal | 316315.2 | 316315.2 | 0.0001165 | 2049.4 | yes | 499 |
| ref | main | pLev20 | 634.2635 | 634.2635 | 6.464e-06 | 14.3850 | yes | 499 |
| ref | main | paSh | 43.1488 | 43.1488 | 0 | 0.125 | yes | 500 |
| ref | main | poSub | 1306.3 | 1306.3 | 9.354e-10 | 4.4748 | yes | 500 |
| ref | main | pov | 2.2720 | 2.2720 | 0 | 0.08897 | yes | 500 |
| ref | main | snAll | 466.8106 | 466.8107 | 0.0001204 | 8.3812 | yes | 499 |
| ref | main | tauMean | 0.02987 | 0.02987 | 5.85e-11 | 0.0002465 | yes | 499 |
| ref | main | wtF0E | 1.7393 | 1.7393 | 0 | 0.07677 | yes | 500 |
| ref | main | wtGnE | 0.7364 | 0.7364 | 1.99e-11 | 0.005752 | yes | 499 |
| ref | main | wtPovE | 2.3747 | 2.3747 | 0 | 0.09176 | yes | 500 |
| ref | main | y0BN | 2.8636 | 2.8636 | 0 | 0.09314 | yes | 500 |
| ref | main | y0BO | 0.9404 | 0.9404 | 0 | 0.0537 | yes | 500 |
| ref | main | y0Ep | 0.1283 | 0.1283 | 0 | 0.001245 | yes | 500 |
| ref | main | y0F0 | 20.8348 | 20.8348 | 0 | 0.2658 | yes | 500 |
| ref | main | y0Fpl | 20.1840 | 20.1840 | 0 | 0.2332 | yes | 500 |
| ref | main | y0GiniW | 0.9878 | 0.9878 | 0 | 0.0003556 | yes | 500 |
| ref | main | y0Pov | 23.5092 | 23.5092 | 0 | 0.1713 | yes | 500 |
| ref | effect | bNAPy | -19.1140 | -19.1140 | 0 | 0.1624 | yes |  |
| ref | effect | bOAPy | -19.2705 | -19.2705 | 0 | 0.1643 | yes |  |
| ref | effect | cost | 60425.8 | 60425.8 | 2.496e-06 | 91.0840 | yes |  |
| ref | effect | crRel | 102635.1 | 102635.1 | 1.545e-06 | 494.7375 | yes |  |
| ref | effect | drHit | -31.0979 | -31.0979 | 0 | 0.6355 | yes |  |
| ref | effect | emUrate | 0 | 0 | 0 | 0 | yes |  |
| ref | effect | endoAnn | 0.4033 | 0.4033 | 7.319e-10 | 0.00162 | yes |  |
| ref | effect | epPY | -0.1991 | -0.1991 | 0 | 0.001841 | yes |  |
| ref | effect | fgt0PY | -30.9622 | -30.9622 | 0 | 0.2144 | yes |  |
| ref | effect | fgt2PY | -9.2321 | -9.2321 | 1.748e-10 | 0.07746 | yes |  |
| ref | effect | finGapSh | 0.09887 | 0.09887 | -4.013e-10 | 0.00105 | yes |  |
| ref | effect | giniD | -0.01844 | -0.01844 | 3.307e-12 | 0.0008419 | yes |  |
| ref | effect | giniX | -0.03596 | -0.03596 | 2.339e-12 | 0.001527 | yes |  |
| ref | effect | hrs | 0.03006 | 0.03006 | -1.196e-08 | 0.01223 | yes |  |
| ref | effect | jnP19 | 100.0000 | 100.0000 | 0 | 0 | yes |  |
| ref | effect | lfShare | 0 | 0 | 0 | 0 | yes |  |
| ref | effect | medWealthReal | 85046.3 | 85046.3 | 0.0001165 | 1850.8 | yes |  |
| ref | effect | pLev20 | 633.2635 | 633.2635 | 6.464e-06 | 14.3850 | yes |  |
| ref | effect | pov | -21.4696 | -21.4696 | 0 | 0.2174 | yes |  |
| ref | effect | snAll | -522.8141 | -522.8140 | 0.0001204 | 8.6987 | yes |  |
| ref | effect | tauMean | 0.02987 | 0.02987 | 5.85e-11 | 0.0002465 | yes |  |
| ref | effect | wtF0E | -31.5158 | -31.5158 | 0 | 0.3034 | yes |  |
| ref | effect | wtGnE | -0.07633 | -0.07633 | 1.99e-11 | 0.001683 | yes |  |
| ref | effect | wtPovE | -21.8900 | -21.8900 | 0 | 0.2202 | yes |  |
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
| adv | base | wtGnE | 0.8209 | 0.8209 | 1.11e-16 | 0.004075 | yes | 500 |
| adv | base | wtPovE | 27.4923 | 27.4923 | 0 | 0.2235 | yes | 500 |
| adv | base | y0BN | 15.9756 | 15.9756 | 0 | 0.1588 | yes | 500 |
| adv | base | y0BO | 15.9756 | 15.9756 | 0 | 0.1588 | yes | 500 |
| adv | base | y0Ep | 0.2245 | 0.2245 | 0 | 0.001216 | yes | 500 |
| adv | base | y0F0 | 39.7592 | 39.7592 | 0 | 0.3082 | yes | 500 |
| adv | base | y0Fpl | 16.3952 | 16.3952 | 0 | 0.2147 | yes | 500 |
| adv | base | y0GiniW | 0.9879 | 0.9879 | 0 | 0.0003521 | yes | 500 |
| adv | base | y0Pov | 25.0232 | 25.0232 | 0 | 0.1735 | yes | 500 |
| adv | main | bNAPy | 0.5567 | 0.5567 | 0 | 0.02754 | yes | 500 |
| adv | main | bOAPy | 0.3902 | 0.3902 | 0 | 0.02372 | yes | 500 |
| adv | main | cost | 57929.9 | 57929.9 | -0.0001219 | 90.2653 | yes | 497 |
| adv | main | crRel | 102747.9 | 102747.9 | -7.761e-07 | 495.4462 | yes | 499 |
| adv | main | drHit | 15.5375 | 15.5375 | 0 | 0.5513 | yes | 500 |
| adv | main | emUrate | 3.5909 | 3.5909 | 0 | 0.05746 | yes | 500 |
| adv | main | endoAnn | 0.4601 | 0.4601 | -1.031e-09 | 0.001931 | yes | 497 |
| adv | main | epPY | 0.05986 | 0.05986 | 0 | 0.0005314 | yes | 500 |
| adv | main | fgt0PY | 5.9706 | 5.9706 | 0 | 0.08448 | yes | 500 |
| adv | main | fgt2PY | 0.2527 | 0.2527 | 2.033e-08 | 0.005004 | yes | 497 |
| adv | main | finGapSh | 0.1538 | 0.1538 | -5.308e-10 | 0.00139 | yes | 497 |
| adv | main | giniD | 0.9577 | 0.9577 | -9.906e-12 | 0.001643 | yes | 497 |
| adv | main | giniX | 0.9396 | 0.9396 | -9.931e-12 | 0.002381 | yes | 498 |
| adv | main | hrs | -0.00211 | -0.00211 | -2.434e-08 | 0.01269 | yes | 497 |
| adv | main | jnP19 | 100.0000 | 100.0000 | 0 | 0 | yes | 500 |
| adv | main | lfShare | 17.3904 | 17.3904 | 0 | 0.2163 | yes | 500 |
| adv | main | medWealthReal | 288961.7 | 288961.7 | 5.374e-05 | 1942.0 | yes | 497 |
| adv | main | pLev20 | 1971.2 | 1971.2 | -2.41e-05 | 51.5300 | yes | 497 |
| adv | main | paSh | 43.0867 | 43.0867 | 0 | 0.1267 | yes | 500 |
| adv | main | poSub | 1301.8 | 1301.8 | 4.826e-07 | 4.5325 | yes | 498 |
| adv | main | pov | 4.2076 | 4.2076 | 0 | 0.1242 | yes | 500 |
| adv | main | snAll | 559.3620 | 559.3619 | -4.91e-05 | 9.7141 | yes | 497 |
| adv | main | tauMean | 0.03669 | 0.03669 | -8.728e-11 | 0.000306 | yes | 497 |
| adv | main | wtF0E | 3.1030 | 3.1030 | 0 | 0.1097 | yes | 500 |
| adv | main | wtGnE | 0.7508 | 0.7508 | 6.548e-10 | 0.005524 | yes | 497 |
| adv | main | wtPovE | 4.3602 | 4.3602 | 0 | 0.1272 | yes | 500 |
| adv | main | y0BN | 2.8636 | 2.8636 | 0 | 0.09314 | yes | 500 |
| adv | main | y0BO | 0.9404 | 0.9404 | 0 | 0.0537 | yes | 500 |
| adv | main | y0Ep | 0.1283 | 0.1283 | 0 | 0.001245 | yes | 500 |
| adv | main | y0F0 | 20.8348 | 20.8348 | 0 | 0.2658 | yes | 500 |
| adv | main | y0Fpl | 20.1840 | 20.1840 | 0 | 0.2332 | yes | 500 |
| adv | main | y0GiniW | 0.9878 | 0.9878 | 0 | 0.0003556 | yes | 500 |
| adv | main | y0Pov | 23.5092 | 23.5092 | 0 | 0.1713 | yes | 500 |
| adv | effect | bNAPy | -20.0871 | -20.0871 | 0 | 0.1676 | yes |  |
| adv | effect | bOAPy | -20.2537 | -20.2537 | 0 | 0.169 | yes |  |
| adv | effect | cost | 57929.9 | 57929.9 | -0.0001219 | 90.2653 | yes |  |
| adv | effect | crRel | 70512.3 | 70512.3 | -7.761e-07 | 339.9869 | yes |  |
| adv | effect | drHit | -26.4552 | -26.4552 | 0 | 0.6064 | yes |  |
| adv | effect | emUrate | 0 | 0 | 0 | 0 | yes |  |
| adv | effect | endoAnn | 0.4601 | 0.4601 | -1.031e-09 | 0.001931 | yes |  |
| adv | effect | epPY | -0.2187 | -0.2187 | 0 | 0.002112 | yes |  |
| adv | effect | fgt0PY | -38.6584 | -38.6584 | 0 | 0.2471 | yes |  |
| adv | effect | fgt2PY | -11.4523 | -11.4523 | 2.033e-08 | 0.09086 | yes |  |
| adv | effect | finGapSh | 0.1538 | 0.1538 | -5.308e-10 | 0.00139 | yes |  |
| adv | effect | giniD | -0.01445 | -0.01445 | -9.906e-12 | 0.0006634 | yes |  |
| adv | effect | giniX | -0.03257 | -0.03257 | -9.931e-12 | 0.001394 | yes |  |
| adv | effect | hrs | 0.01565 | 0.01565 | -2.434e-08 | 0.01268 | yes |  |
| adv | effect | jnP19 | 100.0000 | 100.0000 | 0 | 0 | yes |  |
| adv | effect | lfShare | 0 | 0 | 0 | 0 | yes |  |
| adv | effect | medWealthReal | 79891.9 | 79891.9 | 5.374e-05 | 1807.0 | yes |  |
| adv | effect | pLev20 | 1969.7 | 1969.7 | -2.41e-05 | 51.5300 | yes |  |
| adv | effect | pov | -22.7192 | -22.7192 | 0 | 0.2412 | yes |  |
| adv | effect | snAll | -686.1986 | -686.1986 | -4.91e-05 | 10.3593 | yes |  |
| adv | effect | tauMean | 0.03669 | 0.03669 | -8.728e-11 | 0.000306 | yes |  |
| adv | effect | wtF0E | -46.4263 | -46.4263 | 0 | 0.409 | yes |  |
| adv | effect | wtGnE | -0.07009 | -0.07009 | 6.548e-10 | 0.001576 | yes |  |
| adv | effect | wtPovE | -23.1321 | -23.1321 | 0 | 0.2441 | yes |  |
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
| st | base | wtGnE | 0.8209 | 0.8209 | 1.11e-16 | 0.004075 | yes | 500 |
| st | base | wtPovE | 27.4923 | 27.4923 | 0 | 0.2235 | yes | 500 |
| st | base | y0BN | 15.9756 | 15.9756 | 0 | 0.1588 | yes | 500 |
| st | base | y0BO | 15.9756 | 15.9756 | 0 | 0.1588 | yes | 500 |
| st | base | y0Ep | 0.2245 | 0.2245 | 0 | 0.001216 | yes | 500 |
| st | base | y0F0 | 39.7592 | 39.7592 | 0 | 0.3082 | yes | 500 |
| st | base | y0Fpl | 16.3952 | 16.3952 | 0 | 0.2147 | yes | 500 |
| st | base | y0GiniW | 0.9879 | 0.9879 | 0 | 0.0003521 | yes | 500 |
| st | base | y0Pov | 25.0232 | 25.0232 | 0 | 0.1735 | yes | 500 |
| st | main | bNAPy | 0.6073 | 0.6073 | 0 | 0.02979 | yes | 500 |
| st | main | bOAPy | 0.5869 | 0.5869 | 0 | 0.02994 | yes | 500 |
| st | main | cost | 50662.5 | 50662.5 | -5.376e-05 | 70.7564 | yes | 497 |
| st | main | crRel | 102763.9 | 102763.9 | 1.217e-06 | 495.5328 | yes | 497 |
| st | main | drHit | 15.0441 | 15.0441 | 0 | 0.5008 | yes | 500 |
| st | main | emUrate | 3.5909 | 3.5909 | 0 | 0.05746 | yes | 500 |
| st | main | endoAnn | 0.4875 | 0.4875 | 2.611e-09 | 0.002202 | yes | 497 |
| st | main | epPY | 0.07372 | 0.07372 | 0 | 0.0006308 | yes | 500 |
| st | main | fgt0PY | 7.5146 | 7.5146 | 0 | 0.09882 | yes | 500 |
| st | main | fgt2PY | 0.2934 | 0.2934 | -7.708e-10 | 0.005512 | yes | 497 |
| st | main | finGapSh | 0.1603 | 0.1603 | -7.169e-09 | 0.001012 | yes | 497 |
| st | main | giniD | 0.9621 | 0.9621 | 1.972e-11 | 0.001458 | yes | 497 |
| st | main | giniX | 0.9439 | 0.9439 | 1.686e-11 | 0.002207 | yes | 497 |
| st | main | hrs | -0.0226 | -0.0226 | -7.201e-08 | 0.0118 | yes | 497 |
| st | main | jnP19 | 100.0000 | 100.0000 | 0 | 0 | yes | 500 |
| st | main | lfShare | 17.3904 | 17.3904 | 0 | 0.2163 | yes | 500 |
| st | main | medWealthReal | 279940.3 | 279940.3 | 0.0001589 | 1907.8 | yes | 497 |
| st | main | pLev20 | 2820.8 | 2820.8 | 9.845e-05 | 83.0280 | yes | 497 |
| st | main | paSh | 35.2885 | 35.2885 | 0 | 0.2384 | yes | 500 |
| st | main | poSub | 923.8113 | 923.8113 | -4.556e-09 | 6.8638 | yes | 499 |
| st | main | pov | 5.8568 | 5.8568 | 0 | 0.1356 | yes | 500 |
| st | main | snAll | 697.0763 | 697.0766 | 0.0003287 | 11.5513 | yes | 497 |
| st | main | tauMean | 0.02348 | 0.02348 | 2.916e-10 | 0.000248 | yes | 497 |
| st | main | wtF0E | 5.9757 | 5.9757 | 0 | 0.1531 | yes | 500 |
| st | main | wtGnE | 0.7567 | 0.7567 | 1.68e-10 | 0.00542 | yes | 497 |
| st | main | wtPovE | 6.0513 | 6.0513 | 0 | 0.1384 | yes | 500 |
| st | main | y0BN | 2.8132 | 2.8132 | 0 | 0.09319 | yes | 500 |
| st | main | y0BO | 1.3460 | 1.3460 | 0 | 0.0629 | yes | 500 |
| st | main | y0Ep | 0.1404 | 0.1404 | 0 | 0.001258 | yes | 500 |
| st | main | y0F0 | 21.0760 | 21.0760 | 0 | 0.2675 | yes | 500 |
| st | main | y0Fpl | 20.1064 | 20.1064 | 0 | 0.2328 | yes | 500 |
| st | main | y0GiniW | 0.9878 | 0.9878 | 0 | 0.0003556 | yes | 500 |
| st | main | y0Pov | 23.5092 | 23.5092 | 0 | 0.1723 | yes | 500 |
| st | effect | bNAPy | -20.0365 | -20.0365 | 0 | 0.1676 | yes |  |
| st | effect | bOAPy | -20.0569 | -20.0569 | 0 | 0.1698 | yes |  |
| st | effect | cost | 50662.5 | 50662.5 | -5.376e-05 | 70.7564 | yes |  |
| st | effect | crRel | 70528.3 | 70528.3 | 1.217e-06 | 340.0731 | yes |  |
| st | effect | drHit | -26.9486 | -26.9486 | 0 | 0.5614 | yes |  |
| st | effect | emUrate | 0 | 0 | 0 | 0 | yes |  |
| st | effect | endoAnn | 0.4875 | 0.4875 | 2.611e-09 | 0.002202 | yes |  |
| st | effect | epPY | -0.2048 | -0.2048 | 0 | 0.002093 | yes |  |
| st | effect | fgt0PY | -37.1144 | -37.1144 | 0 | 0.2454 | yes |  |
| st | effect | fgt2PY | -11.4115 | -11.4115 | -7.708e-10 | 0.09062 | yes |  |
| st | effect | finGapSh | 0.1603 | 0.1603 | -7.169e-09 | 0.001012 | yes |  |
| st | effect | giniD | -0.01007 | -0.01007 | 1.972e-11 | 0.0004823 | yes |  |
| st | effect | giniX | -0.02829 | -0.02829 | 1.686e-11 | 0.00122 | yes |  |
| st | effect | hrs | -0.00484 | -0.00484 | -7.201e-08 | 0.01179 | yes |  |
| st | effect | jnP19 | 100.0000 | 100.0000 | 0 | 0 | yes |  |
| st | effect | lfShare | 0 | 0 | 0 | 0 | yes |  |
| st | effect | medWealthReal | 70870.5 | 70870.5 | 0.0001589 | 1811.6 | yes |  |
| st | effect | pLev20 | 2819.3 | 2819.3 | 9.845e-05 | 83.0280 | yes |  |
| st | effect | pov | -21.0700 | -21.0700 | 0 | 0.2415 | yes |  |
| st | effect | snAll | -548.4842 | -548.4839 | 0.0003287 | 9.3904 | yes |  |
| st | effect | tauMean | 0.02348 | 0.02348 | 2.916e-10 | 0.000248 | yes |  |
| st | effect | wtF0E | -43.5536 | -43.5536 | 0 | 0.4137 | yes |  |
| st | effect | wtGnE | -0.06422 | -0.06422 | 1.68e-10 | 0.001476 | yes |  |
| st | effect | wtPovE | -21.4410 | -21.4410 | 0 | 0.2445 | yes |  |
| st | effect | y0BN | -13.1624 | -13.1624 | 0 | 0.1593 | yes |  |
| st | effect | y0BO | -14.6296 | -14.6296 | 0 | 0.1653 | yes |  |
| st | effect | y0Ep | -0.08413 | -0.08413 | 0 | 0.001469 | yes |  |
| st | effect | y0F0 | -18.6832 | -18.6832 | 0 | 0.2935 | yes |  |
| st | effect | y0Fpl | 3.7112 | 3.7112 | 0 | 0.1082 | yes |  |
| st | effect | y0GiniW | -9.174e-05 | -9.174e-05 | -4.472e-19 | 3.846e-06 | yes |  |
| st | effect | y0Pov | -1.5140 | -1.5140 | 0 | 0.08372 | yes |  |
