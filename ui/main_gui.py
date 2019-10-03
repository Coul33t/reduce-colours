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
        self.resized_initial_img = None
        self.new_img = None
        self.resized_new_img = None
        self.colours_to_display = None
        self.final_colour_number = 0
        self.model_listView_choosen_colours = None


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(739, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_import = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_import.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.pushButton_import.setObjectName("pushButton_import")
        self.label_import_name = QtWidgets.QLabel(self.centralwidget)
        self.label_import_name.setGeometry(QtCore.QRect(120, 15, 241, 21))
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
        self.label_n_colours.setGeometry(QtCore.QRect(390, 30, 141, 20))
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
        self.pushButton_reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reset.setGeometry(QtCore.QRect(10, 480, 93, 28))
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.label_total_number_of_colour = QtWidgets.QLabel(self.centralwidget)
        self.label_total_number_of_colour.setGeometry(QtCore.QRect(390, 10, 191, 16))
        self.label_total_number_of_colour.setObjectName("label_total_number_of_colour")
        self.label_image_generation = QtWidgets.QLabel(self.centralwidget)
        self.label_image_generation.setGeometry(QtCore.QRect(110, 480, 101, 21))
        self.label_image_generation.setText("")
        self.label_image_generation.setObjectName("label_image_generation")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(340, 510, 93, 28))
        self.pushButton_save.setObjectName("pushButton_save")
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
        self.pushButton_reset.setText(_translate("MainWindow", "Reset"))
        self.label_total_number_of_colour.setText(_translate("MainWindow", "Total Number of colours:"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))

    def initialise(self):
        self.model_listView_choosen_colours = QtGui.QStandardItemModel(self.listView_choosen_colours)

    def link_components(self):
        self.pushButton_import.clicked.connect(self.select_file)
        self.pushButton_n_colours.clicked.connect(self.get_colours)
        self.pushButton_go.clicked.connect(self.generate_output)
        self.pushButton_reset.clicked.connect(self.reset_displayed_image)
        self.pushButton_save.clicked.connect(self.save_output_image)

    def select_file(self):
        string = QtWidgets.QFileDialog.getOpenFileName(filter="Image Files (*.png *.jpg *.bmp)")
        self.path_to_img = string[0]

        self.label_import_name.setText(self.path_to_img.split('/')[-1])

        self.initial_img = Image.open(self.path_to_img).convert('RGB')

        size = list(np.asarray(self.initial_img).shape[:2])
        label_size = (self.label_original_image.size().height(), self.label_original_image.size().width())

        self.resized_initial_img = resize_image(self.initial_img, label_size)
        resized = False

        self.resized_initial_img = ImageQt.ImageQt(self.resized_initial_img)
        reference_img = QtGui.QPixmap.fromImage(self.resized_initial_img)
        self.label_original_image.setPixmap(reference_img)

        self.label_image_generation.setText('')
        self.label_total_number_of_colour.setText(f"Total number of colours: {get_number_of_colours(self.initial_img)}")

    def get_colours(self):
        self.model_listView_choosen_colours.clear()
        self.final_colour_number = self.spinBox_n_colours.value()
        self.colours_to_display = get_colours(self.initial_img, self.final_colour_number)

        if not self.colours_to_display:
            return

        # TODO: order the list by colour proximity (purely aesthetic)
        for colour in self.colours_to_display:
            # create an item with a caption
            item = QtGui.QStandardItem()

            item.setBackground(QtGui.QColor(int(colour[0]* 255) , int(colour[1]* 255), int(colour[2]* 255)))
            # Add the item to the model
            self.model_listView_choosen_colours.appendRow(item)

        # Apply the model to the list view
        self.listView_choosen_colours.setModel(self.model_listView_choosen_colours)

    def generate_output(self):
        self.label_image_generation.setText('Generating image...')

        self.new_img = merge_colours(self.initial_img, self.colours_to_display)
        size = list(np.asarray(self.new_img).shape[:2])
        label_size = (self.label_original_image.size().height(), self.label_original_image.size().width())

        self.new_img = np.asarray(self.new_img * 255, 'uint8')
        self.new_img = Image.fromarray(self.new_img, mode='RGB')

        self.new_resized_img = resize_image(self.new_img, label_size)
        resized = False

        self.new_resized_img = ImageQt.ImageQt(self.new_resized_img)
        reference_img = QtGui.QPixmap.fromImage(self.new_resized_img)
        self.label_original_image.setPixmap(reference_img)

        self.label_image_generation.setText('Image generated!')

    def reset_displayed_image(self):
        reference_img = QtGui.QPixmap.fromImage(self.resized_initial_img)
        self.label_original_image.setPixmap(reference_img)

    def save_output_image(self):
        final_name = f"{self.path_to_img.split('.')[0]}_reduced.{self.path_to_img.split('.')[-1]}"
        self.new_img.save(final_name)
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(f"Image successfully saved as {final_name} !")
        msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())