"""v5.5: the economist review checklist (ECONOMIST-REVIEW.md) and the GitHub issue template (.github/ISSUE_TEMPLATE/economist-review.yml) are written from the
same rows here, so they cannot drift apart.  python3 dev/tools/review_rows.py [--check]"""
import os, sys, json

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))

# (id, group, what to check, where it is in the repository, what the model does today). S83 (Nov 17, 2026): rebuilt for v5.9; group "first" holds the four
# assumptions the v5.9 results rest on, "rest" the rest of the model. The v5.6 rows are in this file's history at tag v5.9.11.
ROWS = [
    ('backing', 'first',
     '**Full backing.** The main row assumes every dollar the programme pays is matched by new output',
     'TESTBED_SPEC.md section 0; MODEL_SPEC.md 14.0; `dev/reports/s64-round2-q4-backing.md`',
     "This is the design's statement, a design parameter, not a model result: the model's own mechanism for new output reaches 0.2 to 1.9% of the payout. Inflation stays under 5% a year only above about 86 to 90% backing; at the mechanism's own point it runs at 15 to 53 points a year. The backing curve (0, 0.25, 0.5, 0.75, 1) is published beside the main row. Is leading with full backing, with the curve beside it, a fair presentation?"),
    ('supply-limit', 'first',
     '**No limit on supply below full backing.** Demand never runs into what the economy can produce',
     '`dev/reports/s64-round2-q4-backing.md`, item 4 and its note of Nov 17, 2026; MODEL_SPEC 6.12, 14.3',
     'The poverty effects barely depend on backing because, with no new output, the real goods recipients gain are paid for only by higher prices on everyone, and wages, the BU and the basket all follow those prices. A rationing reading is planned for the next engine version. Which limit on real supply would you add first, and how would you size it?'),
    ('wage-index', 'first',
     '**Wages follow prices in full** (`wIdx` 1)',
     'MODEL_SPEC 6.1, 6.12; `dev/reports/s70-screen.md`, item 3',
     'Wages are indexed to the price level each year. At no backing this is the largest mover of programme inflation (μ* 20 to 34 points a year). Partial indexation is planned as a reading. What share is defensible for a programme of this size, and over what lag?'),
    ('asset-returns', 'first',
     '**Asset returns under high inflation**',
     'MODEL_SPEC 14.6, 14.7; `dev/reports/s59-asset-classes.md`, `s71-creditor-side.md`',
     "Real assets keep their real value (plus Shiller's real gains), nominal assets earn 0.46 of inflation, floating debt reprices in full and fixed-rate debt is eroded by inflation (debt relief). At full backing the erosion is under 3% of any wealth gain; at no backing, how far real assets follow inflation is the largest mover of wealth poverty and median wealth. Is that portfolio behaviour plausible at inflation of 15-50% a year, and who should bear the creditors' loss (five readings are run)?"),
    ('spend-share', 'rest',
     'The share of extra cash spent: 0.877 in v5.9, re-derived from the BEA 2025 saving rate on the no-programme run',
     'MODEL_SPEC 13.3; `dev/reports/s64-round2-q2-robustness.md`',
     '0.593 is a reading on every curve and the largest mover of median wealth. A wage-only base (0.862) is planned as a reading. Is the derivation right?'),
    ('income-effect', 'rest',
     'The income effect and the participation margin (one income effect per unconditional dollar, split 0.43 to leaving work)',
     'MODEL_SPEC 6.11, 14.15; `dev/reports/s73-participation.md`',
     "Matches the US guaranteed-income experiment's participation effect (−1.3 points, interval −7.5 to −0.9). Participation falls 1 to 5 points. Is the split right?"),
    ('wage-elasticity', 'rest',
     'One wage elasticity for every change in the return to work',
     'dev/DECISIONS.md (fairness rule)',
     'Every change in the return to work uses the same elasticity. Is that the right treatment?'),
    ('tail-weights', 'rest',
     'The weighted top tail and which measures read the weights',
     'ODD.md section 4 (Observation); MODEL_SPEC 14.8; `dev/reports/s59-tail-returns.md`',
     "18 tail adults with population weights (Pareto exponent 1.490, standard error 0.136, cutoff the 97.5th percentile). Poverty shares count each simulated adult once; median wealth and the distribution measures are weighted; the government's books are weighted sums, the payout and prices are not. Is that split acceptable, and does the tail's fit matter?"),
    ('fixed-population', 'rest',
     'A fixed population in the main row (no births, deaths, ageing, partnerships)',
     'MODEL_SPEC section 2 and 14.15',
     'Ageing exists as a reading; the 40-year figures do not age anyone. How much would ageing change the 40-year results?'),
    ('financed-rows', 'rest',
     'Paying by a contribution instead of the Source (the financed rows)',
     '`dev/reports/s64-round2-q5-financed.md`; `dev/reports/s72-government-budget.md`',
     "Shown, never led with: the full-coverage design needs 63-77% of all money income; 46 of 48 financed curves are fragile. Is the government account's treatment (borrowing rate, debt premium, weighted books) sound?"),
    ('central-bank', 'rest',
     'The central bank: a Taylor rule with purchases, refinancing, asset prices, job loss and forced sales (a study, 100 seeds)',
     'MODEL_SPEC section 15; `dev/reports/s74-central-bank.md`',
     "No channel to the price of essentials, so the design's damping claim cannot show; the rule moves wealth up the distribution through asset prices and forced sales. Are the channels and their slopes reasonable?"),
    ('policy-eras', 'rest',
     "The history readings: today's households under four US policy eras (a study, 100 seeds)",
     'MODEL_SPEC section 16; `dev/reports/s75-deep-history.md`',
     'A model counterfactual, not a backtest; no expectations channel. Is anything in it read as more than that?'),
    ('participation', 'rest',
     'Participation and the amount of BU (Basic Units) in the opt-in design are design choices, not facts about the world',
     '`dev/reports/s64-round2-q1-main-effects.md`; Stress (40% take-up)',
     'The opt-in design loses about two thirds of each effect in Stress. What take-up should be assumed, and on what evidence?'),
    ('us-data', 'rest',
     'The no-programme run against US data (wealth, earnings, labour force, the top 1% share)',
     'ODD.md section 1; findings.html',
     'Which gaps with US data would change a conclusion, and which would not?'),
    ('both-measures', 'rest',
     'Every gain is confirmed on basket poverty and on wealth poverty, not on one measure; BLEI is the days of basic living that savings, income and the BU cover (a capacity measure, not cash on hand)',
     'findings.html; the BLEI paper',
     'Is the way the measures are reported fair?'),
    ('unsourced-constants', 'rest',
     'Two constants with no source remain in the earlier engine (CCO cost relief; PTF and PTH inflation damping)',
     '`dev/runs/unsourced-constants-check.txt`',
     'Neither is used by any v5.9 row. Is a source known for either?'),
]
INTRO = 'One page for an independent economist, rebuilt for v5.9 on Nov 17, 2026 (engine `104691f`). Each row names one thing to check, where it is in the repository, and what the model does today. Mark each row agree, disagree or cannot tell, with a line of why. You need not do every row. Rows about what the framework means (as opposed to how it is modelled) belong to its author, Duke Johnson; say so in a comment. The model in one page: [model-card.html](https://bettertobest.github.io/compassionism-simulation/model-card.html); in full: [ODD.md](ODD.md) and [MODEL_SPEC.md](MODEL_SPEC.md).'
FIRST = '## First: the four assumptions the v5.9 results rest on'
REST = '## Then: the rest of the model'
TAIL = "Everything on the pages comes from files you can run: `node harness.js validate`, `unit`, `domtest`; [REPRODUCE.md](REPRODUCE.md) gives every v5.9 command and fingerprint, and each results folder in BetterToBest/compassionism-sim-results holds `run.txt` and `SHA256SUMS`. The v5.6 checklist (Oct 2026) is in this file's history at tag `v5.9.11`."
ATTRIB = ('The math and code of this simulation were engineered by Claude, an AI model made by Anthropic, from the concepts in Duke Johnson\'s book *Better To Best* and his related vision for eradicating extreme poverty while enriching cultures and supporting human flourishing. '
          'The model has not yet been reviewed by an independent economist; the full code is open for anyone to check, and expert collaborators are welcome.')


