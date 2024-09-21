import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb=myclient["SMEC"]
mycln=mydb["batch"]
# ---------------------------------------------------------------------------------------
def statusCheck():
    check= input("enter  the student Id")
    # find()
    pass

def add():

    name=input("Enter student Name :")
    course=input("Enter the course Name :")
    duration=input("Enter the  course  duration :")
    time=input("Enter the time :")

    mydoc = { "name": name, "course": course, "dutation":duration,"time":time }

    x = mycln.insert_one(mydoc)
    print(x)

# ------------------------------------------------------------------------------------
def deletion():

    dname = input('\nEnter name to delete\n')
    mycln.delete_one({"name":dname})
    print ("'\nDeletion successful\n'")

    # pass
#mycol.delete_one(myquery)
# -----------------------------------------------------------------------------------
def update():
    sname = input(" enter the name of student in SMEC :  ")
    myquery = { "name":sname}
    mydoc = mycln.find(myquery)

    for x in mydoc:
        print(x)
        print("enter the details you want to update")

        try:
            uname = input('\nEnter  new name to update')
            utime = input('\nEnter time to update')
            udurn = input('\nEnter duration to update')
            ucourse= input("\n Enter the course")

            mycln.update_one(
                {"name": sname},
                {
                    "$set": {
                        "name": uname,
                        "duration": udurn,
                        "time": utime,
                        "course": ucourse
                    }
                }
            )
            print("\nRecords updated successfully\n")
           # print "cln" after the update:
        except Exception:
            print(str("error"))
    # pass
# mycol.update_one(myquery, newvalues)
#-----------------------------------------------------------------------------------------
def search():
    # ----------------------------search baseed on course name-------------------------------------------------
    # print all documents in the collection based on course name
    searchCourse = input("Enter the course name : ")
    check = {"course": searchCourse}
    mydoc = mycln.find(check)  # in x will return inserted id
    for i in mydoc:
        print(i)
    # mydoc = mycol.find(myquery)
    pass
# -----------------------------------------------------------------------------------------
while True:
    print("Welcome...")
    print("""
    1.Status
    2.Add Student
    3.Remove Student
    4.Update    
    5.Search
        """)
    choice = input("Enter your choice :")
    if choice==1:
       statusCheck()
    elif choice==2:
        add()
    elif choice==3:
        deletion()
    elif choice==4:
        update()
    elif choice==5:
        search()

