# 6. **Number Sign**
#    Ask for a number and print whether it’s **positive, negative, or zero.**

num = float(input("Please enter number: "))
if num > 0 :
    print(f"{num} is a positive number.")
elif num < 0 :
    print(f"{num} is a negative number.")
elif num == 0:
    print(f"{num} is Zero")
else:
    print("Please enter a valid number!")
