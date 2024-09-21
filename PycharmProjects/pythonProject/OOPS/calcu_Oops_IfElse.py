
class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self,a,b):
        return self.a+self.b

    def sub(self,a,b):
        return self.a - self.b

    def mul(self,a,b):
        return self.a * self.b

    def div(self,a,b):
        return self.a // self.b

a=int(input("No 1:"))
b=int(input("No 2:"))
obj=calculator(a,b)

#--------------------------------------------

print("1.ADD\n 2.Sub\n3.Mul\n4.div")
print("Select your choice:")
choice = int(input())
if choice==1:
    print("ANSWER:",obj.add(obj.a,obj.b))

elif choice==2:
    print("ANSWER:",obj.sub(obj.a, obj.b))

elif choice==3:
    print("ANSWER:",obj.mul(obj.a, obj.b))

elif choice==4:
    print("ANSWER:",obj.div(obj.a, obj.b))
else :
    print("invalid input")