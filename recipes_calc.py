import sqlite3
import os
import matplotlib.pyplot as plt
import numpy as np

db_name = 'final.db'
path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path+'/'+db_name)
cur = conn.cursor()

cur.execute('''SELECT Chicken.Recipe, Chicken.Ingredient1, Chicken.Ingredient2, Chicken.Ingredient3, Chicken.Ingredient4,
Chicken.Ingredient5, Chicken2.Ingredient6
FROM Chicken 
LEFT JOIN Chicken2 
ON Chicken.Recipe = Chicken2.Recipe;''')

joined_db = cur.fetchall()

frequency = {}

for i in joined_db:
    for x in i[1:]:
        if x in frequency:
            frequency[x] += 1
        else:
            frequency[x] = 1

top_ten = sorted(frequency.keys(), key = lambda x: frequency[x], reverse = True)[1:11]


f = open('recipes.txt', 'w')
f.write('Most Common Ingredients in Chicken Dishes:' + '\n' + '\n')
for i in top_ten:
    f.write(i + ': ' + str(frequency[i]) + '\n')
f.close()

heights = []
for i in top_ten:
    heights.append(frequency[i])
plt.bar(np.arange(10), np.array(heights))
plt.title('Bar Graph of Most Common Ingredients in Chicken Recipes')
plt.xticks(np.arange(10), top_ten)
plt.xlabel('Ingredients')
plt.ylabel('# of Recipes containing')
plt.show()