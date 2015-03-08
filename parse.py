 #! /usr/bin/python
from crunchbase import CrunchBase
from alchemyapi import AlchemyAPI
from scipy.spatial.distance import hamming
from pandas import DataFrame
import numpy as np
import json
import re


API_KEY = ["2cc5308e35927f10d8401fc6d1c38b43",
			"d4575a0b5179e993ef03d688b50b1c9f",
			"9abd8b0e3660d0af36170779e95abdba",
			"8fa2532bb5d27713be8189371de45074"]
cb = CrunchBase(API_KEY[3])
alchemyapi = AlchemyAPI()

def init_people_list():
	with open('names.txt','a') as namelist, open('person.json') as f:
		for line in f:
			if re.match("(.*)@id(.*)cbi_person(.*)", line):
				line = line.strip()
				line = line[19:]
				r1 = re.compile('(.*)\s*\"')
				m1 = r1.match(line)
				namelist.write(m1.group(1)+"\n")

# def init_people_list():
# 	people = open('person.json')
# 		peoplelist = people['@id']['items']
# 		data = {}

# 		for person in peoplelist:
# 			path = person['path'].split('/')[1]
# 			data[person['name']] = path

# 		with open('data/people.txt','w') as f:
# 			json.dump(data, f)


def generate_tags():
	people_list = open('data/unique.txt').readlines()
	# print len(people_list)
	person_dict = {}
	for idx,permalink in enumerate(people_list):
		if idx % 200 == 0:
			try: 
				bio = cb.getPerson(permalink.split('\n')[0])['data']['properties']['bio']
				keywords = alchemyapi.keywords('text', bio, {'sentiment': 1})['keywords']
				person_dict[permalink.split('\n')[0]] = {}
				for keyword in keywords:
					person_dict[permalink.split('\n')[0]][keyword['text']] = keyword['relevance']
			except:
				pass
		else: continue
		print idx
	with open('data/data3.txt','w') as f:
		json.dump(person_dict,f)

def get_distance_matrix(matrix):
	distance_m = np.zeros(shape=(matrix.shape[0],matrix.shape[0]))
	for i,i_vector in enumerate(matrix):
		for j,j_vector in enumerate(matrix):
			distance_m[i][j] = hamming(i_vector,j_vector)
			print distance_m[i][j]

	return distance_m






# init_people_list()
generate_tags() 
personToTag = json.load(open('data/data.txt'))
m = DataFrame(personToTag).T.fillna(0)
matrix = np.matrix(m).astype(float)



init_people_list()
# personToTag = json.load(open('data/data.txt'))
# print DataFrame(personToTag).T.fillna(0)

