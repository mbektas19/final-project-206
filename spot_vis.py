import sqlite3
import os
import matplotlib.pyplot as plt

####################
# Change file name #
####################
db_name = 'explicity.db'
path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path+'/'+db_name)
cur = conn.cursor()

# Only for playlist_db ########
# cur.execute('SELECT name, year FROM Years')

# total = 0
# count = 0

# for i in cur:
#     total += i[1]
#     count += 1

# average_year = total/count

# print("Average Year: " + str(average_year))

# cur.execute('''SELECT Years.name, Years.year, Lengths.length
# FROM Years 
# LEFT JOIN Lengths 
# ON Years.name  = Lengths.name;''')

# joined_db = cur.fetchall()

# years = []
# lengths = []

# for i in joined_db:
#     years.append(i[1])
#     lengths.append(i[2])

# color = '#3399FF'
# plt.scatter(years, lengths, c=color)
# plt.title('Song Year vs. Length')
# plt.xlabel('Song Year')
# plt.ylabel('Song Length')
# plt.show()

########## 

########### Only for explicity.db ########

cur.execute('SELECT explicit FROM scoBUT')

explicit_count = 0
song_count = 0
for i in cur:
    if i[0]==1:
        explicit_count +=1
    song_count +=1

percent_ex = (explicit_count/song_count)*100
print(percent_ex)

plt.pie([percent_ex, 100-percent_ex], labels = ['Explicit', 'Clean'], colors = ['#912323', '#54a5e3'])
plt.title('Percent of Songs in my Favorite Playlist that are Explicit')
plt.show()

conn.commit()
cur.close()