# star pattern 2
limit=10
i=1
while i<=limit:             # outer loopDemo for line printig
    k=1
    while k<=(limit -i):    # first innerloop for space print
        print(" ",end="")
        k=k+1
    j=1
    while j<=i:             # 2nd innerloop for * printing
        print("*",end=" ")
        j=j+1
    print()
    i=i+1
