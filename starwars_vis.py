import sqlite3
import os
import matplotlib.pyplot as plt
import numpy as np

db_name = 'starwars.db'
path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path+'/'+db_name)
cur = conn.cursor()

cur.execute('''SELECT Costs.Name, Costs.Cost, Speeds.Hyperdrive
FROM Costs
LEFT JOIN Speeds
ON Costs.name = Speeds.name''')

joined_db = cur.fetchall()

costs_x = []
speeds_y = []

for i in joined_db:
    if i[0] != 'Death Star' and i[0] != 'Executor' and  i[1] != 'unknown' and i[2] != 'unknown':
            costs_x.append(i[1])
            speeds_y.append(i[2])


plt.scatter(costs_x, speeds_y, c='#c97d3e')
plt.title('Scatter Plot of Hyperdrive Speed vs Price for Star Wars Starships')
plt.annotate('Belbullab-22 Starfighter', (168000, 6))
plt.annotate('Star Destroyer', (150000000, 2))
plt.show()

cur.execute('''SELECT Costs.Name, Costs.Cost, Costs.Length, Speeds.Speed, Speeds.Hyperdrive
FROM Costs
LEFT JOIN Speeds
ON Costs.name = Speeds.name''')

tuples = cur.fetchall()
cost_count = 0
cost_total = 0
length_count = 0
length_total = 0
speed_count = 0
speed_total = 0
for i in tuples:
    if i[1] != 'unknown':
        cost_count += 1
        cost_total += int(i[1])
    if i[2] != 'unknown':
        try:
            length_total += float(i[2])
            length_count += 1
        except:
            None
    if i[3] != 'unknown' and i[3] != 'n/a':
        try:
            speed_total += int(i[3])
            speed_count += 1
        except:
            None

average_cost = cost_total/cost_count
average_length = length_total/length_count
average_speed = speed_total/speed_count

f = open('starwars.txt', 'w')
f.write('Averages of Star Wars Starship Data:' + '\n' + '\n')
f.write('Average Cost: ' + str(average_cost) + ' credits' + '\n')
f.write('Average Length: ' + str(average_length) + ' m' + '\n')
f.write('Average Speed: ' + str(average_speed) + ' kph')
f.close()