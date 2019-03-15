import numpy as np
import datetime

class xyC:

    def __init__(self):
        self.x = []
        self.y = []

    def encode_to_json(self):
        return "{\"" + str(self.x) + "\": " + str(self.y) + "}"

class RawDataC(object):
    def __init__(self):
        self.x_array = []
        self.y_array = []
        self._process_type = []
        self._xy_array = []
        self._b_class_is_updated = False
        self._b_array_is_updated = False

    def clear_data(self):
        self._b_class_is_updated = False
        self._b_array_is_updated = False
        self.x_array = []
        self.y_array = []
        self._xy_array = []

    def set_data_type(self,my_type):
        self._process_type = my_type

    def add_x(self, x):
        self._b_class_is_updated = False
        a = self.x_array
        self.x_array = np.append(a, x)

    def add_y(self, y):
        self._b_class_is_updated = False
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
        self._update_array_data()

    def _update_class_data(self):
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
        raw_data_class = self._xy_array
        self.x_array = []
        self.y_array = []
        if not self._b_array_is_updated:

            i = 0
            for item in raw_data_class:
                self.x_array = np.append(self.x_array, item.x)
                self.y_array = np.append(self.y_array, item.y)

            self._b_array_is_updated = True

    def get_xy_data(self):
        self._update_class_data()
        return self._xy_array

    def __eq__(self, other):
        if type(self.x_array[0]) is datetime.datetime:
            i = 0
            for item in self.x_array:
                if not (item == other.x_array[i]):
                    return False
                i = i + 1
        else:
            if not (self.x_array == other.x_array).all():
                return False
        if not (self.y_array == other.y_array).all():
            return False
        if not self._process_type == other._process_type:
            return False
        return True


    def print_data(self):
        self._update_array_data()
        i = 0
        for x in self.x_array:
            try:
                print(str(x) + ": " + str(self.y_array[i]))
                i = i + 1
            except IndexError:
                print("Index not available")

    def add_spaces(self,spaces):
        str_spaces = ""
        for i in range(spaces):
            str_spaces += " "
        return str_spaces

    def encode_to_json(self,space_offset=0):
        self._update_class_data()
        sp = space_offset
        json_string = self.add_spaces(2+sp) + "\"_xy_array\" : [\n" + self.add_spaces(4+sp)
        i = 0
        for item in self._xy_array:
            if i == 0:
                pass
            else:
                json_string += ",\n" + self.add_spaces(4+sp)
            json_string += item.encode_to_json()
            i += 1
        json_string += "\n" + self.add_spaces(2+sp) + "]\n}"

        json_string += self.add_spaces(2+sp) + "\"process_type\" : " + str(self._process_type)
        json_string += self.add_spaces(2 + sp) + "\"date\" : " + str(self._process_type)
        return json_string



