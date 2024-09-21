#-------- global and Local variable--here two variable given first v=1000 this is a global variable
#------- insidse the function variable v=10 this is a lccal varible
# v=1000  # global variable
# def abc():
#     v=10    # local variable
#     print(v)    # here we get output as 10 because, there is a variable v=10 is aissgned so it give  output ac 10
# abc()   #--- calling fun abc
# --------------------------------------------------------------

count=0
def abcd():
    global count #   we declare count as a global variable because other wise there is an error
    count=count+1
    print('hai....')
    print(f"this function called {count} times")
abcd()
abcd()