list=[50,53,500,5,96,100]
x=int(input("enter the number you want to check in the list"))
for i in list:
    if x==i:
        print("the number is in the list")
        print (i)
        break
else :
    print("the number you entered is  not exist in the list")
# print(len(list))
# print(list[4:])
# print(list[0:5:2]) # print list alternate values# gap `2
# print(list[::3])
# print(list[::-1])# reverse indexing -1///////////// important