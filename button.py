from tkinter import *

root = Tk()

def theClick():
    label1 = Label(root, text = "Button Clicked")
    label1.pack()

# Creating a button
button1 = Button(root, text="Click Me", padx=30, command=theClick)
button1.pack()

# Execution
root.mainloop()