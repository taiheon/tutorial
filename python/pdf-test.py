"""
tu for PyPDF and optparse
E:/GoogleDrive/python/tu/pdf-test.py -F "..\re\python cheatkey.pdf"
"""
import optparse
import PyPDF2 as p2

def printMeta(fileName):
    pdfFile = p2.PdfFileReader(open(fileName, 'rb'))
    docInfo = pdfFile.getDocumentInfo()
    print('[*] PDF MetaData For : ' + str(fileName))
    for metaItem in docInfo:
        print('[+] ' + metaItem + ':' + docInfo[metaItem])
    #print('[+] ' + 'getNumPages:' + pdfFile.getNumPages())
    print('[+] getNumPages():' + str(pdfFile.getNumPages()))


def main():
    parser = optparse.OptionParser('usage %prog "+"-F <PDF file name>')
    parser.add_option('-F', dest='fileName', type='string', help ='specify PDF file name')
    (options, args) = parser.parse_args()
    fileName = options.fileName
    if fileName == None:
        print(parser.usage)
        exit()
    else:
        printMeta(fileName)

if __name__ == '__main__':
    main()
