import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["school"]
mycol = mydb["student"]

myquery = { "address": { "$regex": "^A" } }
newvalues = { "$set": { "name": "akshaj" } }

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")
