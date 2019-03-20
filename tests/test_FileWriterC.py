import datetime
import numpy as np

import garminmanager.utils.FileWriterC
import garminmanager.RawDataC

from garminmanager.enumerators.EnumHealthTypeC import EnumHealtTypeC

def create_raw_data(my_date,process_type):
    raw_data = garminmanager.RawDataC.RawDataC()
    for key, value in my_date.items():
        raw_data.add_x(key)
        raw_data.add_y(value)

    raw_data.set_data_type(process_type)

    return raw_data



def test_write():
    my_raw_data_array = []

    # data set 1
    my_dates1 = {datetime.datetime(2019,4,11,1,00) : 100,
        datetime.datetime(2019,4,11,1,00) : 101,
        datetime.datetime(2019,4,11,2,00) : 102
            }
    raw_data = create_raw_data(my_dates1, EnumHealtTypeC.heartrate)
    my_raw_data_array = np.append(my_raw_data_array,raw_data)

    # data set 2
    raw_data = garminmanager.RawDataC.RawDataC()
    my_dates2 = {datetime.datetime(2019,5,11,1,00) : 200,
                 datetime.datetime(2019,5,11,1,00) : 201,
                 datetime.datetime(2019,5,11,2,00) : 202
                 }
    raw_data = create_raw_data(my_dates2, EnumHealtTypeC.heartrate)
    my_raw_data_array = np.append(my_raw_data_array,raw_data)

    # data set 3
    raw_data = garminmanager.RawDataC.RawDataC()
    my_dates3 = {datetime.datetime(2019,6,11,1,00) : 300,
                 datetime.datetime(2019,6,11,1,00) : 301,
                 datetime.datetime(2019,6,11,2,00) : 302
                 }
    raw_data = create_raw_data(my_dates3, EnumHealtTypeC.heartrate)
    my_raw_data_array = np.append(my_raw_data_array,raw_data)


    file_writer = garminmanager.utils.FileWriterC.FileWriterC()
    file_writer.set_data(my_raw_data_array)
    file_writer.set_folder("./writerTest")
    file_writer.write()

    start_date = datetime.datetime(2019,5,11,0,0)
    stop_date = datetime.datetime(2019,6,11,23,59)
    file_writer.set_intervall(start_date,stop_date)


    raw_out = file_writer.read()

    my_dates_result = {**my_dates2, **my_dates3}

    raw_org = create_raw_data(my_dates_result,EnumHealtTypeC.heartrate)

    assert raw_out == raw_org



