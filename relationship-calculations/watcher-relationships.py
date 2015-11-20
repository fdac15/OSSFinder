import pymongo

output = open('watcher-output.txt', 'w')

client = pymongo.MongoClient(host="da0.eecs.utk.edu")

watchers = client['ossfinder']['watchers']
relationships = client['ossfinder']['rel_watchers']

relationships.delete_many({})

users = watchers.distinct("login")

for user in users:
	userWatchers = watchers.find({"login": user}).distinct("full_name")
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
print('\nDONE')
output.write('\nDONE')
