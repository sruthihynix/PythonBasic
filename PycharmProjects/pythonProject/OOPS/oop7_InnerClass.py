        # inner class# codigi class 58

class Employee:
    class company: # inner class or member class of clas employee
        def __init__(self,name, loc, manager):
            self.c_name = name
            self.c_loc = loc
            self.manager = manager

    def __init__(self,name,id,age,c_name,c_loc,c_dir):# init method of employee
        self.name=name
        self.id=id
        self.age=age
        self.company=Employee.company(c_name,c_loc,c_dir) # object is created inside the init fun of employee class

    def show_details(self):
        print(f"Name:{self.name }")
        print(f" Name of the company:{self.company.c_name}")

c_obj= Employee.company("ABCD",'kochi',"ROCKYf")
# passing c_obj to e1
e1=Employee("sruthi","kochi","rocky")  # class object as variable in another class
e1.show_details()