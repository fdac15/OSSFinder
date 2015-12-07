from helpers import pymongo_worker_threads as workers
import aggregate_calculate as agr
import pymongo

client = pymongo.MongoClient(host="da0.eecs.utk.edu")
source = client['ossfinder']['repositories']

# MB:

# Take command line arguments

# Use your aggregate_calculate function as the worker_function

# Replace this with the function that will process the chunk
# of documents. In our case this will be the aggregate_calculate
# function. 
def worker_function(chunk, a, b, c):
  print(len(chunk))
  print(a,b,c)


# Call the module function with the correct params named
workers.do_work(source_collection = source, worker_function = worker_function, find_args = {}, worker_args = {'a': 1, 'b': 2, 'c': 3})





