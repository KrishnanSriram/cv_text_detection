from __future__ import print_function
from wand.image import Image
from wand.color import Color
import os

def convert_pdf_to_png(pdf_file, png_file):
    with Image(filename=pdf_file) as img:
        print('width =', img.width)
        print('height =', img.height)
        print('pages = ', len(img.sequence))
        print('resolution = ', img.resolution)
        img.background_color = Color("white")
        # img.alpha_channel = 'remove'
        with img.convert('png') as converted:
            converted.save(filename=png_file)

def get_all_pdfs_from_directory(source_dir):
    pdf_files = []
    pdfs_dir = os.listdir(source_dir)
    for pdf_file in pdfs_dir:
        pdf_files.append(pdf_file)
    return pdf_files

def main():
    pdfs_dir = os.path.join(os.getcwd(), 'pdfs')
    pngs_dir = os.path.join(os.getcwd(), 'pngs')
    all_pdf_files = get_all_pdfs_from_directory(pdfs_dir)

    for pdf_file in all_pdf_files:
        file_path = os.path.join(pdfs_dir, pdf_file)
        png_file = pdf_file.replace('.pdf', '.png')
        target_png = os.path.join(pngs_dir, png_file)
        print("==========================BEGIN=========================")
        print("Convert {0} to {1}".format(file_path, target_png))
        convert_pdf_to_png(file_path, target_png)
        print("===========================END==========================")

if __name__ == "__main__":
    # source_pdf = './pdfs/ElliottPeytonGSGradeCard.pdf'
    # target_png = './images/ElliottPeytonGSGradeCard.png'

    # convert_pdf_to_png(source_pdf, target_png)
    main()