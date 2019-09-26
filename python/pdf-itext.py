import clr
clr.AddReference("itextsharp")
import iTextSharp, System
from iTextSharp.text import *
from iTextSharp.text.pdf import *
def main():
    ms = System.IO.MemoryStream()
    document = Document()
    writer = PdfWriter.GetInstance(document, ms)
    document.Open()
    chapterFont = FontFactory.GetFont(FontFactory.HELVETICA, 20, Font.BOLDITALIC)
    paragraphFont = FontFactory.GetFont(FontFactory.HELVETICA, 10, Font.NORMAL)
    chunk = Chunk("This is the title", chapterFont)
    chapter = Chapter(Paragraph(chunk), 1)
    chapter.NumberDepth = 0
    chapter.Add(Paragraph("This is the paragraph", paragraphFont))
    document.Add(chapter)
    document.Close()
    bytes = ms.ToArray()
    ms.Close()
    return controller.Action( { "FileContent": bytes, "ContentType": "application/pdf" } )
    pass


if __name__ == '__main__':
    main()
