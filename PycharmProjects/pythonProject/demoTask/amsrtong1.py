
def amsrtong(n):
    sum=0
    ams=n
    while n>0:
        x=n%10
        # y=x*x*x
        sum=sum+(x*x*x)
        n=n//10

    print(sum)
    if sum==ams:
        print('Its a AMSTRONG NUMBER')
    else:
        print('not')

num=int(input('number'))
amsrtong(num)

#
# 153 is an Armstrong number because:
#1*1*1+5*5*5+3*3*3
#  =1+125+27=153