"""
This program is used for adding salt and pepper noise to the image with randomize number.
You can set the prob to control how much noise is added.
"""

import numpy as np
import cv2

def img_noisy(image, prob):
    '''
    Add salt and pepper noise to image
    prob: Probabilty of the noise
    '''
    if len(image.shape) == 2:
        black = 0
        white = 255
    else:
        colorspace = image.shape[2]
        if colorspace == 3: # RGB
            black = np.array([0, 0, 0], dtype='uint8')
            white = np.array([255, 255, 255], dtype='uint8')
        else: #RGBA
            black = np.array([0, 0, 0, 255], dtype='uint8')
            white = np.array([255, 255, 255, 0], dtype='uint8')
    probs = np.random.random(image.shape[:2])
    print(probs < (prob/2))
    image[probs < (prob/2)] = black
    image[probs > 1-(prob/2)] = white if image[probs > 1-(prob/2)] is not black else black
    return image


if __name__ == '__main__':
    image = cv2.imread('test_image/sample1.jpg')
    noise_image = img_noisy(image, 0.001)
    cv2.imwrite('noise_img.jpg', image)