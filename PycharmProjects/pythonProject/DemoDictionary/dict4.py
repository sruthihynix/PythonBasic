    # loopipng of dictionaries

dict1={'name': 'sruthi', "age":"32", 'salary': "50,000","place": "kalady" }
dict2={"fruit": "apple", 'colour': 'red'}
dict3={'food': "fried rice"}
for i in dict1:
    print(i)        # print the keys
    print(dict1[i]) # print tht key values

for x,y in dict1.items():   # print both key and value //dict-name.item()
    print(x,y)

d1=dict3.copy() # copy dictionary using copy() function // copy dict3 to d1 using copy()
print(d1)

d2=dict(dict2)  # copy dictionary using dict() function
print(d2)