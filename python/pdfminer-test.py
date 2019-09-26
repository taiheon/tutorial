"""
tu: PDFminer
"""
import optparse
from pdfminer.layout import LAParams, LTTextBox
from pdfminer.converter import TextConverter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from io import StringIO

def printText(fileName):
    resource_manager = PDFResourceManager()
    fake_file_handle = StringIO()
    converter = TextConverter(resource_manager,fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager,converter)
    with open(fileName,'rb') as fh:
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            page_interpreter.process_page(page)
        text = fake_file_handle.getvalue()
    converter.close()
    fake_file_handle.close()

    print(text)

def main():
    parser = optparse.OptionParser('usage %prog "+"-F <PDF file name>')
    parser.add_option('-F', dest='fileName', type='string', help ='specify PDF file name')
    (options, args) = parser.parse_args()
    fileName = options.fileName
    if fileName == None:
        print(parser.usage)
        exit()
    else:
        printText(fileName)

if __name__ == '__main__':
    main()
