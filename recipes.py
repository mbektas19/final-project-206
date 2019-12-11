import requests
import json
import sqlite3
import os

db_name = 'final.db'
path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path+'/'+db_name)
cur = conn.cursor()


cur.execute('''CREATE TABLE IF NOT EXISTS Chicken (Recipe TEXT PRIMARY KEY UNIQUE, Ingredient1 TEXT, Ingredient2 TEXT, 
Ingredient3 TEXT, Ingredient4 TEXT, Ingredient5 TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Chicken2 (Recipe TEXT PRIMARY KEY UNIQUE, Ingredient6 TEXT)''')

url = 'http://www.recipepuppy.com/api/'
params = {'q':'chicken', 'p':14}

try:
    req = requests.get(url, params = params)
    data = json.loads(req.text)['results']

    for i in data:
        name = i['title']
        #make sure ingredients have a next 1 to take
        try:
            ingredients = i['ingredients'].split(', ')[5]
        except:
            print('No more ingredients')
        #make sure that the recipe isn't a repeat
        try:
            cur.execute('''INSERT INTO Chicken2 (Recipe, Ingredient6) 
            VALUES (?,?)''', (name, ingredients))
        except:
            print('Recipe already exists')
except:
    print('No more recipes in search query')


conn.commit()
cur.close()
    