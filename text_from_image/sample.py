from PIL import Image
import pytesseract
import os
import sys


def get_text_from_image(image_path):
    text = ""
    try:
        text = pytesseract.image_to_string(Image.open(image_path))
        print(text)
    except Exception as e:
        print("ERROR: Failed to read file - {0}".format(image_path))
        print(e)
    return text


if __name__ == "__main__":
    get_text_from_image('./images/ElliottPeytonGSGradeCard.png')