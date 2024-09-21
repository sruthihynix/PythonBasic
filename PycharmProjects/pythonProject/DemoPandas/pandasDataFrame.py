import pandas as pd

# -------creating  Data frame from dictionary
student={'Name':['Jin', 'Min', 'Tin'],
         'Age':[12,13,14],
         'place':['Chennai','Cochin','Banglore']}
# -----------

# --- keys in the dictionary-> 'Name,Age,Place' are the coloumn names of the table
df1=pd.DataFrame(student)
print(df1)
# ---------------------- other funs

print(df1['Age'].min())
print(df1['Age'].max())
print(df1['Age'].count())
print(df1['Age'].idxmax())
print(df1['Age'].idxmin())


#-------- adding custom index to df2
df2=pd.DataFrame(student,index=['s1','s2','s3'])
print(df2)

# -----to get coloumns names only
print(df1.columns)

# ---------------- replacce place with city
df1.columns=['Name','Age','City']
print(df1)

# ----------------to print name column only
print(df1['Name'])

# -------------to print the type of column-> series
print(type(df1['Age']))

# ---------------to print the type of df1-> dataframe
print(type(df1))

# -----------------making data frame from dictioneries ( two dictionaries)
df3=[{'a':1,'b':2,'c':3},{'a':100,'b':200}]# dictionary list
df3=pd.DataFrame(df3)
print(df3)# if one key value is not given then it take as none

# -----------------------------------
# reading tabular data from external sources
# -----------------------------------
xx=pd.read_excel("data.xlsx") # pd.read-'exel/csv/...'('file name')| note that,--
# the file must be present in the same folder
print("------the external tabular data-----")
print(xx)
print("-----first 5 rows-----")
print(xx.head(5))
print('-----last 4 rows-----')
print(xx.tail(4))
# -----------to get a description of tabular dataframe using describe()
print(xx.describe())

print(xx.info())

print(xx.shape)# to get no of of rows and columns
print(xx.shape[0])# to get row no
print(xx.shape[1])#to  get column no
print(xx.columns)# to get the column names
print(xx.index)# to get indexing




