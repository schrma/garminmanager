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
        raw_data1.add_x(key)
        raw_data1.add_y(value)
        raw_data2.add_x(key)
        raw_data2.add_y(value)

    assert raw_data1 == raw_data2

    x = raw_data1.get_x()

    x[0] = datetime.datetime(2019, 4, 11, 23, 00)

    assert (raw_data1 == raw_data2) == False


def test_compare():
    raw_data1 = garminmanager.RawDataC.RawDataC()
    raw_data1.add_x([1, 2, 3, 4, 5, 6, 7])
    raw_data1.add_y([10, 20, 30, 40, 50, 60, 70])

    raw_data2 = garminmanager.RawDataC.RawDataC()
    raw_data2.add_x([1, 2, 3, 4, 5, 6, 7])
    raw_data2.add_y([10, 20, 30, 40, 50, 60, 70])
    raw_data1.set_data_type(EnumHealtTypeC.heartrate)
    raw_data2.set_data_type(EnumHealtTypeC.heartrate)
    assert raw_data1 == raw_data2

    raw_data2 = garminmanager.RawDataC.RawDataC()
    raw_data2.add_x([1, 2, 3, 4, 5, 6, 7])
    raw_data2.add_y([11, 20, 30, 40, 50, 60, 70])

    assert (raw_data1 == raw_data2) == False

    raw_data2 = garminmanager.RawDataC.RawDataC()
    raw_data2.add_x([2, 2, 3, 4, 5, 6, 7])
    raw_data2.add_y([10, 20, 30, 40, 50, 60, 70])

    assert (raw_data1 == raw_data2) == False

    raw_data2 = garminmanager.RawDataC.RawDataC()
    raw_data2.add_x([1, 2, 3, 4, 5, 6, 7])
    raw_data2.add_y([10, 20, 30, 40, 50, 60, 70])
    raw_data1.set_data_type(EnumHealtTypeC.intensity)
    raw_data2.set_data_type(EnumHealtTypeC.heartrate)
    assert (raw_data1 == raw_data2) == False

def test_add_class():
    raw_data1 = garminmanager.RawDataC.RawDataC()
    raw_data1.add_x([1, 2, 3, 4, 5, 6, 7])
    raw_data1.add_y([10, 20, 30, 40, 50, 60, 70])

    raw_data2 = garminmanager.RawDataC.RawDataC()
    raw_data2.add_x([8, 9, 10, 11, 12, 13, 14])
    raw_data2.add_y([80, 90, 100, 110, 120, 130, 140])
    raw_data1.set_data_type(EnumHealtTypeC.heartrate)
    raw_data2.set_data_type(EnumHealtTypeC.heartrate)
    raw_total = raw_data1 + raw_data2

    x = raw_total.get_x()
    y = raw_total.get_y()

    xorg1 = raw_data1.get_x()
    yorg1 = raw_data1.get_y()

    for i, item in enumerate(xorg1):
        assert item == x[i]
        assert yorg1[i] == y[i]

    xorg2 = raw_data2.get_x()
    yorg2 = raw_data2.get_y()

    for i, item in enumerate(xorg2):
        my_offset = len(xorg1)
        assert item == x[i+my_offset]
        assert yorg2[i] == y[i+my_offset]

    raw_data1 = garminmanager.RawDataC.RawDataC()
    raw_total = raw_data1 + raw_data2

    assert raw_data2 == raw_total


    raw_total = raw_data2 + raw_data1

    assert raw_data2 == raw_total



def test_update():
    raw_data1 = garminmanager.RawDataC.RawDataC()
    raw_data1.add_x([1, 2, 3, 4, 5, 6, 7])
    raw_data1.add_y([10, 20, 30, 40, 50, 60, 70])
    raw_data_class = raw_data1.get_xy_data()

    i = 0
    for item in raw_data_class:
        x = raw_data1.get_x()
        y = raw_data1.get_y()
        assert item.x == x[i]
        assert item.y == y[i]
        i = i + 1

    raw_data1.add_xy(8,10)
    raw_data_class = raw_data1.get_xy_data()
    i = 0
    for item in raw_data_class:
        x = raw_data1.get_x()
        y = raw_data1.get_y()
        assert item.x == x[i]
        assert item.y == y[i]
        i = i + 1