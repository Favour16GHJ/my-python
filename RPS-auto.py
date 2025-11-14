# Create a rock paper scissors game with random module (Computer vs Player)
import random


moves = ['rock', 'paper', 'scissors']

while True:
    while True:
        computer_choice = random.choice(moves)
        # print(computer_choice)
        break
    player_choice = input("Enter your move (rock, paper, scissors): ").lower()
    if player_choice not in moves:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue
    print(f"Computer chose: {computer_choice}")
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")

    confirm = input("Do you want to play again? (yes/no): ")
    if confirm.lower() == "yes":
        continue
    else:
        print("Exiting Game...")
        break    