# Use News Api to extract BBC News Articles
# pip install newsapi first if you have not done already
import json
import newsapi
import requests
import sqlite3

api_key = '3014e68bd7bd4196903e79989e41a196'

r = requests.get ('https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey='+api_key)

res = r.json()
# print(res)

# for info in res['articles']:
#     print(info['title'])

# Finish the function setUpNewsTable that takes a list of news, a sqlite connection object, and a cursor and inserts the news information in the database
# Create a database: news.sqlite,
# Load all of the news into a database table called News, with the following columns in each row:
## news_id - containing the unique id that belongs to each article
## title - containing the title for the article 
## author - containing the name of the user who posted the article
## time_posted - containing the date/time value that represents when the article was posted (note that this should be a TIMESTAMP column data type!)
## news_text - containing the text that goes with that article
conn = sqlite3.connect('news.sqlite')
cur = conn.cursor()
# Write code to drop the News table if it exists, and create the table (so you can run the program over and over), 
# with the correct (5) column names and appropriate types for each.
# HINT: Remember that the time_posted column should be the TIMESTAMP data type!
cur.execute('DROP TABLE IF EXISTS News')
cur.execute('CREATE TABLE News (news_id TEXT, title TEXT, author TEXT, time_posted TIMESTAMP, news_text TEXT)')
# Use a for loop, the cursor you defined above to execute INSERT statements
for news in res['articles']:
    # print(tweet)
    _news_id = news['source']['id']
    _title = news['title']
    _author = news['author']
    _time_posted = news['publishedAt']
    _news_text = news['content']
    cur.execute('INSERT INTO News (news_id, title, author, time_posted, news_text) VALUES (?, ?, ?, ?, ?)',
                 (_news_id, _title, _author, _time_posted, _news_text))
#  Use the database connection to commit the changes to the database
conn.commit()


