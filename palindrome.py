# Palindrome checker
# Check if a number entered by the user is a palindrome (same forward and backward).

user = int(input("Enter a value: "))
value  = user
reverse = 0

while value > 0: 
    remainder = value % 10
    reverse = reverse * 10 + remainder
    value = value // 10
print(reverse)
if reverse == user:
    print("This number is a palindrome")
else:
    print("This number is not a palindrome")

# # user_input = "mum"
# user_input = input("Enter your word: ")
# possible_palindrome = ""

# i = len(user_input) - 1
# while i >= 0:
#     possible_palindrome += user_input[i]
#     i -= 1
# print(possible_palindrome)
# if user_input == possible_palindrome:
#     print("This word is a palidrome")
# else:
#     print("This word is not a palidrome")

