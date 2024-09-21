
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

# num=int(input('enter a number'))#user input
# palNo(num)#calling fun palno


#---------------------- chking palindrome using function
def pal(s):
    #str = input('Enter the string you want to chek : ')
    chk = s.lower()     # convet the entered string to lower case fo checking
    str1 = chk[::-1]    #------string slicing to get reverse of the string
    if chk == str1:
        print(s, '- Is PALINDROME')
    else:
        print('Not PALINDROME')

# p=input('Enter the string you want to chek : ')----user input
#  pal(p)

x= int(input("PALINDROME\n 1.NUMBER\n 2.SRTING \n Enter Your Choice :" ))

if x==1:
    num = int(input('enter a number'))  # user input
    palNo(num)  # calling fun palno
elif (x==2):
    p = input('Enter the string you want to chek : ')
    pal(p)
else:
    print("invalid input")



