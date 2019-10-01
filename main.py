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

def merge_colours(img, final_colour_number, colours_lab):
    final_colours = []
    for i in range(final_colour_number):
        idx = [x[0] for x in colours_lab].index(max([x[0] for x in colours_lab]))
        final_colours.append(colours_lab[idx][1])
        colours_lab[idx][0] = -1

    final_img = img.copy()

    for i in range(final_img.shape[0]):
        for j in range(final_img.shape[1]):
            distances = [dst(final_img[i, j], x) for x in final_colours]
            print(distances)
            final_img[i, j] = final_colours[distances.index(min(distances))]

    return final_img

def dst(c1, c2):
    return sqrt(pow(c2[0] + c1[0], 2) + pow(c2[1] + c1[1], 2) + pow(c2[2] + c1[2], 2))

def main():
    final_colour_number = 4
    # img = cv2.imread('tortank.png')
    img = Image.open('tortank.png').convert('RGB')

    # Convert to Lab colourspace
    srgb_p = ImageCms.createProfile("sRGB")
    lab_p  = ImageCms.createProfile("LAB")

    rgb2lab = ImageCms.buildTransformFromOpenProfiles(srgb_p, lab_p, "RGB", "LAB")
    img_lab = ImageCms.applyTransform(img, rgb2lab)

    img_lab_data = np.asarray(img_lab)

    # Get all the colours in the image
    colours_lab = img_lab.getcolors()
    # Convert tuples into lists
    colours_lab = [[x[0], list(x[1])] for x in colours_lab]
    final_img = merge_colours(img_lab_data, final_colour_number, colours_lab)
    final_img = Image.fromarray(final_img, 'LAB')

    lab2rgb = ImageCms.buildTransformFromOpenProfiles(lab_p, srgb_p, "LAB", "RGB")
    final_img = ImageCms.applyTransform(final_img, lab2rgb)

    breakpoint()
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