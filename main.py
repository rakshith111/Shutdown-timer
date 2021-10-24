from tkinter import *
import tkinter as tk
import subprocess
from timer import countdown
def submit():
    try:
        hrsms=int(hrs.get())
        minuitsms=int(minuits.get())
        secondsms=int(minuits.get())
        if((hrsms or minuitsms or secondsms)):
            final=hrsms*3600+minuitsms*60+secondsms
            subprocess.run(["shutdown", "-s", "-t" ,f"{final}"],  shell=True, stdout=subprocess.PIPE, stdin=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            hrs.set(int(0))
            minuits.set(int(0))
            seconds.set(int(0)) 
            cancel_btn.grid(row=2,column=1,sticky='w')
            extend_btn.grid(row=2,column=0,sticky='w')
            countdown(root,final)
        else:
            pass
    except ValueError:
        hrs.set(int(0))
        minuits.set(int(0))
        seconds.set(int(0))
def extend():
    subprocess.run(["shutdown", "-a"],  shell=True, stdout=subprocess.PIPE, stdin=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    submit()

def cancel():
    #if you want to cancel
    subprocess.run(["shutdown", "-a"],  shell=True, stdout=subprocess.PIPE, stdin=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    root.destroy()
root=tk.Tk()
root.title('SHUTDOWN')
root.minsize(225, 70)
root.maxsize(225, 70)
hrs=tk.StringVar()
minuits=tk.StringVar()
seconds=tk.StringVar()
hrs.set(int(0))
minuits.set(int(0))
seconds.set(int(0))
Hrs_label = tk.Label(root, text = 'HRS', font=('calibre',10, 'bold'))
Hrs_entry = tk.Entry(root,textvariable = hrs,width=10, font=('calibre',10,'normal'))
min_label= tk.Label(root, text = 'Min', font=('calibre',10, 'bold'))
min_entry = tk.Entry(root,textvariable = minuits,width=10, font=('calibre',10,'normal'))
sec_label = tk.Label(root, text = 'Sec', font=('calibre',10, 'bold'))
sec_entry = tk.Entry(root,textvariable = seconds,width=10, font=('calibre',10,'normal'))
sub_btn=tk.Button(root,text = 'Submit', command = submit)
cancel_btn=tk.Button(root,text="Cancel",command=cancel)
extend_btn=tk.Button(root,text="EXTEND",command=extend)
Hrs_label.grid(row=0,column=0)
Hrs_entry.grid(row=1,column=0)
min_label.grid(row=0,column=1)
min_entry.grid(row=1,column=1)
sec_label.grid(row=0,column=2)
sec_entry.grid(row=1,column=2)
sub_btn.grid(row=2,column=0,sticky='w')

root.mainloop()