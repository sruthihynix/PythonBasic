import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="examlogin"
)
mycurser = mydb.cursor()
#---------------------------------------------------------------------------------------------
def userStatusCheck():

    id = input("enter ID : ")
    pwd = input("enter 3 digit password :")
    mycurser.execute("SELECT status FROM logincheck WHERE uId ='%s' AND uPwd='%s' " % (id, pwd))
    record = mycurser.fetchone()
    # print(record)
    for i in record:
        # print(i)
        checkStatus=i
    if checkStatus==1:    # STATUS IS 1, THEN THE USER IS LOGGED IN, IF THE STATUS IS 0 NO USER IS LOGGEGD IN
        print("user is logged-in using this id")
    else:
        print("no user logged-in through this id")

# -------------------------------------------------------------------------------------------
def login():

    id = input("enter ID : ")
    pwd = input("enter 3 digit password :")
    mycurser.execute("SELECT status FROM logincheck WHERE uId ='%s' AND uPwd='%s' " % (id, pwd))
    record = mycurser.fetchone()
    # print(record)
    for i in record:
        # print(i)
        checkStatus=i
    if checkStatus != 1:# CHECK THE STATUS IN DB IF STATUS NOT EQUAL TO 1 THEN THE USER IS NOT LOGGED IN,
         # THEN SET STATUS TO 1,WHEN THE USER IS LOGINED
        print("Welcome......\n Sucessfully logged-in")
        mycurser.execute("UPDATE `logincheck` SET `status` = '1' WHERE  uId = '%s' AND uPwd='%s'"%(id,pwd))

        mydb.commit()

    else:
        print("User  already logged-in using this id")
#---------------------------------------------------------------------------------------------------
def logout():

    id = input("enter ID : ")
    pwd = input("enter 3 digit password :")
    mycurser.execute("SELECT status FROM logincheck WHERE uId ='%s' AND uPwd='%s' " % (id, pwd))
    record = mycurser.fetchone()
    # print(record)
    for i in record:
        # print(i)
        checkStatus = i

    if checkStatus ==1:# CHECK THE USER IS LOGGED-IN , IF STATUS  IS 1 THEN SET THE STATUS TO 0 WHILE LOG-OUT
        mycurser.execute("UPDATE `logincheck` SET `status` = '0' WHERE  uId = '%s' AND uPwd='%s'" % (id, pwd))
        mydb.commit()
        print("Sucessfully logged-out.....")

    else:
        print("No user logged-in using this Id")
# --------------------------------------------------------------------------------------------------------
while True:
    print(""" 
    1. User Status Check 
    2. Login
    3. Logout
    """)
    choice=int(input("Please enter your choice : "))

    if choice==1:
        userStatusCheck()

    elif choice==2:
        login()

    elif choice==3:
        logout()

