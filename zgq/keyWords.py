# encoding=utf-8

File = open('/Users/wanghaoxian/Desktop/zgq/keywords.txt')
wFile = open('/Users/wanghaoxian/Desktop/zgq/result.txt', 'w')
List = []
dic = {}
for line in File:
    List.append(line[:-1].split('	'))
print (len(List))

for line in List:
    if len(line) < 3:
        continue
    for i in range(2, len(line)):
        if len(line[i]) < 2:
            continue
        # year = int(line[1])
        # tag = ''
        # if year < 2000:
        #     tag = '1955-1999'
        # elif year < 2010:
        #     tag = '2000-2009'
        # else:
        #     tag = '2010-'
        #
        # word = tag + '\t' + line[i]
        word = line[i]
        if word in dic:
            dic[word] = dic[word] + 1.00 / (len(line) - 2)
        else:
            dic[word] = 1.00 / (len(line) - 2)

for word, count in dic.items():
    line = word + '\t' + str(count) + '\n'
    wFile.write(line)
wFile.flush()
wFile.close()
