#---------------------------- dictionary-------
class student:

    def __init__(self,name,rollno,age,marks:dict):
         self.name=name
         self.rollno=rollno
         self. age= age
         self.marks=marks
    def display_details(self):
        print(f"name:{self.name}")
    def percentage(self):
        total=0
        for i in self.marks.values():# key.value
            total=total+i
            p=total*.25
        print("percentage of marks:",p)

s1=student("vihaan",23,10,{"phy":75,"chem":90,"maths":100,"english": 99})# dictionary { "key":value}
s1.display_details()
s1.percentage()
