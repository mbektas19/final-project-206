import sqlite3
import os
import matplotlib.pyplot as plt


db_name = 'final.db'
path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path+'/'+db_name)
cur = conn.cursor()

# Calculates the average year of a song

cur.execute('SELECT Name, Year FROM Years')

year_total = 0
year_count = 0

for i in cur:
    year_total += i[1]
    year_count += 1

average_year = year_total/year_count

# Calculates the average length of a song

cur.execute('SELECT Name, Length FROM Lengths')

length_total = 0
length_count = 0
for i in cur:
    length_total += i[1]
    length_count += 1

average_length = length_total/length_count

# Joins two tables so they can be put into lists for the scatterplot
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

# Scatterplot of lengths vs year

color = '#3399FF'
plt.scatter(years, lengths, c=color)
plt.title('Song Length vs. Year')
plt.xlabel('Song Year')
plt.ylabel('Song Length (min)')
plt.annotate('American Pie', (1988, 8.59776666666667))
plt.annotate('Hey Jude', (2000, 7.09421666666667))
plt.annotate('Eleanor Rigby', (2000, 2.09776666666667))
plt.show()

# Calculates the percents of songs that are explicit

cur.execute('SELECT Explicit FROM Explicity')

explicit_count = 0
song_count = 0
for i in cur:
    if i[0]==1:
        explicit_count +=1
    song_count +=1

percent_ex = (explicit_count/song_count)*100

# Plots the percentage of songs that are explicit in a pie chart

plt.pie([percent_ex, 100-percent_ex], labels = ['Explicit', 'Clean'], colors = ['#912323', '#54a5e3'], autopct= '%.2f')
plt.title('Percent of Songs in my Favorite Playlist that are Explicit')
plt.show()

# Writes all calculated data to a file

filename = 'songs.txt'
source_dir = os.path.dirname(__file__) #<-- directory name
full_path = os.path.join(source_dir, filename)
f = open(full_path, 'w')
f.write('Calculations for Grill & Chill Playlist Data' + '\n' + '\n')
f.write('Average Song Release Year: ' + str(average_year) + '\n')
f.write('Average Song Length: ' + str(average_length) + ' min' + '\n')
f.write('Percent of Songs that are explicit: ' + str(percent_ex) + '\n' + '\n')
f.close()

conn.commit()
cur.close()