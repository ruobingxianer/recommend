#encoding=utf-8

from PyPDF2 import PdfFileReader, PdfFileWriter

infn = 'infn.pdf'
outfn = 'outfn.pdf'
# 获取一个 PdfFileReader 对象
pdf_input = PdfFileReader(open(infn, 'rb'))
# 获取 PDF 的页数
page_count = pdf_input.getNumPages()
print(page_count)
# 返回一个 PageObject
page = pdf_input.getPage(0)
# 获取一个 PdfFileWriter 对象
pdf_output = PdfFileWriter()
# 将一个 PageObject 加入到 PdfFileWriter 中
pdf_output.addPage(page)
# 输出到文件中
pdf_output.write(open(outfn, 'wb'))

