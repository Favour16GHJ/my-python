# 🔁 Exercise 4 — User Input Until Quit

# Keep asking the user to enter something.
# If they type "quit", the loop stops.
# Otherwise, print back what they typed.

user = input("Type in whatever you want: ")

while user.lower() != "quit":
    print(user)
    print("Remember to type \"quit\" if you want to exit! ")
    user = input("Type something else: ")
