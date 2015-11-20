import sys, re, pymongo
from pprint import pprint

# This script copies all of the unique repositories from
# the repositories collection to the repositories_unique 
# collection

client = pymongo.MongoClient (host="da0.eecs.utk.edu")

# Define the source and target collections
source = client['ossfinder']['forks']
target = client['ossfinder']['forks_fixed']

# Query setup
skip = 0
limit = 500
count = 4
total = 0

target.delete_many({})

while count > 1:
  docs = source.find({}).skip(skip).limit(limit)	
  docs = list(docs)
  to_insert = []
  for doc in docs:
    doc["source_owner"] = doc["owner"]
    doc["owner"] = str(doc["url"]).split("/")[5]
    to_insert.append(doc)

  if len(to_insert) > 0:
    result = target.insert_many(to_insert)  

  count = len(docs)  
  total += count
  skip += limit

  print(len(result.inserted_ids), total)
