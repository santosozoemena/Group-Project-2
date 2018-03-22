import configurate

from configurate import my_client_id
from configurate import my_secret

import spotipy
import json
import csv

playlist_id = '37i9dQZF1DXcF6B6QPhFDv'
user_id = 'Spotify'

sp = spotipy.Spotify()

from spotipy.oauth2 import SpotifyClientCredentials
cid = my_client_id
secret = my_secret
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)     

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False

def music_list():
    playlist = sp.user_playlist(user_id, playlist_id)
    songs = playlist["tracks"]["items"]
    ids = []
    tracks=[]
    for i in range(len(songs)):
        ids.append(songs[i]["track"]["id"])
        features = sp.audio_features(ids)
        tracks.append(sp.audio_features(ids))
        tracks.append("name")
        tracks.append(songs[i]["track"]["name"])
    #output JSON
    with open('output/music.json', 'w') as outfile:
        json.dump(tracks, outfile)


def conversion():
    
    data_file = 'output/music.json'
    
    with open(data_file, 'r') as file:
        data = json.load(file)
        headers = list(data[0][0].keys())
        headers.append('name')
        print (headers)
        
    with open('output/music.csv', 'w') as file_:
        writer = csv.writer(file_, delimiter = ',')



        writer.writerow(headers)
        to_write = []
        count = 0
        
        for x in data:
            if type(x) is list:
                to_write += list(x[count].values())
                count+=1
                
            if type(x) is str and x != 'name':
                to_write.append(x)
                
                writer.writerow(to_write)
                to_write = []

music_list()
conversion()
