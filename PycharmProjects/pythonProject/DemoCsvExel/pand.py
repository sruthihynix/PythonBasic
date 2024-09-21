import pandas as pd

df = pd.read_excel('student_file.xlsx')


choice=input("enter the choice")
if choice=="pass":
   df =df[(df['Status']=='pass')]
   print(df)
elif choice=="fail":
   f = df[(df['Status'] == 'fail')]
   print(f)
else:
   print("enter correct choice")