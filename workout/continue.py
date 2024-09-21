#The continue statement in Python is used to skip the current iteration of a loop
# and move on to the next iteration.
# Unlike the break statement, which terminates the loop,
# continue allows the loop to proceed without executing the remaining code in the current iteration.
# ഒരു ലൂപ്പിൻ്റെ നിലവിലെ ആവർത്തനം ഒഴിവാക്കി അടുത്ത ആവർത്തനത്തിലേക്ക് പോകുന്നതിന്
# പൈത്തണിലെ continue പ്രസ്താവന ഉപയോഗിക്കുന്നു
# Skipping an Iteration in a for Loop:
# You might want to skip processing certain items in a loop based on a condition
# here 2 is not printed
print("example 1 in for")
for number in range(5):
    if number == 2:
        continue
    print(number)
#     Skipping an Iteration in a while Loop:
#     You can use continue to skip the rest of the code in the loop
#     and immediately re-evaluate the loop's condition.
print("example 2 in while")
i = 0
while i < 5:
    i += 2
    if i == 3:
        continue
    print(i)