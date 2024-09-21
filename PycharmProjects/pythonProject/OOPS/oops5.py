 # collection of items as instance variable-------------list []

class student:

    def __init__(self,name,rollno,age,marks:list):
         self.name=name
         self.rollno=rollno
         self. age= age
         self.marks=marks
    def display_details(self):
        print(f"name:{self.name}")
    def percentage(self):
        total=0
        for i in self.marks:
            total=total+i
            p=total*.25
        print("percentage of marks:",p)

s1=student("vihaan",23,10,[90,94,98,85])
s1.display_details()
s1.percentage()
