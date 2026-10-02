# Step 2 report: the new output that backs the Basic Units (the production side)

Oct 1, 2026 · plan step 2 · Claude · 500 paired seeds, three environments · harness only

## What this step changes, in plain words

Until now the model let community-owned businesses (PTFs) serve any number of people from day one, at no cost. So the money the ESP split puts into "capacity" (step 1) bought nothing the model could see. This step gives it a job, and counts two kinds of new output, as your design default says:

1. **PTF capacity.** PTFs can serve only as many people as they have capital for. At the start they serve the PTF members who already exist (18-19% of adults at reference). Each dollar reinvested adds room: enough capital to serve everyone is $18,862 per adult (the 2025 capital stock per adult of grocers, food services and utilities, from the US Bureau of Economic Analysis). New members can join only while there is room. The "enough capacity" moment that starts the 60/40 phase of the split is now the moment PTFs can serve every adult.
2. **Output that backs new money.** Two things count as real output: the capital the split reinvests (buildings and equipment get built), and project work, valued at the pay for the hours worked (the face value of the BU paid). The extra conversion reward on top is not output. This only matters when the programme creates money (steps 3 onward); under a wage contribution it changes nothing, and a test checks that to the last digit.

Neither kind adds essentials supply directly. In the model's price rule, food prices do not move with local supply (food has outside markets), so more grocers help mainly by bringing PTF prices to more people.

## What it does

Measured against step 1 (the split with unlimited PTF reach), same people, 500 seeds. Poverty severity (FGT2), basket poverty and wealth poverty; negative = less poverty.

| Paid for by the wage contribution | Reference | Adverse | Stress |
|---|---|---|---|
| Poverty severity | +0.02 | +0.05 | +0.22 |
| Basket poverty (points) | −0.09 | −0.09 | −0.54 |
| Wealth poverty (points) | −0.04 | −0.11 | −0.71 |
| PTF capacity, years 5 / 10 / 19 | 37% / 68% / 100% | 37% / 66% / 100% | 12% / 17% / 30% |
| PTF members, year 19 | 48.5% | 49.6% | 27.7% |
| 60/40 phase starts (year, mean) | 14.4 | 15.3 | never |

**In everyday words: with the programme paid for by a wage contribution, building PTF capacity makes almost no difference.** At reference and in Adverse, reinvestment builds capacity a little ahead of the people who want to join, so the limit seldom binds. In the Stress Test PTFs earn too little to grow (they reach 30% of adults by year 19), so fewer people get PTF prices; slightly fewer people are poor, but those who are poor fall a little further (the measures disagree, so this is not a confirmed gain or loss).

**When money is created** ("hybrid" financing: conversion rewards are new money), the output that backs part of it slows inflation by about 1.5-2 points a year (reference 25.9% → 24.4% a year; Adverse 33.5% → 31.5%), and poverty falls a little: −0.06 / −0.34 / +0.21 on poverty severity, with basket and wealth poverty both lower in all three environments. Only 5-7% of what is converted is backed by output this way; the rest is reward.

### What moves the result (against the main row, wage contribution, reference)

- Capital target at half ($9,431 per adult): −0.96 (better; capacity reaches everyone by year 10).
- Capital target including health care ($28,113): +0.85 (worse).
- Letting PTF price cuts add essentials supply in the price rule (the most supply could do): −0.42, with prices 1.3% lower by year 20.
- If every essential-service business split its premium (no private owners), PTF capacity reaches everyone from the start (reinvestment is large), and the production side is −0.13.
- Counting project hours at the workers' own wages instead of the contract pay changes nothing measurable.

## What it means

The production side is now in the model, but it is small. Most of what Compassionism pays out is conversion reward, and only a small part of that is matched by output the model can count. That makes the next step, how it is paid for, decisive: if the rewards are new money, what backs them decides inflation.

## Limits

- No materials are counted in project work (the model has none).
- Capacity is one number for the whole country; there are no places.
- The capital target is the existing industries' capital per adult; PTFs that bought or converted existing businesses might need less.

## Exact commands and files

- `node harness.js testbed 500 prod ref`, `… adv`, `… st` (outputs in `dev/runs/step2-prod-500-{ref,adv,st}.txt`).
- Code: `PROD` in `harness.js` (off by default; every earlier output byte-identical with it off). Tests: `prodUnitSuite`, 8 tests.
- Choices made: `dev/DECISIONS.md`, "Step 2".
