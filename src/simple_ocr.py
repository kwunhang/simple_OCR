"""
This program just open the jpg/png file with cv2 to numpy and call the libray to OCR the image.
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract

# open the image
img = cv2.imread('test_image/sample3.png')
# call library to ocr
# text = pytesseract.image_to_string(img)
text = pytesseract.image_to_string(img)
print(text)
