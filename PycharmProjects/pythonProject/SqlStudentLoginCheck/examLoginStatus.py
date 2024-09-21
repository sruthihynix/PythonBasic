import mysql.connector

mydb=mysql.connector.connect(
    host= "local host",
    user= "root",
    password= " ",
    database="examlogin"
)
mycurser=mydb.connect()

print('----------WELCOME TO EXAMINATION LOGIN PAGE-------------')

user=input("Enter user name : ")
status=1
sql="INSERT INTO ulogin (uName,status) VALUES (%s %s)"
value=(user,status)
mycurser.execute(sql,value)
mydb.commit()
print(mycurser.rowcount, "Record inserted")