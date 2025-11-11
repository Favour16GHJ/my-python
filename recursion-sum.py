

user = float(input("Enter a number: "))
def addition(x):
    if x == 0 or x ==1:
        return 1
    else:
        return x + addition(x-1)
print(f"Sum of numbers from 1 to {user} is {addition(user)}")