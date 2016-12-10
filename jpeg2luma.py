# -*- coding: utf-8 -*-
""" main.py
Sample Code
"""
import math
from PIL import Image
from PIL import ImageOps
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

###
# Main
###
def main():
    """ main function
    """
    image_1 = Image.open("./image1.jpg")
    image_1 = ImageOps.grayscale(image_1)
    image_2 = Image.open("./image2.jpg")
    image_2 = ImageOps.grayscale(image_2)

    isRegulate = True
    npdata_2d_org = get_2d_data(image_1, isRegulate)  # (r, luma)
    # plt.scatter(npdata_2d[:,0], npdata_2d[:,1])
    plt.plot(npdata_2d_org[:,0], npdata_2d_org[:,1])
    npdata_2d_org = get_2d_data(image_2, isRegulate)  # (r, luma)
    plt.plot(npdata_2d_org[:,0], npdata_2d_org[:,1])
    plt.xlabel("distance")
    plt.ylabel("luma")
    plt.xlim([-math.sqrt(image_1.size[0]**2+image_1.size[1]**2)/2, math.sqrt(image_1.size[0]**2+image_1.size[1]**2)/2])
    if isRegulate == True:
        plt.ylim([0, 1])
    else:
        plt.ylim([0, 255])
    plt.show()

    # sample for 3d (too heavy)
    # data_3d = []    # (x, y, luma)
    # for y in range(height):
    #     for x in range(width):
    #         luma = image.getpixel((x, y))
    #         data_3d.append([x-width/2, y-height/2, luma])
    # npdata_3d = np.array(data_3d)
    # X = npdata_3d[:, 0].reshape((width, height))
    # Y = npdata_3d[:, 1].reshape((width, height))
    # Z = npdata_3d[:, 2].reshape((width, height))

    # fig = plt.figure()
    # ax = fig.gca(projection='3d')
    # surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    # ax.zaxis.set_major_locator(LinearLocator(10))
    # ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    # fig.colorbar(surf, shrink=0.5, aspect=5)
    # plt.show()

    print('Exit')

###
# Sub functions
###
def get_2d_data(image, isRegulate):
    """ func_a function
    Args:
        image (class 'PIL.JpegImagePlugin.JpegImageFile'): The original image object
        isRegulate (bool): regulate date
    Returns:
        numpy.ndarray: data array (r, luma)
    """
    data_2d = []    # (r, luma)
    width = image.size[0]
    height = image.size[1]
    for x in range(width):
        y = math.floor(x * height / width)
        luma = image.getpixel((x, y))
        r = math.sqrt((x-width/2)**2 + (y-height/2)**2) * (-1 if x-width/2 < 0 else 1)
        data_2d.append([r, luma])
        # print(r, luma)
    np_data_2d = np.array(data_2d)
    if isRegulate == True:
        np_data_2d[:, 1] = np_data_2d[:, 1] / image.getpixel((width/2, height/2))
    return np_data_2d


if __name__ == "__main__":
    main()
