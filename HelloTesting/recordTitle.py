import MySQLdb
import urllib
import urllib2
import xml.dom.minidom

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
    return xmlData;
try:
    db = MySQLdb.connect("localhost", "root", "whx19911105", "ipatron")
    cursor = db.cursor()
    cursor.execute("SELECT item_id,l.ckey FROM ipatron.userlog l, ipatron.bibli b where l.ckey=b.ckey and b.title='' group by item_id,l.ckey")
    data = cursor.fetchall()
    db.close()
except Exception :
    print "db error"

print "db select ok ! null title count",len(data)

wfile = open("/Users/wanghaoxian/Desktop/ckeyTitle.txt","w")
wfile.write("itemID|ckey|title\n")


for row in data:
    try:
        itemId = str(row[0]);
        xml = getXmlDataWithItemID(itemId)
        dom = xml.dom.minidom.parseString(xml)
        root = dom.documentElement
        ckey = root.getElementsByTagName("TitleInfo")[0].getElementsByTagName("titleControlNumber")[0].childNodes[0].nodeValue
        title = root.getElementsByTagName("TitleInfo")[0].getElementsByTagName("title")[0].childNodes[0].nodeValue
        wfile.write(itemId+"|"+ckey+"|"+title+"\n")
        wfile.flush()
    except Exception:
        print itemId
        print xml
        break

wfile.close()