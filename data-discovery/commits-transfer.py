
#commits-transfer.py

#procedure:
#- Source collection for commits and target collection for commits.
#- Take 500 repos at a time from the repositories collection.
#- Execute an $in query using the 500 repos on the source collection.
#- All of the results that match the $in query get inserted to the target collection.

import pymongo
from pprint import pprint

client = pymongo.MongoClient (host="da0.eecs.utk.edu")

# Define the source and target collections
repos = client['ossfinder']['repositories']
source = client['test']['commits']
target = client['ossfinder']['commits']

# Create a dict of "full_name" properties for repos
# The full_name is [user]/[repo name] - ex: twbs/bootstrap
repo_full_names = {};

target.delete_many({})

# Populate the dict
skip = 0
limit = 500
count = 1
while count > 0:
	docs = repos.find({}, {"url": 1, "full_name": 1}).skip(skip).limit(limit);
	docs = list(docs)
	skip += limit
	count = len(docs)
	for doc in docs:
		repo_full_names[doc['full_name']] = 0

pprint(repo_full_names)

# Retrieve and iterate over all commits.
# We only care about the url and the commiter, so we are ignoring other fields. 
# Check the commit's url property to see  if it matches one of the full names.
# If it does, add it to a list that will be inserted to the target collection.
skip = 0
limit = 500
count = 1
total = 0
while count > 0:
	docs = source.find({}, {"url": 1, "author": 1}).skip(skip).limit(limit)
	docs = list(docs)
	count = len(docs)
	commits_to_insert = []
	# Loop over the docs, extract the url and full_name properties
	# The full_name property comes from the url
	for doc in docs:
		url = doc['url']
		full_name = '/'.join(url.split('/')[4:6]) #comment
		# If we care about this commit's repo, we need to insert it.
		if full_name in repo_full_names:
			commits_to_insert.append(doc)
			print(full_name, 1)

	# More efficient to insert a list all at once instead of individually
	if len(commits_to_insert) > 0:
		target.insert_many(commits_to_insert)

	skip += limit	
	total += len(commits_to_insert)

	print(len(commits_to_insert), total)


#pprint(repo_full_names)

#while count > 0:
	# Get the docs, the count, and convert docs to a python friendly list
	#docs = source.find(query, fields).skip(skip).limit(limit)
	
	# Initialize a bulk operation - this is more performant than 
	# individual inserts and allows us to "upsert()", which insert_many()
	# doesn't allow 
	#bulk = target.initialize_ordered_bulk_op()
	#for doc in docs:
	#	bulk.find({'id': doc['id']}).upsert().update({'$set': doc})
		#bulk.insert(doc)
	# Execut the bulk operation
	#bulk_result = bulk.execute()
	#pprint(bulk_result)	

	#result = target.insert_many(list(docs))
	#print(result.inserted_ids)
	# Increment values to maintain the loop
	#count = docs.count(with_limit_and_skip=True)
	#count = len(result.inserted_ids)
	#total += count
	#skip += limit

	#print(count, total)

