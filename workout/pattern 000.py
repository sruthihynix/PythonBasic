

print("***********")
# trick 1
print("*"*10)
print("pattern 1")
for i in range(6):
    print("*" * i)

print("pattern 2")
for i in range(6,0,-1):
     print("*" * i)
print("pattern 3")

n=6
for i in range(1,n+1):
    print(""*(n-i) + "$" * i)

print("pattern4 ")
n=4
for i in range(n):
    print(" " * (n-i) + "*" * ((2*i)+1))


n=4
for i in range(n,-1,-1):
    print(" " * (n-i) + "*" * ((2*i)+1))
