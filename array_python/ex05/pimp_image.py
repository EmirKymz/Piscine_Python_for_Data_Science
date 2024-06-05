import numpy as np
from PIL import Image
import cv2

def ft_invert(array) -> np.array:
    """
    Invert the colors of an image.
    :param array: The image data.
    :return: The image data with inverted colors.
    """
    copy_array = array.copy()
    copy_array[..., 0] = 255 - copy_array[..., 0]
    copy_array[..., 1] = 255 - copy_array[..., 1]
    copy_array[..., 2] = 255 - copy_array[..., 2]
    # cv2.imshow('image', copy_array)
    cv2.imwrite("inverted_image.jpg", copy_array)
    return copy_array

def ft_red(array) -> np.array:
    """
     Red filter of an image.
    """
    copy_red = array.copy()
    copy_red[..., 0] = 0
    copy_red[..., 1] = 0

    cv2.imwrite("red_image.jpg", copy_red)
    return copy_red

def ft_green(array) -> np.array:
    """
    Green filter of an image.
    """
    copy_green = array.copy()
    copy_green[:, :, 0] = 0
    copy_green[:, :, 2] = 0
    cv2.imwrite("green_image.jpg", copy_green)
    return copy_green

def ft_blue(array) -> np.array:
    """
    Blue filter of an image.
    """
    copy_blue = array.copy()
    copy_blue[:, :, 1] = 0
    copy_blue[:, :, 2] = 0

    cv2.imwrite("blue_image.jpg", copy_blue)
    return copy_blue


def ft_grey(array) -> np.array:
    """
    Grey filter of an image.
    """
    copy_grey = array.copy()
    copy_grey = cv2.cvtColor(copy_grey, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("grey_image.jpg", copy_grey)
    return copy_grey


# import numpy as np
# import cv2


# def ft_invert(array) -> np.array:
#     """
#     Inverts the colors of an RGB array.
#     """
#     inverted_array = array.copy()
#     inverted_array[..., 0] = 255 - inverted_array[..., 0]
#     inverted_array[..., 1] = 255 - inverted_array[..., 1]
#     inverted_array[..., 2] = 255 - inverted_array[..., 2]
#     cv2.imwrite("inverted_image.jpg", inverted_array)
#     return inverted_array


# def ft_red(array) -> np.array:
#     """
#     Removes the green and blue channels from an RGB array.
#     """
#     red_array = array.copy()
#     red_array[..., 0] = 0
#     red_array[..., 1] = 0
#     cv2.imwrite("red_image.jpg", red_array)
#     return red_array


# def ft_green(array) -> np.array:
#     """
#     Removes the red and blue channels from an RGB array.
#     """
#     green_array = array.copy()
#     green_array[..., 0] = 0
#     green_array[..., 2] = 0
#     cv2.imwrite("green_image.jpg", green_array)
#     return green_array


# def ft_blue(array) -> np.array:
#     """
#     Removes the red and green channels from an RGB array.
#     """
#     blue_array = array.copy()
#     blue_array[..., 1] = 0
#     blue_array[..., 2] = 0
#     cv2.imwrite("blue_image.jpg", blue_array)
#     return blue_array


# def ft_grey(array) -> np.array:
#     """
#     Converts an RGB array to greyscale.
#     """
#     grey_array = array.copy()
#     grey_array = cv2.cvtColor(grey_array, cv2.COLOR_BGR2GRAY)
#     cv2.imwrite("grey_image.jpg", grey_array)
#     return grey_array