
print("select your choice")
print("1.ADD\n 2.Sub\n3.Mul\n4.div")
choice = int(input())
if choice==1:
    n1=input("enter 1st no:")
    n2=input("enter 2nd no:")
    ans=int(n1)+int(n2)
    print("answer:",ans)
elif choice==2:
    n1=int(input("enter 1st no:"))
    n2=int(input("enter 2nd no:"))
    ans=n1-n2
    print("answer:",ans)
elif choice==3:

    n1 = int(input("enter 1st no:"))
    n2 = int(input("enter 2nd no:"))
    ans = n1 * n2
    print("answer:",ans)
elif choice==4:

    n1 = int(input("enter 1st no:"))
    n2 = int(input("enter 2nd no:"))
    ans=n1/n2
    print("answer:",ans)
else :
    print("invalid input")

