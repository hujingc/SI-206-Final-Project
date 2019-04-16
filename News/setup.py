# Use News Api to extract BBC News Articles
# pip install newsapi first if you have not done already
import json
import newsapi
api_key = '3014e68bd7bd4196903e79989e41a196'

from newsapi.articles import Articles
a = Articles(API_KEY=api_key)
data = a.get(source = "bbc-news", sort_by = 'top')
for info in data['articles']:
    print(info['title'])
