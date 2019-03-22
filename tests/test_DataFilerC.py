import datetime
import numpy as np


import garminmanager.DataFilterC
import garminmanager.RawDataC

from garminmanager.xyC import xyC

def test_starting_date():
    datafilter = garminmanager.DataFilterC.DataFilerC()
    test = datafilter._get_starting_day(datetime.datetime(2019,4,10,23,00))
    assert datetime.datetime(2019,4,10,0,00) == test
    test = datafilter._get_starting_day(datetime.datetime(2019,8,10,3,00,23))
    assert datetime.datetime(2019,8,10,0,00) == test

def test_process():
    datafilter = garminmanager.DataFilterC.DataFilerC()

    raw_data =  garminmanager.RawDataC.RawDataC()

    my_dates = {datetime.datetime(2019,4,10,23,00) : 100,
                datetime.datetime(2019,4,10,23,30) : 101,
                datetime.datetime(2019,4,12,1,00) : 102,
                datetime.datetime(2019,4,12,2,00) : 103,
                datetime.datetime(2019,4,12,5,00) : 105,
                datetime.datetime(2019,4,20,7,00) : 106,
                datetime.datetime(2019,4,20,10,00) : 107}

    for key, value in my_dates.items():
        raw_data.add_x(key)
        raw_data.add_y(value)

    datafilter.set_data(raw_data)
    datafilter.set_time_range_in_hour(24)
    datafilter.process()
    raw_data_array = datafilter.get_data()

    compare_data = garminmanager.RawDataC.RawDataC()
    compare_data.add_xy(list(my_dates.keys())[0], np.array(list(my_dates.values())[0]))
    compare_data.add_xy(list(my_dates.keys())[1], np.array(list(my_dates.values())[1]))

    assert (compare_data == raw_data_array[0])
    compare_data = garminmanager.RawDataC.RawDataC()
    compare_data.add_xy(list(my_dates.keys())[2], np.array(list(my_dates.values())[2]))
    compare_data.add_xy(list(my_dates.keys())[3], np.array(list(my_dates.values())[3]))
    compare_data.add_xy(list(my_dates.keys())[4], np.array(list(my_dates.values())[4]))
    assert (compare_data == raw_data_array[1])
    compare_data = garminmanager.RawDataC.RawDataC()
    compare_data.add_xy(list(my_dates.keys())[5], np.array(list(my_dates.values())[5]))
    compare_data.add_xy(list(my_dates.keys())[6], np.array(list(my_dates.values())[6]))
    assert (compare_data == raw_data_array[2])



