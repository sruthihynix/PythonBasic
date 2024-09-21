n=int(input("enter no"))
if n>1:
    for i in range(2,n):
        if (n%i)==0:
            print(f"{n}, is not prime")
            break
    else:
        print(f"{n}, prime")
else:
    print("not")