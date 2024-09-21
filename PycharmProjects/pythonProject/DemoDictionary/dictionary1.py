empsalaary={'appu':12000, 'achu':15000, 'sruthi':50000,'vihu':45000,'brand': 'bmw'}

print(empsalaary["sruthi"]) # to print vallue of sruthi
print(empsalaary)

empsalaary['vinod']=10000 #to add the value of 'vinod': 10000 to the dictionary
print(empsalaary)

empsalaary.__setitem__('sruthi',100000)# to change the value  or update the value of sruthi to 100000
print(empsalaary)

empsalaary.__setitem__('deep',0)# to add new key deep and value 0 to the dictionary
print(empsalaary)

empsalaary['brand']= 'benz'# adding new key brand to the dictionary nd value benz
print(empsalaary)

empsalaary.clear()# clear all the key and values from the dictionary
print(empsalaary)
