# Today's health coverage, made explicit (setting A)

Session 2a, Oct 13, 2026. Engine work only: the page does not change. Sources: `sources/health/README.md`. Choices and alternatives: `dev/DECISIONS.md`, Session 2a.

## Why this was needed

Until now the model charged every household the same medical cost: 6.85% of the MIT living-cost basket, scaled by household type. No one was uninsured or underinsured, no one's medical need varied, and no one took on medical debt. Single payer's expected gains come from exactly those people. So today's system had to be built first, before single payer could be measured against it. It also gives the Medicaid income limits that session 2b's benefit-cliff check needs.

## What the setting does

It is a switch (`HEALTH`). Switched off, which is the default, it changes nothing. The guard test proves this: every output of 25 release-panel rows, on 20 seeds, in all three environments, is identical.

Switched on:

- **Medical need.** Each person (each adult and, where households are modelled, each child) has a medical need each year. Its average rises with age, following the federal government's spending-by-age figures (CMS). A lasting chronic state (two or more chronic conditions) makes need about 3.8 times higher, as in MEPS. A spread and occasional hospital stays reproduce MEPS's pattern: the top 1% of people account for about 22% of spending, and the bottom half for about 3%. The random numbers come from their own source, so the model's other draws are untouched, and each person has the same needs in the run with the programme and the run without it.
- **Coverage, each year.** Medicare from 65 (only when people age in the model). Medicaid by household income against the poverty guideline: 138% in expansion states; in non-expansion states, parents up to about 40% and other adults not at all; children up to 255%. Employer coverage, more likely at higher pay, and lost in a year spent mostly out of work. The ACA marketplace, with the tax credit by income. Otherwise uninsured.
- **What people pay.** Premiums, deductibles, coinsurance and out-of-pocket limits, from the KFF and federal figures for 2025-26.
- **Care skipped for cost.** A household whose bills are high relative to its income may skip half its non-acute care (emergencies are not skipped).
- **Medical debt.** Bills a household could not cover from its savings, while its wealth stays below zero.
- **Who pays.** The setting records what households, employers, government and insurers pay. The employer's share of the premium counts as pay the worker forgoes. That keeps the later comparison with tax-financed single payer consistent.

**Cost is unchanged on average.** Each household type's average bill is scaled to that type's medical line in the basket. Each household then pays the difference between its own bill and its line, so the setting adds spread, not cost. The scaling factor is 0.69. In other words, the published premium and spending figures give bills about 45% above MIT's medical line, and the model keeps MIT's line.

**Claude's reading of the design (a modelling assumption).** The basic universal payment (BU) and PTF's health-sector price cut cover the average medical line. A bill above the line is paid in cash. The Hub's papers do not say how BU meets one person's medical bills, so the cautious choice is not to assume it pays them.

## What it shows (Reference, 20 paired seeds, without the programme)

| | Model | Real figure (check) |
|---|---|---|
| Employer coverage, adults | 63.8% | about 63% (Census 2024, ages 19-64) |
| Marketplace | 18.7% | about 11% |
| Medicaid, adults | 4.8% | about 15% of ages 19-64 are on public coverage |
| Uninsured, adults | 12.8% | 11% |
| Children on Medicaid or CHIP | 45.6% | about 40% |
| Underinsured (share of insured adults) | 30% | 23% of adults 19-64 (Commonwealth Fund 2024) |
| Adults skipping some care for cost, in a year | 12% | 5.7-17.3% for insured people, 43% for the uninsured (BRFSS 2024) |
| Adults with medical debt over $250 | 21% | about 8% (KFF, SIPP 2021) |

Two of these are model limits, reported rather than tuned away:

- **Medicaid is too low** (and the marketplace too high). Every adult in the model has a job or is between jobs. The model has no adults with disabilities and none outside the labour force, and those are the people who make up much of adult Medicaid.
- **Medical debt is too high.** Many of the model's households already have negative wealth, and an unpaid bill in such a household counts as medical debt. The debt figure is best read as an upper bound.

## How far the spread alone moves the main result

This is a reading, not a release figure. It shows the change in the programme's paired effect when setting A replaces the flat medical line (20 paired seeds):

| | Reference | Adverse | Stress |
|---|---|---|---|
| Basket poverty (person-years) | -1.1 points | -1.6 | -0.4 |
| FGT2 (depth of poverty) | +0.07 | +0.61 | +0.27 |
| Too little wealth at year 20 | +0.4 (interval crosses 0) | +0.1 (crosses 0) | -0.2 (crosses 0) |
| BLEI poverty | -0.3 | -0.3 | -0.2 |

All the changes are small next to the effects themselves (for example, basket poverty falls by about 31 points in Reference). The programme lowers basket poverty slightly more once bills vary. It deepens FGT2 somewhat in Adverse, because a few people with large bills fall further below the line. With the non-expansion limits, the changes are similar. With the medical price response to extra demand at 0 or at 1 (it is 0.5, an unsourced placeholder), the readings move by less than 0.2 points.

The programme run has about 1.3 points more adult-years on Medicaid. In the Medicaid income test the programme's guaranteed income is not counted as cash (the cautious assumption for today's rules; session 2b tests the other reading), and hours fall slightly.

## What is not modelled

Health does not yet change with care received: skipping care does not make next year's need larger. That is session 2b's prevention link. There are no adults with disabilities, no Medicare before 65 and no dual Medicare and Medicaid coverage. A child's marketplace premium is set at half an adult's (a design value). Plan choice is simplified: everyone on the marketplace buys the benchmark silver plan.

## Reproduce

`node dev/tools/health_check.js ref 20 --rows=off,A,Anx,B,Bcau,Bhigh --out=all` (also `adv`, `st`; `--theta=0`, `--theta=1` with `--out=theta0` / `theta1`). Outputs are in `dev/runs/health/`. Tests: `node harness.js unit` (healthUnitSuite). Guard: `node dev/tools/guard_test.js`.
