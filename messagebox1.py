# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:41:14 2019

@author: STUDENT
"""

import tkinter as tk
from tkinter import messagebox

# hide main window
root = tk.Tk()
root.withdraw()

# message box display

messagebox.showinfo("Information","Informative message")
m=tk.messagebox.askquestion("Hello","Are u well?")
if m=='yes':
  print('good')
else :
  print('bad')

m1=tk.messagebox.askyesnocancel("Hello","Are u well?")

if m1=='yes':
  print('good')
elif m1== 'no' :
  print('bad')
else:
    print('hmm')