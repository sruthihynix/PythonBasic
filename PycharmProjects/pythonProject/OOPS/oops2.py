class car :
    company="bmw"
    model="ms"
    price="1.2rore"
    year=2010
    color="black"

    def display_details(self): #method or function
        print("details")

a=car()# create object a
print(type(a))
# accessing class variables with class name...
#class_name.variabla name

print(car.color,car.company, car.year)
