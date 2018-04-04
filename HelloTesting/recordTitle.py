# coding=utf-8

import MySQLdb
import urllib
import urllib2
import xml.dom.minidom
import sys


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
        "SELECT item_id,l.ckey FROM ipatron.userlog l, ipatron.bibli b where l.ckey=b.ckey and b.title='' group by item_id,l.ckey")
    data = cursor.fetchall()
    db.close()
except Exception:
    print "db error"

print "db select ok ! null title count", len(data)

reload(sys)
sys.setdefaultencoding('utf-8')
wfile = open("/Users/wanghaoxian/Desktop/ckeyTitle.txt", "w")
wfile.write("itemID|ckeyinIptron|ckeyinwebService|title\n")

count = 0
for row in data:
    try:
        xmlstr = getXmlDataWithItemID(itemID=str(row[0]))
        dom = xml.dom.minidom.parseString(str(xmlstr))
        root = dom.documentElement
        ckey = root.getElementsByTagName("TitleInfo")[0].getElementsByTagName("titleControlNumber")[0].childNodes[0].nodeValue
        title = root.getElementsByTagName("TitleInfo")[0].getElementsByTagName("title")[0].childNodes[0].nodeValue
        wfile.write(str(row[0]) + "|" + str(row[1]) + "|" + ckey + "|" + title + "\n")
        wfile.flush()
    except Exception:
        print count
        print str(row[0])
    count = count + 1

wfile.close()
