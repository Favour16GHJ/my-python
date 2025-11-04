# def add( first_num, second_num):
#     print(f'Result of {first_num} + {second_num} is {first_num + second_num}')

# def subtract( first_num, second_num):
#     print(f'Result of {first_num} - {second_num} is {first_num - second_num}')

# def multiply( first_num, second_num):
#     print(f'Result of {first_num} * {second_num} is {first_num * second_num}')

# def divide( first_num, second_num):
#     print(f'Result of {first_num} / {second_num} is {first_num / second_num}')

# while True:
#     first_value = float(input("Enter first value: "))
#     second_value = float(input("Enter second value: "))
#     operation = input("Enter operation(+,-,*,/): ")

#     if operation == "+":
#         add(first_value, second_value)
#     elif operation == "-":
#         subtract(first_value, second_value)
#     elif operation == "*":
#         multiply(first_value, second_value)
#     elif operation == "/":
#         if second_value != 0:
#             divide(first_value, second_value)
#         else:
#             print("Zero Division Error") 
#             continue

   
def calculate(a, b, operation):
    if operation == "+":
        print(a+b, "\n")
    elif operation == "-":
        print(a-b, "\n")
    elif operation == "*":
        print(a*b, "\n")
    elif operation == "/":
        if b != 0 :
            print(a/b, "\n")
        else:
            print("Zero Division Error")

while True: 
    first_num = float(input("Enter first number: "))
    second_num = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")
    calculate(first_num, second_num, op)
