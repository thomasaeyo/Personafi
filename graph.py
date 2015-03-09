import matplotlib.pyplot as plt
import networkx as nx
from scipy.spatial.distance import hamming
from pandas import DataFrame
import networkx as nx
import numpy as np
import json
import csv
# from graph_tool.all import *

# returns common edges for person i and j
def get_common_tags(matrix,tag_labels,i,j):
	common_tags = []
	i_vector = np.array(matrix[i]).flatten()
	j_vector = np.array(matrix[j]).flatten()
	idx = 0
	for a,b in zip(i_vector,j_vector):
		if a > 0 and b > 0:
			common_tags.append(tag_labels[idx])
		idx += 1
	return common_tags

def get_count_matrix(matrix):
	def count(i_vector,j_vector):
		i_vector = np.array(i_vector).flatten()
		j_vector = np.array(j_vector).flatten()
		count = [1 if i_vector[x] > 0 and j_vector[x] > 0 else 0 for x in xrange(len(i_vector))]
		return sum(count)

	count_m = np.zeros(shape=(matrix.shape[0],matrix.shape[0]))
	for i,i_vector in enumerate(matrix):
		for j,j_vector in enumerate(matrix):
			count_m[i][j] = count(i_vector,j_vector)
	return count_m

def get_distance_matrix(matrix):
	distance_m = np.zeros(shape=(matrix.shape[0],matrix.shape[0]))
	for i,i_vector in enumerate(matrix):
		for j,j_vector in enumerate(matrix):
			distance_m[i][j] = hamming(i_vector,j_vector)
	return distance_m

def findPeople(personToTag,tag):
	res = [person for person,tags in personToTag.iteritems() if tag in tags]
	return res

def findCommonTag(personToTag,person1,person2):
	intersection = set(personToTag[person1].keys()).intersection(set(personToTag[person2].keys()))
	return intersection


personToTag = json.load(open('data/data3.txt'))
personToTag['geng-tan'] = {'big data platform':0.903587, 'global management consulting':0.871738, 'challenging problems':0.760005, 'MBA':0.719878, 'sernior analyst':0.6954, 'industry reports':0.583186, 'new features':0.579518, 'engineering team':0.575851, 'BCG':0.350661, 'innovation':0.267919, 'associate':0.243626}
temp = [person for person in personToTag]
temp.sort()
person_labels = {}
for idx,person in enumerate(temp):
	person_labels[idx] = person

tag_labels = {}
dataframe = DataFrame(personToTag).T.fillna(0)
for idx,tag in enumerate(dataframe.columns):
	tag_labels[idx] = tag

matrix = np.matrix(dataframe).astype(float)
# distance_matrix = get_distance_matrix(matrix)
count_matrix = get_count_matrix(matrix)

# make graph
# G = nx.Graph()
# for i in xrange(len(count_matrix)):
# 	for j in xrange(i+1,len(count_matrix)):
# 		G.add_edge(person_labels[i],person_labels[j],
# 			weight=count_matrix[i][j],
# 			label=', '.join(str(x) for x in get_common_tags(matrix,tag_labels,i,j))
# 			)
# pos = nx.spring_layout(G)


data = [['source','target','weight','common_tags']]
for i in xrange(len(count_matrix)):
	for j in xrange(i+1,len(count_matrix)):
		source = person_labels[i]
		target = person_labels[j]
		weight = count_matrix[i][j]
		common_tags = ', '.join(str(x) for x in get_common_tags(matrix,tag_labels,i,j))
		data.append([source,target,weight,common_tags])

with open('data/graph_count3.csv','wb') as f:
	csv_writer = csv.writer(f, delimiter=',')
	for x in xrange(4):
		csv_writer.writerow([d[x] for d in data])


nx.draw(G, pos)
# nx.draw_networkx_labels(G, pos, labels = person_labels)
nx.draw_networkx_edge_labels(G, pos, labels = tag_labels)

plt.show()