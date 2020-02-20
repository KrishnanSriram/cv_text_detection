import PyPDF2
import os

def extract_text_from_pdf(pdf_file):
    # pdf file object
    # you can find find the pdf file with complete code in below
    try:
        pdfFileObj = open(pdf_file, 'rb')
        # pdf reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        # number of pages in pdf
        print("Number of pages: {0}".format(pdfReader.numPages))
        # a page object
        for page in range(1, pdfReader.numPages):
            print("<================>{}<================>".format(page))
            pageObj = pdfReader.getPage(page)
            # extracting text from page.
            # this will print the text you can also save that into String
            print(pageObj.extractText())
    except Exception as e:
        print("EXCEPTION: Read filed with exception")
        print(e)

 
def get_all_pdfs_from_directory(source_dir):
    pdf_files = []
    pdfs_dir = os.listdir(source_dir)
    for pdf_file in pdfs_dir:
        pdf_files.append(pdf_file)
    return pdf_files


def main():
    pdfs_dir = os.path.join(os.getcwd(), 'pdfs')
    all_pdf_files = get_all_pdfs_from_directory(pdfs_dir)

    for pdf_file in all_pdf_files:
        file_path = os.path.join(pdfs_dir, pdf_file)
        print("Text from PDF {0}".format(file_path))
        print("==========================BEGIN=========================")
        extract_text_from_pdf(file_path)
        print("===========================END==========================")
    
    # file_path = "./pdfs/GarciaGSDGrades.pdf"
    # extract_text_from_pdf(file_path)
 
if __name__ == "__main__":
    main()