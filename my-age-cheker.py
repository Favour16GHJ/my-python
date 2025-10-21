# Age Group Checker
# Ask for the user’s age and print:

# “Child” if below 13

# “Teenager” if between 13 and 19

# “Adult” if 20 or above

user_age = int(input("Please enter your age: "))

if user_age < 13 and user_age >= 0:
    print("You are a child.")
elif user_age >= 13 and user_age < 20:
    print("You are a teenager.")
elif user_age >= 20:
    print("You are officially an adult.")
else:
    print("Please enter valid age.")