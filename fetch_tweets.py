#!/usr/bin/python3

import os
import requests
import json

f = open('bearer_token.txt')
BEARER_TOKEN = f.read().strip('\n')
f.close()

names = [
    'AgaScigaj',
    'pkukiz',
    'Jaroslaw_Gowin',
    'HannaGillPiatek',
    'Kulesza_pl',
    'KGawkowski',
    'RyszardTerlecki',
    'KosiniakKamysz',
    'bbudka',
]
names = ','.join(names)

res = requests.get(f'https://api.twitter.com/2/users/by?usernames={ names }', headers={
                   'Authorization': f'Bearer {BEARER_TOKEN}'})

ids = list(map(lambda user: user['id'], json.loads(res.text)['data']))
print(ids)


tweets = list(map(lambda id: json.loads(
    requests.get(f'https://api.twitter.com/2/users/{id}/tweets?tweet.fields=public_metrics',
                 headers={'Authorization': f'Bearer {BEARER_TOKEN}'}).text), ids))

print(tweets)
f = open('tweets.json', 'w')
json.dump(tweets, f, indent=4, ensure_ascii=False)
f.close()
