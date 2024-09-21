import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = ""
)
mycurser=mydb.cursor()
mycurser.execute("CREATE DATABASE bank")