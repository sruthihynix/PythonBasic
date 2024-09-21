
#-------------TO CHECK DATABASEs  ALREADY EXISTS--------------
import mysql.connector
mydb= mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database='mydatabase'
)
mycurser = mydb.cursor()

mycurser.execute("SHOW DATABASES")
for i in mycurser:
    print(i)