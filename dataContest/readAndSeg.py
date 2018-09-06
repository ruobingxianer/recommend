# encoding=utf-8
import jieba
import jieba.posseg as pseg
import jieba.analyse

wordsCount = dict()
TFIDFCount = dict()
textrankCount = dict()

#file = open('/Users/wanghaoxian/Desktop/数据大赛/title.txt')
#for line in file:
import os.path
import sys

reload(sys)
sys.setdefaultencoding('utf8')

path = '/Users/wanghaoxian/Desktop/数据大赛/txt'
files = os.listdir(path)
i = 0

for file in files:
    i = i+1
    print i
    fp = open(path + "/" + str(file))
    line = fp.read()
    seg_list = pseg.cut(line)
    for seg in seg_list:
        if len(seg.word) < 2:
            continue
        word = seg.word.encode('utf-8') + ' ' + str(seg.flag)
        if word in wordsCount:
            wordsCount[word] = wordsCount[word] + 1
        else:
            wordsCount[word] = 1

    TFIDF = jieba.analyse.extract_tags(line, withWeight=True)
    for keyword,w in TFIDF:
        if len(keyword) < 2:
            continue
        word = keyword.encode('utf-8')
        if word in TFIDFCount:
            TFIDFCount[word] = TFIDFCount[word] + 1
        else:
            TFIDFCount[word] = 1

    textrank = jieba.analyse.textrank(line, withWeight=True)
    for keyword,w in textrank:
        if len(keyword) < 2:
            continue
        word = keyword.encode('utf-8')
        if word in textrankCount:
            textrankCount[word] = textrankCount[word] + 1
        else:
            textrankCount[word] = 1

    fp.close()

countFile = open('/Users/wanghaoxian/Desktop/数据大赛/AwordCount.txt', 'w')
for key in wordsCount:
    countFile.write(key + "," + str(wordsCount[key]) + '\r\n')
countFile.close()

TFIDFFile = open('/Users/wanghaoxian/Desktop/数据大赛/ATFIDFCount.txt', 'w')
for key in TFIDFCount:
    TFIDFFile.write(key + "," + str(TFIDFCount[key]) + '\r\n')
TFIDFFile.close()

textrankFile = open('/Users/wanghaoxian/Desktop/数据大赛/AtextrankCount.txt', 'w')
for key in textrankCount:
    textrankFile.write(key + "," + str(textrankCount[key]) + '\r\n')
textrankFile.close()
