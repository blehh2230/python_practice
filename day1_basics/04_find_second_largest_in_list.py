l=[34,56,39,72,67,88]
largest=l[0]
second=l[0]
for i in l:
    if i>largest:
        second=largest
        largest=i
    elif i!=largest and i>second:
        second=i
print("largest number in the list is",largest)    
if largest==second:
    print("no second largest number exists")
else:
    print("the second largest number in the list is",second)