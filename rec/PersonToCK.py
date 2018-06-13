# coding=utf-8
import MySQLdb
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

db = MySQLdb.connect("localhost", "root", "whx19911105", "ipatron",charset='utf8')
cursor = db.cursor()
cursor.execute("SELECT icnumber,ckey FROM ipatron.userlog where date_checkout > '2018-01-01 00:00:00'")
data = cursor.fetchall()
print len(data)
wfile = open("/Users/wanghaoxian/Desktop/net.txt","w")
wfile.write("Source,Target\r\n")
for row in data :
    wfile.write("p"+row[0]+",b"+row[1]+"\r\n")
wfile.flush()
wfile.close()
