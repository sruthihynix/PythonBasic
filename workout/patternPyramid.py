n = 5  # Number of rows
i = 1
while i <= n:
    # Print leading spaces
    spaces = n - i
    while spaces > 0:
        print(" ", end="")
        spaces -= 1
    # Print # symbols
    j = 1
    while j <= (2 * i - 1):
        print("*", end="")
        j += 1
    print()  # Move to the next line after each row is printed
    i += 1
