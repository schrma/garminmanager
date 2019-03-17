import logging
import os
import json
import datetime

import garminmanager.RawDataC
from garminmanager.enumerators.EnumHealthTypeC import EnumHealtTypeC

_logger = logging.getLogger(__name__)


class JsonEncDecC:

    def __init__(self, loglevel=logging.INFO):
        _logger.setLevel(loglevel)
        _logger.debug("Init: %s", os.path.basename(__file__))
        self._raw_data_array = []
        self._text = []
        self._input_data = []
        self._output_data = []
        self._input_json = []
        self._sw_version = "1.0.0"

        self.CLASS_TYPE_TAG = "ClassType"
        self.VERSION_TAG = "Version"
        self.XY_ARRAY_TAG = "XY-Value"
        self.PROCESS_TYPE_TAG = "ProcessType"

    def set_input_data(self,data):
        self._input_data = data

    def set_input_json(self,input):
        self._input_json = input

    def encode(self):

        data = self._input_data

        if data.x_array == [] or data.y_array == [] or data._process_type == []:
            _logger.error("Rawdata is empty")
            return ""

        json_string = "{\n"
        json_string += self.add_spaces(2) + "\"Version\" : \"" + self._sw_version + "\",\n"

        switch_options = {
            garminmanager.RawDataC.RawDataC: self._encode_raw_data
                          }

        try:
            json_string += switch_options[type(data)]()
        except:
            json_string += self._encode_default()

        json_string += "}\n"

        return json_string


    def _encode_default(self):
        print("Default encoder - no implemented yet")


    def _encode_raw_data(self):
        raw_data = self._input_data
        raw_data._update_class_data()
        sp = 0
        json_string = self.add_spaces(2 + sp) + "\"" + self.CLASS_TYPE_TAG + "\" : \"" + type(raw_data).__module__ + type(raw_data).__name__ + "\",\n"
        json_string += self.add_spaces(2 + sp) + "\"process_type\" : \"" + str(raw_data._process_type) + "\",\n"
        json_string += self.add_spaces(2 + sp) + "\"date\" : \"" + str(raw_data.x_array[0]) + "\",\n"
        json_string += self.add_spaces(2 + sp) + "\"_xy_array\" : [\n" + self.add_spaces(4 + sp)
        i = 0
        for item in raw_data._xy_array:
            if i == 0:
                pass
            else:
                json_string += ",\n" + self.add_spaces(4 + sp)
            json_string += item.encode_to_json()
            i += 1
        json_string += "\n" + self.add_spaces(2 + sp) + "]\n"


        return json_string

    def _select_encoder(self,classtype):
        self._decode_raw_data(classtype)

    def _decode_raw_data(self,classtype):
        data = self._input_json
        switch_options = {"_xy_array": self._fill_xy_array,
                          "process_type": self._fill_process_type,
                          }

        self._output_data = eval(classtype+"()")

        for key, value in data.items():
            print(key)
            print(value)
            try:
                switch_options[key](value)
            except:
                print("Warning. " + key + " not availble")


    def decode(self):

        data = self._input_json
        for key, value in data.items():
            print(key)
            print(value)
            if key == self.CLASS_TYPE_TAG:
                b_found_classtype = True

        if b_found_classtype:
            self._select_encoder("garminmanager.RawDataC.RawDataC")
        else:
            self._encode_default()

    def add_spaces(self, spaces):
        str_spaces = ""
        for i in range(spaces):
            str_spaces += " "
        return str_spaces

    def _fill_xy_array(self,value):
        print("hello world")
        raw_data = self._output_data
        for m in value:
            for x,y in m.items():
                conv_date = datetime.datetime.strptime(x,'%Y-%m-%d %H:%M:%S')
                raw_data.add_xy(conv_date,y)
        self._output_data = raw_data

    def _fill_date(self,value):
        print("hello world")

    def _fill_process_type(self,value):
        raw_data = self._output_data
        raw_data._process_type = eval(value)
        self._output_data = raw_data

    def get_data(self):
        return self._output_data

    def _fill_sw_version(self):
       print("sw-version")