import mysql.connector # import
#mydb sql object
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='examlogin'
)

mycurser= mydb.cursor()

print("1.login 2.logout")
choice=input("enter choice:")


                # uId, uPwd,status
# ------------------login  checking ----------------
id = input("enter ID : ")
pwd=input("enter 3 digit password :")
mycurser.execute("SELECT status FROM logincheck WHERE uId ='%s'AND uPwd='%s'" % (id,pwd))
record = mycurser.fetchone()
print(record)
for i in record:
    print(i)
    if i==1:
        print(i)
        print("user already logined")

    else:
# ----------------------insert logined user id into the db----------------------------------
        sql = "INSERT INTO logincheck (uId,uPwd,status) VALUES (%s, %s,%s)"
        val = (id,pwd, "1")
        # --------execute() method used to execute query
        mycurser.execute(sql, val)
        # -------mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.
        mydb.commit()
        print("Login Sucessfull")
        # print(mycurser.rowcount, "record inserted.")
    # else:
#     logout
# mycurser.execute("UPDATE logincheck SET status=0, WHERE condition uId ='%s'AND uPwd='%s'" % (id,pwd))
