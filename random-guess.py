# Guess the number game
# The program randomly selects a number between 1–20. 
# The user keeps guessing until they get it right.

user_guess = int(input("Guess the number: "))
secret_number = 5


while user_guess != secret_number:
    # if user_guess != secret_number:
    if user_guess > secret_number:
        print("Too high! Try again.")
    elif user_guess < secret_number:
        print("Too Low! Try again.")
    user_guess = int(input("Guess again: "))
else:
    print("Congratulations! You have guessed the number.")


# Alternatively
number = 25 
while True:
    user_guess = int(input("Enter guess: "))
    if user_guess < number:
        print("Try something higher.")
    elif user_guess > number:
        print("Try something lower.")
    else:
        print("Congratulations! You have guessed the number.")
        retake = input("Woild you like to play again(yes/no): ")
        if retake == 'no':
            break
        else:
            continue
