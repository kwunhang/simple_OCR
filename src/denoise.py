import numpy as np
import cv2


def denoise(filename: str):
    image = np.array(cv2.imread(filename))
    nor_img = np.zeros((image.shape[0], image.shape[1]))
    image = cv2.normalize(image, nor_img, 0, 255, cv2.NORM_MINMAX)
    image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)[1]
    image = cv2.GaussianBlur(image, (3, 3), 0)
    # remove small pixel
    image = np.invert(image)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
    image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=5)
    image = np.invert(image)
    image = cv2.fastNlMeansDenoisingColored(image,None,10,10,7,21)

    cv2.imwrite('deniose_pic.jpg', image)


if __name__ == "__main__":
    denoise("noise_img.jpg")