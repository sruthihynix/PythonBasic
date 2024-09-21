import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="bird.gif") #image must be present in the same directory/project location

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

w = tk.Label(root,
             compound = tk.CENTER,
             text=explanation,
             image=logo).pack(side="right")

root.mainloop()
