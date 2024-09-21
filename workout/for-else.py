numbers = [2, 4, 6, 8, 10]

for number in numbers:
    if number == 7:
        print("Found 7!")
        break
else:
    print("7 not found in the list.")
    # In Python, the for-else loop is a special construct that allows you to execute a block of code
    # if the loop completes its iterations without encountering a break statement.
    # This can be useful when you want to determine
    # whether a loop ran to completion without being interrupted.
    # ---------------------
    # The else block is executed only if the for loop completes all its iterations -
    # without hitting a break statement.
    # If the loop is interrupted by a break, the else block is skipped.

    #
# The else block in a for-else loop runs if the loop was not terminated by a break.