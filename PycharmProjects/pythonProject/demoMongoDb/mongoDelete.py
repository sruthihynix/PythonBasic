import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["school"]
# mycln=mydb["student"]
mycln=mydb["class1A"]
# ------------------------------------------------------------------
# delete_one()  method
# delete this --->Sideway 1633
# myquerry={"address": "Sideway 1633"}
# mycln.delete_one(myquerry)
# print("decument deleted")
# ------------------------------------------------Delete Many Documents-------------------
# delete_many() method
# myquery = { "name": {"$regex": "^S"} }
# #----- ^S for starts with letter S
# x = mycln.delete_many(myquery)
#
# print(x.deleted_count, " documents deleted.")

# -----------------------------------Delete All Documents in a Collection
x = mycln.delete_many({})

print(x.deleted_count, " documents deleted.")

