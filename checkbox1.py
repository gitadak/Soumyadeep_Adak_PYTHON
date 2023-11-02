# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:39:44 2019

@author: STUDENT
"""

from tkinter import *
master = Tk()
m1 =0
v1 = IntVar()
v2 = IntVar()
def select_choice(): 
    global m1 
    m1 = v1.get()
    m2 = v2.get()
    if m1 == 1 and m2 == 1 :
        print(" Male Female")
    elif m1 == 1:
        print("male")
    elif m2 == 1:
        print ("female")
    else :
        print( "Selected None")
master.geometry('200x300')
arr=["male","female"]
Checkbutton(master, text= arr[0], variable=v1,onvalue=1,offvalue=0,
            command = select_choice).grid(row=0, sticky=W)
Checkbutton(master, text = arr[1], variable=v2, onvalue=1,offvalue = 0,
            command = select_choice).grid(row=1, sticky=W)

mainloop()