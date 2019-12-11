import sqlite3
import os
import matplotlib.pyplot as plt


db_name = 'spotify.db'
path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path+'/'+db_name)
cur = conn.cursor()

cur.execute('SELECT Name, Year FROM Years')

year_total = 0
year_count = 0

for i in cur:
    year_total += i[1]
    year_count += 1

average_year = year_total/year_count

cur.execute('SELECT Name, Length FROM Lengths')

length_total = 0
length_count = 0
for i in cur:
    length_total += i[1]
    length_count += 1

average_length = length_total/length_count


cur.execute('''SELECT Years.Name, Years.Year, Lengths.Length
FROM Years 
LEFT JOIN Lengths 
ON Years.Name  = Lengths.Name;''')

joined_db = cur.fetchall()

years = []
lengths = []

for i in joined_db:
    years.append(i[1])
    lengths.append(i[2])

color = '#3399FF'
plt.scatter(years, lengths, c=color)
plt.title('Song Length vs. Year')
plt.xlabel('Song Year')
plt.ylabel('Song Length (min)')
plt.annotate('American Pie', (1988, 8.59776666666667))
plt.annotate('Hey Jude', (2000, 7.09421666666667))
plt.annotate('Eleanor Rigby', (2000, 2.09776666666667))
plt.show()


cur.execute('SELECT Explicit FROM Explicity')

explicit_count = 0
song_count = 0
for i in cur:
    if i[0]==1:
        explicit_count +=1
    song_count +=1

percent_ex = (explicit_count/song_count)*100

plt.pie([percent_ex, 100-percent_ex], labels = ['Explicit', 'Clean'], colors = ['#912323', '#54a5e3'], autopct= '%.2f')
plt.title('Percent of Songs in my Favorite Playlist that are Explicit')
plt.show()

f = open('spotify.txt', 'w')
f.write('Calculations for Grill & Chill Playlist Data' + '\n' + '\n')
f.write('Average Song Release Year: ' + str(average_year) + '\n')
f.write('Average Song Length: ' + str(average_length) + ' min' + '\n')
f.write('Percent of Songs that are explicit: ' + str(percent_ex))
f.close()

conn.commit()
cur.close()