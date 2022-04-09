from pytube import YouTube
from geturls import song_list
from geturls import album_name
from geturls import img_data 
import os 

# Downlods the files and stores them in a new folder 
def download_playlist(): 
    music_directory = f"C:\Music\{album_name}"
    if not os.path.exists(music_directory):
        os.makedirs(music_directory)
    else:
        print('That file already exists')

    # Downloading multiple songs from the playlist   
    try:
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

download_playlist()