from tkinter import *
import mysql.connector
import tkinter.messagebox as tkMessageBox
import time

def funWithdraw():
    pas774120 

def funBalance():
    pass

def funCkPin():
    pass

# ///////////////////////////////////////////
window =Tk()
window.title("welcome...")
window.geometry("650x550")
window.config(bg="medium blue")
# --------------------------------------------------
USERNAME = StringVar()
PINno = StringVar()
amt=StringVar()
# ---------------------------------------------------

def database():
    global mydb, mycursor
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="canarabankdb")
    mycursor = mydb.cursor()

# ----------------------------------------------------
def welcome():
    global welcomeFrame

    welcomeFrame=Frame(window)      # frame 1
    welcomeFrame.config(bg="medium blue")
    welcomeFrame.pack(side=TOP)

    lblwelcome = Label(welcomeFrame, text="WELCOME...", bd=0,bg="medium blue",justify=LEFT,font=('arial', 25))
    lblwelcome.grid(row=1,column=0)

    lblBName=Label(welcomeFrame,text="CANARA BANK",bd=0,bg="medium blue", font=('arial',40),fg="white")
    lblBName.grid(row=3 ,column=2)

    lblSelect = Label(welcomeFrame, text="Select your language",bd=0,bg="medium blue", font=('arial', 20))
    lblSelect.grid(row=5)

    btnEng=Button(welcomeFrame,text="English",bd=0,bg="medium blue",font=('arial',20),fg="white",command=PIN)
    btnEng.grid(row=6, column=2)

    btnMal = Button(welcomeFrame, text="Malayalam", bd=0,bg="medium blue",font=('arial', 20),fg="white")
    btnMal.grid(row=7, column=2)

    btnHin = Button(welcomeFrame, text="Hindi", bd=0,bg="medium blue",font=('arial', 20),fg="white")
    btnHin.grid(row=8, column=2)

    btnotp = Button(welcomeFrame, text="Generate OTP/Forgot PIN", bd=0,bg="medium blue",font=('arial', 20))
    btnotp.grid(row=15, column=2)

    btnEng.bind('<Button-1>', ToggleToPin)
# ----------------------------------------------------------------------------------------------

def PIN():
    global pinFrame, lblMessage1,txtUname,txtpin

    pinFrame=Frame(window)      #frame 2
    pinFrame.config(bg="medium blue")
    pinFrame.pack(side=TOP,pady=20)

    lblBName=Label(pinFrame,text="CANARA BANK",bd=0,bg="medium blue", font=('arial',40),fg="white")
    lblBName.grid(row=3 ,column=1,pady=20)


    lblUname=Label(pinFrame,text="Usernme",bd=0,bg="medium blue", font=('arial',20),fg="white")
    lblUname.grid(row=15 ,column=1,pady=20)

    txtUname = Entry(pinFrame,font=('arial',20),textvariable=USERNAME)
    txtUname.grid(row=15, column=2)

    lblPin=Label(pinFrame,text="PIN",bd=0,bg="medium blue", font=('arial',20),fg="white")
    lblPin.grid(row= 16,column=1)

    txtpin = Entry(pinFrame,font=('arial',20),textvariable=PINno)
    txtpin.grid(row=16,column=2)

    btnPressHere=Button(pinFrame,text="PRESS HERE",bd=0,bg="medium blue", font=('arial',20),fg="white",command=funLogin)
    btnPressHere.grid(row= 17,column=2)

    lblMessage1 = Label(pinFrame,font=('arial',20))
    lblMessage1.grid(row=18,column=1)

    # label for message for invalid pin

    lblcontinue = Button(pinFrame, text="Continue", bd=0, bg="medium blue", font=('arial', 20)) # command
    lblcontinue.grid(row=20, column=2,pady=40)

    lblcontinue.bind('<Button-1>', ToggleToOptions)
