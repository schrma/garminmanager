import logging
import os
import json
import ntpath
import datetime

import garminmanager.RawDataC
import garminmanager.utils.JsonEncDecC
import garminmanager.utils.FileManagerC
import garminmanager.utils.JsonEncDecC
import garminmanager.filter.SettingsFilterC

_logger = logging.getLogger(__name__)


class CalculationFilterC:

    def __init__(self, loglevel=logging.INFO):
        _logger.setLevel(loglevel)
        _logger.debug("Init: %s", os.path.basename(__file__))
        self._input_data = []
        self._output_data = garminmanager.RawDataC.RawDataC()
        self._settings = garminmanager.filter.SettingsFilterC.SettingsFilterC()

    def set_input_data(self,input_data):
        self._input_data = input_data

    def get_output_data(self):
        return self._output_data

    def process(self):
        input_data = self._input_data
        my_set = self._settings
        self._output_data.set_data_type(input_data.get_data_type())
        for item in input_data.get_xy_data():
            if item.y >= my_set.min and item.y <= my_set.max:
                self._output_data.add_xy(item.x,item.y)


    def set_settings(self,settings):
        self._settings = settings
