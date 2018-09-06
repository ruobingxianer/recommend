# -*- coding: utf-8 -*-
import docx
from docx import Document
import sys

reload(sys)
sys.setdefaultencoding('utf8')

path = "/Users/wanghaoxian/Desktop/数据大赛/形式审核论文/5_全球马铃薯消费影响因素的实证研究：基于动态面板模型分析.docx"
document = Document(path)
content = ""
for paragraph in document.paragraphs:
    content = content+paragraph.text
wfile = open('/Users/wanghaoxian/Desktop/output.txt',"w")
wfile.write(content)