from pydriller import Repository
a = []
b = []

url_text = 'https://github.com/BOY4TOSTOBOY/OprosnikDjango'
for commit in Repository(url_text).traverse_commits():
    commit_url = url_text + '/commit/' + commit.hash
    # print('Hash: {}; '.format(commit.hash))
    # a.append(commit.hash)
    b.append(commit_url)
print(b)

