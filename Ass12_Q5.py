import tkinter as tk

def on_click(event):
    if event.num == 1:
        print("Left Click")
    elif event.num == 2:
        print("Middle Click")
    elif event.num == 3:
        print("Right Click")

# Create the main window
root = tk.Tk()
root.title("Click Detection")

# Bind the click event to the on_click function
root.bind("<Button-1>", on_click)  # Left Click
root.bind("<Button-2>", on_click)  # Middle Click
root.bind("<Button-3>", on_click)  # Right Click

# Run the main loop
root.mainloop()
