#issues-transfer.py

# Procedure overview:
# - Same as the commits-transfer procedure

import pymongo, sys
from pprint import pprint
import transfer_helpers as helpers

client = pymongo.MongoClient (host="da0.eecs.utk.edu")

# Define the source and target collections
repos = client['ossfinder']['repositories']
source = client['test']['pull_requests']
target = client['ossfinder']['pull_requests']

repo_full_names = helpers.get_repo_full_names(repos);

# Clear out the target collection to ensure a clean copy
target.delete_many({})

skip = 0
limit = 1000
count = 1
total = 0
while count > 0:
	try:
		docs = source.find({}).skip(skip).limit(limit)
		docs = list(docs)
		to_insert = []
		for doc in docs:
			full_name = helpers.url_to_full_name(doc['url'])
			if full_name in repo_full_names:
				to_insert.append(doc)
	
		if len(to_insert) > 0:
			target.insert_many(to_insert)
			
		skip += limit
		count = len(docs)
		total += len(to_insert)
		print(count, len(to_insert), total)
	except:
		print('error with docs')
		print(str(docs))
		pass

