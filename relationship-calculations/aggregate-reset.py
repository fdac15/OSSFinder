import pymongo

client = pymongo.MongoClient(host="da0.eecs.utk.edu")
target = client['ossfinder']['rel_aggregate']

target.delete_many({})

