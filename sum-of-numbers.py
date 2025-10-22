#🧮 Exercise 2 — total of numberbers

# Ask the user for a positive numberber n, and use a while loop to find the total of all numberbers from 1 to n.

# Example:
# If the user enters 5, the program should output 15
# (since 1 + 2 + 3 + 4 + 5 = 15

number = int(input('Please enter a number: '))
total = 0

while number > 0:
    total += number
    number -= 1

print(total)