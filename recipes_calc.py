import sqlite3
import os
import matplotlib.pyplot as plt
import numpy as np

db_name = 'final.db'
path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path+'/'+db_name)
cur = conn.cursor()

# Finding the frequencies of different ingredients and putting them into a dictionary

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

# sorting frequencies to get the top 10 most common ingredients

top_ten = sorted(frequency.keys(), key = lambda x: frequency[x], reverse = True)[1:11]

# Writing calculation to file

filename = 'recipes.txt'
source_dir = os.path.dirname(__file__) #<-- directory name
full_path = os.path.join(source_dir, filename)
f = open(full_path, 'w')
f.write('Most Common Ingredients in Chicken Dishes:' + '\n' + '\n')
for i in top_ten:
    f.write(i + ': ' + str(frequency[i]) + '\n')
f.close()

# Making bar chart of top ten

heights = []
for i in top_ten:
    heights.append(frequency[i])
plt.bar(np.arange(10), np.array(heights))
plt.title('Bar Graph of Most Common Ingredients in Chicken Recipes')
plt.xticks(np.arange(10), top_ten)
plt.xlabel('Ingredients')
plt.ylabel('# of Recipes containing')
plt.show()