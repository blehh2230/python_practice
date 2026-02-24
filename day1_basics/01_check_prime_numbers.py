num=int(input("enter the number to be checked"))
if num<=1:
    print(num,"is not a prime number")
for i in range(2,num-1):
    if num%i==0:
        print(num,"is not a prime number")
        break
else:
    print(num,"is a prime number")