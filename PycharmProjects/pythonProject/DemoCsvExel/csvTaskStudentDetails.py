import csv

f=open("StudentDetails.csv","w",newline='\n')

dw=csv.writer(f)
stList=['NAME','CLASS','DATE OF ADMISSION']
dw.writerow(stList)

while True:
    name=input('Enter Name : ')
    clas=input('Enter Class : ')
    d=input('Enter the month Admission')
    stList=[name,clas,d]    # add details to list
    dw.writerow(stList)     # write the details in the stlist to the file row by row

    x=input('Add more records (Y/N)') # exit condition if y\Y while loopDemo continue,if n|N while loopDemo breaks
    if x!='Y' and x!='y' :
        break
f.close()

f=open("StudentDetails.csv")# onen StudentDetails.csv to read the data in the xl file
dr=csv.reader(f)    #read the records  from the csv file
for i in dr:        # printing all the records in the file
    print(i)




