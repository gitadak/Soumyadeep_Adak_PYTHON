# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:41:14 2019

@author: STUDENT
"""

import tkinter
from tkinter import messagebox

# hide main window
root = tkinter.Tk()
root.withdraw()

# message box display
messagebox.showerror("Error", "Error message")
messagebox.showwarning("Warning","Warning message")
messagebox.showinfo("Information","Informative message")
