# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from math import floor
from PIL import Image, ImageQt
import numpy as np

from ui_funcs import *

def debug_trace():
  '''Set a tracepoint in the Python debugger that works with Qt'''
  from PyQt5.QtCore import pyqtRemoveInputHook

  # Or for Qt5
  #from PyQt5.QtCore import pyqtRemoveInputHook

  from pdb import set_trace
  pyqtRemoveInputHook()
  set_trace()

class Ui_MainWindow(object):
    def __init__(self):
        self.path_to_img = None
        self.initial_img = None
        self.resized_img = None
        self.colours_to_display = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(739, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_import = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_import.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.pushButton_import.setObjectName("pushButton_import")
        self.label_import_name = QtWidgets.QLabel(self.centralwidget)
        self.label_import_name.setGeometry(QtCore.QRect(120, 20, 55, 16))
        self.label_import_name.setText("")
        self.label_import_name.setObjectName("label_import_name")
        self.label_original_image = QtWidgets.QLabel(self.centralwidget)
        self.label_original_image.setGeometry(QtCore.QRect(10, 90, 361, 361))
        self.label_original_image.setText("")
        self.label_original_image.setObjectName("label_original_image")
        self.spinBox_n_colours = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_n_colours.setGeometry(QtCore.QRect(550, 30, 42, 22))
        self.spinBox_n_colours.setObjectName("spinBox_n_colours")
        self.label_n_colours = QtWidgets.QLabel(self.centralwidget)
        self.label_n_colours.setGeometry(QtCore.QRect(394, 30, 141, 20))
        self.label_n_colours.setObjectName("label_n_colours")
        self.pushButton_n_colours = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_n_colours.setGeometry(QtCore.QRect(600, 30, 51, 28))
        self.pushButton_n_colours.setObjectName("pushButton_n_colours")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(370, 20, 20, 451))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.listView_choosen_colours = QtWidgets.QListView(self.centralwidget)
        self.listView_choosen_colours.setGeometry(QtCore.QRect(390, 90, 341, 361))
        self.listView_choosen_colours.setObjectName("listView_choosen_colours")
        self.label_2_choosen_colours = QtWidgets.QLabel(self.centralwidget)
        self.label_2_choosen_colours.setGeometry(QtCore.QRect(390, 70, 101, 16))
        self.label_2_choosen_colours.setObjectName("label_2_choosen_colours")
        self.pushButton_go = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_go.setGeometry(QtCore.QRect(340, 480, 93, 28))
        self.pushButton_go.setObjectName("pushButton_go")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 739, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.initialise()
        self.link_components()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_import.setText(_translate("MainWindow", "Import"))
        self.label_n_colours.setText(_translate("MainWindow", "Final number of colours:"))
        self.pushButton_n_colours.setText(_translate("MainWindow", "Ok"))
        self.label_2_choosen_colours.setText(_translate("MainWindow", "Choosen colours:"))
        self.pushButton_go.setText(_translate("MainWindow", "Go!"))

    def initialise(self):
        self.listView.setViewMode(QtGui.QListView.IconMode)

    def link_components(self):
        self.pushButton_import.clicked.connect(self.select_file)
        self.pushButton_n_colours.clicked.connect(self.get_colours)

    def select_file(self):
        string = QtWidgets.QFileDialog.getOpenFileName(filter="Image Files (*.png *.jpg *.bmp)")
        self.path_to_img = string[0]

        self.label_import_name.setText(string[0].split('/')[-1])

        self.initial_img = Image.open(self.path_to_img).convert('RGB')

        size = list(np.asarray(self.initial_img).shape[:2])
        label_size = (self.label_original_image.size().height(), self.label_original_image.size().width())

        resized = False

        if size[0] > label_size[0] or size[1] > label_size[1]:
            ratio = min(label_size[1]/size[1], label_size[0]/size[0])
            size[0] = floor(size[0] * ratio)
            size[1] = floor(size[1] * ratio)
            resized = True

        elif size[0] < label_size[0] or size[1] < label_size[1]:
            ratio = min(label_size[1]/size[1], label_size[0]/size[0])
            size[0] = floor(size[0] * ratio)
            size[1] = floor(size[1] * ratio)
            resized = True

        self.resized_img = self.initial_img
        if resized:
            self.resized_img = self.initial_img.resize(size)

        self.resized_img = ImageQt.ImageQt(self.resized_img)
        reference_img = QtGui.QPixmap.fromImage(self.resized_img)
        self.label_original_image.setPixmap(reference_img)

    def get_colours(self):
        #TODO: checks limits of original image number of colours
        self.colours_to_display = get_colours(self.initial_img, self.spinBox_n_colours.value())
        self.listView_choosen_colours



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())