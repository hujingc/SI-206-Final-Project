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
cur.execute('CREATE TABLE IF NOT EXISTS NYT (title TEXT, author TEXT, published TIMESTAMP, section TEXT)')

subjects=['arts', 'business','health', 'world','science', 'technology']
for sub in subjects:
        r=requests.get('https://api.nytimes.com/svc/topstories/v2/'+sub+'.json?api-key='+APIKEY)
        res=r.json()
        for news in res['results'][:20]:
                _title = news['title']
                _author = news['byline'][3:]
                _published = news['published_date']
                _section = news['section']
                cur.execute('INSERT INTO NYT (title, author, published, section) VALUES (?, ?, ?, ?)',(_title, _author, _published, _section))
conn.commit()


# SELECT * FROM table_name; select all attributes(columns) from the table → list of tuples basically
# SELECT column1, colunm2 FROM table_name; select columns1 and column2 from table
# INSERT INTO table_name(col1,col2, col3, …) VALUES (val1, val2, val3, …); insert value1, 2, 3 into columns 1,2,3 respectively
# SELECT col1,col2 FROM table_name WHERE condition; select those records from col1 and 2 which fulfill the condition
# UPDATE table_name SET col1 = val1, col2=val2, … WHERE condition; modify the existins records in a table which fulfill the condition
# DELETE FROM tabel_name WHERE condition; delete existing records in table

# DROP tables
# cur.execute(‘DROP TABLE table_name)
# if table doesn’t exist → error. DO NOT USE ABOVE
# Instead: cur.execute(‘DROP TABLE IF EXISTS Pets’)

# CREATE tables
# cur.execute(‘CREATE TABLE Pets(name TEXT, owner TEXT, species TEXT, ages INTEGER, dob TIMESTAMP)’)

# insert records into DB in python
# sql= “INSERT INTO Pets(name, species) VALUES (?,?)”
# val=(“Spot”, “Dog”)
# cur.execute(sql, val)
