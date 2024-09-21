def addition(x, y):
    return x + y

def subtraction(x, y):
    print(x-y)
    # return x - y
def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero is not possible."

while True:
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result is: {addition(num1, num2)}")
            # print(addition(num1, num2))
        elif choice == '2':
            subtraction(num1,num2)
            # print(f"The result is: {subtraction(num1, num2)}")

        elif choice == '3':
            print(f"The result is: {multiplication(num1, num2)}")
        elif choice == '4':
            print(f"The result is: {division(num1, num2)}")
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid Input, please try again.")
