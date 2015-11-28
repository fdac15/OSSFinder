from helpers import pymongo_worker_threads as workers
import aggregate_calculate as agr
import pymongo

output = open('watcher-output.txt', 'w')

client = pymongo.MongoClient(host="da0.eecs.utk.edu")

watchers = client['ossfinder']['watchers']
relationships = client['ossfinder']['rel_watchers']

relationships.delete_many({})

users = watchers.distinct("login")



# Replace this with the function that will process the chunk
# of documents. In our case this will be the aggregate_calculate
# function. 

def worker_function(chunk, relationships, users, output):
	watchers={}
	for user in users:
		watchers[user] = []
	for doc in chunk:
		watchers[doc['login']].append(doc)

	for key, vals in watchers.items():
		print(key, vals)
		
	
'''
	for user in users:
		userWatchers = chunk.find({"login": user}).distinct("full_name")
		if(len(userWatchers) > 1):
			for i in range(0, len(userWatchers)):
				for j in range(i+1, len(userWatchers)):
					rel = relationships.find({'repo_a': userWatchers[i], 'repo_b': userWatchers[j]})
					rel = list(rel)
					if(len(rel) > 0):
						rel = rel[0]
						rel['watchers'] = rel['watchers'] + 1
						out = str(['U', userWatchers[i], userWatchers[j]])
						print(out)
						output.write(out)
						relationships.update_one({'_id': rel['_id']}, {"$inc": {"watchers":1}})
					else:
						rel = {'repo_a': userWatchers[i], 'repo_b': userWatchers[j], 'watchers': 1}
						out = str(['C', userWatchers[i], userWatchers[j]])
						print(out)
						output.write(out)
						relationships.save(rel)
'''

worker_args = {
	'relationships': relationships,
	'users': users,
	'output': output
}

# Call the module function with the correct params named
workers.do_work(source_collection = watchers, worker_function = worker_function, find_args = {}, worker_args = worker_args, num_docs_per_thread = 10000)

