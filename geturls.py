from matplotlib.image import thumbnail
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getlink import getlink
import requests 

# Makes it so the browser runs in the background
options = Options()
options.add_argument("--headless")

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH, options=options)


driver.get(getlink())

content = driver.find_element_by_xpath('//div[@id="contents"]')

container = content.find_element_by_id('contents')

song_list = container.find_elements_by_xpath('//ytd-playlist-video-renderer[@class="style-scope ytd-playlist-video-list-renderer"]')

# Getting the name of the youtube playlist
playlist_name = driver.find_element_by_xpath('//a[@class="yt-simple-endpoint style-scope yt-formatted-string"]')

album_name = playlist_name.text  # The name of the youtube playlist 

# Getting the album/playlist cover 
thumbnails = driver.find_element_by_xpath('//ytd-playlist-sidebar-primary-info-renderer[@class="style-scope ytd-playlist-sidebar-renderer"]')

# img_container = thumbnails.find_element_by_xpath('//ytd-playlist-video-thumbnail-renderer[@class="style-scope ytd-playlist-thumbnail"]')
img = thumbnails.find_element_by_id('img')

img_src = img.get_attribute('src')


img_data = requests.get(img_src).content # the image data in bytes 


