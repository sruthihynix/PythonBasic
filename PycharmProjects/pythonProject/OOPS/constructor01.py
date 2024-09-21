class employee:
    company_name="abcd tech"
    location="calicut"
    def __init__(self,id,name,salary):#constructor
        self.emp_id=id
        self.emp_Name=name
        self.emp_sal=salary
    def get_details(self):
        print(self.emp_Name,self.emp_id)

obj1=employee(101,"appu",5000) #constructor calling
obj2=employee(102,"vichu",7000)
 
obj1.get_details()
obj2.get_details()


#print(obj1.emp_Name)

