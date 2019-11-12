from skimage import color
import numpy as np
from math import floor, sqrt
from progress_bar import ProgressBar
from number_display import NumberDisplay
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui

def resize_image(img, max_size):
    size = list(np.asarray(img).shape[:2])

    resized = False

    #TODO: sure about this?
    if size[0] > max_size[0] or size[1] > max_size[1]:
        ratio = min(max_size[1] / size[1], max_size[0] / size[0])
        size[0] = floor(size[0] * ratio)
        size[1] = floor(size[1] * ratio)
        resized = True

    elif size[0] < max_size[0] or size[1] < max_size[1]:
        ratio = min(max_size[1] / size[1], max_size[0] / size[0])
        size[0] = floor(size[0] * ratio)
        size[1] = floor(size[1] * ratio)
        resized = True

    if resized:
        return img.resize(size)

    return img

def get_number_of_colours(img):
    return len(img.getcolors(img.size[0] * img.size[1]))

def get_colours(img, final_colour_number):
    # Get all the colours in the image
    all_colours_rgb = img.getcolors(img.size[0] * img.size[1])

    if final_colour_number > len(all_colours_rgb):
        final_colour_number = len(all_colours_rgb)

    # Convert tuples into lists
    all_colours_rgb = [[x[0], np.asarray(x[1]) / 255] for x in all_colours_rgb]

    final_colours = []

    for _ in range(final_colour_number):
        idx = [x[0] for x in all_colours_rgb].index(max([x[0] for x in all_colours_rgb]))
        final_colours.append(all_colours_rgb[idx][1])
        all_colours_rgb[idx][0] = -1

    return final_colours

def reduce_colours(img_rgb, final_colours):

    if not isinstance(img_rgb, np.ndarray):
        img_rgb = np.asarray(img_rgb) / 255

    final_img = img_rgb.copy()

    # TODO: check if the RGB2LAB conversion MUST occurs at the very last
    # or if the problems I had were because of code problem uh

    pb = ProgressBar('Reducing colours')

    for i in range(final_img.shape[0]):
        for j in range(final_img.shape[1]):
            c1 = color.rgb2lab([[final_img[i, j]]])[0][0]
            c2 = [color.rgb2lab([[x]])[0][0] for x in final_colours]
            distances = [dst(c1, x) for x in c2]
            final_img[i, j] = final_colours[distances.index(min(distances))]

            pb.set_value(floor((((i * final_img.shape[1]) + j) / (final_img.shape[0] * final_img.shape[1])) * 100))
            QApplication.processEvents()

    pb.close()

    return final_img

def dst(c1, c2):
    return sqrt(pow(c2[0] - c1[0], 2) + pow(c2[1] - c1[1], 2) + pow(c2[2] - c1[2], 2))

def get_similarity_matrix(listView_colours):
    list_size = listView_colours.rowCount()
    similarity_matrix = np.zeros((list_size, list_size)) - 1

    for i in range(list_size):
        for j in range(list_size):
            if i != j:
                c1 = np.asarray(listView_colours.item(i).background().color().getRgb()[:-1]) / 255
                c2 = np.asarray(listView_colours.item(j).background().color().getRgb()[:-1]) / 255
                similarity_matrix[i, j] = dst(color.rgb2lab([[c1]])[0][0], color.rgb2lab([[c2]])[0][0])

    return similarity_matrix

def merge_colours(listView_colours, threshold):
    similarity_matrix = get_similarity_matrix(listView_colours)

    all_to_merge = np.where(np.logical_and(similarity_matrix > 0, similarity_matrix < threshold))

    number_display_window = NumberDisplay('Merging colours')
    counter = 0

    while len(all_to_merge[0]) > 0:
        # Get the first one to merge
        to_merge = (all_to_merge[0][0], all_to_merge[1][0])

        # Get colour as RGB values in range [0;1]
        c1 = np.asarray(listView_colours.item(to_merge[0]).background().color().getRgb()[:-1]) / 255
        c2 = np.asarray(listView_colours.item(to_merge[1]).background().color().getRgb()[:-1]) / 255

        # Get colour as LAB
        c1 = color.rgb2lab([[c1]])[0][0]
        c2 = color.rgb2lab([[c2]])[0][0]

        # Is this a godd way to merge colours?
        new_colour_lab = (c1 + c2) / 2.0

        nc = color.lab2rgb([[new_colour_lab]])[0][0] * 255
        nc = QtGui.QColor(int(nc[0]), int(nc[1]), int(nc[2]))

        listView_colours.item(to_merge[0]).setBackground(QtGui.QColor(nc))
        listView_colours.removeRow(to_merge[1])

        counter += 1
        number_display_window.set_value(counter)
        QApplication.processEvents()

        similarity_matrix = get_similarity_matrix(listView_colours)
        all_to_merge = np.where(np.logical_and(similarity_matrix > 0, similarity_matrix < threshold))

    number_display_window.close()
