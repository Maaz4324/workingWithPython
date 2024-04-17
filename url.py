import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import json

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials("9441ee3eb6ff4e61bb87b5d06f95dcbf", "069ebb7a0392401c941564121311f108"))

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'One Direction'

results = spotify.search(q='artist:' + name, type='artist')
print(json.dumps(results, indent=4))
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    print(artist['name'], artist['images'][0]['url'])