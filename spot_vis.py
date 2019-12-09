import sqlite3
import os

db_name = 'playlist_data.db'
path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path+'/'+db_name)
cur = conn.cursor()

cur.execute('SELECT name, year FROM Years')

total = 0
count = 0

for i in cur:
    total += i[1]
    count += 1

average_year = total/count

print("Average Year: " + str(average_year))

conn.commit()
cur.close()