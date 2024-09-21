
while 1: #this conditiom will always true
    x=int(input("no1"))
    y=int(input("no2"))
    print("1.ADD \n 2.SUB \n 3.MUL \n 4.DIV")
    a=int(input("enter your choice"))
    if a==1:
        print(x+y)
    elif a==2:
        print(x-y)
    elif a==3:
        print(x*y)
    elif a==4:
        print(x/y)

    elif a==int("hh"): #
        break
else:
        print('invalid') 
