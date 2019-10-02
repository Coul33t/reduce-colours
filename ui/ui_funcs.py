from skimage import color
import numpy as np

def get_colours(img, final_colour_number):
    # Get all the colours in the image
    all_colours_rgb = img.getcolors()

    # Convert tuples into lists
    all_colours_rgb = [[x[0], np.asarray(x[1]) / 255] for x in all_colours_rgb]

    final_colours = []

    for i in range(final_colour_number):
        idx = [x[0] for x in all_colours_rgb].index(max([x[0] for x in all_colours_rgb]))
        final_colours.append(all_colours_rgb[idx][1])
        all_colours_rgb[idx][0] = -1

    return final_colours