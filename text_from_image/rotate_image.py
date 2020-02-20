from PIL import Image
import os

def rotate_image(image_path):
    # Create an Image object from an Image
    colorImage  = Image.open(image_path)
    # Rotate it by 45 degrees
    # rotated     = colorImage.rotate(45)
    # Rotate it by 90 degrees
    transposed  = colorImage.transpose(Image.ROTATE_270)
    # Display the Original Image
    # colorImage.show()
    # Display the Image rotated by 45 degrees
    # rotated.show()
    # Display the Image rotated by 90 degrees
    transposed.show()
    transposed.save(image_path)

if __name__ == "__main__":
    image_path = "./images/BAILEYPGRADES.jpeg"
    abs_path=os.path.abspath(image_path)
    rotate_image(abs_path)
