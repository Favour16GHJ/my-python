#    Ask for **three numbers**, then print which one is the largest.

first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))
third_num = float(input("Enter third number: "))

if first_num > second_num and first_num > third_num:
    print(f"{first_num} is the greatest number.")
elif second_num > first_num and second_num > third_num:
    print(f"{second_num} is the greatest number.")
elif third_num > first_num and third_num > second_num:
    print(f"{third_num} is the greatest number.")
elif first_num == second_num and first_num > third_num:
    print(f"{first_num} and {second_num} are the greatest numbers.")
elif first_num == third_num and first_num > second_num:
    print(f"{first_num} and {third_num} are the greatest numbers.")
elif second_num == third_num and second_num > first_num:
    print(f"{second_num} and {third_num} are the greatest numbers.")
else:
    print("All three numbers are equal.")