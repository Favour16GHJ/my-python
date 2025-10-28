# 7. **Simple ATM Program**

#    * Ask for a PIN (e.g., 1234).
#    * If it’s correct, show options like `1. Withdraw`, `2. Check Balance`, `3. Exit`.
#    * Use conditionals to handle each option.

print("Simple ATM Machine \n Your current pin is 1234")

pin = 1234
user_pin = int(input("Please enter pin: "))

if user_pin == 1234:
    user = input("What action would you like to perform today? \n 1. Withdraw \n 2. Check Balance \n 3. Change Pin \n 4. Exit \n Please input corresponding number: ")
    if int(user) == 1 or user.lower() == "withdraw":
        print("Yay")
    elif int(user) == 2 or user.lower() == "check balance":
        print("Yay")
    elif int(user) == 3 or user.lower() == "change pin":
        # print("Yay")
        change_pin = input("Please enter current pin: ")
        if int(change_pin) == 1234:
            new_pin = input("Please enter new pin: ")
            confirm = input("Please confirm pin: ")  
            if new_pin == confirm:
                user_pin = int(confirm)
                print(f"Pin has been changed. \n You new pin is {user_pin}")
            else: 
                print("Pin incorrect, please recheck. ")    
        else:
            print("Incorrect pin entered!")          
    elif int(user) == 4 or user.lower() == "exit":
        print("Yay")
    else: 
        user = input("Please enter valid option: ")
    
else:
    print("Incorrect pin entered.")