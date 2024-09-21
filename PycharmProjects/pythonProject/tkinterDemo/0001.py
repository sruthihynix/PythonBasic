from  tkinter import *

##creating the application main window.
# top=Tk() # create a tkinter object top
# OR
# top=tkinter.Tk()
# entring tht event n main loop
# top.mainloop() #
#
# --------------tkinter label-------------
# hhh=Tk()
# var = StringVar()
# label --widget
# label = Label( hhh, textvariable= var, relief = RAISED )
# var.set("Hey!? How are you doing?")
# label.pack()
# The pack() widget is used to organize widget in the block.
# widget.pack(options)
# hhh.mainloop()

# ------------------------tkinter label-------
# !/usr/bin/python3
# from tkinter import *
# top = Tk()
# top.geometry("500x500")
# name = Label(top, text = "Name").place(x = 30,y = 50)
# email = Label(top, text = "Email").place(x = 30, y = 90)
# password = Label(top, text = "Password").place(x = 30, y = 130)
# e1 = Entry(top).place(x = 80, y = 50)
# e2 = Entry(top).place(x = 80, y = 90)
# e3 = Entry(top).place(x = 95, y = 130)
# top.mainloop()
# --------------------button---------------------------------------------
# parent = Tk()
# redbutton = Button(parent, text = "Red", fg = "red")
# redbutton.pack( side = LEFT)
# greenbutton = Button(parent, text = "Black", fg = "black")
# greenbutton.pack( side = RIGHT )
# bluebutton = Button(parent, text = "pink", fg = "pink")
# bluebutton.pack( side = TOP )
# blackbutton = Button(parent, text = "violet", fg = "violet")
# blackbutton.pack( side = BOTTOM)
# parent.mainloop()
# --------------------------------------------------
# parent = Tk()
# name = Label(parent,text = "Name").grid(row = 0, column = 0)
# e1 = Entry(parent).grid(row = 0, column = 1)
# password = Label(parent,text = "Password").grid(row = 1, column = 0)
# e2 = Entry(parent).grid(row = 1, column = 1)
# submit = Button(parent, text = "Submit").grid(row = 4, column = 0)
# parent.mainloop()
# ----------------
# top = Tk()
# top.geometry("400x250")
# name = Label(top, text = "Name").place(x = 30,y = 50)
# email = Label(top, text = "Email").place(x = 30, y = 90)
# password = Label(top, text = "Password").place(x = 30, y = 130)
# e1 = Entry(top).place(x = 80, y = 50)
# e2 = Entry(top).place(x = 80, y = 90)
# e3 = Entry(top).place(x = 95, y = 130)
# top.mainloop()
# ------------------------------------
import tkinter.messagebox
top = Tk()

top.geometry("200x100")

def fun():
    
    messagebox.showinfo("Hello", "Red Button clicked")
    # Message.showinfo("Hello", "Red Button clicked")

b1 = Button(top, text="Red", command=fun, activeforeground="red", activebackground="pink", pady=10)

b2 = Button(top, text="Blue", activeforeground="blue", activebackground="pink", pady=10)

b3 = Button(top, text="Green", activeforeground="green", activebackground="pink", pady=10)

b4 = Button(top, text="Yellow", activeforeground="yellow", activebackground="pink", pady=10)

b1.pack(side=LEFT)

b2.pack(side=RIGHT)

b3.pack(side=TOP)

b4.pack(side=BOTTOM)

top.mainloop()