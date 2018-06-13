#!-*- coding:utf8-*-

import networkx as nx

G = nx.Graph()
G.add_node('1')
G.add_edge('2', '3')
print "nodes:", G.nodes()
print "edges:", G.edges()
print "degrees:", G.degree()
print "number of edges:", G.number_of_edges()
