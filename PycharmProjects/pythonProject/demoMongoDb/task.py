import pymongo
# establishing connection to mongodb local host using object myclient object
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# connecting to database named smec2023
mydb = myclient["smec2023"]
mycln=mydb["batch"]

# # --------------------------------------------insert------
# print("Enter the student details\n")
# name = input("Name :")
# course = input("Course :")
# duration = input("course  duration :")
# time = input("Batch time :")
#
# mydoc = { "name": name, "course": course, "dutation":duration,"time":time }
#
# x = mycln.insert_one(mydoc)
#
# print(x)
#
# # ----------update-----------------------------------------------------------------------
# sname=input(" Enter the name of student in SMEC  for upadtion :  ")
# myquery = { "name":sname}
# mydoc = mycln.find(myquery)
#
# for x in mydoc:
#     print(x)
#     print("enter the details you want to update")
#
#     try:
#         uname = input('\nEnter  new name to update')
#         utime = input('\nEnter time to update')
#         udurn = input('\nEnter duration to update')
#         ucourse= input("\n Enter the course")
#
#         mycln.update_one(
#             {"name": sname},
#             {
#                 "$set": {
#                     "name": uname,
#                     "duration": udurn,
#                     "time": utime,
#                     "course": ucourse
#                 }
#             }
#         )
#         print("\nRecords updated successfully\n")
#        # print "cln" after the update:
#     except Exception:
#         print(str("error"))
# # # ----------------------------------delete cln based on name-----------------------------
#
# dname = input('\nEnter name to delete\n')
# mycln.delete_one({"name":dname})
#
# print ("Deletion successful")

# ----------------------------search based on course name-------------------------------------------------
# print all documents in the collection based on course name
searchCourse=input("Enter the course name for seraching : ")
check={"course":searchCourse}
mydoc=mycln.find(check) # in  will return inserted id


# print(mydoc.)
for i in  mydoc:
    print(i)
#-----------------------------------------------------------------
# mydb.mycln.aggregate([
#   {
#     $match: { "course": searchCourse }
#   },
#   {
#     $count: "total no of studens "
#   }
# ])

# ------------------------------------------------------------