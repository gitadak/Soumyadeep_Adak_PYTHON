from tkinter import *

window = Tk()
window.title("Data Entry")
window.geometry("374x369")

root=Frame(window,bg="PowderBlue")
root.pack()
dept=StringVar()

head = Label(root,text="Student's Details",font=("Algerian",20),fg="Red",bg="PowderBlue").grid(row=0,column=0,columnspan=2,pady=5)

Label1 = Label(root,text="Student's name:",bg="PowderBlue").grid(row=1,column=0,padx=5,pady=5,sticky=W)
Entry1 = Entry(root,width=40).grid(row=1,column=1,padx=5,pady=5)

Label1 = Label(root,text="Student's address:",bg="PowderBlue").grid(row=2,column=0,padx=5,pady=5,sticky=W)
Entry1 = Entry(root,width=40).grid(row=2,column=1,padx=5,pady=5)

Label1 = Label(root,text="Guardian's name:",bg="PowderBlue").grid(row=3,column=0,padx=5,pady=5,sticky=W)
Entry1 = Entry(root,width=40).grid(row=3,column=1,padx=5,pady=5)

Label1 = Label(root,text="Department:",bg="PowderBlue").grid(row=4,column=0,padx=5,pady=5,sticky=W)
Entry1 = Entry(root,width=40).grid(row=4,column=1,padx=5,pady=5)

Label1 = Label(root,text="DOB:",bg="PowderBlue").grid(row=5,column=0,padx=5,pady=5,sticky=W)
Entry1 = Entry(root,width=40).grid(row=5,column=1,padx=5,pady=5)

Label1 = Label(root,text="Email ID:",bg="PowderBlue").grid(row=6,column=0,padx=5,pady=5,sticky=W)
Entry1 = Entry(root,width=40).grid(row=6,column=1,padx=5,pady=5)

Label1 = Label(root,text="Phone number:",bg="PowderBlue").grid(row=7,column=0,padx=5,pady=5,sticky=W)
Entry1 = Entry(root,width=40).grid(row=7,column=1,padx=5,pady=5)

Label1 = Label(root,text="Class 10 marks(%):",bg="PowderBlue").grid(row=8,column=0,padx=5,pady=5,sticky=W)
Entry1 = Entry(root,width=40).grid(row=8,column=1,padx=5,pady=5)

Label1 = Label(root,text="Class 12 marks(%):",bg="PowderBlue").grid(row=9,column=0,padx=5,pady=5,sticky=W)
Entry1 = Entry(root,width=40).grid(row=9,column=1,padx=5,pady=5)

Button_submit = Button(root,text="SUBMIT",width=7,bg="LightGreen")
Button_submit.grid(row=10,column=0,pady=15,sticky=W)

Button_back = Button(root,text="BACK",width=7,fg="Red",bg="Yellow")
Button_back.grid(row=10,column=1,pady=15,sticky=E)

window.mainloop()