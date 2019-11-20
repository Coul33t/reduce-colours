# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import json

from math import floor
from PIL import Image, ImageQt
import numpy as np

import ui_funcs
from pixel_perfect import PixelPerfect

class Ui_MainWindow(object):
    def __init__(self):
        self.path_to_img = None
        self.initial_img = None
        self.resized_initial_img = None
        self.new_img = None
        self.resized_new_img = None
        self.colours_to_display = []
        self.final_colour_number = 0
        self.model_listView_choosen_colours = None
        self.model_listView_mouse_colour = None
        self.pixel_perfect = None
        self.colour_corres_list = None

        try:
            with open('res/colours.json', 'r') as json_colours_file:
                self.colour_corres_list = json.load(json_colours_file)
        except FileNotFoundError:
            with open('../res/colours.json', 'r') as json_colours_file:
                self.colour_corres_list = json.load(json_colours_file)

        ui_funcs.convert_rgb_to_numpy_array(self.colour_corres_list)
        ui_funcs.add_Lab(self.colour_corres_list)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(881, 609)
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
        self.label_original_image.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
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
        self.line.setGeometry(QtCore.QRect(370, 20, 20, 511))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.listView_choosen_colours = QtWidgets.QListView(self.centralwidget)
        self.listView_choosen_colours.setGeometry(QtCore.QRect(530, 90, 341, 461))
        self.listView_choosen_colours.setObjectName("listView_choosen_colours")
        self.pushButton_go = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_go.setGeometry(QtCore.QRect(390, 490, 93, 28))
        self.pushButton_go.setObjectName("pushButton_go")
        self.pushButton_reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reset.setGeometry(QtCore.QRect(10, 460, 93, 28))
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.label_total_number_of_colour = QtWidgets.QLabel(self.centralwidget)
        self.label_total_number_of_colour.setGeometry(QtCore.QRect(390, 10, 191, 16))
        self.label_total_number_of_colour.setObjectName("label_total_number_of_colour")
        self.label_image_generation = QtWidgets.QLabel(self.centralwidget)
        self.label_image_generation.setGeometry(QtCore.QRect(110, 480, 101, 21))
        self.label_image_generation.setText("")
        self.label_image_generation.setObjectName("label_image_generation")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(390, 520, 93, 28))
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_pixel_perfect = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pixel_perfect.setGeometry(QtCore.QRect(10, 520, 93, 28))
        self.pushButton_pixel_perfect.setObjectName("pushButton_pixel_perfect")
        self.groupBox_mouse_colour = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_mouse_colour.setGeometry(QtCore.QRect(250, 460, 120, 91))
        self.groupBox_mouse_colour.setObjectName("groupBox_mouse_colour")
        self.listView_mouse_colour = QtWidgets.QListView(self.groupBox_mouse_colour)
        self.listView_mouse_colour.setGeometry(QtCore.QRect(10, 20, 71, 21))
        self.listView_mouse_colour.setObjectName("listView_mouse_colour")
        self.radioButton_add = QtWidgets.QRadioButton(self.groupBox_mouse_colour)
        self.radioButton_add.setGeometry(QtCore.QRect(10, 40, 95, 20))
        self.radioButton_add.setChecked(True)
        self.radioButton_add.setObjectName("radioButton_add")
        self.radioButton_change = QtWidgets.QRadioButton(self.groupBox_mouse_colour)
        self.radioButton_change.setGeometry(QtCore.QRect(10, 60, 95, 20))
        self.radioButton_change.setObjectName("radioButton_change")
        self.label_already_in_list = QtWidgets.QLabel(self.centralwidget)
        self.label_already_in_list.setGeometry(QtCore.QRect(530, 50, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_already_in_list.setFont(font)
        self.label_already_in_list.setText("")
        self.label_already_in_list.setObjectName("label_already_in_list")
        self.groupBox_colours = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_colours.setGeometry(QtCore.QRect(390, 90, 131, 121))
        self.groupBox_colours.setObjectName("groupBox_colours")
        self.pushButton_add_colour = QtWidgets.QPushButton(self.groupBox_colours)
        self.pushButton_add_colour.setGeometry(QtCore.QRect(20, 20, 93, 28))
        self.pushButton_add_colour.setObjectName("pushButton_add_colour")
        self.pushButton_delete_colour = QtWidgets.QPushButton(self.groupBox_colours)
        self.pushButton_delete_colour.setGeometry(QtCore.QRect(20, 80, 93, 28))
        self.pushButton_delete_colour.setObjectName("pushButton_delete_colour")
        self.pushButton_change_colour = QtWidgets.QPushButton(self.groupBox_colours)
        self.pushButton_change_colour.setGeometry(QtCore.QRect(20, 50, 93, 28))
        self.pushButton_change_colour.setObjectName("pushButton_change_colour")
        self.groupBox_auto_merging = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_auto_merging.setGeometry(QtCore.QRect(390, 220, 131, 91))
        self.groupBox_auto_merging.setObjectName("groupBox_auto_merging")
        self.pushButton_merge_colours = QtWidgets.QPushButton(self.groupBox_auto_merging)
        self.pushButton_merge_colours.setGeometry(QtCore.QRect(10, 50, 93, 28))
        self.pushButton_merge_colours.setObjectName("pushButton_merge_colours")
        self.spinBox_merge_colours = QtWidgets.QSpinBox(self.groupBox_auto_merging)
        self.spinBox_merge_colours.setGeometry(QtCore.QRect(80, 20, 42, 22))
        self.spinBox_merge_colours.setObjectName("spinBox_merge_colours")
        self.label_colours_merging = QtWidgets.QLabel(self.groupBox_auto_merging)
        self.label_colours_merging.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.label_colours_merging.setObjectName("label_colours_merging")
        self.groupBox_to_dmc = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_to_dmc.setGeometry(QtCore.QRect(390, 320, 120, 101))
        self.groupBox_to_dmc.setObjectName("groupBox_to_dmc")
        self.radioButton_to_dmc_lab = QtWidgets.QRadioButton(self.groupBox_to_dmc)
        self.radioButton_to_dmc_lab.setGeometry(QtCore.QRect(10, 20, 95, 20))
        self.radioButton_to_dmc_lab.setChecked(True)
        self.radioButton_to_dmc_lab.setObjectName("radioButton_to_dmc_lab")
        self.radioButton_to_dmc_rgb = QtWidgets.QRadioButton(self.groupBox_to_dmc)
        self.radioButton_to_dmc_rgb.setGeometry(QtCore.QRect(10, 40, 95, 20))
        self.radioButton_to_dmc_rgb.setObjectName("radioButton_to_dmc_rgb")
        self.pushButton_to_dmc_colours = QtWidgets.QPushButton(self.groupBox_to_dmc)
        self.pushButton_to_dmc_colours.setGeometry(QtCore.QRect(10, 60, 93, 28))
        self.pushButton_to_dmc_colours.setObjectName("pushButton_to_dmc_colours")
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
        self.pushButton_go.setText(_translate("MainWindow", "Go!"))
        self.pushButton_reset.setText(_translate("MainWindow", "Reset"))
        self.label_total_number_of_colour.setText(_translate("MainWindow", "Total Number of colours:"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.pushButton_pixel_perfect.setText(_translate("MainWindow", "Pixel Perfect"))
        self.groupBox_mouse_colour.setTitle(_translate("MainWindow", "Mouse colour"))
        self.radioButton_add.setText(_translate("MainWindow", "Add"))
        self.radioButton_change.setText(_translate("MainWindow", "Change"))
        self.groupBox_colours.setTitle(_translate("MainWindow", "Colours"))
        self.pushButton_add_colour.setText(_translate("MainWindow", "Add colour"))
        self.pushButton_delete_colour.setText(_translate("MainWindow", "Delete"))
        self.pushButton_change_colour.setText(_translate("MainWindow", "Change colour"))
        self.groupBox_auto_merging.setTitle(_translate("MainWindow", "Auto-merging"))
        self.pushButton_merge_colours.setText(_translate("MainWindow", "Merge"))
        self.label_colours_merging.setText(_translate("MainWindow", "Threshold:"))
        self.groupBox_to_dmc.setTitle(_translate("MainWindow", "To DMC colours"))
        self.radioButton_to_dmc_lab.setText(_translate("MainWindow", "L*a*b*"))
        self.radioButton_to_dmc_rgb.setText(_translate("MainWindow", "RGB"))
        self.pushButton_to_dmc_colours.setText(_translate("MainWindow", "To DMC colour"))

    def initialise(self):
        self.model_listView_choosen_colours = QtGui.QStandardItemModel(self.listView_choosen_colours)
        self.listView_choosen_colours.setModel(self.model_listView_choosen_colours)
        self.model_listView_mouse_colour = QtGui.QStandardItemModel(self.listView_mouse_colour)
        self.listView_mouse_colour.setModel(self.model_listView_mouse_colour)

        self.hide_all()

    def hide_all(self):
        self.label_n_colours.hide()
        self.pushButton_n_colours.hide()
        self.label_already_in_list.hide()
        self.pushButton_go.hide()
        self.pushButton_reset.hide()
        self.label_total_number_of_colour.hide()
        self.pushButton_save.hide()
        self.groupBox_colours.hide()
        self.listView_choosen_colours.hide()
        self.listView_mouse_colour.hide()
        self.spinBox_n_colours.hide()
        self.groupBox_auto_merging.hide()
        self.pushButton_pixel_perfect.hide()
        self.groupBox_mouse_colour.hide()
        self.groupBox_to_dmc.hide()

    def show_all(self):
        self.label_n_colours.show()
        self.pushButton_n_colours.show()
        self.label_already_in_list.show()
        self.pushButton_go.show()
        self.pushButton_reset.show()
        self.label_total_number_of_colour.show()
        self.pushButton_save.show()
        self.groupBox_colours.show()
        self.listView_choosen_colours.show()
        self.listView_mouse_colour.show()
        self.spinBox_n_colours.show()
        self.groupBox_auto_merging.show()
        self.pushButton_pixel_perfect.show()
        self.groupBox_mouse_colour.show()
        self.groupBox_to_dmc.show()


    def link_components(self):
        self.pushButton_import.clicked.connect(self.select_file)
        self.pushButton_n_colours.clicked.connect(self.get_colours)
        self.pushButton_go.clicked.connect(self.generate_output)
        self.pushButton_reset.clicked.connect(self.reset_displayed_image)
        self.pushButton_save.clicked.connect(self.save_output_image)
        self.pushButton_add_colour.clicked.connect(self.add_colour_from_picker)
        self.pushButton_delete_colour.clicked.connect(self.delete_colour)
        self.pushButton_change_colour.clicked.connect(self.change_colour_from_picker)
        self.label_original_image.mousePressEvent = self.get_colour_under_mouse
        self.pushButton_merge_colours.clicked.connect(self.merge_colours)
        self.pushButton_pixel_perfect.clicked.connect(self.open_pixel_perfect)
        self.pushButton_to_dmc_colours.clicked.connect(self.to_dmc_colours)

    def select_file(self):
        string = QtWidgets.QFileDialog.getOpenFileName(filter="Image Files (*.png *.jpg *.bmp)")
        self.path_to_img = string[0]

        if not self.path_to_img:
            return

        self.label_import_name.setText(self.path_to_img.split('/')[-1])

        self.initial_img = Image.open(self.path_to_img).convert('RGB')

        label_size = (self.label_original_image.size().height(), self.label_original_image.size().width())

        self.resized_initial_img = ui_funcs.resize_image(self.initial_img, label_size)

        self.resized_initial_img = ImageQt.ImageQt(self.resized_initial_img)
        reference_img = QtGui.QPixmap.fromImage(self.resized_initial_img)
        self.label_original_image.setPixmap(reference_img)

        self.label_image_generation.setText('')
        self.label_total_number_of_colour.setText(f"Total number of colours: {ui_funcs.get_number_of_colours(self.initial_img)}")

        self.show_all()

    def open_pixel_perfect(self):
        if self.new_img is not None:
            self.pixel_perfect = PixelPerfect(self.new_img)
        else:
            self.pixel_perfect = PixelPerfect(self.initial_img)

    def check_if_colour_exists(self, colour):
        for index in range(self.model_listView_choosen_colours.rowCount()):
            if colour == self.model_listView_choosen_colours.item(index).background().color().getRgb()[:-1]:
                return True
        return False

    def add_colour_to_listview(self, colour_to_add):
        if isinstance(colour_to_add, QtGui.QColor):
            colour_to_add = colour_to_add.getRgb()[:-1]

        colour_to_add = tuple(colour_to_add)

        if self.check_if_colour_exists(colour_to_add):
            self.colour_already_in_list(colour_to_add)
            return

        closest = ui_funcs.get_closest_colour(colour_to_add, self.colour_corres_list)
        rgb_value = f'({int(colour_to_add[0])},{int(colour_to_add[1])},{int(colour_to_add[2])})'
        item = QtGui.QStandardItem(f'{closest[1]["DMC Name"]} {rgb_value}')

        item.setForeground((QtGui.QColor(int(closest[2][0] * 255),
                                         int(closest[2][1] * 255),
                                         int(closest[2][2] * 255))))

        item.setBackground(QtGui.QColor(int(colour_to_add[0]),
                                        int(colour_to_add[1]),
                                        int(colour_to_add[2])))
        self.model_listView_choosen_colours.appendRow(item)

    def get_colours(self):
        self.model_listView_choosen_colours.clear()
        self.final_colour_number = self.spinBox_n_colours.value()
        self.colours_to_display = ui_funcs.get_colours(self.initial_img, self.final_colour_number)

        if not self.colours_to_display:
            return

        # TODO: order the list by colour proximity (purely aesthetic)
        for colour in self.colours_to_display:
            self.add_colour_to_listview(colour)

    def colour_already_in_list(self, colour):
        self.label_already_in_list.setText(f"{colour} already in list")

    def add_colour_from_picker(self):
        new_colour = QtWidgets.QColorDialog.getColor()

        print(new_colour)

        if not new_colour:
            return

        self.add_colour_to_listview(new_colour)

    def change_colour_from_picker(self):
        new_colour = QtWidgets.QColorDialog.getColor()

        self.change_colour(new_colour)

    def add_mouse_colour(self):
        if self.model_listView_mouse_colour.item(0) is None:
            return

        new_colour = self.model_listView_mouse_colour.item(0).background().color()

        self.add_colour_to_listview(new_colour)

    def change_colour(self, new_colour):
        if self.check_if_colour_exists(new_colour):
            self.colour_already_in_list(new_colour)
            return

        index = self.listView_choosen_colours.selectedIndexes()
        if len(index) < 1:
            return

        bg_colour = QtGui.QColor(int(new_colour[0]),
                                 int(new_colour[1]),
                                 int(new_colour[2]))
        self.model_listView_choosen_colours.itemFromIndex(index[0]).setBackground(bg_colour)


    def delete_colour(self):
        index = self.listView_choosen_colours.selectedIndexes()
        if len(index) > 0:
            self.model_listView_choosen_colours.removeRow(index[0].row())

    def get_colour_under_mouse(self, event):
        if self.resized_initial_img is None:
            return

        # TODO: pixel offset sometimes (probably has something to do with resizing)
        x = event.localPos().x()
        y = event.localPos().y()

        colour = self.resized_initial_img.pixel(x, y)
        rgb = QtGui.QColor(colour).getRgb()[0:3]

        if self.radioButton_add.isChecked():
            self.add_colour_to_listview(rgb)

        elif self.radioButton_change.isChecked():
            self.change_colour(rgb)

        item = QtGui.QStandardItem()
        item.setBackground(QtGui.QColor(int(rgb[0]),
                                        int(rgb[1]),
                                        int(rgb[2])))

        self.model_listView_mouse_colour.removeRow(0)
        self.model_listView_mouse_colour.appendRow(item)


    def merge_colours(self):
        ui_funcs.merge_colours(self.model_listView_choosen_colours,
                               self.spinBox_merge_colours.value())

    def to_dmc_colours(self):
        colours_list = []
        for i in range(self.model_listView_choosen_colours.rowCount()):
            item = self.model_listView_choosen_colours.item(i)
            colours_list.append(np.asarray(item.background().color().getRgb()[0:3]))

        colour_space = None

        if self.radioButton_to_dmc_lab.isChecked():
            colour_space = 'lab'

        elif self.radioButton_to_dmc_rgb.isChecked():
            colour_space = 'rgb'

        new_colours = ui_funcs.to_dmc_colours(colours_list, self.colour_corres_list, colour_space)

        self.model_listView_choosen_colours.clear()

        for colour in new_colours:
            self.add_colour_to_listview(colour)



    def generate_output(self):
        self.label_image_generation.setText('Generating image...')

        self.colours_to_display = []
        for i in range(self.model_listView_choosen_colours.rowCount()):
            item = self.model_listView_choosen_colours.item(i)
            self.colours_to_display.append(np.asarray(item.background().color().getRgb()[0:3], np.float64) / 255)

        self.new_img = ui_funcs.reduce_colours(self.initial_img, self.colours_to_display)

        label_size = (self.label_original_image.size().height(), self.label_original_image.size().width())

        self.new_img = np.asarray(self.new_img * 255, 'uint8')
        self.new_img = Image.fromarray(self.new_img, mode='RGB')

        self.new_resized_img = ui_funcs.resize_image(self.new_img, label_size)

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
