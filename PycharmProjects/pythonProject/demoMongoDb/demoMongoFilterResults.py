import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["school"]
mycln = mydb["student"]

# ----------------Filter the Result-----------------------------------------------

# myquery = { "address": "Park Lane 38" }
check={"name":"achu"} # condition

mydoc = mycln.find(check) #

for x in mydoc:
  print(x)
# ----------------------Advanced Query-------------
# ---$gt for grater than----$lt lessthan
myquery = { "class": { "$gt": "s" } }
# myquery = { "address": { "$lt": "A" } }
mydoc = mycln.find(myquery)

for x in mydoc:
  print(x)

