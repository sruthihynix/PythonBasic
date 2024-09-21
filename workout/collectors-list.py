# list
# touple
# set
# dictionary
# list[0,1,2,3]
fruits=[]
print(type(fruits))
# append allows to add only one argument
fruits.append("apple")
print(fruits)
fruits.append("orange")
print(fruits)
fruits.append("mango")
print(fruits)
fruits.remove("apple")
print(fruits)
fruits.insert(1,"rambootan")
print(fruits)
vegitables=['onion','mango','cabbage','tomato','potato','mango',768]
print(vegitables)
vegitables.pop(0)# item in index 0  removed
print(vegitables)
vegitables.pop()# index is not specified then last item removed
print(vegitables)
del vegitables[1] # item in index 1 is deleted
print(vegitables)
shop=['onion','mango','cabbage','tomato','potato']
print(shop)
shop.clear() # clear items in shop
print(shop)
# del shop# delete list shop
# print(shop)
print(len(fruits)) # to get the lengtn of list
fruits.sort()# sort in alphabatically
print(fruits)
fruits.sort(reverse=True) #sort in decending order
print(fruits)
print(shop)
shop=fruits.copy()# copy the items in list fruits to list shop
print(shop)
market=fruits+vegitables # combine list fruits and list vegetables into new list market
print(market)

# ----------------insert in to list
list_aaa=['a1','a2','a3']
list_aaa.insert(1,'b1')
print(list_aaa)
# -----------------reverse list
list_2=[20,40,60,80]
print(list_2)
list_2.reverse()
print(list_2)

my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)  # Output: [5, 4, 3, 2, 1]

list_1=[1,2,3,4]
rev_list=list_1[::-1]
print(rev_list)

# convert list string to list integer
nums=['22','34','35','55']
x=([int(i) for i in nums])
print(type(nums[0]))
print(type(x[1]))