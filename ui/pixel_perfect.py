# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\pixel_perfect.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from math import floor
from skimage import color
import numpy as np
from PIL import Image, ImageQt
from ui_funcs import resize_image

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

class PixelPerfect(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, original_image=None, name=None, parent=None):
        super(PixelPerfect, self).__init__(parent)
        self.setupUi(self)
        self.show()
        self.original_image = original_image

        self.label_size = (self.label_img.size().height(), self.label_img.size().width())

        self.resized_original_image = original_image.copy()
        self.resized_original_image = resize_image(self.resized_original_image, self.label_size)
        self.qimage_resized_original = None
        self.pixel_perfected_image = None
        self.resized_pixel_perfected_image = None
        self.qimage_resized_pixel_perfected = None

        self.link_components()

        self.display_original_image()


    def link_components(self):
        self.pushButton_cancel.clicked.connect(self.close_window)
        self.pushButton_validate.clicked.connect(self.return_image)
        self.pushButton_reset.clicked.connect(self.display_original_image)
        self.pushButton_go.clicked.connect(self.pixelate_image)

    def close_window(self):
        self.close()

    def reset_pixel_perfected_image(self):
        self.pixel_perfected_image = self.original_image.copy()

    def display_original_image(self):
        self.qimage_resized_original = ImageQt.ImageQt(self.resized_original_image)
        reference_img = QtGui.QPixmap.fromImage(self.qimage_resized_original)
        self.label_img.setPixmap(reference_img)

    def pixelate_image(self):
        grid_offset = int(self.spinBox_offset_pixel_grid.value())

        pixel_size = int(self.spinBox_pixel_size.value())
        x_size = floor((self.original_image.size[0] - grid_offset) / pixel_size)
        y_size = floor((self.original_image.size[1] - grid_offset) / pixel_size)


        self.reset_pixel_perfected_image()
        img_as_array = np.array(self.pixel_perfected_image)

        for y in range(y_size):
            for x in range(x_size):
                sub_image = self.pixel_perfected_image.crop((x * pixel_size + grid_offset,
                                                             y * pixel_size + grid_offset,
                                                             (x * pixel_size) + pixel_size + grid_offset,
                                                             (y * pixel_size) + pixel_size + grid_offset))

                colours = sub_image.getcolors(sub_image.size[0] * sub_image.size[1])
                # TODO: check if max() behaviour is correct
                dominant_colour = max(colours, key=lambda x: x[0])[1]

                img_as_array[y * pixel_size  + grid_offset : (y * pixel_size) + pixel_size + grid_offset,
                             x * pixel_size  + grid_offset : (x * pixel_size) + pixel_size + grid_offset] = dominant_colour



        self.pixel_perfected_image = Image.fromarray(img_as_array, mode='RGB')
        self.resized_pixel_perfected_image = resize_image(self.pixel_perfected_image, self.label_size)
        self.qimage_resized_pixel_perfected = ImageQt.ImageQt(self.resized_pixel_perfected_image)
        reference_img = QtGui.QPixmap.fromImage(self.qimage_resized_pixel_perfected)
        self.label_img.setPixmap(reference_img)


    def return_image(self):
        pass
        self.close_window()

