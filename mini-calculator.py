# Write a program  for a simple calculator
# It should be able to perform addition, subtraction, multiplication, and division
# The program should take two numbers and an operator as input from the user
# Also create a statement to handle the undefined divisions

first_num = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ") 
second_num = float(input("Enter second number: "))

if operator == '+':
    print(f"The sum of {first_num} and {second_num} is {first_num + second_num}")
elif operator == '-':
    print(f"The difference between {first_num} and {second_num} is {first_num - second_num}")
elif operator == '*':
    print(f"The product of {first_num} and {second_num} is {first_num * second_num}")
elif operator == '/':
    if second_num != 0:
        print(f"The division of {first_num} by {second_num} is {first_num / second_num}")
    else:
        print("Error: Division by zero is undefined.")
else:
    print("Invalid Operator")