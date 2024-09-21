from openpyxl import Workbook

wb = Workbook()
sheet= wb.active

sheet['A1']= 'Name'
sheet['B1']= 'Class'
sheet['C1']= 'Grade'
n=int(input('Enter the number of students :'))
for i in range(1,n+1):
    sheet['A'+str(i+1)]= input("Enter name")

wb.save('std1.xlsx')


