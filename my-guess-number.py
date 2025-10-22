# 💡 Mini Challenge — Guess the Number Game
# Create a simple game where:
# The computer has a secret number (you can set it manually, e.g., 7).
# The user keeps guessing until they get it right.
# Each time, tell the user whether their guess was too high, too low, or correct!

# Example:
# Guess the number: 4
# Too low!
# Guess the number: 9
# Too high!
# Guess the number: 7
# Correct! You got it!

user_guess = int(input("Guess the number: "))
secret_number = 13

while user_guess != secret_number:
    if user_guess > secret_number:
        print("Too high!")
    elif user_guess < secret_number:
        print("Too low!")
    user_guess = int(input("Try again: "))

print("Congratulations!!")