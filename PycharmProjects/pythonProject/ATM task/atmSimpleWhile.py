import time

balance=500
pin= int(input('--------WELCOME--------\n Please  Enter the PIN : '))

while True:
    if pin==123:
        time.sleep(2)
        print("Your Account Balance : ",balance)
        print('---------------------------------------')
        print('\n 1.Deposit\n2.Withdrawal \n3. Cancel')
        choice = int(input('Enter your choice : '))

        if choice == 1:
            time.sleep(1.5)
            depo = int(input("Enter the amount to deposit : "))
            balance = balance + depo

        elif choice == 2:
            time.sleep(1.5)
            wd = int(input("Enter the amount :"))

            if wd >balance:
                time.sleep(1.5)
                print("Insufficient amount in your account")

            else:
                balance = balance - wd
            # print('new balance:', balance)

        elif choice==3:
            print('Tranction Cancelled \n--------Thank You--------\n')
            break

    else:
        print('INVALID PIN \n TRY AGAIN')
        break




