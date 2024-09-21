def fact(f):
    if f==0:
        return 1
    else :
        ans=f*fact(f-1)
        return ans
        # print(ans)


n=int(input('enter the number to find factorial'))

fact(n)
print('factorial is : ',fact(n))