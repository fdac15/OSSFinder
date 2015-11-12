import pymongo

output = open('pull-output.txt', 'w')

client = pymongo.MongoClient(host="da0.eecs.utk.edu")

pulls = client['ossfinder']['pull_requests']
relationships = client['ossfinder']['rel_pulls']

relationships.delete_many({})

users = pulls.distinct('user.login')

for user in users:
	userPulls = pulls.find({'user.login': user}).distinct("full_name")
	if(len(userPulls) > 1):
		for i in range(0, len(userPulls)):
			for j in range(i+1, len(userPulls)):
				rel = relationships.find({'repo_a': userPulls[i], 'repo_b': userPulls[j]})
				rel = list(rel)
				if(len(rel) > 0):
					rel = rel[0]
					rel['users'] = rel['users'] + 1
					out = str(['U', userPulls[i], userPulls[j]])
					print(out)
					output.write(out)
					relationships.update_one({'_id':rel['_id']}, {'$inc':{'pulls':1}})
				else:
					rel = {'repo_a':userPulls[i], 'repo_b': userPulls[j], 'pulls': 1}
					out = str(['C', userPulls[i], userPulls[j]])
					print(out)
					output.write(out)
					relationships.save(rel)

print('\nDONE')
output.write('\nDONE')
