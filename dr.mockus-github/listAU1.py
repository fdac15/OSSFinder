import sys, re, pymongo, json
import requests


jsonDict = {}

client = pymongo.MongoClient (host="da0.eecs.utk.edu")
# Get a reference to a particular database
db = client [sys.argv[1]]
# Reference a particular collection in the database
coll = db [sys.argv[2]]

for r in coll .find ({}):
  a = r[sys.argv[3]]
  n = r[sys.argv[4]]
  for el in n:
    print (str(a) + ';' + str(el[sys.argv[5]]))
