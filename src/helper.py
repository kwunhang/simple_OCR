import matplotlib.pyplot as plt
import numpy as np
import cv2
from pdf2image import convert_from_path
from PIL import Image
import os

def normalize(image):
    nor_img = np.zeros(shape = (image.shape[0]/2, image.shape[1]/2))
    image = cv2.normalize(image, nor_img, 0, 255, cv2.NORM_MINMAX)
    return image

def image_BW(image):
    ret, image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)
    return image

def gs_blur(image):
    image = cv2.GaussianBlur(image, (3, 3), 0)
    return image

def median_blur(image):
    image = cv2.medianBlur(image, 3)
    return image

def salt_remove(image):
    # remove small pixel
    image = np.invert(image)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
    # image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=5)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=1)
    image = np.invert(image)
    plt.imshow(image)

def invert_color(image):
    image = np.invert(image)
    return image
 
def fmdnoise(image):
    image = cv2.fastNlMeansDenoisingColored(image,None,10,10,7,21)
    return image

def pdf_file_to_img(filename: str, save_dir: str):
    pages = convert_from_path(filename)
    for i in range(len(pages)):
        # print('page'+str(i)+'jpg')
        path = os.path.join(save_dir,'page'+str(i)+'.jpg')
        pages[i].save(path, 'JPEG')

#skew correction
#need try
def deskew(image):
    coords = np.column_stack(np.where(image>0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90+angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.wrapAffine(image, M, (w,h), flages=cv2.INTER_CUBIC, noarderMode=cv2.BORDER_REPLICATE)
    return rotated
