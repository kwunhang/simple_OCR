import helper
import os
import cv2
import numpy as np
import pytesseract
import shutil


def image_ocr(target_file: str):
    print("*" * 10)
    print("Below is the text in" + target_file)
    image = np.array(cv2.imread(target_file))
    ret, image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)
    image = cv2.medianBlur(image, 3)
    image = cv2.fastNlMeansDenoisingColored(image,None,10,10,7,21)
    text = pytesseract.image_to_string(image)
    print(text)

def main():
    directory = "test"
    tmp_directory = "for_pdf"
    tmp_dir_path = os.path.join(directory, tmp_directory)
    for filename in os.listdir(directory):
        target_file = os.path.join(directory, filename)
        if not os.path.isfile(target_file):
            print(target_file + " cannot be found")
            continue
        if os.path.splitext(filename)[1].lower() in {".jpg", ".png", ".JPEG"}:
            # handle with image
            image_ocr(target_file)
        elif os.path.splitext(filename)[1].lower() == ".pdf":
            # handle with pdf
            try:
                os.mkdir(tmp_dir_path)
            except FileExistsError:
                pass
            except:
                print("There are some problems while making tmp_directory.")
                continue
            print(target_file)
            helper.pdf_file_to_img(target_file, tmp_dir_path)
            for tmp_file in os.listdir(tmp_dir_path):
                tmp_file = os.path.join(tmp_file, tmp_dir_path)
                if not os.path.isfile(tmp_file):
                    continue
                image_ocr(tmp_file)
            # clear tmp_dir
            for filename in os.listdir(tmp_dir_path):
                file_path = os.path.join(tmp_dir_path, filename)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))
    if os.path.isdir(tmp_dir_path):
        shutil.rmtree(tmp_dir_path)
    return

if __name__ == "__main__":
    main()