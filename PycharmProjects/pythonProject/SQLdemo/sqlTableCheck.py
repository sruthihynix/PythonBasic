
#-------------TO CHECK tables ALREADY EXISTS--------------
import mysql.connector
mydb= mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database='mydatabase'
)
mycurser = mydb.cursor()

mycurser.execute("SHOW TABLES")
for i in mycurser:
    print(i)