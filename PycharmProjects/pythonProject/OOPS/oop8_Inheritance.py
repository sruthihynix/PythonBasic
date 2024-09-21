# inheritance codigo part 59
#all properties of parent belongs to child

#parent class or superclass
# child class or subclass

class vehicle:#PARENT
    def __init__(self,company,model,color,engine,fuel):
        self.company=company
        self.model=model
        self.color=color
        self.engine=engine
        self.fuel=fuel
    def start_engine(self):
        print("starting")
    def change_gear(self):
        print("Engine")
class car(vehicle):#CHILD OF PARENT VEHICLE
     def open_sunroof(self):
         print("opening engine")

c=car("bmw","x5","black","2000cc", "desial") # c is the object of class car// child class
c.start_engine()



