import pymongo
import pymongo_worker_threads as workers

client = pymongo.MongoClient (host="da0.eecs.utk.edu")
source = client['ossfinder']['repositories']

def worker_function(chunk):
  print(len(chunk))

workers.do_work(source_collection = source, worker_function = worker_function)
