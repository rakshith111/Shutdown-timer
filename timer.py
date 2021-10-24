import time
import tkinter as tk
from tkinter import *
def countdown(root,time_sec):
    hour=StringVar()
    minute=StringVar()
    second=StringVar()
    root.minsize(300, 160)
    root.maxsize(300, 160)
    Hrt_label = tk.Label(root, text = 'Hrs', font=('calibre',10, 'bold'))
    Mint_label = tk.Label(root, text = 'Min', font=('calibre',10, 'bold'))
    Sect_label = tk.Label(root, text = 'Sec', font=('calibre',10, 'bold'))
    Time_rem_label=tk.Label(root, text = 'Time \nremaining', font=('calibre',10, 'bold'))
    Time_rem_label.grid(row=5,column=0)
    Hrt_label.grid(row=6,column=0)
    Mint_label.grid(row=6,column=1)
    Sect_label.grid(row=6,column=2)
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        hours=0
        if(mins>60):
            hours,mins=divmod(mins, 60)
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        hrwindo= Entry(root, width=3, font=('calibre',10, 'bold'),textvariable=hour)
        minwindo= Entry(root, width=3, font=('calibre',10, 'bold'),textvariable=minute)
        secondswino= Entry(root, width=3, font=('calibre',10, 'bold'),textvariable=second)
        hrwindo.grid(row=7,column=0)
        minwindo.grid(row=7,column=1)
        secondswino.grid(row=7,column=2)
 
        root.after(1000)
        root.update()
        time_sec-=1