NOTE = '> **Note (Nov 28, 2026).** The results repository named in this document, `BetterToBest/compassionism-sim-results`, is offline: GitHub disabled it. Every figure can be reproduced from the engine commit named beside it, with the commands in `REPRODUCE.md`. The results folders are deposited in an archive with a permanent identifier, DOI 10.5281/zenodo.24615619 (copied on OSF at osf.io/7v5ur); folders not in the archive are listed in `data/results-manifest.json`.'


def md():
    head = ['| # | Check | Where | What the model does today | Agree / disagree / cannot tell, and why |', '|---|---|---|---|---|']
    o = ['# Economist review checklist (v5.9)', '', NOTE, '', INTRO, '', 'Send it by opening an issue with the "Economist review" template (Issues, New issue), or by a comment on the pull request or discussion where you found the model.', '']
    for i, (_, g, a, w, m) in enumerate(ROWS, 1):
        if i == 1: o += [FIRST, ''] + head
        if g == 'rest' and ROWS[i - 2][1] == 'first': o += ['', REST, ''] + head
        o.append('| %d | %s | %s | %s |  |' % (i, a, w.replace('|', '/'), m))
    o += ['', TAIL, '', '---', '', ATTRIB, '']
    return '\n'.join(o)


def yml():
    q = lambda t: json.dumps(t, ensure_ascii=False)
    o = ['name: Economist review', 'description: A review of the model by an economist, one row at a time (the same rows as ECONOMIST-REVIEW.md)', 'title: "Economist review: "', 'body:',
         '  - type: markdown', '    attributes:', '      value: ' + q(INTRO),
         '  - type: input', '    id: who', '    attributes:', '      label: Your name and field (optional)', '    validations:', '      required: false']
    for i, (id_, _g, a, w, m) in enumerate(ROWS, 1):
        o += ['  - type: textarea', '    id: ' + id_.replace('-', '_'), '    attributes:', '      label: ' + q('%d. %s' % (i, a)), '      description: ' + q('Where: %s. Today: %s Say agree, disagree or cannot tell, and why.' % (w, m)),
              '    validations:', '      required: false']
    o += ['  - type: textarea', '    id: other', '    attributes:', '      label: Anything else', '    validations:', '      required: false',
          '  - type: markdown', '    attributes:', '      value: ' + q(ATTRIB)]
    return '\n'.join(o) + '\n'


FILES = {'ECONOMIST-REVIEW.md': md(), '.github/ISSUE_TEMPLATE/economist-review.yml': yml()}
if __name__ == '__main__':
    bad = []
    for p, t in FILES.items():
        fp = os.path.join(ROOT, p)
        if '--check' in sys.argv:
            if not os.path.exists(fp) or open(fp, encoding='utf-8').read() != t: bad.append(p)
        else:
            open(fp, 'w', encoding='utf-8').write(t)
    if '--check' in sys.argv:
        if bad: print('review_rows.py --check: out of date: ' + ', '.join(bad)); sys.exit(1)
        print('review_rows.py --check: the checklist and the issue template are what the generator writes (%d rows)' % len(ROWS))
    else:
        print('wrote ' + ', '.join(FILES))
