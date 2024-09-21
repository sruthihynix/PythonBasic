import io
import os   # for deleting --- use 'os' module
import pyqrcode
from pyqrcode import QRCode

def add():
    id=input('Enter Employee ID :')
    global name
    name=input('Enter Name: ')
    age=input('Enter Age')
    salary=input('Enter Salary')
    dep=input('Enter Department ')
    global details
    # details= id+name+age+salary+dep # add all the details enterd  added to the variable 'details'
    details = 'ID = '+id +'\nNAME = '+name +'\nAGE = '+age + '\nSALARY ='+salary +'\nEPARTMENT = '+dep
    f=open(name,'w')    # open a file in write mode
    f.write(details)    # write the data in variable 'details' write into the opened file
    f.close()           # close the opened file
    print("--------------------Details added-------------------")

def dele():
    d=input('Enter the Name of the file you want to delete ')
    if os.path.exists(d):   # check the file enterd exist or not
        os.remove(d)        # remove the specified file
        print('-------------file is deleted--------------')
    else:
        print('The file you entered not exist')

def read():
    x=input('Enter the name of the file to read: ')
    if os.path.exists(x):   # to check whether the file is exist or not
        print('-------------DETAILS--------------')
        y=open(x)           # open file
        print(y.read())     # read or displaly the opened file

        fp = io.open(x, mode='r', encoding='utf-8')
        audi = fp.read()
        obj = gTTS(audi, lang='en')
        obj.save('a1.mp3')
        playsound(('a1.mp3'))


    else:
        print('File you entered not exist')

def codeQR():
    x = input('Enter the name of the file to generate QR Code ')
    if os.path.exists(x):  # to check whether the file is exist or not
        y=open(x,'r')   #if file exists open that file to vatiable y in read mode
        f1=y.read()    # then f1 = file in y

        n=x+'.svg'
        xx = pyqrcode.create(f1)  # ---xx variable, make() fun, data in file f1 create the qrcode
        xx.svg(n,scale=5)
        print('-------------QR Code Generted Sucessfully--------------')
    else:
        print('File you entered not exist')

# fun to read the  employee details
from gtts import gTTS
from playsound import playsound
import io

# def playdetails():
#     pd = input('Enter the employee name : ')
#     if os.path.exists(pd):  # to check whether the file is exist or not
#         fp=io.open(pd,mode='r',encoding='utf-8')
#         audi=fp.read()
#         obj=gTTS(audi,lang='en')
#         obj.save('a1.mp3')
#         playsound(('a1.mp3'))
#         print("details playing")
#
#     else:
#         print('File you entered not exist')
# choice
while 1:

    print('EMPLOYEE DETAILS')
    print(' 1.Add File\n 2.Read File\n 3.Delete File\n 4.Generate QR Code')

    choice=int(input("Enter your choice"))
    # c = input("Enter your choice")
    # choice=int(c)
    if choice==1:
        add()

    elif choice==2:
        read()

    elif choice==3:
        dele()
    elif choice==4:
        codeQR()
    elif choice=='xxx':
        print("invalid choice....")
        break

else:
    print("Try again")
