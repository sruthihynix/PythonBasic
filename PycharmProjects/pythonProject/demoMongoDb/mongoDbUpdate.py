import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["python"]
mycln=mydb["b1"]


# myquery = { "name": "joyal" }
# newvalues = { "$set": { "name": "JOY" } }
myquery = { "name": { "$regex": "^J" } }
newvalues = { "$set": { "name": "vihaan" } }

mycln.update_one(myquery, newvalues)

#print "b1" after the update:
for x in mycln.find():
  print(x)
#   ---------------------------------------
