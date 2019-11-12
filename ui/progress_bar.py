# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progress_bar.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 70)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(137, 10, 251, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 40, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Reducing colours..."))
        self.pushButton.setText(_translate("Dialog", "Cancel"))

class ProgressBar(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, name=None, parent=None):
        super(ProgressBar, self).__init__(parent)
        self.setupUi(self)
        self.show()

        if name is not None:
            self.set_title(name)

    def set_value(self, val):
        self.progressBar.setProperty("value", val)

    def set_title(self, desc):
        self.setWindowTitle(desc)
