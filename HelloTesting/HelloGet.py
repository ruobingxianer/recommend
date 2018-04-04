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

itemID = '21101000001129'

for i in range(1,10) :
    dom = xml.dom.minidom.parseString(getXmlDataWithItemID(itemID))
    root = dom.documentElement
