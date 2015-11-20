'''
Aggregate the relationships across the multiple relationship collections
to create a single collection that can be searched more easily.

The entries should be formatted as:
{
  repo_a: "twbs/bootstrap",
  repo_b: "zurb/foundation-sites",
  watchers: 123,
  forks: 123,
  commits: 123,
  issues: 123,
  pull_requests: 123,
  total: (123 + 123 + 123 + 123 + 123)
}

These entries should be stored in the collection rel_aggregate

'''

import pymongo

def giterdone(curlist, multiplier, name, count):
	aggregate = client['ossfinder']['rel_aggregate']
	
	#loop through curlist
		#check if the repos exist
			#add the value and increment total by it
		#else
			#add a new doc with the repos, value, and total
	#print(str(count) + " " + tuple(curlist[0]))

	#index = 0
	#while index != count:
	for rel in curlist:
		#rel = curlist[index]
		#print(rel['repo_a'])
		f1 = aggregate.find({'repo_a': {'$in': {rel['repo_a'], rel['repo_b']} } })
		if(f1): print('yes')
		else: print('no')
		#print(f1['repo_a'] + " " + f1['repo_b'] + " " + f1[name])
		#index += 1


client = pymongo.MongoClient(host="da0.eecs.utk.edu")

commits = client['ossfinder']['rel_commits']
forks = client['ossfinder']['rel_forks']
issues = client['ossfinder']['rel_issues']
issuecomments = client['ossfinder']['rel_issuecomments']
pulls = client['ossfinder']['rel_pulls']
watchers = client['ossfinder']['rel_watchers']

giterdone(commits.find({}), 13, "commits", commits.find({}).count())


