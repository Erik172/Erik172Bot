from settings import api

for tweet in api.search(q='Python', lang='es', rpp=10):
    print(f'@{tweet.user.name}: {tweet.text} \n')