import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["python"]
mycln=mydb["b1"]
mycln.drop()
print("collection is deleted")