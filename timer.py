from time import sleep
import tkinter as tk
from tkinter import *
import subprocess
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
        time_sec = time_sec - 1
        seconds = (time_sec // 60) % 60
        minutes = (time_sec // 3600)
        hours = (time_sec // 10800)
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(minutes))
        second.set("{0:2d}".format(seconds))
        hrwindo= Entry(root, width=3, font=('calibre',10, 'bold'),textvariable=hour)
        minwindo= Entry(root, width=3, font=('calibre',10, 'bold'),textvariable=minute)
        secondswino= Entry(root, width=3, font=('calibre',10, 'bold'),textvariable=second)
        hrwindo.grid(row=7,column=0)
        minwindo.grid(row=7,column=1)
        secondswino.grid(row=7,column=2)
        root.update()

        
def screentimer():
     subprocess.run(["powercfg", "-change", "-monitor-timeout-ac" ,"1"],  shell=True, stdout=subprocess.PIPE, stdin=subprocess.DEVNULL, stderr=subprocess.DEVNULL)