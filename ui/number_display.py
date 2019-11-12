# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'merging_colours.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(245, 32)
        self.label_number = QtWidgets.QLabel(Dialog)
        self.label_number.setGeometry(QtCore.QRect(10, 10, 161, 16))
        self.label_number.setObjectName("label_number")
        self.label_number_value = QtWidgets.QLabel(Dialog)
        self.label_number_value.setGeometry(QtCore.QRect(170, 10, 55, 16))
        self.label_number_value.setText("")
        self.label_number_value.setObjectName("label_number_value")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_number.setText(_translate("Dialog", "Number of colours merged:"))

class NumberDisplay(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, name=None, parent=None):
        super(NumberDisplay, self).__init__(parent)
        self.setupUi(self)
        self.show()

        if name is not None:
            self.set_title(name)

    def set_value(self, val):
        self.label_number_value.setText(str(val))

    def set_title(self, desc):
        self.setWindowTitle(desc)
