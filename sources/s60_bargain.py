#!/usr/bin/env python3
"""S60 (Nov 13, 2026; research-update prereg/2026-11-s60-bargaining-power.md): the sources of BARGAIN (row option bg), a worker's outside option and an
employer markdown, and the readings derived from them. Every figure below was read in the opened source on Nov 13, 2026 (the PDF's SHA-256 where a PDF
was opened); nothing is fitted and no engine run is involved. Writes sources/s60_bargain.json.

Usage: python3 sources/s60_bargain.py
"""
import json, os

SRC = {
  'abm': {'cite': 'Azar, Berry and Marinescu, Estimating Labor Market Power, NBER Working Paper 30365 (Aug 2022)',
          'url': 'https://www.nber.org/system/files/working_papers/w30365/w30365.pdf', 'sha256': 'ad4b832ba748d768d3ec19ea5906c08b73b913c0f901e1ae17bf667fd424c51d',
          'read': {'firm_elasticity': 4.8, 'market_elasticity': 0.5, 'median_markdown_(MRPL-w)/w': 0.21},
          'note': 'abstract and section 7: "the median markdown is 0.21, implying that workers\' marginal productivity is about 21% higher than their wages"'},
  'ymh': {'cite': 'Yeh, Macaluso and Hershbein, Monopsony in the US Labor Market, American Economic Review 112(7), 2022, 2099-2138',
          'url': 'https://www.aeaweb.org/articles?id=10.1257/aer.20200025', 'sha256': None,
          'read': {'average_markdown_MRPL/w': 1.53}, 'note': 'abstract (journal page): US manufacturing plants, 1976-2014; "65 cents on the marginal dollar"'},
  'jsyz': {'cite': 'Jager, Schoefer, Young and Zweimuller, Wages and the Value of Nonemployment, Quarterly Journal of Economics 135(4), 2020, 1905-1963 (NBER w25230)',
           'url': 'https://www.nber.org/system/files/working_papers/w25230/w25230.pdf', 'sha256': '862c7fe774b75e06b2ee1a9cfe2ea2458fd3594eae6031bdbe649d9ab9c6d7c2',
           'read': {'preferred_1yr': [0.00, 0.013], 'preferred_2yr': [-0.027, 0.026], 'scatter_1yr': [-0.005, 0.008], 'scatter_2yr': [0.028, 0.018], 'ruled_out_above': 0.03,
                    'nash_benchmark_basic': 0.48, 'nash_benchmark_institutional': 0.24, 'calibrated_worker_bargaining_power': 0.1},
           'note': 'abstract and section 4: dollars of wage per dollar of unemployment benefit (estimate, standard error); four Austrian reforms; the outside option is paid only when not working'},
  'vivalt': {'cite': 'Vivalt, Rhodes, Bartik, Broockman, Krause and Miller, The Employment Effects of a Guaranteed Income: Experimental Evidence from Two U.S. States, NBER w32719, revised Aug 2026 (NBER page: QJE 141(4), 2026, 2675-2734)',
             'url': 'https://www.nber.org/system/files/working_papers/w32719/w32719.pdf', 'sha256': '46ccf7872b347f04e93ca85b59de816b243187459cb88224422769b211e6fca8',
             'read': {'transfer_per_month': 1000, 'months': 36, 'income_excl_transfer_per_year': -1900, 'per_dollar_individual': -0.16, 'per_dollar_household': -0.28,
                      'participation_points_pooled': [-4.2, 1.7], 'participation_points_survey': [-2.3, 1.2], 'participation_points_ui_records': [-6.6, 2.0], 'hours_per_week_survey': [-1.3, 0.6],
                      'hourly_income_all_jobs': [-0.14, 0.37], 'hourly_income_control_mean': 17.26, 'hourly_increase_ruled_out_above': 0.58,
                      'reservation_wage_hourly': [-0.27, 0.50], 'reservation_wage_control_mean': 18.30, 'searched_for_job_points': [6, 1], 'nonemployment_spell_months': 0.8},
             'note': 'abstract; section V (labour supply, Table IV text; quality of employment); Appendix Tables A.17, A.20, A.23 (estimate, standard error)'},
  'egger': {'cite': 'Egger, Haushofer, Miguel, Niehaus and Walker, General Equilibrium Effects of Cash Transfers: Experimental Evidence from Kenya, Econometrica 2022 (NBER w26600, revised Oct 2021)',
            'url': 'https://www.nber.org/system/files/working_papers/w26600/w26600.pdf', 'sha256': '0b8da5e6199a45dea41a0768992fb1d75bd38278d85cee932822dcbf5bf100f3',
            'read': {'hourly_wage_recipients_total_effect': [0.04, 0.04], 'hourly_wage_nonrecipients_total_effect': [0.19, 0.10], 'control_mean': 0.70},
            'note': 'Table 2, panel A (USD PPP an hour); the paper attributes wage gains to local demand (a multiplier), not to recipients\' outside options'},
  'finland': {'cite': 'Verho, Hamalainen and Kanninen, Removing Welfare Traps: Employment Responses in the Finnish Basic Income Experiment, AEJ: Economic Policy 14(1), 2022, 501-22',
              'url': 'https://www.aeaweb.org/articles?id=10.1257/pol.20200143', 'sha256': None,
              'read': {'employment_days_first_year': 'no significant change', 'participation_tax_cut_points': 23, 'n_treated': 2000}, 'note': 'abstract (journal page); no wage measure'},
  'alaska': {'cite': 'Jones and Marinescu, The Labor Market Impacts of Universal and Permanent Cash Transfers: Evidence from the Alaska Permanent Fund, AEJ: Economic Policy 14(2), 2022, 315-40',
             'url': 'https://www.aeaweb.org/articles?id=10.1257/pol.20190299', 'sha256': None,
             'read': {'employment': 'no effect', 'part_time_points': 1.8, 'part_time_relative': 0.17}, 'note': 'abstract (journal page); no wage measure'},
  'stockton': {'cite': 'West and Castro Baker, SEED first-year results, released Mar 3, 2021 (University of Pennsylvania School of Social Policy and Practice)',
               'url': 'https://sp2.upenn.edu/guaranteed-income-increases-employment-improves-financial-and-physical-health/', 'sha256': None,
               'read': {'transfer_per_month': 500, 'months': 24, 'n_treated': 125, 'full_time_employment': 'rose faster among recipients (press figures 28% to 40% against 32% to 37%)'},
               'note': 'evaluators\' release; small sample; no wage measure'},
}