# -------------------------------------------------------------
def options():

    global optionsFrame,lblBalDisplay

    optionsFrame = Frame(window)    #frame 3
    optionsFrame.config(bg="medium blue")
    optionsFrame.pack(side=TOP, pady=20)

    lblBName = Label(optionsFrame, text="CANARA BANK", bd=0, bg="medium blue", font=('arial', 40), fg="white")
    lblBName.grid(row=3, column=1, pady=20)

    lblSelect = Label(optionsFrame, text="SELECT YOUR SERVICES", bd=0, bg="yellow", font=('arial', 20), fg="black")
    lblSelect.grid(row=10, column=1, pady=20)

    btnWithdraw = Button(optionsFrame, text="WITHDRAWAL", bd=0, bg="Medium blue", font=('arial', 20), fg="black",command=acType) #command
    btnWithdraw.grid(row=12, column=2, pady=20)

    btnBalance = Button(optionsFrame, text="BALANCE ENQUARY", bd=0, bg="Medium blue", font=('arial', 20), fg="black",command=funBalance) #command
    btnBalance.grid(row=16, column=2, pady=20)

    lblBalDisplay = Label(optionsFrame, bd=0,bg="medium blue",font=('arial', 20), fg="white")
    lblBalDisplay.grid(row=20, column=1, pady=20)

    #label to display balance....

    btnWithdraw.bind('<Button-1>', ToggleToAccountTYpe)
# ---------------------------------------------------------

#-------------------------------------------------------------------------------------------

# --------------------------------------------------

def acType():

    global acTypeFrame

    acTypeFrame = Frame(window)     #frame 6
    acTypeFrame.config(bg="medium blue")
    acTypeFrame.pack(side=TOP, pady=20)

    lblBName = Label(acTypeFrame, text="CANARA BANK", bd=0, bg="medium blue", font=('arial', 40), fg="white")
    lblBName.grid(row=3, column=1, pady=20)

    lblSelect = Label(acTypeFrame, text="Plese select your account type", bd=0, bg="yellow", font=('arial', 20), fg="black")
    lblSelect.grid(row=10, column=1, pady=20)

    btnsavings = Button(acTypeFrame, text="Savings", bd=0, bg="Medium blue", font=('arial', 20), fg="black") #command
    btnsavings.grid(row=12, column=2, pady=20)

    btncurrent = Button(acTypeFrame, text="Current", bd=0, bg="Medium blue", font=('arial', 20), fg="black") #command
    btncurrent.grid(row=14, column=2, pady=20)
    #
    # btncredit = Button(acTypeFrame, text="Credit", bd=0, bg="Medium blue", font=('arial', 20), fg="black") #command
    # btncredit.grid(row=12, column=2, pady=20)
    btnsavings.bind('<Button-1>', ToggleToWithdrawAmt)
# -----------------------------------------------------------------------------------------------

def withdrawAmt():

    global withdrawAmtFrame,txtRs

    withdrawAmtFrame = Frame(window)    #frame 7
    withdrawAmtFrame.config(bg="medium blue")
    withdrawAmtFrame.pack(side=TOP, pady=20)

    lblBName = Label(withdrawAmtFrame, text="CANARA BANK", bd=0, bg="medium blue", font=('arial', 40), fg="white")
    lblBName.grid(row=3, column=1, pady=20)

    lblEnter = Label(withdrawAmtFrame, text="Enter the amount", bd=0, bg="yellow", font=('arial', 20), fg="black")
    lblEnter.grid(row=10, column=1, pady=20)

    lblRs = Label(withdrawAmtFrame, text="Rs.", bd=0, bg="yellow", font=('arial', 20), fg="black")
    lblRs.grid(row=11, column=1, pady=20)

    txtRs=Entry(withdrawAmtFrame,font=('arial',20),textvariable=amt)
    txtRs.grid(row=11,column=2)
    # /////////
    btnPressHere = Button(withdrawAmtFrame, text="PRESS HERE", bd=0, bg="medium blue", font=('arial', 20), fg="white",
                          command=funLogin)
    btnPressHere.grid(row=17, column=2)

    btnCorrect = Button(withdrawAmtFrame, text="Correct", bd=0, bg="Medium blue", font=('arial', 20), fg="black",command=funWithdraw) #command
    btnCorrect.grid(row=13, column=2, pady=20)

    btnClear=Button(withdrawAmtFrame, text="CLEAR", bd=0, bg="Medium blue", font=('arial', 20), fg="black") #command
    btnClear.grid(row=14, column=2, pady=20)

    # write a fun to clear txtRs field

    # btnIncorrect = Button(withdrawAmtFrame, text="Incorrect", bd=0, bg="Medium blue", font=('arial', 20), fg="black") #command
    # btnIncorrect.grid(row=14, column=2, pady=20)

    btnCorrect.bind('<Button-1>', ToggleToWait)
