# -*- coding: utf-8 -*-
import docx
from docx import Document
path = "/Users/wanghaoxian/Desktop/数据大赛/形式审核论文/24_中国卫生统计期刊文献的现状与未来趋势预测.doc"
document = Document(path)
for paragraph in document.paragraphs:
    print(paragraph.text)