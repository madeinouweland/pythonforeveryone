from tkinter import *

def show_time():
    print("Hello world")

root = Tk()

frame = Frame(root)
frame.pack()

label = Label(frame, text = "Click the button")
label.pack()

button = Button(frame, text = "Click me!")
button.pack()

button.config(command = show_time)

root.mainloop()
