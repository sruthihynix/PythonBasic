# -- fuction passing parameters
def addTwo(num1,num2):
    total=num1+num2
    return total # return is used to return a value to the called function
#-------functon call
# s=addTwo(10,50) #----- here the value in variable "total" returned to the variable s
# print(s)

# print('sum = ',addTwo(100,20)) # calling function inside print/
# print('sun = ', addTwo(1000,50)) # second time calling of fun

#-------- function without input but with return value
def getPie():
    return 3.14

print(getPie())
