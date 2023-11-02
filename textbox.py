# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:06:46 2019

@author: STUDENT
"""

import tkinter as tk

root = tk.Tk()
T = tk.Text(root, height=2, width=30)
T.pack()
T.insert(tk.END, "Just a text Widget\nin two lines\n")
tk.mainloop()