from ui.MainGui_auto import *
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

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

class MainWindow(Ui_MainWindow):

    def __init__(self,Dialog,DialogInterface):
        self._on_test_callback = None
        self._figure = []
        self._Dialog = Dialog
        self._DialogInterface = DialogInterface
        self._settings = []

    def PrepareApplication(self):
        with open("settings.json", 'r') as read_file:
            self._settings = json.load(read_file)
        self.mTextTB.append("FitSourceFolder:")
        self.mTextTB.append(self._settings["FitSourceFolder"])
        self.mTextTB.append("FitDstFolder:")
        self.mTextTB.append(self._settings["FitDstFolder"])
        self.mTextTB.append("FitBackupFolder:")
        self.mTextTB.append(self._settings["FitBackupFolder"])

        # Right place for image in label
        self.labelMainPic.setPixmap(QtGui.QPixmap("./images/fenix3.jpg"))



    def register_signals(self,MainWindow):

        self.mTestPB.clicked.connect(self.PrintOverlay)
        self.mProcessPB.clicked.connect(self.ProcessHeartrate)
        self.ParseToFileButton.clicked.connect(self.ParseAndWrite)
        self.mBackupPB.clicked.connect(self.BackupData)
        self.mGetDataFromWatchPB.clicked.connect(self.GetDataFromWatch)
        self.actionVersion.triggered.connect(self.TestFunction)



        data = np.array([0.7, 0.7, 0.7, 0.8, 0.9, 0.9, 1.5, 1.5, 1.5, 1.5])
        self._DialogInterface.labelPciture.setPixmap(QtGui.QPixmap("./images/fenix3.jpg"))
        self._DialogInterface.VersionLabel.setText("Version: 2.0.0")
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

    def TestFunction(self):
        self._Dialog.show()

    def GetDataFromWatch(self):
        src = self._settings["FitSourceFolder"] + "/ACTIVITY"
        dst = self._settings["FitDstFolder"] + "/GarminWatch/MyActivities"
        self.MoveFiles(src,dst)

        src = self._settings["FitSourceFolder"] + "/MONITOR"
        dst = self._settings["FitDstFolder"] + "/GarminWatch/Monitor"
        self.MoveFiles(src,dst)


    def BackupData(self):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        src = self._settings["FitDstFolder"] + "/GarminWatch"
        dst = self._settings["FitBackupFolder"] + "/" + timestr
        self.Copytree(src,dst)

    def CopyFilesWithSubfolder(self,src,dst):
        if not os.path.exists(dst):
            os.makedirs(dst)
        for root, dirs, files in os.walk(src):  # replace the . with your starting directory
            for file in files:
                path_file = os.path.join(root, file)
                shutil.copy2(path_file, dst)  # change you destination dir

    def Copytree(self, src, dst, symlinks=False, ignore=None):
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)

    def MoveFiles(self,src,dst):
        if not os.path.exists(dst):
            os.makedirs(dst)
        for root, dirs, files in os.walk(src):  # replace the . with your starting directory
            for file in files:
                path_file = os.path.join(root, file)
                shutil.move(path_file, dst)  # change you destination dir

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

    def _get_files(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Files)

        if dlg.exec_():
            file_names = dlg.selectedFiles()
        else:
            file_names = []
        return file_names
