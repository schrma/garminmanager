import logging
import os
import numpy as np

from datetime import datetime
import datetime

from fitparse import FitFile

from garminmanager.enumerators.EnumHealthTypeC import EnumHealtTypeC
import garminmanager.RawDataC

_logger = logging.getLogger(__name__)


class FitParserC:

    def __init__(self, loglevel=logging.INFO):
        self._file_list = []
        self._gmt_value_in_seconds = 3600
        self._raw_data = garminmanager.RawDataC.RawDataC()
        self._process_type = EnumHealtTypeC.heartrate
        _logger.setLevel(loglevel)
        _logger.debug("Init: %s", os.path.basename(__file__))

    def _get_value_of_first_occurence(self):
        pass

    def set_file_list(self, my_filelist):
        self._file_list = my_filelist

    def set_type(self, my_type):
        self._process_type = my_type

    def process(self):
        switch_options = {EnumHealtTypeC.heartrate: self._process_hearrate,
                          EnumHealtTypeC.intensity: self._process_intensity,
                          }

        my_type = self._process_type
        # switch_options = {1 : self.printB,
        #     2 : self.printA,
        # }

        try:
            switch_options[my_type]()
        except:
            print("C")

    def _process_intensity(self):
        print("Not implmented yet")
        _logger.warning("_process_intensity not yet implemented")

    def get_data(self):
        return self._raw_data

    def _parse_single_file(self,filename):
        fitfile = FitFile(filename)
        data = ""
        for record in fitfile.get_messages():

            # Go through all the data entries in this record
            for record_data in record:

                # Print the records name and value (and units if it has any)
                if record_data.units:
                    # tempText = record_data.name + " " + record_data.value + " " + record_data.units
                    data += "U->{0:s},{1:s}\n".format(record_data.name, str(record_data.value), str(record_data.units))
                elif record_data.value:
                    data += "V->{0:s},{1:s}\n".format(record_data.name, str(record_data.value))
                else:
                    data += "N->{0:s}\n".format(record_data.name)
                    # f.write(tempText)k

        return data

    def parse_file(self):
        filename_list = self._file_list
        if not filename_list:
            _logger.error("Filelist is empty")
            return
        data = ""
        for filename in filename_list:
            data += self._parse_single_file(filename)

        return str(data)


    def _process_hearrate(self):

        filename_list = self._file_list
        if not filename_list:
            _logger.error("Filelist is empty")
            return
        self._raw_data.clear_data()
        self._raw_data.set_data_type(EnumHealtTypeC.heartrate)
        self.set_type(EnumHealtTypeC.heartrate)
        for filename in filename_list:
            self._process_hearrate_single_file(filename)

    def _process_hearrate_single_file(self, filename):
        my_pattern_x = 'timestamp_16'
        my_pattern_y = 'heart_rate'
        my_pattern_time = 'timestamp'
        try:
            fitfile = FitFile(filename)
        except:
            _logger.error("File %s not found", filename)
            return

        # to_zone = tz.tzutc()
        save_i = -1
        i = 0
        last_timestamp_16 = -1
        first_timestamp_16 = []
        b_is_first_timestamp = True
        b_is_first_timestamp_16 = True
        timestamp_base = []
        try:
            for record in fitfile.get_messages():
                # Go through all the data entries in this record
                for record_data in record:
                    if record_data.name == my_pattern_time:
                        if b_is_first_timestamp:
                            timestamp_base = record_data.value
                            b_is_first_timestamp = False
                    elif record_data.name == my_pattern_y:
                        if record_data.value < 40:
                            self._raw_data.add_y(np.nan)
                        else:
                            self._raw_data.add_y(record_data.value)
                        save_i = i
                    elif (record_data.name == my_pattern_x) and (i == save_i + 1):
                        if record_data.value > last_timestamp_16:
                            if b_is_first_timestamp_16:
                                x_time = timestamp_base + datetime.timedelta(seconds=self._gmt_value_in_seconds)
                                self._raw_data.add_x(x_time)
                                first_timestamp_16 = record_data.value
                                b_is_first_timestamp_16 = False
                            else:
                                x_time = timestamp_base + datetime.timedelta(
                                    seconds=record_data.value - first_timestamp_16 + self._gmt_value_in_seconds)
                                self._raw_data.add_x(x_time)
                            last_timestamp_16 = record_data.value
                        else:
                            x_time = timestamp_base + datetime.timedelta(
                                seconds=record_data.value + pow(2,
                                                                16) - first_timestamp_16 + self._gmt_value_in_seconds)
                            self._raw_data.add_x(x_time)
                            last_timestamp_16 = record_data.value + pow(2, 16)
                    i = i + 1
        except:
            print("Error")
            pass

        return self._raw_data
