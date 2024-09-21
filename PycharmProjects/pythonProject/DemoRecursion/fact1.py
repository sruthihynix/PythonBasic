# def fact(n):
#     if (n>0):
#         result = n*fact(n-1)
#         print(result)
#     else:
#         result=1
#         return result
# print("your answer is :")
# fact(3)
#
def fact(n):
    if n > 0:
        result = n * fact(n - 1)
        return result  # Return the result of the multiplication
    else:
        return 1  # Base case: return 1 when n is 0 or negative

print("Your answer is:", fact(3))  # Call the function and print the final result