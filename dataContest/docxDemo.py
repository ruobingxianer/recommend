# -*- coding: utf-8 -*-
import docx
from docx import Document
path = "/Users/wanghaoxian/Desktop/数据大赛/形式审核论文/5_全球马铃薯消费影响因素的实证研究：基于动态面板模型分析.docx"
document = Document(path)
for paragraph in document.paragraphs:
    print ""+paragraph.text