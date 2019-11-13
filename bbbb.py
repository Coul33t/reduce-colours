# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\pixel_perfect.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(574, 417)
        self.label_img = QtWidgets.QLabel(Dialog)
        self.label_img.setGeometry(QtCore.QRect(10, 10, 361, 361))
        self.label_img.setText("")
        self.label_img.setObjectName("label_img")
        self.pushButton_go = QtWidgets.QPushButton(Dialog)
        self.pushButton_go.setGeometry(QtCore.QRect(370, 100, 93, 28))
        self.pushButton_go.setObjectName("pushButton_go")
        self.pushButton_validate = QtWidgets.QPushButton(Dialog)
        self.pushButton_validate.setGeometry(QtCore.QRect(470, 100, 93, 28))
        self.pushButton_validate.setObjectName("pushButton_validate")
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancel.setGeometry(QtCore.QRect(470, 130, 93, 28))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.label_pixel_size = QtWidgets.QLabel(Dialog)
        self.label_pixel_size.setGeometry(QtCore.QRect(370, 10, 55, 16))
        self.label_pixel_size.setObjectName("label_pixel_size")
        self.spinBox_pixel_size = QtWidgets.QSpinBox(Dialog)
        self.spinBox_pixel_size.setGeometry(QtCore.QRect(500, 10, 61, 22))
        self.spinBox_pixel_size.setMinimum(1)
        self.spinBox_pixel_size.setMaximum(999999)
        self.spinBox_pixel_size.setObjectName("spinBox_pixel_size")
        self.pushButton_reset = QtWidgets.QPushButton(Dialog)
        self.pushButton_reset.setGeometry(QtCore.QRect(370, 130, 93, 28))
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.label_offset_pixel_grid = QtWidgets.QLabel(Dialog)
        self.label_offset_pixel_grid.setGeometry(QtCore.QRect(370, 40, 101, 16))
        self.label_offset_pixel_grid.setObjectName("label_offset_pixel_grid")
        self.spinBox_offset_pixel_grid = QtWidgets.QSpinBox(Dialog)
        self.spinBox_offset_pixel_grid.setGeometry(QtCore.QRect(500, 40, 61, 22))
        self.spinBox_offset_pixel_grid.setObjectName("spinBox_offset_pixel_grid")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_go.setText(_translate("Dialog", "Go"))
        self.pushButton_validate.setText(_translate("Dialog", "Validate"))
        self.pushButton_cancel.setText(_translate("Dialog", "Cancel"))
        self.label_pixel_size.setText(_translate("Dialog", "Pixel size:"))
        self.pushButton_reset.setText(_translate("Dialog", "Reset"))
        self.label_offset_pixel_grid.setText(_translate("Dialog", "Offset pixel grid:"))

