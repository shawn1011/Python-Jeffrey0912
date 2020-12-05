# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:55:26 2020

@author: user
"""

import tkinter as tk


window = tk.Tk()
label=tk.Label(window,text="請輸入網址")
label.pack()

var=tk.StringVar()


entry=tk.Entry(window,width=50)
entry.pack()

def onClick():
    
    yt=YouTube(var.get(),on_progress_callback=showProgress)
    stream=yt.streams.first()
    stream.download()

  

button=tk.Button(window,text="下載")
button.pack()
window.title("Scale尺度")


scale = tk.Scale(window,label="進度條",
                 orient=tk.HORIZONTAL,
                 length=200)
scale.pack()

window.mainloop()
    






















