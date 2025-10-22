# 🌟 Bonus Challenge — Limited Attempts Guessing Game
# Let’s upgrade your previous game:
# This time, the user only has 5 attempts to guess the secret number.
# Here’s what it should do:

# The computer still has a secret_number (you can set it to any number).
# The user can only guess 5 times.
# After each wrong guess, tell them if it’s too high or too low and how many attempts they have left.
# If they guess correctly → print "You got it!" 🎉
# If they use all 5 attempts → print "Out of tries! The number was X."
# It’s a fun one — combines while loops + counters + conditions 😏
# Go ahead and give it a try, Favour 🐍💻


user_guess = int(input("Guess the secret number: "))
no_of_user_guess = 1
secret_number = 13

while no_of_user_guess < 5:
    if user_guess != secret_number:
        if user_guess > secret_number:
            print("Too high!")
        elif user_guess < secret_number:
            print("Too low!")
        print(f"You have {5 - no_of_user_guess} tries left")
        user_guess = int(input("Try again: "))
    elif user_guess == secret_number:
        print("Congratulations! You have guessed the number.")
        break
    no_of_user_guess += 1
else:
    print(f"Out of tries! The secret number was {secret_number}")
    
