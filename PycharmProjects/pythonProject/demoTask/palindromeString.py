# str=input("enter a string You want to check")
# dup=str
# n=len(str)
# x=int(n/2)
# for i in range (x):
#
#     if str[i]==str[n-1]:
#         print(" palindrome")
#         break
#     else:
#         print("not palindrome")

# s='malayalam'
# q=s[::-1] #string slicing
# print(s)
# print(q)

#---------------------- chking palindrome using function
def pal(s):
    #str = input('Enter the string you want to chek : ')

    chk = s.lower()     # convet the entered string to lower case fo checking
    str1 = chk[::-1]    #------string slicing to get reverse of the string 
    if chk == str1:
        print(f'{s} Is PALINDROME')
    else:
        print('Not PALINDROME')

p=input('Enter the string you want to chek : ')
pal(p)



