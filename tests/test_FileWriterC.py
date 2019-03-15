import datetime
import numpy as np

import garminmanager.utils.FileWriterC



def test_write():
    my_raw_data_array = []

    # data set 1
    raw_data = garminmanager.RawDataC.RawDataC()
    my_dates1 = {datetime.datetime(2019,4,11,1,00) : 100,
        datetime.datetime(2019,4,11,1,00) : 101,
        datetime.datetime(2019,4,11,2,00) : 102
            }
    for key, value in my_dates1.items():
        raw_data.add_x(key)
        raw_data.add_y(value)
    my_raw_data_array = np.append(my_raw_data_array,raw_data)

    # data set 2
    raw_data = garminmanager.RawDataC.RawDataC()
    my_dates2 = {datetime.datetime(2019,5,11,1,00) : 200,
                 datetime.datetime(2019,5,11,1,00) : 201,
                 datetime.datetime(2019,5,11,2,00) : 202
                 }
    for key, value in my_dates2.items():
        raw_data.add_x(key)
        raw_data.add_y(value)
    my_raw_data_array = np.append(my_raw_data_array,raw_data)

    # data set 3
    raw_data = garminmanager.RawDataC.RawDataC()
    my_dates3 = {datetime.datetime(2019,6,11,1,00) : 300,
                 datetime.datetime(2019,6,11,1,00) : 301,
                 datetime.datetime(2019,6,11,2,00) : 302
                 }
    for key, value in my_dates3.items():
        raw_data.add_x(key)
        raw_data.add_y(value)
    my_raw_data_array = np.append(my_raw_data_array,raw_data)


    file_writer = garminmanager.utils.FileWriterC.FileWriterC()
    file_writer.set_data(my_raw_data_array)
    file_writer.write()

    file_writer.read()


