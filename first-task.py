age = int(input("Please enter your age: "))
has_membership = True
has_large_bag = bool(input("You are carrying a large bag (True/False): ").capitalize())


if (age <= 12 or age >= 65) and has_large_bag == False:
    global is_allowed
    is_allowed = "Access Granted!"
    # print("Please proceed into the museum")
else:
    is_allowed = "Access Denied!"
    # print("Sorry, you are not eligible for entry. Please fufill all required conditions.") 

print(is_allowed)