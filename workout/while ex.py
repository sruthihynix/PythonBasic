# Write code to print only upto the letter t.
i=0
s='i love python'
while s[i]!='t':
    print(s[i],end='')
    i+=1
print()
# Write code to print everything in the string except the spaces.
#
for i in s:
    if i==' ':
        continue
    print(i,end='')
print()
# to print 5 times
for i in range(6):
    print(s)