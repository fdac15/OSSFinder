import pymongo

client = pymongo.MongoClient(host="da0.eecs.utk.edu")
source = client['ossfinder']['rel_aggregate']

'''
Take a list of feature repos and user repos.
feature_repos are the repos that are returned from a feature search (step 1 in the webapp).
user_repos are the repos that the user selected (step 2 in the webapp).

Create a matched list.
The matched list consists of any feature_repos that have a relationship > 0 with user_repos
Sort the list by relationship value
'''
def match_repos(feature_repos, user_repos):
  matched = []
  
  # Find stuff
  
  # Put stuff in the matched list
  


  return matched
