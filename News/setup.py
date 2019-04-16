# Use News Api to extract BBC News Articles
# pip install newsapi first if you have not done already
import json
import newsapi
import requests
api_key = '3014e68bd7bd4196903e79989e41a196'

r = requests.get ('https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey='+api_key)

res = r.json()
for info in res['articles']:
    print(info['title'])
