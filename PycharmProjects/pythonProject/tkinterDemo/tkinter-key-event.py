
from tkinter import *
from tkinter.ttk import *

# function to be called when
# keyboard buttons are pressed
def key_press(event):
	key = event.char # char is a keyword
	print(key, 'is pressed')


# creates tkinter window or root window
root = Tk()
root.geometry('200x100')

# lbl1.Label(root,text="key")
# lbl1.pack()

# here we are binding keyboard
# with the main window
root.bind('<Key>', lambda a : key_press(a))

mainloop()

# An Event Handler is a class, part of events,
# which simply is responsible for managing all callbacks which are to be executed when invoked.
# An Event is simply an action, like clicking a button,
# which then leads to another event, which the developer already assigns.