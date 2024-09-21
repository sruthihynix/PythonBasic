# n=29
# i=2
# x=n/2
# while i<x:
#
#     if n%i==0:
#         print("not prime")
#         break
#     i+=1
# else:
#     print("prime")
#----------------------------------------PN using for  else loopDemo
n=int(input("enter the number"))
for i in range(2,n):
    if n%i==0:
        print('not a primenumber')
        break
else:
    print('prime NUmber')

