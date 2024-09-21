
n=int(input("enter no: "))
i=2
x=n/2 # we need to check upto n/2
# print(x)
while (i<=x):
    if n%i==0:
        print(" not prime")
        break
    i+=1
else :
    print("prime")
print("--------------------------------------")
# ======================================2.
n=int(input("enter the number"))
for i in range(2,n):
    if n%i==0:
        print('not a prime number')
        break
else:
    print(f"{n},is a prime Number")
