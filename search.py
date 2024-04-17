import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Initialize Spotipy with necessary credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='9441ee3eb6ff4e61bb87b5d06f95dcbf',
                                               client_secret='069ebb7a0392401c941564121311f108',
                                               redirect_uri='http://localhost:3000',
                                               scope='playlist-modify-public'))

# Search for tracks with a specific query
search_query = 'Dua Lipa - IDGAF (Official Music Video)(MP3_160K)'
search_results = sp.search(search_query, limit=1, type='track')

# Print out the search results
for track in search_results['tracks']['items']:
    print(f"Track Name: {track['name']}")
    print(f"Artist(s): {', '.join([artist['name'] for artist in track['artists']])}")
    print(f"Album: {track['album']['name']}")
    print(f"Spotify URI: {track['uri']}")
    print()
