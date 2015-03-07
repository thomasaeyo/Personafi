#!/usr/bin/python

from crunchbase import CrunchBase
import re
API_KEY = "d4575a0b5179e993ef03d688b50b1c9f"

cb = CrunchBase(API_KEY)
people = cb.getPeople()
peoplelist = people['data']['items']

#output (name, path) json file
data = {}
for person in peoplelist:
  path = person['path'].split('/')[1]
  data[person['name']] = path
  
json_data = json.dumps(data)