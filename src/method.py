import matplotlib.pyplot as plt
import numpy as np
import cv2
from pdf2image import convert_from_path
from PIL import Image


def normalize(image): 
    # change the size of img(e.g. change the img from 1000*500pixel to 2000*1000), u can both enlarge or smaller the image.
    # Since there may be some library is more sensitive to specific image size
    nor_img = np.zeros(shape = (image.shape[0]*2, image.shape[1]*2))
    image = cv2.normalize(image, nor_img, 0, 255, cv2.NORM_MINMAX)
    return image

def image_BW(image): #black white the image
    ret, image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)
    return image

def gs_blue(image):
    # it use a blur method from library to try to denose.
    # It help on denoise but also blur the original image which contain the word we want.
    image = cv2.GaussianBlur(image, (3, 3), 0)
    return image

def median_blur(image):
    # another blur library.
    # This library is taking method just like remvoing pixel smaller than specific size.
    image = cv2.medianBlur(image, 3)
    return image

def salt_remove(image):
    # remove small pixel from the image with specific space.
    image = np.invert(image)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
    # image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=5)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=1)
    image = np.invert(image)
    plt.imshow(image)

def invert_color(image):
    # invert the color of image e.g. black to white, white to black
    image = np.invert(image)
    return image
 
def fmdnoise(image):
    # another build in method to denoise the image. It not so useful in our case.
    image = cv2.fastNlMeansDenoisingColored(image,None,10,10,7,21)
    return image

def pdf_file_to_img(filename: str):
    # open a pdf file and convert it to jpg/png in pages
    pages = convert_from_path(filename)
    print(pages)
    for i in range(len(pages)):
        print('page'+str(i)+'jpg')
        pages[i].save('page'+str(i)+'.jpg', 'JPEG')
