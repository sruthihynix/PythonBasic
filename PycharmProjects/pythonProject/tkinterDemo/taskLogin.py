from tkinter import *
import mysql.connector

window=Tk()
window.title("Tkinter simple login" )
window.geometry("500x500")

# ---------------variables---------------------------------
USERNAME=StringVar()
PASSWORD=StringVar()
FIRSTNAME=StringVar()
LASTNAME=StringVar()

# ------------------methods-------------------------------
def database():
    global mydb,mycurser
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="logintkinter")
    mycurser = mydb.cursor()

# ------------------------------------------------
def loginForm():

    global lblmessage,loginFrame

    loginFrame=Frame(window)
    loginFrame.pack(side=TOP,pady=50)

    lblUserName=Label(loginFrame,text="Username :", font="arial 20")
    lblUserName.grid(row= 1)

    lblPwd=Label(loginFrame,text="Password :", font="arial  20")
    lblPwd.grid(row=2)

    ebUserName=Entry(loginFrame,font="arial 20",textvariable=USERNAME, width=15)
    ebUserName.grid(row=1,column=1)

    ebPwd = Entry(loginFrame, font="arial 20", textvariable=PASSWORD, width=15)
    ebPwd.grid(row=2, column=1)

    btnLogin=Button(loginFrame,text="Login",font="arial 15",width=30,command=login)
    btnLogin.grid(row=3,columnspan=2,pady=20)

    lblmessage=Label(loginFrame,text="",font="arial 20")
    lblmessage.grid(row=5,column=0)

    # lblDetails = Label(loginFrame, text="Details", fg="Blue", font=('arial', 12))
    # lblDetails.grid(row=0, sticky=W)
    btnDetails=Button(loginFrame, text="Details",command=Details)
    btnDetails.grid(row=0,sticky=W)
    btnDetails.bind('<Button-1>', ToggleToDetails())


def login():
    database()
    # loginForm()
    if USERNAME.get()=="" or PASSWORD.get()=="":
        lblmessage.config(text="enter values ")
    else:
        mycurser.execute("SELECT * FROM framelogintable where username=%s and password=%s", (USERNAME.get(),
                         PASSWORD.get()))
        record=mycurser.fetchone()
        if record is not None:

            mycurser.execute("SELECT * FROM framelogintable where username=%s and password=%s", USERNAME.get(),
                             PASSWORD.get())
            record = mycurser.fetchone()
            lblmessage.config(text="login successfull")
            # details()******************
        else:
            lblmessage.config(text="invalid", fg="red")

def Details():
    global detailsFrame
    database()

    detailsFrame=Frame(window)
    detailsFrame.pack(side=TOP, pady=40)
    lblMessage2=Label(detailsFrame,text="", font="arial 30",bg="orange")
    lblMessage2.pack()

    mycurser.execute("SELECT * FROM framelogintable WHERE username=%s",(USERNAME.get()))
    record=mycurser.fetchall()
    for i in record:
        lblMessage2.config(text=i)




def ToggleToDetails(event=None):
    loginFrame.destroy()
    Details()

def ToggleToLogin(event=None):
   pass


# *************************************

# window=Tk()
# window.title("Tkinter simple login" )
# window.geometry("500x500")


loginForm()

window.mainloop()