# star pattern 1
limit =int(input("enter the number "))
#limit=5
i=1
while i <=limit:
    k=1
    while k<=(limit-i):
        print(" ",end="")
        k=k+1
    j=1
    while j<=i:
        print(j,end=" ")
        j=j+1
    print()
    i=i+1
