import numpy as np

class RawDataC():
    def __init__(self):
        self.timestamp_array = []
        self.data_array = []
        self._process_type = []

    def clear_data(self):
        self.timestamp_array = []
        self.data_array = []

    def set_data_type(self,my_type):
        self._process_type = my_type

    def add_timestamp(self,x):
        a = self.timestamp_array
        self.timestamp_array = np.append(a,x)

    def add_data(self,y):
        a = self.data_array
        self.data_array = np.append(a, y)

    def print_data(self):
        i = 0
        for x in self.timestamp_array:
            try:
                print(str(x) + ": " + str(self.data_array[i]))
                i = i + 1
            except IndexError:
                print("Index not available")