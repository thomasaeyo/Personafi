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
<<<<<<< HEAD
<<<<<<< HEAD
		namelist.seek(0)
		namelist.truncate()
=======
>>>>>>> 09f3195f26176ef3358671d9ff817004c880f209
=======
>>>>>>> 1a0e88121cfde0aa52b55606f85f54fc1cfac5c9
		for line in f:
			if re.match("(.*)@id(.*)cbi_person(.*)", line):
				line = line.strip()
				line = line[19:]
				r1 = re.compile('(.*)\s*\"')
				m1 = r1.match(line)
				namelist.write(m1.group(1)+"\n")

<<<<<<< HEAD
<<<<<<< HEAD
def remove_dups():
	lines_seen = set() # holds lines already seen
	outfile = open('unique.txt', "a")
	for line in open('names.txt', "r"):
	    if line not in lines_seen: # not a duplicate
	        outfile.write(line)
	        lines_seen.add(line)
	outfile.close()

=======
>>>>>>> 09f3195f26176ef3358671d9ff817004c880f209
=======
>>>>>>> 1a0e88121cfde0aa52b55606f85f54fc1cfac5c9
# def init_people_list():
# 	people = open('person.json')
# 		peoplelist = people['@id']['items']
# 		data = {}

# 		for person in peoplelist:
# 			path = person['path'].split('/')[1]
# 			data[person['name']] = path

# 		with open('data/people.txt','w') as f:
# 			json.dump(data, f)


<<<<<<< HEAD
<<<<<<< HEAD
# def generate_tags():
# 	people_list = json.load(open('data/people.txt'))
# 	personToTag = {}
# 	for idx,p in enumerate(people_list):
# 		name = p.split(' ')
# 		first_name = name[0]
# 		last_name = name[1]
# 		try: 
# 			bio = cb.getPerson(people_list[p])['data']['properties']['bio']
# 			keywords = alchemyapi.keywords('text', bio, {'sentiment': 1})['keywords']
# 			# find the person
# 			found = False
# 			for i,ptt in personToTag.iteritems():
# 				if ptt['first_name'] == first_name and ptt['last_name'] == last_name:
# 					person = i
# 					found = True
# 					break
# 			if not found: 
# 				person = idx
# 				personToTag[idx] = {'first_name':first_name,'last_name':last_name,'tags':{}
# 			# update tags
# 			try: tags = personToTag[person]['tags']
# 			except KeyError: personToTag[person]['tags'] = {}; tags = {}
# 			for keyword in keywords:
# 				if keyword['text'] in tags:
# 					new_tags = tags
# 					new_tags[keyword['text']]['relevance'] = (new_tags[keyword['text']]['relevance']*new_tags[keyword['text']]['count'] + keyword['relevance']) / (new_tags[keyword['text']]['count'] + 1)
# 					new_tags[keyword['text']]['count'] += 1
# 				else:
# 					new_tags = tags
# 					new_tags[keyword['text']] = {'relevance':keyword['relevance'], 'count':1}
# 				personToTag[person]['tags'] = new_tags
# 		except:
# 			pass
# 	with open('data/data.txt','w') as f:
# 		json.dump(personToTag,f)


=======
>>>>>>> 09f3195f26176ef3358671d9ff817004c880f209
=======
>>>>>>> 1a0e88121cfde0aa52b55606f85f54fc1cfac5c9
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

<<<<<<< HEAD
<<<<<<< HEAD

# def generate_tags():
# 	people_list = json.load(open('data/people.txt'))
# 	# print len(people_list)
# 	person_dict = {}
# 	for p,permalink in people_list.iteritems():
# 		try: 
# 			bio = cb.getPerson(people_list[p])['data']['properties']['bio']
# 			keywords = alchemyapi.keywords('text', bio, {'sentiment': 1})['keywords']
# 			person_dict[permalink] = {}
# 			for keyword in keywords:
# 				person_dict[permalink][keyword['text']] = keyword['relevance']
# 		except:
# 			pass
# 	with open('data/data_entities.txt','w') as f:
# 		json.dump(person_dict,f)

=======
>>>>>>> 09f3195f26176ef3358671d9ff817004c880f209
=======
>>>>>>> 1a0e88121cfde0aa52b55606f85f54fc1cfac5c9
def get_distance_matrix(matrix):
	distance_m = np.zeros(shape=(matrix.shape[0],matrix.shape[0]))
	for i,i_vector in enumerate(matrix):
		for j,j_vector in enumerate(matrix):
			distance_m[i][j] = hamming(i_vector,j_vector)
			print distance_m[i][j]

	return distance_m



<<<<<<< HEAD
<<<<<<< HEAD
=======



>>>>>>> 09f3195f26176ef3358671d9ff817004c880f209
=======



>>>>>>> 1a0e88121cfde0aa52b55606f85f54fc1cfac5c9
# init_people_list()
generate_tags() 
personToTag = json.load(open('data/data.txt'))
m = DataFrame(personToTag).T.fillna(0)
matrix = np.matrix(m).astype(float)

<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 1a0e88121cfde0aa52b55606f85f54fc1cfac5c9


init_people_list()
# personToTag = json.load(open('data/data.txt'))
# print DataFrame(personToTag).T.fillna(0)

<<<<<<< HEAD
>>>>>>> 09f3195f26176ef3358671d9ff817004c880f209
=======
>>>>>>> 1a0e88121cfde0aa52b55606f85f54fc1cfac5c9
