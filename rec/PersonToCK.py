# coding=utf-8
import MySQLdb
import sys
import networkx as nx
import matplotlib.pyplot as plt

reload(sys)
sys.setdefaultencoding('utf-8')

db = MySQLdb.connect("localhost", "root", "whx19911105", "ipatron", charset='utf8')
cursor = db.cursor()
cursor.execute("SELECT icnumber,ckey FROM ipatron.userlog where date_checkout > '2018-01-01 00:00:00'")
data = cursor.fetchall()
print len(data)
mindegree = 4
wfile = open("/Users/wanghaoxian/Desktop/"+str(mindegree)+"net.txt", "w")
wfile.write("Source,Target\r\n")
G = nx.Graph()
for row in data:
    G.add_edge(row[0], row[1])
nodes = G.nodes()
edges = G.edges()
greatNodes = []
greatEdges = []
for node in nodes:
    if(G.degree(node)>mindegree):
        greatNodes.append(node)
print len(greatNodes)
for edge in edges:
    if(edge[0] in greatNodes and edge[1] in greatNodes):
        greatEdges.append(edge)
        wfile.write(edge[0]+","+edge[1]+"\r\n")
print len(greatEdges)

wfile.flush()
wfile.close()
