# The break statement in Python is used to exit a loop prematurely,
# that is, before the loop has iterated over all its items.
# When break is encountered inside a loop, the loop stops immediately,
# and control is transferred to the first statement following the loop.
# 1
# In this case, the loop will continue indefinitely until the user types "quit",
# at which point the break statement exits the loop.
print("example 1")
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        print("sucessfully exited")
        break
# 2
# In this example, the loop stops when number equals 5, so numbers 5 through 9 are not printed.
print("example 2")
for number in range(10):
    if number == 5:
        break
    print(number)