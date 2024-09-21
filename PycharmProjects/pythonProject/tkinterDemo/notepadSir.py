
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

master = Tk(className=" Text Editor")

# To add a text box
text = Text(master)
text.pack()


# Functions
def dummy():
    print("rr")

def open_command():
    file = filedialog.askopenfile(parent=master,mode="rb",title="Select a file")

if file != None:
    contents = file.read()
    text.insert("1.0",contents)
    file.close()

def saving():
    save_command(text)

def save_command(self):
    file = filedialog.asksaveasfile(mode="w")
if file != None:
    data = self.get("1.0", END+"-1c")
    file.write(data)
    file.close()

def exit_command():
    if messagebox.askokcancel("Quit, Do you really want to quit?"):
        master.destroy()

def about_command():
    label = messagebox.showinfo("About", "Text Editor Version 1.0.0 \nCopyright 2016 \nCreator : Abhishek Singh")

# Menus
menu = Menu(master)
master.config(menu=menu)

# File Menu
FileMenu = Menu(menu)
menu.add_cascade(label="File", menu=FileMenu)
FileMenu.add_command(label="Open File", command=open_command)
FileMenu.add_command(label="Save As", command=saving)
FileMenu.add_separator()
FileMenu.add_command(label="Exit", command=exit_command)

# Edit Menu
EditMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=EditMenu)
EditMenu.add_command(label="Undo", command=dummy)
EditMenu.add_command(label="Redo", command=dummy)
EditMenu.add_command(label="Cut", command=dummy)
EditMenu.add_command(label="Copy", command=dummy)
EditMenu.add_command(label="Paste", command=dummy)

# Help Menu
HelpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=HelpMenu)
HelpMenu.add_command(label="About", command=about_command)

master.mainloop()

