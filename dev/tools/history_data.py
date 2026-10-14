#!/usr/bin/env python3
"""Oct 14, 2026 (ledger steps s156 and s168, for the history check s146): turns the outside poverty-history data into one small file.

sources/history/ holds the files the outside data packs delivered. Pack A (the CSVs directly in sources/history/) is the more complete one
and is the base. Pack B (sources/history/cross-check-pack/) is a smaller, independent pack, used only to cross-check pack A. Nothing in either
pack was verified against its source by this repository: the Claude Code machine cannot reach census.gov. Read sources/history/README.md first.

Usage (run from the repository root):
  python3 dev/tools/history_data.py build        write sources/history/history_series.json (what the history check reads)
  python3 dev/tools/history_data.py check        rebuild in memory; fail if the committed history_series.json differs or a sanity test fails
  python3 dev/tools/history_data.py crosscheck   write sources/history/CROSSCHECK.csv (every cell where the two packs disagree, with the reason)

Rules for the built file (also written into its _meta):
  - Each figure is pack A's `value`. Where a source series has a break (2013 and 2017 survey redesigns; the 2019-2024 restatement of the
    supplemental measure in September 2026), `value` is the forward-comparable figure and `value_original` the first-published one; both are kept.
  - Groups are named all, under_18, 18_64, 65_plus.
  - A cell is listed under `disputed` when pack B disagrees and neither the first-published value nor an alternate row named in pack A's own
    notes explains the difference. The history check should not lean on a disputed cell.
"""
import csv, hashlib, json, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
A = os.path.join(ROOT, 'sources', 'history')
B = os.path.join(A, 'cross-check-pack')
OUT = os.path.join(A, 'history_series.json')
GROUP = {'all': 'all', 'all people': 'all', 'under 18': 'under_18', 'under_18': 'under_18', '18-64': '18_64', '18_64': '18_64',
         '65+': '65_plus', '65_plus': '65_plus'}
SERIES_B = {'OPM_rate': 'official_poverty_rate', 'OPM_number': 'number_in_poverty', 'OPM_below50': 'share_below_50pct_poverty',
            'Census_SPM_rate': 'SPM_rate', 'Official_threshold': 'official_threshold', 'SPM_threshold_renters': 'SPM_threshold_renters'}
ALT_ORDER = ['all', 'under_18', '18_64', '65_plus']   # the order of "also published as a/b/c/d" in pack A's notes


