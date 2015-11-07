import pymongo

output = open('pull-output.txt', 'w')

client = pymongo.MongoClient(host="da0.eecs.utk.edu")

pulls = client['ossfinder']['pull_requests']
relationships = client['ossfinder']['rel_pulls']

relationships.delete_many({})

names = pulls.distinct('full_name')

pullInfo = {}

for name in names:
	userInfo = name.split("/")
	if (pullInfo.has_key(userInfo[0]):
		#person already has another pull, create relation
	else:
		#person doesn't have another pull, add to the dict
		






'''
usernames = []

for name in names:
	username = name.split("/")
	if ((username[0] not in usernames)):
		usernames.append(username[0])
print(usernames)
'''
