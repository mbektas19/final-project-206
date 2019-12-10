import requests
import json
import sqlite3
import os

db_name = 'starwars.db'
path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path+'/'+db_name)
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS Costs (Name TEXT PRIMARY KEY UNIQUE, Cost TEXT, Length TEXT)')
cur.execute('CREATE TABLE IF NOT EXISTS Speeds (Name TEXT PRIMARY KEY UNIQUE, Speed TEXT, Hyperdrive TEXT)')

url = 'https://swapi.co/api/starships/'
params = {'page':4}

data = json.loads(requests.get(url, params = params).text)

for i in data['results']:
    name = i['name']
    cost = i['cost_in_credits']
    length = i['length']
    hyperdrive_rating = i['hyperdrive_rating']
    speed = i['max_atmosphering_speed']
    try:
        cur.execute('INSERT INTO Costs (Name, Cost, Length) VALUES (?,?,?)', (name, cost, length))
    except:
        None
    try:
        cur.execute('INSERT INTO Speeds (Name, Speed, Hyperdrive) VALUES (?,?,?)', (name, speed, hyperdrive_rating))
    except:
        None


conn.commit()
cur.close()
    