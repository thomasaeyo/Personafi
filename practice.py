from crunchbase import CrunchBase
from alchemyapi import AlchemyAPI

# def get_articles(name):

API_KEY = ["2cc5308e35927f10d8401fc6d1c38b43","d4575a0b5179e993ef03d688b50b1c9f"]
cb = CrunchBase(API_KEY[0])
alchemyapi = AlchemyAPI()

def init_people():
	people = cb.getPeople()
	peoplelist = people['data']['items']
	data = {}

	for person in peoplelist:
		path = person['path'].split('/')[1]
		data[person['name']] = path

	return json.dumps(data)



def get_bio(permalink):
	bio = cb.getPerson(permalink)['data']['properties']['bio']
