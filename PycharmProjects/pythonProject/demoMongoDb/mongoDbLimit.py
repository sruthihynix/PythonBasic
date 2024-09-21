import pymongo
mongoclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=mongoclient["school"]
mycln=mydb["student"]

result=mycln.find().limit(5) # limit(5) show first 5 documents

for x in result:
    print(x)