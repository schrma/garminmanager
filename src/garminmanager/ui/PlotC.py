import logging
import os
import matplotlib.pyplot as plt
import numpy as np

_logger = logging.getLogger(__name__)


class PlotC:

    def __init__(self, loglevel=logging.INFO):
        _logger.setLevel(loglevel)
        _logger.debug("Init: %s", os.path.basename(__file__))
        self._x_array = []
        self._y_array = []
        self._label_array = []
        fig, ax = plt.subplots(1, figsize=(8, 6))
        self._fig = fig
        self._ax = ax
        self.COLORS = ["blue","red","green"]

    def add_plot_data(self,x,y,label=[]):
        self._x_array.append(x)
        self._y_array.append(y)
        self._label_array.append(label)

    def show(self):

        for i, item in enumerate(self._x_array):
            self._ax.plot(item, self._y_array[i], color=self.COLORS[i], label = self._label_array[i])

        plt.legend()
        plt.show()



