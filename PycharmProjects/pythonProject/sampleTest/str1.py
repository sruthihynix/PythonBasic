a='an apple a day keeps doctor away'
#print('apple' in a) #string check -- if yes, then we get result as true
if "an" in a:   # chk  in string --using if
    print("yes", 'doctor' "present ")
    print(a.upper())
    print(a.lower())
    print(a.title())
    print(a.replace('apple','.......'))
    print(a.split("day"))

x='Sruthi'
y="Vinod"
print(x+" "+y)

print("i am",x)
age=32
txt = "My name is sruthi, and I am {}"
print(txt.format(age)) # format() METHOD IS USED TO INSERT  NUMBERS TO STRING

day=6
month=10
year=1990
dob= 'i am {}, and i was bourn in {} {}{}'
print(dob.format(x,day,month,year))         #format()

dob= 'i am {2}, and i was bourn in {0}-{3}-{1}'
print(dob.format(day, year,x,month))        #format()


p= "hai i want to learn \"python\""# back slash "\" is used to give doublq quotes, inside another double quotes
print(p)

print("an apple a day \n keeps doctor away ") # \n used to print in next line
print("xxxxxxxxxxxxxx")
print("an apple a day \r keeps doctor away ")   # \r
print("xxxxxxxxxxxxxxxxxxxx")
print("an apple a day keeps\t doctor away ")    # \t insert tab
print(x.capitalize())       # capitalise  first letter
#print(x.count())
