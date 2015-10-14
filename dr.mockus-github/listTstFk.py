import sys, re, pymongo, json
import requests


jsonDict = {}

client = pymongo.MongoClient (host="da0.eecs.utk.edu")
# Get a reference to a particular database
db = client ['test']
# Reference a particular collection in the database
coll = db ['forks']

for r in coll .find ({}):
  a = r['full_name']
  n = str(r['owner']) + "/" + str(r['name'])
  print (str(n) + ';' + str(a) + ';' + str(r['forks_count']) + ';' + str(r['fork']) + ';' + str(r['watchers_count']))
