#!/usr/bin/python3

import os
import requests
import json
import sys
import datetime


f = open('bearer_token.txt')
BEARER_TOKEN = f.read().strip('\n')
f.close()

time = datetime.datetime.now().isoformat(
    sep='_', timespec='seconds').replace(':', '-')
result_filename = f'tweets/tweets_{time}.json'

if len(sys.argv) == 2:
    result_filename = sys.argv[1]

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

MAX_RESULTS = 10

print(f'Fetching tweets of: {names}')

res = requests.get(f'https://api.twitter.com/2/users/by?usernames={ names }', headers={
                   'Authorization': f'Bearer {BEARER_TOKEN}'})
ids = list(map(lambda user: user['id'], json.loads(res.text)['data']))

tweets = list(map(lambda id: json.loads(
    requests.get(f'https://api.twitter.com/2/users/{id}/tweets?tweet.fields=public_metrics,created_at&expansions=author_id&max_results={MAX_RESULTS}&user.fields=name',
                 headers={'Authorization': f'Bearer {BEARER_TOKEN}'}).text), ids))

print(tweets)
f = open(result_filename, 'w')
json.dump(tweets, f, indent=4, ensure_ascii=False)
f.close()

print(f'Results written to: {result_filename}')
