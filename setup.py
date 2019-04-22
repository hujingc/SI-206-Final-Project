# Use News Api to extract Top Articles from different categories in the U.S.
# pip install newsapi first if you have not done already
import json
import newsapi
import csv
import requests
import sqlite3

api_key = '3014e68bd7bd4196903e79989e41a196'
conn = sqlite3.connect('news.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS News')
cur.execute('CREATE TABLE News (news_name TEXT, title TEXT, author TEXT, time_posted TIMESTAMP, news_text TEXT, subject TEXT)')

subjects=['business','sports','entertainment','science', 'technology']
for sub in subjects:
    r = requests.get ('https://newsapi.org/v2/top-headlines?country=us&category='+sub+'&apiKey='+api_key)
    res = r.json()
    cur.execute('SELECT COUNT(*) FROM News')
    count = cur.fetchall()
    start=count[0][0]
    for news in res['articles'][:20]:
        _news_name = news['source']['name']
        _title = news['title']
        _author = news['author']
        _time_posted = news['publishedAt']
        _news_text = news['content']
        _subject = sub
        cur.execute('INSERT INTO News (news_name, title, author, time_posted, news_text, subject) VALUES (?, ?, ?, ?, ?, ?)',
                 (_news_name, _title, _author, _time_posted, _news_text, _subject))
#  Use the database connection to commit the changes to the database
conn.commit()
