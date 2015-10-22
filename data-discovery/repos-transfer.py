import sys, re, pymongo
from pprint import pprint

client = pymongo.MongoClient (host="da0.eecs.utk.edu")

# Define the source and target collections
source = client['test']['repos']
target = client['ossfinder']['repos']

# Define an index to ensure uniqueness by id
# index = target.create_index([('full_name', pymongo.ASCENDING)], unique=True)

# Query setup
minForks = 20
minWatchers = 20
skip = 0
limit = 200
count = 4
total = 0
query = {"forks": {"$gt": minForks}, "watchers": {"$gt": minWatchers}}
fields = {"_id": 0}

print('watchers: ', minWatchers)
print('forks: ',  minForks)

while count > 1:
	# Get the docs, the count, and convert docs to a python friendly list
	docs = source.find(query, fields).skip(skip).limit(limit)
	
	# Initialize a bulk operation - this is more performant than 
	# individual inserts and allows us to "upsert()", which insert_many()
	# doesn't allow 
	bulk = target.initialize_unordered_bulk_op()
	for doc in docs:
		bulk.find({'id': doc['id']}).upsert().update({'$setOnInsert': doc})
	# Execut the bulk operation
	bulk_result = bulk.execute()
	pprint(bulk_result)	

	# Increment values to maintain the loop
	count = docs.count(with_limit_and_skip=True)
	total += count
	skip += limit

