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


def aggregate_calculate(source, target, multiplier, name):
	curlist = source
	aggregate = target
	# aggregate = client['ossfinder']['rel_aggregate']
	# aggregate.delete_many({})
	#loop through curlist
		#check if the repos exist
			#add the value and increment total by it
		#else
			#add a new doc with the repos, value, and total
	for rel in curlist:
		tot = rel[name] * multiplier
		aggregate.save(rel)
		if(aggregate.find({'repo_a' : rel['repo_a']}).count() > 0): #rel a is f1 a
			for f1 in aggregate.find({'repo_a':rel['repo_a']}):
				if(rel['repo_b'] == f1['repo_b']):
					aggregate.update_one({'_id':f1['_id']}, {"$inc":{name:1}})
					aggregate.update_one({'_id':f1['_id']}, {"$inc":{'total':tot}})
					out = str(['U', rel['repo_a'], rel['repo_b'], name])
					break;
		elif(aggregate.find({'repo_b': rel['repo_a']}).count() > 0): #rel a is f1 b
			for f1 in aggregate.find({'repo_b':rel['repo_a']}):
				if(rel['repo_b'] == f1['repo_a']):
					aggregate.update_one({'_id':f1['_id']}, {"$inc":{name:1}})
					aggregate.update_one({'_id':f1['_id']}, {"$inc":{'total':tot}})
					out = str(['U', rel['repo_a'], rel['repo_b'], name])
					break;
		elif(aggregate.find({'repo_a': rel['repo_b']}).count() > 0): #rel b is f1 a
			for f1 in aggregate.find({'repo_a':rel['repo_b']}):
				if(rel['repo_a'] == f1['repo_b']):
					aggregate.update_one({'_id':f1['_id']}, {"$inc":{name:1}})
					aggregate.update_one({'_id':f1['_id']}, {"$inc":{'total':tot}})
					out = str(['U', rel['repo_a'], rel['repo_b'], name])
					break;
		elif(aggregate.find({'repo_b': rel['repo_b']}).count() > 0): #rel b is f1 b
			for f1 in aggregate.find({'repo_b':rel['repo_b']}):
				if(rel['repo_a'] == f1['repo_a']):
					aggregate.update_one({'_id':f1['_id']}, {"$inc":{name:1}})
					aggregate.update_one({'_id':f1['_id']}, {"$inc":{'total':tot}})
					out = str(['U', rel['repo_a'], rel['repo_b'], name])
					break;
		else: #add a new one to the aggregate relation
			newrel = {'repo_a':rel['repo_a'], 'repo_b':rel['repo_b'], name:rel['name'], total:tot}
			aggregate.save(newrel)
			out = str(['C', rel['repo_a'], rel['repo_b'], name])
