"""v5.5: the economist review checklist (ECONOMIST-REVIEW.md) and the GitHub issue template (.github/ISSUE_TEMPLATE/economist-review.yml) are written from the
same rows here, so they cannot drift apart.  python3 dev/tools/review_rows.py [--check]"""
import os, sys, json

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))

# (id, what to check, where it is in the repository, what the model does today)
ROWS = [
    ('unsourced-cco', 'CCO (Creative Currency Octaves) cost relief has no source (20% of the basket at the reference BU, ceiling 50%)',
     'index.html: CCO_RELIEF_AT_REF, CCO_RELIEF_CAP; dev/runs/unsourced-constants-check.txt',
     'Earlier engine only. Raising it left every released row unchanged. Is that right, and is there a source or a range worth sweeping?'),
    ('unsourced-damping', 'PTF (community businesses) and PTH (community housing) inflation damping has no source (0.5 and 0.1 times the share who joined)',
     'index.html: grep "inflRate*=(1-"; dev/runs/unsourced-constants-check.txt',
     'Off in every main row; on only in one optional row. Is a source known for its size?'),
    ('rho', 'The income effect on earnings (how far people cut paid work when given money; sourced range 0.05 to 0.30)',
     'dev/reports/v5-30-s137-results.md, section 8; dev/DECISIONS.md',
     'The one uncertain behavioural constant that matters for basket poverty. Is the range right for a payment of this size and kind?'),
    ('wage-elasticity', 'One wage elasticity for every change in the return to work',
     'dev/DECISIONS.md (fairness rule)',
     'Every change in the return to work uses the same elasticity. Is that the right treatment?'),
    ('spend-share', 'The share of extra cash spent (from the range of the US saving rate in recent years)',
     'dev/reports/v5-30-s137-results.md, section 8',
     'Drives the "too little wealth" result more than any other input. Is the range right?'),
    ('participation', 'Participation and the amount of BU (Basic Units) paid are design choices, not facts about the world',
     'study.html, "What the results depend on"',
     'They explain most of the spread in poverty, cost and inflation. What take-up should be assumed, and on what evidence?'),
    ('price-rule', 'The price rule: how programme spending and extra demand raise prices',
     'dev/reports/v5-30-s137-results.md, section 6; dev/DECISIONS.md',
     'Not calibrated to outside evidence on benefit-funded demand. The "too little wealth" rise comes through it. Which evidence would calibrate it?'),
    ('single-payer', 'Single-payer savings come from one preprint that is not peer reviewed',
     'study.html, "Single payer depends on the Yale preprint"',
     'Central, cautious and high-cost cases are run. Are these the right cases?'),
    ('cost-line', 'The cost-of-living line is the unweighted state average',
     'dev/reports/v5-30-s137-results.md, section 9',
     'A population-weighted line is a known later fix. How much would it matter?'),
    ('both-measures', 'Every gain is confirmed on basket poverty (below the cost of living) and on wealth poverty (too little wealth), not on one measure',
     'study.html; findings.html',
     'Compassionism lowers basket poverty and raises "too little wealth". Is the way both are reported fair?'),
    ('us-data', 'The no-programme run against US data (poverty, debt, savings)',
     'findings.html; dev/DECISIONS.md',
     'Which gaps with US data would change a conclusion, and which would not?'),
    ('safety-net', 'Tax revenue is not reconciled with today\'s safety-net outlays or government\'s share of the plan',
     'dev/reports/v5-30-s137-results.md, section 9',
     'The model reports these costs; it does not show they are financed. Is that an acceptable limit, stated this way?'),
]
INTRO = ('One page for an independent economist. Each row names one thing to check, where it is in the repository, and what the model does today. '
         'Mark each row agree, disagree or cannot tell, with a line of why. You need not do every row. Rows about what the framework means (as opposed to how it is modelled) belong to its author, Duke Johnson; say so in a comment.')
ATTRIB = ('The math and code of this simulation were engineered by Claude, an AI model made by Anthropic, from the concepts in Duke Johnson\'s book *Better To Best* and his related vision for eradicating extreme poverty while enriching cultures and supporting human flourishing. '
          'The model has not yet been reviewed by an independent economist; the full code is open for anyone to check, and expert collaborators are welcome.')


def md():
    o = ['# Economist review checklist', '', INTRO, '', 'Send it by opening an issue with the "Economist review" template (Issues, New issue), or by a comment on the pull request or discussion where you found the model.', '',
         '| # | Check | Where | What the model does today | Agree / disagree / cannot tell, and why |', '|---|---|---|---|---|']
    for i, (_, a, w, m) in enumerate(ROWS, 1):
        o.append('| %d | %s | %s | %s |  |' % (i, a, w.replace('|', '/'), m))
    o += ['', 'Everything on the pages comes from files you can run: `node harness.js validate`, `unit`, `domtest`; the 500-seed figures are in `data/`. The study page (`study.html`) names what the results depend on and the two constants with no source.', '', '---', '', ATTRIB, '']
    return '\n'.join(o)


def yml():
    q = lambda t: json.dumps(t, ensure_ascii=False)
    o = ['name: Economist review', 'description: A review of the model by an economist, one row at a time (the same rows as ECONOMIST-REVIEW.md)', 'title: "Economist review: "', 'body:',
         '  - type: markdown', '    attributes:', '      value: ' + q(INTRO),
         '  - type: input', '    id: who', '    attributes:', '      label: Your name and field (optional)', '    validations:', '      required: false']
    for i, (id_, a, w, m) in enumerate(ROWS, 1):
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
