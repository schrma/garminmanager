import logging
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets

_logger = logging.getLogger(__name__)


class PlotC:

    def __init__(self, loglevel=logging.INFO,main_window=[],layout=[]):
        _logger.setLevel(loglevel)
        _logger.debug("Init: %s", os.path.basename(__file__))
        self._x_array = []
        self._y_array = []
        self._label_array = []
        self._settings = []
        self.COLORS = ["blue","red","green"]


        if main_window != [] and layout != []:
            self._b_is_qt = 'True'
            dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
            self._dynamic_canvas = dynamic_canvas
            # self._figuerHost = host_subplot(111,figure=dynamic_canvas.figure)
            # self._figuerHost = host_subplot(111,figure=dynamic_canvas.figure,axes_class=AA.Axes)
            layout.addWidget(dynamic_canvas)
            main_window.addToolBar(QtCore.Qt.BottomToolBarArea, NavigationToolbar(dynamic_canvas, main_window))
            self._ax = dynamic_canvas.figure.subplots()
            dynamic_canvas.figure.subplots_adjust(left=0.05, bottom=0.3, right=0.9, top=0.9, wspace=0, hspace=0)
            self._fig = dynamic_canvas.figure
        else:
            self._b_is_qt = 'False'
            fig, ax = plt.subplots(1, figsize=(8, 6))
            self._fig = fig
            self._ax = ax

    def set_settings(self,settings):
        self._settings = settings

    def add_plot_data(self,x,y,label=[]):
        self._x_array.append(x)
        self._y_array.append(y)
        self._label_array.append(label)

    def plot_adjust(self,left=0.05, bottom=0.3, right=0.9, top=0.9, wspace=0, hspace=0):
        self._fig.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)
        self._fig.canvas.draw()

    def clear(self):
        self._x_array = []
        self._y_array = []

    def show(self):

        if self._settings == []:
            _logger.warning("Please set settings")
            return

        self._ax.clear()

        for i, item in enumerate(self._x_array):
            self._ax.plot(item, self._y_array[i], marker = "x", linestyle = 'None', color=self.COLORS[i], label = self._label_array[i])

        self._ax.legend()
        if self._settings._title != []:
            self._ax.set_title(self._settings._title)

        if self._settings._x_limit != []:
            self._ax.set_xlim(self._settings._x_limit[0],self._settings._x_limit[1])

        if self._settings._y_limit != []:
            self._ax.set_ylim(self._settings._y_limit[0],self._settings._y_limit[1])

        if self._settings._x_label != []:
            self._ax.set_xlabel(self._settings._x_label)

        if self._settings._y_label != []:
            self._ax.set_ylabel(self._settings._y_label)

        self._ax.xaxis.set_major_formatter(mdates.DateFormatter('%a-%d-%Hh'))
        self._ax.grid(True)

        self._fig.canvas.draw()

        # plt.legend()
        # plt.show()



