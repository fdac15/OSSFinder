import pymongo

output = open("issue-output.txt", 'w')

client = pymongo.MongoClient(host="da0.eecs.utk.edu")

issues = client['ossfinder']['issues']
relationships = client['ossfinder']['rel_issues']

relationships.delete_many({})

users = issues.distinct("user.login")

for user in users:
	userIssues = issues.find({"user.login": user}).distinct("full_name")
	if (len(userIssues) > 1):
		for i in range(0, len(userIssues)):
			for j in range(i+1, len(userIssues)):
				rel = relationships.find({'repo_a':user})	
				rel = list(rel)
				if(len(rel) > 0):
					rel = rel[0]
					rel['issues'] = rel['issues']+1
					out = str(['U', userIssues[i], userIssues[j]])
					print(out)
					output.write(out)
				else:
					rel = {'repo_a':userIssues[i], 'repo_b':userIssues[j], 'commits': 1}
					out = str(['C', userIssues[i], userIssues[j]])
					print(out)
					output.write(out)

print('\nDONE')
output.write('\nDONE')
