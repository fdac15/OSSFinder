import sys, re, pymongo
from pprint import pprint

# This script copies all of the unique repositories from
# the repositories collection to the repositories_unique 
# collection

client = pymongo.MongoClient (host="da0.eecs.utk.edu")

# Define the source and target collections
source = client['ossfinder']['repositories']
target = client['ossfinder']['repositories_unique']

# Query setup
skip = 0
limit = 500
count = 4
total = 0
unique = {}

target.delete_many({})

while count > 1:
  docs = source.find({}).skip(skip).limit(limit)	
  docs = list(docs)
  to_insert = []
  for doc in docs:
    if doc['full_name'] not in unique:
      to_insert.append(doc)  
    unique[doc['full_name']] = 0
  
  if len(to_insert) > 0:
    result = target.insert_many(to_insert)  

  count = len(docs)  
  total += count
  skip += limit

  print(len(result.inserted_ids), total)
