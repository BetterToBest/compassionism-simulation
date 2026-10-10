"""v5.4 item 5 (Oct 7, 2026; dev/reports/v5-21-v54-design.md, 1.6): federal disaster aid to households, for the disaster shock (harness.js CFG.DIS_*).

Source: OpenFEMA, Individuals and Households Program summaries by ZIP code, HousingAssistanceOwners and HousingAssistanceRenters (v2 API,
www.fema.gov/api/open/v2/...), every disaster numbered 4400 or above (major disasters declared from late 2018 on), retrieved Oct 7, 2026.
Result: 10,796,864 valid registrations, of which 5,464,568 approved (50.6%); approved Individuals and Households Program amounts $16.90 billion, a mean of
$3,092 per approved household (owners $3,485, renters $2,637). Nominal dollars of each year; the model treats the mean as 2025 dollars (a stated
approximation: most awards are from 2020-2025).

Usage: python3 sources/fema_ihp.py   (about 15 API calls; standard library only)
"""
import json, urllib.request, urllib.parse
tot = {}
for ds in ['HousingAssistanceOwners', 'HousingAssistanceRenters']:
    skip, s = 0, {'reg': 0, 'appr': 0, 'amt': 0}
    while True:
        q = urllib.parse.urlencode({'$select': 'disasterNumber,validRegistrations,approvedForFemaAssistance,totalApprovedIhpAmount',
                                    '$filter': 'disasterNumber ge 4400', '$top': 10000, '$skip': skip, '$format': 'json'})
        d = json.load(urllib.request.urlopen('https://www.fema.gov/api/open/v2/%s?%s' % (ds, q), timeout=120))[ds]
        for r in d:
            s['reg'] += r['validRegistrations'] or 0; s['appr'] += r['approvedForFemaAssistance'] or 0; s['amt'] += r['totalApprovedIhpAmount'] or 0
        skip += 10000
        if len(d) < 10000: break
    tot[ds] = s
    print('%s: approved share %.3f, mean award per approved household $%.0f' % (ds, s['appr']/s['reg'], s['amt']/s['appr']))
r, a, m = (sum(v[k] for v in tot.values()) for k in ('reg', 'appr', 'amt'))
print('all: registrations %d, approved %d (%.3f), mean award per approved household $%.0f' % (r, a, a/r, m/a))
