from helpers import pymongo_worker_threads as workers
import aggregate_calculate as agr
import pymongo
import sys

client = pymongo.MongoClient(host="da0.eecs.utk.edu")

# MB:

# Take command line arguments
src = sys.argv[1]
multiplier = int(sys.argv[2])
name = sys.argv[3]
wait_to_join = False
if sys.argv[4].lower() == 'true': wait_to_join = True

source = client['ossfinder'][src]
target = client['ossfinder']['rel_aggregate2']


# Call the module function with the correct params named
workers.do_work(source_collection = source, worker_function = agr.aggregate_calculate, find_args = {}, worker_args = {'target': target, 'multiplier': multiplier, 'name': name}, wait_to_join = wait_to_join)

