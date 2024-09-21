from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

wb = Workbook()
sheet = wb.active

# Let's create some sample student data
rows = [
    ["Serial_no", "Roll no", "Marks"],
    [1, "0090011", 75],
    [2, "0090012", 60],
    [3, "0090013", 43],
    [4, "0090014", 97],
    [5, "0090015", 63],
    [6, "0090016", 54],
    [7, "0090017", 86],
]

for i in rows:
    sheet.append(i)

chart = BarChart()
values = Reference(worksheet=sheet,
                   min_row=1,
                   max_row=8,
                   min_col=2,
                   max_col=3)

chart.add_data(values, titles_from_data=True)
sheet.add_chart(chart, "E2")

wb.save("student_chart.xlsx")

