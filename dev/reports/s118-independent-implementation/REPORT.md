# A second, independent program for the simulation's yearly loop: what it found

Oct 29, 2026. For Duke; plain words. The program, the gap list and the result files are in this folder. The brief it follows is `dev/packets/s118-brief.md`, and the acceptance rule was set in advance (`dev/DECISIONS.md`, "Acceptance rule for the second implementation").

## Why this was done

Until an outside economist reviews the simulation, the strongest check one author can arrange is to write the model again, in a different language, from its written description, and see whether the second program gets the same numbers. Where they agree, the description and the code say the same thing. Where they differ, one of them has a mistake, or the description leaves something out.

## What was checked

A new program in Python (`s118_loop.py`), written from the packet prepared on Oct 15: the written description (`ODD.md`, `MODEL_SPEC.md`), an excerpt of the engine's code, and the engine's own results for five settings. The settings are no programme with 3% inflation, CCO Only, Full Integration, the Adverse Environment and the Stress Test, each with 500 adults over 20 years. I read the description first and opened the code excerpt only when the description did not answer a question. Each time I opened it is listed in `GAPS.md`. No constant or rule was changed to make a number agree.

The engine's results compared against: its own outputs for seeds 1 to 30 and 42 (in the packet) and for seeds 1 to 500 (study s171 in the results repository). Today's engine gives exactly the same outputs for these settings as the Oct 15 engine (checked on seeds 1 to 30), so the check applies to the engine as it is now.

The work had two phases, and the order matters for what the check proves.

1. **Phase 1, independent.** The program as written from the packet alone. Its results were saved to the repository before anything else was read.
2. **Phase 2, explaining the differences.** Only then did I read, in the engine itself, the three small functions the packet had left out, and add them to the program behind a switch (`--engine-fills`) to see whether they explained every difference.

## What agreed

**Phase 1, 500 seeds.** On the five headline figures (wealth poverty, median wealth, median BLEI days, the Gini, BLEI poverty), the independent program agrees with the engine on 17 of the 20 figures other than the Gini, by the brief's test. The three misses (wealth poverty and BLEI poverty in CCO Only, wealth poverty in Full Integration) are a quarter to a third of a percentage point. The year-0 population matches the engine's in distribution: 37.78% of adults below the wealth line against the engine's 37.80%, where theory says 37.8%.

| Setting | Wealth poverty % (engine / mine) | Median wealth $ | Median BLEI days | Gini | BLEI poverty % |
|---|---|---|---|---|---|
| No programme, 3% inflation | 71.5 / 71.5 | −10,000 / −10,000 | 7 / 7 | 0.857 / 0.852 | 70.5 / 70.5 |
| CCO Only | 24.2 / 23.9 | 391,095 / 393,293 | 1,173 / 1,179 | 0.577 / 0.568 | 21.1 / 20.8 |
| Full Integration | 15.3 / 15.0 | 528,624 / 530,844 | 1,834 / 1,844 | 0.518 / 0.509 | 12.4 / 12.3 |
| Adverse Environment | 40.3 / 40.1 | 146,364 / 148,947 | 526 / 534 | 0.678 / 0.672 | 36.6 / 36.5 |
| Stress Test | 62.0 / 61.9 | −10,000 / −10,000 | 16 / 16 | 0.803 / 0.798 | 59.9 / 59.8 |

(Means over seeds 1 to 500. Every key, with both tests, is in `results/phase1-500-seeds.md`.)

**Phase 2: exact.** With the three missing functions added, the Python program reproduces the engine **exactly** on all 2,500 runs (five settings × 500 seeds). That covers all fifteen figures that can be compared: the five headline figures, the 10th and 90th percentiles of wealth, the flourishing share, the debt-cost index, the share at the debt floor, the recession count and the year-0 figures. This includes the seed-42 figures the engine checks itself against (`results/phase2-500-seeds.md`, `results/phase2-seeds-1-30-and-42.txt`). Everything else in the yearly loop, as the presets run it, was therefore written correctly from the packet, line for line: the random draws, wages, costs, BLEI, conversion, octave advancement, PTF and PTH, recessions and automation.

## What did not agree, and why

