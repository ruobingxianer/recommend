import urllib
import urllib2
import xml.dom.minidom

itemID = '21101000001129'
url = 'http://162.105.138.200:8085/symws2016041/rest/standard/lookupTitleInfo'
values = {'clientID': 'SymWSTestClient',
          'itemID': itemID,
          'includeCatalogingInfo': 'true',
          'includeOPACInfo': 'true'}
data = urllib.urlencode(values)
print data
url2 = url + '?' + data
print url2
response = urllib2.urlopen(url2)
the_page = response.read()
print the_page

dom = xml.dom.minidom.parseString(the_page)
root = dom.documentElement