def derive():
    m_abm = 1/(1 + SRC['abm']['read']['median_markdown_(MRPL-w)/w']); m_ymh = 1/SRC['ymh']['read']['average_markdown_MRPL/w']
    v = SRC['vivalt']['read']; per_hour = v['transfer_per_month']*12/2080  # the transfer spread over a full-time year
    pi_viv = v['hourly_increase_ruled_out_above']/per_hour
    rw_hi = v['reservation_wage_hourly'][0] + 1.96*v['reservation_wage_hourly'][1]
    J = SRC['jsyz']['read']
    pis = {'central': 0.0, 'jsyz_bound': J['ruled_out_above'], 'vivalt_bound': round(pi_viv, 2), 'nash_institutional': J['nash_benchmark_institutional'], 'nash_basic': J['nash_benchmark_basic']}
    nash = {}
    for k, pi in pis.items():
        for mk, m in (('abm', m_abm), ('ymh', m_ymh)):
            nash['%s_%s' % (k, mk)] = (1 - (1 - pi)/m)/pi if pi > 0 else None  # r/w the Nash relation implies before the programme
    return {'m': {'abm': m_abm, 'ymh': m_ymh, 'none': 1.0}, 'pi': pis, 'transfer_per_full_time_hour': per_hour, 'pi_vivalt_unrounded': pi_viv,
            'vivalt_reservation_wage_rise_upper_95_per_hour': rw_hi, 'vivalt_reservation_wage_upper_per_transfer_dollar': rw_hi/per_hour,
            'jsyz_preferred_mean': (J['preferred_1yr'][0] + J['preferred_2yr'][0])/2, 'nash_reservation_wage_share': nash}

if __name__ == '__main__':
    d = derive(); out = {'what': 'S60 sources and readings (sources/s60_bargain.py)', 'sources': SRC, 'derived': d}
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 's60_bargain.json'), 'w'), indent=1)
    print('markdown readings (wage over MRPL): %.4f (Azar et al.), %.4f (Yeh et al.), 1' % (d['m']['abm'], d['m']['ymh']))
    print('pass-through readings: %s' % ', '.join('%s %.2f' % kv for kv in d['pi'].items()))
    print('Vivalt et al.: $%.2f of transfer per full-time hour; hourly pay bound %.3f per dollar; reservation-wage bound $%.2f an hour, %.3f per dollar'
          % (d['transfer_per_full_time_hour'], d['pi_vivalt_unrounded'], d['vivalt_reservation_wage_rise_upper_95_per_hour'], d['vivalt_reservation_wage_upper_per_transfer_dollar']))
    print('Nash reservation wage before the programme (share of the wage): ' + ', '.join('%s %s' % (k, 'n/a' if v is None else '%.3f' % v) for k, v in d['nash_reservation_wage_share'].items()))
