import random
import string
# pwd="abcd1234ABCD!@#$"
# l=int(input('enter the length pf pwd : '))
# a="".join(random.sample(pwd,l))
# print('pwd = ',a)
# a=random.randrange(5)
# print(a)
# -------------------------------------------
# x=random.random()
# print(x)
#--------------------------------------------
# y=random.uniform(2,3)
# print(y)
# --------------------------------------------
# pl=('c','c++','python','java','vb.net')
# x=random.choice(pl)
# print(x)
#----------------------------------------
# l=['c','c++','python','java','vb.net']
# x=random.shuffle(l)
# print(pl)
# ------------------------------------------
length=int(input('Enter the length of the password'))
a=string.ascii_letters
d=string.digits
p=string.punctuation
char=a+d+p

# pwd="".join(random.sample(char,length))
# print("pwd=: ", pwd)
password="".join(random.sample(char,length)) #---- join fun , sample fun
print("Password : "+password)

# for i in range(length):
#     x="".join(random.choice(char))
#     print(x)
