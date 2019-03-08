# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\schrma\Documents\python\03-fitparser\ui\Version.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBoxVersion = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBoxVersion.setGeometry(QtCore.QRect(120, 260, 161, 32))
        self.buttonBoxVersion.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBoxVersion.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBoxVersion.setObjectName("buttonBoxVersion")
        self.VersionLabel = QtWidgets.QLabel(Dialog)
        self.VersionLabel.setGeometry(QtCore.QRect(30, 20, 101, 16))
        self.VersionLabel.setObjectName("VersionLabel")
        self.labelPciture = QtWidgets.QLabel(Dialog)
        self.labelPciture.setGeometry(QtCore.QRect(30, 70, 141, 91))
        self.labelPciture.setText("")
        self.labelPciture.setPixmap(QtGui.QPixmap("../../../../ownCloud/leica/fenix/01-documentations/images/fenix3.jpg"))
        self.labelPciture.setScaledContents(True)
        self.labelPciture.setObjectName("labelPciture")

        self.retranslateUi(Dialog)
        self.buttonBoxVersion.accepted.connect(Dialog.accept)
        self.buttonBoxVersion.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Version"))
        self.VersionLabel.setText(_translate("Dialog", "Version: 1.0.0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

