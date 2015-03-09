 #! /usr/bin/python

import networkx as nx
import matplotlib.pyplot as plt
import csv
import re

def makeGraph():
	G=nx.Graph()
	with open('data/node_edge.csv') as csvfile:
		person_seen = set()
		for line in csvfile.readlines():
			pair = line.split(",",3)
			print pair
			if pair[0] not in person_seen: 
				G.add_node(pair[0])
			if pair[1] not in person_seen: 
				G.add_node(pair[1])
			pair[2] = pair[2]
			if int(weight) > 0:
				print weight
				G.add_edge(pair[0], pair[1], weight=pair[2])
	nx.draw(G)
	plt.show()
	nx.write_gml(G,'data/idata.gml')

makeGraph()