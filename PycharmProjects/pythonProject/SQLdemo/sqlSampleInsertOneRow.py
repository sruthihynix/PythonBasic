import mysql.connector # import
#mydb sql object
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  # database='mydatabase'
  database='examlogin'
)

# mycursor
# It is an object that is used to make the connection for executing SQL queries
mycurser= mydb.cursor()

# ------------create table customers------------------------
# mycurser.execute('CREATE TABLE customers (name varchar(255), address varchar(255))')
# add a primary key id in to the existing table customers
# mycurser.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# ------------------ insesrting vallues in to table----------------
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Sruthi", "house no: 290")
# --------execute() method used to execute query
# mycurser.execute(sql, val)
# -------mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.
# mydb.commit()

# print(mycurser.rowcount, "record inserted.")
#---------return the last inserted row number-------------
# print("1 record inserted, ID:", mycurser.lastrowid)
# -----------------------------update
sql= "UPDATE `logincheck` SET `status`='0' WHERE uId='vinod';"
mycurser.execute(sql)
mydb.commit()
# ------------------------------------------------------------------