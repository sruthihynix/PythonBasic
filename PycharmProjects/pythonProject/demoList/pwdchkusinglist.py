listun=["abc1","abc2",'abc3']    #u
listpwd=["p1","p12",'p123']      #index

un=input("enter  username:")
index=0
for u in listun:
    if un==u:
        pwd = input("enter password:")
        if pwd==listpwd[index]:
            #x=listun.index(un) list name.index(...) # to find the position in list
            print(index)
            print('welcome',un)
        else:
            print('password incorrect')
        break
    index=index+1
else :
    print("invalid user name")
