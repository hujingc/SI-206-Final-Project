# use NYT API here to get the articles data
# then make a cache file for it and cache the data for future use
import json
import csv
import requests
import sqlite3

AppID = 'af9fbb82-d750-4fd6-a708-d01cd0fae0ec'
APIKEY = 'KIBl6ffb7lJrM6UAdpiOwAms0ppqvNf2'
APISecret = 'zkt6V2HOt9XyBL0G'
conn = sqlite3.connect('news.sqlite')
cur = conn.cursor()
cur.execute(
    'CREATE TABLE IF NOT EXISTS NYT (title TEXT, author TEXT, published TIMESTAMP, section TEXT)')

# count how many rows are in the table
cur.execute('SELECT COUNT(*) FROM NYT')
count = cur.fetchall()
start = count[0][0]
print(start)
# this part is so I don't have to run the file 5 times
subjects = ['business', 'health', 'world', 'science', 'technology']
for sub in subjects:
    r = requests.get(
        'https://api.nytimes.com/svc/topstories/v2/'+sub+'.json?api-key='+APIKEY)
    res = r.json()
    num=0
    for news in res['results']:
        _title = news['title']
        _author = news['byline'][3:]
        _published = news['published_date']
        _section = news['section']
        cur.execute("SELECT title FROM NYT WHERE title = ? LIMIT 1", (_title,) )
        if (num<4) and (cur.fetchone()==None):
            num=num+1
            cur.execute('INSERT INTO NYT (title, author, published, section) VALUES (?,?,?,?)',(_title, _author, _published, _section))
        
conn.commit()
cur.execute('SELECT COUNT(*) FROM NYT')
count = cur.fetchall()
end = count[0][0]
print(end)