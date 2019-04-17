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
