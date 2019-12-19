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

page = 1
for i in range(15):
    url = 'http://www.recipepuppy.com/api/'
    params = {'q':'chicken', 'p':page}

    try:
        req = requests.get(url, params = params)
        data = json.loads(req.text)['results']

        for i in data:
            name = i['title']
            try:
                ingredients1 = i['ingredients'].split(', ')[:5]
            except:
                ingredients1 = i['ingredients'].split(', ')
            #make sure that the recipe isn't a repeat
            # print(name)
            # print(ingredients1)
            try:
                cur.execute('''INSERT INTO Chicken (Recipe, Ingredient1, Ingredient2, Ingredient3, Ingredient4, Ingredient5) 
                VALUES (?,?,?,?,?,?)''', (name, ingredients1[0], ingredients1[1], ingredients1[2], ingredients1[3], ingredients1[4]))
            except:
                print('Recipe already exists')
            
            #second table
            
            try:
                ingredients2 = i['ingredients'].split(', ')[5]
            except:
                print('No more ingredients')
            #make sure that the recipe isn't a repeat
            try:
                cur.execute('''INSERT INTO Chicken2 (Recipe, Ingredient6) 
                VALUES (?,?)''', (name, ingredients2))
            except:
                print('Recipe already exists')
    except:
        print('No more recipes in search query')
    page += 1


conn.commit()
cur.close()
    