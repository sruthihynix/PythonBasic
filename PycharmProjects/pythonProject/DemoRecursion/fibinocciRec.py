# ------------------------fibinocci using recursion
def fib(n):
    if (n <= 1):
        return n
    else:
        return (fib(n - 1) + fib(n - 2))


n = int(input("Enter number of terms:"))
print("Fibonacci serires:")
for i in range(n):
    print(fib(i), end="")

