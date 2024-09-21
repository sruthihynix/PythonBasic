import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = "",
    database = "bank"
)
mycurser=mydb.cursor()

print("-----------Welcome To ATM---------------")
print(""" 
Press 1 for LOGIN
Press 0 for New user registration""")
n=int(input("enter your choice : "))

# ----------------new user registration--------------
if n==0:
    print("Welcome to user registration")
    acno= int(input("Enter Account Number : "))
    username=input("Enter User Name : ")
    pwd=input("Enter a 4 digit password :")
    bal=int(input("Enter starting amount :"))
    sql = "INSERT INTO atmusers (username,userpassword,AcBalance) VALUES (%s, %s,%s)"
    val = (username,pwd,bal)
    mycurser.execute(sql,val)
    mydb.commit()
    print(" New User registered")

# --------------login-------------------------------
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
            1. balance chk
            2. deposit
            3. withdrawal
            """)
            choice=int(input("Enter your choice : "))
            if choice== 1:
                mycurser.execute("SELECT AcBalance FROM atmusers WHERE userPassword='%s'"%(upwd))
                blist=mycurser.fetchone()
                for i in blist:
                    bal = int(i)  # to get the value AcBalance from the tuple
                    print(bal)
            elif choice==2:
                depo=int(input("Enter the amount to deposit:"))
                mycurser.execute("SELECT AcBalance FROM atmusers WHERE userPassword='%s'"%(upwd))
                balTuple=mycurser.fetchone()# we get a tuple in balTuple
                # print(balTuple)
                blist=list(balTuple)
                for i in blist:
                    w=int(i)
                    # print(i)
                    newBal=w+depo
                    # print(newBal)
                    mycurser.execute("UPDATE  atmusers SET AcBalance='%s' WHERE userPassword='%s'" % (newBal,upwd))
                    mydb.commit()   #commit() given to change value in the database
                    print(f"{depo} Rupees Deposited,\n New Balance is : {newBal} Rupees")
#-----------withdrawal---------------------
            elif choice==3:
                wd=int(input("Enter the amount :"))
                mycurser.execute("SELECT AcBalance FROM atmusers WHERE userPassword='%s'" % (upwd))
                balTuple = mycurser.fetchone()  # we get a tuple in balTuple
                # print(balTuple)
                blist = list(balTuple)
                for i in blist:
                    bal = int(i) # to get the value AcBalance from the tuple
                    # print(i)
                    newBal = bal - wd
                    # print(newBal)
                    mycurser.execute("UPDATE  atmusers SET AcBalance='%s' WHERE userPassword='%s'" % (newBal, upwd))
                    mydb.commit()  # commit() given to change value in the database
                    print(f"{wd} Rupees Withdrawn,\nRemaining Balance is : {newBal} Rupees")


        else:
              print("SORRY invalid pwd")
    else:
        print("account not exist")
# else:
#     print('Account not exist')

