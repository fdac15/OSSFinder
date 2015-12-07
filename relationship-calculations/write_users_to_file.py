import pymongo

client = pymongo.MongoClient(host="da0.eecs.utk.edu")

issues = client['ossfinder']['issues']
issuecomments = client['ossfinder']['issue_comments']
forks = client['ossfinder']['forks']

i_users_file = open('issue-users.txt', 'w')
i_users = issues.distinct("user.login")
for user in i_users:
	out = str(user + '\n')
	i_users_file.write(out)

ic_users_file = open('isscom-users.txt', 'w')
ic_users = issuecomments.distinct("user.login")
for user in ic_users:
	out = str(user + '\n')
	ic_users_file.write(out)

f_users_file = open('fork-users.txt', 'w')
f_users = forks.distinct("owner")
for user in f_users:
	out = str(user + '\n')
	f_users_file.write(out)

