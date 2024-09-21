n=25
end=int(n/2)+1
for i in range(2,end):
 if n%i==0:
    print("its not prime")
    break
#else:
#    print("its prime")
