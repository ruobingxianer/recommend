#!-*- coding:utf8-*-

import networkx as nx

G = nx.Graph()
G.add_node('1')
G.add_node('5')
G.add_edge('2', '3')
G.add_edge('4', '3')
edges = G.edges()
for edge in edges:
    print edge[1]
# print "nodes:", G.nodes()
# print "edges:", G.edges()
# print "degrees:", G.degree()
# print "number of edges:", G.number_of_edges()
