import pymongo
from bson.json_util import dumps

client = pymongo.MongoClient(host="da0.eecs.utk.edu")
source = client['ossfinder']['repositories']

def find():
  docs = source.find({}, {"full_name": 1, "html_url": 1, "name": 1, "owner.login": 1})
  return dumps(docs)
