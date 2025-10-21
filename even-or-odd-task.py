# Write a program that asks the user for a number and determines if it is even or odd.

num = int(input("Please enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
