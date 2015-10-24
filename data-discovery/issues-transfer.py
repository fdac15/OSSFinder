#issues-transfer.py

# Procedure overview:
# - Same as the commits-transfer procedure

import pymongo
from pprint import pprint
import transfer_helpers as helpers

client = pymongo.MongoClient (host="da0.eecs.utk.edu")

# Define the source and target collections
repos = client['ossfinder']['repositories']
source = client['test']['issues']
target = client['ossfinder']['issues']

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
		issues_to_insert = []
		for doc in docs:
			full_name = helpers.url_to_full_name(doc['url'])
			if full_name in repo_full_names:
				issues_to_insert.append(doc)
	
		if len(issues_to_insert) > 0:
			target.insert_many(issues_to_insert)
				
		skip += limit
		count = len(docs)
		total += len(issues_to_insert)
		print(len(issues_to_insert), total)
	except:
                print("Unexpected error:", sys.exc_info()[0])
                pass
