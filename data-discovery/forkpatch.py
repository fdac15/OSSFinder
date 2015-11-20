import pymongo

client = pymongo.MongoClient(host="da0.eecs.utk.edu")

mongoforks = client['ossfinder']['forks']

forks = mongoforks.find()
forks = list(forks)

#fork_owner = "thisis/atest".split('/')
#print(fork_owner[0])

for fork in forks:
	fork_owner = fork['full_name'].split('/')
	print(fork_owner[0])
	mongoforks.replace_one({'_id': fork['_id']}, {"full_name":fork_owner[0]})
	break;	
#print(str.split('/', fork['full_name']))
	#print(fork['full_name'])
