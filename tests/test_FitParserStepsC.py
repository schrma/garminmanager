import pickle
import numpy as np

import garminmanager.fitparser.FitParserStepsC
from garminmanager.fitparser.FitParserC import RecordC
import garminmanager.utils.FileWriterC
from garminmanager.enumerators.EnumHealthTypeC import EnumHealtTypeC

def test_process():
    fitparser_steps = garminmanager.fitparser.FitParserStepsC.FitParserStepsC()
    input_data = [["timestamp", "2019-01-01 12:00:00","first_timestamp"],
                  ["timestamp", "2019-01-02 12:00:00","timestamp"],
                  ["active_time", "222222","timestamp"],
                  ["timestamp", "2019-01-03 12:00:00","timestamp"],
                  ["activity_type", "walking","walking"],
                  ["distance", 1000.10,"walking"],
                  ["duration_min", 953,"walking"],
                  ["steps", 1500,"walking"],
                  ["timestamp", "2019-01-04 12:00:00","timestamp"],
                  ["activity_type", "running","running"],
                  ["distance", 2000.20,"running"],
                  ["duration_min", 953,"running"],
                  ["steps", 2500,"running"]]


    record_array = []

    for item in input_data:
        record = RecordC()
        record.name = item[0]
        record.value = item[1]
        record_array.append(record)

    i = 0
    for i,item in enumerate(record_array):
        fitparser_steps._record = item
        fitparser_steps.run()
        print(str(i) + " state: " + str(fitparser_steps.state) + " org_state: " + str(input_data[i][2]))
        assert fitparser_steps.state == input_data[i][2]

    pass