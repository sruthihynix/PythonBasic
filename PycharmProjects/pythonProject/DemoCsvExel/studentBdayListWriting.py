import csv # importhing csv module

f = open("studentBday.csv",'w',newline='\n') # in to file object 'f' open a file named studentBday in write mode

dw=csv.writer(f)    # using a writer object 'dw' writes datas into opened file object 'f'
# here a list named stList datas are given to write into the file
stList=[['NAME','CLASS','BIRTHDAY MONTH'],['Alan','10','March'],['John','9','April'],['Raj','11','January']]

# for i in stList:    # datas are witten in row by row  using for-loopDemo
#     dw.writerow(i)  #writerow() function to write data into the row
dw.writerows(f)