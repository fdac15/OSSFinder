from helpers import pymongo_worker_threads as workers
import aggregate_calculate as agr
import pymongo

output = open('issue_comment-output-threaded.txt', 'w')

client = pymongo.MongoClient(host="da0.eecs.utk.edu")

issue_comments = client['ossfinder']['issue_comments']
relationships = client['ossfinder']['rel_issue_comments2']

relationships.delete_many({})

# Read all of the unique users in from a file to save some time.
users_file = open('isscom-users.txt', 'r')
users = []
for line in users_file: users.append(line.strip())

# Replace this with the function that will process the chunk
# of documents. In our case this will be the aggregate_calculate
# function. 

def worker_function(chunk, relationships, users, output):
	# dict for key/val storage
	# key: user name
	# val: the repos that the user has watched
	issue_comments={}
	for user in users:
		issue_comments[user] = []

	# iterate over the mongo docs in the chunk
	for doc in chunk:
		# grab the user's list from the dict
		tmp = issue_comments[doc['user']['login']]
		# append the repo full name to the list
		tmp.append(doc['full_name'])
		# store the list back on the issue_comments dict
		issue_comments[doc['user']['login']] = tmp

	for user in users:
		#if the user has more than one watched repo
		if(len(issue_comments[user]) > 1):
			#loop through all of the possible repos
			for i in range(0, len(issue_comments[user])):
				for j in range(i+1, len(issue_comments[user])):
					#check if the relationship already exists
					rel = relationships.find({'repo_a': issue_comments[user][i], 'repo_b': issue_comments[user][j]})
					rel = list(rel)
					#if the relationship already exists, update the issue_comments count
					if(len(rel) > 0):
						rel = rel[0]
						out = str(['U', issue_comments[user][i], issue_comments[user][j]])
						print(out)
						output.write(out)
						relationships.update_one({'_id':rel['_id']}, {"$inc": {"issue_comments":1}})
					#if the relationship doesn't exist, create it
					else:
						rel = {'repo_a': issue_comments[user][i], 'repo_b': issue_comments[user][j], 'issue_comments': 1}
						out = str(['C', issue_comments[user][i], issue_comments[user][j]])
						print(out)
						output.write(out)
						relationships.save(rel)
	
	


worker_args = {
	'relationships': relationships,
	'users': users,
	'output': output
}

# Call the module function with the correct params named
workers.do_work(source_collection = issue_comments, worker_function = worker_function, find_args = {}, worker_args = worker_args, num_docs_per_thread = 10000, wait_to_join = False)

