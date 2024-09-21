car=('swift','inova','benz','bmw','aveo','kia',122) # tuple car
print(type(car))
print(car)
print(car[2])
vehicle=list(car) # tuple car is changed to list vehicle
print(type(vehicle))
x=tuple(vehicle)# list converted to tuple
print(type(x))
#  tuple is not changable once its created--

#----------- tuple unpaking
t=(10,34,25,100)
a,b,c,d=t # we can assign values from tuple to variables like this this is called tuple unpaking
print(a)
print(d)
print()