import mysql.connector
import time
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = "",
    database = "bank"
)
mycurser=mydb.cursor()

#----------------------deposit------------------------------------

def deposit():
    depo = int(input("Enter the amount to deposit:"))
    mycurser.execute("SELECT AcBalance FROM atmusers WHERE userPassword='%s'" % (upwd))
    balTuple = mycurser.fetchone()  # we get a tuple in balTuple
    # print(balTuple)
    blist = list(balTuple)
    for i in blist:
        w = int(i)
        # print(i)
        newBal = w + depo
        # print(newBal)
        mycurser.execute("UPDATE  atmusers SET AcBalance='%s' WHERE userPassword='%s'" % (newBal, upwd))
        mydb.commit()  # commit() given to change value in the database
        print(f"{depo} Rupees Deposited,\n New balance is : {newBal} Rupees")
        mydb.commit()  # commit() given to change value in the database

#-------------withdrawal--------------------------

def withdraw():
    wd=int(input("Enter the amount :"))
    mycurser.execute("SELECT AcBalance FROM atmusers WHERE userPassword='%s'" % (upwd))
    balTuple = mycurser.fetchone()  # we get a tuple in balTuple

    blist = list(balTuple)
    for i in blist:
        bal = int(i) # to get the value AcBalance from the tuple
        # print(i)
        if bal>wd and bal>500:
            newBal = bal - wd
            # print(newBal)
            mycurser.execute("UPDATE  atmusers SET AcBalance='%s' WHERE userPassword='%s'" % (newBal, upwd))
            mydb.commit()  # commit() given to change value in the database
            print(f"{wd} Rupees Withdrawed \nNew balance is : {newBal} Rupees")
        else:
            print("Insufficient amount in your account")

# -----------------balabce ckeck------------------------------
def balanceCheck():
    mycurser.execute("SELECT AcBalance FROM atmusers WHERE userPassword='%s'" % (upwd))
    blist = mycurser.fetchone()
    for i in blist:
        bal = int(i)  # to get the value AcBalance from the tuple
        print(f"Your balance after depositing  : {bal} Rupees. ")


print("-----------Welcome To ATM---------------")
print(""" 
Press 1 for LOGIN
Press 0 for New user registration""")
n=int(input("enter your choice : "))
if n==0:
    print("-----------Welcome to user registration--------------")
# ----------------new user registration--------------

if n==0:

    while True:
            # this while is used to check the username is unique or not
            # only unique user name allowed here
        # print("-----------Welcome to user registration--------------")
        # acno= int(input("Enter Account Number : "))
        username=input("Enter User Name : ")
        mycurser.execute("SELECT username FROM atmusers WHERE username='%s'"%(username))
        record=mycurser.fetchone()
        if mycurser.rowcount ==0:
                pwd=input("Enter a 4 digit password :")
                bal=int(input("Enter starting amount :"))
                sql = "INSERT INTO atmusers (username,userpassword,AcBalance) VALUES (%s, %s,%s)"
                val = (username,pwd,bal)
                mycurser.execute(sql,val)
                mydb.commit()
                print(" New User registered")
                continue
        else:
            print("try another uname")


elif n==1:
    print("WElCOME")
    user= input("Enter your User Name :")
    upwd=input("Enter 4 digit password : ")
    # mycurser=mydb.cursor()
    mycurser.execute("SELECT * FROM atmusers WHERE username='%s'"%(user))
    record=mycurser.fetchone()
    # print(record)
    if mycurser.rowcount==1:
        mycurser.execute("SELECT * FROM atmusers WHERE userPassword ='%s'"%(upwd))
        record= mycurser.fetchone()
        # print(record)
        if mycurser.rowcount==1:
            print("login sucessfull")
            print("""
            1. Balance Enquiry
            2. Deposit
            3. Withdrawal
            4. Cancel Transcation
            """)

while True:
    choice=int(input("Enter your Choice : "))
    if choice==1:
        balanceCheck()
    elif choice==2:
        deposit()
    elif choice==3:
        withdraw()
    elif choice==4: # exit
        print('\nTranscation Cancelled')
        print('----THANK YOU-----')
        break
