# coding=utf-8

import MySQLdb
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


try:
    db = MySQLdb.connect("localhost", "root", "whx19911105", "ipatron")
    cursor = db.cursor()
    cursor.execute(
        "SELECT item_id,l.ckey FROM ipatron.userlog l, ipatron.bibli b where l.ckey=b.ckey and b.author='' group by item_id,l.ckey")
    data = cursor.fetchall()
    db.close()
except Exception:
    print "db error"

print "db select ok ! null title count", len(data)

reload(sys)
sys.setdefaultencoding('utf-8')
wfile = open("/Users/wanghaoxian/Desktop/ckeyauthor.txt", "w")
wfile.write("itemID|ckeyinIptron|ckeyinwebService|author\n")

count = 0
for row in data:
    try:
        xmlstr = getXmlDataWithItemID(itemID=str(row[0]))
        dom = xml.dom.minidom.parseString(str(xmlstr))
        root = dom.documentElement
        if len(root.getElementsByTagName("TitleInfo")[0].getElementsByTagName("titleControlNumber")) < 1:
            continue
        ckey = root.getElementsByTagName("TitleInfo")[0].getElementsByTagName("titleControlNumber")[0].childNodes[0].nodeValue
        if len(root.getElementsByTagName("TitleInfo")[0].getElementsByTagName("author")) < 1:
            continue
        title = root.getElementsByTagName("TitleInfo")[0].getElementsByTagName("author")[0].childNodes[0].nodeValue
        wfile.write(str(row[0]) + "|" + str(row[1]) + "|" + ckey + "|" + title + "\n")
        wfile.flush()
        if count%1000 == 0:
            print count,"time",time.time()
    except Exception:
        print count
        print str(row[0])
    count = count + 1
wfile.close()
