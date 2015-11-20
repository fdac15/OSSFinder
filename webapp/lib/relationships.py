import pymongo

client = pymongo.MongoClient(host="da0.eecs.utk.edu")
source = client['ossfinder']['rel_aggregate']

'''
Take a list of feature repos and user repos.
Create a matched list.
The matched list consists of 
1) any feature_repos that are in user_repos
2) any feature_repos that have a relationship > 0 with user_repos
Sort the list by relationship value
'''
def match_repos(feature_repos, user_repos):
  


  return feature_repos
