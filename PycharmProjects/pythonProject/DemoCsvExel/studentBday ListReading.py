import csv

f=open('studentBday.csv','r')

dr= csv.reader(f)
for i in dr:
    print(i)