abc=(32,1990,"sruthi", "vinod")
print(type(abc))
print(len(abc))
print(abc[2])
print("using for loopDemo")
for i in abc:
    print(i)
print(abc.count("sruthi"))

print("USING WHILE LOOP")
j=0
size=len(abc)
while j<size:
    print(abc[j])
    j=j+1

print('empty tuple creating')
t1=()

print('tuple with sigle value')
t2=(1000,)
print(t2)





