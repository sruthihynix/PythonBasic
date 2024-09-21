# import re# module re import
# flag=0
# p=input("enter a passwrod")
#
# if not re.search('[a-z]',p):
#     # print('lower case letter missing')
#     flag=1
# if not re.search('[0-9]',p):
#     flag=1
# if not re.search('[A-Z]',p):
#     flag=1
# if not re.search('[!@#$%]',p):
#     flag=1
# if len(p)<4:# length of password
#     flag=1
# if flag==0:
#     print("valid password")
# else:
#     print('invalid')

# ----------------------------------------------------------

# ((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{6,20})
# regular expression to say the password is strong.
# ------------------------------------------------------------
# import re
# v=input("Enter the password:")
# if(len(v)>=8):
#     if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,30})',v))==True):
#         print("The password is strong")
#     elif(bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{8,30})',v))==True):
#         print("The password is weak")
# else:
#     print("You have entered an invalid password.")
# ------------------------------------------------------------------------
import re
# p=input('enter a PWD')
# if len(p)>=6:
#     if (re.match('(?=.*\d)',p))==1):
#         print('no present')
#     else:
#         print('NOt')


