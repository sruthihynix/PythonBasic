

# n=int(input('enter a number'))
def palNo(n):   # defining a function PalNo to chek nois palindrome ot not
    rev=0
    pal=n
    while n>0:
        rev= rev*10+n%10
        n=n//10

    if rev != pal:  # checking the reversed no in rev is equal to  the entered number n
        print('not')
    else:
         print('it is palindrome')

num=int(input('enter a number'))#user input
palNo(num)#calling fun palno



