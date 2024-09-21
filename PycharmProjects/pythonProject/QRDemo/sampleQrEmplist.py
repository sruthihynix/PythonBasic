import qrcode

id=input('Enter Employee ID : ')
name=input('Enter Name : ')
age=input('Enter Age : ')
salary=input('Enter Salary : ')
dep=input('Enter Department : ')
phno=input('Enter Mob No : ')
details = id+name+age+salary+dep # add all the details enterd  added to the variable 'details'
details = 'ID = '+id +'\nNAME = '+name +'\nAGE = '+age + '\nSALARY ='+salary +'\nEPARTMENT = '+dep+'\n MOb= '+phno
xx=qrcode.make(details) #---xx variable, make() fun,  details-- the data added into the qrcode
xx.save(name.img)       #---variable . save(qr filename.img)--here file name created with the name of employee
xx.png.width(20)

# f=open(name,'w')    # open a file in write mode
# f.write(details)    # write the data in variable 'details' write into the opened file
# f.close()           # close the opened file
print("--------------------Details added-------------------")



