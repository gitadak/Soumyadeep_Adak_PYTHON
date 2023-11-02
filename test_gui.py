import tkinter as tk
from tkinter import *
    
#############
def write_slogan():
    print("Tkinter is easy to use!")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Hello",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

###########
var1 = IntVar()
Checkbutton(root, text="male", variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(root, text="female", variable=var2).grid(row=1, sticky=W)
root.mainloop()
##########