# import connection
import mysql.connector

# create mydb- a reference object to connect to database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

print(mydb)
# create a database named "mydatabase":
mycurser= mydb.cursor()
mycurser.execute('CREATE DATABASE mydatabase')

