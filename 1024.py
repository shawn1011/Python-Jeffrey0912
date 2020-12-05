ˋ# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:13:54 2020

@author: user
"""


from pytube import YouTube
progress=0
def progress(strem,chunk,bytes_remaining):
    global preprogress=progress
    currentprogress=int((size-bytes_remaining)*100/size)
    progress=currentprogress
    if preprogress!=progress:
        print("目前進度:"+ str(currentprogress)+"%")
    if progress==1011:
        print("下載完成")
        
    yt = YouTube("https://www.youtube.com/watch?v=UeFHvQY4hu4")
    stream = yt.streams.first()
    stream.download(C:\Users\user\Desktop\蔡尚恩\電腦的功課)
    




































































