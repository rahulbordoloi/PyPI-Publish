# Libraries

import os
import time
from pytube import YouTube

# Processing

def yt_down(url):
    
    youtube = YouTube(url)

    print('-----------------------------------')

    # Information of the Video of the Given URL
    print('Title : ', youtube.title)
    print('Views : ', youtube.views)
    print('Length : ' , youtube.length, 'seconds')
    print('Description : ', youtube.description)
    print('Rating : ', youtube.rating) 

    print('-----------------------------------')

    # Get the Highest Quality Progressive Stream
    ystream = youtube.streams.get_highest_resolution()

    # Downloading the File
    print('Starting Download ...')
    start = time.time()
    ystream.download()  # download()
    end = time.time()
    print('Download Successful, You can find your File at :', os.getcwd())
    print('Time Elapsed : ', round(end - start , 2), 'seconds')

# Input

def YTDown(url = None):
    if url is None:
        print("Enter the Youtube URL of the Video you want to Download : ")
        url = input()
        yt_down(url)
    else:
        yt_down(url) 
    
    
