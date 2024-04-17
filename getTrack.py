import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

lz_uri = 'spotify:artist:4AK6F7OLvEQ5QYCBNiQWHq'

track_uris = [
    'spotify:track:6rqhFgbbKwnb9MLmUQDhG6',
    'spotify:track:7xGfFoTpQ2E7fRF5lN10tr',
    'spotify:track:2VxeLyX666F8uXCJ0dZF8B'
]

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='9441ee3eb6ff4e61bb87b5d06f95dcbf',
                                               client_secret='069ebb7a0392401c941564121311f108',
                                               redirect_uri='http://localhost:3000',
                                               scope='playlist-modify-public'))

results = spotify.playlist_add_items('2ceXxZhqbLdfHz1Q07CsmU', track_uris)

i = 1

print(results)

# for track in results['tracks'][:20]:
#     print(i)
#     # print(json.dumps(track, indent=4))
#     # print("\n\n")
#     # print(track['album'])
#     print('track    : ' + track['name'])
#     print('audio    : ' + track['preview_url'])
#     print('cover art: ' + track['album']['images'][0]['url'])
#     print()
#     i = i + 1