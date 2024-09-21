class student:
    school = "SNHSS OKKAL"

    def __init__(self, rollNo,name,div,teacher):
        self.rollNo=rollNo
        self.name=name
        self.div=div
        self.teacher=teacher

#------------ instance or object method-------------

    def display_student_details(self):
        print(f"Name:{self.name}\n rollno:{self.rollNo} "
              f"\ndivision:{self.div}\n teacher:{self.teacher}\n "
              f"schoolName:{student.school}")

#     def set_marks(self,phy,maths,che,english): #mutators
#         self.maths=maths
#         self.phy=phy
#         self.eng=english
#         self.che=che
#     def getAverage(self):
#         return (self.che+self.eng+self.maths+self.phy)
#
# s1=student(1,"anjali","a","manu") #object s1--constructor calling
# s1.display_student_details()#
# s1.set_marks(97,67,90,67)
# # s1.getAverage()
# # print("average marks:", s1.getAverage ())

#------------------class method--------
    @classmethod
#     def get_school(cls):
#         print("school name:",cls.school)
# student.get_school()

#---------------static method-------------
    @staticmethod
    def about_us():
        print("this school is the best school")
student.about_us()
