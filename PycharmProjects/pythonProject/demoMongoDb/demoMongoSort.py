import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["school"]
mycln = mydb["student"]
# ------------------------------------------+
mydoc = mycln.find().sort("name")

for x in mydoc:
  print(x)

