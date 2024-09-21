
#one Class object as variable in another class((codigo class 57part))

class company:
    def __init__(self,name,loc,manager):
        self.c_name=name
        self.c_loc=loc
        self.manager=manager

class Employee:
    def __init__(self,name,id,age,comp:company):#
        self.name=name
        self.id=id
        self.age=age
        self.company=comp   # object of other class
            #actually this company is an object of another class (company)

    def show_details(self):
        print(f"Name:{self.name }")
        print(f" Name of the company:{self.company.c_name}")

c_obj=company("ABCD",'kochi',"kuttan")
# passing c_obj to e1
e1=Employee("sruthi",101,34,c_obj)  # class object as variable in another class
e1.show_details()