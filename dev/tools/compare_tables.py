#!/usr/bin/env python3
"""Build the Part 1 tables of compare.html from the s171 match-*.txt result files.

Usage: python3 dev/tools/compare_tables.py RESULTS_DIR [--check]
RESULTS_DIR is the s171-cfc3322 folder of BetterToBest/compassionism-sim-results.
Without --check it rewrites the block between the two PART1 markers in compare.html;
with --check it only reports whether the page already matches the files.
Every figure is copied from the files; nothing is typed by hand.
"""
import html, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
PAGE = ROOT / 'compare.html'
BEGIN, END = '<!-- PART1-TABLES:BEGIN -->', '<!-- PART1-TABLES:END -->'
ENVS = [('ref', 'Reference'), ('adv', 'Adverse'), ('st', 'Stress Test')]
FINS = [('money', 'The Source pays (money created; the released reading)'),
        ('tax', 'A flat contribution on wages pays (the old comparison’s rule)')]
YEARS = [20, 40]


def name(label):
    if label.startswith('Compassionism:'):
        if 'shaded' in label:
            return 'Compassionism with its two untested mechanisms on'
        if 'a = 1' in label:
            return 'Compassionism Core, if every reward dollar is matched by output (a = 1)'
        if 'damping kept on' in label:
            return 'Compassionism Core, price damping kept on'
        return 'Compassionism Core (untested mechanisms off)'
    return label


def rows(path):
    out = []
    for line in path.read_text().splitlines():
        if not line.startswith('|') or line.startswith('|---') or line.startswith('| Design'):
            continue
        c = [x.strip() for x in line.strip().strip('|').split('|')]
        out.append((name(c[0]), c[1], c[4], c[7], c[8], c[9], c[11]))
    return out


def table(rs, years):
    head = ['Design', 'Cost per adult per year', 'Price rise caused by the program (points a year)',
            'Change in earnings from the work response', 'Wealth poverty at year %d (%%)' % years,
            'Below the cost of living (%) / severity',
            'Change in severity vs no program, %d-year average [95%% range]' % years]
    h = '<table class="fx-table"><thead><tr>' + ''.join('<th scope="col">%s</th>' % html.escape(x, quote=False) for x in head) + '</tr></thead><tbody>'
    for n, cost, infl, earn, wp, fg, dp in rs:
        h += '<tr><th scope="row">%s</th><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % tuple(
            html.escape(x, quote=False) for x in (n, cost, infl, earn, wp, fg, dp))
    return h + '</tbody></table>'


def build(res):
    parts = []
    for fin, title in FINS:
        parts.append('<h3 class="fx-h3">%s</h3>' % html.escape(title, quote=False))
        for env, en in ENVS:
            for y in YEARS:
                rs = rows(res / ('match-%s-%d-%s.txt' % (env, y, fin)))
                op = ' open' if env == 'ref' and fin == 'money' else ''
                parts.append('<details%s data-y="%d"><summary>%s, %d years</summary><div class="fx-tw">%s</div></details>' % (op, y, en, y, table(rs, y)))
    return '\n'.join(parts)


if __name__ == '__main__':
    res = pathlib.Path(sys.argv[1])
    page = PAGE.read_text()
    new = BEGIN + '\n' + build(res) + '\n' + END
    if BEGIN not in page:
        sys.exit('markers missing in compare.html')
    cur = page[page.index(BEGIN):page.index(END) + len(END)]
    if '--check' in sys.argv:
        print('compare.html Part 1 tables match the result files' if cur == new else 'DIFFERENT'); sys.exit(0 if cur == new else 1)
    PAGE.write_text(page.replace(cur, new)); print('written')
