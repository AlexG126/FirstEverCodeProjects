from tkinter import *
from tkinter.ttk import *

from time import strftime

root = tk()
root.title("Clock")

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)

label = label(root, font=("ds_digital",80), background = "black", foreground = "cyan")
label.pack(anchor="center")
time()

mainloop()
