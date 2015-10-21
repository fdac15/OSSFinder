import sys, re, pymongo

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
limit = 100
count = 4
total = 0
query = {"forks": {"$gt": minForks}, "watchers": {"$gt": minWatchers}}
#fields = {"_id": 0, "id": 1, "name": 1, "description": 1, "owner": 1, "forks": 1, "full_name": 1, "git_url": 1, "watchers": 1, "language": 1}
fields = {"_id": 0}

print('watchers: ', minWatchers)
print('forks: ',  minForks)

# Clear out the target
target.delete_many({})

while count > 1:
	result = source.find(query, fields).skip(skip).limit(limit)
	result_list = list(result)	
	target.insert_many(result_list)
	count = result.count(with_limit_and_skip=True)
	total += count
	skip += limit
	print('inserted: ', count)
	print('   total: ', total)

