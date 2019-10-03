import PIL
from skimage import color
import numpy as np
from math import floor, sqrt

def resize_image(img, max_size):
    size = list(np.asarray(img).shape[:2])

    resized = False

    #TODO: sure about this?
    if size[0] > max_size[0] or size[1] > max_size[1]:
        ratio = min(max_size[1]/size[1], max_size[0]/size[0])
        size[0] = floor(size[0] * ratio)
        size[1] = floor(size[1] * ratio)
        resized = True

    elif size[0] < max_size[0] or size[1] < max_size[1]:
        ratio = min(max_size[1]/size[1], max_size[0]/size[0])
        size[0] = floor(size[0] * ratio)
        size[1] = floor(size[1] * ratio)
        resized = True

    if resized:
        return img.resize(size)

    return img

def get_number_of_colours(img):
    return len(img.getcolors())

def get_colours(img, final_colour_number):
    # Get all the colours in the image
    all_colours_rgb = img.getcolors()

    if final_colour_number > len(all_colours_rgb):
        final_colour_number = len(all_colours_rgb)

    # Convert tuples into lists
    all_colours_rgb = [[x[0], np.asarray(x[1]) / 255] for x in all_colours_rgb]

    final_colours = []

    for i in range(final_colour_number):
        idx = [x[0] for x in all_colours_rgb].index(max([x[0] for x in all_colours_rgb]))
        final_colours.append(all_colours_rgb[idx][1])
        all_colours_rgb[idx][0] = -1

    return final_colours

def merge_colours(img_rgb, final_colours):

    if not isinstance(img_rgb, np.ndarray):
        img_rgb = np.asarray(img_rgb) / 255

    final_img = img_rgb.copy()

    #TODO: check if the RGB2LAB conversion MUST occurs at the very last
    # or if the problems I had were because of code problem uh

    for i in range(final_img.shape[0]):
        for j in range(final_img.shape[1]):
            c1 = color.rgb2lab([[final_img[i, j]]])[0][0]
            c2 = [color.rgb2lab([[x]])[0][0] for x in final_colours]
            distances = [dst(c1, x) for x in c2]
            final_img[i, j] = final_colours[distances.index(min(distances))]

    return final_img

def dst(c1, c2):
    return sqrt(pow(c2[0] - c1[0], 2) + pow(c2[1] - c1[1], 2) + pow(c2[2] - c1[2], 2))