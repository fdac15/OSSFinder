import pymongo

client = pymongo.MongoClient(host="da0.eecs.utk.edu")
source = client['ossfinder']['rel_aggregate']

'''
Take a list of feature repos and user repos.
feature_repos are the repos that are returned from a feature search (step 1 in the webapp).
user_repos are the repos that the user selected (step 2 in the webapp).

Create a matched list.
The matched list consists of any feature_repos that have a relationship > 0 with user_repos
Sort the list by relationship value.

The returned list should have the format:
[{ full_name: 'user/repo', count: 12345 }, { full_name: 'user/repo', count: 6789}]
'''



#without pre-calculation
#parameter: features is a list of search results, and user_repo is a list of repos that user has selected.
def match_repos(features,user_repos):
    features_refined = list(set(features).difference(set(user_repos)))    
#    Client = pymongo.MongoClient(host='da0.eecs.utk.edu')
#    source = Client['ossfinder']['rel_aggregate']
    return_list = []    
    def calculation(repo_a,repo_b_list):
        count = 0
        for repo_b in repo_b_list:
            link = source.find({"repo_a": repo_a,"repo_b": repo_b})
            if link.count() == 0:
                continue

            count = count + link[0].get('total',0)
        return count
    
    for feature in features_refined:
        return_list.append({'full_name':feature,'count':calculation(feature,user_repos)})
    return sorted(return_list, key=lambda entry: entry['count'], reverse=True)

  

  

