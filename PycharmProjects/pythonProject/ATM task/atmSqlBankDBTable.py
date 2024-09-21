import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = "",
    database = "bank"
)
mycurser=mydb.cursor()
mycurser.execute("CREATE TABLE AtmUsers (usesrName varchar(50), userPassword varchar(50))")
