import openpyxl
from openpyxl import Workbook
from openpyxl.styles import cell_style
wb=Workbook()
# wb['sheet']="Report"
sh1=wb.active
print(wb.active)
sh1['A1'].value='name'
sh1['B1'].value='status'
sh1['a2'].value='python'
sh1['b2'].value='Active'
sh1['A3'].value='Java'
sh1['B3'].value='Active'

wb.save('StatusReport.xlsx')

