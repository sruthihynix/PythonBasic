import  pymongo # pymongo module inserted

myclient = pymongo.MongoClient("mongodb://localhost:27017/")# establshing connection

# //////////////mongodb://localhost:27017 --- connection string
mydb = myclient["school"] # connecting to dataase - school
mycln=mydb["student"] # connecting to collection (table) -student
# ---------------------------------------------------------------------------------
#//////////////////// in mongodb id is automatocally generated
# mydict = { "name": "sruthi", "class": "3A", "address": "NH 47" }

# x = mycln.insert_one(mydict) # insert_one()

# print(" document inserted")
# print(x.inserted_id) # returns the inserted id
# -----------------------------------------------------------------------------------

# ////////////////// inserting multiple documents to collection
# mylist = [
#   { "name": "Amy", "address": "Apple st 652"},
#   { "name": "Hannah", "address": "Mountain 21"},
#   { "name": "Michael", "address": "Valley 345"},
#   { "name": "Sandy", "address": "Ocean blvd 2"},
#   { "name": "Betty", "address": "Green Grass 1"},
#   { "name": "Richard", "address": "Sky st 331"},
#   { "name": "Susan", "address": "One way 98"},
#   { "name": "Vicky", "address": "Yellow Garden 2"},
#   { "name": "Ben", "address": "Park Lane 38"},
#   { "name": "William", "address": "Central st 954"},
#   { "name": "Chuck", "address": "Main Road 989"},
#   { "name": "Viola", "address": "Sideway 1633"}
# ]
#
# x = mycln.insert_many(mylist) # insert_many()

#//////////////// print list of the _id values of the inserted documents:
# print(x.inserted_ids)
#-----------------------------------------------------------
#/////////////// inserting with specified id
# mylist={"_id": 7, "name": "Betty", "address": "Green Grass 1"}
# x=mycln.insert_one(mylist)
# print("inserted")
# ------------------------------------------------------------
#  ////////////////////// return the first document in the collectiom
# x = mycln.find_one()
# print(x)
#------------------------------------------------------------------------