def rows(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def sha(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()[:16]


def grid(rs, series, unit=None):
    """{group: {year: value}} for one series of a pack-A file (blank cells are left out)."""
    out = {}
    for r in rs:
        if r['series'] != series or (unit and r['unit'] != unit) or num(r['value']) is None:
            continue
        out.setdefault(GROUP.get(r['group'].lower(), r['group']), {})[r['year']] = num(r['value'])
    return out


def first_published(rs, series):
    out = {}
    for r in rs:
        if r['series'] == series and num(r['value_original']) is not None:
            out.setdefault(GROUP.get(r['group'].lower(), r['group']), {})[r['year']] = num(r['value_original'])
    return out


def crosscheck_rows():
    """Every cell present in both packs whose value differs, with the reason. Returns (list of dicts, number of cells that agree)."""
    out, agree = [], 0
    for fn in ['poverty_official.csv', 'poverty_spm.csv', 'thresholds.csv']:
        a = {(r['series'], r['year'], GROUP.get(r['group'].lower(), r['group'])): r for r in rows(os.path.join(A, fn))}
        for r in rows(os.path.join(B, fn)):
            k = (SERIES_B.get(r['series'], r['series']), r['year'], GROUP.get(r['group'].lower(), r['group']))
            if k not in a:
                continue
            ra, va, vb, vo = a[k], num(a[k]['value']), num(r['value']), num(a[k]['value_original'])
            if va is None or vb is None:
                continue
            if abs(va - vb) < 1e-9:
                agree += 1
                continue
            why, kind = 'no explanation in either pack', 'unexplained'
            alt = re.search(r'also published as ([\d.]+(?:/[\d.]+){3})', ra['notes'])
            if k[0] == 'official_threshold':
                kind, why = 'definition', 'pack B gives the weighted-average four-person threshold (Historical Table 1) under the label "2 adults 2 children"; pack A gives the actual two-adult, two-child cell'
            elif abs(va - vb) < 1 and k[0] == 'SPM_threshold_renters':
                kind, why = 'rounding', 'same threshold, pack B kept more decimals'
            elif vo is not None and abs(vo - vb) < 1e-9:
                kind, why = 'first-published value', 'pack B equals pack A\'s value_original (the first-published figure; pack A uses the forward-comparable or restated one)'
            elif alt and abs(float(alt.group(1).split('/')[ALT_ORDER.index(k[2])]) - vb) < 1e-9:
                kind, why = 'other row of the same table', 'pack B equals the alternate row pack A names in its notes (' + alt.group(1) + ', all/under 18/18-64/65+)'
            out.append({'file': fn, 'series': k[0], 'year': k[1], 'group': k[2], 'pack_a_value': ra['value'], 'pack_a_value_original': ra['value_original'],
                        'pack_b_value': r['value'], 'difference': round(vb - va, 6), 'kind': kind, 'why': why})
    return out, agree


def build():
    o, s, h, t = (rows(os.path.join(A, f)) for f in ['poverty_official.csv', 'poverty_spm.csv', 'poverty_spm_history.csv', 'thresholds.csv'])
    m, sn, pe, sc = (rows(os.path.join(A, f)) for f in ['macro_drivers.csv', 'snap.csv', 'policy_events.csv', 'scf_wealth.csv'])
    cc, agree = crosscheck_rows()
    d = {
        '_meta': {
            'built_by': 'dev/tools/history_data.py build', 'read_first': 'sources/history/README.md',
            'status': 'outside data, not verified against the sources by this repository; use for a rough shape check only',
            'files': {f: sha(os.path.join(A, f)) for f in ['poverty_official.csv', 'poverty_spm.csv', 'poverty_spm_history.csv', 'thresholds.csv',
                                                          'macro_drivers.csv', 'snap.csv', 'policy_events.csv', 'scf_wealth.csv']},
            'pack_b_cells_agreeing': agree, 'pack_b_cells_differing': len(cc),
            'income_year': 'every year is the income (reference) year, not the publication year; 2025 is the latest (Census P60-290, September 2026)',
            'breaks': {
                '2013': 'official and supplemental measures: split panel; value = redesigned income questions (forward-comparable), value_original = traditional questions',
                '2017': 'updated processing system; value = updated, value_original or notes = prior processing',
                '2019-2024 supplemental': 'restated in September 2026 (BLS corrected thresholds July 2026); value = restated, value_original = first published (only 2019 and 2020 carry it)',
                '2020': 'pandemic nonresponse in the survey; Census research puts the official rate about 0.5 point higher with alternative weights',
                'official_threshold': 'the two-adult, two-child cell, not the weighted four-person average'},
            'units': {'official_poverty_rate': 'percent', 'number_in_poverty': 'thousands of people', 'spm_rate': 'percent',
                      'thresholds': 'dollars, same-year (nominal)', 'real_median_household_income': '2025 dollars',
                      'household_net_worth_yearend': 'billions of nominal dollars', 'snap_total_benefits': 'millions of nominal dollars'},
            'groups': ALT_ORDER},
        'years': [str(y) for y in range(2005, 2026)],
        'official': {'rate': grid(o, 'official_poverty_rate'), 'rate_first_published': first_published(o, 'official_poverty_rate'),
                     'number_thousands': grid(o, 'number_in_poverty'), 'share_below_half_of_line': grid(o, 'share_below_50pct_poverty')},
        'spm_census': {'rate': grid(s, 'SPM_rate'), 'rate_first_published': first_published(s, 'SPM_rate'),
                       'market_income_only_count_thousands': grid(s, 'SPM_market_income_only_count'),
                       'lifted_out_of_poverty_thousands': {k[len('lifted_'):]: grid(s, k, 'thousands').get('all', {}) for k in sorted({r['series'] for r in s}) if k.startswith('lifted_')},
                       'lifted_out_of_poverty_percentage_points': {k[len('lifted_'):]: grid(s, k, 'percentage_points').get('all', {}) for k in sorted({r['series'] for r in s}) if k.startswith('lifted_')}},
        'spm_columbia_2005_2012': {k: grid(h, k) for k in ['historical_SPM_rate', 'historical_SPM_rate_before_transfers', 'anchored_SPM_rate', 'anchored_SPM_rate_before_transfers']},
        'thresholds': {'official_two_adults_two_children': grid(t, 'official_threshold').get('2 adults 2 children', {}),
                       'spm_renters_first_published': grid(t, 'SPM_threshold_renters').get('2 adults 2 children', {})},
        'macro': {k: grid(m, k).get('all', {}) for k in sorted({r['series'] for r in m})},
        'snap': {k: grid(sn, k).get('all', {}) for k in sorted({r['series'] for r in sn})},
        'scf': {'median_net_worth_all_families_thousands_nominal': grid(sc, 'SCF median net worth').get('All families', {}),
                'dfa_bottom50_net_worth_yearend_billions_nominal': {y: v for g in grid(sc, 'DFA bottom-50% net worth').values() for y, v in g.items()}},
        'policy_events': [{k: r[k] for k in ['event', 'start_date', 'end_date', 'amount_or_rule', 'legal_citation']} for r in pe],
        'disputed': [{k: c[k] for k in ['series', 'year', 'group', 'pack_a_value', 'pack_b_value']} for c in cc if c['kind'] == 'unexplained'],
    }
    # lifted_out_of_poverty_thousands uses the group-less grid: grid() keys by group, rows here all have group "all"
    return d


def sanity(d):
    bad = []
    for g in ALT_ORDER:
        for y in d['years']:
            if y not in d['official']['rate'].get(g, {}):
                bad.append('official rate missing %s %s' % (g, y))
    for g in ALT_ORDER:
        for y in range(2009, 2026):
            if str(y) not in d['spm_census']['rate'].get(g, {}):
                bad.append('SPM rate missing %s %s' % (g, y))
    for k, v in d['macro'].items():
        miss = [y for y in d['years'] if y not in v]
        if miss:
            bad.append('macro %s missing %s' % (k, miss))
    if sorted(d['snap']) != ['SNAP_avg_monthly_participants', 'SNAP_total_benefits']:
        bad.append('snap series changed')
    for y in d['years']:
        if y not in d['thresholds']['official_two_adults_two_children']:
            bad.append('official threshold missing ' + y)
    return bad


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'crosscheck':
        cc, agree = crosscheck_rows()
        with open(os.path.join(A, 'CROSSCHECK.csv'), 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=list(cc[0].keys())); w.writeheader(); w.writerows(cc)
        kinds = {}
        for c in cc:
            kinds[c['kind']] = kinds.get(c['kind'], 0) + 1
        print('cells in both packs: %d agree, %d differ %s' % (agree, len(cc), kinds))
    elif cmd in ('build', 'check'):
        d = build(); bad = sanity(d); text = json.dumps(d, indent=1, sort_keys=True) + '\n'
        if bad:
            print('SANITY FAILED:\n  ' + '\n  '.join(bad)); sys.exit(1)
        if cmd == 'build':
            open(OUT, 'w', encoding='utf-8').write(text); print('wrote %s (%d bytes)' % (os.path.relpath(OUT, ROOT), len(text)))
        else:
            ok = os.path.exists(OUT) and open(OUT, encoding='utf-8').read() == text
            print('history_series.json is current' if ok else 'history_series.json is stale: run build'); sys.exit(0 if ok else 1)
    else:
        print(__doc__); sys.exit(2)
