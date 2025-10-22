# 6.  Menu-driven program
#     Create a small menu (like calculator: add, subtract, multiply, divide). Keep running until the user chooses to exit.

print("A Simple Calculator.")
print("Choose an operation to perform.")
print("Type the number corresponding to the operation or \"exit\" to exit.")

while True:
    user = input("Would you like to add, substract, multply or divide: \n 1. Addition  \n 2. Subtraction  \n 3. Multiplication  \n 4. Division \n 5. Exit")
    if user == "1":
        firstnum = int(input("Enter first number: ")) 
        secondnum = int(input("Enter second number: "))
        print(f"The sum of {firstnum} and {secondnum} is {firstnum + secondnum}")
    elif user == "2":
        firstnum = int(input("Enter first number: "))
        secondnum = int(input("Enter second number: "))
        print(f"The difference between {firstnum} and {secondnum} is {firstnum - secondnum}")
    elif user == "3":
        firstnum = int(input("Enter first number: "))
        secondnum = int(input("Enter second number: "))
        print(f"The product of {firstnum} and {secondnum} is {firstnum * secondnum}")
    elif user == "4":
        firstnum = int(input("Enter first number: "))
        secondnum = int(input("Enter second number: "))
        if secondnum == 0:
           secondnum =  int(input("Please enter a valid number:"))
           print(f"{firstnum} divided by {secondnum} is {firstnum / secondnum}")
        else: 
            print(f"{firstnum} divided by {secondnum} is {firstnum / secondnum}")
    elif user == "5" or user.lower() == "exit":
        print("Thank you for using the calculator. Goodbye!")
        break
    else:
        retry = input("Do you want to exit(yes/no): ")
        if retry == "yes":
            break
        else:
            continue