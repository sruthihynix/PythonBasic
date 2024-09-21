# pin=123
import time

balance=500
amt=balance

def deposit():
    b=int(input("Enter amount : "))
    global amt,balance
    amt=balance + b
    balance=amt
    time.sleep(1.5)
    print(f"Your balance after depositing  : {amt} Rupees. ")

def withdraw():
    global amt,balance
    wd=int(input("Please enter amount : "))
    if wd > balance:        # ---------error----here balance amt is not getting updating
        time.sleep(1.5)
        print("\nInsufficient balance...!")
    else:
        global amt
        amt=amt-wd
        balance=amt
        time.sleep(1.5)
        print(f"Your available balance  after withdrawal : {amt} Rupees. ")
        # balance=amt

def Balance():
    # global amt
    print('\n\nYour Current Balance is : ',amt )#-------error----balance is not get updating

print('--------WELCOME--------')
pin=int(input("Please Enter your pin : "))
if pin==123:
     print("\nBalance amount : ",balance)
     print('----------------------------------------------------------')
     while True:
        print("\n1.Balance Enquiry\n2.Deposit\n3.Withdrawal\n4.Cancel Transcation")
        choice=int(input("Enter your Choice : "))
        if choice==1:
            Balance()
        elif choice==2:
            deposit()
        elif choice==3:
            withdraw()
        elif choice==4:
            print('\nTranscation Cancelled')
            print('----THANK YOU-----')
            break
else:
    print('INVALID PIN')