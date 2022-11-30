import matplotlib.pyplot as plt
import numpy as np
import cv2

filename = 'noise_img.jpg'
image = np.array(cv2.imread(filename))
plt.imshow(image)

ret, image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)

plt.imshow(image)

image = cv2.medianBlur(image, 3)
plt.imshow(image)

plt.imshow(image)

image = cv2.fastNlMeansDenoisingColored(image,None,10,10,7,21)
plt.imshow(image)

import pytesseract

text = pytesseract.image_to_string(image)
print(text)

