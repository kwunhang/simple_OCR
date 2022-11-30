"""
This program convert the image to binary image before using the tessaract library.
It would help a bit for OCR if the image is colored originally
"""
import cv2
import numpy as numpy
import matplotlib.pyplot as plt

# open the image
img = cv2.imread('noise_img.jpg')
# plt.imshow(img, cmap='gray')
# cv2.imshow('asd',img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_image.jpg',img)