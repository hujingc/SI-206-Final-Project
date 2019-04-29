import textcleaner as tc
import sqlite3

#pull data from database
conn = sqlite3.connect('news.sqlite')
cur = conn.cursor()
cur.execute('SELECT title, section FROM NYT')
results=cur.fetchall()

#set up initial dictionary
sectionD={}
for result in results:
    title=result[0]
    section=result[1]
    sectionD[section]=sectionD.get(section,0)
    if sectionD[section]==0:
        sectionD[section]=[title]
    else:
        sectionD[section].append(title)

#set up dictionary with list of dictionaryies
for section in sectionD:
    temp={}
    for title in sectionD[section]:
        p1=tc.main_cleaner(title)
        p2=tc.remove_stpwrds(p1)
        p3=p2[0].split()
        for word in p3:
            temp[word]=temp.get(word,0)+1
    print(temp)
