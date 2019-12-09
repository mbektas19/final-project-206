import sqlite3
import os
import matplotlib.pyplot as plt

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

cur.execute('''SELECT Years.name, Years.year, Lengths.length
FROM Years 
LEFT JOIN Lengths 
ON Years.name  = Lengths.name;''')

joined_db = cur.fetchall()

years = []
lengths = []

for i in joined_db:
    years.append(i[1])
    lengths.append(i[2])

color = '#3399FF'
plt.scatter(years, lengths, c=color)
plt.title('Song Year vs. Length')
plt.xlabel('Song Year')
plt.ylabel('Song Length')
plt.show()


conn.commit()
cur.close()