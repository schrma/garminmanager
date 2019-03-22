import garminmanager.ui.PlotC
import garminmanager.ui
import garminmanager.ui.Version_auto
import garminmanager.ui.MainGui
import garminmanager.ui.PlotSettingsC

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import argparse
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

def test_qt():
    print("STart")

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    Dialog = QtWidgets.QDialog()
    DialogInterface = garminmanager.ui.Version_auto.Ui_Dialog()
    gui = garminmanager.ui.MainGui.MainWindow(Dialog, DialogInterface)
    gui.setupUi(MainWindow)
    layout = QtWidgets.QVBoxLayout(gui.widget)

    settings = garminmanager.ui.PlotSettingsC.PlotSettingsC()

    settings._title = 'My Title 1'
    settings._x_limit = [0,100]
    my_plot = garminmanager.ui.PlotC.PlotC(main_window=MainWindow,layout=layout)
    my_plot.set_settings(settings)
    my_plot.add_plot_data([1,2,3],[4,5,7],"first")
    my_plot.add_plot_data([1,2,3],[10,22,23],"seccond")
    my_plot.show()
    MainWindow.show()
    my_plot.plot_adjust(left=0.2)
    settings._title = 'My Title 2'
    settings._x_limit = [0,10]
    my_plot.show()





    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # Dialog = QtWidgets.QDialog()
    # DialogInterface = garminmanager.ui.Version_auto.Ui_Dialog()
    # DialogInterface.setupUi(Dialog)
    # gui = garminmanager.ui.MainGui.MainWindow(Dialog, DialogInterface)
    # gui.setupUi(MainWindow)
    # gui.register_signals(MainWindow)
    # gui.PrepareApplication()
    # MainWindow.show()
    #
    # layout = QtWidgets.QVBoxLayout(gui.widget)
    # dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
    # # self._figuerHost = host_subplot(111,figure=dynamic_canvas.figure)
    # # self._figuerHost = host_subplot(111,figure=dynamic_canvas.figure,axes_class=AA.Axes)
    # layout.addWidget(dynamic_canvas)
    # MainWindow.addToolBar(QtCore.Qt.BottomToolBarArea, NavigationToolbar(dynamic_canvas, MainWindow))
    # dynamic_ax = dynamic_canvas.figure.subplots()
    # dynamic_ax.plot([1,2,3],[1,2,3], color="red", label="test")
    # dynamic_canvas.figure.subplots_adjust(left=0.05, bottom=0.3, right=0.9, top=0.9, wspace=0, hspace=0)
    # sys.exit(app.exec_())

def test_plot():
    my_plot = garminmanager.ui.PlotC.PlotC()
    settings = garminmanager.ui.PlotSettingsC.PlotSettingsC()
    settings._title = 'My Title 1'
    settings._x_limit = [0,20]
    my_plot.set_settings(settings)
    my_plot.add_plot_data([1,2,3],[4,5,7],"first")
    my_plot.add_plot_data([1,2,3],[10,22,23],"seccond")
    my_plot.show()
    print("hello")


