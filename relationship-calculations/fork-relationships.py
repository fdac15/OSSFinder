import pymongo

output = open('fork-output.txt', 'w')

client = pymongo.MongoClient(host="da0.eecs.utk.edu")

forks = client['ossfinder']['forks_fixed']
relationships = client['ossfinder']['rel_forks'] 

relationships.delete_many({})

users = forks.distinct("owner")

for user in users:
	userForks = forks.find({"owner": user}).distinct("source_full_name")
	if(len(userForks) > 1):
		for i in range(0, len(userForks)):
			for j in range(i+1, len(userForks)):
				rel = relationships.find({'repo_a': userForks[i], 'repo_b': userForks[j]})
				rel = list(rel)
				if(len(rel) > 0):
					rel = rel[0]
					rel['forks'] = rel['forks'] + 1
					out = str(['U', userForks[i], userForks[j]])
					print(out)
					output.write(out)
					relationships.update_one({'_id': rel['_id']}, {"$inc": {"forks":1}})
				else:
					rel = {'repo_a': userForks[i], 'repo_b': userForks[j], 'forks': 1}
					out = str(['C', userForks[i], userForks[j]])
					print(out)
					output.write(out)
					relationships.save(rel)
print('\nDONE')
output.write('\nDONE')
