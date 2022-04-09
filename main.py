from pytube import YouTube  # Allows us to download videos and their mp3s
from geturls import song_list  # The urls of each song 
from geturls import album_name # the playlist name 
from geturls import img_data # the album cover's byte info
from inputvars import namedir  # the directory the user would wish to install the playlist songs into
import os 

# Downlods the files and stores them in a new folder 
def download_playlist(): 
    music_directory = f"{namedir()}\{album_name}"  # the directory the playlist will be installed in
    if not os.path.exists(music_directory):
        os.makedirs(music_directory)
    else:
        print('A folder with that playlist name already exists')

    # Downloading multiple songs from the playlist   
    try:
        print(f"There are {len(song_list)} videos in the playlist")
        for video in song_list: 
            # Getting the links
            title = video.find_element_by_id('video-title')
            link = title.get_attribute('href')

            print(f'Downloading... {title.text}')
            #Downloading...    
            yt = YouTube(link)
            stream = yt.streams.filter(only_audio=True).first()
            out_file = stream.download(music_directory)
            base, ext = os.path.splitext(out_file)
            new_file = base + ".mp3"
            os.rename(out_file, new_file)

        print("Downloading playlist image...")
        with open(f"{music_directory}\cover.png", 'wb') as f:
            f.write(img_data)

        print("Success!")

    except:
        print("Oops! Something went wrong")

if __name__ == "__main__":
    download_playlist()