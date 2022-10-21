import requests
from bs4 import BeautifulSoup
import datetime
import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth

#portion of getting date from user input
SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
OAUTH_AUTHORIZE_URL= 'https://accounts.spotify.com/authorize'
OAUTH_TOKEN_URL= 'https://accounts.spotify.com/api/token'

print(os.environ.get('SPOTIPY_CLIENT_ID'))

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

#playlists = sp.user_playlists("n1gg5vew4t68cmrlfjh6frt9q")

# for playlist in playlists['items']:
#     print(playlist['name'])

user_id = sp.current_user()["id"]
month = str(input("Please enter the month you would like to search for: "))
date = str(input("Please enter the date you would like to search for: "))
year = str(input("Please enter the year you would like to search for: "))

unformatted_date = year + "-" + month + "-" + date

datetime_object = datetime.datetime.strptime(unformatted_date, "%Y-%m-%d")

URL = "https://www.billboard.com/charts/hot-100/" + datetime_object.strftime("%Y-%m-%d")

request = requests.get(URL)
billboard_site = request.text

soup = BeautifulSoup(billboard_site, "html.parser")

song_titles = soup.find_all(name="h3", class_="a-no-trucate")
artist_names = soup.find_all(name="span", class_="a-no-trucate")

song_list = [title.getText().strip() for title in song_titles]
artist_list = [artist.getText().strip() for artist in artist_names]


artist_song_list = dict(zip(song_list, artist_list))
print(artist_song_list)

song_ids = []

for song in artist_song_list:
    print("This is the song:", song)
    track_id = sp.search(q='artist:' + artist_song_list[song] + ' track:' + song, type='track')
    #print("This is the artist:", artist_song_list[song])
    #print("This is the track_id:", track_id)
    #print(artist_song_list[song])
    try:   
        trackId = track_id['tracks']['items'][0]['id']
    except IndexError:
        print("The song", song, "by artist(s)", artist_song_list[song], "could not be added to the playlist.")
        continue
    song_ids.append(trackId)

#print(song_ids)

playlist = sp.user_playlist_create(user_id, "Top 100 Billboard Songs of " + datetime_object.strftime("%Y-%m-%d"), public=False, collaborative=False, description="Created by you!")
playlist_id = playlist["id"]

sp.playlist_add_items(playlist_id, song_ids, position=None)

print("All tracks have been added.")

#user_playlist_create(user, name, public=True, collaborative=False, description='')



