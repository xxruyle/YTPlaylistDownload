from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from inputvars import getlink
import requests 

# Finds the URLS of the playlist, the playlist name, and the playlist cover image 

# Makes it so the browser runs in the background
options = Options()
options.add_argument("--headless")

PATH = 'C:\Program Files (x86)\chromedriver.exe'  # Place a path to your chromedriver !!!! 
driver = webdriver.Chrome(PATH, options=options)
driver.get(getlink())

# Getting each url href from the playlist
print("Getting urls...")
content = driver.find_element_by_xpath('//div[@id="contents"]')
container = content.find_element_by_id('contents')
song_list = container.find_elements_by_xpath('//ytd-playlist-video-renderer[@class="style-scope ytd-playlist-video-list-renderer"]')
print("URLs obtained!")

# Getting the name of the youtube playlist
playlist_name = driver.find_element_by_xpath('//a[@class="yt-simple-endpoint style-scope yt-formatted-string"]')
album_name = playlist_name.text  # The name of the youtube playlist 
print(f"Playlist name: {album_name}")

# Getting the album/playlist cover 
thumbnails = driver.find_element_by_xpath('//ytd-playlist-sidebar-primary-info-renderer[@class="style-scope ytd-playlist-sidebar-renderer"]')
img = thumbnails.find_element_by_id('img')
img_src = img.get_attribute('src')
img_data = requests.get(img_src).content # the image data in bytes 
print("Playlist cover obtained!")

