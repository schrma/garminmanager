import logging
import os
import json

import garminmanager.RawDataC

_logger = logging.getLogger(__name__)


class FileWriterC:

    def __init__(self, loglevel=logging.INFO):
        _logger.setLevel(loglevel)
        _logger.debug("Init: %s", os.path.basename(__file__))
        self._raw_data_array = []
        self._text = []

    def set_data(self,data):
        self._raw_data_array = data

    def set_filename(self,name):
        self._full_filename = name

    def set_text(self,text):
        self._text = text

    def write_text_to_file(self):
        fp = open(self._full_filename,"w")
        fp.write(self._text)
        fp.close()

    def read_json(self):
        with open(self._full_filename) as json_data:
            d = json.load(json_data)
        return d
