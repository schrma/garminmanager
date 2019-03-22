import datetime
import numpy as np

import garminmanager.ui.MainGui
import garminmanager.DataFilterC
import garminmanager.RawDataC
import filecmp

from garminmanager.xyC import xyC

def test_fit_to_database():
    gui = garminmanager.ui.MainGui.MainWindow()
    gui._settings = {"monitor_folder": "./tests/samples",
                     "json_folder" : "./tests/json"}
    gui.fit_to_database()

    assert filecmp.cmp("./tests/samples/2019-02-23_00-00-002019-02-23_15-56-00.json","./tests/json/2019-02-23_00-00-002019-02-23_15-56-00.json")
    assert filecmp.cmp("./tests/samples/2019-03-02_13-33-002019-03-02_17-11-00.json","./tests/json/2019-03-02_13-33-002019-03-02_17-11-00.json")
    assert filecmp.cmp("./tests/samples/2019-03-04_19-11-002019-03-04_23-52-00.json","./tests/json/2019-03-04_19-11-002019-03-04_23-52-00.json")

