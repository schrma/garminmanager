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
                  ["duration_min", 100,"walking"],
                  ["steps", 10,"walking"],
                  ["timestamp", "2019-01-03 13:00:00", "timestamp"],
                  ["activity_type", "walking", "walking"],
                  ["distance", 1000.20, "walking"],
                  ["duration_min", 200, "walking"],
                  ["steps", 20, "walking"],
                  ["timestamp", "2019-01-04 12:00:00","timestamp"],
                  ["activity_type", "running","running"],
                  ["distance", 2000.20,"running"],
                  ["duration_min", 300,"running"],
                  ["steps", 30,"running"]]


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
        input_name = input_data[i][0]
        input_value = input_data[i][1]
        state_org = str(input_data[i][2])
        print(str(i) + " state: " + str(fitparser_steps.state) + " org_state: " + state_org)
        assert fitparser_steps.state == state_org

        if input_name == "timestamp":
            current_time_stamp = input_value

        if input_name == "distance" and state_org == 'walking':
            check_data(fitparser_steps._raw_data_walking_distance,current_time_stamp,input_value)

        if input_name == "distance" and state_org == 'running':
            check_data(fitparser_steps._raw_data_running_distance,current_time_stamp,input_value)

        if input_name == "steps" and state_org == 'running':
            check_data(fitparser_steps._raw_data_running_steps,current_time_stamp,input_value)

        if input_name == "steps" and state_org == 'walking':
            check_data(fitparser_steps._raw_data_walking_steps,current_time_stamp,input_value)



def check_data(inputdata,current_time_stamp,value):
    x = inputdata.get_x()
    assert x[-1] == current_time_stamp
    y = inputdata.get_y()
    assert y[-1] == value