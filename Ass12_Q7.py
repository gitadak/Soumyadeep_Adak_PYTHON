from tkinter import *

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        sum_result = num1 + num2
        diff_result = num1 - num2
        sum_label.config(text=f"Sum: {sum_result}")
        diff_label.config(text=f"Difference: {diff_result}")
    except ValueError:
        sum_label.config(text="Please enter valid numbers")
        diff_label.config(text="Please enter valid numbers")

root = Tk()
root.title("Simple Calculator")

frame = Frame(root)
frame.pack(padx=20, pady=20)

label1 = Label(frame, text="Enter number 1:")
label1.grid(row=0, column=0, padx=5, pady=5)

entry1 = Entry(frame)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2 = Label(frame, text="Enter number 2:")
label2.grid(row=1, column=0, padx=5, pady=5)

entry2 = Entry(frame)
entry2.grid(row=1, column=1, padx=5, pady=5)

calculate_button = Button(frame, text="Calculate", command=calculate)
calculate_button.grid(row=2, columnspan=2, padx=5, pady=10)

sum_label = Label(frame, text="Sum: ")
sum_label.grid(row=3, columnspan=2, padx=5, pady=5)

diff_label = Label(frame, text="Difference: ")
diff_label.grid(row=4, columnspan=2, padx=5, pady=5)

root.mainloop()
