import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time 
import os
#
# directory/folder path
dir_path = r'/home/maazhamed/Music'

# list to store files
res = []
count = 0

start = time.time()
# Initialize Spotipy with necessary credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='9441ee3eb6ff4e61bb87b5d06f95dcbf',
                                               client_secret='069ebb7a0392401c941564121311f108',
                                               redirect_uri='http://localhost:3000',
                                               scope='playlist-modify-public'))

# Search for tracks with a specific query


# Iterate directory
for file_path in os.listdir(dir_path):
    
    # check if current file_path is a file
    if os.path.isfile(os.path.join(dir_path, file_path)):

        # add filename to list
        filtered_files = file_path.replace('_1', '').replace('(MP360K)', '').replace('[Official Music Video]','').replace('(M4A28K)','').replace('(Official Audio)', '').replace('(M4A_128K)', '').replace('(M4A_128K)_1', '').replace(".mp3",'').replace(".ogg",'').replace(".wav",'').replace(".m4a",'').replace(".lrc",'').replace("(Official Video)", '').replace("(official video)",'').replace("(Official Lyric Video)",'').replace('(MP3_160K)',"").replace('(Official Music Video)','').replace('[Official Video]', '').replace('(MP3_320K)','')
        search_results = sp.search(filtered_files, limit=1, type='track')

        # Print out the search results
        for track in search_results['tracks']['items']:
            res.append(track['uri'])
            count = count + 1
            print(res)
            if(count == 100):
                count = 0
                result = sp.playlist_add_items('2ceXxZhqbLdfHz1Q07CsmU', res)
                print(result)
                res = []

        

            
print(res)

result = sp.playlist_add_items('2ceXxZhqbLdfHz1Q07CsmU', res)
print(result)

print(time.time() - start)

