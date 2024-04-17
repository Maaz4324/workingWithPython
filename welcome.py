import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

uri = 'spotify:artist:4AK6F7OLvEQ5QYCBNiQWHq'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials("9441ee3eb6ff4e61bb87b5d06f95dcbf", "069ebb7a0392401c941564121311f108"))

results = spotify.artist_albums(uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])