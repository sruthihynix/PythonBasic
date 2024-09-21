# i=0
# while(i<5):
#     print(i)
#     i+=1
i=0
n=int(input("enter the number"))
while i<n:
    i+=1
    if i==3: # skip where i=3
        continue
    print(i)
print("limit",n)