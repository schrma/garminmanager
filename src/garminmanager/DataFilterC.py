import logging
import os
from datetime import datetime
import datetime
import numpy as np
import copy

import garminmanager.RawDataC

_logger = logging.getLogger(__name__)


class DataFilerC:

    def __init__(self, loglevel=logging.INFO):
        _logger.setLevel(loglevel)
        _logger.debug("Init: %s", os.path.basename(__file__))
        self._time_range_hour = 24
        self._raw_data_array = []
        self._raw_data = garminmanager.RawDataC.RawDataC()

    def set_data(self,data):
        self._raw_data = data

    def set_time_range_in_hour(self,my_range):
        self._time_range_hour = my_range

    def process(self):
        first_date = self._raw_data.x_array[0]
        my_range = self._time_range_hour

        start_point = self._get_starting_day(first_date)
        end_point = start_point + datetime.timedelta(hours=my_range)
        temp_raw_data = garminmanager.RawDataC.RawDataC()
        raw_data_class = self._raw_data.get_xy_data()
        temp_raw_dataArray = []
        print("--------------------------" + str(start_point))
        for item in raw_data_class:
            if item.x < end_point:
                temp_raw_data.add_xy(item.x,item.y)
                print(str(item.x) + ": " + str(item.y))
            else:
                temp_raw_dataArray = np.append(temp_raw_dataArray,temp_raw_data)
                temp_raw_data = garminmanager.RawDataC.RawDataC()
                temp_raw_data.add_xy(item.x, item.y)
                print("--------------------------" + str(end_point))
                end_point = end_point + datetime.timedelta(hours=my_range)

        self._raw_data_array = np.append(temp_raw_dataArray, temp_raw_data)
        print("hello")

    def _get_starting_day(self,mydate):
        dt = mydate.replace(hour=0, minute=0, second=0, microsecond=0)
        return dt

    def get_data(self):
        return self._raw_data_array

