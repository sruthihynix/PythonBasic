from tkinter import *
import mysql.connector
import tkinter.messagebox as tkMessageBox



root = Tk()
image = PhotoImage(file="Canara_Bank_Logo.svg")
label = Label(image=image)
label.pack()
root.mainloop()