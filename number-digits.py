# Digits of a number
# Ask the user for a number and print each digit separately using a while loop.

user_number = input("Enter the number you know: ")
i = 0
while i < len(user_number):
    print(user_number[i])
    i += 1


# Alternatively, using integer operations
# value  = int(input("Enter a value: "))
# reverse = 0

# while value > 0: 
#     remainder = value % 10
#     reverse = reverse * 10 + remainder
#     value = value // 10
# print(reverse)    

