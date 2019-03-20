import datetime

import garminmanager.filter.SettingsFilterC
import garminmanager.filter.CalculationFilterC

import garminmanager.testsupport.help_functions

from garminmanager.enumerators.EnumFilterTypeC import EnumFilterTypeC
from garminmanager.enumerators.EnumHealthTypeC import EnumHealtTypeC

def test_calc_min_max():


    # Prepare raw data
    my_dates = {datetime.datetime(2019,4,10,23,00) : 30,
        datetime.datetime(2019,4,10,23,30) : 99,
        datetime.datetime(2019,4,11,1,00) : 100,
        datetime.datetime(2019,4,11,2,00) : 101}
    raw_data = garminmanager.testsupport.help_functions.create_raw_data(my_dates,EnumHealtTypeC.heartrate)

    # Settings
    settings = garminmanager.filter.SettingsFilterC.SettingsFilterC()
    settings.max = 100
    settings.min = 40
    settings.filter_type = EnumFilterTypeC.CALC_RANGE

    # calculation_filter
    calculation_filter = garminmanager.filter.CalculationFilterC.CalculationFilterC()
    calculation_filter.set_input_data(raw_data)
    calculation_filter.set_settings(settings)
    calculation_filter.process()
    raw_result = calculation_filter.get_output_data()

    org_dates = dict((k, v) for k, v in my_dates.items() if v >= settings.min and v<=settings.max)

    raw_org = garminmanager.testsupport.help_functions.create_raw_data(org_dates, EnumHealtTypeC.heartrate)

    assert raw_result == raw_org

