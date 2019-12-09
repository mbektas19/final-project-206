import spotipy as sp
from spotipy.oauth2 import SpotifyClientCredentials
import sqlite3
import os

db_name = 'playlist_data.db'
path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path+'/'+db_name)
cur = conn.cursor()

client_id='435610e6bc6741e8b60f11f6425b8397'
client_secret='3884178bbf7d4004badd984c561543f2'

client_credentials_managera = SpotifyClientCredentials(client_id,client_secret)
spot = sp.Spotify(client_credentials_manager=client_credentials_managera)

current_playlist = spot.user_playlist('bradgurdlinger', '6wyXbq1Zf8iF3OQWUAE0rS')

songs = []
dates = []

for i in current_playlist['tracks']['items']:
    songs.append((i['track']['name'], i['track']['duration_ms']/60000))
    dates.append((i['track']['name'], i['track']['album']['release_date'][:4]))

cur.execute('CREATE TABLE IF NOT EXISTS Lengths (name TEXT PRIMARY KEY, length REAL)')
for x in songs[:80]:   
    cur.execute('INSERT INTO Lengths (name, length) VALUES (?, ?)', (x[0], x[1]))

cur.execute('CREATE TABLE IF NOT EXISTS Years (name TEXT PRIMARY KEY, year INTEGER)')
for q in dates[:80]
    cur.execute('INSERT INTO Years (name, year) VALUES (?,?)', (q[0],q[1]))


conn.commit()
cur.close()
