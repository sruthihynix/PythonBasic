class school:
    def school_info(self,sname,locn):
        self.school_name=sname
        self.loction=locn
        print('School NAme:', sname, 'Location:', locn)

class teacher:
    def teacher_Reg(self,tname,sub,mobNo):
        self.t_name=tname
        self.subject=sub
        self.mob=mobNo
        print('Teacher NAme:',tname, 'Subject:',sub,"mobile:",mobNo)

class student(teacher,school):
    def student_Reg(self,stname,no,div,age):
        self.studentName=stname
        self.admn_no=no
        self.division=div
        self.age=age
        print('Student Name:',stname, 'Admission NO:',no,'div:',div,'Age:',age)
        print("SUCCESSFULLY REGISTERED")

stname=input("Enter the name of student:")
no=input("Admission No:")
age=input("age:")
div=input("Division:")

obj1=student()
obj1.school_info("SH","Kochi")
obj1.teacher_Reg("Tom","IT",9098329293)
obj1.student_Reg(stname,no,div,age)
#





# def get_info():
    # stname=input("Enter the name of student:")
    # no=input("Admission No:")
    # age=input("age:")
    # div=input("Division:")


