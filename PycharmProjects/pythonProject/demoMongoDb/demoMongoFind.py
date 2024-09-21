import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["school"]
mycln = mydb["student"]


# -------------------------------------------------------------
# find_one() this returns the first document in the collection
# x = mycln.find_one()
# print(x)
# -------------------------------------------------------------
# //// print all documents in the collection
# x=mycln.find_one() # in x will return inserted id
# for x in  mycln.find():
#     print(x)
# --------------------------------------------------------------
# ------0/1 boolean expressions
x=mycln.find_one()
print("---------------Return only the names and addresses, not the _ids:--------------")

for x in mycln.find({},{ "_id": 0, "name": 1, "address": 1 }):
    print(x)
#-------------------------------------------------------------------
print("--------------print name field only--------------")
for x in mycln.find({},{ "_id": 0, "name": 1}):
    print(x)
# -------------------------------------------------------------------
print("--------------print adres field only--------------")
for x in mycln.find({},{ "_id": 0, "address": 1 }):
    print(x)
# --------------------------to list all the databases on the compus--------------------------------------
# print(myclient.list_database_names())
# ------------------------------------------------------------