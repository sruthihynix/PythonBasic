import mysql.connector

mydb=mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mydatabase"
)
mycurser = mydb.cursor()

# ---------SELECT * from customers table and print------------
# mycurser.execute("SELECT * FROM customers")

# We use the fetchall() method, which fetches all rows from the last executed statement
# myresult1 = mycurser.fetchall()
# for i in myresult1:
#     print(i)

# ---------SELECT name from customers table and print ------------
# mycurser.execute("SELECT name FROM customers")
# myresult2 = mycurser.fetchall()
# for i in myresult2:
#     print(i)

# ---------to get first row in the table-------------fetchone()
mycurser.execute("SELECT * FROM customers")
myresult3 = mycurser.fetchone()
print(myresult3)
 