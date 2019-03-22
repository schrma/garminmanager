import logging
import os
import json
import ntpath
import datetime

import garminmanager.RawDataC
import garminmanager.utils.JsonEncDecC
import garminmanager.utils.FileManagerC
import garminmanager.utils.JsonEncDecC

_logger = logging.getLogger(__name__)


class FileWriterC:

    def __init__(self, loglevel=logging.INFO):
        _logger.setLevel(loglevel)
        _logger.debug("Init: %s", os.path.basename(__file__))
        self._raw_data_array = []
        self._text = []
        self._folder = []
        self._start_date = []
        self._end_date = []
        self._full_filename = []

    def set_intervall(self,start,stop):
        self._start_date = start
        self._end_date = stop

    def set_data(self,data):
        self._raw_data_array = data

    def set_filename(self,name):
        self._full_filename = name

    def set_folder(self,folder):
        file_manger = garminmanager.utils.FileManagerC.FilemManagerC()
        file_manger.create_folder(folder)
        self._folder = folder

    def set_text(self,text):
        self._text = text

    def read(self):
        file_manager = garminmanager.utils.FileManagerC.FilemManagerC()
        file_manager.process_get_file_list(self._folder)
        file_list = file_manager.get_file_list()
        file_list_intervall = []
        json_enc_dec = garminmanager.utils.JsonEncDecC.JsonEncDecC()
        for item in file_list:
            filename = ntpath.basename(item)
            datetime_file = datetime.datetime.strptime(filename[0:10], '%Y-%m-%d')
            if datetime_file >= self._start_date and datetime_file <= self._end_date:
                file_list_intervall.append(item)

        raw_data_output = garminmanager.RawDataC.RawDataC()
        for item in file_list_intervall:
            self.set_filename(item)
            d = self.read_json()
            json_enc_dec.set_input_json(d)
            json_enc_dec.decode()
            raw_data_temp = json_enc_dec.get_data()
            raw_data_output = raw_data_output + raw_data_temp

        return raw_data_output


    def write(self):

        for raw_data in self._raw_data_array:

            x = raw_data.get_x()
            y = raw_data.get_y()

            if x == [] or y == [] or raw_data._process_type == []:
                _logger.error("Rawdata is empty")
                return
            json_enc_dec = garminmanager.utils.JsonEncDecC.JsonEncDecC()
            json_enc_dec.set_input_data(raw_data)
            json_string = json_enc_dec.encode()
            filename = str(x[0]).replace(" ", "_") + str(x[-1]).replace(" ", "_") + ".json"
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
