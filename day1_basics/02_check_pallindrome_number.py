num=int(input("enter the number to checked"))
original=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10

if original==rev:
    print("the number is pallindrome")
else:
    print("the number is not a pallindrome")