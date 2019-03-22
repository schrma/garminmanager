import datetime
import numpy as np
import filecmp
import datetime

import garminmanager.ui.MainGui
import garminmanager.DataFilterC
import garminmanager.RawDataC
import pickle

from garminmanager.enumerators.EnumFilterTypeC import EnumFilterTypeC

from garminmanager.xyC import xyC

def test_fit_to_database():
    gui = garminmanager.ui.MainGui.MainWindow()
    gui._settings = {"monitor_folder": "./tests/samples",
                     "json_folder" : "./tests/json"}
    gui.fit_to_database()

    assert filecmp.cmp("./tests/samples/2019-02-23_00-00-002019-02-23_15-56-00.json","./tests/json/2019-02-23_00-00-002019-02-23_15-56-00.json")
    assert filecmp.cmp("./tests/samples/2019-03-02_13-33-002019-03-02_17-11-00.json","./tests/json/2019-03-02_13-33-002019-03-02_17-11-00.json")
    assert filecmp.cmp("./tests/samples/2019-03-04_19-11-002019-03-04_23-52-00.json","./tests/json/2019-03-04_19-11-002019-03-04_23-52-00.json")

def test_prepare_data():
    gui = garminmanager.ui.MainGui.MainWindow()
    gui._settings = {"monitor_folder": "./tests/samples",
                     "json_folder": "./tests/json"}
    # Settings
    gui.cal_filter_settings = garminmanager.filter.SettingsFilterC.SettingsFilterC()
    gui.cal_filter_settings.max = 80
    gui.cal_filter_settings.min = 40
    gui.cal_filter_settings.filter_type = EnumFilterTypeC.CALC_RANGE


    gui._start_date_time = datetime.datetime(2019,2,23,00,00)
    gui._end_date_time = datetime.datetime(2019,3,3,00,00)
    gui.prepare_data()

    with open("test_prepare_data_MainGui.txt", "wb") as fp:  # Pickling
         pickle.dump(gui._raw_result, fp)

    with open("./tests/samples/test_prepare_data_MainGui.txt", "rb") as fp:  # Unpickling
        org_data = pickle.load(fp)

    x = gui._raw_result.get_x()
    y = gui._raw_result.get_y()

    org_x = org_data.get_x()
    org_y = org_data.get_y()

    y[np.isnan(y)] = -100
    org_y[np.isnan(org_y)] = -100
    # org_data.y_array[10] = 10

    assert (y == org_y).all()
    assert (x == org_x).all()

