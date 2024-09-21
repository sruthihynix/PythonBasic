from tkinter import *
import mysql.connector
import tkinter.messagebox as tkMessageBox

window=Tk()
window.title("login-----")
window.geometry("650x500")
window.config(bg="yellow")
# ----------------------------------------------------------------
USERNAME = StringVar()
PASSWORD = StringVar()
FIRSTNAME = StringVar()
LASTNAME = StringVar()
# ----------------------------------------------------------------
""" functions--> database()
              funlogin()
              fundetails()
              
              frameLogin()
              frameDetails()
              
              ToogleToLogin()
              ToogleToDetails()
              
            
    frame-->  deaFrame
              logFrame"""

# -------------------------------------------------------------------
def database():
    global mydb, mycursor
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="logintkinter")
    mycursor = mydb.cursor()

# table->framelogintable
# -------------------------------------------------------
def frameLogin():

    global LoginFrame,lblMessage1

    LoginFrame = Frame(window)
    LoginFrame.pack(side=TOP, pady=80)

    lblUsername = Label(LoginFrame, text="Username:", font=('arial', 25), bd=18)
    lblUsername.grid(row=1)

    lblPwd = Label(LoginFrame, text="Password:", font=('arial', 25), bd=18)
    lblPwd.grid(row=2)

    lblMessage1 = Label(LoginFrame, text="")
    lblMessage1.grid(row=3, column=1)

    username = Entry(LoginFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=1, column=1)

    password = Entry(LoginFrame, font=('arial', 20), textvariable=PASSWORD, width=15) #show="*"
    password.grid(row=2, column=1)

    btnLogin = Button(LoginFrame, text="Login", font=('arial', 18), width=35, command=funLogin)
    btnLogin.grid(row=4, columnspan=2, pady=20)

    lblDetail = Label(LoginFrame, text="Go To Details", fg="Blue", font=('arial', 15))
    lblDetail.grid(row=0, sticky=W)

    lblDetail.bind('<Button-1>', ToggleToDetails)

# --------------------------------------------------------------------------------------
def frameDetails():

    global deaFrame,lblMessage2

    deaFrame=Frame(window)

    deaFrame.pack(side=TOP,pady=100)
    # deaFrame.config(bg="pink")

    lblMessage2=Label(deaFrame,text="",font="arial 30")
    lblMessage2.grid(row=1,columnspan=1)

    # lbl_login = Label(deaFrame, text=" Login", fg="Blue", font=('arial', 12))
    # lbl_login.grid(row=0, sticky=W)
    btn_login = Button(deaFrame, text="Back To login", font=('arial', 10), width=20, command=funDetails())# while not use () get error
    btn_login.grid(row=20,column=10)

    btn_login.bind('<Button-1>', ToggleToLogin)

def funLogin():
    database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lblMessage1.config(text="Please complete the required field!", fg="orange")
    else:
        mycursor.execute("SELECT * FROM framelogintable WHERE username = %s AND password = %s",(USERNAME.get(), PASSWORD.get()))
        if mycursor.fetchone() is not None:

            lblMessage1.config(text="You Successfully Login", fg="blue")

        else:
            lblMessage1.config(text="Invalid Username or password", fg="red")



def funDetails():

    database()

    mycursor.execute("SELECT * FROM framelogintable WHERE username = %s ",(USERNAME.get(),))

    if mycursor.fetchone() is not None:
        mycursor.execute("SELECT * FROM framelogintable WHERE username = %s ", (USERNAME.get(),))
        record=mycursor.fetchall()
        for i in record:
            lblMessage2.config(text=i)

    else:
        lblMessage2.config(text="no record ")


def ToggleToLogin(event=None):
    deaFrame.destroy()
    frameLogin()


def ToggleToDetails(event=None):
    LoginFrame.destroy()
    frameDetails()

# ------------------------------------------------------------

frameLogin()

window.mainloop()
