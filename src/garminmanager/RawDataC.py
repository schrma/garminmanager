import numpy as np
import datetime

class xyC:

    def __init__(self):
        self.x = []
        self.y = []

class RawDataC(object):
    def __init__(self):
        self.timestamp_array = []
        self.data_array = []
        self._process_type = []
        self._xyArray = []
        self._b_class_is_updated = False
        self._b_array_is_updated = False

    def clear_data(self):
        self._b_class_is_updated = False
        self._b_array_is_updated = False
        self.timestamp_array = []
        self.data_array = []
        self._xyArray = []

    def set_data_type(self,my_type):
        self._process_type = my_type

    def add_timestamp(self,x):
        self._b_class_is_updated = False
        a = self.timestamp_array
        self.timestamp_array = np.append(a,x)

    def add_data(self,y):
        self._b_class_is_updated = False
        a = self.data_array
        self.data_array = np.append(a, y)

    def add_xy(self,x,y):
        self._b_array_is_updated = False
        self._update_class_data()
        a = self._xyArray
        m = xyC()
        m.x = x
        m.y = y
        a = np.append(a,m)
        self._xyArray = a
        self._update_array_data()

    def _update_class_data(self):
        if not self._b_class_is_updated:
            r = []
            i = 0
            for x in self.timestamp_array:
                try:
                    m = xyC()
                    m.x = x
                    m.y = self.data_array[i]
                    r = np.append(r, m)
                    print(str(x) + ": " + str(self.data_array[i]))
                    i = i + 1
                except IndexError:
                    print("Index not available")
            self._xyArray = r
            self._b_class_is_updated = True

    def _update_array_data(self):
        raw_data_class = self._xyArray
        self.timestamp_array = []
        self.data_array = []
        if not self._b_array_is_updated:

            i = 0
            for item in raw_data_class:
                self.timestamp_array = np.append(self.timestamp_array,item.x)
                self.data_array = np.append(self.data_array,item.y)

            self._b_array_is_updated = True

    def get_xy_data(self):
        self._update_class_data()
        return self._xyArray

    def __eq__(self, other):
        if type(self.timestamp_array[0]) is datetime.datetime:
            i = 0
            for item in self.timestamp_array:
                if not (item == other.timestamp_array[i]):
                    return False
                i = i + 1
        else:
            if not (self.timestamp_array == other.timestamp_array).all():
                return False
        if not (self.data_array == other.data_array).all():
            return False
        if not self._process_type == other._process_type:
            return False
        return True


    def print_data(self):
        self._update_array_data()
        i = 0
        for x in self.timestamp_array:
            try:
                print(str(x) + ": " + str(self.data_array[i]))
                i = i + 1
            except IndexError:
                print("Index not available")