import cv2
from PIL import Image, ImageCms
from skimage import color
import numpy as np
from math import floor, sqrt
# Display the initial and final in a console
import tcod as libtcod
import argparse


def compute_similarity_matrix(colours):
    colour_without_occurences = colours
    # If the occurence are in the colours array
    if len(colours[0]) == 2:
        colour_without_occurences = [x[1] for x in colours]

    similarity_matrix = np.zeros((len(colour_without_occurences), len(colour_without_occurences)))

    for i, current_colour in enumerate(colour_without_occurences):
        for j, colour_to_compare in enumerate(colour_without_occurences):
                similarity_matrix[i, j] = sum(abs(np.asarray(current_colour) - np.asarray(colour_to_compare)))

    similarity_matrix = 1 - (similarity_matrix / 255)

    return similarity_matrix

def merge_most_similar(similarity_matrix, colours_lab, replaced_colours, replacement:'bright'):
    # TODO:
    # get most similar
    # merge (take the most lumineuse one)
    # add to dict the replaced colour
    # ex: green replaced by blue, blue replaced by violet -> green replaced by violet too

    # TODO:
    # Maybe actually replace everything in the original image and redo the whole process?

    # Get the most similar colours
    similarity_matrix[similarity_matrix == 1] = -1
    max_idx = np.unravel_index(similarity_matrix.argmax(), similarity_matrix.shape)

    c1_idx = max_idx[0]
    c2_idx = max_idx[1]
    c1 = colours_lab[c1_idx]
    c2 = colours_lab[c2_idx]

    # Compare their luminances : we keep the brightest one
    # TODO: try with lowest and merge
    if replacement == 'bright':
        # c1 is brigther than c2
        brigther_colour = c1
        darker_colour = c2
        brigther_idx = c1_idx
        darker_idx = c2_idx
        # If not, switch them
        if c1[1][0] < c2[1][0]:
            brigther_colour = c2
            darker_colour = c1
            brigther_idx = c2_idx
            darker_idx = c1_idx

        brigther_colour = ','.join([str(x) for x in brigther_colour[1]])
        darker_colour = ','.join([str(x) for x in darker_colour[1]])

        # Add the colours to the replacement array
        replaced_colours[darker_colour] = brigther_colour


        colours_lab[brigther_idx][0] += colours_lab[darker_idx][0]
        del colours_lab[darker_idx]


    return colours_lab, replaced_colours

def replace_colours(img_lab_data, colours_lab, replaced_colours):
    final_img = img_lab_data.copy()
    breakpoint()
    for i in range(final_img.shape[0]):
        for j in range(final_img.shape[1]):
            final_img[i, j] = replaced_colours[colour_to_str(final_img[i, j])]
            breakpoint()

    return final_img

def colour_to_str(colour):
    return ','.join([str(x) for x in colour])

def merge_colours(img_rgb, final_colour_number, all_colours_rgb):
    final_colours = []

    for i in range(final_colour_number):
        idx = [x[0] for x in all_colours_rgb].index(max([x[0] for x in all_colours_rgb]))
        final_colours.append(all_colours_rgb[idx][1])
        all_colours_rgb[idx][0] = -1

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

# return : file to convert, number of color
def parser():
    parser = argparse.ArgumentParser(description="Reduce the color number of a given file.")
    parser.add_argument("filename", metavar="filename", type=str,nargs=1, help="the path of the image")
    parser.add_argument("final_color_number", metavar="N", type=int, nargs='?', default=4, help="the final number of colors")
    args = parser.parse_args()
    return args.filename[0], args.final_color_number

def main():
    filename, final_colour_number = parser()
    
    # img = cv2.imread('tortank.png')
    img = Image.open(filename).convert('RGB')

    # sRGB instead of RGB ([0, 1] instead of [0, 255])
    img_rgb_data = np.asarray(img) / 255

    # Get all the colours in the image
    all_colours_rgb = img.getcolors()

    # Convert tuples into lists
    all_colours_rgb = [[x[0], np.asarray(x[1]) / 255] for x in all_colours_rgb]

    # NEW METHOD:
    # take the 4 most represented colours
    # compute closeness to each colour, assign the closest one
    final_img = merge_colours(img_rgb_data, final_colour_number, all_colours_rgb)

    # MUST specify that the datatype should be uint8 (float in the array),
    # or else it displays a weird image
    final_img = np.asarray(final_img * 255, 'uint8')

    final_img = Image.fromarray(final_img, mode='RGB')
    final_img.show()
    final_img.save('dracaufeu_reduced.png')

    # OLD METHOD

    # # k: original value
    # # v: replacement
    # replaced_colours = {}
    # for elem in colours_lab:
    #     replaced_colours[colour_to_str(elem[1])] = None

    # while len(colours_lab) > final_colour_number:
    #     # Compute the similarity matrix between colours
    #     similarity_matrix = compute_similarity_matrix(colours_lab)
    #     # Merge two colours
    #     colours_lab, replaced_colours = merge_most_similar(similarity_matrix, colours_lab, replaced_colours, 'bright')

    # final_img = replace_colours(img_lab_data, colours_lab, replaced_colours)

if __name__ == '__main__':
    main()