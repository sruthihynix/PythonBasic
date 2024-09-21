class car: # class classname:
    def __init__(self, modelname, year):
        self.modelname = modelname
        self.year = year
# __init__method in Python is used to initialize objects of a class. It is also called a constructor.
#self represents the instance of class. This handy keyword allows you to access variables, attributes, and methods of a defined class in Python
    def display(self):
        print(self.modelname, self.year)


c1 = car("Toyota", 2016)
c2=car("innova",2024)
c1.display()
c2.display()