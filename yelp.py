import requests
import json
import sqlite3
import os

db_name = 'yelp.db'
path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path+'/'+db_name)
cur = conn.cursor()

# change param 'offset' in order to get next results
# api returns 20 results
api_key = 'OPUebJ4zTSF3JNrO0QGxfpOZve7u5LvWpOe5hDCEwfW3q-PwTHGAWD-ad6ySoyIjmwFh7vAINGu475mwGkQeXGy1oY-Ev0IIuNhZRMfeI_7-gS79xtTMejSiYQfvXXYx'
headers = {'Authorization': 'Bearer %s' % api_key}
params = {'location':'Ann Arbor', 'offset':120, 'limit': 20}
url='https://api.yelp.com/v3/businesses/search'

res = requests.get(url, headers = headers, params = params)
data = json.loads(res.text)

cur.execute('CREATE TABLE IF NOT EXISTS Ratings (Name TEXT PRIMARY KEY UNIQUE, Category TEXT, Rating REAL)')

for i in data['businesses']:
    name = i['name']
    category = i['categories'][0]['title']
    rating = i['rating']
    try:
        cur.execute('INSERT INTO Ratings (Name, Category, Rating) VALUES (?,?,?)', (name, category, rating))
    except:
        print('Restaurant already in database.')

cur.execute('CREATE TABLE IF NOT EXISTS Prices (Name TEXT PRIMARY KEY UNIQUE, Price TEXT)')

for x in data['businesses']:
    name = x['name']
    try:
        price = x['price']
    except:
        print('Price of restaurant not available.')
    try:
        cur.execute('INSERT INTO Prices (Name, Price) VALUES (?,?)', (name, price))
    except:
        print('Restaurant already in database')

conn.commit()
cur.close()
