from PIL import Image
import pytesseract
import os
import sys
import cv2
import numpy as np

####################################################################################
########################All image customization methods#############################
# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
 
#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#dilation
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

#skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

#template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)


########################All image customization methods#############################    
#####################Check for more customization choices at########################
#####################https://nanonets.com/blog/ocr-with-tesseract/##################
####################################################################################

def get_text_from_image(image_path):
    text = ""
    try:
        img = cv2.imread(image_path)
        # text = pytesseract.image_to_string(Image.open(image_path))
        img = get_grayscale(img)
        # img = opening(img)
        img = canny(img)
        text = pytesseract.image_to_string(img)
    except Exception as e:
        print("ERROR: Failed to read file - {0}".format(image_path))
        print(e)
    return text
    

def extract_text_from_image(image_path):
    text = get_text_from_image(image_path)
    print("Text extracted from image {0}".format(image_path))
    print("==========================BEGIN=========================")
    print(text)
    print("===========================END==========================")


def get_all_images_from_directory(source_dir):
    image_files = []
    images_dir = os.listdir(source_dir)
    for image_file in images_dir:
        image_files.append(image_file)
    return image_files


def main():
    # images_dir = os.path.join(os.getcwd(), 'images')
    # all_image_files = get_all_images_from_directory(images_dir)

    # for image_file in all_image_files:
    #     extract_text_from_image(os.path.join(images_dir, image_file))
    extract_text_from_image('/home/krishnan/Projects/Grange/Python/text_from_image/images/FortnerGrades.png')

if __name__ == "__main__":
    main()