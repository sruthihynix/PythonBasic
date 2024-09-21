num=int(input("enter no"))
x=int(num/2)
for i in range(2,x):
    if num%i==0:
        print("not")
        break
else:
    print("prime")