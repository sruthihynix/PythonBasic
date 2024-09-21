# method overriding
class A:        #parent
    def fun1(self):
        print("function1")
    def fun(self):
        print("function2 working from cls A using key word super()")
class B(A): # cls B  inherit cls A # Child
    def fun3(self):
        print("function 3")
    def fun(self):
        print("function 4 from class B")
        super().fun()# super is used to calll the function from parent class while overriding

obj=B()
obj.fun1()
# obj.fun2()
obj.fun3()
obj.fun()# here function  named (fun) is common in  both class
         # parent class function override by child fun

