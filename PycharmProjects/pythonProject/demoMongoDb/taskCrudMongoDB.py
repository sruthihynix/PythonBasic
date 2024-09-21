# PTYHON PROGRAM TO PERFORM CRUD OPERATIONS CONNECTING TO MONGODB

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb=myclient["smec2023"]
mycln=mydb["batch"]

# ------------------------------------------------------------------
def add():
    name=input("Enter student Name :")
    course=input("Enter the course Name :")
    duration=input("Enter the  course  duration :")
    time=input("Enter the time :")

    mydoc = { "name": name, "course": course, "dutation":duration,"time":time }

    x = mycln.insert_one(mydoc)
    print("student added successfully ")
    print(x)
# ------------------------------------------------------------------------
def remove():
    dname = input('\nEnter name to delete : ')
    mycln.delete_one({"name":dname})
    print ("Deletion successful")
#------------------------------------------------------------------------
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
#---------------------------------------------------------------------------

def search():
    # ----------------------------search baseed on course name---------------
    # print all documents in the collection based on course name
    searchCourse = input("Enter the course name : ")
    check = {"course": searchCourse}
    mydoc = mycln.find(check)  # in x will return inserted id
    for i in mydoc:
        print(i)
# --------------------------------------------------------------------
print('--------WELCOME TO SMEC--------')
while True:
    print("""
    1.Add Student
    2.Remove Student
    3.Update Student Details
    4.Search course
        """)

    choice=int(input("Enter your Choice : "))

    if choice==1:
        add()
    elif choice==2:
        remove()
    elif choice==3:
        update()
    elif choice==4:
        search()
    else:
        print('----THANK YOU-----')
        break
