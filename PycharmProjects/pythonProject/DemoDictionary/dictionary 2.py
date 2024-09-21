dict1={'name': 'sruthi', "age":"32", 'salary': "50,000","place": "kalady" }
dict2={"fruit": "apple", 'colour': 'red'}
print(len(dict1))
print(len(dict2))
print(str(dict1))
print(dict1.items())

print(dict1.keys()) #print(dict1(values()))

x=dict1.get('name')# to get value of key name to x
print(x)

y=dict1.keys()# to get the list of keys
print(y)

dict1.update({"salary":00})
print(dict1)