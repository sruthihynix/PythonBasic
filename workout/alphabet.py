x='apple'
print(x.upper())
y='ApPLE'
print(y.lower())
print(x.islower())
print(y.isupper())

print('apple'.islower()) #This should output: True
print(y.isupper())#This should output: false

x=(1,2,3,4,5)[2:4] # string slicing
print(x)

a=[7,6,8,5,9][2:]
print(a)

b=[7,6,8,5,9][:2]
print(b)

print('apple'.isalnum())
print('apple'.isalpha())
print('apple'.capitalize())
print(type(str.capitalize)) #o check the type of str.capitalize, you can use the type() function.

# ------Joining a List of Strings
nums=['one','two','three','four','five','six','seven']
s=' '.join(nums)
print(s)
