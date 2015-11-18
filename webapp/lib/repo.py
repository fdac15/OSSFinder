import pymongo
from bson.json_util import dumps

client = pymongo.MongoClient(host="da0.eecs.utk.edu")
source = client['ossfinder']['repositories']

# A little cache never hurt
cache = {}

def find():
  cache_key = 'repos'

  if(cache_key not in cache):
    docs = source.find({}, {"full_name": 1, "html_url": 1, "name": 1, "owner.login": 1})
    cache[cache_key] = dumps(docs)

  return cache[cache_key]
