from tkinter import *

def display_input():
    user_input = entry.get()
    label_result.config(text=f"You entered: {user_input}")

# Create the main window
root = Tk()
root.title("Label and Textbox Demo")
root.geometry("200x200")

# Create a label
label = Label(root, text="Enter Something:")
label.pack(pady=10)

# Create a text box
entry = Entry(root)
entry.pack(pady=10)

# Create a button to display input
button_display = Button(root, text="Display Input", command=display_input)
button_display.pack(pady=10)

# Create a label to display the result
label_result = Label(root, text="")
label_result.pack(pady=10)

# Run the main loop
root.mainloop()
