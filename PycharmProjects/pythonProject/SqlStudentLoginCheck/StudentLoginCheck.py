import mysql.connector # import
#mydb sql object
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='examlogin'
)

mycurser= mydb.cursor()

# uId,status
# ------------------login  checking ----------------
id = input("enter ID : ")
pwd=input("enter 3 digit password :")
mycurser.execute("SELECT * FROM logincheck WHERE uId ='%s'" % (id))
record = mycurser.fetchone()
# print(record)
if mycurser.rowcount == 1:
  print("user already logined")

else:
# ----------------------insert logined user id into the db----------------------------------
    status=1
    sql = "INSERT INTO logincheck (uId,uPwd,status) VALUES (%s, %s,%s)"
    val = (id,pwd, "1")
    # --------execute() method used to execute query
    mycurser.execute(sql, val)
    # -------mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.
    mydb.commit()
    print("Login Sucessfull")
    # print(mycurser.rowcount, "record inserted.")

