import sqlite3
import os
import matplotlib.pyplot as plt
import numpy as np

db_name = 'yelp.db'
path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path+'/'+db_name)
cur = conn.cursor()

category_counts = {}
rating_totals = {}
price_totals = {}
tuples = []

cur.execute('SELECT Category, Rating FROM Ratings')
cur.execute('''SELECT Ratings.Name, Ratings.Category, Ratings.Rating, Prices.Price
FROM Ratings 
LEFT JOIN Prices 
ON Ratings.Name  = Prices.Name;''')

joined_db = cur.fetchall()

for i in joined_db:
    if i[1] not in category_counts:
        category_counts[i[1]] = 1
        rating_totals[i[1]] = i[2]
        try:
            price_totals[i[1]] = len(i[3])
        except:
            None
    else:
        category_counts[i[1]] += 1
        rating_totals[i[1]] += i[2]
        try:
            price_totals[i[1]] += len(i[3])
        except:
            None

average_ratings = {}
average_prices = {}
for i in category_counts:
    average_ratings[i] = (rating_totals[i]/category_counts[i])
for i in category_counts:
    try:
        average_prices[i] = price_totals[i]/category_counts[i]
    except:
        None

# f = open('yelp_ratings_and_prices.txt', 'w')

# for i in average_ratings:
#     f.write(i + " " + str(average_ratings[i]) + '\n')
# for i in average_prices:
#     f.write(i + " " + str(average_prices[i]) + '\n')
# f.close()

#plot 1

categories = []
totals = []
ratings = []

for i in category_counts:
    categories.append(i)
    totals.append(category_counts[i])
    ratings.append(average_ratings[i])
    try:
        tuples.append((i, average_prices[i], average_ratings[i]))
    except:
        None
# plt.bar(range(59), totals)
# plt.xticks(y_pos, categories)
# plt.show()

#PLOT 2

x = []
y = []
for i in tuples:
    x.append(i[2])
    y.append(i[1])
plt.scatter(x,y,c='#8a66d9')
plt.title('Scatterplot of Price vs. Rating in Ann Arbor Restaurants')
plt.xlabel('Average Rating per Category')
plt.ylabel('Average Price ($-\$$$)')
plt.show()