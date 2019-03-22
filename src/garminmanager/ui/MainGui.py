from garminmanager.ui.MainGui_auto import *
import os
import time
from os import listdir
from os.path import isfile, join

from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QDir

#from FitParserC import *
#from myTypes.xyPairC import xyPairC
import matplotlib.dates as mdates

import matplotlib
matplotlib.use('QT5Agg')
import numpy as np
from dateutil import tz
import matplotlib.pylab as plt
import json
import shutil
import garminmanager.utils.FileManagerC
import garminmanager.FitParserC
from garminmanager.enumerators.EnumHealthTypeC import EnumHealtTypeC
import garminmanager.DataFilterC
import garminmanager.utils.FileWriterC
import garminmanager.filter.SettingsFilterC
import garminmanager.ui.PlotSettingsC
import garminmanager.filter.CalculationFilterC
import logging

_logger = logging.getLogger(__name__)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

class MainWindow(Ui_MainWindow):

    def __init__(self,Dialog=[],DialogInterface=[]):
        _logger.setLevel(logging.DEBUG)
        _logger.debug("Init: %s", os.path.basename(__file__))
        self._figure = []
        self._Dialog = Dialog
        self._DialogInterface = DialogInterface
        self._settings = {"watch_folder": "d:/GARMIN",
                    "activity_folder": "c:/Users/schrma/ownCloud/leica/fitfolder",
                    "activity_folder": "c:/Users/schrma/ownCloud/leica/fitfolder",
                    "json_folder": "c:/Users/schrma/ownCloud/leica/fitfolder",
                    "backup_folder": "c:/Users/schrma/ownCloud/leica/fitfolder/backup"}
        self._file_list_fit = []
        self.cal_filter_settings =  garminmanager.filter.SettingsFilterC.SettingsFilterC()
        self.plot_settings = garminmanager.ui.PlotSettingsC.PlotSettingsC()

    def PrepareApplication(self):
        with open("./settings.json", 'r') as read_file:
            self._settings = json.load(read_file)
        self._show_text_tb()


        # Right place for image in label
        self.label_fenix_pic.setPixmap(QtGui.QPixmap("./src/garminmanager/images/fenix3.jpg"))

    def _show_text_tb(self):
        try:
            self.text_tb.clear()
            self.text_tb.append("Monitor folder:")
            self.text_tb.append(self._settings["monitor_folder"])
            self.text_tb.append("Activity folder:")
            self.text_tb.append(self._settings["activity_folder"])
            self.text_tb.append("BackupFolder:")
            self.text_tb.append(self._settings["backup_folder"])
            self.text_tb.append("Watch Folder:")
            self.text_tb.append(self._settings["watch_folder"])
            self.text_tb.append("Json Folder:")
            self.text_tb.append(self._settings["json_folder"])
        except:
            pass

    def register_signals(self,MainWindow):

        self.test_pb.clicked.connect(self.fit_to_database)
        self.process_pb.clicked.connect(self.process)
        self.ParseToFileButton.clicked.connect(self.ParseAndWrite)
        self.backup_pb.clicked.connect(self.backup_data)
        self.data_from_watch_pb.clicked.connect(self.get_data_from_watch)
        self.actionVersion.triggered.connect(self.TestFunction)
        self.save_settings_pb.clicked.connect(self.save_settings)
        self.load_settings_pb.clicked.connect(self.load_settings)
        self.set_folders_pb.clicked.connect(self.set_folder)
        self.start_de.dateChanged.connect(self.start_date_changed)
        self.end_de.dateChanged.connect(self.end_date_changed)

        data = np.array([0.7, 0.7, 0.7, 0.8, 0.9, 0.9, 1.5, 1.5, 1.5, 1.5])
        self._DialogInterface.labelPciture.setPixmap(QtGui.QPixmap("./images/fenix3.jpg"))
        self._DialogInterface.VersionLabel.setText("Version: 2.0.0")

        self._start_date_time = self.start_de.dateTime().toPyDateTime()
        self._end_date_time = self.end_de.dateTime().toPyDateTime()
        # self._figure = plt.figure()
        # ax1 = self._figure.add_subplot(111)
        # bins = np.arange(0.6, 1.62, 0.02)
        # n1, bins1, patches1 = ax1.hist(data, bins, alpha=0.6, density=False, cumulative=False)
        # # plot
        # self.plotWidget = FigureCanvas(self._figure)
        layout = QtWidgets.QVBoxLayout(self.widget)
        dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self._dynamic_canvas = dynamic_canvas
        #self._figuerHost = host_subplot(111,figure=dynamic_canvas.figure)
        #self._figuerHost = host_subplot(111,figure=dynamic_canvas.figure,axes_class=AA.Axes)
        layout.addWidget(dynamic_canvas)
        MainWindow.addToolBar(QtCore.Qt.BottomToolBarArea,NavigationToolbar(dynamic_canvas, MainWindow))
        self._dynamic_ax = dynamic_canvas.figure.subplots()
        dynamic_canvas.figure.subplots_adjust(left=0.05 , bottom=0.3, right=0.9, top=0.9  , wspace=0, hspace=0)

    def register_callback_on_submit(self, call_back):
        self._on_submit_callback = call_back

    def start_date_changed(self):
        self._start_date_time = self.start_de.dateTime().toPyDateTime()

    def end_date_changed(self):
        self._end_date_time = self.end_de.dateTime().toPyDateTime()

    def load_settings(self):
        _logger.info("load settings ...")
        json_file = self._get_file()
        with open(json_file, 'r') as read_file:
            self._settings = json.load(read_file)
        self._show_text_tb()

    def save_settings(self):
        _logger.info("save settings")
        current_path = os.getcwd()
        filename = current_path + "/" + "settings.json"
        self.statusbar.showMessage("Saved in " + filename)
        with open(filename, "w") as write_file:
            json.dump(self._settings, write_file)

    def set_folder(self):
        _logger.info("set folder")
        _logger.info("Folder: " + self.folder_cb.currentText())

        selected_folder = self._get_folder()
        selected_index =  self.folder_cb.currentIndex()

        if selected_index == 0:
            self._settings["monitor_folder"] = selected_folder
        elif selected_index == 1:
            self._settings["activity_folder"] = selected_folder
        elif selected_index == 2:
            self._settings["backup_folder"] = selected_folder
        elif selected_index == 3:
            self._settings["watch_folder"] = selected_folder
        elif selected_index == 4:
            self._settings["json_folder"] = selected_folder
        else:
            _logger.error("Index out of range: " + str(selected_index))

        self._show_text_tb()


    def get_data_from_watch(self):
        file_handler = garminmanager.utils.FileManagerC.FilemManagerC()

        file_handler = garminmanager.utils.FileManagerC.FilemManagerC()
        src_folder = self._settings["watch_folder"] + "/ACTIVITY"
        file_handler.set_src_folder(src_folder)
        dest_folder = self._settings["activity_folder"]
        file_handler.set_dst_folder(dest_folder)
        file_handler.copy()
        src_folder = self._settings["watch_folder"] + "/MONITOR"
        file_handler.set_src_folder(src_folder)
        dest_folder = self._settings["monitor_folder"]
        file_handler.copy()

        self._file_list_fit = file_handler.get_file_list()

    def fit_to_database(self):

        sc = garminmanager.utils.FileManagerC.FilemManagerC(loglevel=logging.DEBUG)
        sc.process_get_file_list(self._settings["monitor_folder"])
        file_list = sc.get_file_list()

        # ParseData
        fit_parser = garminmanager.FitParserC.FitParserC()
        fit_parser.set_file_list(file_list)
        fit_parser.set_type(EnumHealtTypeC.heartrate)
        fit_parser.process()
        raw_data = fit_parser.get_data()
        datafilter = garminmanager.DataFilterC.DataFilerC()
        datafilter.set_data(raw_data)
        datafilter.set_time_range_in_hour(24)
        try:
            datafilter.process()
        except:
            _logger.warning("Problem with data filter")
            return
        raw_data_array = datafilter.get_data()

        file_writer = garminmanager.utils.FileWriterC.FileWriterC()
        file_writer.set_data(raw_data_array)
        folder = self._settings["json_folder"] + "/" + str()
        file_writer.set_folder(folder)
        file_writer.write()


    def transfer_to_database(self):

        self.get_data_from_watch()

        # ParseData
        fit_parser = garminmanager.FitParserC.FitParserC()
        fit_parser.set_file_list(self._file_list_fit)
        fit_parser.set_type(EnumHealtTypeC.heartrate)
        fit_parser.process()
        raw_data = fit_parser.get_data()
        datafilter = garminmanager.DataFilterC.DataFilerC()
        datafilter.set_data(raw_data)
        datafilter.set_time_range_in_hour(24)
        datafilter.process()
        raw_data_array = datafilter.get_data()

        file_writer = garminmanager.utils.FileWriterC.FileWriterC()
        file_writer.set_data(raw_data_array)
        file_writer.set_folder("./writerTest")
        file_writer.write()

    def prepare_data(self):
        file_writer = garminmanager.utils.FileWriterC.FileWriterC()

        file_writer.set_intervall(self._start_date_time,self._end_date_time)
        file_writer.set_folder(self._settings["json_folder"])
        raw_out = file_writer.read()
        calculation_filter = garminmanager.filter.CalculationFilterC.CalculationFilterC()

        calculation_filter.set_input_data(raw_out)
        calculation_filter.set_settings(self.cal_filter_settings)
        calculation_filter.process()
        self._raw_result = calculation_filter.get_output_data()
        pass

    def ProcessHeartrate(self):
        generateData = GenerateData()
        generatorSettings = GeneratorSettingsC()
        generatorSettings.SetStartDateTime(startDateTime)
        generatorSettings.SetEndDateTime(startDateTime)
        generatorSettings.SetInput(inputFolder)
        generateData.SetSettings(generatorSettings)
        generateData.Process()
        fitnessData = generateData.GetData()
        statisticCalc = StatisticC(fitnessData)
        statisticCalc.Calculate()
        statisticData = statisticCalc.GetData()
        plotData = PlotC(plotSettings,statisticData)
        plotData.Plot()

    def TestFunction(self):
        self._Dialog.show()

    def backup_data(self):
        timestr = time.strftime("%Y%m%d-%H%M%S")

        file_handler = garminmanager.utils.FileManagerC.FilemManagerC()

        file_handler = garminmanager.utils.FileManagerC.FilemManagerC()
        src_folder = self._settings["activity_folder"]
        file_handler.set_src_folder(src_folder)
        dest_folder = self._settings["backup_folder"] + "/activity/" + timestr
        file_handler.set_dst_folder(dest_folder)
        file_handler.copy()
        src_folder = self._settings["monitor_folder"]
        file_handler.set_src_folder(src_folder)
        dest_folder = self._settings["backup_folder"] + "/monitor/" + timestr
        file_handler.copy()

    def PrintOverlay(self):
        filename = 'c:\\Users\\schrma\\Documents\\20190223-fit-all\\30731164854.fit'
        myPatternX1 = 'timestamp'
        myPatternY1 = 'current_activity_type_intensity'
        m = FitParserC()
        m.ClearData()
        m.SetFilename(filename)
        xyPairIntensity = m.GetTimeRecordPairActivityTypeIntensity()
        data1 = xyPairIntensity.y
        times1_raw = xyPairIntensity.x

        # Hear_rate
        # myPatternX2 = 'timestamp_16'
        # myPatternY2 = 'heart_rate'
        # m.ClearData()
        # firstTimestamp = m.GetRecordValue('timestamp')
        # myPairHeart = m.GetTimeRecordPairHeartbeat(myPatternX2, myPatternY2)
        # x = []
        # for selTime in myPairHeart.x:
        #     x = np.append(x, firstTimestamp + datetime.timedelta(seconds=selTime - myPairHeart.x[0]))
        #
        # data2 = myPairHeart.y;
        # times2_raw = x

        # Intensity
        myPairHeart = m.GetTimeRecordPairHeartbeat()
        data2 = myPairHeart.y
        times2_raw = myPairHeart.x

        host = self._dynamic_ax
        par1 = host.twinx()
        # par2 = host.twinx()
        #
        # offset = 60
        # new_fixed_axis = par2.get_grid_helper().new_fixed_axis
        # par2.axis["right"] = new_fixed_axis(loc="right",
        #                                      axes=par2,
        #                                      offset=(offset, 0))
        # par2.axis["right"].toggle(all=True)

        color = 'tab:green'
        p1, = host.plot(times1_raw, data1, color=color)
        host.set_xlabel('Time')
        host.set_ylabel('Intensity', color=color)
        host.set_ylim(0,500)

        color = 'tab:blue'
        p2, = par1.plot(times2_raw, data2)
        par1.set_ylabel('Heartrate', color=color)
        par1.set_ylim(40,200)

        host.legend()

        host.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d %H:%M'))
        host.xaxis.set_major_locator(mdates.HourLocator())
        plt.setp(host.xaxis.get_majorticklabels(), rotation=70)

        host.figure.canvas.draw()

    def ProcessHeartrate(self):
        myPattern = ['number','time_created','activity_type','intensity','heart_rate']
        outputName = 'summary.txt'
        #d = self._getFileList()
        matplotlib.rcParams['timezone'] = 'GMT+1'
        foldername = 'c:\\Users\\schrma\\Documents\\20190223-fit-all'
        foldername = 'c:\\Users\\schrma\\ownCloud\\leica\\fitfolder\\GarminWatch\\Monitor'
        d = self._getFileList(foldername)
        filenameList = d['names']
        fitFolder = d['folder']
        m = FitParserC()
        myPatternX = 'timestamp_16'
        myPatternY = 'heart_rate'
        m.ClearData()
        m.SetFilename(fitFolder + "\\" + filenameList[0])
        firstTimestamp = m.GetValueOfFirstOccurence('timestamp')
        x = []
        y = []
        m.ClearData()
        for filename in filenameList:
            m.SetFilename(fitFolder + "\\" + filename)
            #m.ClearData()

            xyPair = m.GetTimeRecordPairHeartbeat()

        data1 = xyPair.y
        times1_raw = xyPair.x

        host = self._dynamic_ax
        self._dynamic_ax.clear()
        color = 'tab:green'
        p1, = host.plot(times1_raw, data1, color=color)
        host.set_xlabel('Time')
        host.set_ylabel(myPatternY, color=color)
        host.set_ylim(40, 200)
        self._dynamic_ax.grid(True)
        plt.gca().xaxis_date(tz.tzlocal())
        #host.xaxis.set_title("3 - tzinfo NO, xaxis_date = YES, formatter=NO")
        host.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d %H:%M'))
        host.xaxis.set_major_locator(mdates.HourLocator())
        plt.setp(host.xaxis.get_majorticklabels(), rotation=70)

        host.figure.canvas.draw()


    def ParseOverAll(self):
        myPattern = ['timestamp','current_activity_type_intensity','timestamp_16']
        outputName = 'summary.txt'
        d = self._getFileList()
        #d = self._getFileList('c:\\Users\\schrma\\Documents\\20190223-1016-small')
        filenameList = d['names']
        fitFolder = d['folder']
        txtFolder = fitFolder + '\\all\\'
        if not os.path.exists(txtFolder):
            os.makedirs(txtFolder)
        m = FitParserC()
        for filename in filenameList:
            m.ClearData()
            m.SetFilename(fitFolder + "\\" + filename)
            m.ParseByPattern(myPattern)
        outputNameFull = txtFolder + outputName
        print(outputNameFull)
        m.PrintAll()
        m.SetOuputName(outputNameFull)
        m.WriteToFileOverall()

    def ParseAndWrite(self):
        d = self._getFileList()
        #d = self._getFileList('c:\\Users\\schrma\\Documents\\20190223-1016-fit')
        filenameList = d['names']
        fitFolder = d['folder']
        txtFolder = fitFolder + '\\txt\\'
        if not os.path.exists(txtFolder):
            os.makedirs(txtFolder)
        for filename in filenameList:
            outputName = filename.lower()
            outputName = txtFolder + outputName.replace(".fit", ".txt")
            print(outputName)
            m = FitParserC()
            m.SetFilename(fitFolder + "\\" + filename)
            m.SetOuputName(outputName)
            m.ParseFile()
            m.WriteToFileSingle()

    def _on_file_dialog(self):
        filenameList = self._get_files()
        if 0 < len(filenameList):
            for filename in filenameList:
                print(filename)

    def _getFileList(self,selectedFolder=None):
        if selectedFolder == None:
            selectedFolder = self._get_folder()

        print(selectedFolder)
        fullName = []
        onlyfiles = [f for f in listdir(selectedFolder) if isfile(join(selectedFolder, f))]
        for filename in onlyfiles:
            fullName.append(selectedFolder + "/" + filename)

        d = dict();
        d['fullNames'] = fullName
        d['names'] = onlyfiles
        d['folder'] = selectedFolder
        return d

    def _get_folder(self):
        dlg = QFileDialog()
        folder = dlg.getExistingDirectory()
        return folder

    def _get_file(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Files)

        if dlg.exec_():
            file_names = dlg.selectedFiles()
        else:
            file_names = []
        return file_names[0]
