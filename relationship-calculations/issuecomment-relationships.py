import pymongo

output = open("issuecomment-output.txt", 'w')

client = pymongo.MongoClient(host="da0.eecs.utk.edu")

issue_comment = client['ossfinder']['issue_comments']
relationships = client['ossfinder']['rel_issuecomments']

relationships.delete_many({})

users = issue_comment.distinct("user.login")

for user in users:
	userIssues = issue_comment.find({"user.login": user}).distinct("full_name")
	if (len(userIssues) > 1):
		for i in range(0, len(userIssues)):
			for j in range(i+1, len(userIssues)):
				rel = relationships.find({'repo_a':user})	
				rel = list(rel)
				if(len(rel) > 0):
					rel = rel[0]
					rel['issue_comments'] = rel['issue_comments']+1
					out = str(['U', userIssues[i], userIssues[j]])
					print(out)
					output.write(out)
					relationships.update_one({'_id': rel['_id']}, {"$inc": {"issue_comments":1}})
				else:
					rel = {'repo_a':userIssues[i], 'repo_b':userIssues[j], 'issue_comments': 1}
					out = str(['C', userIssues[i], userIssues[j]])
					print(out)
					output.write(out)
					relationships.save(rel)

print('\nDONE')
output.write('\nDONE')
