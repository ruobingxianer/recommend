# coding=utf-8

import urllib
import urllib2
import xml.dom.minidom
import sys
import time


def getXmlDataWithItemID(itemID):
    url = 'http://162.105.138.200:8085/symws2016041/rest/standard/lookupTitleInfo'
    values = {'clientID': 'SymWSTestClient',
              'itemID': itemID,
              'includeCatalogingInfo': 'true',
              'includeOPACInfo': 'true'}
    data = urllib.urlencode(values)
    url2 = url + '?' + data
    response = urllib2.urlopen(url2)
    xmlData = response.read()
    return str(xmlData)


reload(sys)
sys.setdefaultencoding('utf-8')
wfile = open("/Users/wanghaoxian/Desktop/ckeyTitle0702.txt", "w")
wfile.write("itemID|ckeyinIptron|ckeyinwebService|title\n")

count = 0
file = open("/Users/wanghaoxian/Downloads/bibli-title-empty.csv", "r")
for line in file:
    itemID = line.split("\t")[0]
    ckeyinIptron = line.split("\t")[1][:-1]
    try:
        xmlstr = getXmlDataWithItemID(itemID=str(itemID))
        dom = xml.dom.minidom.parseString(str(xmlstr))
        root = dom.documentElement
        ckey = root.getElementsByTagName("TitleInfo")[0].getElementsByTagName("titleControlNumber")[0].childNodes[
            0].nodeValue
        title = root.getElementsByTagName("TitleInfo")[0].getElementsByTagName("title")[0].childNodes[0].nodeValue
        wfile.write(str(itemID) + "|" + str(ckeyinIptron) + "|" + ckey + "|" + title + "\n")
        wfile.flush()
    except Exception:
        print count
        print str(itemID)
    count = count + 1
    if (count % 1000 == 0):
        print count, time.asctime(time.localtime(time.time()))

wfile.close()
file.close()
