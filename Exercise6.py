#Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.
correct_password = "12345"
max_attemps = 5
attemps = 0

while attemps <max_attemps:
    password = input("Enter your password") #The user if asked to input the password
    if password == correct_password:
        print("You have been signed in") #If the correct password has been inputed, the user is signed in
        break
    else: 
        attemps += 1
        remaining_attemps = max_attemps - attemps
        if remaining_attemps > 0:
            print(f"The password is incorrect. You have {remaining_attemps} attemps remaining") #If the user has inputed the wrong password, user is asked to try again with attemps remaining shown
        else: 
            print (f"The authorities have been alerted") #If the user has given the wrong password every time, the authorities are alerted.
#The user is asked to input a password, if incorrect is given for 5 times (max tries) the authorities are alerted.