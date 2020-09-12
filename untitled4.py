# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 14:08:21 2020

@author: user
"""

import tkinter as tk
import tkinter.messagebox
window = tk.Tk()
window.title("我的tk888")
window.geometry('300x300')

def clickMe():
    tkinter.messagebox.showinfo(title='哥哥的遺言',message='母湯喔')
    

label = tk.Label(window,text="我的tk888",bg="#0FF",fg="#909")
label.pack()

entry=tk.Entry(window,width=20)
entry.pack()

button=tk.Button(window,text="按了就會超爽",command = clickMe)
button.pack()












window.mainloop()