while True:
    print(" 1. Addition\n 2. Substration\n 3. Multiplication\n 4. Division")
    choice=int(input("Enter your choice : "))
    x = int(input("No. 1:"))
    y = int(input("No. 2:"))
    if choice == 1:
        print("Answer is : ",x+y)
    elif choice == 2:
        print("Answer is : ", x - y)
    elif choice==3:
        print("Answer is : ", x * y)
    elif choice==4:
        print("Answer is : ", x / y)

    # elif choice == "XXX":
    #     break
else:
    print("Invalid Input")