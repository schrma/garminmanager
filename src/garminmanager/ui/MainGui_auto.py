# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\schrma\Documents\python\garminmanager\src\garminmanager\ui\MainGui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1057, 940)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 300, 881, 471))
        self.widget.setObjectName("widget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(51, 51, 486, 143))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 0, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.test_pb = QtWidgets.QPushButton(self.layoutWidget)
        self.test_pb.setObjectName("test_pb")
        self.verticalLayout.addWidget(self.test_pb)
        self.process_pb = QtWidgets.QPushButton(self.layoutWidget)
        self.process_pb.setObjectName("process_pb")
        self.verticalLayout.addWidget(self.process_pb)
        self.ParseToFileButton = QtWidgets.QPushButton(self.layoutWidget)
        self.ParseToFileButton.setObjectName("ParseToFileButton")
        self.verticalLayout.addWidget(self.ParseToFileButton)
        self.backup_pb = QtWidgets.QPushButton(self.layoutWidget)
        self.backup_pb.setObjectName("backup_pb")
        self.verticalLayout.addWidget(self.backup_pb)
        self.data_from_watch_pb = QtWidgets.QPushButton(self.layoutWidget)
        self.data_from_watch_pb.setObjectName("data_from_watch_pb")
        self.verticalLayout.addWidget(self.data_from_watch_pb)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.start_de = QtWidgets.QDateTimeEdit(self.layoutWidget)
        self.start_de.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 2, 28), QtCore.QTime(0, 0, 0)))
        self.start_de.setObjectName("start_de")
        self.gridLayout.addWidget(self.start_de, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.end_de = QtWidgets.QDateTimeEdit(self.layoutWidget)
        self.end_de.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 2, 28), QtCore.QTime(0, 0, 0)))
        self.end_de.setObjectName("end_de")
        self.gridLayout.addWidget(self.end_de, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 3, 1, 1)
        self.m_UseDefaultFolderCB = QtWidgets.QCheckBox(self.layoutWidget)
        self.m_UseDefaultFolderCB.setObjectName("m_UseDefaultFolderCB")
        self.gridLayout_2.addWidget(self.m_UseDefaultFolderCB, 0, 1, 1, 1)
        self.label_fenix_pic = QtWidgets.QLabel(self.centralwidget)
        self.label_fenix_pic.setGeometry(QtCore.QRect(910, 50, 111, 91))
        self.label_fenix_pic.setScaledContents(True)
        self.label_fenix_pic.setObjectName("label_fenix_pic")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(550, 50, 340, 223))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.text_tb = QtWidgets.QTextBrowser(self.layoutWidget1)
        self.text_tb.setObjectName("text_tb")
        self.gridLayout_3.addWidget(self.text_tb, 0, 0, 1, 4)
        self.load_settings_pb = QtWidgets.QPushButton(self.layoutWidget1)
        self.load_settings_pb.setObjectName("load_settings_pb")
        self.gridLayout_3.addWidget(self.load_settings_pb, 1, 0, 1, 1)
        self.save_settings_pb = QtWidgets.QPushButton(self.layoutWidget1)
        self.save_settings_pb.setObjectName("save_settings_pb")
        self.gridLayout_3.addWidget(self.save_settings_pb, 1, 1, 1, 1)
        self.folder_cb = QtWidgets.QComboBox(self.layoutWidget1)
        self.folder_cb.setObjectName("folder_cb")
        self.folder_cb.addItem("")
        self.folder_cb.addItem("")
        self.folder_cb.addItem("")
        self.folder_cb.addItem("")
        self.folder_cb.addItem("")
        self.gridLayout_3.addWidget(self.folder_cb, 1, 2, 1, 1)
        self.set_folders_pb = QtWidgets.QPushButton(self.layoutWidget1)
        self.set_folders_pb.setObjectName("set_folders_pb")
        self.gridLayout_3.addWidget(self.set_folders_pb, 1, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1057, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.menuHelp.addAction(self.actionVersion)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Heartrate"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Steps"))
        self.test_pb.setText(_translate("MainWindow", "TestButton"))
        self.process_pb.setText(_translate("MainWindow", "Process"))
        self.ParseToFileButton.setText(_translate("MainWindow", "ParseToFile"))
        self.backup_pb.setText(_translate("MainWindow", "Backup"))
        self.data_from_watch_pb.setText(_translate("MainWindow", "Get Data from Watch"))
        self.label_2.setText(_translate("MainWindow", "End Date"))
        self.label.setText(_translate("MainWindow", "Start Date"))
        self.m_UseDefaultFolderCB.setText(_translate("MainWindow", "Use default Folder"))
        self.label_fenix_pic.setText(_translate("MainWindow", "Picture"))
        self.load_settings_pb.setText(_translate("MainWindow", "Load"))
        self.save_settings_pb.setText(_translate("MainWindow", "Save"))
        self.folder_cb.setItemText(0, _translate("MainWindow", "Monitor Folder"))
        self.folder_cb.setItemText(1, _translate("MainWindow", "Activity Folder"))
        self.folder_cb.setItemText(2, _translate("MainWindow", "Backup Folder"))
        self.folder_cb.setItemText(3, _translate("MainWindow", "Watch Folder"))
        self.folder_cb.setItemText(4, _translate("MainWindow", "Json Folder"))
        self.set_folders_pb.setText(_translate("MainWindow", "Set"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionVersion.setText(_translate("MainWindow", "Version"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

