from tkinter import *
import pymongo
import tkinter as tk

# CONNECTING DATABASE MONGODB
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["class"]
mycln=mydb["students"]

def add():
    name=txtname.get()
    # print(name)
    cls=txtclass.get()
    # print(cls)
    age=txtage.get()
    # print(age)
    mydoc = {"name": name, "class": cls, "age": age}

    x = mycln.insert_one(mydoc)
    # print(x)
    lblmsg.config(text="Student details added successfully:" )
    txtname.delete(0, END)
    txtage.delete(0, END)
    txtclass.delete(0, END)

    #Tkinter Config() function, which can be used on any widget to change settings
    # that you may have applied earlier, or haven’t applied yet.

def delete():
    # dname=input("enter the name to delete")
    lblmsg.config(text="enter name :")
    dname=txtname.get()
    check = {"name": dname}
    mydoc = mycln.find(check)  # in x will return inserted id
    if mycln.count_documents(check).bit_count()>0:
        for i in mydoc:
            print(i)
            mycln.delete_one({"name":dname})
            print("Deleted successfully")
            lblmsg.config(text="Student deleted:")
            txtname.delete(0, END)
            txtage.delete(0, END)
            txtclass.delete(0, END)

    else:
        lblmsg.config(text="Student not found:")
        print("not found")

def clear():
    txtname.delete(0,END)
    # txtname.set('')
    txtage.delete(0,END)
    txtclass.delete(0,END)
    lblmsg.config(text="")
#-------------------------------------------------------------------
# def details():
#
#     # lblmsg.config(text="enter name :")
#     dname=txtname.get()
#     check = {"name": dname}
#     mydoc = mycln.find(check)  # in x will return inserted id
#     if mycln.count_documents(check).bit_count()>0:
#         for i in mydoc:
#             print(i)
#             a=mydoc["age"]
#             print(a)
#             # txtage.config(text="")
#
#     else:
#         lblmsg.config(text="Student not found:")
#         print("not found")
# # -----------------------------------------------------------------------------
def update():
    lblmsg.config(text="Enter the name:")
    Uname=txtname.get()
    myquery = {"name": Uname}
    mydoc = mycln.find(myquery)

    for x in mydoc:
        print(x)
        print("Enter the details you want to update")

        try:
           name=txtname.get()
           cls=txtclass.get()
           age=txtage.get()

           mycln.update_one(
                {"name": Uname},
                {
                    "$set": {
                        "name": name,
                        "class":cls,
                        "age": age

                    }
                }
            )
           lblmsg.config(text="Records updated successfully")
           # print("\nRecords updated successfully\n")
                     # print "cln" after the update:
        except Exception:
            print(str("error"))
# -------------------------------------gender selection----------------------
# def selection():
#     value=rbtn.get()
#     if value==1:
#         gender="Male"
#         print(gender)
#     else:
#         gender="Female"
#         print(gender)




window=Tk() # OBJECT WINDOW IS CREATED

window.title("Students Registration")
window.geometry("500x400")

lblHeading=Label(window,text= "STUDENT REGISTRATION FORM", width=10, height=2,bg="pink",fg= "#fff", font="arial 20 bold",anchor="e")
lblHeading.pack(side=TOP,fill=X)

lblname = Label(window,text="Name")
lblname.pack()

txtname = Entry(window)
txtname.pack()

lblclass = Label(window,text="Class")
lblclass.pack()

txtclass = Entry(window)
txtclass.pack()

lblage = Label(window,text="Age")
lblage.pack()

txtage = Entry(window)
txtage.pack()

# rbtn=Radiobutton(window,text="Male",variable=radio,value=1,font=10,command=selection)
# rbtn.pack()

# rbtn=Radiobutton(window,text="Female",variable=radio,value=2,font=10)
# rbtn.pack()


btnadd = Button(window,text="ADD",command=add)
btnadd.pack()

btndel = Button(window,text="DELETE",command=delete)
btndel.pack()

btnclear = Button(window,text="CLEAR ", fg ="blue",command=clear)
btnclear.pack()

lblmsg = Label(window,text="", font="bold 20",fg="red" )
lblmsg.pack(side=BOTTOM)

btnupdate = Button(window,text="UPDATE",command=update)
btnupdate.pack()

# btndetails = Button(window,text="VIEW DETAILS",command=details)
# btndetails.pack()

window.mainloop()