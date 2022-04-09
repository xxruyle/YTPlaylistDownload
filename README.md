# YTPlaylistDownload
Download multiple songs from a youtube playlist as well as the playlist thumbnail image

---

# Requirements 
- Must have proper chrome version and <a href="https://chromedriver.chromium.org/downloads">chromedriver</a> installed 
- Python 3.8.8  </br>

## Python Libraries
- Selenium 
- Requests module 
- <a href="https://pypi.org/project/pytube/">Pytube</a> </br>

 ```pip install selenium```  </br>

 ```pip install requests```

```pip install pytube```



# Setup
1) Make sure all libraries are installed
2) Add the installed chromedriver directory in  geturls.py

`PATH = 'C:\yourdirectorypath\chromedriver.exe'`

3) Find the Youtube playlist you would like to use

- Playlist must be public
- Must be on the main playlist viewer page (EXAMPLE:)

![alt text](images\playlist_page_example.png)

4) With the project directory open, in the command line run:  `python main.py`

5) Enter the playlist link

6) Type in the directory you would like to install the playlist into


# Tips
- Sort by date and ascending in the directory you install your music into to get the playlist in order