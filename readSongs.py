import os
import time
#
# directory/folder path
start = time.time()
dir_path = r'/home/maazhamed/Music'

# list to store files
res = []

# remove= ['.mp3', '.ogg', '.wav', '.m4a', '.lrc', '(Official Video)', '(official video)', '(Official Lyric Video)', '(MP3_160K)', '(MP3_)']

# Iterate directory
for file_path in os.listdir(dir_path):
    # check if current file_path is a file
    if os.path.isfile(os.path.join(dir_path, file_path)):
        # add filename to list
        print(file_path.replace('_1', '').replace('(MP360K)', '').replace('[Official Music Video]','').replace('(M4A28K)','').replace('(Official Audio)', '').replace('(M4A_128K)', '').replace('(M4A_128K)_1', '').replace(".mp3",'').replace(".ogg",'').replace(".wav",'').replace(".m4a",'').replace(".lrc",'').replace("(Official Video)", '').replace("(official video)",'').replace("(Official Lyric Video)",'').replace('(MP3_160K)',"").replace('(Official Music Video)','').replace('[Official Video]', '').replace('(MP3_320K)',''))
        res.append(file_path)
print(len(res))
print(time.time() - start)

# current_directory = os.getcwd()
# print(current_directory)