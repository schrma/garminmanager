import logging
import os
import json

import garminmanager.RawDataC
import garminmanager.utils.JsonEncDecC

_logger = logging.getLogger(__name__)


class FileWriterC:

    def __init__(self, loglevel=logging.INFO):
        _logger.setLevel(loglevel)
        _logger.debug("Init: %s", os.path.basename(__file__))
        self._raw_data_array = []
        self._text = []
        self._folder = []

    def set_data(self,data):
        self._raw_data_array = data

    def set_filename(self,name):
        self._full_filename = name

    def set_folder(self,folder):
        self._folder = folder

    def set_text(self,text):
        self._text = text

    def write(self):

        for raw_data in self._raw_data_array:
            if raw_data.x_array == [] or raw_data.y_array == [] or raw_data._process_type == []:
                _logger.error("Rawdata is empty")
                return
            json_enc_dec = garminmanager.utils.JsonEncDecC.JsonEncDecC()
            json_enc_dec.set_input_data(raw_data)
            json_string = json_enc_dec.encode()
            filename = str(raw_data.x_array[0]).replace(" ", "_") + str(raw_data.x_array[-1]).replace(" ", "_") + ".json"
            filename = filename.replace(":","-")
            filename = self._folder + "/" + filename
            self._full_filename = filename
            self.set_text(json_string)
            self.write_text_to_file()

    def write_text_to_file(self):
        fp = open(self._full_filename,"w")
        fp.write(self._text)
        fp.close()

    def read_json(self):
        with open(self._full_filename) as json_data:
            d = json.load(json_data)
        return d
