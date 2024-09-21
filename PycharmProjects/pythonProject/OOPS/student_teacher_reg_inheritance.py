
class school:
    def school_info(self,sname,locn):
        self.school_name=sname
        self.loction=locn
        print('School Name:', sname, 'Location:', locn)

class teacher(school):
    def teacher_Reg(self,tname,sub,mobNo):
        self.t_name=tname
        self.subject=sub
        self.mob=mobNo
        print('Teacher Name:',tname, 'Subject:', sub, 'Mobile NO:', mobNo)

#--------------------------------------------------
class student(teacher,school):
    def student_Reg(self,stname,no,div,age):
        self.admn_no=no
        self.division=div
        self.age=age
        print('Student Name:',stname, 'Admission NO:',no,'div:',div,'Age:',age)
        #
#--------------------------------------------------------------------
obj1=student()
while 1: #this conditiom will always true

    print("1.Teacher \n 2.Student ")
    a=int(input("enter your choice:"))
    if a==1:
        tname = input("Enter the name of Teacher:")
        sub = input("Subject:")
        mobNo = input("Mobile No:")
        print("SUCCESSFULLY REGISTERED")

        obj1.school_info("SH", "Kochi")
        obj1.teacher_Reg(tname,sub,mobNo)
    elif a==2:
        stname = input("Enter the name of student:")
        no = input("Admission No:")
        age = input("age:")
        div = input("Division:")
        print("SUCCESSFULLY REGISTERED")
        obj1.school_info("SH", "Kochi")
        obj1.student_Reg(stname,no,div,age)
    elif a==int("hh"): #
        break
else:
        print("invalid")



# obj1.teacher_Reg("Tom","IT",9098329293)
# obj1.student_Reg("appu",123,"5E",10)
