# star pattern 2
limit=5
i=1
while i<=limit:             # outer loopDemo for line printig
    k=1
    while k<=(limit -i):    # first innerloop for space print
        print(" ",end="") # same line il thanne printing nadakkanayit anu engane end="" kodukunath
        k=k+1
    j=1
    while j<=i:             # 2nd innerloop for * printing
        print(j,end=" ")
        j=j+1
    print()
    i=i+1
