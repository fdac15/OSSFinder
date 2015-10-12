import sys, re, pymongo, json
import requests


jsonDict = {}

client = pymongo.MongoClient (host="da0.eecs.utk.edu")
# Get a reference to a particular database
db = client ['test']
# Reference a particular collection in the database
coll = db ['watchers']

for r in coll .find ({}):
  a = r['login']
  n = str(r['owner']) + "/" + str(r['repo'])
  print (str(n) + ';' + str(a))
