import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017")

mydb=myclient["smec"]
mycln=mydb["batch1"]
#----------------------------------------------------------
# mylist = [
#   { "name": "jio", "address": "ekm","Time":"2 pm"},
#   { "name": "hari", "address": "klm","Time":"4 pm"},
#   { "name": "midhin", "address": "tsr","Time":"3 pm"},
#   { "name": "Sana", "address": "tvm","Time":"5 pm"},
#   { "name": "binu", "address": "Ekm","Time":"2 pm"},
#   { "name": "Richu", "address": "pkd","Time":"10 pm"},
#   { "name": "sruthi", "address": "mplm","Time":"3 pm"},
#   { "name": "viga", "address": "ekm","Time":"4 pm"},
#   { "name": "Bella", "address": "ktym","Time":"3 pm"},
#   { "name": "vichu", "address": "ekm","Time":"3 pm"},
#   { "name": "siya", "address": "tsr"},
#   { "name": "vihu", "address": "Ekm"}
# ]
#
# x = mycln.insert_many(mylist)
# print("documents inserted")
# ------------------------------------------------------------------------
myquery = { "name": "binu" }
newvalues = { "$set": { "address": "banglore","time":"10 pm" } }

mycln.update_one(myquery,newvalues)

#print "batch1" after the update
for x in mycln.find():
  print(x)

# ------------------------------------------------------------------
myquery = { "time": { "$regex": "" } }
newvalues = { "$set": { "address": "palakad" } }

x = mycln.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")
