# Iterate over repos, compare each of the repos to all of the
# repos after it.

import pymongo
from pprint import pprint

output = open('commit-output.txt', 'w')

client = pymongo.MongoClient(host="da0.eecs.utk.edu")

# Define source and target collections
repositories = client['ossfinder']['repositories']
commits = client['ossfinder']['commits']
relationships = client['ossfinder']['rel_commits']

# Clear 
relationships.delete_many({})

users = commits.distinct("author.login")


for user in users:
	userCommits = commits.find({"author.login": user}).distinct("full_name")
	if (len(userCommits) > 1): #map all relations between the repos
		for i in range(0, len(userCommits)):
			for j in range(i+1, len(userCommits)): #this works
				rel = relationships.find({'repo_a': userCommits[i], 'repo_b': userCommits[j]})
				rel = list(rel)
				if(len(rel) > 0):
					rel = rel[0]
					rel['commits'] = rel['commits'] + 1
					out = str(['U', userCommits[i], userCommits[j]])
					print(out)
					output.write(out)
				else:
					rel = {'repo_a': userCommits[i], 'repo_b': userCommits[j], 'commits': 1}
					out = str(['C', userCommits[i], userCommits[j]])
					print(out)
					output.write(out)

print('\nDONE')
output.write('\nDONE')
