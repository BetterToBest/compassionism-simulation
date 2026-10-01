# N1 restudy: the damping off by default, 500 seeds (session 23, s34)

Sep 30, 2026 · v4.22 live · harness only (`apply-session-23.zip`) · `node harness.js testbed 500 projcore ref,adv,st`; `… esp ref,adv,st`; `… match ref,adv,st --fin=money,hybrid`

Read with: `N1-design-damping-theta.md` (the design, d86–d90), `N1-core-rows-500.md`, `N1-esp-restudy-500.md`, `N1-blei-by-group-500.md`.

**Configuration.** Testbed profile, tax-financed at each row's own cost unless stated, CRN-paired on seeds 1–500. The main rows are project hiring with your d58–d66 picks, the octave wage raise off, the gift paid as you go, and now the PTF/PTH inflation damping off (d86) and the capacity term at 0 (d87). The Hub-spec main row carries ESP payroll (d76). The measure is the change in 20-year average FGT₂ against no program; negative means less poverty.

**What the build changed.** `projcore`, `esp` and `match` print the N1 rows through one builder, `n1Row`. `--damp=on` prints each section exactly as session 21 did. `a5` and `frontdoor` keep their rows until s35 (d93). The damping is switched on each Compassionism row rather than through a profile switch, so the comparators and every other section are untouched (unit test s34-3).

**Checks.**
- `validate` passes; `unit` passes with every suite clean, including six new s34 tests; `domtest` 95 of 95.
- With `--damp=on`, `projcore`, `esp`, `match` and `a5` print session 21's output line for line (3 seeds, Adverse; elapsed times aside).
- At 500 seeds every row that sessions 16, 19 or 22 had run reproduces exactly: for example −1.77 / −3.11 / −1.94 and −1.51 / −0.92 in the engine model, +4.14 / −1.65 / −1.58 and −0.34 / −0.54 in the Hub-spec model, and the capacity term at 1.

## 1. The page's Compassionism rows (d88)

| Row | Engine: ref / Adverse / Stress | Hub spec: ref / Adverse / Stress |
|---|---|---|
| **Main row** (damping off) | **−1.77 / −1.51 / −0.92** | **+4.14 / −0.34 / −0.54** |
| Beneath: gift paid over the run (d67) | −1.80 / −1.48 / −0.91 | +4.08 / −0.47 / −0.53 |
| Shaded: both former stand-ins on | −3.17 / −7.67 / −3.69 | +0.02 / −2.12 / −3.28 |

At reference there is no exogenous inflation, so the shaded row is the octave raise alone.

**Cost per adult-year and contribution** (main row): engine $12,466 (24.5%) / $10,799 (33.0%) / $4,556 (13.3%); Hub spec $33,908 (80.0%) / $28,422 (83.0%) / $10,471 (30.6%).

**Price level in year 20** (Adverse and Stress): 1.457 on the main row, the no-program level; 1.317–1.346 with the damping on.

## 2. Sensitivities (harness and restudy notes; not on the page)

Change against the main row, [95% CI]:

| Sensitivity | Engine: ref / Adverse / Stress | Hub spec: ref / Adverse / Stress |
|---|---|---|
| Damping kept on (d86) | — / −1.61 [−1.62, −1.60] / −1.03 | — / −1.31 [−1.32, −1.30] / −1.04 |
| Octave raise kept on, damping off | (= shaded) / −4.84 [−4.86, −4.82] / −1.81 | (= shaded) / −0.49 [−0.55, −0.44] / −1.77 |
| Both stand-ins (the shaded row) | −1.41 / −6.16 / −2.77 | −4.12 / −1.78 / −2.74 |
| Capacity term at 1 (d87) | −0.17 / −0.36 / −0.20 | −0.28 / −0.27 / −0.21 |

**The two stand-ins are not equal, and which matters more depends on the model.** In the engine model the raise carries three times what the damping does in Adverse (4.84 against 1.61). In the Hub-spec model in Adverse it is the other way round (0.49 against 1.31). In the Stress Test the raise is the larger in both. Together they do slightly less than the sum of the two, in every cell.

## 3. Groups (main rows, against no program)

**Real resources per adult-year, Hub spec with ESP payroll** (participants / non-participants / bottom third / top third by year-0 wage):
- Reference: −$6,256 / −$25,837 / +$868 / −$24,613.
- Adverse: +$1,411 / −$14,370 / +$4,142 / −$9,875.
- Stress: +$4,756 / −$4,710 / +$1,862 / −$4,460.

**Engine model, in percent of each group's no-program resources** (participants / non-participants / bottom third / top third): reference +0.6% / −20.8% / +15.5% / −12.0%; Adverse −0.5% / −26.0% / +18.5% / −16.3%; Stress +8.7% / −9.1% / +8.5% / −6.3%. The dollar figures come from `a5` at s35.

