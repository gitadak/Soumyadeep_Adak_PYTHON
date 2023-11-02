import tkinter
from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("350x200")

t1=StringVar()
t2=StringVar()
t3=StringVar()
s1=Label(root,width=20,text="Enter the 1st no.: ")
s1.grid(row=0,column=0)
s2=Entry(root,width=20,textvariable=t1)
s2.grid(row=0,column=1)
s3=Label(root,width=20,text="Enter the 2nd no.: ")
s3.grid(row=1,column=0)
s4=Entry(root,width=20,textvariable=t2)
s4.grid(row=1,column=1)
s5=Label(root,width=20,text="Result: ")
s5.grid(row=2,column=0)
s6=Entry(root,width=20,state='readonly',textvariable=t3)
s6.grid(row=2,column=1)

def add():
    try:
        a=int(t1.get())
        b=int(t2.get())
        c=a+b
        t3.set(c)
    except ValueError:
        messagebox.showerror("!!!ERROR!!!","Input must be an integer")
        t3.set("")

def reset():
    t1.set('')
    t2.set('')
    t3.set('')

s7=Button(root,command=add,text="ADD",padx=20)
s7.grid(row=3,column=0)
s8=Button(root,command=reset,text="RESET",padx=20)
s8.grid(row=3,column=1)
root.mainloop()