# x=234
# # print(x%10)
# # print(x//10)
n=int(input('enter a number'))  # n->242
rev=0                           #rev=0
pal=n                           # pal=242-----keep a duplicate of n for final checking
while n>0:
    rev= rev*10+n%10    # rev=->0->2->24->242
    n=n//10             # n= 24-> 2->0

if rev != pal:
    print('not a palindrome no')
else:
     print('it is palindrome')
#2%10=2
