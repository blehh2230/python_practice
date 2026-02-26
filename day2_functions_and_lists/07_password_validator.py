def check(password):
    i=0
    while i==0:
     if len(password)<8:
        print("Invalid! Password must be minimum 8 characters long")
        continue
     else:
        if (0,1,2,3,4,5,6,7,8,9) not in password:
            print("Password must contain atleast one number")
            continue
        else:
            print("Your password is valid")
            i=1


password=input("enter your password")
check(password)