import random
j=1
while j<=3: # no of chances
    a=random.randrange(50)
    # or
    #a = random.randint(1,50) # randint(x,y)this module randomly returns a number in the given range
    print("ramdomly selected no is",+a) # to print the randon selection

    x=int(input("Enter a number between 1-50 : "))
    if x==a:
        print("CORRECT...You win the game")
        break
    elif x<a:
        print("YOU FAILED...The number is grater")
    elif x>a:
        print("YOU FAILED... The number is smaller")
    j=j+1
else :
    print("TRY NEXT TIME")
