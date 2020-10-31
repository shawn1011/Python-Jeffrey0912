# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:24:39 2020

@author: user
"""

import threading
import tkinter as tk
from pytube import YouTube
window =tk.Tk()

window.title("Youtube下載器")
window.geometry("500x150")
window.resizable(False,False)

window = tk.Tk()
window.title("youtube下載器")
window.geometry("500x150")
window.resizable(False,False)
entry=tk.Entry(window,width=21)
entry.pack()
onlyMusic = tk.BooleanVar()
check = tk.Checkbutton(window, text ="只有音樂",variable = onlyMusic,onvalue = True, offvalue = False)
button = tk.Button(window,text="按我")
button.pack()
check.pack()
window.mainloop()

check.pack()

window.mainloop()


def thread():
    threading.Thread(targat=onClick).start()
    
    
progress=0        
def showProgress(stream,chunk,bytes_remaining):
    size=stream.filesize
    global progress
    preProgress = progress
    
    currentProgress=int((size-bytes_remaining)*100/size)
    progress=currentProgress
    
    if progress == 100:
        print("下載完成")
        return
    
    if preProgress != progress:
        scale.set(progress)
        window.update()
        print("目前進度"+ str(currentProgress)+"%")

def onClick():
    global var
    var.set(entry.get())
    
    button.config(state=tk.DISABLED)
    
    try:
        yt=YouTube(var.get(),on_progress_callback=showProgress)
        if onlyMusic.get():
            stream=yt.streams.filter(only_audio=True).first()
            stream.download()
        else:
            stream=yt.steams.first()
            stream.download()
    except:
            print("下載失敗")
    button.config(state=tk.NORMAL)
            
entry=tk.Entry(window,width=21)
entry.pack()
onlyMusic = tk.BooleanVar()
check = tk.Checkbutton(window, text ="只有音樂",variable = onlyMusic,onvalue = True, offvalue = False)
button = tk.Button(window,text="按我",command = thread)
button.pack()
check.pack()
scale=tk.Scale(window,label="進度條",from_=0,to=100,orient=tk.HORIZONTAL,length=200,showvalue=False,tickinterval=0)
scale.pack()
window.mainloop()
            
        
    

























































































































































































































































































































































































