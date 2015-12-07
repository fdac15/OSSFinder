from helpers import pymongo_worker_threads as workers
import aggregate_calculate as agr
import pymongo

client = pymongo.MongoClient(host="da0.eecs.utk.edu")

# MB:

# Take command line arguments
src = sys.argv[1]
multiplier = sys.argv[2]
name = sys.argv[3]

source = client['ossfinder'][src]
target = client['ossfinder']['rel_aggregate']


# Use your aggregate_calculate function as the worker_function

# Replace this with the function that will process the chunk
# of documents. In our case this will be the aggregate_calculate
# function. 
'''
def worker_function(chunk, a, b, c):
  print(len(chunk))
  print(a,b,c)
'''

# Call the module function with the correct params named
workers.do_work(source_collection = source, worker_function = agr, find_args = {}, worker_args = {'source': source, 'target': target, 'multiplier': multiplier, 'name' = name})





