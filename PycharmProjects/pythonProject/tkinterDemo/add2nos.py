from tkinter import *

def add():
    n1=float(txt1.get())
    n2=float(txt2.get())
    result=n1+n2
    # rlabel.config(text=result)
    # result.set(result)
    rlabel.config(text="result is :"+str(result)) # to display the result in the label

parent=Tk()

parent.title("ADD TWO NUMBERS")
parent.geometry("200x200")
parent.config(background="blue")

no1=Label(parent,text=" First No ",)
txt1=Entry(parent)

no2=Label(parent ,text="Second No ")
txt2=Entry(parent)

addbtn=Button(parent,text="ADD",command=add)
rlabel=Label(parent,text="result : ")
# rlabel=Label(parent)

no1.grid(row=0,column=0)
txt1.grid(row=0,column=1)

no2.grid(row=1,column=0)
txt2.grid(row=1,column=1)

addbtn.grid(row=2,column=0,columnspan=2)
rlabel.grid(row=3,column=0,columnspan=10,rowspan=5)

parent.mainloop()



# https://www.code4example.com/python/tkinter/python-program-to-add-two-numbers-in-tkinter/