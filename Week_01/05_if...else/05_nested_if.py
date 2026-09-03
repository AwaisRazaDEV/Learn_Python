

# Login validation with nested check

username = input("Enter username: ")
password = input("Enter password: ")
is_active = True

if username: 
    if password:  
        if is_active:
            print("Login Successful")
        else:
            print("Account in not active")     
    else:
        print("Password REQUIRED!")    
else:
    print("Username REQUIRED!")