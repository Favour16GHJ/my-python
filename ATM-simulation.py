# 5.  ATM Withdrawal Simulation
#     Ask the user for withdrawal amounts. Keep asking until they enter a valid amount that is a multiple of 100 and less than the balance.

print("You have $50,000")
user_balance = 50000
user_amount = int(input("Please enter the amount you would like to withdraw: "))

while user_amount > user_balance or user_amount % 100 != 0:
     print("Please enter a number less than balance and a multiple of 100")
     user_amount = int(input("Please enter a valid amount: "))
else:
     print(f"Your current balance is ${user_balance - user_amount} ") 

# Deposit and Check Balance options