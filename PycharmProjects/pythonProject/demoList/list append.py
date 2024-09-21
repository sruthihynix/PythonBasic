age=[]
i=1
limit=5
print("entering values to  the list")
while i<=limit:
    #a=input("enter the age you want")  # when we not give type"int()" the  value stored as  string value then, when we print
    # - the list it will disply the value inside quotes like this-['56', '23', '56', '01', '2']-

    a= int(input("enter age"))
    age.append(a)
    i=i+1
#    print(i)
age.append("sruthi") # in list we can add any datatype values
print(age)

print("reading values from list")
j=0
sum=0
while j<len(age):
    sum= sum+j  #sum of ages in the list
    print(age[j])
    j=j+1
print('age sum',sum)
print('avg= ',sum/len(age))# average



