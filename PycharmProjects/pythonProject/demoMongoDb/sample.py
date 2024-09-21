import pymongo
# establishing connection to mongodb local host using object myclient
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# connecting to database named mydatabase
mydb = myclient["smec2023"]
mycln=mydb["batch"]

# cname = input(" please enter name")
# myquery = {"name": "joyal"}
# # mydoc = mycln.find(myquery)
# newvalues = {"$set": {"name": cname}}
# mycln.update_one(myquery, newvalues)
# --------------------------------------------------------