**Worse off** (the table's test: resources, income poverty, wealth poverty):
- Non-participants and the top third are worse off in every cell.
- Participants are worse off at reference in the Hub-spec model (all three tests), and in Adverse in both models (income poverty; the engine model also on wealth poverty).
- With the damping off, the engine model's Adverse participants now also lose resources (−0.5%).

## 4. BLEI by group (design-neutral reading N, vs no program; participants / non-participants)

| Model | Reference | Adverse | Stress |
|---|---|---|---|
| Engine | −4.08 / +16.33 | **−0.06 [−0.13, +0.01]** / +14.27 | −5.82 / +5.29 |
| Hub spec | +5.43 / +32.72 | +1.91 / +22.07 | −8.86 / +7.12 |

With the damping off, participants in the engine model no longer gain on BLEI in Adverse (−1.95 with it on, session 21), and Hub-spec participants lose more (+1.91, against +0.58). Reference is unchanged.

## 5. ESP payroll against today's rule, damping off

| Row | Reference | Adverse | Stress |
|---|---|---|---|
| Main row | +2.71 [+2.67, +2.75] | +1.12 [+1.10, +1.14] | +0.25 [+0.24, +0.26] |
| Gift over the run | +2.70 | +1.11 | +0.25 |
| Shaded | +1.58 | +1.79 | +0.28 |
| Hybrid, a = 0 | +0.23 | +0.35 | +0.15 |
| Hybrid, a = 1 (H1) | +0.22 | +0.41 | +0.13 |
| Worker cooperative (d75) | +19.37 | +17.14 | +2.66 |
| Workforce = every adult | +1.42 | **−0.33** | +0.18 |

Reference equals session 19. In Adverse and Stress each figure moves by 0.1 or less, except the worker-cooperative row (+17.55 → +17.14). Session 19's conclusion holds: ESP payroll makes the Hub-spec row worse in every environment and at every setting but one.

**Non-participants against today's rule:** −$5,986 at reference, −$2,663 in Adverse, −$531 in Stress. BLEI poverty (N), participants / non-participants: −0.26 / +4.44, −2.55 / +2.39, −1.09 / +0.66.

**Hybrid financing.** At a = 0 prices rise 23.4 points a year at reference, 29.5 in Adverse and 13.4 in Stress with ESP payroll. At a = 1 (H1) no group is worse off than with no program in Adverse or Stress.

## 6. The money comparison (d90; fills the Limits and costs draft's gap)

`match` on the N1 rows. Under **money financing** every design is paid for with new money. UBI, the NIT and the endowment are matched to the N1 main row's gross cost under that financing (60 pilot seeds). Endogenous inflation, points a year:

| Environment · model | Compassionism, a = 0 | Compassionism, a = 1 (H1) | UBI | NIT | Endowment | Shaded row, a = 0 |
|---|---|---|---|---|---|---|
| Reference · engine | 21.9 | 15.8 | 24.5 | 27.6 | 10.3 | 19.7 |
| Reference · Hub spec | 41.7 | 20.2 | 61.5 | 73.8 | 15.1 | 38.9 |
| Adverse · engine | 30.7 | 22.7 | 34.9 | 39.8 | 10.2 | 26.6 |
| Adverse · Hub spec | 52.5 | 26.6 | 82.5 | 98.9 | 14.8 | 47.9 |
| Stress · engine | 13.8 | 11.1 | 14.4 | 16.0 | 6.3 | 12.7 |
| Stress · Hub spec | 26.1 | 14.3 | 31.8 | 36.2 | 9.8 | 24.6 |

Matched costs per adult-year: engine $11,928 / $11,747 / $4,967; Hub spec $27,578 / $26,201 / $10,752 (reference / Adverse / Stress).

**What it says**

1. **Compassionism inflates less than a basic income or NIT of equal cost in every cell, and more than the asset endowment.** The gap is widest in the Hub-spec model (41.7 against 61.5 for UBI at reference). A plausible reason is that part of Compassionism's cost is BU restricted to essentials and price cuts, but the harness does not decompose it, so this is not a finding.
2. **H1 does not stop the inflation.** With every conversion reward matched by output (a = 1), Compassionism still runs 11–27 points a year, because the BU and the price cuts are also new money. This is round close-out finding 7 on the N1 rows: engine reference at a = 1 is 15.8 points a year (14.4 before N1).
3. **Every large design inflates** under money financing. The endowment inflates least because it pays once into wealth, and of the three matched designs it also cuts FGT₂ least (−0.9 to −1.3).

**Hybrid financing** (only conversion rewards are new money; everything else is taxed). The comparators have no conversion rewards, so they are tax-financed there and show no inflation by construction; this is not a like-for-like inflation comparison. Compassionism at a = 0: 6.3 / 9.1 / 2.2 points a year as coded and 23.4 / 29.5 / 13.4 on the Hub spec (reference / Adverse / Stress); at a = 1, 0. The Hub-spec hybrid rows equal `esp`'s hybrid rows (−5.27 at reference, a = 0), a consistency check across sections.

**Run note.** The first background run stopped after the engine model's reference sections; the Hub-spec reference sections were rerun alone (`--models=framework`) on the same code. Seeds are paired, so the split does not change any figure.

## What the results say

1. **The main rows land where session 22's sizing put them**, and the page's three rows (d88) are now computed. With both stand-ins retired, Compassionism as coded still does better than no program on FGT₂ in all three environments (−1.77 / −1.51 / −0.92); specified on the Hub it does worse at reference (+4.14) and slightly better in Adverse and Stress (−0.34 / −0.54).
2. **The octave raise is the larger stand-in in the engine model; the damping is the larger in the Hub-spec model's Adverse row.** Both remain one shaded row away.
3. **With the damping off, Adverse is where participants lose ground**: as coded they no longer gain on BLEI, and in both models they fail the worse-off test on income poverty.
4. **ESP payroll's effect barely moves**; the ESP's own premium (s40) still carries the Hub-spec result.
5. **Under money financing, Compassionism inflates less than a basic income or NIT of equal cost**, but it still inflates, even at H1.
