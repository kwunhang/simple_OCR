import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract

# open the image
img = cv2.imread('test_image/sample1.jpg')
# call library to ocr
# text = pytesseract.image_to_string(img)
text = pytesseract.image_to_string(img)
print(text)

results = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
for i in range(0, len(results["text"])):
    x = results["left"][i]
    y = results["top"][i]
    
    w = results["width"][i]
    h = results["height"][i]
    text = results["text"][i]
    conf = int(results["conf"][i])
    if conf > 70:
        text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 200), 2)

cv2.imwrite('detacted.jpg',img)