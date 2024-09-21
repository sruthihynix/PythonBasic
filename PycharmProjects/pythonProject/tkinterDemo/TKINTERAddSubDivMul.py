from tkinter import *

def add():
    n1=float(txt1.get())
    n2=float(txt2.get())
    result=n1 + n2
    # rlabel.config(text=result)
    # result.set(result)
    rlabel.config(text="result is :"+str(result))

def sub():
    n1=float(txt1.get())
    n2=float(txt2.get())
    result=n1 - n2
    rlabel.config(text="result is :"+str(result))

def div():
    n1=float(txt1.get())
    n2=float(txt2.get())
    result=n1 / n2
    rlabel.config(text="result is :"+str(result))

def mul():
    n1=float(txt1.get())
    n2=float(txt2.get())
    result=n1 * n2
    rlabel.config(text="result is :"+str(result))

def clear():
    txt2.delete(0,END)
    txt1.delete(0,END)
    # rlabel(parent,)


parent=Tk()

parent.title("ADD-DIV-SUB-MUL") #title of the window
parent.geometry("300x200")  # width and height of the window
parent.config(background="pink")
parent.resizable(False,False)# to set the window size not resizable


no1=Label(parent,text=" First No ",)
txt1=Entry(parent)

no2=Label(parent ,text="Second No ")
txt2=Entry(parent)

rlabel=Label(parent,text="Result : ",fg="blue",bg="yellow")

# calling fun when button click
clearBtn=Button(parent,text="CLEAR",command=clear)
addbtn=Button(parent,text="ADD",command=add)
subBtn=Button(parent,text="SUB", command=sub)
divBtn=Button(parent,text="DIV", command=div)
mulBtn=Button(parent,text="MUL", command=mul)


# arranging positions
no1.grid(row=0,column=0)
no2.grid(row=1,column=0)

txt1.grid(row=0,column=1)
txt2.grid(row=1,column=1)

addbtn.grid(row=2,column=0)
subBtn.grid(row=2,column=1)
divBtn.grid(row=3,column=0)
mulBtn.grid(row=3,column=1)
clearBtn.grid(row=4,column=1)

rlabel.grid(row=4,column=0,sticky="ew")

parent.mainloop()






# https://www.code4example.com/python/tkinter/python-program-to-add-two-numbers-in-tkinter/