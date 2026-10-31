"""S14 (Oct 31, 2026): check the weighted line 'ext' ($51,201.28) against MIT's 51 state figures (dev/reports/lw-weighted-line.md, section 1).

ext came from an outside AI review (v4.11) that reported a population-weighted mean of $24.6160 an hour, which was only partly checked. Its source
was found on Oct 31: Money Talks News, "How much is really a living wage in every state"
(moneytalksnews.com/slideshows/how-much-is-really-a-living-wage-in-every-state/), which republishes MIT's "Required annual income before taxes",
one adult, no children, for the 50 states (not DC). Duke copied the table from the page; the site refuses automated access.

The 51 figures are not committed: MIT's terms allow web use of at most ten locations. The input file is identified by its hash:
  a CSV with header "state,required_annual_income_before_taxes_1a0k" and 50 rows in the article's order,
  sha256 527fb6d60f546cc5665a40a69a0b64bf5337737708758754cffa787e530f26ba.
DC: MIT's $26.72 an hour, read directly from livingwage.mit.edu in v4.11 (CHANGELOG, v4.11). Populations: Census Vintage 2025 (sources/lw_bea.py).

The check: (1) the eight states held in mit_household_types.json equal the input exactly; (2) each state's hourly living wage is its annual
figure / 2,080, rounded to the cent; (3) the unweighted mean x 2,080 against the line ($49,369.82), the population-weighted mean x 2,080
against ext ($51,201.28).

  python3 sources/lw_check_ext.py <input CSV>
"""
import csv, hashlib, importlib.util, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SHA = '527fb6d60f546cc5665a40a69a0b64bf5337737708758754cffa787e530f26ba'
DC_HOURLY = 26.72
LINE, EXT = 49369.82, 51201.28

path = sys.argv[1]
raw = open(path, 'rb').read()
got = hashlib.sha256(raw).hexdigest()
print('input sha256 %s (%s)' % (got, 'matches' if got == SHA else 'DIFFERS from the recorded file'))
annual = {r['state']: float(r['required_annual_income_before_taxes_1a0k']) for r in csv.DictReader(raw.decode().splitlines())}

spec = importlib.util.spec_from_file_location('lw_bea', os.path.join(HERE, 'lw_bea.py'))
lb = importlib.util.module_from_spec(spec); spec.loader.exec_module(lb)
pop = {k: v[1] for k, v in lb.STATES.items()}
assert set(annual) | {'District of Columbia'} == set(pop) and len(annual) == 50, 'the input must hold the 50 states'

held = json.load(open(os.path.join(HERE, 'mit_household_types.json')))['states']
for st, v in held.items():
    mit = v['rows']['Required annual income before taxes'][0]
    print('  %-14s MIT page %7.0f  input %7.0f  %s' % (st, mit, annual[st], 'same' if mit == annual[st] else 'DIFFERENT'))
    assert mit == annual[st]

hourly = {k: round(a / 2080, 2) for k, a in annual.items()}
hourly['District of Columbia'] = DC_HOURLY
un = sum(hourly.values()) / len(hourly)
w = sum(hourly[k] * pop[k] for k in hourly) / sum(pop.values())
print('51 jurisdictions; population %s' % format(sum(pop.values()), ','))
print('unweighted  $%.4f an hour -> $%.2f a year (the line $%.2f; difference $%.2f)' % (un, un * 2080, LINE, un * 2080 - LINE))
print('weighted    $%.4f an hour -> $%.2f a year (ext $%.2f; difference $%.2f)' % (w, w * 2080, EXT, w * 2080 - EXT))
print('weighting ratio %.4f (ext / line %.4f)' % (w / un, EXT / LINE))
for dc in (DC_HOURLY - 0.05, DC_HOURLY + 0.05):
    h2 = dict(hourly); h2['District of Columbia'] = dc
    print('  DC at $%.2f: weighted $%.2f a year' % (dc, sum(h2[k] * pop[k] for k in h2) / sum(pop.values()) * 2080))
