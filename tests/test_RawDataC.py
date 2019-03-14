import garminmanager.RawDataC
import datetime

from garminmanager.enumerators.EnumHealthTypeC import EnumHealtTypeC


def test_compare_datetime():
    my_dates = {datetime.datetime(2019,4,10,23,00) : 100,
        datetime.datetime(2019,4,10,23,30) : 101,
        datetime.datetime(2019,4,11,1,00) : 102,
        datetime.datetime(2019,4,11,2,00) : 103

            }

    raw_data1 = garminmanager.RawDataC.RawDataC()
    raw_data2 = garminmanager.RawDataC.RawDataC()

    for key, value in my_dates.items():
        raw_data1.add_timestamp(key)
        raw_data1.add_data(value)
        raw_data2.add_timestamp(key)
        raw_data2.add_data(value)

    assert raw_data1 == raw_data2

    raw_data1.timestamp_array[0] = datetime.datetime(2019,4,11,23,00)

    assert (raw_data1 == raw_data2) == False


def test_compare():
    raw_data1 = garminmanager.RawDataC.RawDataC()
    raw_data1.add_timestamp([1,2,3,4,5,6,7])
    raw_data1.add_data([10,20,30,40,50,60,70])

    raw_data2 = garminmanager.RawDataC.RawDataC()
    raw_data2.add_timestamp([1,2,3,4,5,6,7])
    raw_data2.add_data([10,20,30,40,50,60,70])
    raw_data1.set_data_type(EnumHealtTypeC.heartrate)
    raw_data2.set_data_type(EnumHealtTypeC.heartrate)
    assert raw_data1 == raw_data2

    raw_data2 = garminmanager.RawDataC.RawDataC()
    raw_data2.add_timestamp([1,2,3,4,5,6,7])
    raw_data2.add_data([11,20,30,40,50,60,70])

    assert (raw_data1 == raw_data2) == False

    raw_data2 = garminmanager.RawDataC.RawDataC()
    raw_data2.add_timestamp([2, 2, 3, 4, 5, 6, 7])
    raw_data2.add_data([10, 20, 30, 40, 50, 60, 70])

    assert (raw_data1 == raw_data2) == False

    raw_data2 = garminmanager.RawDataC.RawDataC()
    raw_data2.add_timestamp([1,2,3,4,5,6,7])
    raw_data2.add_data([10,20,30,40,50,60,70])
    raw_data1.set_data_type(EnumHealtTypeC.intensity)
    raw_data2.set_data_type(EnumHealtTypeC.heartrate)
    assert (raw_data1 == raw_data2) == False

def test_update():
    raw_data1 = garminmanager.RawDataC.RawDataC()
    raw_data1.add_timestamp([1,2,3,4,5,6,7])
    raw_data1.add_data([10,20,30,40,50,60,70])
    raw_data_class = raw_data1.get_xy_data()

    i = 0
    for item in raw_data_class:
        assert item.x == raw_data1.timestamp_array[i]
        assert item.y == raw_data1.data_array[i]
        i = i + 1

    raw_data1.add_xy(8,10)
    raw_data_class = raw_data1.get_xy_data()
    i = 0
    for item in raw_data_class:
        assert item.x == raw_data1.timestamp_array[i]
        assert item.y == raw_data1.data_array[i]
        i = i + 1