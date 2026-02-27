def check(password):
     if len(password)<8:
        print("Invalid! Password must be minimum 8 characters long")
        
     else:
        for ch in password:
            if ch.isdigit():
                print("Your password is valid")
                break  
        else:
            print("Password must contain atleast one number")

password=input("enter your password")
check(password)