from tkinter import *

def clickBtn(item):
    global expression
    expression = expression + str(item)
    inputValue.set(expression)

def clearButton():
    global expression
    expression = ""
    inputValue.set("")

def FunInEqualBtn():

    global expression
    result=str(eval(expression))
    inputValue.set(result)

expression=""

window=Tk()
window.geometry("350x350")
window.title("sample calculator")

inputValue=StringVar() # the value entered in the result Field // display box

# ++++++++++++++ frame for result

resultFrame=Frame(window,width=320, height=50)
resultFrame.pack(side=TOP)

resultField=Entry(resultFrame,font=('arial', 18, 'bold'),textvariable=inputValue,
                  width=50 ,bg="white",bd=2,
                  justify=CENTER)
resultField.grid(row=0,column=0)

# ++++++++++++++++++++++++++frame for buttons
buttonFrame=Frame(window,width=300,height=50,bg='grey')
buttonFrame.pack()

# ++++++++++++first row -> C &

clearBtn=Button(buttonFrame,text='C',width=int(34),height=3,command=lambda : clearButton()).grid(row=0,column=0,columnspan=3,padx=1,pady=1)

divBtn=Button(buttonFrame,text='/',width=10,height=3,command=lambda : clickBtn('/')).grid(row=0,column=3,padx=1,pady=1)

# +++++++++++++++++++++++++second row 7/8/9/*

seven=Button(buttonFrame,text='7',width=10,height=3,command=lambda : clickBtn(7)).grid(row=1,column=0,padx=1,pady=1)
eight=Button(buttonFrame,text='8',width=10,height=3,command=lambda : clickBtn(8)).grid(row=1,column=1,padx=1,pady=1)
nine=Button(buttonFrame,text='9',width=10,height=3,command=lambda : clickBtn(9)).grid(row=1,column=2,padx=1,pady=1)
multiplyBtn=Button(buttonFrame,text='*',width=10,height=3,command=lambda : clickBtn('*')).grid(row=1,column=3,padx=1,pady=1)

# +++++++++++++++++++++++++++++++third row 4/5/6/-

four=Button(buttonFrame,text='4',width=10,height=3,command=lambda : clickBtn(4)).grid(row=2,column=0,padx=1,pady=1)
five=Button(buttonFrame,text='5',width=10,height=3,command=lambda : clickBtn(5)).grid(row=2,column=1,padx=1,pady=1)
six=Button(buttonFrame,text='6',width=10,height=3,command=lambda : clickBtn(6)).grid(row=2,column=2,padx=1,pady=1)
subBtn=Button(buttonFrame,text='-',width=10,height=3,command=lambda : clickBtn('-')).grid(row=2,column=3,padx=1,pady=1)

# +++++++++++++++++++++++++++++++++fourth row 1/2/3/+

one=Button(buttonFrame,text='1',width=10,height=3,command=lambda : clickBtn(1)).grid(row=3,column=0,padx=1,pady=1)
two=Button(buttonFrame,text='2',width=10,height=3,command=lambda : clickBtn(2)).grid(row=3,column=1,padx=1,pady=1)
three=Button(buttonFrame,text='3',width=10,height=3,command=lambda : clickBtn(3)).grid(row=3,column=2,padx=1,pady=1)
plusBtn=Button(buttonFrame,text='+',width=10,height=3,command=lambda : clickBtn('+')).grid(row=3,column=3,padx=1,pady=1)

# ++++++++++++++++++++++++++++++++++++fifth row 0/./=

zero=Button(buttonFrame,text='0',width=22,height=3,command=lambda : clickBtn(0)).grid(row=4,column=0,columnspan=2,padx=1,pady=1)
point=Button(buttonFrame,text='.',width=10,height=3,command=lambda : clickBtn(0)).grid(row=4,column=2,padx=1,pady=1)
equal=Button(buttonFrame,text='=',width=10,height=3,command=lambda : FunInEqualBtn()).grid(row=4,column=3,padx=1,pady=1)


window.mainloop()