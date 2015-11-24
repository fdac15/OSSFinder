from threading import Thread
import pymongo, sys, math

# The worker class defines an object that takes a portion 
# of the collection and runs the aggregation algorithm against it. 
# For example, if begin = 0, end = 1000, skip = 100, then the 
# aggregator object will run the aggregation algorithm against
# records 0-100, 101-200, 201-300, ..., 901-1000.
class Worker(Thread):

  # Constructor that take 
  # property_name is the property we are aggregating,
  # source being aggregated, 
  # target in which aggregations are stored 
  # multiplier for aggregating
  # begin and end defining the span of records to aggregate
  # and skip being the interval at which records are pulled
  # from mongo
  def __init__(self, property_name, source, target, multiplier, begin, end, skip):
    Thread.__init__(self)
    self.property_name = property_name
    self.source = source
    self.target = target
    self.multiplier = multiplier
    self.begin = begin
    self.end = end
    self.skip = skip

  def run(self):

    print('run', self.begin, self.end, self.skip)

    # Searches for and finds the repo in the aggregates collection
    # Returns the 
    # def get_repo_in_aggregates(full_name)


  def get_next_documents(self):
    print('get next documents')

  def aggregate(self, docs):
    print('aggregate')

# Parse command line args and store them for usage
# python3 script.py [collection name] [multiplier]
# ex: python3 script.py rel_commits 3
if len(sys.argv) != 3:
  sys.exit(1)
  
collection_name = sys.argv[1]
multiplier = sys.argv[2]

client = pymongo.MongoClient(host="da0.eecs.utk.edu")
source = client['ossfinder'][collection_name]
target = client['ossfinder']['rel_aggregate']

# find the count of documents to determine number of threads
# that will be spawned.
count = source.find({}).count()

n_docs_per_thread = 1000
n_threads = math.ceil(count / n_docs_per_thread)

# spawn n_threads worker threads
for i in range(0, n_threads):
  worker = Worker(source, target, multiplier, (i * n_docs_per_thread), ((i+1)*n_docs_per_thread), n_docs_per_thread)
  worker.start()
  worker.join()

print(count, n_threads)



'''
db.ProductData.update_one({
  '_id': p['_id']
},{
  '$inc': {
    'd.a': 1
  }
}, upsert=False)
'''
