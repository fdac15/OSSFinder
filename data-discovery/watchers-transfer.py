import pymongo, sys
from pprint import pprint
import transfer_helpers as helpers
import helpers.pymongo_worker_threads as workers

# output file
output = open('watchers-transfer.txt', 'w')

# Define the source and target collections
client = pymongo.MongoClient (host="da0.eecs.utk.edu")
repos = client['ossfinder']['repositories_unique']
source = client['test']['watchers']
target = client['ossfinder']['watchers']

# full names of all of the repos
repo_full_names = helpers.get_repo_full_names(repos);
print('retrieved full names')

# Clear out the target collection to ensure a clean copy
target.delete_many({})
print('deleted from target')

# This is the worker function that gets passed into the do_work function.
# It will be given a "chunk" of mongodb records. It iterates over those
# records to find any documents with a full_name that exists in the "repo_full_names"
# argument. Then it inserts the documents that it finds into the "target" collection.
# Finally it writes some information to the "output" argument.

# It is important to understand that this function DOES NOT execute in the context of this
# script. It executes in the context of the do_work function. So it's like your packing
# your lunch here, but then you're gonna eat it once you get to work. If you need a fork
# and knife to eat your lunch, you put it in your lunch box. "Chunk" is your lunch, and the
# remaining arguments are your fork and knife...
def worker_function(chunk, target, repo_full_names, output):
  info = str(['chunk', len(chunk)])
  print(info)
  output.write(info)
  n_inserted = 0
  for doc in chunk:
    full_name = doc['owner'] + '/' + doc['repo']
    if full_name in repo_full_names:
      doc['full_name'] = full_name
      target.insert(doc)
      n_inserted += 1
    
  info = str(['watchers', n_inserted])
  print(info)
  output.write(info)

# These are the arguments that have to get passed into worker_function
# by the do_work function. These are the fork and knife that you put in
# your lunch box. 
worker_args = {
  'target': target,
  'repo_full_names': repo_full_names,
  'output': output
}

# Finally we call the do_work function, passing in all of the named arguments that we defined above.
# Note, that when passing worker_args = worker_args, the second worker_args refers to the variable 
# defined above.
workers.do_work(source_collection = source, worker_function = worker_function, worker_args = worker_args, num_docs_per_thread=10000)
