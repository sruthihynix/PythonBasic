import openpyxl # import module

wb = openpyxl.Workbook()    # call workbook()function of open openpyxel to create a new blank workbook object wb
sheet = wb.active   # to get wb workbook active using the 'active' attribute

sheet['A1'] = 100   # writing to the cell of an xel sheet
sheet['A2'] = 150
sheet['A3'] = 200
sheet['A4'] = 250

sheet['A6'] = '= SUM(A1:A5)'    # calculations
wb.save('Sum1.xlsx')    # to save the file with name sum1.xlsx