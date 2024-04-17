import os
#
# directory/folder path
dir_path = r'/home/maazhamed/Music'

# list to store files
res = []

remove= ['.mp3', '.ogg', '.wav', '.m4a', '.lrc', '(Official Video)', '(official video)', '(Official Lyric Video)', '(MP3_160K)', '(MP3_320K)', '(Official Music Video)', '[Official Video]']

# Iterate directory
for file_path in os.listdir(dir_path):
    # check if current file_path is a file
    if os.path.isfile(os.path.join(dir_path, file_path)):
        # add filename to list
        for rm in remove:
            if rm in file_path:
                # file_path.replace(rm,'')

                print(file_path.replace(rm,''))
                
print(len(res))

# current_directory = os.getcwd()
# print(current_directory)