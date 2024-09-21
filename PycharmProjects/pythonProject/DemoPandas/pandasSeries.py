import pandas as pd # import panda to the variable pd
# create a sreirs from list
s1= pd.Series(['mini', 'mohan','meera'])
print(s1)
print(s1[0])
# ----------------------------------------------
import numpy as np #
# numpy is an arrey
# create a series from numpy arrey
s2=pd.Series(np.random.randn( 5))
print(s2)
s3=pd.Series(np.random.randn(6),index=['a','b','c', 'd,','e','f'])
print(s3)
print(s3['a'])# index a

# --------------------------------
# create a series from dictionary
d={'a':1,'b':2,'c':3}
s4=pd.Series(d)
print(s4)
print(s4['a'])
# giving custom index
ss4=pd.Series(d,index=['a','b','f'])# here f is not given in the dictionary so value of f get as NaN
print(ss4)

# --------------------------------------
#giving  a scalar value (here 10) to index
s5=pd.Series(10,index=['a','b', 'c', 'd'])
print(s5)


