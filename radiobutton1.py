# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:26:36 2019

@author: STUDENT
"""

import tkinter as tk

root = tk.Tk()
root.geometry('200x300')

v = tk.IntVar()
arr = ["Python", "Perl"]
tk.Label(root, 
        text="""Choose a 
programming language:""",
        justify = tk.LEFT,
        padx = 20).pack()
m1="hello"
def select_choice(): 
    global m1 
    m1 = v.get()
    print(arr[m1])
x1=tk.Radiobutton(root, 
              text=arr[0],
              padx = 20, 
              variable=v, 
              value=0, command = select_choice)
x1.pack(anchor =tk.W)

x2 = tk.Radiobutton(root, 
              text=arr[1],
              padx = 20, 
              variable=v, 
              value=1, command = select_choice)
x2.pack(anchor=tk.W)


root.mainloop()