# -------------------------------------------------------------
def wait():
    global waitFrame

    waitFrame = Frame(window)   #frame 5
    waitFrame.config(bg="medium blue")
    waitFrame.pack(side=TOP, pady=20)

    lblBName = Label(waitFrame, text="CANARA BANK", bd=0, bg="medium blue", font=('arial', 40), fg="white")
    lblBName.grid(row=3, column=1, pady=20)

    time.sleep(2)

    lblplease = Label(waitFrame, text="Please wait Your Transction Being Preceeded...", bd=0, bg="yellow", font=('arial', 20), fg="black")
    lblplease.grid(row=10, column=1, pady=40)

    # btnWithdraw.bind('<Button-1>', ToggleToAccountTYpe)

# ------------------------functions-----------------------------


def funLogin():
    database()
    if USERNAME.get == "" or PINno.get() == "":
        lblMessage1.config(text="Please complete the required field!", fg="red")
    else:
        mycursor.execute("SELECT * FROM usampletable WHERE uName = %s AND pinNo = %s",(USERNAME.get(), PINno.get()))
        if mycursor.fetchone() is not None:

            lblMessage1.config(text="You Successfully Login", fg="blue")

        else:
            lblMessage1.config(text="Invalid Username or password, TRY AGAIN", fg="red")
            txtpin.delete(0, END)
            txtUname.delete(0,END)

# ----------------------------------------------------------------------------------------
def funWithdraw():

    database()
    wd = txtRs.get()
    print(wd)
    mycursor.execute("SELECT acbal FROM usampletable WHERE uName = %s AND pinNo = %s",(USERNAME.get(), PINno.get()))
    balTuple = mycursor.fetchone()  # we get a tuple in balTuple

    blist = list(balTuple)
    for i in blist:
        bal = int(i)  # to get the value AcBalance from the tuple
        # print(i)
        if bal > wd and bal > 500:
            newBal = bal - wd
            # print(newBal)
            mycursor.execute("UPDATE  usampletable SET acbal='%s' WHERE uName = %s AND pinNo = %s",(USERNAME.get(), PINno.get()))
            mydb.commit()  # commit() given to change value in the database
            print(f"{wd} Rupees Withdrawed \nNew balance is : {newBal} Rupees")
        else:
            print("Insufficient amount in your account")

# ------------------------------------------------------------
def funBalance():

    mycursor.execute("SELECT acbal FROM usampletable WHERE uName = %s AND pinNo = %s",(USERNAME.get(), PINno.get()))
    blist = mycursor.fetchone()
    for i in blist:
        bal = int(i)  # to get the value AcBalance from the tuple
        # print(f"Your balance after depositing  : {bal} Rupees. ")

        lblBalDisplay.config(text='Your current Balance:'+str(bal)) # to concandenate bal (intrger)with string convert balance to string


#--------------TOOGLE FRAMES-------------------------------
# -----------------------------------------------------------
def ToggleToPin(event=None):
    welcomeFrame.destroy()
    PIN()
# ------------------------------------------------------------
def ToggleToOptions(event=None):
    pinFrame.destroy()
    options()
# -----------------------------------------------------------
def ToggleToAccountTYpe(event=None):
    optionsFrame.destroy()
    acType()
# -----------------------------------------------------------
def ToggleToWithdrawAmt(event=None):
    acTypeFrame.destroy()
    withdrawAmt()
# -----------------------------------------------------------
def ToggleToWait(event=None):
    withdrawAmtFrame.destroy()
    wait()

# --------------------------------------------------------------------------------
welcome()
window.mainloop()
