import sqlite3
import os
import matplotlib.pyplot as plt
import numpy as np

db_name = 'final.db'
path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path+'/'+db_name)
cur = conn.cursor()

#Calculating counts of each different restaurant category as well as price and rating totals

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

# Calculating the average price and rating for each category

average_ratings = {}
average_prices = {}
for i in category_counts:
    average_ratings[i] = (rating_totals[i]/category_counts[i])
for i in category_counts:
    try:
        average_prices[i] = price_totals[i]/category_counts[i]
    except:
        None

# Finding the top 8 categories by count of restaurants

top_eight = {}
top_eight_keys = sorted(category_counts, key=lambda x:category_counts[x], reverse = True)[:8]
for i in top_eight_keys:
    top_eight[i] = category_counts[i]

# Writing calculations to file

filename = 'restaurants.txt'
source_dir = os.path.dirname(__file__) #<-- directory name
full_path = os.path.join(source_dir, filename)
f = open(full_path, 'w')

f.write('Average Ratings for AA Restaurants' + '\n' + '\n')
for i in average_ratings:
    f.write(i + " " + str(average_ratings[i]) + '\n')
f.write("\n" + 'Average Prices for AA Restaurants ($-$$$)' + '\n' + '\n')
for i in average_prices:
    f.write(i + " " + str(average_prices[i]) + '\n')
f.write('\n' + "Top Eight Restaurant Categories in AA" + '\n' + '\n')
for i in top_eight:
    f.write(i + ': ' + str(top_eight[i]) + '\n' + '\n')
f.close()

#plot 1: bar chart of top 8 categories

heights = np.array(list(top_eight.values()))
ticks = np.arange(len(top_eight))
labels = np.array(list(top_eight.keys()))

plt.bar(ticks, heights)
plt.xticks(ticks, labels)
plt.title('Bar Graph of Most Common Cusines in Ann Arbor')
plt.show()

# Getting average prices and ratings into lists for the scatterplot

categories = []
totals = []
ratings = []
graph_category_count = []

for i in category_counts:
    categories.append(i)
    totals.append(category_counts[i])
    ratings.append(average_ratings[i])
    try:
        tuples.append((i, average_prices[i], average_ratings[i]))
    except:
        None


#PLOT 2: Scatterplot of Average Price vs Average Rating

x = []
y = []
for i in tuples:
    x.append(i[2])
    y.append(i[1])

plt.scatter(x,y,c='#8a66d9')
plt.title('Scatterplot of Average Price vs. Average Rating in Ann Arbor Restaurants')
plt.xlabel('Average Rating per Category')
plt.ylabel('Average Price ($-\$$$)')
plt.annotate('Local Flavor', (5, 3))
plt.annotate('Wine Bars', (3.5, 3))
plt.annotate('Salad', (4.5, 1))
plt.annotate('Burgers', (3.5, 1))
plt.show()