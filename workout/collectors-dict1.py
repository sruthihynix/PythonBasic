
my_dict = {
    'name': 'Alice',
    'age': 25,
    'courses': ['Math', 'Physics']
}
print(my_dict['name'])
print(my_dict['age'])
print(my_dict['courses'])

# Using the dict() function
my_dict = dict(name='Alice', age=25, courses=['Math', 'Physics'])

my_dict['address'] = '123 Main St'  # Adding a new key-value pair

my_dict['age'] = 26  # Updating an existing value
print(my_dict)

del my_dict['age']  # Removes the key 'age' and its associated value
print(my_dict)

address = my_dict.pop('address')  # Removes and returns the value of 'address'
print(my_dict)
x=my_dict.keys()
print(x)
y=my_dict.values()
print(y)
z=my_dict.items()
print(z)

my_dict.update({'age':30})#---------------------update
print(my_dict)
