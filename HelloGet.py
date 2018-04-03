import urllib
import urllib2
import xml.dom.minidom

url = 'http://162.105.138.200:8085/symws2016041/rest/standard/lookupTitleInfo'
values = {'clientID': 'SymWSTestClient',
          'itemID': '21101000576124',
          'includeCatalogingInfo':'true',
          'includeMarcHoldings':'true',
          'marcEntryFilter':'FULL'}
data = urllib.urlencode(values)
print data
url2 = url + '?' + data
response = urllib2.urlopen(url2)
the_page = response.read()
print the_page

dom = xml.dom.minidom.parseString(the_page)
root = dom.documentElement

