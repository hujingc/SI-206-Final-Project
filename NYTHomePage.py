#use NYT API here to get the articles data
#then make a cache file for it and cache the data for future use
import json
import csv
import requests
import sqlite3

AppID = 'af9fbb82-d750-4fd6-a708-d01cd0fae0ec'
APIKEY='KIBl6ffb7lJrM6UAdpiOwAms0ppqvNf2'
APISecret='zkt6V2HOt9XyBL0G'
conn = sqlite3.connect('news.sqlite')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS NYTHome (title TEXT, author TEXT, published TIMESTAMP, section TEXT)')

r=requests.get('https://api.nytimes.com/svc/topstories/v2/home.json?api-key='+APIKEY)
res=r.json()
cur.execute('SELECT COUNT(*) FROM NYTHome')
count = cur.fetchall()
start=count[0][0]
print(count)
print(start)
for news in res['results'][start:start+20]:
        _title = news['title']
        _author = news['byline'][3:]
        _published = news['published_date']
        _section = news['section']
        cur.execute('INSERT INTO NYTHome (title, author, published, section) VALUES (?, ?, ?, ?)',(_title, _author, _published, _section))
conn.commit()