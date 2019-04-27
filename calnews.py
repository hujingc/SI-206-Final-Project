import sqlite3
import matplotlib
import matplotlib.pyplot as plt

conn = sqlite3.connect('news.sqlite')
cur = conn.cursor()
# Calculate the number and percentage of the news that miss the author's name
cur.execute('SELECT count(news_name) as anonymity FROM News WHERE author IS NULL')
for row in cur:
    print(row[0])
xvals = ["having no author names", "having author names"]
yvals = [row[0],(100-row[0])]


# generate a dictionary that counts the number of news from different media
cur.execute("SELECT * FROM News GROUP BY subject HAVING COUNT(news_name) > 1")
media_dict={}
for row in cur:
    media = row[0]
    media_dict[media] = media_dict.get(media, 0) + 1
print(media_dict)
print(row)
plt.bar(xvals, yvals, align = "center", color = ["skyblue", "cadetblue"])
plt.ylabel("Count of News")
plt.xlabel("Anomity of authors")
plt.title("Number of anonymous news among 100 news")
plt.savefig("bar.png")
plt.show()

# generate a dictionary that counts the number of news from different media
cur.execute("SELECT news_name, count(news_name) as num FROM News WHERE subject == business ORDER BY num DESC LIMIT 3")
for row in cur:
    print(row[0])
    print(row[1])

# use pie chart to show the distribution
"""
labels = ['Mon', 'Tue', 'Wed', 'Thu','Fri','Sat','Sun']
yvals = [day_dict['Mon'], day_dict['Tue'], day_dict['Wed'], day_dict['Thu'], day_dict['Fri'], day_dict['Sat'], day_dict['Sun']]

plt.bar(xvals, yvals, align = "center", color = ["red", "blue", "yellow", "green", "black", "grey", "orange"])
plt.ylabel("Count of days")
plt.xlabel("Days of the week")
plt.title("Number of tweets on different days of the week")
plt.savefig("bar.png")
plt.show()
"""