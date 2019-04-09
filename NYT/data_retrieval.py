#use NYT API here to get the articles data
#then make a cache file for it and cache the data for future use
import json
import csv
import requests

APISecret='zkt6V2HOt9XyBL0G'
api = 'KIBl6ffb7lJrM6UAdpiOwAms0ppqvNf2'

r=requests.get('https://api.nytimes.com/svc/topstories/v2/science.json?api-key='+api)

res=r.json()
for result in res['results']:
    print(result['title'])