1. **The exact test (seed 42) failed in phase 1.** The way the engine draws a Beta-distributed number (used for each adult's starting octave) is not in the packet. That draw uses a variable number of random numbers, so a different method shifts every later draw. My program used the textbook method. I tried eight other standard methods; none was the engine's. The engine uses an older method, the "tangent" rejection method. Both methods give the correct distribution (checked on a million draws each). They simply pick different adults, so the comparison falls back on averages.
2. **The Gini was lower in every setting in phase 1, by 0.005 to 0.010.** The engine's "Gini" is not quite a wealth Gini. At the end of a run it is the Gini of each adult's wealth less one year of the "extractive debt cost" index times their annual wage. Neither the description nor the packet says so; the description says it is the Gini of wealth. **This is a real gap in the description.** Every Gini these presets report, including the seed-42 regression figures, measures something slightly different from what the description says.
3. **CCO Only and Full Integration in phase 1.** Wealth poverty and BLEI poverty were about 0.3 points lower in my program, between 2 and 3 standard errors. Phase 2 shows this is chance. The phase-1 and phase-2 programs are the same apart from the Beta draw and the reporting function, and phase 2 equals the engine exactly. So these differences can only come from the two programs picking different (equally valid) adults. A fresh test confirms it: on 1,000 new seeds (501 to 1,500), with the phase-2 program standing in for the engine, every figure other than the Gini agrees by the two-sample test (all within 1.5 standard errors). The CCO Only and Full Integration gaps vanish (`results/fresh-seeds-501-1500.md`). The small differences all lean the same way because the five settings share each program's adults: one lucky draw counts five times.
4. **The brief's own test was too strict.** The brief counts a figure as matching if my mean is within two of the *engine's* standard errors. But my 30 runs are a separate sample, so even a perfect copy of the engine would fail that test on about one figure in six. On seeds 1 to 30 my program "failed" 16 of 25 headline figures that way. Most of that was this effect, plus a starting population that happened to be slightly richer than the engine's (36.96% below the wealth line in year 0, against the engine's 37.83%). Read literally, the brief says to stop at the first setting that fails, which would have been the first one. I went on, because the reason was found and the rest cost little. The results files give both the brief's test and the fair one.

## The gaps in the written description

`GAPS.md` lists 31 points where the description did not settle a question; eight of them are outright contradictions between the description and the code. The most important:

- **The description and the reference results are of two different models.** The description is of the release model (households, BU buying essentials all year, project work, ESP payroll and the surplus split, the price module, the spending rule). The packet's reference results come from the engine's older validation path, in which all of those are switched off. Most of what the validation path does is described nowhere in the description.
- In that path **nobody spends any of their surplus**, so the programme's median wealth of $400,000 to $530,000 after 20 years is all saved surplus.
- In that path **wages do not keep up with prices**, which is why the 3% no-programme setting ends with 70% of adults below the wealth line.
- **The octave wage raise is on, the price-damping by PTF and PTH is on, and the double counting of PTH appreciation that the description says was corrected is still there.** The description says each of these is off or fixed.

## What it means

- The written description is **not enough on its own to rebuild the model**. A careful reader would build something like the release model and would not reproduce the validation results. A list of what to add is at the end of `GAPS.md`.
- The **engine's validation path does what its code says, and nothing hidden.** A second program built from the excerpt plus three short functions reproduces it exactly, 2,500 runs out of 2,500.
- The **Gini in these presets is not a plain wealth Gini**; it should be described as what it is, or changed (a modelling decision, noted for the next release).
- **Not covered by this check:** the release model's own mechanisms, the ones behind the figures the Hub and NEEC cite. Those are project hiring, ESP payroll and the surplus split, the price module, households, open enrolment and the spending rule. None of them runs in the validation presets. An independent check of the release row would need a second packet built from it. That is the natural next step for this check.

## Presets reached

All five: no programme (3%), CCO Only, Full Integration, Adverse Environment, Stress Test.

## Files

- `s118_loop.py`: the program (`python3 -I s118_loop.py --preset baseline --seed 42`; `--engine-fills` for phase 2).
- `GAPS.md`: every question the description left open, with the line of code that settled it.
- `results/`: phase 1 and phase 2 comparisons (seeds 1-30 and 42; seeds 1-500), phase 1's per-seed outputs (`phase1-mine-500.json`, the record of the independent result), the fresh-seed check, `run.txt` (commands, versions, file hashes) and `SHA256SUMS`. The other per-seed outputs are not kept; the commands in `run.txt` regenerate them in about two minutes.
