import numpy as np
import datetime
import logging
import os
_logger = logging.getLogger(__name__)

class xyC:

    def __init__(self):
        self.x = []
        self.y = []

    def encode_to_json(self):
        return "{\"" + str(self.x) + "\": " + str(self.y) + "}"

class RawDataC(object):
    def __init__(self,loglevel=logging.INFO):
        _logger.setLevel(loglevel)
        _logger.debug("Init: %s", os.path.basename(__file__))
        self.x_array = []
        self.y_array = []
        self._process_type = []
        self._xy_array = []
        self._b_class_is_updated = True
        self._b_array_is_updated = True

    def clear_data(self):
        self._b_class_is_updated = True
        self._b_array_is_updated = True
        self.x_array = []
        self.y_array = []
        self._xy_array = []

    def set_data_type(self,my_type):
        self._process_type = my_type

    def get_data_type(self):
        return self._process_type

    def add_x(self, x):
        self._b_class_is_updated = False
        self._update_array_data()
        a = self.x_array
        self.x_array = np.append(a, x)

    def add_y(self, y):
        self._b_class_is_updated = False
        self._update_array_data()
        a = self.y_array
        self.y_array = np.append(a, y)

    def add_xy(self,x,y):
        self._b_array_is_updated = False
        self._update_class_data()
        a = self._xy_array
        m = xyC()
        m.x = x
        m.y = y
        a = np.append(a,m)
        self._xy_array = a

    def get_x(self):
        self._update_array_data()
        return self.x_array

    def get_y(self):
        self._update_array_data()
        return self.y_array

    def _update_class_data(self):
        _logger.info("Update class")
        if not self._b_class_is_updated:
            r = []
            i = 0
            for x in self.x_array:
                try:
                    m = xyC()
                    m.x = x
                    m.y = self.y_array[i]
                    r = np.append(r, m)
                    print(str(x) + ": " + str(self.y_array[i]))
                    i = i + 1
                except IndexError:
                    print("Index not available")
            self._xy_array = r
            self._b_class_is_updated = True

    def _update_array_data(self):
        _logger.info("update array")
        raw_data_class = self._xy_array

        if not self._b_array_is_updated:
            self.x_array = []
            self.y_array = []
            i = 0
            for item in raw_data_class:
                self.x_array = np.append(self.x_array, item.x)
                self.y_array = np.append(self.y_array, item.y)

            self._b_array_is_updated = True

    def get_xy_data(self):
        self._update_class_data()
        return self._xy_array

    def __eq__(self, other):
        x = self.get_x()
        y = self.get_y()
        ox = other.get_x()
        oy = other.get_y()
        if type(x[0]) is datetime.datetime:
            i = 0
            for item in x:
                if not (item == ox[i]):
                    return False
                i = i + 1
        else:
            if not (x == ox).all():
                return False
        if not (y == oy).all():
            return False
        if not self._process_type == other._process_type:
            return False
        return True


    def print_data(self):
        xarray = self.get_x()
        yarray = self.get_y()
        i = 0
        for x in xarray:
            try:
                print(str(x) + ": " + str(yarray[i]))
                i = i + 1
            except IndexError:
                print("Index not available")




